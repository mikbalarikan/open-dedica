"""U-03 (a), (b), E-01, E-05 against the references placed by spec 1.1 section 2."""
from common import *
from itertools import combinations
from tools.measure import clearance, interference, bore_census, locate_bore, envelope
from tools.core import common_volume, validity
from build123d import fillet, Axis
out = {}
def IN(a, b):
    res = a & b
    return res
s, ss = part(); P = Solid(ss[0])
r = refs()
names = ["C01", "C05", "HOUS", "G04", "G10", "C10", "E02"]
unsound = {"G10", "E02"}
# ---- every pair ----
parts = {"PANEL": P, **{k: r[k] for k in names}}
pairs = {}
import os
if os.path.exists(WORK / "s02_pairs.json"):
    pairs = json.loads((WORK / "s02_pairs.json").read_text())
for a, b in ([] if pairs else combinations(parts.keys(), 2)):
    A, B = parts[a], parts[b]
    rec = {}
    if a in unsound or b in unsound:
        rec["mode"] = "clearance_fallback"
    else:
        cv = common_volume(A, B); rec["common_mm3"] = cv.measured; rec["status"] = cv.status; rec["reason"] = cv.reason
    c = clearance(A, B); rec["clearance"] = c.measured; rec["inside"] = c.detail.get("inside"); rec["at"] = c.at; rec["on_b"] = c.detail.get("on_b")
    pairs[f"{a}|{b}"] = rec
    print(a, b, rec, flush=True)
out["pairs"] = pairs
dump("s02_pairs.json", pairs)
# panel to E02 with the panel moved off the seat by 0.005 and 0.001 along +Z
for dz in (0.001, 0.005):
    c = clearance(translate(P, (0, 0, dz)), r["E02"]); out[f"panel_E02_shift_{dz}"] = {"clearance": c.measured, "inside": c.detail["inside"], "at": c.at}
# ---- contacts ----
wall_foot = IN(P, box(-117, 117, -1, 0.5, 93.9, 97.1))
flL = IN(P, box(-105, -75.5, -1, 0.5, 71.9, 93.9)); flR = IN(P, box(75.5, 105, -1, 0.5, 71.9, 93.9))
for k, sh in {"wall_foot": wall_foot, "flange_L": flL, "flange_R": flR}.items():
    c = clearance(sh, r["C01"]); out["contact_" + k] = {"clearance": c.measured, "at": c.at, "vol": sh.volume}
c = clearance(P, r["C10"]); out["contact_C10"] = {"clearance": c.measured, "at": c.at, "on_b": c.detail["on_b"]}
# boss end faces: boss solids
bossL_ax, bossR_ax = (-91.0555, 153.2349), (-90.9987, 127.2515)
bosses = {}
for k, (x, y) in {"L": bossL_ax, "R": bossR_ax}.items():
    b = IN(P, cyl_z(x, y, 5.6, 85.0, 93.99)); bosses[k] = b
    bb = b.bounding_box()
    c = clearance(b, r["E02"]); out["contact_boss_" + k] = {"clearance": c.measured, "at": c.at, "inside": c.detail["inside"], "vol": b.volume,
        "bb": [bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z]}
    for lift in (0.05, 0.5, 2.0):
        piece = IN(P, cyl_z(x, y, 5.6, 85.485 + lift, 93.99))
        c = clearance(piece, r["E02"]); out[f"E01_boss_{k}_above_{lift}"] = {"clearance": c.measured, "at": c.at, "on_b": c.detail["on_b"], "inside": c.detail["inside"]}
# panel without the bosses
nob = P - cyl_z(*bossL_ax, 5.6, 85.0, 93.999) - cyl_z(*bossR_ax, 5.6, 85.0, 93.999)
out["nob_volume"] = nob.volume; out["panel_volume"] = P.volume
c = clearance(nob, r["E02"]); out["E01_no_bosses"] = {"clearance": c.measured, "at": c.at, "on_b": c.detail["on_b"], "inside": c.detail["inside"]}
print("E01", out["E01_no_bosses"], flush=True)
# ---- footprint ----
outline = box(-120, 120, 0, 0.01, -305, 100)
outline = fillet(outline.edges().filter_by(Axis.Y), 10)
skin = box(-140, 140, 0, 0.01, -330, 130) - outline
foot = IN(P, box(-130, 130, 0, 0.01, 60, 110))
c = clearance(foot, skin); out["footprint"] = {"clearance": c.measured, "at": c.at, "on_b": c.detail["on_b"]}
# ---- OD-C01 holes ----
cb = bore_census(r["C01"]); holes = cb.detail["bores"]
out["c01_bores"] = [(round(h["diameter"], 3), h["start"], h["end"], h["axis_dir"]) for h in holes]
flanges = IN(P, box(-105, -75.5, -1, 4.1, 71.9, 93.99)) , IN(P, box(75.5, 105, -1, 4.1, 71.9, 93.99))
footband = IN(P, box(-117, 117, -0.1, 0.5, 93.99, 97.1))
best_fl, best_wall, best_cc = None, None, None
fh = [(-95, 77), (-85, 77), (85, 77), (95, 77)]
hole_rows = []
for h in holes:
    st, en = h["start"], h["end"]
    ax = h["axis_dir"]
    if abs(abs(ax[1]) - 1) > 1e-6:
        continue
    x, z = st[0], st[2]
    cyl = cyl_y(x, z, h["radius"], -6, 0)
    dfl = min(clearance(f, cyl).measured for f in flanges)
    dw = clearance(footband, cyl).measured
    dcc = min(math.hypot(x - a, z - b) for a, b in fh)
    hole_rows.append((x, z, h["diameter"], dfl, dw, dcc))
    best_fl = dfl if best_fl is None else min(best_fl, dfl); best_wall = dw if best_wall is None else min(best_wall, dw); best_cc = dcc if best_cc is None else min(best_cc, dcc)
out["c01_hole_rows"] = sorted(hole_rows, key=lambda t: t[3])[:6]
out["c01_holes_min"] = {"flange": best_fl, "wall_foot": best_wall, "centre": best_cc}
# ---- brew area ----
for k in ("C05", "HOUS", "G04"):
    c = clearance(P, r[k]); out["brew_" + k] = {"clearance": c.measured, "at": c.at}
# ---- OD-C15 keep-outs ----
for x in (-110, 110):
    k = cyl_y(x, 90, 4.0, 0, 2.0)
    cv = common_volume(P, k); c = clearance(P, k)
    out[f"C15_{x}"] = {"common": cv.measured, "status": cv.status, "clearance": c.measured, "at": c.at}
# ---- U-03 (b) lowering ----
low = []
for i in range(21):
    dy = 40.0 - 2.0 * i
    Q = translate(P, (0, dy, 0))
    row = {"dy": dy}
    for k in ("C01", "C05", "HOUS", "G04"):
        cv = common_volume(Q, r[k]); row[k] = cv.measured if cv.ok else ("INC", cv.reason)
    c = clearance(Q, r["G10"]); row["G10"] = (c.measured, c.detail["inside"])
    for k in ("C05", "HOUS"):
        row["gap_" + k] = clearance(Q, r[k]).measured
    low.append(row); print(row, flush=True)
out["lowering"] = low
# ---- E-05 ----
eb = bore_census(r["E02"])
out["e02_bore_status"] = eb.status
out["e02_bores"] = [(round(b["diameter"], 4), b["start"], b["end"], b["axis_dir"], b.get("through")) for b in eb.detail.get("bores", [])] if eb.ok else eb.reason
pc = bore_census(P)
e05 = []
if eb.ok:
    for b in eb.detail["bores"]:
        if 3.2 < b["diameter"] < 3.8 and abs(abs(b["axis_dir"][2]) - 1) < 1e-3:
            pt = b["start"]
            # point on the board hole axis at the boss bore's mid-depth z 88.485
            sx, sy, sz = b["start"]; ex, ey, ez = b["end"]
            t = (88.485 - sz) / (ez - sz) if ez != sz else 0
            p = (sx + t * (ex - sx), sy + t * (ey - sy), 88.485)
            lb = locate_bore(pc, p, (0, 0, 1))
            e05.append({"board_hole": b["start"], "end": b["end"], "d": b["diameter"], "probe": p,
                        "offset": lb["offset"].measured, "diam": lb["diameter"].measured, "found": lb["diameter"].at})
out["E05"] = e05
dump("s02_assembly.json", out)
print(json.dumps({k: v for k, v in out.items() if k not in ("pairs", "lowering")}, indent=1, default=str))
