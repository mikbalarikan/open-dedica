"""D1: OD-G10 travel (REQ-05) against the planned panel and the posed OD-E02, clearance only
(OD-G10 fails brep_valid, so common_volume is INCONCLUSIVE on it)."""
import sys, math, time; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, BOARD, load, place
from standin import panel
from build123d import Solid, Compound
from OCP.gp import gp_Trsf, gp_Ax1, gp_Pnt, gp_Dir, gp_Vec
from tools.core import solids
from tools.measure import clearance
g10 = solids(load("od_g01_assembly_C1_v03.step", HOUSING))[2]
e02 = solids(load("OD-E02_control_board.step", BOARD))[0]
holes = [(-94.248, 166.514, 15.0), (-98.991, 139.901, 15.0), (-93.765, 113.426, 15.0)]
parts = panel(holes, [(-91.055, 153.235), (-90.999, 127.251)], (85.485, 85.485))
pan = Compound([p for p in parts.values()])
def pose(phi, dy=0.0, dz=0.0):
    t = gp_Trsf(); t.SetRotation(gp_Ax1(gp_Pnt(0, 0, 32.0), gp_Dir(0, 1, 0)), math.radians(phi))
    m = gp_Trsf(); m.SetTranslation(gp_Vec(0, dy, dz))
    return place(g10, m.Multiplied(t))
t0 = time.time()
print("(a) locked pose rotated by phi")
for phi in range(-55, 11, 5):
    g = pose(phi); a = clearance(pan, g); b = clearance(e02, g)
    print(f"  phi {phi:4d}: panel {a.measured:7.3f} at {a.at}  board {b.measured:7.3f}  ({time.time()-t0:.0f}s)")
print("(b) phi -50, lowered 15, axis z 32 -> 182")
for dz in range(0, 151, 5):
    g = pose(-50, -15.0, dz); a = clearance(pan, g); b = clearance(e02, g)
    print(f"  dz {dz:4d}: panel {a.measured:7.3f} inside {a.detail['inside']} at {a.at}  board {b.measured:7.3f}")
