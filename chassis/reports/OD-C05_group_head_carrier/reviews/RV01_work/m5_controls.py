"""RV01 positive controls: mutants of the exported carrier, each run through the check family it tests."""
import json, sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from build123d import Box, Cylinder, Pos, Polygon, extrude, export_step, Shell, Compound, Solid
from tools.core import read_step, validity, compare_step, common_volume, write_stl, mesh_sagitta
from tools.core.shapes import faces
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, overhang_census,
                           radial_extent, clearance, interference, mesh_census, mesh_deviation)
from tools.result import gate
from lib_rv import downward_faces
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
W = J / "reviews/RV01_work"; M = W / "mutants"; M.mkdir(exist_ok=True)
P = J / "02_STEP_STL/od_c05_carrier_C1_v01.step"
part = read_step(P)
if not isinstance(part, Solid):
    part = part.solids()[0]
res = []
def rec(check, mutant, g):
    got = g.status if g.status in ("FAIL", "INCONCLUSIVE") else "PASS"
    res.append(dict(check=check, mutant=mutant, got=got, measured=g.measured, required=g.required, margin=g.margin))
    print(f"{check:34} {got:12} {g.measured!s:>22} {g.required:>18}  | {mutant}")
def save(shape, name):
    export_step(shape, str(M / f"{name}.step"))
def through_z(x, y, d):
    return Pos(x, y, -27.44) * Cylinder(d / 2, 12)
def plug8(s):
    for sx in (1, -1):
        for sy in (1, -1):
            s = s + Pos(sx * 44, sy * 44, -27.44) * Cylinder(3.25, 5)
    return s
def analytic_least(s):
    rows = [r for r in downward_faces(s) if r["least_deg"] is not None]
    keep = []
    for r in rows:
        if r["kind"] == "plane" and abs(r["at"][1] + 175.0) < 0.01: continue     # the bed face
        if r["kind"] == "cylinder":
            ax, loc = np.array(r["axis_dir"]), np.array(r["axis_loc"])
            if abs(abs(ax[2]) - 1) < 1e-9 and abs(abs(loc[0]) - 44) < 1e-6 and abs(abs(loc[1]) - 44) < 1e-6 and min(abs(r["radius"] - 1.7), abs(r["radius"] - 3.25)) < 0.06:
                continue                                                           # the named exception
        keep.append(r)
    return keep
from tools.result import Result
def R(name, value, unit, at=None): return Result(name, value, unit, at=at)
def bridge_span(rows):
    spans = []
    for r in rows:
        if r["least_deg"] >= 45 - 1e-3: continue
        spans.append(2 * r["radius"] if r["kind"] == "cylinder" else float("nan"))
    return max(spans) if spans else 0.0

# M1 validity: one face removed (open shell)
fs = faces(part)
from OCP.BRepBuilderAPI import BRepBuilderAPI_Sewing
sew = BRepBuilderAPI_Sewing(1e-6)
for f in fs[1:]: sew.Add(f)
sew.Perform(); open_shape = Compound(sew.SewedShape())
v = validity(open_shape)
rec("validity (U-01)", "front face removed: open shell", gate("U-01", v["naked_edges"], "==", 0, band=0))
rec("validity solid_count (U-01)", "front face removed: open shell", gate("U-01", v["solid_count"], "==", 1, band=0))
# M2 envelope: foot extended 1.06 mm behind its rear edge (z -71.0)
m2 = part + Pos(0, -173, -70.47) * Box(100, 4, 1.06); save(m2, "M2_foot_to_z-71")
e = envelope(m2)
rec("envelope (U-02 size_z)", "foot rear edge moved to z -71.0", gate("U-02", e["size_z"], "in", (44.9, 45.1), band=0.005))
rec("envelope (REQ-07 min_z)", "foot rear edge moved to z -71.0", gate("REQ-07", e["min_z"], ">=", -70.0, band=0.005))
rec("envelope (D-02 height)", "wall top raised to y 80 (255 tall)", gate("D-02", envelope(part + Pos(0, 65, -27.44) * Box(20, 30, 5))["size_y"], "<=", 250.0, band=0.005))
# M3 U-04 compare_step: the exported file against a relocated-hole mutant of it
m5 = part + through_z(44, 44, 6.5)
m5 = m5 - through_z(44.5, 44, 3.4) - Pos(44.5, 44, -28.94) * Cylinder(3.25, 2); save(m5, "M5_hole_moved_0.5")
cs = compare_step(m5, P)
rec("compare_step (U-04 volume_delta)", "file compared with a shape whose (+44,+44) hole moved 0.5 in x", gate("U-04", cs["volume_delta"], "<=", 0.0, band=0.001))
# M4 feature/bore census: counterbore (+44,-44) removed
m4 = part + Pos(44, -44, -28.94) * Cylinder(3.25, 2); save(m4, "M4_cb_removed")
fc = feature_census(m4)
rec("feature_census (U-05 bores)", "counterbore at (+44,-44) filled", gate("U-05", fc["bores"], "==", 14, band=0))
bc4 = bore_census(m4); lb = locate_bore(bc4, (44, -44, -28.94), (0, 0, 1))
rec("bore_census+locate_bore (REQ-02 dia)", "counterbore at (+44,-44) filled", gate("REQ-02", lb["diameter"], "in", (6.4, 6.6), band=0.005))
# M5 locate_bore: hole (+44,+44) relocated 0.5 mm
lb5 = locate_bore(bore_census(m5), (44, 44, -26.44), (0, 0, 1))
rec("locate_bore (REQ-01 offset)", "hole (+44,+44) moved 0.5 in x", gate("REQ-01", lb5["offset"], "<=", 0.10, band=0.005))
# M6 D-04a: foot hole resized to 3.2
m6 = part + Pos(35, -173, -40) * Cylinder(1.7, 4, rotation=(90, 0, 0)) - Pos(35, -173, -40) * Cylinder(1.6, 6, rotation=(90, 0, 0)); save(m6, "M6_foot_hole_3.2")
lb6 = locate_bore(bore_census(m6), (35, -173, -40), (0, 1, 0))
rec("locate_bore (D-04a dia)", "foot hole (+35, z -40) resized to 3.2", gate("D-04a", lb6["diameter"], ">=", 3.25, band=0.005))
# M7 min_wall: counterbore (+44,+44) enlarged to 10.6 (web 0.7)
m7 = part - Pos(44, 44, -28.94) * Cylinder(5.3, 2); save(m7, "M7_cb_10.6")
mw = min_wall(m7)
rec("min_wall (D-01a)", "counterbore (+44,+44) enlarged to 10.6: web 0.7", gate("D-01a", mw, ">=", 0.8, band=0.005))
rec("min_wall wide (U-06)", "counterbore (+44,+44) enlarged to 10.6: web 0.7", gate("U-06", R("min_wall_wide", mw.detail["wide"]["measured"], "mm"), ">=", 2.0, band=0.005))
# M8 overhang (tool, with the eight exception crowns plugged) and the analytic face angle and bridge span
pl = plug8(part); save(pl, "P0_plugged_nominal")
oc0 = overhang_census(pl, build_dir=(0, 1, 0))
print("plugged nominal overhang_census:", oc0.measured, oc0.status, oc0.reason, oc0.detail.get("below_min_deg"), oc0.detail.get("sampling_bound_deg"), oc0.at)
m8a = part - through_z(0, -40, 6.0); save(m8a, "M8a_round_hole_6_no_gable")
oc = overhang_census(plug8(m8a), build_dir=(0, 1, 0))
rec("overhang_census (D-03a)", "plain Ø6 hole along Z at (0,-40), no gable", gate("D-03a", oc, ">=", 45.0, band=0.001))
k = analytic_least(m8a); lm = min(k, key=lambda r: r["least_deg"])
rec("analytic face angle (D-03a)", "plain Ø6 hole along Z at (0,-40), no gable", gate("D-03a", R("least", lm["least_deg"], "deg", lm["at"]), ">=", 45.0, band=0.001))
rec("bridge span (D-03b)", "plain Ø6 hole along Z at (0,-40), no gable", gate("D-03b", R("span", bridge_span(k), "mm"), "<=", 5.0, band=0.005))
def teardrop(r, alpha):
    phi = math.radians(90 - alpha)
    pts = [(r * math.cos(phi), r * math.sin(phi)), (0, r / math.sin(phi)), (-r * math.cos(phi), r * math.sin(phi)), (0, 0)]
    return Pos(0, -40, -27.44) * (Cylinder(r, 12) + extrude(Polygon(*pts, align=None), amount=6, both=True))
m8b = part - teardrop(6, 44.0); save(m8b, "M8b_teardrop_44deg")
k = analytic_least(m8b); lm = min(k, key=lambda r: r["least_deg"])
rec("analytic face angle (D-03a)", "R6 teardrop at (0,-40), gable 44.0 deg, arc tangent", gate("D-03a", R("least", lm["least_deg"], "deg", lm["at"]), ">=", 45.0, band=0.001))
oc = overhang_census(plug8(m8b), build_dir=(0, 1, 0))
rec("overhang_census (D-03a)", "R6 teardrop at (0,-40), gable 44.0 deg, arc tangent", gate("D-03a", oc, ">=", 45.0, band=0.001))
m8c = part - teardrop(6, 45.0)
k = analytic_least(m8c); lm = min(k, key=lambda r: r["least_deg"])
print("known-good R6 teardrop 45 deg: analytic least", repr(lm["least_deg"]), lm["kind"], lm.get("where"))
kn = analytic_least(part); ln = min(kn, key=lambda r: r["least_deg"])
print("nominal analytic least outside exception", repr(ln["least_deg"]), ln["kind"], ln["at"], "faces", len(kn), "span", bridge_span(kn))
res.append(dict(note="nominal analytic", least=ln["least_deg"], at=ln["at"], plugged_census=[oc0.measured, oc0.status, oc0.reason, oc0.detail.get("below_min_deg")], teardrop45=lm["least_deg"]))
# M9 radial_extent: a bar into the hub window and one into the lower window
m9 = part + Pos(28.5, 0, -27.44) * Box(5, 4, 5) + Pos(0, -110 - 23.5, -27.44) * Box(4, 5, 5); save(m9, "M9_bars_in_windows")
rr = radial_extent(m9, (0, 0, -27.44), (0, 0, 1), (1, 0, 0), 0, 0.0, side="inner", r_min=0, r_max=30.0)
rec("radial_extent (REQ-04)", "4 x 5 bar from the hub window edge to r 26 at theta 0", gate("REQ-04", rr, ">=", 30.0, band=0.005))
rr = radial_extent(m9, (0, -110, -27.44), (0, 0, 1), (1, 0, 0), 270, 0.0, side="inner", r_min=0, r_max=25.0)
rec("radial_extent (REQ-08)", "4 x 5 bar from the lower window edge to r 21 at theta 270", gate("REQ-08", rr, ">=", 25.0, band=0.005))
# M10 assembly: carrier moved +3.1 along Z (into the housing, 1.9 from OD-G04)
from build123d import Rot
g01 = read_step(J / "00_Spec/inputs/OD-G01_housing_C1_v02.step")
g04 = Pos(0, 0, -6.82) * (Rot(0, 0, 6.05) * read_step(J / "00_Spec/inputs/OD-G04_brewing_gasket_support.step"))
m10 = Pos(0, 0, 3.1) * part
rec("interference (U-03 carrier|OD-G01)", "carrier moved +3.1 along Z", gate("U-03", interference({"c": m10, "g": g01})["c|g"], "<=", 0.0, band=0.001))
rec("clearance (U-03 carrier|OD-G04)", "carrier moved +3.1 along Z", gate("U-03", clearance(m10, g04), ">=", 2.0, band=0.005))
m10b = Pos(0, 0, -0.5) * part
rec("clearance (U-03 contact == 0)", "carrier moved -0.5 along Z (gap to the housing)", gate("U-03", clearance(m10b, g01), "==", 0.0, band=0.005))
# M11 E-06: gussets removed
m11 = part - Pos(48, -151, -49.94) * Box(4, 40, 40) - Pos(-48, -151, -49.94) * Box(4, 40, 40); save(m11, "M11_no_gussets")
gv = common_volume(m11, Pos(48, -151, -49.94) * Box(4, 40, 40))
rec("gusset volume (E-06)", "both gussets removed", gate("E-06", R("gusset", gv.measured, "mm3"), ">=", 3200.0 - 0.001, band=0.001))
# M12 meshes: a coarse STL, and the delivered STL with one triangle dropped
w = write_stl(part, M / "coarse_0.1_0.5.stl", tolerance=0.1, angular_tolerance=0.5)
rec("mesh_sagitta (U-07)", "STL meshed at tol 0.1 / 0.5 rad", gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=0.005))
rec("mesh_deviation (V-05)", "STL meshed at tol 0.1 / 0.5 rad", gate("U-07", mesh_deviation(M / "coarse_0.1_0.5.stl", part), "<=", 0.01, band=0.005))
b = (J / "02_STEP_STL/od_c05_carrier_C1_v01.stl").read_bytes(); n = int.from_bytes(b[80:84], "little")
(M / "stl_one_triangle_dropped.stl").write_bytes(b[:80] + (n - 1).to_bytes(4, "little") + b[84:84 + (n - 1) * 50])
rec("mesh_census (U-07 closed shell)", "delivered STL with its last triangle dropped", gate("U-07", mesh_census(M / "stl_one_triangle_dropped.stl")["naked_edges"], "==", 0, band=0))
cc = mesh_census(M / "coarse_0.1_0.5.stl")
rec("3MF/STL triangle comparison (U-07)", "coarse STL (tol 0.1) compared with the delivered 3MF", gate("U-07", R("tri", cc["triangles"].measured, "count"), "==", 4264, band=0))
(W / "m5_controls.json").write_text(json.dumps(res, indent=1, default=str))
