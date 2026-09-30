"""Checks for od_c02_bulkhead v01 (job 20260930-od-c02-bulkhead, concept C1, spec 1.0).

Written before the build (PLAYBOOK D3). Every predicate measures the re-imported
STEP files with tools.core / tools.measure and compares through tools.result.gate
with the GATES.md section 0 band. Thresholds come from DESIGN_SPEC.md 1.0 section 5
only (the SPEC table cites the row of each value). Any exception or missing value
gives INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c02_bulkhead.py \
        --step 02_STEP_STL/od_c02_bulkhead_C1_v01.step \
        --asm 02_STEP_STL/od_c02_assembly_C1_v01.step \
        --stl 02_STEP_STL/od_c02_bulkhead_C1_v01.stl \
        --out 01_CAD/check_od_c02_bulkhead_v01.json [--variant '{...}'] [--light]
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

from tools.core import common_volume, compare_step, read_step, validity, write_stl  # noqa: E402
from tools.core.step import file_sha256  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census, locate_bore,  # noqa: E402
                           mass_properties, mesh_census, min_wall, min_wall_wide, overhang_census,
                           radial_extent)
from tools.result import INCONCLUSIVE, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.0) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "count": 0, "bool": 0}
SPEC = {
    # U-02: 14.0 x 215.0 x 210.0 each +-0.1; position x 59 .. 73, y 0 .. 215, z -240 .. -30
    "size": {"size_x": 14.0, "size_y": 215.0, "size_z": 210.0}, "size_tol": 0.1,
    "position": {"min_x": 59.0, "max_x": 73.0, "min_y": 0.0, "max_y": 215.0, "min_z": -240.0, "max_z": -30.0},
    # D-02 (A-08): K1C 220 x 220 x 250; standing on z -240: x and y on the bed, z tall
    "bed": {"size_x": 220.0, "size_y": 220.0, "size_z": 250.0},
    # D-01a, D-01b, D-06a, U-06 (Soft)
    "wall_floor": 0.8, "wall_struct": 1.75, "min_feature": 1.0, "wall_wide": 2.0,
    # J-05, D-05a
    "wall_insert": 3.0, "boss_across": 8.0,
    # D-03a: >= 45 deg, build direction +Z (A-10); D-03b span <= 5
    "overhang_deg": 45.0, "build_dir": (0.0, 0.0, 1.0), "bridge_span": 5.0,
    # U-07
    "stl_tol": 0.01, "stl_ang_max": 4.0 * math.acos(1.0 - 0.01 / 6.0),
    # U-03 (a): contact 0, interference <= 0, coaxial <= 0.10, neighbours >= 3.0, carrier box >= 4.0
    "contact": 0.0, "interference": 0.0, "coax": 0.10, "neighbour_gap": 3.0, "box_gap": 4.0,
    # REQ-01, D-04a
    "holes_z": (-45.0, -105.0, -165.0, -225.0), "hole_x": 65.0, "hole_d": 3.4, "hole_tol": 0.1,
    "hole_min": 3.25, "cbore_d": 6.5, "cbore_tol": 0.1, "cbore_depth": 8.0, "cbore_depth_tol": 0.1,
    "cbore_top_y": 12.0, "offset_max": 0.10,
    # REQ-02
    "wet_face_x": 63.0, "elec_face_x": 67.0, "face_tol": 0.10, "rail_wet_x": 59.0, "face_ys": (100.0, 200.0),
    # REQ-03
    "rail_under_y": 0.0, "rail_under_tol": 0.10, "rail_top_y": 12.0, "rail_top_tol": 0.1, "rail_under_faces": 1,
    # REQ-04
    "windows": ((150.0, -200.0), (150.0, -130.0), (150.0, -60.0), (60.0, -40.0)), "win_d": 14.0,
    "win_tol": 0.1, "win_apex_above_centre": 14.0, "collar_od": 18.0, "front_end_faces": 1,
    # REQ-05, REQ-06, REQ-08
    "keepout_min_x": 59.0, "top_y": 215.0, "top_tol": 0.1, "max_x": 73.0, "elec_face_max": 70.0,
    # REQ-07, D-05b
    "inserts": ((67.5, -60.0), (67.5, -210.0)), "insert_d": 4.0, "insert_tol": 0.05, "insert_depth": 6.0,
    "insert_depth_tol": 0.1, "insert_min_depth": 5.7,
    # U-05 census (plan section 3): 10 bores (4 x 3.4, 4 x 6.5, 2 x 4.0)
    "bores": 10, "bore_groups": {3.4: 4, 6.5: 4, 4.0: 2}, "window_half_cyl": 4, "collar_half_cyl": 4,
    "density": 1070.0,
}
ASSUMES = {"U-03": ("A-01", "A-02"), "REQ-01": ("A-01", "A-03"), "REQ-02": ("A-01",), "REQ-03": ("A-01",),
           "REQ-04": ("A-04",), "REQ-05": ("A-02",), "REQ-06": ("A-06",), "REQ-07": ("A-05",),
           "REQ-08": ("A-07",), "D-02": ("A-08",), "D-03a": ("A-10",), "D-05a": ("A-05",), "D-05b": ("A-05",)}
SPACING = 0.7   # plan section 2 and the brief: the tools refuse the large faces at the default spacing
PART = "od_c02_bulkhead"
LABELS = {"plate": "od_c01_frame", "c03": "od_c03_cradle", "h01": "od_h01_pump", "c04": "od_c04_mount",
          "h11": "od_h11_thermoblock", "g01": "od_g01_housing", "box": "od_c05_foot_reference_A02"}
NEIGHBOURS = ("c03", "h01", "c04", "h11", "g01")


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
    """The feature a downward face belongs to, by position (plan section 3)."""
    cx, cz = 0.5 * (bb.min.X + bb.max.X), 0.5 * (bb.min.Z + bb.max.Z)
    if kind == "cylinder" and r is not None:
        if abs(r - 1.7) < 0.05 and abs(cx - 65.0) < 2.5:
            return "exception: hole 3.4 crown"
        if abs(r - 3.25) < 0.05 and abs(cx - 65.0) < 4.0:
            return "exception: counterbore 6.5 crown"
        if abs(r - 2.0) < 0.05 and abs(cx - 67.5) < 3.0 and bb.min.Y > 205.0:
            return "exception: insert bore 4.0 crown"
        if abs(r - 9.0) < 0.05 and bb.max.X <= 63.001:
            return "collar outer round part"
        if abs(r - 7.0) < 0.05:
            return "window round part"
    if kind == "plane":
        if bb.min.X >= 66.999 and bb.max.X <= 72.001 and abs(bb.max.Z - bb.min.Z) < 1e-3:
            return "rib underside"
        if bb.max.X <= 68.001 and bb.min.X >= 59.999:
            return "window roof or collar"
    return "other"


def check(step_path: Path, asm_path: Path | None, stl_path: Path | None, variant: dict, light: bool) -> dict:
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

    # REQ-03 rail underside and top: planar faces and rays along +-Y
    under = [f for f in _planar_faces(one, (0, -1, 0)) if abs(f["at"] + env["min_y"].measured) < 1e-4]
    facts["rail_underside_faces"] = under
    G.add("REQ-03.underside_faces", Result("planar_faces_at_min_y", len(under), "count"), "==",
          SPEC["rail_under_faces"], assumes=ASSUMES["REQ-03"])
    if under:
        u = under[0]
        G.add("REQ-03.underside_y", Result("underside_y", -u["at"], "mm", at=u["min"]), "in",
              (SPEC["rail_under_y"] - SPEC["rail_under_tol"], SPEC["rail_under_y"] + SPEC["rail_under_tol"]),
              assumes=ASSUMES["REQ-03"])
        for k, v, i, which in (("x_from", 59.0, 0, "min"), ("x_to", 70.0, 0, "max"), ("z_from", -240.0, 2, "min"),
                               ("z_to", -30.0, 2, "max")):
            G.add(f"REQ-03.underside_{k}", Result("underside_extent", u[which][i], "mm"), "in",
                  (v - SPEC["rail_under_tol"], v + SPEC["rail_under_tol"]), assumes=ASSUMES["REQ-03"])
    for x in (60.0, 68.5):
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
        G.add("U-05.bores", fc["bores"], "==", SPEC["bores"])
        G.add("feature_census.bores", fc["bores"], "==", SPEC["bores"])
    else:
        G.add("U-05.bores", fc, "==", SPEC["bores"])
    bores = census.detail.get("bores", []) if isinstance(census, Result) else []
    facts["bores"] = bores
    for d, n in SPEC["bore_groups"].items():
        got = sum(1 for b in bores if abs(b.get("diameter", 0) - d) < 0.3)
        G.add(f"U-05.bores_d{d:g}", Result("bores_by_diameter", got, "count"), "==", n)
    cyl = [(f, f.radius) for f in one.faces() if f.geom_type.name == "CYLINDER"]
    wh = sum(1 for f, r in cyl if abs(r - 7.0) < 1e-3)
    ch = sum(1 for f, r in cyl if abs(r - 9.0) < 1e-3)
    G.add("U-05.window_half_cylinders_r7", Result("cyl_faces_r7", wh, "count"), "==", SPEC["window_half_cyl"])
    G.add("U-05.collar_half_cylinders_r9", Result("cyl_faces_r9", ch, "count"), "==", SPEC["collar_half_cyl"])
    G.add("feature_census.window_half_cylinders_r7", Result("cyl_faces_r7", wh, "count"), "==", SPEC["window_half_cyl"])
    G.add("feature_census.collar_half_cylinders_r9", Result("cyl_faces_r9", ch, "count"), "==", SPEC["collar_half_cyl"])

    # REQ-01, D-04a: holes and counterbores
    hole_axes = {}
    for z in SPEC["holes_z"]:
        tag = f"z{z:g}"
        loc = _safe(locate_bore, "locate_bore", "mm", census, (SPEC["hole_x"], 2.0, z), (0, 1, 0))
        if isinstance(loc, Result):
            loc = {"diameter": loc, "offset": loc, "length": loc, "through": loc}
        hole_axes[z] = loc["diameter"].at
        G.add(f"REQ-01.hole.{tag}.diameter", loc["diameter"], "in",
              (SPEC["hole_d"] - SPEC["hole_tol"], SPEC["hole_d"] + SPEC["hole_tol"]), assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.hole.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.hole.{tag}.through", loc["through"], "==", 1, assumes=ASSUMES["REQ-01"])
        G.add(f"D-04a.{tag}.diameter", loc["diameter"], ">=", SPEC["hole_min"])
        cb = _safe(locate_bore, "locate_bore", "mm", census, (SPEC["hole_x"], 8.0, z), (0, 1, 0))
        if isinstance(cb, Result):
            cb = {"diameter": cb, "offset": cb, "length": cb, "through": cb}
        G.add(f"REQ-01.cbore.{tag}.diameter", cb["diameter"], "in",
              (SPEC["cbore_d"] - SPEC["cbore_tol"], SPEC["cbore_d"] + SPEC["cbore_tol"]), assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.cbore.{tag}.depth", cb["length"], "in",
              (SPEC["cbore_depth"] - SPEC["cbore_depth_tol"], SPEC["cbore_depth"] + SPEC["cbore_depth_tol"]),
              assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.cbore.{tag}.offset", cb["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-01"])
        # what stands over the counterbore's mouth: material on the axis above y 12 (a finding for P2)
        above = _ray(one, (SPEC["hole_x"] - 0.0, 12.5, z), (0, 0, 1), (0, 1, 0), 0.0, 0.0, "outer", r_max=210.0)
        facts[f"material_above_cbore_{tag}"] = _res(above) | {"material": above.detail.get("material")}

    # REQ-07, D-05b, D-05a, J-05: insert bores
    for x, z in SPEC["inserts"]:
        tag = f"x{x:g}_z{z:g}"
        loc = _safe(locate_bore, "locate_bore", "mm", census, (x, 212.0, z), (0, -1, 0))
        if isinstance(loc, Result):
            loc = {"diameter": loc, "offset": loc, "length": loc, "through": loc}
        lim = (SPEC["insert_d"] - SPEC["insert_tol"], SPEC["insert_d"] + SPEC["insert_tol"])
        dlim = (SPEC["insert_depth"] - SPEC["insert_depth_tol"], SPEC["insert_depth"] + SPEC["insert_depth_tol"])
        G.add(f"REQ-07.{tag}.diameter", loc["diameter"], "in", lim, assumes=ASSUMES["REQ-07"])
        G.add(f"REQ-07.{tag}.depth", loc["length"], "in", dlim, assumes=ASSUMES["REQ-07"])
        G.add(f"REQ-07.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-07"])
        G.add(f"REQ-07.{tag}.blind", loc["through"], "==", 0, assumes=ASSUMES["REQ-07"])
        G.add(f"D-05b.{tag}.diameter", loc["diameter"], "in", lim, assumes=ASSUMES["D-05b"])
        G.add(f"D-05b.{tag}.depth", loc["length"], "in", dlim, assumes=ASSUMES["D-05b"])
        G.add(f"D-05b.{tag}.depth_min", loc["length"], ">=", SPEC["insert_min_depth"], assumes=ASSUMES["D-05b"])
        rp = _ray(one, (x, 215.0, z), (0, -1, 0), (1, 0, 0), 0.0, 3.0, "outer", r_max=12.0)
        rn = _ray(one, (x, 215.0, z), (0, -1, 0), (1, 0, 0), 180.0, 3.0, "outer", r_max=12.0)
        if rp.measured is not None and rn.measured is not None:
            across = Result("boss_across_x", rp.measured + rn.measured, "mm", at=[rp.at, rn.at])
        else:
            across = inconclusive("boss_across_x", "mm", f"{rp.reason} {rn.reason}".strip())
        G.add(f"D-05a.{tag}.across_x", across, ">=", SPEC["boss_across"], assumes=ASSUMES["D-05a"])
        dm = loc["diameter"].measured
        for side, rr in (("elec", rp), ("wet", rn)):
            if rr.measured is not None and dm is not None:
                w = Result("wall_around_insert", rr.measured - dm / 2.0, "mm", at=rr.at)
            else:
                w = inconclusive("wall_around_insert", "mm", rr.reason or "no diameter")
            G.add(f"J-05.{tag}.{side}", w, ">=", SPEC["wall_insert"])

    # REQ-04 windows: round part (three rays on the lower half), apex, roof, collar, front end
    for i, (yc, zc) in enumerate(SPEC["windows"], start=1):
        tag = f"w{i}_y{yc:g}_z{zc:g}"
        org = (60.0, yc, zc)
        pts, reasons = [], []
        for ang in (200.0, 270.0, 340.0):
            r = _ray(one, org, (1, 0, 0), (0, 1, 0), ang, 5.0, "inner")
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
        apex = _ray(one, org, (1, 0, 0), (0, 1, 0), 90.0, 5.0, "inner")
        G.add(f"REQ-04.{tag}.apex_above_centre", apex, "in",
              (SPEC["win_apex_above_centre"] - SPEC["win_tol"], SPEC["win_apex_above_centre"] + SPEC["win_tol"]),
              assumes=ASSUMES["REQ-04"], note="gable apex: 7.0 above the circle's top = 14.0 above the centre")
        for ang in (60.0, 120.0):
            rr = _ray(one, org, (1, 0, 0), (0, 1, 0), ang, 5.0, "inner")
            a = math.radians(ang)
            facts[f"REQ-04.{tag}.roof_ray_{ang:g}"] = _res(rr) | {
                "design_mm": SPEC["win_apex_above_centre"] / (abs(math.cos(a)) + math.sin(a))}
        col = _ray(one, org, (1, 0, 0), (0, 1, 0), 270.0, 2.0, "outer")
        G.add(f"REQ-04.{tag}.collar_od", Result("collar_od", None if col.measured is None else 2 * col.measured,
                                                 "mm", at=col.at, status=col.status, reason=col.reason),
              "in", (SPEC["collar_od"] - SPEC["win_tol"], SPEC["collar_od"] + SPEC["win_tol"]),
              assumes=ASSUMES["REQ-04"])
        # the electric-side mouth: first material above and below the axis at x 69.5 (in the rib zone)
        for ang in (90.0, 270.0):
            m = _ray(one, org, (1, 0, 0), (0, 1, 0), ang, 9.5, "inner")
            facts[f"REQ-04.{tag}.mouth_x69.5_{ang:g}"] = _res(m)
    front = [f for f in _planar_faces(one, (0, 0, 1)) if abs(f["at"] - env["max_z"].measured) < 1e-4]
    facts["front_end_faces"] = front
    G.add("REQ-04.w4.front_end_closed", Result("planar_faces_at_max_z", len(front), "count"), "==",
          SPEC["front_end_faces"], assumes=ASSUMES["REQ-04"],
          note="one front end face when window 4 and its gable close inside the wall; two when they run out")

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
            for z in SPEC["holes_z"]:
                bl = _safe(locate_bore, "locate_bore", "mm", bcen, (SPEC["hole_x"], 2.0, z), (0, 1, 0))
                if isinstance(bl, Result):
                    G.add(f"U-03.coax.z{z:g}", bl, "<=", SPEC["coax"], assumes=ASSUMES["U-03"])
                    continue
                d = bl["diameter"].detail if bl["diameter"].detail else {}
                start = bl["diameter"].at or (SPEC["hole_x"], 0.0, z)
                pl = _safe(locate_bore, "locate_bore", "mm", pcen, tuple(start), (0, 1, 0))
                res = pl if isinstance(pl, Result) else pl["offset"]
                G.add(f"U-03.coax.z{z:g}", res, "<=", SPEC["coax"], assumes=ASSUMES["U-03"],
                      note=f"plate insert axis to the bulkhead hole's measured axis point {start}; {d.get('axis', '')}")
            for key in NEIGHBOURS:
                s = kids.get(LABELS[key])
                if s is None:
                    G.add(f"U-03.{key}.clearance", inconclusive("clearance", "mm", "missing in the assembly"), ">=",
                          SPEC["neighbour_gap"])
                    continue
                G.add(f"U-03.{key}.clearance", clearance(bh, s), ">=", SPEC["neighbour_gap"], assumes=ASSUMES["U-03"])
                G.add(f"REQ-05.{key}.clearance", clearance(bh, s), ">=", SPEC["neighbour_gap"],
                      assumes=ASSUMES["REQ-05"])
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
            # the bulkhead in the assembly is the part file's bulkhead
            facts["assembly_bulkhead_volume_mm3"] = mass_properties(bh, SPEC["density"])["volume"].measured
    else:
        G.add("U-03.contact", inconclusive("clearance", "mm", "no assembly file"), "==", 0.0)
    G.fixed("U-03(b)", "N/A", "N/A", "U-03 (b) N/A by the spec row")

    # U-04: part and assembly round trip against the build
    try:
        import build_od_c02_bulkhead as B
        p = B.Params(**variant)
        built = B.build_bulkhead(p)
        rt = compare_step(built, step_path)
        for k, v in rt.items():
            if k == "volume_delta":
                G.add("U-04.part.volume_delta", v, "in", (0.0, 0.0))
            elif k == "faces_delta":
                G.add("U-04.part.faces_delta", v, "==", 0)
            elif k in ("solids",):
                G.add("U-04.part.solids", v, "==", 1)
            elif k == "valid_after":
                G.add("U-04.part.valid_after", v, "==", 1)
            else:
                facts[f"U-04.part.{k}"] = _res(v)
        if asm_path is not None and asm_path.exists() and not light:
            ba = B.build_assembly(p, built)["assembly"]
            ra = compare_step(ba, asm_path)
            for k, v in ra.items():
                facts[f"U-04.assembly.{k}"] = _res(v) | {"detail": {kk: vv for kk, vv in (v.detail or {}).items()
                                                                     if not isinstance(vv, (list, dict))}}
            G.add("U-04.assembly.solids", ra["solids"], "==", 8)
            G.add("U-04.assembly.faces_delta", ra["faces_delta"], "==", 0)
            G.add("U-04.assembly.labels", ra["labels"], "==", 1)
            # per part: each labelled solid's volume in the file against the built one
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
    if not light:
        mw = _safe(min_wall, "min_wall", "mm", one, spacing=SPACING)
        G.add("D-01a", mw, ">=", SPEC["wall_floor"])
        G.add("D-01b", mw, ">=", SPEC["wall_struct"])
        G.add("D-06a", mw, ">=", SPEC["min_feature"])
        ww = _safe(min_wall_wide, "min_wall_wide", "mm", one, spacing=SPACING)
        G.add("U-06(Soft)", ww, ">=", SPEC["wall_wide"])
        # D-03a: the census over the whole part, and the faces split by region (diagnostic)
        oh = _safe(overhang_census, "overhang_census", "deg", one, build_dir=SPEC["build_dir"], spacing=SPACING)
        G.add("D-03a", oh, ">=", SPEC["overhang_deg"], assumes=ASSUMES["D-03a"],
              note="census over every face; the named-exception crowns are split out in facts.down_faces")
        split = _down_face_split(one, env["min_z"].measured)
        facts["down_faces"] = split
        regions: dict = {}
        for r in split:
            regions.setdefault(r["region"], []).append(r["least_deg"])
        facts["down_face_regions_least_deg"] = {k: {"faces": len(v), "least_deg": min(v)} for k, v in regions.items()}
        outside = [r for r in split if not r["region"].startswith("exception")]
        facts["least_outside_named_exception_deg"] = min((r["least_deg"] for r in outside), default=90.0)
        facts["least_outside_named_exception_at"] = min(outside, key=lambda r: r["least_deg"]) if outside else None
        ribs = [r for r in split if r["region"] == "rib underside"]
        facts["rib_undersides"] = ribs
        span = max((r["max"][1] - r["min"][1] for r in ribs), default=None)
        G.add("D-03b.rib_underside_span_y",
              Result("unsupported_span", span, "mm", detail={"basis": "rib underside faces (0 deg, build +Z) "
                                                             "between the base rail and the top rail, B-rep face box"})
              if span is not None else inconclusive("unsupported_span", "mm", "no rib underside found"),
              "<=", SPEC["bridge_span"], note="reviewer row; designer's reading from the B-rep and the sections")

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
        rec = json.loads((HERE / "build_record_v01.json").read_text()) if (HERE / "build_record_v01.json").exists() else {}
        ang = rec.get("stl", {}).get("angular_tolerance", None) or rec.get("params", {}).get("stl_ang")
        G.add("U-07.angular_tolerance", Result("stl_angular_tolerance", ang, "rad") if ang is not None
              else inconclusive("stl_angular_tolerance", "rad", "no build record"), "<=", SPEC["stl_ang_max"])
        scratch = HERE / "sweep_v01" / "_mesh_check"
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
    G.fixed("D-07", "N/A", "N/A", "no fit-critical bores (N/A by its row)")
    G.fixed("E-06", INCONCLUSIVE, "reviewer", "reviewer row; designer's reading in the REPORT (one solid; collars "
            "and ribs fused to the wall; rails full length)")
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
    ap.add_argument("--out", required=True)
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--light", action="store_true")
    a = ap.parse_args()

    def rel(s):
        if s is None:
            return None
        q = Path(s)
        return q if q.is_absolute() else WS / q
    out = check(rel(a.step), rel(a.asm), rel(a.stl), json.loads(a.variant), a.light)
    rel(a.out).write_text(json.dumps(out, indent=1, default=str))
    for r in out["gates"]:
        print(f"{r['gate']:<48} {r['status']:<13} {r.get('measured')!s:<22} {r.get('required')!s:<28} "
              f"{r.get('margin')!s:<12} {r.get('reason', '')[:90]}")


if __name__ == "__main__":
    main()
