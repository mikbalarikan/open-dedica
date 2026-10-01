from pathlib import Path
from build123d import *
from tools.core import read_step
from tools.measure import interference, clearance
W=Path(__file__).resolve().parents[2] / "00_Spec" / "inputs"
h22=read_step(W/"OD-H22_3way_valve.step")
def bb(s):
    b=s.bounding_box(); return tuple(round(v,3) for v in (b.min.X,b.max.X,b.min.Y,b.max.Y,b.min.Z,b.max.Z))
for z in [-8,-10,-12,-14,-16,-18,-20,-22,-24,-26,-28,-30]:
    sec=h22 & Box(80,80,0.02).moved(Location((0,0,z)))
    print(z,[bb(s) for s in sec.solids()])
# footprint of H22 below z=-7.7 projected: max radius
low = h22 & Box(80,80,30,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((0,0,-7.7)))
print("below deck bb", bb(low))
# probe: deck with bore and spec slits in H22 frame; H22 raised by d along +Z
import math
deck = Box(44,30,7.7,align=(Align.CENTER,Align.CENTER,Align.MAX)) - Cylinder(7.05,20)
for d in [40,30,20,15,10,7.8,5,2,0.5,0]:
    r=interference({"deck":deck,"h22":h22.moved(Location((0,0,d)))})
    v=list(r.values())[0]
    print("raised",d,"common mm3",v.measured,v.status)
