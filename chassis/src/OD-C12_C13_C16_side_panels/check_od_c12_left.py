"""Checks for OD-C12 (left panel), written before build_od_c12_left.py (D3).

The panel predicates of check_od_c13_right.py at side -1, plus REQ-04 (the valve-mount relief).
Run: check_od_c12_left.py [--step S] [--stl L] [--params JSON] [--json OUT]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Location, Plane  # noqa: E402

from check_od_c13_right import CENSUS_RIGHT, main  # noqa: E402
from checklib_od_side_panels import BAND_MM, BAND_N, INP, face_box, planar_faces, run_guarded, val  # noqa: E402
from tools.core import read_step  # noqa: E402
from tools.measure import clearance, radial_extent  # noqa: E402

# spec 1.1: the relief adds four planes (floor x -117.9, top y 55, ends z -160 / -29); U-05
CENSUS_LEFT = {**CENSUS_RIGHT, "plane_faces": CENSUS_RIGHT["plane_faces"] + 4}
REQ04 = {"floor_x": -117.90, "floor_tol": 0.05, "y": (0.0, 55.0), "z": (-160.0, -29.0), "tol": 0.1,
         "clear_c07": 0.5}


def placed_c07():
    """OD-C07 by its section 2 joint: x -> -Z, y -> -X, z -> +Y, origin (-92, 0, -60)."""
    s = read_step(INP / "OD-C07_valve_flowmeter_mount.step")
    return s.moved(Location(Plane(origin=(-92, 0, -60), x_dir=(0, 0, -1), z_dir=(0, 1, 0))))


def relief(params, step, rows):
    def go():
        sh = read_step(step)
        solid = sh.solids()[0]
        floors = [f for f in planar_faces(solid, (1, 0, 0)) if abs(face_box(f)[0] - REQ04["floor_x"]) < 0.5]
        rows.add("REQ-04 relief floor faces", val("relief_floor_faces", len(floors), "count"), "==", 1, BAND_N)
        for f in floors:
            b = face_box(f)
            rows.add("REQ-04 relief floor x", val("relief_floor_x", b[0], "mm", box=b), "in",
                     (REQ04["floor_x"] - REQ04["floor_tol"], REQ04["floor_x"] + REQ04["floor_tol"]), BAND_MM,
                     assumes=("A-04",))
            t = REQ04["tol"]
            for name, got, want in (("y0", b[2], REQ04["y"][0]), ("y1", b[3], REQ04["y"][1]),
                                    ("z0", b[4], REQ04["z"][0]), ("z1", b[5], REQ04["z"][1])):
                rows.add(f"REQ-04 relief {name}", val(f"relief_{name}", got, "mm"), "in", (want - t, want + t), BAND_MM)
        # the wall left over the relief, read across at y 30, z -100 (2.1 by 1.1 Q4)
        o = radial_extent(solid, (0, 30.0, 0), (0, 0, 1), (-1, 0, 0), 0.0, -100.0, side="outer", r_min=100.0)
        i = radial_extent(solid, (0, 30.0, 0), (0, 0, 1), (-1, 0, 0), 0.0, -100.0, side="inner", r_min=100.0)
        if o.ok and i.ok:
            rows.add("REQ-04 wall at the relief (info for D-01b)", val("relief_wall", o.measured - i.measured, "mm"),
                     ">=", 2.0, BAND_MM)
        cl = clearance(solid, placed_c07())
        rows.add("REQ-04 clearance OD-C12 to OD-C07", cl, ">=", REQ04["clear_c07"], BAND_MM, assumes=("A-04",))
    run_guarded(rows, "REQ-04", "mm", go)


if __name__ == "__main__":
    main(side=-1, part="od_c12_left", census=CENSUS_LEFT, extra=relief)
