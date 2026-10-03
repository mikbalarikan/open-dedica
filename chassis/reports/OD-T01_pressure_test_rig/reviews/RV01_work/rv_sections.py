import json
from pathlib import Path
from build123d import Solid, Compound, Location
from tools.core import read_step, solids
from tools.drawing import write_sections
J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig"); W = J / "reviews/RV01_work/sections"
rig = Solid(solids(read_step(J / "02_STEP_STL/od_t01_rig_C1_v01.step"))[0])
S = [Solid(s) for s in solids(read_step(J / "00_Spec/inputs/od_g01_assembly_C1_v03.step"))]
POSE = Location((0, 110.06, 0)) * Location((0, 0, 0), (1, 0, 0), 90)
setp = [s.moved(POSE) for s in S]   # identified in rv_asm: 0 housing, 1 OD-G04, 2 OD-G10
asm = Compound([rig] + setp)
out = {}
for name, shape, view, thr in [("y142p5", rig, "front", (0, 142.5, 0)), ("y136p5", rig, "front", (0, 136.5, 0)),
                               ("y5", rig, "front", (0, 5, 0)), ("x44", rig, "left", (44, 75, 0)),
                               ("z0_asm", asm, "top", (0, 75, 0)), ("z44_asm", asm, "top", (0, 75, 44)),
                               ("z50_rig", rig, "top", (0, 75, 50)), ("x0_asm", asm, "left", (0, 75, 0))]:
    ws = write_sections(shape, W, part=f"rv01_{name}", version=1, views=(view,), through=thr)
    for w in ws:
        out[name] = {"path": str(w.path), "nothing_clipped": w.checks["nothing_clipped"].measured}
print(json.dumps(out, indent=1))
