import sys, time, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.measure import min_wall, min_wall_wide, overhang_census, flat_ceiling_spans, feature_census
from tools.core import validity
from tools.result import gate
L = lid(); out = {}; t = time.time()
def g(gid, r, op, lim, band):
    G = gate(gid, r, op, lim, band=band); return (G.status, G.measured, G.required, G.at)
which = sys.argv[1]
fill = ycyl(65, -60, 3.30, 218.0, 250.0) + ycyl(65, -210, 3.30, 218.0, 250.0) + ycyl(90, -293, 3.30, 218.0, 250.0) + ycyl(-90, -293, 3.30, 218.0, 250.0)
if which == "refill":
    R = L + fill
    out["refill_valid"] = {k: v.measured for k, v in validity(R).items()}
    oh = overhang_census(R, build_dir=(0, -1, 0), spacing=0.7)
    out["D-03a_refilled"] = g("D-03a", oh, ">=", 45.0, 0.001); out["oh_detail"] = oh.detail
    fs = flat_ceiling_spans(R, build_dir=(0, -1, 0), max_span=5.0, spacing=0.7)
    out["D-03b_refilled"] = g("D-03b", fs, "<=", 5.0, 0.005); out["fs_detail"] = fs.detail
elif which == "mut_print":
    M = (L + fill) - box(-10, 10, 248, 251, -150, -130)
    oh = overhang_census(M, build_dir=(0, -1, 0), spacing=0.7)
    out["ctl_overhang"] = ("counterbores refilled + 20x20x2 pocket from the top face", g("D-03a", oh, ">=", 45.0, 0.001))
    fs = flat_ceiling_spans(M, build_dir=(0, -1, 0), max_span=5.0, spacing=0.7)
    out["ctl_flat"] = ("same mutant", g("D-03b", fs, "<=", 5.0, 0.005))
elif which == "mut_wall":
    M = L - box(116.9, 118.5, 216, 246, -10, 10)
    mw = min_wall(M, spacing=0.7)
    out["ctl_min_wall"] = ("+x skirt thinned to 1.5 over z -10..10", g("D-01b", mw, ">=", 2.0, 0.005))
    ww = min_wall_wide(M, spacing=0.7)
    out["ctl_min_wall_wide"] = ("same mutant", g("U-06", ww, ">=", 2.0, 0.005))
elif which == "mut_census":
    M = L - ycyl(48, 30, 5.5, 209, 247)
    fc = feature_census(M)
    out["ctl_census_pad"] = ("pad (48,30) removed flush with the skin underside", g("U-05", fc["convex_cylinders"], "==", 10, 0), fc["cylinder_faces"].measured)
out["t"] = time.time() - t
dump(f"m6_{which}.json", out)
print(json.dumps({k: v for k, v in out.items() if "detail" not in k}, default=str))
