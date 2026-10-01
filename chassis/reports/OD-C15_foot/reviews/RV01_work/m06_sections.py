"""RV01: own sections of the foot and of my own pose-1 assembly (plate cut to a window)."""
import json
from pathlib import Path
from build123d import Cylinder, Polygon, extrude, Location, Align, Box, Pos, Compound
import math
from tools.core import read_step
from tools.drawing import write_sections
W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet"); R = W / "reviews/RV01_work"
foot = read_step(W / "02_STEP_STL/od_c15_foot_C1_v01.step")
plate = read_step(W / "00_Spec/inputs/OD-C01_base_frame.step")
def hexagon(s):
    e2 = s / math.sqrt(3)
    return Polygon(*[(e2 * math.cos(math.radians(60 * k)), e2 * math.sin(math.radians(60 * k))) for k in range(6)], align=None)
nut = (extrude(hexagon(5.5), 2.4) - Cylinder(1.5, 3, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -0.3)))).moved(Location((0, 0, 2.5)))
screw = Cylinder(2.85, 1.65, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -7.65))) + Cylinder(1.5, 12.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -6.0)))
L = Location((110, -6.0, 90), (90, 0, 0))
win = plate & Pos(105, -3, 85) * Box(30, 6, 30)
asm = Compound([win, foot.moved(L), nut.moved(L), screw.moved(L)])
res = {}
for w in write_sections(foot, R / "sections", part="rv01_foot", version=1, views=("front", "left", "top"), through=(0, 0, 6.0)):
    res[w.path.name] = w.checks["nothing_clipped"].measured
for w in write_sections(asm, R / "sections", part="rv01_pose1", version=1, views=("front", "left"), through=(110, -8, 90)):
    res[w.path.name] = w.checks["nothing_clipped"].measured
print(res)
