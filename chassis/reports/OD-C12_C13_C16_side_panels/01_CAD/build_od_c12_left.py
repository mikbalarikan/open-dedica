"""OD-C12 left side panel, concept C1, spec 1.1 (D4): the mirror of OD-C13 about x = 0 plus the
valve-mount relief. F11 right panel rebuilt from the shared parameters, F12 mirror, F13 relief.

Run: build_od_c12_left.py [--params JSON] [--out-dir DIR] [--tag C1_v01]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Plane, mirror  # noqa: E402

from build_od_c13_right import build as build_right, cli, span_box  # noqa: E402
from params_od_side_panels import P  # noqa: E402

PART = "od_c12_left"


def build(p=P):
    right = build_right(p)                                   # F11
    mirrored = mirror(right, about=Plane.YZ)                 # F12
    # F13 relief: floor at x -117.9, opens through the inner face and the underside
    relief = span_box(p.relief_floor_x, -p.wall_inner_x + p.overrun, p.wall_y0 - p.overrun, p.relief_y1,
                      p.relief_z0, p.relief_z1)
    panel = (mirrored - relief).clean()
    panel = panel.solids()[0]
    panel.label = PART
    return panel


if __name__ == "__main__":
    cli(build, PART)
