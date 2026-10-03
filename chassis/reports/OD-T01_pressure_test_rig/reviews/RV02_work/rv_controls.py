"""RV02 positive controls: mutants of the delivered rig, each check must FAIL."""
import json, sys, math
from pathlib import Path
import numpy as np, trimesh
sys.path.insert(0, str(Path(__file__).parent))
from rv_pose import *
from build123d import Box, Cylinder, Solid, Shell, Compound, Location
from tools.result import gate
from tools.core.validity import validity
from tools.core.boolean import common_volume
from tools.core import step as st
from tools.core.mesh import write_stl, mesh_sagitta
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, flat_ceiling_spans, clearance, mesh_census, mesh_deviation,
                           min_wall_mesh, radial_extent)
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN, TopAbs_OUT
OUT = W / "reviews/RV02_work"; M = OUT / "mutants"; M.mkdir(exist_ok=True)
rig = load_rig()
C = []
def rec(check, mutant, g):
    C.append({"check": check, "mutant": mutant, "measured": g.measured, "status": g.status, "got": "FAIL" if g.status == "FAIL" else g.status})
    print(C[-1], flush=True)
def ycyl(x, z, r, y0, y1):
    return Location((x, (y0 + y1) / 2, z)) * Location((0, 0, 0), (1, 0, 0), -90) * Cylinder(r, y1 - y0)
def box(x0, x1, y0, y1, z0, z1):
    return Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)) * Box(x1 - x0, y1 - y0, z1 - z0)
def one(s):
    return Solid(s.solids()[0].wrapped) if len(s.solids()) == 1 else s
# 1 validity: two solids
two = Compound([rig, Location((300, 0, 0)) * rig])
rec("validity (solid_count)", "rig plus a copy relocated 300 in X", gate("U-01", validity(two)["solid_count"], "==", 1, band=0))
# 2 naked edges: one face removed
fs = rig.faces(); sh = Shell(fs[1:])
rec("validity (naked_edges)", "rig shell with one face removed", gate("U-01", validity(sh)["naked_edges"], "==", 0, band=0))
# 3 envelope
m3 = one(rig + box(119.9, 121.0, 0, 10, -60, 60))
rec("envelope (U-02, D-02)", "base resized +1.0 at +X", gate("U-02", envelope(m3)["size_x"], "in", (239.9, 240.1), band=0.005))
# 4 bore removed
m4 = one(rig + ycyl(44, 44, 1.75, 134.0, 140.0))
fc = feature_census(m4)
rec("feature_census / bore_census (U-05)", "3.4 hole at (44, 44) removed (plugged)", gate("U-05", fc["bores"], "==", 13, band=0))
# 5 relocated hole
m5 = one(one(rig + ycyl(44, 44, 1.75, 134.0, 140.0)) - ycyl(44.5, 44, 1.7, 134.0, 141.0))
loc = locate_bore(bore_census(m5), (44, 137.5, 44), (0, 1, 0))
rec("locate_bore offset (REQ-01)", "3.4 hole at (44, 44) relocated +0.5 in X", gate("REQ-01", loc["offset"], "<=", 0.10, band=0.005))
# 6 resized hole
m6 = one(one(rig + ycyl(44, 44, 1.75, 134.0, 140.0)) - ycyl(44, 44, 1.6, 134.0, 141.0))
loc6 = locate_bore(bore_census(m6), (44, 137.5, 44), (0, 1, 0))
rec("locate_bore diameter (D-04a, REQ-01)", "3.4 hole at (44, 44) resized to 3.2", gate("D-04a", loc6["diameter"], ">=", 3.25, band=0.005))
# 7 wall: counterbore (-44,-44) deepened to y 135.6
m7 = one(rig - ycyl(-44, -44, 3.25, 135.6, 141.0))
st.write_step(Solid(m7.wrapped), M / "mut_cbore_deep.step", timestamp="2026-10-03T00:00:00") if False else None
mw = min_wall(m7)
rec("min_wall (D-01a, D-01b, D-06a)", "counterbore (-44, -44) deepened to y 135.6: 0.6 under the head", gate("D-01a", mw, ">=", 0.8, band=0.005))
rec("min_wall_wide (U-06)", "same deepened counterbore", gate("U-06", min_wall_wide(m7), ">=", 2.0, band=0.005))
# 8 overhang & bridge: plugged copy plus a flat-roofed slot through the plate
plug = rig
for x in (-44, 44):
    for z in (-44, 44):
        plug = plug + ycyl(x, z, 1.8, 135.0, 140.0)
m8 = one(one(plug) - box(55, 65, 134, 161, 0, 5))
rec("overhang_census (D-03a)", "plugged copy with a 10-wide flat-roofed slot through the plate, x 55..65, z 0..5", gate("D-03a", overhang_census(m8, build_dir=(0, 0, 1), min_deg=45), ">=", 45, band=0.001))
rec("flat_ceiling_spans (D-03b)", "same slot", gate("D-03b", flat_ceiling_spans(m8, build_dir=(0, 0, 1), max_span=5.0), "<=", 5.0, band=0.005))
# 9 clearance REQ-04a: block on the +X wall's inner front
H, G04, G10, _, _ = identify()
m9 = one(rig + box(62, 75.5, 80, 100, 25, 40))
least = min(clearance(m9, place(G10, phi=p)).measured for p in np.arange(-60, 15.001, 5.0))
from tools.result import Result
rec("clearance (REQ-04 sweep)", "block x 62..75, y 80..100, z 25..40 on the +X wall's inner front, phi -60..+15", gate("REQ-04", Result("clearance", least, "mm"), ">=", 5.0, band=0.005))
# 10 pair-B: window resized to R 29.5
m10 = one(rig - ycyl(0, 0, 29.5, 134, 161)) if False else None
from build123d import Edge
win_small = one(rig + ycyl(0, 0, 30.2, 135.0, 160.0)) 
win_small = one(win_small - ycyl(0, 0, 29.5, 134.0, 161.0))
pb = clearance(win_small, Edge.make_line((10.641441, 135.0, -15.776585), (10.641441, 160.0, -15.776585)))
rec("clearance (REQ-03 pair-B)", "window filled and re-cut at R 29.5 (no teardrop)", gate("REQ-03", pb, ">=", 10.87, band=0.005))
# 11 seat contact
rec("clearance (U-03 seat contact)", "housing relocated 0.2 down", gate("U-03", clearance(rig, place(H, dy=-0.2)), "==", 0.0, band=0.005))
# 12 interference
rec("interference / common_volume (U-03, REQ-06, REQ-07)", "housing relocated 0.5 up into the plate", gate("U-03", common_volume(rig, place(H, dy=0.5)), "<=", 0.0, band=0.001))
m12 = one(rig + ycyl(44, 44, 4.0, 160.0, 165.0))
rec("interference / common_volume (REQ-07 probe)", "boss r 4 on the (44, 44) screw axis above the plate", gate("REQ-07", common_volume(m12, ycyl(44, 44, 3.0, 160, 300)), "<=", 0.0, band=0.001))
# 13 compare_step: deepened counterbore shape vs the delivered file
cs = st.compare_step(Solid(m7.wrapped), W / "02_STEP_STL/od_t01_rig_C1_v02.step")
rec("compare_step (U-04)", "deepened counterbore shape compared with the delivered STEP", gate("U-04", cs["volume_delta"], "<=", 0.0, band=0.001))
# 14 sagitta: coarse remesh
wr = write_stl(rig, M / "coarse.stl", tolerance=0.1, angular_tolerance=0.5)
rec("stl_max_sagitta (U-07)", "rig re-meshed at 0.1 mm / 0.5 rad", gate("U-07", wr.checks["max_sagitta"], "<=", 0.01, band=0.005))
# 15 mesh_census: triangle removed
mesh = trimesh.load(W / "02_STEP_STL/od_t01_rig_C1_v02.stl", process=False)
holed = trimesh.Trimesh(mesh.vertices, mesh.faces[:-1], process=False); holed.export(M / "holed.stl")
rec("mesh_census (U-07, V-05)", "delivered STL with its last triangle removed", gate("U-07", mesh_census(M / "holed.stl")["naked_edges"], "==", 0, band=0))
# 16 mesh_deviation: coarse STL against the shape
rec("mesh_deviation (U-07)", "coarse STL (0.1 mm) against the delivered B-rep", gate("U-07", mesh_deviation(M / "coarse.stl", rig), "<=", 0.01, band=0.005))
# 17 min_wall_mesh: deep counterbore STL
write_stl(m7, M / "deep.stl", tolerance=0.01, angular_tolerance=0.1)
rec("min_wall_mesh (D-01b corroboration)", "STL of the deepened counterbore mutant", gate("D-01b", min_wall_mesh(M / "deep.stl"), ">=", 2.0 - 0.01, band=0.005))
# 18 REQ-02 grid classifier: 0.5 pocket in the underside
m18 = one(rig - box(45, 49, 134, 135.5, -20, -10))
cls = BRepClass3d_SolidClassifier(m18.wrapped); bad = 0
for x in np.arange(-49.5, 50.0, 1.0):
    for z in np.arange(-49.5, 50.0, 1.0):
        if math.hypot(x, z) < 31 or (abs(x) < 31 and 0 < z < 44): continue
        if any(math.hypot(x - sx, z - sz) < 2.0 for sx in (-44, 44) for sz in (-44, 44)): continue
        cls.Perform(gp_Pnt(x, 135.002, z), 1e-6); a = cls.State(); cls.Perform(gp_Pnt(x, 134.998, z), 1e-6); b = cls.State()
        if not (a == TopAbs_IN and b == TopAbs_OUT): bad += 1
rec("underside grid classifier (REQ-02)", "1.5-deep pocket x 45..49, z -20..-10 in the underside", gate("REQ-02", Result("grid_bad", bad, "count"), "==", 0, band=0))
# 19 apex: rig relocated +0.5 in Z -> radial_extent along +Z
m19 = Location((0, 0, 0.5)) * rig
ap = radial_extent(m19, (0, 147.5, 0), (0, 1, 0), (0, 0, 1), 0.0, 0.0, side="inner")
rec("radial_extent apex (REQ-03)", "rig relocated +0.5 in Z", gate("REQ-03", ap, "in", (42.35, 42.67), band=0.005))
# 20 flank-plane angle: rig rotated 2 deg about Y changes the flank normals -> recorded via overhang census plane least
(OUT / "controls.json").write_text(json.dumps(C, indent=1, default=str))
