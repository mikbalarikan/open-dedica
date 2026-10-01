"""RV01: write the verdict's JSON twin from my measurements and validate it against the schema."""
import json
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
A3 = ["A-01", "A-02", "A-07"]
def g(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}
gates = [
 g("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "whole part; brep_valid 1, naked_edges 0", "PASS", "validity"),
 g("U-02", 232.0, "mm", "232.0 x 215.0 x 25.0 each in [spec - 0.1, spec + 0.1]; position x +-116.0, y 0 ... 215.0, z -302.0 ... -277.0 reported apart", 0.1,
   "size_x 232.000 (governing, ties with size_y 215.000 and size_z 25.000, each +0.100); position x -116.000 ... 116.000, y 0.000 ... 215.000, z -302.000 ... -277.000", "PASS", "envelope"),
 g("U-03", 0.780, "mm", "(a) contact clearance = 0, interference <= 0; footprint wholly over plate material, >= 0.5 from the outline; flanges >= 3.0 and wall foot >= 2.0 from every existing hole edge; flange holes >= 6.0 c-c from existing holes; >= 20.0 to OD-C02, OD-C03, OD-H01. (b) lowered from +40.0 in steps <= 2.0: interference <= 0", 0.28,
   "(116.0, 0.0, -302.0) wall corner to the plate's R 10 arc at (116.51, 0, -302.59): governing; plate contact clearance 0.000, common 0.000 mm3; area outside outline 0.000 mm2, over holes 0.000 mm2 of 2067.683; wall foot to feet-hole rim (+-110, 0, -295) 2.300 (+0.300); flanges to rim 4.300 (+1.300); 26 plate bores along Y; plate material missing under each flange-hole plug 0.000 mm3; nearest existing hole c-c 19.849 (+13.849); OD-C02 37.014, OD-C03 43.863, OD-H01 61.540 at (72, 0, -277), common 0.000 mm3 each; lowering 41 poses at 1.0 steps, worst 0.000 mm3", "PASS_ASSUMED",
   "clearance, common_volume (tools.core), envelope, bore_census; footprint and rim distances by reviewer code (BRepExtrema on the y 0 underside face split at z -299)", A3),
 g("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0,
   "part: AP242, mm, label od_c11_back, 1 solid, valid; round trip volume_delta 0.000 mm3, faces_delta 0, labels 1, valid_after 1; assembly: 5 named solids each valid, children identical to my own placements (common = volume)", "PASS", "compare_step, step_roundtrip"),
 g("U-05", 9, "count", "1 wall, 2 floor flanges, 4 gussets, 1 top ledge, 2 insert bosses, 4 d3.4 flange holes, 2 d4.0 blind bores, 3 d12.0 pass-throughs, 5 vent slots", 0,
   "bores 9 (4 d3.4 Y through, 2 d4.0 Y blind, 3 d12.0 Z through); planar 46, cylindrical 19 (concave 19, convex 0), other kinds 0; 10 R 2.0 slot ends; 4 hypotenuses, 2 boss undersides, 2 flange fronts, 3 ledge-underside pieces", "PASS", "feature_census, bore_census, locate_bore"),
 g("U-06", 3.0, "mm", ">= 2.0 (Soft, min_wall wide)", 1.0, "(76.0, 34.0, -302.0) wall at the inner +X gusset's top", "PASS", "min_wall_wide (spacing 0.7)"),
 g("U-07", 0.00499, "mm", "STL tol 0.01, angular <= 4 acos(1 - 0.01/R_max) = 0.23097 rad; stl_max_sagitta <= 0.01; the 3MF carries the same mesh", 0.00501,
   "STL 3928 triangles, 1 body, 0 naked edges, winding 1, volume 165531.487 mm3 (B-rep 165529.565), bbox = B-rep; mesh_deviation 0.00499 mm; my re-mesh at 0.01 mm / 0.20 rad: 3928 triangles, the same 1942 vertices, sagitta 0.00499; 3MF: 3928 triangles, millimetre, watertight, the same triangle set as the STL", "PASS", "mesh_census, mesh_deviation, write_stl, mesh_sagitta"),
 g("U-08", None, "count", "threads cosmetic; applies to threaded parts", None, "the target has no threads", "NOT_APPLICABLE", "N/A by the spec row"),
 g("D-01a", 3.0, "mm", "min_wall >= 0.8", 2.2, "(116.0, 0.0, -299.0) wall", "PASS", "min_wall (spacing 0.7)"),
 g("D-01b", 3.0, "mm", "min_wall >= 2.0", 1.0, "(116.0, 0.0, -299.0) wall", "PASS", "min_wall (spacing 0.7)"),
 g("D-02", 232.0, "mm", "each size <= the Kobra Max 3 volume (420 x 420 x 500, A-09): 232.0 x 215.0 on the bed, 25.0 tall", 188.0, "x 232.000, y 215.000 on the bed, z 25.000 tall", "PASS_ASSUMED", "envelope", ["A-09"]),
 g("D-03a", 90.0, "deg", ">= 45 from horizontal, build +Z, outside the named exception (crowns of 4 d3.4 and 2 d4.0 horizontal holes)", 45.0,
   "solid with the six exception holes plugged by position (57 faces, valid): no downward face off the bed; exception crowns read 0.0 deg at (-95.0, 0.0, -280.3), reported apart", "PASS_ASSUMED", "overhang_census(build_dir=(0,0,1), spacing=0.7)", ["A-08"]),
 g("D-03b", 4.0, "mm", "span <= 5: the d3.4 and d4.0 horizontal holes bridge <= 4.0; nothing else bridges", 1.0,
   "widest horizontal hole d4.000 (insert bores at (+-90, 209 ... 215, -293)); flange holes d3.400; flat_ceiling_spans 0.000 (no flat ceiling off the bed)", "PASS_ASSUMED", "bore_census, flat_ceiling_spans(max_span=5.0, spacing=0.7), reviewer sections", ["A-08"]),
 g("D-04a", 3.4, "mm", "the four flange holes d >= 3.25", 0.15, "(+-81 / +-95, 0, -282), all four 3.400", "PASS", "bore_census, locate_bore"),
 g("D-05a", 12.0, "mm", "material >= 8.0 across around each of the two d4.0 insert bores", 4.0,
   "across X 12.000 (6.0 + 6.0) and across Z 15.000 (9.0 + 6.0) at y 210 about (+-90, -293), both bosses", "PASS_ASSUMED", "radial_extent", ["A-05"]),
 g("D-05b", 4.0, "mm", "the two insert bores d 4.0 +- 0.05, depth 6.0 +- 0.1 (>= 5.7)", 0.05, "(+-90, 209 ... 215, -293): d 4.000, depth 6.000 (+0.100), blind", "PASS_ASSUMED", "bore_census, locate_bore", ["A-05"]),
 g("D-06a", 3.0, "mm", ">= 1.0", 2.0, "(116.0, 0.0, -299.0) wall", "PASS", "min_wall (spacing 0.7)"),
 g("D-07", None, "count", "fit-critical bores: none on this target", None, "the spec row names none for this target", "NOT_APPLICABLE", "N/A by the spec row"),
 g("J-05", 4.0, "mm", ">= 3.0 around each insert bore", 1.0, "(96.0, 210.0, -293.0) +X and (84, 210, -293) -X and (90, 210, -287) +Z: 4.000; -Z 7.000; both bores, y 210 and y 213", "PASS", "radial_extent"),
 g("E-06", 1, "bool", "each insert boss a block tied into the wall and the ledge; each flange tied to the wall by two gussets", 0,
   "sections x +-93 (boss, wall, ledge one region), x +-74 and x +-102 (gusset, wall, flange one region), x 0 (ledge and wall): 7 of 7 tied", "PASS", "reviewer sections (cut regions, BRepAlgoAPI_Common + point-in-region)"),
 g("E-11", 1, "bool", "cord strain relief = grommet OD-C14 in the d12 cord hole (A-03); the five vent slots open the bay's rear", 0,
   "rays along +Z at each slot centre and each pass-through axis meet no material (5 + 3 through); d12 cylinders z -299 ... -277 behind each hole: 0.000 mm3; vents x 76 ... 112, y 100 ... 180", "PASS_ASSUMED", "radial_extent, common_volume, reviewer sections", ["A-03", "A-06"]),
 g("REQ-01", 0.0, "mm", "four d3.4 +- 0.1 through-holes along Y at (+-81, -282), (+-95, -282), offset <= 0.10, 4.0 +- 0.1 long; underside one plane at y 0.00 +- 0.10", 0.1,
   "(+-81 / +-95, 0 ... 4, -282): offset 0.000, d 3.400 (+0.100), length 4.000 (+0.100), through; underside one planar face y 0.000, 2067.683 mm2", "PASS_ASSUMED", "locate_bore, envelope, reviewer face list", ["A-01"]),
 g("REQ-02", -302.0, "mm", "outer face z -302.00 +- 0.10 and inner face z -299.00 +- 0.10 at y 50 and y 200; x +-116.0 +- 0.1", 0.1,
   "rays at x -40, 0, 40 at y 50 and y 200: outer -302.000, inner -299.000; x -116.000 / 116.000 at y 50 and y 200", "PASS_ASSUMED", "radial_extent, envelope", ["A-02"]),
 g("REQ-03", 12.0, "mm", "one d12.0 +- 0.1 hole along Z at (95, 30), offset <= 0.10", 0.1, "(95, 30, -302 ... -299): d 12.000, offset 0.000, through", "PASS_ASSUMED", "locate_bore", ["A-03"]),
 g("REQ-04", 12.0, "mm", "two d12.0 +- 0.1 holes along Z at (-100, 30) and (-84, 30), offset <= 0.10", 0.1, "(-100, 30) and (-84, 30): d 12.000, offset 0.000, through", "PASS_ASSUMED", "locate_bore", ["A-04"]),
 g("REQ-05", -277.0, "mm", "max_z <= -277.0; box x +-70, y 0 ... 100, z -298.8 ... -250 common with the panel = 0", 0.0, "max_z -277.000 (flange fronts); box common 0.000 mm3", "PASS_ASSUMED", "envelope, common_volume", ["A-07"]),
 g("REQ-06", 4.0, "mm", "five slots 4.0 +- 0.1 x 80.0 +- 0.1 along Z, centres x 78/86/94/102/110 +- 0.1, y 100.0 ... 180.0 +- 0.1", 0.1,
   "rays at (x_c, 140, -300.5): each slot 2.000 + 2.000 wide, 40.000 + 40.000 tall (y 100.000 ... 180.000), centres 0.000 off, through", "PASS_ASSUMED", "feature_census, radial_extent, reviewer sections", ["A-06"]),
 g("REQ-07", 4.0, "mm", "two d4.0 +- 0.05 blind bores along -Y from y 215.0, depth 6.0 +- 0.1, at (+-90, -293), offset <= 0.10; top face one plane y 215.00 +- 0.10 over z -299 ... -287", 0.05,
   "(+-90, 209 ... 215, -293): d 4.000, depth 6.000, offset 0.000, blind; top one planar face y 215.000 spanning z -302 ... -287", "PASS_ASSUMED", "locate_bore, bore_census, envelope, reviewer face list", ["A-05"]),
 g("REQ-08", 0.0, "mm3", "four d6 cylinders y 4 ... 260 on the flange-hole axes: interference with the panel = 0", 0.0,
   "all four 0.000 mm3; nearest material above y 4.5 is the flange top (0.5); boss face x 84 and ledge front z -287 stay outside r 3", "PASS", "common_volume, clearance"),
 g("REQ-09", None, "bool", "Soft: no visible drumming or flex with the top panel on and the side panels absent (bench, first print)", None, "not a geometric gate", "INCONCLUSIVE", "bench (not measurable from the CAD)", ["A-11"]),
 g("exactly_one_solid", 1, "count", "solid_count = 1", 0, "whole part", "PASS", "validity"),
 g("feature_census", 46, "count", "plan counts: planar 46, cylindrical 19 (concave 19), bores 9", 0, "planar 46, cylindrical 19, bores 9, other kinds 0", "PASS", "feature_census"),
 g("envelope_within_spec", 232.0, "mm", "232.0 x 215.0 x 25.0 each +- 0.1; position x +-116.0, y 0 ... 215.0, z -302.0 ... -277.0 +- 0.1", 0.1, "sizes 232.000 x 215.000 x 25.000; every position bound at 0.000 off", "PASS", "envelope"),
]
census = [
 ("F01 wall x +-116, y 0 ... 215, z -302 ... -299", "1 slab; outer and inner face one plane each", "outer face z -302 (47957.876 mm2), inner face z -299 (46213.876 mm2), ends x +-116 (645 mm2 each)", "PASS"),
 ("F02 floor flanges x2, x +-(72 ... 104), y 0 ... 4, z -299 ... -277", "2", "2 front faces z -277 (128 mm2 each), 2 tops y 4 (557.842 mm2 each), ends x +-72 / +-104", "PASS"),
 ("F03 gussets x4 (inner wall leg 30, outer 18, flange leg 16)", "4 hypotenuses facing up", "inner at x +-(72 ... 76) y 4 ... 34, normal (0, 0.4706, 0.8824); outer at x +-(100 ... 104) y 4 ... 22, normal (0, 0.6644, 0.7474)", "PASS"),
 ("F04 top ledge x +-114, y 211 ... 215, z -299 ... -287", "1; underside in 3 pieces", "front z -287 (1104 mm2), underside pieces 216 / 2016 / 216 mm2, ends x +-114", "PASS"),
 ("F05 insert bosses x2, x +-(84 ... 96), y 203 ... 211", "2", "2 undersides y 203 (144 mm2 each), side faces x +-84 / +-96", "PASS"),
 ("F06 flange holes x4 d3.4 along Y at (+-81, -282), (+-95, -282)", "4 bores, through", "4 x d3.400, length 4.000, offset 0.000, through", "PASS"),
 ("F07 insert bores x2 d4.0 x 6.0 blind at (+-90, -293)", "2 bores, blind, flat floor y 209", "2 x d4.000, depth 6.000, blind; floors y 209 (12.566 mm2)", "PASS"),
 ("F08 pass-throughs x3 d12.0 along Z at (95, 30), (-100, 30), (-84, 30)", "3 bores, through", "3 x d12.000, length 3.000, offset 0.000, through", "PASS"),
 ("F09 vent slots x5, 4.0 x 80.0, ends R 2.0, centres x 78 ... 110", "5 slots; 10 R 2.0 half-cylinders, 10 side faces", "10 concave R 2.0 arcs (not bores), 10 side faces 228 mm2; each 4.000 x 80.000, through", "PASS"),
]
plaus = [
 ("P1 gravity", "Stands on the plate's top face y 0 (clearance 0.000, common 0.000 mm3), foot and flanges flat on it; prints on the outer face z -302 with everything else rising along +Z.", "YES"),
 ("P2 function chains", "Cord and both tube holes are through with nothing behind them to z -277 (0.000 mm3), gussets 3.434 / 2.000 / 2.000 away; vents open behind the bay; insert bores open upward at y 215; driver axes clear from y 4 to 260.", "YES"),
 ("P3 moving parts", "No moving parts; the assembly path (panel lowered from +40 in 1.0 steps, 41 poses) is clear of OD-C01, OD-C02, OD-C03 and OD-H01 (0.000 mm3).", "YES"),
 ("P4 grip, reach, insertion", "A straight d6 driver reaches all four flange screws from above (0.000 mm3; 2.0 clear of the ledge front and the boss faces); the panel drops straight down along -Y onto the plate.", "YES"),
 ("P5 next to a real product", "An ordinary appliance back panel: flat 3 mm wall, top ledge with two inserts, gusseted floor tabs, grommet holes low on the sides, vent slots behind the board.", "YES"),
 ("P6 floating, embedded, mirrored, upside-down", "One solid, embedded in nothing (0.000 mm3 with every neighbour); cord on +X (right) and tubes on -X (left) as spec section 4; flanges, gussets, ledge and bosses on the front (+Z) side; ledge at the top.", "YES"),
]
controls = [
 ("validity", "loose 5 mm cube 18 mm in front of the outer face: solid_count 2", "FAIL"),
 ("envelope", "wall's +X end extended 0.5 mm: size_x 232.5", "FAIL"),
 ("feature_census", "vent slot at x 110 filled: cylindrical faces 17", "FAIL"),
 ("bore_census", "flange hole (-81, -282) filled: bores 8", "FAIL"),
 ("locate_bore", "flange hole (81, -282) moved 0.5 mm along +X: offset 0.500", "FAIL"),
 ("radial_extent", "+X side of the boss at x 90 cut back 1.5 mm: bore wall 2.500", "FAIL"),
 ("min_wall", "20 x 20 pocket 1.5 deep in the outer face at (0, 60): wall 1.500", "FAIL"),
 ("min_wall_wide", "same pocket mutant: 1.500", "FAIL"),
 ("overhang_census", "pocket mutant with the exception holes plugged: flat ceiling 0.0 deg", "FAIL"),
 ("flat_ceiling_spans", "pocket mutant: span 19.700", "FAIL"),
 ("common_volume (keep-out box)", "5 mm cube on the inner face at (0, 50) in the tank zone: 120.000 mm3", "FAIL"),
 ("common_volume (lowering path)", "tab x 60 ... 70, y 100 ... 105 reaching z -235 into OD-C02: 100.000 mm3", "FAIL"),
 ("common_volume (driver cylinders)", "rib 6 x 2 x 10 at y 151 over the axis (95, -282): 56.549 mm3", "FAIL"),
 ("clearance", "panel moved 18 mm toward +Z: 19.026 to OD-C02", "FAIL"),
 ("footprint rim distance (reviewer code)", "flange's +X end extended to x 107: 1.300 to the feet-hole rim", "FAIL"),
 ("compare_step (round trip)", "the +0.5 mm envelope mutant against the delivered STEP: volume_delta 322.500 mm3", "FAIL"),
 ("mesh_census", "delivered STL with two triangles removed: 4 naked edges", "FAIL"),
 ("mesh_sagitta", "re-mesh at 0.1 mm / 0.5 rad: 0.04375", "FAIL"),
 ("mesh_deviation", "same coarse re-mesh: 0.04375", "FAIL"),
 ("section regions (E-06 ties)", "boss at x 90 cut free of the wall and the ledge by 0.5 gaps: not tied", "FAIL"),
 ("through ray (E-11, REQ-06)", "vent slot at x 110 filled: material on the ray", "FAIL"),
]
findings = [{"id": "F1", "gate": "REQ-09", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "bool",
             "required": "Soft: no visible drumming or flex with the top panel on and the side panels absent (bench)", "margin": None,
             "at": "whole wall, free vertical edges x +-116 over y 0 ... 215", "blocks": False, "risk": "MEDIUM",
             "risk_basis": "a 3.0 mm PETG wall 232 x 215 held at four floor screws and two top inserts with both side edges free until OD-C12/C13 exist may drum with the pump's vibration; only the first print can tell (A-11)",
             "fix_direction": "bench-test the first print with the top panel on; if it drums, add a vertical rib or tie the free edges once the side panels are designed"}]
least = [
 {"item": "Tube holes' 2.0 gap to the gussets behind the wall (1.950 at d12.1)", "answer": "Measured 2.000 (-100 hole to the -X outer gusset top at (-100, 22, -299)), 2.000 (-84 hole to the -X inner gusset face x -76), cord 3.434; with the holes at d12.1 1.950 each. No section 5 row sets this gap, so it is not a deviation; a grommet or fitting rear flange wider than about d16 would land on a gusset, which stays with A-04."},
 {"item": "Wall foot's U-03 margin: +0.300 nominal, +0.200 at wall_z +0.1", "answer": "Measured 2.300 from the feet-hole rims (+-110, -295) to the wall foot (limit 2.0); my own variant with the inner face at z -298.9 reads 2.200 (+0.200). It holds only while OD-C01's feet holes stay d3.4 at (+-110, -295): re-measure when OD-C01 is revised for A-01."},
 {"item": "Region split at the measured inner face is job code", "answer": "I split the y 0 underside face myself at z -299 and got the same numbers: wall foot 696.0 mm2 at 2.300, flanges 1371.683 mm2 at 4.300; the rim code FAILs on a mutant with the flange extended to x 107 (1.300), so the reading can fail."},
]
files = [(f, True) for f in ["02_STEP_STL/od_c11_back_C1_v03.step", "02_STEP_STL/od_c11_back_C1_v03.stl", "02_STEP_STL/od_c11_assembly_C1_v03.step"]] + [("02_STEP_STL/od_c11_back_C1_v03.3mf", False)]
import hashlib
fl = [{"path": f, "sha256": hashlib.sha256(open(f"{J}/{f}", "rb").read()).hexdigest(), "matches_report": m} for f, m in files]
assumed = sorted({a for x in gates if x["status"] == "PASS_ASSUMED" for a in x["assumes"]})
doc = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20261001-od-c11-back-panel", "target": "od_c11_back_v03",
       "spec_version": "1.2", "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"},
       "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
       "summary": "One valid solid 232.0 x 215.0 x 25.0 at x +-116, y 0 ... 215, z -302 ... -277; every Hard row passes when re-measured, 14 of them resting on open rows A-01 ... A-09; wall foot 2.300 from the feet-hole rims (limit 2.0); REQ-09 is a Soft bench row left INCONCLUSIVE (MEDIUM).",
       "files": fl, "gates": gates,
       "feature_census": [{"feature": a, "expected": b, "found": c, "status": d} for a, b, c, d in census],
       "plausibility": [{"question": a, "answer": b, "status": c} for a, b, c in plaus],
       "positive_controls": [{"check": a, "mutant": b, "got": c} for a, b, c in controls],
       "findings": findings, "least_sure_answers": least, "assumptions_relied_on": assumed}
json.dump(doc, open(f"{J}/reviews/RV01_od_c11_back_v03.json", "w"), indent=1, ensure_ascii=False)
print("assumed", assumed, "pass_assumed rows", sum(1 for x in gates if x["status"] == "PASS_ASSUMED"))
import sys; sys.exit(0)
schema = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
jsonschema.validate(doc, schema); print("valid")
for x in fl: print(x)
