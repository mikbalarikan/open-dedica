import sys, json
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_work")
from common import *
from tools.measure import radial_profile
A = half()
res = radial_profile(A, (95,30,0), (0,0,1), (1,0,0), list(range(10,171,10)), (-303.45, -291.53), margin=0.0, z_step=0.1, side="inner")
for k in ("max","min"):
    print(k, res[k].measured, res[k].at, res[k].status, res[k].reason[:200], res[k].detail.get("unread", [])[:3] if res[k].detail else "")
json.dump({k: res[k].to_dict() for k in ("max","min")}, open(W/"reviews/RV01_work/m3b_bore.json","w"), default=str)
