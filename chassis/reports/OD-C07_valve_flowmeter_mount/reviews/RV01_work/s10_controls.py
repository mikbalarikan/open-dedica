"""Positive controls: each check family, run on a mutant of this job's exported part, must FAIL."""
import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.core import validity, common_volume, compare_step, write_stl, mesh_sagitta
from tools.measure import (envelope, bore_census, locate_bore, feature_census, clearance, radial_profile, radial_extent,
                           min_wall, min_wall_wide, overhang_census, mesh_census)
from tools.result import gate
from build123d import Shell, Compound, Rot
m = load_mount(); h22, h24, h22p, h24p = load_oem(); H22 = comp(h22p); H24 = comp(h24p); H22_0 = comp(h22); H24_0 = comp(h24)
C = []
def ctl(check, mutant, g):
    print(f"{check:34s} | {mutant:70s} | {g.status} measured={g.measured} req={g.required}"); C.append({"check": check, "mutant": mutant, "got": "FAIL" if g.status == "FAIL" else g.status, "gate": g.row()})
# 1 validity
mut = Compound(children=[m, box(200, 210, 0, 10, 0, 10)])
v = validity(mut); ctl("validity.solid_count", "exported part plus a loose 10 mm cube", gate("U-01", v["solid_count"], "==", 1, band=0))
sh = Shell(m.faces()[1:]); v2 = validity(sh)
ctl("validity.naked_edges", "exported part with one face removed (open shell)", gate("U-01", v2["naked_edges"], "==", 0, band=0))
ctl("validity.brep_valid", "exported part with one face removed (open shell)", gate("U-01", v2["brep_valid"], "==", 1, band=0))
# 2 envelope
mut = m + box(42, 44, -14, -12, 48.0, 48.5)
e = envelope(mut); ctl("envelope", "0.5 mm pad added on the deck top at (43, -13)", gate("U-02", e["size_z"], "in", (47.9, 48.1), band=BAND_MM))
ctl("envelope (REQ-08 max z)", "same pad", gate("REQ-08", e["max_z"], "<=", 48.1, band=BAND_MM))
# 3 locate_bore (relocate) and diameter (resize)
mut = (m + ann(0, 1.75, -0.1, 4.1, -18, 21)) - ann(0, 1.7, -1, 5, -17.5, 21)
lb = locate_bore(bore_census(mut), (-18, 21, 2), (0, 0, 1))
ctl("locate_bore offset", "footprint hole (-18, 21) moved 0.5 mm to (-17.5, 21)", gate("REQ-06", lb["offset"], "<=", 0.10, band=BAND_MM))
mut = m - ann(0, 2.1, 40.0, 46.0, 46.662, 0)
lb = locate_bore(bore_census(mut), (46.662, 0, 43), (0, 0, 1))
ctl("bore_census diameter", "insert bore (46.662, 0) resized Ø4.0 -> Ø4.2", gate("D-05b", lb["diameter"], "in", (3.95, 4.05), band=BAND_MM))
# 4 feature census count
mut = m + ann(0, 1.75, -0.1, 4.1, -18, 21)
fc = feature_census(mut); ctl("feature_census bores", "footprint hole (-18, 21) removed (filled)", gate("U-05", fc["bores"], "==", 12, band=0))
# 5 common_volume / interference at the delivered pose
mut = m + box(50, 56, -9, -5, 48.0, 48.2)
ctl("common_volume (interference)", "0.2 mm pad on the deck top under the OD-H22 flange", gate("U-03", common_volume(mut, H22), "<=", 0, band=BAND_MM3))
# 6 clearance + 7 radial_profile on a ring made 0.2 mm tighter
mut = m + ann(16.1, 16.35, 10.3, 13.0)
cup = H24 & ann(15.71, 16.5, 10.3, 14.0)
ring = mut & ann(16.0, 18.6, 10.0, 13.5)
ctl("clearance", "ring inner radius reduced 16.30 -> 16.10", gate("REQ-01", clearance(ring, cup), "in", (0.50, 0.70), band=BAND_MM))
rp = radial_profile(mut, (0,0,0), (0,0,1), (1,0,0), [float(a) for a in range(0, 360, 2)], (10.5, 12.5), margin=0, z_step=0.5, side="inner", r_min=15.0, r_max=19.0)
ctl("radial_profile", "same ring mutant", gate("REQ-01", rp["min"], "in", (16.30, 16.40), band=BAND_MM))
# 8 radial_extent (J-05 wall) on a relocated insert bore
mut = (m + ann(0, 2.05, 40.25, 46.0, 46.662, 0)) - ann(0, 2.0, 40.0, 46.0, 47.662, 0)
ends = []
for k in range(72):
    r = radial_extent(mut, (47.662, 0, 0), (0,0,1), (1,0,0), k * 5.0, 45.99, side="outer", r_min=0, r_max=60)
    st = [s for s in stretches(r) if s[0] < 2.05]
    if st: ends.append(st[0][1] - 2.0)
from tools.result import Result
ctl("radial_extent (J-05 wall)", "insert bore (46.662, 0) moved 1.0 mm toward the slit", gate("J-05", Result("wall", min(ends), "mm"), ">=", 3.0, band=BAND_MM))
# 8b J-01 arithmetic on a catch reaching further in
mut = m + sector(70, 7.88, 16.87, 18.9, 29.9, 31.5)
cr = radial_extent(mut, (0,0,0), (0,0,1), (1,0,0), 70, 30.4, side="inner", r_min=15.0, r_max=24).measured
y = 20.37 - cr; t = 2.0; L = 29.9 - 4.0; eps = 1.5 * y * t / (L * L) * 100
ctl("J-01 arithmetic (radial_extent)", "hook 70° catch extended inward to R 16.87", gate("J-01", Result("eps", eps, "%"), "<=", 1.5, band=0))
# 9 min_wall and min_wall_wide on a thinned ring wall
mut = m - ann(17.0, 18.6, 10.6, 13.1)
mw = min_wall(mut); ctl("min_wall", "ring wall thinned to 0.7 mm (outer R 18.3 -> 17.0 over z 10.6..13)", gate("D-01a", mw, ">=", 0.8, band=BAND_MM))
mww = min_wall_wide(mut); ctl("min_wall_wide", "same thinned ring", gate("U-06", mww, ">=", 1.5, band=BAND_MM))
# 10 overhang census + flat downward face census on a ledge
mut = m + box(32, 36, -5, 5, 20, 22)
oc = overhang_census(mut & box(-30, 100, -30, 30, 10.5, 29.9), (0,0,1), min_deg=45.0, spacing=0.5)
ctl("overhang_census", "2 mm flat ledge added on the -X leg's outer face at z 20", gate("D-03a", oc, ">=", 45.0, band=BAND_DEG))
dn = [f for f in mut.faces() if f.geom_type.name == "PLANE" and f.normal_at(f.center()).Z < -0.99 and f.center().Z > 0.01]
ctl("flat downward face census", "same ledge", gate("D-03a", Result("flat_down", len(dn), "count"), "==", 9, band=0))
# 11 U-04 compare_step
cs = compare_step(mut, MOUNT)
ctl("compare_step", "the ledge mutant compared with the delivered STEP", gate("U-04", cs["volume_delta"], "<=", 0, band=BAND_MM3))
# 12 U-03(b) path sweeps
mut = m + box(54.9, 69.1, 13, 15, 47.0, 48.0)
worst = max(common_volume(mut, H22_0.moved(Location((62.0, yy, 53.0)))).measured for yy in (20, 16, 14, 12, 10))
ctl("U-03(b) OD-H22 slide sweep", "1 mm bridge across the U-slot mouth at y 13..15", gate("U-03", Result("sweep", worst, "mm3"), "<=", 0, band=BAND_MM3))
mut = m + ann(0, 2.4, 5.0, 9.4, 0.185, 0.093)
worst = max(common_volume(mut - (m & ann(18.5, 27, 4, 40)), H24_0.moved(Location((0, 0, 10.0 + d)))).measured for d in (5, 2, 1, 0))
ctl("U-03(b) OD-H24 drop sweep", "pin-1 hole filled from z 5.0 to 9.4", gate("U-03", Result("sweep", worst, "mm3"), "<=", 0, band=BAND_MM3))
# 13 deck-top flatness (+Z planes above z 40 at a single height 48.0)
mut = m - box(50, 54, -8, -5, 47.7, 48.1)
tops = sorted({round(f.center().Z, 4) for f in mut.faces() if f.geom_type.name == "PLANE" and f.normal_at(f.center()).Z > 0.99 and f.center().Z > 40})
ctl("deck flatness (+Z planes)", "0.3 mm pocket in the deck top under the flange", gate("REQ-04", Result("planes", len(tops), "count"), "==", 1, band=0))
# 14 notch probe
mut = m + (Rot(0, 0, 25) * box(16.2, 18.4, -1.05, 1.05, 10.0, 10.5))
ctl("notch probe (common_volume)", "notch at 25° filled", gate("REQ-09", common_volume(mut, Rot(0, 0, 25) * box(15.0, 19.0, -0.9, 0.9, 10.02, 10.48)), "<=", 0, band=BAND_MM3))
# 15 landing void under a catch
hk = m & sector(320, 12.0, 18.5, 27.0, 4.0, 40.0)
mut = (m - sector(320, 12.0, 18.5, 27.0, 4.0, 40.0)) + (Rot(0, 0, -20) * hk)
prism = sector(300, 7.88, 18.87, 19.70, 27.25, 29.9)
void = prism.volume - common_volume(prism, H24).measured
ctl("catch landing void", "hook 320° relocated to 300° (over the 296.5° slot)", gate("REQ-03", Result("void", void, "mm3"), "<=", 0, band=BAND_MM3))
# 16 mesh checks
wr = write_stl(m, W / "mutant_coarse.stl", tolerance=0.2, angular_tolerance=0.5)
ctl("mesh_sagitta", "STL re-meshed at 0.2 mm / 0.5 rad", gate("U-07", mesh_sagitta(m), "<=", 0.01, band=BAND_MM))
data = STL.read_bytes(); import struct
n = struct.unpack("<I", data[80:84])[0]; keep = n - 10
(W / "mutant_holed.stl").write_bytes(data[:80] + struct.pack("<I", keep) + data[84:84 + 50 * keep])
mc = mesh_census(W / "mutant_holed.stl")
ctl("mesh_census naked_edges", "delivered STL with its last 10 triangles removed", gate("U-07", mc["naked_edges"], "==", 0, band=0))
dump("s10.json", C)
