import sys, time, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.core import validity, common_volume, write_stl, write_step
from tools.core.step import compare_step
from tools.core.shapes import solids
from tools.measure import envelope, feature_census, bore_census, locate_bore, clearance, engaged_area, radial_extent, mesh_census, mesh_deviation
from build123d import Pos, Compound
import numpy as np, trimesh
from tools.result import gate
L = lid(); out = {}
CROP = box(-125, 125, 200, 300, -310, 105)
C02 = placed("C02") & CROP; C05 = placed("C05") & CROP; C11 = placed("C11") & CROP
def g(gid, r, op, lim, band):
    G = gate(gid, r, op, lim, band=band); return (G.status, G.measured, G.required)
# validity: two solids
m = Compound([L, box(0, 10, 260, 270, 0, 10)])
out["validity"] = ("lid + loose 10 mm cube above the skin", g("U-01", validity(m)["solid_count"], "==", 1, 0))
# envelope: skirt bulge to x 121
m = L + box(119, 121, 220, 240, -20, 20)
out["envelope"] = ("+x skirt bulged 1.0 out (x 121) over z -20..20", g("U-02", envelope(m)["size_x"], "in", (239.9, 240.1), 0.005))
# bore family: hole (65,-60) moved 0.5 in x
m = (L + ycyl(65, -60, 3.3, 214.9, 218.0)) - ycyl(65.5, -60, 1.7, 214, 219)
bc = bore_census(m)
lb = locate_bore(bc, (65, 216.5, -60), (0, 1, 0))
out["bore_relocate"] = ("Ø3.4 hole at (65,-60) moved +0.5 in x", g("REQ-03", lb["offset"], "<=", 0.10, 0.005))
fc = feature_census(L + ycyl(90, -293, 1.75, 214.9, 218.1))
out["feature_census_remove"] = ("Ø3.4 hole at (90,-293) filled", g("U-05", fc["bores"], "==", 8, 0))
m = L - ycyl(48, 30, 5.1, 209, 246.5)
fc2 = feature_census(m)
out["feature_census_remove_pad"] = ("pad (48,30) removed", g("U-05", fc2["convex_cylinders"], "==", 10, 0))
# radial_extent: skirt thinned to 2.5 at z 0
m = L - box(116.9, 117.5, 216, 246, -10, 10)
o = radial_extent(m, (0, 0, 0), (0, 1, 0), (1, 0, 0), 0, 230.0, side="outer", r_min=110, r_max=130)
i = radial_extent(m, (0, 0, 0), (0, 1, 0), (1, 0, 0), 0, 230.0, side="inner", r_min=110, r_max=130)
from tools.result import Result
th = Result("skirt_t", o.measured - i.measured, "mm")
out["radial_extent"] = ("+x skirt thinned 0.5 from inside at z 0", g("REQ-02", th, "in", (2.9, 3.1), 0.005))
# clearance + common_volume: lid lowered 0.2
m = Pos(0, -0.2, 0) * L
out["clearance_pads"] = ("lid lowered 0.2", g("REQ-05", clearance(m, C05), "in", (0.45, 0.55), 0.005))
out["common_volume_seat"] = ("lid lowered 0.2", g("U-03", common_volume(m, C02), "<=", 0.0, 0.001))
# rear rib lowered onto ledge: clearance_away and contact area outside
m = L + box(92.5, 95.5, 215, 216.01, -299, -293.5)
cols = ycyl(65, -60, 6.05, 214, 251) + ycyl(65, -210, 6.05, 214, 251) + ycyl(90, -293, 6.05, 214, 251) + ycyl(-90, -293, 6.05, 214, 251)
away = m - cols - box(-125, 125, 200, 251, -310, -301.95) - box(109.95, 125, 200, 251, -310, -294.95) - box(-125, -109.95, 200, 251, -310, -294.95)
out["clearance_away"] = ("rear rib (x 92.5..95.5) bottom lowered 1.0 onto OD-C11's ledge", g("U-03", clearance(away, C11), ">=", 0.5, 0.005))
ea = engaged_area(m, C11, (0, -1, 0), 0.01)
outside = Result("outside_area", ea.measured - (2 * 100.53096491477933 + 2 * 5.906631992666668), "mm2")
out["engaged_area"] = ("same mutant: contact area outside seats and corners", g("U-03", outside, "<=", 0.0, 0.001))
# descent: pad extended 1 mm down
m = L + ycyl(48, 30, 5, 209.5, 211)
desc = max(common_volume(Pos(0, 40 - 2 * k, 0) * m, C05).measured for k in range(21))
out["descent"] = ("pad (48,30) extended 1.0 down", g("U-03", Result("cv", desc, "mm3"), "<=", 0.0, 0.001))
# REQ-06 box: a boss inside the headroom box
m = L + box(-5, 5, 240, 247.5, 0, 10)
out["req06"] = ("10x10x7 boss under the skin over the hub", g("REQ-06", common_volume(m, box(-42, 42, 200, 247, -70, 70)), "<=", 0.0, 0.001))
# compare_step: mutant vs delivered file
m = L - box(-5, 5, 249, 251, -5, 5)
cs = compare_step(m, JOB / "02_STEP_STL/od_c10_top_C1_v01.step")
out["compare_step"] = ("1 mm pocket in the top face vs the delivered STEP", g("U-04", cs["volume_delta"], "<=", 0.0, 0.001))
# mesh: STL with 20 triangles removed
mm = trimesh.load(JOB / "02_STEP_STL/od_c10_top_C1_v01.stl", process=False)
mm2 = trimesh.Trimesh(mm.vertices, mm.faces[20:], process=False); p = WORK / "mut_open.stl"; mm2.export(p)
out["mesh_census"] = ("delivered STL less 20 triangles", g("U-07", mesh_census(p)["naked_edges"], "==", 0, 0))
mm3 = mm.copy(); mm3.apply_translation((0.5, 0, 0)); p3 = WORK / "mut_shift.stl"; mm3.export(p3)
out["mesh_deviation"] = ("delivered STL shifted 0.5 in x", g("U-07", mesh_deviation(p3, L), "<=", 0.01, 0.005))
w = write_stl(L, WORK / "mut_coarse.stl", tolerance=0.1, angular_tolerance=0.5)
out["mesh_sagitta"] = ("lid meshed at 0.1 / 0.5 rad", g("U-07", w.checks["max_sagitta"], "<=", 0.01, 0.005))
dump("m5_controls.json", out)
for k, v in out.items(): print(k, v)
