from common import *
from tools.measure import radial_profile
s, ss = part(); P = Solid(ss[0])
out = {}
for k, (x, y, a0) in {"L": (-91.0555, 153.2349, 104.0), "R": (-90.9987, 127.2515, 258.0)}.items():
    angs = [a0 - 3 + 0.05 * i for i in range(121)]
    pr = radial_profile(P, (x, y, 85.485), (0, 0, 1), (1, 0, 0), angs, (0.0, 6.0), margin=(0.0, 0.0), z_step=0.1, side="outer", r_min=2.0, r_max=7.0)
    mn = pr["min"]
    out[k] = {"min_r": mn.measured, "wall": mn.measured - 2.0, "at": mn.at, "angle": mn.detail["angle_deg"], "z": mn.detail["z"], "status": mn.status}
print(out); dump("s09_j05.json", out)
