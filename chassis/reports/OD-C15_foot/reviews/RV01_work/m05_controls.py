"""RV01 measurement 5: U-04 on a detached copy, STL vertex comparison, and positive controls (mutants of this foot)."""
import json, math, struct
from pathlib import Path
import numpy as np
from build123d import Box, Cylinder, Polygon, extrude, Location, Align, Pos, Solid, Shell, scale
from tools.core import read_step, validity, step_roundtrip, compare_step, write_stl
from tools.core.boolean import common_volume
from tools.core.shapes import faces
from tools.result import gate
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, overhang_census,
                           flat_ceiling_spans, clearance, interference, radial_extent, radial_profile,
                           mass_properties, mesh_census, mesh_deviation)

W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet"); R = W / "reviews/RV01_work"
DEL = W / "02_STEP_STL/od_c15_foot_C1_v01.step"
read = read_step(DEL)
def leaf(s):
    ch = list(getattr(s, "children", ()) or ()); return leaf(ch[0]) if ch else s
foot = Solid(leaf(read).wrapped); foot.label = "od_c15_foot"
plate = read_step(W / "00_Spec/inputs/OD-C01_base_frame.step")
out = {}; ctl = []
def rx(res): return {"m": None if res.measured is None else round(res.measured, 6), "at": res.at, "st": res.status, "why": res.reason}
def G(*a, **k):
    g = gate(*a, **k); return {"gate": g.gate, "measured": g.measured, "status": g.status, "margin": g.margin}

# U-04 on a detached copy of the delivered solid
rt = step_roundtrip(foot, R / "rt_foot.step", timestamp="2026-10-01T00:00:00")
out["U04_roundtrip"] = {k: rx(v) for k, v in rt.items()}
cs = compare_step(foot, DEL); out["U04_compare_delivered"] = {k: rx(v) for k, v in cs.items()}

# STL vertex comparison delivered vs own re-mesh
def tris(p):
    b = Path(p).read_bytes(); n = struct.unpack("<I", b[80:84])[0]
    a = np.frombuffer(b[84:84 + 50 * n], dtype=np.dtype([("n", "<3f4"), ("v", "<3f4", (3,)), ("x", "<u2")]))
    return a["v"].reshape(-1, 3)
va, vb = tris(W / "02_STEP_STL/od_c15_foot_C1_v01.stl"), tris(R / "own_remesh_0.01_0.18.stl")
from scipy.spatial import cKDTree
out["stl_vertex_max_dist_delivered_to_own"] = float(cKDTree(vb).query(va)[0].max())

O, Z, X = (0, 0, 0), (0, 0, 1), (1, 0, 0)
def hexagon(s):
    e2 = s / math.sqrt(3)
    return Polygon(*[(e2 * math.cos(math.radians(60 * k)), e2 * math.sin(math.radians(60 * k))) for k in range(6)], align=None)
def nut(s=5.5, top=2.5):
    body = extrude(hexagon(s), 2.4) - Cylinder(1.5, 3, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -0.3)))
    return body.moved(Location((0, 0, top)))
LOC1 = Location((110, -6.0, 90), (90, 0, 0))

# 1 validity: remove one face -> open shell
fs = foot.faces()
open_shell = Shell(fs[1:])
v = validity(open_shell)
ctl.append(["validity (U-01)", "one face (counter annulus) removed: open shell", G("U-01", v["naked_edges"], "==", 0, band=0)])
# 2 envelope + radial (resize): uniform scale 1.02
big = scale(foot, 1.02)
e = envelope(big)
ctl.append(["envelope (U-02, D-02 size, REQ-04 height, REQ-06, REQ-07)", "foot scaled x1.02 (18.36 x 18.36 x 10.2)", G("U-02", e["size_x"], "in", (17.9, 18.1), band=0.005)])
pr = radial_profile(big, O, Z, X, list(range(0, 360, 10)), (0.7, 9.0), margin=0, z_step=0.5, side="outer")
ctl.append(["radial_profile (REQ-04 diameter, REQ-05 arc)", "foot scaled x1.02, outer R 9.18", G("REQ-04", pr["max"], "in", (8.95, 9.05), band=0.005)])
af = radial_extent(big, O, Z, X, 90, 6.0, side="inner", r_min=2.0).measured + radial_extent(big, O, Z, X, 270, 6.0, side="inner", r_min=2.0).measured
from tools.result import Result
ctl.append(["radial_extent (REQ-03 across flats)", "foot scaled x1.02, af 5.712", G("REQ-03", Result("across_flats", af, "mm"), "in", (5.60, 5.65), band=0.005)])
# REQ-05 arc on the placed scaled foot
pl = radial_profile(plate, (110, -6, 90), (0, 1, 0), (1, 0, 0), list(range(0, 95, 5)), (0.5, 5.5), margin=0, z_step=1.0, side="outer")
pf = radial_profile(big.moved(LOC1), (110, -6, 90), (0, -1, 0), (1, 0, 0), list(range(0, 360, 10)), (0.7, 9.0), margin=0, z_step=1.0, side="outer")
ctl.append(["radial_profile on the plate arc (REQ-05)", "scaled foot x1.02 at pose 1", G("REQ-05", Result("arc_margin", pl["min"].measured - pf["max"].measured, "mm"), ">=", 0.9, band=0.005)])
# 3 rotation 2 deg about Z (relocate)
rot = foot.rotate(__import__("build123d").Axis.Z, 2)
r80 = radial_extent(rot, O, Z, X, 80, 6.0, side="inner", r_min=2.0).measured; r100 = radial_extent(rot, O, Z, X, 100, 6.0, side="inner", r_min=2.0).measured
phi = min((abs(r80 * math.cos(math.radians(-10 - p)) - r100 * math.cos(math.radians(10 - p))), p) for p in [i / 1000 for i in range(-5000, 5001)])[1]
ctl.append(["radial_extent (REQ-03 flat rotation)", "foot rotated 2 deg about its axis", G("REQ-03", Result("flat_rotation", abs(phi), "deg"), "<=", 1.0, band=0.001)])
# 4 feature_census / bore_census (remove): lid hole filled
filled = foot + Cylinder(1.7, 2.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
fc = feature_census(filled)
ctl.append(["feature_census (U-05, REQ-01)", "lid hole filled (remove)", G("U-05", fc["bores"], "==", 1, band=0)])
ctl.append(["bore_census (J-06, U-05)", "lid hole filled (remove)", G("J-06", bore_census(filled), "==", 1, band=0)])
# 5 locate_bore (relocate 0.5 mm, resize to 3.2)
moved = filled - Cylinder(1.7, 2.5, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0.5, 0, 0)))
lb = locate_bore(bore_census(moved), (0, 0, 1.25), (0, 0, 1))
ctl.append(["locate_bore offset (REQ-02)", "lid hole moved 0.5 mm in x", G("REQ-02", lb["offset"], "<=", 0.10, band=0.005)])
small = filled - Cylinder(1.6, 2.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
lb2 = locate_bore(bore_census(small), (0, 0, 1.25), (0, 0, 1))
ctl.append(["locate_bore diameter (D-04a, REQ-02)", "lid hole resized to 3.2", G("D-04a", lb2["diameter"], ">=", 3.25, band=0.005)])
# 6 min_wall (degrade): groove from the top face leaves the lid 0.7 thick
thin = foot - (Cylinder(7.0, 1.8, align=(Align.CENTER, Align.CENTER, Align.MIN)) - Cylinder(3.2, 1.8, align=(Align.CENTER, Align.CENTER, Align.MIN)))
ctl.append(["min_wall (D-01a, D-01b, D-06a)", "annular groove 1.8 deep in the top face: lid 0.7", G("D-01a", min_wall(thin), ">=", 0.8, band=0.005)])
wide = min_wall(thin).detail.get("wide", {}).get("measured")
ctl.append(["min_wall wide (U-06)", "same mutant", G("U-06", Result("min_wall_wide", wide, "mm"), ">=", 2.0, band=0.005)])
ringm = (foot - extrude(hexagon(12.6), 7.5).moved(Location((0, 0, 2.5)))) & Pos(0, 0, 2.5) * Cylinder(20, 10, align=(Align.CENTER, Align.CENTER, Align.MIN))
ctl.append(["min_wall on the ring (J-05)", "pocket opened to af 12.6 (degrade): ring wall ~1.7", G("J-05", min_wall(ringm), ">=", 3.0, band=0.005)])
# 7 overhang + bridge: tunnel under the bed face, y 2..8, z 0..1
tun = foot - Pos(0, 5, 0.5) * Box(20, 6, 1)
ctl.append(["overhang_census (D-03a)", "tunnel 6 wide x 1 high across the bed face", G("D-03a", overhang_census(tun, (0, 0, 1), min_deg=45), ">=", 45, band=0.001)])
ctl.append(["flat_ceiling_spans (D-03b)", "same tunnel: flat ceiling 6 wide", G("D-03b", flat_ceiling_spans(tun, (0, 0, 1), max_span=5), "<=", 5, band=0.005)])
# 8 clearance (contacts, D-04c, REQ-03 nut)
gap = foot.moved(Location((110, -6.5, 90), (90, 0, 0)))
ctl.append(["clearance contact (U-03 a)", "foot 1 relocated 0.5 mm off the plate underside", G("U-03", clearance(gap, plate), "==", 0, band=0.005)])
rib = foot + Pos(0, 2.35, 4.5) * Box(1.0, 0.9, 3.0)
ringrib = rib & Pos(0, 0, 2.5) * Cylinder(20, 10, align=(Align.CENTER, Align.CENTER, Align.MIN))
shank = Pos(0, 0, 2.5) * Cylinder(1.5, 3.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
ctl.append(["clearance (D-04c)", "rib 0.9 deep on a flat in the pocket (degrade)", G("D-04c", clearance(ringrib, shank), ">=", 0.5, band=0.005)])
# 9 interference (U-03 a and b)
sunk = foot.moved(Location((110, -5.5, 90), (90, 0, 0)))
it = interference({"foot": sunk, "plate": plate})
ctl.append(["interference (U-03 a)", "foot 1 relocated 0.5 mm into the plate", G("U-03", it["foot|plate"], "<=", 0, band=0.001)])
ctl.append(["interference slide (U-03 b)", "nut envelope s 5.7 slid to z 6.0 in the delivered pocket", G("U-03", common_volume(foot, nut(5.7, 6.0)), "<=", 0, band=0.001)])
# 10 mass_properties COM inside the feet (REQ-06)
mp = mass_properties(plate.moved(Location((0, 0, 300))), 1000)
ctl.append(["mass_properties (REQ-06 COM inside feet)", "plate relocated +300 in Z", G("REQ-06", Result("com_margin_z+", 90 - mp["com_z"].measured, "mm"), ">=", 0, band=0.005)])
# 11 compare_step (U-04)
cm = compare_step(filled, DEL)
ctl.append(["compare_step (U-04)", "delivered file compared with the hole-filled mutant", G("U-04", cm["volume_delta"], "<=", 0, band=0.001)])
# 12 mesh checks (U-07)
sag = write_stl(foot, R / "ctl_coarse.stl", tolerance=0.1, angular_tolerance=0.5).checks["max_sagitta"]
ctl.append(["stl_max_sagitta (U-07)", "re-mesh at 0.1 mm / 0.5 rad (degrade)", G("U-07", sag, "<=", 0.01, band=0.005)])
b = bytearray((W / "02_STEP_STL/od_c15_foot_C1_v01.stl").read_bytes()); n = struct.unpack("<I", b[80:84])[0]
drop = b[:80] + struct.pack("<I", n - 1) + b[84:84 + 50 * (n - 1)]
(R / "ctl_drop.stl").write_bytes(bytes(drop))
ctl.append(["mesh_census (U-07 one closed shell)", "delivered STL with its last triangle removed", G("U-07", mesh_census(R / "ctl_drop.stl")["naked_edges"], "==", 0, band=0)])
arr = np.frombuffer(bytes(b[84:84 + 50 * n]), dtype=np.dtype([("n", "<3f4"), ("v", "<3f4", (3,)), ("x", "<u2")])).copy()
arr["v"][:, :, 0] += 0.05
(R / "ctl_shift.stl").write_bytes(bytes(b[:84]) + arr.tobytes())
ctl.append(["mesh_deviation (U-07)", "delivered STL shifted 0.05 mm in x", G("U-07", mesh_deviation(R / "ctl_shift.stl", foot), "<=", 0.01, band=0.005)])
out["controls"] = ctl
json.dump(out, open(R / "m05_controls.json", "w"), indent=1, default=str)
for k, v in out.items():
    if k != "controls": print(k, json.dumps(v, default=str)[:800])
for c in ctl: print(c)
