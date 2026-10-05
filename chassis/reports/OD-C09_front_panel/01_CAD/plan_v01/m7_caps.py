"""D1: cap axes and foremost points; clearance of the posed board to the planned panel."""
import sys, math; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import BOARD, load
from standin import box, cyl_z, panel
from build123d import Solid
from tools.core import solids
from tools.measure import clearance
e02 = Solid(solids(load("OD-E02_control_board.step", BOARD))[0])
caps = {"B1": (155, 180), "B3": (100, 125), "B2": (125, 155)}
axes = {}
for name, (y0, y1) in caps.items():
    top = e02 & box(-120, -60, y0, y1, 90, 100)
    tb = top.bounding_box(); print(name, "foremost z %.3f" % tb.max.Z, "piece x %.2f..%.2f y %.2f..%.2f" % (tb.min.X, tb.max.X, tb.min.Y, tb.max.Y))
    for z in (91.0, 92.0, 93.0, 94.0, 95.0, 95.5, 96.5, 98.0):
        if z >= tb.max.Z: continue
        sl = e02 & box(-120, -60, y0, y1, z, z+0.01)
        if not sl.solids(): continue
        c = sl.center(); bb = sl.bounding_box()
        print("   z %.1f centroid (%.3f, %.3f) size %.2f x %.2f" % (z, c.X, c.Y, bb.size.X, bb.size.Y))
        if z == 93.0: axes[name] = (c.X, c.Y)
print("axes at z 93", axes)
for name, (y0, y1) in caps.items():
    ax = axes[name]
    w = box(-120, -60, y0, y1, 94, 97) - cyl_z(ax[0], ax[1], 7.5, 93, 98)
    r = clearance(w, e02)
    print(name, "Ø15 hole at", [round(v, 3) for v in ax], "clearance to board %.3f at %s" % (r.measured, r.at))
