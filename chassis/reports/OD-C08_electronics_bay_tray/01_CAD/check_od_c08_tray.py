"""Checks for od_c08_tray (job 20261001-od-c08-electronics-bay-tray, concept C1, spec 1.0).

Written before the build (PLAYBOOK D3) from 01_CAD/DESIGN_PLAN.md section 6. Every
predicate measures the re-imported STEP files with tools.core / tools.measure and
compares through tools.result.gate with the GATES.md section 0 band. Thresholds come
from DESIGN_SPEC.md 1.0 section 5 only (the SPEC table cites the row of each value).
Any exception or missing value gives INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c08_tray.py \
        --step 02_STEP_STL/od_c08_tray_C1_v01.step \
        --asm 02_STEP_STL/od_c08_assembly_C1_v01.step \
        --stl 02_STEP_STL/od_c08_tray_C1_v01.stl \
        --record 01_CAD/build_record_v01.json \
        --out 01_CAD/check_od_c08_tray_v01.json [--variant '{...}'] [--skip-path]
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
from tools.measure.features import cylinder as cyl_axis  # noqa: E402
from tools.result import INCONCLUSIVE, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.0) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "count": 0, "bool": 0, "rad": 0.00002}
SPEC = {
    # U-02: 39.0 x 92.0 x 160.0 each +-0.1; position x 73 .. 112, y 0 .. 92, z -230 .. -70
    "size": {"size_x": 39.0, "size_y": 92.0, "size_z": 160.0}, "size_tol": 0.1,
    "position": {"min_x": 73.0, "max_x": 112.0, "min_y": 0.0, "max_y": 92.0, "min_z": -230.0, "max_z": -70.0},
    # D-02 (A-09): K1C 220 x 220 x 250; lying on the wall: y and z on the bed, x tall
    "bed": {"size_y": 220.0, "size_z": 220.0, "size_x": 250.0},
    # D-01a, D-01b, D-06a, U-06 (Soft)
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wall_wide": 2.0,
    # J-05, D-05a
    "wall_insert": 3.0, "boss_across": 8.0,
    # D-03a: >= 45 deg, build direction +X (A-08); D-03b span <= 5
    "overhang_deg": 45.0, "build_dir": (1.0, 0.0, 0.0), "bridge_span": 5.0,
    # U-07: tol 0.01, angular <= 4 acos(1 - 0.01 / R_max), R_max 5.0 (the Ø10 standoff)
    "stl_tol": 0.01, "stl_ang_max": 4.0 * math.acos(1.0 - 0.01 / 5.0),
    # U-03 (a)
    "contact": 0.0, "interference": 0.0, "pin_gap": 0.30, "keepout": 0.5, "c02_gap_tray": 1.5,
    "c02_gap_board": 10.0, "zone_x": (70.0, 117.0), "zone_z": (-240.0, -30.0), "zone_min_y": 10.0,
    # U-03 (a) plate material under each flange hole (brief WP-02, A-01)
    "plate_hole_gap": 6.0, "plate_edge_gap": 8.0, "plate_t": 6.0,
    # U-03 (b): from +5.0 above the seat in steps <= 0.5, along -X
    "path_from": 5.0, "path_step": 0.5,
    # REQ-01, D-04a: four flange holes
    "holes": ((88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0)),   # (x, z)
    "hole_d": 3.4, "hole_tol": 0.1, "hole_min_d": 3.25, "hole_len": 4.0, "hole_len_tol": 0.1,
    "underside_y": 0.0, "underside_tol": 0.10, "offset_max": 0.10,
    # REQ-02, D-05b, E-05
    "seat_x": 82.44, "seat_tol": 0.05,
    "inserts": ((80.00, -100.00), (27.99, -100.01)),                              # (y, z)
    "pins": ((81.98, -157.52), (30.99, -157.51)),
    "bore_d": 4.0, "bore_tol": 0.05, "bore_depth": 6.0, "bore_depth_tol": 0.1, "bore_min_depth": 5.7,
    "pin_d": 1.8, "pin_tol": 0.05, "pin_len": 2.5, "pin_len_tol": 0.1, "coax": 0.10,
    # REQ-03
    "min_x": 73.0, "front_z": -70.0, "front_tol": 0.1,
    # REQ-04: Ø8 x 116 cylinders, y 4 .. 120, on the flange holes' axes
    "driver_r": 4.0, "driver_y": (4.0, 120.0),
    # REQ-05: box x 85 .. 117, y 4 .. 92, z -195 .. -95
    "faston_box": ((85.0, 117.0), (4.0, 92.0), (-195.0, -95.0)),
    # U-05 census (plan section 3)
    "census": {"plane_faces": 42, "cylinder_faces": 12, "concave_cylinders": 6, "convex_cylinders": 6,
               "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0, "bspline_faces": 0, "other_faces": 0,
               "bores": 6},
    "bores_x_blind": 2, "bores_y_through": 4, "pins_n": 2, "slot_faces": 16, "slots": 4, "gussets": 4,
    "standoffs_d10": 2, "standoffs_d6": 2, "seat_faces": 4,
    "refilled_faces": 50,
    "density": 1270.0,
}
ASSUMES = {"U-03": ("A-02", "A-03", "A-06"), "U-03.plate": ("A-01",), "D-02": ("A-09",), "D-03a": ("A-08",),
           "D-03b": ("A-08",), "D-04c": ("A-02",), "D-04d": ("A-02",), "D-05a": ("A-07",), "D-05b": ("A-07",),
           "E-01": ("A-02",), "E-05": ("A-02", "A-03"), "E-11": ("A-11",), "REQ-01": ("A-01",),
           "REQ-02": ("A-02", "A-03"), "REQ-03": ("A-06",), "REQ-04": ("A-03",), "REQ-05": ("A-03",)}
SPACING = 0.7   # brief WP-02: min_wall and overhang_census refuse the large faces at the default spacing
PART = "od_c08_tray"
LABELS = {"tray": "od_c08_tray", "board": "od_e01_power_pcb", "plate": "od_c01_frame", "c02": "od_c02_bulkhead"}
STANDOFF_MARGIN = 0.5   # plan: the region box around a standoff column is its radius + 0.5


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


def _one(shape):
    sols = shape.solids()
    return sols[0] if len(sols) == 1 else shape


def _stl_facts(path: Path) -> dict:
    data = path.read_bytes()
    n = struct.unpack_from("<I", data, 80)[0]
    arr = np.frombuffer(data, dtype=np.dtype([("n", "<3f4"), ("v", "<9f4"), ("a", "<u2")]), count=n, offset=84)
    v = arr["v"].reshape(-1, 3).astype(float)
    return {"triangles_header": n, "bytes": len(data), "bbox_min": v.min(0).round(4).tolist(),
            "bbox_max": v.max(0).round(4).tolist(), "bbox_size": (v.max(0) - v.min(0)).round(4).tolist()}


def _res(r):
    return {"measured": r.measured, "unit": r.unit, "status": r.status, "at": r.at, "reason": r.reason}


def _box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, y0, z0) * Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN))


def _ycyl(x, z, r, y0, y1):
    up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return Pos(x, y0, z) * (up * Cylinder(r, y1 - y0, align=(Align.CENTER, Align.CENTER, Align.MIN)))


def _vol(shape):
    try:
        return float(sum(s.volume for s in shape.solids()))
    except Exception:  # noqa: BLE001
        return None


def _planar(shape, normal, tol=1e-6):
    n = np.array(normal, float)
    out = []
    for f in shape.faces():
        if f.geom_type.name != "PLANE":
            continue
        fn = np.array(tuple(f.normal_at()))
        if float(np.dot(fn, n)) < 1.0 - tol:
            continue
        bb = f.bounding_box()
        out.append({"face": f, "at": float(np.dot(np.array(tuple(f.center())), n)), "area": f.area,
                    "min": [bb.min.X, bb.min.Y, bb.min.Z], "max": [bb.max.X, bb.max.Y, bb.max.Z]})
    return out


def _cyl_faces(shape):
    """Cylindrical faces with their axis (point, direction) and radius, and their box."""
    out = []
    for f in shape.faces():
        if f.geom_type.name != "CYLINDER":
            continue
        try:
            o, d, r = cyl_axis(f.wrapped)
        except Exception:  # noqa: BLE001
            continue
        bb = f.bounding_box()
        out.append({"face": f, "origin": o, "dir": d, "r": r,
                    "min": [bb.min.X, bb.min.Y, bb.min.Z], "max": [bb.max.X, bb.max.Y, bb.max.Z]})
    return out


def _line_offset(p, o, d):
    """Distance from point p to the line through o along d."""
    p, o, d = (np.array(v, float) for v in (p, o, d))
    d = d / np.linalg.norm(d)
    w = p - o
    return float(np.linalg.norm(w - np.dot(w, d) * d))


def _down_faces(shape, bed_x):
    """Diagnostic beside the overhang census: faces with a downward sample (build +X)
    off the bed, their least angle on a 9 x 9 parameter grid, kind and box."""
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
                if p.X - bed_x <= 0.01:
                    continue
                tb = -n.X
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
        region = "other"
        if kind == "cylinder" and r is not None and abs(r - 0.5 * SPEC["hole_d"]) < 0.2 and bb.max.Y <= 4.0 + 1e-3:
            region = "exception: flange hole crown"
        rows.append({"kind": kind, "radius": r, "least_deg": round(least, 4), "region": region,
                     "min": [round(bb.min.X, 3), round(bb.min.Y, 3), round(bb.min.Z, 3)],
                     "max": [round(bb.max.X, 3), round(bb.max.Y, 3), round(bb.max.Z, 3)]})
    return rows


def _unpack(loc):
    if isinstance(loc, Result):
        return {"diameter": loc, "offset": loc, "length": loc, "through": loc}
    return loc


def check(step_path: Path, asm_path: Path | None, stl_path: Path | None, record_path: Path | None,
          variant: dict, scratch: Path, skip_path: bool = False) -> dict:
    G = Gates()
    facts: dict = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    timings: dict = {}
    t0 = time.time()
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

    # U-02, envelope_within_spec, D-02, REQ-03
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
              note="lying on the wall's outer face: y and z on the bed, x tall")
    G.add("REQ-03.min_x", env["min_x"], ">=", SPEC["min_x"], assumes=ASSUMES["REQ-03"])
    G.add("REQ-03.front_z", env["max_z"], "in", (SPEC["front_z"] - SPEC["front_tol"], SPEC["front_z"] + SPEC["front_tol"]),
          assumes=ASSUMES["REQ-03"])
    facts["envelope"] = {k: v.measured for k, v in env.items()}
    timings["envelope"] = round(time.time() - t0, 1)

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
    bores = census.detail.get("bores", []) if isinstance(census, Result) and census.detail else []
    facts["bores"] = bores
    bx = [b for b in bores if abs(abs(b["axis_dir"][0]) - 1.0) < 1e-6 and not b["through"]]
    by = [b for b in bores if abs(abs(b["axis_dir"][1]) - 1.0) < 1e-6 and b["through"]]
    G.add("U-05.bores_x_blind", Result("bores_along_x_blind", len(bx), "count"), "==", SPEC["bores_x_blind"])
    G.add("U-05.bores_y_through", Result("bores_along_y_through", len(by), "count"), "==", SPEC["bores_y_through"])
    cyls = _cyl_faces(one)
    along_x = [c for c in cyls if abs(abs(c["dir"][0]) - 1.0) < 1e-6]
    pins = [c for c in along_x if c["r"] < 1.5]
    d10 = [c for c in along_x if abs(c["r"] - 5.0) < 0.5]
    d6 = [c for c in along_x if abs(c["r"] - 3.0) < 0.5]
    G.add("U-05.pins", Result("convex_pin_faces_along_x", len(pins), "count"), "==", SPEC["pins_n"])
    G.add("U-05.standoffs_d10", Result("cyl_faces_r5_along_x", len(d10), "count"), "==", SPEC["standoffs_d10"])
    G.add("U-05.standoffs_d6", Result("cyl_faces_r3_along_x", len(d6), "count"), "==", SPEC["standoffs_d6"])
    s2 = math.sqrt(0.5)
    hyp = _planar(one, (s2, s2, 0.0))
    G.add("U-05.gussets", Result("gusset_hypotenuse_faces", len(hyp), "count"), "==", SPEC["gussets"])
    G.add("E-06.gussets", Result("gusset_hypotenuse_faces", len(hyp), "count"), "==", SPEC["gussets"],
          note="designer's reading of a reviewer row: four gussets tie the flange to the wall")
    slot_faces = []
    for f in one.faces():
        if f.geom_type.name != "PLANE":
            continue
        bb = f.bounding_box()
        if bb.min.X >= 73.0 - 1e-3 and bb.max.X <= 76.0 + 1e-3 and bb.min.Y >= 85.9 and bb.max.Y <= 90.1 \
                and (bb.max.Z - bb.min.Z) <= 2.1:
            n = f.normal_at()
            if abs(n.X) < 1e-6:
                slot_faces.append({"y": [bb.min.Y, bb.max.Y], "z": [bb.min.Z, bb.max.Z], "n": tuple(n)})
    slot_centres = sorted({round(0.5 * (s["z"][0] + s["z"][1]), 3) for s in slot_faces if abs(s["n"][1]) > 0.999})
    facts["slot_centres_z"] = slot_centres
    G.add("U-05.slot_faces", Result("slot_side_faces", len(slot_faces), "count"), "==", SPEC["slot_faces"])
    G.add("U-05.slots", Result("tie_slots", len(slot_centres), "count"), "==", SPEC["slots"])
    G.add("E-11.slots", Result("tie_slots", len(slot_centres), "count"), "==", SPEC["slots"], assumes=ASSUMES["E-11"],
          note="designer's reading of a reviewer row: four tie slots (two pairs) through the wall above the board")
    timings["census"] = round(time.time() - t0, 1)

    # REQ-01, D-04a: flange holes; underside
    hole_axes = {}
    for x, z in SPEC["holes"]:
        tag = f"x{x:g}_z{z:g}"
        loc = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (x, 2.0, z), (0, 1, 0)))
        G.add(f"REQ-01.{tag}.diameter", loc["diameter"], "in", (SPEC["hole_d"] - SPEC["hole_tol"],
                                                                SPEC["hole_d"] + SPEC["hole_tol"]), assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.{tag}.length", loc["length"], "in", (SPEC["hole_len"] - SPEC["hole_len_tol"],
                                                            SPEC["hole_len"] + SPEC["hole_len_tol"]), assumes=ASSUMES["REQ-01"])
        G.add(f"REQ-01.{tag}.through", loc["through"], "==", 1, assumes=ASSUMES["REQ-01"])
        G.add(f"D-04a.{tag}.diameter", loc["diameter"], ">=", SPEC["hole_min_d"])
        st = loc["diameter"].at
        hole_axes[tag] = (float(st[0]), float(st[2])) if st is not None else (x, z)
    under = [f for f in _planar(one, (0, -1, 0)) if abs(-f["at"] - env["min_y"].measured) < 1e-4]
    facts["underside_faces"] = [{k: v for k, v in f.items() if k != "face"} for f in under]
    G.add("REQ-01.underside_faces", Result("planar_faces_at_min_y", len(under), "count"), "==", 1,
          assumes=ASSUMES["REQ-01"])
    if under:
        G.add("REQ-01.underside_y", Result("underside_y", -under[0]["at"], "mm", at=under[0]["min"]), "in",
              (SPEC["underside_y"] - SPEC["underside_tol"], SPEC["underside_y"] + SPEC["underside_tol"]),
              assumes=ASSUMES["REQ-01"])
    else:
        G.add("REQ-01.underside_y", inconclusive("underside_y", "mm", "no underside face"), "in", (-0.1, 0.1))

    # REQ-02: seat faces, insert bores, pins; D-05b, D-05a, J-05
    seats = [f for f in _planar(one, (1, 0, 0)) if 80.0 < f["at"] < 84.0]
    facts["seat_faces"] = [{k: v for k, v in f.items() if k != "face"} for f in seats]
    G.add("REQ-02.seat_faces", Result("seat_faces", len(seats), "count"), "==", SPEC["seat_faces"],
          assumes=ASSUMES["REQ-02"])
    for i, f in enumerate(sorted(seats, key=lambda r: (r["min"][2], r["min"][1]))):
        G.add(f"REQ-02.seat_{i + 1}.x", Result("seat_x", f["at"], "mm", at=f["min"]), "in",
              (SPEC["seat_x"] - SPEC["seat_tol"], SPEC["seat_x"] + SPEC["seat_tol"]), assumes=ASSUMES["REQ-02"])
    seat_x = float(np.mean([f["at"] for f in seats])) if seats else 82.438
    facts["seat_x_mean"] = seat_x
    if seats:
        G.add("REQ-02.seats_coplanar", Result("seat_x_spread", max(f["at"] for f in seats) - min(f["at"] for f in seats),
                                              "mm"), "<=", 0.0, assumes=ASSUMES["REQ-02"],
              note="the four seat faces lie on one plane")
    dlim = (SPEC["bore_d"] - SPEC["bore_tol"], SPEC["bore_d"] + SPEC["bore_tol"])
    hlim = (SPEC["bore_depth"] - SPEC["bore_depth_tol"], SPEC["bore_depth"] + SPEC["bore_depth_tol"])
    insert_axes = {}
    for y, z in SPEC["inserts"]:
        tag = f"y{y:g}_z{z:g}"
        loc = _unpack(_safe(locate_bore, "locate_bore", "mm", census, (seat_x - 3.0, y, z), (1, 0, 0)))
        for gid in ("REQ-02", "D-05b"):
            G.add(f"{gid}.insert_{tag}.diameter", loc["diameter"], "in", dlim, assumes=ASSUMES[gid])
            G.add(f"{gid}.insert_{tag}.depth", loc["length"], "in", hlim, assumes=ASSUMES[gid])
        G.add(f"D-05b.insert_{tag}.depth_min", loc["length"], ">=", SPEC["bore_min_depth"], assumes=ASSUMES["D-05b"])
        G.add(f"D-05b.insert_{tag}.blind", loc["through"], "==", 0, assumes=ASSUMES["D-05b"])
        G.add(f"REQ-02.insert_{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=ASSUMES["REQ-02"])
        det = loc["diameter"].detail or {}
        if det.get("start") is not None:
            s, e = np.array(det["start"], float), np.array(det["end"], float)
            insert_axes[tag] = (s, e)
            G.add(f"REQ-02.insert_{tag}.mouth_x", Result("bore_mouth_x", float(max(s[0], e[0])), "mm", at=det["start"]),
                  "in", (SPEC["seat_x"] - SPEC["seat_tol"], SPEC["seat_x"] + SPEC["seat_tol"]), assumes=ASSUMES["REQ-02"],
                  note="the bore opens on the seat")
            org = (73.0, float(s[1]), float(s[2]))
            xmid = 0.5 * (s[0] + e[0])
            rad = 0.5 * loc["diameter"].measured
            outs = {}
            for ang in (0.0, 90.0, 180.0, 270.0):
                outs[ang] = _safe(radial_extent, "radial_extent", "mm", one, org, (1, 0, 0), (0, 1, 0), ang,
                                  xmid - 73.0, side="outer", r_max=6.0)
            for a1, a2 in ((0.0, 180.0), (90.0, 270.0)):
                r1, r2 = outs[a1], outs[a2]
                if r1.measured is not None and r2.measured is not None:
                    across = Result("boss_across", r1.measured + r2.measured, "mm", at=[r1.at, r2.at])
                else:
                    across = inconclusive("boss_across", "mm", f"{r1.reason} {r2.reason}".strip())
                G.add(f"D-05a.insert_{tag}.across_{a1:g}_{a2:g}", across, ">=", SPEC["boss_across"],
                      assumes=ASSUMES["D-05a"])
            for ang, r in outs.items():
                w = (Result("wall_around_insert", r.measured - rad, "mm", at=r.at) if r.measured is not None
                     else inconclusive("wall_around_insert", "mm", r.reason or "no ray"))
                G.add(f"J-05.insert_{tag}.ray_{ang:g}", w, ">=", SPEC["wall_insert"])
        else:
            for ang in (0.0, 90.0, 180.0, 270.0):
                G.add(f"J-05.insert_{tag}.ray_{ang:g}", inconclusive("wall_around_insert", "mm", "bore not found"),
                      ">=", SPEC["wall_insert"])
    pin_axes = {}
    for y, z in SPEC["pins"]:
        tag = f"y{y:g}_z{z:g}"
        near = None
        for c in pins:
            off = _line_offset((seat_x, y, z), c["origin"], c["dir"])
            if near is None or off < near[0]:
                near = (off, c)
        if near is None:
            for k in ("diameter", "length", "offset"):
                G.add(f"REQ-02.pin_{tag}.{k}", inconclusive("pin", "mm", "no pin face"), "<=", 0.0)
            continue
        off, c = near
        pin_axes[tag] = c
        tops = [f for f in _planar(one, (1, 0, 0)) if f["at"] > seat_x + 0.5
                and abs(0.5 * (f["min"][1] + f["max"][1]) - c["origin"][1]) < 1.0
                and abs(0.5 * (f["min"][2] + f["max"][2]) - c["origin"][2]) < 1.0]
        length = (Result("pin_length", tops[0]["at"] - seat_x, "mm", at=tops[0]["min"]) if tops
                  else Result("pin_length", c["max"][0] - c["min"][0], "mm", at=c["min"]))
        G.add(f"REQ-02.pin_{tag}.diameter", Result("pin_diameter", 2.0 * c["r"], "mm", at=c["min"]), "in",
              (SPEC["pin_d"] - SPEC["pin_tol"], SPEC["pin_d"] + SPEC["pin_tol"]), assumes=ASSUMES["REQ-02"])
        G.add(f"REQ-02.pin_{tag}.length", length, "in", (SPEC["pin_len"] - SPEC["pin_len_tol"],
                                                          SPEC["pin_len"] + SPEC["pin_len_tol"]), assumes=ASSUMES["REQ-02"])
        G.add(f"REQ-02.pin_{tag}.offset", Result("pin_axis_offset", off, "mm", at=c["min"]), "<=", SPEC["offset_max"],
              assumes=ASSUMES["REQ-02"])
        facts[f"pin_{tag}"] = {"r": c["r"], "origin": c["origin"].tolist(), "x": [c["min"][0], c["max"][0]],
                               "top_faces": len(tops)}
    timings["features"] = round(time.time() - t0, 1)

    # D-01a, D-01b, D-06a, U-06 (Soft): the whole part, and the part without the two pins
    mw = _safe(min_wall, "min_wall", "mm", one, spacing=SPACING)
    G.add("D-01a", mw, ">=", SPEC["wall_floor"])
    G.add("D-06a", mw, ">=", SPEC["min_feature"], note="whole part: the pins are the thinnest feature")
    try:
        nopin = one
        for c in pins:
            nopin = nopin - _box(seat_x, seat_x + 5.0, c["origin"][1] - 1.5, c["origin"][1] + 1.5,
                                 c["origin"][2] - 1.5, c["origin"][2] + 1.5)
        nopin = _one(nopin.clean())
        facts["nopin_faces"] = len(nopin.faces())
        mwp = _safe(min_wall, "min_wall", "mm", nopin, spacing=SPACING)
        wwp = _safe(min_wall_wide, "min_wall_wide", "mm", nopin, spacing=SPACING)
    except Exception as exc:  # noqa: BLE001
        mwp = inconclusive("min_wall", "mm", f"{type(exc).__name__}: {exc}")
        wwp = mwp
    G.add("D-01b", mwp, ">=", SPEC["wall_struct"], note="the part without the two pins (D-01b exception)")
    G.add("U-06(Soft)", wwp, ">=", SPEC["wall_wide"], note="the part without the two pins")
    ww = _safe(min_wall_wide, "min_wall_wide", "mm", one, spacing=SPACING)
    facts["U-06.whole_part"] = _res(ww)
    timings["walls"] = round(time.time() - t0, 1)

    # D-03a outside the named exception: the four flange holes refilled by position
    try:
        filled = one
        for tag, (hx, hz) in hole_axes.items():
            filled = filled + _ycyl(hx, hz, 0.5 * SPEC["hole_d"] + 0.1, 0.0, 4.0)
        filled = filled.clean()
        nf, ns = len(filled.faces()), len(filled.solids())
        facts["D-03a.refilled"] = {"faces": nf, "solids": ns}
        if ns != 1 or nf != SPEC["refilled_faces"] or len(hole_axes) != 4:
            oh = inconclusive("overhang_census", "deg", f"refill not as planned: {nf} faces, {ns} solids")
        else:
            oh = _safe(overhang_census, "overhang_census", "deg", _one(filled), build_dir=SPEC["build_dir"],
                       spacing=SPACING)
    except Exception as exc:  # noqa: BLE001
        oh = inconclusive("overhang_census", "deg", f"{type(exc).__name__}: {exc}")
    G.add("D-03a", oh, ">=", SPEC["overhang_deg"], assumes=ASSUMES["D-03a"],
          note="outside the named exception: the four flange holes refilled by position")
    oh_all = _safe(overhang_census, "overhang_census", "deg", one, build_dir=SPEC["build_dir"], spacing=SPACING)
    facts["D-03a.whole_part"] = _res(oh_all) | {"detail": {k: v for k, v in (oh_all.detail or {}).items()
                                                           if not isinstance(v, list)}}
    down = _down_faces(one, env["min_x"].measured)
    facts["down_faces"] = down
    regions: dict = {}
    for r in down:
        regions.setdefault(r["region"], []).append(r["least_deg"])
    facts["down_face_regions_least_deg"] = {k: {"faces": len(v), "least_deg": min(v)} for k, v in regions.items()}
    # D-03b designer's reading
    fcs = _safe(flat_ceiling_spans, "flat_ceiling_spans", "mm", one, build_dir=SPEC["build_dir"],
                max_span=SPEC["bridge_span"], spacing=SPACING)
    G.add("D-03b.flat_ceilings", fcs, "<=", SPEC["bridge_span"], assumes=ASSUMES["D-03b"],
          note="reviewer row; designer's reading: flat ceilings in the print")
    widest = max((b["diameter"] for b in by), default=None)
    G.add("D-03b.horizontal_holes", Result("horizontal_hole_bridge", widest, "mm") if widest is not None
          else inconclusive("horizontal_hole_bridge", "mm", "no hole"), "<=", SPEC["bridge_span"],
          assumes=ASSUMES["D-03b"], note="reviewer row; designer's reading: the Ø3.4 holes bridge their diameter")
    timings["print"] = round(time.time() - t0, 1)

    # Assembly rows: U-03 (a), (b), D-04c, D-04d, E-01, E-05, REQ-04, REQ-05
    if asm_path is not None and asm_path.exists():
        asm = read_step(asm_path)
        kids = _children(asm)
        facts["assembly_labels"] = sorted(kids)
        tray = kids.get(LABELS["tray"])
        board = kids.get(LABELS["board"])
        plate = kids.get(LABELS["plate"])
        c02 = kids.get(LABELS["c02"])
        missing = [k for k, v in (("tray", tray), ("board", board), ("plate", plate), ("c02", c02)) if v is None]
        if missing:
            G.add("U-03.assembly", inconclusive("assembly", "count", f"missing {missing}"), "==", 0)
        else:
            tray, board, plate, c02 = (_one(s) for s in (tray, board, plate, c02))
            A = ASSUMES["U-03"]
            # flange on the plate
            G.add("U-03.plate.clearance", _safe(clearance, "clearance", "mm", tray, plate), "==", SPEC["contact"],
                  assumes=A, note="designed contact: the flange's underside on OD-C01's top face")
            G.add("U-03.plate.interference", _safe(common_volume, "common_volume", "mm3", tray, plate), "<=",
                  SPEC["interference"], assumes=A)
            # the board: interference, seats, pins, the rest
            tb = time.time()
            iv = _safe(common_volume, "common_volume", "mm3", tray, board)
            timings["tray_board_common_s"] = round(time.time() - tb, 1)
            G.add("U-03.board.interference", iv, "<=", SPEC["interference"], assumes=A)
            seat_parts, columns = [], []
            for f in seats:
                cy = 0.5 * (f["min"][1] + f["max"][1])
                cz = 0.5 * (f["min"][2] + f["max"][2])
                h = 0.5 * max(f["max"][1] - f["min"][1], f["max"][2] - f["min"][2]) + STANDOFF_MARGIN
                columns.append(_box(76.0, seat_x + 5.0, cy - h, cy + h, cz - h, cz + h))
                try:
                    sp = tray & _box(seat_x - 1.0, seat_x, cy - h, cy + h, cz - h, cz + h)
                    seat_parts.append(((cy, cz), _one(sp)))
                except Exception as exc:  # noqa: BLE001
                    seat_parts.append(((cy, cz), exc))
            for (cy, cz), sp in seat_parts:
                tag = f"y{cy:.2f}_z{cz:.2f}"
                r = (inconclusive("clearance", "mm", f"{type(sp).__name__}: {sp}") if isinstance(sp, Exception)
                     else _safe(clearance, "clearance", "mm", sp, board))
                G.add(f"U-03.seat_{tag}.clearance", r, "==", SPEC["contact"], assumes=A,
                      note="designed contact: the solder face on the standoff's seat (top 1.0 of the standoff)")
            for tag, c in pin_axes.items():
                try:
                    pin_solid = _one(tray & _box(seat_x, seat_x + 5.0, c["origin"][1] - 1.5, c["origin"][1] + 1.5,
                                                 c["origin"][2] - 1.5, c["origin"][2] + 1.5))
                    r = _safe(clearance, "clearance", "mm", pin_solid, board)
                except Exception as exc:  # noqa: BLE001
                    r = inconclusive("clearance", "mm", f"{type(exc).__name__}: {exc}")
                for gid in ("U-03", "D-04d"):
                    G.add(f"{gid}.pin_{tag}.clearance", r, ">=", SPEC["pin_gap"],
                          assumes=A if gid == "U-03" else ASSUMES["D-04d"],
                          note="the pin (above the seat plane) to the board solid: the gap to the hole's wall")
            try:
                rest = tray
                for col in columns:
                    rest = rest - col
                rest = _one(rest.clean())
                rr = _safe(clearance, "clearance", "mm", rest, board)
            except Exception as exc:  # noqa: BLE001
                rr = inconclusive("clearance", "mm", f"{type(exc).__name__}: {exc}")
            for gid in ("U-03", "D-04c", "E-01"):
                G.add(f"{gid}.rest.clearance", rr, ">=", SPEC["keepout"],
                      assumes=A if gid == "U-03" else ASSUMES[gid],
                      note="the tray less the four standoff columns (x >= 76, radius + 0.5) to the board")
            try:
                sub = tray
                for c in pins:
                    sub = sub - _box(seat_x, seat_x + 5.0, c["origin"][1] - 1.5, c["origin"][1] + 1.5,
                                     c["origin"][2] - 1.5, c["origin"][2] + 1.5)
                for f in seats:
                    cy = 0.5 * (f["min"][1] + f["max"][1])
                    cz = 0.5 * (f["min"][2] + f["max"][2])
                    h = 0.5 * max(f["max"][1] - f["min"][1], f["max"][2] - f["min"][2]) + STANDOFF_MARGIN
                    sub = sub - _box(seat_x - 1.0, seat_x, cy - h, cy + h, cz - h, cz + h)
                sub = _one(sub.clean())
                facts["rest_with_columns_below_seat_layer.clearance"] = _res(clearance(sub, board))
            except Exception as exc:  # noqa: BLE001
                facts["rest_with_columns_below_seat_layer.clearance"] = f"{type(exc).__name__}: {exc}"
            # neighbours and the zone
            G.add("U-03.c02.tray_clearance", _safe(clearance, "clearance", "mm", tray, c02), ">=",
                  SPEC["c02_gap_tray"], assumes=A)
            G.add("U-03.c02.board_clearance", _safe(clearance, "clearance", "mm", board, c02), ">=",
                  SPEC["c02_gap_board"], assumes=A)
            be = envelope(board)
            facts["board_envelope"] = {k: v.measured for k, v in be.items()}
            G.add("U-03.board_zone.min_x", be["min_x"], ">=", SPEC["zone_x"][0], assumes=A)
            G.add("U-03.board_zone.max_x", be["max_x"], "<=", SPEC["zone_x"][1], assumes=A)
            G.add("U-03.board_zone.min_z", be["min_z"], ">=", SPEC["zone_z"][0], assumes=A)
            G.add("U-03.board_zone.max_z", be["max_z"], "<=", SPEC["zone_z"][1], assumes=A)
            G.add("U-03.board_zone.min_y", be["min_y"], ">=", SPEC["zone_min_y"], assumes=A)
            # plate material under each flange hole (A-01)
            pc = _safe(bore_census, "bore_census", "count", plate)
            pbores = pc.detail.get("bores", []) if isinstance(pc, Result) and pc.detail else []
            facts["plate_bores"] = len(pbores)
            rh = 0.5 * SPEC["hole_d"]
            for tag, (hx, hz) in hole_axes.items():
                foot = _ycyl(hx, hz, rh, -SPEC["plate_t"], 0.0)
                vfoot = math.pi * rh * rh * SPEC["plate_t"]
                cv = _safe(common_volume, "common_volume", "mm3", foot, plate)
                miss = (Result("plate_missing_under_hole", vfoot - cv.measured, "mm3", at=[hx, -3.0, hz])
                        if cv.measured is not None else cv)
                G.add(f"U-03.plate_under_{tag}.missing_volume", miss, "<=", 0.0, assumes=ASSUMES["U-03.plate"],
                      note="the hole's footprint (Ø3.4 through the 6.0 plate) over solid plate")
                G.add(f"REQ-01.plate_under_{tag}.missing_volume", miss, "<=", 0.0, assumes=ASSUMES["REQ-01"])
                gaps = []
                for b in pbores:
                    s, e = np.array(b["start"], float), np.array(b["end"], float)
                    d = _line_offset((hx, -3.0, hz), s, e - s) - 0.5 * b["diameter"] - rh
                    gaps.append((d, [round(v, 3) for v in s]))
                if pbores:
                    gmin = min(gaps)
                    hg = Result("plate_hole_gap", gmin[0], "mm", at=gmin[1])
                else:
                    hg = inconclusive("plate_hole_gap", "mm", "no plate bores read")
                G.add(f"U-03.plate_under_{tag}.hole_gap", hg, ">=", SPEC["plate_hole_gap"], assumes=ASSUMES["U-03.plate"])
                G.add(f"REQ-01.plate_under_{tag}.hole_gap", hg, ">=", SPEC["plate_hole_gap"], assumes=ASSUMES["REQ-01"])
                edges = []
                for ang in range(0, 360, 45):
                    r = _safe(radial_extent, "radial_extent", "mm", plate, (hx, 0.0, hz), (0, -1, 0), (1, 0, 0),
                              float(ang), 3.0, side="outer", r_max=600.0)
                    if r.measured is not None:
                        edges.append((r.measured - rh, ang, r.at))
                if len(edges) == 8:
                    e0 = min(edges)
                    eg = Result("plate_edge_gap", e0[0], "mm", at=e0[2], detail={"angle_deg": e0[1]})
                else:
                    eg = inconclusive("plate_edge_gap", "mm", f"{8 - len(edges)} rays unread")
                G.add(f"U-03.plate_under_{tag}.edge_gap", eg, ">=", SPEC["plate_edge_gap"], assumes=ASSUMES["U-03.plate"])
                G.add(f"REQ-01.plate_under_{tag}.edge_gap", eg, ">=", SPEC["plate_edge_gap"], assumes=ASSUMES["REQ-01"])
            # E-05: tray bores and pins against the board's holes, both measured
            bc = _safe(bore_census, "bore_census", "count", board)
            tc = _safe(bore_census, "bore_census", "count", tray)
            for name, (y, z) in (("H1", SPEC["inserts"][0]), ("H2", SPEC["inserts"][1])):
                bh = _unpack(_safe(locate_bore, "locate_bore", "mm", bc, (83.2, y, z), (1, 0, 0)))
                st = bh["diameter"].at
                if st is None:
                    G.add(f"E-05.{name}.offset", inconclusive("bore_axis_offset", "mm", "board hole not found"), "<=",
                          SPEC["coax"])
                    continue
                th = _unpack(_safe(locate_bore, "locate_bore", "mm", tc, (seat_x - 3.0, st[1], st[2]), (1, 0, 0)))
                G.add(f"E-05.{name}.offset", th["offset"], "<=", SPEC["coax"], assumes=ASSUMES["E-05"],
                      note=f"tray insert bore axis vs the board's {name} axis at (y {st[1]:.3f}, z {st[2]:.3f}), "
                           f"Ø{bh['diameter'].measured:.3f}")
            for name, (y, z), key in (("H5", SPEC["pins"][0], f"y{SPEC['pins'][0][0]:g}_z{SPEC['pins'][0][1]:g}"),
                                      ("H6", SPEC["pins"][1], f"y{SPEC['pins'][1][0]:g}_z{SPEC['pins'][1][1]:g}")):
                bh = _unpack(_safe(locate_bore, "locate_bore", "mm", bc, (83.2, y, z), (1, 0, 0)))
                st = bh["diameter"].at
                c = pin_axes.get(key)
                if st is None or c is None:
                    G.add(f"E-05.{name}.offset", inconclusive("pin_axis_offset", "mm", "hole or pin not found"), "<=",
                          SPEC["coax"])
                    continue
                off = _line_offset((83.2, st[1], st[2]), c["origin"], c["dir"])
                G.add(f"E-05.{name}.offset", Result("pin_axis_offset", off, "mm", at=st), "<=", SPEC["coax"],
                      assumes=ASSUMES["E-05"], note=f"pin axis vs the board's {name} axis, hole "
                                                    f"Ø{bh['diameter'].measured:.3f}")
                facts[f"E-05.{name}.hole_diameter"] = bh["diameter"].measured
            # REQ-04: drivers
            for tag, (hx, hz) in hole_axes.items():
                drv = _ycyl(hx, hz, SPEC["driver_r"], SPEC["driver_y"][0], SPEC["driver_y"][1])
                G.add(f"REQ-04.{tag}.tray", _safe(common_volume, "common_volume", "mm3", drv, tray), "<=", 0.0,
                      assumes=ASSUMES["REQ-04"])
                G.add(f"REQ-04.{tag}.board", _safe(common_volume, "common_volume", "mm3", drv, board), "<=", 0.0,
                      assumes=ASSUMES["REQ-04"])
                facts[f"REQ-04.{tag}.board_clearance"] = _res(_safe(clearance, "clearance", "mm", drv, board))
            # REQ-05: faston access
            (x0, x1), (y0, y1), (z0, z1) = SPEC["faston_box"]
            fb = _box(x0, x1, y0, y1, z0, z1)
            G.add("REQ-05.box", _safe(common_volume, "common_volume", "mm3", fb, tray), "<=", 0.0,
                  assumes=ASSUMES["REQ-05"])
            G.add("E-11.open_plus_x", _safe(common_volume, "common_volume", "mm3", fb, tray), "<=", 0.0,
                  assumes=ASSUMES["E-11"], note="designer's reading: nothing of the tray over the board on +X")
            timings["assembly_a"] = round(time.time() - t0, 1)
            # U-03 (b): the board slid along -X onto the pins from +5.0
            if skip_path:
                G.fixed("U-03(b)", INCONCLUSIVE, "<= 0 mm3 at each step", "path not run in this sweep run")
            else:
                n = int(round(SPEC["path_from"] / SPEC["path_step"]))
                worst_iv, worst_cl, path = None, None, []
                for i in range(n, -1, -1):
                    d = i * SPEC["path_step"]
                    moved = board.moved(Location((d, 0.0, 0.0)))
                    ivd = _safe(common_volume, "common_volume", "mm3", tray, moved)
                    cld = _safe(clearance, "clearance", "mm", tray, moved)
                    path.append({"dx": d, "interference_mm3": ivd.measured, "status": ivd.status,
                                 "reason": ivd.reason, "clearance_mm": cld.measured})
                    if ivd.measured is None:
                        worst_iv = ivd
                        break
                    if worst_iv is None or (worst_iv.measured is not None and ivd.measured > worst_iv.measured):
                        worst_iv = Result("path_interference", ivd.measured, "mm3", at=[d, 0, 0])
                facts["U-03(b).path"] = path
                G.add("U-03(b).interference_max", worst_iv if worst_iv is not None else
                      inconclusive("path_interference", "mm3", "no step"), "<=", 0.0, assumes=A,
                      note=f"{len(path)} poses, +{SPEC['path_from']} to 0 along -X in steps of {SPEC['path_step']}")
                timings["path"] = round(time.time() - t0, 1)
    else:
        G.add("U-03.assembly", inconclusive("assembly", "count", "no assembly file"), "==", 0)

    # U-04: part and assembly round trip against the build
    try:
        import build_od_c08_tray as B
        p = B.Params(**variant)
        built = B.build_tray(p)
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
            elif k == "labels":
                G.add("U-04.part.labels", v, "==", 1)
            else:
                facts[f"U-04.part.{k}"] = _res(v)
        if asm_path is not None and asm_path.exists():
            ba = B.build_assembly(p)["assembly"]
            ra = compare_step(ba, asm_path)
            for k, v in ra.items():
                facts[f"U-04.assembly.{k}"] = _res(v)
            G.add("U-04.assembly.solids", ra["solids"], "==", 4)
            G.add("U-04.assembly.faces_delta", ra["faces_delta"], "==", 0)
            G.add("U-04.assembly.labels", ra["labels"], "==", 1)
            G.add("U-04.assembly.valid_after", ra["valid_after"], "==", 1)
    except Exception as exc:  # noqa: BLE001
        G.add("U-04.part", inconclusive("compare_step", "", f"{type(exc).__name__}: {exc}"), "==", 0)
        facts["U-04.traceback"] = traceback.format_exc()
    timings["roundtrip"] = round(time.time() - t0, 1)

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
        tol_used = rec.get("stl", {}).get("tolerance", None)
        G.add("U-07.tolerance", Result("stl_tolerance", tol_used, "mm") if tol_used is not None
              else inconclusive("stl_tolerance", "mm", "no build record"), "<=", SPEC["stl_tol"])
        G.add("U-07.angular_tolerance", Result("stl_angular_tolerance", ang, "rad") if ang is not None
              else inconclusive("stl_angular_tolerance", "rad", "no build record"), "<=", SPEC["stl_ang_max"])
        G.add("U-07.build_sagitta", Result("stl_max_sagitta", rec.get("stl", {}).get("max_sagitta"), "mm")
              if rec.get("stl", {}).get("max_sagitta") is not None
              else inconclusive("stl_max_sagitta", "mm", "no build record"), "<=", SPEC["stl_tol"],
              note="measured by write_stl when the delivered STL was written")
        scratch.mkdir(parents=True, exist_ok=True)
        w = _safe(write_stl, "write_stl", "mm", one, scratch / "remesh_check.stl", tolerance=SPEC["stl_tol"],
                  angular_tolerance=ang or 0.2)
        sag = w.checks["max_sagitta"] if hasattr(w, "checks") else w
        G.add("U-07.max_sagitta", sag, "<=", SPEC["stl_tol"],
              note="re-meshed from the re-imported STEP at the build's settings")
    else:
        G.add("U-07", inconclusive("mesh", "mm", "no STL"), "<=", SPEC["stl_tol"])

    # by the rows
    G.fixed("U-08", "N/A", "N/A", "no threads (N/A by its row)")
    G.fixed("D-07", "N/A", "N/A", "no fit-critical bores (N/A by its row)")
    G.fixed("REQ-06(Soft)", INCONCLUSIVE, "bench", "Soft bench gate: not geometric, answered at the first assembly",
            assumes=("A-04", "A-12"))
    mp = mass_properties(one, SPEC["density"])
    facts["mass"] = {k: v.measured for k, v in mp.items()}
    facts["timings_s"] = timings
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
    ap.add_argument("--skip-path", action="store_true")
    a = ap.parse_args()

    def rel(s):
        if s is None:
            return None
        q = Path(s)
        return q if q.is_absolute() else WS / q
    out = check(rel(a.step), rel(a.asm), rel(a.stl), rel(a.record), json.loads(a.variant), rel(a.scratch),
                skip_path=a.skip_path)
    rel(a.out).write_text(json.dumps(out, indent=1, default=str))
    for r in out["gates"]:
        print(f"{r['gate']:<52} {r['status']:<13} {r.get('measured')!s:<22} {r.get('required')!s:<24} "
              f"{r.get('margin')!s:<12} {r.get('reason', '')[:80]}")
    print(json.dumps(out["facts"].get("timings_s", {})))


if __name__ == "__main__":
    main()
