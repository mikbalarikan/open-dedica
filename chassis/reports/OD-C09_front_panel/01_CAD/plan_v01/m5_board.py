"""D1: OD-E02 as posed: pieces in front of z 90, caps, screw holes, front surface at the holes."""
import sys, math; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from poses import BOARD, load
from build123d import Box, Pos, Solid, Plane, Vector
from tools.core import solids
from tools.measure import bore_census
from OCP.IntCurvesFace import IntCurvesFace_ShapeIntersector
from OCP.gp import gp_Lin, gp_Pnt, gp_Dir

e02 = Solid(solids(load("OD-E02_control_board.step", BOARD))[0])
# pieces in front of z 90
for z0 in (88.0, 90.0, 92.0, 93.0, 94.0):
    c = e02 & (Pos(-88, 140, (z0+100)/2) * Box(80, 100, 100-z0))
    print("z >=", z0, [(round(p.volume,1), [round(v,2) for v in (p.bounding_box().min.X,p.bounding_box().max.X,p.bounding_box().min.Y,p.bounding_box().max.Y,p.bounding_box().min.Z,p.bounding_box().max.Z)]) for p in c.solids()])
bc = bore_census(e02)
print("E02 bores", bc.measured)
for b in bc.detail["bores"]:
    print("  d%.3f start %s end %s len %.2f through %s" % (b["diameter"], [round(v,3) for v in b["start"]], [round(v,3) for v in b["end"]], b["length"], b.get("through")))

isect = IntCurvesFace_ShapeIntersector(); isect.Load(e02.wrapped, 1e-6)
def first_hit(x, y, z_from=110.0):
    isect.Perform(gp_Lin(gp_Pnt(x, y, z_from), gp_Dir(0, 0, -1)), 0, 200)
    if not isect.IsDone() or isect.NbPnt() == 0: return None
    return max(isect.Pnt(i).Z() for i in range(1, isect.NbPnt()+1))
for name, (cx, cy) in {"L": (-91.06, 153.23), "R": (-91.0, 127.25)}.items():
    zs = []
    for r in np.arange(2.0, 5.51, 0.25):
        for a in np.arange(0, 360, 10):
            h = first_hit(cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a)))
            zs.append((h, r, a))
    hs = [h for h,_,_ in zs if h is not None]
    print(name, "ring r2..5.5 hits", len(hs), "of", len(zs), "z max %.3f min %.3f" % (max(hs), min(hs)))
    for rr in (2.0, 3.0, 4.0, 5.0, 5.5):
        v=[h for h,r,a in zs if abs(r-rr)<1e-6 and h is not None]; print("   r", rr, "z", round(min(v),3), round(max(v),3), "n", len(v))
