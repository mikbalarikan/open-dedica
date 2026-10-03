"""RV01: exact B-rep rays (radial_extent) for REQ-02, REQ-06, J-05, D-05a, and the gusset / pass-through gaps."""
import json, sys
from tools.core import read_step
from tools.measure import radial_extent
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
p = read_step(STEP)
out = {}
def r(name, *a, **k):
    res = radial_extent(p, *a, **k)
    out[name] = res.to_dict()
    print(name, res.measured, res.status, res.reason[:80], res.detail.get("material"))
    return res
# REQ-02: axis along X through (x0, y, -300.5); angle 0 = +Z, 180 = -Z (ref +Z, about +X)
for y in (50, 200):
    for x in (-40, 0, 40):
        r(f"REQ02_inner_y{y}_x{x}", (x, y, -300.5), (1, 0, 0), (0, 0, 1), 0, 0, side="inner", r_min=0, r_max=1.0e-9+1.4) if False else None
        r(f"REQ02_plusZ_y{y}_x{x}", (x, y, -300.5), (1, 0, 0), (0, 0, 1), 0, 0, side="outer", r_min=0, r_max=10)
        r(f"REQ02_minusZ_y{y}_x{x}", (x, y, -300.5), (1, 0, 0), (0, 0, 1), 180, 0, side="outer", r_min=0, r_max=10)
# x extent of the wall at y 50 / 200: axis along Z at (0, y, -300.5), ref +X
for y in (50, 200):
    r(f"REQ02_plusX_y{y}", (0, y, -300.5), (0, 0, 1), (1, 0, 0), 0, 0, side="outer", r_min=60, r_max=130)
    r(f"REQ02_minusX_y{y}", (0, y, -300.5), (0, 0, 1), (1, 0, 0), 180, 0, side="outer", r_min=60, r_max=130)
# REQ-06 slots: axis along Z at (xc, 140, -300.5); inner material in +-X and +-Y
for xc in (78, 86, 94, 102, 110):
    for ang in (0, 90, 180, 270):
        r(f"REQ06_x{xc}_a{ang}", (xc, 140, -300.5), (0, 0, 1), (1, 0, 0), ang, 0, side="inner", r_min=0, r_max=60)
    # through: ray along Z at slot centre reaches no material: check a ray along Z from (xc,140,-310)
# J-05 / D-05a: axis = insert bore, origin (x, 209, -293), dir +Y, ref +X; levels y 210 and y 213
for x in (90, -90):
    for lev in (1.0, 4.0):
        for ang in (0, 90, 180, 270):
            r(f"J05_x{x}_y{209+lev}_a{ang}", (x, 209, -293), (0, 1, 0), (1, 0, 0), ang, lev, side="inner", r_min=1.0, r_max=40) if False else None
            r(f"J05o_x{x}_y{209+lev}_a{ang}", (x, 209, -293), (0, 1, 0), (1, 0, 0), ang, lev, side="outer", r_min=1.0, r_max=12)
json.dump(out, open(f"{J}/reviews/RV01_work/m3_rays.json" if len(sys.argv) < 3 else sys.argv[2], "w"), indent=1, default=str)
