"""Checks for od_c09_front (job 20261002-od-c09-front-panel, concept C1, spec 1.1 section 5).

Written before the build (PLAYBOOK D3). Every predicate re-imports the exported STEP,
measures it with tools.measure / tools.core, and compares with tools.result.gate using
the one tolerance band of atolye/GATES.md section 0. Thresholds are the spec 1.1 section 5
values, collected in SPEC below with the clause they come from. A measurement that raises
or returns nothing is INCONCLUSIVE, never PASS.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c09_front.py [--step <path>] [--stl <path>]
        [--out <json>] [--quick] [--params <json of build overrides>]
--quick skips nothing gated; it only skips writing section pictures (the sweep never writes them).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import tempfile
import time
from itertools import combinations
from pathlib import Path

from build123d import Box, Compound, Cylinder, Pos, Rot, Solid
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.GeomAbs import GeomAbs_Cylinder, GeomAbs_Plane
from OCP.gp import gp_Ax1, gp_Ax3, gp_Dir, gp_Lin, gp_Pnt, gp_Trsf, gp_Vec
from OCP.IntCurvesFace import IntCurvesFace_ShapeIntersector
from OCP.TopAbs import TopAbs_IN, TopAbs_ON, TopAbs_OUT, TopAbs_REVERSED

from tools.core import (brep_valid, common_volume, compare_step, read_step, solid_count, solids,
                        validity, write_stl)
from tools.core.shapes import faces
from tools.measure import (bore_census, clearance, envelope, feature_census, flat_ceiling_spans,
                           interference, locate_bore, min_wall, min_wall_wide, overhang_census,
                           radial_extent, radial_profile)
from tools.result import FAIL, INCONCLUSIVE, MEASURED, PASS, PASS_ASSUMED, Result, gate, inconclusive

WS = Path(__file__).resolve().parents[1]
INP = WS / "00_Spec" / "inputs"
PART = "od_c09_front"
STEP_DEFAULT = WS / "02_STEP_STL" / "od_c09_front_C1_v01.step"
STL_DEFAULT = WS / "02_STEP_STL" / "od_c09_front_C1_v01.stl"

# GATES.md section 0 bands, in the result's own unit
BAND_MM, BAND_MM3, BAND_DEG, BAND_COUNT = 0.005, 0.001, 0.001, 0

# Spec 1.1 thresholds and stated geometry (clause in the comment). Nothing below this block
# carries a threshold of its own.
SPEC = {
    "envelope_size": (232.0, 215.0, 25.0), "envelope_tol": 0.1,                  # U-02
    "envelope_pos": {"min_x": -116.0, "max_x": 116.0, "min_y": 0.0, "max_y": 215.0,
                     "min_z": 72.0, "max_z": 97.0},                               # U-02 (reported apart)
    "bed_volume": (420.0, 420.0, 500.0),                                         # D-02, A-10
    "footprint_edge_min": 0.5,                                                    # U-03 (a)
    "flange_to_hole_min": 3.0, "foot_to_hole_min": 2.0, "hole_centre_min": 6.0,  # U-03 (a)
    "brew_area_min": 2.0,                                                         # U-03 (a)
    "c15_keepouts": [(-110.0, 90.0), (110.0, 90.0)], "c15_d": 8.0, "c15_y": (0.0, 2.0),  # U-03 (a)
    "lower_from": 40.0, "lower_step": 2.0,                                        # U-03 (b)
    "wall_d01a": 0.8, "wall_d01b": 2.0, "wall_d06a": 1.0, "wall_u06": 2.0,        # D-01a, D-01b, D-06a, U-06
    "stl_tol": 0.01,                                                              # U-07
    "overhang_min_deg": 45.0, "bridge_max": 5.0,                                  # D-03a, D-03b
    "flange_hole_min_d": 3.25,                                                    # D-04a
    "insert_across_min": 8.0, "insert_d": (3.95, 4.05), "insert_depth": (5.9, 6.1),  # D-05a, D-05b
    "insert_wall_min": 3.0,                                                       # J-05
    "board_keepout": 0.5,                                                         # E-01
    "board_hole_offset_max": 0.10,                                                # E-05
    "flange_holes": [(-95.0, 77.0), (-85.0, 77.0), (85.0, 77.0), (95.0, 77.0)],   # REQ-01 (x, z)
    "flange_hole_d": (3.3, 3.5), "flange_hole_len": (3.9, 4.1), "flange_hole_offset_max": 0.10,
    "underside_y": (-0.10, 0.10),                                                 # REQ-01
    "wall_out_z": (96.9, 97.1), "wall_in_z": (93.9, 94.1), "wall_x": 116.0, "wall_top_y": (214.9, 215.1),  # REQ-02
    "req02_levels_y": (100.0, 200.0),
    "slot": {"x": (-75.0, 75.0), "y": (0.0, 50.0)}, "window": {"x": (-57.5, 75.0), "y": (0.0, 188.0)},  # REQ-03
    "opening_edge_tol": 0.1, "opening_shrink": 0.2, "opening_z": (93.8, 97.2), "section_z": 95.5,
    "b2_foremost_min": 97.5, "side_cap_foremost_min": 95.0, "button_offset_max": 0.25,  # REQ-04
    "phi_range": (-55.0, 10.0), "phi_step": 5.0, "g10_gap_min": 2.0,              # REQ-05 (a)
    "carry_phi": -50.0, "carry_drop": 15.0, "carry_z": (32.0, 182.0), "carry_step": 5.0,  # REQ-05 (b)
    "driver_r": 3.0, "driver_y_top": 260.0, "flange_driver_y0": 4.0, "c15_driver_y0": 2.0,  # REQ-06
    "tray_box": {"x": (-74.8, 74.8), "y": (0.0, 49.8), "z": (-15.0, 120.0)},      # REQ-07
    "knob": {"x": 95.5, "y": 140.0, "d": 32.0, "z": (60.0, 93.8)}, "min_z": 72.0,
}

# the underside is read on the faces turned to -Y below the flanges' top (spec 4: flanges 4.0 thick)
UNDERSIDE_BAND_Y = 4.0

# Spec section 2 poses (machine frame = OD-C01 frame)
HOUSING_POSE = ((0.0, 180.06, 32.0), (1, 0, 0), (0, -1, 0))      # origin, source +x -> , source +z ->
BOARD_POSE = ((-99.0, 140.0, 69.35), (0, -1, 0), (0, 0, -1))
HOUSING_AXIS = ((0.0, 0.0, 32.0), (0.0, 1.0, 0.0))                # OD-G10 phi rotation axis (x 0, z 32, along Y)


# ----------------------------------------------------------------------------- placement
def trsf(origin, x_to, z_to) -> gp_Trsf:
    """Map a source frame onto the machine frame: source +x goes to x_to, +z to z_to."""
    t = gp_Trsf()
    t.SetTransformation(gp_Ax3(gp_Pnt(*origin), gp_Dir(*z_to), gp_Dir(*x_to)), gp_Ax3())
    return t


def place(shape, t: gp_Trsf):
    w = shape.wrapped if hasattr(shape, "wrapped") else shape
    return BRepBuilderAPI_Transform(w, t, True).Shape()


def moved(shape, dx=0.0, dy=0.0, dz=0.0):
    t = gp_Trsf()
    t.SetTranslation(gp_Vec(dx, dy, dz))
    return Solid(place(shape, t))


def g10_pose(g10, phi_deg, dy=0.0, dz=0.0):
    rot = gp_Trsf()
    rot.SetRotation(gp_Ax1(gp_Pnt(*HOUSING_AXIS[0]), gp_Dir(*HOUSING_AXIS[1])), math.radians(phi_deg))
    shift = gp_Trsf()
    shift.SetTranslation(gp_Vec(0.0, dy, dz))
    return Solid(place(g10, shift.Multiplied(rot)))


def load_refs() -> dict:
    """Every reference solid placed by spec section 2, never by a bounding box."""
    housing_t, board_t = trsf(*HOUSING_POSE), trsf(*BOARD_POSE)
    refs = {"C01": Solid(solids(read_step(INP / "OD-C01_base_frame.step"))[0]),
            "C05": Solid(solids(place(read_step(INP / "OD-C05_group_head_carrier.step"), housing_t))[0]),
            "C10": Solid(solids(read_step(INP / "OD-C10_top_panel.step"))[0]),
            "E02": Solid(solids(place(read_step(INP / "OD-E02_control_board.step"), board_t))[0])}
    asm = [Solid(s) for s in solids(place(read_step(INP / "od_g01_assembly_C1_v03.step"), housing_t))]
    housing_alone = Solid(solids(place(read_step(INP / "od_g01_housing_C1_v03.step"), housing_t))[0])
    # identify by measurement: OD-G10 reaches furthest toward the user (+Z, housing y ~ 150);
    # the housing is the solid whose volume matches the housing-alone file; OD-G04 the rest
    g10 = max(asm, key=lambda s: s.bounding_box().max.Z)
    rest = [s for s in asm if s is not g10]
    housing = min(rest, key=lambda s: abs(s.volume - housing_alone.volume))
    g04 = [s for s in rest if s is not housing][0]
    refs.update(housing=housing, G04=g04, G10=g10)
    refs["_ident"] = {"G10_max_z": g10.bounding_box().max.Z, "housing_volume": housing.volume,
                      "housing_alone_volume": housing_alone.volume, "G04_volume": g04.volume}
    return refs


# ----------------------------------------------------------------------------- helpers
def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def cyl_z(cx, cy, r, z0, z1):
    return Pos(cx, cy, (z0 + z1) / 2) * Cylinder(r, z1 - z0)


def cyl_y(cx, cz, r, y0, y1):
    return Pos(cx, (y0 + y1) / 2, cz) * Rot(90, 0, 0) * Cylinder(r, y1 - y0)


def clip(shape, region):
    out = shape & region
    parts = [s for s in (out.solids() if out is not None else []) if s.volume > 1e-9]
    if not parts:
        raise ValueError("the clip region holds no material")
    return Compound(parts) if len(parts) > 1 else parts[0]


def classify(solid, p) -> str:
    c = BRepClass3d_SolidClassifier(solid.wrapped, gp_Pnt(*p), 1e-7)
    return {TopAbs_IN: "IN", TopAbs_ON: "ON", TopAbs_OUT: "OUT"}.get(c.State(), "UNKNOWN")


def line_hits(solid, origin, direction) -> list[float]:
    """Parameters of every exact line-solid hit along a line (sorted)."""
    it = IntCurvesFace_ShapeIntersector()
    it.Load(solid.wrapped, 1e-7)
    it.Perform(gp_Lin(gp_Pnt(*origin), gp_Dir(*direction)), -1e4, 1e4)
    if not it.IsDone():
        raise RuntimeError("line intersection did not finish")
    return sorted(it.WParameter(i) for i in range(1, it.NbPnt() + 1))


def fact(name, value: bool, at=None, detail=None) -> Result:
    return Result(name, int(bool(value)), "bool", at=at, detail=detail or {})


def num(name, value, unit="mm", at=None, detail=None) -> Result:
    return Result(name, float(value), unit, at=at, detail=detail or {})


def guarded(name, unit, fn):
    try:
        return fn()
    except Exception as exc:  # noqa: BLE001: a check never raises
        return inconclusive(name, unit, f"{type(exc).__name__}: {exc}")


class Rows:
    def __init__(self):
        self.rows = []

    def add(self, gate_id, item, result, op, limit, band, assumes=(), required=None, note=""):
        try:
            g = gate(gate_id, result, op, limit, band=band, assumes=assumes, required=required)
            row = {**g.row(), "item": item, "reason": g.reason, "note": note}
        except Exception as exc:  # noqa: BLE001
            row = {"gate": gate_id, "item": item, "measured": None, "unit": getattr(result, "unit", ""),
                   "required": str(limit), "margin": None, "at": None, "status": INCONCLUSIVE,
                   "method": getattr(result, "name", "?"), "assumes": list(assumes),
                   "reason": f"{type(exc).__name__}: {exc}", "note": note}
        self.rows.append(row)
        return row

    def literal(self, gate_id, item, status, measured=None, unit="", required="", note="", assumes=()):
        self.rows.append({"gate": gate_id, "item": item, "measured": measured, "unit": unit,
                          "required": required, "margin": None, "at": None, "status": status,
                          "method": "row", "assumes": list(assumes), "reason": note, "note": note})

    def separated(self, gate_id, item, a, b, assumes=(), note="", cache=None):
        """Spec REQ-05 / Q6 fallback for an unsound solid: clearance > 0 and not inside."""
        r = cache.clearance(item, a, b) if cache is not None else clearance(a, b)
        if r.status != MEASURED:
            return self.add(gate_id, item, r, ">=", 0.0, BAND_MM, assumes)
        ok = r.measured > 0.0 and not r.detail.get("inside", True)
        res = fact("separated_clearance_gt_0_not_inside", ok, at=r.at,
                   detail={"clearance_mm": r.measured, "inside": r.detail.get("inside")})
        row = self.add(gate_id, item, res, "==", 1, BAND_COUNT, assumes,
                       required="clearance > 0 and inside == False", note=note)
        row["clearance_mm"] = r.measured
        return row


# ----------------------------------------------------------------------------- panel-independent cache
class RefCache:
    """Optional cache (sweep only) for measurements that do not involve the panel: the
    clearance between two reference solids at a pose. Keyed by the SHA-256 of the input
    STEPs, so a changed input is measured afresh. Without --cache every value is measured."""

    def __init__(self, path):
        self.path = Path(path) if path else None
        from tools.core.step import file_sha256
        self.inputs = {n: file_sha256(INP / n) for n in ("OD-E02_control_board.step", "od_g01_assembly_C1_v03.step",
                                                          "OD-C01_base_frame.step", "OD-C05_group_head_carrier.step",
                                                          "OD-C10_top_panel.step", "od_g01_housing_C1_v03.step")} \
            if self.path else {}
        self.data = {}
        d = self._read()
        if d.get("inputs") == self.inputs:
            self.data = d.get("values", {})

    def _read(self) -> dict:
        try:
            return json.loads(self.path.read_text()) if self.path and self.path.exists() else {}
        except (OSError, ValueError):
            return {}

    def clearance(self, key, a, b):
        if self.path is None:
            return clearance(a, b)
        if key in self.data:
            v = self.data[key]
            return Result("clearance", v["measured"], "mm", at=tuple(v["at"]) if v["at"] else None,
                          detail={"inside": v["inside"], "cached": True})
        r = clearance(a, b)
        if r.status == MEASURED:
            self.data[key] = {"measured": r.measured, "at": list(r.at) if r.at else None,
                              "inside": r.detail.get("inside")}
            cur = self._read()
            vals = cur.get("values", {}) if cur.get("inputs") == self.inputs else {}
            vals.update(self.data)
            tmp = self.path.with_name(f"{self.path.name}.{os.getpid()}.tmp")
            tmp.write_text(json.dumps({"inputs": self.inputs, "values": vals}, indent=0))
            tmp.replace(self.path)
        return r


# ----------------------------------------------------------------------------- the checks
ALL_STAGES = ("assembly", "motion", "process")


def run(step_path: Path, stl_path: Path | None, params_override: dict | None, sections: bool,
        timeline: list, stages=ALL_STAGES, cache_path=None) -> list[dict]:
    rows = Rows()
    rc = RefCache(cache_path)
    W = SPEC
    t0 = time.time()

    def lap(what):
        timeline.append((what, round(time.time() - t0, 1)))
        print("lap", what, round(time.time() - t0, 1), flush=True)

    shape = read_step(step_path)
    found = solids(shape)
    rows.add("exactly_one_solid", "solid_count", solid_count(shape), "==", 1, BAND_COUNT)
    v = validity(shape)
    rows.add("U-01", "solid_count", v["solid_count"], "==", 1, BAND_COUNT)
    rows.add("U-01", "brep_valid", v["brep_valid"], "==", 1, BAND_COUNT)
    rows.add("U-01", "naked_edges", v["naked_edges"], "==", 0, BAND_COUNT)
    if len(found) != 1:
        return rows.rows
    P = Solid(found[0])
    lap("validity")

    # ---- envelope: U-02, envelope_within_spec, D-02, REQ-02 extents, REQ-07 min z
    env = envelope(P)
    tol = SPEC["envelope_tol"]
    for axis, size in zip("xyz", SPEC["envelope_size"]):
        for gid in ("U-02", "envelope_within_spec"):
            rows.add(gid, f"size_{axis}", env[f"size_{axis}"], "in", (size - tol, size + tol), BAND_MM)
    for key, value in SPEC["envelope_pos"].items():
        rows.add("envelope_within_spec", f"position_{key}", env[key], "in", (value - tol, value + tol), BAND_MM,
                 note="position against the datum, reported apart from size")
    for axis, cap in zip("xyz", SPEC["bed_volume"]):
        rows.add("D-02", f"size_{axis}", env[f"size_{axis}"], "<=", cap, BAND_MM, ("A-10",))
    rows.add("REQ-02", "x_min", env["min_x"], "in", (-SPEC["wall_x"] - tol, -SPEC["wall_x"] + tol), BAND_MM, ("A-02",))
    rows.add("REQ-02", "x_max", env["max_x"], "in", (SPEC["wall_x"] - tol, SPEC["wall_x"] + tol), BAND_MM, ("A-02",))
    rows.add("REQ-02", "top_y", env["max_y"], "in", SPEC["wall_top_y"], BAND_MM, ("A-02",))
    rows.add("REQ-07", "min_z", env["min_z"], ">=", SPEC["min_z"], BAND_MM, ("A-06", "A-13"))
    lap("envelope")

    # ---- U-04 round trip: the STEP against a fresh build of the same parameters
    def roundtrip():
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import build_od_c09_front as bmod
        built = bmod.build(bmod.params_with(params_override or {}))
        return compare_step(built, step_path)
    rt = roundtrip()
    rows.add("U-04", "schema_AP242", rt["schema"], "==", 1, BAND_COUNT)
    rows.add("U-04", "solids", rt["solids"], "==", 1, BAND_COUNT)
    rows.add("U-04", "volume_delta", rt["volume_delta"], "<=", 0.0, BAND_MM3)
    rows.add("U-04", "faces_delta", rt["faces_delta"], "==", 0, BAND_COUNT)
    rows.add("U-04", "labels", rt["labels"], "==", 1, BAND_COUNT)
    rows.add("U-04", "valid_after", rt["valid_after"], "==", 1, BAND_COUNT)
    lap("roundtrip")

    # ---- references
    refs = load_refs()
    ident = refs.pop("_ident")
    E02, G10 = refs["E02"], refs["G10"]
    ref_sound = {k: brep_valid(s) for k, s in refs.items()}
    lap("refs")

    # ---- census: U-05, feature_census, D-04a, D-05b, E-05, REQ-01, REQ-04
    census = bore_census(P)
    fc = feature_census(P)
    bores = census.detail.get("bores", []) if census.ok else []

    def along(b, axis):
        return abs(abs(b["axis_dir"][axis]) - 1.0) < 1e-6

    n_y34 = sum(1 for b in bores if along(b, 1) and abs(b["diameter"] - 3.4) < 0.3)
    n_z15 = sum(1 for b in bores if along(b, 2) and abs(b["diameter"] - 15.0) < 0.5)
    n_z4 = sum(1 for b in bores if along(b, 2) and abs(b["diameter"] - 4.0) < 0.2 and not b.get("through"))
    for gid in ("U-05", "feature_census"):
        rows.add(gid, "bores_total", fc["bores"], "==", 9, BAND_COUNT, note="4 flange + 3 button + 2 insert")
        rows.add(gid, "flange_holes_d3.4_along_Y", Result("count", n_y34, "count"), "==", 4, BAND_COUNT)
        rows.add(gid, "button_holes_d15_along_Z", Result("count", n_z15, "count"), "==", 3, BAND_COUNT)
        rows.add(gid, "insert_bores_d4_blind_along_Z", Result("count", n_z4, "count"), "==", 2, BAND_COUNT)

    # faces by kind and geometry: gussets (inclined planes), bosses (convex cylinders r 5.5),
    # collar reliefs (concave cylinder arcs about the collar axes)
    inclined, boss_axes, relief_axes, cyl_radii = [], set(), set(), []
    for f in faces(P.wrapped):
        s = BRepAdaptor_Surface(f)
        if s.GetType() == GeomAbs_Plane:
            n = s.Plane().Axis().Direction()
            vec = (n.X(), n.Y(), n.Z())
            if abs(vec[0]) < 1e-6 and 0.2 < abs(vec[1]) < 0.9:
                inclined.append(vec)
        elif s.GetType() == GeomAbs_Cylinder:
            c = s.Cylinder()
            loc, r = c.Location(), c.Radius()
            cyl_radii.append(r)
            d = c.Axis().Direction()
            if abs(abs(d.Z()) - 1) < 1e-6:
                key = (round(loc.X(), 3), round(loc.Y(), 3), round(r, 3))
                if abs(r - 5.5) < 0.2:
                    boss_axes.add(key)
                elif r > 7.6:
                    relief_axes.add(key)
    for gid in ("U-05", "feature_census"):
        rows.add(gid, "gusset_hypotenuse_planes", Result("count", len(inclined), "count", detail={"normals": inclined}),
                 "==", 4, BAND_COUNT)
        rows.add(gid, "boss_d11_axes", Result("count", len(boss_axes), "count", detail={"axes": sorted(boss_axes)}),
                 "==", 2, BAND_COUNT)
        rows.add(gid, "collar_reliefs", Result("count", len(relief_axes), "count", detail={"axes": sorted(relief_axes)}),
                 "==", 2, BAND_COUNT)

    # positional probes: each named feature has material where the plan puts it
    probes = {
        "wall": (0.0, 200.0, 95.5),
        "R1": (0.0, 189.5, 89.0), "R2": (76.5, 100.0, 89.0), "R3": (-59.0, 120.0, 89.0),
        "R4": (-76.5, 25.0, 89.0), "R5": (-68.0, 51.5, 89.0),
        "flange_L": (-90.0, 2.0, 74.0), "flange_R": (90.0, 2.0, 74.0),
        "gusset_L_in": (-78.0, 6.0, 92.0), "gusset_L_out": (-102.0, 6.0, 92.0),
        "gusset_R_in": (78.0, 6.0, 92.0), "gusset_R_out": (102.0, 6.0, 92.0),
    }
    empty = {"opening_slot": (0.0, 25.0, 95.5), "opening_window": (0.0, 150.0, 95.5),
             "opening_slot_left_of_window": (-66.0, 25.0, 95.5), "below_ribs_inside": (0.0, 189.5, 83.0)}
    states = {k: classify(P, p) for k, p in probes.items()}
    states_e = {k: classify(P, p) for k, p in empty.items()}
    for gid in ("U-05", "feature_census"):
        rows.add(gid, "named_features_present", Result("count", sum(1 for s in states.values() if s == "IN"), "count",
                                                         detail=states), "==", len(probes), BAND_COUNT,
                 note="wall, R1-R5, 2 flanges, 4 gussets by a probe point in each")
        rows.add(gid, "brew_opening_open", Result("count", sum(1 for s in states_e.values() if s == "OUT"), "count",
                                                   detail=states_e), "==", len(empty), BAND_COUNT)
        for k in ("plane", "cylinder", "cone", "sphere", "torus", "bspline", "other"):
            key = f"{k}_faces"
            if key in fc and fc[key].ok:
                rows.add(gid, f"faces_{k}", fc[key], ">=", 0, BAND_COUNT, note="reference count recorded")
    lap("census")

    # flange holes: REQ-01, D-04a, D-03b (bridge = hole diameter)
    for (x, z) in SPEC["flange_holes"]:
        loc = locate_bore(census, (x, 2.0, z), (0, 1, 0))
        tag = f"hole({x:+.0f},{z:.0f})"
        rows.add("REQ-01", f"{tag}_diameter", loc["diameter"], "in", SPEC["flange_hole_d"], BAND_MM, ("A-01",))
        rows.add("REQ-01", f"{tag}_offset", loc["offset"], "<=", SPEC["flange_hole_offset_max"], BAND_MM, ("A-01",))
        rows.add("REQ-01", f"{tag}_length", loc["length"], "in", SPEC["flange_hole_len"], BAND_MM, ("A-01",))
        rows.add("REQ-01", f"{tag}_through", loc["through"], "==", 1, BAND_COUNT, ("A-01",))
        rows.add("D-04a", f"{tag}_diameter", loc["diameter"], ">=", SPEC["flange_hole_min_d"], BAND_MM)
        rows.add("D-03b", f"{tag}_bridge_span", loc["diameter"], "<=", SPEC["bridge_max"], BAND_MM, ("A-09",),
                 note="the horizontal hole's crown bridges its diameter; reviewer confirms from sections")
    # underside one plane at y 0
    down_y = []
    for f in faces(P.wrapped):
        s = BRepAdaptor_Surface(f)
        if s.GetType() == GeomAbs_Plane:
            pl = s.Plane()
            n = pl.Axis().Direction()
            sign = -1.0 if f.Orientation() == TopAbs_REVERSED else 1.0
            # the underside: the faces turned to -Y that stand on the plate (below the flanges' top,
            # y < floor + flange thickness); the opening's top edges also face -Y and are not the underside
            if abs(n.Y() * sign + 1.0) < 1e-9 and pl.Location().Y() < UNDERSIDE_BAND_Y:
                down_y.append(pl.Location().Y())
    rows.add("REQ-01", "underside_faces_y_min", num("underside_y", min(down_y) if down_y else float("nan"),
                                                    detail={"faces": len(down_y), "ys": down_y}) if down_y
             else inconclusive("underside_y", "mm", "no -Y face"), "in", SPEC["underside_y"], BAND_MM, ("A-01",))
    rows.add("REQ-01", "underside_faces_y_max", num("underside_y", max(down_y)) if down_y
             else inconclusive("underside_y", "mm", "no -Y face"), "in", SPEC["underside_y"], BAND_MM, ("A-01",))

    # insert bores: D-05b, E-05, D-05a, J-05; board screw holes measured on the posed OD-E02
    e02_census = bore_census(E02)
    board_holes = sorted([b for b in e02_census.detail.get("bores", []) if along(b, 2) and 3.3 < b["diameter"] < 3.7],
                         key=lambda b: -b["start"][1])
    if len(board_holes) != 2:
        rows.literal("E-05", "board_holes", INCONCLUSIVE, note=f"found {len(board_holes)} board screw holes")
    for name, bh in zip(("upper", "lower"), board_holes):
        hx, hy = bh["start"][0], bh["start"][1]
        insert = [b for b in bores if along(b, 2) and abs(b["diameter"] - 4.0) < 0.2
                  and math.hypot(b["start"][0] - hx, b["start"][1] - hy) < 2.0]
        if not insert:
            for gid in ("D-05b", "E-05", "D-05a", "J-05"):
                rows.literal(gid, f"{name}_insert", FAIL if census.ok else INCONCLUSIVE, note="no insert bore near the board hole")
            continue
        ib = insert[0]
        z_lo, z_hi = min(ib["start"][2], ib["end"][2]), max(ib["start"][2], ib["end"][2])
        loc = locate_bore(census, (hx, hy, 0.5 * (z_lo + z_hi)), (0, 0, 1))
        rows.add("D-05b", f"{name}_diameter", loc["diameter"], "in", SPEC["insert_d"], BAND_MM, ("A-03",))
        rows.add("D-05b", f"{name}_depth", loc["length"], "in", SPEC["insert_depth"], BAND_MM, ("A-03",))
        rows.add("D-05b", f"{name}_blind", loc["through"], "==", 0, BAND_COUNT, ("A-03",))
        rows.add("E-05", f"{name}_axis_offset", loc["offset"], "<=", SPEC["board_hole_offset_max"], BAND_MM, ("A-03",),
                 note=f"board hole axis ({hx:.4f}, {hy:.4f}) d {bh['diameter']:.4f}")
        ax_o = (ib["start"][0], ib["start"][1], z_lo)
        r_bore = ib["radius"]
        # D-05a: material across = r(theta) + r(theta + 180) at 0..330 every 30, three levels
        depth = z_hi - z_lo
        worst_across, worst_at = None, None
        try:
            for lvl in (0.25 * depth, 0.5 * depth, 0.75 * depth):
                for a in range(0, 180, 30):
                    ra = radial_extent(P, ax_o, (0, 0, 1), (1, 0, 0), a, lvl, side="outer", r_min=r_bore - 0.1, r_max=7.0)
                    rb = radial_extent(P, ax_o, (0, 0, 1), (1, 0, 0), a + 180, lvl, side="outer", r_min=r_bore - 0.1, r_max=7.0)
                    if not (ra.ok and rb.ok):
                        raise RuntimeError(ra.reason or rb.reason)
                    across = ra.measured + rb.measured
                    if worst_across is None or across < worst_across:
                        worst_across, worst_at = across, (a, round(lvl, 3))
            res = num("material_across_insert_bore", worst_across, at=f"angle {worst_at[0]} deg, {worst_at[1]} mm from the boss end")
        except Exception as exc:  # noqa: BLE001
            res = inconclusive("material_across_insert_bore", "mm", str(exc))
        rows.add("D-05a", f"{name}_across", res, ">=", SPEC["insert_across_min"], BAND_MM, ("A-03",))
        # J-05: least wall around the bore over every 2 degrees and every 0.2 mm of the bore
        prof = radial_profile(P, ax_o, (0, 0, 1), (1, 0, 0), [float(a) for a in range(0, 360, 2)], (0.0, depth),
                              margin=0.0, z_step=0.2, side="outer", r_min=r_bore - 0.1, r_max=7.0)
        pm = prof["min"]
        wall = (num("wall_around_insert_bore", pm.measured - r_bore, at=pm.at,
                    detail={"r_outer_min": pm.measured, "r_bore": r_bore}) if pm.ok else pm)
        rows.add("J-05", f"{name}_wall", wall, ">=", SPEC["insert_wall_min"], BAND_MM, ("A-03",))
    lap("bores")

    # REQ-04: caps measured on the posed OD-E02 (foremost by exact distance from a plane face
    # over each cap; axes from cap sections), button holes located on the panel
    caps = {}
    for cap, (y0, y1) in {"B1": (155.0, 180.0), "B2": (125.0, 155.0), "B3": (100.0, 125.0)}.items():
        try:
            probe = box(-118.0, -80.0, y0, y1, 100.0, 100.01)
            d = clearance(probe, E02)
            fore = num("cap_foremost_z", 100.0 - d.measured, at=d.detail.get("on_b"))
            # axis: centroids of full cap sections (constant area) above the collar
            cents = []
            for z in (89.5, 90.0):
                sl = E02 & box(-118.0, -80.0, y0, y1, z, z + 0.001)
                cents.append((sl.center().X, sl.center().Y, z))
            if cap == "B2":
                sl = E02 & box(-118.0, -80.0, y0, y1, SPEC["section_z"], SPEC["section_z"] + 0.001)
                axis_pt = (sl.center().X, sl.center().Y)
            else:   # B1, B3: elliptic prisms along the board axis (Z); constant centroid
                axis_pt = (0.5 * (cents[0][0] + cents[1][0]), 0.5 * (cents[0][1] + cents[1][1]))
            caps[cap] = (fore, axis_pt)
        except Exception as exc:  # noqa: BLE001
            caps[cap] = (inconclusive("cap_foremost_z", "mm", str(exc)), None)
    for cap, (fore, axis_pt) in caps.items():
        limit = SPEC["b2_foremost_min"] if cap == "B2" else SPEC["side_cap_foremost_min"]
        rows.add("REQ-04", f"{cap}_foremost_z", fore, ">=", limit, BAND_MM, ("A-03", "A-04"))
        if axis_pt is None:
            rows.literal("REQ-04", f"{cap}_hole_offset", INCONCLUSIVE, note="cap axis not measured")
            continue
        loc = locate_bore(census, (axis_pt[0], axis_pt[1], SPEC["section_z"]), (0, 0, 1))
        row = rows.add("REQ-04", f"{cap}_hole_offset", loc["offset"], "<=", SPEC["button_offset_max"], BAND_MM,
                       ("A-03", "A-04"), note=f"cap axis at z 95.5: ({axis_pt[0]:.4f}, {axis_pt[1]:.4f})")
        row["hole_diameter"] = loc["diameter"].measured if loc["diameter"].ok else None
    lap("caps")

    if "assembly" in stages:
        # ---- U-03 (a) designed contacts (clearance = 0)
        W = SPEC
        foot = clip(P, box(-120, 120, 0.0, 0.01, 60, 100))
        wall_foot = clip(P, box(-120, 120, 0.0, 0.01, W["wall_in_z"][0] + 0.1, 100))
        flange_L = clip(P, box(-110, -70, 0.0, 0.01, 60, W["wall_in_z"][0] + 0.1))
        flange_R = clip(P, box(70, 110, 0.0, 0.01, 60, W["wall_in_z"][0] + 0.1))
        rows.add("U-03", "a_contact_wall_foot_on_C01", clearance(wall_foot, refs["C01"]), "==", 0.0, BAND_MM, ("A-02",))
        rows.add("U-03", "a_contact_flange_L_on_C01", clearance(flange_L, refs["C01"]), "==", 0.0, BAND_MM, ("A-01",))
        rows.add("U-03", "a_contact_flange_R_on_C01", clearance(flange_R, refs["C01"]), "==", 0.0, BAND_MM, ("A-01",))
        top_edge = clip(P, box(-120, 120, 214.0, 216.0, 93, 98))
        rows.add("U-03", "a_contact_C10_skirt_on_wall_top", clearance(top_edge, refs["C10"]), "==", 0.0, BAND_MM, ("A-07",))
        boss_ends = []
        for name, bh in zip(("upper", "lower"), board_holes):
            end_slab = clip(P, cyl_z(bh["start"][0], bh["start"][1], 5.8, 80.0, 86.0))
            boss_ends.append(end_slab)
            rows.add("U-03", f"a_contact_boss_{name}_on_E02", clearance(end_slab, E02), "==", 0.0, BAND_MM, ("A-03",))
        lap("contacts")

        # ---- U-03 (a) interference, every pair; OD-G10 and OD-E02 by the clearance fallback
        sound = {"panel": P, **{k: refs[k] for k in ("C01", "C05", "housing", "G04", "C10")}}
        for key, res in interference(sound).items():
            rows.add("U-03", f"a_interference_{key}", res, "<=", 0.0, BAND_MM3, ("A-05",))
        for other in ("C01", "C05", "housing", "G04", "C10"):
            rows.separated("U-03", f"a_interference_G10|{other}", G10, refs[other], ("A-05",), cache=rc)
            rows.separated("U-03", f"a_interference_E02|{other}", E02, refs[other], ("A-03",), cache=rc)
        rows.separated("U-03", "a_interference_E02|G10", E02, G10, ("A-03", "A-05"), cache=rc)
        rows.separated("U-03", "a_interference_panel|G10", P, G10, ("A-05",))
        rows.separated("U-03", "a_interference_panel|E02", moved(P, dz=BAND_MM), E02, ("A-03",),
                       note="panel pulled 0.005 (the mm band) off the board along +Z: the boss ends are designed contacts")
        lap("interference")

        # ---- U-03 (a) footprint and holes against OD-C01
        c01 = refs["C01"]
        slab = box(-200, 200, -1.0, 0.0, -400, 200) - c01
        pieces = slab.solids()
        outside = [s for s in pieces if s.bounding_box().max.X > 199 or s.bounding_box().min.X < -199]
        holes = [s for s in pieces if s not in outside]
        rows.add("U-03", "a_footprint_to_plate_edge", clearance(foot, Compound(outside)), ">=", W["footprint_edge_min"],
                 BAND_MM, ("A-02",))
        c01_census = bore_census(c01)
        c01_holes = [b for b in c01_census.detail.get("bores", []) if along(b, 1)]
        if holes:
            hc = Compound(holes)
            # the flanges alone: stop 0.4 short of the wall's inner face at its low limit (REQ-02), so the
            # wall's foot (its own rule, >= 2.0) is never read as flange when the wall plane moves
            flange_top_z = W["wall_in_z"][0] - 0.4
            rows.add("U-03", "a_flange_L_to_C01_holes", clearance(clip(P, box(-110, -70, 0, 4.0, 60, flange_top_z)), hc), ">=",
                     W["flange_to_hole_min"], BAND_MM, ("A-01",))
            rows.add("U-03", "a_flange_R_to_C01_holes", clearance(clip(P, box(70, 110, 0, 4.0, 60, flange_top_z)), hc), ">=",
                     W["flange_to_hole_min"], BAND_MM, ("A-01",))
            rows.add("U-03", "a_wall_foot_to_C01_holes", clearance(wall_foot, hc), ">=", W["foot_to_hole_min"], BAND_MM, ("A-02",))
        else:
            rows.literal("U-03", "a_C01_holes", INCONCLUSIVE, note="no hole found in the OD-C01 slab")
        if c01_holes:
            dmin, at = None, None
            for (x, z) in W["flange_holes"]:
                for b in c01_holes:
                    d = math.hypot(b["start"][0] - x, b["start"][2] - z)
                    if dmin is None or d < dmin:
                        dmin, at = d, f"flange hole ({x}, {z}) to C01 hole ({b['start'][0]:.2f}, {b['start'][2]:.2f})"
            rows.add("U-03", "a_flange_hole_centres_to_C01_hole_centres", num("centre_distance", dmin, at=at), ">=",
                     W["hole_centre_min"], BAND_MM, ("A-01",))
        else:
            rows.literal("U-03", "a_hole_centres", INCONCLUSIVE, note="no OD-C01 bore along Y")

        # brew area >= 2.0
        for other in ("C05", "housing", "G04"):
            rows.add("U-03", f"a_panel_to_{other}", clearance(P, refs[other]), ">=", W["brew_area_min"], BAND_MM, ("A-05",))
        # OD-C15 keep-outs
        ko = {f"C15_keepout({x:+.0f},{z:.0f})": cyl_y(x, z, W["c15_d"] / 2, *W["c15_y"]) for (x, z) in W["c15_keepouts"]}
        for k, res in interference({"panel": P, **ko}).items():
            if k.startswith("panel|"):
                rows.add("U-03", f"a_{k}", res, "<=", 0.0, BAND_MM3)
        lap("footprint")

        # ---- U-03 (b) the panel lowered along -Y from +40 in steps of 2.0, OD-C10 and OD-E02 absent
        worst = {}

        def keep_worse(key, dy, res, value):
            """Keep the worst step: an INCONCLUSIVE step sticks; else the larger value."""
            cur = worst.get(key)
            if cur is None or (cur[1].status == MEASURED and (res.status != MEASURED or value > cur[2])):
                worst[key] = (dy, res, value)

        steps = int(round(W["lower_from"] / W["lower_step"]))
        for i in range(steps + 1):
            dy = W["lower_from"] - i * W["lower_step"]
            Pm = moved(P, dy=dy)
            for other in ("C01", "C05", "housing", "G04"):
                res = common_volume(Pm, refs[other])
                keep_worse(f"b_lowering_{other}", dy, res, res.measured if res.status == MEASURED else 0.0)
            r = clearance(Pm, G10)
            ok = r.ok and r.measured > 0.0 and not r.detail.get("inside", True)
            res = (fact("separated_clearance_gt_0_not_inside", ok, at=r.at, detail={"clearance_mm": r.measured})
                   if r.ok else r)
            keep_worse("b_lowering_G10_separated", dy, res, (0.0 if not ok else -r.measured))
        for key, (dy, res, _) in worst.items():
            if key.endswith("separated"):
                row = rows.add("U-03", key, res, "==", 1, BAND_COUNT, ("A-05",), required="clearance > 0 and inside == False",
                               note=f"least step at +{dy:.1f}")
                row["clearance_mm"] = res.detail.get("clearance_mm")
            else:
                rows.add("U-03", key, Result("interference", res.measured, "mm3", status=res.status, reason=res.reason),
                         "<=", 0.0, BAND_MM3, ("A-05",), note=f"worst step at +{dy:.1f}")
        lap("lowering")

        # ---- E-01: panel without its bosses >= 0.5; each boss above its end + 0.5 >= 0.5; at + 2.0 reported
        no_boss = P
        for bh in board_holes:
            no_boss = no_boss - cyl_z(bh["start"][0], bh["start"][1], 5.8, 80.0, W["wall_in_z"][0] + 0.1)
        rows.add("E-01", "panel_without_bosses_to_E02", clearance(no_boss, E02), ">=", W["board_keepout"], BAND_MM, ("A-03",))
        for name, bh in zip(("upper", "lower"), board_holes):
            end_z = None
            try:
                slab_hits = line_hits(P, (bh["start"][0] - 4.0, bh["start"][1], 70.0), (0, 0, 1))
                end_z = 70.0 + slab_hits[0]
            except Exception:  # noqa: BLE001
                pass
            if end_z is None:
                rows.literal("E-01", f"boss_{name}", INCONCLUSIVE, note="boss end not found")
                continue
            for lift, gated in ((0.5, True), (2.0, False)):
                part = clip(P, cyl_z(bh["start"][0], bh["start"][1], 5.8, end_z + lift, W["wall_in_z"][0] - 0.01))
                res = clearance(part, E02)
                if gated:
                    rows.add("E-01", f"boss_{name}_from_end+0.5", res, ">=", W["board_keepout"], BAND_MM, ("A-03",),
                             note=f"boss end measured at z {end_z:.4f}; reads <= 0.5 by construction")
                else:
                    rows.add("E-01", f"boss_{name}_from_end+2.0_side_gap", res, ">=", W["board_keepout"], BAND_MM, ("A-03",),
                             note="reported side gap")
        lap("E-01")

    # ---- REQ-02 wall planes by exact line probes; REQ-03 opening edges and boxes
    for y in W["req02_levels_y"]:
        for x in (-100.0, 0.0, 100.0):
            if y < W["window"]["y"][1] and W["window"]["x"][0] < x < W["window"]["x"][1]:
                continue
            try:
                h = [70.0 + t for t in line_hits(P, (x, y, 70.0), (0, 0, 1))]
                rows.add("REQ-02", f"outer_face_at({x:+.0f},{y:.0f})", num("face_z", max(h)), "in", W["wall_out_z"], BAND_MM, ("A-02",))
                inner = [z for z in h if z < max(h) - 1.0]
                rows.add("REQ-02", f"inner_face_at({x:+.0f},{y:.0f})", num("face_z", max(inner)), "in", W["wall_in_z"], BAND_MM, ("A-02",))
            except Exception as exc:  # noqa: BLE001
                rows.literal("REQ-02", f"faces_at({x:+.0f},{y:.0f})", INCONCLUSIVE, note=str(exc))
    zc = W["section_z"]
    et = W["opening_edge_tol"]

    def edge_x(y, x_from, x_to):
        h = sorted(x_from + t for t in line_hits(P, (x_from, y, zc), (1, 0, 0)))
        return h

    try:
        hx = edge_x(25.0, -130.0, 130.0)     # through the tray slot
        left = max(x for x in hx if x < 0); right = min(x for x in hx if x > 0)
        rows.add("REQ-03", "slot_left_x", num("edge_x", left), "in", (W["slot"]["x"][0] - et, W["slot"]["x"][0] + et), BAND_MM, ("A-06",))
        rows.add("REQ-03", "slot_right_x", num("edge_x", right), "in", (W["slot"]["x"][1] - et, W["slot"]["x"][1] + et), BAND_MM, ("A-06",))
        hx = edge_x(120.0, -130.0, 130.0)    # through the window, below the lower button hole
        left = max(x for x in hx if x < 0); right = min(x for x in hx if x > 0)
        rows.add("REQ-03", "window_left_x", num("edge_x", left), "in", (W["window"]["x"][0] - et, W["window"]["x"][0] + et), BAND_MM, ("A-05",))
        rows.add("REQ-03", "window_right_x", num("edge_x", right), "in", (W["window"]["x"][1] - et, W["window"]["x"][1] + et), BAND_MM, ("A-05",))
        hy = sorted(-10.0 + t for t in line_hits(P, (0.0, -10.0, zc), (0, 1, 0)))
        top = min(y for y in hy if y > 1.0)
        rows.add("REQ-03", "window_top_y", num("edge_y", top), "in", (W["window"]["y"][1] - et, W["window"]["y"][1] + et), BAND_MM, ("A-05",))
        hy = sorted(-10.0 + t for t in line_hits(P, (-66.0, -10.0, zc), (0, 1, 0)))
        step = min(y for y in hy if y > 1.0)
        rows.add("REQ-03", "slot_top_y_at_step", num("edge_y", step), "in", (W["slot"]["y"][1] - et, W["slot"]["y"][1] + et), BAND_MM, ("A-06",))
    except Exception as exc:  # noqa: BLE001
        rows.literal("REQ-03", "edges", INCONCLUSIVE, note=str(exc))
    s = W["opening_shrink"]
    zb = W["opening_z"]
    ob = {"slot_box": box(W["slot"]["x"][0] + s, W["slot"]["x"][1] - s, W["slot"]["y"][0] + s, W["slot"]["y"][1] - s, *zb),
          "window_box": box(W["window"]["x"][0] + s, W["window"]["x"][1] - s, W["window"]["y"][0] + s, W["window"]["y"][1] - s, *zb)}
    for k, res in interference({"panel": P, **ob}).items():
        if k.startswith("panel|"):
            rows.add("REQ-03", k, res, "<=", 0.0, BAND_MM3, ("A-05", "A-06"))
    lap("REQ-02/03")

    if "motion" in stages:
        # ---- REQ-05 (a) OD-G10 rotated by phi; (b) carried in at phi -50, lowered 15, along +Z
        worst_a = {"panel": None, "E02": None}
        phi = W["phi_range"][0]
        nphi = int(round((W["phi_range"][1] - W["phi_range"][0]) / W["phi_step"]))
        for i in range(nphi + 1):
            phi = W["phi_range"][0] + i * W["phi_step"]
            g = g10_pose(G10, phi)
            for k, other in (("panel", P), ("E02", E02)):
                r = clearance(other, g) if k == "panel" else rc.clearance(f"req05a_E02_phi{phi:+.1f}", other, g)
                if worst_a[k] is None or (r.status != MEASURED) or (worst_a[k][1].ok and r.measured < worst_a[k][1].measured):
                    if worst_a[k] is None or worst_a[k][1].ok:
                        worst_a[k] = (phi, r)
        for k, (phi_w, r) in worst_a.items():
            rows.add("REQ-05", f"a_G10_to_{k}_least", r, ">=", W["g10_gap_min"], BAND_MM, ("A-05",), note=f"worst phi {phi_w:+.0f} deg")
        lap("REQ-05a")
        worst_b = {"panel": None, "E02": None}
        nz = int(round((W["carry_z"][1] - W["carry_z"][0]) / W["carry_step"]))
        for i in range(nz + 1):
            dz = i * W["carry_step"]
            g = g10_pose(G10, W["carry_phi"], dy=-W["carry_drop"], dz=dz)
            for k, other in (("panel", P), ("E02", E02)):
                r = clearance(other, g) if k == "panel" else rc.clearance(f"req05b_E02_dz{dz:.1f}", other, g)
                ok = r.ok and r.measured > 0.0 and not r.detail.get("inside", True)
                cur = worst_b[k]
                if cur is None or (cur[2] and (not ok or (r.ok and r.measured < cur[1].measured))):
                    worst_b[k] = (dz, r, ok)
        for k, (dz, r, ok) in worst_b.items():
            res = fact("separated_clearance_gt_0_not_inside", ok, at=r.at if r.ok else None,
                       detail={"clearance_mm": r.measured if r.ok else None})
            row = rows.add("REQ-05", f"b_carry_G10_vs_{k}", res, "==", 1, BAND_COUNT, ("A-05",),
                           required="clearance > 0 and inside == False at every step",
                           note=f"worst step: axis at z {W['carry_z'][0] + dz:.0f}")
            row["clearance_mm"] = r.measured if r.ok else None
        lap("REQ-05b")

    # ---- REQ-06 driver access, REQ-07 keep-outs
    drivers = {}
    for (x, z) in W["flange_holes"]:
        drivers[f"driver_flange({x:+.0f},{z:.0f})"] = cyl_y(x, z, W["driver_r"], W["flange_driver_y0"], W["driver_y_top"])
    for (x, z) in W["c15_keepouts"]:
        drivers[f"driver_C15({x:+.0f},{z:.0f})"] = cyl_y(x, z, W["driver_r"], W["c15_driver_y0"], W["driver_y_top"])
    for k, res in interference({"panel": P, **drivers}).items():
        if k.startswith("panel|"):
            rows.add("REQ-06", k, res, "<=", 0.0, BAND_MM3, ("A-14",))
    tb = W["tray_box"]
    kn = W["knob"]
    keep = {"tray_box": box(*tb["x"], *tb["y"], *tb["z"]),
            "knob_place": cyl_z(kn["x"], kn["y"], kn["d"] / 2, *kn["z"])}
    for k, res in interference({"panel": P, **keep}).items():
        if k.startswith("panel|"):
            rows.add("REQ-07", k, res, "<=", 0.0, BAND_MM3, ("A-06", "A-13"))
    lap("REQ-06/07")

    # ---- E-06 self-check (the reviewer gates it from sections): bosses and gussets tied in
    tie = {}
    for name, bh in zip(("upper", "lower"), board_holes):
        tie[f"boss_{name}_into_wall"] = classify(P, (bh["start"][0] + 4.0, bh["start"][1], W["wall_in_z"][0] - 0.05)) == "IN" \
            and classify(P, (bh["start"][0] + 4.0, bh["start"][1], W["wall_in_z"][0] + 0.05)) == "IN"
    for k in ("gusset_L_in", "gusset_L_out", "gusset_R_in", "gusset_R_out"):
        x = probes[k][0]
        tie[f"{k}_on_flange_and_wall"] = classify(P, (x, 4.5, 93.9)) == "IN" and classify(P, (x, 3.9, 80.0)) == "IN"
    rows.add("E-06", "self_check_ties", Result("count", sum(tie.values()), "count", detail=tie), "==", len(tie), BAND_COUNT,
             note="self-check only; the reviewer gates E-06 from sections")

    mw = oc_all = None
    if "process" in stages:
        # ---- process: min_wall (D-01a, D-01b, D-06a, U-06), overhang (D-03a), ceilings (D-03b)
        mw = min_wall(P, spacing=0.4)
        if mw.status != MEASURED and "spacing" in mw.reason:
            timeline.append(("min_wall 0.4 refused", mw.reason[:200]))
            import re
            m = re.search(r"spacing of ([0-9.]+)", mw.reason)
            if m:
                mw = min_wall(P, spacing=float(m.group(1)))
        rows.add("D-01a", "min_wall", mw, ">=", W["wall_d01a"], BAND_MM)
        rows.add("D-06a", "min_wall", mw, ">=", W["wall_d06a"], BAND_MM)
        rows.add("D-01b", "min_wall", mw, ">=", W["wall_d01b"], BAND_MM, ("A-11",))
        wide = (Result("min_wall_wide", mw.detail["wide"]["measured"], "mm", at=mw.detail["wide"].get("at"))
                if mw.ok and isinstance(mw.detail.get("wide"), dict) else min_wall_wide(P, spacing=mw.params.get("spacing", 0.4) if mw.params else 0.4))
        rows.add("U-06", "min_wall_wide", wide, ">=", W["wall_u06"], BAND_MM, note="Soft")
        lap("min_wall")
        build_dir = (0, 0, -1)
        filled = P
        for (x, z) in W["flange_holes"]:
            # the hole filled over its own length (the flange, y 0 ... 4.0) with a plug 0.2 over its radius
            filled = filled + cyl_y(x, z, 1.9, 0.0, UNDERSIDE_BAND_Y)
        filled = Solid(filled.solids()[0].wrapped) if len(filled.solids()) == 1 else filled
        oc = overhang_census(filled, build_dir=build_dir, min_deg=W["overhang_min_deg"], spacing=0.5)
        rows.add("D-03a", "least_downward_angle_excluding_flange_hole_crowns", oc, ">=", W["overhang_min_deg"], BAND_DEG, ("A-09",))
        oc_all = overhang_census(P, build_dir=build_dir, min_deg=W["overhang_min_deg"], spacing=0.5)
        rows.literal("D-03a", "flange_hole_crowns_named_exception", "INFO",
                     measured=oc_all.measured if oc_all.ok else None, unit="deg",
                     note=f"whole part including the crowns: least {oc_all.measured if oc_all.ok else oc_all.reason} at {oc_all.at}")
        fs = flat_ceiling_spans(filled, build_dir=build_dir, max_span=W["bridge_max"], spacing=0.5)
        rows.add("D-03b", "flat_ceiling_spans_lead", fs, "<=", W["bridge_max"], BAND_MM, ("A-09",),
                 note="lead for the reviewer, on the part with the four horizontal holes filled")
        lap("overhang")

    # ---- U-07 the STL: re-mesh the re-imported STEP and compare bytes; sagitta; angular bound
    r_max = max(cyl_radii) if cyl_radii else None
    if stl_path is not None and stl_path.exists():
        meta_path = WS / "01_CAD" / f"{stl_path.stem}.stl_meta.json"
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        ang = meta.get("angular_tolerance_rad")
        tolm = meta.get("tolerance_mm")
        if ang is None or tolm is None:
            rows.literal("U-07", "stl_meta", INCONCLUSIVE, note="no STL tolerance record beside the STL")
        else:
            with tempfile.TemporaryDirectory() as tmp:
                again = write_stl(P, Path(tmp) / "again.stl", tolerance=tolm, angular_tolerance=ang)
                from tools.core.step import file_sha256
                same = file_sha256(stl_path) == again.sha256
            rows.add("U-07", "stl_tolerance", num("stl_tolerance", tolm), "<=", W["stl_tol"], BAND_MM)
            rows.add("U-07", "stl_max_sagitta", again.checks["max_sagitta"], "<=", W["stl_tol"], BAND_MM)
            bound = 4.0 * math.acos(1.0 - W["stl_tol"] / r_max)
            rows.add("U-07", "angular_tolerance", num("angular_tolerance", ang, unit="rad",
                                                      detail={"R_max_mm": r_max}), "<=", bound, 0.00002,
                     note=f"bound 4*acos(1-0.01/R_max) with R_max {r_max:.4f} = {bound:.5f} rad")
            rows.add("U-07", "delivered_stl_is_this_mesh", fact("same_bytes", same), "==", 1, BAND_COUNT,
                     note=f"triangles {again.detail.get('triangles')}")
    else:
        rows.literal("U-07", "stl", INCONCLUSIVE, note="no STL given")
    lap("stl")

    # ---- rows answered by the spec itself
    rows.literal("U-08", "threads", "N/A", note="no threads on this target (row text)")
    rows.literal("D-07", "fit_critical_bores", "N/A", note="none: insert bores formed by the insert (row text)")
    rows.literal("REQ-08", "stiffness", INCONCLUSIVE, note="Soft, bench: answered by the first print (A-12)", assumes=("A-12",))
    out = rows.rows
    out.append({"gate": "_meta", "ident": ident, "ref_brep_valid": {k: r.measured for k, r in ref_sound.items()},
                "boss_axes": sorted(boss_axes), "relief_axes": sorted(relief_axes), "r_max": r_max,
                "board_holes": [(b["start"], b["diameter"]) for b in board_holes],
                "caps": {k: (v[0].measured if v[0].ok else None, v[1]) for k, v in caps.items()},
                "min_wall": ({"measured": mw.measured, "at": mw.at, "params": mw.params, "reason": mw.reason,
                              "largest_step": mw.detail.get("largest_step_mm"), "wide": mw.detail.get("wide")}
                             if mw is not None else None),
                "overhang_all": ({"measured": oc_all.measured, "at": oc_all.at,
                                  "per_kind": oc_all.detail.get("per_kind_least_deg")} if oc_all is not None else None),
                "stages": list(stages),
                "volume": P.volume})
    return out


def summary(rows: list[dict]) -> dict:
    order = {"FAIL": 3, "INCONCLUSIVE": 2, "PASS_ASSUMED": 1, "PASS": 0}
    out = {}
    for r in rows:
        g = r["gate"]
        if g.startswith("_"):
            continue
        s = r["status"]
        if s in ("N/A", "INFO"):
            out.setdefault(g, s)
            continue
        cur = out.get(g)
        if cur in (None, "N/A", "INFO") or order.get(s, 2) > order.get(cur, 0):
            out[g] = s
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", default=str(STEP_DEFAULT))
    ap.add_argument("--stl", default=str(STL_DEFAULT))
    ap.add_argument("--out", default=None)
    ap.add_argument("--params", default=None, help="JSON object of build parameter overrides (sweep)")
    ap.add_argument("--cache", default=None, help="sweep only: cache of reference-to-reference clearances")
    ap.add_argument("--stages", default=",".join(ALL_STAGES),
                    help="debugging only: a gated run always runs every stage")
    args = ap.parse_args()
    timeline = []
    override = json.loads(args.params) if args.params else None
    stages = tuple(x for x in args.stages.split(",") if x)
    rows = run(Path(args.step), Path(args.stl) if args.stl else None, override, False, timeline, stages, args.cache)
    result = {"step": Path(args.step).name, "params": override, "stages": list(stages), "cache": args.cache, "summary": summary(rows), "rows": rows,
              "timeline": timeline}
    text = json.dumps(result, indent=1, default=str)
    if args.out:
        Path(args.out).write_text(text)
    for g, s in result["summary"].items():
        print(f"{g:28s} {s}")
    bad = [r for r in rows if r.get("status") in ("FAIL", "INCONCLUSIVE") and not r["gate"].startswith("_")]
    for r in bad:
        print("  ", r["status"], r["gate"], r["item"], r.get("measured"), r.get("required"), r.get("reason", "")[:160])
    print("timeline", timeline)


if __name__ == "__main__":
    main()
