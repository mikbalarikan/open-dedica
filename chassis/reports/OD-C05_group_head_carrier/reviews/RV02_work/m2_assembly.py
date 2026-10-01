import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Box, Pos, Rot, Location, Solid, Compound, Axis
from tools.core.validity import validity
from tools.core.boolean import common_volume
from tools.measure import clearance, interference, bore_census, locate_bore, envelope, mass_properties
from tools.core.step import labels, node_labels
res = {}
c = carrier(); cs = solids(c)[0]
g01 = read_step(G01); g04 = read_step(G04)
res["g01_valid"] = validity(g01); res["g04_valid"] = validity(g04)
res["g01_env"] = envelope(g01)
g01s = Solid(solids(g01)[0])
g04s = Solid(solids(g04)[0])
g04p = Pos(0, 0, -6.82) * Rot(0, 0, 6.05) * g04s
res["g04p_env"] = envelope(g04p)
cS = Solid(cs)
res["clear_c_g01"] = clearance(cS, g01s)
res["clear_c_g04"] = clearance(cS, g04p)
res["interf"] = interference({"carrier": cS, "g01": g01s, "g04": g04p})
# insert bores of G01
bg = bore_census(g01s)
res["g01_bores"] = [ (round(b["diameter"],4), [round(v,4) for v in b["start"]], [round(v,4) for v in b["end"]], b["through"]) for b in bg.detail["bores"]]
bc = bore_census(cS)
loc = {}
for x in (44, -44):
    for y in (44, -44):
        ins = locate_bore(bg, (x, y, -22.0), (0,0,1))
        s = ins["offset"].detail["start"]; e = ins["offset"].detail["end"]
        # carrier hole located on the insert's axis point
        h = locate_bore(bc, (s[0], s[1], -26.44), (0,0,1))
        loc[f"({x},{y})"] = {"insert_d": ins["diameter"].measured, "insert_len": ins["length"].measured, "insert_off_from_nominal": ins["offset"].measured, "insert_start": s, "insert_end": e,
                             "hole_off_from_insert_axis": h["offset"].measured, "hole_d": h["diameter"].measured}
res["coax"] = loc
# REQ-08: carrier material below the contact plane
big = 1000
below = Pos(0, 0, -24.94 + big/2) * Box(big, big, big)       # z in [-24.94, 975.06]
front = Pos(0, -52 + big/2, -24.94 + big/2) * Box(big, big, big)  # y > -52
back = Pos(0, -52 - big/2, -24.94 + big/2) * Box(big, big, big)   # y < -52
pf = cS & front; pb = cS & back
res["front_piece_vol"] = pf.volume; res["back_piece_vol"] = pb.volume
res["clear_g01_front"] = clearance(g01s, pf)
res["clear_g01_back"] = clearance(g01s, pb)
# per-gusset
for sx, nm in ((1, "gus+x"), (-1, "gus-x")):
    boxg = Pos(sx*53, -32, -4.94) * Box(4, 40, 40)
    res[f"{nm}_vol"] = common_volume(cS, boxg)
# assembly path: housing moved +Z (down in machine, away from the plate) then offered back
path = {}
for d in (40, 30, 20, 10, 5, 2, 1, 0.5, 0.1, 0.0):
    moved = Pos(0, 0, d) * g01s
    path[str(d)] = {"interf": common_volume(cS, moved).measured, "clear": clearance(cS, moved).measured}
res["path"] = path
# delivered assembly
a = read_step(ASM)
res["asm_labels"] = node_labels(a)
asol = solids(a)
res["asm_n_solids"] = len(asol)
per = []
for s in asol:
    S = Solid(s)
    per.append({"vol": S.volume, "bbox": [round(v,4) for v in (S.bounding_box().min.X, S.bounding_box().min.Y, S.bounding_box().min.Z, S.bounding_box().max.X, S.bounding_box().max.Y, S.bounding_box().max.Z)],
                "com_c": common_volume(S, cS).measured, "com_g01": common_volume(S, g01s).measured, "com_g04": common_volume(S, g04p).measured})
res["asm_parts"] = per
res["vols"] = {"carrier": cS.volume, "g01": g01s.volume, "g04": g04p.volume}
dump("m2_assembly", res)
print("done")
