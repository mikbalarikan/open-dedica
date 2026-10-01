import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Solid
from tools.measure import min_wall
s = Solid(solids(read_step(STEP))[0])
r = min_wall(s, opposition_deg=46.0)
dump("m3b_wall46", {"r": r}); print("46deg", r.measured, r.status, r.reason, r.at, r.detail.get("from_face"), r.detail.get("to_face"))
