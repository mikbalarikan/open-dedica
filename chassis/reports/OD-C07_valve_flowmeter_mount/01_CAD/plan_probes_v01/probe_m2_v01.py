from pathlib import Path
import math
from build123d import *
from tools.core import read_step
from tools.measure import envelope, clearance, interference, radial_profile, radial_extent
W=Path(__file__).resolve().parents[2] / "00_Spec" / "inputs"
h22=read_step(W/"OD-H22_3way_valve.step"); h24=read_step(W/"OD-H24_flowmeter.step")
def bb(s):
    b=s.bounding_box(); return tuple(round(v,3) for v in (b.min.X,b.max.X,b.min.Y,b.max.Y,b.min.Z,b.max.Z))
print("--- H22 planar faces at z=0 facing -Z")
for f in h22.faces():
    if f.geom_type==GeomType.PLANE:
        n=f.normal_at(); c=f.center()
        if abs(c.Z)<1e-3 and n.Z<-0.99: print("area",round(f.area,2),"bb",bb(f))
print("--- H22 slices below flange (x,y extents of material)")
for z in [-0.05,-0.5,-1,-2,-3,-4,-5,-6,-7,-7.7]:
    sec=h22 & Box(60,60,0.02,align=(Align.CENTER,Align.CENTER,Align.CENTER)).moved(Location((0,0,z)))
    parts=[bb(s) for s in (sec.solids() if hasattr(sec,'solids') else [])]
    print(z,parts)
print("--- H22 gusset slabs: material with |x|>7.1 below z=0")
for sx in (1,-1):
    box=Box(15,10,10,align=(Align.MIN if sx>0 else Align.MAX,Align.CENTER,Align.MAX)).moved(Location((7.1*sx,0,0)))
    g=h22 & box
    for s in g.solids(): print("side",sx,bb(s),round(s.volume,3))
print("--- H22 above z=0 up to 5.63: outline")
for z in [0.5,2.0,3.0,5.0]:
    sec=h22 & Box(60,60,0.02).moved(Location((0,0,z)))
    print(z,[bb(s) for s in sec.solids()])
print("--- H24 planar faces facing -Z")
for f in h24.faces():
    if f.geom_type==GeomType.PLANE and f.normal_at().Z<-0.99: print("z",round(f.center().Z,3),"area",round(f.area,2),"bb",bb(f))
print("--- H24 planar faces facing +Z, z>15")
for f in h24.faces():
    if f.geom_type==GeomType.PLANE and f.normal_at().Z>0.99 and f.center().Z>15: print("z",round(f.center().Z,3),"area",round(f.area,2),"bb",bb(f))
print("--- H24 slices")
for z in [-3,-0.05,0.05,1,2,3,3.5,5,8,12,13,15,18,19.8]:
    sec=h24 & Box(90,90,0.02).moved(Location((0,0,z)))
    print(z,[bb(s) for s in sec.solids()])
