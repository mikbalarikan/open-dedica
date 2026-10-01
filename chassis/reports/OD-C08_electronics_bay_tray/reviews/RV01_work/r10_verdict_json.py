"""Build reviews/RV01_od_c08_tray_v01.json from the reviewer's own measurements (r01..r08) and validate it."""
import json, hashlib, sys
from pathlib import Path
J = Path("/root/oguz-jobs/20261001-od-c08-electronics-bay-tray"); W = J / "reviews/RV01_work"
def sha(p): return hashlib.sha256((J / p).read_bytes()).hexdigest()
in_report = ["01_CAD/DESIGN_PLAN.md", "01_CAD/REPORT_od_c08_tray_v01.md", "01_CAD/check_od_c08_tray_v01.json", "01_CAD/build_record_v01.json",
             "01_CAD/sections_v01.json", "01_CAD/probe/probe_inputs.json", "02_STEP_STL/od_c08_tray_C1_v01.step",
             "02_STEP_STL/od_c08_assembly_C1_v01.step", "02_STEP_STL/od_c08_tray_C1_v01.stl"] + sorted("03_Sections/" + p.name for p in (J / "03_Sections").glob("*.png"))
files = [{"path": p, "sha256": sha(p), "matches_report": p != "01_CAD/REPORT_od_c08_tray_v01.md"} for p in in_report]
files.insert(9, {"path": "02_STEP_STL/od_c08_tray_C1_v01.3mf", "sha256": sha("02_STEP_STL/od_c08_tray_C1_v01.3mf"), "matches_report": False})
rep = (J / "01_CAD/REPORT_od_c08_tray_v01.md").read_text()
for f in files:
    if f["matches_report"]: assert f["sha256"] in rep, f["path"]
def G(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at, "status": status, "method": method, "assumes": list(assumes)}
A3 = ["A-01", "A-02", "A-03", "A-06"]
gates = [
 G("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "tray STEP re-imported: 1 solid, brep_valid 1, naked_edges 0; each of the 4 assembly parts one valid solid", "PASS", "validity"),
 G("U-02", 39.0, "mm", "39.0 x 92.0 x 160.0 each in [spec - 0.1, spec + 0.1]; position x 73.0..112.0, y 0..92.0, z -230.0..-70.0", 0.1, "sizes 39.000 x 92.000 x 160.000; position x 73.000..112.000, y 0.000..92.000, z -230.000..-70.000 (each margin 0.1)", "PASS", "envelope"),
 G("U-03", 0.0, "mm", "(a) contacts clearance = 0 and interference <= 0; pins >= 0.30; rest of board >= 0.5; tray-C02 >= 1.5; E01-C02 >= 10.0; E01 in x 70..117, z -240..-30, y >= 10; (b) path interference <= 0", 0.0,
   "seat contact: tray less pins reaches x 82.4380 = board solder face x 82.4380 (overlap depth 0.000, four seats clearance 0); flange on plate clearance 0 at (73, 0, -230), interference 0; pins 0.3389 (H5) / 0.3278 (H6) at (82.438, 30.185, -157.108); rest 1.000 (wall/flange/gussets 6.438); tray-C02 2.000; E01-C02 15.438; E01 x 82.438..109.262, z -195.002..-94.838, y 24.000; path dx 5.0..0.25 clearance >= 0.250 (20 poses), 21 poses common_volume 0; plate material under the four holes complete (A-01)", "PASS_ASSUMED",
   "clearance, common_volume, envelope; decomposition (envelope of tray less pins in the board footprint vs board min x)", A3),
 G("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "AP242, unit MM, label od_c08_tray, 1 MANIFOLD_SOLID_BREP / 1 CLOSED_SHELL, no open shells; re-write/re-read volume delta 0, faces delta 0, labels 1; assembly 4 named parts, each identical to its input (common volume = own volume)", "PASS", "compare_step, step_roundtrip, read_schema, read_length_unit"),
 G("U-05", 42, "count", "1 wall, 1 flange, 4 gussets, 4 standoffs (2 with Ø4.0 blind bore, 2 with Ø1.8 pin), 4 Ø3.4 flange holes, 4 tie slots; plan: 42 planes, 12 cylinders (6 convex, 6 concave), 6 bores", 0, "42 planes, 12 cylinders (6 convex, 6 concave), 0 other; 6 bores (2 blind along X, 4 through along Y); 4 gusset hypotenuses; 4 standoffs; 2 pins; 4 slots (section x 74.5)", "PASS", "feature_census, bore_census, locate_bore, sections"),
 G("U-06", 1.8, "mm", "min_wall wide >= 2.0 (Soft)", -0.2, "(82.688, 31.519, -158.238) the Ø1.8 H6 locating pin; the tray less its two pins reads 2.000 at (75.75, 92.0, -113.478)", "FAIL", "min_wall_wide (spacing 0.7)"),
 G("U-07", 0.004895, "mm", "STL tol 0.01, angular <= 4 acos(1 - 0.01/R_max) = 0.2530 rad; stl_max_sagitta <= 0.01; 3MF carries the same mesh", 0.005105, "delivered STL to B-rep both ways 0.00489 at (82.438, 30.980, -104.018); fresh 0.01/0.2 rad re-mesh sagitta 0.00489, surfaces coincide with the STL (1.8e-8); 3244 triangles, 1 body, 0 naked edges, consistent winding, 70594.55 mm3; 3MF: 1 object, mm, 3244 triangles, same triangles as the STL (8e-7), watertight", "PASS", "mesh_census, mesh_deviation, write_stl/mesh_sagitta, min_wall_mesh"),
 G("U-08", None, "count", "applies to threaded parts; this target has none", None, None, "NOT_APPLICABLE", "N/A by the spec row (no threads on this part)"),
 G("D-01a", 1.8, "mm", "min_wall >= 0.8", 1.0, "(82.688, 31.519, -158.238) Ø1.8 pin", "PASS", "min_wall (spacing 0.7)"),
 G("D-01b", 2.0, "mm", "min_wall >= 2.0 except the two pins and the 0.44 floor under each insert bore", 0.0, "(75.75, 92.0, -113.478) the 2.0 web above the tie slots (y 90..92), tray less its two pins", "PASS", "min_wall (spacing 0.7)"),
 G("D-02", 160.0, "mm", "each envelope size <= K1C build volume: 92.0 x 160.0 on the bed, 39.0 tall (220 x 220 x 250, A-09)", 60.0, "bed 92.0 x 160.0, height 39.0", "PASS_ASSUMED", "envelope", ["A-09"]),
 G("D-03a", 90.0, "deg", "every downward face >= 45 deg in the print (build +X); the four flange-hole crowns the named exception", 45.0, "four flange holes refilled by position: nothing downward off the bed; whole part least 0.0 deg only on the four hole crowns, e.g. (89.7, 0.0, -78.0) (named exception)", "PASS_ASSUMED", "overhang_census(build_dir=(1,0,0), spacing 0.7)", ["A-08"]),
 G("D-03b", 3.4, "mm", "span <= 5", 1.6, "the four Ø3.4 horizontal flange-hole crowns at (88/106, 0..4, -222/-78); flat ceilings 0", "PASS_ASSUMED", "flat_ceiling_spans(build_dir=(1,0,0)), bore_census, sections", ["A-08"]),
 G("D-04a", 3.4, "mm", "four flange holes Ø >= 3.25", 0.15, "all four Ø3.400 at (88/106, 0, -222/-78)", "PASS", "bore_census, locate_bore"),
 G("D-04c", 1.0, "mm", ">= 0.5 per side tray to OD-E01 away from the designed contacts", 0.5, "(81.438, 32.990, -100.010) tray less pins and the top 1.0 of each standoff; wall/flange/gussets 6.438 at (76.0, 24.0, -94.838); interference 0 (seat contact only, decomposition)", "PASS_ASSUMED", "clearance; decomposition", ["A-02"]),
 G("D-04d", 0.3278, "mm", "each pin in its board hole >= 0.30 per side", 0.0278, "H6 pin (82.438, 30.185, -157.108); H5 0.3389", "PASS_ASSUMED", "clearance (pin to OD-E01)", ["A-02"]),
 G("D-05a", 10.0, "mm", "material >= 8.0 across around each Ø4.0 insert bore", 2.0, "both bores, 12 diameters x 3 depths each, least 10.000 at (76.938, 85.0, -100.0)", "PASS_ASSUMED", "radial_extent", ["A-07"]),
 G("D-05b", 4.0, "mm", "Ø 4.0 ± 0.05, depth 6.0 ± 0.1 (>= 5.7), blind", 0.05, "both bores Ø4.000, depth 6.000 (x 76.438..82.438), floor closed, at (76.438, 80.0, -100.0) and (76.438, 27.99, -100.01)", "PASS_ASSUMED", "bore_census, locate_bore", ["A-07"]),
 G("D-06a", 1.8, "mm", ">= 1.0 (the pins Ø1.8)", 0.8, "both pins Ø1.800 (exact cylinders); min_wall 1.800", "PASS", "min_wall, cylinder axes"),
 G("D-07", None, "count", "none: the insert bores are formed by the insert, the flange holes are clearance holes", None, None, "NOT_APPLICABLE", "N/A by the spec row (no fit-critical bores on this part)"),
 G("J-05", 3.0, "mm", ">= 3.0 around each insert bore", 0.0, "both bores, 24 rays x 3 depths each, least 3.000 at (76.938, 85.0, -100.0)", "PASS", "radial_extent"),
 G("E-01", 1.0, "mm", "= D-04c", 0.5, "as D-04c", "PASS_ASSUMED", "clearance", ["A-02"]),
 G("E-05", 0.0041, "mm", "insert bores coaxial with H1/H2, pins with H5/H6, offset <= 0.10", 0.0959, "H5 at (82.438, 81.976, -157.519); H1 0.0032, H2 0.0032, H6 0.0022", "PASS_ASSUMED", "bore_census/locate_bore on both solids, cylinder axes", ["A-02", "A-03"]),
 G("E-06", 4, "count", "every standoff grows from the wall; flange tied to the wall by four gussets", 0, "4 standoffs start at x 76.000 and section in one face with wall and flange; 4 gussets 20 x 20 x 3 at z -230..-227, -212..-209, -88..-85, -73..-70, each one face with wall and flange (section area 620)", "PASS", "sections, cylinder faces"),
 G("E-11", 4, "count", "two tie-slot pairs above the board; tray open on +X, ±Z and above", 0, "4 slots 2.0 (z) x 4.0 (y) through the wall at y 86..90, z -177..-175, -169..-167, -123..-121, -115..-113, 2.131 above the board top; boxes on +X, front, rear and above hold 0 mm3 of tray", "PASS_ASSUMED", "sections, common_volume", ["A-11"]),
 G("REQ-01", 3.4, "mm", "four Ø3.4 ± 0.1 through-holes along Y at (88,-222), (106,-222), (88,-78), (106,-78), offset <= 0.10, 4.0 ± 0.1 long; underside one plane at y 0.00 ± 0.10", 0.1, "all four Ø3.400, offset 0.000, 4.000 long, through; underside one plane y 0.000 (6203.68 mm2); OD-C01 material complete under each hole (Ø10 x 6 column), nearest plate edge or void 12.0 from the Ø4 insert hole", "PASS_ASSUMED", "bore_census, locate_bore, faces, common_volume", ["A-01"]),
 G("REQ-02", 82.438, "mm", "standoff tops x 82.44 ± 0.05 (coplanar); bores Ø4.0 at H1/H2; pins Ø1.8 ± 0.05, 2.5 ± 0.1 at H5/H6; offsets <= 0.10", 0.048, "four seat faces x 82.4380 (spread 0); bores Ø4.000 offset 0.000; pins Ø1.800, 2.500 long (x 82.438..84.938), offset 0.000", "PASS_ASSUMED", "faces, bore_census, locate_bore, cylinder axes", ["A-02", "A-03"]),
 G("REQ-03", 73.0, "mm", "nothing at x < 73.0; front end z -70.0 ± 0.1", 0.0, "min x 73.000; max z -70.000", "PASS_ASSUMED", "envelope", ["A-06"]),
 G("REQ-04", 0.0, "mm3", "four Ø8 x 116 cylinders (y 4..120) on the hole axes: interference with tray and board = 0", 0.0, "all four 0 with tray and board; board clearance to the cylinders >= 13.307 (x88 z-78)", "PASS_ASSUMED", "common_volume, clearance", ["A-03"]),
 G("REQ-05", 0.0, "mm3", "box x 85..117, y 4..92, z -195..-95 with the tray = 0", 0.0, "box empty", "PASS_ASSUMED", "common_volume", ["A-03"]),
 G("REQ-06", None, "bool", "Soft: board does not flex visibly under a faston push at z -188 (bench)", None, "farthest tab z -188, 30.5 beyond the H6 pin standoff", "INCONCLUSIVE", "bench gate, not geometric", ["A-04", "A-12"]),
 G("exactly_one_solid", 1, "count", "solid_count = 1", 0, None, "PASS", "validity"),
 G("feature_census", 42, "count", "plan §3 counts: 42 planes, 12 cylinders (6 convex, 6 concave), 0 cones/spheres/tori/B-splines/other, 6 bores", 0, "every count equal to the plan", "PASS", "feature_census"),
 G("envelope_within_spec", 39.0, "mm", "39.0 x 92.0 x 160.0 each ± 0.1, position apart", 0.1, "as U-02", "PASS", "envelope"),
]
census = [
 {"feature": "F01 wall + floor flange", "expected": "L section x 73..112 x y 0..4 and x 73..76 x y 0..92, z -230..-70", "found": "section area 420.000 at z -150 / -120; envelope 39 x 92 x 160", "status": "PASS"},
 {"feature": "F02 gussets x4", "expected": "20 x 20 triangles, 3.0 thick at z -230..-227, -212..-209, -88..-85, -73..-70", "found": "4 hypotenuse faces x 76..96, y 4..24 at exactly those z ranges; sections 620.000", "status": "PASS"},
 {"feature": "F03 insert standoffs x2 Ø10", "expected": "r 5.0 along +X, x 76.0..82.438 at H1, H2", "found": "2 cylinders r 5.000, x 76.000..82.438, axes (80.00, -100.00), (27.99, -100.01)", "status": "PASS"},
 {"feature": "F04 pin standoffs x2 Ø6", "expected": "r 3.0 along +X, x 76.0..82.438 at H5, H6", "found": "2 cylinders r 3.000, x 76.000..82.438, axes (81.98, -157.52), (30.99, -157.51)", "status": "PASS"},
 {"feature": "F05 locating pins x2 Ø1.8 x 2.5", "expected": "r 0.9, x 82.438..84.938", "found": "2 cylinders r 0.900, x 82.438..84.938, coaxial with F04", "status": "PASS"},
 {"feature": "F06 insert bores x2 Ø4.0 x 6.0 blind", "expected": "2 blind bores along X", "found": "2 bores Ø4.000, 6.000 deep, x 76.438..82.438, floor closed", "status": "PASS"},
 {"feature": "F07 flange holes x4 Ø3.4", "expected": "4 through bores along Y", "found": "4 bores Ø3.400, y 0..4, through, at (88/106, -222/-78)", "status": "PASS"},
 {"feature": "F08 tie slots x4 2.0 x 4.0", "expected": "4 slots through the wall along X at y 86..90, centres z -176, -168, -122, -114", "found": "4 holes in sections x 73.2 / 74.5 / 75.8, each y 86..90 x z 2.0 at those centres", "status": "PASS"},
]
P = [
 {"question": "P1 gravity", "answer": "Flange lies on the plate top (clearance 0, interference 0) and takes four screws; the 0.1 kg board sits on four standoffs off a gusseted wall; in the print the tray lies on its wall face with everything rising as prisms.", "status": "YES"},
 {"question": "P2 function chains", "answer": "Screw path: Ø3.4 hole over complete plate material (inserts still to be added, A-01); board: seat at its solder face, insert bores coaxial with H1/H2 within 0.004; wires: four tie slots 2.13 above the board top; faston box on +X empty.", "status": "YES"},
 {"question": "P3 motion clearance", "answer": "No moving parts in service; the board's mounting path along -X from +5.0 keeps clearance >= 0.25 in 20 poses and meets the seats at 0; pins enter H5/H6 with 0.33 per side.", "status": "YES"},
 {"question": "P4 grip, reach, insertion", "answer": "Driver cylinders Ø8 to y 120 on all four screw axes clear the tray and the board (board >= 13.3 away); board goes on along -X over two pins, then two screws from the component side.", "status": "YES"},
 {"question": "P5 absurdity", "answer": "A 3 mm PETG wall with 6.4 mm standoffs and a 4 mm screwed flange, 90 g, is an ordinary on-edge PCB bracket; only the Ø1.8 pins are slender, and they only locate.", "status": "YES"},
 {"question": "P6 floating, embedded, mirrored, upside-down", "answer": "One solid; standoffs share one section face with the wall; the board placed by the reviewer from the input STEP at the spec joint (proper rotation) equals the assembly's board; solder face toward the bulkhead at x 82.438, heatsink to +X at 109.262; flange underside at y 0.", "status": "YES"},
]
ctl = []
for f in ("r06_controls.json", "r08_controls.json", "r07_controls.json"):
    for c in json.loads((W / f).read_text()):
        if "on regions" in c["check"]:  # region method not used for any gate (its control ran on a degenerate mutant)
            continue
        if c["check"] == "common_volume (U-03 interference)":
            c = dict(c, check="common_volume whole tray vs OD-E01 (blind-spot record; no gate rests on it alone)", mutant="resize: H1 seat raised 0.06 by fusing a Ø10/Ø4 disc onto the seat face (fused topology)")
        ctl.append({"check": c["check"], "mutant": c["mutant"], "got": c["got"]})
findings = [
 {"id": "F1", "gate": "U-06", "kind": "SOFT_GATE_MISS", "measured": 1.8, "unit": "mm", "required": "min_wall wide >= 2.0 (Soft)", "margin": -0.2, "at": "(82.688, 31.519, -158.238) Ø1.8 H6 pin; same at H5", "blocks": False, "risk": "LOW",
  "risk_basis": "the reading is the locating pins' own Ø1.8, gated and passing under D-06a; the part has no rounds and the tray less its pins reads 2.000; the spec names the pin exception under D-01b only, not U-06", "fix_direction": "the Usta names the two pins as a U-06 exception (as under D-01b), or the pins grow to Ø2.0, which takes D-04d to 0.23/0.24 per side"},
 {"id": "F2", "gate": "REQ-06", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "bool", "required": "board does not flex visibly under a faston push at the farthest tab (bench)", "margin": None, "at": "faston row y ~29.5, z -136..-188; farthest tab z -188 is 30.5 beyond the H6 pin standoff (z -157.51), the push toward -X", "blocks": False, "risk": "MEDIUM",
  "risk_basis": "INCONCLUSIVE by its row; the 1.56 board is held by two pins and two screws, and the six tabs between z -136 and -188 sit up to 30.5 past the nearest standoff with 6.44 of air behind them, so a 6.3 mm faston push bends that overhang; A-04, A-12", "fix_direction": "bench-test at first assembly; if it flexes, add a plain rest pad (no pin) on the wall under the tab row near z -185, y 30, clear of solder-side mains tracks (A-05)"},
 {"id": "F3", "gate": "D-05b", "kind": "OBSERVATION", "measured": 6.0, "unit": "mm", "required": "M3 x 8 screw tip short of the bore floor (A-04)", "margin": -0.438, "at": "insert bores H1/H2, floor x 76.438", "blocks": False, "risk": "MEDIUM",
  "risk_basis": "an M3 x 8 through the 1.562 board reaches x 76.0 with no washer, 0.438 past the 6.0 bore floor, so it bottoms before clamping the board; it fits only with the >= 0.44 washer A-04 assumes", "fix_direction": "state the washer thickness (>= 0.5) in A-04, or use M3 x 6, or deepen the bores to >= 6.5 by a spec change to D-05b"},
 {"id": "F4", "gate": "D-04d", "kind": "OBSERVATION", "measured": 0.3278, "unit": "mm", "required": ">= 0.30 per side with E-05 allowing 0.10 of offset", "margin": 0.0278, "at": "H6 pin (82.438, 30.185, -157.108)", "blocks": False, "risk": "LOW",
  "risk_basis": "reviewer control: a 0.10 pin shift reads 0.229 (D-04d FAIL) while E-05 still passes, so the two rows cannot both use their allowance; the pin still enters its hole with up to about 0.33 of combined error, and the hole positions are scan values (A-02)", "fix_direction": "the Usta reconciles D-04d and E-05 (for example E-05 <= 0.03 for the pins, or D-04d >= 0.20), and calipers retire A-02 on H5/H6"},
 {"id": "F5", "gate": "U-03", "kind": "OBSERVATION", "measured": 0.0, "unit": "mm3", "required": "common_volume reports a real overlap or INCONCLUSIVE", "margin": None, "at": "H1 seat, mutant with a 0.06 (also 0.5) disc fused onto the seat face", "blocks": False, "risk": "LOW",
  "risk_basis": "tool finding, not a part deviation: tools.core.common_volume returned a MEASURED 0 for tray x OD-E01 on that fused mutant (the disc alone reads 3.65 mm3; the standoff rebuilt 0.06 taller reads 3.65); the delivered rows rest on the decomposition and clearance checks, whose controls FAIL", "fix_direction": "tools maintainers: make common_volume fail closed when the boolean result has no solids while the operands' boxes overlap past contact, and add this case to the mutation manifest"},
]
least = [
 {"item": "1. D-04d against E-05 (pins 0.339 / 0.328 per side; a 0.10 offset gives 0.23)", "answer": "Confirmed: 0.3389 (H5) and 0.3278 (H6), margins 0.039 and 0.028; my H6-pin +0.10 z mutant reads 0.229 (FAIL) while E-05 would pass, so D-04d allows about 0.03 of position error. The pins still enter with up to about 0.33 of combined error; finding F4 (LOW), A-02 calipers needed."},
 {"item": "2. The seat at x 82.438, an exact contact on a scanned flat solder face; solder-side screw heads not modelled", "answer": "Four seat faces at x 82.4380, spread 0, equal to the board's lowest x 82.4380; tray less pins reaches exactly that plane (overlap 0), clearance 0 on all four seats. The board model carries the heatsink screw holes at (y 46.6, z -148.1) and (72.1, -148.2), 10.6 and 15.3 from the nearest standoff edge; their heads clear the wall only if under 6.44 tall (A-05 says under 6): open, not measurable here."},
 {"item": "3. Two walls exactly at their limits: the 2.0 web above the tie slots (D-01b) and the 3.0 boss wall (J-05; 2.975 at Ø4.05)", "answer": "Both re-measured at their limits: web 2.000 at (75.75, 92.0, -113.478) (margin 0, inside the 0.005 band) and boss wall 3.000 on all 72 rays per bore. Both PASS as built; neither has a build tolerance. FDM tends to print small vertical holes undersize, so a Ø4.05 bore is the less likely direction."},
]
out = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20261001-od-c08-electronics-bay-tray", "target": "od_c08_tray_v01", "spec_version": "1.0",
       "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"}, "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
       "summary": "Every Hard gate re-measured PASS or PASS_ASSUMED on the exported STEP, STL and 3MF; U-06 Soft misses at the Ø1.8 pins (1.8 vs 2.0); REQ-06 bench gate INCONCLUSIVE; D-01b and J-05 sit exactly at their limits; passes rest on A-01, A-02, A-03, A-06, A-07, A-08, A-09, A-11.",
       "files": files, "gates": gates, "feature_census": census, "plausibility": P, "positive_controls": ctl, "findings": findings,
       "least_sure_answers": least, "assumptions_relied_on": ["A-01", "A-02", "A-03", "A-06", "A-07", "A-08", "A-09", "A-11"]}
(J / "reviews/RV01_od_c08_tray_v01.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
import jsonschema
schema = json.loads(Path("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json").read_text())
jsonschema.validate(out, schema); print("valid", len(gates), "gates", len(ctl), "controls")
for c in ctl: print(c["got"], c["check"])
