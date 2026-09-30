"""RV01: controls for min_wall_mesh and the spacer-in-casting classifier probe."""
import json, math
from pathlib import Path
import numpy as np
from build123d import Solid, Box, Cylinder, Pos, Align
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN
from tools.core import read_step, write_stl
from tools.core.shapes import solids
from tools.measure import min_wall_mesh
from tools.result import gate
W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount"); OUT = W / "reviews/RV01_work"
m = Solid(solids(read_step(W / "02_STEP_STL/od_c04_mount_C1_v01.step"))[0])
pocket = m - Pos(-10, -30, -17.5) * Box(20, 20, 5.0, align=(Align.MIN, Align.MIN, Align.MIN))
write_stl(pocket, OUT / "mutants/mut_pocket.stl", tolerance=0.01, angular_tolerance=0.23097)
g = gate("D-01b.mesh", min_wall_mesh(OUT / "mutants/mut_pocket.stl"), ">=", 2.0 - 0.01, band=0.005)
H = solids(read_step(W / "00_Spec/inputs/OD-H11_thermoblock.step"))[0]
cl = BRepClass3d_SolidClassifier(H)
def probe_body(cx, cy, z0, z1):
    hits = n = 0
    for z in np.linspace(z0 + 0.02, z1 - 0.02, 60):
        for r in (2.0, 2.75, 3.5):
            for a in range(0, 360, 10):
                cl.Perform(gp_Pnt(cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a)), z), 1e-6); n += 1
                hits += cl.State() == TopAbs_IN
    return hits, n
h, n = probe_body(-19.62, 20.18, -10.1, 0.5)     # S1 spacer 0.5 longer, into the base face
out = {"min_wall_mesh_pocket": (g.measured, g.status), "probe_S1_long": (h, n, "FAIL" if h > 0 else "PASS")}
(OUT / "m8.json").write_text(json.dumps(out, indent=1, default=str)); print(out)
