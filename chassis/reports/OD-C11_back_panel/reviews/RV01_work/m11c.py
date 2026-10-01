"""RV01 U-04: the re-read part's solid detached from its parent, labelled as delivered, written with write_step to my
work folder, re-read and compared (step_roundtrip); and the delivered file's re-read solid compared with that file."""
import json
from build123d import Solid
from tools.core import read_step, step_roundtrip, compare_step
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
s = read_step(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
solid = Solid(s.solids()[0].wrapped); solid.label = s.solids()[0].label or "od_c11_back"
print("label", repr(solid.label), "faces", len(solid.faces()))
rt = step_roundtrip(solid, f"{W}/roundtrip_part.step", timestamp="2026-10-01T00:00:00")
c = compare_step(solid, f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
out = {"roundtrip": {k: (v.measured, v.status, v.reason[:100]) for k, v in rt.items()},
       "vs_delivered": {k: (v.measured, v.status, v.reason[:100]) for k, v in c.items()}}
print(out); json.dump(out, open(f"{W}/m11c_roundtrip.json", "w"), indent=1)
