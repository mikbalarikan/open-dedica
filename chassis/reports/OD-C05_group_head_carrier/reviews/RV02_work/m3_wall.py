import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Solid
from tools.measure import min_wall, min_wall_wide
import time
path = Path(sys.argv[1]) if len(sys.argv) > 1 else STEP
tag = sys.argv[2] if len(sys.argv) > 2 else "nominal"
s = Solid(solids(read_step(path))[0])
t = time.time()
r = min_wall(s)
rw = min_wall_wide(s)
dump(f"m3_wall_{tag}", {"min_wall": r, "wide": rw, "secs": time.time() - t})
print(tag, r.measured, r.status, r.reason, r.at, "| wide", rw.measured, rw.status, rw.at)
