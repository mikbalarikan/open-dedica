import math
from pathlib import Path
from build123d import Solid, Cylinder, Box, Pos, Axis, Location
from tools.core import read_step
from tools.core.shapes import solids
from tools.measure import bore_census, locate_bore
W = Path("/root/oguz-jobs/20261002-od-c14-cord-grommet")
STEP = W/"02_STEP_STL/od_c14_grommet_half_C1_v01.step"
def load(p): return Solid(solids(read_step(p))[0])
def half(): return load(STEP)
def c11(): return load(W/"00_Spec/inputs/OD-C11_back_panel.step")
def c01():
    s = solids(read_step(W/"00_Spec/inputs/OD-C01_base_frame.step"))
    assert len(s) == 1, len(s)
    return Solid(s[0])
def hole_axis(panel):
    bc = bore_census(panel)
    lb = locate_bore(bc, (95, 30, -300.5), (0, 0, 1))
    # find bore record
    best = None
    for b in bc.detail["bores"]:
        st = b["start"]; 
        d = math.hypot(st[0]-95, st[1]-30)
        if abs(b["diameter"]-12) < 0.01 and (best is None or d < best[0]): best = (d, b)
    return lb, best[1]
def box(x0,x1,y0,y1,z0,z1):
    return Pos((x0+x1)/2,(y0+y1)/2,(z0+z1)/2)*Box(x1-x0,y1-y0,z1-z0)
def ring(cx, cy, rin, rout, z0, z1):
    h = z1-z0; p = Pos(cx, cy, (z0+z1)/2)
    return p*Cylinder(rout, h) - p*Cylinder(rin, h)
def cyl(cx, cy, r, z0, z1):
    return Pos(cx, cy, (z0+z1)/2)*Cylinder(r, z1-z0)
def one(s):
    ss = solids(s); assert len(ss) == 1, len(ss); return Solid(ss[0])
