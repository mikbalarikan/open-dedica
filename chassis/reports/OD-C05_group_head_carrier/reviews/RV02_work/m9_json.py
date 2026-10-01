import json, sys
from pathlib import Path
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
files = [
 ("02_STEP_STL/od_c05_carrier_C4_v04.step", "7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1"),
 ("02_STEP_STL/od_c05_assembly_C4_v04.step", "70390d91f1aa6ff710208065366aa3598675796fd76e782113f842cb59cd1a77"),
 ("02_STEP_STL/od_c05_carrier_C4_v04.stl", "7ecc4de80bd2b69533b534d660a74e9f3d25e6f14c0f954f93392913605eea2b"),
 ("02_STEP_STL/od_c05_carrier_C4_v04.3mf", "7fd7f6a12c0d3920f4c28c761c9f22a2e038b28fab69e49ff0a052096b53b6d7"),
 ("01_CAD/REPORT_od_c05_carrier_v04.md", "c6fca509698cac42c292c4bd7950f3346b5e78d1eeead09e494c2392261e61c2"),
 ("01_CAD/DESIGN_PLAN_v02.md", "c580be8de01b9060e96b8ed8b64640c34fefa5a7d71c5fb7e319cf4985cba6bf"),
 ("briefs/WP-05_designer.md", "a063c978322b35727ee18290245023daf8454a1508c2f73784d17b74877d89a8"),
 ("briefs/WP-06_designer.md", "c37d317a9179a587d52d2172317bd420df894b4108848b88e53ed02ec42b0ad2"),
 ("briefs/WP-07_designer.md", "e373fcd3502d6f9da392eb2a21f69bfb24494505d8202c4a90ebf31faf09ff88"),
 ("01_CAD/check_od_c05_carrier_v04.json", "1ac98922997de08a8e8e091a4a25e7c60ae4027607b3b9c62d455480e67a9cd2"),
 ("01_CAD/build_od_c05_carrier_v04.json", "69b57eae4df14bd02a0304a3e2fba05ccdf7bca2f25b4ed5ed841f8ab66e9305"),
 ("01_CAD/sections_od_c05_carrier_v04.json", "14e458b76b293399eba666f9a31af492f62203139a3b109e6d1312b513e04b9e"),
 ("01_CAD/sweep_v04/summary_v04.json", "5dfed2547113a8f451e599ebe392d37ccaf459dee48e95c278b3d7156ff15bbe"),
 ("03_Sections/od_c05_assembly_x0_v04_left.png", "475e12a2a6a556d925960dd2cf7041f5d7ed3e4545aebcb649c511acc443b058"),
 ("03_Sections/od_c05_assembly_y0_v04_front.png", "eb9f08ce9cc6b29882e96be22ff353afa8bcf6bb8cf4f6f996a5c9272beaa535"),
 ("03_Sections/od_c05_carrier_x0_v04_left.png", "903fe49d7fc2203c6a4651494e820b246d74eb28f6b7c338a762873bdcc7c3a1"),
 ("03_Sections/od_c05_carrier_x35_v04_left.png", "30678270d27ed691fb8ee5e9dd15310a625c41d7d2a8ed9acd6dd7f98d8c46f0"),
 ("03_Sections/od_c05_carrier_x53_v04_left.png", "b488b7150c4393ae341f980278b5888c24c35aa20101b8b85afa7f8f47c309f7"),
 ("03_Sections/od_c05_carrier_y0_v04_front.png", "f5552864272d7f34b61fcac837579274d104e2f7e442c121a7a7ed230c64bf17"),
 ("03_Sections/od_c05_carrier_ym100_v04_front.png", "1b78bca5d37f8e5081c08b7a94eedc719cb26883f5e90c56b3de28ea4ffea8a8"),
 ("03_Sections/od_c05_carrier_ym80_v04_front.png", "e3740700304349f4be0dfbcf20a62f885135b188a48ed7841a10141d54c9dd58"),
 ("03_Sections/od_c05_carrier_z165_v04_top.png", "06837f88f50a34f09375c73c3f864eacd4daf25eaa6341a378e27e9a0f7bd4d5"),
 ("03_Sections/od_c05_carrier_zm27p44_v04_top.png", "1fcc9436a60d3f14205e980d7ed5d025fbe3c0d77c0667050f0c9d809ee66b3c"),
 ("reviews/RV01_od_c05_carrier_v01.md", "e97b9778da1930dad125cc7e0080d5d270119ac47742e4bc66aedbf0f95ad8c4"),
 ("00_Spec/inputs/OD-G01_housing_C1_v02.step", "f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02"),
 ("00_Spec/inputs/OD-G04_brewing_gasket_support.step", "19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2"),
]
import hashlib
fl = []
for p, h in files:
    real = hashlib.sha256((J / p).read_bytes()).hexdigest()
    assert real == h, p
    fl.append({"path": p, "sha256": h, "matches_report": True})
def g(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}
gates = [
 g("U-01", 1, "bool", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "whole part: solid_count 1, brep_valid 1, naked_edges 0; 1 shell, 0 free shells, 0 free faces", "PASS", "validity"),
 g("U-02", 110.0, "mm", "110.0 x 152.0 x 210.0 each in [spec - 0.1, spec + 0.1]", 0.1, "size_x 110.000; also size_y 152.000, size_z 210.000 (each margin +0.100); x -55..55, y -102..50, z -29.94..180.06", "PASS", "envelope"),
 g("U-03", 0.0, "mm", "carrier|OD-G01 clearance = 0 at the contact, interference <= 0 mm3, holes coaxial <= 0.10; carrier|OD-G04 clearance >= 2.0; (b) N/A no motion", 0.0, "contact (-42.0, 50.0, -24.94); interference 0.000 mm3 (all pairs); coaxial 0.000 (margin +0.100); OD-G04 5.000 at carrier (30.0, 0.0, -24.94) / OD-G04 (30.0, 0.0, -19.94) (margin +3.000); housing offered along -Z from 40 mm: interference 0 at every step", "PASS_ASSUMED", "clearance, interference (common_volume), bore_census + locate_bore on both solids", ["A-01", "A-06"]),
 g("U-04", 1.4e-09, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.001, "label od_c05_carrier, AP242, MM, 1 solid, 1 shell; file vs re-read volume delta 0.000, faces delta 0, valid 1; my step_roundtrip volume delta 1.4e-9, faces delta 0, labels 1, valid 1", "PASS", "read_step, compare_step, step_roundtrip"),
 g("U-05", 17, "count", "counts per the plan: plate with hub window and hatch, column (front, two side, rear walls, rear window), roofed foot, 2 gussets, 4+4 D3.4 holes, 4+4 D6.5 counterbores (36 planar / 21 cyl concave / 0 convex / 17 bores)", 0, "36 planar, 21 cylindrical (21 concave, 0 convex), 17 bores, no other kind; 16 bores along Z located", "PASS", "feature_census, bore_census, locate_bore"),
 g("U-06", 2.75, "mm", ">= 2.0 (Soft, min_wall wide)", 0.75, "(-44.0, 50.0, -29.94) plate counterbore to front edge; 45 deg feather edges at the foot counterbore rims sit on the opposition limit (F3)", "PASS", "min_wall detail['wide'], min_wall_wide"),
 g("U-07", 0.004995, "mm", "STL tol 0.01, angular <= 4*acos(1 - 0.01/6.0) = 0.23097 rad, stl_max_sagitta <= 0.01, 3MF the same mesh", 0.005005, "sagitta at (-38.245, -92.007, 160.053); remesh at 0.01/0.20 byte-identical; 1 body, 0 naked, winding 1; mesh_deviation 0.004946; 3MF 5232 triangles matched one-to-one within 1.4e-6 mm", "PASS", "write_stl, mesh_sagitta, mesh_census, mesh_deviation, 3MF parse and triangle match"),
 g("U-08", None, "count", "threads cosmetic; applies to threaded parts; this target has none", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("D-01a", 2.75, "mm", "min_wall >= 0.8", 1.95, "(-44.0, 50.0, -29.94)", "PASS", "min_wall"),
 g("D-01b", 2.75, "mm", "min_wall >= 2.0", 0.75, "(-44.0, 50.0, -29.94)", "PASS", "min_wall"),
 g("D-02", 210.0, "mm", "each envelope size <= K1C build volume 220 x 220 x 250, plate down", 40.0, "210.0 tall (margin +40.0); 110.0 x 152.0 on the bed (margins +110.0, +68.0)", "PASS_ASSUMED", "envelope", ["A-08"]),
 g("D-03a", 45.0, "deg", ">= 45 from horizontal, build +Z, the eight counterbore floors excepted", 0.0, "census least (-10.0, -98.0, 140.0) gable flat; analytic: roof planes and gable flats 45.000000; exception rings 0.000 (8, by position)", "PASS_ASSUMED", "overhang_census(build_dir=(0,0,1)) on the part with the counterbores plugged; analytic face listing; sections", ["A-13"]),
 g("D-03b", 6.5, "mm", "span <= 5; counterbore floors <= 6.6 (named exception)", 0.1, "widest bridge 6.500 in the exception (counterbores); outside it 0 flat downward faces, 0 valleys (margin +5.0); peaks: ridge (-51..51, -78, 174.06), window apex (0, -102..-98, 150)", "PASS", "flat-ceiling and valley/peak finder on the analytic listing; sections x 0, x 35, y -100"),
 g("D-04a", 3.4, "mm", "all eight D3.4 holes >= 3.25", 0.15, "(+-44, +-44); (+-35, -72 / -92)", "PASS", "locate_bore"),
 g("D-06a", 2.75, "mm", ">= 1.0", 1.75, "(-44.0, 50.0, -29.94)", "PASS", "min_wall"),
 g("D-07", None, "count", "fit-critical bores: none on this part", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("E-06", 3200.0, "mm3", "plate tied to the front wall by two gussets and to the column by its lid; no free-standing boss", None, "gussets x +-(51..55), y -52..-12, z -24.94..15.06, 3200.000 each inside the one solid; plate's rear part is the column lid (section x 0)", "PASS", "common_volume with gusset boxes; validity; sections"),
 g("REQ-01", 0.0, "mm", "four D3.4 +- 0.1 through along Z at (+-44, +-44), offset <= 0.10 from the OD-G01 insert bores", 0.1, "(+-44, +-44): D3.400 x 3.000 through (margin +0.100), offset 0.000 from nominal and from the inserts", "PASS_ASSUMED", "bore_census + locate_bore on both solids", ["A-01"]),
 g("REQ-02", 2.0, "mm", "four D6.5 +- 0.1 counterbores 2.0 +- 0.1 deep from z -29.94, coaxial", 0.1, "(+-44, +-44): depth 2.000, D6.500, open at z -29.940, coaxial 0.000", "PASS_ASSUMED", "bore_census, locate_bore; section z -27.44", ["A-09"]),
 g("REQ-03", -24.94, "mm", "underside z = -24.94 +- 0.10; top z = -29.94 +- 0.10", 0.1, "underside planes z -24.940 (8036.25 and 1533.74 mm2); top z -29.940 (min_z); 2.000 + 3.000 = 5.000", "PASS_ASSUMED", "envelope, face listing, locate_bore", ["A-01"]),
 g("REQ-04", 30.0, "mm", "innermost material over z -29.94..-24.94 at every 10 deg >= 30.0, whole ray", -3.6e-15, "least theta 10 deg at (29.5442, 5.2094, -29.9); 180 rays all MEASURED at 30.000", "PASS_ASSUMED", "radial_extent(side='inner'), whole ray", ["A-06"]),
 g("REQ-05", 180.06, "mm", "underside z = +180.06 +- 0.10; 4.0 +- 0.1 under each head; floors z 176.06 +- 0.10", 0.1, "max_z 180.060; foot holes 4.000 long (z 176.06..180.06); floors 176.060", "PASS_ASSUMED", "envelope, locate_bore, face listing", ["A-03", "A-04"]),
 g("REQ-06", 0.0, "mm", "four D3.4 +- 0.1 through at (+-35, -72) and (+-35, -92), offset <= 0.10; D6.5 +- 0.1 counterbores from the roof, floor z 176.06 +- 0.10", 0.1, "offsets 0.000; holes D3.400 through; counterbores D6.500, coaxial 0.000, floors 176.060; rim lowest 164.810 / 156.810", "PASS_ASSUMED", "bore_census + locate_bore; edge sampling", ["A-04"]),
 g("REQ-07", -102.0, "mm", "envelope min_y >= -102.0", 0.0, "rear face y -102 (plate, column, foot)", "PASS_ASSUMED", "envelope", ["A-05"]),
 g("REQ-08", 1.0, "mm", "housing sides to the gussets >= 1.0 and to the front wall >= 2.0", 0.0, "gussets 1.000 at housing (-50, -42, -24.94) / gusset (-51, -42, -24.94); front wall 2.000 (margin 0.000) at (-42, -50, -24.94) / (-42, -52, -24.94)", "PASS_ASSUMED", "clearance on the carrier cut by position below the contact plane", ["A-01"]),
 g("REQ-09", None, "bool", "Soft: no visible flex under the locking torque, sideways push and brewing pull (bench)", None, "column and plate; hand estimate in the review section 7", "INCONCLUSIVE", "bench (first print); hand estimate", ["A-11"]),
]
census = [
 ("Plate with hub window and hatch", "z -29.94..-24.94, x +-55, y -102..50; R30 window; hatch x +-40, y -96..-64, 4 x R4", "top -29.940, underside -24.940; bore D60.000 through; 4 concave R4.000", "PASS"),
 ("Column front wall", "y -58..-52, 6.0, x +-55", "face y -52 at 2.000 from the housing; section x 0", "PASS"),
 ("Column side walls x2", "|x| 51..55, 4.0, y -102..-58", "inner faces x +-51; section z 165", "PASS"),
 ("Column rear wall with rear window and gable", "y -102..-98; window x +-10, z 110..140, 45 deg gable to apex z 150", "bottom z 110.000; gable flats 45.000000 deg z 140..150; section y -100", "PASS"),
 ("Foot with roof", "underside z 180.06; two 45 deg faces z 154.06 at y -58/-98 to ridge y -78, z 174.06", "two planes 45.000000 deg sharing ridge (+-51, -78, 174.06); underside 180.060", "PASS"),
 ("Gussets x2", "4.0 at |x| 51..55, legs 40", "3200.000 mm3 each", "PASS"),
 ("Plate holes x4 + counterbores x4", "D3.4 through, D6.5 x 2.0 at (+-44, +-44)", "4 x D3.400 x 3.000 through; 4 x D6.500 x 2.000; offsets 0.000", "PASS"),
 ("Foot holes x4 + counterbores x4", "D3.4 through at (+-35, -72/-92); D6.5 to floor z 176.06", "4 x D3.400 x 4.000 through; 4 x D6.500 to 176.060; offsets 0.000", "PASS"),
 ("Totals", "36 planar, 21 cyl (21/0), 17 bores, 1 solid", "36 / 21 / 21 / 0 / 17, 1 solid, 57 faces", "PASS"),
]
plaus = [
 ("P1 gravity", "Machine (-Z up): plate on the housing's rear face, housing hangs below, axis vertical, mouth down; closed column stands behind on the floor z 180.06. Print: roof ridge and window apex are the highest lines", "YES"),
 ("P2 function chains", "Holes coaxial with the inserts (0.000); hub window r 30.000 clears OD-G04 (5.000); TUBE 7: rear window, column, hatch, hub window; foot screw axes inside the hatch", "YES"),
 ("P3 moving parts", "No motion; housing seats along -Z with interference 0 and 1.000 side clearance over the path; gussets >= 52 from the axis behind the portafilter", "YES"),
 ("P4 human factors", "Housing screws from above, portafilter from below; foot screws through the hatch, 206.0 to the floors, at the edge of A-14's 200 driver (F5)", "YES"),
 ("P5 absurdity", "Nothing absurd: flat bracket on a closed tower behind the group head; the foot's inside is an undrained trough in the machine (F2)", "YES"),
 ("P6 floating, embedded, mirrored, upside-down", "One solid, interference 0 with both neighbours; roof and gable point +Z in the print; counterbores open away from their mating faces", "YES"),
]
controls = [
 ("validity (U-01)", "one face dropped, open shell: solid_count 0, naked_edges 7", "FAIL"),
 ("envelope (U-02, D-02, REQ-03, REQ-05, REQ-07)", "rear lip to y -102.5 (size_y 152.5); post to z 225.06 (size_z 255 > 250); pad under the top (min_z -30.44)", "FAIL"),
 ("compare_step / step_roundtrip (U-04)", "counterbore (+44,-44) filled vs the delivered file: volume delta 57.287 mm3, faces delta 1", "FAIL"),
 ("feature_census (U-05)", "counterbore (+44,-44) filled: 20 cylinders, 16 bores", "FAIL"),
 ("bore_census + locate_bore (U-03, U-05, D-04a, REQ-01, REQ-02, REQ-05, REQ-06)", "hole (+44,+44) moved 0.5: offset 0.500; foot hole D3.2; foot counterbore 1.0 deeper: hole 3.000, floor 177.06; plate counterbore 2.5 deep", "FAIL"),
 ("min_wall incl. wide (D-01a, D-01b, D-06a, U-06)", "+X side wall thinned to 1.5: 1.500, wide 1.500", "FAIL"),
 ("overhang_census plugged (D-03a)", "pointed front-wall window with 44.0 deg gables: 44.000 (known-good 45.0 twin: 45.000)", "FAIL"),
 ("analytic face listing (D-03a)", "same 44.0 deg window: 44.000000 (45.0 twin: 45.000000)", "FAIL"),
 ("flat-ceiling and valley finder (D-03b)", "flat-topped 20 x 20 slot: one flat ceiling 20.0 x 6.0; V-notched window: valley edge at (0, -58..-52, 70)", "FAIL"),
 ("radial_extent whole ray inner (REQ-04)", "4 x 5 bar into the hub window to r 26: 26.000", "FAIL"),
 ("clearance (U-03, REQ-08)", "carrier -0.5 Z: contact 0.500; +3.1 Z: OD-G04 1.900; gusset bump: 0.500; front-wall bump at the flange: 1.500", "FAIL"),
 ("interference / common_volume (U-03, E-06)", "carrier +3.1 Z: 21900.579 mm3 with OD-G01; gussets removed: 0.000 mm3", "FAIL"),
 ("write_stl / mesh_sagitta (U-07)", "meshed at 0.1 mm / 0.5 rad: 0.0489", "FAIL"),
 ("mesh_deviation (U-07)", "coarse STL: 0.0489", "FAIL"),
 ("mesh_census (U-07)", "delivered STL with one triangle dropped: 3 naked edges", "FAIL"),
 ("3MF / STL triangle match (U-07)", "coarse STL 2176 triangles vs 3MF 5232", "FAIL"),
]
def f(id, gate, kind, measured, unit, required, margin, at, blocks, risk, basis, fix):
    return {"id": id, "gate": gate, "kind": kind, "measured": measured, "unit": unit, "required": required, "margin": margin,
            "at": at, "blocks": blocks, "risk": risk, "risk_basis": basis, "fix_direction": fix}
findings = [
 f("F1", "REQ-09", "OBSERVATION", None, "rad", "Soft bench: no visible flex", None, "column y -102..-52; plate y -52..+50", False, "LOW",
   "Soft bench gate INCONCLUSIVE; hand estimates: column torsion 1.8e-3 rad (0.10 deg) at 10 N m, sway <= 0.14 mm at 50 N x 210, plate root about 0.02 mm at 100 N",
   "Bench the first print, preferably with the machine hot (A-12)"),
 f("F2", "P5", "OBSERVATION", None, "mm", "none specified (outside the gates)", None, "foot interior: trough bottom (y -78, z 174.06), counterbore floors z 176.06", False, "MEDIUM",
   "Water through the hatch (connection leak, condensate, TUBE 7) pools in an undrained ~41 ml trough and on the four screw heads, and can wick into OD-C01",
   "Spec change: a drain along Z at the ridge line through the 6.0 foot with a path in OD-C01 to the drip tray, or a hatch cover"),
 f("F3", "U-06", "OBSERVATION", 2.75, "mm", ">= 2.0 (Soft, wide 45 deg)", 0.75, "ridge-side rims of the four foot counterbores, e.g. (-35.10, -75.25, 171.34)", False, "LOW",
   "45 deg feather edges exactly on the wide opposition limit (0.032 at 46 deg); the lip carries no load, the head bears on the floor z 176.06",
   "None required; optionally a 0.5 flat or chamfer at the rims (spec change)"),
 f("F4", "D-03a", "OBSERVATION", 0.0, "deg", "named exception: eight counterbore floors, span <= 6.6", 0.1, "counterbore floors z -27.94 (+-44, +-44) and z 176.06 (+-35, -72/-92)", False, "LOW",
   "D-03a and D-03b pass inside the named exception (U-18); spec 2.2 records it for the Usta to confirm with section 5, still pending; 1.55 rings over D6.5 are usual FDM practice",
   "The Usta confirms section 5 with the exception"),
 f("F5", "REQ-08", "OBSERVATION", 1.0, "mm", ">= 1.0 gussets, >= 2.0 front wall; REQ-07 >= -102.0; A-14 driver about 200", 0.0, "gusset faces x +-51, wall y -52, rear face y -102; foot counterbore floors 206.0 below the plate top", False, "LOW",
   "Margins are 0 by the spec's construction (band absorbs float only); FDM growth takes the gusset gap to about 0.6-0.8, still free; foot heads 203-204 below the plate top, past A-14's 200 reach, 250 mm drivers common",
   "A-14 to name a >= 210 mm reach driver; optionally a print-growth allowance in REQ-08"),
]
least = [
 ("1 Drips in the foot's V-trough", "Confirmed: in the machine the ridge line (-78, 174.06) is the trough bottom and the counterbore floors 2.0 lower, no outlet; MEDIUM, non-blocking, a spec decision (F2)"),
 ("2 45 deg wedges at the foot counterbore rims (U-06)", "Confirmed: wide reading 2.750 at 45 deg; at 46 deg min_wall finds a 0.032 feather at (-35.10, -75.25, 171.34); U-06 PASS as defined (F3, LOW)"),
 ("3 REQ-09 risk MEDIUM", "Hand estimate: Bredt J 1.37e6 mm4, 1.8e-3 rad (0.10 deg) at 10 N m against about 0.3 rad for the spec 1.x wall (RV01 F2) and 5 deg in v02 section 9; sway 0.04/0.14 mm at 50 N; the 96 plate cantilever is stiffened by the bolted housing and gussets (about 0.02 mm at 100 N); rated LOW (F1), first print answers it"),
]
doc = {
 "schema": "oguz-verdict-v1", "review_id": "RV02", "job_id": "20260930-od-c05-group-head-carrier",
 "target": "od_c05_carrier_v04", "spec_version": "2.2",
 "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"},
 "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
 "summary": "All hard rows PASS or PASS_ASSUMED on the re-measured STEP (envelope 110 x 152 x 210, D-03a 45.000 deg outside the counterbore-floor exception, REQ-04 r 30.000, REQ-08 1.000/2.000); REQ-09 Soft INCONCLUSIVE LOW; P1-P6 YES; all controls FAIL; no blocking finding; undrained foot trough rated MEDIUM",
 "files": fl, "gates": gates,
 "feature_census": [{"feature": a, "expected": b, "found": c, "status": d} for a, b, c, d in census],
 "plausibility": [{"question": a, "answer": b, "status": c} for a, b, c in plaus],
 "positive_controls": [{"check": a, "mutant": b, "got": c} for a, b, c in controls],
 "findings": findings,
 "least_sure_answers": [{"item": a, "answer": b} for a, b in least],
 "assumptions_relied_on": ["A-01", "A-03", "A-04", "A-05", "A-06", "A-08", "A-09", "A-13"],
}
out = J / "reviews/RV02_od_c05_carrier_v04.json"
out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
schema = json.loads(Path("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json").read_text())
try:
    import jsonschema
    jsonschema.validate(doc, schema); print("schema valid")
except ImportError:
    print("no jsonschema")
# self-consistency
assert not any(x["blocks"] for x in findings)
assert all(x["assumes"] for x in gates if x["status"] == "PASS_ASSUMED")
assert set(a for x in gates if x["status"] == "PASS_ASSUMED" for a in x["assumes"]) == set(doc["assumptions_relied_on"])
assert all((x["measured"] is None) == (x["status"] in ("INCONCLUSIVE", "NOT_APPLICABLE")) for x in gates)
print(len(gates), "gates")
