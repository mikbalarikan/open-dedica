"""RV02 static assembly rows: U-03a, REQ-01 offsets, REQ-02, REQ-03, REQ-05, REQ-06, REQ-07."""
import json, sys, math
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from rv_pose import *
from build123d import Box, Cylinder, Edge, Vector
from tools.core.validity import validity
from tools.core.boolean import common_volume
from tools.measure import clearance, envelope, bore_census, locate_bore, radial_extent
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN, TopAbs_OUT
OUT = W / "reviews/RV02_work"
R = {}
rig = load_rig()
H, G04, G10, info, idx = identify()
R["ident"] = {"order(housing,g04,g10)": idx, "info": [(i, e, v) for i, e, v in info]}
R["pose_axes"] = check_pose_axes()
h, g4, g10 = place(H), place(G04), place(G10)
R["validity"] = {n: {k: v.measured for k, v in validity(s).items()} for n, s in (("housing", h), ("g04", g4), ("g10", g10))}
R["env"] = {n: {k: round(v.measured, 4) for k, v in envelope(s).items()} for n, s in (("housing", h), ("g04", g4), ("g10", g10))}
def cl(a, b):
    r = clearance(a, b); return {"mm": r.measured, "at": r.at, "on_b": r.detail.get("on_b"), "inside": r.detail.get("inside"), "status": r.status, "reason": r.reason}
def cv(a, b):
    r = common_volume(a, b); return {"mm3": r.measured, "status": r.status, "reason": r.reason}
R["U03a"] = {"seat_clearance": cl(rig, h), "int_housing": cv(rig, h), "int_g04": cv(rig, g4), "int_g10": cv(rig, g10),
             "cl_g04": cl(rig, g4), "cl_g10": cl(rig, g10)}
below = rig & Box(400, 134.9 + 10, 200, align=None).moved(Location((0, (134.9 - 10) / 2 - 0.0, 0)))
# simpler: rig material below y 134.9
below = rig & (Location((0, (134.9 - 10) / 2, 0)) * Box(400, 134.9 + 10, 200))
R["U03a"]["cl_housing_elsewhere_below_134.9"] = cl(below, h)
plate = rig & (Location((0, 147.5, 0)) * Box(400, 25.0, 200))
R["U03a"]["cl_housing_plate_only"] = cl(plate, h)
# REQ-01: posed insert bores vs rig hole axes
hb = bore_census(h)
ins = [b for b in hb.detail["bores"] if abs(b["diameter"] - 4.0) < 0.01]
rb = bore_census(rig)
off = []
for b in ins:
    s = np.array(b["start"]); e = np.array(b["end"])
    loc = locate_bore(rb, tuple(((s + e) / 2 * np.array([1, 0, 1]) + np.array([0, 137.5, 0])).tolist()), (0, 1, 0))
    # axis distance between the two parallel axes
    hole = [x for x in rb.detail["bores"] if abs(x["diameter"] - 3.4) < 0.01 and np.hypot(x["start"][0] - s[0], x["start"][2] - s[2]) < 2]
    d = float(np.hypot(hole[0]["start"][0] - s[0], hole[0]["start"][2] - s[2])) if hole else None
    off.append({"insert": b["start"], "insert_end": b["end"], "dia": b["diameter"], "axis_offset": d,
                "hole_dia": loc["diameter"].measured, "hole_start": loc["diameter"].detail["start"], "hole_end": loc["diameter"].detail["end"]})
R["REQ01_inserts"] = off
# pair-B holes (3.8) on the posed housing
pb = [b for b in hb.detail["bores"] if abs(b["diameter"] - 3.8) < 0.02]
R["pairB_bores"] = pb
pbd = []
for b in pb:
    x, z = b["start"][0], b["start"][2]
    line = Edge.make_line((x, 135.0, z), (x, 160.0, z))
    pbd.append({"axis": (x, z), "r": math.hypot(x, z), "to_rig": cl(rig, line)})
R["REQ03_pairB"] = pbd
# window: flank planes, apex
R["REQ03_window"] = {k: v.measured for k, v in locate_bore(rb, (0, 147.5, 0), (0, 1, 0)).items()}
ap = []
for y in (135.5, 147.5, 159.5):
    r = radial_extent(rig, (0, y, 0), (0, 1, 0), (0, 0, 1), 0.0, 0.0, side="inner", r_min=0.0, r_max=59.0)
    ap.append({"y": y, "inner_r_along_+Z": r.measured, "status": r.status, "reason": r.reason})
R["REQ03_apex_radial"] = ap
# REQ-03 OD-G04 hub tube to rig: overall G04 clearance (covers the tube)
# REQ-02 grid classifier over x, z +-50 off the window and holes
cls_in = BRepClass3d_SolidClassifier(rig.wrapped); bad = 0; n = 0
for x in np.arange(-49.5, 50.0, 1.0):
    for z in np.arange(-49.5, 50.0, 1.0):
        rr = math.hypot(x, z)
        if rr < 31 or (abs(x) < 31 and 0 < z < 44): continue
        if any(math.hypot(x - sx, z - sz) < 2.0 for sx in (-44, 44) for sz in (-44, 44)): continue
        n += 1
        cls_in.Perform(gp_Pnt(x, 135.002, z), 1e-6); a = cls_in.State()
        cls_in.Perform(gp_Pnt(x, 134.998, z), 1e-6); b = cls_in.State()
        if not (a == TopAbs_IN and b == TopAbs_OUT): bad += 1
R["REQ02_grid"] = {"points": n, "bad": bad}
# REQ-05
R["REQ05"] = {"g10_min_y": R["env"]["g10"]["min_y"], "headroom": R["env"]["g10"]["min_y"] - 10.0}
# REQ-06, REQ-07 probes
def probe(x, z, r, y0, y1):
    return Location((x, (y0 + y1) / 2, z)) * Location((0, 0, 0), (1, 0, 0), -90) * Cylinder(r, y1 - y0)
R["REQ06"] = {f"({x},{z})": cv(rig, probe(x, z, 4.0, 10.0, 300.0)) for x in (-105, 105) for z in (-40, 40)}
R["REQ07"] = {f"({x},{z})": cv(rig, probe(x, z, 3.0, 160.0, 300.0)) for x in (-44, 44) for z in (-44, 44)}
R["REQ07_cl"] = {f"({x},{z})": cl(rig, probe(x, z, 3.0, 160.0, 300.0)) for x in (44,) for z in (44,)}
# handle direction at locked pose
(OUT / "asm_static.json").write_text(json.dumps(R, indent=1, default=str))
print(json.dumps(R, indent=1, default=str))
