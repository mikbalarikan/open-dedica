"""RV01 positive controls: one mutant of this job's parts per check family; each must FAIL
its gate with the same comparison used in the review."""
import sys, math, struct
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
import numpy as np
from tools.result import gate
from tools.core import validity, compare_step, common_volume, write_stl
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, overhang_census,
                           flat_ceiling_spans, clearance, radial_profile, mesh_census, mesh_deviation)
from build123d import Box, Cylinder, Pos, Rot, Solid, Compound, Align
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.BRepExtrema import BRepExtrema_DistShapeShape

R = one(load("od_c13_right_C1_v01.step")); L = one(load("od_c12_left_C1_v01.step"))
BR = one(load("od_c16_bracket_C1_v01.step"))
refs = references()
C01, C07, C10 = refs["OD-C01"], refs["OD-C07"], refs["OD-C10"]
rows = []
def rec(check, mutant, g):
    rows.append({"check": check, "mutant": mutant, "got": "FAIL" if g.status == "FAIL" else g.status,
                 "measured": g.measured, "required": g.required, "status": g.status})
    print(check, "|", mutant, "|", g.status, g.measured, g.required)

# validity: the bracket file plus a second, overlapping-free copy -> two solids
two = Compound([BR, Pos(30, 0, 0) * BR])
rec("validity (solid_count)", "bracket with a second solid beside it", gate("U-01", validity(two)["solid_count"], "==", 1, band=0))
# envelope: right panel lengthened 0.5 at its front end
m = R.fuse(Pos(118.5, 107.5, 90.25) * Box(3, 215, 0.5))
rec("envelope", "OD-C13 wall lengthened 0.5 at z +90", gate("U-02", envelope(m)["size_z"], "in", (384.9, 385.1), band=BAND_MM))
# compare_step: delivered bracket file against a bracket with its insert bore 0.5 deeper
deeper = BR.cut(Pos(-6.25, 10, 0) * Rot(0, 90, 0) * Cylinder(2.0, 0.5))
deeper.label = "od_c16_bracket"
rec("step_roundtrip/compare_step", "bracket insert bore 0.5 deeper vs the delivered file",
    gate("U-04", compare_step(deeper, EXP / "od_c16_bracket_C1_v01.step")["volume_delta"], "<=", 0.0, band=BAND_MM3))
# feature_census / bore_census: one panel hole filled
filled = R.fuse(Pos(118.5, 10, -15) * Rot(0, 90, 0) * Cylinder(1.7, 3.0)).clean()
rec("feature_census (bores)", "OD-C13 middle hole filled", gate("U-05", feature_census(filled)["bores"], "==", 3, band=0))
# locate_bore offset: right panel hole relocated 0.5 in z (filled and re-cut)
moved = filled.cut(Pos(118.5, 10, -14.5) * Rot(0, 90, 0) * Cylinder(1.7, 3.0))
lb = locate_bore(bore_census(moved), (118.5, 10, -15), (1, 0, 0))
rec("locate_bore (offset)", "OD-C13 middle hole moved 0.5 in z", gate("REQ-03", lb["offset"], "<=", 0.10, band=BAND_MM))
# locate_bore diameter: bracket plate hole shrunk to 3.2
small = BR.fuse(Pos(-12.5, 1.5, 0) * Rot(90, 0, 0) * Cylinder(1.7, 3.0)).cut(Pos(-12.5, 1.5, 0) * Rot(90, 0, 0) * Cylinder(1.6, 3.0))
lb = locate_bore(bore_census(small), (-12.5, 1.5, 0), (0, 1, 0))
rec("bore_census/locate_bore (diameter)", "bracket plate hole resized to 3.2", gate("D-04a", lb["diameter"], ">=", 3.25, band=BAND_MM))
# coaxiality (two locate_bore axes): panel hole moved 0.5 against the placed bracket
br = bracket_pose(BR, "R", -15.0)
a = locate_bore(bore_census(br), (114, 10, -15), (1, 0, 0))["offset"].detail
b = locate_bore(bore_census(moved), (118.5, 10, -15), (1, 0, 0))["offset"].detail
s1, s2 = np.array(a["start"]), np.array(b["start"])
w = s1 - s2; w[0] = 0
from tools.result import Result
rec("coaxiality (locate_bore x2)", "OD-C13 middle hole moved 0.5 vs placed bracket R2",
    gate("U-03", Result("coax_offset", float(np.linalg.norm(w)), "mm"), "<=", 0.20, band=BAND_MM))
# min_wall: OD-C12 relief deepened to x -118.5 (wall 1.5)
deep = L.cut(Pos(-118.2, 27.5, -94.5) * Box(0.6, 55, 131))
rec("min_wall", "OD-C12 relief floor moved to -118.5 (wall 1.5)", gate("D-01b", min_wall(deep, spacing=0.6), ">=", 2.0, band=BAND_MM))
# J-05 exact face distance: insert bore 1.0 deeper (web 2.25)
d7 = BR.cut(Pos(-6.5, 10, 0) * Rot(0, 90, 0) * Cylinder(2.0, 1.0))
from tools.core.shapes import faces as tf
from build123d import Face
bf = [f for f in tf(d7) if (Face(f).geom_type.name == "CYLINDER" and abs(Face(f).radius - 2.0) < 1e-6)
      or (Face(f).geom_type.name == "PLANE" and abs(Face(f).center().X + 7.0) < 1e-6)]
cb = [f for f in tf(d7) if Face(f).geom_type.name == "CYLINDER" and abs(Face(f).radius - 3.25) < 1e-6]
dmin = min((lambda d: (d.Perform(), d.Value())[1])(BRepExtrema_DistShapeShape(x, y)) for x in bf for y in cb)
rec("J-05 exact face distance", "bracket insert bore 7.0 deep (web to counterbore 2.25)",
    gate("J-05", Result("insert_web", dmin, "mm"), ">=", 3.0, band=BAND_MM))
# overhang_census + flat_ceiling_spans: a block hung under OD-C13's rail
hung = R.fuse(Pos(111.5, 200, -75) * Box(3, 10, 50))
rec("overhang_census", "OD-C13 block x110..113 hung under the rail (print -X)",
    gate("D-03a", overhang_census(hung, build_dir=(-1, 0, 0), spacing=0.6), ">=", 45.0, band=BAND_DEG))
rec("flat_ceiling_spans", "same block: its x 113 face a 10 deep ceiling",
    gate("D-03b", flat_ceiling_spans(hung, build_dir=(-1, 0, 0), max_span=5.0, spacing=0.6), "<=", 5.0, band=BAND_MM))
# overhang outside the exception on the bracket: a lip on its outer face
blip = BR.fuse(Pos(1.5, 14, 0) * Box(3, 4, 16))
filled_b = blip.fuse(Pos(-3.0, 10.0, 0.0) * Rot(0, 90, 0) * Cylinder(2.0, 6.0))
rec("overhang_census (bracket, exception filled)", "bracket with a 3 x 4 ledge off its outer face",
    gate("D-03a", overhang_census(filled_b, build_dir=(0, 1, 0)), ">=", 45.0, band=BAND_DEG))
# clearance: OD-C13 moved out 0.2 -> lip gap 0.2 and bracket contact gap 0.2
out02 = Pos(0.2, 0, 0) * R
lip = out02 & (Pos(0, 265, 0) * Box(400, 100, 800))
rec("clearance (lip, D-04d)", "OD-C13 relocated +0.2 in x", gate("D-04d", clearance(lip, C10), ">=", 0.30, band=BAND_MM))
rec("clearance (designed contact)", "OD-C13 relocated +0.2 in x vs bracket R2",
    gate("U-03", clearance(out02, br), "==", 0.0, band=BAND_MM))
in05 = Pos(0.5, 0, 0) * L
rec("clearance (other pairs)", "OD-C12 relocated 0.5 inward vs OD-C07",
    gate("REQ-04", clearance(in05, C07), ">=", 0.5, band=BAND_MM))
# interference: bracket lowered 0.5 into the plate
low = Pos(0, -0.5, 0) * br
rec("interference/common_volume", "bracket R2 relocated 0.5 down into OD-C01",
    gate("U-03", common_volume(low, C01), "<=", 0.0, band=BAND_MM3))
# path stepper: lid lowered onto OD-C13 relocated +0.5 (toe at 117.1)
o5 = Pos(0.5, 0, 0) * R
worst = 0.0
for k in range(40, -1, -1):
    r = common_volume(Pos(0, k, 0) * C10, o5)
    worst = max(worst, r.measured if r.ok else float("inf"))
rec("assembly path stepper", "lid lowered over OD-C13 relocated +0.5 in x",
    gate("U-03", Result("path_interference", worst, "mm3"), "<=", 0.0, band=BAND_MM3))
# REQ-07 keep-out: a 2 mm boss on bracket R3 inside its driver cylinder
boss = br.fuse(Pos(104.5, 17, -15) * Rot(90, 0, 0) * Cylinder(3.0, 2.0))
drv = Pos(104.5, 115.5, -15) * Rot(90, 0, 0) * Cylinder(4.0, 199.0)
rec("interference (REQ-07 access)", "bracket R2 with a 2 tall boss over its screw",
    gate("REQ-07", common_volume(drv, boss), "<=", 0.0, band=BAND_MM3))
# radial_profile: bracket top cut to y 13 (3 above the insert axis)
cut13 = BR.cut(Pos(-9.5, 14.5, 0) * Box(19, 3, 16))
rp = radial_profile(cut13, (0, 10, 0), (-1, 0, 0), (0, 1, 0), list(range(0, 360, 15)), (0.0, 6.0), margin=(0.0, 0.0),
                    z_step=0.25, r_min=2.0)
mn = rp["min"]
rec("radial_profile", "bracket top lowered to y 13", gate("D-05a", Result("across", 2 * mn.measured, "mm") if mn.ok else mn, ">=", 8.0, band=BAND_MM))
# section-based wedge reading: apex raised to 220 (slope 52.5 deg)
from build123d import Polyline, make_face, extrude, Plane
tri = Plane.XY.offset(-100.5) * make_face(Polyline((110, 218.8), (110, 220.0), (116.0, 218.8), close=True))
steeper = R.fuse(extrude(tri, 1.0))
s = BRepAlgoAPI_Section(steeper.wrapped, gp_Pln(gp_Pnt(0, 0, -100), gp_Dir(0, 0, 1))); s.Build()
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopoDS import TopoDS
from build123d import Edge
ex = TopExp_Explorer(s.Shape(), TopAbs_EDGE); ang = []
while ex.More():
    e = Edge(TopoDS.Edge_s(ex.Current())); a0, a1 = e.position_at(0), e.position_at(1)
    if abs(a0.X - a1.X) > 1e-3 and abs(a0.Y - a1.Y) > 1e-3:
        ang.append(math.degrees(math.atan2(abs(a0.X - a1.X), abs(a0.Y - a1.Y))))
    ex.Next()
worst_ang = max(ang, key=lambda v: abs(v - 60))
rec("section wedge reading", "OD-C13 lip with a bump raising its top at z -100",
    gate("REQ-02", Result("slope", worst_ang, "deg"), "in", (59.0, 61.0), band=BAND_DEG))
# mesh_deviation: a coarse STL of the bracket
cw = write_stl(load("od_c16_bracket_C1_v01.step"), WORK / "mut_coarse_bracket.stl", tolerance=0.1, angular_tolerance=1.0)
rec("mesh_deviation", "bracket STL at tol 0.1, 1.0 rad", gate("U-07", mesh_deviation(WORK / "mut_coarse_bracket.stl", BR), "<=", 0.01, band=BAND_MM))
# mesh_census: one triangle dropped from the delivered bracket STL
raw = (EXP / "od_c16_bracket_C1_v01.stl").read_bytes()
n = struct.unpack("<I", raw[80:84])[0]
mut = raw[:80] + struct.pack("<I", n - 1) + raw[84 + 50:]
(WORK / "mut_hole_bracket.stl").write_bytes(mut)
rec("mesh_census (naked edges)", "delivered bracket STL with one triangle removed",
    gate("U-07", mesh_census(WORK / "mut_hole_bracket.stl")["naked_edges"], "==", 0, band=0))
# REQ-06 distance arithmetic: a position moved to x 114 (6 from the edge)
rec("REQ-06 distance arithmetic", "insert position moved to (114, -15)",
    gate("REQ-06", Result("edge_distance", 120 - 114.0, "mm"), ">=", 8.0, band=BAND_MM))
# E-06: lip detached 0.5 from the rail -> two solids
lipsolid = R & (Pos(0, 265, 0) * Box(400, 100, 800))
body = R.cut(Pos(0, 265, 0) * Box(400, 100, 800))
det = Compound([body, Pos(0, 0.5, 0) * lipsolid])
rec("E-06 one solid (validity + section)", "OD-C13 lip lifted 0.5 off the rail",
    gate("E-06", validity(det)["solid_count"], "==", 1, band=0))
dump(rows, "controls.json")
