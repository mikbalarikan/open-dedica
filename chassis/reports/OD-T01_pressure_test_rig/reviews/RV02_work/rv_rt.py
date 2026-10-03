import json
from pathlib import Path
from build123d import Solid
from tools.core import step as st
W = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig"); OUT = W / "reviews/RV02_work"
P = W / "02_STEP_STL/od_t01_rig_C1_v02.step"
rig = st.read_step(P)
print(type(rig), st.labels(rig), len(rig.solids()), [type(c) for c in getattr(rig, "children", [])])
s = Solid(rig.solids()[0].wrapped); s.label = "od_t01_rig"
direct = st.compare_step(s, P)
print("delivered vs its read solid", {k: (v.measured, v.status) for k, v in direct.items()})
rt = st.step_roundtrip(s, OUT / "rt_v02.step", timestamp="2026-10-03T00:00:00")
print("reviewer re-export", {k: (v.measured, v.status, v.reason) for k, v in rt.items()})
print(st.file_sha256(OUT / "rt_v02.step"))
(OUT / "part_rt.json").write_text(json.dumps({"direct": {k: v.to_dict() for k, v in direct.items()}, "rt": {k: v.to_dict() for k, v in rt.items()}}, indent=1, default=str))
