from pathlib import Path
import math
from build123d import *
from tools.core import read_step
from tools.measure import clearance, interference
W=Path(__file__).resolve().parents[2] / "00_Spec" / "inputs"
h24=read_step(W/"OD-H24_flowmeter.step")
half=math.degrees(math.asin(3/21.87))
def arc(r0,r1,z0,h,th):
    s=(Cylinder(r1,h,align=(Align.CENTER,Align.CENTER,Align.MIN))-Cylinder(r0,h,align=(Align.CENTER,Align.CENTER,Align.MIN)))
    R=40; a=math.radians(half)
    w=extrude(Polygon((0,0),(R*math.cos(a),-R*math.sin(a)),(R*math.cos(a),R*math.sin(a)),align=None),amount=h)
    return (s & w).moved(Location((0,0,z0))).rotate(Axis.Z,th)
far = h24 & (Box(100,100,60) - Cylinder(20.5,60))
for th in (70,160,290,300,315,320,325):
    beam=arc(20.87,22.87,-6,25.9+3,th); catch=arc(18.87,22.87,19.9,1.0,th)
    below=arc(18.87,22.87,17.25,2.65,th)
    v=list(interference({"a":below,"b":h24}).values())[0].measured
    c=clearance(beam+catch,far)
    cb=clearance(beam,h24)
    print(th,"flange under catch mm3",round(v,3),"clear to outside-r20.5 parts",round(c.measured,3),c.at,"beam-H24",round(cb.measured,3))
print("half angle",half)
