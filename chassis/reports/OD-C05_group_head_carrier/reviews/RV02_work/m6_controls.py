"""Positive controls: mutants of the exported carrier, each check must FAIL on its mutant."""
import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from faces_lib import listing, shared_edges
from mesh_lib import *
from build123d import (Solid, Shell, Pos, Rot, Cylinder, Box, Polyline, make_face, extrude, Plane, export_step, export_stl)
from tools.core.validity import validity
from tools.core.step import compare_step, labels
from tools.core.boolean import common_volume
from tools.core.mesh import write_stl, mesh_sagitta
from tools.measure import (envelope, feature_census, bore_census, locate_bore, overhang_census, radial_extent,
                           clearance, interference, mesh_census, mesh_deviation)
from tools.core.shapes import faces as F
import numpy as np, math
MD = W / "mutants"; MD.mkdir(exist_ok=True)
s = Solid(solids(read_step(STEP))[0])
g01 = Solid(solids(read_step(G01))[0])
g04 = Pos(0, 0, -6.82) * Rot(0, 0, 6.05) * Solid(solids(read_step(G04))[0])
R = {}
def one(x):
    ss = solids(x)
    return Solid(ss[0]) if len(ss) == 1 else x
def save(m, name):
    export_step(m, str(MD / f"{name}.step"))
# A validity: open shell
fs = F(s)
from build123d import Face
sh = Shell([Face(f) for f in fs[1:]])   # drop one face
R["A_validity_open_shell"] = validity(sh)
# B envelope
mB1 = one(s + Pos(0, -102.25, 170) * Box(20, 0.5, 10)); save(mB1, "B1_rear_lip_y-102.5")
R["B1_env"] = envelope(mB1)
mB2 = one(s + Pos(0, -80, 202.56) * Box(10, 10, 45)); save(mB2, "B2_post_to_z225")
R["B2_env"] = envelope(mB2)
mB3 = one(s + Pos(0, 20, -30.19) * Box(40, 40, 0.5)); save(mB3, "B3_pad_below_top")
R["B3_env"] = envelope(mB3)
# helper to refill and recut holes
def fill_plate(x, y, m):
    return m + Pos(x, y, -27.44) * Cylinder(3.25, 5.0)
# C compare_step: hole (+44,+44) moved 0.5 in x
mE1 = fill_plate(44, 44, s)
mE1 = mE1 - Pos(44.5, 44, -28.94) * Cylinder(3.25, 2.0) - Pos(44.5, 44, -26.44) * Cylinder(1.7, 3.0)
mE1 = one(mE1); save(mE1, "E1_hole_44_44_moved_0p5")
R["C_compare_mutant_vs_file"] = compare_step(mE1, STEP)
bcE1 = bore_census(mE1)
R["E1_locate"] = locate_bore(bcE1, (44, 44, -26.44), (0, 0, 1))
R["E1_locate_cb"] = locate_bore(bcE1, (44, 44, -28.94), (0, 0, 1))
# D census: counterbore (+44,-44) filled (hole kept)
mD = one(s + Pos(44, -44, -28.94) * Cylinder(3.25, 2.0) - Pos(44, -44, -26.44) * Cylinder(1.7, 5.0)); save(mD, "D_cb_44_-44_filled")
R["D_census"] = feature_census(mD)
bcD = bore_census(mD)
R["D_locate_cb"] = locate_bore(bcD, (44, -44, -28.94), (0, 0, 1))
# E2 foot hole (35,-72) re-cut at 3.2
mE2 = one(s + Pos(35, -72, 178.06) * Cylinder(1.7, 4.0) - Pos(35, -72, 178.06) * Cylinder(1.6, 4.0)); save(mE2, "E2_foothole_d3p2")
R["E2_locate"] = locate_bore(bore_census(mE2), (35, -72, 178.06), (0, 0, 1))
# E3 foot counterbore (-35,-92) deepened by 1.0 (floor z 177.06)
mE3 = one(s - Pos(-35, -92, 176.56) * Cylinder(3.25, 1.0)); save(mE3, "E3_footcb_floor_177p06")
bcE3 = bore_census(mE3)
R["E3_locate_hole"] = locate_bore(bcE3, (-35, -92, 178.56), (0, 0, 1))
R["E3_locate_cb"] = locate_bore(bcE3, (-35, -92, 175.5), (0, 0, 1))
# E4 plate counterbore (-44,44) deepened to 2.5
mE4 = one(s - Pos(-44, 44, -27.69) * Cylinder(3.25, 0.5)); save(mE4, "E4_plate_cb_2p5_deep")
R["E4_locate_cb"] = locate_bore(bore_census(mE4), (-44, 44, -28.94), (0, 0, 1))
# F min_wall mutant saved for the background run: +x side wall thinned to 1.5 over a patch
mF = one(s - Pos(52.25, -80, 65) * Box(2.5, 20, 30)); save(mF, "F_sidewall_1p5")
# G 44 deg pointed window through the front wall
h = 10 * math.tan(math.radians(44.0))
G44 = extrude(make_face(Plane.XZ * Polyline((-10, 60), (10, 60), (10, 80), (0, 80 + h), (-10, 80), close=True)), amount=20, both=True)
mG = one(s - Pos(0, -55, 0) * G44); save(mG, "G_frontwall_window_44deg")
R["G_listing_least"] = min(r["angle"] for r in listing(mG) if r.get("down") and r["angle"] is not None and r["angle"] > 1e-6)
# overhang on the plugged mutant: plug as for nominal
plugs = None
for x in (44, -44):
    for y in (44, -44):
        p = Pos(x, y, -28.94) * Cylinder(3.25, 2.0); plugs = p if plugs is None else plugs + p
roof = extrude(make_face(Plane.YZ * Polyline((-58, 154.06), (-78, 174.06), (-98, 154.06), (-98, 180.06), (-58, 180.06), close=True)), amount=55, both=True)
for x in (35, -35):
    for y in (-72, -92):
        plugs = plugs + ((Pos(x, y, 163.06) * Cylinder(3.25, 26.0)) & roof)
R["G_overhang_plugged"] = overhang_census(one(mG + plugs), build_dir=(0, 0, 1))
# known-good for the listing: same window at 45.0 deg
G45 = extrude(make_face(Plane.XZ * Polyline((-10, 60), (10, 60), (10, 80), (0, 90), (-10, 80), close=True)), amount=20, both=True)
mG45 = one(s - Pos(0, -55, 0) * G45)
R["G45_listing_least"] = min(r["angle"] for r in listing(mG45) if r.get("down") and r["angle"] is not None and r["angle"] > 1e-6)
R["G45_overhang_plugged"] = overhang_census(one(mG45 + plugs), build_dir=(0, 0, 1))
# H bridge: flat-topped slot 20 wide through the front wall
mH = one(s - Pos(0, -55, 70) * Box(20, 20, 20)); save(mH, "H_frontwall_flat_slot20")
def flats(m):
    out = []
    for r in listing(m):
        if not r.get("down") or r["angle"] is None or r["angle"] >= 1.0: continue
        x, y, z = r["centre"]
        if abs(z + 29.94) < 1e-6: continue                         # bed
        if abs(r["area"] - 24.104) < 0.01 and (abs(z + 27.94) < 1e-6 or abs(z - 176.06) < 1e-6): continue   # exception
        pts = [p for p in []]
        out.append(r)
    return out
def span(m, r):
    from faces_lib import vz
    f = F(m)[r["i"]]
    pts = np.array(vz(f)); ext = pts.max(0) - pts.min(0)
    return float(min(e for e in ext[:2] if e > 1e-9))
fl = flats(mH)
R["H_flats"] = [(r["centre"], span(mH, r)) for r in fl]
# H2 valley ceiling: window with a V-notch top through the front wall
V = extrude(make_face(Plane.XZ * Polyline((-10, 60), (10, 60), (10, 80), (0, 70), (-10, 80), close=True)), amount=20, both=True)
mH2 = one(s - Pos(0, -55, 0) * V); save(mH2, "H2_frontwall_valley")
def pairs(m):
    L = listing(m); fsm = F(m)
    down = [r for r in L if r.get("down") and r["angle"] is not None and r["angle"] >= 1.0]
    out = []
    for a in range(len(down)):
        for b in range(a + 1, len(down)):
            for e in shared_edges(m, fsm[down[a]["i"]], fsm[down[b]["i"]]):
                ez = max(e[0][2], e[1][2])
                kind = "peak" if ez >= max(down[a]["zmax"], down[b]["zmax"]) - 1e-9 else ("valley" if ez <= min(down[a]["zmin"], down[b]["zmin"]) + 1e-9 else "other")
                out.append((kind, e))
    return out
R["H2_pairs"] = pairs(mH2)
R["nominal_pairs"] = pairs(s)
# I radial: bar into the hub window to r 26 at theta 90
mI = one(s + Pos(0, 28.5, -27.44) * Box(4, 5, 5)); save(mI, "I_hub_bar_r26")
R["I_radial_90"] = radial_extent(mI, (0, 0, 0), (0, 0, 1), (1, 0, 0), 90, -27.44, side="inner")
# J clearance / interference
mJ1 = Pos(0, 0, 3.1) * s
R["J1_interf"] = interference({"carrier": mJ1, "g01": g01, "g04": g04})
R["J1_clear_g04"] = clearance(mJ1, g04)
mJ2 = Pos(0, 0, -0.5) * s
R["J2_contact"] = clearance(mJ2, g01)
mJ3 = one(s + Pos(-50.75, -32, -22.94) * Box(0.5, 20, 4)); save(mJ3, "J3_gusset_bump_x-50.5")
big = 1000
front = Pos(0, -52 + big/2, -24.94 + big/2) * Box(big, big, big)
R["J3_req08_front"] = clearance(g01, mJ3 & front)
mJ4 = one(s + Pos(0, -51.25, 0) * Box(40, 0.5, 10)); save(mJ4, "J4_frontwall_bump_y-51.5")
back = Pos(0, -52 - big/2 + 1.0, -24.94 + big/2) * Box(big, big, big)   # y < -51, holds the bump
R["J4_req08_back"] = clearance(g01, mJ4 & back)
# K E-06 gussets removed
mK = one(s - Pos(53, -32, -4.94) * Box(4.2, 40.2, 40) - Pos(-53, -32, -4.94) * Box(4.2, 40.2, 40)); save(mK, "K_gussets_removed")
R["K_gusset_vol"] = [common_volume(mK, Pos(sx * 53, -32, -4.94) * Box(4, 40, 40)) for sx in (1, -1)]
# L meshes
wc = write_stl(s, MD / "L_coarse_0p1_0p5.stl", tolerance=0.1, angular_tolerance=0.5)
R["L_coarse_sagitta"] = wc.checks["max_sagitta"]
R["L_coarse_deviation"] = mesh_deviation(MD / "L_coarse_0p1_0p5.stl", s)
st = read_stl(STL); mm = read_3mf(MF3)["tris"]; co = read_stl(MD / "L_coarse_0p1_0p5.stl")
R["L_coarse_vs_3mf"] = {"coarse_tris": len(co), "3mf_tris": len(mm)}
# one triangle dropped
b = open(STL, "rb").read(); import struct
n = struct.unpack("<I", b[80:84])[0]
nb = b[:80] + struct.pack("<I", n - 1) + b[84:84 + 50 * (n - 1)]
(MD / "L_dropped_triangle.stl").write_bytes(nb)
R["L_dropped_census"] = mesh_census(MD / "L_dropped_triangle.stl")
dump("m6_controls", R); print("done")
