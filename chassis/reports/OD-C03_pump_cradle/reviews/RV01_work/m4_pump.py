import json
import numpy as np
from pathlib import Path
from build123d import Cylinder, Pos, Rot, Box
from tools.core import read_step, common_volume
from tools.measure import radial_extent, mass_properties, clearance, envelope
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
p = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
pump = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
mp = mass_properties(pump, 1000)
print("pump COM", [ (k, round(v.measured,3)) for k,v in mp.items()])
# pump volume in slabs along z
for z0 in range(-70, 60, 10):
    b = Pos(0,0,z0+5)*Box(200,200,10)
    print(z0, z0+10, round(common_volume(pump, b).measured,1))
# pump outer radius on the -Y side (theta 180..360) over the tie bands
O,A,R=(0,0,0),(0,0,1),(1,0,0)
for zc in (18.0, 28.0):
    worst=None
    for z in np.arange(zc-2.4, zc+2.41, 0.4):
        for a in range(180, 361, 5):
            r = radial_extent(pump, O,A,R, float(a), float(z), side="outer")
            if r.ok and (worst is None or r.measured>worst[0]): worst=(r.measured, a, round(float(z),2))
    print("tie band", zc, "max outer radius of pump over theta 180..360:", worst)
    for a in (200, 225, 250, 270, 290, 315, 340):
        r = radial_extent(pump, O,A,R, float(a), zc, side="outer")
        print("  ", a, r.measured, r.status)
# driver access: cylinder r 2.75 along Y from y=-80 to y=36.99 over each hole
for x in (-34, 34):
    for z in (-4, 37):
        c = Pos(x, (-80+36.99)/2, z) * Rot(90,0,0) * Cylinder(2.75, 36.99+80)
        print("driver", x, z, "pump clr", round(clearance(c, pump).measured,3), "cradle clr", round(clearance(c, p).measured,3))
