"""RV01 U-03 (b): the assembly path in the order of spec sec. 4, steps of 1.0 (<= 2.0).
(1) each bracket lowered along -Y from +20 to 0, every delivered part present (and the
brackets already seated); (2) each panel moved inward along X from 20 outside, brackets
in place, lid off; (3) OD-C10 lowered along -Y from +40 to 0, panels and brackets in place.
interference (common_volume) <= 0 mm3 at every step against every solid."""
import sys, time
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
from tools.core import common_volume
from build123d import Pos

t0 = time.time()
STEP = 1.0
R = one(load("od_c13_right_C1_v01.step")); L = one(load("od_c12_left_C1_v01.step"))
BR = one(load("od_c16_bracket_C1_v01.step"))
refs = references()
brackets = {f"OD-C16_{s}{i+1}": bracket_pose(BR, s, zc) for s in "RL" for i, zc in enumerate(ZC)}
out = {"bracket_down": {}, "panel_in": {}, "lid_down": {}}

def worst(moving, others, name):
    w, where, inc = 0.0, None, []
    for n, s in others.items():
        r = common_volume(moving, s)
        if not r.ok:
            inc.append((n, r.reason)); continue
        if r.measured > w:
            w, where = r.measured, n
    return w, where, inc

seated = {}
for b, s in brackets.items():
    rows = []
    for k in range(int(20 / STEP), -1, -1):
        d = k * STEP
        w, where, inc = worst(Pos(0, d, 0) * s, {**refs, **seated}, b)
        rows.append((d, w, where, inc))
    seated[b] = s
    out["bracket_down"][b] = rows
    print(b, "max", max(r[1] for r in rows), [r for r in rows if r[3]])
no_lid = {k: v for k, v in refs.items() if k != "OD-C10"}
placed_panels = {}
for p, s, sx in (("OD-C13", R, 1), ("OD-C12", L, -1)):
    rows = []
    for k in range(int(20 / STEP), -1, -1):
        d = k * STEP
        w, where, inc = worst(Pos(sx * d, 0, 0) * s, {**no_lid, **brackets, **placed_panels}, p)
        rows.append((d, w, where, inc))
    placed_panels[p] = s
    out["panel_in"][p] = rows
    print(p, "max", max(r[1] for r in rows), [r for r in rows if r[3]])
lid = refs["OD-C10"]
rows = []
for k in range(int(40 / STEP), -1, -1):
    d = k * STEP
    w, where, inc = worst(Pos(0, d, 0) * lid, {**no_lid, **brackets, **placed_panels}, "OD-C10")
    rows.append((d, w, where, inc))
out["lid_down"]["OD-C10"] = rows
print("lid max", max(r[1] for r in rows), [r for r in rows if r[3]])
dump(out, "assembly_path.json")
print("seconds", round(time.time() - t0, 1))
