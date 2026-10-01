"""Positive controls: one mutant of this job's tray (from the exported STEP) per check family; each check must FAIL."""
import sys, math, zipfile, re, shutil; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
import numpy as np, trimesh
from build123d import Box, Cylinder, Pos, Rot, Align, Solid, Shell, Location, Plane, Rectangle, export_step, export_stl
from tools.core import read_step, validity, common_volume, write_stl, compare_step
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide, overhang_census,
                           flat_ceiling_spans, radial_extent, clearance, mesh_census, mesh_deviation, min_wall_mesh)
from tools.result import Result
M = W / "mutants"; M.mkdir(exist_ok=True)
t = Solid(read_step(PART).wrapped)
e = read_step(E01).solids()[0]
board = e.moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
C = []
def ctl(family, mutant, gt):
    got = gt.status if gt.status in ("FAIL", "INCONCLUSIVE") else "PASS"
    C.append({"check": family, "mutant": mutant, "got": got, "measured": gt.measured, "required": gt.required})
    print(f"CONTROL {family:28s} {got:12s} {gt.measured} req {gt.required}  <- {mutant}", flush=True)
def one(s): ss = s.solids(); return ss[0] if len(ss) == 1 else s
def save(s, name): export_step(s, str(M / f"{name}.step"))
BOX = lambda x0, y0, z0, dx, dy, dz: Pos(x0, y0, z0) * Box(dx, dy, dz, align=(Align.MIN, Align.MIN, Align.MIN))
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
YCYL = lambda x, y0, z, r, L: Pos(x, y0, z) * Rot(-90, 0, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))

# 1 validity (degrade): one face removed -> open shell
fs = t.faces(); sh = Shell(fs[:-1])
ctl("validity (U-01)", "degrade: tray shell with one face removed", g("ctl", validity(sh)["naked_edges"], "==", 0))
# 2 envelope (resize): wall top raised to y 92.5
m2 = one(t + BOX(73, 91.9, -230, 3, 0.6, 160)); save(m2, "m2_wall_y92.5")
ctl("envelope (U-02, REQ-03, D-02)", "resize: wall top raised 0.5 to y 92.5", g("ctl", envelope(m2)["size_y"], "in", (91.9, 92.1)))
# 3 feature_census (remove): tie slot at z -176 filled
m3 = one(t + BOX(73, 86, -177, 3, 4, 2)); save(m3, "m3_slot_filled")
ctl("feature_census (U-05)", "remove: tie slot z -176 filled", g("ctl", feature_census(m3)["plane_faces"], "==", 42))
# 4 bore_census + locate_bore (relocate): flange hole x88 z-222 moved +0.5 in x
m4 = one((t + YCYL(88, 0, -222, 1.7, 4)) - YCYL(88.5, -1, -222, 1.7, 6)); save(m4, "m4_hole_moved_0.5")
ctl("bore_census/locate_bore (REQ-01, D-04a, D-05b, REQ-02)", "relocate: flange hole x88 z-222 moved 0.5 in +X", g("ctl", locate_bore(bore_census(m4), (88, 2, -222), (0, 1, 0))["offset"], "<=", 0.10))
# 5 min_wall (resize): web above tie slots thinned to 1.5 (wall top cut to y 91.5 across slot zone)
m5 = one(t - BOX(72, 91.5, -180, 5, 1, 70)); save(m5, "m5_web_1.5")
nop = m5
for py, pz in ((81.98, -157.52), (30.99, -157.51)):
    nop = one(nop - Pos(82.438, py, pz) * Box(4.0, 3.0, 3.0, align=(Align.MIN, Align.CENTER, Align.CENTER)))
ctl("min_wall (D-01a/b, D-06a)", "resize: web above the tie slots thinned 2.0 -> 1.5", g("ctl", min_wall(nop, spacing=0.7), ">=", 2.0))
ctl("min_wall_wide (U-06)", "resize: web above the tie slots thinned 2.0 -> 1.5", g("ctl", min_wall_wide(nop, spacing=0.7), ">=", 2.0))
# 6 overhang + flat ceiling (degrade): a mushroom cap on a stem off the wall, cap underside facing the bed (-X)
m6 = one(t + BOX(76, 48, -212, 4, 4, 4) + BOX(80, 40, -220, 2, 20, 20)); save(m6, "m6_cap")
fill = m6
for x, z in ((88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0)):
    fill = fill + YCYL(x, 0, z, 1.7, 4)
fill = one(fill)
ctl("overhang_census (D-03a)", "degrade: 20x20 cap on a 4x4 stem off the wall, ceiling facing the bed", g("ctl", overhang_census(fill, build_dir=(1, 0, 0), spacing=0.7), ">=", 45.0))
ctl("flat_ceiling_spans (D-03b)", "degrade: same cap (unsupported ceiling)", g("ctl", flat_ceiling_spans(m6, build_dir=(1, 0, 0), max_span=5.0, spacing=0.7), "<=", 5.0))
# 7 radial_extent (resize): H1 boss turned down to Ø7.8
m7 = one(t - (XCYL(76.0, 80.0, -100.0, 6.0, 7.0) - XCYL(75.9, 80.0, -100.0, 3.9, 7.2))); save(m7, "m7_boss_d7.8")
r1 = radial_extent(m7, (76.438, 80.0, -100.0), (1, 0, 0), (0, 1, 0), 0, 3.0, side="outer", r_max=6.0)
r2 = radial_extent(m7, (76.438, 80.0, -100.0), (1, 0, 0), (0, 1, 0), 180, 3.0, side="outer", r_max=6.0)
i1 = radial_extent(m7, (76.438, 80.0, -100.0), (1, 0, 0), (0, 1, 0), 0, 3.0, side="inner", r_max=6.0)
ctl("radial_extent (D-05a)", "resize: H1 insert boss Ø10 -> Ø7.8", g("ctl", Result("across", r1.measured + r2.measured, "mm"), ">=", 8.0))
ctl("radial_extent (J-05)", "resize: H1 insert boss Ø10 -> Ø7.8", g("ctl", Result("wall", r1.measured - i1.measured, "mm"), ">=", 3.0))
# 8 clearance (relocate): H6 pin moved +0.1 in z
m8 = one((t - XCYL(82.438, 30.99, -157.51, 0.9, 2.6)) + XCYL(82.438, 30.99, -157.41, 0.9, 2.5)); save(m8, "m8_pin_H6_z+0.1")
pin = one(m8 & (Pos(82.438, 30.99, -157.51) * Box(3.0, 2.6, 2.6, align=(Align.MIN, Align.CENTER, Align.CENTER))))
ctl("clearance (D-04d, U-03, E-01, D-04c)", "relocate: H6 pin moved 0.10 in +Z", g("ctl", clearance(pin, board), ">=", 0.30))
# 9 clearance == 0 seat contact (resize): H1 seat lowered 0.05
m9 = one(t - (XCYL(82.388, 80.0, -100.0, 5.1, 0.2))); save(m9, "m9_seat_low")
lay = one(m9 & (Pos(81.9, 80.0, -100.0) * Box(0.6, 10.2, 10.2, align=(Align.MIN, Align.CENTER, Align.CENTER))))
ctl("clearance == 0 (U-03 seat contact)", "resize: H1 seat lowered 0.05", g("ctl", clearance(lay, board), "==", 0.0))
# 10 common_volume (resize): H1 seat raised 0.06 (also the REQ-02 seat-x face reading)
m10 = one(t + (XCYL(82.438, 80.0, -100.0, 5.0, 0.06) - XCYL(82.3, 80.0, -100.0, 2.0, 0.3))); save(m10, "m10_seat_high")
ctl("common_volume (U-03 interference)", "resize: H1 seat raised 0.06", g("ctl", common_volume(m10, board), "<=", 0.0))
sx = max(f.bounding_box().max.X for f in m10.faces() if f.bounding_box().size.X < 1e-6 and abs(f.center().Y - 80) < 6 and abs(f.center().Z + 100) < 6 and f.bounding_box().min.X > 82)
ctl("seat-face reading (REQ-02)", "resize: H1 seat raised 0.06", g("ctl", Result("seat_x", sx, "mm"), "in", (82.39, 82.49)))
# 11 common_volume along the path (relocate): H5 pin moved 0.5 in +Y
m11 = one((t - XCYL(82.438, 81.98, -157.52, 0.9, 2.6)) + XCYL(82.438, 82.48, -157.52, 0.9, 2.5))
worst = max(common_volume(m11, board.moved(Location((dx, 0, 0)))).measured for dx in (2.0, 1.0, 0.5, 0.0))
ctl("common_volume path (U-03 b)", "relocate: H5 pin moved 0.5 in +Y", g("ctl", Result("path", worst, "mm3"), "<=", 0.0))
# 12 common_volume driver/faston boxes (degrade): a rib over the x88 z-78 screw and into the faston box
m12 = one(t + BOX(76, 4, -80, 14, 2, 2)); cyl = YCYL(88, 4, -78, 4.0, 116)
ctl("common_volume (REQ-04)", "degrade: 2x2 rib across the x88 z-78 driver path", g("ctl", common_volume(m12, cyl), "<=", 0.0))
m12b = one(t + BOX(76, 40, -150, 10, 2, 2))
ctl("common_volume (REQ-05, E-11)", "degrade: rib reaching x 86 inside the faston box", g("ctl", common_volume(m12b, BOX(85, 4, -195, 32, 88, 100)), "<=", 0.0))
# 13 sections (remove): gusset at z -88 removed; slot count with a slot filled
m13 = one(t - BOX(76.0001, 4.0001, -88, 25, 25, 3)); 
def sec(s, o, n, xd):
    pl = Plane(origin=o, z_dir=n, x_dir=xd); return (s & (pl * Rectangle(2000, 2000).face())).faces()
gus = sum(int(abs(sum(f.area for f in sec(m13, (0, 0, zc), (0, 0, 1), (1, 0, 0))) - 620) < 0.01) for zc in (-228.5, -210.5, -86.5, -71.5))
ctl("sections (E-06)", "remove: gusset z -88..-85", g("ctl", Result("gussets", gus, "count"), "==", 4))
ns = sum(len(f.inner_wires()) for f in sec(m3, (74.5, 0, 0), (1, 0, 0), (0, 0, 1)))
ctl("sections (E-11)", "remove: tie slot z -176 filled", g("ctl", Result("slots", ns, "count"), "==", 4))
# 14 compare_step (resize): re-read check of the delivered part file against the resized mutant
cs = compare_step(m2, PART)
ctl("compare_step (U-04)", "resize: wall top raised 0.5, compared with the delivered file", g("ctl", cs["volume_delta"], "<=", 0.0))
# 15 mesh_census (degrade): delivered STL with one triangle removed
md = trimesh.load(STL, process=False); md2 = trimesh.Trimesh(md.vertices, md.faces[1:], process=False); md2.export(M / "m15_hole.stl")
ctl("mesh_census (U-07)", "degrade: delivered STL with one triangle removed", g("ctl", mesh_census(M / "m15_hole.stl")["naked_edges"], "==", 0))
# 16 mesh_deviation / sagitta (degrade): mesh at 0.1 mm
wr = write_stl(t, M / "m16_coarse.stl", tolerance=0.1, angular_tolerance=0.5)
ctl("mesh_deviation (U-07)", "degrade: STL meshed at 0.1 mm / 0.5 rad", g("ctl", mesh_deviation(M / "m16_coarse.stl", t), "<=", 0.01))
ctl("mesh_sagitta (U-07)", "degrade: STL meshed at 0.1 mm / 0.5 rad", g("ctl", wr.checks["max_sagitta"], "<=", 0.01))
# 17 3MF-vs-STL comparison (relocate): one 3MF vertex moved 0.05
z = zipfile.ZipFile(TMF); xml = z.read("3D/3dmodel.model").decode()
vx = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml)])
tr = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml)])
vx[100, 0] += 0.05; m3 = trimesh.Trimesh(vx, tr, process=False)
pa = np.vstack([m3.vertices, m3.triangles_center]); sd = trimesh.proximity.closest_point(md, pa)[1].max()
ctl("3MF-vs-STL surface comparison (U-07)", "relocate: one 3MF vertex moved 0.05", g("ctl", Result("3mf_vs_stl", float(sd), "mm"), "<=", 1e-4))
# 18 min_wall_mesh (resize): STL of the thinned-web mutant
write_stl(nop, M / "m18_web.stl", tolerance=0.01, angular_tolerance=0.2)
ctl("min_wall_mesh (corroboration)", "resize: STL of the web-1.5 mutant (pins removed)", g("ctl", min_wall_mesh(M / "m18_web.stl"), ">=", 2.0 - 0.01))
import json; (W / "r06_controls.json").write_text(json.dumps(C, indent=1, default=str))
