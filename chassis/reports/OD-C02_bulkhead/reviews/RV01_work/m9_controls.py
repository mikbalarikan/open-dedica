import json, math
import numpy as np
from pathlib import Path
from build123d import Box, Cylinder, Pos, Rot, Solid, Compound
from tools.core.step import read_step, write_step, compare_step
from tools.core.shapes import faces, solids
from tools.core.validity import validity
from tools.core.boolean import common_volume
from tools.core.mesh import write_stl
from tools.result import gate
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, radial_extent, clearance, mesh_census, mesh_deviation)
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); I = J/"00_Spec/inputs"; W = J/"reviews/RV01_work"; M = W/"mutants"; M.mkdir(exist_ok=True)
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
MM, DEG, MM3 = 0.005, 0.001, 0.001
res = {}
def rec(name, mutant, g):
    res[name] = {"mutant": mutant, "status": g.status, "measured": g.measured, "required": g.required, "at": g.at}
    print(name, g.status, g.measured, g.required)
def bore_cyl(x, y0, y1, z, r):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(r, abs(y1 - y0))
# 1 validity: an extra disjoint solid; an open shell
m = Compound([s, Pos(100, 100, -100) * Box(5, 5, 5)])
rec("validity.solid_count", "part + a loose 5 mm cube", gate("U-01", validity(m)["solid_count"], "==", 1, band=0))
from OCP.BRepBuilderAPI import BRepBuilderAPI_Sewing
sew = BRepBuilderAPI_Sewing(1e-6)
for f in faces(s)[1:]: sew.Add(f)          # leave out the front end face z -30
sew.Perform(); openshell = Compound(sew.SewedShape()) if False else sew.SewedShape()
from build123d import Shell
rec("validity.naked_edges", "the front end face z -30 removed (open shell)", gate("U-01", validity(Shell(openshell))["naked_edges"], "==", 0, band=0))
# 2 envelope: base rail widened on the wet side to x 58.5
m = s.fuse(Pos(58.75, 6, -135) * Box(0.5, 12, 210)).clean()
rec("envelope", "base rail wet face moved from x 59.0 to 58.5", gate("REQ-05", envelope(m)["min_x"], ">=", 59.0, band=MM))
rec("envelope.size", "same mutant, size_x", gate("U-02", envelope(m)["size_x"], "in", (11.9, 12.1), band=MM))
# 3 bore_census / feature_census / locate_bore: remove one bore, relocate another 0.5 mm
m_rm = s.fuse(bore_cyl(65, 0, 6.0, -225, 2.1)).clean()
rec("feature_census", "base bore z -225 filled (removed)", gate("U-05", feature_census(m_rm)["bores"], "==", 6, band=0))
m_mv = s.fuse(bore_cyl(65, 0, 6.0, -165, 2.1)).clean().cut(bore_cyl(65.5, -1, 6.0, -165, 2.0)).clean()
bc = bore_census(m_mv)
rec("locate_bore.offset", "base bore z -165 moved 0.5 mm to x 65.5", gate("REQ-01", locate_bore(bc, (65, 3, -165), (0, 1, 0))["offset"], "<=", 0.10, band=MM))
m_d = s.cut(bore_cyl(65, -1, 6.0, -105, 2.1)).clean()
rec("locate_bore.diameter", "base bore z -105 opened to 4.2", gate("D-05b", locate_bore(bore_census(m_d), (65, 3, -105), (0, 1, 0))["diameter"], "in", (3.95, 4.05), band=MM))
m_dp = s.cut(bore_cyl(65, -1, 6.5, -45, 2.0)).clean()
rec("locate_bore.depth", "base bore z -45 deepened to 6.5", gate("D-05b", locate_bore(bore_census(m_dp), (65, 3, -45), (0, 1, 0))["length"], "in", (5.9, 6.1), band=MM))
# 4 min_wall: a pocket in the wet face leaves the wall 0.6 thick (x 66.4 ... 67)
m_w = s.cut(Pos(64.7, 100, -100) * Box(3.4, 20, 20)).clean()
mw = min_wall(m_w, spacing=0.7)
rec("min_wall", "wet-face pocket 20 x 20 leaves the wall 0.6 thick", gate("D-01a", mw, ">=", 0.8, band=MM))
rec("min_wall_wide", "same mutant, 45 deg reading", gate("U-06", min_wall_wide(m_w, spacing=0.7), ">=", 2.0, band=MM))
# 5 overhang_census: window 1's gable replaced by a flat roof (refilled bores so only the window counts)
fill = s
for b in bore_census(s).detail["bores"]:
    y0, y1 = (0, 6.05) if b["open_ends"][0] else (208.95, 215)
    fill = fill.fuse(bore_cyl(b["start"][0], y0, y1, b["start"][2], 2.1)).clean()
m_o = fill.cut(Pos(65, 150, -196.5) * Box(6, 14, 7)).clean()     # box z -200..-193 full width 14 -> flat ceiling at z -193? keep gable above
m_o = m_o.cut(Pos(65, 150, -189.5) * Box(6, 14, 7)).clean()      # flat roof at z -186
oh = overhang_census(m_o, build_dir=(0, 0, 1), spacing=0.7)
rec("overhang_census", "window 1 cut square to z -186 (flat roof, gable removed)", gate("D-03a", oh, ">=", 45.0, band=DEG))
# 6 radial_extent: window 1 enlarged to 15; top rail narrowed to x 62 ... 68
m_r = s.cut(Pos(65, 150, -200) * Rot(0, 90, 0) * Cylinder(7.5, 6)).clean()
r = radial_extent(m_r, (0, 150, -200), (1, 0, 0), (0, 0, 1), 180.0, 65.0, side="inner")
from tools.result import Result
rec("radial_extent.window", "window 1 round part opened to 15.0", gate("REQ-04", Result("window_d", 2 * r.measured, "mm", at=r.at), "in", (13.9, 14.1), band=MM))
m_t = s.cut(Pos(60.75, 211, -135) * Box(2.5, 8.2, 210)).clean().cut(Pos(69.25, 211, -135) * Box(2.5, 8.2, 210)).clean()
px = radial_extent(m_t, (65, 209, -60), (0, 1, 0), (1, 0, 0), 0.0, 3.0, side="outer")
rec("radial_extent.J-05", "top rail narrowed to x 62 ... 68", gate("J-05", Result("wall", px.measured - 2.0, "mm", at=px.at), ">=", 3.0, band=MM))
# 7 clearance / common_volume: bulkhead moved -X 5 mm into the pump; lifted 0.5 off the plate
pump = read_step(I/"OD-H01_ulka_ep5_pump.step")
from OCP.gp import gp_Trsf
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
tr = gp_Trsf(); tr.SetValues(0, 0, 1, 0, 0, -1, 0, 40, 1, 0, 0, -205)
pump = Solid(BRepBuilderAPI_Transform(solids(pump)[0], tr, True).Shape())
plate = read_step(I/"OD-C01_base_frame.step")
m_x = Pos(-5, 0, 0) * s
rec("clearance", "bulkhead moved 5 mm toward -X", gate("U-03", clearance(m_x, pump), ">=", 3.0, band=MM))
m_x2 = Pos(-10, 0, 0) * s
rec("common_volume", "bulkhead moved 10 mm toward -X (into the pump)", gate("U-03", common_volume(m_x2, pump), "<=", 0.0, band=MM3))
m_y = Pos(0, 0.5, 0) * s
rec("clearance.contact", "bulkhead lifted 0.5 off the plate", gate("U-03", clearance(m_y, plate), "==", 0.0, band=MM))
m_z = Pos(0, 0, 0.5) * s
pc = bore_census(plate); bz = locate_bore(bore_census(m_z), (65, 3, -44.5), (0, 1, 0))
rec("locate_bore.coax", "bulkhead moved 0.5 along +Z: plate hole read at the bore axis", gate("U-03", locate_bore(pc, (65, -3, -44.5), (0, 1, 0))["offset"], "<=", 0.10, band=MM))
# 8 mesh: coarse STL and an STL with one triangle dropped
wc = write_stl(s, M/"coarse.stl", tolerance=0.2, angular_tolerance=0.8)
rec("mesh_deviation", "STL meshed at 0.2 mm / 0.8 rad", gate("U-07", mesh_deviation(M/"coarse.stl", s), "<=", 0.01, band=MM))
import trimesh
from tools.measure.wall import load_mesh
mm = load_mesh(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.stl"); mm2 = trimesh.Trimesh(mm.vertices, mm.faces[1:], process=False); mm2.export(M/"holed.stl")
rec("mesh_census", "STL with one triangle dropped", gate("U-07", mesh_census(M/"holed.stl")["naked_edges"], "==", 0, band=0))
# 9 compare_step: the part compared with a mutant file
write_step(m_w, M/"pocket.step", timestamp="2026-09-30T00:00:00")
cs = compare_step(s, M/"pocket.step")
rec("compare_step", "the exported part against a re-export with a wall pocket", gate("U-04", cs["volume_delta"], "<=", 0.0, band=MM3))
# 10 face rays (REQ-02 reading): wet face moved to x 62.5 over y 50..60
m_f = s.fuse(Pos(62.75, 55, -100) * Box(0.5, 10, 10)).clean()
rr = radial_extent(m_f, (0, 55, -100), (0, 0, 1), (1, 0, 0), 0.0, 0.0, side="outer")
x0 = rr.detail["material"][0][0]
rec("face_rays", "a 0.5 boss on the wet face at (62.5, 55, -100)", gate("REQ-02", Result("wet_face_x", x0, "mm", at=(x0, 55, -100)), "in", (62.9, 63.1), band=MM))
(W/"m9_controls.json").write_text(json.dumps(res, indent=1, default=str))
