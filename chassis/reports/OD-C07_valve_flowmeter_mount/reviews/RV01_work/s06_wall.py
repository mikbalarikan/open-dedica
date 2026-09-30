import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from tools.measure import min_wall, min_wall_wide
import time
m = load_mount(); t = time.time()
a = min_wall(m); print("min_wall", a.status, a.measured, a.at, a.reason, {k: v for k, v in a.detail.items() if k in ("wide", "largest_step_mm")}, time.time() - t)
b = min_wall_wide(m); print("min_wall_wide", b.status, b.measured, b.at, b.reason, b.detail.get("gated_mm"), time.time() - t)
dump("s06.json", {"min_wall": a, "min_wall_wide": b})
