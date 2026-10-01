"""D6 screening sections for od_c15_foot v01, from the exported STEP files (re-imported).

Foot: the plane XZ (view "front") and YZ (view "left") through the axis, and XY (view "top")
at z 6.0 across the nut pocket. Assembly at pose 1 (hole at X 110, Z 90): the plate is
cut to a 40 mm square window around the hole so the foot is legible; planes YZ ("left",
X = 110) and XY ("top", Z = 90) through the hole axis.

Usage: python sections_od_c15_foot.py --foot <foot.step> --assembly <asm.step> --out <03_Sections> --version 1
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from build123d import Box, Compound, Pos, Solid

from tools.core import read_step, solids
from tools.drawing import write_sections

WINDOW = 40.0                # mm, the plate window around the pose-1 hole
POSE1 = (110.0, -6.0, 90.0)  # spec §2
POCKET_Z = 6.0               # foot frame: across the nut pocket


def labelled(asm, name):
    for c in asm.children:
        if c.label == name:
            return Solid(solids(c)[0])
    raise KeyError(name)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--foot", required=True)
    ap.add_argument("--assembly", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--version", type=int, required=True)
    a = ap.parse_args(argv)
    out = Path(a.out)
    foot = Solid(solids(read_step(a.foot))[0])
    rows = []
    for w in write_sections(foot, out, part="od_c15_foot", version=a.version,
                            views=("front", "left", "top"), through=(0.0, 0.0, POCKET_Z)):
        rows.append({"file": w.path.name, "sha256": w.sha256,
                     "nothing_clipped": w.checks["nothing_clipped"].to_dict()})
    asm = read_step(a.assembly)
    x, y, z = POSE1
    window = Pos(x, y, z) * Box(WINDOW, 60.0, WINDOW)
    plate_win = Solid(solids(labelled(asm, "plate") & window)[0])
    parts = [plate_win, labelled(asm, "foot_1"), labelled(asm, "screw_1"), labelled(asm, "nut_1")]
    local = Compound(children=parts)
    for w in write_sections(local, out, part="od_c15_assembly_pose1", version=a.version,
                            views=("left", "top"), through=(x, y - 4.0, z)):
        rows.append({"file": w.path.name, "sha256": w.sha256,
                     "nothing_clipped": w.checks["nothing_clipped"].to_dict()})
    print(json.dumps(rows, indent=1, default=str))


if __name__ == "__main__":
    sys.exit(main())
