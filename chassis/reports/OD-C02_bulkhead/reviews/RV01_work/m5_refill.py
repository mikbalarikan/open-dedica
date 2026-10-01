import json, math
import numpy as np
from pathlib import Path
from build123d import Cylinder, Pos, Rot
from tools.core.step import read_step
from tools.core.shapes import faces
from tools.core.validity import validity
from tools.measure import overhang_census, bore_census, envelope
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); W = J/"reviews/RV01_work"
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
bc = bore_census(s)
fill = s
for b in bc.detail["bores"]:
    mouth_at_start = b["open_ends"][0]
    st, en = np.array(b["start"]), np.array(b["end"])
    mouth, floor = (st, en) if mouth_at_start else (en, st)
    u = (floor - mouth) / np.linalg.norm(floor - mouth)
    far = floor + 0.05 * u
    mid = (mouth + far) / 2; L = float(np.linalg.norm(far - mouth))
    c = Pos(*mid) * Rot(90, 0, 0) * Cylinder(b["radius"] + 0.1, L)
    fill = fill.fuse(c).clean()
out = {"refill_valid": {k: v.measured for k, v in validity(fill).items()}, "faces": len(faces(fill)),
       "bores": bore_census(fill).measured, "env": {k: v.measured for k, v in envelope(fill).items()}}
oh = overhang_census(fill, build_dir=(0, 0, 1), spacing=0.7)
out["overhang_refilled"] = oh.to_dict()
(W/"m5_refill.json").write_text(json.dumps(out, indent=1, default=str))
print(out["refill_valid"], out["faces"], out["bores"], out["env"]); print(oh.measured, oh.at, oh.status, oh.reason, oh.detail)
