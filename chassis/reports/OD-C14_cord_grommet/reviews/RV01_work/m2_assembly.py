import json, math, sys
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_work")
from common import *
from build123d import Axis, Pos
from tools.measure import clearance, interference, radial_extent, radial_profile, envelope
from tools.core import common_volume, validity
out = {}
def R(k, res):
    d = res.to_dict(); out[k] = d
    print(f"{k}: {d['measured']} {d['unit']} at {d['at']} {d['status']} {d['reason'][:120]} {('on_b '+str(d['detail'].get('on_b'))) if 'on_b' in d['detail'] else ''}")
P = c11(); F = c01(); A = half()
lb, bore = hole_axis(P)
for k, v in lb.items(): R("hole_"+k, v)
print("bore", bore)
ax0 = bore["start"]; cx, cy = ax0[0], ax0[1]
out["hole_record"] = bore
axis = Axis((cx, cy, 0), (0, 0, 1))
B = A.rotate(axis, 180)
# B is a rotation, check identity of shape: common volume with A mirrored? check B's envelope
for k, v in envelope(B).items(): print("B", k, round(v.measured, 6))
# measured bore radius of A about the axis
rb = []
for ang in (20, 45, 90, 135, 160):
    for z in (-302.5, -298.0, -295.0, -292.0):
        r = radial_extent(A, (cx, cy, 0), (0, 0, 1), (1, 0, 0), ang, z, side="inner")
        rb.append(r.measured)
print("bore radii", min(rb), max(rb)); out["bore_r"] = [min(rb), max(rb)]
r_b = sum(rb)/len(rb)
split_A = envelope(A)["min_y"].measured - cy
split_B = cy - envelope(B)["max_y"].measured
print("split offsets", split_A, split_B); out["split"] = [split_A, split_B]
cord = cyl(cx, cy, r_b, -330, -260)
tie = ring(cx, cy, 10.3/2, 12.9/2, -298.8, -294.0)
head = box(92.5, 97.5, 36.45, 42.45, -298.8, -293.8)
R("tie_outer_d", envelope(tie)["size_x"])
inner_zone = box(-300, 300, -50, 300, -298.99, -250)   # OD-C11 inside the wall's inner face: floor flange, gussets
P_in = one(P & inner_zone) if len(solids(P & inner_zone)) == 1 else (P & inner_zone)
print("P_in solids", len(solids(P_in)))
flange_zone = box(0, 200, 0, 100, -310, -301.9)
neck_zone = box(0, 200, 0, 100, -301.9, -280)
def poses(ya, yb, dz=0.0):
    return A.moved(Location((0, ya, dz))), B.moved(Location((0, yb, dz)))
# ---- open pose
a, b = poses(0, 0)
for n, h in (("A", a), ("B", b)):
    R(f"open_{n}_flange_to_C11", clearance(h & flange_zone, P))
    R(f"open_{n}_neck_to_C11", clearance(h & neck_zone, P))
    R(f"open_{n}_to_C11", clearance(h, P))
    R(f"open_{n}_bore_to_cord", clearance(h, cord))
    R(f"open_{n}_tie_to_half", clearance(tie, h))
    R(f"open_{n}_to_C11_inside_features", clearance(h, P_in))
    R(f"open_{n}_to_C01", clearance(h, F))
R("open_halves", clearance(a, b))
R("open_tie_to_C11", clearance(tie, P)); R("open_head_to_C11", clearance(head, P))
R("open_tie_to_C11_inside_features", clearance(tie, P_in)); R("open_head_to_C11_inside_features", clearance(head, P_in))
R("open_tie_to_C01", clearance(tie, F)); R("open_head_to_C01", clearance(head, F))
R("open_cord_to_C11", clearance(cord, P))
R("open_head_to_halfA", clearance(head, a)); R("open_head_to_halfB", clearance(head, b))
for k, v in interference({"A": a, "B": b, "C11": P, "C01": F, "cord": cord, "tie": tie, "head": head}).items():
    R("open_int_"+k, v)
# ---- closed pose: each half moved toward the axis by its own measured split offset
a, b = poses(-split_A, +split_B)
R("closed_halves", clearance(a, b))
R("closed_halves_int", common_volume(a, b))
for n, h in (("A", a), ("B", b)):
    R(f"closed_{n}_neck_to_C11", clearance(h & neck_zone, P))
    R(f"closed_{n}_flange_to_C11", clearance(h & flange_zone, P))
    R(f"closed_{n}_int_C11", common_volume(h, P))
    R(f"closed_{n}_int_cord", common_volume(h, cord))
# squeeze: cord radius minus innermost radius of the moved half about the cord axis
sq = []
for n, h, angs in (("A", a, (60, 90, 120)), ("B", b, (240, 270, 300))):
    for ang in angs:
        for z in (-302.5, -298.0, -295.0, -292.0):
            r = radial_extent(h, (cx, cy, 0), (0, 0, 1), (1, 0, 0), ang, z, side="inner", r_min=0)
            sq.append((r_b - r.measured, n, ang, z))
sq90 = [s for s in sq if s[2] in (90, 270)]
print("squeeze at 90/270:", min(s[0] for s in sq90), max(s[0] for s in sq90))
out["squeeze"] = sq
R("closed_union_size_x", envelope(a.fuse(b))["size_x"]); R("closed_union_size_y", envelope(a.fuse(b))["size_y"]); R("closed_union_size_z", envelope(a.fuse(b))["size_z"])
U = a.fuse(b); out["closed_union_valid"] = {k: v.measured for k, v in validity(U).items()}; print("union validity", out["closed_union_valid"])
# ---- assembly path, with closing swept together with insertion
PC = P & box(60, 130, -10, 70, -335, -270)
FC = F & box(60, 130, -10, 70, -335, -270)
print("clipped C11 solids", len(solids(PC)), "C01", len(solids(FC)))
path = []
for close in (0.0, 0.2, 0.4):
    for i in range(0, 41):
        dz = -20.0 + 0.5*i
        a, b = poses(-close*split_A/0.4, close*split_B/0.4, dz)
        row = {"close": close, "dz": dz}
        for n, h in (("A", a), ("B", b)):
            row[n+"_C11"] = common_volume(h, PC).measured
            row[n+"_C01"] = common_volume(h, FC).measured if len(solids(FC)) else 0.0
            row[n+"_clr_C11"] = clearance(h, PC).measured
        path.append(row)
worst = max(max(r["A_C11"], r["B_C11"], r["A_C01"], r["B_C01"]) for r in path)
least = min(min(r["A_clr_C11"], r["B_clr_C11"]) for r in path if r["dz"] < -0.01)
print("path worst interference", worst, "least clearance before seat", least)
for r in path:
    if r["close"] == 0.0 and r["dz"] in (-20, -12, -10, -8, -4, -2, -1, -0.5, 0): print("  ", r)
out["path"] = path
json.dump(out, open(W/"reviews/RV01_work/m2_assembly.json", "w"), indent=1, default=str)
