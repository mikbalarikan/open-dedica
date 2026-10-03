"""Shared check helpers for od_side_panels_v01 (D3). Job code, not repo code.

Every limit below is spec 1.1 section 5 (D-009); every band is GATES.md section 0 (L-21):
0.005 mm, 0.001 degree, 0.001 mm3, 0 for counts and 1/0 facts. A helper that raises
gives an INCONCLUSIVE row, never a number (D-026).
"""
from __future__ import annotations

import json
import math
import sys
import traceback
from pathlib import Path

import numpy as np
from build123d import Box, GeomType, Location, Plane, Vector

from tools.core import read_step, validity, compare_step, common_volume
from tools.measure import (bore_census, clearance, envelope, feature_census, locate_bore, min_wall,
                           overhang_census, flat_ceiling_spans)
from tools.result import Result, gate, inconclusive

WS = Path(__file__).resolve().parents[1]
CAD = WS / "01_CAD"
OUT = WS / "02_STEP_STL"
INP = WS / "00_Spec" / "inputs"

# GATES.md section 0
BAND_MM, BAND_DEG, BAND_MM3, BAND_N = 0.005, 0.001, 0.001, 0


class Rows:
    """Collects gate rows; a predicate that raises becomes an INCONCLUSIVE row."""

    def __init__(self, part: str):
        self.part, self.rows = part, []

    def add(self, gate_id, result, op, limit, band, *, assumes=(), required=None, note=""):
        try:
            g = gate(gate_id, result, op, limit, band=band, assumes=assumes, required=required)
            row = g.row()
            row["reason"] = g.reason
        except Exception as exc:  # noqa: BLE001
            row = {"gate": gate_id, "measured": None, "unit": getattr(result, "unit", ""),
                   "required": required or f"{op} {limit}", "margin": None, "at": None,
                   "status": "INCONCLUSIVE", "method": getattr(result, "name", "?"),
                   "assumes": list(assumes), "reason": f"{type(exc).__name__}: {exc}"}
        row["part"], row["note"] = self.part, note
        self.rows.append(row)
        return row

    def fail_closed(self, gate_id, unit, exc, required="", note=""):
        self.rows.append({"gate": gate_id, "measured": None, "unit": unit, "required": required,
                          "margin": None, "at": None, "status": "INCONCLUSIVE", "method": "-",
                          "assumes": [], "reason": f"{type(exc).__name__}: {exc}",
                          "part": self.part, "note": note})

    def manual(self, gate_id, status, measured=None, unit="", required="", note="", assumes=()):
        """A row with no tool predicate (reviewer rows, N/A rows, Soft bench rows)."""
        self.rows.append({"gate": gate_id, "measured": measured, "unit": unit, "required": required,
                          "margin": None, "at": None, "status": status, "method": "reviewer/none",
                          "assumes": list(assumes), "reason": "", "part": self.part, "note": note})

    def worst(self):
        order = {"FAIL": 0, "INCONCLUSIVE": 1, "PASS_ASSUMED": 2, "PASS": 3, "N/A": 4}
        return sorted(self.rows, key=lambda r: order.get(r["status"], 5))[0]["status"] if self.rows else None

    def dump(self, path: Path, extra=None):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"part": self.part, "rows": self.rows, "extra": extra or {}},
                                   indent=1, default=str))

    def table(self):
        for r in self.rows:
            m = r["measured"]
            m = f"{m:.4f}" if isinstance(m, float) else m
            mg = r["margin"]
            mg = f"{mg:+.4f}" if isinstance(mg, float) else mg
            print(f"{r['part']:16s} {r['gate']:28s} {r['status']:13s} {m!s:>12} {r['unit']:5s} "
                  f"{r['required']:24s} margin {mg!s:>9}  {r['note']}")


def val(name, value, unit, at=None, **detail) -> Result:
    """A derived number as a Result (composite readings: offsets, distances, angles)."""
    if value is None or (isinstance(value, float) and not math.isfinite(value)):
        return inconclusive(name, unit, "no value")
    return Result(name, float(value), unit, at=at, detail=detail)


def load_part(path) -> object:
    shape = read_step(path)
    return shape


def one_solid(shape):
    s = shape.solids()
    if len(s) != 1:
        raise ValueError(f"{len(s)} solids")
    return s[0]


def box(x0, x1, y0, y1, z0, z1):
    x0, x1 = sorted((x0, x1))
    return Box(x1 - x0, y1 - y0, z1 - z0).moved(Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)))


def planar_faces(shape, normal, tol_deg=0.05):
    n = Vector(*normal).normalized()
    out = []
    for f in shape.faces():
        if f.geom_type != GeomType.PLANE:
            continue
        fn = f.normal_at()
        if fn.get_angle(n) < tol_deg:
            out.append(f)
    return out


def face_box(f):
    bb = f.bounding_box()
    return (bb.min.X, bb.max.X, bb.min.Y, bb.max.Y, bb.min.Z, bb.max.Z)


def common_part(shape, cutter):
    """shape & cutter as one solid set (for region envelopes); raises when empty."""
    r = shape.intersect(cutter)
    if r is None:
        raise ValueError("empty region")
    sol = [s for item in (r if isinstance(r, list) else [r]) for s in item.solids()]
    if not sol:
        raise ValueError("empty region")
    if len(sol) == 1:
        return sol[0]
    from build123d import Compound
    return Compound(sol)


# ---------------------------------------------------------------- generic part predicates

def gate_validity(rows: Rows, shape):
    v = validity(shape)
    rows.add("exactly_one_solid", v["solid_count"], "==", 1, BAND_N)
    rows.add("U-01 solid_count", v["solid_count"], "==", 1, BAND_N)
    rows.add("U-01 brep_valid", v["brep_valid"], "==", 1, BAND_N)
    rows.add("U-01 naked_edges", v["naked_edges"], "==", 0, BAND_N)
    return v


def gate_envelope(rows: Rows, shape, size, pos, gate_ids=("U-02", "envelope_within_spec")):
    """size (sx, sy, sz) in [spec - 0.1, spec + 0.1]; position against the datum reported apart."""
    e = envelope(shape)
    for gid in gate_ids:
        for ax, s in zip("xyz", size):
            rows.add(f"{gid} size_{ax}", e[f"size_{ax}"], "in", (s - 0.1, s + 0.1), BAND_MM)
    for ax, (lo, hi) in zip("xyz", pos):
        rows.add(f"U-02 position min_{ax}", e[f"min_{ax}"], "in", (lo - 0.1, lo + 0.1), BAND_MM,
                 note="position, reported apart from size (L-12)")
        rows.add(f"U-02 position max_{ax}", e[f"max_{ax}"], "in", (hi - 0.1, hi + 0.1), BAND_MM,
                 note="position, reported apart from size (L-12)")
    return e


def gate_roundtrip(rows: Rows, built, step_path):
    """U-04: the part rebuilt in memory from its build script (same parameters) against the
    exported file (named body re-read unchanged, no stray shells, valid after re-import)."""
    c = compare_step(built, step_path)
    rows.add("U-04 schema", c["schema"], "==", 1, BAND_N)
    rows.add("U-04 solids", c["solids"], "==", 1, BAND_N)
    rows.add("U-04 volume_delta", c["volume_delta"], "<=", 0.0, BAND_MM3)
    rows.add("U-04 faces_delta", c["faces_delta"], "==", 0, BAND_N)
    rows.add("U-04 labels", c["labels"], "==", 1, BAND_N, note=str(c["labels"].detail.get("reimported")))
    rows.add("U-04 valid_after", c["valid_after"], "==", 1, BAND_N)
    return c


def gate_census(rows: Rows, shape, plan: dict):
    """U-05 / feature_census: every count exact against the plan."""
    c = feature_census(shape)
    for key, want in plan.items():
        for gid in ("U-05", "feature_census"):
            rows.add(f"{gid} {key}", c[key], "==", want, BAND_N)
    return c


def gate_walls(rows: Rows, shape, spacing, struct_limit=2.0):
    w = min_wall(shape, spacing=spacing)
    rows.add("D-01a", w, ">=", 0.8, BAND_MM)
    rows.add("D-01b", w, ">=", struct_limit, BAND_MM)
    rows.add("D-06a", w, ">=", 1.0, BAND_MM)
    wide = (w.detail or {}).get("wide") if w.ok else None
    if isinstance(wide, dict) and wide.get("measured") is not None:
        wr = Result("min_wall_wide", wide["measured"], "mm", at=wide.get("at"))
    else:
        wr = inconclusive("min_wall_wide", "mm", "detail['wide'] missing" if w.ok else w.reason)
    rows.add("U-06 (Soft)", wr, ">=", 2.0, BAND_MM)
    return w


def stl_rows(rows: Rows, written):
    """U-07 from the Written of write_stl."""
    s = written.checks["max_sagitta"]
    rows.add("U-07 stl_max_sagitta", s, "<=", 0.01, BAND_MM,
             note=f"tol {written.detail['tolerance_mm']} mm, angular {written.detail['angular_tolerance_rad']:.6f} rad, "
                  f"{written.detail['triangles']} triangles")


def run_guarded(rows: Rows, gate_id, unit, fn, *args, **kw):
    try:
        return fn(*args, **kw)
    except Exception as exc:  # noqa: BLE001
        rows.fail_closed(gate_id, unit, exc, note=traceback.format_exc(limit=2).splitlines()[-1])
        return None


def bores_along(census, direction):
    d = np.array(direction, float)
    return [b for b in census.detail["bores"] if np.linalg.norm(np.cross(np.array(b["axis_dir"]), d)) < 1e-6]


def axis_offset(b1, b2):
    """Largest distance of b2's two axis end points from b1's (infinite) axis line, in mm."""
    a = np.array(b1["axis_dir"], float)
    p0 = np.array(b1["start"], float)
    worst = 0.0
    for q in (np.array(b2["start"], float), np.array(b2["end"], float)):
        v = q - p0
        worst = max(worst, float(np.linalg.norm(v - np.dot(v, a) * a)))
    return worst


def nearest_bore(census, point, direction):
    pt = np.array(point, float)
    best = None
    for b in bores_along(census, direction):
        a = np.array(b["axis_dir"], float)
        s, e = np.array(b["start"], float), np.array(b["end"], float)
        t = float(np.clip(np.dot(pt - s, a), 0.0, np.linalg.norm(e - s)))
        off = float(np.linalg.norm(pt - (s + t * a)))
        if best is None or off < best[0]:
            best = (off, b)
    if best is None:
        raise ValueError(f"no bore along {direction}")
    return best[1]
