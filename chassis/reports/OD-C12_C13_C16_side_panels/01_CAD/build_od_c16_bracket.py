"""OD-C16 corner bracket, concept C1, spec 1.1 (D4), in its own frame: outer face x 0, underside
y 0, symmetric about z 0. F21 block, F22 plate-screw hole along Y, F23 counterbore, F24 insert bore.

Run: build_od_c16_bracket.py [--params JSON] [--out-dir DIR] [--tag C1_v01]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Cylinder, Location  # noqa: E402

from build_od_c13_right import cli, span_box  # noqa: E402
from params_od_side_panels import P  # noqa: E402

PART = "od_c16_bracket"


def build(p=P):
    block = span_box(p.block_x0, p.block_x1, 0.0, p.block_y1, -p.block_half_z, p.block_half_z)   # F21
    # F22 through-hole along Y at (x -12.5, z 0); a cylinder's axis is Z, turned 90 deg about X onto Y
    h_len = p.block_y1 + 2 * p.overrun
    hole = Location((p.br_hole_x, p.block_y1 / 2, p.br_hole_z), (90, 0, 0)) * Cylinder(p.br_hole_d / 2, h_len)
    # F23 counterbore from the top face down to its flat floor at y 3.0
    c_len = (p.block_y1 - p.cbore_floor_y) + p.overrun
    cbore = Location((p.br_hole_x, p.cbore_floor_y + c_len / 2, p.br_hole_z), (90, 0, 0)) * Cylinder(p.cbore_d / 2, c_len)
    # F24 blind insert bore along -X from the outer face x 0, flat floor at x -6.0
    i_len = p.insert_bore_depth + p.overrun
    insert = (Location((p.block_x1 - p.insert_bore_depth + i_len / 2, p.insert_bore_y, p.insert_bore_z), (0, 90, 0))
              * Cylinder(p.insert_bore_d / 2, i_len))
    bracket = (block - hole - cbore - insert).clean()
    bracket = bracket.solids()[0]
    bracket.label = PART
    return bracket


if __name__ == "__main__":
    cli(build, PART)
