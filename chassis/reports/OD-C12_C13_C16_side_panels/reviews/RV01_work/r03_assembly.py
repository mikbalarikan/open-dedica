"""RV01: my own check assembly from the three part files and the inputs at the spec 1.2
sec. 2 poses. U-03 (a) contacts, lip gap, other pairs, coaxiality; U-03 (b) assembly
path; REQ-02 lip gap, REQ-04 C07 clearance, REQ-05 at poses, REQ-06, REQ-07."""
import sys, math, time, itertools
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
import numpy as np
from tools.core import common_volume
from tools.measure import clearance, bore_census, locate_bore
from build123d import Box, Cylinder, Pos, Rot, Align, Solid

t0 = time.time()
R = one(load("od_c13_right_C1_v01.step"))
L = one(load("od_c12_left_C1_v01.step"))
BR = one(load("od_c16_bracket_C1_v01.step"))
refs = references()
new = {"OD-C13": R, "OD-C12": L}
for side in "RL":
    for i, zc in enumerate(ZC):
        new[f"OD-C16_{side}{i+1}"] = bracket_pose(BR, side, zc)
panel_of = lambda b: "OD-C13" if "_R" in b else "OD-C12"
out = {"contacts": {}, "others": {}, "lip": {}, "coax": {}, "plate_holes": {}, "req06": {}, "req07": {},
       "path": {}}

def cv(a, b):
    r = common_volume(a, b)
    return r

# ---- (a) designed contacts
contact_pairs = [("OD-C13", "OD-C01"), ("OD-C12", "OD-C01"), ("OD-C13", "OD-C10"), ("OD-C12", "OD-C10")]
for b in [k for k in new if k.startswith("OD-C16")]:
    contact_pairs += [(b, "OD-C01"), (b, panel_of(b))]
allsolids = {**refs, **new}
for a, b in contact_pairs:
    c = clearance(allsolids[a], allsolids[b]); v = cv(allsolids[a], allsolids[b])
    out["contacts"][f"{a}|{b}"] = {"clearance": c, "interference": v}
    print("contact", a, b, c.measured, c.status, v.measured, v.status)

# ---- lip to OD-C10 skirt: panel material above y 215 (the wedge only)
for p in ("OD-C13", "OD-C12"):
    cut = Pos(0, 215.0 + 50, 0) * Box(400, 100, 800)
    lip = allsolids[p] & cut
    c = clearance(lip, refs["OD-C10"])
    out["lip"][p] = {"clearance": c, "lip_bbox": [lip.bounding_box().min.to_tuple(), lip.bounding_box().max.to_tuple()],
                     "lip_volume": lip.volume}
    print("lip", p, c.measured, c.at, out["lip"][p]["lip_bbox"], lip.volume)

# ---- other pairs: every new part with every solid, not a designed contact pair
cset = {frozenset(p) for p in contact_pairs}
names = list(allsolids)
for a in new:
    for b in names:
        if a == b or frozenset((a, b)) in cset:
            continue
        key = "|".join(sorted((a, b)))
        if key in out["others"]:
            continue
        c = clearance(allsolids[a], allsolids[b])
        out["others"][key] = {"clearance": c}
least = sorted(((v["clearance"].measured if v["clearance"].ok else -1, k) for k, v in out["others"].items()))
print("others least", least[:8], "n", len(least), [k for k, v in out["others"].items() if not v["clearance"].ok])
# interference over all pairs that involve a new part
inter = {}
for a in new:
    for b in names:
        if a == b:
            continue
        key = "|".join(sorted((a, b)))
        if key in inter:
            continue
        inter[key] = cv(allsolids[a], allsolids[b])
out["interference_all"] = inter
bad = {k: (v.measured, v.status) for k, v in inter.items() if not v.ok or v.measured > BAND_MM3}
print("interference all pairs", len(inter), "nonzero/inconclusive", bad)

# ---- coaxiality: bracket insert bore vs panel hole, both located with locate_bore
pc = {p: bore_census(allsolids[p]) for p in ("OD-C13", "OD-C12")}
for b in [k for k in new if k.startswith("OD-C16")]:
    side = 1 if "_R" in b else -1
    zc = ZC[int(b[-1]) - 1]
    bc = bore_census(new[b])
    ib = locate_bore(bc, (side * 114.0, 10.0, zc), (1, 0, 0))
    ph = locate_bore(pc[panel_of(b)], (side * 118.5, 10.0, zc), (1, 0, 0))
    pb = locate_bore(bc, (side * 104.5, 1.5, zc), (0, 1, 0))
    def axis(res):
        d = res["offset"].detail
        s, e = np.array(d["start"]), np.array(d["end"])
        return s, (e - s) / np.linalg.norm(e - s)
    s1, u1 = axis(ib); s2, u2 = axis(ph)
    w = s1 - s2
    perp = w - np.dot(w, u2) * u2
    off = float(np.linalg.norm(perp))
    out["coax"][b] = {"insert": ib, "panel_hole": ph, "axis_offset_mm": off,
                      "insert_axis": (s1.tolist(), u1.tolist()), "hole_axis": (s2.tolist(), u2.tolist()),
                      "parallel_cross": float(np.linalg.norm(np.cross(u1, u2)))}
    out["plate_holes"][b] = pb
    print("coax", b, round(off, 6), ib["diameter"].measured, ib["offset"].measured, ph["diameter"].measured,
          ph["offset"].measured, "plate hole", pb["diameter"].measured, pb["offset"].measured, pb["through"].measured)

# ---- REQ-06: new insert positions on OD-C01
c01 = refs["OD-C01"]
c01b = bore_census(c01)
bores = c01b.detail["bores"]
handed = [(88, -222), (88, -78), (106, -222), (106, -78)] + [(sx * x, -282) for sx in (1, -1) for x in (81, 95)]
posn = [(sx * 104.5, zc) for sx in (1, -1) for zc in ZC]
def edge_dist(x, z):
    # plate outline x +-120, z -305..+100, R10 corners about (+-110, -295 / +90)
    ax, cz = abs(x), z
    if ax <= 110 or (-295 <= cz <= 90):
        d = min(120 - ax, cz + 305, 100 - cz)
        if ax > 110 and not (-295 <= cz <= 90):
            pass
        return d
    ccz = -295 if cz < -295 else 90
    return 10 - math.hypot(ax - 110, cz - ccz)
for (x, z) in posn:
    dists = []
    for bb in bores:
        s = np.array(bb["start"]); u = np.array(bb["axis_dir"])
        # in-plane distance of the bore axis from (x, z): axes are along Y
        dists.append((math.hypot(s[0] - x, s[2] - z), bb["diameter"], tuple(round(v, 3) for v in s), tuple(u)))
    dists.sort()
    hd = sorted((math.hypot(hx - x, hz - z), (hx, hz)) for hx, hz in handed)
    others_new = sorted(math.hypot(px - x, pz - z) for (px, pz) in posn if (px, pz) != (x, z))
    disc = Pos(x, -3.0, z) * Rot(90, 0, 0) * Cylinder(4.0, 6.0)
    fill = common_volume(disc, c01)
    out["req06"][f"{x},{z}"] = {"edge": edge_dist(x, z), "nearest_bore": dists[0], "nearest_handed": hd[0],
                               "nearest_new": others_new[0], "disc_fill": fill, "disc_volume": disc.volume}
    print("req06", x, z, round(edge_dist(x, z), 3), dists[0][:2], dists[0][2], [round(v, 3) for v in (hd[0][0], others_new[0])],
          fill.measured, round(disc.volume, 3))
out["c01_bores"] = c01b

# ---- REQ-07 keep-outs and access cylinders
keep = {}
for (fx, fz) in ((110, 90), (-110, 90), (110, -295), (-110, -295)):
    k = Pos(fx, 1.0, fz) * Rot(90, 0, 0) * Cylinder(4.0, 2.0)
    for n, s in new.items():
        keep[f"keepout({fx},{fz})|{n}"] = common_volume(k, s)
drv = {}
for (x, z) in posn:
    c = Pos(x, (16.0 + 215.0) / 2, z) * Rot(90, 0, 0) * Cylinder(4.0, 215.0 - 16.0)
    for n, s in allsolids.items():
        if n in ("OD-C13", "OD-C12", "OD-C10"):
            continue
        drv[f"driver({x},{z})|{n}"] = common_volume(c, s)
ph_acc = {}
for sx in (1, -1):
    for z in ZC:
        c = Pos(sx * 130.0, 10.0, z) * Rot(0, 90, 0) * Cylinder(4.0, 20.0)
        for n, s in allsolids.items():
            ph_acc[f"panelscrew({sx*120}+20,{z})|{n}"] = common_volume(c, s)
for nm, dd in (("keepout", keep), ("driver", drv), ("panel_screw", ph_acc)):
    worst = max(((v.measured if v.ok else float("inf")), k) for k, v in dd.items())
    out["req07"][nm] = {"n": len(dd), "worst": worst, "inconclusive": [k for k, v in dd.items() if not v.ok]}
    print("req07", nm, len(dd), worst, out["req07"][nm]["inconclusive"])

dump(out, "assembly_a.json")
print("seconds", round(time.time() - t0, 1))
