"""RV02 motion: U-03b offer-up, REQ-04a phi sweep, REQ-04b insertion, the lift, and a joint phi x dy grid."""
import json, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from rv_pose import *
from tools.core.boolean import common_volume
from tools.measure import clearance, envelope
OUT = W / "reviews/RV02_work"
rig = load_rig(); H, G04, G10, _, _ = identify()
def cl(a, b):
    r = clearance(a, b); return (r.measured, r.at, r.detail.get("inside"), r.status)
R = {}
t = time.time()
u = []
for dy in np.arange(0.0, -30.0001, -1.0):
    h, g4, g10 = place(H, dy=dy), place(G04, dy=dy), place(G10, dy=dy)
    a, b = common_volume(rig, h), common_volume(rig, g4)
    c = cl(rig, g10)
    u.append({"dy": float(dy), "housing_mm3": a.measured, "hs": a.status, "g04_mm3": b.measured, "gs": b.status, "g10_cl": c[0], "g10_inside": c[2], "at": c[1]})
R["U03b"] = u; print("U03b done", time.time() - t, max(x["housing_mm3"] or 0 for x in u), max(x["g04_mm3"] or 0 for x in u), min(x["g10_cl"] for x in u), flush=True)
a4 = []
for phi in np.arange(-60.0, 15.0001, 1.0):
    g = place(G10, phi=phi); c = cl(rig, g)
    a4.append({"phi": float(phi), "cl": c[0], "at": c[1], "inside": c[2], "max_x": envelope(g)["max_x"].measured})
R["REQ04a"] = a4; m = min(a4, key=lambda x: x["cl"]); print("04a", m, flush=True)
print("handle max_x at -10/0/+10:", [x["max_x"] for x in a4 if x["phi"] in (-10.0, 0.0, 10.0)], flush=True)
b4 = []
for dz in np.arange(0.0, 200.0001, 2.5):
    g = place(G10, phi=-50.0, dy=-15.0, dz=dz); c = cl(rig, g)
    b4.append({"dz": float(dz), "cl": c[0], "at": c[1], "inside": c[2]})
R["REQ04b"] = b4; print("04b", min(b4, key=lambda x: x["cl"]), flush=True)
lift = []
for dy in np.arange(-15.0, 0.0001, 1.0):
    g = place(G10, phi=-50.0, dy=dy); c = cl(rig, g)
    lift.append({"dy": float(dy), "cl": c[0], "at": c[1], "inside": c[2]})
R["lift"] = lift; print("lift", min(lift, key=lambda x: x["cl"]), flush=True)
grid = []
for phi in np.arange(-60.0, 15.0001, 5.0):
    for dy in np.arange(-15.0, 0.0001, 1.5):
        g = place(G10, phi=phi, dy=dy); c = cl(rig, g)
        grid.append({"phi": float(phi), "dy": float(dy), "cl": c[0], "at": c[1], "inside": c[2]})
R["grid_phi_dy"] = grid; print("grid", min(grid, key=lambda x: x["cl"]), len(grid), time.time() - t, flush=True)
(OUT / "asm_motion.json").write_text(json.dumps(R, indent=1, default=str))
