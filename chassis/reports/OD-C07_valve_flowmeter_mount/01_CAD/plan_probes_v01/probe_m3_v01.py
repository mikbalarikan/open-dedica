from pathlib import Path
import math
from build123d import *
from tools.core import read_step
from tools.measure import clearance, interference, radial_profile
W=Path(__file__).resolve().parents[2] / "00_Spec" / "inputs"
h22=read_step(W/"OD-H22_3way_valve.step"); h24=read_step(W/"OD-H24_flowmeter.step")
def cl(a,b,name):
    r=clearance(a,b); print(name, r.status, round(r.measured,4) if r.measured is not None else None, r.at, r.reason)
# probes in H24 frame (mount z = H24 z + 10)
ped = Cylinder(18,6,align=(Align.CENTER,Align.CENTER,Align.MAX))
ped = ped - Cylinder(2.4,6,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((0.185,0.093,0))) - Cylinder(1.9,6,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((-11.78,0.14,0)))
cl(ped,h24,"pedestal flat top (contact expected 0)")
# pedestal minus rim annulus contact: probe the inner region only
inner = Cylinder(13.5,1,align=(Align.CENTER,Align.CENTER,Align.MAX))
cl(inner,h24,"pedestal inner disc r13.5 (no pin holes) ")
inner2 = inner - Cylinder(2.4,6).moved(Location((0.185,0.093,0))) - Cylinder(1.9,6).moved(Location((-11.78,0.14,0)))
cl(inner2,h24,"pedestal inner disc r13.5 with pin holes")
ring = Cylinder(18.3,3,align=(Align.CENTER,Align.CENTER,Align.MIN)) - Cylinder(16.3,3,align=(Align.CENTER,Align.CENTER,Align.MIN))
cl(ring,h24,"ring 16.3..18.3 z0..3")
pinholes_wall = Cylinder(4,6,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((0.185,0.093,-0.001))) - Cylinder(2.4,6,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((0.185,0.093,-0.001)))
cl(pinholes_wall,h24,"pin1 hole wall")
p2 = Cylinder(3.5,6,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((-11.78,0.14,-0.001))) - Cylinder(1.9,6,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((-11.78,0.14,-0.001)))
cl(p2,h24,"pin2 hole wall")
def hook(th):
    beam = Box(2.0,6.0,25.9+2,align=(Align.MIN,Align.CENTER,Align.MIN)).moved(Location((20.87,0,-6.0)))
    catch = Box(4.0,6.0,2.0,align=(Align.MIN,Align.CENTER,Align.MIN)).moved(Location((18.87,0,19.9)))
    return (beam+catch).rotate(Axis.Z,th)
for th in (70,160,290):
    hk=hook(th); cl(hk,h24,f"hook {th} (catch contact expected 0)")
    beam = Box(2.0,6.0,25.9,align=(Align.MIN,Align.CENTER,Align.MIN)).moved(Location((20.87,0,-6.0))).rotate(Axis.Z,th)
    cl(beam,h24,f"hook {th} beam only")
    # clearance to pipes: H24 material with y< -20.5 or anything outside r>20.5
    far = h24 & (Box(100,100,60) - Cylinder(20.5,60))
    cl(hk, far, f"hook {th} vs H24 outside r20.5")
    # catch over slot: catch footprint vs slot pocket volume (below flange top, above slot floor)
    catchbelow = Box(4.0,6.0,2.65,align=(Align.MIN,Align.CENTER,Align.MAX)).moved(Location((18.87,0,19.9))).rotate(Axis.Z,th)
    iv = interference({"catchproj":catchbelow,"h24":h24})
    vol=list(iv.values())[0] if isinstance(iv,dict) else iv
    print("  catch prism below flange top: common with h24", vol.measured if hasattr(vol,'measured') else vol, " prism vol", round(catchbelow.volume,3))
# H22 probe deck (H22 frame): x +-22, y +-15, z -7.7..0; bore r 7.05; slits y+-1.15 to x+-11.6 at top tapering 43.4 deg
deck = Box(44,30,7.7,align=(Align.CENTER,Align.CENTER,Align.MAX))
deck -= Cylinder(7.05,20)
a=math.radians(43.42)
for s in (1,-1):
    # slit profile in XZ: from x=0 to x_top at z=0, end line going down-inward at angle a
    xt=11.6; d=7.7
    pts=[(0,0.1),(s*(xt+0.1/math.tan(a)),0.1),(s*(xt-d/math.tan(a)),-d-0.1),(0,-d-0.1)]
    sk = Polygon(*pts, align=None)
    sl = extrude(Plane.XZ*sk, amount=1.15, both=True)
    deck -= sl
cl(deck,h22,"probe deck (spec slits) vs H22 (contact expected at flange)")
below = h22 & Box(100,100,40,align=(Align.CENTER,Align.CENTER,Align.MAX)).moved(Location((0,0,-0.001)))
cl(deck,below,"probe deck vs H22 below z=-0.001")
g = h22 & Box(10,10,10,align=(Align.MIN,Align.CENTER,Align.MAX)).moved(Location((7.2,0,-0.001)))
cl(deck,g,"probe deck vs +X gusset below z0")
