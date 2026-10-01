import json
from pathlib import Path
W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet")
def g(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin,
            "at": at, "status": status, "method": method, "assumes": list(assumes)}
gates = [
 g("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0.0, "foot file: 1 solid, brep_valid 1, naked_edges 0; OD-C01 input and each of the 13 assembly parts 1 solid", "PASS", "tools.core.validity"),
 g("U-02", 18.0, "mm", "18.0 x 18.0 x 10.0 each in [spec - 0.1, spec + 0.1]; position min x -9, min y -9, min z 0", 0.1, "size 18.000 x 18.000 x 10.000; position min (-9.000, -9.000, 0.000), max (9.000, 9.000, 10.000)", "PASS", "envelope"),
 g("U-03", 0.0, "mm3", "(a) designed contacts clearance = 0, other pairs interference <= 0 mm3 at the 4 poses; (b) nut slid mouth -> seat >= 5 poses, interference <= 0 mm3", 0.0, "own placement per spec 2 joint at (+-110, -6, +90) and (+-110, -6, -295): foot|plate, nut|foot seat, head|plate top clearance 0.000 at (111.7, -6.0, 90.0), (111.588, -8.5, 92.75), (112.85, 0.0, 90.0) (pose 1, same at poses 2-4); 24 pairs 0.000 mm3; (b) 33 poses nut top z 10.5 -> 2.5 x nut s {5.32, 5.50} x pocket af {5.60, 5.65}: max 0.000 mm3; designer assembly parts coincide with own placement (symmetric difference 0.000 mm3)", "PASS_ASSUMED", "clearance, interference (common_volume), own slide script", ("A-01", "A-02")),
 g("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "file: AP242, label od_c15_foot, 1 solid, 1 shell; step_roundtrip of a detached copy and compare_step against the delivered file: volume_delta 0.000, faces_delta 0, labels 1, valid_after 1", "PASS", "step_roundtrip, compare_step"),
 g("U-05", 19, "count", "per plan: 15 planar (top, counter, seat, 6 flats, 6 mouth-chamfer planes), 2 cylinders (1 convex Ø18.0, 1 concave Ø3.4), 2 cones (bed and counter chamfers), 1 bore, 0 other", 0.0, "planes 15, cylinders 2 (convex 1, concave 1), cones 2, sphere/torus/bspline/other 0, bores 1 (Ø3.400, axis Z, z 0 -> 2.5, through)", "PASS", "feature_census, bore_census, locate_bore"),
 g("U-06", 2.5, "mm", ">= 2.0 (min_wall wide)", 0.5, "(-3.054, 0.0, 2.5) lid, seat to top face", "PASS", "min_wall detail['wide']"),
 g("U-07", 0.006586, "mm", "STL at tol 0.01, angular <= 4 acos(1 - 0.01/9.0) = 0.18858 rad; stl_max_sagitta <= 0.01", 0.003414, "delivered STL to B-rep deviation 0.006586 at (-5.023, 6.846, 9.5); own re-mesh at 0.01 mm / 0.18 rad: same 1194 triangles, same vertex set (max vertex distance 0.000), sagitta 0.006606; mesh_census 1 body, 0 naked edges, winding 1, volume 2282.616 mm3 (B-rep 2284.451); min_wall_mesh 2.500", "PASS", "write_stl, stl_max_sagitta, mesh_census, mesh_deviation"),
 g("U-08", None, "bool", "applies to threaded parts; this target has none", None, "no helical or freeform faces; one plain Ø3.4 bore", "NOT_APPLICABLE", "N/A by its row"),
 g("D-01a", 2.5, "mm", "min_wall >= 0.8", 1.7, "(-3.054, 0.0, 2.5) lid", "PASS", "min_wall"),
 g("D-01b", 2.5, "mm", "min_wall >= 2.0", 0.5, "(-3.054, 0.0, 2.5) lid", "PASS_ASSUMED", "min_wall", ("A-03",)),
 g("D-02", 18.0, "mm", "each envelope size <= build volume 220 x 220 x 250, top face down", 202.0, "18.000 x 18.000 x 10.000 in the print frame (z 0 on the bed); least margin x/y 202.0, z 240.0", "PASS_ASSUMED", "envelope", ("A-08",)),
 g("D-03a", 59.886267, "deg", "every downward face >= 45 deg from horizontal", 14.886267, "(8.758, 0.0, 0.083) bed-edge chamfer cone; only downward face; sampling bound 0.0052 deg; 0 samples below 45", "PASS", "overhang_census"),
 g("D-03b", 0.0, "mm", "bridge span <= 5; none in print orientation", 5.0, "no flat ceiling off the bed (seat, counter face and mouth chamfer face up); own sections confirm", "PASS", "flat_ceiling_spans, own sections"),
 g("D-04a", 3.4, "mm", "lid hole Ø >= 3.25", 0.15, "(0, 0, 0) -> (0, 0, 2.5) lid bore", "PASS", "bore_census, locate_bore"),
 g("D-04c", 1.3, "mm", ">= 0.5 per side, foot to screw shank below the nut seat", 0.8, "(2.425, 1.4, 2.5) flat edge at the seat to shank Ø3.0 segment z 2.5 -> 6.0", "PASS_ASSUMED", "clearance", ("A-02",)),
 g("D-06a", 2.5, "mm", "min_wall >= 1.0", 1.5, "(-3.054, 0.0, 2.5) lid", "PASS", "min_wall"),
 g("D-07", None, "bool", "applies to reamed fit bores; this part has none", None, "the only bore is the Ø3.4 clearance hole; the pocket is REQ-03", "NOT_APPLICABLE", "N/A by its row"),
 g("J-05", 4.189488, "mm", "wall around the nut pocket on the ring z 2.5 -> 10 >= 3.0", 1.189488, "(3.811, 0.0, 10.0) mouth-chamfer corner to (8.0, 0.0, 10.0) counter-chamfer edge (face-to-face least distance); min_wall on the ring 5.911 at (-8.965, 0.790, 2.681); radial corner material 5.767 below z 9.0, 4.192 at z 9.999", "PASS", "min_wall on foot cut at z 2.5; BRepExtrema pocket faces to outer faces; radial_extent"),
 g("J-06", 1, "count", "no threaded bore (none below M5)", 0.0, "one plain Ø3.4 bore, 0 helical/freeform faces", "PASS", "bore_census, feature_census"),
 g("REQ-01", 17.42, "mm", "face at z 0.0 +- 0.1 is one plane, annulus lid hole -> Ø17.42, normal -Z", 0.0, "one plane at z 0.000, area 229.255 mm2 = pi/4 (17.42^2 - 3.4^2); outer edge r 8.710 at 12 angles (z 1e-5); envelope min_z 0.000", "PASS", "envelope, feature_census, radial_extent"),
 g("REQ-02", 3.4, "mm", "Ø3.4 +- 0.1 through z 0 -> 2.5, coaxial offset <= 0.10", 0.1, "(0, 0, 0) -> (0, 0, 2.5), through; offset to outer axis 0.000; offset to each plate hole axis at the 4 own poses 0.000", "PASS_ASSUMED", "locate_bore, radial_profile", ("A-01",)),
 g("REQ-03", 5.6, "mm", "af 5.60 +0.05/-0 (0.05 -> 0.165 per side), flats parallel to X +- 1 deg, centred <= 0.10, seat z 2.50 +- 0.1 to z 10.0 open, entry chamfer 0.5", 0.0, "af 5.600 on 3 pairs at z 2.6, 4, 6, 8, 9.4; flat normals 30/90/150 deg, rotation 0.000 deg; centre 0.000; seat z 2.500; open at z 10 (mouth r 3.299 at z 9.999), chamfer 0.5 x 0.5 (z 9.5 -> 10); nut envelope to flats 0.050 per side (s 5.50), 0.140 (s 5.32); af 5.65 variant 0.075 / 0.165", "PASS_ASSUMED", "radial_extent, clearance, feature_census, sections", ("A-06",)),
 g("REQ-04", 18.0, "mm", "outer Ø18.0 +- 0.1, height 10.0 +- 0.1, chamfers 0.50 x 0.29 (z 0) and 1.0 x 1.0 (z 10) each +- 0.1", 0.1, "Ø18.000 (36 angles, z 0.6 -> 8.9); height 10.000; bed chamfer z 0 -> 0.5, r 8.710 -> 9.0 (59.886 deg); counter chamfer z 9.0 -> 10.0, r 9.0 -> 8.0", "PASS_ASSUMED", "radial_profile, radial_extent, envelope", ("A-05",)),
 g("REQ-05", 1.0, "mm", "foot footprint to plate edge >= 0.9 at each pose", 0.1, "pose 1-4: 1.000 to the X edge, 1.000 to the Z edge, 1.000 to the R10 corner arc (plate R 10.000 over the outward sector minus foot R 9.000, axis offset 0.000)", "PASS_ASSUMED", "envelope, radial_profile, locate_bore", ("A-01",)),
 g("REQ-06", -16.0, "mm", "four counter faces at y -16.00 +- 0.10; feet enclose plate centre of mass", 0.1, "counter faces y -16.000 at poses 1-4; plate COM (0.089, -3.000, -102.371) inside the axes rectangle, least margin 109.911 (x+)", "PASS_ASSUMED", "envelope, mass_properties", ("A-01", "A-04")),
 g("REQ-07", 6.0, "mm", "screw tip at foot z 6.0 +- 0.1; >= 0.5 past nut lower face z 4.9; >= 2.0 above counter face", 0.1, "screw envelope max z 6.000 in the foot frame (plate measured 6.000 thick): 1.100 past z 4.9, 4.000 above z 10.0", "PASS_ASSUMED", "envelope", ("A-02",)),
]
census = [
 {"feature": "F01 body cylinder Ø18.0 x 10.0", "expected": "1 convex cylinder r 9.0, z 0 -> 10", "found": "1 convex cylinder r 9.000, z 0.5 -> 9.0 between chamfers; envelope 18.000 x 18.000 x 10.000", "status": "PASS"},
 {"feature": "F02 bed-edge chamfer (spec 1.1: 0.50 axial x 0.29 radial, 60 deg)", "expected": "1 cone, z 0 -> 0.5, r 8.71 -> 9.0", "found": "1 cone z 0.000 -> 0.500, r 8.710 -> 9.000, 59.886 deg from horizontal", "status": "PASS"},
 {"feature": "F03 counter-edge chamfer 1.0 x 45", "expected": "1 cone, z 9 -> 10, r 9.0 -> 8.0", "found": "1 cone z 9.000 -> 10.000, r 9.000 -> 8.000, 45 deg", "status": "PASS"},
 {"feature": "F04 lid hole Ø3.4, z 0 -> 2.5", "expected": "1 concave cylinder, 1 bore Ø3.4 axis Z, through", "found": "1 bore Ø3.400, axis (0,0,1), (0,0,0) -> (0,0,2.5), through, offset 0.000", "status": "PASS"},
 {"feature": "F05 hex nut pocket af 5.60, flats parallel to X, z 2.5 -> 10", "expected": "6 planar flats at 2.80 from the axis", "found": "6 vertical planes at 2.800, normals 30/90/150 deg (flat pair parallel to X), z 2.5 -> 9.5", "status": "PASS"},
 {"feature": "F06 nut seat plane z 2.5", "expected": "1 plane at z 2.5 between Ø3.4 and the hex", "found": "1 plane at z 2.500, area 18.079 mm2 (hex af 5.6 minus Ø3.4)", "status": "PASS"},
 {"feature": "F07 pocket mouth chamfer 0.5 x 45", "expected": "6 planes at 45 deg, z 9.5 -> 10", "found": "6 planes, normal z 0.7071, z 9.500 -> 10.000; mouth af 6.6 (r 3.299 at z 9.999)", "status": "PASS"},
 {"feature": "End faces (top annulus, counter annulus)", "expected": "2 planes: z 0 (Ø3.4 -> Ø17.42) and z 10", "found": "plane z 0.000 area 229.255 mm2; plane z 10.000 area 163.338 mm2 (Ø16 minus mouth hex af 6.6)", "status": "PASS"},
 {"feature": "F08 name and export", "expected": "label od_c15_foot, AP242, STL", "found": "label od_c15_foot, AP242, unit MM; STL 1194 triangles", "status": "PASS"},
]
plaus = [
 {"question": "P1 gravity", "answer": "Own pose-1 section: the foot hangs under the plate, top face on the underside y -6.0, counter face down at y -16.0; load goes plate -> foot body -> counter", "status": "YES"},
 {"question": "P2 function chains", "answer": "Screw head on plate top -> plate Ø3.4 -> lid Ø3.4 -> nut on the seat, all coaxial (offset 0.000); tip at z 6.0 ends inside the pocket", "status": "YES"},
 {"question": "P3 moving parts", "answer": "Only the nut moves at assembly: it slides mouth -> seat with 0.000 mm3 at 33 poses over nut s 5.32/5.50 and pocket af 5.60/5.65; flats stop it turning", "status": "YES"},
 {"question": "P4 grip, reach, insertion", "answer": "Nut drops in from the open counter side through the 0.5 chamfer, screw driven from the plate top; head Ø5.7 inside the A-09 Ø8 keep-out", "status": "YES"},
 {"question": "P5 against a real product", "answer": "Ø18 x 10 mm, 2.76 g screw-on rubber-like foot under a 240 x 405 mm base is ordinary for small appliances", "status": "YES"},
 {"question": "P6 floating, embedded, mirrored, upside-down", "answer": "Interference 0 and contacts 0 at all poses; pocket opens away from the plate; small bed chamfer on the plate side; flats parallel to X as specified", "status": "YES"},
]
controls = [
 {"check": "validity (U-01)", "mutant": "one face of the foot removed: open shell (naked_edges 7)", "got": "FAIL"},
 {"check": "envelope (U-02, D-02, REQ-04 height, REQ-06, REQ-07)", "mutant": "foot scaled x1.02: 18.36 x 18.36 x 10.2", "got": "FAIL"},
 {"check": "radial_profile (REQ-04 diameter)", "mutant": "foot scaled x1.02: outer R 9.18", "got": "FAIL"},
 {"check": "radial_profile on the plate arc (REQ-05)", "mutant": "foot scaled x1.02 at pose 1: arc margin 0.82", "got": "FAIL"},
 {"check": "radial_extent across flats (REQ-03)", "mutant": "foot scaled x1.02: af 5.712", "got": "FAIL"},
 {"check": "radial_extent flat rotation (REQ-03)", "mutant": "foot rotated 2 deg about its axis: 2.0 deg", "got": "FAIL"},
 {"check": "feature_census (U-05, REQ-01)", "mutant": "lid hole filled: bores 0", "got": "FAIL"},
 {"check": "bore_census (J-06, U-05)", "mutant": "lid hole filled: 0 bores", "got": "FAIL"},
 {"check": "locate_bore offset (REQ-02)", "mutant": "lid hole moved 0.5 mm in x: offset 0.5", "got": "FAIL"},
 {"check": "locate_bore diameter (D-04a, REQ-02)", "mutant": "lid hole resized to Ø3.2", "got": "FAIL"},
 {"check": "min_wall (D-01a, D-01b, D-06a)", "mutant": "annular groove 1.8 deep in the top face: lid 0.7", "got": "FAIL"},
 {"check": "min_wall wide (U-06)", "mutant": "same groove mutant: 0.7", "got": "FAIL"},
 {"check": "min_wall on the ring (J-05)", "mutant": "pocket opened to af 12.6: ring wall 2.010", "got": "FAIL"},
 {"check": "overhang_census (D-03a)", "mutant": "tunnel 6 wide x 1 high across the bed face: 0 deg", "got": "FAIL"},
 {"check": "flat_ceiling_spans (D-03b)", "mutant": "same tunnel: span 12.08", "got": "FAIL"},
 {"check": "clearance designed contact (U-03 a)", "mutant": "foot 1 relocated 0.5 mm off the plate underside: 0.5", "got": "FAIL"},
 {"check": "clearance (D-04c)", "mutant": "rib 0.9 deep on a pocket flat: 0.40", "got": "FAIL"},
 {"check": "interference (U-03 a)", "mutant": "foot 1 relocated 0.5 mm into the plate: 118.6 mm3", "got": "FAIL"},
 {"check": "interference slide (U-03 b)", "mutant": "nut envelope s 5.7 at z 6.0 in the delivered pocket: 2.35 mm3", "got": "FAIL"},
 {"check": "mass_properties (REQ-06 centre of mass)", "mutant": "plate relocated +300 in Z: COM outside by 107.6", "got": "FAIL"},
 {"check": "compare_step (U-04)", "mutant": "delivered file against the hole-filled mutant: volume_delta 22.70 mm3", "got": "FAIL"},
 {"check": "stl_max_sagitta (U-07)", "mutant": "re-mesh at 0.1 mm / 0.5 rad: 0.0493", "got": "FAIL"},
 {"check": "mesh_census (U-07)", "mutant": "delivered STL with its last triangle removed: 3 naked edges", "got": "FAIL"},
 {"check": "mesh_deviation (U-07)", "mutant": "delivered STL shifted 0.05 mm in x: 0.0546", "got": "FAIL"},
]
least = [
 {"item": "1. REQ-03 at the tolerance corner af 5.65 x s 5.32: 0.165 against 0.16", "answer": "Own af 5.65 variant cut from the exported part with an s 5.32 nut envelope reads 0.165 per side, equal to spec 1.2's corrected upper limit (5.65 - 5.32)/2 = 0.165, margin 0.000: PASS; the REPORT's FAIL was against spec 1.1's 0.16 and is closed by spec 1.2 with no geometry change. No finding."},
 {"item": "2. A-06: TPU 95A grip on the nut at 0.05 -> 0.165 per side", "answer": "Geometry confirmed: 0.050 (s 5.50) to 0.165 (s 5.32, af 5.65) per side, flats parallel to X, centred 0.000. Whether TPU holds the nut against turning is not measurable in CAD; REQ-03 is PASS_ASSUMED on open A-06, retired only by the first printed foot."},
 {"item": "3. J-05 at the mouth: 4.243 sampled to z 9.975, 4.19 at z 10 extrapolated", "answer": "Measured at z 10 directly: least face-to-face distance mouth-chamfer corner (3.811, 0, 10) to counter-chamfer edge (8.0, 0, 10) is 4.189; radial 4.192 at z 9.999. Margin +1.189 over 3.0: PASS, no extrapolation needed."},
]
files = [
 {"path": "02_STEP_STL/od_c15_foot_C1_v01.step", "sha256": "830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7", "matches_report": True},
 {"path": "02_STEP_STL/od_c15_foot_C1_v01.stl", "sha256": "cc66c8c8961c9becda42111b1d3c0246c81940d4fc9fb98fe94036c4d8e4f20c", "matches_report": True},
 {"path": "02_STEP_STL/od_c15_assembly_C1_v01.step", "sha256": "e3228ea2f667eeb98ef1add9c37c38c8bbab9adb7d7a85bed61105f58d261d8f", "matches_report": True},
 {"path": "01_CAD/REPORT_od_c15_foot_v01.md", "sha256": "df020639538f2faa6f406485432f0d52f25ebf3cf57fbc8ae6f9dfbbb089a242", "matches_report": True},
 {"path": "00_Spec/DESIGN_SPEC.md", "sha256": "a24c23f25b2f02b916d89beb76e3db5c899d02d518c3775c402b5ed27e0e496f", "matches_report": True},
 {"path": "00_Spec/inputs/OD-C01_base_frame.step", "sha256": "7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805", "matches_report": True},
 {"path": "03_Sections/od_c15_foot_v01_front.png", "sha256": "fbf888202a8f4c282c5c9e2d5f80a8b80776b99947d418038ea57ebd4dc6e184", "matches_report": True},
 {"path": "03_Sections/od_c15_foot_v01_left.png", "sha256": "385a31c5822e531a26ff159b6d8de22cb78cd5a77eea941809e1fb164f0163de", "matches_report": True},
 {"path": "03_Sections/od_c15_foot_v01_top.png", "sha256": "4e47ba6451f0f09d7920e855b1268f933b6d912bdc5b79b7b5fd2935d4d22d0e", "matches_report": True},
 {"path": "03_Sections/od_c15_assembly_pose1_v01_left.png", "sha256": "6e5e5dcd5fe15409742a47cd5a478779b40d9328ec0eb5eff339473ae1eb9701", "matches_report": True},
 {"path": "03_Sections/od_c15_assembly_pose1_v01_top.png", "sha256": "920a82e982264c5a66700c47e799dbd0f076500d631f28c908748ceb9f1f36b4", "matches_report": True},
]
v = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20261001-od-c15-feet", "target": "od_c15_foot_v01",
     "spec_version": "1.2", "reviewer": {"runtime": "claude-code", "model": "reviewer role, strong class (model name withheld per repository rule)"},
     "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
     "summary": "All 26 spec 1.2 gate rows re-measured from the exported STEP/STL and an own OD-C01 placement: 24 PASS or PASS_ASSUMED, 2 N/A by their rows, 0 FAIL, 0 INCONCLUSIVE; 9 plan features present; P1-P6 YES; 24 positive controls FAIL; no findings; conditional on open A-01, A-02, A-03, A-04, A-05, A-06, A-08.",
     "files": files, "gates": gates, "feature_census": census, "plausibility": plaus, "positive_controls": controls,
     "findings": [], "least_sure_answers": least,
     "assumptions_relied_on": ["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-08"]}
p = W / "reviews/RV01_od_c15_foot_v01.json"
p.write_text(json.dumps(v, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
import jsonschema
jsonschema.validate(v, json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json")))
print("valid", len(gates), "gates", len(controls), "controls")
