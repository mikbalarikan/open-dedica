"""Checks for od_c15_foot (job 20261001-od-c15-feet, concept C1), written before the build (D3).

Every predicate re-imports the exported STEP files (the foot part file and the check
assembly), measures with tools.measure / tools.core, and compares through
tools.result.gate with the GATES.md §0 band. Thresholds are spec 1.1 §5 values only.
Arithmetic on tool Results (across flats, orientation, centring, chamfer legs, margins)
is done here and wrapped as Results; any input that is INCONCLUSIVE makes the derived
value INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
  python check_od_c15_foot.py --foot <foot.step> --assembly <assembly.step>
         --params <params.json> --out <results.json> [--stl <foot.stl>] [--nut-s 5.5]
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build123d import Box, Location, Pos, Solid                                   # noqa: E402
from OCP.BRepAdaptor import BRepAdaptor_Surface                             # noqa: E402
from OCP.BRepTools import BRepTools                                         # noqa: E402
from OCP.gp import gp_Trsf                                                  # noqa: E402

from tools.core import (compare_step, read_step, solid_count, solids, validity,   # noqa: E402
                        write_stl)
from tools.core.step import labels as step_labels                           # noqa: E402
from tools.measure import (bore_census, clearance, engaged_area, envelope,  # noqa: E402
                           feature_census, flat_ceiling_spans, interference, locate_bore,
                           mass_properties, mesh_census, mesh_deviation, min_wall,
                           overhang_census, radial_extent, radial_profile)
from tools.measure.sampling import kind, outward_normal                     # noqa: E402
from tools.result import INCONCLUSIVE, MEASURED, Result, gate, inconclusive  # noqa: E402

# ---- GATES.md §0 bands ---------------------------------------------------------------
B_MM, B_DEG, B_MM3, B_COUNT = 0.005, 0.001, 0.001, 0

# ---- spec 1.1 values (§2, §4, §5) ------------------------------------------------------
SPEC = {
    "body_d": 18.0, "height": 10.0, "tol": 0.1,
    "top_ch_axial": 0.50, "top_ch_radial": 0.29, "counter_ch": 1.0, "mouth_ch": 0.5,
    "top_annulus_d": 17.42,
    "lid_t": 2.5, "lid_hole_d": 3.4, "lid_hole_min": 3.25,
    "pocket_af": (5.60, 5.65), "flat_rot_deg": 1.0, "centre_max": 0.10,
    "per_side": (0.05, 0.16),
    "bed": (220.0, 220.0, 250.0),
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "j05_wall": 3.0,
    "overhang_deg": 45.0, "bridge_max": 5.0, "d04c_min": 0.5,
    "plate_edge_min": 0.9, "counter_y": -16.00,
    "tip_z": 6.0, "tip_past_nut": 0.5, "tip_above_counter": 2.0,
    "stl_tol": 0.01, "r_max": 9.0,
    "poses": [(110.0, -6.0, 90.0), (-110.0, -6.0, 90.0), (110.0, -6.0, -295.0), (-110.0, -6.0, -295.0)],
    "plate_underside_y": -6.0, "plate_top_y": 0.0,
    "nut_s": 5.5, "nut_m": 2.4, "nut_bore": 3.0,
    "density": 1210.0,
}
FOOT_LABEL = "od_c15_foot"
FLAT_NORMALS = (90.0, 270.0, 30.0, 210.0, 150.0, 330.0)   # flats parallel to X: normals at 90° and ±60°
ROWS: list[dict] = []


# ---- helpers ---------------------------------------------------------------------------
def add(gate_id: str, item: str, result: Result, op: str, limit, band: float, assumes=(), required=None):
    g = gate(gate_id, result, op, limit, band=band, assumes=list(assumes), required=required)
    row = g.row()
    row["item"] = item
    row["reason"] = g.reason
    ROWS.append(row)
    return g


def na(gate_id: str, why: str):
    ROWS.append({"gate": gate_id, "item": "N/A by its row", "measured": None, "unit": "", "required": why,
                 "margin": None, "at": None, "status": "N/A", "method": "-", "assumes": [], "reason": ""})


def derived(name: str, unit: str, inputs: list[Result], fn, at=None, detail=None) -> Result:
    bad = [r for r in inputs if r.status != MEASURED or r.measured is None]
    if bad:
        return inconclusive(name, unit, f"input {bad[0].name} INCONCLUSIVE: {bad[0].reason}")
    try:
        value = fn(*[r.measured for r in inputs])
    except Exception as exc:                                          # noqa: BLE001
        return inconclusive(name, unit, f"{type(exc).__name__}: {exc}")
    return Result(name, value, unit, at=at, detail=detail or {})


def fact(name: str, value, unit: str = "count", at=None, detail=None) -> Result:
    if value is None:
        return inconclusive(name, unit, "not measured")
    return Result(name, value, unit, at=at, detail=detail or {})


def trsf_of_pose(origin) -> Location:
    """Spec §2 joint: foot x -> X, foot y -> +Z, foot z -> -Y, origin at the pose."""
    t = gp_Trsf()
    x, y, z = origin
    t.SetValues(1, 0, 0, x,
                0, 0, -1, y,
                0, 1, 0, z)
    return Location(t)


def face_uv_mid(face):
    u0, u1, v0, v1 = BRepTools.UVBounds_s(face.wrapped)
    return 0.5 * (u0 + u1), 0.5 * (v0 + v1)


def planar_faces(shape):
    """Every plane of the shape: (outward normal, centre, z range, face)."""
    out = []
    for f in shape.faces():
        if kind(f.wrapped) != "plane":
            continue
        u, v = face_uv_mid(f)
        n = outward_normal(f.wrapped, u, v)
        bb = f.bounding_box()
        out.append({"normal": tuple(float(c) for c in n), "centre": tuple(f.center()),
                    "zmin": bb.min.Z, "zmax": bb.max.Z, "face": f})
    return out


def child_by_label(assembly, name):
    for c in assembly.children:
        if c.label == name:
            return c
        found = child_by_label(c, name) if list(getattr(c, "children", ()) or ()) else None
        if found is not None:
            return found
    return None


def single(shape):
    s = solids(shape)
    return Solid(s[0]) if len(s) == 1 else None


# ---- foot part predicates --------------------------------------------------------------
def check_part(foot, foot_step: Path, params_path: Path, stl_path: Path | None):
    E = envelope(foot)
    # exactly_one_solid, U-01
    add("exactly_one_solid", "foot part file", solid_count(foot), "==", 1, B_COUNT)
    v = validity(foot)
    add("U-01", "solid_count", v["solid_count"], "==", 1, B_COUNT)
    add("U-01", "brep_valid", v["brep_valid"], "==", 1, B_COUNT)
    add("U-01", "naked_edges", v["naked_edges"], "==", 0, B_COUNT)

    # U-02 and envelope_within_spec: sizes and position apart
    t = SPEC["tol"]
    for axis, nominal in (("x", SPEC["body_d"]), ("y", SPEC["body_d"]), ("z", SPEC["height"])):
        for gid in ("U-02", "envelope_within_spec"):
            add(gid, f"size_{axis}", E[f"size_{axis}"], "in", (nominal - t, nominal + t), B_MM)
    for axis, nominal in (("x", -SPEC["body_d"] / 2), ("y", -SPEC["body_d"] / 2), ("z", 0.0)):
        for gid in ("U-02", "envelope_within_spec"):
            add(gid, f"position min_{axis}", E[f"min_{axis}"], "in", (nominal - t, nominal + t), B_MM)

    # D-02 bed fit
    for axis, lim in zip("xyz", SPEC["bed"]):
        add("D-02", f"size_{axis} vs bed", E[f"size_{axis}"], "<=", lim, B_MM, assumes=["A-08"])

    # U-04 round trip against the nominal build from the recorded parameters
    import build_od_c15_foot as build_mod
    p = json.loads(Path(params_path).read_text())
    built = build_mod.build_foot(build_mod.Params(**p))
    rt = compare_step(built, foot_step)
    add("U-04", "schema AP242", rt["schema"], "==", 1, B_COUNT)
    add("U-04", "solids (no stray shells)", rt["solids"], "==", 1, B_COUNT)
    add("U-04", "volume_delta", rt["volume_delta"], "<=", 0.0, B_MM3)
    add("U-04", "faces_delta", rt["faces_delta"], "==", 0, B_COUNT)
    add("U-04", "labels unchanged", rt["labels"], "==", 1, B_COUNT)
    add("U-04", "valid_after", rt["valid_after"], "==", 1, B_COUNT)
    add("U-04", f"label reads '{FOOT_LABEL}'",
        fact("step_label_is_part_name", int(step_labels(foot) == [FOOT_LABEL]), "bool",
             detail={"labels": step_labels(foot)}), "==", 1, B_COUNT)

    # U-05 feature census
    fc = feature_census(foot)
    plan = {"plane_faces": 15, "cylinder_faces": 2, "cone_faces": 2, "sphere_faces": 0, "torus_faces": 0,
            "bspline_faces": 0, "other_faces": 0, "concave_cylinders": 1, "convex_cylinders": 1, "bores": 1}
    for k, n in plan.items():
        add("U-05", k, fc[k], "==", n, B_COUNT)
        if k in ("plane_faces", "cylinder_faces", "cone_faces", "bspline_faces"):
            add("feature_census", k, fc[k], "==", n, B_COUNT)
    planes = planar_faces(foot)
    tol_n = 1e-6
    top = [q for q in planes if q["normal"][2] < -1 + tol_n]
    counter = [q for q in planes if q["normal"][2] > 1 - tol_n and abs(q["zmin"] - E["max_z"].measured) < 0.2]
    seat = [q for q in planes if q["normal"][2] > 1 - tol_n and q["zmin"] < 5.0]
    flats = [q for q in planes if abs(q["normal"][2]) < tol_n]
    mouth = [q for q in planes if 0.5 < q["normal"][2] < 0.9 and math.hypot(*q["centre"][:2]) < 5.0]
    for item, group, n in (("top annulus (normal -Z)", top, 1), ("counter annulus (normal +Z)", counter, 1),
                           ("nut seat (normal +Z, z<5)", seat, 1), ("hex flats (vertical planes)", flats, 6),
                           ("mouth chamfer planes (45 deg, inside r 5)", mouth, 6)):
        add("U-05", item, fact("planes_" + item.split()[0], len(group)), "==", n, B_COUNT)
    census = bore_census(foot)
    lb = locate_bore(census, (0.0, 0.0, SPEC["lid_t"] / 2), (0.0, 0.0, 1.0))
    add("U-05", "lid bore located on the Z axis (offset)", lb["offset"], "<=", SPEC["centre_max"], B_MM)

    # bore ends (in z) and seat z
    def bore_z(which):
        r = lb["diameter"]
        if r.status != MEASURED:
            return inconclusive("bore_" + which, "mm", r.reason)
        zs = sorted([r.detail["start"][2], r.detail["end"][2]])
        return Result("lid_bore_" + which + "_z", zs[0] if which == "low" else zs[1], "mm", at=r.detail["start"])
    bore_lo, bore_hi = bore_z("low"), bore_z("high")
    seat_z = fact("seat_plane_z", seat[0]["zmin"] if len(seat) == 1 else None, "mm",
                  at=seat[0]["centre"] if len(seat) == 1 else None)

    # J-06 and U-08 corroboration
    add("J-06", "bores in the part (one plain lid hole)", census, "==", 1, B_COUNT)
    add("J-06", "helical / freeform faces", fc["bspline_faces"], "==", 0, B_COUNT)
    na("U-08", "no threads in this part (the nut takes the thread); bspline faces 0, one plain bore")
    na("D-07", "no reamed fit bores (the nut pocket is REQ-03)")

    # D-04a, REQ-02
    add("D-04a", "lid hole diameter", lb["diameter"], ">=", SPEC["lid_hole_min"], B_MM)
    d = SPEC["lid_hole_d"]
    add("REQ-02", "lid hole diameter", lb["diameter"], "in", (d - t, d + t), B_MM)
    add("REQ-02", "lid hole start z", bore_lo, "in", (-t, t), B_MM)
    add("REQ-02", "lid hole end z (seat)", bore_hi, "in", (SPEC["lid_t"] - t, SPEC["lid_t"] + t), B_MM)
    add("REQ-02", "lid hole through", lb["through"], "==", 1, B_COUNT)
    # coaxial with the outer cylinder: the outer cylinder's own axis from the B-rep
    outer_axis = None
    for f in foot.faces():
        if kind(f.wrapped) == "cylinder":
            cyl = BRepAdaptor_Surface(f.wrapped).Cylinder()
            if cyl.Radius() > 5.0:
                a = cyl.Axis()
                outer_axis = ((a.Location().X(), a.Location().Y(), a.Location().Z()),
                              (a.Direction().X(), a.Direction().Y(), a.Direction().Z()), cyl.Radius())
    if outer_axis is not None:
        coax = locate_bore(census, outer_axis[0], outer_axis[1])
        # offset of the outer axis point from the bore axis line (extended): planar distance
        o = outer_axis[0]
        st = lb["diameter"].detail.get("start") if lb["diameter"].status == MEASURED else None
        off = fact("bore_to_outer_axis_offset", math.hypot(o[0] - st[0], o[1] - st[1]) if st else None, "mm",
                   at=st, detail={"outer_axis": outer_axis, "dir_check": coax["offset"].measured})
    else:
        off = inconclusive("bore_to_outer_axis_offset", "mm", "no outer cylinder found")
    add("REQ-02", "coaxial with the outer cylinder (offset)", off, "<=", SPEC["centre_max"], B_MM, assumes=["A-01"])

    # REQ-01 top face
    add("REQ-01", "planes facing -Z", fact("top_planes", len(top)), "==", 1, B_COUNT)
    if len(top) == 1:
        tf = top[0]
        add("REQ-01", "top plane z", fact("top_plane_z", tf["zmax"], "mm", at=tf["centre"]), "in", (-t, t), B_MM)
        add("REQ-01", "top plane is flat (z range)", fact("top_plane_z_range", tf["zmax"] - tf["zmin"], "mm"),
            "<=", 0.0, B_MM)
    # annulus outer diameter: radial extent of the top face's material at z 0+ (inside the plane by 1e-4)
    r_top = [radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, 1e-4) for a in range(0, 360, 30)]
    r_top_min = derived("top_annulus_outer_d", "mm", r_top,
                        lambda *rs: 2 * (min(rs) - 1e-4 * SPEC["top_ch_radial"] / SPEC["top_ch_axial"]))
    lo_d = SPEC["body_d"] - t - 2 * (SPEC["top_ch_radial"] + t)
    hi_d = SPEC["body_d"] + t - 2 * (SPEC["top_ch_radial"] - t)
    add("REQ-01", "annulus outer diameter (to 17.42; REQ-04 tolerances composed)", r_top_min, "in",
        (lo_d, hi_d), B_MM, required=f"Ø17.42, in [{lo_d:.2f}, {hi_d:.2f}]")
    add("REQ-01", "annulus inner diameter = lid hole", lb["diameter"], "in", (d - t, d + t), B_MM)

    # REQ-04 body: outer diameter, height, chamfers
    rp = radial_profile(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), list(range(0, 360, 10)), (1.5, 8.5),
                        margin=0.0, z_step=0.5, side="outer")
    dmax = derived("outer_d_max", "mm", [rp["max"]], lambda r: 2 * r, at=rp["max"].at)
    dmin = derived("outer_d_min", "mm", [rp["min"]], lambda r: 2 * r, at=rp["min"].at)
    bd = SPEC["body_d"]
    add("REQ-04", "outer diameter (max over 36 angles, z 1.5-8.5)", dmax, "in", (bd - t, bd + t), B_MM, assumes=["A-05"])
    add("REQ-04", "outer diameter (min)", dmin, "in", (bd - t, bd + t), B_MM, assumes=["A-05"])
    h = SPEC["height"]
    add("REQ-04", "height", E["size_z"], "in", (h - t, h + t), B_MM, assumes=["A-04"])
    hm = E["max_z"].measured if E["max_z"].status == MEASURED else h   # probes sit on the measured counter face
    R = rp["min"]

    def chamfer_legs(z1, z2, zface, name, angle=45.0, side="outer", r_ref=None):
        r1 = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), angle, z1, side=side)
        r2 = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), angle, z2, side=side)
        slope = derived(name + "_slope", "mm/mm", [r1, r2], lambda a, b: (b - a) / (z2 - z1))
        r_face = derived(name + "_r_at_face", "mm", [r1, slope], lambda a, s: a + s * (zface - z1))
        radial = derived(name + "_radial_leg", "mm", [r_face, r_ref],
                         lambda rf, rr: abs(rr - rf))
        axial = derived(name + "_axial_leg", "mm", [radial, slope], lambda rl, s: rl / abs(s))
        ang = derived(name + "_angle_from_horizontal", "deg", [slope], lambda s: math.degrees(math.atan(1 / abs(s))))
        return radial, axial, ang

    top_rad, top_ax, top_ang = chamfer_legs(0.1, 0.4, 0.0, "top_chamfer", r_ref=R)
    add("REQ-04", "top chamfer axial leg", top_ax, "in", (SPEC["top_ch_axial"] - t, SPEC["top_ch_axial"] + t), B_MM)
    add("REQ-04", "top chamfer radial leg", top_rad, "in", (SPEC["top_ch_radial"] - t, SPEC["top_ch_radial"] + t), B_MM)
    c = SPEC["counter_ch"]
    cr, ca, cang = chamfer_legs(hm - 0.8, hm - 0.2, hm, "counter_chamfer", r_ref=R)
    add("REQ-04", "counter chamfer axial leg", ca, "in", (c - t, c + t), B_MM)
    add("REQ-04", "counter chamfer radial leg", cr, "in", (c - t, c + t), B_MM)

    # REQ-03 nut pocket: across flats, orientation, centring, seat, mouth chamfer
    zmid = 6.0
    rin = {a: radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, zmid, side="inner") for a in FLAT_NORMALS}
    for a, b in ((90.0, 270.0), (30.0, 210.0), (150.0, 330.0)):
        af = derived(f"across_flats_{int(a)}", "mm", [rin[a], rin[b]], lambda x, y: x + y)
        add("REQ-03", f"across flats, normals {int(a)}/{int(b)} deg", af, "in", SPEC["pocket_af"], B_MM, assumes=["A-06"])
    r80 = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), 80.0, zmid, side="inner")
    r100 = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), 100.0, zmid, side="inner")
    r260 = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), 260.0, zmid, side="inner")
    r280 = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), 280.0, zmid, side="inner")
    k10 = math.cos(math.radians(10)) / math.sin(math.radians(10))
    rot = derived("flat_rotation_from_X", "deg", [r80, r100, r260, r280],
                  lambda a, b, c_, d_: 0.5 * (math.degrees(math.atan((a - b) / (a + b) * k10))
                                              + math.degrees(math.atan((c_ - d_) / (c_ + d_) * k10))))
    rot_abs = derived("flat_rotation_abs", "deg", [rot], abs)
    add("REQ-03", "flats parallel to X (|rotation|)", rot_abs, "<=", SPEC["flat_rot_deg"], B_DEG)

    def centre(*rs):
        # least squares of the centre from three opposite pairs: shift along n = (r_a - r_b) / 2
        import numpy as np
        rows, rhs = [], []
        for (a, b), (ra, rb) in zip(((90, 270), (30, 210), (150, 330)), ((rs[0], rs[1]), (rs[2], rs[3]), (rs[4], rs[5]))):
            n = (math.cos(math.radians(a)), math.sin(math.radians(a)))
            rows.append(n)
            rhs.append(-(ra - rb) / 2)
        sol = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)[0]
        return float(math.hypot(*sol))
    cen = derived("pocket_centre_offset", "mm", [rin[a] for a in FLAT_NORMALS], centre)
    add("REQ-03", "pocket centred on the axis", cen, "<=", SPEC["centre_max"], B_MM)
    add("REQ-03", "seat z (plane)", seat_z, "in", (SPEC["lid_t"] - t, SPEC["lid_t"] + t), B_MM)
    add("REQ-03", "seat z (lid bore end)", bore_hi, "in", (SPEC["lid_t"] - t, SPEC["lid_t"] + t), B_MM)
    open_mouth = radial_extent(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), 90.0, hm - 1e-3, side="inner")
    add("REQ-03", "pocket open at the counter face (void on the axis at z 9.999; inner radius > 0)",
        open_mouth, ">=", 2.8, B_MM, required="material only outside the pocket at z 9.999 (r >= 2.8)")
    m_rad, m_ax, m_ang = chamfer_legs(hm - 0.4, hm - 0.1, hm, "mouth_chamfer", angle=90.0, side="inner",
                                      r_ref=rin[90.0])
    mc = SPEC["mouth_ch"]
    add("REQ-03", "entry chamfer axial leg", m_ax, "in", (mc - t, mc + t), B_MM)
    add("REQ-03", "entry chamfer radial leg (on a flat)", m_rad, "in", (mc - t, mc + t), B_MM)

    # walls: D-01a, D-01b, D-06a, U-06 on the whole foot; J-05 on the ring above the seat
    mw = min_wall(foot)
    add("D-01a", "min_wall whole foot", mw, ">=", SPEC["wall_floor"], B_MM)
    add("D-01b", "min_wall whole foot", mw, ">=", SPEC["wall_struct"], B_MM, assumes=["A-03"])
    add("D-06a", "min_wall whole foot", mw, ">=", SPEC["min_feature"], B_MM)
    wide = mw.detail.get("wide") if mw.status == MEASURED else None
    wide_r = (Result("min_wall_wide", wide["measured"], "mm", at=wide["at"]) if wide
              else inconclusive("min_wall_wide", "mm", mw.reason or "no wide reading"))
    add("U-06", "min_wall wide (45 deg) [Soft]", wide_r, ">=", SPEC["wall_struct"], B_MM)
    sz = seat_z.measured if seat_z.status == MEASURED else SPEC["lid_t"]
    ring = foot & Pos(0, 0, sz + 10.0) * Box(40, 40, 20)
    ring_s = single(ring)
    j05 = min_wall(ring_s) if ring_s is not None else inconclusive("min_wall", "mm", "ring cut is not one solid")
    add("J-05", f"min_wall ring z {sz:.3f}-10 around the pocket", j05, ">=", SPEC["j05_wall"], B_MM)
    # corroboration from the plan: radial material at the six hex corners over z seat ... height,
    # through the mouth and counter chamfers (where min_wall's opposed-normal rule does not pair faces)
    corners = [0.0, 60.0, 120.0, 180.0, 240.0, 300.0]
    pin = radial_profile(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), corners, (sz, hm), margin=0.0, z_step=0.05, side="inner")
    pout = radial_profile(foot, (0, 0, 0), (0, 0, 1), (1, 0, 0), corners, (sz, hm), margin=0.0, z_step=0.05, side="outer")

    def radial_wall(*_):
        inner = {(q["angle_deg"], q["z"]): q["radius"] for q in pin["max"].detail["points"]}
        outer = {(q["angle_deg"], q["z"]): q["low"] for q in pout["max"].detail["points"]}
        return min(outer[k] - inner[k] for k in inner if k in outer)
    rw = derived("radial_wall_at_corners", "mm", [pin["max"], pout["max"]], radial_wall)
    add("J-05", f"radial material at the 6 hex corners, z {sz:.3f}-10 (corroboration)", rw, ">=", SPEC["j05_wall"], B_MM)

    # D-03a, D-03b
    oc = overhang_census(foot, (0, 0, 1), min_deg=SPEC["overhang_deg"])
    add("D-03a", "least overhang angle from horizontal", oc, ">=", SPEC["overhang_deg"], B_DEG)
    fs = flat_ceiling_spans(foot, (0, 0, 1), max_span=SPEC["bridge_max"])
    add("D-03b", "widest bridge", fs, "<=", SPEC["bridge_max"], B_MM)

    # U-07 export mesh
    amax = 4 * math.acos(1 - SPEC["stl_tol"] / SPEC["r_max"])
    meta = json.loads(Path(params_path).with_name(Path(params_path).name.replace("params", "stlmeta")).read_text()) \
        if Path(params_path).with_name(Path(params_path).name.replace("params", "stlmeta")).exists() else None
    tol_used = meta["tolerance_mm"] if meta else SPEC["stl_tol"]
    ang_used = meta["angular_tolerance_rad"] if meta else 0.18
    add("U-07", "STL tolerance", fact("stl_tolerance", tol_used, "mm"), "<=", SPEC["stl_tol"], B_MM)
    add("U-07", "STL angular tolerance (rad, limit 4 acos(1-0.01/9))", fact("stl_angular", ang_used, "rad"),
        "<=", amax, 0.00002)
    with tempfile.TemporaryDirectory() as tmp:
        w = write_stl(read_step(foot_step), Path(tmp) / "remesh.stl", tolerance=tol_used, angular_tolerance=ang_used)
        add("U-07", "stl_max_sagitta (re-imported STEP meshed at the same settings)", w.checks["max_sagitta"],
            "<=", SPEC["stl_tol"], B_MM)
        remesh_tris = w.detail.get("triangles")
    if stl_path is not None and Path(stl_path).exists():
        mc_ = mesh_census(stl_path)
        add("U-07", "delivered STL bodies", mc_["bodies"] if isinstance(mc_, dict) else mc_, "==", 1, B_COUNT)
        if isinstance(mc_, dict):
            add("U-07", "delivered STL naked edges", mc_["naked_edges"], "==", 0, B_COUNT)
            add("U-07", "delivered STL triangles = re-mesh triangles",
                fact("stl_triangles_match", int(mc_["triangles"].measured == remesh_tris), "bool",
                     detail={"stl": mc_["triangles"].measured, "remesh": remesh_tris}), "==", 1, B_COUNT)
        dev = mesh_deviation(stl_path, foot)
        add("U-07", "delivered STL deviation from the B-rep, both ways (corroboration, D-025)", dev, "<=",
            SPEC["stl_tol"] + 0.001, B_MM, required="<= 0.01 + reference tolerance 0.001")

    mp = mass_properties(foot, SPEC["density"])
    return {"seat_z": sz, "lid_bore": lb, "mass": mp, "envelope": E}


# ---- assembly predicates ----------------------------------------------------------------
def nut_envelope(s: float, m: float, bore: float, top_z: float):
    """U-03 nut envelope in the foot frame: hexagon across flats s, flats parallel to X, height m,
    Ø bore through; top face at foot z top_z, extending to top_z + m (toward the counter face)."""
    from build123d import Cylinder, RegularPolygon, extrude, Plane, Align
    hexa = extrude(Plane.XY.offset(top_z) * RegularPolygon(radius=s / 2, side_count=6, major_radius=False), amount=m)
    hole = Pos(0, 0, top_z - 1) * Cylinder(bore / 2, m + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return hexa - hole


def check_assembly(asm, foot_part, part_info, nut_s: float):
    names = ["plate"] + [f"{p}_{i}" for p in ("foot", "screw", "nut") for i in range(1, 5)]
    parts = {n: child_by_label(asm, n) for n in names}
    missing = [n for n, s in parts.items() if s is None]
    add("exactly_one_solid", "assembly parts found by label",
        fact("assembly_parts_missing", len(missing), detail={"missing": missing}), "==", 0, B_COUNT)
    for n, s in parts.items():
        if s is not None:
            add("exactly_one_solid", f"assembly {n}", solid_count(s), "==", 1, B_COUNT)
    if missing:
        return
    plate = parts["plate"]
    pcensus = bore_census(plate)
    PE = envelope(plate)
    t = SPEC["tol"]
    foot_vol = mass_properties(foot_part, SPEC["density"])["volume"]
    seat = part_info["seat_z"]
    feet_axes = []
    for i, pose in enumerate(SPEC["poses"], start=1):
        foot, screw, nut = parts[f"foot_{i}"], parts[f"screw_{i}"], parts[f"nut_{i}"]
        T = trsf_of_pose(pose)
        Tinv = T.inverse()
        # joint pose: the placed foot is the part file under the spec §2 joint (common volume = whole volume)
        expect = foot_part.moved(T)
        cv = interference({"placed": foot, "expected": expect})["placed|expected"]
        pose_dev = derived("pose_volume_shortfall", "mm3", [foot_vol, cv], lambda a, b: abs(a - b))
        add("U-03", f"(a) pose {i}: foot placed by the spec joint (volume not shared with the expected pose)",
            pose_dev, "<=", 0.0, B_MM3, assumes=["A-01"])
        # measured plate hole for this pose
        hole = locate_bore(pcensus, (pose[0], -3.0, pose[2]), (0, 1, 0))
        add("REQ-02", f"(assembly) pose {i}: plate hole axis offset from the spec pose (foot coaxial with its hole)",
            hole["offset"], "<=", SPEC["centre_max"], B_MM, assumes=["A-01"])
        # designed contacts
        for item, a, b, push in ((f"foot_{i} top face on plate underside", foot, plate, (0, 1, 0)),
                                 (f"nut_{i} top face on foot_{i} seat", nut, foot, (0, 1, 0)),
                                 (f"screw_{i} head on plate top", screw, plate, (0, -1, 0))):
            add("U-03", f"(a) pose {i}: contact {item} (clearance)", clearance(a, b), "==", 0.0, B_MM,
                assumes=["A-01", "A-02"])
            ea = engaged_area(a, b, push, 0.01)
            ROWS.append({"gate": "U-03", "item": f"(a) pose {i}: engaged area {item} [corroboration, not gated]",
                         "measured": ea.measured, "unit": "mm2", "required": "-", "margin": None,
                         "at": str(ea.at), "status": "INFO" if ea.ok else "INFO_INCONCLUSIVE", "method": "engaged_area",
                         "assumes": [], "reason": ea.reason})
        inter = interference({"foot": foot, "plate": plate, "nut": nut, "screw": screw})
        for pair in ("foot|plate", "foot|nut", "foot|screw", "plate|nut", "plate|screw"):
            add("U-03", f"(a) pose {i}: interference {pair}", inter[pair], "<=", 0.0, B_MM3, assumes=["A-01", "A-02"])

        # (b) assembly path: the nut slid from the mouth to the seat along the measured pocket axis
        fb = locate_bore(bore_census(foot), (pose[0], pose[1] - SPEC["lid_t"] / 2, pose[2]), (0, 1, 0))
        feet_axes.append(fb)
        hm = part_info["envelope"]["max_z"].measured          # the measured counter face (the mouth)
        tops = [hm, hm - SPEC["nut_m"], 6.75, 5.9, 5.05, 4.2, 3.35, seat]
        vols = []
        for zt in tops:
            local = nut_envelope(nut_s, SPEC["nut_m"], SPEC["nut_bore"], zt)
            vols.append(common_after(local.moved(T), foot))
        bad_v = [v_ for v_ in vols if v_.status != MEASURED]
        worst = bad_v[0] if bad_v else max(vols, key=lambda v_: v_.measured)
        worst = Result(worst.name, worst.measured, worst.unit, at=worst.at, status=worst.status, reason=worst.reason,
                       detail={"poses_top_z": tops, "volumes": [v_.measured for v_ in vols]}) if not bad_v else worst
        add("U-03", f"(b) pose {i}: nut slide mouth -> seat, 8 poses (worst interference)", worst, "<=", 0.0,
            B_MM3, assumes=["A-02"])

        # straight edges and corner arc (REQ-05)
        FE = envelope(foot)
        if pose[0] > 0:
            ex = derived("edge_x", "mm", [PE["max_x"], FE["max_x"]], lambda a, b: a - b)
        else:
            ex = derived("edge_x", "mm", [FE["min_x"], PE["min_x"]], lambda a, b: a - b)
        if pose[2] > 0:
            ez = derived("edge_z", "mm", [PE["max_z"], FE["max_z"]], lambda a, b: a - b)
        else:
            ez = derived("edge_z", "mm", [FE["min_z"], PE["min_z"]], lambda a, b: a - b)
        add("REQ-05", f"pose {i}: foot to plate X edge", ex, ">=", SPEC["plate_edge_min"], B_MM, assumes=["A-01"])
        add("REQ-05", f"pose {i}: foot to plate Z edge", ez, ">=", SPEC["plate_edge_min"], B_MM, assumes=["A-01"])
        if hole["offset"].status == MEASURED:
            st = hole["offset"].detail["start"]
            origin = (st[0], SPEC["plate_underside_y"], st[2])
            sx, sz_ = (1 if pose[0] > 0 else -1), (1 if pose[2] > 0 else -1)
            # angles about +Y from ref +X: direction (cos a, 0, -sin a)
            angs = [a for a in range(0, 360, 5)
                    if math.cos(math.radians(a)) * sx >= -1e-9 and -math.sin(math.radians(a)) * sz_ >= -1e-9]
            pr = radial_profile(plate, origin, (0, 1, 0), (1, 0, 0), angs, (0.5, 5.5), margin=0.4, z_step=1.0)
            fr = radial_profile(foot, origin, (0, 1, 0), (1, 0, 0), angs, (-9.5, -0.5), margin=0.4, z_step=1.0)

            def arc_margin(*_):
                pts_p = {}
                for q in pr["min"].detail["points"]:
                    pts_p[q["angle_deg"]] = min(pts_p.get(q["angle_deg"], 1e9), q["low"])
                pts_f = {}
                for q in fr["max"].detail["points"]:
                    pts_f[q["angle_deg"]] = max(pts_f.get(q["angle_deg"], -1e9), q["radius"])
                return min(pts_p[a] - pts_f[a] for a in pts_p if a in pts_f)
            arc = derived("corner_arc_margin", "mm", [pr["min"], fr["max"]], arc_margin)
            add("REQ-05", f"pose {i}: foot to plate corner arc (R plate - R foot, outward quadrant)", arc, ">=",
                SPEC["plate_edge_min"], B_MM, assumes=["A-01"])
        # REQ-06 counter face level
        cy = SPEC["counter_y"]
        add("REQ-06", f"pose {i}: counter face y", FE["min_y"], "in", (cy - t, cy + t), B_MM, assumes=["A-01", "A-04"])

        # foot-frame quantities (REQ-07, D-04c, REQ-03 per-side)
        screw_l = screw.moved(Tinv)
        nut_l = nut.moved(Tinv)
        SE, NE = envelope(screw_l), envelope(nut_l)
        cz = SPEC["tip_z"]
        add("REQ-07", f"pose {i}: screw tip z in the foot frame", SE["max_z"], "in", (cz - t, cz + t), B_MM, assumes=["A-02"])
        add("REQ-07", f"pose {i}: tip past the nut's lower face", derived("tip_past_nut", "mm", [SE["max_z"], NE["max_z"]],
            lambda a, b: a - b), ">=", SPEC["tip_past_nut"], B_MM, assumes=["A-02"])
        add("REQ-07", f"pose {i}: tip above the counter face", derived("tip_above_counter", "mm",
            [part_info["envelope"]["max_z"], SE["max_z"]], lambda a, b: a - b), ">=", SPEC["tip_above_counter"],
            B_MM, assumes=["A-02"])
        ring = single(foot_part & Pos(0, 0, seat + 10.0) * Box(40, 40, 20))
        shank = single(screw_l & Pos(0, 0, seat + 10.0) * Box(40, 40, 20))
        dc = clearance(ring, shank) if ring is not None and shank is not None else \
            inconclusive("clearance", "mm", "region cut is not one solid")
        add("D-04c", f"pose {i}: foot above the seat to the screw shank below the seat", dc, ">=", SPEC["d04c_min"],
            B_MM, assumes=["A-02"])
        zn = seat + SPEC["nut_m"] / 2
        for a in FLAT_NORMALS:
            rf = radial_extent(foot_part, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, zn, side="inner")
            rn = radial_extent(nut_l, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, zn, side="outer")
            ps = derived("nut_to_flat", "mm", [rf, rn], lambda x, y: x - y)
            add("REQ-03", f"pose {i}: nut envelope to flat at {int(a)} deg (per side)", ps, "in", SPEC["per_side"],
                B_MM, assumes=["A-06"])
        cl_flats = clearance(single(foot_part & Pos(0, 0, seat + 0.1 + 10.0) * Box(40, 40, 20)), nut_l)
        add("REQ-03", f"pose {i}: nut envelope to the pocket walls (least, above the seat)", cl_flats, "in",
            SPEC["per_side"], B_MM, assumes=["A-06"])

    # REQ-06 centre of mass inside the four feet
    com = mass_properties(plate, 7850.0)   # density irrelevant to the centre; a uniform plate
    xs = [fa["offset"].detail["start"][0] for fa in feet_axes if fa["offset"].status == MEASURED]
    zs = [fa["offset"].detail["start"][2] for fa in feet_axes if fa["offset"].status == MEASURED]
    if len(xs) == 4:
        m = derived("com_inside_feet_margin", "mm", [com["com_x"], com["com_z"]],
                    lambda x, z: min(x - min(xs), max(xs) - x, z - min(zs), max(zs) - z),
                    detail={"feet_x": xs, "feet_z": zs})
    else:
        m = inconclusive("com_inside_feet_margin", "mm", "a foot axis was not measured")
    add("REQ-06", "plate centre of mass inside the four foot axes (least margin)", m, ">=", 0.0, B_MM,
        assumes=["A-01", "A-04"])


def common_after(a, b) -> Result:
    r = interference({"nut": a, "foot": b})["nut|foot"]
    return r


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--foot", required=True)
    ap.add_argument("--assembly", required=True)
    ap.add_argument("--params", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--stl")
    ap.add_argument("--nut-s", type=float, default=SPEC["nut_s"])
    ap.add_argument("--part-only", action="store_true")
    args = ap.parse_args(argv)
    ROWS.clear()
    foot_raw = read_step(args.foot)
    foot = single(foot_raw)
    if foot is None:
        add("exactly_one_solid", "foot part file", solid_count(foot_raw), "==", 1, B_COUNT)
    else:
        foot.label = getattr(foot_raw, "label", "")
        info = check_part(foot_raw if solid_count(foot_raw).measured == 1 else foot, Path(args.foot), Path(args.params),
                          Path(args.stl) if args.stl else None)
        if not args.part_only:
            asm = read_step(args.assembly)
            check_assembly(asm, foot, info, args.nut_s)
    out = {"foot": args.foot, "assembly": args.assembly, "nut_s": args.nut_s, "rows": ROWS}
    Path(args.out).write_text(json.dumps(out, indent=1, default=str))
    worst = {}
    order = {"FAIL": 3, "INCONCLUSIVE": 2, "PASS_ASSUMED": 1, "PASS": 0, "N/A": -1}
    for r in ROWS:
        if r["status"] in order:
            g = r["gate"]
            if g not in worst or order[r["status"]] > order[worst[g]["status"]] or (
                    order[r["status"]] == order[worst[g]["status"]] and r["margin"] is not None
                    and worst[g]["margin"] is not None and r["margin"] < worst[g]["margin"]):
                worst[g] = r
    for g, r in worst.items():
        print(f"{g:22s} {r['status']:13s} {r['measured']!s:>24} {r['unit']:5s} margin {r['margin']!s:>24}  [{r['item']}]")
    bad = [r for r in ROWS if r["status"] in ("FAIL", "INCONCLUSIVE")]
    for r in bad:
        print("  !!", r["gate"], r["item"], r["status"], r["measured"], r["reason"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
