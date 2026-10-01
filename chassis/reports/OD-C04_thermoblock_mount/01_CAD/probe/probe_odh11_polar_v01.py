"""D2 probe 5: in/out map of OD-H11 on a polar grid at z 20 (cross-check of the ray reads)."""
import math
from pathlib import Path
HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN
from tools.core import read_step
tb = read_step(WS / "00_Spec/inputs/OD-H11_thermoblock.step").solids()[0].wrapped
rs = [5, 10, 14, 16, 18, 20, 25, 30, 33, 34.5, 36, 38, 40, 45, 50]
for z in (20.0, 40.0):
    print("z", z, "r:", rs)
    for a in range(0, 360, 15):
        row = ""
        for r in rs:
            c = BRepClass3d_SolidClassifier(tb, gp_Pnt(r*math.cos(math.radians(a)), r*math.sin(math.radians(a)), z), 1e-6)
            row += "#" if c.State() == TopAbs_IN else "."
        print(f"{a:4d} {row}", flush=True)
