import json, sys, math
from pathlib import Path
from build123d import import_step
from tools.core import (validity, compare_step, mesh_sagitta, read_schema, read_length_unit)
from tools.measure import (envelope, feature_census, bore_census, locate_bore,
                           min_wall, min_wall_wide, overhang_census, flat_ceiling_spans,
                           mass_properties, mesh_census, radial_extent)
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
STEP = W/"02_STEP_STL/od_c01_frame_C1_v03.step"
STL  = W/"02_STEP_STL/od_c01_frame_C1_v03.stl"
out = {}
def R(r):
    if r is None: return None
    try:
        return dict(measured=r.measured, unit=r.unit, at=r.at, status=str(r.status),
                    reason=getattr(r,"reason",None), detail=getattr(r,"detail",None),
                    params=getattr(r,"params",None))
    except Exception:
        return repr(r)
sh = import_step(str(STEP))
out["schema"]=read_schema(STEP); out["unit"]=read_length_unit(STEP)
# U-01
v = validity(sh)
out["validity"] = {k:R(x) for k,x in v.items()} if isinstance(v,dict) else R(v)
# U-02 envelope
env = envelope(sh)
out["envelope"] = {k:R(x) for k,x in env.items()} if isinstance(env,dict) else R(env)
# U-04 roundtrip (compare only, no write)
out["compare_step"] = {k:R(x) for k,x in compare_step(sh, STEP).items()}
# U-05 census
fc = feature_census(sh)
out["feature_census"] = {k:R(x) for k,x in fc.items()} if isinstance(fc,dict) else R(fc)
bc = bore_census(sh)
out["bore_census_raw"] = R(bc)
bores = bc.detail["bores"] if getattr(bc,"detail",None) and "bores" in bc.detail else None
out["bore_count"] = bc.measured
if bores:
    from collections import Counter
    out["dia_hist"] = dict(Counter(round(b["diameter"],4) for b in bores))
    out["bores"] = [{"d":round(b["diameter"],6),"dir":[round(c,6) for c in b["axis_dir"]],
                     "start":[round(c,6) for c in b["start"]],"end":[round(c,6) for c in b["end"]],
                     "len":round(b["length"],6),"through":b.get("through"),
                     "span_deg":round(b.get("span_deg",0),4)} for b in bores]
json.dump(out, open(W/"reviews/RV02_work/r2_part.json","w"), indent=1, default=str)
print("bore count", bc.measured, out.get("dia_hist"))
print("env", {k:getattr(x,'measured',None) for k,x in env.items()})
print("validity", {k:getattr(x,'measured',None) for k,x in (v.items() if isinstance(v,dict) else [])})
print("fc", {k:getattr(x,'measured',None) for k,x in (fc.items() if isinstance(fc,dict) else [])})
