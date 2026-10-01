"""RV01 reviewer measurement 1: the foot part file (foot frame)."""
import json, math, sys
from pathlib import Path
from tools.core import validity, solid_count, read_step, compare_step, step_roundtrip
from tools.core.step import read_schema, labels, read_length_unit
from tools.core.shapes import faces, solids
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall,
                           overhang_census, flat_ceiling_spans, radial_extent, radial_profile,
                           mass_properties)
from tools.measure.sampling import kind
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps

W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet")
STEP = W / "02_STEP_STL/od_c15_foot_C1_v01.step"
out = {}
def r(res):
    return {"measured": res.measured, "unit": res.unit, "at": res.at, "status": res.status,
            "reason": res.reason}

foot = read_step(STEP)
out["schema"] = read_schema(STEP); out["unit"] = read_length_unit(STEP)
out["labels"] = labels(foot)
out["validity"] = {k: r(v) for k, v in validity(foot).items()}
env = envelope(foot); out["envelope"] = {k: v.measured for k, v in env.items()}
fc = feature_census(foot); out["feature_census"] = {k: v.measured for k, v in fc.items()}
bc = bore_census(foot); out["bore_census"] = {"n": bc.measured, "bores": bc.detail["bores"]}
lb = locate_bore(bc, (0, 0, 1.25), (0, 0, 1)); out["locate_bore"] = {k: r(v) for k, v in lb.items()}
out["locate_bore_detail"] = lb["diameter"].detail
# faces list
fl = []
for f in faces(foot):
    a = BRepAdaptor_Surface(f); g = GProp_GProps(); BRepGProp.SurfaceProperties_s(f, g)
    c = g.CentreOfMass()
    fl.append({"kind": kind(f), "area": round(g.Mass(), 4), "c": (round(c.X(), 4), round(c.Y(), 4), round(c.Z(), 4))})
out["faces"] = fl
mw = min_wall(foot); out["min_wall"] = r(mw); out["min_wall_wide"] = mw.detail.get("wide")
oh = overhang_census(foot, (0, 0, 1), min_deg=45); out["overhang"] = r(oh); out["overhang_detail"] = {k: oh.detail.get(k) for k in ("per_kind_least_deg", "below_min_deg", "sampling_bound_deg", "bed_samples")}
fs = flat_ceiling_spans(foot, (0, 0, 1), max_span=5); out["flat_ceiling"] = r(fs)
mp = mass_properties(foot, 1210); out["mass"] = {k: v.measured for k, v in mp.items()}
json.dump(out, open(W / "reviews/RV01_work/m01_foot.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
