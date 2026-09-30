"""RV01 part measurements on the exported carrier STEP (reviewer's own script)."""
import json, math, sys
from pathlib import Path
from tools.core import read_step, validity, compare_step, read_schema
from tools.core.step import labels
from tools.core.shapes import solids, volume_mm3
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall,
                           mass_properties, overhang_census)
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
W = J / "reviews/RV01_work"
P = J / "02_STEP_STL/od_c05_carrier_C1_v01.step"
part = read_step(P)
out = {}
def R(r): return r.to_dict()
out["labels"] = labels(part)
out["schema"] = read_schema(P)
out["validity"] = {k: R(v) for k, v in validity(part).items()}
out["envelope"] = {k: v.measured for k, v in envelope(part).items()}
out["feature_census"] = {k: v.measured for k, v in feature_census(part).items()}
bc = bore_census(part)
out["bores"] = bc.detail["bores"]
loc = {}
for sx in (1, -1):
    for sy in (1, -1):
        loc[f"Zhole({sx*44},{sy*44})"] = {k: R(v) for k, v in locate_bore(bc, (sx*44, sy*44, -26.44), (0, 0, 1)).items()}
        loc[f"cb({sx*44},{sy*44})"] = {k: R(v) for k, v in locate_bore(bc, (sx*44, sy*44, -28.94), (0, 0, 1)).items()}
for sx in (1, -1):
    for z in (-40, -60):
        loc[f"Yhole({sx*35},{z})"] = {k: R(v) for k, v in locate_bore(bc, (sx*35, -173.0, z), (0, 1, 0)).items()}
out["locate"] = loc
mw = min_wall(part)
out["min_wall"] = R(mw)
out["mass"] = {k: R(v) for k, v in mass_properties(part, 1070).items()} if isinstance(mass_properties(part, 1070), dict) else R(mass_properties(part, 1070))
oc = overhang_census(part, build_dir=(0, 1, 0))
out["overhang_whole"] = R(oc)
# round trip: re-read and compare with itself read again
rt = compare_step(part, P)
out["roundtrip_reread"] = {k: R(v) for k, v in rt.items()}
(W / "m1_part.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps({k: out[k] for k in ("labels", "schema", "envelope", "feature_census")}, indent=1, default=str))
print("validity", {k: v["measured"] for k, v in out["validity"].items()})
for k, v in loc.items(): print(k, {a: (b["measured"], b["status"]) for a, b in v.items()}, v["diameter"]["at"])
print("min_wall", mw.measured, mw.at, mw.status, mw.reason, {k: mw.detail.get(k) for k in ("wide", "wide_at", "largest_step_mm")})
print("overhang", oc.measured, oc.at, oc.status, oc.reason, {k: oc.detail.get(k) for k in ("sampling_bound_deg", "below_min_deg", "per_kind_least_deg", "bed_samples")})
print("rt", {k: (v.measured, v.status) for k, v in rt.items()})
print("mass", out["mass"])
