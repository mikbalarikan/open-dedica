import json, math, sys, struct
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build123d import Pos, Rot, Box, Cylinder, Solid, Compound, Shell, Location
from tools.core.step import read_step, compare_step
from tools.core import write_stl, validity
from tools.result import gate, Result
from tools.measure import mesh_census, mesh_deviation, mass_properties
import checks as C
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle"); R = W/"reviews/RV02_work"; M = R/"mutants"
P = W/"02_STEP_STL/od_c03_cradle_C1_v02.step"
part = read_step(P); part = Solid(part.wrapped)
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v02.step")
pump = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
sleeve = {c.label: c for c in asm.children}["od_h02_sleeve_assumed_A03"]
def one(s):
    ss = s.solids(); return ss[0] if len(ss) == 1 else s
out = []
def rec(family, mutant, rows, gates=None):
    sel = [r for r in rows if gates is None or r.gate in gates]
    st = C.worst(sel)
    fails = [(r.gate, r.method, r.measured, r.required) for r in sel if r.status != "PASS" and r.status != "PASS_ASSUMED"]
    out.append({"check": family, "mutant": mutant, "got": st, "failing": fails[:6]}); print(family, "|", mutant, "->", st, fails[:3], flush=True)
hole = lambda x, z, d: Pos(x, 38.5, z) * Rot(90, 0, 0) * Cylinder(d / 2, 3.0)
fill = lambda x, z: Pos(x, 38.5, z) * Rot(90, 0, 0) * Cylinder(1.75, 3.0)
# 1 validity: two solids; and an open shell (one face removed)
two = Compound(children=[part, Pos(0, 50, 0) * Box(5, 5, 5)])
rec("validity (solid_count)", "delivered part plus a loose 5 mm cube", C.g_validity(two))
opn = Shell(part.faces()[1:])
rec("validity (naked_edges)", "delivered part with its foot end face removed (open shell)", C.g_validity(opn))
# 2 envelope: foot 0.5 longer in +Z ; underside 0.3 lower
m = one(part + Pos(0, 38.5, 42.25) * Box(80, 3, 0.5)); rec("envelope (U-02)", "foot extended 0.5 mm in +Z (z to 42.5)", C.g_envelope(m)[0], {"U-02"})
m = one(part + Pos(0, 40.15, 16) * Box(80, 0.3, 52)); rec("envelope max_y (REQ-08)", "foot underside moved 0.3 mm down (y 40.3)", C.g_envelope(m)[0] + C.g_foot(m), {"REQ-08"})
# 3 feature census / bores
m = one(part + fill(-34, -4)); rec("feature_census, bore_census (U-05)", "hole (-34, -4) filled", C.g_census(m))
m.export_step if False else None
m2 = one(part + fill(-34, -4) - hole(-34, -3.5, 3.4)); rec("locate_bore offset (REQ-07)", "hole (-34, -4) moved 0.5 mm to z -3.5", C.g_bores(m2), {"REQ-07"})
m3 = one(part + fill(34, 37) - hole(34, 37, 3.2)); rec("locate_bore diameter (D-04a, REQ-07)", "hole (34, 37) drilled 3.2", C.g_bores(m3), {"D-04a", "REQ-07"})
# 4 walls: slot 2 of the -X block widened to leave a 0.5 ligament at the block end
m = one(part - Pos(-31.5, 7.0, 31.75) * Box(5, 2.5, 1.5)); rw, mw = C.g_walls(m); rec("min_wall, min_wall_wide (D-01a/b, D-06a, U-06)", "-X rear slot widened to z 32.5 (ligament 0.5)", rw)
rec("sections: slot ligament (REQ-05)", "-X rear slot widened to z 32.5 (ligament 0.5)", C.g_slots(m)[0])
# 5 overhang / bridge: flat-roofed pocket 7 wide under the +X front slot
m = one(part - Pos(31.5, 13.0, 18.5) * Box(5, 2, 7)); rec("overhang_census (D-03a)", "+X post: flat-roofed pocket y 12..14, z 15..22 cut through", C.g_overhang(m)[0])
rec("bridge_span from faces and sections (D-03b)", "same pocket: 7.0 mm flat ceiling", C.g_bridge(m))
# 6 slot geometry from sections: slot floor raised 0.3 on +X front slot
m = one(part + Pos(31.5, 8.1, 17.0) * Box(4, 0.3, 6)); rec("sections: slot clear section (REQ-05)", "+X front slot floor raised 0.3 (clear 2.2)", C.g_slots(m)[0])
# 7 rib faces from sections: rib 1 thickened 0.2 at z 3
m = one(part + Pos(0, 32, 3.1) * Box(40, 10, 0.2)); rec("sections: rib faces (REQ-02)", "rib 1 rear face moved to z 3.2", C.g_ribfaces(m)[0])
# 8 radial: saddle enlarged to r 26.75 ; small lump at theta 40
m = one(part - Pos(0, 0, 14) * Cylinder(26.75, 40)); rec("radial_profile (REQ-01)", "both saddles opened to r 26.75", C.g_radial(m))
rec("clearance == 0 (REQ-04, U-03 sleeve)", "both saddles opened to r 26.75", C.g_pump(m, pump, sleeve)[0], {"REQ-04"})
lump = Pos(30 * math.cos(math.radians(40)), 30 * math.sin(math.radians(40)), 0) * Box(1, 1, 6)
m = one(part + lump + Pos(22.8, 22.0, 0) * Box(1.0, 5.0, 6)); rec("radial_extent window (REQ-02)", "1 mm lump at r 30, theta 40, joined to the web", C.g_req02(m))
# 9 interference: saddle 1 closed to r 26.55 on the saddle sector
ring = (Cylinder(26.66, 6) - Cylinder(26.55, 6)) & (Pos(0, 30, 0) * Box(60, 24, 6))
m = one(part + ring); rec("interference (REQ-04, U-03)", "saddle 1 closed to r 26.55 over its arc", C.g_pump(m, pump, sleeve)[0], {"REQ-04"})
# 10 clearance: -X post inner face moved 0.5 inward
m = one(part + Pos(-29.25, 18.5, 22.5) * Box(0.5, 37, 21)); rec("clearance (REQ-03, D-04c, U-03)", "-X post inner face moved to x -29.0", C.g_pump(m, pump, sleeve)[0], {"REQ-03"})
rec("post faces (REQ-06)", "-X post inner face moved to x -29.0", C.g_posts(m))
# 11 compare_step (U-04): the hole-filled mutant against the delivered file
m = one(part + fill(-34, -4)); rec("compare_step (U-04)", "hole (-34, -4) filled, compared with the delivered STEP", C.g_roundtrip(m, P))
# 12 mesh: coarse STL
w = write_stl(read_step(P), M/"coarse_tol0p1.stl", tolerance=0.1, angular_tolerance=0.5)
rec("mesh_sagitta (U-07)", "STL at tolerance 0.1 / 0.5 rad", [gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=C.MM)])
rec("mesh_deviation (U-07, V-05)", "STL at tolerance 0.1 / 0.5 rad", [gate("U-07", mesh_deviation(M/"coarse_tol0p1.stl", read_step(P)), "<=", 0.011, band=C.MM)])
raw = (W/"02_STEP_STL/od_c03_cradle_C1_v02.stl").read_bytes(); n = struct.unpack("<I", raw[80:84])[0]
holed = raw[:80] + struct.pack("<I", n - 1) + raw[84:84 + 50 * (n - 1)]
(M/"holed.stl").write_bytes(holed); mc = mesh_census(M/"holed.stl")
rec("mesh_census (U-07)", "delivered STL with its last triangle removed", [gate("U-07", mc["naked_edges"], "==", 0, band=0), gate("U-07", mc["bodies"], "==", 1, band=0)])
# 13 mass_properties (P1 centre of mass inside the saddle span)
pm = pump.moved(Location((0, 0, -15)))
cz = mass_properties(pm, 1000)["com_z"]
rec("mass_properties com (P1)", "OD-H01 moved 15 mm toward -Z", [gate("P1", cz, "in", (-3.0, 31.0), band=C.MM)])
(R/"controls.json").write_text(json.dumps(out, indent=1, default=str)); print("done")
