"""check_od_g01_housing_v03.py - one predicate per DESIGN_SPEC 1.3 §5 gate id (D3).

Written before build_od_g01_housing_v03.py. Every predicate re-imports the exported
STEP, gates tools.core.validity first, measures with tools/measure on the B-rep,
and compares only through tools.result.gate, with the limit from spec §5 and the
band from GATES §0 (0.005 mm, 0.001 deg, 0.001 mm3, 0 for counts and 1/0 facts).
A raised exception or a missing value is INCONCLUSIVE and never a PASS.

What changed from v02 (spec 1.3), and nothing else - the geometry is v02's:

- **the locked pose of OD-G10 is measured, not fixed.** Spec 1.3 §5 U-03(a) reads
  "the locked pose is the measured first contact of the three ear tops with the lug
  undersides as OD-G10 moves along +Z at the locked clock (report the rim z; A-14
  expects -11.20 +- 0.10); clearance = 0 there; clearance in [0.19, 0.21] with
  OD-G10 displaced 0.20 along -Z from that pose". So the pose comes from
  assemble_od_g01_check_v03.first_contact_rim_z(), a bisection on the distance, and
  the rim z it returns is gated against A-14's band and carried into the probe, the
  per-lug diagnostics, the lock path and the check assembly. When the bisection
  cannot answer, every row that rests on it is INCONCLUSIVE, never a PASS.
- **the 0.20 mm probe is displaced along -Z**, the direction that opens the designed
  contact. The +Z reading is kept as a reported diagnostic beside it, not as a gate:
  spec 1.3 names one direction.

Unchanged from v02: the Ø26 opening runs straight through the 5.00 slab (REQ-11
length 5.00, REQ-13 the two Ø9 pair-A holes only); REQ-03's lug rays are start + 1,
+ 27, + 40 deg and its gap rays start - 1 and + 55 deg; REQ-04's brackets are
start + 20 deg at z -5.7 / -6.7 and start + 47 deg at z -3.2 / -4.2; the OD-G10
boolean is reported INCONCLUSIVE beside the distance rows (A-28); U-03(b) walks the
three-leg lock path of assemble_od_g01_check_v03.lock_path.

Rows whose spec cell says "reviewer" or "bench test" (D-03a, D-03b, E-06, REQ-12,
and the boss OD half of D-05a) are reported INCONCLUSIVE with the missing tool
named: no local predicate stands in for them.

Run on its own:  uv run tools/run.py python 01_CAD/check_od_g01_housing_v03.py
"""
from __future__ import annotations

import json
import math
from dataclasses import replace
from pathlib import Path

from tools.core import read_step, validity
from tools.core.step import compare_step
from tools.measure import (bore_census, clearance, envelope, feature_census, interference,
                           locate_bore, mass_properties, min_wall, radial_extent, radial_profile)
from tools.result import INCONCLUSIVE, Result, gate, inconclusive

from assemble_od_g01_check_v03 import (A14_BAND, A14_RIM_Z, G10_LOCK_CLOCK_DEG,
                                       first_contact_rim_z, feature_pieces, load_mates,
                                       lock_path, lug_pieces, place_g04, place_g10,
                                       rotate_rim_z)

WORKSPACE = Path(__file__).resolve().parents[1]
STEP = WORKSPACE / "02_STEP_STL" / "od_g01_housing_C1_v03.step"

# ---------------------------------------------------------------- tolerance bands (GATES §0)
MM, DEG, MM3, COUNT = 0.005, 0.001, 0.001, 0

# ---------------------------------------------------------------- the frame and the probe rays
ORIGIN, ZDIR, XDIR = (0, 0, 0), (0, 0, 1), (1, 0, 0)
LUG_STARTS = (336.0, 96.0, 216.0)          # spec §2, §4 C1, A-04
LUG_SPAN = 54.0
R_WINDOW = (25.0, 45.0)                    # the annulus every inner ray reads (cup wall included)
R_WINDOW_OUT = (0.0, 55.0)

# ---------------------------------------------------------------- limits, spec §5 only
U02_SIZE = {"size_x": (99.9, 100.1), "size_y": (99.9, 100.1), "size_z": (28.14, 28.34)}
D02_BED = {"size_x": 220.0, "size_y": 220.0, "size_z": 250.0}          # A-16
U06_WIDE_WALL = 1.0
U07_TOL = 0.01
U07_ANG_TOL = 4 * math.acos(1 - 0.01 / 43.1)
D01A_WALL, D01B_WALL, D06A_FEATURE = 0.8, 1.0, 1.0
D04A_HOLE = 3.75
D05A_ACROSS = 8.0
D05B_DIA, D05B_DEPTH = (3.95, 4.05), 5.7
J05_WALL = 3.0
U03_CLEAR = 0.5                 # OD-G04's tabs, pair A, pair B, bead and hub
U03_CONTACT = 0.0               # the designed contacts
U03_PROBE_MM = 0.20             # the displacement spec 1.3 §5 U-03(a) asks for
U03_PROBE_SIGN = -1.0           # along -Z: spec 1.3 §5 U-03(a), the opening direction
U03_PROBE_BAND = (0.19, 0.21)   # what the clearance must read after it
U03_LOCKED_RIM_BAND = (A14_RIM_Z - A14_BAND, A14_RIM_Z + A14_BAND)   # A-14, spec §5 U-03(a)
U03_PATH_CLEAR = 0.30           # U-03(b), before the last 0.5 mm of approach
U03_PATH_SEAT = 0.0             # U-03(b), inside the last 0.5 mm of approach
U03_PATH_EXEMPT_MM = 0.5        # "the last 0.5 mm of approach"
U03_PATH_MIN_POSES = 40
REQ01_BAND, REQ01_Z = (31.58, 31.78), (-5.0, -1.0)
REQ02_BAND, REQ02_Z = (37.05, 37.15), (-13.0, 2.0)
REQ03_LUG, REQ03_GAP, REQ03_Z = 31.78, 37.05, -3.0
REQ03_LUG_RAYS, REQ03_GAP_RAYS = (1.0, 27.0, 40.0), (-1.0, 55.0)
REQ04_LUG, REQ04_CLEAR = 31.78, 34.0
REQ04_RAYS = ((20.0, -5.7, -6.7), (47.0, -3.2, -4.2))
REQ05_LUG, REQ05_CLEAR = 31.78, 34.0
REQ06_DIA = (25.9, 26.1)
REQ07_OFFSET, REQ07_RECESS_DIA, REQ07_RECESS_DEPTH = 0.10, (8.9, 9.1), (2.20, 2.40)
REQ08_OFFSET = 0.10
REQ09_OUTER, REQ09_INNER, REQ09_WALL = 43.05, 37.15, 5.9
REQ10_CLEAR = 0.30
REQ11_LENGTH = (4.90, 5.10)
REQ13_LOBE_DIA, REQ13_OFFSET = (8.9, 9.1), 0.10
D07_HUB_CLEAR = 2.9

# ---------------------------------------------------------------- where the features sit (§4 C1)
FLOOR_Z, SLAB_BACK_Z = -19.94, -24.94
KEYHOLE_Z = (-24.94, -19.94)               # the Ø26 opening, straight through the slab
LOBE_R, LOBE_THETA = 15.5, (359.5, 179.0)
PAIR_B_R, PAIR_B_THETA = 19.03, (119.3, 304.0)
PAIR_B_RECESS_Z = (-22.24, -19.94)
CARRIER_XY = 44.0
INSERT_TOP_Z = -19.24
ASSUMES = {"U-02": (), "D-02": ("A-16",), "D-05a": ("A-17",), "D-05b": ("A-17",),
           "U-03": ("A-13", "A-14", "A-19"), "REQ-01": ("A-02",), "REQ-02": ("A-03",),
           "REQ-03": ("A-04",), "REQ-04": ("A-05",), "REQ-05": ("A-06",),
           "REQ-06": ("A-10", "A-11"), "REQ-07": ("A-12", "A-26"), "REQ-08": ("A-18",),
           "REQ-09": ("A-21",), "REQ-10": ("A-19",), "REQ-11": ("A-10",),
           "REQ-13": ("A-11",), "D-04a": ("A-26",), "D-01b": ("A-05",), "D-07": ("A-24",)}


def _assumes(gate_id: str) -> tuple:
    return ASSUMES.get(gate_id.split()[0], ())


def worst(gate_id: str, subs: list) -> object:
    """One row per gate id: INCONCLUSIVE if any sub-row is, else the worst FAIL, else
    the smallest margin. The sub-rows stay in the JSON beside it."""
    subs = [s for s in subs if s is not None]
    if not subs:
        return None
    bad = [g for g in subs if g.status == INCONCLUSIVE]
    if bad:
        return replace(bad[0], gate=gate_id)
    failed = [g for g in subs if not g.passed]
    pool = failed or subs
    pick = min(pool, key=lambda g: (g.margin if g.margin is not None else 0.0))
    return replace(pick, gate=gate_id)


def polar(r: float, theta_deg: float) -> tuple:
    return (r * math.cos(math.radians(theta_deg)), r * math.sin(math.radians(theta_deg)))


def extent(shape, angle: float, z: float, side: str, window=R_WINDOW) -> Result:
    return radial_extent(shape, ORIGIN, ZDIR, XDIR, angle, z, side=side,
                         r_min=window[0], r_max=window[1])


def _at(angle: float, z: float) -> str:
    return f"theta {angle:.2f} deg, z {z:.2f} mm"


# =====================================================================  universal rows
def gates_validity(shape) -> tuple[list, dict]:
    v = validity(shape)
    rows = [gate("U-01", v["solid_count"], "==", 1, band=COUNT),
            gate("U-01", v["brep_valid"], "==", 1, band=COUNT),
            gate("U-01", v["naked_edges"], "==", 0, band=COUNT)]
    return [worst("U-01", rows),
            replace(gate("exactly_one_solid", v["solid_count"], "==", 1, band=COUNT),
                    gate="exactly_one_solid")], v


def gates_envelope(shape) -> tuple[list, dict]:
    e = envelope(shape)
    size = [gate("U-02", e[k], "in", v, band=MM) for k, v in U02_SIZE.items()]
    bed = [gate("D-02", e[k], "<=", v, band=MM, assumes=_assumes("D-02")) for k, v in D02_BED.items()]
    rows = [worst("U-02", size), worst("envelope_within_spec", size), worst("D-02", bed)]
    position = {k: (e[k].measured if e[k].ok else None)
                for k in ("min_x", "max_x", "min_y", "max_y", "min_z", "max_z")}
    return rows, position


def gates_roundtrip(built, path: Path) -> tuple[list, list]:
    r = compare_step(built, path)
    rows = [gate("U-04", r["schema"], "==", 1, band=COUNT),
            gate("U-04", r["solids"], "==", 1, band=COUNT),
            gate("U-04", r["labels"], "==", 1, band=COUNT),
            gate("U-04", r["faces_delta"], "==", 0, band=COUNT),
            gate("U-04", r["volume_delta"], "<=", 0.0, band=MM3),
            gate("U-04", r["valid_after"], "==", 1, band=COUNT)]
    return [worst("U-04", rows)], rows


def gates_walls(shape) -> tuple[list, dict]:
    w = min_wall(shape)
    rows = [gate("D-01a", w, ">=", D01A_WALL, band=MM),
            gate("D-01b", w, ">=", D01B_WALL, band=MM, assumes=_assumes("D-01b")),
            gate("D-06a", w, ">=", D06A_FEATURE, band=MM)]
    wide = w.detail.get("wide") if isinstance(w.detail, dict) else None
    if isinstance(wide, dict) and wide.get("measured") is not None:
        wide_result = Result("min_wall_wide", wide["measured"], "mm", at=wide.get("at"),
                             params={"opposition_deg": 45.0})
    else:
        wide_result = inconclusive("min_wall_wide", "mm",
                                   "min_wall gave no detail['wide'] value (U-06)")
    rows.append(gate("U-06", wide_result, ">=", U06_WIDE_WALL, band=MM))
    return rows, {"min_wall": w.to_dict()}


def gates_mesh(stl_written) -> list:
    if stl_written is None:
        return [inconclusive_gate("U-07", "mm", "no STL was written in this run")]
    sagitta = stl_written.checks["max_sagitta"]
    ang = Result("stl_angular_tolerance", stl_written.detail["angular_tolerance_rad"], "rad")
    tol = Result("stl_tolerance", stl_written.detail["tolerance_mm"], "mm")
    rows = [gate("U-07", sagitta, "<=", U07_TOL, band=MM),
            gate("U-07", tol, "<=", U07_TOL, band=MM),
            gate("U-07", ang, "<=", U07_ANG_TOL, band=0.00002)]
    return [worst("U-07", rows)]


def inconclusive_gate(gate_id: str, unit: str, reason: str):
    return gate(gate_id, inconclusive(gate_id, unit, reason), ">=", 0.0, band=0.0)


# =====================================================================  census (U-05)
def bores_by_diameter(census: Result, low: float, high: float) -> list:
    return [b for b in census.detail["bores"] if low <= b["diameter"] <= high]


def gates_census(shape, census: Result) -> tuple[list, dict]:
    fc = feature_census(shape)
    rows, detail = [], {"faces": {k: (r.measured if r.ok else None) for k, r in fc.items()}}

    def count_row(name, n, expected):
        return gate("U-05", Result(f"census_{name}", n, "count"), "==", expected, band=COUNT)

    # bores by diameter, each located where the spec puts it (spec 1.2 §5 U-05)
    groups = {"keyhole_26": (25.9, 26.1, 1), "lobe_and_recess_9": (8.9, 9.1, 4),
              "screw_3p8": (3.75, 3.85, 2), "insert_4p0": (3.95, 4.05, 4)}
    found = {}
    for name, (low, high, expected) in groups.items():
        hits = bores_by_diameter(census, low, high)
        found[name] = [{"diameter": round(b["diameter"], 4), "start": b["start"], "end": b["end"],
                        "length": round(b["length"], 4), "through": b.get("through")} for b in hits]
        rows.append(count_row(name, len(hits), expected))
    detail["bores"] = found

    # lugs, stop blocks and pockets, counted from the material each puts on a ray
    lugs = stops = pockets = 0
    probes = []
    for start in LUG_STARTS:
        mid = extent(shape, start + 27.0, REQ03_Z, "inner")
        lugs += int(mid.ok and mid.measured <= REQ03_LUG)
        below = extent(shape, start + 2.9, -11.0, "inner")
        above = extent(shape, start + 2.9, -9.0, "inner")
        stops += int(above.ok and below.ok and above.measured <= REQ05_LUG
                     and below.measured >= REQ05_CLEAR)
        inside = extent(shape, start + 26.75, -16.0, "inner")
        under = extent(shape, start + 26.75, -17.6, "inner")
        pockets += int(inside.ok and under.ok and inside.measured >= 34.5 and under.measured <= 31.75)
        probes += [{"at": _at(start + 27.0, REQ03_Z), "inner": mid.measured},
                   {"at": _at(start + 2.9, -9.0), "inner": above.measured},
                   {"at": _at(start + 2.9, -11.0), "inner": below.measured},
                   {"at": _at(start + 26.75, -16.0), "inner": inside.measured},
                   {"at": _at(start + 26.75, -17.6), "inner": under.measured}]
    detail["sector_probes"] = probes
    rows += [count_row("lugs", lugs, 3), count_row("stop_blocks", stops, 3),
             count_row("pockets", pockets, 3)]
    # U-08: the target has no thread (its row says N/A); no helical or unnamed face
    u08 = gate("U-08", fc["other_faces"], "==", 0, band=COUNT)
    return [worst("U-05", rows), worst("feature_census", rows), u08], detail


# =====================================================================  located bores
def gates_bores(census: Result) -> tuple[list, dict]:
    rows, detail = [], {}
    key = locate_bore(census, (0, 0, sum(KEYHOLE_Z) / 2), (0, 0, 1))
    rows += [worst("REQ-06", [gate("REQ-06", key["diameter"], "in", REQ06_DIA, band=MM,
                                   assumes=_assumes("REQ-06")),
                              gate("REQ-06", key["offset"], "<=", REQ07_OFFSET, band=MM,
                                   assumes=_assumes("REQ-06")),
                              gate("REQ-06", key["through"], "==", 1, band=COUNT,
                                   assumes=_assumes("REQ-06"))]),
             gate("REQ-11", key["length"], "in", REQ11_LENGTH, band=MM, assumes=_assumes("REQ-11"))]
    detail["keyhole"] = {k: (r.measured if r.ok else None) for k, r in key.items()}

    # REQ-13 (spec 1.2): the two Ø9.0 pair-A pass-through holes, nothing else
    lobes, req13 = [], []
    for theta in LOBE_THETA:
        x, y = polar(LOBE_R, theta)
        b = locate_bore(census, (x, y, sum(KEYHOLE_Z) / 2), (0, 0, 1))
        lobes.append({k: (r.measured if r.ok else None) for k, r in b.items()})
        req13 += [gate("REQ-13", b["diameter"], "in", REQ13_LOBE_DIA, band=MM,
                       assumes=_assumes("REQ-13")),
                  gate("REQ-13", b["offset"], "<=", REQ13_OFFSET, band=MM, assumes=_assumes("REQ-13")),
                  gate("REQ-13", b["through"], "==", 1, band=COUNT, assumes=_assumes("REQ-13"))]
    rows.append(worst("REQ-13", req13))
    detail["lobes"] = lobes

    req07, d04a, pairb = [], [], []
    for theta in PAIR_B_THETA:
        x, y = polar(PAIR_B_R, theta)
        screw = locate_bore(census, (x, y, (PAIR_B_RECESS_Z[0] + SLAB_BACK_Z) / 2), (0, 0, 1))
        recess = locate_bore(census, (x, y, sum(PAIR_B_RECESS_Z) / 2), (0, 0, 1))
        pairb.append({"screw": {k: (r.measured if r.ok else None) for k, r in screw.items()},
                      "recess": {k: (r.measured if r.ok else None) for k, r in recess.items()}})
        req07 += [gate("REQ-07", screw["offset"], "<=", REQ07_OFFSET, band=MM, assumes=_assumes("REQ-07")),
                  gate("REQ-07", screw["through"], "==", 1, band=COUNT, assumes=_assumes("REQ-07")),
                  gate("REQ-07", recess["diameter"], "in", REQ07_RECESS_DIA, band=MM,
                       assumes=_assumes("REQ-07")),
                  gate("REQ-07", recess["length"], "in", REQ07_RECESS_DEPTH, band=MM,
                       assumes=_assumes("REQ-07"))]
        d04a.append(gate("D-04a", screw["diameter"], ">=", D04A_HOLE, band=MM, assumes=_assumes("D-04a")))
    rows += [worst("REQ-07", req07), worst("D-04a", d04a)]
    detail["pair_b"] = pairb

    req08, d05b, inserts = [], [], []
    for sx in (1, -1):
        for sy in (1, -1):
            point = (sx * CARRIER_XY, sy * CARRIER_XY, (SLAB_BACK_Z + INSERT_TOP_Z) / 2)
            b = locate_bore(census, point, (0, 0, 1))
            inserts.append({k: (r.measured if r.ok else None) for k, r in b.items()})
            req08.append(gate("REQ-08", b["offset"], "<=", REQ08_OFFSET, band=MM,
                              assumes=_assumes("REQ-08")))
            d05b += [gate("D-05b", b["diameter"], "in", D05B_DIA, band=MM, assumes=_assumes("D-05b")),
                     gate("D-05b", b["length"], ">=", D05B_DEPTH, band=MM, assumes=_assumes("D-05b"))]
    rows += [worst("REQ-08", req08), worst("D-05b", d05b)]
    detail["carrier_inserts"] = inserts
    return rows, detail


def gates_insert_walls(shape) -> tuple[list, dict]:
    """J-05 and D-05a around each carrier insert: the material on 24 rays from the
    insert's own axis, read from tools.measure.radial_extent's material stretches.
    The boss OD row of D-05a has no tool (GATES: reviewer); reported, not gated."""
    rings, j05, d05a = [], [], []
    for sx in (1, -1):
        for sy in (1, -1):
            axis = (sx * CARRIER_XY, sy * CARRIER_XY, 0)
            for z in (SLAB_BACK_Z + 1.0, SLAB_BACK_Z + 3.0, FLOOR_Z + 0.35):
                for k in range(24):
                    angle = k * 15.0
                    r = radial_extent(shape, axis, ZDIR, XDIR, angle, z, side="outer",
                                      r_min=0.0, r_max=140.0)
                    stretches = r.detail.get("material") if r.ok else None
                    if not stretches:
                        res = inconclusive("insert_wall", "mm",
                                           r.reason or "no material on the ray")
                    else:
                        first = min(stretches, key=lambda s: s[0])
                        res = Result("insert_wall", first[1] - 2.0, "mm",
                                     at=(axis[0], axis[1], z),
                                     params={"angle_deg": angle, "hole_r": 2.0,
                                             "stretch": first})
                    rings.append({"insert": [axis[0], axis[1]], "z": z, "angle": angle,
                                  "wall": None if not res.ok else round(res.measured, 4)})
                    j05.append(gate("J-05", res, ">=", J05_WALL, band=MM))
                    across = (replace(res, name="insert_material_across",
                                      measured=2 * (res.measured + 2.0)) if res.ok else res)
                    d05a.append(gate("D-05a", across, ">=", D05A_ACROSS, band=MM,
                                     assumes=_assumes("D-05a")))
    return [worst("J-05", j05), worst("D-05a", d05a)], {"insert_rings": rings}


# =====================================================================  the REQ profile rows
def _frange(low: float, high: float, step: float) -> list:
    n = int(round((high - low) / step))
    return [low + i * step for i in range(n + 1)]


def gates_profiles(shape, coarse: bool = False) -> tuple[list, dict]:
    rows, detail = [], {}
    step = 2.0 if coarse else 1.0
    angles01 = [s + a for s in LUG_STARTS for a in _frange(8.0, 40.0, step)]
    p1 = radial_profile(shape, ORIGIN, ZDIR, XDIR, angles01, REQ01_Z, margin=(0.0, 0.0),
                        z_step=0.2 if coarse else 0.1, side="inner",
                        r_min=R_WINDOW[0], r_max=R_WINDOW[1])
    rows.append(worst("REQ-01", [gate("REQ-01", p1["max"], "in", REQ01_BAND, band=MM,
                                      assumes=_assumes("REQ-01")),
                                 gate("REQ-01", p1["min"], "in", REQ01_BAND, band=MM,
                                      assumes=_assumes("REQ-01"))]))
    detail["REQ-01"] = {k: (r.measured, r.at) for k, r in p1.items()}

    angles02 = [s + a for s in LUG_STARTS for a in _frange(60.0, 114.0, 2.0 * step)]
    p2 = radial_profile(shape, ORIGIN, ZDIR, XDIR, angles02, REQ02_Z, margin=(0.0, 0.0),
                        z_step=0.4 if coarse else 0.2, side="inner",
                        r_min=R_WINDOW[0], r_max=R_WINDOW[1])
    rows.append(worst("REQ-02", [gate("REQ-02", p2["max"], "in", REQ02_BAND, band=MM,
                                      assumes=_assumes("REQ-02")),
                                 gate("REQ-02", p2["min"], "in", REQ02_BAND, band=MM,
                                      assumes=_assumes("REQ-02"))]))
    detail["REQ-02"] = {k: (r.measured, r.at) for k, r in p2.items()}

    angles09 = _frange(0.0, 355.0, 5.0 if not coarse else 15.0)
    # z_step is chosen so that no level lands on z = 0.0, the lug top plane: a ray there
    # runs along two faces at once at a lug side angle and cannot be read either side
    p9 = radial_profile(shape, ORIGIN, ZDIR, XDIR, angles09, (-19.0, 3.0), margin=(0.0, 0.0),
                        z_step=0.1 if not coarse else 0.3, side="outer",
                        r_min=R_WINDOW_OUT[0], r_max=R_WINDOW_OUT[1])
    wall = (Result("cup_wall", p9["min"].measured - p2["max"].measured, "mm",
                   at=p9["min"].at) if (p9["min"].ok and p2["max"].ok)
            else inconclusive("cup_wall", "mm", "the outer or inner profile is INCONCLUSIVE"))
    rows.append(worst("REQ-09", [gate("REQ-09", p9["min"], ">=", REQ09_OUTER, band=MM,
                                      assumes=_assumes("REQ-09")),
                                 gate("REQ-09", p2["max"], "<=", REQ09_INNER, band=MM,
                                      assumes=_assumes("REQ-09")),
                                 gate("REQ-09", wall, ">=", REQ09_WALL, band=MM,
                                      assumes=_assumes("REQ-09"))]))
    detail["REQ-09"] = {k: (r.measured, r.at) for k, r in p9.items()}
    detail["REQ-09 wall"] = wall.measured if wall.ok else None
    return rows, detail


def gates_rays(shape) -> tuple[list, dict]:
    rows, detail = [], []
    req03 = []
    for start in LUG_STARTS:
        for off in REQ03_LUG_RAYS:
            r = extent(shape, start + off, REQ03_Z, "inner")
            req03.append(gate("REQ-03", r, "<=", REQ03_LUG, band=MM, assumes=_assumes("REQ-03")))
            detail.append({"gate": "REQ-03", "at": _at(start + off, REQ03_Z),
                           "inner": None if not r.ok else round(r.measured, 4),
                           "required": "<= 31.78"})
        for off in REQ03_GAP_RAYS:
            r = extent(shape, start + off, REQ03_Z, "inner")
            req03.append(gate("REQ-03", r, ">=", REQ03_GAP, band=MM, assumes=_assumes("REQ-03")))
            detail.append({"gate": "REQ-03", "at": _at(start + off, REQ03_Z),
                           "inner": None if not r.ok else round(r.measured, 4),
                           "required": ">= 37.05"})
    rows.append(worst("REQ-03", req03))

    req04 = []
    for start in LUG_STARTS:
        for off, z_in, z_out in REQ04_RAYS:
            a = extent(shape, start + off, z_in, "inner")
            b = extent(shape, start + off, z_out, "inner")
            req04 += [gate("REQ-04", a, "<=", REQ04_LUG, band=MM, assumes=_assumes("REQ-04")),
                      gate("REQ-04", b, ">=", REQ04_CLEAR, band=MM, assumes=_assumes("REQ-04"))]
            detail += [{"gate": "REQ-04", "at": _at(start + off, z_in),
                        "inner": None if not a.ok else round(a.measured, 4), "required": "<= 31.78"},
                       {"gate": "REQ-04", "at": _at(start + off, z_out),
                        "inner": None if not b.ok else round(b.measured, 4), "required": ">= 34.0"}]
    rows.append(worst("REQ-04", req04))

    req05 = []
    for start in LUG_STARTS:
        a = extent(shape, start + 2.9, -9.0, "inner")
        b = extent(shape, start + 2.9, -11.0, "inner")
        req05 += [gate("REQ-05", a, "<=", REQ05_LUG, band=MM, assumes=_assumes("REQ-05")),
                  gate("REQ-05", b, ">=", REQ05_CLEAR, band=MM, assumes=_assumes("REQ-05"))]
        detail += [{"gate": "REQ-05", "at": _at(start + 2.9, -9.0),
                    "inner": None if not a.ok else round(a.measured, 4), "required": "<= 31.78"},
                   {"gate": "REQ-05", "at": _at(start + 2.9, -11.0),
                    "inner": None if not b.ok else round(b.measured, 4), "required": ">= 34.0"}]
    rows.append(worst("REQ-05", req05))
    return rows, {"rays": detail}


# =====================================================================  the assembly rows
def lumps(housing, other) -> list:
    """Where a common volume sits: one entry per lump, with its volume and its box, so
    a designed contact can be told from a clash. A diagnostic, never a gate: OD-G10's
    own STEP reads brep_valid = 0 (A-28)."""
    try:
        pieces = (housing & other).solids()
    except Exception as exc:                                    # noqa: BLE001
        return [{"error": f"{type(exc).__name__}: {exc}"}]
    out = []
    for solid in pieces:
        box = solid.bounding_box()
        out.append({"volume_mm3": round(solid.volume, 6),
                    "z": [round(box.min.Z, 4), round(box.max.Z, 4)],
                    "x": [round(box.min.X, 4), round(box.max.X, 4)],
                    "y": [round(box.min.Y, 4), round(box.max.Y, 4)],
                    "r_max": round(max(math.hypot(box.min.X, box.min.Y),
                                       math.hypot(box.max.X, box.max.Y)), 4)})
    return out


def gates_assembly(shape, path_poses: bool = True, insert_steps: int = 22,
                   rotate_steps: int = 14, seat_steps: int = 6,
                   pose_count: bool = True) -> tuple[list, dict]:
    """U-03(a), U-03(b), REQ-10 and the D-07 hub clearance, on the parts as placed."""
    rows, detail = [], {}
    g04, g10 = load_mates()
    g04p = place_g04(g04)
    pieces = feature_pieces(g04p)
    u03 = []

    pair = interference({"housing": shape, "od_g04": g04p})["housing|od_g04"]
    u03.append(gate("U-03 (a) housing|od_g04", pair, "<=", 0.0, band=MM3, assumes=_assumes("U-03")))
    detail["interference_g04_mm3"] = pair.measured if pair.ok else None

    seat = clearance(shape, g04p)
    u03.append(gate("U-03 (a) g04 flange on the floor", seat, "==", U03_CONTACT, band=MM,
                    assumes=_assumes("U-03")))
    detail["g04_contact"] = {"clearance": seat.measured if seat.ok else None, "at": str(seat.at),
                             "on_b": str(seat.detail.get("on_b")) if seat.ok else None}

    feature_rows, feature_detail = [], {}
    for name, piece in pieces.items():
        c = clearance(shape, piece)
        feature_rows.append(gate(f"U-03 (a) {name}", c, ">=", U03_CLEAR, band=MM,
                                 assumes=_assumes("U-03")))
        feature_detail[name] = {"clearance": c.measured if c.ok else None, "at": str(c.at),
                                "reason": c.reason}
    u03.append(worst("U-03 (a) g04 features", feature_rows))
    u03 += feature_rows
    detail["g04_features"] = feature_detail

    # --- OD-G10 at the locked pose (spec 1.3 §5 U-03(a)). The locked pose is not a
    # number here: it is the measured first contact of the three ear tops with the lug
    # undersides as OD-G10 moves along +Z at the locked clock. The rim z that
    # bisection returns is reported and gated against A-14's -11.20 +- 0.10; the
    # designed contact is gated at clearance = 0 there; and the probe row is the
    # clearance with OD-G10 displaced 0.20 mm along -Z from it, the direction that
    # opens the contact. If the bisection cannot answer, every row below it is
    # INCONCLUSIVE.
    locked_rim_z = first_contact_rim_z(shape, g10, G10_LOCK_CLOCK_DEG)
    detail["g10_locked_rim_z"] = locked_rim_z
    detail["a14_expectation"] = {"rim_z": A14_RIM_Z, "band": A14_BAND}
    if locked_rim_z is None:
        reason = ("the first contact of the ear tops with the lug undersides could not be "
                  "measured: the bisection bracket does not straddle it or a distance "
                  "could not be read (spec 1.3 §5 U-03(a))")
        u03 += [inconclusive_gate("U-03 (a) locked rim z", "mm", reason),
                inconclusive_gate("U-03 (a) ear tops on the lug undersides", "mm", reason),
                inconclusive_gate(f"U-03 (a) od_g10 moved {U03_PROBE_MM:.2f} along -Z",
                                  "mm", reason)]
        boolean_row = inconclusive_gate("U-03 (a) housing|od_g10 boolean", "mm3", reason)
        detail["g10_locked"] = None
        detail["g10_probe"] = None
    else:
        u03.append(gate("U-03 (a) locked rim z",
                        Result("g10_locked_rim_z", locked_rim_z, "mm",
                               params={"clock_deg": G10_LOCK_CLOCK_DEG,
                                       "expectation": "A-14 -11.20 +- 0.10"}),
                        "in", U03_LOCKED_RIM_BAND, band=MM, assumes=_assumes("U-03")))
        g10_locked = place_g10(g10, G10_LOCK_CLOCK_DEG, locked_rim_z)

        # the same distance lug by lug, on the housing cut into its three lug sectors:
        # a located diagnostic, not a gate. With the ears at 120.5 / 120.5 / 119 deg
        # (A-25) against lugs at a symmetric 120 deg pitch, the three ear tops cannot
        # all reach their underside at one pose, and spec §5 names one contact pair.
        ear_detail = {}
        for name, piece in lug_pieces(shape).items():
            c = clearance(piece, g10_locked)
            ear_detail[name] = {"clearance": c.measured if c.ok else None, "at": str(c.at),
                                "on_b": str(c.detail.get("on_b")) if c.ok else None,
                                "reason": c.reason}
        contact = clearance(shape, g10_locked)
        u03.append(gate("U-03 (a) ear tops on the lug undersides", contact, "==", U03_CONTACT,
                        band=MM, assumes=_assumes("U-03")))
        detail["g10_locked"] = {"rim_z": locked_rim_z,
                                "whole_part": {"clearance": contact.measured if contact.ok
                                               else None, "at": str(contact.at),
                                               "on_b": str(contact.detail.get("on_b"))
                                               if contact.ok else None},
                                "per_lug": ear_detail}

        # the 0.20 mm probe: spec 1.3 displaces OD-G10 along -Z from the measured
        # locked pose. The +Z reading is measured and reported beside it as a
        # diagnostic, because it is what shows that the contact is a contact.
        probe = {}
        for label, sign in (("-Z", U03_PROBE_SIGN), ("+Z", -U03_PROBE_SIGN)):
            rim = locked_rim_z + sign * U03_PROBE_MM
            c = clearance(shape, place_g10(g10, G10_LOCK_CLOCK_DEG, rim))
            probe[label] = {"rim_z": round(rim, 6),
                            "clearance": c.measured if c.ok else None, "at": str(c.at),
                            "on_b": str(c.detail.get("on_b")) if c.ok else None,
                            "gated": label == "-Z"}
            if label == "-Z":
                u03.append(gate(f"U-03 (a) od_g10 moved {U03_PROBE_MM:.2f} along -Z", c, "in",
                                U03_PROBE_BAND, band=MM, assumes=_assumes("U-03")))
        detail["g10_probe"] = probe
        detail["g10_locked_lumps"] = lumps(shape, g10_locked)

        # the boolean, reported beside the distance rows and never gated (A-28)
        locked_bool = interference({"housing": shape, "od_g10": g10_locked})["housing|od_g10"]
        boolean_row = gate("U-03 (a) housing|od_g10 boolean", locked_bool, "<=", 0.0, band=MM3,
                           assumes=_assumes("U-03"))
        detail["interference_g10_locked_mm3"] = (locked_bool.measured if locked_bool.ok
                                                 else None)

    # --- U-03(b) and REQ-10 along the lock path
    path_rows, req10, path = [], [], []
    if path_poses and locked_rim_z is None:
        reason = ("the lock path ends at the measured locked pose, which could not be "
                  "measured (spec 1.3 §5 U-03(a))")
        rows += [inconclusive_gate("U-03 (b) lock path", "mm", reason),
                 inconclusive_gate("REQ-10", "mm", reason)]
    elif path_poses:
        poses = lock_path(locked_rim_z, insert_steps, rotate_steps, seat_steps)
        for i, pose in enumerate(poses):
            c = clearance(shape, place_g10(g10, pose["clock_deg"], pose["rim_z"]))
            exempt = pose["remaining"] <= U03_PATH_EXEMPT_MM + 1e-9
            limit = U03_PATH_SEAT if exempt else U03_PATH_CLEAR
            path_rows.append(gate("U-03 (b) lock path", c, ">=", limit, band=MM,
                                  assumes=_assumes("U-03")))
            if pose["leg"] == "insertion":
                req10.append(gate("REQ-10", c, ">=", REQ10_CLEAR, band=MM,
                                  assumes=_assumes("REQ-10")))
            path.append({"pose": i, "leg": pose["leg"], "clock_deg": round(pose["clock_deg"], 3),
                         "rim_z": round(pose["rim_z"], 4),
                         "remaining_mm": round(pose["remaining"], 4), "exempt": exempt,
                         "required": limit,
                         "clearance": c.measured if c.ok else None, "at": str(c.at),
                         "on_b": str(c.detail.get("on_b")) if c.ok else None})
        if pose_count:          # the sweep walks the same path more coarsely and says so
            path_rows.append(gate("U-03 (b) poses", Result("path_poses", len(poses), "count"),
                                  ">=", U03_PATH_MIN_POSES, band=COUNT))
        rows.append(worst("U-03 (b) lock path", path_rows))
        rows.append(worst("REQ-10", req10))
    detail["lock_path"] = path
    detail["rotation_rim_z"] = None if locked_rim_z is None else rotate_rim_z(locked_rim_z)

    hub = clearance(shape, pieces["hub"])
    rows.append(gate("D-07", hub, ">=", D07_HUB_CLEAR, band=MM, assumes=_assumes("D-07")))
    detail["hub_clearance"] = hub.measured if hub.ok else None

    rows = [worst("U-03", u03 + [r for r in rows if r is not None and r.gate.startswith("U-03")])] \
        + u03 + [boolean_row] + rows
    return [r for r in rows if r is not None], detail


# =====================================================================  rows no tool answers
def gates_no_tool() -> list:
    reasons = {
        "D-03a": "no overhang measurement in tools/measure; GATES records the row as "
                 "reviewer, from sections (sections supplied at D6)",
        "D-03b": "no bridge measurement in tools/measure; GATES records the row as "
                 "reviewer, from sections",
        "E-06": "no boss-root measurement in tools/measure; GATES records the row as "
                "reviewer; the fillet radius achieved is in the REPORT",
        "REQ-12": "not a geometric gate: the OD-T01 bench test answers it (spec §5, §7)",
        "D-05a boss OD": "no boss-OD measurement in tools/measure (GATES: reviewer); the "
                         "material around each insert axis is measured and gated above",
    }
    return [inconclusive_gate(k, "mm", v) for k, v in reasons.items()]


# =====================================================================  the run
def _tick(label: str, started: list) -> None:
    import sys as _sys
    import time as _time
    print(f"  [{_time.time() - started[0]:7.1f}s] {label}", file=_sys.stderr, flush=True)


def run(step_path: Path, *, built=None, stl_written=None, assembly: bool = True,
        heavy: bool = True, coarse: bool = False, path_poses: bool = True,
        insert_steps: int = 22, rotate_steps: int = 14, seat_steps: int = 6,
        pose_count: bool = True) -> dict:
    import time as _time
    started = [_time.time()]
    shape = read_step(step_path)
    rows, detail = [], {"step": str(step_path)}
    validity_rows, v = gates_validity(shape)
    rows += validity_rows
    detail["validity"] = {k: (r.measured if r.ok else None) for k, r in v.items()}
    _tick("validity", started)
    env_rows, position = gates_envelope(shape)
    rows += env_rows
    detail["envelope_position"] = position

    _tick("envelope", started)
    census = bore_census(shape)
    census_rows, census_detail = gates_census(shape, census)
    rows += census_rows
    detail["census"] = census_detail
    bore_rows, bore_detail = gates_bores(census)
    rows += bore_rows
    detail["bores"] = bore_detail
    ring_rows, ring_detail = gates_insert_walls(shape)
    rows += ring_rows
    detail["inserts"] = ring_detail

    _tick("census+bores+rings", started)
    profile_rows, profile_detail = gates_profiles(shape, coarse=coarse)
    rows += profile_rows
    detail["profiles"] = profile_detail
    _tick("profiles", started)
    ray_rows, ray_detail = gates_rays(shape)
    rows += ray_rows
    detail["rays"] = ray_detail

    _tick("rays", started)
    if heavy:
        wall_rows, wall_detail = gates_walls(shape)
        rows += wall_rows
        detail["walls"] = wall_detail
    _tick("walls", started)
    if built is not None:
        rt_rows, rt_all = gates_roundtrip(built, step_path)
        rows += rt_rows
        detail["roundtrip"] = [g.row() for g in rt_all]
    if stl_written is not None:
        rows += gates_mesh(stl_written)
    _tick("roundtrip+mesh", started)
    if assembly:
        asm_rows, asm_detail = gates_assembly(shape, path_poses=path_poses,
                                              insert_steps=insert_steps,
                                              rotate_steps=rotate_steps, seat_steps=seat_steps,
                                              pose_count=pose_count)
        rows += asm_rows
        detail["assembly"] = asm_detail
    _tick("assembly", started)
    if heavy:
        rows += gates_no_tool()
        mass = mass_properties(shape, 1070.0)
        detail["mass"] = {k: (r.measured if r.ok else None) for k, r in mass.items()}
    return {"gates": [{**g.row(), "reason": g.reason} for g in rows if g is not None],
            "detail": detail}


def main():
    out = run(STEP)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
