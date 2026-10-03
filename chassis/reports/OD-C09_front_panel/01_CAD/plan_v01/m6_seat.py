"""D1: map the board front surface about each screw hole (machine frame, first hit along -Z)."""
import sys, math; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from poses import BOARD, load
from build123d import Solid
from tools.core import solids
from OCP.IntCurvesFace import IntCurvesFace_ShapeIntersector
from OCP.gp import gp_Lin, gp_Pnt, gp_Dir
e02 = Solid(solids(load("OD-E02_control_board.step", BOARD))[0])
isect = IntCurvesFace_ShapeIntersector(); isect.Load(e02.wrapped, 1e-6)
def hit(x, y):
    isect.Perform(gp_Lin(gp_Pnt(x, y, 110.0), gp_Dir(0, 0, -1)), 0, 200)
    return max((isect.Pnt(i).Z() for i in range(1, isect.NbPnt()+1)), default=None)
for name, (cx, cy) in {"L": (-91.055, 153.235), "R": (-90.999, 127.251)}.items():
    print("==", name, "rows: angle (deg, 0 = +X, 90 = +Y); cols r")
    rs = [3.6, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0]
    print("ang " + " ".join(f"{r:6.1f}" for r in rs))
    for a in range(0, 360, 20):
        row = [hit(cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a))) for r in rs]
        print(f"{a:3d} " + " ".join("  None" if v is None else f"{v:6.2f}" for v in row))
