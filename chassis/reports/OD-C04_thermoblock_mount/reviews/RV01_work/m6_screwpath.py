"""RV01: OD-H11 screw holes against the mount bores, and the screw path (P2, P4)."""
import json, math
from pathlib import Path
import numpy as np
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN
from tools.core import read_step
from tools.core.shapes import solids
from tools.measure import bore_census, locate_bore
W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount"); OUT = W / "reviews/RV01_work"
H = read_step(W / "00_Spec/inputs/OD-H11_thermoblock.step")
bc = bore_census(H)
res = {"H_bores": [{k: b[k] for k in ("diameter", "axis_dir", "start", "end", "length", "through", "open_ends")} for b in bc.detail["bores"]]}
for n, p in (("S1", (-19.62, 20.18, 5.5)), ("S2", (25.01, 9.08, 30.4))):
    res[n] = {k: (r.measured, r.status, r.at) for k, r in locate_bore(bc, p, (0, 0, 1)).items()}
cl = BRepClass3d_SolidClassifier(solids(H)[0])
def path(cx, cy, z0, z1, r=1.75):
    hits = []
    for z in np.arange(z0, z1, 0.1):
        for rr in (0.0, r * 0.5, r):
            for a in range(0, 360, 15):
                cl.Perform(gp_Pnt(cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a)), z), 1e-6)
                if cl.State() == TopAbs_IN: hits.append(round(float(z), 2))
    return {"first_material_z": min(hits) if hits else None, "n": len(hits)}
res["S1_path_r1.75"] = path(-19.62, 20.18, -17.0, 9.0)
res["S2_path_r1.75"] = path(25.01, 9.08, -17.0, 34.0)
(OUT / "m6.json").write_text(json.dumps(res, indent=1, default=str)); print(json.dumps(res, indent=1, default=str))
