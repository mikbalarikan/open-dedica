"""RV01 U-04: the delivered part and assembly re-read: label, solids, validity, schema; a round trip of each to my work folder."""
import json
from tools.core import read_step, read_schema, read_length_unit, step_roundtrip, validity, solid_count
from tools.core.step import labels
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
out = {}
for k, path in [("part", f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"), ("assembly", f"{J}/02_STEP_STL/od_c11_assembly_C1_v03.step")]:
    s = read_step(path)
    o = {"schema": read_schema(path), "unit": read_length_unit(path), "labels": labels(s), "solids": solid_count(s).measured,
         "validity": {kk: v.measured for kk, v in validity(s).items()}}
    if k == "assembly":
        o["children"] = {c.label: {kk: v.measured for kk, v in validity(c).items()} for c in s.children}
    rt = step_roundtrip(s, f"{W}/roundtrip_{k}.step", timestamp="2026-10-01T00:00:00")
    o["roundtrip"] = {kk: (v.measured, v.status) for kk, v in rt.items()}
    out[k] = o; print(k, o)
json.dump(out, open(f"{W}/m11_roundtrip.json", "w"), indent=1, default=str)
