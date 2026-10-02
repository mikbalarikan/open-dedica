"""RV01: rays with the whole-ray window: REQ-02 x extent, REQ-06 slot inner extents."""
import json, sys
from tools.core import read_step
from tools.measure import radial_extent
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
p = read_step(STEP)
out = {}
def r(name, *a, **k):
    res = radial_extent(p, *a, **k); out[name] = res.to_dict()
    print(name, res.measured, res.status, res.reason[:60]); return res
for y in (50, 200):
    r(f"REQ02_plusX_y{y}", (0, y, -300.5), (0, 0, 1), (1, 0, 0), 0, 0, side="outer")
    r(f"REQ02_minusX_y{y}", (0, y, -300.5), (0, 0, 1), (1, 0, 0), 180, 0, side="outer")
for xc in (78, 86, 94, 102, 110):
    for ang in (0, 90, 180, 270):
        r(f"REQ06_x{xc}_a{ang}", (xc, 140, -300.5), (0, 0, 1), (1, 0, 0), ang, 0, side="inner")
    # through along Z: a ray along +Z from below the part at the slot's centre (axis along Y, ref +Z)
    r(f"REQ06_thru_x{xc}", (xc, 140, -310), (1, 0, 0), (0, 0, 1), 0, 0, side="inner") 
for (x, y) in [(95, 30), (-100, 30), (-84, 30)]:
    r(f"PASS_thru_{x}", (x, y, -310), (1, 0, 0), (0, 0, 1), 0, 0, side="inner")
json.dump(out, open(sys.argv[2] if len(sys.argv) > 2 else f"{J}/reviews/RV01_work/m3b_rays.json", "w"), indent=1, default=str)
