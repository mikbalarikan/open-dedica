import json, hashlib
from pathlib import Path
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
paths = """01_CAD/REPORT_od_c01_frame_v02.md
01_CAD/DESIGN_PLAN.md
briefs/WP-03_designer.md
briefs/WP-04_designer.md
01_CAD/check_od_c01_frame_v02.json
01_CAD/build_record_v02.json
01_CAD/sections_v02.json
01_CAD/sweep_v02/sweep_summary_v02.json
02_STEP_STL/od_c01_frame_C1_v02.step
02_STEP_STL/od_c01_assembly_C1_v02.step
02_STEP_STL/od_c01_frame_C1_v02.stl
02_STEP_STL/od_c01_frame_C1_v02.3mf""".split("\n")
paths += sorted(str(p.relative_to(J)) for p in (J / "03_Sections").glob("od_c01_frame_v02_*.png"))
paths += ["00_Spec/inputs/OD-C03_pump_cradle.step", "00_Spec/inputs/OD-C04_thermoblock_mount.step",
          "00_Spec/inputs/OD-G01_housing_C1_v02.step", "00_Spec/inputs/OD-H01_ulka_ep5_pump.step",
          "00_Spec/inputs/OD-H11_thermoblock.step"]
files = [{"path": p, "sha256": hashlib.sha256((J / p).read_bytes()).hexdigest(), "matches_report": True} for p in paths]
def g(gate, m, unit, req, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": m, "unit": unit, "required": req, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}
P, PA, NA, INC = "PASS", "PASS_ASSUMED", "NOT_APPLICABLE", "INCONCLUSIVE"
gates = [
 g("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "plate STEP: solid_count 1, brep_valid 1 (BOPAlgo faults none, loose shells 0, loose faces 0), naked_edges 0 of 102 edges; the six other check-assembly solids 1/1/0 except OD-H11 brep_valid 0 (input, OD-C04 A-14)", P, "validity"),
 g("U-02", 405.0, "mm", "240.0 x 6.0 x 405.0 each in [spec - 0.1, spec + 0.1]", 0.1, "size 240.000 x 6.000 x 405.000; position x -120.000..120.000, y -6.000..0.000, z -305.000..100.000", P, "envelope"),
 g("U-03", 0.0, "mm", "(a) contacts clearance = 0 and interference <= 0 mm3; holes coaxial <= 0.10; plate|OD-H01 >= 2.0; plate|OD-H11 >= 10.0; OD-C03|OD-C04 >= 2.0; OD-H11 max z <= -85.0; OD-G01 v02 at its pose >= 2.0 to everything else; (b) N/A", 0.0,
   "governing: plate|OD-C03 contact 0.000 at (-2, 0, -171) and plate|OD-C04 0.000 at (-38, 0, -114), common volume 0.000 mm3 each; plate|foot box 0.000 at (-33, 0, -40); coaxial offsets 0.000 on all 8 mount holes (Ø3.4 over Ø4.0); plate|OD-H01 16.250 at (33.5, 0, -205.2); plate|OD-H11 16.4925 at (-9.66, 0, -140) (boolean not relied on; bbox-disjoint); OD-C03|OD-C04 8.000; OD-H11 max z -89.210; OD-G01 pose read back x->X, y->+Z, z->-Y, rear face y 205.000, mouth plane y 176.760, x +-50, z -18..82; OD-G01 least clearance 110.780 to OD-H11; path: clearance = lift at 10, 1, 0.1, 0.01, 0 for OD-C03, OD-C04, foot box",
   PA, "clearance, interference, bore_census + locate_bore on both solids, envelope", ("A-01", "A-02", "A-03")),
 g("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "plate STEP: label od_c01_frame, 1 solid, 0 loose shells/faces, valid 1; reviewer rewrite of the delivered solid: volume delta 0.0 mm3, faces delta 0 (36), label kept, valid after 1; check assembly (not the gated target): 7 labels kept, rewrite deltas <= 3e-9 mm3 per part; OD-H11 input->assembly volume integral 0.0524 mm3 on an unsound body with identical 406 faces and 734 vertices (F2)", P, "step_roundtrip, compare_step, validity"),
 g("U-05", 26, "count", "1 plate, 20 Ø4.0, 4 Ø3.4, 2 Ø8.0 through-holes", 0, "1 solid; 26 bores all through, length 6.000: 20 Ø4.000, 4 Ø3.400, 2 Ø8.000, each located at its spec axis with offset 0.000; faces 6 planar, 30 cylindrical (26 concave, 4 convex)", P, "feature_census, bore_census, locate_bore"),
 g("U-06", 5.0, "mm", ">= 2.0 (Soft, min_wall wide)", 3.0, "(-115, -5.7, -42): web from OD-C07 hole (-113, -42) to the edge x -120; spacing 0.7", P, "min_wall_wide(spacing=0.7)"),
 g("U-07", 0.004975, "mm", "STL tol 0.01, angular <= 0.2310 rad; stl_max_sagitta <= 0.01; the 3MF carries the same mesh", 0.005025, "delivered STL vs B-rep mesh_deviation 0.004975 at (-77.66, -3.0, -226.75); re-mesh at 0.01 / 0.20 rad: 7068 triangles, sagitta 0.004972; STL 1 body, 0 naked edges, winding 1, volume 580358.524 vs B-rep 580355.904; 3MF: 7068 triangles, mm, no transform, all 7068 equal to the STL's, volume 580358.524", P, "write_stl, mesh_sagitta, mesh_deviation, mesh_census, reviewer 3MF parse"),
 g("U-08", None, "count", "applies to threaded parts; this target has none", None, None, NA, "none (N/A by its row)"),
 g("D-01a", 5.0, "mm", "min_wall >= 0.8", 4.2, "(-115, -5.7, -42), OD-C07 hole to the left edge; spacing 0.7; mesh corroboration 5.0025", P, "min_wall(spacing=0.7)"),
 g("D-01b", 5.0, "mm", "min_wall >= 2.0", 3.0, "(-115, -5.7, -42), OD-C07 hole to the left edge; spacing 0.7", P, "min_wall(spacing=0.7)"),
 g("D-02", 405.0, "mm", "each envelope size <= Kobra Max 3 build volume (420 x 420 x 500), flat", 15.0, "240.0 x 405.0 on the bed, 6.0 tall", PA, "envelope", ("A-09",)),
 g("D-03a", 90.0, "deg", "every downward face >= 45 deg from horizontal, build +Y; none but the bed face", 45.0, "no downward point off the bed (200283 bed samples, 0 below 45); spacing 0.7", PA, "overhang_census(build_dir=(0,1,0), spacing=0.7)", ("A-14",)),
 g("D-03b", 0.0, "mm", "span <= 5: none", 5.0, "no downward face off the bed; reviewer sections at y -0.001, -3, -5.999 each one piece of 96725.984 mm2 (straight vertical holes, no roof)", P, "overhang_census + reviewer sections"),
 g("D-04a", 3.4, "mm", "four feet holes Ø >= 3.25", 0.15, "(+-110, -3, 90) and (+-110, -3, -295), all Ø3.400 through", PA, "locate_bore", ("A-12",)),
 g("D-05a", 14.0, "mm", "material >= 8.0 across around each Ø4.0 hole", 6.0, "(-113, -3, -42) and (-113, -3, -148.5) at 180 deg: material r 2.0..7.0; 4320 rays + exact 180 deg ray, 0 unread", PA, "bore_census, radial_extent", ("A-11",)),
 g("D-05b", 4.0, "mm", "twenty insert holes Ø4.0 +- 0.05, depth >= 5.7", 0.05, "all 20 Ø4.000, length 6.000 through (depth margin +0.3)", PA, "bore_census, locate_bore", ("A-11",)),
 g("D-06a", 5.0, "mm", ">= 1.0", 4.0, "(-115, -5.7, -42); spacing 0.7", P, "min_wall(spacing=0.7)"),
 g("D-07", None, "mm", "none: no fit-critical bores", None, None, NA, "none (N/A by its row)"),
 g("J-05", 5.0, "mm", ">= 3.0 around each of the twenty insert holes", 2.0, "min_wall 5.000 at (-115, -5.7, -42); ring wall r 7.0 - 2.0 = 5.0 at (-113, -42) and (-113, -148.5), 180 deg", P, "min_wall(spacing=0.7), radial_extent"),
 g("E-06", None, "count", "no bosses on this part", None, None, NA, "none (N/A by its row)"),
 g("REQ-01", 4.0, "mm", "four Ø4.0 +- 0.05 through at (+-35, -40), (+-35, -60), offset <= 0.10", 0.05, "all four Ø4.000 through, offset 0.000 (offset margin +0.10)", PA, "locate_bore", ("A-01",)),
 g("REQ-02", 4.0, "mm", "four Ø4.0 +- 0.05 at (+-40, -148), (+-40, -114), offset <= 0.10, coaxial with OD-C04", 0.05, "all four Ø4.000 through, offset 0.000; OD-C04 Ø3.4 axes coaxial, offset 0.000", PA, "locate_bore", ("A-02",)),
 g("REQ-03", 4.0, "mm", "four Ø4.0 +- 0.05 at (-4, -239), (-4, -171), (37, -239), (37, -171), offset <= 0.10, coaxial with OD-C03", 0.05, "all four Ø4.000 through, offset 0.000; OD-C03 Ø3.4 axes coaxial, offset 0.000", PA, "locate_bore", ("A-03",)),
 g("REQ-04", 4.0, "mm", "four Ø4.0 +- 0.05 at (65, -45 / -105 / -165 / -225), offset <= 0.10", 0.05, "all four Ø4.000 through, offset 0.000", PA, "locate_bore", ("A-04",)),
 g("REQ-05", 3.4, "mm", "four Ø3.4 +- 0.1 through at (+-110, 90), (+-110, -295), offset <= 0.10", 0.1, "all four Ø3.400 through, offset 0.000; each concentric with its R10 corner (web 8.3)", PA, "locate_bore", ("A-12",)),
 g("REQ-06", 8.0, "mm", "two Ø8.0 +- 0.1 through at (-80, -120), (-80, -230), offset <= 0.10", 0.1, "both Ø8.000 through, offset 0.000", PA, "locate_bore", ("A-13",)),
 g("REQ-07", 0.0, "mm", "top face y = 0.00 +- 0.10, 6.0 +- 0.1 thick, one plane", 0.1, "max_y 0.000, size_y 6.000; exactly one +Y planar face, y extent 0.000..0.000, area 96725.984 mm2; sections one piece at every level", P, "envelope, face listing, reviewer sections"),
 g("REQ-08", -89.21, "mm", "OD-H11 max z <= -85.0 and clearance(plate, OD-H11) >= 10.0", 4.21, "OD-H11 max z -89.210 (outlet pins); clearance 16.4925 at (-9.66, 0, -140), margin +6.4925", PA, "envelope, clearance", ("A-02",)),
 g("REQ-10", 4.0, "mm", "four Ø4.0 +- 0.05 at (-113, -42), (-71, -42), (-113, -148.5), (-71, -148.5), offset <= 0.10; against the pattern until the OD-C07 STEP", 0.05, "all four Ø4.000 through, offset 0.000; checked against the spec pattern only (no OD-C07 STEP)", PA, "locate_bore", ("A-17",)),
 g("REQ-09", None, "bool", "Soft bench gate: flat in service; INCONCLUSIVE with a risk rating", None, "not geometric; answered by the first print (F1)", INC, "none (bench)", ("A-10", "A-14")),
]
census = [
 {"feature": "F01 plate", "expected": "1 solid, 240 x 6 x 405, 6 planar faces, 4 convex R10 corner cylinders", "found": "1 solid, 240.000 x 6.000 x 405.000, 6 planar, 4 convex cylinders, corner rays from the feet axes read r 10.0", "status": "PASS"},
 {"feature": "F02 carrier insert holes x4", "expected": "Ø4.0 through at (+-35, -40), (+-35, -60)", "found": "4 x Ø4.000 through, offset 0.000", "status": "PASS"},
 {"feature": "F03 OD-C04 insert holes x4", "expected": "Ø4.0 through at (+-40, -148), (+-40, -114)", "found": "4 x Ø4.000 through, offset 0.000", "status": "PASS"},
 {"feature": "F04 OD-C03 insert holes x4", "expected": "Ø4.0 through at (-4 / 37, -239 / -171)", "found": "4 x Ø4.000 through, offset 0.000", "status": "PASS"},
 {"feature": "F05 bulkhead insert holes x4", "expected": "Ø4.0 through at (65, -45 / -105 / -165 / -225)", "found": "4 x Ø4.000 through, offset 0.000", "status": "PASS"},
 {"feature": "F05b OD-C07 insert holes x4 (WP-04)", "expected": "Ø4.0 through at (-113 / -71, -42 / -148.5)", "found": "4 x Ø4.000 through, offset 0.000", "status": "PASS"},
 {"feature": "F06 feet holes x4", "expected": "Ø3.4 through at (+-110, 90 / -295)", "found": "4 x Ø3.400 through, offset 0.000", "status": "PASS"},
 {"feature": "F07 drain holes x2", "expected": "Ø8.0 through at (-80, -120 / -230)", "found": "2 x Ø8.000 through, offset 0.000", "status": "PASS"},
 {"feature": "F08 clean-up / census totals", "expected": "6 planar, 30 cylindrical (26 concave, 4 convex), 0 other, 26 bores", "found": "6 planar, 30 cylindrical (26 concave, 4 convex), 0 other, 26 bores", "status": "PASS"},
]
plaus = [
 {"question": "P1 gravity", "answer": "Plate lies flat, bottom on the counter via four feet at (+-110, 90 / -295) enclosing the plate COM (0.09, -102.4) and every placed part; each mount stands on y 0 with 0 mm3 overlap.", "status": "YES"},
 {"question": "P2 function chains", "answer": "Mount foot Ø3.4 over plate Ø4.0 insert holes coaxial (offset 0.000) on all 8 placed mount holes; OD-C05, bulkhead, OD-C07 patterns at spec points; drains at x -80 in the wet zone, (-80, -120) under the OD-C07 hose window.", "status": "YES"},
 {"question": "P3 moving parts", "answer": "No moving part; assembly path checked: OD-C03, OD-C04 and the carrier box lowered along -Y read clearance = lift at 10, 1, 0.1, 0.01, 0 mm; column under the mouth (x +-50, z -18..82) empty from y 0 to 176.76.", "status": "YES"},
 {"question": "P4 grip, reach, insertion", "answer": "Inserts go in from the top before the mounts; feet screws from below; group head mouth faces down at y 176.76 over the tray zone; nearest insert to an edge is 5.0 from x -120, reachable with an iron.", "status": "YES"},
 {"question": "P5 absurdity", "answer": "Group head front over tray, thermoblock behind (z -140..-89), pump across the back (axis along X, z -232..-178), valve mount left, electric zone right of x 65: the Dedica layout; 240 x 405 x 6 PETG base 737 g is in proportion, larger than a Dedica footprint to carry tank and bay.", "status": "YES"},
 {"question": "P6 floating, embedded, mirrored, upside-down", "answer": "No overlap anywhere (all sound pairs 0 mm3); housing upright (rear face y 205 above mouth y 176.76, proper rotation); OEM parts sit in their mounts; the housing floats only because OD-C05 is not built (A-01, reference box).", "status": "YES"},
]
ctl = [
 ("validity", "plate plus a loose 5 mm cube: solid_count 2"),
 ("envelope", "front edge moved +0.5 in z: size_z 405.5"),
 ("feature_census", "insert hole (65, -225) filled: 25 bores"),
 ("bore_census", "same mutant: 19 Ø4.0 bores"),
 ("locate_bore offset", "REQ-10 hole (-71, -42) moved +0.5 in x: offset 0.5"),
 ("locate_bore diameter", "feet hole (-110, 90) resized Ø3.2: 3.2 < 3.25"),
 ("clearance", "OD-H11 placed 7.0 lower: 9.49 < 10.0"),
 ("clearance contact", "OD-C04 lifted 0.5: 0.5 != 0"),
 ("interference", "OD-C03 lowered 0.5 into the plate: 2054.87 mm3"),
 ("overhang_census", "Ø10 x 3 pocket from the bed face at (0, -270): 0.0 deg"),
 ("top face count (REQ-07)", "0.5 deep 20 x 20 pocket in the top face: 2 planes"),
 ("radial_extent", "OD-C07 hole moved to x -116.5: 7.0 across < 8.0"),
 ("min_wall / min_wall_wide", "OD-C07 hole moved to x -117.5: 0.5 (D-01a, J-05, U-06 all FAIL)"),
 ("compare_step (U-04)", "hole-removed mutant file: faces delta 1, volume delta 75.40 mm3; renamed body: labels 0"),
 ("mesh_sagitta / mesh_deviation", "STL at 0.1 mm / 0.5 rad: 0.0482 > 0.01"),
 ("mesh_census", "delivered STL with one triangle deleted: 3 naked edges"),
 ("3MF same-mesh compare", "3MF with one vertex moved 0.5: 7030 of 7068 triangles match"),
]
controls = [{"check": c, "mutant": m, "got": "FAIL"} for c, m in ctl]
findings = [
 {"id": "F1", "gate": "REQ-09", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "bool", "required": "flat in service (Soft bench gate)", "margin": None, "at": "whole plate, corners (+-120, -6, 100 / -305)", "blocks": False, "risk": "MEDIUM",
  "risk_basis": "an unribbed 240 x 405 x 6 PETG plate printed flat can lift at the corners and creep under a 1 kg tank; the three mounts seat on its top face, so warp shows as rocking; only a print can tell",
  "fix_direction": "first print with brim, measure flatness under the mounts and at the feet; if it rocks, C2 ribs or a two-piece C3"},
 {"id": "F2", "gate": "U-04", "kind": "OBSERVATION", "measured": 0.0524, "unit": "mm3", "required": "volume delta <= 0.001 (band) on re-read", "margin": -0.0514, "at": "check assembly body od_h11_thermoblock (input OD-H11 as placed vs its copy in the assembly STEP)", "blocks": False, "risk": "LOW",
  "risk_basis": "ruled INCONCLUSIVE, not FAIL: OD-H11 is brep_valid 0 (BOPAlgo_InvalidCurveOnSurface) on input, so its volume integral is not a sound measurement; its 406 faces and 734 vertices are identical to 1e-5 mm and a second write moves it 2.9e-9 mm3; U-04 gates the target's named body, which round-trips exactly; every OD-H11 row here rests on distances, not on its volume",
  "fix_direction": "repair or re-export OD-H11 in its own job (OD-C04 A-14); no change to this plate"},
]
least = [
 {"item": "The 5.0 web between the OD-C07 outer inserts and the left edge", "answer": "Measured 5.000 (min_wall at (-115, -5.7, -42), mesh 5.0025) and ring material r 2.0..7.0 at 180 deg: J-05 +2.0, D-05a 14.0 across (+6.0); after a Ø4.6 insert about 4.7 remains, above J-05's 3.0; edge bulge on pressing is a low, print-checkable risk resting on A-11 and A-17 (the OD-C07 pattern may still move)."},
 {"item": "U-04 on the check assembly for OD-H11 (0.0524 mm3)", "answer": "Confirmed 0.0524 mm3 (159766.4574 input vs 159766.4050 in the assembly) with faces and vertices identical; ruled INCONCLUSIVE on an unsound body, not a FAIL; U-04 on the target plate PASS (reviewer rewrite delta 0.0 mm3); filed as F2, non-blocking."},
 {"item": "REQ-09 flatness (Soft)", "answer": "Not measurable in CAD; INCONCLUSIVE by its row, risk MEDIUM (F1); the first print answers it."},
]
assum = ["A-01", "A-02", "A-03", "A-04", "A-09", "A-11", "A-12", "A-13", "A-14", "A-17"]
doc = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20260930-od-c01-base-frame", "target": "od_c01_frame_v02",
       "spec_version": "1.2", "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"},
       "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
       "summary": "One valid 240 x 6 x 405 plate, 26 through-holes all at their spec axes (offset 0.000), min wall 5.0 at the OD-C07 edge web, assembly contacts 0 with no interference; every Hard row passes, 14 of them on open assumptions; REQ-09 flatness INCONCLUSIVE (Soft, MEDIUM).",
       "files": files, "gates": gates, "feature_census": census, "plausibility": plaus, "positive_controls": controls,
       "findings": findings, "least_sure_answers": least, "assumptions_relied_on": assum}
(J / "reviews/RV01_od_c01_frame_v02.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
import jsonschema
jsonschema.validate(doc, json.loads(Path("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json").read_text()))
print("valid", len(gates), sum(1 for x in gates if x["status"] == "PASS_ASSUMED"))
