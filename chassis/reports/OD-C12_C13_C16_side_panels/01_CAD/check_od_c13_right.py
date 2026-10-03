"""Checks for OD-C13 (right panel), written before build_od_c13_right.py (D3).

One predicate per spec 1.1 section 5 row that applies to a panel, plus exactly_one_solid,
feature_census and envelope_within_spec. Every number is read from the re-imported STEP.
`check_panel(side=...)` is shared with check_od_c12_left.py (side -1).

Run: check_od_c13_right.py [--step S] [--stl L] [--params JSON] [--json OUT]
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import tempfile
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np  # noqa: E402
from build123d import Axis, Vector, extrude  # noqa: E402

from checklib_od_side_panels import (BAND_DEG, BAND_MM, BAND_MM3, BAND_N, CAD, INP, OUT, Rows,  # noqa: E402
                                     box, common_part, face_box, gate_census, gate_envelope,
                                     gate_roundtrip, gate_validity, gate_walls, nearest_bore,
                                     planar_faces, run_guarded, stl_rows, val, bores_along)
from params_od_side_panels import P  # noqa: E402
from tools.core import common_volume, read_step, write_stl  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, flat_ceiling_spans, locate_bore,  # noqa: E402
                           mesh_census, overhang_census, radial_extent)
from tools.result import Result  # noqa: E402

# ---- spec 1.1 section 5 values used by the panel predicates (copied with their row ids) ----
SPEC = {
    "size": (10.0, 218.81, 385.0),                       # U-02
    "pos_x": {1: (110.0, 120.0), -1: (-120.0, -110.0)},   # U-02
    "pos_y": (0.0, 218.81), "pos_z": (-295.0, 90.0),     # U-02
    "outer_x": 120.0, "inner_x": 117.0, "face_tol": 0.10,  # REQ-01
    "under_y": 0.0, "top_y": 215.0, "y_tol": 0.05,       # REQ-01
    "top_x": (116.6, 120.0),                             # REQ-01 (116.6 +- 0.1 from REQ-02's vertex tolerance)
    "end_z": (-295.0, 90.0), "end_tol": 0.10,            # REQ-01
    "lip_tri": ((110.0, 215.0), (116.6, 215.0), (110.0, 218.81)), "lip_tol": 0.1,  # REQ-02
    "lip_slope_deg": 60.0, "lip_slope_tol": 1.0,          # REQ-02
    "lip_z": (-280.0, 80.0),                             # REQ-02
    "lip_gap": 0.40, "lip_gap_tol": 0.05,                # REQ-02 / U-03 (a)
    "lip_gap_min": 0.30,                                 # D-04d
    "hole_d": 3.4, "hole_d_tol": 0.1, "hole_y": 10.0, "hole_z": (-262.0, -15.0, 62.0),  # REQ-03
    "hole_offset": 0.10,                                 # REQ-03
    "clear_hole_min": 3.25,                              # D-04a
    "overhang_min": 45.0,                                # D-03a
    "bridge_max": 5.0,                                   # D-03b
    "bed": (420.0, 420.0, 500.0),                        # D-02 via A-09
    "lid_free_x": (109.5, 117.0),                        # brief Q1: nothing of the lid in x +-(109.5 .. 117) in the lip's zone
    "stl_tol": 0.01,                                     # U-07
}
CENSUS_RIGHT = {"plane_faces": 11, "cylinder_faces": 3, "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0,
                "bspline_faces": 0, "other_faces": 0, "concave_cylinders": 3, "convex_cylinders": 0, "bores": 3}
WALL_SPACING = 1.0      # mm: a 385 x 215 face at 0.4 exceeds the sampler's 250 000 samples per face
PRINT_SPACING = 1.0     # mm: the same for overhang_census / flat_ceiling_spans


def lid():
    return read_step(INP / "OD-C10_top_panel.step")


def plate():
    return read_step(INP / "OD-C01_base_frame.step")


def check_panel(side: int, params, step: Path, stl: Path | None, built, census_plan: dict, rows: Rows):
    s = side
    sh = read_step(step)
    v = gate_validity(rows, sh)
    solid = sh.solids()[0] if sh.solids() else sh

    # U-02 / envelope_within_spec / D-02
    e = run_guarded(rows, "U-02", "mm", gate_envelope, rows, sh, SPEC["size"],
                    (SPEC["pos_x"][s], SPEC["pos_y"], SPEC["pos_z"]))
    if e:
        bed = SPEC["bed"]
        rows.add("D-02 bed length (z)", e["size_z"], "<=", bed[0], BAND_MM, assumes=("A-09",),
                 note="lying on its outer face: 385 x 218.81 on the bed")
        rows.add("D-02 bed width (y)", e["size_y"], "<=", bed[1], BAND_MM, assumes=("A-09",))
        rows.add("D-02 height (x)", e["size_x"], "<=", bed[2], BAND_MM, assumes=("A-09",))

    # U-04
    run_guarded(rows, "U-04", "-", gate_roundtrip, rows, built, step)

    # U-05 / feature_census
    run_guarded(rows, "U-05", "count", gate_census, rows, sh, census_plan)
    bc = bore_census(sh)
    xb = bores_along(bc, (1, 0, 0)) if bc.ok else []
    rows.add("U-05 bores along X", val("bores_along_x", len(xb), "count"), "==", 3, BAND_N)

    # walls: D-01a, D-01b, D-06a, U-06
    run_guarded(rows, "D-01b", "mm", gate_walls, rows, sh, WALL_SPACING)

    # D-03a overhang, D-03b bridges, REQ-02 slope (the census reads it)
    bd = (-s, 0, 0)
    oh = overhang_census(sh, build_dir=bd, spacing=PRINT_SPACING)
    rows.add("D-03a", oh, ">=", SPEC["overhang_min"], BAND_DEG,
             note=f"build_dir {bd}; per kind {oh.detail.get('per_kind_least_deg') if oh.ok else oh.reason}")
    rows.add("REQ-02 slope (overhang_census)", oh, "in",
             (SPEC["lip_slope_deg"] - SPEC["lip_slope_tol"], SPEC["lip_slope_deg"] + SPEC["lip_slope_tol"]), BAND_DEG,
             note="the lip's sloped face is the only downward face")
    fc = flat_ceiling_spans(sh, build_dir=bd, max_span=SPEC["bridge_max"], spacing=PRINT_SPACING)
    rows.add("D-03b (corroboration; reviewer from sections)", fc, "<=", SPEC["bridge_max"], BAND_MM)

    # REQ-03 / D-04a holes
    for z in SPEC["hole_z"]:
        lb = locate_bore(bc, (s * 118.5, SPEC["hole_y"], z), (1, 0, 0))
        rows.add(f"REQ-03 hole z{z:+.0f} diameter", lb["diameter"], "in",
                 (SPEC["hole_d"] - SPEC["hole_d_tol"], SPEC["hole_d"] + SPEC["hole_d_tol"]), BAND_MM)
        rows.add(f"REQ-03 hole z{z:+.0f} offset", lb["offset"], "<=", SPEC["hole_offset"], BAND_MM)
        rows.add(f"REQ-03 hole z{z:+.0f} through", lb["through"], "==", 1, BAND_N)
        rows.add(f"D-04a hole z{z:+.0f}", lb["diameter"], ">=", SPEC["clear_hole_min"], BAND_MM)

    # REQ-01 faces
    def req01():
        tol = SPEC["face_tol"]
        outer = [f for f in planar_faces(solid, (s, 0, 0)) if abs(face_box(f)[0] - s * SPEC["outer_x"]) < 1.0]
        rows.add("REQ-01 outer face count", val("outer_faces", len(outer), "count"), "==", 1, BAND_N)
        if outer:
            b = face_box(outer[0])
            rows.add("REQ-01 outer face x", val("outer_x", b[0], "mm"), "in",
                     (s * SPEC["outer_x"] - tol, s * SPEC["outer_x"] + tol), BAND_MM)
            rows.add("REQ-01 outer face z min", val("outer_z0", b[4], "mm"), "in",
                     (SPEC["end_z"][0] - tol, SPEC["end_z"][0] + tol), BAND_MM)
            rows.add("REQ-01 outer face z max", val("outer_z1", b[5], "mm"), "in",
                     (SPEC["end_z"][1] - tol, SPEC["end_z"][1] + tol), BAND_MM)
        # sections at y 50 and y 200: material along X read by radial_extent from the machine axis
        zs = [-294.0, -200.0, -100.0, -60.0, 0.0, 50.0, 89.0]
        for y in (50.0, 200.0):
            for z in zs:
                if s < 0 and y <= 55.0 and -160.0 <= z <= -29.0:
                    continue  # OD-C12's relief, REQ-04
                o = radial_extent(solid, (0, y, 0), (0, 0, 1), (s, 0, 0), 0.0, z, side="outer", r_min=100.0)
                i = radial_extent(solid, (0, y, 0), (0, 0, 1), (s, 0, 0), 0.0, z, side="inner", r_min=100.0)
                rows.add(f"REQ-01 section y{y:.0f} z{z:+.0f} outer", o, "in",
                         (SPEC["outer_x"] - tol, SPEC["outer_x"] + tol), BAND_MM)
                rows.add(f"REQ-01 section y{y:.0f} z{z:+.0f} inner", i, "in",
                         (SPEC["inner_x"] - tol, SPEC["inner_x"] + tol), BAND_MM)
        under = [f for f in planar_faces(solid, (0, -1, 0)) if face_box(f)[2] < 1.0]
        rows.add("REQ-01 underside planes", val("underside_faces", len(under), "count"), "==", 1, BAND_N)
        for f in under:
            b = face_box(f)
            rows.add("REQ-01 underside y", val("underside_y", b[2], "mm"), "in",
                     (SPEC["under_y"] - SPEC["y_tol"], SPEC["under_y"] + SPEC["y_tol"]), BAND_MM)
        top = [f for f in planar_faces(solid, (0, 1, 0)) if abs(face_box(f)[2] - SPEC["top_y"]) < 1.0]
        rows.add("REQ-01 top face count", val("top_faces", len(top), "count"), "==", 1, BAND_N)
        for f in top:
            b = face_box(f)
            rows.add("REQ-01 top face y", val("top_y", b[2], "mm"), "in",
                     (SPEC["top_y"] - SPEC["y_tol"], SPEC["top_y"] + SPEC["y_tol"]), BAND_MM)
            xi, xo = (b[0], b[1]) if s > 0 else (-b[1], -b[0])
            rows.add("REQ-01 top face inner x", val("top_x_inner", xi, "mm"), "in",
                     (SPEC["top_x"][0] - 0.1, SPEC["top_x"][0] + 0.1), BAND_MM)
            rows.add("REQ-01 top face outer x", val("top_x_outer", xo, "mm"), "in",
                     (SPEC["top_x"][1] - 0.1, SPEC["top_x"][1] + 0.1), BAND_MM)
        for nz, zt, name in ((-1, SPEC["end_z"][0], "rear"), (1, SPEC["end_z"][1], "front")):
            ends = [f for f in planar_faces(solid, (0, 0, nz)) if abs(face_box(f)[4] - zt) < 1.0]
            rows.add(f"REQ-01 {name} end face count", val("end_faces", len(ends), "count"), "==", 1, BAND_N)
            for f in ends:
                b = face_box(f)
                rows.add(f"REQ-01 {name} end z", val("end_z", b[4], "mm"), "in",
                         (zt - SPEC["end_tol"], zt + SPEC["end_tol"]), BAND_MM)
                square = abs(f.area - (b[1] - b[0]) * (b[3] - b[2])) < 1e-3
                rows.add(f"REQ-01 {name} end square (rectangle 1/0)", val("end_square", int(square), "bool",
                         area=f.area, box=b), "==", 1, BAND_N)
        # no arc faces on the panels (1.1 Q2): no convex cylinder
        # footprint wholly over the plate: the underside extruded 6.0 down lies inside OD-C01
        c01 = plate()
        foot = extrude(under[0], amount=6.0, dir=(0, -1, 0))
        cv = common_volume(foot, c01)
        outside = val("footprint_outside_plate", foot.volume - cv.measured, "mm3",
                      footprint_mm3=foot.volume, common_mm3=cv.measured) if cv.ok else cv
        rows.add("REQ-01 footprint outside plate", outside, "<=", 0.0, BAND_MM3)
    run_guarded(rows, "REQ-01", "mm", req01)

    # REQ-02 lip wedge, D-04d, U-03 (a) lip gap
    def req02():
        n = (s * 0.5, math.sqrt(3) / 2, 0.0)  # expected outward normal of a 60 degree slope
        slopes = [f for f in solid.faces() if f.geom_type.name == "PLANE"
                  and f.normal_at().get_angle(Vector(*n)) < 5.0]
        rows.add("REQ-02 sloped faces", val("sloped_faces", len(slopes), "count"), "==", 1, BAND_N)
        if not slopes:
            return
        f = slopes[0]
        nn = f.normal_at()
        ang = math.degrees(math.acos(abs(nn.X)))
        rows.add("REQ-02 slope from panel plane", val("lip_slope", ang, "deg", normal=tuple(nn)), "in",
                 (SPEC["lip_slope_deg"] - SPEC["lip_slope_tol"], SPEC["lip_slope_deg"] + SPEC["lip_slope_tol"]), BAND_DEG)
        # the lip region: panel above y 215 (the wedge); its section vertices from its faces
        lip = common_part(solid, box(s * 100.0, s * 125.0, SPEC["top_y"], 230.0, -300.0, 100.0))
        le = envelope(lip)
        t = SPEC["lip_tol"]
        (xa, ya), (xb_, yb), (xc, yc) = SPEC["lip_tri"]
        xin, xout = (le["min_x"].measured, le["max_x"].measured) if s > 0 else (-le["max_x"].measured, -le["min_x"].measured)
        rows.add("REQ-02 lip inner x (vertices 1, 3)", val("lip_x_inner", xin, "mm"), "in", (xa - t, xa + t), BAND_MM)
        rows.add("REQ-02 lip outer x (vertex 2)", val("lip_x_outer", xout, "mm"), "in", (xb_ - t, xb_ + t), BAND_MM)
        rows.add("REQ-02 lip base y (vertices 1, 2)", le["min_y"], "in", (ya - t, ya + t), BAND_MM)
        rows.add("REQ-02 lip apex y (vertex 3)", le["max_y"], "in", (yc - t, yc + t), BAND_MM)
        rows.add("REQ-02 lip z0", le["min_z"], "in", (SPEC["lip_z"][0] - t, SPEC["lip_z"][0] + t), BAND_MM)
        rows.add("REQ-02 lip z1", le["max_z"], "in", (SPEC["lip_z"][1] - t, SPEC["lip_z"][1] + t), BAND_MM)
        # apex at the inner x: the vertex of the sloped face with the largest y
        verts = sorted(((vv.X, vv.Y) for vv in f.vertices()), key=lambda p: -p[1])
        ax_ = verts[0][0] * s
        rows.add("REQ-02 apex x (vertex 3)", val("lip_apex_x", ax_, "mm"), "in", (xc - t, xc + t), BAND_MM)
        c10 = lid()
        cl = clearance(lip, c10)
        rows.add("REQ-02 lip to OD-C10", cl, "in", (SPEC["lip_gap"] - SPEC["lip_gap_tol"],
                 SPEC["lip_gap"] + SPEC["lip_gap_tol"]), BAND_MM, assumes=("A-02", "A-14"))
        rows.add("D-04d lip to OD-C10 skirt", cl, ">=", SPEC["lip_gap_min"], BAND_MM, assumes=("A-02", "A-14"))
        lx = SPEC["lid_free_x"]
        zone = box(s * lx[0], s * lx[1], SPEC["top_y"], SPEC["lip_tri"][2][1], SPEC["lip_z"][0], SPEC["lip_z"][1])
        cz = common_volume(zone, c10)
        rows.add("REQ-02 lid material in x +-(109.5..117) over the lip's zone", cz, "<=", 0.0, BAND_MM3,
                 assumes=("A-02",))
    run_guarded(rows, "REQ-02", "mm", req02)

    # U-07 export mesh: the delivered STL against a fresh mesh of the re-imported STEP
    def u07():
        r_max = max([fc_.radius for fc_ in solid.faces() if fc_.geom_type.name == "CYLINDER"] or [None])
        ang = params.stl_angular(r_max)
        with tempfile.TemporaryDirectory() as tmp:
            w = write_stl(solid, Path(tmp) / "m.stl", tolerance=SPEC["stl_tol"], angular_tolerance=ang)
        stl_rows(rows, w)
        rows.add("U-07 angular tolerance", val("stl_angular", ang, "rad", r_max=r_max), "<=",
                 4 * math.acos(1 - SPEC["stl_tol"] / r_max), 0.00002)
        if stl is not None and stl.exists():
            mc = mesh_census(stl)
            rows.add("U-07 delivered STL triangles = fresh mesh", mc["triangles"], "==", w.detail["triangles"], BAND_N)
            rows.add("U-07 delivered STL bodies", mc["bodies"], "==", 1, BAND_N)
            rows.add("U-07 delivered STL naked edges", mc["naked_edges"], "==", 0, BAND_N)
    run_guarded(rows, "U-07", "mm", u07)

    rows.manual("U-08", "N/A", note="no threads (row's own N/A)")
    rows.manual("D-07", "N/A", note="no fit-critical bores (row's own N/A)")
    rows.manual("E-06", "PASS" if v["solid_count"].measured == 1 else "FAIL", measured=v["solid_count"].measured,
                unit="count", required="one solid; lip tied into rail, rail into wall (reviewer from sections)",
                note="designer reading of 03_Sections; the reviewer decides")
    rows.manual("REQ-08 (Soft, bench)", "INCONCLUSIVE", required="no visible flex or drumming (first print)",
                note="not geometric; risk MEDIUM (A-13)", assumes=("A-13",))
    return sh


def main(side=1, part="od_c13_right", census=CENSUS_RIGHT, extra=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", default=str(OUT / f"{part}_C1_v01.step"))
    ap.add_argument("--stl", default=str(OUT / f"{part}_C1_v01.stl"))
    ap.add_argument("--params", default="{}")
    ap.add_argument("--json", default=str(CAD / "results_v01" / f"check_{part}.json"))
    a = ap.parse_args()
    params = replace(P, **json.loads(a.params))
    if side > 0:
        from build_od_c13_right import build
    else:
        from build_od_c12_left import build
    built = build(params)
    rows = Rows(part)
    check_panel(side, params, Path(a.step), Path(a.stl) if a.stl else None, built, census, rows)
    if extra:
        extra(params, Path(a.step), rows)
    rows.table()
    rows.dump(Path(a.json), {"step": a.step, "params": json.loads(a.params)})
    print("WORST", rows.worst())


if __name__ == "__main__":
    main()
