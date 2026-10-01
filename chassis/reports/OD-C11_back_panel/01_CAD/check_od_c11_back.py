"""Checks for od_c11_back v01 (job 20261001-od-c11-back-panel, concept C1, spec 1.0).

Written before the build (PLAYBOOK D3), from 01_CAD/DESIGN_PLAN.md section 6. Every
predicate measures the re-imported STEP files with tools.core / tools.measure and
compares through tools.result.gate with the GATES.md section 0 band of the result's
unit. Thresholds come from DESIGN_SPEC.md 1.0 section 5 only (the SPEC table cites the
row of each value). Any exception or missing value gives INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c11_back.py \
        --step 02_STEP_STL/od_c11_back_C1_v01.step \
        --asm 02_STEP_STL/od_c11_assembly_C1_v01.step \
        --stl 02_STEP_STL/od_c11_back_C1_v01.stl \
        --record 01_CAD/build_record_v01.json \
        --out 01_CAD/check_od_c11_back_v01.json [--variant '{...}'] [--quick]
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
from build123d import Align, Box, Cylinder, Face, Location, Plane, Pos, Vertex  # noqa: E402

from tools.core import common_volume, compare_step, read_step, validity, write_stl  # noqa: E402
from tools.core.step import file_sha256  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census, flat_ceiling_spans,  # noqa: E402
                           locate_bore, mass_properties, mesh_census, min_wall, min_wall_wide,
                           overhang_census, radial_extent)
from tools.result import INCONCLUSIVE, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.0) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "rad": 0.00002}   # every other unit: 0
SPEC = {
    # U-02: 232.0 x 215.0 x 19.0 each +-0.1; position x +-116.0, y 0 .. 215.0, z -302.0 .. -283.0
    "size": {"size_x": 232.0, "size_y": 215.0, "size_z": 19.0}, "size_tol": 0.1,
    "position": {"min_x": -116.0, "max_x": 116.0, "min_y": 0.0, "max_y": 215.0, "min_z": -302.0, "max_z": -283.0},
    # D-02 (A-09): Kobra Max 3 420 x 420 x 500; lying on the outer face: x and y on the bed, z tall
    "bed": {"size_x": 420.0, "size_y": 420.0, "size_z": 500.0},
    # D-01a, D-01b, D-06a, U-06 (Soft)
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wall_wide": 2.0,
    # J-05, D-05a
    "wall_insert": 3.0, "boss_across": 8.0,
    # D-03a >= 45 deg, build +Z (A-08); D-03b span <= 5
    "overhang_deg": 45.0, "build_dir": (0.0, 0.0, 1.0), "bridge_span": 5.0,
    # U-07: tol 0.01, angular <= 4 acos(1 - 0.01/R_max), R_max = 6.0 (the pass-throughs)
    "stl_tol": 0.01, "stl_ang_max": 4.0 * math.acos(1.0 - 0.01 / 6.0),
    # U-03 (a)
    "contact": 0.0, "interference": 0.0, "edge_gap": 0.5, "hole_gap": 6.0, "neighbour_gap": 20.0,
    "area_off_material": 0.0,
    # U-03 (b): from +40.0 above the seat, steps <= 2.0
    "lower_from": 40.0, "lower_step": 2.0,
    # REQ-01, D-04a
    "flange_holes": ((81.0, -290.0), (100.0, -290.0), (-81.0, -290.0), (-100.0, -290.0)),
    "hole_d": 3.4, "hole_tol": 0.1, "hole_len": 4.0, "hole_len_tol": 0.1, "hole_min_d": 3.25,
    "under_y": 0.0, "under_tol": 0.10, "under_faces": 1, "offset_max": 0.10,
    # REQ-02
    "out_z": -302.0, "in_z": -299.0, "face_tol": 0.10, "face_ys": (50.0, 200.0), "face_xs": (-40.0, 0.0, 40.0),
    "x_half": 116.0, "x_tol": 0.1,
    # REQ-03, REQ-04
    "cord": ((95.0, 30.0),), "tubes": ((-100.0, 30.0), (-84.0, 30.0)), "pass_d": 12.0, "pass_tol": 0.1,
    # REQ-05
    "keepout_max_z": -283.0, "tank_box": (-70.0, 70.0, 0.0, 100.0, -299.0, -250.0),
    # REQ-06
    "vent_x": (78.0, 86.0, 94.0, 102.0, 110.0), "vent_w": 4.0, "vent_h": 80.0, "vent_y0": 100.0, "vent_y1": 180.0,
    "vent_tol": 0.1,
    # REQ-07, D-05b
    "inserts": ((90.0, -293.0), (-90.0, -293.0)), "insert_d": 4.0, "insert_tol": 0.05, "insert_depth": 6.0,
    "insert_depth_tol": 0.1, "insert_min_depth": 5.7, "top_y": 215.0, "top_tol": 0.10, "top_z": (-299.0, -287.0),
    "top_faces": 1,
    # REQ-08: Ø6 (r 3.0) cylinders y 4 .. 211 on the flange holes' axes
    "driver_r": 3.0, "driver_y": (4.0, 211.0),
    # U-05 census (plan section 3)
    "census": {"plane_faces": 46, "cylinder_faces": 19, "concave_cylinders": 19, "convex_cylinders": 0,
               "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0, "bspline_faces": 0, "other_faces": 0,
               "bores": 9},
    "bores_d34_y_through": 4, "bores_d40_y_blind": 2, "bores_d12_z_through": 3, "slot_end_faces": 10,
    "gusset_hypotenuses": 4, "boss_undersides": 2, "flange_fronts": 2, "ledge_under_pieces": 3, "wall_outer": 1,
    "ledge_ends": 2,
    "refilled_faces": 57,
    "density": 1270.0,
}
ASSUMES = {"U-03": ("A-01", "A-02", "A-07"), "REQ-01": ("A-01",), "REQ-02": ("A-02",), "REQ-03": ("A-03",),
           "REQ-04": ("A-04",), "REQ-05": ("A-07",), "REQ-06": ("A-06",), "REQ-07": ("A-05",),
           "D-02": ("A-09",), "D-03a": ("A-08",), "D-03b": ("A-08",), "D-05a": ("A-05",), "D-05b": ("A-05",),
           "REQ-09": ("A-11",), "E-11": ("A-03", "A-06")}
SPACING = 0.7   # brief WP-02 and plan section 2: the default spacing refuses the large faces
PART = "od_c11_back"
LABELS = {"plate": "od_c01_frame", "c02": "od_c02_bulkhead", "c03": "od_c03_cradle", "h01": "od_h01_pump"}
NEIGHBOURS = ("c03", "h01", "c02")
AREA_NOISE = 1e-6   # relative: an area difference below 1e-6 of the footprint is floating-point noise


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
    """The census bore along `axis`, of about diameter d, whose axis passes nearest `point`."""
    best = None
    p = np.array(point, float)
    a = np.array(axis, float)
    for b in bores:
        if not _along(b, axis) or abs(b["diameter"] - d) > dtol:
            continue
        s = np.array(b["start"], float)
        v = p - s
        off = float(np.linalg.norm(v - np.dot(v, a) * a))
        if best is None or off < best[0]:
            best = (off, b)
    return None if best is None else best[1]


def _unpack(loc):
    if isinstance(loc, Result):
        return {"diameter": loc, "offset": loc, "length": loc, "through": loc}
    return loc


def _area(shape):
    if shape is None:
        return 0.0
    return float(sum(f.area for f in shape.faces()))


def _down_face_split(shape, bed_z):
    """Diagnostic beside the overhang census (the census takes no region): every face
    with a downward-facing sample (build +Z), its least angle on a 9 x 9 grid of its
    parameters, its kind and its box, and the feature its position names."""
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
    """The named-exception region a downward face belongs to, by position (plan section 6)."""
    cx = 0.5 * (bb.min.X + bb.max.X)
    cz = 0.5 * (bb.min.Z + bb.max.Z)
    if kind == "cylinder" and r is not None:
        if abs(r - 1.7) < 0.1 and bb.max.Y <= 4.0 + 1e-3 and abs(cz + 290.0) < 2.0 \
                and min(abs(abs(cx) - 81.0), abs(abs(cx) - 100.0)) < 2.0:
            return "exception: flange hole 3.4 crown"
        if abs(r - 2.0) < 0.1 and bb.min.Y >= 203.0 and abs(cz + 293.0) < 2.5 and abs(abs(cx) - 90.0) < 2.5:
            return "exception: insert bore 4.0 crown"
    return "other"


def _refilled(one, bores):
    """The solid with each named-exception hole refilled by position: a cylinder of the
    measured diameter + 0.2 on the measured axis, from the hole's lower end (0.1 below a
    blind floor) to its upper end. The D-03a census outside the exception reads this."""
    solid = one
    for b in bores:
        ys = sorted((b["start"][1], b["end"][1]))
        y0 = ys[0] if b.get("through") else ys[0] - 0.1
        solid = solid + _ycyl(b["start"][0], b["start"][2], 0.5 * b["diameter"] + 0.1, y0, ys[1])
    solid = solid.clean()
    sols = solid.solids()
    return sols[0] if len(sols) == 1 else solid


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

    # U-02, envelope_within_spec, D-02, REQ-02 (x), REQ-05 (max z)
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
              note="lying on the outer face z -302: size_x and size_y on the bed, size_z tall")
    for k in ("min_x", "max_x"):
        v = SPEC["x_half"] * (1 if k == "max_x" else -1)
        G.add(f"REQ-02.{k}", env[k], "in", (v - SPEC["x_tol"], v + SPEC["x_tol"]), assumes=ASSUMES["REQ-02"])
    G.add("REQ-05.max_z", env["max_z"], "<=", SPEC["keepout_max_z"], assumes=ASSUMES["REQ-05"])
    facts["envelope"] = {k: v.measured for k, v in env.items()}
    min_y, max_y = env["min_y"].measured, env["max_y"].measured

    # REQ-02 wall faces: rays along -Z (outer) and +Z (inner) from z -300.5 inside the wall
    for y in SPEC["face_ys"]:
        for x in SPEC["face_xs"]:
            org = (0.0, y, -300.5)
            out_r = _ray(one, org, (1, 0, 0), (0, 0, 1), 180.0, x, "outer", r_max=5.0)
            in_r = _ray(one, org, (1, 0, 0), (0, 0, 1), 0.0, x, "outer", r_max=5.0)
            for tag, r, target, sgn in (("outer_face_z", out_r, SPEC["out_z"], -1.0),
                                        ("inner_face_z", in_r, SPEC["in_z"], 1.0)):
                zz = Result("wall_face_z", None if r.measured is None else -300.5 + sgn * r.measured, "mm",
                            at=r.at, status=r.status, reason=r.reason,
                            detail={"ray": "radial_extent outer from z -300.5 along Z"})
                G.add(f"REQ-02.{tag}.y{y:g}_x{x:g}", zz, "in", (target - SPEC["face_tol"], target + SPEC["face_tol"]),
                      assumes=ASSUMES["REQ-02"])

    # REQ-01 underside: one planar face at min y
    under = [f for f in _planar(one, (0, -1, 0)) if abs(-f["at"] - min_y) < 1e-4]
    facts["underside_faces"] = _strip(under)
    G.add("REQ-01.underside_faces", Result("planar_faces_at_min_y", len(under), "count"), "==",
          SPEC["under_faces"], assumes=ASSUMES["REQ-01"])
    if under:
        G.add("REQ-01.underside_y", Result("underside_y", -under[0]["at"], "mm", at=under[0]["min"]), "in",
              (SPEC["under_y"] - SPEC["under_tol"], SPEC["under_y"] + SPEC["under_tol"]), assumes=ASSUMES["REQ-01"])
    else:
        G.add("REQ-01.underside_y", inconclusive("underside_y", "mm", "no planar face at min y"), "in",
              (SPEC["under_y"] - SPEC["under_tol"], SPEC["under_y"] + SPEC["under_tol"]))

    # REQ-07 top: one planar face at max y spanning z -299 .. -287
    top = [f for f in _planar(one, (0, 1, 0)) if abs(f["at"] - max_y) < 1e-4]
    facts["top_faces"] = _strip(top)
    G.add("REQ-07.top_faces", Result("planar_faces_at_max_y", len(top), "count"), "==", SPEC["top_faces"],
          assumes=ASSUMES["REQ-07"])
    if top:
        G.add("REQ-07.top_y", Result("top_y", top[0]["at"], "mm", at=top[0]["min"]), "in",
              (SPEC["top_y"] - SPEC["top_tol"], SPEC["top_y"] + SPEC["top_tol"]), assumes=ASSUMES["REQ-07"])
        for k, i, v in (("top_min_z", 0, SPEC["out_z"]), ("top_max_z", 1, SPEC["top_z"][1])):
            val_ = top[0]["min"][2] if i == 0 else top[0]["max"][2]
            G.add(f"REQ-07.{k}", Result(k, val_, "mm"), "in", (v - SPEC["top_tol"], v + SPEC["top_tol"]),
                  assumes=ASSUMES["REQ-07"],
                  note="the top face spans the wall (from z -302) and the ledge (to z -287): it covers z -299 .. -287")
    else:
        G.add("REQ-07.top_y", inconclusive("top_y", "mm", "no planar face at max y"), "in",
              (SPEC["top_y"] - SPEC["top_tol"], SPEC["top_y"] + SPEC["top_tol"]))

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
    bores = _bores(census)
    facts["bores"] = bores
    y34 = [b for b in bores if _along(b, (0, 1, 0)) and abs(b["diameter"] - 3.4) < 0.3 and b.get("through")]
    y40 = [b for b in bores if _along(b, (0, 1, 0)) and abs(b["diameter"] - 4.0) < 0.3 and not b.get("through")]
    z12 = [b for b in bores if _along(b, (0, 0, 1)) and abs(b["diameter"] - 12.0) < 0.5 and b.get("through")]
    for tag, lst, n in (("bores_d34_y_through", y34, SPEC["bores_d34_y_through"]),
                        ("bores_d40_y_blind", y40, SPEC["bores_d40_y_blind"]),
                        ("bores_d12_z_through", z12, SPEC["bores_d12_z_through"])):
        G.add(f"U-05.{tag}", Result(tag, len(lst), "count"), "==", n)
    slot_ends = sum(1 for f in one.faces() if f.geom_type.name == "CYLINDER" and abs(f.radius - 2.0) < 1e-3
                    and abs(f.axis_of_rotation.direction.Z) > 0.9999)
    G.add("U-05.slot_end_faces_r2_along_z", Result("slot_end_faces", slot_ends, "count"), "==",
          SPEC["slot_end_faces"])
    G.add("feature_census.slot_end_faces_r2_along_z", Result("slot_end_faces", slot_ends, "count"), "==",
          SPEC["slot_end_faces"])
    hyp = [f for f in one.faces() if f.geom_type.name == "PLANE" and abs(f.normal_at().X) < 1e-6
           and f.normal_at().Y > 0.1 and f.normal_at().Z > 0.1]
    boss_u = [f for f in _planar(one, (0, -1, 0)) if abs(-f["at"] - 203.0) < 0.5]
    fronts = [f for f in _planar(one, (0, 0, 1)) if abs(f["at"] - SPEC["keepout_max_z"]) < 0.5]
    ledge_u = [f for f in _planar(one, (0, -1, 0)) if abs(-f["at"] - 211.0) < 0.5]
    outer = [f for f in _planar(one, (0, 0, -1)) if abs(-f["at"] - SPEC["out_z"]) < 0.5]
    ledge_ends = [f for f in one.faces() if f.geom_type.name == "PLANE" and abs(abs(f.normal_at().X) - 1) < 1e-6
                  and f.bounding_box().min.Y >= 210.0 and abs(abs(f.center().X) - 114.0) < 0.5]
    for tag, n, want, what in (("gusset_hypotenuses", len(hyp), SPEC["gusset_hypotenuses"], "4 gussets"),
                               ("boss_undersides", len(boss_u), SPEC["boss_undersides"], "2 insert bosses"),
                               ("flange_fronts", len(fronts), SPEC["flange_fronts"], "2 floor flanges"),
                               ("ledge_under_pieces", len(ledge_u), SPEC["ledge_under_pieces"], "1 ledge, 2 bosses"),
                               ("ledge_ends", len(ledge_ends), SPEC["ledge_ends"], "1 top ledge"),
                               ("wall_outer_faces", len(outer), SPEC["wall_outer"], "1 wall")):
        G.add(f"U-05.{tag}", Result(tag, n, "count"), "==", want, note=what)
        G.add(f"feature_census.{tag}", Result(tag, n, "count"), "==", want, note=what)

    # REQ-01, D-04a: the four flange holes
    dlim = (SPEC["hole_d"] - SPEC["hole_tol"], SPEC["hole_d"] + SPEC["hole_tol"])
    llim = (SPEC["hole_len"] - SPEC["hole_len_tol"], SPEC["hole_len"] + SPEC["hole_len_tol"])
    widest = None
    for x, z in SPEC["flange_holes"]:
        tag = f"x{x:g}_z{z:g}"
        loc = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, 2.0, z), (0, 1, 0)))
        G.add(f"REQ-01.{tag}.diameter", loc["diameter"], "in", dlim, assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.{tag}.length", loc["length"], "in", llim, assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.{tag}.through", loc["through"], "==", 1, assumes=ASSUMES["REQ-01"])
        G.add(f"D-04a.{tag}.diameter", loc["diameter"], ">=", SPEC["hole_min_d"])
        dm = loc["diameter"].measured
        if dm is not None:
            widest = dm if widest is None else max(widest, dm)

    # REQ-03, REQ-04: the pass-throughs along Z
    plim = (SPEC["pass_d"] - SPEC["pass_tol"], SPEC["pass_d"] + SPEC["pass_tol"])
    for req, pts in (("REQ-03", SPEC["cord"]), ("REQ-04", SPEC["tubes"])):
        for x, y in pts:
            tag = f"x{x:g}_y{y:g}"
            loc = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, y, -300.5), (0, 0, 1)))
            G.add(f"{req}.{tag}.diameter", loc["diameter"], "in", plim, assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES[req])
            G.add(f"{req}.{tag}.through", loc["through"], "==", 1, assumes=ASSUMES[req])
            facts[f"{req}.{tag}.length"] = _res(loc["length"])

    # REQ-07, D-05b, D-05a, J-05: the two insert bores
    idlim = (SPEC["insert_d"] - SPEC["insert_tol"], SPEC["insert_d"] + SPEC["insert_tol"])
    ihlim = (SPEC["insert_depth"] - SPEC["insert_depth_tol"], SPEC["insert_depth"] + SPEC["insert_depth_tol"])
    for x, z in SPEC["inserts"]:
        tag = f"x{x:g}_z{z:g}"
        loc = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, SPEC["top_y"] - 3.0, z), (0, -1, 0)))
        G.add(f"REQ-07.{tag}.diameter", loc["diameter"], "in", idlim, assumes=ASSUMES["REQ-07"])
        G.add(f"REQ-07.{tag}.depth", loc["length"], "in", ihlim, assumes=ASSUMES["REQ-07"])
        G.add(f"REQ-07.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-07"])
        G.add(f"REQ-07.{tag}.blind", loc["through"], "==", 0, assumes=ASSUMES["REQ-07"])
        G.add(f"D-05b.{tag}.diameter", loc["diameter"], "in", idlim, assumes=ASSUMES["D-05b"])
        G.add(f"D-05b.{tag}.depth", loc["length"], "in", ihlim, assumes=ASSUMES["D-05b"])
        G.add(f"D-05b.{tag}.depth_min", loc["length"], ">=", SPEC["insert_min_depth"], assumes=ASSUMES["D-05b"])
        b = _find_bore(bores, (0, 1, 0), (x, 212.0, z), SPEC["insert_d"])
        if b is None:
            for k in ("across_x", "across_z"):
                G.add(f"D-05a.{tag}.{k}", inconclusive("boss_across", "mm", "bore not found"), ">=",
                      SPEC["boss_across"], assumes=ASSUMES["D-05a"])
            for side in ("+x", "-x", "+z", "-z"):
                G.add(f"J-05.{tag}.{side}", inconclusive("wall_around_insert", "mm", "bore not found"), ">=",
                      SPEC["wall_insert"])
            continue
        ys = sorted((b["start"][1], b["end"][1]))
        yp = ys[0] + 1.0          # 1.0 above the floor, in the boss (the ledge starts at y 211)
        org = (b["start"][0], 0.0, b["start"][2])
        rays = {"+x": _ray(one, org, (0, 1, 0), (1, 0, 0), 0.0, yp, "outer", r_min=0.0, r_max=15.0),
                "-x": _ray(one, org, (0, 1, 0), (1, 0, 0), 180.0, yp, "outer", r_min=0.0, r_max=15.0),
                "-z": _ray(one, org, (0, 1, 0), (1, 0, 0), 90.0, yp, "outer", r_min=0.0, r_max=15.0),
                "+z": _ray(one, org, (0, 1, 0), (1, 0, 0), 270.0, yp, "outer", r_min=0.0, r_max=15.0)}
        facts[f"D-05a.{tag}.ray_level_y"] = yp
        for k, (a, c) in (("across_x", ("+x", "-x")), ("across_z", ("+z", "-z"))):
            ra, rc = rays[a], rays[c]
            if ra.measured is not None and rc.measured is not None:
                acr = Result("boss_across", ra.measured + rc.measured, "mm", at=[ra.at, rc.at])
            else:
                acr = inconclusive("boss_across", "mm", f"{ra.reason} {rc.reason}".strip() or "no ray")
            G.add(f"D-05a.{tag}.{k}", acr, ">=", SPEC["boss_across"], assumes=ASSUMES["D-05a"])
        for side, rr in rays.items():
            if rr.measured is not None:
                w = Result("wall_around_insert", rr.measured - b["diameter"] / 2.0, "mm", at=rr.at)
            else:
                w = inconclusive("wall_around_insert", "mm", rr.reason or "no ray")
            G.add(f"J-05.{tag}.{side}", w, ">=", SPEC["wall_insert"])

    # REQ-06: the five vent slots, rays inside each slot at z -300.5
    for xc in SPEC["vent_x"]:
        tag = f"x{xc:g}"
        yc = 0.5 * (SPEC["vent_y0"] + SPEC["vent_y1"])
        org = (xc, yc, 0.0)
        r = {a: _ray(one, org, (0, 0, 1), (1, 0, 0), a, -300.5, "inner") for a in (0.0, 180.0, 90.0, 270.0)}
        if all(v.measured is not None for v in r.values()):
            w = Result("vent_width", r[0.0].measured + r[180.0].measured, "mm", at=[r[0.0].at, r[180.0].at])
            cx = Result("vent_centre_x", xc + 0.5 * (r[0.0].measured - r[180.0].measured), "mm")
            h = Result("vent_height", r[90.0].measured + r[270.0].measured, "mm", at=[r[90.0].at, r[270.0].at])
            y0 = Result("vent_y0", yc - r[270.0].measured, "mm")
            y1 = Result("vent_y1", yc + r[90.0].measured, "mm")
        else:
            why = "; ".join(v.reason for v in r.values() if v.reason) or "no ray"
            w, cx, h, y0, y1 = (inconclusive(n, "mm", why) for n in
                                ("vent_width", "vent_centre_x", "vent_height", "vent_y0", "vent_y1"))
        vt = SPEC["vent_tol"]
        G.add(f"REQ-06.{tag}.width", w, "in", (SPEC["vent_w"] - vt, SPEC["vent_w"] + vt), assumes=ASSUMES["REQ-06"])
        G.add(f"REQ-06.{tag}.height", h, "in", (SPEC["vent_h"] - vt, SPEC["vent_h"] + vt), assumes=ASSUMES["REQ-06"])
        G.add(f"REQ-06.{tag}.centre_x", cx, "in", (xc - vt, xc + vt), assumes=ASSUMES["REQ-06"])
        G.add(f"REQ-06.{tag}.y0", y0, "in", (SPEC["vent_y0"] - vt, SPEC["vent_y0"] + vt), assumes=ASSUMES["REQ-06"])
        G.add(f"REQ-06.{tag}.y1", y1, "in", (SPEC["vent_y1"] - vt, SPEC["vent_y1"] + vt), assumes=ASSUMES["REQ-06"])
        # through along Z: no material on the slot's centre line over the wall's thickness
        thru = _ray(one, (xc, yc, -303.0), (0, 0, 1), (1, 0, 0), 0.0, 3.0, "inner", r_max=1.9)
        facts[f"REQ-06.{tag}.centre_line_clear"] = _res(thru)

    # REQ-05: the tank zone box
    x0, x1, y0_, y1_, z0, z1 = SPEC["tank_box"]
    G.add("REQ-05.tank_zone_interference", _safe(common_volume, "common_volume", "mm3", one,
                                                 _box(x0, x1, y0_, y1_, z0, z1)), "<=", SPEC["interference"],
          assumes=ASSUMES["REQ-05"])

    # REQ-08: four Ø6 driver cylinders y 4 .. 211 on the flange holes' nominal axes
    for x, z in SPEC["flange_holes"]:
        cyl = _ycyl(x, z, SPEC["driver_r"], *SPEC["driver_y"])
        G.add(f"REQ-08.x{x:g}_z{z:g}", _safe(common_volume, "common_volume", "mm3", one, cyl), "<=",
              SPEC["interference"])
        facts[f"REQ-08.x{x:g}_z{z:g}.clearance"] = _res(_safe(clearance, "clearance", "mm", one, cyl))
        # beside the gate: a straight driver on above y 211 meets the ledge; a driver line tilted toward +Z
        for deg in (0.0, 2.0):
            # the tilted end cap would dip r sin(tilt) below its centre: start it that far (+0.01) higher
            y_start = SPEC["driver_y"][0] + SPEC["driver_r"] * math.sin(math.radians(deg)) + (0.01 if deg else 0.0)
            length = 260.0 - y_start
            pl = Plane(origin=(x, y_start, z), x_dir=(1, 0, 0),
                       z_dir=(0, math.cos(math.radians(deg)), math.sin(math.radians(deg))))
            tilted = pl * Cylinder(SPEC["driver_r"], length, align=(Align.CENTER, Align.CENTER, Align.MIN))
            facts[f"REQ-08.x{x:g}_z{z:g}.driver_to_y260_tilt{deg:g}deg_common_mm3"] = _res(
                _safe(common_volume, "common_volume", "mm3", one, tilted))

    # D-03b designer's reading
    G.add("D-03b.widest_horizontal_hole", Result("horizontal_hole_bridge", widest, "mm") if widest is not None
          else inconclusive("horizontal_hole_bridge", "mm", "no hole located"), "<=", SPEC["bridge_span"],
          assumes=ASSUMES["D-03b"], note="reviewer row; designer reading: the flange holes Ø3.4 (and the insert "
          "bores Ø4.0, below) are the only horizontal holes in the print")
    widest_ins = max((b["diameter"] for b in y40), default=None)
    G.add("D-03b.widest_insert_bore", Result("horizontal_hole_bridge", widest_ins, "mm") if widest_ins is not None
          else inconclusive("horizontal_hole_bridge", "mm", "no insert bore"), "<=", SPEC["bridge_span"],
          assumes=ASSUMES["D-03b"])
    if not quick:
        fcs = _safe(flat_ceiling_spans, "flat_ceiling_spans", "mm", one, build_dir=SPEC["build_dir"],
                    max_span=SPEC["bridge_span"], spacing=SPACING)
        G.add("D-03b.flat_ceiling_span", fcs, "<=", SPEC["bridge_span"], assumes=ASSUMES["D-03b"],
              note="designer reading; the row is the reviewer's, from sections")

    # U-03 (a) and (b): the parts as placed in the check assembly
    if asm_path is not None and asm_path.exists():
        asm = read_step(asm_path)
        kids = _children(asm)
        facts["assembly_labels"] = sorted(kids)
        pn = kids.get(PART)
        plate = kids.get(LABELS["plate"])
        if pn is None or plate is None:
            G.add("U-03.contact", inconclusive("clearance", "mm", "panel or plate missing in the assembly"), "==", 0.0)
        else:
            pn, plate = _one(pn), _one(plate)
            G.add("U-03.plate.clearance", _safe(clearance, "clearance", "mm", pn, plate), "==", SPEC["contact"],
                  assumes=ASSUMES["U-03"], note="designed contact: the underside on the plate's top face")
            G.add("U-03.plate.interference", _safe(common_volume, "common_volume", "mm3", pn, plate), "<=",
                  SPEC["interference"], assumes=ASSUMES["U-03"])
            # footprint against the plate's top face and its outline
            top_face = None
            try:
                pmax = envelope(plate)["max_y"].measured
                ptop = [f["face"] for f in _planar(plate, (0, 1, 0)) if abs(f["at"] - pmax) < 1e-4]
                pmin = envelope(pn)["min_y"].measured
                fp = [f["face"] for f in _planar(pn, (0, -1, 0)) if abs(-f["at"] - pmin) < 1e-4]
                if len(ptop) != 1 or not fp:
                    raise ValueError(f"{len(ptop)} plate top faces, {len(fp)} footprint faces")
                top_face = ptop[0]
                outline = Face(top_face.outer_wire())
                a_fp = sum(f.area for f in fp)
                a_outline = sum(_area(f.intersect(outline)) for f in fp)
                a_material = sum(_area(f.intersect(top_face)) for f in fp)
                off_outline = a_fp - a_outline
                over_holes = a_outline - a_material
                off_outline = 0.0 if abs(off_outline) < AREA_NOISE * a_fp else off_outline
                over_holes = 0.0 if abs(over_holes) < AREA_NOISE * a_fp else over_holes
                facts["U-03.footprint"] = {"footprint_mm2": a_fp, "inside_outline_mm2": a_outline,
                                           "over_material_mm2": a_material}
                G.add("U-03.footprint_outside_outline_area",
                      Result("footprint_outside_outline", off_outline, "mm2"), "<=", SPEC["area_off_material"],
                      assumes=ASSUMES["U-03"], note="footprint inside the plate's outline")
                # which plate holes lie under the footprint
                pc = _safe(bore_census, "bore_census", "count", plate)
                under_holes = []
                for b in _bores(pc):
                    if not _along(b, (0, 1, 0)):
                        continue
                    cx_, cz_ = b["start"][0], b["start"][2]
                    if any(f.bounding_box().min.X - 0.5 * b["diameter"] <= cx_ <= f.bounding_box().max.X
                           + 0.5 * b["diameter"] and f.bounding_box().min.Z - 0.5 * b["diameter"] <= cz_
                           <= f.bounding_box().max.Z + 0.5 * b["diameter"] for f in fp):
                        under_holes.append({"centre_xz": [round(cx_, 4), round(cz_, 4)],
                                            "diameter": round(b["diameter"], 4)})
                facts["U-03.plate_holes_near_or_under_footprint"] = under_holes
                G.add("U-03.footprint_over_plate_holes_area",
                      Result("footprint_over_plate_holes", over_holes, "mm2",
                             at=str(under_holes) if under_holes else None), "<=", SPEC["area_off_material"],
                      assumes=ASSUMES["U-03"],
                      note="the underside wholly over plate material: footprint area inside the outline that lies "
                           "over a plate hole")
                dist = min(f.outer_wire().distance_to(top_face.outer_wire()) for f in fp)
                G.add("U-03.footprint_to_outline_distance", Result("footprint_to_outline", dist, "mm"), ">=",
                      SPEC["edge_gap"], assumes=ASSUMES["U-03"],
                      note="least distance from the footprint's edges to the plate's outline (edge and corner arcs)")
            except Exception as exc:  # noqa: BLE001
                why = f"{type(exc).__name__}: {exc}"
                for k in ("footprint_outside_outline_area", "footprint_over_plate_holes_area"):
                    G.add(f"U-03.{k}", inconclusive(k, "mm2", why), "<=", SPEC["area_off_material"])
                G.add("U-03.footprint_to_outline_distance", inconclusive("footprint_to_outline", "mm", why), ">=",
                      SPEC["edge_gap"])
            # under each flange hole: plate material and the distance to every existing plate hole
            pcen = _safe(bore_census, "bore_census", "count", plate)
            pbores = [b for b in _bores(pcen) if _along(b, (0, 1, 0))]
            ncen = _safe(bore_census, "bore_census", "count", pn)
            nb = _bores(ncen)
            pmin_y = envelope(plate)["min_y"].measured
            pmax_y = envelope(plate)["max_y"].measured
            for x, z in SPEC["flange_holes"]:
                tag = f"x{x:g}_z{z:g}"
                b = _find_bore(nb, (0, 1, 0), (x, 2.0, z), SPEC["hole_d"])
                if b is None:
                    G.add(f"U-03.under_hole.{tag}.plate_material",
                          inconclusive("plate_under_hole", "mm3", "flange hole not found"), "==", 0.0)
                    continue
                hx, hz, hd = b["start"][0], b["start"][2], b["diameter"]
                plug = _ycyl(hx, hz, 0.5 * hd, pmin_y, pmax_y)
                cv = _safe(common_volume, "common_volume", "mm3", plug, plate)
                if cv.measured is not None:
                    miss = Result("plate_missing_under_hole", plug.volume - cv.measured, "mm3",
                                  at=[hx, 0.0, hz], detail={"plug_mm3": plug.volume, "common_mm3": cv.measured})
                else:
                    miss = inconclusive("plate_missing_under_hole", "mm3", cv.reason)
                G.add(f"U-03.under_hole.{tag}.plate_material_missing", miss, "<=", SPEC["interference"],
                      assumes=ASSUMES["U-03"] + ("A-01",),
                      note="a plug of the hole's measured diameter through the plate's thickness on the hole's "
                           "measured axis lies wholly in plate material (REQ-01 and A-01: the new insert's site)")
                near = min(((math.hypot(pb["start"][0] - hx, pb["start"][2] - hz), pb) for pb in pbores),
                           key=lambda t: t[0], default=None)
                if near is None:
                    r = inconclusive("hole_to_plate_hole", "mm", "no plate hole found")
                else:
                    r = Result("hole_to_plate_hole", near[0], "mm", at=[near[1]["start"][0], 0.0, near[1]["start"][2]],
                               detail={"plate_hole_d": near[1]["diameter"]})
                G.add(f"U-03.under_hole.{tag}.to_nearest_plate_hole", r, ">=", SPEC["hole_gap"],
                      assumes=ASSUMES["U-03"])
                G.add(f"REQ-01.plate_site.{tag}.to_nearest_plate_hole", r, ">=", SPEC["hole_gap"],
                      assumes=ASSUMES["REQ-01"])
                # the brief's edge distance, reported beside (not a section 5 threshold)
                if top_face is not None:
                    facts[f"U-03.under_hole.{tag}.centre_to_plate_edge_mm"] = Vertex(hx, pmax_y, hz).distance_to(
                        top_face.outer_wire())
            for key in NEIGHBOURS:
                s = kids.get(LABELS[key])
                if s is None:
                    G.add(f"U-03.{key}.clearance", inconclusive("clearance", "mm", "missing in the assembly"), ">=",
                          SPEC["neighbour_gap"])
                    continue
                s = _one(s)
                G.add(f"U-03.{key}.clearance", _safe(clearance, "clearance", "mm", pn, s), ">=",
                      SPEC["neighbour_gap"], assumes=ASSUMES["U-03"])
                G.add(f"U-03.{key}.interference", _safe(common_volume, "common_volume", "mm3", pn, s), "<=",
                      SPEC["interference"], assumes=ASSUMES["U-03"])
            # U-03 (b): lowered along -Y from +40.0 in steps of 2.0
            refs = {k: _one(kids[LABELS[k]]) for k in ("plate", "c02", "c03", "h01") if LABELS[k] in kids}
            steps = int(round(SPEC["lower_from"] / SPEC["lower_step"]))
            path_rows = []
            for i in range(steps + 1):
                dy = SPEC["lower_from"] - i * SPEC["lower_step"]
                moved = pn.moved(Location((0.0, dy, 0.0)))
                for k, s in refs.items():
                    cv = _safe(common_volume, "common_volume", "mm3", moved, s)
                    path_rows.append({"dy": dy, "ref": k, "measured": cv.measured, "status": cv.status,
                                      "reason": cv.reason})
            facts["U-03b.path"] = path_rows
            for k in ("plate", "c02", "c03", "h01"):
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
            facts["assembly_panel_volume_mm3"] = mass_properties(pn, SPEC["density"])["volume"].measured
    else:
        G.add("U-03.contact", inconclusive("clearance", "mm", "no assembly file"), "==", 0.0)

    # U-04: part and assembly round trip against the build
    try:
        import build_od_c11_back as B
        p = B.Params(**variant)
        built = B.build_panel(p)
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
            G.add("U-04.assembly.solids", ra["solids"], "==", 5)
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

    # D-03a: census outside the named exception (the six horizontal holes refilled by position)
    exc_bores = y34 + y40
    facts["D-03a.exception_holes"] = len(exc_bores)
    try:
        filled = _refilled(one, exc_bores)
        nf = len(filled.faces())
        facts["D-03a.refilled_faces"] = nf
        facts["D-03a.refilled_solids"] = len(filled.solids())
        if len(exc_bores) != 6 or nf != SPEC["refilled_faces"] or len(filled.solids()) != 1:
            oh_out = inconclusive("overhang_census", "deg", f"refill not as planned: {len(exc_bores)} holes, "
                                  f"{nf} faces, {len(filled.solids())} solids")
        else:
            oh_out = _safe(overhang_census, "overhang_census", "deg", filled, build_dir=SPEC["build_dir"],
                           spacing=SPACING)
    except Exception as exc:  # noqa: BLE001
        oh_out = inconclusive("overhang_census", "deg", f"{type(exc).__name__}: {exc}")
    G.add("D-03a", oh_out, ">=", SPEC["overhang_deg"], assumes=ASSUMES["D-03a"],
          note="overhang_census outside the named exception: the four Ø3.4 flange holes and the two Ø4.0 insert "
               "bores refilled by position; the whole-part census and the crowns in facts")
    if not quick:
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
        ang = rec.get("stl", {}).get("angular_tolerance")
        G.add("U-07.angular_tolerance", Result("stl_angular_tolerance", ang, "rad") if ang is not None
              else inconclusive("stl_angular_tolerance", "rad", "no build record"), "<=", SPEC["stl_ang_max"])
        tl = rec.get("stl", {}).get("tolerance")
        G.add("U-07.tolerance", Result("stl_tolerance", tl, "mm") if tl is not None
              else inconclusive("stl_tolerance", "mm", "no build record"), "<=", SPEC["stl_tol"])
        scratch.mkdir(parents=True, exist_ok=True)
        try:
            w = write_stl(one, scratch / "remesh_check.stl", tolerance=SPEC["stl_tol"], angular_tolerance=ang or 0.2)
            sag = w.checks["max_sagitta"]
            facts["remesh_triangles"] = w.detail.get("triangles")
        except Exception as exc:  # noqa: BLE001
            sag = inconclusive("stl_max_sagitta", "mm", f"{type(exc).__name__}: {exc}")
        G.add("U-07.max_sagitta", sag, "<=", SPEC["stl_tol"],
              note="re-meshed from the re-imported STEP at the build's settings")
    else:
        G.add("U-07", inconclusive("mesh", "mm", "no STL"), "<=", SPEC["stl_tol"])

    # by the rows
    G.fixed("U-08", "N/A", "N/A", "no threads (N/A by its row)")
    G.fixed("D-07", "N/A", "N/A", "no fit-critical bores (N/A by its row)")
    G.fixed("E-06", INCONCLUSIVE, "reviewer", "reviewer row, from sections; designer reading in the REPORT")
    G.fixed("E-11", INCONCLUSIVE, "reviewer", "reviewer row, from sections; designer reading in the REPORT",
            assumes=ASSUMES["E-11"])
    G.fixed("REQ-09(Soft)", INCONCLUSIVE, "bench", "Soft bench gate: not geometric, answered by the first print",
            assumes=ASSUMES["REQ-09"])
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
              f"{r.get('margin')!s:<12} {r.get('reason', '')[:90]}")


if __name__ == "__main__":
    main()
