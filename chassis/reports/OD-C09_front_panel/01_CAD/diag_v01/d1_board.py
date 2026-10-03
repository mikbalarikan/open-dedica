"""J3 diagnostic (guides the build, gates nothing): posed OD-E02 screw holes, cap sections, collar fronts."""
import sys, time; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plan_v01"))
from poses import BOARD, load
from build123d import Box, Pos, Solid, Cylinder
from tools.core import solids
from tools.measure import bore_census, clearance
t0 = time.time()
e02 = Solid(solids(load("OD-E02_control_board.step", BOARD))[0])
bc = bore_census(e02)
for b in bc.detail["bores"]:
    if abs(b["axis_dir"][2]) > 0.99 and b["diameter"] < 4:
        print("hole d%.4f start %s end %s" % (b["diameter"], [round(v, 4) for v in b["start"]], [round(v, 4) for v in b["end"]]))
def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0+x1)/2, (y0+y1)/2, (z0+z1)/2) * Box(x1-x0, y1-y0, z1-z0)
caps = {"B1": (-94.248, 166.514), "B2": (-98.991, 139.901), "B3": (-93.765, 113.426)}
for n, (x, y) in caps.items():
    for z in (88.0, 88.5, 89.0, 89.5, 90.0, 90.5, 91.0, 92.0, 93.0, 95.5):
        s = e02 & box(x-7.2, x+7.2, y-7.2, y+7.2, z, z+0.001)
        ps = s.solids() if s is not None else []
        if not ps: print(n, z, "none"); continue
        v = sum(p.volume for p in ps)/0.001; c = s.center()
        print(n, z, "area %.2f centroid (%.4f, %.4f) pieces %d" % (v, c.X, c.Y, len(ps)))
# collar fronts: board within ring r 7.2..9 about collar axes
for n, (x, y, r) in {"B1": (-94.172, 166.513, 8.0898), "B3": (-93.731, 113.543, 8.1907)}.items():
    ring = (Pos(x, y, 90) * Cylinder(r + 1.0, 10)) - (Pos(x, y, 90) * Cylinder(6.9, 10))
    c = e02 & ring
    print(n, "collar ring max z %.4f" % c.bounding_box().max.Z)
print("t %.1f" % (time.time()-t0))
