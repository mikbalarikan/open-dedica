import sys, json
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_work")
from common import *
from build123d import Axis, Location, Shell, Solid, Face
from tools.result import gate
from tools.core import validity, write_stl, compare_step, common_volume, read_step
from tools.core.shapes import faces
from tools.measure import (envelope, feature_census, bore_census, min_wall, min_wall_wide, overhang_census,
    flat_ceiling_spans, clearance, interference, radial_extent, radial_profile, mesh_census, mesh_deviation)
A = half(); P = c11()
keep = box(80, 110, 30.4, 50, -310, -280)   # the half's side of the split plane
rows = []
def ctl(check, mutant, g):
    print(f"{check:28s} {g.status:12s} measured {g.measured} ({mutant})"); rows.append({"check": check, "mutant": mutant, "got": "FAIL" if g.status == "FAIL" else g.status, "measured": g.measured})
# validity: remove the collar-top face -> open shell
fs = [f for f in A.faces() if abs(f.center().Z + 291.0) < 1e-6 and abs(f.normal_at().Z) > 0.99]
open_shell = Shell([f for f in A.faces() if not any(f.is_same(x) for x in fs)])
v = validity(open_shell)
ctl("validity (naked_edges)", "collar-top face removed (open shell)", gate("U-01", v["naked_edges"], "==", 0, band=0))
# envelope: flange resized to Ø21.2
M1 = one(A.fuse(cyl(95, 30, 10.6, -304, -302) & keep))
ctl("envelope", "flange resized Ø20.0 -> Ø21.2", gate("U-02", envelope(M1)["size_x"], "in", (19.9, 20.1), band=0.005))
# feature_census: groove filled (groove floor and flank removed)
M2 = one(A.fuse(ring(95, 30, 5.0, 5.65, -298.8, -292.734) & keep).clean())
fc = feature_census(M2)
ctl("feature_census", "tie groove filled to Ø11.3 (groove floor, flank removed)", gate("U-05", fc["cylinder_faces"], "==", 5, band=0))
# bore_census: a Ø3 through-hole added in the flange
M3 = one(A.cut(cyl(95, 37.5, 1.5, -310, -301)))
ctl("bore_census", "Ø3 through-hole drilled in the flange at (95, 37.5)", gate("J-06", bore_census(M3), "==", 0, band=0))
# radial_extent / radial_profile: bore opened to r 3.60
M4 = one(A.cut(cyl(95, 30, 3.6, -310, -280)))
rp = radial_profile(M4, (95,30,0), (0,0,1), (1,0,0), list(range(10,171,10)), (-303.45, -291.53), margin=0.0, side="inner")
ctl("radial_profile (inner)", "bore radius 3.50 -> 3.60", gate("REQ-02", rp["max"], "in", (3.45, 3.55), band=0.005))
re = radial_extent(M4, (95,30,0), (0,0,1), (1,0,0), 90, -295.0, side="inner")
ctl("radial_extent (squeeze)", "bore r 3.60: squeeze of the closed pose", gate("U-03", type(re)("squeeze", 3.5 - (re.measured - 0.4), "mm"), "in", (0.33, 0.47), band=0.005))
# min_wall: groove deepened to Ø9.8 (floor wall 1.40)
M5 = one(A.cut(ring(95, 30, 4.9, 6.0, -298.8, -293.6) & keep))
mw = min_wall(M5)
ctl("min_wall", "groove floor thinned to 1.40 (Ø9.8)", gate("D-01b", mw, ">=", 1.6, band=0.005))
ctl("min_wall_wide", "same mutant, 45° reading", gate("U-06", min_wall_wide(M5), ">=", 1.6, band=0.005))
# overhang: a flat ledge ring on the collar's top, overhanging the collar
M6 = one(A.fuse(ring(95, 30, 4.5, 7.5, -291.5, -291.0) & keep))
ctl("overhang_census", "collar top ledge to Ø15 (flat underside)", gate("D-03a", overhang_census(M6, (0,0,1)), ">=", 45, band=0.001))
# flat_ceiling_spans: a 11 mm bridge on two posts over the flange
M7 = one(A.fuse(box(89.5, 100.5, 37, 38, -296, -295)).fuse(box(89.5, 90.5, 37, 38, -302, -295)).fuse(box(99.5, 100.5, 37, 38, -302, -295)))
ctl("flat_ceiling_spans", "11 mm bridge on two posts above the flange", gate("D-03b", flat_ceiling_spans(M7, (0,0,1), max_span=5.0), "<=", 5.0, band=0.005))
# clearance: half relocated 0.5 mm along +X
M8 = A.moved(Location((0.5, 0, 0)))
ctl("clearance", "half moved 0.5 along +X (neck into the hole wall)", gate("D-04d", clearance(M8 & box(0,200,0,100,-301.9,-280), P), ">=", 0.30, band=0.005))
ctl("clearance (contact =0)", "half moved 0.5 along -Z off the wall", gate("U-03", clearance(A.moved(Location((0,0,-0.5))), P), "==", 0.0, band=0.005))
# interference: same relocation
ctl("interference", "half moved 0.5 along +X", gate("U-03", interference({"h": M8, "C11": P})["h|C11"], "<=", 0, band=0.001))
# mesh sagitta: STL at 0.1 mm
w = write_stl(A, W/"reviews/RV01_work/mutant_coarse.stl", tolerance=0.1, angular_tolerance=0.5)
ctl("mesh_sagitta (write_stl)", "STL written at 0.1 mm / 0.5 rad", gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=0.005))
ctl("mesh_deviation", "same coarse STL against the B-rep", gate("U-07", mesh_deviation(W/"reviews/RV01_work/mutant_coarse.stl", A), "<=", 0.01, band=0.005))
# mesh_census: STL with 10 triangles dropped
import struct
raw = open(W/"02_STEP_STL/od_c14_grommet_half_C1_v01.stl", "rb").read(); n = struct.unpack("<I", raw[80:84])[0]
cut = raw[:80] + struct.pack("<I", n-10) + raw[84:84+50*(n-10)]
open(W/"reviews/RV01_work/mutant_holed.stl", "wb").write(cut)
ctl("mesh_census", "delivered STL with its last 10 triangles removed", gate("U-07", mesh_census(W/"reviews/RV01_work/mutant_holed.stl")["naked_edges"], "==", 0, band=0))
# compare_step: a degraded shape compared with the delivered STEP
cs = compare_step(M4, STEP)
ctl("compare_step", "bore r 3.60 compared with the delivered file", gate("U-04", cs["volume_delta"], "<=", 0.0, band=0.001))
json.dump(rows, open(W/"reviews/RV01_work/m5_controls.json", "w"), indent=1, default=str)
