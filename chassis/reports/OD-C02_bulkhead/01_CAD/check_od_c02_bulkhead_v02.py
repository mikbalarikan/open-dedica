"""Checks for od_c02_bulkhead v02 (job 20260930-od-c02-bulkhead, concept C1, spec 1.1).

Written before the v02 build (PLAYBOOK D3), from the v01 checks and the plan
amendment 01_CAD/DESIGN_PLAN_v02.md. Every predicate measures the re-imported
STEP files with tools.core / tools.measure and compares through tools.result.gate
with the GATES.md section 0 band. Thresholds come from DESIGN_SPEC.md 1.1 section 5
only (the SPEC table cites the row of each value). Any exception or missing value
gives INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c02_bulkhead_v02.py \
        --step 02_STEP_STL/od_c02_bulkhead_C1_v02.step \
        --asm 02_STEP_STL/od_c02_assembly_C1_v02.step \
        --stl 02_STEP_STL/od_c02_bulkhead_C1_v02.stl \
        --record 01_CAD/build_record_v02.json \
        --out 01_CAD/check_od_c02_bulkhead_v02.json [--variant '{...}']
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
from build123d import Align, Cylinder, Plane, Pos  # noqa: E402

from tools.core import common_volume, compare_step, read_step, validity, write_stl  # noqa: E402
from tools.core.step import file_sha256  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census, locate_bore,  # noqa: E402
                           mass_properties, mesh_census, min_wall, min_wall_wide, overhang_census,
                           radial_extent)
from tools.result import INCONCLUSIVE, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.1) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "count": 0, "bool": 0}
SPEC = {
    # U-02: 12.0 x 215.0 x 210.0 each +-0.1; position x 59 .. 71, y 0 .. 215, z -240 .. -30
    "size": {"size_x": 12.0, "size_y": 215.0, "size_z": 210.0}, "size_tol": 0.1,
    "position": {"min_x": 59.0, "max_x": 71.0, "min_y": 0.0, "max_y": 215.0, "min_z": -240.0, "max_z": -30.0},
    # D-02 (A-08): K1C 220 x 220 x 250; standing on z -240: x and y on the bed, z tall
    "bed": {"size_x": 220.0, "size_y": 220.0, "size_z": 250.0},
    # D-01a, D-01b (spec 1.1: 2.0), D-06a, U-06 (Soft)
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wall_wide": 2.0,
    # J-05, D-05a
    "wall_insert": 3.0, "boss_across": 8.0,
    # D-03a: >= 45 deg, build direction +Z (A-10); D-03b span <= 5
    "overhang_deg": 45.0, "build_dir": (0.0, 0.0, 1.0), "bridge_span": 5.0,
    # U-07
    "stl_tol": 0.01, "stl_ang_max": 4.0 * math.acos(1.0 - 0.01 / 6.0),
    # U-03 (a): contact 0, interference <= 0, coaxial <= 0.10, neighbours >= 3.0, carrier box >= 4.0
    "contact": 0.0, "interference": 0.0, "coax": 0.10, "neighbour_gap": 3.0, "box_gap": 4.0,
    # REQ-01, REQ-07, D-05b: six insert bores
    "base_bores": ((65.0, -45.0), (65.0, -105.0), (65.0, -165.0), (65.0, -225.0)),
    "top_bores": ((65.0, -60.0), (65.0, -210.0)),
    "bore_d": 4.0, "bore_tol": 0.05, "bore_depth": 6.0, "bore_depth_tol": 0.1, "bore_min_depth": 5.7,
    "offset_max": 0.10,
    # REQ-02
    "wet_face_x": 63.0, "elec_face_x": 67.0, "face_tol": 0.10, "rail_wet_x": 59.0, "face_ys": (100.0, 200.0),
    # REQ-03
    "rail_under_y": 0.0, "rail_under_tol": 0.10, "rail_top_y": 12.0, "rail_top_tol": 0.1, "rail_under_faces": 1,
    "rail_under_extent": {"x_from": 59.0, "x_to": 71.0, "z_from": -240.0, "z_to": -30.0}, "rail_under_mouths": 4,
    # REQ-04
    "windows": ((150.0, -200.0), (150.0, -130.0), (150.0, -60.0), (60.0, -55.0)), "win_d": 14.0,
    "win_tol": 0.1, "win_apex_above_centre": 14.0, "front_end_faces": 1, "collar_faces": 0,
    # REQ-05, REQ-06, REQ-08
    "keepout_min_x": 59.0, "top_y": 215.0, "top_tol": 0.1, "max_x": 71.0, "elec_face_max": 70.0,
    # U-05 census (plan amendment v02 section 3)
    "census": {"plane_faces": 36, "cylinder_faces": 10, "concave_cylinders": 10, "convex_cylinders": 0,
               "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0, "bspline_faces": 0, "other_faces": 0,
               "bores": 6},
    "bores_from_below": 4, "bores_from_above": 2, "window_half_cyl": 4, "refilled_faces": 34,
    "density": 1070.0,
}
ASSUMES = {"U-03": ("A-01", "A-02"), "REQ-01": ("A-01", "A-03"), "REQ-02": ("A-01",), "REQ-03": ("A-01",),
           "REQ-04": ("A-04",), "REQ-05": ("A-02",), "REQ-06": ("A-06",), "REQ-07": ("A-05",),
           "REQ-08": ("A-07",), "D-02": ("A-08",), "D-03a": ("A-10",), "D-05a": ("A-05",), "D-05b": ("A-05",)}
SPACING = 0.7   # plan section 2 and the WP-02 brief: the tools refuse the large faces at the default spacing
PART = "od_c02_bulkhead"
LABELS = {"plate": "od_c01_frame", "c03": "od_c03_cradle", "h01": "od_h01_pump", "c04": "od_c04_mount",
          "h11": "od_h11_thermoblock", "g01": "od_g01_housing", "box": "od_c05_foot_reference_A02"}
NEIGHBOURS = ("c03", "h01", "c04", "h11", "g01")
PLATE_PROBE_Y = -3.0   # plan section 2: a point 3.0 below the plate top, inside the plate's 6.0 holes


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
            row["detail"] = {k: v for k, v in detail.items() if k not in ("bores", "points", "pairs", "samples")}
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


def _circle3(p1, p2, p3):
    """Centre and radius of the circle through three points in a plane (2-D)."""
    ax, ay = p1
    bx, by = p2
    cx, cy = p3
    d = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy), math.hypot(ax - ux, ay - uy)


def _planar_faces(shape, normal, tol=1e-6):
    """Planar faces of the B-rep whose normal is `normal` (unit axis), with their
    position along it and their bounding box."""
    n = np.array(normal, float)
    out = []
    for f in shape.faces():
        if f.geom_type.name != "PLANE":
            continue
        fn = np.array(tuple(f.normal_at()))
        if float(np.dot(fn, n)) < 1.0 - tol:
            continue
        bb = f.bounding_box()
        out.append({"at": float(np.dot(np.array(tuple(f.center())), n)), "area": f.area,
                    "min": [bb.min.X, bb.min.Y, bb.min.Z], "max": [bb.max.X, bb.max.Y, bb.max.Z]})
    return out


def _down_face_split(shape, bed_z):
    """Diagnostic beside the overhang census (the census takes no region): every face
    with a downward-facing sample (build +Z), its least angle on a 9 x 9 grid of its
    parameters, its kind and its box, grouped by the feature its position names."""
    rows = []
    for f in shape.faces():
        least = None
        for u in np.linspace(0.0, 1.0, 9):
            for v in np.linspace(0.0, 1.0, 9):
                try:
                    p = f.position_at(u, v)
                    n = f.normal_at(u, v)
                except Exception:  # noqa: BLE001
                    continue
                if p.Z - bed_z <= 0.01:
                    continue
                tb = -n.Z
                if tb <= 1e-6:
                    continue
                a = math.degrees(math.acos(min(1.0, tb)))
                least = a if least is None else min(least, a)
        if least is None:
            continue
        bb = f.bounding_box()
        kind = f.geom_type.name.lower()
        r = None
        if kind == "cylinder":
            try:
                r = round(f.radius, 4)
            except Exception:  # noqa: BLE001
                r = None
        rows.append({"kind": kind, "radius": r, "least_deg": round(least, 4),
                     "min": [round(bb.min.X, 3), round(bb.min.Y, 3), round(bb.min.Z, 3)],
                     "max": [round(bb.max.X, 3), round(bb.max.Y, 3), round(bb.max.Z, 3)],
                     "region": _region(kind, r, bb)})
    return rows


def _region(kind, r, bb):
    """The feature a downward face belongs to, by position (plan amendment v02 section 3)."""
    cx = 0.5 * (bb.min.X + bb.max.X)
    if kind == "cylinder" and r is not None:
        if abs(r - 2.0) < 0.05 and abs(cx - 65.0) < 2.5 and bb.max.Y <= 12.0:
            return "exception: base-rail insert bore 4.0 crown"
        if abs(r - 2.0) < 0.05 and abs(cx - 65.0) < 2.5 and bb.min.Y >= 207.0:
            return "exception: top-rail insert bore 4.0 crown"
        if abs(r - 7.0) < 0.05:
            return "window round part"
    if kind == "plane" and bb.min.X >= 62.999 and bb.max.X <= 67.001:
        return "window roof"
    return "other"


def _bore_axis_point(bore, y):
    """The point of a bore's measured axis at height y."""
    s, a = np.array(bore["start"], float), np.array(bore["axis_dir"], float)
    if abs(a[1]) < 1e-9:
        return None
    return tuple(float(v) for v in s + a * ((y - s[1]) / a[1]))


def _find_bore(bores, x, z, y_lo, y_hi):
    """The census bore along Y whose axis passes nearest (x, z) with its span inside y_lo .. y_hi."""
    best = None
    for b in bores:
        a = np.array(b["axis_dir"], float)
        if abs(abs(a[1]) - 1.0) > 1e-6:
            continue
        ys = sorted((b["start"][1], b["end"][1]))
        if ys[0] < y_lo - 1e-6 or ys[1] > y_hi + 1e-6:
            continue
        d = math.hypot(b["start"][0] - x, b["start"][2] - z)
        if best is None or d < best[0]:
            best = (d, b)
    return None if best is None else best[1]


def _refilled(one, bores):
    """The solid with each of the named-exception bores refilled: a cylinder of the
    measured diameter + 0.2 on the measured axis, from the mouth to 0.05 past the
    floor. The census outside the named exception is read on it (plan section 2)."""
    solid = one
    for b in bores:
        s, e = np.array(b["start"], float), np.array(b["end"], float)
        ys = sorted((s[1], e[1]))
        mouth_low = ys[0] <= 1e-6            # a base-rail bore opens at y 0
        y0 = ys[0] if mouth_low else ys[0] - 0.05
        y1 = ys[1] + 0.05 if mouth_low else ys[1]
        up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
        plug = Pos(s[0], y0, s[2]) * (up * Cylinder(0.5 * b["diameter"] + 0.1, y1 - y0,
                                                    align=(Align.CENTER, Align.CENTER, Align.MIN)))
        solid = solid + plug
    solid = solid.clean()
    sols = solid.solids()
    return sols[0] if len(sols) == 1 else solid


def _unpack(loc):
    if isinstance(loc, Result):
        return {"diameter": loc, "offset": loc, "length": loc, "through": loc}
    return loc


def check(step_path: Path, asm_path: Path | None, stl_path: Path | None, record_path: Path | None,
          variant: dict, scratch: Path) -> dict:
    G = Gates()
    facts: dict = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    part = read_step(step_path)
    sols = part.solids()
    one = sols[0] if len(sols) == 1 else part
    facts["step_sha256"] = file_sha256(step_path)

    # U-01, exactly_one_solid
    val = _safe(validity, "validity", "", part)
    if isinstance(val, Result):
        val = {"solid_count": val, "brep_valid": val, "naked_edges": val}
    G.add("U-01.solid_count", val["solid_count"], "==", 1)
    G.add("U-01.brep_valid", val["brep_valid"], "==", 1)
    G.add("U-01.naked_edges", val["naked_edges"], "==", 0)
    G.add("exactly_one_solid", val["solid_count"], "==", 1)

    # U-02, envelope_within_spec, D-02, REQ-02 (rail wet face), REQ-05, REQ-06, REQ-08
    env = envelope(one)
    tol = SPEC["size_tol"]
    for k, v in SPEC["size"].items():
        G.add(f"U-02.{k}", env[k], "in", (v - tol, v + tol))
        G.add(f"envelope_within_spec.{k}", env[k], "in", (v - tol, v + tol))
    for k, v in SPEC["position"].items():
        G.add(f"envelope_within_spec.position.{k}", env[k], "in", (v - tol, v + tol),
              note="position against the datum, reported apart from the size (L-12)")
    for k, v in SPEC["bed"].items():
        G.add(f"D-02.{k}", env[k], "<=", v, assumes=ASSUMES["D-02"])
    G.add("REQ-02.rail_wet_face_min_x", env["min_x"], "in",
          (SPEC["rail_wet_x"] - SPEC["face_tol"], SPEC["rail_wet_x"] + SPEC["face_tol"]), assumes=ASSUMES["REQ-02"])
    G.add("REQ-05.min_x", env["min_x"], ">=", SPEC["keepout_min_x"], assumes=ASSUMES["REQ-05"])
    G.add("REQ-06.max_y", env["max_y"], "in", (SPEC["top_y"] - SPEC["top_tol"], SPEC["top_y"] + SPEC["top_tol"]),
          assumes=ASSUMES["REQ-06"])
    G.add("REQ-08.max_x", env["max_x"], "<=", SPEC["max_x"], assumes=ASSUMES["REQ-08"])
    facts["envelope"] = {k: v.measured for k, v in env.items()}

    # REQ-02 wall faces: rays along +-X from the wall's mid-plane at y 100 and y 200, z -100 and z -170
    for y in SPEC["face_ys"]:
        for z in (-100.0, -170.0):
            wet = _ray(one, (65.0, 0.0, z), (0, 1, 0), (1, 0, 0), 180.0, y, "outer", r_max=3.5)
            ele = _ray(one, (65.0, 0.0, z), (0, 1, 0), (1, 0, 0), 0.0, y, "outer", r_max=3.5)
            for tag, r, target, sgn in (("wet_face_x", wet, SPEC["wet_face_x"], -1.0),
                                        ("elec_face_x", ele, SPEC["elec_face_x"], 1.0)):
                x = Result("wall_face_x", None if r.measured is None else 65.0 + sgn * r.measured, "mm", at=r.at,
                           status=r.status, reason=r.reason, detail={"ray": "radial_extent outer from x 65"})
                G.add(f"REQ-02.{tag}.y{y:g}_z{z:g}", x, "in", (target - SPEC["face_tol"], target + SPEC["face_tol"]),
                      assumes=ASSUMES["REQ-02"])
    ele = _ray(one, (65.0, 0.0, -100.0), (0, 1, 0), (1, 0, 0), 0.0, 100.0, "outer", r_max=3.5)
    xe = Result("wall_face_x", None if ele.measured is None else 65.0 + ele.measured, "mm", at=ele.at,
                status=ele.status, reason=ele.reason)
    G.add("REQ-08.wall_elec_face_x", xe, "<=", SPEC["elec_face_max"], assumes=ASSUMES["REQ-08"])

    # REQ-03 rail underside (one planar face less the four bore mouths) and rail top
    min_y = env["min_y"].measured
    under_faces = [f for f in one.faces() if f.geom_type.name == "PLANE"
                   and float(f.normal_at().Y) < -1.0 + 1e-6 and abs(f.center().Y - min_y) < 1e-4]
    under = [f for f in _planar_faces(one, (0, -1, 0)) if abs(f["at"] + min_y) < 1e-4]
    facts["rail_underside_faces"] = under
    G.add("REQ-03.underside_faces", Result("planar_faces_at_min_y", len(under), "count"), "==",
          SPEC["rail_under_faces"], assumes=ASSUMES["REQ-03"])
    if len(under_faces) == 1:
        G.add("REQ-03.underside_bore_mouths", Result("underside_inner_wires", len(under_faces[0].inner_wires()),
                                                     "count"), "==", SPEC["rail_under_mouths"],
              assumes=ASSUMES["REQ-03"], note="the four insert bore mouths are the underside's inner wires")
    if under:
        u = under[0]
        G.add("REQ-03.underside_y", Result("underside_y", -u["at"], "mm", at=u["min"]), "in",
              (SPEC["rail_under_y"] - SPEC["rail_under_tol"], SPEC["rail_under_y"] + SPEC["rail_under_tol"]),
              assumes=ASSUMES["REQ-03"])
        for k, (i, which) in {"x_from": (0, "min"), "x_to": (0, "max"), "z_from": (2, "min"),
                              "z_to": (2, "max")}.items():
            v = SPEC["rail_under_extent"][k]
            G.add(f"REQ-03.underside_{k}", Result("underside_extent", u[which][i], "mm"), "in",
                  (v - SPEC["rail_under_tol"], v + SPEC["rail_under_tol"]), assumes=ASSUMES["REQ-03"])
    for x in (60.0, 69.0):
        top = _ray(one, (x, 6.0, -140.0), (1, 0, 0), (0, 1, 0), 0.0, 0.0, "outer", r_max=6.5)
        yt = Result("rail_top_y", None if top.measured is None else 6.0 + top.measured, "mm", at=top.at,
                    status=top.status, reason=top.reason)
        G.add(f"REQ-03.rail_top_y.x{x:g}", yt, "in", (SPEC["rail_top_y"] - SPEC["rail_top_tol"],
                                                       SPEC["rail_top_y"] + SPEC["rail_top_tol"]),
              assumes=ASSUMES["REQ-03"])

    # U-05 feature census, bores
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
    bores = census.detail.get("bores", []) if isinstance(census, Result) and census.detail else []
    facts["bores"] = bores
    y_top = env["max_y"].measured
    below = [b for b in bores if min(b["start"][1], b["end"][1]) <= min_y + 1e-6]
    above = [b for b in bores if max(b["start"][1], b["end"][1]) >= y_top - 1e-6]
    G.add("U-05.bores_from_below", Result("bores_open_at_min_y", len(below), "count"), "==", SPEC["bores_from_below"])
    G.add("U-05.bores_from_above", Result("bores_open_at_max_y", len(above), "count"), "==", SPEC["bores_from_above"])
    wh = sum(1 for f in one.faces() if f.geom_type.name == "CYLINDER" and abs(f.radius - 7.0) < 1e-3)
    G.add("U-05.window_half_cylinders_r7", Result("cyl_faces_r7", wh, "count"), "==", SPEC["window_half_cyl"])
    G.add("feature_census.window_half_cylinders_r7", Result("cyl_faces_r7", wh, "count"), "==",
          SPEC["window_half_cyl"])

    # REQ-01, REQ-07, D-05b, D-05a, J-05: the six insert bores
    dlim = (SPEC["bore_d"] - SPEC["bore_tol"], SPEC["bore_d"] + SPEC["bore_tol"])
    hlim = (SPEC["bore_depth"] - SPEC["bore_depth_tol"], SPEC["bore_depth"] + SPEC["bore_depth_tol"])
    groups = [("REQ-01", "base", SPEC["base_bores"], 3.0, (0, 1, 0), min_y, min_y + 12.0),
              ("REQ-07", "top", SPEC["top_bores"], 212.0, (0, -1, 0), y_top - 8.0, y_top)]
    widest = None
    located = {}
    for req, name, xzs, ymid, direction, ylo, yhi in groups:
        for x, z in xzs:
            tag = f"{name}.x{x:g}_z{z:g}"
            loc = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, ymid, z), direction))
            located[tag] = loc
            G.add(f"{req}.{tag}.diameter", loc["diameter"], "in", dlim, assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.depth", loc["length"], "in", hlim, assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.blind", loc["through"], "==", 0, assumes=ASSUMES[req])
            G.add(f"D-05b.{tag}.diameter", loc["diameter"], "in", dlim, assumes=ASSUMES["D-05b"])
            G.add(f"D-05b.{tag}.depth", loc["length"], "in", hlim, assumes=ASSUMES["D-05b"])
            G.add(f"D-05b.{tag}.depth_min", loc["length"], ">=", SPEC["bore_min_depth"], assumes=ASSUMES["D-05b"])
            dm = loc["diameter"].measured
            if dm is not None:
                widest = dm if widest is None else max(widest, dm)
            # D-05a, J-05: rays along +-X at the bore's mid-depth, from its measured axis
            b = _find_bore(bores, x, z, ylo, yhi)
            if b is None:
                for side in ("elec", "wet"):
                    G.add(f"J-05.{tag}.{side}", inconclusive("wall_around_insert", "mm", "bore not found"), ">=",
                          SPEC["wall_insert"])
                G.add(f"D-05a.{tag}.across_x", inconclusive("boss_across_x", "mm", "bore not found"), ">=",
                      SPEC["boss_across"], assumes=ASSUMES["D-05a"])
                continue
            ymid_b = 0.5 * (b["start"][1] + b["end"][1])
            org = (b["start"][0], 0.0, b["start"][2])
            rp = _ray(one, org, (0, 1, 0), (1, 0, 0), 0.0, ymid_b, "outer", r_max=12.0)
            rn = _ray(one, org, (0, 1, 0), (1, 0, 0), 180.0, ymid_b, "outer", r_max=12.0)
            if rp.measured is not None and rn.measured is not None:
                across = Result("boss_across_x", rp.measured + rn.measured, "mm", at=[rp.at, rn.at])
            else:
                across = inconclusive("boss_across_x", "mm", f"{rp.reason} {rn.reason}".strip())
            G.add(f"D-05a.{tag}.across_x", across, ">=", SPEC["boss_across"], assumes=ASSUMES["D-05a"])
            for side, rr in (("elec", rp), ("wet", rn)):
                if rr.measured is not None:
                    w = Result("wall_around_insert", rr.measured - b["diameter"] / 2.0, "mm", at=rr.at)
                else:
                    w = inconclusive("wall_around_insert", "mm", rr.reason or "no ray")
                G.add(f"J-05.{tag}.{side}", w, ">=", SPEC["wall_insert"])

    # D-03b designer's reading: the widest horizontal (print) bore is the widest bridge; windows gabled (REQ-04)
    G.add("D-03b.widest_bore_bridge", Result("bore_bridge_span", widest, "mm") if widest is not None
          else inconclusive("bore_bridge_span", "mm", "no bore located"), "<=", SPEC["bridge_span"],
          note="reviewer row; designer's reading: the six horizontal insert bores bridge their diameter, "
               "the windows carry a 45-degree gable (REQ-04)")

    # REQ-04 windows: round part (three rays on the lower half), apex, roof, front end, no collar
    for i, (yc, zc) in enumerate(SPEC["windows"], start=1):
        tag = f"w{i}_y{yc:g}_z{zc:g}"
        org = (62.0, yc, zc)
        pts, reasons = [], []
        for ang in (200.0, 270.0, 340.0):
            r = _ray(one, org, (1, 0, 0), (0, 1, 0), ang, 3.0, "inner")
            if r.measured is None:
                reasons.append(r.reason)
            else:
                a = math.radians(ang)
                pts.append((r.measured * math.cos(a), r.measured * math.sin(a)))
        if len(pts) == 3:
            (uy, uz), rad = _circle3(*pts)
            dia = Result("window_round_diameter", 2.0 * rad, "mm", at=[65.0, yc + uy, zc + uz],
                         detail={"from": "three radial_extent rays at 200/270/340 deg, x 65"})
            off = Result("window_round_offset", math.hypot(uy, uz), "mm", at=[65.0, yc + uy, zc + uz])
        else:
            dia = inconclusive("window_round_diameter", "mm", "; ".join(reasons))
            off = inconclusive("window_round_offset", "mm", "; ".join(reasons))
        G.add(f"REQ-04.{tag}.diameter", dia, "in", (SPEC["win_d"] - SPEC["win_tol"], SPEC["win_d"] + SPEC["win_tol"]),
              assumes=ASSUMES["REQ-04"])
        G.add(f"REQ-04.{tag}.offset", off, "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-04"])
        apex = _ray(one, org, (1, 0, 0), (0, 1, 0), 90.0, 3.0, "inner")
        G.add(f"REQ-04.{tag}.apex_above_centre", apex, "in",
              (SPEC["win_apex_above_centre"] - SPEC["win_tol"], SPEC["win_apex_above_centre"] + SPEC["win_tol"]),
              assumes=ASSUMES["REQ-04"], note="gable apex: 7.0 beyond the circle's +Z edge = 14.0 above the centre")
        for ang in (60.0, 120.0):
            rr = _ray(one, org, (1, 0, 0), (0, 1, 0), ang, 3.0, "inner")
            a = math.radians(ang)
            facts[f"REQ-04.{tag}.roof_ray_{ang:g}"] = _res(rr) | {
                "design_mm": SPEC["win_apex_above_centre"] / (abs(math.cos(a)) + math.sin(a))}
        # through along X: no material on the axis between the two wall faces
        thru = _ray(one, (65.0, yc, zc), (0, 1, 0), (1, 0, 0), 0.0, 0.0, "outer", r_max=1.9)
        facts[f"REQ-04.{tag}.axis_x63_67_clear"] = _res(thru)
    front = [f for f in _planar_faces(one, (0, 0, 1)) if abs(f["at"] - env["max_z"].measured) < 1e-4]
    facts["front_end_faces"] = front
    G.add("REQ-04.w4.front_end_closed", Result("planar_faces_at_max_z", len(front), "count"), "==",
          SPEC["front_end_faces"], assumes=ASSUMES["REQ-04"],
          note="one front end face when window 4 and its gable close inside the wall")
    collars = sum(1 for f in one.faces() if f.geom_type.name == "CYLINDER" and f.radius > 7.5)
    G.add("REQ-04.no_collar", Result("cyl_faces_larger_than_window", collars, "count"), "==", SPEC["collar_faces"],
          assumes=ASSUMES["REQ-04"])

    # U-03 (a) on the parts as placed in the check assembly
    if asm_path is not None and asm_path.exists():
        asm = read_step(asm_path)
        kids = _children(asm)
        facts["assembly_labels"] = sorted(kids)
        bh = kids.get(PART)
        plate = kids.get(LABELS["plate"])
        if bh is None or plate is None:
            G.add("U-03.contact", inconclusive("clearance", "mm", "bulkhead or plate missing"), "==", 0.0)
        else:
            G.add("U-03.plate.clearance", clearance(bh, plate), "==", SPEC["contact"], assumes=ASSUMES["U-03"],
                  note="designed contact: rail underside on the plate's top face")
            G.add("U-03.plate.interference", _safe(common_volume, "common_volume", "mm3", bh, plate), "<=",
                  SPEC["interference"], assumes=ASSUMES["U-03"])
            pcen = _safe(bore_census, "bore_census", "count", plate)
            bcen = _safe(bore_census, "bore_census", "count", bh)
            bb = bcen.detail.get("bores", []) if isinstance(bcen, Result) and bcen.detail else []
            for x, z in SPEC["base_bores"]:
                b = _find_bore(bb, x, z, -1e-3, 12.0)
                pt = None if b is None else _bore_axis_point(b, PLATE_PROBE_Y)
                if pt is None:
                    res = inconclusive("bore_axis_offset", "mm", "bulkhead bore not found in the assembly")
                    G.add(f"U-03.coax.x{x:g}_z{z:g}", res, "<=", SPEC["coax"], assumes=ASSUMES["U-03"])
                    G.add(f"REQ-01.plate_coax.x{x:g}_z{z:g}", res, "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-01"])
                    continue
                pl = _unpack(_safe(locate_bore, "locate_bore", "mm", pcen, pt, (0, 1, 0)))
                note = f"plate hole located at the bulkhead bore's measured axis point {tuple(round(v, 4) for v in pt)}"
                G.add(f"U-03.coax.x{x:g}_z{z:g}", pl["offset"], "<=", SPEC["coax"], assumes=ASSUMES["U-03"], note=note)
                G.add(f"REQ-01.plate_coax.x{x:g}_z{z:g}", pl["offset"], "<=", SPEC["offset_max"],
                      assumes=ASSUMES["REQ-01"], note=note)
                facts[f"U-03.plate_hole.x{x:g}_z{z:g}"] = {"diameter": pl["diameter"].measured,
                                                         "length": pl["length"].measured,
                                                         "through": pl["through"].measured,
                                                         "start": pl["diameter"].at}
            for key in NEIGHBOURS:
                s = kids.get(LABELS[key])
                if s is None:
                    G.add(f"U-03.{key}.clearance", inconclusive("clearance", "mm", "missing in the assembly"), ">=",
                          SPEC["neighbour_gap"])
                    continue
                cl = clearance(bh, s)
                G.add(f"U-03.{key}.clearance", cl, ">=", SPEC["neighbour_gap"], assumes=ASSUMES["U-03"])
                G.add(f"REQ-05.{key}.clearance", cl, ">=", SPEC["neighbour_gap"], assumes=ASSUMES["REQ-05"])
                if key == "h11":
                    G.fixed("U-03.h11.interference", INCONCLUSIVE, "<= 0 mm3",
                            "OD-H11 unsound (brep_valid 0, OD-C04 A-14): boolean INCONCLUSIVE by the U-03 row; "
                            "gated on distance", unit="mm3", assumes=ASSUMES["U-03"])
                else:
                    G.add(f"U-03.{key}.interference", _safe(common_volume, "common_volume", "mm3", bh, s), "<=",
                          SPEC["interference"], assumes=ASSUMES["U-03"])
            bx = kids.get(LABELS["box"])
            if bx is None:
                G.add("U-03.c05_box.clearance", inconclusive("clearance", "mm", "missing"), ">=", SPEC["box_gap"])
            else:
                G.add("U-03.c05_box.clearance", clearance(bh, bx), ">=", SPEC["box_gap"], assumes=ASSUMES["U-03"])
            facts["assembly_bulkhead_volume_mm3"] = mass_properties(bh, SPEC["density"])["volume"].measured
    else:
        G.add("U-03.contact", inconclusive("clearance", "mm", "no assembly file"), "==", 0.0)
    G.fixed("U-03(b)", "N/A", "N/A", "U-03 (b) N/A by the spec row")

    # U-04: part and assembly round trip against the build
    try:
        import build_od_c02_bulkhead_v02 as B
        p = B.Params(**variant)
        built = B.build_bulkhead(p)
        rt = compare_step(built, step_path)
        for k, v in rt.items():
            if k == "volume_delta":
                G.add("U-04.part.volume_delta", v, "in", (0.0, 0.0))
            elif k == "faces_delta":
                G.add("U-04.part.faces_delta", v, "==", 0)
            elif k == "solids":
                G.add("U-04.part.solids", v, "==", 1)
            elif k == "valid_after":
                G.add("U-04.part.valid_after", v, "==", 1)
            else:
                facts[f"U-04.part.{k}"] = _res(v)
        if asm_path is not None and asm_path.exists():
            ba = B.build_assembly(p)["assembly"]
            ra = compare_step(ba, asm_path)
            for k, v in ra.items():
                facts[f"U-04.assembly.{k}"] = _res(v) | {"detail": {kk: vv for kk, vv in (v.detail or {}).items()
                                                                     if not isinstance(vv, (list, dict))}}
            G.add("U-04.assembly.solids", ra["solids"], "==", 8)
            G.add("U-04.assembly.faces_delta", ra["faces_delta"], "==", 0)
            G.add("U-04.assembly.labels", ra["labels"], "==", 1)
            kb = _children(ba)
            kr = _children(read_step(asm_path))
            for lab, sb in kb.items():
                sr = kr.get(lab)
                if sr is None:
                    G.add(f"U-04.assembly.{lab}.volume_delta", inconclusive("volume_delta", "mm3", "label lost"),
                          "in", (0.0, 0.0))
                    continue
                dv = abs(mass_properties(sr, SPEC["density"])["volume"].measured
                         - mass_properties(sb, SPEC["density"])["volume"].measured)
                if lab == LABELS["h11"]:
                    G.fixed(f"U-04.assembly.{lab}.volume_delta", INCONCLUSIVE, "in [0, 0] mm3",
                            "OD-H11 unsound (brep_valid 0, OD-C04 A-14): its volume changes on the write; "
                            "INCONCLUSIVE by the U-03 row's note", measured=dv, unit="mm3")
                else:
                    G.add(f"U-04.assembly.{lab}.volume_delta", Result("volume_delta", dv, "mm3"), "in", (0.0, 0.0))
    except Exception as exc:  # noqa: BLE001
        G.add("U-04.part", inconclusive("compare_step", "", f"{type(exc).__name__}: {exc}"), "==", 0)
        facts["U-04.traceback"] = traceback.format_exc()

    # D-01a, D-01b, D-06a, U-06 (Soft)
    mw = _safe(min_wall, "min_wall", "mm", one, spacing=SPACING)
    G.add("D-01a", mw, ">=", SPEC["wall_floor"])
    G.add("D-01b", mw, ">=", SPEC["wall_struct"])
    G.add("D-06a", mw, ">=", SPEC["min_feature"])
    ww = _safe(min_wall_wide, "min_wall_wide", "mm", one, spacing=SPACING)
    G.add("U-06(Soft)", ww, ">=", SPEC["wall_wide"])

    # D-03a: census outside the named exception (the six bores refilled by position), the whole part apart
    exc_bores = [b for b in bores if abs(abs(b["axis_dir"][1]) - 1.0) < 1e-6 and abs(b["diameter"] - 4.0) < 0.3]
    facts["D-03a.exception_bores"] = len(exc_bores)
    try:
        filled = _refilled(one, exc_bores)
        nf = len(filled.faces())
        facts["D-03a.refilled_faces"] = nf
        facts["D-03a.refilled_solids"] = len(filled.solids())
        if len(exc_bores) != 6 or nf != SPEC["refilled_faces"] or len(filled.solids()) != 1:
            oh_out = inconclusive("overhang_census", "deg", f"refill not as planned: {len(exc_bores)} bores, "
                                  f"{nf} faces, {len(filled.solids())} solids")
        else:
            oh_out = _safe(overhang_census, "overhang_census", "deg", filled, build_dir=SPEC["build_dir"],
                           spacing=SPACING)
    except Exception as exc:  # noqa: BLE001
        oh_out = inconclusive("overhang_census", "deg", f"{type(exc).__name__}: {exc}")
    G.add("D-03a", oh_out, ">=", SPEC["overhang_deg"], assumes=ASSUMES["D-03a"],
          note="overhang_census outside the named exception: the six insert bores refilled by position "
               "(plan amendment v02 section 2); the whole-part census and the crowns in facts")
    oh_all = _safe(overhang_census, "overhang_census", "deg", one, build_dir=SPEC["build_dir"], spacing=SPACING)
    facts["D-03a.whole_part_census"] = _res(oh_all) | {"detail": oh_all.detail}
    split = _down_face_split(one, env["min_z"].measured)
    facts["down_faces"] = split
    regions: dict = {}
    for r in split:
        regions.setdefault(r["region"], []).append(r["least_deg"])
    facts["down_face_regions_least_deg"] = {k: {"faces": len(v), "least_deg": min(v)} for k, v in regions.items()}

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
        ang = rec.get("stl", {}).get("angular_tolerance", None)
        G.add("U-07.angular_tolerance", Result("stl_angular_tolerance", ang, "rad") if ang is not None
              else inconclusive("stl_angular_tolerance", "rad", "no build record"), "<=", SPEC["stl_ang_max"])
        scratch.mkdir(parents=True, exist_ok=True)
        w = _safe(write_stl, "write_stl", "mm", one, scratch / "remesh_check.stl", tolerance=SPEC["stl_tol"],
                  angular_tolerance=ang or 0.2)
        sag = w.checks["max_sagitta"] if hasattr(w, "checks") else w
        G.add("U-07.max_sagitta", sag, "<=", SPEC["stl_tol"],
              note="re-meshed from the re-imported STEP at the build's settings")
        facts["remesh_triangles"] = getattr(w, "detail", {}).get("triangles") if hasattr(w, "detail") else None
    else:
        G.add("U-07", inconclusive("mesh", "mm", "no STL"), "<=", SPEC["stl_tol"])

    # by the rows
    G.fixed("U-08", "N/A", "N/A", "no threads (N/A by its row)")
    G.fixed("D-04a", "N/A", "N/A", "no clearance hole on this part; the plate's holes are the clearance holes "
            "(N/A by its row, A-01)")
    G.fixed("D-07", "N/A", "N/A", "no fit-critical bores (N/A by its row)")
    G.fixed("E-06", INCONCLUSIVE, "reviewer", "reviewer row; designer's reading in the REPORT (one solid; both "
            "rails span the wall's whole length; no free-standing boss)")
    G.fixed("REQ-09(Soft)", INCONCLUSIVE, "bench", "Soft bench gate: not geometric, answered by the first print",
            assumes=("A-11",))
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
    ap.add_argument("--scratch", default="01_CAD/sweep_v02/_mesh_check")
    ap.add_argument("--variant", default="{}")
    a = ap.parse_args()

    def rel(s):
        if s is None:
            return None
        q = Path(s)
        return q if q.is_absolute() else WS / q
    out = check(rel(a.step), rel(a.asm), rel(a.stl), rel(a.record), json.loads(a.variant), rel(a.scratch))
    rel(a.out).write_text(json.dumps(out, indent=1, default=str))
    for r in out["gates"]:
        print(f"{r['gate']:<48} {r['status']:<13} {r.get('measured')!s:<22} {r.get('required')!s:<28} "
              f"{r.get('margin')!s:<12} {r.get('reason', '')[:90]}")


if __name__ == "__main__":
    main()
