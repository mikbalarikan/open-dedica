"""RV01: pass-through gap behind the wall: least distance from a d12 cylinder z -299..-277 on each hole axis
to the panel's material in front of the wall face (box z -299..-270 common with the panel), BRepExtrema."""
import json, sys
from build123d import Pos, Cylinder, Box, Location
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from tools.core import read_step
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
D = float(sys.argv[2]) if len(sys.argv) > 2 else 12.0
p = read_step(STEP)
box = Box(300, 300, 30).moved(Location((0, 100, -299.0 + 15)))
c = BRepAlgoAPI_Common(p.wrapped, box.wrapped); c.Build(); front = c.Shape()
out = {}
for (x, y) in [(95, 30), (-100, 30), (-84, 30)]:
    cyl = Pos(x, y, (-299 - 277) / 2) * Cylinder(D / 2, 22.0)
    d = BRepExtrema_DistShapeShape(cyl.wrapped, front); d.Perform()
    q1, q2 = d.PointOnShape1(1), d.PointOnShape2(1)
    out[f"gap_{x}"] = {"gap": d.Value(), "on_cyl": (q1.X(), q1.Y(), q1.Z()), "on_panel": (q2.X(), q2.Y(), q2.Z())}
    print(x, out[f"gap_{x}"])
json.dump(out, open(f"{W}/m7c_gaps_d{D}.json", "w"), indent=1, default=str)
