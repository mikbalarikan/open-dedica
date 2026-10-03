"""D1: why OD-G10 fails brep_valid; does common_volume run on it."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, load
from build123d import Box, Pos
from tools.core import solids, brep_valid, common_volume
from OCP.BRepCheck import BRepCheck_Analyzer
asm = load("od_g01_assembly_C1_v03.step", HOUSING)
g10 = solids(asm)[2]
r = brep_valid(g10); print(r.measured, r.reason, r.detail)
print("BRepCheck", BRepCheck_Analyzer(g10).IsValid())
b = Pos(50, 160, 95.5) * Box(20, 20, 3)
cv = common_volume(g10, b); print("common_volume", cv.status, cv.measured, cv.reason[:200])
