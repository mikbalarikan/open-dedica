import json
from pathlib import Path
from build123d import Pos
from tools.core import read_step, common_volume
from tools.measure import envelope, clearance, interference
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
g01 = read_step(J / "00_Spec/inputs/OD-G01_housing_C1_v02.step")
asm = read_step(J / "02_STEP_STL/od_c05_assembly_C1_v01.step")
k = [c for c in asm.children if c.label == "od_g01_housing"][0]
car = [c for c in asm.children if c.label == "od_c05_carrier"][0]
e1 = {a: round(b.measured, 6) for a, b in envelope(g01).items()}; e2 = {a: round(b.measured, 6) for a, b in envelope(k).items()}
print("input", e1); print("asm  ", e2)
print("centroid in", g01.center(), "asm", k.center())
print("common in/asm", common_volume(g01, k).to_dict()["measured"], common_volume(g01, k).reason)
print("common in/in(shift 0.001)", common_volume(g01, Pos(0,0,0.001)*g01).measured)
print("common asm/asm shift", common_volume(k, Pos(0,0,0.001)*k).measured)
print("common in/asm shifted 1e-3", common_volume(g01, Pos(0,0,0.001)*k).measured)
print("clearance asm carrier/asm g01", clearance(car, k).measured, "interf", interference({"c": car, "g": k})["c|g"].measured)
