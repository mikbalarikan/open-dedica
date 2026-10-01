import json
from pathlib import Path
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead")
F = [("02_STEP_STL/od_c02_bulkhead_C1_v02.step","1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc"),
     ("02_STEP_STL/od_c02_assembly_C1_v02.step","7d2e760590973fdfe529338231b117a9fc456d246b886a0217c4785f61d37141"),
     ("02_STEP_STL/od_c02_bulkhead_C1_v02.stl","e48afe62c8beb97acc76da990d75ab7e4e2bfbd5416b9cf3f38a0f65d573e18e"),
     ("02_STEP_STL/od_c02_bulkhead_C1_v02.3mf","8a82334c463566c6ac2d57616d59a2c432be3dd9a9246526e926670b183cf082"),
     ("01_CAD/REPORT_od_c02_bulkhead_v02.md","afcf6b68b21166862ac6c388f4403e643c095951d8fa2663f3f50817c039fb82"),
     ("01_CAD/DESIGN_PLAN.md","119de1e798b8c65da5e8bbb882fdb86e1b358b0a7813cb16654dc2d406cf4005"),
     ("01_CAD/DESIGN_PLAN_v02.md","cc39c89c991d21038ed6167b5f5e017f902c3f91749e65d43e3cbb4b6dcc1e25"),
     ("briefs/WP-03_designer.md","1639c07d87977f3afe27cec6e1ca4437aab9388e474f9151600686ae1a2813d5"),
     ("01_CAD/check_od_c02_bulkhead_v02.json","e25653f36074ef4e2736981b5bdb438118182f14636df42c47b1d90b37572a96"),
     ("01_CAD/build_record_v02.json","29df8e6a1c410cd24d54753d03be262990cb0cff5dc05c726a6ff5c5c72dfcbc"),
     ("01_CAD/sections_v02.json","a0f85af79cea879c5ad317fd9ed49d3bd93642812fa08ff24524b531373004cc"),
     ("01_CAD/sweep_v02/sweep_summary_v02.json","835489ee99be3c15d6499678b7a8ff3bb01d16089de7df9c8a8aaaa660d62b7f")]
files = [{"path": p, "sha256": h, "matches_report": True} for p, h in F]
def g(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}
gates = [
 g("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "whole part: solid_count 1, brep_valid 1 (BRepCheck, BOP analyzer 0 faults), naked_edges 0 of 114 edges", "PASS", "validity"),
 g("U-02", 12.0, "mm", "12.0 x 215.0 x 210.0 each in [spec - 0.1, spec + 0.1]", 0.1, "size_x 12.000, size_y 215.000, size_z 210.000; position x 59.000...71.000, y 0.000...215.000, z -240.000...-30.000 (reported apart, exact)", "PASS", "envelope"),
 g("U-03", 4.0, "mm", "plate contact clearance = 0 and interference <= 0; base bores coaxial with plate holes <= 0.10; neighbours >= 3.0; carrier box >= 4.0", 0.0, "governing: carrier box 4.000 at (59.0, 0.0, -30.0) to (55.0, 0.0, -30.0). Also: plate clearance 0.000 at (67.0, 0.0, -225.0), common 0.000 mm3; coax offsets 0.000 x4; OD-H01 7.500 at (63.0, 40.0, -202.4); OD-C04 9.000 at (59.0, 0.0, -157.0); OD-C03 17.000 at (59.0, 0.0, -240.0); OD-G01 18.683 at (59.5, 207.0, -30.0); OD-H11 20.161 at (63.0, 99.357, -97.3); interference 0.000 mm3 with every part, OD-H11 by disjoint bounding boxes (x <= 42.839 vs x >= 59.0), no boolean on the unsound solid", "PASS_ASSUMED", "clearance, common_volume (interference), locate_bore on both solids", ("A-01", "A-02")),
 g("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "part STEP: AP242, 1 solid labelled od_c02_bulkhead, valid after re-import, 0 loose shells/faces, volume equals the analytic plan volume within 2.6e-10 mm3; reviewer re-export of a copy: volume_delta 4.7e-10, faces_delta 0, labels 1, valid 1; the bulkhead in the assembly STEP identical (208484.106 mm3, same box)", "PASS", "compare_step, step_roundtrip, validity"),
 g("U-05", 6, "count", "1 wall, 1 base rail, 1 top rail, 4 gabled windows, 4 + 2 D4.0 blind bores", 0, "46 faces: 36 planar, 10 cylindrical all concave (4 window R7.0, 6 bore R2.0), 0 convex; 6 blind bores (4 open at y 0, 2 open at y 215); 8 window roof planes at 45 deg", "PASS", "feature_census, bore_census, locate_bore"),
 g("U-06", 2.0, "mm", ">= 2.0 (Soft)", 0.0, "(63.0, 207.0, -60.0) to (63.0, 209.0, -60.0): top-rail bore floor rim to the flange underside (same at z -210)", "PASS", "min_wall_wide spacing 0.7"),
 g("U-07", 0.004896, "mm", "STL tol 0.01, angular <= 0.2310 rad, sagitta <= 0.01; 3MF carries the same mesh", 0.005104, "STL: 2308 triangles, 1 body, 0 naked edges, winding consistent; deviation both ways 0.004896 at (65.0, 64.95, -59.95); reviewer re-mesh at 0.01 / 0.20 rad gives the same 2308 triangles and vertex set; 3MF: 2308 triangles, unit mm, no transform, all 2308 triangles identical to the STL", "PASS", "mesh_census, mesh_deviation, write_stl (re-mesh), 3MF triangle-set comparison"),
 g("U-08", None, "count", "applies to threaded parts; this target has none", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("D-01a", 2.0, "mm", "min_wall >= 0.8", 1.2, "(63.0, 207.0, -60.0) top-rail bore floor rim to flange underside", "PASS", "min_wall spacing 0.7"),
 g("D-01b", 2.0, "mm", "min_wall >= 2.0", 0.0, "(63.0, 207.0, -60.0) to (63.0, 209.0, -60.0): top-rail bore floor (y 209) over the flange underside (y 207) at the wall-face line; same at z -210", "PASS", "min_wall spacing 0.7"),
 g("D-02", 215.0, "mm", "each envelope size <= K1C volume 220 x 220 x 250 (12.0 x 215.0 on the bed, 210.0 tall)", 5.0, "bed 12.0 x 215.0 (margins 208, 5), height 210.0 (margin 40)", "PASS_ASSUMED", "envelope", ("A-08",)),
 g("D-03a", 45.0, "deg", "every downward face >= 45 deg from horizontal, build +Z; six bore crowns excepted", 0.0, "(67.0, 150.0, -186.0) window 1 gable; all 8 roof planes normal (0, +-0.707107, -0.707107) = 45.000 analytic; census on the part with the six bores refilled: least 45.0, sampling bound 0, 0 samples below 45; whole part: 0.0 at the bore crowns (named exception, e.g. (65.0, 0.0, -223.0))", "PASS_ASSUMED", "overhang_census(build_dir=(0,0,1), spacing 0.7) on the refilled solid; B-rep face normals", ("A-10",)),
 g("D-03b", 4.0, "mm", "span <= 5", 1.0, "the six D4.0 insert bores (bore_census 4.000); windows gabled; no other downward face below 45 deg in the refilled census; sections z -44/-45/-60/-200", "PASS", "bore_census, overhang_census (refilled), reviewer sections"),
 g("D-04a", None, "mm", "none on this part", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("D-05a", 11.0, "mm", "material >= 8.0 across around each of the six bores", 3.0, "top bores (65, 212, -60) and (65, 212, -210): x 59.5...70.5 = 11.0; base bores 12.0 (x 59...71)", "PASS_ASSUMED", "radial_extent at 0 and 180 deg, radial_profile", ("A-05",)),
 g("D-05b", 4.0, "mm", "D 4.0 +- 0.05, depth 6.0 +- 0.1 (>= 5.7)", 0.05, "all six: D 4.000, depth 6.000, blind; governing margin on diameter", "PASS_ASSUMED", "bore_census, locate_bore", ("A-05",)),
 g("D-06a", 2.0, "mm", ">= 1.0", 1.0, "(63.0, 207.0, -60.0)", "PASS", "min_wall spacing 0.7"),
 g("D-07", None, "mm", "none: insert bores formed by the insert", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("J-05", 3.5, "mm", ">= 3.0 around each insert bore", 0.5, "(70.5, 209.25, -60.0) top bores: least outer radius 5.5 over 36 angles x 12 levels less r 2.0; base bores 4.0 at (71.0, 0.25, z)", "PASS", "radial_profile, radial_extent, locate_bore"),
 g("E-06", 210.0, "mm", "rails span the wall's whole length (210.0); no free-standing boss", 0.0, "sections x 61 and x 69: two cuts each 12 x 210 + 8 x 210 = 4200 mm2, rails z -240...-30; all six bores inside a rail", "PASS", "reviewer sections (write_sections), bore_census"),
 g("REQ-01", 4.0, "mm", "four D4.0 +- 0.05 blind along +Y from y 0, depth 6.0 +- 0.1, at (65, -45/-105/-165/-225), offset <= 0.10 from the plate holes", 0.05, "(65, 0, -45/-105/-165/-225): D 4.000, depth 6.000, blind, offset 0.000 to nominal and 0.000 to the plate holes (plate holes D 4.000, through y -6...0)", "PASS_ASSUMED", "bore_census, locate_bore on both solids", ("A-01", "A-03")),
 g("REQ-02", 63.0, "mm", "wet face 63.00 +- 0.10, electric face 67.00 +- 0.10 over the height above the rail; rail wet face 59.00 +- 0.10", 0.1, "858 rays along X at y 12.5...205, 11 z levels: wet 63.000 every ray, electric 67.000 every ray; envelope min_x 59.000", "PASS_ASSUMED", "radial_extent rays (reviewer sections), envelope", ("A-01",)),
 g("REQ-03", 0.0, "mm", "underside y 0.00 +- 0.10, one planar face less four bore mouths; rail top y 12.0 +- 0.1", 0.1, "one planar face y 0, 5 wires, 2469.73 mm2 = 12 x 210 less four D4 mouths; rail tops y 12.000 (rays at x 61, 62.5, 67.5, 69)", "PASS_ASSUMED", "envelope, feature_census, B-rep faces, rays", ("A-01",)),
 g("REQ-04", 14.0, "mm", "four D14.0 +- 0.1 at spec centres, offset <= 0.10, 45 deg gable toward +Z, apex 7.0 beyond +Z edge, no collar", 0.1, "w1 (150, -200), w2 (150, -130), w3 (150, -60), w4 (60, -55): D 14.000 by 54-point circle fit, offset < 1e-10, apex 14.000 above centre (w4 apex z -41, front end z -30 one face 1012 mm2), 30 deg gable ray 10.2487 = design, convex cylinders 0", "PASS_ASSUMED", "radial_extent (54 rays per window), B-rep faces", ("A-04",)),
 g("REQ-05", 59.0, "mm", "min_x >= 59.0; U-03 clearances to wet neighbours >= 3.0", 0.0, "envelope min_x 59.000; nearest wet neighbour OD-H01 7.500", "PASS_ASSUMED", "envelope, clearance", ("A-02",)),
 g("REQ-06", 215.0, "mm", "top face y 215.0 +- 0.1; wall reaches the top rail everywhere", 0.1, "envelope max_y 215.000; rays along Y at x 64 and 66 continuous to y 215 outside the windows", "PASS_ASSUMED", "envelope, rays", ("A-06",)),
 g("REQ-07", 4.0, "mm", "two D4.0 +- 0.05 blind along -Y from y 215, depth 6.0 +- 0.1, at (65, -60) and (65, -210), offset <= 0.10", 0.05, "(65, 215, -60) and (65, 215, -210): D 4.000, depth 6.000, blind, offset 0.000", "PASS_ASSUMED", "bore_census, locate_bore", ("A-05",)),
 g("REQ-08", 71.0, "mm", "max_x <= 71.0; wall face x 67 <= 70", 0.0, "envelope max_x 71.000 (base rail); electric face 67.000 (margin 3.0)", "PASS_ASSUMED", "envelope, rays", ("A-07",)),
 g("REQ-09", None, "bool", "Soft bench: no visible rattle or flex with the panels on", None, None, "INCONCLUSIVE", "bench (not geometric)", ("A-11",)),
]
census = [
 {"feature": "F01 wall x 63...67, y 0...215, z -240...-30", "expected": "planar faces x 63 and x 67, 4.0 thick", "found": "faces x 63.000 and x 67.000, each 40054.12 mm2 with 5 wires (outer + 4 windows)", "status": "PASS"},
 {"feature": "F02 base rail x 59...71, y 0...12", "expected": "underside y 0, sides x 59/71, tops y 12, full length", "found": "underside 1 face y 0 (2469.73 mm2), sides 2520 mm2 each, tops 840 mm2 each, z -240...-30", "status": "PASS"},
 {"feature": "F03 top rail x 59.5...70.5, y 207...215", "expected": "top y 215, sides x 59.5/70.5, undersides y 207, full length", "found": "top 2284.87 mm2 (3 wires), sides 1680 mm2, undersides 735 mm2 each", "status": "PASS"},
 {"feature": "F04 wire windows x4, gabled", "expected": "4 concave half-cylinders R7.0, 8 side planes, 8 roof planes at 45 deg", "found": "4 R7.000 half-cylinders on axes (y,z) = (150,-200), (150,-130), (150,-60), (60,-55); 8 sides; 8 roofs normal (0, +-0.707107, -0.707107)", "status": "PASS"},
 {"feature": "F05 D4.0 x 6.0 blind bores from below x4", "expected": "4 bores D4.0, open at y 0, floor y 6", "found": "4 bores D4.000 x 6.000, open at y 0, blind, at z -45/-105/-165/-225, x 65", "status": "PASS"},
 {"feature": "F06 D4.0 x 6.0 blind bores from above x2", "expected": "2 bores D4.0, open at y 215, floor y 209", "found": "2 bores D4.000 x 6.000, open at y 215, blind, at z -60/-210, x 65", "status": "PASS"},
 {"feature": "census totals", "expected": "planar 36, cylindrical 10, concave 10, convex 0, bores 6, faces 46", "found": "planar 36, cylindrical 10, concave 10, convex 0, bores 6, faces 46", "status": "PASS"},
]
plaus = [
 {"question": "P1 gravity", "answer": "YES: the rail underside rests on the plate top (clearance 0.000, common 0.000 mm3), four M3 x 12 from below into coaxial inserts (offset 0.000); in print it stands on a 1012 mm2 I-profile end, centre of mass (65.00, 103.26) over the footprint, slenderness 210/12 (A-10 risk, brim advised)", "status": "YES"},
 {"question": "P2 function chains", "answer": "YES: dam = one continuous underside z -240...-30 holed only by the four blind bore mouths; windows open through both faces with nothing in front; top bores open at y 215; ends of the dam open to the plate beyond z -30 / -240 (A-12)", "status": "YES"},
 {"question": "P3 moving parts and assembly path", "answer": "YES: no moving parts; lowered along -Y, its footprint box swept y 0...500 clears OD-H01 3.500, carrier box 4.000, OD-C04 9.000, OD-H11 16.161, OD-C03 17.000, OD-G01 18.249; final pose 7.500 to the pump", "status": "YES"},
 {"question": "P4 grip, reach, insertion", "answer": "YES: each screw goes in from below along the bore axis; a D6 driver column y -80...-9 is 3.000 from the plate and >= 11.4 from every neighbour; the head seats flat on the plate underside (gap 0, common 0); needs the machine on its side (A-03); tip lands exactly on the bore floor (see F2)", "status": "YES"},
 {"question": "P5 next to a real product", "answer": "YES: a printed 4 mm partition with rails and grommet windows is normal appliance practice; only the unbraced 195 mm span (REQ-09) and the zero-margin screw length (F2) draw comment", "status": "YES"},
 {"question": "P6 floating, embedded, mirrored, upside-down", "answer": "YES: one solid; interference 0 with every neighbour; gables point +Z (the print's up); independently placed neighbours match the assembly STEP solids (same volumes and boxes)", "status": "YES"},
]
controls = [
 {"check": "validity (solid_count)", "mutant": "part plus a loose 5 mm cube: solid_count 2", "got": "FAIL"},
 {"check": "validity (naked_edges)", "mutant": "front end face z -30 left out of the shell: 12 naked edges", "got": "FAIL"},
 {"check": "envelope", "mutant": "base rail wet face moved to x 58.5: min_x 58.5 (REQ-05), size_x 12.5 (U-02)", "got": "FAIL"},
 {"check": "feature_census / bore_census", "mutant": "base bore z -225 filled: 5 bores", "got": "FAIL"},
 {"check": "locate_bore (offset)", "mutant": "base bore z -165 moved 0.5 to x 65.5: offset 0.5", "got": "FAIL"},
 {"check": "locate_bore (diameter)", "mutant": "base bore z -105 opened to D4.2", "got": "FAIL"},
 {"check": "locate_bore (depth)", "mutant": "base bore z -45 deepened to 6.5", "got": "FAIL"},
 {"check": "min_wall", "mutant": "20 x 20 pocket in the wet face leaving 0.6 (D-01a, D-01b, D-06a)", "got": "FAIL"},
 {"check": "min_wall_wide", "mutant": "same pocket: 0.6 < 2.0 (U-06)", "got": "FAIL"},
 {"check": "overhang_census", "mutant": "window 1 cut square to z -186 (gable replaced by a flat roof), bores refilled: 0.0 deg", "got": "FAIL"},
 {"check": "radial_extent (window)", "mutant": "window 1 round part opened to D15.0", "got": "FAIL"},
 {"check": "radial_extent (J-05, D-05a)", "mutant": "top rail narrowed to x 62...68: wall 1.0", "got": "FAIL"},
 {"check": "clearance", "mutant": "bulkhead moved 5 mm to -X: 2.5 to OD-H01", "got": "FAIL"},
 {"check": "clearance (plate contact)", "mutant": "bulkhead lifted 0.5: plate clearance 0.5", "got": "FAIL"},
 {"check": "common_volume (interference)", "mutant": "bulkhead moved 10 mm to -X: 53.96 mm3 with OD-H01", "got": "FAIL"},
 {"check": "locate_bore (coaxiality with plate)", "mutant": "bulkhead moved 0.5 along +Z: axis offset 0.5", "got": "FAIL"},
 {"check": "mesh_deviation", "mutant": "STL re-meshed at 0.2 mm / 0.8 rad: 0.086", "got": "FAIL"},
 {"check": "mesh_census", "mutant": "STL with one triangle dropped: 3 naked edges", "got": "FAIL"},
 {"check": "3MF triangle-set comparison", "mutant": "3MF vertex 0 moved 0.05: 2289 of 2308 triangles match", "got": "FAIL"},
 {"check": "compare_step", "mutant": "exported part compared with a re-export carrying the wall pocket: 1360 mm3", "got": "FAIL"},
 {"check": "face rays (REQ-02, REQ-03, REQ-06 readings)", "mutant": "0.5 boss on the wet face at (62.5, 55, -100): wet face 62.5", "got": "FAIL"},
]
findings = [
 {"id": "F1", "gate": "REQ-09", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "bool", "required": "Soft bench: no visible rattle or flex with the panels on", "margin": None, "at": "wall x 63...67 between the rails y 12...207, z -240...-30", "blocks": False, "risk": "MEDIUM", "risk_basis": "INCONCLUSIVE by its row; a 4.0 ASA plate spanning 195 between rails is about 0.07 mm/N at mid-span once the top panel holds the top rail, but about 1.5 mm/N at the top as a cantilever before the panel is fitted (E 2 GPa, hand estimate)", "fix_direction": "answer on the first print with the panel on; if it flexes, ribs along Y (vertical in the print) on the electric face or a 5 mm wall"},
 {"id": "F2", "gate": "A-03", "kind": "OBSERVATION", "measured": 0.0, "unit": "mm", "required": "screw tip clear of the bore floor (no spec row)", "margin": 0.0, "at": "(65, 6.0, -45/-105/-165/-225) base bore floors", "blocks": False, "risk": "MEDIUM", "risk_basis": "an M3 x 12 with its head on the plate underside (y -6) ends at y 6.000, exactly the bore floor (shank common volume with the part 0.000); a screw at the long end of its length tolerance, or melt pushed below the insert, bottoms out before the joint clamps", "fix_direction": "Usta decision under A-03: M3 x 10 (4 mm into the 5.7 insert) or base bores deepened to about 7.0 in the spec (REQ-01)"},
 {"id": "F3", "gate": "D-01b", "kind": "OBSERVATION", "measured": 2.0, "unit": "mm", "required": ">= 2.0", "margin": 0.0, "at": "(63.0, 207.0...209.0, -60.0) and (63.0, 207.0...209.0, -210.0)", "blocks": False, "risk": "LOW", "risk_basis": "passes at margin 0; the reading is a point where the D4.0 bore's floor rim meets the wall-face line over the flange underside, with the full wall column below; but REQ-07's +0.1 depth tolerance would take it to 1.9, so the spec's own bands conflict there", "fix_direction": "spec: top-bore depth 6.0 -0.1/+0 or the top rail's underside at y 206; no change to this build needed"},
 {"id": "F4", "gate": "REQ-05", "kind": "OBSERVATION", "measured": 59.0, "unit": "mm", "required": "min_x >= 59.0; max_x <= 71.0; carrier box >= 4.0", "margin": 0.0, "at": "base rail faces x 59.0 and x 71.0; carrier box nearest (59.0, 0.0, -30.0)", "blocks": False, "risk": "LOW", "risk_basis": "REQ-05, REQ-08 and the carrier-box clearance sit exactly on their limits in CAD; the printed rail (first-layer squish on the z -240 end) may exceed them by tenths, with 3.5 to the pump and nothing that moves there", "fix_direction": "none for this build; if the spec wants print margin, narrow the base rail to x 59.2...70.8"},
 {"id": "F5", "gate": "U-04", "kind": "OBSERVATION", "measured": 0.052, "unit": "mm3", "required": "reference solids carried unchanged in the check assembly", "margin": None, "at": "od_h11_thermoblock in 02_STEP_STL/od_c02_assembly_C1_v02.step", "blocks": False, "risk": "LOW", "risk_basis": "the assembly's OD-H11 body is 0.052 mm3 (3e-7 relative) off the input placed by its joint, from re-writing an unsound input; the target and the other six solids match exactly; the assembly is a check artefact", "fix_direction": "none; retire with OD-C04 A-14 (a sound OD-H11)"},
 {"id": "F6", "gate": "A-12", "kind": "OBSERVATION", "measured": 210.0, "unit": "mm", "required": "dam continuous over z -240...-30", "margin": 0.0, "at": "dam ends at z -240 and z -30; plate spans z -305...100", "blocks": False, "risk": "UNKNOWN", "risk_basis": "the dam is continuous where specified, but water can run round either end on a flat plate; whether it reaches the electric zone depends on the drains and the tilt, which no file shows", "fix_direction": "first wet test (A-12); if needed, dam returns or a plate lip at the ends"},
 {"id": "F7", "gate": "A-10", "kind": "OBSERVATION", "measured": 1012.0, "unit": "mm2", "required": "stands and prints without supports on its rear end", "margin": None, "at": "bed face z -240, I-profile 12 x 215", "blocks": False, "risk": "MEDIUM", "risk_basis": "a 210 tall, 4 mm web on a 1012 mm2 footprint only 12 deep is a tall fin in ASA: warp and knock-over risk at the top layers", "fix_direction": "brim or mouse ears on the z -240 end, enclosed printer (the K1C is), slow top layers; confirm on the first print"},
]
least = [
 {"item": "1. D-01b and U-06 at margin 0.000 on the top-rail bores", "answer": "confirmed: min_wall 2.000 at (63.0, 207.0, -60.0) to (63.0, 209.0, -60.0), same at z -210; PASS in the band at margin 0; the spec's REQ-07 depth band conflicts with D-01b (F3, LOW)"},
 {"item": "2. D-03a gated on a derived (refilled) solid", "answer": "my own refill (D4.2 plugs mouth to floor + 0.05, valid, 34 faces, 0 bores) reads 45.0 deg at (67, 150, -186), bound 0, 0 samples below; the 8 roof planes are analytically 45.000; the crowns read 0 deg and are the named exception in ratified spec 1.2 section 5"},
 {"item": "3. Envelope rows on their limits; ledger text lag", "answer": "confirmed min_x 59.000, max_x 71.000, carrier box 4.000: PASS at margin 0 (F4, LOW); spec 1.2 now names window 4 at (60, -55) and the top bores at x 65, as built"},
]
out = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20260930-od-c02-bulkhead", "target": "od_c02_bulkhead_v02",
       "spec_version": "1.2", "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"},
       "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
       "summary": "Every Hard row re-measured from the exported STEP passes (D-01b, REQ-05, REQ-08 and the carrier box at margin 0); REQ-09 Soft bench INCONCLUSIVE; no blocking finding; passes rest on A-01...A-08, A-10.",
       "files": files, "gates": gates, "feature_census": census, "plausibility": plaus, "positive_controls": controls,
       "findings": findings, "least_sure_answers": least,
       "assumptions_relied_on": ["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-07", "A-08", "A-10"]}
(J/"reviews/RV01_od_c02_bulkhead_v02.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
import jsonschema
schema = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
jsonschema.validate(out, schema); print("valid", len(gates))
