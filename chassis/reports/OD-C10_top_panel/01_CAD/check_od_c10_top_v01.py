"""Checks for od_c10_top v01 (job 20261001-od-c10-top-panel, concept C1, spec 1.1).

Written before the build (PLAYBOOK D3), from 01_CAD/DESIGN_PLAN.md section 6. Every
predicate measures the re-imported STEP files with tools.core / tools.measure and
compares through tools.result.gate with the GATES.md section 0 band of the result's
unit. Thresholds come from DESIGN_SPEC.md 1.1 section 5 only (the SPEC table cites the
row of each value). Any exception or missing value gives INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c10_top.py \
        --step 02_STEP_STL/od_c10_top_C1_v01.step \
        --asm 02_STEP_STL/od_c10_assembly_C1_v01.step \
        --stl 02_STEP_STL/od_c10_top_C1_v01.stl \
        --record 01_CAD/build_record_v01.json \
        --out 01_CAD/check_od_c10_top_v01.json [--variant '{...}'] [--quick]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
import math
import struct
import sys
import time
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402
from build123d import Align, Box, Cylinder, Location, Plane, Pos  # noqa: E402

from tools.core import common_volume, compare_step, read_step, validity, write_stl  # noqa: E402
from tools.core.step import file_sha256  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census, flat_ceiling_spans,  # noqa: E402
                           locate_bore, mass_properties, mesh_census, min_wall, min_wall_wide,
                           overhang_census, radial_extent)
from tools.result import INCONCLUSIVE, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.1) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "rad": 0.00002}   # every other unit: 0
SPEC = {
    # U-02: 240.0 x 39.5 x 405.0 each +-0.1; position x +-120.0, y 210.5 .. 250.0, z -305.0 .. +100.0
    "size": {"size_x": 240.0, "size_y": 39.5, "size_z": 405.0}, "size_tol": 0.1,
    "position": {"min_x": -120.0, "max_x": 120.0, "min_y": 210.5, "max_y": 250.0, "min_z": -305.0, "max_z": 100.0},
    # D-02 (A-09): Kobra Max 3 420 x 420 x 500; upside down: x and z on the bed, y tall
    "bed": {"size_x": 420.0, "size_z": 420.0, "size_y": 500.0},
    # D-01a, D-01b, D-06a, U-06 (Soft)
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wall_wide": 2.0,
    # D-03a >= 45 deg, build -Y (A-08); D-03b span <= 5
    "overhang_deg": 45.0, "build_dir": (0.0, -1.0, 0.0), "bridge_span": 5.0,
    # U-07: tol 0.01, angular <= 4 acos(1 - 0.01/R_max), R_max = 10.0 (outer corners)
    "stl_tol": 0.01, "stl_ang_max": 4.0 * math.acos(1.0 - 0.01 / 10.0),
    # U-03 (a)
    "contact": 0.0, "interference": 0.0, "pad_gap": 0.50, "pad_gap_tol": 0.05, "c07_gap": 3.0, "c01_gap": 3.0,
    "away_gap": 0.5, "coax_max": 0.10,
    # U-03 (b): from +40.0 above the seat, steps <= 2.0
    "lower_from": 40.0, "lower_step": 2.0,
    # REQ-01
    "top_y": 250.0, "top_tol": 0.10, "top_faces": 1, "skin_t": 3.0, "skin_tol": 0.1,
    "skin_points": ((0.0, -150.0), (-100.0, -100.0), (100.0, 0.0), (0.0, 0.0), (-80.0, 80.0)),
    # REQ-02
    "x_half": 120.0, "z_min": -305.0, "z_max": 100.0, "outline_tol": 0.1, "corner_r": 10.0, "corner_tol": 0.1,
    "corners": ((110.0, -295.0, 45.0), (110.0, 90.0, 315.0), (-110.0, -295.0, 135.0), (-110.0, 90.0, 225.0)),
    "skirt_t": 3.0, "skirt_tol": 0.1, "skirt_bottom_y": 215.0, "skirt_bottom_tol": 0.10,
    # REQ-03, REQ-04
    "bulkhead_cols": ((65.0, -60.0), (65.0, -210.0)), "rear_cols": ((90.0, -293.0), (-90.0, -293.0)),
    "col_d": 12.0, "col_tol": 0.1, "offset_max": 0.10, "col_bottom_y": 215.0, "col_bottom_tol": 0.05,
    "hole_d": 3.4, "hole_tol": 0.1, "hole_min_d": 3.25, "cbore_d": 6.5, "cbore_tol": 0.1,
    "cbore_floor_y": 218.0, "cbore_floor_tol": 0.1,
    # REQ-05
    "pads": ((48.0, 30.0), (-48.0, 30.0)), "pad_d": 10.0, "pad_tol": 0.1, "pad_bottom_y": 210.5, "pad_bottom_tol": 0.05,
    "hub_r_min": 40.0, "cbore_edge_min": 20.0,
    # REQ-06: no material below y 247 in x +-42, z -70 .. +70
    "headroom_box": (-42.0, 42.0, 200.0, 247.0, -70.0, 70.0),
    # REQ-07: a driver of diameter <= 6 down to the head
    "driver_r": 3.0,
    # U-05 census (plan section 3)
    "census": {"plane_faces": 59, "cylinder_faces": 22, "concave_cylinders": 12, "convex_cylinders": 10,
               "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0, "bspline_faces": 0, "other_faces": 0,
               "bores": 8},
    "bores_d34_y_through": 4, "bores_d65_y_blind": 4, "column_cylinders": 4, "pad_cylinders": 2,
    "bulk_rib_sides": 8, "bulk_rib_hyp": 4, "rear_rib_sides": 16, "rear_rib_bottoms": 4, "rear_rib_hyp": 4,
    "skin_under_faces": 3, "skirt_bottom_faces": 1,
    "density": 1270.0,
}
ASSUMES = {"U-03": ("A-01", "A-02", "A-03"), "REQ-01": ("A-06",), "REQ-02": ("A-04",),
           "REQ-03": ("A-01", "A-05"), "REQ-04": ("A-02", "A-05"), "REQ-05": ("A-03",), "REQ-06": ("A-06",),
           "D-02": ("A-09",), "D-03a": ("A-08",), "D-03b": ("A-08",), "REQ-08": ("A-04", "A-11")}
SPACING = 0.7   # brief WP-02 and plan section 2: the default spacing refuses the large faces
PART = "od_c10_top"
LABELS = {"plate": "od_c01_frame", "c02": "od_c02_bulkhead", "c05": "od_c05_carrier",
          "c07": "od_c07_valve_mount", "c11": "od_c11_back"}
CROP = (-125.0, 125.0, 200.0, 300.0, -310.0, 105.0)   # holds the lid's swept box (y 210.5 .. 290)


def _safe(fn, name, unit, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001: a check never raises
        return inconclusive(name, unit, f"{type(exc).__name__}: {exc}")


class Gates:
    def __init__(self):
        self.rows: list[dict] = []

    def add(self, gate_id, result, op, limit, *, assumes=(), required=None, note=""):
        try:
            g = gate(gate_id, result, op, limit, band=BAND.get(result.unit, 0), assumes=assumes,
                     required=required)
            row = g.row()
            row["reason"] = g.reason
        except Exception as exc:  # noqa: BLE001
            row = {"gate": gate_id, "measured": None, "unit": getattr(result, "unit", ""),
                   "required": required or f"{op} {limit}", "margin": None, "at": None,
                   "status": INCONCLUSIVE, "method": getattr(result, "name", ""),
                   "assumes": list(assumes), "reason": f"{type(exc).__name__}: {exc}"}
        if note:
            row["note"] = note
        params = getattr(result, "params", None)
        if params:
            row["params"] = {k: v for k, v in params.items() if isinstance(v, (int, float, str, tuple, list))}
        detail = getattr(result, "detail", None)
        if detail:
            row["detail"] = {k: v for k, v in detail.items()
                             if k not in ("bores", "points", "pairs", "samples", "ceilings", "material")}
        self.rows.append(row)
        return row

    def fixed(self, gate_id, status, required, note, measured=None, unit="", assumes=()):
        self.rows.append({"gate": gate_id, "measured": measured, "unit": unit, "required": required,
                          "margin": None, "at": None, "status": status, "method": "by the row",
                          "assumes": list(assumes), "reason": "", "note": note})


def _children(shape):
    out = {}
    for child in getattr(shape, "children", ()) or ():
        if getattr(child, "children", ()):
            out.update(_children(child))
        else:
            out[child.label] = child
    return out


def _one(shape):
    s = shape.solids()
    return s[0] if len(s) == 1 else shape


def _box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, y0, z0) * Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN))


def _ycyl(x, z, r, y0, y1):
    up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return Pos(x, y0, z) * (up * Cylinder(r, y1 - y0, align=(Align.CENTER, Align.CENTER, Align.MIN)))


def _stl_facts(path: Path) -> dict:
    data = path.read_bytes()
    n = struct.unpack_from("<I", data, 80)[0]
    arr = np.frombuffer(data, dtype=np.dtype([("n", "<3f4"), ("v", "<9f4"), ("a", "<u2")]), count=n, offset=84)
    v = arr["v"].reshape(-1, 3).astype(float)
    return {"triangles_header": n, "bytes": len(data), "bbox_min": v.min(0).round(4).tolist(),
            "bbox_max": v.max(0).round(4).tolist(), "bbox_size": (v.max(0) - v.min(0)).round(4).tolist()}


def _res(r):
    return {"measured": r.measured, "unit": r.unit, "status": r.status, "at": r.at, "reason": r.reason}


def _ray(shape, origin, axis, ref, angle, z, side, **kw):
    return _safe(radial_extent, "radial_extent", "mm", shape, origin, axis, ref, angle, z, side=side, **kw)


def _planar(shape, normal, tol=1e-6):
    n = np.array(normal, float)
    out = []
    for f in shape.faces():
        if f.geom_type.name != "PLANE":
            continue
        if float(np.dot(np.array(tuple(f.normal_at())), n)) < 1.0 - tol:
            continue
        bb = f.bounding_box()
        out.append({"face": f, "at": float(np.dot(np.array(tuple(f.center())), n)), "area": f.area,
                    "min": [bb.min.X, bb.min.Y, bb.min.Z], "max": [bb.max.X, bb.max.Y, bb.max.Z]})
    return out


def _strip(rows):
    return [{k: v for k, v in r.items() if k != "face"} for r in rows]


def _bores(census):
    return census.detail.get("bores", []) if isinstance(census, Result) and census.detail else []


def _along(b, axis):
    return abs(abs(float(np.dot(np.array(b["axis_dir"], float), np.array(axis, float)))) - 1.0) < 1e-6


def _find_bore(bores, axis, point, d, dtol=0.3):
    """The census bore along `axis`, of about diameter d, whose axis segment passes nearest `point`."""
    best = None
    p = np.array(point, float)
    a = np.array(axis, float)
    for b in bores:
        if not _along(b, axis) or abs(b["diameter"] - d) > dtol:
            continue
        s, e = np.array(b["start"], float), np.array(b["end"], float)
        t = float(np.clip(np.dot(p - s, a) / max(np.dot(e - s, a), 1e-12), 0.0, 1.0)) if np.dot(e - s, a) else 0.0
        q = s + t * (e - s)
        off = float(np.linalg.norm(p - q))
        if best is None or off < best[0]:
            best = (off, b)
    return None if best is None else best[1]


def _unpack(loc):
    if isinstance(loc, Result):
        return {"diameter": loc, "offset": loc, "length": loc, "through": loc}
    return loc


def _ycyl_faces(shape, r, x, z, rtol=0.05, ptol=1.0):
    """Cylindrical faces of radius r (within rtol) with an axis along Y passing within ptol of (x, z)."""
    out = []
    for f in shape.faces():
        if f.geom_type.name != "CYLINDER":
            continue
        try:
            ax = f.axis_of_rotation
            rr = f.radius
        except Exception:  # noqa: BLE001
            continue
        if abs(abs(ax.direction.Y) - 1.0) > 1e-6 or abs(rr - r) > rtol:
            continue
        cx, cz = ax.position.X, ax.position.Z
        if math.hypot(cx - x, cz - z) <= ptol:
            out.append({"face": f, "r": rr, "cx": cx, "cz": cz, "bb": f.bounding_box()})
    return out


def _area(shape):
    if shape is None:
        return 0.0
    return float(sum(f.area for f in shape.faces()))


def _cut(shape, tools_):
    out = shape
    for t in tools_:
        out = out - t
    sols = out.solids()
    return sols[0] if len(sols) == 1 else out


def _crop(shape, bounds):
    c = shape & _box(*bounds)
    return c


def _refilled(one, cbores):
    """The solid with each named-exception counterbore refilled by position: a cylinder of
    the measured diameter + 0.2 on the measured axis from 0.1 below the floor to the top
    face. The D-03a census outside the exception reads this (plan section 6)."""
    solid = one
    for b in cbores:
        ys = sorted((b["start"][1], b["end"][1]))
        solid = solid + _ycyl(b["start"][0], b["start"][2], 0.5 * b["diameter"] + 0.1, ys[0] - 0.1, ys[1])
    solid = solid.clean()
    sols = solid.solids()
    return sols[0] if len(sols) == 1 else solid


def _down_faces(shape, build_dir):
    """Faces with any point facing down in the print (normal . build_dir < 0 means
    facing the bed): kind, least angle from horizontal on a 9 x 9 parameter grid, box."""
    bd = np.array(build_dir, float)
    rows = []
    for f in shape.faces():
        least = None
        for u in np.linspace(0.0, 1.0, 9):
            for v in np.linspace(0.0, 1.0, 9):
                try:
                    n = f.normal_at(u, v)
                except Exception:  # noqa: BLE001
                    continue
                tb = -float(np.dot(np.array(tuple(n)), bd))
                if tb <= 1e-6:
                    continue
                a = math.degrees(math.acos(min(1.0, tb)))
                least = a if least is None else min(least, a)
        if least is None:
            continue
        bb = f.bounding_box()
        rows.append({"kind": f.geom_type.name.lower(), "least_deg": round(least, 4), "area": round(f.area, 4),
                     "min": [round(bb.min.X, 3), round(bb.min.Y, 3), round(bb.min.Z, 3)],
                     "max": [round(bb.max.X, 3), round(bb.max.Y, 3), round(bb.max.Z, 3)]})
    return rows


def check(step_path: Path, asm_path: Path | None, stl_path: Path | None, record_path: Path | None,
          variant: dict, scratch: Path, quick: bool = False) -> dict:
    G = Gates()
    facts: dict = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    part = read_step(step_path)
    one = _one(part)
    facts["step_sha256"] = file_sha256(step_path)

    # U-01, exactly_one_solid
    val = _safe(validity, "validity", "", part)
    if isinstance(val, Result):
        val = {"solid_count": val, "brep_valid": val, "naked_edges": val}
    G.add("U-01.solid_count", val["solid_count"], "==", 1)
    G.add("U-01.brep_valid", val["brep_valid"], "==", 1)
    G.add("U-01.naked_edges", val["naked_edges"], "==", 0)
    G.add("exactly_one_solid", val["solid_count"], "==", 1)

    # U-02, envelope_within_spec, D-02, REQ-01 (max y), REQ-02 (outline)
    env = envelope(one)
    tol = SPEC["size_tol"]
    for k, v in SPEC["size"].items():
        G.add(f"U-02.{k}", env[k], "in", (v - tol, v + tol))
        G.add(f"envelope_within_spec.{k}", env[k], "in", (v - tol, v + tol))
    for k, v in SPEC["position"].items():
        G.add(f"envelope_within_spec.position.{k}", env[k], "in", (v - tol, v + tol),
              note="position against the datum, reported apart from the size (L-12)")
    for k, v in SPEC["bed"].items():
        G.add(f"D-02.{k}", env[k], "<=", v, assumes=ASSUMES["D-02"],
              note="upside down: size_x and size_z on the bed, size_y tall")
    facts["envelope"] = {k: v.measured for k, v in env.items()}
    max_y = env["max_y"].measured
    G.add("REQ-01.max_y", env["max_y"], "in", (SPEC["top_y"] - SPEC["top_tol"], SPEC["top_y"] + SPEC["top_tol"]),
          assumes=ASSUMES["REQ-01"])
    ot = SPEC["outline_tol"]
    for k, v in (("min_x", -SPEC["x_half"]), ("max_x", SPEC["x_half"]), ("min_z", SPEC["z_min"]),
                 ("max_z", SPEC["z_max"])):
        G.add(f"REQ-02.{k}", env[k], "in", (v - ot, v + ot), assumes=ASSUMES["REQ-02"])

    # REQ-01 top face: one planar face at max y
    top = [f for f in _planar(one, (0, 1, 0)) if abs(f["at"] - max_y) < 1e-4]
    facts["top_faces"] = _strip(top)
    G.add("REQ-01.top_faces", Result("planar_faces_at_max_y", len(top), "count"), "==", SPEC["top_faces"],
          assumes=ASSUMES["REQ-01"])
    if top:
        G.add("REQ-01.top_face_y", Result("top_face_y", top[0]["at"], "mm", at=top[0]["min"]), "in",
              (SPEC["top_y"] - SPEC["top_tol"], SPEC["top_y"] + SPEC["top_tol"]), assumes=ASSUMES["REQ-01"])
    else:
        G.add("REQ-01.top_face_y", inconclusive("top_face_y", "mm", "no planar face at max y"), "in",
              (SPEC["top_y"] - SPEC["top_tol"], SPEC["top_y"] + SPEC["top_tol"]))
    # skin thickness: rays up (+Y) and down (-Y) from y 248.5 (axis along X, ref +Y)
    st = SPEC["skin_tol"]
    for x, z in SPEC["skin_points"]:
        org = (0.0, 248.5, z)
        up = _ray(one, org, (1, 0, 0), (0, 1, 0), 0.0, x, "outer", r_max=10.0)
        dn = _ray(one, org, (1, 0, 0), (0, 1, 0), 180.0, x, "outer", r_max=10.0)
        if up.measured is not None and dn.measured is not None:
            t = Result("skin_thickness", up.measured + dn.measured, "mm", at=[x, 248.5, z],
                       detail={"top_y": 248.5 + up.measured, "underside_y": 248.5 - dn.measured})
        else:
            t = inconclusive("skin_thickness", "mm", f"{up.reason} {dn.reason}".strip() or "no ray")
        G.add(f"REQ-01.skin_t.x{x:g}_z{z:g}", t, "in", (SPEC["skin_t"] - st, SPEC["skin_t"] + st),
              assumes=ASSUMES["REQ-01"])

    # REQ-02 corners: outer radius from each corner centre at 15, 45, 75 deg off the bisector side
    ct = SPEC["corner_tol"]
    for cx, cz, bis in SPEC["corners"]:
        for da in (-30.0, 0.0, 30.0):
            a = bis + da
            r = _ray(one, (cx, 0.0, cz), (0, 1, 0), (1, 0, 0), a, 230.0, "outer", r_min=0.0, r_max=15.0)
            G.add(f"REQ-02.corner_r.x{cx:g}_z{cz:g}.a{a:g}", r, "in", (SPEC["corner_r"] - ct, SPEC["corner_r"] + ct),
                  assumes=ASSUMES["REQ-02"])
        ri = _ray(one, (cx, 0.0, cz), (0, 1, 0), (1, 0, 0), bis, 230.0, "inner", r_min=0.0, r_max=15.0)
        ro = _ray(one, (cx, 0.0, cz), (0, 1, 0), (1, 0, 0), bis, 230.0, "outer", r_min=0.0, r_max=15.0)
        t = (Result("skirt_thickness", ro.measured - ri.measured, "mm", at=ro.at)
             if ro.measured is not None and ri.measured is not None
             else inconclusive("skirt_thickness", "mm", f"{ri.reason} {ro.reason}".strip() or "no ray"))
        G.add(f"REQ-02.skirt_t.corner_x{cx:g}_z{cz:g}", t, "in", (SPEC["skirt_t"] - st, SPEC["skirt_t"] + st),
              assumes=ASSUMES["REQ-02"])
    # REQ-02 skirt on each side: rays at y 230 from inside, the window past r 100 / 250 / 50
    sides = [("+x", (0.0, 0.0, z), (0, 1, 0), (1, 0, 0), 0.0, 100.0, 130.0) for z in (-150.0, 0.0, 60.0)]
    sides += [("-x", (0.0, 0.0, z), (0, 1, 0), (1, 0, 0), 180.0, 100.0, 130.0) for z in (-150.0, 0.0, 60.0)]
    sides += [("-z", (x, 0.0, 0.0), (0, 1, 0), (1, 0, 0), 90.0, 290.0, 320.0) for x in (-40.0, 0.0, 40.0)]
    sides += [("+z", (x, 0.0, 0.0), (0, 1, 0), (1, 0, 0), 270.0, 90.0, 110.0) for x in (-40.0, 0.0, 40.0)]
    for tag, org, ax, ref, a, r0, r1 in sides:
        ri = _ray(one, org, ax, ref, a, 230.0, "inner", r_min=r0, r_max=r1)
        ro = _ray(one, org, ax, ref, a, 230.0, "outer", r_min=r0, r_max=r1)
        t = (Result("skirt_thickness", ro.measured - ri.measured, "mm", at=ro.at,
                    detail={"inner": ri.measured, "outer": ro.measured})
             if ro.measured is not None and ri.measured is not None
             else inconclusive("skirt_thickness", "mm", f"{ri.reason} {ro.reason}".strip() or "no ray"))
        G.add(f"REQ-02.skirt_t.{tag}.at{org[0]:g}_{org[2]:g}", t, "in", (SPEC["skirt_t"] - st, SPEC["skirt_t"] + st),
              assumes=ASSUMES["REQ-02"])
    # skirt bottom face at y 215 spanning the outline
    downs = _planar(one, (0, -1, 0))
    skirt_bottom = [f for f in downs if f["max"][0] - f["min"][0] > 200.0 and f["max"][2] - f["min"][2] > 350.0
                    and abs(-f["at"] - SPEC["skirt_bottom_y"]) < 2.0]
    facts["skirt_bottom_faces"] = _strip(skirt_bottom)
    G.add("U-05.skirt_bottom_faces", Result("skirt_bottom_faces", len(skirt_bottom), "count"), "==",
          SPEC["skirt_bottom_faces"])
    if skirt_bottom:
        G.add("REQ-02.skirt_bottom_y", Result("skirt_bottom_y", -skirt_bottom[0]["at"], "mm", at=skirt_bottom[0]["min"]),
              "in", (SPEC["skirt_bottom_y"] - SPEC["skirt_bottom_tol"], SPEC["skirt_bottom_y"] + SPEC["skirt_bottom_tol"]),
              assumes=ASSUMES["REQ-02"])
    else:
        G.add("REQ-02.skirt_bottom_y", inconclusive("skirt_bottom_y", "mm", "no skirt bottom face"), "in",
              (SPEC["skirt_bottom_y"] - SPEC["skirt_bottom_tol"], SPEC["skirt_bottom_y"] + SPEC["skirt_bottom_tol"]))

    # U-05 feature census
    fc = _safe(feature_census, "feature_census", "count", one)
    census = _safe(bore_census, "bore_census", "count", one)
    if isinstance(fc, dict):
        facts["feature_census"] = {k: v.measured for k, v in fc.items()}
        for k, n in SPEC["census"].items():
            G.add(f"U-05.{k}", fc[k], "==", n)
            G.add(f"feature_census.{k}", fc[k], "==", n)
    else:
        G.add("U-05.census", fc, "==", 0)
        G.add("feature_census", fc, "==", 0)
    bores = _bores(census)
    facts["bores"] = bores
    y34 = [b for b in bores if _along(b, (0, 1, 0)) and abs(b["diameter"] - 3.4) < 0.3 and b.get("through")]
    y65 = [b for b in bores if _along(b, (0, 1, 0)) and abs(b["diameter"] - 6.5) < 0.3 and not b.get("through")]
    for tag, lst, n in (("bores_d34_y_through", y34, SPEC["bores_d34_y_through"]),
                        ("bores_d65_y_blind", y65, SPEC["bores_d65_y_blind"])):
        G.add(f"U-05.{tag}", Result(tag, len(lst), "count"), "==", n)
    cols = list(SPEC["bulkhead_cols"]) + list(SPEC["rear_cols"])
    # the measured column axes (cylinder faces of radius ~6 near each nominal axis): every
    # by-position selection and exclusion volume below follows the column as built (fix cycle 1)
    col_axis = {}
    for x, z in cols:
        cf = _ycyl_faces(one, 0.5 * SPEC["col_d"], x, z, rtol=0.5)
        col_axis[(x, z)] = (cf[0]["cx"], cf[0]["cz"]) if cf else (x, z)
    facts["column_axes_measured"] = {f"{x:g},{z:g}": col_axis[(x, z)] for x, z in cols}
    ncol = sum(1 for x, z in cols if _ycyl_faces(one, 0.5 * SPEC["col_d"], x, z, rtol=0.5))
    npad = sum(1 for x, z in SPEC["pads"] if _ycyl_faces(one, 0.5 * SPEC["pad_d"], x, z, rtol=0.5))
    planes = [f for f in one.faces() if f.geom_type.name == "PLANE"]

    def nrm(f):
        n = f.normal_at()
        return n.X, n.Y, n.Z
    bulk_sides = [f for f in planes if abs(abs(nrm(f)[2]) - 1) < 1e-6 and f.bounding_box().min.Y > 220.0
                  and any(abs(f.center().Z - (col_axis[(xc, zc)][1] + s * 1.5)) < 0.01
                          for xc, zc in SPEC["bulkhead_cols"] for s in (1, -1))]
    bulk_hyp = [f for f in planes if abs(nrm(f)[0]) > 0.1 and nrm(f)[1] < -0.1 and abs(nrm(f)[2]) < 1e-6]
    rear_sides = [f for f in planes if abs(abs(nrm(f)[0]) - 1) < 1e-6 and f.bounding_box().min.Z > -303.5
                  and f.bounding_box().max.Z < -270.0 and f.bounding_box().min.Y > 215.5
                  and any(abs(f.center().X - (col_axis[(xc, zc)][0] + d)) < 0.01
                          for xc, zc in SPEC["rear_cols"] for d in (2.5, -2.5, 5.5, -5.5))]
    rear_bot = [f for f in _planar(one, (0, -1, 0)) if abs(-f["at"] - 216.0) < 0.5]
    rear_hyp = [f for f in planes if abs(nrm(f)[2]) > 0.1 and nrm(f)[1] < -0.1 and abs(nrm(f)[0]) < 1e-6]
    skin_under = [f for f in downs if abs(-f["at"] - (SPEC["top_y"] - SPEC["skin_t"])) < 0.5]
    for tag, n, want, what in (("column_cylinders", ncol, SPEC["column_cylinders"], "4 screw columns"),
                               ("pad_cylinders", npad, SPEC["pad_cylinders"], "2 rest pads"),
                               ("bulk_rib_sides", len(bulk_sides), SPEC["bulk_rib_sides"], "bulkhead-column ribs"),
                               ("bulk_rib_hyp", len(bulk_hyp), SPEC["bulk_rib_hyp"], "bulkhead-column ribs"),
                               ("rear_rib_sides", len(rear_sides), SPEC["rear_rib_sides"], "rear-column ribs"),
                               ("rear_rib_bottoms", len(rear_bot), SPEC["rear_rib_bottoms"], "rear-column ribs"),
                               ("rear_rib_hyp", len(rear_hyp), SPEC["rear_rib_hyp"], "rear-column ribs"),
                               ("skin_under_faces", len(skin_under), SPEC["skin_under_faces"], "1 skin")):
        G.add(f"U-05.{tag}", Result(tag, n, "count"), "==", want, note=what)
        G.add(f"feature_census.{tag}", Result(tag, n, "count"), "==", want, note=what)

    # REQ-03, REQ-04, D-04a, REQ-07 per column
    dlim = (SPEC["hole_d"] - SPEC["hole_tol"], SPEC["hole_d"] + SPEC["hole_tol"])
    cblim = (SPEC["cbore_d"] - SPEC["cbore_tol"], SPEC["cbore_d"] + SPEC["cbore_tol"])
    hole_axes = {}
    for req, pts in (("REQ-03", SPEC["bulkhead_cols"]), ("REQ-04", SPEC["rear_cols"])):
        for x, z in pts:
            tag = f"x{x:g}_z{z:g}"
            cf = _ycyl_faces(one, 0.5 * SPEC["col_d"], x, z, rtol=0.5)
            if cf:
                off = Result("column_axis_offset", max(math.hypot(c["cx"] - x, c["cz"] - z) for c in cf), "mm",
                             at=[cf[0]["cx"], 215.0, cf[0]["cz"]], detail={"faces": len(cf)})
                dface = Result("column_diameter_face", 2.0 * cf[0]["r"], "mm", at=[cf[0]["cx"], 215.0, cf[0]["cz"]])
            else:
                off = inconclusive("column_axis_offset", "mm", "no column cylinder found")
                dface = inconclusive("column_diameter_face", "mm", "no column cylinder found")
            G.add(f"{req}.{tag}.column_offset", off, "<=", SPEC["offset_max"], assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.column_d_face", dface, "in", (SPEC["col_d"] - SPEC["col_tol"],
                                                             SPEC["col_d"] + SPEC["col_tol"]), assumes=ASSUMES[req])
            # the window starts on the axis (the material from the hole wall r 1.7 to r 6 is one stretch)
            # and stops at r 8.5, short of the rear skirt (r 9 from the rear columns at -Z)
            r = {a: _ray(one, (x, 0.0, z), (0, 1, 0), (1, 0, 0), a, 215.5, "outer", r_min=0.0, r_max=8.5)
                 for a in (0.0, 90.0, 180.0, 270.0)}
            for k, (a1, a2) in (("x", (0.0, 180.0)), ("z", (90.0, 270.0))):
                d = (Result("column_diameter_ray", r[a1].measured + r[a2].measured, "mm", at=r[a1].at)
                     if r[a1].measured is not None and r[a2].measured is not None
                     else inconclusive("column_diameter_ray", "mm", "no ray"))
                G.add(f"{req}.{tag}.column_d_{k}", d, "in", (SPEC["col_d"] - SPEC["col_tol"],
                                                             SPEC["col_d"] + SPEC["col_tol"]), assumes=ASSUMES[req])
            bots = [f for f in downs if math.hypot(0.5 * (f["min"][0] + f["max"][0]) - x,
                                                   0.5 * (f["min"][2] + f["max"][2]) - z) < 1.0
                    and f["max"][0] - f["min"][0] < 13.0]
            by = (Result("column_bottom_y", -bots[0]["at"], "mm",
                         at=bots[0]["min"], detail={"faces": len(bots)})
                  if len(bots) == 1 else inconclusive("column_bottom_y", "mm", f"{len(bots)} bottom faces found"))
            G.add(f"{req}.{tag}.column_bottom_y", by, "in", (SPEC["col_bottom_y"] - SPEC["col_bottom_tol"],
                                                             SPEC["col_bottom_y"] + SPEC["col_bottom_tol"]),
                  assumes=ASSUMES[req])
            hl = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, 216.5, z), (0, 1, 0)))
            G.add(f"{req}.{tag}.hole_d", hl["diameter"], "in", dlim, assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.hole_offset", hl["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.hole_through", hl["through"], "==", 1, assumes=ASSUMES[req])
            G.add(f"D-04a.{tag}.hole_d", hl["diameter"], ">=", SPEC["hole_min_d"])
            cb = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, 234.0, z), (0, 1, 0)))
            G.add(f"{req}.{tag}.cbore_d", cb["diameter"], "in", cblim, assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.cbore_offset", cb["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES[req])
            G.add(f"REQ-07.{tag}.cbore_d", cb["diameter"], "in", cblim)
            hb = _find_bore(bores, (0, 1, 0), (x, 216.5, z), SPEC["hole_d"])
            cbb = _find_bore(bores, (0, 1, 0), (x, 234.0, z), SPEC["cbore_d"])
            if cbb is not None:
                ys = sorted((cbb["start"][1], cbb["end"][1]))
                fy = Result("cbore_floor_y", ys[0], "mm", at=[cbb["start"][0], ys[0], cbb["start"][2]],
                            detail={"top_y": ys[1], "open_ends": cbb.get("open_ends")})
                topy = Result("cbore_top_y", ys[1], "mm", at=[cbb["start"][0], ys[1], cbb["start"][2]])
                oe = cbb.get("open_ends")
                facts[f"{tag}.cbore_open_ends"] = oe
            else:
                fy = inconclusive("cbore_floor_y", "mm", "counterbore not found")
                topy = inconclusive("cbore_top_y", "mm", "counterbore not found")
            G.add(f"{req}.{tag}.cbore_floor_y", fy, "in", (SPEC["cbore_floor_y"] - SPEC["cbore_floor_tol"],
                                                           SPEC["cbore_floor_y"] + SPEC["cbore_floor_tol"]),
                  assumes=ASSUMES[req])
            G.add(f"REQ-07.{tag}.cbore_mouth_y", topy, "in", (SPEC["top_y"] - SPEC["top_tol"],
                                                              SPEC["top_y"] + SPEC["top_tol"]),
                  note="the counterbore runs to the top face (its mouth at y 250)")
            if cbb is not None:
                drv = _ycyl(cbb["start"][0], cbb["start"][2], SPEC["driver_r"],
                            min(cbb["start"][1], cbb["end"][1]) + 0.05, SPEC["top_y"] + 10.0)
                dpi = _safe(common_volume, "common_volume", "mm3", one, drv)
            else:
                dpi = inconclusive("common_volume", "mm3", "counterbore not found")
            G.add(f"REQ-07.{tag}.driver_path_interference", dpi,
                  "<=", SPEC["interference"], note="a driver of diameter 6.0 on the counterbore's measured axis, from "
                  "0.05 above its measured floor to 10 above the top face")
            if hb is not None:
                hole_axes[(x, z)] = (hb["start"][0], hb["start"][2])

    # REQ-05 pads (geometry on the lid)
    pad_meas = {}
    for x, z in SPEC["pads"]:
        tag = f"x{x:g}_z{z:g}"
        pf = _ycyl_faces(one, 0.5 * SPEC["pad_d"], x, z, rtol=0.5)
        if pf:
            off = Result("pad_axis_offset", max(math.hypot(c["cx"] - x, c["cz"] - z) for c in pf), "mm",
                         at=[pf[0]["cx"], 210.5, pf[0]["cz"]])
            pad_meas[(x, z)] = (pf[0]["cx"], pf[0]["cz"], pf[0]["r"])
        else:
            off = inconclusive("pad_axis_offset", "mm", "no pad cylinder found")
        G.add(f"REQ-05.{tag}.pad_offset", off, "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-05"])
        r = {a: _ray(one, (x, 0.0, z), (0, 1, 0), (1, 0, 0), a, 220.0, "outer", r_min=0.0, r_max=8.0)
             for a in (0.0, 90.0, 180.0, 270.0)}
        for k, (a1, a2) in (("x", (0.0, 180.0)), ("z", (90.0, 270.0))):
            d = (Result("pad_diameter_ray", r[a1].measured + r[a2].measured, "mm", at=r[a1].at)
                 if r[a1].measured is not None and r[a2].measured is not None
                 else inconclusive("pad_diameter_ray", "mm", "no ray"))
            G.add(f"REQ-05.{tag}.pad_d_{k}", d, "in", (SPEC["pad_d"] - SPEC["pad_tol"], SPEC["pad_d"] + SPEC["pad_tol"]),
                  assumes=ASSUMES["REQ-05"])
        bots = [f for f in downs if math.hypot(0.5 * (f["min"][0] + f["max"][0]) - x,
                                               0.5 * (f["min"][2] + f["max"][2]) - z) < 1.0
                and f["max"][0] - f["min"][0] < 11.0]
        by = (Result("pad_bottom_y", -bots[0]["at"], "mm", at=bots[0]["min"])
              if len(bots) == 1 else inconclusive("pad_bottom_y", "mm", f"{len(bots)} bottom faces found"))
        G.add(f"REQ-05.{tag}.pad_bottom_y", by, "in", (SPEC["pad_bottom_y"] - SPEC["pad_bottom_tol"],
                                                        SPEC["pad_bottom_y"] + SPEC["pad_bottom_tol"]),
              assumes=ASSUMES["REQ-05"])

    # REQ-06 headroom box
    x0, x1, y0_, y1_, z0, z1 = SPEC["headroom_box"]
    G.add("REQ-06.headroom_interference", _safe(common_volume, "common_volume", "mm3", one,
                                                _box(x0, x1, y0_, y1_, z0, z1)), "<=", SPEC["interference"],
          assumes=ASSUMES["REQ-06"])
    facts["REQ-06.box_clearance"] = _res(_safe(clearance, "clearance", "mm", one, _box(x0, x1, y0_, y1_ - 0.0, z0, z1)))

    # D-03b designer reading
    if not quick:
        fcs = _safe(flat_ceiling_spans, "flat_ceiling_spans", "mm", one, build_dir=SPEC["build_dir"],
                    max_span=SPEC["bridge_span"], spacing=SPACING)
        G.add("D-03b.flat_ceiling_span", fcs, "<=", SPEC["bridge_span"], assumes=ASSUMES["D-03b"],
              note="designer reading; the row is the reviewer's, from sections; only the four counterbore floors "
                   "(the named exception) are flat ceilings")
        facts["D-03b.ceilings"] = (fcs.detail or {}).get("ceilings") if isinstance(fcs, Result) else None

    # U-03 (a), (b), REQ-03/04 coaxiality, REQ-05 clearances: the parts as placed
    if asm_path is not None and asm_path.exists():
        asm = read_step(asm_path)
        kids = _children(asm)
        facts["assembly_labels"] = sorted(kids)
        lid = kids.get(PART)
        refs = {k: _one(kids[v]) for k, v in LABELS.items() if v in kids}
        if lid is None or len(refs) != len(LABELS):
            G.add("U-03.assembly", inconclusive("clearance", "mm", f"labels found: {sorted(kids)}"), "==", 0.0)
        else:
            lid = _one(lid)
            # placement checks (brief): the carrier's plate top at y 210.0, the valve mount's top y 48
            e05, e07 = envelope(refs["c05"]), envelope(refs["c07"])
            facts["placement.c05_max_y"] = e05["max_y"].measured
            facts["placement.c07_max_y"] = e07["max_y"].measured
            facts["placement.c05_envelope"] = {k: v.measured for k, v in e05.items()}
            facts["placement.c07_envelope"] = {k: v.measured for k, v in e07.items()}
            crop = {k: (_one(_crop(refs[k], CROP)) if k in ("c02", "c05", "c11") else refs[k]) for k in refs}
            facts["crop_volumes_mm3"] = {k: float(sum(s.volume for s in v.solids())) for k, v in crop.items()}
            # column seats: contact and no interference
            seat_ref = {(x, z): "c02" for x, z in SPEC["bulkhead_cols"]} | {(x, z): "c11" for x, z in SPEC["rear_cols"]}
            for (x, z), k in seat_ref.items():
                tag = f"x{x:g}_z{z:g}"
                ax_, az_ = col_axis[(x, z)]
                colpiece = _one(lid & _ycyl(ax_, az_, 6.2, 214.0, 222.0))
                G.add(f"U-03.seat.{tag}.{k}.clearance", _safe(clearance, "clearance", "mm", colpiece, crop[k]), "==",
                      SPEC["contact"], assumes=ASSUMES["U-03"], note="designed contact: the column bottom on its seat")
                G.add(f"U-03.seat.{tag}.{k}.interference", _safe(common_volume, "common_volume", "mm3", colpiece,
                                                                  crop[k]),
                      "<=", SPEC["interference"], assumes=ASSUMES["U-03"])
                rc = _safe(bore_census, "bore_census", "count", crop[k])
                ax = hole_axes.get((x, z))
                if ax is None:
                    co = inconclusive("bore_axis_offset", "mm", "lid hole not found")
                    G.add(f"U-03.coaxial.{tag}", co, "<=", SPEC["coax_max"])
                    continue
                L = _unpack(_safe(locate_bore, "locate_bore", "mm", rc, (ax[0], 212.0, ax[1]), (0, -1, 0)))
                facts[f"insert_under_{tag}"] = {kk: _res(vv) for kk, vv in L.items()}
                req = "REQ-03" if k == "c02" else "REQ-04"
                G.add(f"U-03.coaxial.{tag}", L["offset"], "<=", SPEC["coax_max"], assumes=ASSUMES["U-03"],
                      note="the lid hole's measured axis point located in the insert bore under it")
                G.add(f"{req}.{tag}.coaxial_with_insert", L["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES[req])
            # OD-C05: the pads, and nowhere less
            c05c = _safe(clearance, "clearance", "mm", lid, crop["c05"])
            G.add("U-03.c05.clearance", c05c, "in", (SPEC["pad_gap"] - SPEC["pad_gap_tol"],
                                                     SPEC["pad_gap"] + SPEC["pad_gap_tol"]), assumes=ASSUMES["U-03"])
            nopads = _cut(lid, [_ycyl(x, z, 0.5 * SPEC["pad_d"] + 0.05, 205.0, 246.0) for x, z in SPEC["pads"]])
            G.add("U-03.c05.clearance_without_pads", _safe(clearance, "clearance", "mm", nopads, crop["c05"]), ">=",
                  SPEC["pad_gap"], assumes=ASSUMES["U-03"], note="the lid less the two pads (r 5.05, y 205 .. 246)")
            G.add("U-03.c05.interference", _safe(common_volume, "common_volume", "mm3", lid, crop["c05"]), "<=",
                  SPEC["interference"], assumes=ASSUMES["U-03"])
            for x, z in SPEC["pads"]:
                tag = f"x{x:g}_z{z:g}"
                padpiece = _one(lid & _ycyl(x, z, 0.5 * SPEC["pad_d"] + 0.05, 205.0, 240.0))
                G.add(f"REQ-05.{tag}.clearance_to_c05", _safe(clearance, "clearance", "mm", padpiece, crop["c05"]), "in",
                      (SPEC["pad_gap"] - SPEC["pad_gap_tol"], SPEC["pad_gap"] + SPEC["pad_gap_tol"]),
                      assumes=ASSUMES["REQ-05"])
            # REQ-05 against the carrier's measured hub window and housing-screw counterbores
            c5c = _safe(bore_census, "bore_census", "count", crop["c05"])
            c5b = _bores(c5c)
            hub = _find_bore(c5b, (0, 1, 0), (0.0, 207.0, 32.0), 60.0, dtol=2.0)
            cbs = [b for b in c5b if _along(b, (0, 1, 0)) and abs(b["diameter"] - 6.5) < 0.3
                   and max(b["start"][1], b["end"][1]) > 209.0]
            facts["c05_hub"] = hub
            facts["c05_counterbores"] = cbs
            for x, z in SPEC["pads"]:
                tag = f"x{x:g}_z{z:g}"
                pm = pad_meas.get((x, z))
                if pm is None or hub is None:
                    G.add(f"REQ-05.{tag}.hub_r", inconclusive("pad_to_hub_r", "mm", "pad or hub not found"), ">=",
                          SPEC["hub_r_min"])
                else:
                    rr = math.hypot(pm[0] - hub["start"][0], pm[1] - hub["start"][2]) - pm[2]
                    G.add(f"REQ-05.{tag}.hub_r", Result("pad_to_hub_r", rr, "mm",
                          detail={"hub_d": hub["diameter"], "hub_centre": [hub["start"][0], hub["start"][2]]}),
                          ">=", SPEC["hub_r_min"], assumes=ASSUMES["REQ-05"],
                          note="the pad's nearest point to the hub window's axis")
                if pm is None or len(cbs) != 4:
                    G.add(f"REQ-05.{tag}.to_counterbores", inconclusive("pad_to_cbore", "mm",
                          f"pad found {pm is not None}, {len(cbs)} counterbores"), ">=", SPEC["cbore_edge_min"])
                else:
                    ds = [(math.hypot(pm[0] - b["start"][0], pm[1] - b["start"][2]) - pm[2] - 0.5 * b["diameter"], b)
                          for b in cbs]
                    dmin, bmin = min(ds, key=lambda t: t[0])
                    G.add(f"REQ-05.{tag}.to_counterbores", Result("pad_to_cbore", dmin, "mm",
                          at=[bmin["start"][0], 210.0, bmin["start"][2]]), ">=", SPEC["cbore_edge_min"],
                          assumes=ASSUMES["REQ-05"], note="edge to edge, the nearest of the four")
            # OD-C07, OD-C01
            G.add("U-03.c07.clearance", _safe(clearance, "clearance", "mm", lid, refs["c07"]), ">=", SPEC["c07_gap"],
                  assumes=ASSUMES["U-03"])
            G.add("U-03.plate.clearance", _safe(clearance, "clearance", "mm", lid, refs["plate"]), ">=",
                  SPEC["c01_gap"], assumes=ASSUMES["U-03"])
            # OD-C02 away from the column bottoms
            colx = [_ycyl(col_axis[(x, z)][0], col_axis[(x, z)][1], 6.05, 214.0, 251.0) for x, z in cols]
            away02 = _cut(lid, colx)
            G.add("U-03.c02.clearance_away", _safe(clearance, "clearance", "mm", away02, crop["c02"]), ">=",
                  SPEC["away_gap"], assumes=ASSUMES["U-03"], note="the lid less the four column volumes (r 6.05)")
            # OD-C11: the rear skirt's line contact, and away from it and the column bottoms
            G.add("U-03.c11.clearance_line_contact", _safe(clearance, "clearance", "mm", lid, crop["c11"]), "==",
                  SPEC["contact"], assumes=ASSUMES["U-03"])
            G.add("U-03.c11.interference", _safe(common_volume, "common_volume", "mm3", lid, crop["c11"]), "<=",
                  SPEC["interference"], assumes=ASSUMES["U-03"])
            away11 = _cut(lid, colx + [_box(-121.0, 121.0, 214.0, 251.0, -306.0, -301.95)])
            G.add("U-03.c11.clearance_away", _safe(clearance, "clearance", "mm", away11, crop["c11"]), ">=",
                  SPEC["away_gap"], assumes=ASSUMES["U-03"],
                  note="the lid less the column volumes and the rear skirt behind z -301.95 (the named line contact)")
            away11c = _cut(lid, colx + [_box(-121.0, 121.0, 214.0, 251.0, -306.0, -295.0)])
            facts["U-03.c11.clearance_without_rear_skirt_and_corner_arcs"] = _res(
                _safe(clearance, "clearance", "mm", away11c, crop["c11"]))
            # the contact faces between the lid's bottom faces at y 215 and OD-C11's top face at y 215
            try:
                l_b = [f["face"] for f in _planar(lid, (0, -1, 0)) if abs(-f["at"] - 215.0) < 1e-4]
                c_t = [f["face"] for f in _planar(crop["c11"], (0, 1, 0)) if abs(f["at"] - 215.0) < 1e-4]
                patches = []
                for fa in l_b:
                    for fb in c_t:
                        inter = fa.intersect(fb)
                        for pf in (inter.faces() if inter is not None else []):
                            bb = pf.bounding_box()
                            patches.append({"area_mm2": pf.area, "x": [bb.min.X, bb.max.X], "z": [bb.min.Z, bb.max.Z]})
                facts["U-03.c11.contact_patches"] = patches
                skirt_patch = [p for p in patches if p["z"][0] < -301.0]
                G.add("U-03.c11.skirt_contact_area_off_the_line",
                      Result("skirt_contact_area", sum(p["area_mm2"] for p in skirt_patch), "mm2",
                             at=[[p["x"], p["z"]] for p in skirt_patch]), "<=", 0.0, assumes=ASSUMES["U-03"],
                      note="a line contact has no area: area over which the skirt's bottom face lies on OD-C11's top "
                           "face (face intersection at y 215)")
            except Exception as exc:  # noqa: BLE001
                G.add("U-03.c11.skirt_contact_area_off_the_line",
                      inconclusive("skirt_contact_area", "mm2", f"{type(exc).__name__}: {exc}"), "<=", 0.0)
            # U-03 (b): lowered along -Y from +40.0 in steps of 2.0
            steps = int(round(SPEC["lower_from"] / SPEC["lower_step"]))
            path_rows = []
            for i in range(steps + 1):
                dy = SPEC["lower_from"] - i * SPEC["lower_step"]
                moved = lid.moved(Location((0.0, dy, 0.0)))
                for k, s in crop.items():
                    cv = _safe(common_volume, "common_volume", "mm3", moved, s)
                    path_rows.append({"dy": dy, "ref": k, "measured": cv.measured, "status": cv.status,
                                      "reason": cv.reason})
            facts["U-03b.path"] = path_rows
            for k in LABELS:
                rows_k = [r for r in path_rows if r["ref"] == k]
                bad = [r for r in rows_k if r["measured"] is None]
                if not rows_k:
                    r = inconclusive("common_volume", "mm3", f"{k} missing in the assembly")
                elif bad:
                    r = inconclusive("common_volume", "mm3", f"dy {bad[0]['dy']:g}: {bad[0]['reason']}")
                else:
                    wr = max(rows_k, key=lambda t: t["measured"])
                    r = Result("common_volume", wr["measured"], "mm3", at=f"dy {wr['dy']:g}")
                G.add(f"U-03(b).{k}.worst_interference", r, "<=", SPEC["interference"], assumes=ASSUMES["U-03"],
                      note=f"{steps + 1} poses, dy {SPEC['lower_from']:g} .. 0 in {SPEC['lower_step']:g} steps")
    else:
        G.add("U-03.assembly", inconclusive("clearance", "mm", "no assembly file"), "==", 0.0)

    # U-04: part and assembly round trip against the build
    try:
        import build_od_c10_top as B
        p = B.Params(**variant)
        built = B.build_lid(p)
        rt = compare_step(built, step_path)
        G.add("U-04.part.schema", rt["schema"], "==", 1)
        G.add("U-04.part.solids", rt["solids"], "==", 1)
        G.add("U-04.part.volume_delta", rt["volume_delta"], "in", (0.0, 0.0))
        G.add("U-04.part.faces_delta", rt["faces_delta"], "==", 0)
        G.add("U-04.part.labels", rt["labels"], "==", 1)
        G.add("U-04.part.valid_after", rt["valid_after"], "==", 1)
        if asm_path is not None and asm_path.exists():
            ba = B.build_assembly(p)["assembly"]
            ra = compare_step(ba, asm_path)
            G.add("U-04.assembly.schema", ra["schema"], "==", 1)
            G.add("U-04.assembly.solids", ra["solids"], "==", 6)
            G.add("U-04.assembly.faces_delta", ra["faces_delta"], "==", 0)
            G.add("U-04.assembly.labels", ra["labels"], "==", 1)
            G.add("U-04.assembly.valid_after", ra["valid_after"], "==", 1)
            kb, kr = _children(ba), _children(read_step(asm_path))
            for lab, sb in kb.items():
                sr = kr.get(lab)
                if sr is None:
                    G.add(f"U-04.assembly.{lab}.volume_delta", inconclusive("volume_delta", "mm3", "label lost"),
                          "in", (0.0, 0.0))
                    continue
                dv = abs(mass_properties(sr, SPEC["density"])["volume"].measured
                         - mass_properties(sb, SPEC["density"])["volume"].measured)
                G.add(f"U-04.assembly.{lab}.volume_delta", Result("volume_delta", dv, "mm3"), "in", (0.0, 0.0))
    except Exception as exc:  # noqa: BLE001
        G.add("U-04.part", inconclusive("compare_step", "", f"{type(exc).__name__}: {exc}"), "==", 0)
        facts["U-04.traceback"] = traceback.format_exc()

    # D-01a, D-01b, D-06a, U-06 (Soft)
    if not quick:
        mw = _safe(min_wall, "min_wall", "mm", one, spacing=SPACING)
        G.add("D-01a", mw, ">=", SPEC["wall_floor"])
        G.add("D-01b", mw, ">=", SPEC["wall_struct"])
        G.add("D-06a", mw, ">=", SPEC["min_feature"])
        ww = _safe(min_wall_wide, "min_wall_wide", "mm", one, spacing=SPACING)
        G.add("U-06(Soft)", ww, ">=", SPEC["wall_wide"])

    # D-03a: census outside the named exception (the four counterbores refilled by position)
    facts["D-03a.exception_counterbores"] = len(y65)
    exc_area = sum(math.pi * ((0.5 * b["diameter"]) ** 2 - (0.5 * h["diameter"]) ** 2)
                   for b in y65 for h in y34 if math.hypot(b["start"][0] - h["start"][0],
                                                           b["start"][2] - h["start"][2]) < 0.5)
    facts["D-03a.exception_floor_area_mm2"] = exc_area
    try:
        filled = _refilled(one, y65)
        nf = len(filled.faces())
        facts["D-03a.refilled_faces"] = nf
        facts["D-03a.refilled_solids"] = len(filled.solids())
        if len(y65) != 4 or len(filled.solids()) != 1:
            oh_out = inconclusive("overhang_census", "deg", f"refill not as planned: {len(y65)} counterbores, "
                                  f"{len(filled.solids())} solids")
        else:
            oh_out = _safe(overhang_census, "overhang_census", "deg", filled, build_dir=SPEC["build_dir"],
                           spacing=SPACING)
    except Exception as exc:  # noqa: BLE001
        oh_out = inconclusive("overhang_census", "deg", f"{type(exc).__name__}: {exc}")
    G.add("D-03a", oh_out, ">=", SPEC["overhang_deg"], assumes=ASSUMES["D-03a"],
          note="overhang_census outside the named exception: the four counterbores refilled by position; the "
               "whole-part census and the exception floors' area in facts")
    if not quick:
        oh_all = _safe(overhang_census, "overhang_census", "deg", one, build_dir=SPEC["build_dir"], spacing=SPACING)
        facts["D-03a.whole_part_census"] = _res(oh_all) | {"detail": oh_all.detail}
    facts["down_faces_in_print"] = _down_faces(one, SPEC["build_dir"])

    # U-07: mesh
    if stl_path is not None and stl_path.exists():
        facts["stl"] = _stl_facts(stl_path)
        facts["stl_sha256"] = file_sha256(stl_path)
        mc = _safe(mesh_census, "mesh_census", "count", stl_path)
        if isinstance(mc, dict):
            facts["mesh_census"] = {k: v.measured for k, v in mc.items()}
            G.add("U-07.mesh.bodies", mc["bodies"], "==", 1)
            G.add("U-07.mesh.naked_edges", mc["naked_edges"], "==", 0)
            G.add("U-07.mesh.winding", mc["winding"], "==", 1)
        else:
            G.add("U-07.mesh", mc, "==", 1)
        rec = json.loads(record_path.read_text()) if record_path is not None and record_path.exists() else {}
        ang = rec.get("stl", {}).get("angular_tolerance")
        G.add("U-07.angular_tolerance", Result("stl_angular_tolerance", ang, "rad") if ang is not None
              else inconclusive("stl_angular_tolerance", "rad", "no build record"), "<=", SPEC["stl_ang_max"])
        tl = rec.get("stl", {}).get("tolerance")
        G.add("U-07.tolerance", Result("stl_tolerance", tl, "mm") if tl is not None
              else inconclusive("stl_tolerance", "mm", "no build record"), "<=", SPEC["stl_tol"])
        scratch.mkdir(parents=True, exist_ok=True)
        try:
            w = write_stl(one, scratch / "remesh_check.stl", tolerance=SPEC["stl_tol"], angular_tolerance=ang or 0.17)
            sag = w.checks["max_sagitta"]
            facts["remesh_triangles"] = w.detail.get("triangles")
        except Exception as exc:  # noqa: BLE001
            sag = inconclusive("stl_max_sagitta", "mm", f"{type(exc).__name__}: {exc}")
        G.add("U-07.max_sagitta", sag, "<=", SPEC["stl_tol"],
              note="re-meshed from the re-imported STEP at the build's settings")
        rs = rec.get("stl", {}).get("max_sagitta")
        G.add("U-07.max_sagitta_delivered", Result("stl_max_sagitta", rs, "mm") if rs is not None
              else inconclusive("stl_max_sagitta", "mm", "no build record"), "<=", SPEC["stl_tol"],
              note="the sagitta write_stl measured on the delivered STL")
    else:
        G.add("U-07", inconclusive("mesh", "mm", "no STL"), "<=", SPEC["stl_tol"])

    # by the rows
    G.fixed("U-08", "N/A", "N/A", "no threads (N/A by its row)")
    G.fixed("D-05a", "N/A", "N/A", "no insert boss on this part (N/A by its row)")
    G.fixed("D-05b", "N/A", "N/A", "no insert hole on this part (N/A by its row)")
    G.fixed("D-07", "N/A", "N/A", "no fit-critical bores (N/A by its row)")
    G.fixed("J-05", "N/A", "N/A", "no threaded hole on this part (N/A by its row)")
    G.fixed("E-06", INCONCLUSIVE, "reviewer", "reviewer row, from sections; designer evidence: one solid, the rib "
            "faces by position (U-05 rows), sections through every column axis")
    G.fixed("REQ-08(Soft)", INCONCLUSIVE, "bench", "Soft bench gate: not geometric, answered by the first print",
            assumes=ASSUMES["REQ-08"])
    mp = mass_properties(one, SPEC["density"])
    facts["mass"] = {k: v.measured for k, v in mp.items()}
    facts["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return {"gates": G.rows, "facts": facts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True)
    ap.add_argument("--asm")
    ap.add_argument("--stl")
    ap.add_argument("--record")
    ap.add_argument("--out", required=True)
    ap.add_argument("--scratch", default="01_CAD/sweep_v01/_mesh_check")
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--quick", action="store_true", help="skip min_wall, the whole-part census, flat ceilings")
    a = ap.parse_args()

    def rel(s):
        if s is None:
            return None
        q = Path(s)
        return q if q.is_absolute() else WS / q
    out = check(rel(a.step), rel(a.asm), rel(a.stl), rel(a.record), json.loads(a.variant), rel(a.scratch),
                quick=a.quick)
    rel(a.out).write_text(json.dumps(out, indent=1, default=str))
    for r in out["gates"]:
        print(f"{r['gate']:<52} {r['status']:<13} {r.get('measured')!s:<22} {r.get('required')!s:<28} "
              f"{r.get('margin')!s:<12} {str(r.get('reason', ''))[:90]}")


if __name__ == "__main__":
    main()
