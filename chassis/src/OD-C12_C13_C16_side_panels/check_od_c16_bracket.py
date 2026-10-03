"""Checks for OD-C16 (corner bracket, its own frame), written before build_od_c16_bracket.py (D3).

Run: check_od_c16_bracket.py [--step S] [--stl L] [--params JSON] [--json OUT]
The six placed poses (REQ-05 plate holes, coaxiality) are checked in check_od_side_panels_assembly.py.
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

from checklib_od_side_panels import (BAND_DEG, BAND_MM, BAND_N, CAD, OUT, Rows, bores_along,  # noqa: E402
                                     gate_census, gate_envelope, gate_roundtrip, gate_validity, gate_walls,
                                     nearest_bore, run_guarded, stl_rows, val)
from params_od_side_panels import P  # noqa: E402
from tools.core import read_step, write_stl  # noqa: E402
from tools.measure import (bore_census, flat_ceiling_spans, locate_bore, mesh_census, overhang_census,  # noqa: E402
                           radial_profile)

SPEC = {
    "size": (19.0, 16.0, 16.0), "pos": ((-19.0, 0.0), (0.0, 16.0), (-8.0, 8.0)),   # U-02, REQ-05
    "hole_d": 3.4, "d_tol": 0.1, "hole_xz": (-12.5, 0.0), "offset": 0.10,          # REQ-05
    "cbore_d": 6.5, "cbore_floor_y": 3.00, "floor_tol": 0.10,                      # REQ-05
    "insert_d": 4.0, "insert_d_tol": 0.05, "insert_depth": 6.0, "depth_tol": 0.1,  # D-05b
    "insert_len_min": 5.7,                                                          # D-05b (>= the insert)
    "insert_yz": (10.0, 0.0),                                                       # REQ-05
    "boss_across": 8.0,                                                             # D-05a
    "wall_threaded": 3.0,                                                           # J-05
    "clear_hole_min": 3.25,                                                         # D-04a
    "overhang_min": 45.0, "bridge_max": 5.0,                                        # D-03a, D-03b
    "bed": (220.0, 220.0, 250.0),                                                   # D-02 via A-10
    "stl_tol": 0.01,                                                                # U-07
}
CENSUS = {"plane_faces": 8, "cylinder_faces": 3, "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0,
          "bspline_faces": 0, "other_faces": 0, "concave_cylinders": 3, "convex_cylinders": 0, "bores": 3}
WALL_SPACING = 0.4


def check_bracket(params, step: Path, stl: Path | None, built, rows: Rows):
    sh = read_step(step)
    v = gate_validity(rows, sh)
    solid = sh.solids()[0]
    e = run_guarded(rows, "U-02", "mm", gate_envelope, rows, sh, SPEC["size"], SPEC["pos"],
                    gate_ids=("U-02", "envelope_within_spec", "REQ-05 block"))
    if e:
        for ax, lim in zip("xyz", SPEC["bed"]):
            rows.add(f"D-02 size_{ax}", e[f"size_{ax}"], "<=", lim, BAND_MM, assumes=("A-10",))
    run_guarded(rows, "U-04", "-", gate_roundtrip, rows, built, step)
    run_guarded(rows, "U-05", "count", gate_census, rows, sh, CENSUS)
    w = run_guarded(rows, "D-01b", "mm", gate_walls, rows, sh, WALL_SPACING)

    bc = bore_census(sh)
    hx, hz = SPEC["hole_xz"]
    t = SPEC["d_tol"]
    # REQ-05 / D-04a: the plate-screw hole along Y
    lb = locate_bore(bc, (hx, 1.5, hz), (0, 1, 0))
    rows.add("REQ-05 hole diameter", lb["diameter"], "in", (SPEC["hole_d"] - t, SPEC["hole_d"] + t), BAND_MM)
    rows.add("REQ-05 hole offset", lb["offset"], "<=", SPEC["offset"], BAND_MM)
    rows.add("REQ-05 hole through", lb["through"], "==", 1, BAND_N)
    rows.add("D-04a hole diameter", lb["diameter"], ">=", SPEC["clear_hole_min"], BAND_MM)
    # REQ-05: counterbore
    def cbore():
        b = nearest_bore(bc, (hx, 10.0, hz), (0, 1, 0))
        rows.add("REQ-05 counterbore diameter", val("cbore_d", b["diameter"], "mm"), "in",
                 (SPEC["cbore_d"] - t, SPEC["cbore_d"] + t), BAND_MM)
        floor = min(b["start"][1], b["end"][1])
        rows.add("REQ-05 counterbore floor y", val("cbore_floor_y", floor, "mm"), "in",
                 (SPEC["cbore_floor_y"] - SPEC["floor_tol"], SPEC["cbore_floor_y"] + SPEC["floor_tol"]), BAND_MM)
        top = max(b["start"][1], b["end"][1])
        rows.add("REQ-05 counterbore opens at y 16", val("cbore_top_y", top, "mm"), "in",
                 (SPEC["pos"][1][1] - 0.1, SPEC["pos"][1][1] + 0.1), BAND_MM)
        lo_open = b["open_ends"][0] if b["start"][1] < b["end"][1] else b["open_ends"][1]
        rows.add("REQ-05 counterbore floor closed (1 = closed)", val("cbore_closed", int(not lo_open), "bool"),
                 "==", 1, BAND_N)
        off = math.hypot(b["start"][0] - hx, b["start"][2] - hz)
        rows.add("REQ-05 counterbore offset", val("cbore_offset", off, "mm"), "<=", SPEC["offset"], BAND_MM)
        return b
    cb = run_guarded(rows, "REQ-05 counterbore", "mm", cbore)
    # D-05b / REQ-05: the insert bore along -X from x 0
    iy, iz = SPEC["insert_yz"]
    li = locate_bore(bc, (-1.0, iy, iz), (1, 0, 0))
    rows.add("D-05b insert bore diameter", li["diameter"], "in",
             (SPEC["insert_d"] - SPEC["insert_d_tol"], SPEC["insert_d"] + SPEC["insert_d_tol"]), BAND_MM, assumes=("A-12",))
    rows.add("D-05b insert bore depth", li["length"], "in",
             (SPEC["insert_depth"] - SPEC["depth_tol"], SPEC["insert_depth"] + SPEC["depth_tol"]), BAND_MM, assumes=("A-12",))
    rows.add("D-05b insert bore depth >= insert", li["length"], ">=", SPEC["insert_len_min"], BAND_MM, assumes=("A-12",))
    rows.add("D-05b insert bore blind (through = 0)", li["through"], "==", 0, BAND_N)
    rows.add("REQ-05 insert bore offset", li["offset"], "<=", SPEC["offset"], BAND_MM)

    def insert_rows():
        ib = nearest_bore(bc, (-1.0, iy, iz), (1, 0, 0))
        xs = (ib["start"][0], ib["end"][0])
        mouth_open = ib["open_ends"][xs.index(max(xs))]
        rows.add("REQ-05 insert bore opens at x 0", val("insert_mouth_x", max(xs), "mm", open=mouth_open), "in",
                 (-0.1, 0.1), BAND_MM)
        rows.add("REQ-05 insert bore mouth open (1/0)", val("insert_mouth_open", int(mouth_open), "bool"), "==", 1, BAND_N)
        r = ib["radius"]
        prof = radial_profile(solid, (0.0, ib["start"][1], ib["start"][2]), (-1, 0, 0), (0, 1, 0),
                              [a * 15.0 for a in range(24)], (0.0, ib["length"]), margin=(0.1, 0.0), z_step=0.25,
                              side="outer", r_min=r - 0.05)
        mn = prof["min"]
        if mn.ok:
            across = val("insert_boss_across", 2.0 * mn.measured, "mm", at=mn.at)
            radial_wall = val("insert_radial_wall", mn.measured - r, "mm", at=mn.at)
        else:
            across = radial_wall = mn
        rows.add("D-05a material across the insert bore", across, ">=", SPEC["boss_across"], BAND_MM, assumes=("A-12",))
        rows.add("J-05 radial wall around the insert bore", radial_wall, ">=", SPEC["wall_threaded"], BAND_MM)
        if cb:
            web = abs(min(xs) - cb["start"][0]) - cb["radius"]
            rows.add("J-05 axial web, insert-bore floor to counterbore", val("insert_axial_web", web, "mm"), ">=",
                     SPEC["wall_threaded"], BAND_MM)
        return ib
    ib = run_guarded(rows, "D-05a/J-05", "mm", insert_rows)

    # D-03a: print on the underside, build +Y; the insert-bore crown is the named exception (by position)
    oh = overhang_census(sh, build_dir=(0, 1, 0), spacing=0.25)
    pk = oh.detail.get("per_kind_least_deg", {}) if oh.ok else {}
    if oh.ok:
        planes = val("overhang_planes", pk.get("plane", 90.0), "deg")
        rows.add("D-03a planes (every face but the insert bore)", planes, ">=", SPEC["overhang_min"], BAND_DEG)
        non_y = [b for b in bc.detail["bores"] if abs(abs(b["axis_dir"][1]) - 1.0) > 1e-6]
        rows.add("D-03a cylinders not along Y = the insert bore only", val("non_vertical_bores", len(non_y), "count"),
                 "==", 1, BAND_N, note="every other cylinder is vertical in the print and cannot face down")
        rows.manual("D-03a exception: insert-bore crown least angle", "INFO", measured=round(oh.measured, 4), unit="deg",
                    note=f"named exception (spec 5, Usta U-18); at {oh.at}; per kind {pk}")
    else:
        rows.add("D-03a", oh, ">=", SPEC["overhang_min"], BAND_DEG)
    fc = flat_ceiling_spans(sh, build_dir=(0, 1, 0), max_span=SPEC["bridge_max"], spacing=0.25)
    rows.add("D-03b flat ceilings (corroboration)", fc, "<=", SPEC["bridge_max"], BAND_MM)
    if ib:
        rows.add("D-03b insert-bore crown bridge (its diameter; reviewer from sections)",
                 val("crown_bridge", ib["diameter"], "mm"), "<=", SPEC["bridge_max"], BAND_MM, assumes=("A-11",))

    def u07():
        r_max = max(f.radius for f in solid.faces() if f.geom_type.name == "CYLINDER")
        ang = params.stl_angular(r_max)
        with tempfile.TemporaryDirectory() as tmp:
            wr = write_stl(solid, Path(tmp) / "m.stl", tolerance=SPEC["stl_tol"], angular_tolerance=ang)
        stl_rows(rows, wr)
        rows.add("U-07 angular tolerance", val("stl_angular", ang, "rad", r_max=r_max), "<=",
                 4 * math.acos(1 - SPEC["stl_tol"] / r_max), 0.00002)
        if stl is not None and stl.exists():
            mc = mesh_census(stl)
            rows.add("U-07 delivered STL triangles = fresh mesh", mc["triangles"], "==", wr.detail["triangles"], BAND_N)
            rows.add("U-07 delivered STL bodies", mc["bodies"], "==", 1, BAND_N)
            rows.add("U-07 delivered STL naked edges", mc["naked_edges"], "==", 0, BAND_N)
    run_guarded(rows, "U-07", "mm", u07)

    rows.manual("U-08", "N/A", note="no threads (row's own N/A)")
    rows.manual("D-07", "N/A", note="no fit-critical bores (row's own N/A)")
    rows.manual("E-06", "PASS" if v["solid_count"].measured == 1 else "FAIL", measured=v["solid_count"].measured,
                unit="count", required="the bracket is one solid block (reviewer from sections)",
                note="designer reading of 03_Sections; the reviewer decides")
    if w is not None and w.ok:
        rows.manual("J-05 global min_wall (beside, never instead)", "INFO", measured=round(w.measured, 4), unit="mm",
                    note=f"at {w.at}")
    return sh


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", default=str(OUT / "od_c16_bracket_C1_v01.step"))
    ap.add_argument("--stl", default=str(OUT / "od_c16_bracket_C1_v01.stl"))
    ap.add_argument("--params", default="{}")
    ap.add_argument("--json", default=str(CAD / "results_v01" / "check_od_c16_bracket.json"))
    a = ap.parse_args()
    params = replace(P, **json.loads(a.params))
    from build_od_c16_bracket import build
    rows = Rows("od_c16_bracket")
    check_bracket(params, Path(a.step), Path(a.stl) if a.stl else None, build(params), rows)
    rows.table()
    rows.dump(Path(a.json), {"step": a.step, "params": json.loads(a.params)})
    print("WORST", rows.worst())


if __name__ == "__main__":
    main()
