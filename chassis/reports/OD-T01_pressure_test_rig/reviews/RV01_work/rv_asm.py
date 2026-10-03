"""RV01 reviewer: assembly / motion rows. Housing set posed by spec §2 from the v03 assembly, solids identified by measurement."""
import json, sys, time, math
from pathlib import Path
import numpy as np
from build123d import Solid, Compound, Location, Cylinder, Pos, Rot, Box, Edge, Vector
from tools.core import read_step, solids, validity, common_volume
from tools.measure import envelope, bore_census, locate_bore, clearance, interference

J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
W = J / "reviews/RV01_work"
rig_path = Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else J / "02_STEP_STL/od_t01_rig_C1_v01.step"
tag = sys.argv[2] if len(sys.argv) > 2 else "nominal"
which = sys.argv[3].split(",") if len(sys.argv) > 3 else ["all"]
def want(k): return "all" in which or k in which
out = {}
t0 = time.time()
rig = Solid(solids(read_step(rig_path))[0])
asm = read_step(J / "00_Spec/inputs/od_g01_assembly_C1_v03.step")
S = [Solid(s) for s in solids(asm)]
info = []
for i, s in enumerate(S):
    bb = s.bounding_box()
    info.append({"i": i, "size": [bb.size.X, bb.size.Y, bb.size.Z], "vol": s.volume})
out["asm_solids"] = info
# identification by measurement: housing = 100x100 in x,y with four Ø4.0 bores at (±44,±44); OD-G10 = longest extent > 120; OD-G04 = rest
def n_insert_bores(s):
    bc = bore_census(s)
    if not bc.ok: return -1
    return sum(1 for b in bc.detail["bores"] if abs(b["diameter"] - 4.0) < 0.05 and abs(abs(b["start"][0]) - 44) < 0.1 and abs(abs(b["start"][1]) - 44) < 0.1)
cand = []
for i, s in enumerate(S):
    sz = info[i]["size"]
    cand.append((i, max(sz), abs(sz[0] - 100) < 0.2 and abs(sz[1] - 100) < 0.2))
hous_i = [i for i, m, sq in cand if sq]
g10_i = [i for i, m, sq in cand if m > 120]
assert len(hous_i) == 1 and len(g10_i) == 1, cand
hi, gi = hous_i[0], g10_i[0]
oi = [i for i in range(len(S)) if i not in (hi, gi)][0]
out["ident"] = {"housing": hi, "g10": gi, "g04": oi, "housing_insert_bores": n_insert_bores(S[hi])}
POSE = Location((0, 110.06, 0)) * Location((0, 0, 0), (1, 0, 0), 90)   # x->X, y->+Z, z->-Y
def posed(s, phi=0.0, dy=0.0, dz=0.0):
    loc = Location((0, dy, dz)) * Location((0, 0, 0), (0, 1, 0), phi) * POSE
    return s.moved(loc)
# check the pose map
v = POSE * Location((1, 0, 0)); vy = POSE * Location((0, 1, 0)); vz = POSE * Location((0, 0, 1))
out["pose_map"] = {"x": tuple(round(c, 6) for c in (v.position - POSE.position)), "y": tuple(round(c, 6) for c in (vy.position - POSE.position)), "z": tuple(round(c, 6) for c in (vz.position - POSE.position))}
H, G4, G10 = posed(S[hi]), posed(S[oi]), posed(S[gi])
R = lambda r: r.to_dict()
out["validity"] = {n: {k: x.measured for k, x in validity(s).items()} for n, s in (("housing", H), ("g04", G4), ("g10", G10))}
out["env"] = {n: {k: x.measured for k, x in envelope(s).items()} for n, s in (("housing", H), ("g04", G4), ("g10", G10))}
if want("static"):
    # U-03a
    out["U03a_contact"] = R(clearance(rig, H))
    out["U03a_int"] = {k: R(x) for k, x in interference({"rig": rig, "housing": H, "g04": G4}).items()}
    below = rig.intersect(Box(400, 134.99, 400, align=None).moved(Location((-200, 0, -200))))  # rig y<134.99
    below = Compound(list(below)) if not hasattr(below, "wrapped") else below
    out["below_env"] = {k: x.measured for k, x in envelope(below).items()}
    out["U03a_rig_below_to_housing"] = R(clearance(below, H))
    out["U03a_rig_g04"] = R(clearance(rig, G4))
    out["U03a_rig_g10"] = R(clearance(rig, G10))
    out["U03a_housing_g10_int"] = R(clearance(H, G10))
    # REQ-01: posed insert bores
    bch = bore_census(H)
    ins = []
    for sx in (1, -1):
        for sz in (1, -1):
            lb = locate_bore(bch, (sx * 44.0, 132.0, sz * 44.0), (0, 1, 0))
            st = lb["diameter"].detail["start"]; en = lb["diameter"].detail["end"]
            ins.append({"pt": (sx * 44, sz * 44), "d": lb["diameter"].measured, "start": st, "end": en,
                        "axis_offset_from_hole": math.hypot(st[0] - sx * 44.0, st[2] - sz * 44.0)})
    out["REQ01_inserts"] = ins
    # pair-B Ø3.8 bores on the posed housing
    pb = [b for b in bch.detail["bores"] if abs(b["diameter"] - 3.8) < 0.1]
    out["pairB_bores"] = [{"d": b["diameter"], "start": b["start"], "end": b["end"], "r": math.hypot(b["start"][0], b["start"][2])} for b in pb]
    pbd = []
    for b in pb:
        x, z = b["start"][0], b["start"][2]
        seg = Edge.make_line((x, 135.0, z), (x, 150.0, z))
        c = clearance(seg, rig)
        pbd.append({"axis": (x, z), "dist": c.measured, "at": c.detail.get("on_b"), "status": c.status})
    out["REQ03_pairB"] = pbd
    # REQ-05
    out["REQ05_g10_min_y"] = envelope(G10)["min_y"].measured
    # REQ-06 / REQ-07 probes
    probes6 = {f"b{sx}{sz}": Cylinder(4.0, 290.0, align=None).moved(Location((sx * 105.0, 10.0, sz * 40.0)) * Location((0, 0, 0), (1, 0, 0), -90)) for sx in (1, -1) for sz in (1, -1)}
    probes7 = {f"s{sx}{sz}": Cylinder(3.0, 150.0, align=None).moved(Location((sx * 44.0, 150.0, sz * 44.0)) * Location((0, 0, 0), (1, 0, 0), -90)) for sx in (1, -1) for sz in (1, -1)}
    out["probe_check"] = {k: [envelope(p)[q].measured for q in ("min_y", "max_y", "min_x", "max_x")] for k, p in list(probes6.items())[:1] + list(probes7.items())[:1]}
    out["REQ06"] = {k: R(common_volume(rig, p)) for k, p in probes6.items()}
    out["REQ07"] = {k: R(common_volume(rig, p)) for k, p in probes7.items()}
    out["REQ06_clear"] = {k: clearance(rig, p).measured for k, p in probes6.items()}
    out["REQ07_clear"] = {k: clearance(rig, p).measured for k, p in probes7.items()}
    # handle direction check (phi sign)
    out["phi_sign"] = {str(p): envelope(posed(S[gi], phi=p))["max_x"].measured for p in (-10, 0, 10)}
if want("u03b"):
    rows = []
    for k in range(0, 31):          # every 1.0 mm (spec: steps <= 2.0)
        dy = -float(k)
        h, g4, g10 = posed(S[hi], dy=dy), posed(S[oi], dy=dy), posed(S[gi], dy=dy)
        ih = common_volume(rig, h); i4 = common_volume(rig, g4); c10 = clearance(rig, g10)
        rows.append({"dy": dy, "int_h": ih.measured, "st_h": ih.status, "int_g4": i4.measured, "st_g4": i4.status,
                     "c_g10": c10.measured, "in_g10": c10.detail.get("inside"), "c_h": clearance(rig, h).measured, "c_g4": clearance(rig, g4).measured})
    out["U03b"] = rows
if want("req04a"):
    rows = []
    phis = sorted(set([float(p) for p in range(-60, 16, 5)] + [float(p) for p in range(-60, 16, 1)]))
    for p in phis:
        c = clearance(rig, posed(S[gi], phi=p))
        rows.append({"phi": p, "c": c.measured, "at": c.at, "inside": c.detail.get("inside"), "st": c.status})
    out["REQ04a"] = rows
if want("req04b"):
    rows = []
    for k in range(0, 81):          # dz 0..200 every 2.5
        dz = 2.5 * k
        c = clearance(rig, posed(S[gi], phi=-50.0, dy=-15.0, dz=dz))
        rows.append({"dz": dz, "c": c.measured, "at": c.at, "inside": c.detail.get("inside")})
    out["REQ04b"] = rows
    # path segments joining (b) to the locked pose: lift at phi -50 dy -15..0, then (a) covers rotation
    lift = []
    for k in range(0, 16):
        c = clearance(rig, posed(S[gi], phi=-50.0, dy=-float(k)))
        lift.append({"dy": -float(k), "c": c.measured, "inside": c.detail.get("inside")})
    out["REQ04_lift"] = lift
out["seconds"] = time.time() - t0
(W / f"asm_{tag}_{'_'.join(which)}.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, default=str)[:12000])
