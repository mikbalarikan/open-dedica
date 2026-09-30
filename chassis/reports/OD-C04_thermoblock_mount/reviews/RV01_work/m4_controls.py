"""RV01: assembly path, and positive controls (mutants of this job's exported part)."""
import json, math
from pathlib import Path
import numpy as np
import trimesh
from build123d import Solid, Compound, Cylinder, Box, Pos, Rot, Align, GeomType
from OCP.BRepAdaptor import BRepAdaptor_Surface
from tools.core import read_step, validity, write_stl, write_step, compare_step, common_volume
from tools.core.shapes import solids
from tools.measure import (envelope, clearance, interference, bore_census, locate_bore, feature_census,
                           min_wall, min_wall_wide, overhang_census, mesh_census, mesh_deviation, radial_profile)
from tools.result import gate

W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount")
OUT = W / "reviews/RV01_work"; MUT = OUT / "mutants"; MUT.mkdir(exist_ok=True)
MM, VOL = 0.005, 0.001
m = Solid(solids(read_step(W / "02_STEP_STL/od_c04_mount_C1_v01.step"))[0]); m.label = "od_c04_mount"
asm = read_step(W / "02_STEP_STL/od_c04_assembly_C1_v01.step")
parts = {}
def walk(s):
    ch = list(getattr(s, "children", ()) or ())
    if ch: [walk(c) for c in ch]
    else: parts[s.label] = s
walk(asm)
H = Solid(solids(parts["OD-H11_thermoblock"])[0]); S1 = Solid(solids(parts["spacer_S1_assumed_A05"])[0]); S2 = Solid(solids(parts["spacer_S2_assumed_A05"])[0])
out = {"path": {}, "controls": []}
# ---- assembly path: thermoblock + spacers approach along -Z; thermoblock alone lowered along -Y
for d in [0.0, 0.1, 0.5, 1, 2, 5, 10, 20, 40, 60]:
    g = [Pos(0, 0, d) * s for s in (H, S1, S2)]
    out["path"][f"dz{d}"] = min(clearance(m, s).measured for s in g)
for d in [0.5, 2, 5, 10, 20, 40, 60, 80]:
    out["path"][f"H_dy{d}"] = clearance(m, Pos(0, d, 0) * H).measured
def rec(check, mutant, g_list):
    fails = [g for g in g_list if g.status == "FAIL"]
    got = "FAIL" if fails else ("INCONCLUSIVE" if any(g.status == "INCONCLUSIVE" for g in g_list) else "PASS")
    out["controls"].append({"check": check, "mutant": mutant, "got": got,
                            "rows": [(g.gate, g.measured, g.required, g.status) for g in g_list]})
# 1 validity: open shell (tip face of S1 removed) and two solids
from build123d import Shell
fs = [f for f in m.faces() if not (f.geom_type == GeomType.PLANE and abs(f.center().Z + 10.1) < 1e-6 and f.center().X < 0)]
open_shell = Shell(fs)
v = validity(open_shell); v2 = validity(Compound([m, Pos(200, 0, 0) * m]))
rec("validity", "S1 tip face removed (open shell); and a second copy of the mount beside it",
    [gate("U-01.naked_edges", v["naked_edges"], "==", 0, band=0), gate("U-01.solid_count", v2["solid_count"], "==", 1, band=0)])
# 2 envelope: mount moved +0.5 in x; and U-02 size with a foot 0.5 longer
mx = Pos(0.5, 0, 0) * m
e = envelope(mx)
e2 = envelope(m + Pos(0, -68, 33) * Box(100, 4, 0.5, align=(Align.CENTER, Align.CENTER, Align.MIN)))
rec("envelope", "mount relocated +0.5 in x; foot extended 0.5 in z",
    [gate("U-02.max_x", e["max_x"], "in", (49.9, 50.1), band=MM), gate("U-02.size_z", e2["size_z"], "in", (49.9, 50.1), band=MM)])
# 3 clearance + tip envelope: S1 standoff 0.2 taller (tip z -9.9)
tall = m + Pos(-19.62, 20.18, -10.1) * Cylinder(6.0, 0.2, align=(Align.CENTER, Align.CENTER, Align.MIN)) \
         - Pos(-19.62, 20.18, -20) * Cylinder(2.0, 20, align=(Align.CENTER, Align.CENTER, Align.MIN))
tip = [f for f in tall.faces() if f.geom_type == GeomType.PLANE and f.center().X < 0 and abs(f.center().Y - 20.18) < 0.5 and f.center().Z > -11]
c = clearance(tall, H)
rec("clearance (REQ-01) and envelope of the tip face (REQ-03)", "S1 standoff 0.20 taller (tip z -9.90)",
    [gate("REQ-01", c, ">=", 10.0, band=MM), gate("REQ-03.S1.tip_z", envelope(tip[0])["max_z"], "in", (-10.2, -10.0), band=MM)])
# 3b clearance == 0 for designed contacts: S1 spacer 0.1 shorter at the mount end
S1s = Pos(-19.62, 20.18, -10.0) * (Cylinder(3.5, 10.0, align=(Align.CENTER, Align.CENTER, Align.MIN)) - Cylinder(2.0, 10.0, align=(Align.CENTER, Align.CENTER, Align.MIN)))
rec("clearance == 0 (spacer contacts)", "S1 spacer 0.10 shorter (10.00, gap at the tip)",
    [gate("U-03.S1/mount.clearance", clearance(S1s, m), "==", 0.0, band=MM)])
# 4 interference / common_volume: S1 spacer 0.5 longer into the mount; boss into the REQ-07 keep-out
S1l = Pos(-19.62, 20.18, -10.6) * (Cylinder(3.5, 10.6, align=(Align.CENTER, Align.CENTER, Align.MIN)) - Cylinder(2.0, 10.6, align=(Align.CENTER, Align.CENTER, Align.MIN)))
it = interference({"mount": m, "S1": S1l})["mount|S1"]
boss = m + Pos(0, -66, 20) * Box(4, 8, 10, align=(Align.CENTER, Align.MIN, Align.MIN))
keep = Pos(-8.33, -14.13, 0) * Cylinder(45.0, 47.64, align=(Align.CENTER, Align.CENTER, Align.MIN))
cv = common_volume(boss, keep)
rp = radial_profile(boss, (-8.33, -14.13, 0), (0, 0, 1), (1, 0, 0), list(range(250, 290, 2)), (20.0, 30.0),
                    margin=(0, 0), z_step=2.0, side="inner", r_min=0, r_max=45.0)
out["boss_radial_min"] = (rp["min"].measured, rp["min"].status, rp["min"].reason[:200], rp["min"].at)
rec("interference / common_volume (U-03, REQ-07)", "S1 spacer 0.50 longer into the S1 standoff; 4 x 8 x 10 boss on the foot reaching y -58 (r 43.9 from the axis)",
    [gate("U-03.S1/mount.interference", it, "<=", 0, band=VOL), gate("REQ-07", cv, "<=", 0, band=VOL)])
# 5 step round trip: the mount compared against a file of the mutant with one bore filled
filled = m + Pos(25.01, 9.08, -17) * Cylinder(2.0, 6.9, align=(Align.CENTER, Align.CENTER, Align.MIN))
filled = Solid(solids(filled)[0]); filled.label = "od_c04_mount"
write_step(filled, MUT / "mut_S2_bore_filled.step", timestamp="2026-09-30T00:00:00")
rt = compare_step(m, MUT / "mut_S2_bore_filled.step")
rec("step_roundtrip / compare_step (U-04)", "delivered mount compared with a re-written file whose S2 bore is filled",
    [gate("U-04.volume_delta", rt["volume_delta"], "<=", 0, band=VOL), gate("U-04.faces_delta", rt["faces_delta"], "==", 0, band=0)])
# 6 bore census / locate_bore / feature_census: S2 bore filled (remove); frame hole moved 0.5 (relocate); S1 bore Ø3.7 (resize)
fc = feature_census(filled)
bc = bore_census(filled)
moved = m + Pos(40, -70, -8) * Box(5, 4, 7, align=(Align.CENTER, Align.MIN, Align.CENTER))
moved = moved - Pos(40.5, -71, -8) * Rot(-90, 0, 0) * Cylinder(1.7, 6, align=(Align.CENTER, Align.CENTER, Align.MIN))
lb = locate_bore(bore_census(moved), (40, -68, -8), (0, 1, 0))
small = m + Pos(-19.62, 20.18, -17) * Cylinder(2.0, 6.9, align=(Align.CENTER, Align.CENTER, Align.MIN))
small = small - Pos(-19.62, 20.18, -18) * Cylinder(1.85, 9, align=(Align.CENTER, Align.CENTER, Align.MIN))
ls = locate_bore(bore_census(small), (-19.62, 20.18, -13.5), (0, 0, 1))
rec("feature_census / bore_census / locate_bore (U-05, REQ-02, REQ-06, D-04a)",
    "S2 bore filled; frame hole (40, -8) moved +0.5 in x; S1 bore cut at Ø3.70",
    [gate("U-05.bores", fc["bores"], "==", 6, band=0), gate("U-05.bore_census", bc, "==", 6, band=0),
     gate("REQ-06.x+40_z-8.offset", lb["offset"], "<=", 0.10, band=MM),
     gate("REQ-02.S1.diameter", ls["diameter"], "in", (3.9, 4.1), band=MM), gate("D-04a.S1", ls["diameter"], ">=", 3.75, band=MM)])
# 6b E-06 root fillet: S1 fillet buried under a Ø14 x 1.0 collar
collar = m + Pos(-19.62, 20.18, -12) * Cylinder(7.0, 1.0, align=(Align.CENTER, Align.CENTER, Align.MIN)) \
            - Pos(-19.62, 20.18, -20) * Cylinder(2.0, 20, align=(Align.CENTER, Align.CENTER, Align.MIN))
fcc = feature_census(collar)
rec("feature_census torus count (E-06)", "S1 root fillet buried under a Ø14.0 x 1.0 collar",
    [gate("E-06.torus_faces", fcc["torus_faces"], "==", 2, band=0)])
# 7 min_wall: plate pocket leaving 0.5 mm
pocket = m - Pos(-10, -30, -17.5) * Box(20, 20, 5.0, align=(Align.MIN, Align.MIN, Align.MIN))
mw = min_wall(pocket); mww = min_wall_wide(pocket)
rec("min_wall / min_wall_wide (D-01a, D-01b, D-06a, U-06)", "20 x 20 pocket from the plate back leaving 0.50 of plate",
    [gate("D-01a", mw, ">=", 0.8, band=MM), gate("D-01b", mw, ">=", 2.0, band=MM), gate("D-06a", mw, ">=", 1.0, band=MM), gate("U-06", mww, ">=", 2.0, band=MM)])
# 8 overhang: the moved frame hole is round (no teardrop roof)
oh = overhang_census(moved, build_dir=(0, 0, 1), min_deg=45)
rec("overhang_census (D-03a)", "frame hole (40, -8) re-cut round, no teardrop roof",
    [gate("D-03a", oh, ">=", 45.0, band=0.001)])
# 9 STL: sagitta at a coarse tolerance; mesh census of an STL with triangles removed; mesh deviation of a shifted STL
w = write_stl(m, MUT / "mut_coarse.stl", tolerance=0.1, angular_tolerance=0.5)
tm = trimesh.load(W / "02_STEP_STL/od_c04_mount_C1_v01.stl")
holed = tm.copy(); holed.update_faces(np.arange(len(holed.faces)) > 20); holed.export(MUT / "mut_holed.stl")
shifted = tm.copy(); shifted.apply_translation((0.05, 0, 0)); shifted.export(MUT / "mut_shift005.stl")
mc = mesh_census(MUT / "mut_holed.stl")
md = mesh_deviation(MUT / "mut_shift005.stl", m)
rec("write_stl / mesh_sagitta / mesh_census / mesh_deviation (U-07)",
    "STL meshed at 0.1 / 0.5 rad; delivered STL with 21 triangles removed; delivered STL shifted 0.05 in x",
    [gate("U-07.stl_max_sagitta", w.checks["max_sagitta"], "<=", 0.01, band=MM),
     gate("U-07.naked_edges", mc["naked_edges"], "==", 0, band=0), gate("U-07.mesh_deviation", md, "<=", 0.01, band=MM)])
(OUT / "m4.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, indent=1, default=str))
