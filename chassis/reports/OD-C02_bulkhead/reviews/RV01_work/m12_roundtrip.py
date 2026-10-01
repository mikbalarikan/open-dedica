import json
from pathlib import Path
from tools.core.step import read_step, compare_step, step_roundtrip, read_header
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); W = J/"reviews/RV01_work"
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
out = {"compare_file": {k: (v.measured, v.reason) for k, v in compare_step(s, J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step").items()},
       "roundtrip_mine": {k: (v.measured, v.reason) for k, v in step_roundtrip(s, W/"mutants/rv01_reexport.step", timestamp="2026-09-30T00:00:00").items()},
       "header": read_header(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")}
(W/"m12_roundtrip.json").write_text(json.dumps(out, indent=1, default=str)); print(out)
