"""D1: Ø15 holes on the planned axes: wall-to-board gap, at the §2 pose and moved +2.5 in Z (Q1 a)."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import BOARD, load, place
from standin import panel
from build123d import Compound
from OCP.gp import gp_Trsf, gp_Vec
from tools.core import solids
from tools.measure import clearance
holes = [(-94.248, 166.514, 15.0), (-98.991, 139.901, 15.0), (-93.765, 113.426, 15.0)]
for dz in (0.0, 2.5):
    m = gp_Trsf(); m.SetTranslation(gp_Vec(0, 0, dz))
    e02 = solids(place(load("OD-E02_control_board.step", BOARD), m))[0]
    parts = panel(holes, [(-91.055, 153.235), (-90.999, 127.251)], (85.485 + dz, 85.485 + dz))
    r = clearance(parts["wall"], e02)
    print(f"dz {dz}: wall-board {r.measured:.3f} at {r.at}")
    for k in ("R3", "R5", "FL"):
        print("   ", k, round(clearance(parts[k], e02).measured, 3))
