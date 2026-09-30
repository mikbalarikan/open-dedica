import json, sys
from pathlib import Path
from tools.core import read_step
from tools.core.validity import validity
from tools.measure import envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide, overhang_census, mass_properties
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
p = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
print("type", type(p), getattr(p,"label",None))
out = {}
def d(r): return r.to_dict()
out["validity"] = {k: d(v) for k,v in validity(p).items()}
out["envelope"] = {k: d(v) for k,v in envelope(p).items()}
fc = feature_census(p)
out["feature_census"] = {k: (v.measured, v.status) for k,v in fc.items()}
bc = bore_census(p)
out["bores"] = bc.to_dict()
loc = {}
for x in (-34.0, 34.0):
    for z in (-4.0, 37.0):
        r = locate_bore(bc, (x, 38.5, z), (0,1,0))
        loc[f"{x},{z}"] = {k:(v.measured, v.status) for k,v in r.items()}
out["locate"] = loc
mw = min_wall(p); out["min_wall"] = d(mw)
mww = min_wall_wide(p); out["min_wall_wide"] = d(mww)
oh = overhang_census(p, build_dir=(0,-1,0), min_deg=45); out["overhang"] = d(oh)
out["mass"] = {k: d(v) for k,v in mass_properties(p, 1270).items()}
json.dump(out, open(W/"reviews/RV01_work/m1_part.json","w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:12000])
