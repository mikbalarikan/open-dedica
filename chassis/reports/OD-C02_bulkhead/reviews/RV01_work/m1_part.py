import json, sys, math
from pathlib import Path
from tools.core.step import read_step, labels, compare_step, read_schema
from tools.core.validity import validity
from tools.core.shapes import solids, faces
from tools.measure import (envelope, feature_census, bore_census, locate_bore, mass_properties)
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead")
W = J/"reviews/RV01_work"
step = J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step"
s = read_step(step)
out = {}
def d(r): return r.to_dict()
out["labels"] = labels(s)
out["schema"] = read_schema(step)
out["validity"] = {k: d(v) for k, v in validity(s).items()}
out["envelope"] = {k: d(v) for k, v in envelope(s).items()}
out["mass"] = {k: d(v) for k, v in mass_properties(s, 1070).items()}
fc = feature_census(s)
out["feature_census"] = {k: d(v) for k, v in fc.items()}
bc = bore_census(s)
out["bore_census"] = d(bc)
bores = {}
for z in (-45, -105, -165, -225):
    bores[f"base_z{z}"] = {k: d(v) for k, v in locate_bore(bc, (65, 3, z), (0, 1, 0)).items()}
for z in (-60, -210):
    bores[f"top_z{z}"] = {k: d(v) for k, v in locate_bore(bc, (65, 212, z), (0, 1, 0)).items()}
out["bores"] = bores
# face kinds
from tools.measure.sampling import kind
kinds = {}
for f in faces(s):
    kinds[kind(f)] = kinds.get(kind(f), 0) + 1
out["face_kinds"] = kinds
out["n_faces"] = len(faces(s))
(W/"m1_part.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, default=str)[:6000])
