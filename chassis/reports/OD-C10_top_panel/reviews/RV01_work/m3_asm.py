import sys, time, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.core import common_volume, validity
from tools.core.shapes import solids, volume_mm3
from tools.measure import clearance, envelope, bore_census, locate_bore, engaged_area
from build123d import Pos
out = {}; t = time.time()
L = lid()
def R(r): return {"m": r.measured, "at": r.at, "st": r.status, "why": r.reason, "on_b": (r.detail or {}).get("on_b"), "inside": (r.detail or {}).get("inside")}
refs = {n: placed(n) for n in ("C01", "C02", "C05", "C07", "C11")}
out["ref_env"] = {n: {k: v.measured for k, v in envelope(s).items()} for n, s in refs.items()}
out["ref_valid"] = {n: {k: v.measured for k, v in validity(s).items()} for n, s in refs.items()}
# assembly STEP vs own placement
asm = solids(read_step(JOB / "02_STEP_STL/od_c10_assembly_C1_v01.step"))
out["asm"] = [{"vol": volume_mm3(s), "env": {k: v.measured for k, v in envelope(s).items()}} for s in asm]
print("loaded", time.time() - t, flush=True)
CROP = box(-125, 125, 200, 300, -310, 105)
cr = {}
for n, s in refs.items():
    e = out["ref_env"][n]
    cr[n] = (s & CROP) if e["max_y"] > 200 else None
cl = {}
for n, s in refs.items():
    cl[n] = R(clearance(L, s if cr[n] is None else cr[n]))
    cl[n]["cv"] = common_volume(L, s if cr[n] is None else cr[n]).measured
out["clear"] = cl
print("clear", json.dumps(cl, default=str), time.time() - t, flush=True)
# insert bores in refs
loc = {}
for n, pts in (("C02", [(65, -60), (65, -210)]), ("C11", [(90, -293), (-90, -293)])):
    bc = bore_census(cr[n])
    for (x, z) in pts:
        lb = locate_bore(bc, (x, 212.0, z), (0, 1, 0))
        loc[f"{n} {x},{z}"] = {k: (v.measured, v.detail.get("start") if v.detail else None, v.detail.get("end") if v.detail else None) for k, v in lb.items()}
out["insert_bores"] = loc
# lid holes' axes (from census) -> offset to ref bore axes
lbc = bore_census(L)
coax = {}
for n, pts in (("C02", [(65, -60), (65, -210)]), ("C11", [(90, -293), (-90, -293)])):
    bc = bore_census(cr[n])
    for (x, z) in pts:
        h = locate_bore(lbc, (x, 216.5, z), (0, 1, 0))["offset"]
        st = h.detail["start"]
        # point on lid hole axis, extended to the insert depth
        r = locate_bore(bc, (st[0], 212.0, st[2]), (0, 1, 0))
        coax[f"{n} {x},{z}"] = (r["offset"].measured, r["diameter"].measured, r["length"].measured, st)
out["coaxial"] = coax
# seats
seats = {}
for (x, z, n) in [(65, -60, "C02"), (65, -210, "C02"), (90, -293, "C11"), (-90, -293, "C11")]:
    piece = L & ycyl(x, z, 6.05, 214, 222)
    seats[f"{x},{z}"] = {"clear": R(clearance(piece, cr[n])), "cv": common_volume(piece, cr[n]).measured,
                         "area": engaged_area(piece, cr[n], (0, -1, 0), 0.01).measured}
out["seats"] = seats
print("seats", json.dumps(seats, default=str), time.time() - t, flush=True)
# pads vs C05; lid less pads vs C05
pads = L & (ycyl(48, 30, 5.05, 209, 246) + ycyl(-48, 30, 5.05, 209, 246))
nopads = L - (ycyl(48, 30, 5.05, 209, 246.0) + ycyl(-48, 30, 5.05, 209, 246.0))
out["pads_c05"] = R(clearance(pads, cr["C05"]))
out["nopads_c05"] = R(clearance(nopads, cr["C05"]))
for x in (48, -48):
    p = L & ycyl(x, 30, 5.05, 209, 246)
    out[f"pad{x}_c05"] = R(clearance(p, cr["C05"]))
# C05 features for REQ-05
c05b = bore_census(refs["C05"])
out["c05_bores"] = [b for b in c05b.detail["bores"] if abs(b["axis_dir"][1]) > 0.99]
# lid less columns vs C02
cols = ycyl(65, -60, 6.05, 214, 251) + ycyl(65, -210, 6.05, 214, 251) + ycyl(90, -293, 6.05, 214, 251) + ycyl(-90, -293, 6.05, 214, 251)
nocol = L - cols
out["nocol_c02"] = R(clearance(nocol, cr["C02"]))
# C11 rows
out["c11_whole"] = R(clearance(L, cr["C11"])); out["c11_cv"] = common_volume(L, cr["C11"]).measured
out["c11_area_total"] = engaged_area(L, cr["C11"], (0, -1, 0), 0.01).measured
corner = {}
for sx in (1, -1):
    c = L & box(min(sx * 109.95, sx * 125), max(sx * 109.95, sx * 125), 210, 251, -310, -294.95)
    corner[sx] = {"clear": R(clearance(c, cr["C11"])), "cv": common_volume(c, cr["C11"]).measured,
                  "area": engaged_area(c, cr["C11"], (0, -1, 0), 0.01).measured}
out["c11_corner"] = corner
# line region (rear skirt slab between the corners)
line = L & box(-109.95, 109.95, 210, 251, -310, -301.95)
out["c11_line"] = {"clear": R(clearance(line, cr["C11"])), "cv": common_volume(line, cr["C11"]).measured,
                   "area": engaged_area(line, cr["C11"], (0, -1, 0), 0.01).measured}
away = nocol - box(-125, 125, 200, 251, -310, -301.95) - box(109.95, 125, 200, 251, -310, -294.95) - box(-125, -109.95, 200, 251, -310, -294.95)
out["c11_away"] = R(clearance(away, cr["C11"]))
out["c02_away"] = out["nocol_c02"]
print("c11", json.dumps({k: out[k] for k in ("c11_whole", "c11_cv", "c11_area_total", "c11_corner", "c11_line", "c11_away", "nocol_c02", "pads_c05", "nopads_c05")}, default=str), time.time() - t, flush=True)
# REQ-06 headroom box
out["req06"] = common_volume(L, box(-42, 42, 200, 247, -70, 70)).measured
out["req06_strict"] = common_volume(L, box(-42, 42, 200, 246.99, -70, 70)).measured
# REQ-07 drivers
drv = {}
for (x, z) in [(65, -60), (65, -210), (90, -293), (-90, -293)]:
    drv[f"{x},{z}"] = {"d6": common_volume(L, ycyl(x, z, 3.0, 218.05, 260)).measured,
                       "d6.49": common_volume(L, ycyl(x, z, 3.245, 218.01, 251)).measured}
out["req07"] = drv
# U-03 (b) descent
desc = {}
for k in range(0, 21):
    dy = 40 - 2 * k
    M = Pos(0, dy, 0) * L
    desc[dy] = {n: common_volume(M, cr[n] if cr[n] is not None else refs[n]).measured for n in refs}
out["descent"] = desc
print("descent max", max(max(v.values()) for v in desc.values()), time.time() - t, flush=True)
dump("m3_asm.json", out)
