import json, math, sys
from pathlib import Path
from build123d import import_step
from tools.measure import (min_wall, min_wall_wide, overhang_census, flat_ceiling_spans,
                           mass_properties, mesh_census, radial_extent, bore_census)
from tools.core import mesh_sagitta
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
sh = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
def R(r):
    return dict(measured=getattr(r,"measured",None), unit=getattr(r,"unit",None),
                at=getattr(r,"at",None), status=str(getattr(r,"status",None)),
                reason=getattr(r,"reason",None),
                detail={k:v for k,v in (getattr(r,"detail",None) or {}).items()
                        if not isinstance(v,(list,dict)) or len(str(v))<400})
out={}
out["min_wall"]=R(min_wall(sh, spacing=0.7))
out["min_wall_wide"]=R(min_wall_wide(sh, spacing=0.7))
out["overhang"]=R(overhang_census(sh, build_dir=(0,1,0), spacing=0.7))
try:
    out["bridge"]=R(flat_ceiling_spans(sh, build_dir=(0,1,0), max_span=5.0, spacing=0.7))
except Exception as e:
    out["bridge"]={"error":repr(e)}
mp = mass_properties(sh, 1240)
out["mass"]={k:R(v) for k,v in mp.items()}
json.dump(out, open(W/"reviews/RV02_work/r4_walls.json","w"), indent=1, default=str)
for k,v in out.items():
    print(k, v if "error" in str(v)[:20] else {kk:v.get(kk) for kk in ("measured","at","status","reason")} if isinstance(v,dict) and "measured" in v else {a:b.get("measured") for a,b in v.items()})
