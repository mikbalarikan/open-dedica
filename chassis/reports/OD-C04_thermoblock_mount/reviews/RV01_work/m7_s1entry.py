"""RV01: S1 screw entry, z 0 .. 3.2 on the S1 axis of OD-H11: which angles and radii hold casting material."""
import json, math
from pathlib import Path
import numpy as np
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN
from tools.core import read_step
from tools.core.shapes import solids
from tools.measure import radial_extent
W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount"); OUT = W / "reviews/RV01_work"
H = read_step(W / "00_Spec/inputs/OD-H11_thermoblock.step")
cl = BRepClass3d_SolidClassifier(solids(H)[0])
cx, cy = -19.62, 20.18
rows = {}
for z in (0.05, 0.5, 1.0, 1.5, 2.0, 2.5, 2.9, 3.1, 3.5, 5.0):
    row = {}
    for rr in (0.0, 0.5, 1.0, 1.5, 1.75, 1.8, 2.0, 2.5, 3.0, 3.5):
        angs = []
        for a in range(0, 360, 5):
            cl.Perform(gp_Pnt(cx + rr*math.cos(math.radians(a)), cy + rr*math.sin(math.radians(a)), z), 1e-6)
            if cl.State() == TopAbs_IN: angs.append(a)
        row[rr] = (len(angs), (min(angs), max(angs)) if angs else None)
    rows[z] = row
# innermost material radius about the S1 axis at a few angles and heights
ext = {}
for z in (0.5, 1.5, 2.5):
    for a in range(0, 360, 30):
        r = radial_extent(H, (cx, cy, 0), (0, 0, 1), (1, 0, 0), a, z, side="inner", r_min=0, r_max=None)
        ext[f"z{z}_a{a}"] = (None if r.measured is None else round(r.measured, 3), r.status, r.reason[:100])
res = {"classify": rows, "inner_radius": ext}
(OUT / "m7.json").write_text(json.dumps(res, indent=1, default=str))
for z, row in rows.items(): print(z, row)
for k, v in ext.items(): print(k, v)
