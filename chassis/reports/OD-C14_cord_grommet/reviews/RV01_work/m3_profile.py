import json, math, sys
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_work")
from common import *
from tools.measure import radial_extent, radial_profile
A = half(); O = (95, 30, 0); D = (0, 0, 1); X = (1, 0, 0)
angs = list(range(10, 171, 10))
out = {}
def prof(name, z0, z1, side="outer", r_min=0, r_max=None):
    # window inside the band, 0.05 off each end
    res = radial_profile(A, O, D, X, angs, (z0 + 0.05, z1 - 0.05), margin=0.0, z_step=0.1, side=side, r_min=r_min, r_max=r_max)
    mx, mn = res["max"], res["min"]
    out[name] = {"max": mx.measured, "min": mn.measured, "max_at": mx.at, "min_at": mn.at, "status": [mx.status, mn.status], "reason": mx.reason}
    print(name, mx.measured, mn.measured, mx.status, mn.status, mx.at, mx.reason[:100])
prof("flange", -304.0 + 0.6, -302.0)          # above the bed-side chamfer zone... outer reading unaffected
prof("neck", -302.0, -298.8)
prof("groove", -298.8, -293.6)
prof("collar", -292.734, -291.0)
prof("bore", -303.5, -291.5, side="inner")
# flank angle: two outer readings across the flank
z1, z2 = -293.4, -292.9
r1 = radial_extent(A, O, D, X, 90, z1).measured; r2 = radial_extent(A, O, D, X, 90, z2).measured
ang = math.degrees(math.atan2(z2 - z1, r2 - r1)); print("flank r", r1, r2, "angle from horizontal", ang); out["flank_deg"] = ang
# flank end z: r reaches 5.65 at z: r1 + (z - z1)*tan... compute from slope
slope = (r2 - r1) / (z2 - z1); zend = z1 + (5.65 - r1) / slope; zstart = z1 + (5.15 - r1) / slope
print("flank z", zstart, zend); out["flank_z"] = [zstart, zend]
# chamfers: inner radius near each end
for z in (-303.999, -303.75, -303.5001, -291.4999, -291.25, -291.001):
    r = radial_extent(A, O, D, X, 90, z, side="inner"); print("inner r at", z, r.measured); out[f"inner_{z}"] = r.measured
# outside chamfer radial and axial: radius at bed face and where it meets 3.5
# radial step readings at band ends (z ends)
for z in (-302.05, -301.95, -298.85, -298.75, -293.65, -293.55, -292.78, -292.69, -291.05):
    print("outer r at", z, radial_extent(A, O, D, X, 90, z).measured)
json.dump(out, open(W/"reviews/RV01_work/m3_profile.json", "w"), indent=1, default=str)
