import json
from pathlib import Path
from tools.core.step import read_step
from tools.measure import radial_extent
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
pump = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
A = ((0,0,0),(0,0,1),(1,0,0)); o = {}
for z in (-2.5, 0.0, 2.5, 25.5, 28.0, 30.5):
    for a in (45, 60, 90, 120, 135):
        r = radial_extent(pump, *A, a, z, side="outer", r_min=0, r_max=26.0)
        o[f"z{z} th{a}"] = r.measured if r.ok else r.reason
print(json.dumps(o, indent=0)); (W/"reviews/RV02_work/m6_coil.json").write_text(json.dumps(o, indent=1))
