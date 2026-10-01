import json, time
from pathlib import Path
from tools.core.step import read_step
from tools.measure import min_wall, min_wall_wide, overhang_census
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead")
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
out = {}
t=time.time(); out["min_wall"] = min_wall(s, spacing=0.7).to_dict(); out["t_mw"]=time.time()-t
t=time.time(); out["min_wall_wide"] = min_wall_wide(s, spacing=0.7).to_dict(); out["t_mww"]=time.time()-t
t=time.time(); out["overhang_whole"] = overhang_census(s, build_dir=(0,0,1), spacing=0.7).to_dict(); out["t_oh"]=time.time()-t
(J/"reviews/RV01_work/m3_walls.json").write_text(json.dumps(out, indent=1, default=str))
for k,v in out.items():
    if isinstance(v, dict): print(k, v["measured"], v["at"], v["status"], v["reason"], {kk: vv for kk, vv in v["detail"].items() if kk not in ("points",)} )
    else: print(k, v)
