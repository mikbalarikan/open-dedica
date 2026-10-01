"""RV01 D: positive controls - mutants of this job's delivered plate; each check must FAIL."""
import json, sys, re, zipfile, struct, io
from pathlib import Path
import numpy as np
from build123d import Cylinder, Box, Location, Pos, Rot, Solid, Compound, Plane
from tools.core import read_step, validity, write_step, compare_step, write_stl, mesh_sagitta, common_volume
from tools.measure import envelope, feature_census, bore_census, locate_bore, clearance, interference, overhang_census, radial_extent
from tools.measure.wall import mesh_census, mesh_deviation
from tools.measure.sampling import kind
from tools.result import gate
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); W = J / "reviews/RV01_work"; M = W / "mutants"; M.mkdir(exist_ok=True)
TS = "2026-09-30T00:00:00"
plate0 = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step")
plate = Solid(plate0.solids()[0].wrapped); plate.label = "od_c01_frame"
def ycyl(d, x, z, y0=-7.0, h=8.0):
    return Pos(x, y0 + h / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2, h)
def one(s, label):
    s = Solid(s.solids()[0].wrapped) if len(s.solids()) == 1 else s; s.label = label; return s
res = {}
def rec(check, mutant, g):
    res[check] = {"mutant": mutant, "got": g.status, "measured": g.measured, "required": g.required, "margin": g.margin}
    print(check, g.status, g.measured, g.required)

# 1 validity: plate plus a loose second solid
m1 = Compound([plate, Pos(0, 10, 0) * Box(5, 5, 5)])
rec("validity", "plate plus a loose 5 mm cube 10 above it", gate("U-01", validity(m1)["solid_count"], "==", 1, band=0))
# 2 envelope: plate lengthened 0.5 at the front (z +100 -> +100.5)
m2 = one(plate + Pos(0, -3, 100.25) * Box(200, 6, 0.5), "od_c01_frame")
rec("envelope", "plate front edge moved +0.5 in z (z max 100.5)", gate("U-02", envelope(m2)["size_z"], "in", (404.9, 405.1), band=0.005))
# 3 feature_census/bore_census: one insert hole removed (filled)
m3 = one(plate + ycyl(4.0, 65, -225, y0=-6, h=6), "od_c01_frame")
fc = feature_census(m3)
rec("feature_census", "insert hole (65, -225) filled (removed)", gate("U-05", fc["bores"], "==", 26, band=0))
bc3 = bore_census(m3)
n4 = sum(1 for b in bc3.detail["bores"] if abs(b["diameter"] - 4.0) < 0.05)
from tools.result import Result
rec("bore_census", "same mutant: Ø4.0 bores counted", gate("U-05", Result("bore_census_d4", n4, "count"), "==", 20, band=0))
# 4 locate_bore offset: OD-C07 hole (-71,-42) moved 0.5 in x
m4 = one(plate + ycyl(4.0, -71, -42, y0=-6, h=6) - ycyl(4.0, -70.5, -42), "od_c01_frame")
bc4 = bore_census(m4)
rec("locate_bore offset", "REQ-10 hole (-71, -42) moved +0.5 in x", gate("REQ-10", locate_bore(bc4, (-71, -3, -42), (0, 1, 0))["offset"], "<=", 0.10, band=0.005))
# 4b locate_bore diameter: feet hole resized to 3.2
m4b = one(plate + ycyl(3.4, -110, 90, y0=-6, h=6) - ycyl(3.2, -110, 90), "od_c01_frame")
rec("locate_bore diameter", "feet hole (-110, 90) resized to Ø3.2", gate("D-04a", locate_bore(bore_census(m4b), (-110, -3, 90), (0, 1, 0))["diameter"], ">=", 3.25, band=0.005))
# 5 clearance: OD-H11 lowered 7.0 (its low point to 9.49 above plate)
inp = J / "00_Spec/inputs"
h11 = read_step(inp / "OD-H11_thermoblock.step").moved(Location((0, 63, -140)))
rec("clearance", "OD-H11 placed 7.0 lower (y offset 63 instead of 70)", gate("REQ-08", clearance(plate, h11), ">=", 10.0, band=0.005))
c04 = read_step(inp / "OD-C04_thermoblock_mount.step").moved(Location((0, 70.5, -140)))
rec("clearance contact", "OD-C04 lifted 0.5 off the plate", gate("U-03", clearance(plate, c04), "==", 0.0, band=0.005))
# 6 interference: OD-C03 lowered 0.5 into the plate
L03 = Location(Plane(origin=(0, 39.5, -205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))
c03 = read_step(inp / "OD-C03_pump_cradle.step").moved(L03)
rec("interference", "OD-C03 lowered 0.5 into the plate", gate("U-03", interference({"plate": plate, "c03": c03})["plate|c03"], "<=", 0.0, band=0.001))
# 7 overhang: a Ø10 blind pocket 3 deep from the bottom at (0, -270) leaves a flat ceiling
m7 = one(plate - (Pos(0, -4.5, -270) * Rot(90, 0, 0) * Cylinder(5, 3)), "od_c01_frame")
rec("overhang_census", "Ø10 x 3 pocket from the bed face at (0, -270): ceiling at y -3", gate("D-03a", overhang_census(m7, build_dir=(0, 1, 0), spacing=0.7), ">=", 45.0, band=0.001))
# 8 top face one plane: a 0.5 step pocket in the top face
m8 = one(plate - (Pos(0, -0.25, 50) * Box(20, 0.5, 20)), "od_c01_frame")
tops = sum(1 for f in m8.faces() if kind(f.wrapped) == "plane" and f.normal_at(f.center()).Y > 0.999)
rec("top face count", "0.5 deep 20 x 20 pocket in the top face at (0, 50)", gate("REQ-07", Result("top_planes", tops, "count"), "==", 1, band=0))
# 9 radial_extent: OD-C07 hole moved to x -116.5 (web 1.5 to the edge)
m9 = one(plate + ycyl(4.0, -113, -42, y0=-6, h=6) - ycyl(4.0, -116.5, -42), "od_c01_frame")
r9 = radial_extent(m9, (-116.5, 0, -42), (0, -1, 0), (1, 0, 0), 180.0, 3.0, side="outer")
first = [m for m in r9.detail["material"] if m[1] > 1.99][0]
rec("radial_extent", "OD-C07 hole moved to x -116.5; ring across = 2 x first stretch end", gate("D-05a", Result("ring_across", 2 * first[1], "mm", at=r9.at), ">=", 8.0, band=0.005))
# reviewer's exact ray at 180 on the delivered plate (D-05a governing point)
r0 = radial_extent(plate, (-113, 0, -42), (0, -1, 0), (1, 0, 0), 180.0, 3.0, side="outer")
res["delivered_ray_180"] = {"material": r0.detail["material"], "status": r0.status, "reason": r0.reason}
# 10 compare_step (U-04): delivered plate compared with a mutant file missing a hole
write_step(m3, M / "m3_hole_removed.step", timestamp=TS)
cs = compare_step(plate, M / "m3_hole_removed.step")
rec("compare_step faces", "file of the hole-removed mutant compared with the plate", gate("U-04", cs["faces_delta"], "==", 0, band=0))
rec("compare_step volume", "same", gate("U-04", cs["volume_delta"], "<=", 0.0, band=0.001))
m10 = Solid(plate.wrapped); m10.label = "od_c01_frame_x"
write_step(m10, M / "m10_label.step", timestamp=TS)
rec("compare_step labels", "plate written under another name", gate("U-04", compare_step(plate, M / "m10_label.step")["labels"], "==", 1, band=0))
# 11 mesh: coarse STL (tol 0.1, ang 0.5)
w = write_stl(plate, M / "coarse.stl", tolerance=0.1, angular_tolerance=0.5)
rec("mesh_sagitta", "STL at tol 0.1 / 0.5 rad", gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=0.005))
rec("mesh_deviation", "the coarse STL against the plate", gate("U-07", mesh_deviation(M / "coarse.stl", plate), "<=", 0.01, band=0.005))
raw = (J / "02_STEP_STL/od_c01_frame_C1_v02.stl").read_bytes()
n = struct.unpack("<I", raw[80:84])[0]
cut = raw[:80] + struct.pack("<I", n - 1) + raw[84 + 50:84 + 50 * n]
(M / "hole_in_mesh.stl").write_bytes(cut)
rec("mesh_census", "delivered STL with one triangle deleted", gate("U-07", mesh_census(M / "hole_in_mesh.stl")["naked_edges"], "==", 0, band=0))
# 12 3MF equality check: one vertex moved 0.5
z = zipfile.ZipFile(J / "02_STEP_STL/od_c01_frame_C1_v02.3mf")
xml = z.read("3D/3dmodel.model").decode()
first_v = re.search(r'<vertex x="([^"]+)"', xml)
xml2 = xml[:first_v.start(1)] + str(float(first_v.group(1)) + 0.5) + xml[first_v.end(1):]
verts = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml2)])
tris = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml2)])
tri = np.frombuffer(raw[84:84 + 50 * n], dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]))
key = lambda T: tuple(sorted(tuple(np.round(q, 3)) for q in T))
common = len({key(t) for t in tri["v"].astype(float)} & {key(t) for t in verts[tris]})
rec("3mf_same_mesh", "3MF with one vertex moved 0.5 in x", gate("U-07", Result("3mf_common_triangles", common, "count"), "==", n, band=0))
(W / "rv_d.json").write_text(json.dumps(res, indent=1, default=str))
