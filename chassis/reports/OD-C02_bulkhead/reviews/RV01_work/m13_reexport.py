import json, math
from pathlib import Path
from build123d import Solid
from OCP.BRepBuilderAPI import BRepBuilderAPI_Copy
from tools.core.step import read_step, step_roundtrip
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); W = J/"reviews/RV01_work"
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
c = Solid(BRepBuilderAPI_Copy(s.wrapped).Shape()); c.label = "od_c02_bulkhead"
rt = {k: (v.measured, v.reason) for k, v in step_roundtrip(c, W/"mutants/rv01_reexport.step", timestamp="2026-09-30T00:00:00").items()}
analytic = 1012*210 - 16*(math.pi*49/2 + 98 + 49) - 6*math.pi*4*6
out = {"roundtrip_copy": rt, "analytic_volume": analytic, "step_volume": s.volume, "delta": s.volume - analytic}
(W/"m13_reexport.json").write_text(json.dumps(out, indent=1)); print(out)
