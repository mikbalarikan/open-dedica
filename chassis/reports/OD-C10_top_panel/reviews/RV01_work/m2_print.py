import sys, time, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.measure import min_wall, min_wall_wide, overhang_census, flat_ceiling_spans, radial_extent
L = lid(); out = {}
def R(r): return {"measured": r.measured, "at": r.at, "status": r.status, "reason": r.reason,
                  "detail": {k: v for k, v in (r.detail or {}).items() if k in ("wide_mm", "gated_mm", "at", "ceilings", "widest", "on_bed", "below", "downward", "per_kind", "bed", "solids", "faces")}}
t = time.time()
# skin thickness: rays +Y from y 230 at (x, z)
skin = {}
for (x, z) in [(0, -150), (-100, -100), (100, 0), (0, 0), (-80, 80), (-30, -250), (100, -150)]:
    o = radial_extent(L, (x, 230, z), (0, 0, 1), (0, 1, 0), 0.0, 0.0, side="outer", r_min=10, r_max=30)
    i = radial_extent(L, (x, 230, z), (0, 0, 1), (0, 1, 0), 0.0, 0.0, side="inner", r_min=10, r_max=30)
    skin[f"{x},{z}"] = (o.measured, i.measured, None if o.measured is None or i.measured is None else o.measured - i.measured, o.status, o.reason, i.reason)
out["skin"] = skin
skirt = {}
for y in (216.0, 230.0, 246.0):
    for z in (-150, 0, 60):
        for a, nm in ((0, "+x"), (180, "-x")):
            o = radial_extent(L, (0, 0, z), (0, 1, 0), (1, 0, 0), a, y, side="outer", r_min=110, r_max=130)
            i = radial_extent(L, (0, 0, z), (0, 1, 0), (1, 0, 0), a, y, side="inner", r_min=110, r_max=130)
            skirt[f"{nm} y{y} z{z}"] = (o.measured, i.measured, (o.measured - i.measured) if o.ok and i.ok else None, o.reason + i.reason)
    for x in (-40, 0, 40):
        for a, nm, zc in ((90, "-z", -100), (270, "+z", -100)):
            o = radial_extent(L, (x, 0, zc), (0, 1, 0), (1, 0, 0), a, y, side="outer", r_min=180, r_max=220)
            i = radial_extent(L, (x, 0, zc), (0, 1, 0), (1, 0, 0), a, y, side="inner", r_min=180, r_max=220)
            skirt[f"{nm} y{y} x{x}"] = (o.measured, i.measured, (o.measured - i.measured) if o.ok and i.ok else None, o.reason + i.reason)
out["skirt"] = skirt
corners = {}
for (cx, cz, angs) in [(110, -295, (15, 45, 75)), (-110, -295, (105, 135, 165)), (-110, 90, (195, 225, 255)), (110, 90, (285, 315, 345))]:
    for a in angs:
        for y in (216.0, 230.0):
            o = radial_extent(L, (cx, 0, cz), (0, 1, 0), (1, 0, 0), a, y, side="outer", r_min=2, r_max=15)
            i = radial_extent(L, (cx, 0, cz), (0, 1, 0), (1, 0, 0), a, y, side="inner", r_min=2, r_max=15)
            corners[f"{cx},{cz} a{a} y{y}"] = (o.measured, i.measured, o.at, o.reason + i.reason)
out["corners"] = corners
print("rays", time.time() - t, flush=True)
mw = min_wall(L, spacing=0.7); out["min_wall"] = R(mw); print("min_wall", mw.measured, mw.at, time.time() - t, flush=True)
ww = min_wall_wide(L, spacing=0.7); out["min_wall_wide"] = R(ww); print("wide", ww.measured, ww.at, time.time() - t, flush=True)
oh = overhang_census(L, build_dir=(0, -1, 0), spacing=0.7); out["overhang"] = R(oh); out["overhang_detail_full"] = {k: v for k, v in oh.detail.items() if k != "points"}
print("overhang", oh.measured, oh.at, time.time() - t, flush=True)
fs = flat_ceiling_spans(L, build_dir=(0, -1, 0), max_span=5.0, spacing=0.7); out["flat"] = R(fs); out["flat_detail_full"] = fs.detail
print("flat", fs.measured, fs.at, time.time() - t, flush=True)
dump("m2_print.json", out)
