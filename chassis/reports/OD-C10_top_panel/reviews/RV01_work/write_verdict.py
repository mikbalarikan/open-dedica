import json
from pathlib import Path
JOB = Path("/root/oguz-jobs/20261001-od-c10-top-panel")
files = [
 ("02_STEP_STL/od_c10_top_C1_v01.step", "0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f"),
 ("02_STEP_STL/od_c10_top_C1_v01.stl", "2e3f1c736115fe1b6efca9110229357fca8c840fe8786f4b0ccced3e39d93bc9"),
 ("02_STEP_STL/od_c10_top_C1_v01.3mf", "cbab510c1faddc029fe40c16b5b351a9c6179b44547af0bcac30729f5fc6e643"),
 ("02_STEP_STL/od_c10_assembly_C1_v01.step", "d5881320038a66454cfb9d8a2b89aba4ca38c4cc69cd9182cad4eb6a9ef3c9d9"),
 ("00_Spec/DESIGN_SPEC.md", "e2eda540dd141c27a3ca8f7a84f2d05cfbf99a1d8df283c03bff28000c4ee966"),
 ("01_CAD/DESIGN_PLAN.md", "0d0fc1a890e8431278bdd05ace29f67e8403dfa7a030ea4c36ce7c460171c0f7"),
 ("01_CAD/REPORT_od_c10_top_v01b.md", "2d5462f20f3fb0dd4267474db4a696cbff4cf71592837bee649437fca9802a8e"),
 ("01_CAD/check_od_c10_top_v01b.json", "1076b253f353c7cf8bd50c5a92e87e5bcb689696d2235b26bcf31428afbe5d4a"),
 ("01_CAD/build_record_v01.json", "61569d261817da34b2749064f9ad75e21f8b834ea6198d6ba439e83cbc12d197"),
 ("00_Spec/inputs/OD-C01_base_frame.step", "7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805"),
 ("00_Spec/inputs/OD-C02_bulkhead.step", "1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc"),
 ("00_Spec/inputs/OD-C05_group_head_carrier.step", "7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1"),
 ("00_Spec/inputs/OD-C07_valve_flowmeter_mount.step", "55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c"),
 ("00_Spec/inputs/OD-C11_back_panel_v02.step", "80803f53c7ca267565115d46c61c4280e95baaef6afd800eeae0afa1e3e16235"),
]
def G(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}
gates = [
 G("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "whole part: 1 solid, brep_valid 1, naked edges 0", "PASS", "validity"),
 G("U-02", 405.0, "mm", "240.0 x 39.5 x 405.0 each in [spec - 0.1, spec + 0.1]", 0.1, "sizes 240.000 x 39.500 x 405.000 (each margin 0.1); position x -120 ... 120, y 210.5 ... 250.0, z -305 ... 100 as specified", "PASS", "envelope"),
 G("U-03", 0.0, "mm", "(a) designed contacts clearance = 0, interference <= 0; coaxial <= 0.10; OD-C05 0.50 +/- 0.05 and nowhere less; OD-C07, OD-C01 >= 3.0; OD-C02, OD-C11 away from contacts >= 0.5; (b) descent from +40 in 2.0 steps interference <= 0",
   0.0, "contact clearance 0.000 / 0.000 mm3 at the four column seats (65,215,-60), (65,215,-210), (90,215,-293), (-90,215,-293), the rear skirt line (-110,215,-302) and the corner patches x +/-109.95...116 (5.907 mm2 each); hole-to-insert offset 0.000 (4 of 4); OD-C05 0.500 at the pads (-43,210.5,30), lid less pads 6.403; OD-C07 167.299; OD-C01 210.500; OD-C02 away 14.331; OD-C11 away 1.000 at (-95.5,216,-301.95); contact area outside seats and corners 0.000 mm2 (total 212.875 = 2 x 100.531 + 2 x 5.907); descent 21 poses +40 ... 0: 0.000 mm3 with all five references",
   "PASS_ASSUMED", "clearance, common_volume, locate_bore, bore_census, engaged_area", ("A-01", "A-02", "A-03")),
 G("U-04", 6.98e-10, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "part: AP242, unit MM, label od_c10_top, 1 solid, 0 free shells/faces; delivered file vs a copy: volume delta 0.0, faces delta 0; rewrite and re-read: volume delta 7e-10 mm3, faces delta 0, labels kept, valid after; assembly: AP242, 6 solids, 6 labels, 0 free shells, valid", "PASS", "compare_step, step_roundtrip"),
 G("U-05", 81, "count", "per the plan: 59 planar + 22 cylindrical (12 concave, 10 convex), 8 bores (4 x 3.4 through, 4 x 6.5 blind), skin, skirt, 4 columns, 2 pads, ribs", 0, "59 planar, 22 cylindrical (12 concave, 10 convex), 0 other; 8 bores along Y at the four column axes", "PASS", "feature_census, bore_census, locate_bore"),
 G("U-06", 2.75, "mm", "min_wall wide >= 2.0 (Soft)", 0.75, "(-92.98, 247.0, -294.30) wall round the 6.5 counterbore, rear column (-90,-293)", "PASS", "min_wall_wide (spacing 0.7)"),
 G("U-07", 0.005385, "mm", "STL tol 0.01, angular <= 4 acos(1 - 0.01/R_max) = 0.1789 rad, stl_max_sagitta <= 0.01; 3MF carries the same mesh", 0.004615, "fresh mesh of the STEP at 0.01 / 0.17 rad: sagitta 0.005385, 5164 triangles; delivered STL: 5164 triangles, 1 body, 0 naked edges, winding consistent, 433996.82 mm3, bbox = B-rep bbox, deviation to B-rep 0.00506; 3MF: unit mm, 5164 triangles identical to the STL (max coordinate difference 0), watertight, 433996.82 mm3", "PASS", "write_stl, mesh_sagitta, mesh_census, mesh_deviation"),
 G("U-08", None, "count", "threads cosmetic; applies to threaded parts; this target has none", None, None, "NOT_APPLICABLE", "N/A by its row"),
 G("D-01a", 2.75, "mm", "min_wall >= 0.8", 1.95, "(-92.98, 247.0, -294.30) counterbore wall, rear column (-90,-293)", "PASS", "min_wall (spacing 0.7)"),
 G("D-01b", 2.75, "mm", "min_wall >= 2.0", 0.75, "(-92.98, 247.0, -294.30) counterbore wall, rear column (-90,-293)", "PASS", "min_wall (spacing 0.7)"),
 G("D-02", 405.0, "mm", "each envelope size <= Kobra Max 3 volume (420 x 420 x 500, A-09): 240 x 405 on the bed, 39.5 tall", 15.0, "bed 240.0 (margin 180) and 405.0 (margin 15); height 39.5 (margin 460.5)", "PASS_ASSUMED", "envelope", ("A-09",)),
 G("D-03a", 90.0, "deg", "every downward face >= 45 deg, build dir -Y; the four counterbore floors excepted by position", 45.0, "counterbores refilled by position (r 3.30, y 218 ... 250): no downward-facing sample; whole part: 0 deg only on the four floors at y 218 (named exception, 4 x 24.104 = 96.42 mm2)", "PASS_ASSUMED", "overhang_census(build_dir=(0,-1,0), spacing 0.7)", ("A-08",)),
 G("D-03b", 3.139, "mm", "span <= 5; only the four counterbore floors bridge (named exception)", 1.861, "the four counterbore floor rings at y 218, widest bridge 3.139 at (66.5,218,-60.8); none other (0 ceilings with the counterbores refilled); sections at y 217.5 and through each axis", "PASS_ASSUMED", "flat_ceiling_spans(build_dir=(0,-1,0), max_span 5, spacing 0.7); reviewer sections", ("A-08",)),
 G("D-04a", 3.4, "mm", "the four column holes diameter >= 3.25", 0.15, "all four holes 3.400 through, y 215 ... 218", "PASS", "bore_census, locate_bore"),
 G("D-05a", None, "count", "heat-set insert boss: none on this part", None, None, "NOT_APPLICABLE", "N/A by its row"),
 G("D-05b", None, "count", "heat-set insert hole: none on this part", None, None, "NOT_APPLICABLE", "N/A by its row"),
 G("D-06a", 2.75, "mm", "minimum feature >= 1.0", 1.75, "(-92.98, 247.0, -294.30)", "PASS", "min_wall (spacing 0.7)"),
 G("D-07", None, "count", "fit-critical bores: none", None, None, "NOT_APPLICABLE", "N/A by its row"),
 G("J-05", None, "count", "wall around a threaded hole: none on this part", None, None, "NOT_APPLICABLE", "N/A by its row"),
 G("E-06", 2, "count", "every column tied into the skin and by two ribs (the rear two also into the rear skirt); pads tied into the skin", 0, "bulkhead columns: 2 ribs each along +/-X, 3.0 thick, root y 229.3 at the column, 20 along the skin; rear columns: 2 ribs each at x = xc +/- 4 into the rear skirt (one cut face skin-skirt-rib at x 94); pads fused to the skin (one solid; y 230 section: 5 islands = skirt+rear columns, 2 bulkhead columns, 2 pads)", "PASS", "reviewer sections (write_sections), face census by position"),
 G("REQ-01", 3.0, "mm", "top face one plane at y 250.00 +/- 0.10; skin 3.0 +/- 0.1 (underside y 247.0)", 0.1, "one planar face at y 250.000 (96981.4 mm2, less 4 counterbore mouths); skin 3.000 at 7 points", "PASS_ASSUMED", "envelope, radial_extent", ("A-06",)),
 G("REQ-02", 3.0, "mm", "outline x +/-120.0, z -305.0 ... 100.0 +/- 0.1; corners R 10.0 +/- 0.1; skirt 3.0 +/- 0.1 all round; skirt bottom y 215.00 +/- 0.10", 0.1, "outline as specified; corners R 10.000 (inner R 7.000) at 12 angles x 2 heights; skirt 3.000 at 27 side points; skirt bottom one face at y 215.000", "PASS_ASSUMED", "envelope, radial_extent", ("A-04",)),
 G("REQ-03", 215.0, "mm", "columns 12.0 +/- 0.1 at (65,-60), (65,-210), offset <= 0.10; bottoms y 215.00 +/- 0.05; 3.4 +/- 0.1 through, coaxial with OD-C02 inserts <= 0.10; 6.5 +/- 0.1 counterbores, floors y 218.0 +/- 0.1", 0.05, "column bottoms y 215.000 (margin 0.05); columns 12.000, offset 0.000; holes 3.400 through, offset to the 4.0 x 6.0 inserts 0.000; counterbores 6.500, floors y 218.000, mouths y 250.000", "PASS_ASSUMED", "locate_bore on both solids, bore_census, radial_extent", ("A-01", "A-05")),
 G("REQ-04", 215.0, "mm", "columns 12.0 +/- 0.1 at (+/-90,-293), offset <= 0.10; bottoms y 215.00 +/- 0.05; 3.4 through, coaxial with OD-C11 inserts <= 0.10; counterbores as REQ-03", 0.05, "column bottoms y 215.000 (margin 0.05); columns 12.000, offset 0.000; holes 3.400 through, offset to OD-C11 v02 inserts 0.000; counterbores 6.500, floors y 218.000", "PASS_ASSUMED", "locate_bore on both solids, bore_census, radial_extent", ("A-02", "A-05")),
 G("REQ-05", 0.5, "mm", "pads 10.0 +/- 0.1 at (+/-48,30), offset <= 0.10, bottoms y 210.50 +/- 0.05; clearance to OD-C05 0.50 +/- 0.05; >= 10 from hub window edge (r >= 40); >= 20 from housing-screw counterbores", 0.05, "both pads clearance 0.500 at (53,210.5,30) and (-43,210.5,30); diameter 10.000, centre (+/-48.000, 30.000), bottoms y 210.500; edge r 43.042 from the hub axis (0,32) (margin 3.042); 33.940 to the nearest 6.5 counterbore at (+/-44,-12) (margin 13.94)", "PASS_ASSUMED", "clearance, radial_extent, bore_census", ("A-03",)),
 G("REQ-06", 0.0, "mm3", "no material below y 247.0 in the box x +/-42, z -70 ... 70: interference = 0", 0.0, "box x +/-42, y 200 ... 247, z -70 ... 70: 0.000 mm3 (also 0.000 to y 246.99)", "PASS_ASSUMED", "common_volume", ("A-06",)),
 G("REQ-07", 0.0, "mm3", "each screw axis clear from y 250 to its counterbore floor: 6.5 open over the whole depth", 0.0, "all four: 6.0 driver y 218.05 ... 260: 0.000 mm3; 6.49 cylinder y 218.01 ... 251: 0.000 mm3; counterbores 6.500, length 32.0, mouth y 250", "PASS", "locate_bore, common_volume"),
 G("REQ-08", None, "bool", "Soft bench: no visible sag or rattle on four columns with the side panels absent; a hand bears on the pads", None, "not a geometric gate (first print)", "INCONCLUSIVE", "bench (by its row)", ("A-04", "A-11")),
 G("exactly_one_solid", 1, "count", "== 1", 0, "the part STEP", "PASS", "validity"),
 G("feature_census", 81, "count", "plan section 3 topology", 0, "as U-05", "PASS", "feature_census, bore_census"),
 G("envelope_within_spec", 405.0, "mm", "240.0 x 39.5 x 405.0 +/- 0.1", 0.1, "as U-02", "PASS", "envelope"),
]
census = [
 ("F01 top skin y 247 ... 250, outline R 10 corners", "1 planar face at y 250; skin 3.0", "1 face at y 250.000 (96981.4 mm2); skin 3.000 at 7 points; underside main face at y 247 plus 2 pocket faces", "PASS"),
 ("F02 perimeter skirt 3.0, y 215 ... 247", "4 outer + 4 inner planes, 4 R 10 + 4 R 7 corner cylinders, 1 bottom face at y 215", "4 + 4 planes, 4 convex R 10 + 4 concave R 7, 1 bottom face y 215 (3790.2 mm2)", "PASS"),
 ("F03 four columns 12.0, y 215 ... 247", "4 convex cylinders R 6 at (65,-60), (65,-210), (+/-90,-293); 4 bottom faces y 215", "4 cylinders R 6.000, offset 0.000; 4 bottom faces y 215.000", "PASS"),
 ("F04 bulkhead-column ribs, 2 per column", "8 side planes + 4 hypotenuses", "8 side planes (z -61.5/-58.5, -211.5/-208.5) + 4 hypotenuses, x 45 ... 85", "PASS"),
 ("F05 rear-column ribs, 2 per column, into the rear skirt", "16 sides, 4 bottoms y 216, 4 hypotenuses", "16 sides (x +/-84.5, 87.5, 92.5, 95.5), 4 bottoms y 216.0, 4 hypotenuses to z -273", "PASS"),
 ("F06 two rest pads 10.0, bottom y 210.5", "2 convex cylinders R 5 at (+/-48,30), 2 bottom faces", "2 cylinders R 5.000 at (+/-48.000, 30.000), bottoms y 210.500", "PASS"),
 ("F07 four 3.4 through-holes y 215 ... 218", "4 concave R 1.7 bores, through", "4 bores 3.400, through, offset 0.000", "PASS"),
 ("F08 four 6.5 counterbores y 218 ... 250", "4 concave R 3.25 bores, blind, open at y 250", "4 bores 6.500, length 32.0, blind, open at y 250", "PASS"),
]
plaus = [
 ("P1 gravity", "Screwed, the lid sits on the four column seats and the rear skirt on OD-C11's wall top; unscrewed, its centre of mass (0.98, 242.77, -105.21) lies 24 mm outside the seat polygon on -X, so it settles 0.5 onto the left pad on the carrier until the screws pull it flat.", "YES"),
 ("P2 function chains", "Screw from above through the 6.5 counterbore, head on the 3.0 floor at y 218, shank through the 3.4 hole into an insert coaxial at 0.000; hand load to the pads, then to the carrier after 0.5.", "YES"),
 ("P3 moving parts", "The only motion is lowering along -Y: 21 poses +40 ... 0 give 0.000 mm3 with every reference; the skin's underside is 37 above the carrier's plate.", "YES"),
 ("P4 grip, reach, insertion", "All four counterbores open at the top face, 6.0 driver path clear to 0.05 above each floor; the lid lifts straight up by its skirt.", "YES"),
 ("P5 absurdity", "A 240 x 405 x 39.5 printed cover, 3.0 walls, 551 g PETG, screw bosses on the bulkhead and back panel: an ordinary appliance top cover; the asymmetric screw layout follows the spec.", "YES"),
 ("P6 floating, embedded, mirrored, upside-down", "One solid; 0 mm3 with every reference; columns at x +65 over OD-C02's rail (x 59 ... 71), the rear pair over OD-C11's inserts; top face at y 250, columns hang down.", "YES"),
]
controls = [
 ("validity", "lid plus a loose 10 mm cube above the skin: solid_count 2", "FAIL"),
 ("envelope", "+X skirt bulged to x 121 over z -20 ... 20: size_x 241.0", "FAIL"),
 ("bore_census / locate_bore", "hole (65,-60) moved +0.5 in X: offset 0.500 > 0.10", "FAIL"),
 ("feature_census", "hole (90,-293) filled: bores 7 != 8; pad (48,30) removed: convex cylinders 9 != 10", "FAIL"),
 ("radial_extent", "+X skirt thinned 0.5 from inside at z 0: 2.50 outside 3.0 +/- 0.1", "FAIL"),
 ("clearance", "lid lowered 0.2: pad clearance 0.300 outside 0.50 +/- 0.05; rear rib bottom lowered onto OD-C11's ledge: clearance away 0.000 < 0.5", "FAIL"),
 ("common_volume", "lid lowered 0.2: 38.92 mm3 with OD-C02; 10 x 10 x 7 boss under the skin: 700 mm3 in REQ-06's box; pad extended 1.0 down: descent 39.27 mm3 with OD-C05", "FAIL"),
 ("engaged_area", "rear rib bottom lowered onto OD-C11's ledge: 5.09 mm2 contact outside the seats and corner patches", "FAIL"),
 ("min_wall / min_wall_wide", "+X skirt thinned to 1.5 over y 216 ... 246, z -10 ... 10: 1.000 < 2.0 (both readings)", "FAIL"),
 ("overhang_census", "counterbores refilled plus a 20 x 20 x 2 pocket from the top face: 0 deg < 45", "FAIL"),
 ("flat_ceiling_spans", "same mutant: span 19.70 > 5", "FAIL"),
 ("compare_step / step_roundtrip", "1 mm deep 10 x 10 pocket in the top face against the delivered STEP: volume delta 100.0 mm3", "FAIL"),
 ("mesh_census", "delivered STL less 20 triangles: 24 naked edges", "FAIL"),
 ("mesh_deviation", "delivered STL shifted 0.5 in X: 0.505 > 0.01", "FAIL"),
 ("write_stl / mesh_sagitta", "lid meshed at 0.1 mm / 0.5 rad: sagitta 0.0714 > 0.01", "FAIL"),
]
findings = [
 {"id": "F1", "gate": "REQ-08", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "bool", "required": "no visible sag or rattle on four columns, side panels absent; a hand bears on the pads",
  "margin": None, "at": "free -X and front edges; front-left corner (-120, 250, 100) is 245 from the nearest screw seat (65,-60) and 100 from the nearest pad (-48,30)",
  "blocks": False, "risk": "MEDIUM",
  "risk_basis": "INCONCLUSIVE by its row (bench gate): a 3.0 PETG skin 240 x 405 with a 32 skirt held along x 65 and the rear only, centre of mass 24 mm outside the seat polygon; the pads catch a hand after 0.5, but drumming or rattle at the free edges cannot be ruled out without the first print",
  "fix_direction": "answer on the first print (A-11); if it drums or sags, add skin ribs toward the free corner or a third seat on the -X side, or land the side and front panels (A-04)"},
 {"id": "F2", "gate": "U-03", "kind": "OBSERVATION", "measured": 0.0, "unit": "mm", "required": "designed contacts clearance = 0, interference <= 0",
  "margin": 0.0, "at": "four column seats at y 215, rear skirt line (x +/-116, 215, -302) and corner patches x +/-110 ... 116",
  "blocks": False, "risk": "LOW",
  "risk_basis": "the lid seats on four columns plus the rear skirt line and two 5.9 mm2 patches, all exactly at 0 by design; column and skirt bottoms are the same last layer in the upside-down print, so a mismatch comes from warp, and the screw clamp closes a 0.1 gap within PETG compliance with no function depending on both touching",
  "fix_direction": "none needed for v01; if the first print rocks before screwing, relieve the rear skirt bottom by about 0.3 (a spec change to U-03 (a))"},
]
least = [
 ("1 Stiffness (REQ-08, A-11)", "INCONCLUSIVE by its row; geometry supports the concern: free front-left corner 245 from the nearest screw seat, centre of mass 24 mm outside the seat polygon on -X (the left pad takes it unscrewed). Risk MEDIUM (F1)."),
 ("2 OD-C11 reference unreviewed (build v02)", "Measured against v02 (80803f53...): rear seats 100.53 mm2 each, coaxial 0.000, corner patches 5.907 mm2 each, nothing else touching (outside area 0.000), away 1.000. Its third build changes gussets near the floor only; no lid row reads below y 200. U-03 and REQ-04 are PASS_ASSUMED on A-02; re-measure if the wall top, its x +/-116 ends, the ledge or the bores move."),
 ("3 The ribs are a design choice", "E-06 PASS from my sections: two 3.0 ribs per column, the rear pairs into the rear skirt. The 5.0 pocket between each rear pair opens downward; with the counterbores refilled the overhang census finds no downward face, so it prints unsupported; a dust trap only."),
 ("Brief: designed contacts pass only at nominal", "Confirmed by construction: seats and skirt contacts are exactly 0.000 clearance and 0.000 mm3; any height error opens a gap or an overlap. Rated LOW (F2)."),
 ("Brief: over-constraint and rocking", "Screwed: four seats plus the rear skirt line and patches, closed by the clamp. Unscrewed: the lid tips 0.5 onto the left pad (centre of mass 24 mm outside the seat polygon). No gate fails; F2."),
 ("Brief: open assumptions A-01 ... A-13", "PASS rows rest on A-01, A-02, A-03, A-04, A-05, A-06, A-08, A-09. A-03: pads 0.500 above the delivered carrier, 33.94 from its counterbores; A-06: 37.0 headroom, REQ-06 box 0 mm3; A-09: 405 on a 420 bed, margin 15; A-10 (PETG over the group head) is not a geometric row: the lowest point is 37 above the carrier's plate."),
]
assum = ["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-08", "A-09"]
doc = {
 "schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20261001-od-c10-top-panel", "target": "od_c10_top_v01",
 "spec_version": "1.2", "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"},
 "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
 "summary": "One valid 434010.6 mm3 solid, 240 x 39.5 x 405; every Hard row passes on re-measurement (seats and OD-C11 contacts 0.000 mm / 0.000 mm3, pads 0.500 to OD-C05, OD-C11 away 1.000, walls 2.75, counterbore floors the only bridges at 3.14); REQ-08 Soft INCONCLUSIVE (bench); 15 control families FAIL on their mutants.",
 "files": [{"path": p, "sha256": h, "matches_report": True} for p, h in files],
 "gates": gates,
 "feature_census": [{"feature": a, "expected": b, "found": c, "status": d} for a, b, c, d in census],
 "plausibility": [{"question": a, "answer": b, "status": c} for a, b, c in plaus],
 "positive_controls": [{"check": a, "mutant": b, "got": c} for a, b, c in controls],
 "findings": findings,
 "least_sure_answers": [{"item": a, "answer": b} for a, b in least],
 "assumptions_relied_on": assum,
}
(JOB / "reviews/RV01_od_c10_top_v01.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")

def cell(v): return "—" if v is None or v == "" else str(v)
st = {"PASS_ASSUMED": "PASS (assumed: {})", "NOT_APPLICABLE": "N/A: by its row (none on this part)"}
md = []
md.append("# RV01 — od_c10_top_v01 (20261001-od-c10-top-panel) — 2026-10-01 UTC\n")
md.append("Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted")
md.append("Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` · report `01_CAD/REPORT_od_c10_top_v01b.md`\n")
md.append("**VERDICT: APPROVED (assumption-conditional)**")
md.append("Blocking findings: 0 · open assumptions relied on: " + ", ".join(assum) + "\n")
md.append("Measured on the exported STEP files, re-imported. The references were placed by the reviewer from `00_Spec/inputs/` per spec §2. Their envelopes match the six solids of the check assembly STEP. Bands: mm 0.005, mm³ 0.001, deg 0.001, counts 0 (GATES §0 as the plan states). Scripts, mutants, sections and raw JSON are in `reviews/RV01_work/`.\n")
md.append("## 1. Files reviewed\n\n| File | SHA-256 | Matches REPORT |\n|---|---|---|")
for p, h in files: md.append(f"| `{p}` | {h} | yes |")
md.append("\nAll 30 files in the brief's table hash as listed. The five reference inputs match `briefs/WP-02_designer.md`.\n")
md.append("## 2. Gate table\n\n| Gate | Measured | Required | Margin | At | Status | Method | Assumes |\n|---|---|---|---|---|---|---|---|")
for g in gates:
    s = g["status"]
    s = st["PASS_ASSUMED"].format(", ".join(g["assumes"])) if s == "PASS_ASSUMED" else st.get(s, s)
    meas = "—" if g["measured"] is None else f"{g['measured']} {g['unit']}"
    md.append(f"| {g['gate']} | {meas} | {g['required']} | {cell(g['margin'])} | {cell(g['at'])} | {s} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
md.append("\nREQ-08 is a Soft bench row: INCONCLUSIVE by its own wording. It is rated in F1 and does not block. U-06 is Soft and passes.\n")
md.append("## 3. Feature census against the plan\n\n| Plan feature | Expected | Found | Status |\n|---|---|---|---|")
for a, b, c, d in census: md.append(f"| {a} | {b} | {c} | {d} |")
md.append("\n## 4. Plausibility (`GATES.md` §P, one line each)\n\n| # | Question | Answer | Status |\n|---|---|---|---|")
for a, b, c in plaus: md.append(f"| {a.split()[0]} | {' '.join(a.split()[1:])} | {b} | {c} |")
md.append("\n## 5. Positive controls\n\n| Check | Mutant of this job's part | Got |\n|---|---|---|")
for a, b, c in controls: md.append(f"| `{a}` | {b} | {c} |")
md.append("\n## 6. Findings\n\n| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |\n|---|---|---|---|---|---|---|---|---|---|")
for f in findings:
    meas = "not measured (bench)" if f["measured"] is None else f"{f['measured']} {f['unit']}"
    md.append(f"| {f['id']} | {f['gate']} | {f['kind']} | {meas} → {f['required']} | {cell(f['margin'])} | {f['at']} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {f['risk_basis']} | {f['fix_direction']} |")
md.append("\n## 7. \"Least sure of\", answered\n\n| REPORT item | What the review found |\n|---|---|")
for a, b in least: md.append(f"| {a} | {b} |")
md.append("")
(JOB / "reviews/RV01_od_c10_top_v01.md").write_text("\n".join(md))
print("written")
