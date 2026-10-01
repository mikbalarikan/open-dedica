"""Checks for od_c03_cradle v02 (job 20260930-od-c03-pump-cradle, concept C1, spec 1.2).

Written before the build (PLAYBOOK D3). Every predicate re-imports an exported STEP
and measures it with tools.measure / tools.core; tools.result.gate compares. Limits
are the spec 1.2 section 5 values; bands are the GATES.md section 0 bands the plan
names (0.005 mm, 0.001 deg, 0.001 mm3, 0 for counts and 1/0 facts). Any exception
or missing value gives INCONCLUSIVE. Job-local helpers below only select faces by
type and position and hand them to `envelope`; they gate nothing on their own.

Frame: pump axis at the origin along +Z, theta counter-clockwise about +Z from +X,
+Y down in the machine; the foot underside is y = +40.0 (spec section 2).

Usage (from the repository root, after sourcing the environment):
    uv run tools/run.py python <workspace>/01_CAD/check_od_c03_cradle_v02.py [cradle.step assembly.step stl]
"""
from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path

from build123d import Box, Edge, GeomType, Pos

from tools.core import compare_step, read_step, validity, write_stl
from tools.measure import (bore_census, clearance, envelope, feature_census, interference,
                           locate_bore, mass_properties, mesh_census, min_wall, overhang_census,
                           radial_extent, radial_profile)
from tools.measure.features import cylinder
from tools.result import INCONCLUSIVE, Gate, Result, gate, inconclusive

WS = Path(__file__).resolve().parents[1]

# ---- limits: spec 1.2 section 5 (never from memory or code defaults) -------------
ENV_SIZE = {"x": 80.0, "y": 40.0, "z": 52.0}           # U-02, +-0.1
ENV_TOL = 0.1
ENV_POS = {"min_x": -40.0, "max_x": 40.0, "min_y": 0.0, "max_y": 40.0,
           "min_z": -10.0, "max_z": 42.0}                # U-02 position, reported apart
BED = {"x": 420.0, "z": 420.0, "y": 500.0}               # D-02 (A-10), foot down: Y vertical
WALL_FLOOR, WALL_STRUCT, MIN_FEATURE, WALL_WIDE = 0.8, 2.0, 1.0, 2.0   # D-01a, D-01b, D-06a, U-06
OVERHANG_MIN = 45.0                                      # D-03a
BRIDGE_MAX = 5.0                                         # D-03b
HOLE_D_MIN = 3.25                                        # D-04a
PUMP_CLEAR = 2.0                                         # REQ-03 (U-03 a)
SEATED_CLEAR = 0.5                                       # D-04c
SADDLE_R = (26.60, 26.70)                                # REQ-01
SADDLE_THETAS = [50.0 + 5.0 * i for i in range(17)]      # REQ-01: 50 ... 130 at every 5
SADDLE_BANDS = ((-2.5, 2.5), (25.5, 30.5))               # REQ-01 windows (spec 1.2)
REQ02_Z = (0.0, 28.0)                                    # REQ-02 levels (spec 1.2)
REQ02_IN = (50.0, 130.0)
REQ02_OUT = (40.0, 140.0)
REQ02_RIN_MAX, REQ02_RCLEAR = 26.70, 32.0
RIB_FACES_Z = (-3.0, 3.0, 25.0, 31.0)                    # REQ-02, +-0.10 (spec 1.2)
FACE_TOL = 0.10
SLOT_W, SLOT_H = 6.0, 2.5                                # REQ-05 clear section, at least
SLOT_YC, SLOT_ZC, SLOT_C_TOL = 7.0, (17.0, 28.0), 0.5    # REQ-05 centres (spec 1.2)
LIGAMENT = 2.0                                           # REQ-05 (D-01b)
POST_X, POST_Z, POST_TOL = 29.5, (12.0, 33.0), 0.1       # REQ-06 (spec 1.2)
HOLE_D, HOLE_D_TOL, HOLE_OFFSET = 3.4, 0.1, 0.10         # REQ-07
HOLES = [(sx * 34.0, zc) for zc in (-4.0, 37.0) for sx in (-1, 1)]
FOOT_Y, FOOT_T, FOOT_TOL = 40.0, 3.0, 0.1                # REQ-08
STL_TOL = 0.01                                           # U-07
STL_ANG_MAX = 4.0 * math.acos(1.0 - 0.01 / 32.0)         # U-07: a <= 4 acos(1 - 0.01/32.0)
CENSUS = {"plane_faces": 48, "cylinder_faces": 6, "cone_faces": 0, "sphere_faces": 0,
          "torus_faces": 0, "bspline_faces": 0, "other_faces": 0, "concave_cylinders": 6,
          "convex_cylinders": 0, "bores": 4}             # U-05, plan section 6 as amended (spec 1.1, unchanged in 1.2)
DENSITY = 1270.0                                         # A-09, information only

# ---- bands: GATES.md section 0 -----------------------------------------------------
MM, DEG, MM3, COUNT = 0.005, 0.001, 0.001, 0

# ---- labels in the check assembly --------------------------------------------------
CRADLE, PUMP, SLEEVE = "od_c03_cradle", "OD_H01_ulka_ep5_pump", "od_h02_sleeve_assumed_A03"

AXIS = ((0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))


# ---- helpers -----------------------------------------------------------------------
def _safe(gid, fn, unit="mm"):
    """Run one predicate; an exception becomes one INCONCLUSIVE row."""
    try:
        out = fn()
        return out if isinstance(out, list) else [out]
    except Exception as exc:                                  # noqa: BLE001: the contract
        return [gate(gid, inconclusive(gid, unit, f"{type(exc).__name__}: {exc}"), ">=", 0.0,
                     band=0.0)]


def _named(gid, result, op, limit, band, assumes=(), note=None):
    g = gate(gid, result, op, limit, band=band, assumes=list(assumes))
    if note:
        g = Gate(g.gate, g.measured, g.unit, g.required, g.margin,
                 f"{g.at} {note}" if g.at else note, g.status, g.method, g.assumes, g.reason)
    return g


def _count(name, n):
    return Result(name, int(n), "count")


def _box(face):
    bb = face.bounding_box()
    return (bb.min.X, bb.min.Y, bb.min.Z), (bb.max.X, bb.max.Y, bb.max.Z)


def _planes(shape, axis_index):
    """Planar faces whose normal lies along one coordinate axis."""
    out = []
    for f in shape.faces():
        if f.geom_type != GeomType.PLANE:
            continue
        n = f.normal_at(f.center())
        if abs(abs((n.X, n.Y, n.Z)[axis_index]) - 1.0) < 1e-6:
            out.append(f)
    return out


def _within(face, lo, hi):
    a, b = _box(face)
    return all(lo[i] - 1e-3 <= a[i] and b[i] <= hi[i] + 1e-3 for i in range(3))


def _env(face):
    return envelope(face)


def _part(shape, label):
    for child in getattr(shape, "children", ()) or ():
        if getattr(child, "label", "") == label:
            return child
        found = _part(child, label)
        if found is not None:
            return found
    return None


# ---- part predicates ---------------------------------------------------------------
def part_gates(step_path: Path) -> list[Gate]:
    shape = read_step(step_path)
    PART_INFO.clear()
    rows: list[Gate] = []

    v = validity(shape)
    rows.append(_named("exactly_one_solid", v["solid_count"], "==", 1, COUNT))
    rows.append(_named("U-01 solid_count", v["solid_count"], "==", 1, COUNT))
    rows.append(_named("U-01 brep_valid", v["brep_valid"], "==", 1, COUNT))
    rows.append(_named("U-01 naked_edges", v["naked_edges"], "==", 0, COUNT))
    sound = all(r.ok for r in v.values()) and v["solid_count"].measured == 1 \
        and v["brep_valid"].measured == 1 and v["naked_edges"].measured == 0
    if not sound:
        rows.append(gate("part_sound", inconclusive("part_sound", "bool",
                                                    "the part is not one sound solid"), "==", 1, band=0))
        return rows

    env = envelope(shape)
    for ax, size in ENV_SIZE.items():
        rows.append(_named(f"U-02 size_{ax}", env[f"size_{ax}"], "in",
                           (size - ENV_TOL, size + ENV_TOL), MM))
        rows.append(_named(f"envelope_within_spec size_{ax}", env[f"size_{ax}"], "in",
                           (size - ENV_TOL, size + ENV_TOL), MM))
    for key, val in ENV_POS.items():
        rows.append(_named(f"envelope_within_spec position {key}", env[key], "==", val, MM))
    rows.append(_named("D-02 bed x", env["size_x"], "<=", BED["x"], MM, ["A-10"]))
    rows.append(_named("D-02 bed z", env["size_z"], "<=", BED["z"], MM, ["A-10"]))
    rows.append(_named("D-02 height y", env["size_y"], "<=", BED["y"], MM, ["A-10"]))

    # U-05 feature census
    fc = feature_census(shape)
    for key, want in CENSUS.items():
        rows.append(_named(f"U-05 feature_census {key}", fc[key], "==", want, COUNT))
    rows.extend(_safe("U-05 by position", lambda: _census_by_position(shape), "count"))

    # walls: one scan read at 25 deg and its 45 deg reading beside it
    mw = min_wall(shape)
    rows.append(_named("D-01a", mw, ">=", WALL_FLOOR, MM))
    rows.append(_named("D-01b", mw, ">=", WALL_STRUCT, MM))
    rows.append(_named("D-06a", mw, ">=", MIN_FEATURE, MM))
    if mw.ok and mw.detail.get("wide") is not None:
        wide = mw.detail["wide"]
        wide_val = wide if isinstance(wide, (int, float)) else wide.get("mm", wide.get("measured"))
        wide_at = None if isinstance(wide, (int, float)) else wide.get("at")
        wr = Result("min_wall_wide", wide_val, "mm", at=wide_at)
    else:
        wr = inconclusive("min_wall_wide", "mm", mw.reason or "no 45 deg reading in detail")
    rows.append(_named("U-06 (soft)", wr, ">=", WALL_WIDE, MM))

    # D-03a overhang, printed foot down along -Y
    oh = overhang_census(shape, build_dir=(0, -1, 0), min_deg=OVERHANG_MIN)
    rows.append(_named("D-03a", oh, ">=", OVERHANG_MIN, DEG, ["A-13"]))
    rows.extend(_safe("D-03b", lambda: _bridge(shape)))

    # holes
    bc = bore_census(shape)
    for x, z in HOLES:
        lb = locate_bore(bc, (x, 38.5, z), (0, 1, 0))
        tag = f"({x:+.1f}, {z:+.1f})"
        rows.append(_named(f"D-04a {tag}", lb["diameter"], ">=", HOLE_D_MIN, MM))
        rows.append(_named(f"REQ-07 diameter {tag}", lb["diameter"], "in",
                           (HOLE_D - HOLE_D_TOL, HOLE_D + HOLE_D_TOL), MM, ["A-11"]))
        rows.append(_named(f"REQ-07 offset {tag}", lb["offset"], "<=", HOLE_OFFSET, MM, ["A-11"]))
        rows.append(_named(f"REQ-07 through {tag}", lb["through"], "==", 1, COUNT, ["A-11"]))

    # REQ-01 saddle radius over both rib windows
    for lo, hi in SADDLE_BANDS:
        rp = radial_profile(shape, *AXIS, SADDLE_THETAS, (lo, hi), margin=0.0, z_step=0.1,
                            side="inner")
        for k in ("min", "max"):
            rows.append(_named(f"REQ-01 {k} z {lo}..{hi}", rp[k], "in", SADDLE_R, MM, ["A-03"]))

    # REQ-02 sector
    for z in REQ02_Z:
        for th in REQ02_IN:
            r = radial_extent(shape, *AXIS, th, z, side="inner")
            rows.append(_named(f"REQ-02 inner r at th {th:.0f} z {z:.0f}", r, "<=", REQ02_RIN_MAX,
                               MM, ["A-06"]))
        for th in REQ02_OUT:
            r = radial_extent(shape, *AXIS, th, z, side="inner", r_max=REQ02_RCLEAR)
            g = _named(f"REQ-02 window r<=32 at th {th:.0f} z {z:.0f} (expected: no material)", r,
                       ">=", 0.0, MM, ["A-06"])
            rows.append(g)
            # positive control 1: the first material on the whole ray lies beyond r 32.0.
            # Only where a post block spans the level (z 12 ... 33); at z 0 the whole ray
            # holds no material and the tool reads INCONCLUSIVE, recorded as such.
            if POST_Z[0] < z < POST_Z[1]:
                r2 = radial_extent(shape, *AXIS, th, z, side="inner")
                rows.append(_named(f"REQ-02 first material at th {th:.0f} z {z:.0f}", r2, ">=",
                                   REQ02_RCLEAR, MM, ["A-06"]))
            # positive control 2 (every level): the distance from the cradle to the ray
            # segment r 0 ... 32.0 is a measured number > 0 when no material lies on it.
            PART_INFO[f"REQ-02 segment r 0..32 th {th:.0f} z {z:.0f}"] = _segment(shape, th, z)
    rows.extend(_safe("REQ-02 rib faces", lambda: _rib_faces(shape)))

    # REQ-05 slots, REQ-06 posts, REQ-08 foot
    rows.extend(_safe("REQ-05", lambda: _slots(shape)))
    rows.extend(_safe("REQ-06", lambda: _posts(shape)))
    rows.append(_named("REQ-08 underside max_y", env["max_y"], "in",
                       (FOOT_Y - FOOT_TOL, FOOT_Y + FOOT_TOL), MM, ["A-11"]))
    rows.extend(_safe("REQ-08 thickness", lambda: _foot(shape, env)))
    return rows


def _segment(shape, th, z) -> dict:
    """Information, not a gate row: distance from the cradle to the straight segment
    from the axis to r = 32.0 at angle th and level z (tools.measure.clearance against
    an Edge). A positive distance says no material lies on the segment."""
    try:
        a = math.radians(th)
        seg = Edge.make_line((0.0, 0.0, z),
                             (REQ02_RCLEAR * math.cos(a), REQ02_RCLEAR * math.sin(a), z))
        c = clearance(shape, seg)
        return {"distance_mm": c.measured, "on_cradle": c.at, "on_segment": c.detail.get("on_b")}
    except Exception as exc:                                  # noqa: BLE001
        return {"error": f"{type(exc).__name__}: {exc}"}


PART_INFO: dict = {}


def _census_by_position(shape) -> list[Gate]:
    rows = []
    saddles = []
    for f in shape.faces():
        if f.geom_type == GeomType.CYLINDER:
            o, d, r = cylinder(f.wrapped)
            if abs(abs(d[2]) - 1) < 1e-6 and abs(r - 26.65) < 0.2 and math.hypot(o[0], o[1]) < 1e-6:
                saddles.append(f)
    rows.append(_named("U-05 saddle ribs (arc faces on the pump axis)",
                       _count("saddle_arcs", len(saddles)), "==", 2, COUNT))
    posts = [f for f in _planes(shape, 0)
             if abs(abs(f.center().X) - POST_X) < 0.5 and _box(f)[1][1] - _box(f)[0][1] > 20]
    rows.append(_named("U-05 post blocks (inner faces)", _count("post_inner_faces", len(posts)),
                       "==", 2, COUNT))
    floors = [f for f in _planes(shape, 1)
              if abs(f.center().Y - (SLOT_YC + SLOT_H / 2)) <= SLOT_C_TOL + 0.01
              and abs(f.center().X) > 28 and _box(f)[1][0] - _box(f)[0][0] < 5]
    rows.append(_named("U-05 strap slots (slot floors)", _count("slot_floors", len(floors)),
                       "==", 4, COUNT))
    bc = bore_census(shape)
    located = 0
    for x, z in HOLES:
        lb = locate_bore(bc, (x, 38.5, z), (0, 1, 0))
        if lb["offset"].ok and lb["offset"].measured <= HOLE_OFFSET:
            located += 1
    rows.append(_named("U-05 through-holes located", _count("holes_located", located), "==", 4,
                       COUNT))
    feet = [f for f in _planes(shape, 1) if abs(f.center().Y - FOOT_Y) < 0.5]
    rows.append(_named("U-05 foot plate (underside faces)", _count("foot_underside", len(feet)),
                       "==", 1, COUNT))
    return rows


def _bridge(shape) -> Gate:
    """Largest flat downward face (angle from horizontal under 1 deg, printed along -Y):
    a flat ceiling is a bridge; its shorter side is the span."""
    span = 0.0
    where = None
    for f in _planes(shape, 1):
        n = f.normal_at(f.center())
        a, b = _box(f)
        if n.Y > 0.5 and b[1] < FOOT_Y - 0.01:          # faces the bed, not on it
            s = min(b[0] - a[0], b[2] - a[2])
            if s > span:
                span, where = s, tuple(f.center())
    return _named("D-03b", Result("bridge_span", span, "mm", at=where), "<=", BRIDGE_MAX, MM,
                  note="designer reading; the reviewer confirms from sections")


def _rib_faces(shape) -> list[Gate]:
    rows = []
    faces = [f for f in _planes(shape, 2) if _within(f, (-25, 15, -100), (25, 38, 100))
             and _box(f)[0][1] < 30]
    for z in RIB_FACES_Z:
        hit = [f for f in faces if abs(f.center().Z - z) < 1.0]
        if len(hit) != 1:
            rows.append(gate(f"REQ-02 rib face z {z}", inconclusive(
                "rib_face", "mm", f"{len(hit)} rib faces near z {z}"), "==", z, band=MM))
            continue
        e = _env(hit[0])
        rows.append(_named(f"REQ-02 rib face z {z}", e["min_z"], "in", (z - FACE_TOL, z + FACE_TOL),
                           MM, ["A-06"]))
    return rows


def _slots(shape) -> list[Gate]:
    rows = []
    for sx in (-1, 1):
        post = [f for f in _planes(shape, 2)
                if sx * f.center().X > POST_X - 0.5 and sx * f.center().X < POST_X + 5
                and _box(f)[1][1] - _box(f)[0][1] > 20]          # post end faces (z 13, 33)
        post_z = sorted(_env(f)["min_z"].measured for f in post)
        for zc in SLOT_ZC:
            tag = f"x {'+' if sx > 0 else '-'} z {zc:.0f}"
            walls = [f for f in _planes(shape, 2)
                     if sx * f.center().X > POST_X - 0.5 and sx * f.center().X < POST_X + 5
                     and abs(f.center().Z - zc) < SLOT_W and _box(f)[1][1] - _box(f)[0][1] < 5]
            if len(walls) != 2:
                rows.append(gate(f"REQ-05 {tag}", inconclusive("slot_walls", "mm",
                                 f"{len(walls)} slot side walls found"), ">=", SLOT_W, band=MM))
                continue
            e = [_env(w) for w in walls]
            zlo = min(x["min_z"].measured for x in e)
            zhi = max(x["max_z"].measured for x in e)
            ylo = max(x["min_y"].measured for x in e)
            yhi = min(x["max_y"].measured for x in e)
            xs = min(x["size_x"].measured for x in e)
            rows.append(_named(f"REQ-05 clear Z {tag}", Result("slot_clear_z", zhi - zlo, "mm"),
                               ">=", SLOT_W, MM, ["A-07"]))
            rows.append(_named(f"REQ-05 clear Y {tag}", Result("slot_clear_y", yhi - ylo, "mm"),
                               ">=", SLOT_H, MM, ["A-07"]))
            rows.append(_named(f"REQ-05 centre y {tag}", Result("slot_centre_y", (yhi + ylo) / 2, "mm"),
                               "in", (SLOT_YC - SLOT_C_TOL, SLOT_YC + SLOT_C_TOL), MM, ["A-07"]))
            rows.append(_named(f"REQ-05 centre z {tag}", Result("slot_centre_z", (zhi + zlo) / 2, "mm"),
                               "in", (zc - SLOT_C_TOL, zc + SLOT_C_TOL), MM, ["A-07"]))
            rows.append(_named(f"REQ-05 through X {tag}", Result("slot_length_x", xs, "mm"), ">=",
                               4.0, MM, ["A-07"]))
            roofs = [f for f in shape.faces() if f.geom_type == GeomType.PLANE
                     and sx * f.center().X > POST_X - 0.5 and abs(f.center().Z - zc) < SLOT_W / 2
                     and f.center().Y < ylo and abs(f.normal_at(f.center()).Y) > 0.1
                     and abs(f.normal_at(f.center()).Z) > 0.1]
            if len(roofs) == 2:
                ang = min(math.degrees(math.asin(min(1.0, abs(r.normal_at(r.center()).Z))))
                          for r in roofs)
                rows.append(_named(f"REQ-05 roof angle from horizontal {tag}",
                                   Result("slot_roof_deg", ang, "deg"), ">=", OVERHANG_MIN, DEG,
                                   ["A-07", "A-13"]))
            else:
                rows.append(gate(f"REQ-05 roof {tag}", inconclusive("slot_roof", "deg",
                                 f"{len(roofs)} roof faces"), ">=", OVERHANG_MIN, band=DEG))
            below = [p for p in post_z if p < zlo]
            above = [p for p in post_z if p > zhi]
            others = [s for s in SLOT_ZC if s != zc]
            lig = []
            if below:
                lig.append(zlo - max(below))
            if above:
                lig.append(min(above) - zhi)
            for o in others:
                gap = abs(o - zc) - SLOT_W   # neighbour slot measured the same way
                lig.append(gap)
            rows.append(_named(f"REQ-05 ligament {tag}", Result("slot_ligament", min(lig), "mm"),
                               ">=", LIGAMENT, MM, ["A-07"]))
    return rows


def _posts(shape) -> list[Gate]:
    rows = []
    for sx in (-1, 1):
        faces = [f for f in _planes(shape, 0)
                 if abs(abs(f.center().X) - POST_X) < 0.5 and sx * f.center().X > 0
                 and _box(f)[1][1] - _box(f)[0][1] > 20]
        tag = "+X" if sx > 0 else "-X"
        if len(faces) != 1:
            rows.append(gate(f"REQ-06 {tag}", inconclusive("post_face", "mm",
                             f"{len(faces)} inner faces"), "==", POST_X, band=MM))
            continue
        e = _env(faces[0])
        xr = Result("post_inner_abs_x", abs(e["min_x"].measured), "mm", at=tuple(faces[0].center()))
        rows.append(_named(f"REQ-06 inner face |x| {tag}", xr, "in", (POST_X - POST_TOL, POST_X + POST_TOL),
                           MM, ["A-06"]))
        rows.append(_named(f"REQ-06 z min {tag}", e["min_z"], "in",
                           (POST_Z[0] - POST_TOL, POST_Z[0] + POST_TOL), MM, ["A-06"]))
        rows.append(_named(f"REQ-06 z max {tag}", e["max_z"], "in",
                           (POST_Z[1] - POST_TOL, POST_Z[1] + POST_TOL), MM, ["A-06"]))
    return rows


def _foot(shape, env) -> Gate:
    tops = [f for f in _planes(shape, 1) if abs(f.center().Y - (FOOT_Y - FOOT_T)) < 0.5
            and _box(f)[1][0] - _box(f)[0][0] > 70]
    if len(tops) != 1:
        return gate("REQ-08 thickness", inconclusive("foot_top", "mm", f"{len(tops)} foot top faces"),
                    "in", (FOOT_T - FOOT_TOL, FOOT_T + FOOT_TOL), band=MM)
    top = _env(tops[0])["min_y"].measured
    return _named("REQ-08 thickness", Result("foot_thickness", env["max_y"].measured - top, "mm"),
                  "in", (FOOT_T - FOOT_TOL, FOOT_T + FOOT_TOL), MM, ["A-11"])


# ---- export predicates -------------------------------------------------------------
def roundtrip_gates(built, step_path: Path) -> list[Gate]:
    c = compare_step(built, step_path)
    return [_named("U-04 schema AP242", c["schema"], "==", 1, COUNT),
            _named("U-04 solids", c["solids"], "==", 1, COUNT),
            _named("U-04 volume_delta", c["volume_delta"], "<=", 0.0, MM3),
            _named("U-04 faces_delta", c["faces_delta"], "==", 0, COUNT),
            _named("U-04 labels", c["labels"], "==", 1, COUNT),
            _named("U-04 valid_after", c["valid_after"], "==", 1, COUNT)]


def stl_gates(step_path: Path, stl_path: Path, angular: float) -> list[Gate]:
    """U-07: mesh the re-imported STEP afresh at the delivery settings into a scratch
    file, gate the sagitta, and hold the delivered STL to the same triangle count."""
    shape = read_step(step_path)
    rows = [_named("U-07 angular tolerance", Result("stl_angular_rad", angular, "rad"), "<=",
                   STL_ANG_MAX, 0.0)]
    with tempfile.TemporaryDirectory() as tmp:
        w = write_stl(shape, Path(tmp) / "check.stl", tolerance=STL_TOL, angular_tolerance=angular)
        rows.append(_named("U-07 stl_max_sagitta", w.checks["max_sagitta"], "<=", STL_TOL, MM))
        tri = w.detail.get("triangles")
    mc = mesh_census(stl_path)
    rows.append(_named("U-07 delivered STL triangles match", Result(
        "stl_triangles_match", int(mc["triangles"].ok and mc["triangles"].measured == tri), "bool",
        detail={"delivered": mc["triangles"].measured, "remeshed": tri}), "==", 1, COUNT))
    rows.append(_named("U-07 delivered STL bodies", mc["bodies"], "==", 1, COUNT))
    rows.append(_named("U-07 delivered STL naked_edges", mc["naked_edges"], "==", 0, COUNT))
    return rows


# ---- assembly predicates -----------------------------------------------------------
def assembly_gates(asm_path: Path) -> tuple[list[Gate], dict]:
    asm = read_step(asm_path)
    cradle, pump, sleeve = (_part(asm, n) for n in (CRADLE, PUMP, SLEEVE))
    info = {}
    rows: list[Gate] = []
    missing = [n for n, p in ((CRADLE, cradle), (PUMP, pump), (SLEEVE, sleeve)) if p is None]
    if missing:
        rows.append(gate("U-03", inconclusive("assembly_parts", "count", f"missing {missing}"),
                         "==", 3, band=0))
        return rows, info
    pv = validity(pump)
    pump_sound = all(r.ok for r in pv.values()) and pv["solid_count"].measured == 1 and \
        pv["brep_valid"].measured == 1 and pv["naked_edges"].measured == 0
    info["pump_validity"] = {k: r.measured for k, r in pv.items()}

    c = clearance(cradle, pump)
    info["cradle_pump_nearest"] = {"on_cradle": c.at, "on_pump": c.detail.get("on_b")}
    rows.append(_named("REQ-03", c, ">=", PUMP_CLEAR, MM, ["A-01", "A-03"],
                       note=f"pump point {c.detail.get('on_b')}"))
    rows.append(_named("U-03 (a) clearance cradle|OD-H01", c, ">=", PUMP_CLEAR, MM, ["A-01", "A-03"]))
    rows.append(_named("D-04c", c, ">=", SEATED_CLEAR, MM, ["A-01"]))
    if pump_sound:
        it = interference({CRADLE: cradle, PUMP: pump})
        rows.append(_named("U-03 (a) interference cradle|OD-H01", it[f"{CRADLE}|{PUMP}"], "<=", 0.0,
                           MM3, ["A-01", "A-03"]))
    else:
        rows.append(gate("U-03 (a) interference cradle|OD-H01", inconclusive(
            "interference", "mm3", "OD-H01 is not a sound solid"), "<=", 0.0, band=MM3))

    # posts alone to the pump (REQ-06, part of REQ-03)
    s = clearance(cradle, sleeve)
    info["cradle_sleeve_nearest"] = {"on_cradle": s.at, "on_sleeve": s.detail.get("on_b")}
    rows.append(_named("REQ-04 clearance cradle|sleeve", s, "==", 0.0, MM, ["A-03"]))
    rows.append(_named("U-03 (a) clearance cradle|sleeve", s, "==", 0.0, MM, ["A-03"]))
    if s.ok and s.at is not None:
        x, y, _ = s.at
        r = math.hypot(x, y)
        th = math.degrees(math.atan2(y, x))
        rows.append(_named("REQ-04 nearest point radius (on a saddle arc)",
                           Result("contact_radius", r, "mm", at=s.at, detail={"theta_deg": th}),
                           "in", SADDLE_R, MM, ["A-03"], note=f"theta {th:.2f} deg"))
        rows.append(_named("REQ-04 nearest point theta (saddle sector 45..135)",
                           Result("contact_theta", th, "deg", at=s.at), "in", (45.0, 135.0), DEG,
                           ["A-03"]))
    it2 = interference({CRADLE: cradle, SLEEVE: sleeve})
    rows.append(_named("REQ-04 interference cradle|sleeve", it2[f"{CRADLE}|{SLEEVE}"], "<=", 0.0, MM3,
                       ["A-03"]))
    rows.append(_named("U-03 (a) interference cradle|sleeve", it2[f"{CRADLE}|{SLEEVE}"], "<=", 0.0,
                       MM3, ["A-03"]))
    # information only: clearance of each cradle region to OD-H01 (rib 1 must not meet
    # an OD-H01 feature; brief WP-05), and the pump's centre of mass against the saddle span
    regions = {"rib 1 with web (z -3 ... 3)": ((-25, 0, -3.5), (25, 36.9, 3.5)),
               "rib 2 with web (z 25 ... 31)": ((-25, 0, 24.5), (25, 36.9, 31.5)),
               "-X post block": ((-40, -1, 11), (-29, 36.9, 34)),
               "+X post block": ((29, -1, 11), (40, 36.9, 34)),
               "foot plate (y 37 ... 40)": ((-41, 36.9, -11), (41, 41, 43))}
    info["region_clearance_to_OD-H01"] = {}
    for name, (lo, hi) in regions.items():
        try:
            box = Pos(*[(a + b) / 2 for a, b in zip(lo, hi)]) * Box(*[b - a for a, b in zip(lo, hi)])
            piece = cradle & box
            rc = clearance(piece, pump)
            info["region_clearance_to_OD-H01"][name] = {"mm": rc.measured, "on_cradle": rc.at,
                                                        "on_pump": rc.detail.get("on_b")}
        except Exception as exc:                              # noqa: BLE001
            info["region_clearance_to_OD-H01"][name] = {"error": f"{type(exc).__name__}: {exc}"}
    try:
        pm = mass_properties(pump, DENSITY)                 # centroid; density does not move it
        info["OD-H01_centroid"] = {k: pm[k].measured for k in ("com_x", "com_y", "com_z")}
        info["saddle_span_z"] = (RIB_FACES_Z[0], RIB_FACES_Z[-1])
    except Exception as exc:                                  # noqa: BLE001
        info["OD-H01_centroid"] = {"error": f"{type(exc).__name__}: {exc}"}
    # information only (not a section 5 pair): the assumed sleeve against the pump
    sp = interference({SLEEVE: sleeve, PUMP: pump})[f"{SLEEVE}|{PUMP}"]
    info["sleeve_pump_common_mm3"] = sp.measured if sp.ok else sp.reason
    info["sleeve_solids"] = len(sleeve.solids())
    return rows, info


def fixed_rows() -> list[Gate]:
    """Rows answered by the spec itself: N/A and the bench gate."""
    na = "N/A by its row"
    return [Gate("U-03 (b)", None, "", "no motion variable (ties not modelled)", None, na,
                 INCONCLUSIVE, "none", (), "N/A by its row: no motion variable"),
            Gate("U-08", None, "", "threads cosmetic", None, na, INCONCLUSIVE, "none", (),
                 "N/A by its row: no threads"),
            Gate("D-07", None, "", "fit-critical bores", None, na, INCONCLUSIVE, "none", (),
                 "N/A by its row: clearance holes only"),
            Gate("REQ-09 (soft)", None, "", "no unacceptable vibration (Soft, bench)", None, "bench",
                 INCONCLUSIVE, "none", ("A-03", "A-05"),
                 "Soft bench gate (spec 1.2): not geometric, INCONCLUSIVE until the first run")]


def facts(step_path: Path) -> dict:
    shape = read_step(step_path)
    mp = mass_properties(shape, DENSITY)
    return {k: r.measured for k, r in mp.items()}


def run_all(step_path: Path, asm_path: Path, stl_path: Path | None, *, built=None,
            angular: float | None = None) -> dict:
    rows = part_gates(step_path)
    if built is not None:
        rows += roundtrip_gates(built, step_path)
    if stl_path is not None and angular is not None:
        rows += _safe("U-07", lambda: stl_gates(step_path, stl_path, angular))
    arows, info = assembly_gates(asm_path)
    info.update(PART_INFO)
    rows += arows + fixed_rows()
    return {"gates": [dict(g.row(), reason=g.reason) for g in rows], "info": info,
            "facts": facts(step_path)}


def summary(result: dict) -> dict:
    """Worst row per gate family (the id before the first space)."""
    fam: dict[str, dict] = {}
    order = {"FAIL": 0, "INCONCLUSIVE": 1, "PASS_ASSUMED": 2, "PASS": 3}
    for g in result["gates"]:
        k = g["gate"].split(" ")[0]
        cur = fam.get(k)
        if cur is None or order[g["status"]] < order[cur["status"]] or (
                order[g["status"]] == order[cur["status"]] and g["margin"] is not None
                and (cur["margin"] is None or g["margin"] < cur["margin"])):
            fam[k] = g
    return fam


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    args = sys.argv[1:]
    step = Path(args[0]) if args else WS / "02_STEP_STL/od_c03_cradle_C1_v02.step"
    asm = Path(args[1]) if len(args) > 1 else WS / "02_STEP_STL/od_c03_assembly_C1_v02.step"
    stl = Path(args[2]) if len(args) > 2 else WS / "02_STEP_STL/od_c03_cradle_C1_v02.stl"
    import build_od_c03_cradle_v02 as build                    # U-04 compares with the nominal build
    out = run_all(step, asm, stl, built=build.build(build.P()), angular=build.P().stl_ang)
    print(json.dumps(out, indent=1, default=str))
