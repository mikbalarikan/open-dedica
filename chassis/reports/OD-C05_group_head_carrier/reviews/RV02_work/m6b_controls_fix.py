import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from faces_lib import listing, vz
from build123d import Solid, Pos, Box, Cylinder, export_step
from tools.core.step import compare_step, step_roundtrip, labels
from tools.core.shapes import faces as F
from tools.measure import clearance
import numpy as np
MD = W / "mutants"
s = Solid(solids(read_step(STEP))[0])
g01 = Solid(solids(read_step(G01))[0])
R = {}
# U-04: my own round trip of the re-read body, labelled as delivered
fresh = Solid(s.wrapped); fresh.label = "od_c05_carrier"
R["U04_roundtrip"] = step_roundtrip(fresh, OUT / "rt_carrier.step", timestamp="2026-09-30T00:00:00")
R["U04_file_vs_reread"] = compare_step(fresh, STEP)
# compare_step control: counterbore filled (volume changes), labelled like the part
mD = Solid(solids(s + Pos(44, -44, -28.94) * Cylinder(3.25, 2.0) - Pos(44, -44, -26.44) * Cylinder(1.7, 5.0))[0]); mD.label = "od_c05_carrier"
R["C_compare_cbfilled_vs_file"] = compare_step(mD, STEP)
# bridge span as the largest horizontal extent of the flat ceiling (upper bound)
mH = Solid(solids(s - Pos(0, -55, 70) * Box(20, 20, 20))[0])
out = []
for r in listing(mH):
    if r.get("down") and r["angle"] is not None and r["angle"] < 1.0 and abs(r["centre"][2] + 29.94) > 1e-6 and not (abs(r["area"] - 24.104) < 0.01):
        pts = np.array(vz(F(mH)[r["i"]])); ext = pts.max(0) - pts.min(0)
        out.append({"centre": r["centre"], "extent_xy": ext[:2].tolist()})
R["H_flats"] = out
# REQ-08 back control: bump on the front wall face at the housing flange height
mJ4 = Solid(solids(s + Pos(0, -51.75, -22.44) * Box(40, 0.5, 4))[0]); export_step(mJ4, str(MD / "J4b_frontwall_bump_y-51.5_flange.step"))
big = 1000
back = Pos(0, -52 - big/2 + 1.0, -24.94 + big/2) * Box(big, big, big)
R["J4b_req08_back"] = clearance(g01, mJ4 & back)
dump("m6b_controls", R)
for k, v in R.items():
    if isinstance(v, dict) and all(hasattr(x, "measured") for x in v.values()): print(k, {kk: (vv.measured, vv.reason[:50]) for kk, vv in v.items()})
    elif hasattr(v, "measured"): print(k, v.measured, v.status, v.at)
    else: print(k, v)
