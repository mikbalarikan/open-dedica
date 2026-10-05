import json
from pathlib import Path
J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
files = [
 ("02_STEP_STL/od_t01_rig_C1_v01.step", "cc6b1c721fd34f74232c4cee504c95c0852573fa351411ca12a02c27904c9f5c"),
 ("02_STEP_STL/od_t01_rig_C1_v01.stl", "1b2985d19a6fe86930bdf4ec448b78576ec830f6ee1f5c513a1ae2e63077d3a5"),
 ("02_STEP_STL/od_t01_assembly_C1_v01.step", "407386d44f5483aa2d2e6eab7eb72a47749aafbdb06252de5dbecfc3acf7774b"),
 ("01_CAD/REPORT_od_t01_rig_v01.md", "d44d3356664af278e29003e388db94c2aec862bc9a2b4a574604a3f50ca056b1"),
 ("01_CAD/DESIGN_PLAN.md", "544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d"),
 ("00_Spec/DESIGN_SPEC.md", "0036578bbb64a9fe6fac276b06938b135a37e9afc9de4e906ac8d5cfaa6db9f4"),
 ("00_Spec/inputs/od_g01_assembly_C1_v03.step", "9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2"),
 ("00_Spec/inputs/od_g01_housing_C1_v03.step", "55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399"),
 ("03_Sections/od_t01_rig_v01_z0_assembly.png", "777d644c8467745a38f7357d8e9e8e546c1150b9865b933c3ccd928309b9910d"),
 ("03_Sections/od_t01_rig_v01_z44_assembly.png", "388c579e5ee53f010d6f9b46fce46ca521ba0ccb037b52c876bf8360189aaf09"),
 ("03_Sections/od_t01_rig_v01_x44.png", "40a86f731c369c5b458a87ddb685e7b3bb28daa47f6cf22e9b3d85d518f61c9b"),
 ("03_Sections/od_t01_rig_v01_y5.png", "29ad37abb3054b15a07cef2be1dc8ec25c5e51de687dcdc4bd1046c9fb19b9a3"),
 ("03_Sections/od_t01_rig_v01_y142.png", "7a88b8025e5b7ade3fbf65842432f2ab761a6a4ea7a1420c8b16750f0a838116"),
]
def G(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}
gates = [
 G("U-01", 1, "bool", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "solid_count 1, brep_valid 1 (BOPAlgo faults none), naked_edges 0 of 147 edges; 0 loose shells or faces", "PASS", "tools.core.validity"),
 G("U-02", 240.0, "mm", "240.0 x 150.0 x 120.0 each in [spec - 0.1, spec + 0.1]", 0.1, "size 240.000 x 150.000 x 120.000 (each margin +0.100); position x -120.000 .. 120.000, y 0.000 .. 150.000, z -60.000 .. 60.000 (on the datum)", "PASS", "envelope"),
 G("U-03", 0.0, "mm", "(a) seat clearance = 0; interference <= 0 mm3 every pair; rig to housing elsewhere, OD-G04, OD-G10 >= 2.0; (b) offer-up dy 0..-30, steps <= 2.0: interference <= 0", 0.0, "(a) seat clearance 0.000 at (21.25, 135.00, 21.18) plate underside / housing rear face; interference rig|housing 0.000 mm3, rig|OD-G04 0.000 mm3; elsewhere: rig below y 135 to housing 15.000 (+13.0, (-65.0, 135.0, 40.0) chamfer root), rig to OD-G04 5.000 (+3.0, (-21.25, 135.0, 21.18) window edge over the pair-A boss y 130), rig to OD-G10 13.689 not inside (+11.689, (21.25, 135.0, 21.18)); (b) 31 poses dy 0..-30 every 1.0: interference rig|housing and rig|OD-G04 0.000 mm3 at every pose, OD-G10 least 13.689 (dy 0), never inside", "PASS_ASSUMED", "clearance, interference (common_volume); OD-G10 clearance fallback (REQ-04 text)", ["A-01"]),
 G("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "delivered STEP: AP242, 1 solid, label od_t01_rig, brep_valid 1, 0 stray shells / faces; reviewer re-export of the read solid: volume delta 0.000 mm3, faces delta 0 (54), labels equal, valid after", "PASS", "compare_step, step_roundtrip"),
 G("U-05", 13, "count", "plan counts: 1 plate, 2 walls (z -60..+40), 1 base, 4 corner chamfers, 4 x 3.4 holes + 4 x 6.5 counterbores (teardrop), 1 hub window (R 30 + teardrop), 4 x 4.5 bench holes (teardrop)", 0, "faces 41 planar + 13 concave cylinders, 0 other; 13 bores: 4 x 3.400 (360 deg), 4 x 6.500, 1 x 60.000, 4 x 4.500 (each 269.8 deg + 2 flanks); 4 chamfer planes 10 x 10; wall inner faces x +-75 z -60.000..40.000", "PASS", "feature_census, bore_census, locate_bore"),
 G("U-06", 3.0, "mm", ">= 2.0 (Soft)", 1.0, "(-45.10, 135.00, -47.04) plate under the (-44,-44) counterbore", "PASS", "min_wall_wide"),
 G("U-07", 0.004997, "mm", "STL at tol 0.01, angular <= 4 acos(1 - 0.01/30) = 0.1033 rad; stl_max_sagitta <= 0.01", 0.005003, "reviewer re-mesh at 0.01 mm / 0.10 rad is byte-identical to the delivered STL (SHA 1b2985d1...); 5752 triangles; sagitta 0.0050 at (-21.63, 138.75, 20.78); STL 1 body, 0 naked edges, winding consistent, volume +7.8 mm3 vs B-rep; mesh_deviation 0.0050; 3MF at J5", "PASS", "write_stl, stl_max_sagitta, mesh_census, mesh_deviation"),
 G("U-08", None, "count", "applies to threaded parts; this target has none", None, None, "NOT_APPLICABLE", "N/A by the spec row"),
 G("D-01a", 3.0, "mm", ">= 0.8", 2.2, "(-45.10, 135.00, -47.04) plate under a counterbore", "PASS", "min_wall"),
 G("D-01b", 3.0, "mm", ">= 2.0 (webs between counterbores and window, and around bench holes, included)", 1.0, "(-45.10, 135.00, -47.04) plate under a counterbore; mesh corroboration min_wall_mesh 3.000", "PASS_ASSUMED", "min_wall", ["A-08"]),
 G("D-02", 240.0, "mm", "each size <= 420 x 420 x 500 lying on the rear face: 240 x 150 on the bed, 120 tall", 180.0, "bed 240.000 x 150.000 (margins +180, +270), height 120.000 (+380)", "PASS_ASSUMED", "envelope", ["A-09"]),
 G("D-03a", 45.1, "deg", ">= 45 (build +Z); crowns of the four 3.4 holes excepted by position", 0.1, "least 45.100 at (21.25, 135.00, 21.18) window teardrop flank, on a copy with the four 3.4 holes plugged (r 1.8, y 135..138); sampling bound 0.009 deg, 0 samples below 45; unplugged: least 0.0 at (-44.0, 135.0, -42.3) on a 3.4 crown, the named exception; the 216 samples below 45 all vanish with the plugs", "PASS_ASSUMED", "overhang_census(build_dir=(0,0,1))", ["A-10"]),
 G("D-03b", 3.4, "mm", "span <= 5: the four 3.4 crowns bridge <= 3.4; nothing else bridges", 0.0, "flat_ceiling_spans 0.000 (no flat ceiling); crowns are 3.400 bores (360 deg) along Y, 3.0 long, seen in reviewer sections y 136.5 and x 44", "PASS_ASSUMED", "flat_ceiling_spans, bore_census, reviewer sections", ["A-10"]),
 G("D-04a", 3.4, "mm", "screw holes >= 3.25; bench holes >= 4.25", 0.15, "4 x 3.400 at (+-44, 135..138, +-44); 4 x 4.500 at (+-105, 0..10, +-40) (+0.250)", "PASS", "bore_census, locate_bore"),
 G("D-06a", 3.0, "mm", ">= 1.0", 2.0, "(-45.10, 135.00, -47.04)", "PASS", "min_wall"),
 G("D-07", None, "count", "none: clearance holes only", None, None, "NOT_APPLICABLE", "N/A by the spec row"),
 G("J-05", None, "count", "applies to threaded holes in this part; it has none", None, None, "NOT_APPLICABLE", "N/A by the spec row"),
 G("REQ-01", 0.0, "mm", "4 x 3.4 +- 0.1 at (+-44, +-44), offset <= 0.10 from the posed insert bores, through; 6.5 +- 0.1 counterbores y 150.0 to 138.00 +- 0.10; 3.0 +- 0.1 under each head", 0.1, "hole axes offset 0.000 from the posed insert-bore axes (4.000, y 129.3..135.0); 4 x 3.400 open both ends y 135.000..138.000; 4 x 6.500 y 138.000..150.000, floor closed; plate under head 3.000; every sub-margin +0.100", "PASS_ASSUMED", "locate_bore, bore_census", ["A-01"]),
 G("REQ-02", 135.0, "mm", "underside one plane at y 135.00 +- 0.10 over x +-50, z +-50; housing rear face on it", 0.1, "one -Y planar face at y 135.000 (x +-90, z +-60); 6960 grid points over x, z +-50 off the holes: material at y 135.002 and air at y 134.998 at every point; seat clearance 0 (U-03)", "PASS_ASSUMED", "envelope, BRep classifier grid, clearance", ["A-01"]),
 G("REQ-03", 10.97, "mm", "R 30.0 +- 0.1; roof 45.1 +- 1 deg toward +Z, apex z 42.51 +- 0.15; OD-G04 hub tube >= 2.0; pair-B axes >= 10.87 from the window face", 0.1, "pair-B axis (10.64, -15.78) to window face 10.970 at (16.78, 135.0, -24.87) (+0.100); other pair-B axis (-9.31, 16.60) 11.689; window 60.000 offset 0.000, through (R margin +0.100); flanks 45.100 deg (+0.99997); apex z 42.5006 (+0.1406); OD-G04 to rig 5.000 (+3.000)", "PASS_ASSUMED", "bore_census, locate_bore, plane-normal flank analysis, clearance, reviewer sections", ["A-05", "A-12"]),
 G("REQ-04", 11.755, "mm", "(a) phi -60..+15 deg, steps <= 5: clearance >= 5.0; (b) phi -50, dy -15, dz 0..200, steps <= 5.0: interference <= 0 read as clearance > 0, not inside", 6.755, "(a) 76 poses every 1 deg: least 11.755 at phi +15 at (75.0, 90.4, 40.0) +X wall front end, never inside; phi > 0 turns the handle to +X (max_x 67.7 / 92.0 / 114.6 at -10 / 0 / +10); (b) 81 poses every 2.5: least 28.689 at dz 50, never inside; lift phi -50, dy -15..0: least 13.689", "PASS_ASSUMED", "clearance (OD-G10 fallback)", ["A-07"]),
 G("REQ-05", 52.296, "mm", ">= 50.0 above the base top y 10", 2.296, "OD-G10 locked lowest point y 62.296", "PASS_ASSUMED", "envelope", ["A-07"]),
 G("REQ-06", 0.0, "mm3", "4 x 4.5 +- 0.1 at (+-105, +-40), offset <= 0.10; four 8 cylinders y 10..300 interference = 0", 0.0, "4 x 4.500 offset 0.000, through y 0..10 (+0.100); probes common volume 0.000 mm3 each", "PASS_ASSUMED", "locate_bore, common_volume", ["A-11"]),
 G("REQ-07", 0.0, "mm3", "four 6 cylinders y 150..300 on the screw axes: interference = 0", 0.0, "common volume 0.000 mm3 each; least clearance 0.250 to the counterbore rims", "PASS", "common_volume, clearance"),
 G("REQ-08", None, "kN", "Soft: holds 3.06 kN on four screws with no visible yield or crack (bench)", None, "not geometric; see finding F1", "INCONCLUSIVE", "bench test (A-02 hand calculation re-checked)", ["A-02"]),
]
census = [
 {"feature": "F01 frame profile (plate, 2 walls, base, 4 chamfers)", "expected": "plate y 135..150 x +-90; walls x +-(75..90) z -60..+40; base y 0..10 x +-120; 4 chamfer planes 10 x 10 at 45 deg; 41 planar faces (spec 1.1)", "found": "plate, base and walls at those coordinates; wall end faces at z 40.000; 4 chamfer planes width 14.142 (10 x 10); 41 planar faces", "status": "PASS"},
 {"feature": "F02 hub window R 30 + teardrop", "expected": "1 bore 60.0 along Y through the plate, 2 flanks 45.1 deg, apex z 42.51", "found": "60.000, y 135..150, open both ends, 269.8 deg; flanks 45.100 deg, apex z 42.501", "status": "PASS"},
 {"feature": "F03 4 x 6.5 counterbore + teardrop", "expected": "4 bores 6.5, y 138.00..150, floor closed, 8 flanks, apex 4.61", "found": "4 x 6.500 at (+-44, +-44), y 138.000..150.000, bottom closed; 8 flanks 45.100 deg; apex 4.604 from the axis", "status": "PASS"},
 {"feature": "F04 4 x 3.4 hole (no teardrop)", "expected": "4 bores 3.4 360 deg, y 135..138", "found": "4 x 3.400, 360 deg, y 135.000..138.000, open into the counterbore", "status": "PASS"},
 {"feature": "F05 4 x 4.5 bench hole + teardrop", "expected": "4 bores 4.5 through the base at (+-105, +-40), 8 flanks, apex 3.19", "found": "4 x 4.500, y 0..10 through; 8 flanks 45.100 deg; apex 3.188", "status": "PASS"},
 {"feature": "F06 name and export", "expected": "body od_t01_rig, AP242 STEP, STL 0.01 mm / 0.10 rad", "found": "label od_t01_rig, AP242; STL byte-identical to the reviewer re-mesh at 0.01 / 0.10", "status": "PASS"},
 {"feature": "F07 check assembly", "expected": "rig + housing + OD-G04 + OD-G10 at the spec 2 pose", "found": "file present, hash matches; not used for any gate (reviewer posed the set from the v03 input)", "status": "PASS"},
]
plaus = [
 {"question": "P1 gravity", "answer": "Base 240 x 120 on the bench at y 0, centre of mass (0, 72.5, -4.2) inside the footprint; the housing hangs under the plate on four screws and the brew load pulls it down into them, as on OD-C05.", "status": "YES"},
 {"question": "P2 function chains", "answer": "Screw heads on 3.0 of plate, axes 0.000 off the inserts; hub reached through the R 30 window from above; load path plate - walls - base - bench holes closed (sections z0, z44).", "status": "YES"},
 {"question": "P3 moving parts", "answer": "OD-G10 turns phi -60..+15 with >= 11.755 to the rig, goes in at phi -50 along +Z with >= 28.689 and lifts with >= 13.689; the housing set offers up 30 with no interference.", "status": "YES"},
 {"question": "P4 grip, reach, insertion", "answer": "Screw axes and bench-screw axes clear to y 300 (6 and 8 probes); the handle leaves at the open front where the walls stop at z +40; 52.3 under the portafilter for a cup.", "status": "YES"},
 {"question": "P5 absurdity", "answer": "A 240 x 150 x 120 PLA frame of 1.19 kg holding a 100 x 100 group head reads as an ordinary bench test fixture.", "status": "YES"},
 {"question": "P6 floating, embedded, mirrored, upside-down", "answer": "Housing seat clearance 0.000 with 0.000 mm3 interference; the pose is a proper rotation (x->X, y->+Z, z->-Y); teardrops point +Z, the build direction (section y 142.5); handle on +X at 34 deg as in v03.", "status": "YES"},
]
controls = [
 {"check": "validity (solid_count)", "mutant": "rig plus a copy relocated 300 in X: 2 solids", "got": "FAIL"},
 {"check": "validity (naked_edges)", "mutant": "rig with one face removed: open shell, 6 naked edges", "got": "FAIL"},
 {"check": "envelope", "mutant": "base resized +1.0 at +X: size_x 241.0", "got": "FAIL"},
 {"check": "feature_census / bore_census", "mutant": "3.4 hole at (44, 44) removed: 12 bores, 12 cylinders", "got": "FAIL"},
 {"check": "locate_bore (offset)", "mutant": "3.4 hole at (44, 44) relocated +0.5 in X: offset 0.500", "got": "FAIL"},
 {"check": "locate_bore (diameter)", "mutant": "3.4 hole at (44, 44) resized to 3.2 (D-04a)", "got": "FAIL"},
 {"check": "min_wall", "mutant": "counterbore (-44, -44) deepened to y 135.6: 0.600 under the head (D-01a, D-01b)", "got": "FAIL"},
 {"check": "min_wall_wide", "mutant": "same deepened counterbore: 0.600 (U-06)", "got": "FAIL"},
 {"check": "overhang_census (crowns plugged)", "mutant": "plugged copy with a 10-wide flat-roofed slot through the plate at x 55..65, z 0..5: 0.0 deg", "got": "FAIL"},
 {"check": "flat_ceiling_spans", "mutant": "same slot: span 10.000", "got": "FAIL"},
 {"check": "clearance (REQ-04 sweep)", "mutant": "block x 62..75, y 80..100, z 25..40 on the +X wall's inner front: least 2.655 over phi -60..+15", "got": "FAIL"},
 {"check": "clearance (REQ-03 pair-B)", "mutant": "rig relocated (-0.35, 0, +0.35): pair-B distance 10.484", "got": "FAIL"},
 {"check": "clearance (U-03 seat contact)", "mutant": "housing relocated 0.2 down: seat clearance 0.200", "got": "FAIL"},
 {"check": "interference (common_volume)", "mutant": "housing relocated 0.5 up into the plate: 3436.3 mm3; boss on a screw axis above the plate: REQ-07 282.7 mm3", "got": "FAIL"},
 {"check": "compare_step", "mutant": "re-export with the deepened counterbore compared with the delivered shape: volume delta 57.85 mm3, faces delta 1", "got": "FAIL"},
 {"check": "stl_max_sagitta", "mutant": "rig re-meshed at 0.1 mm / 0.5 rad: sagitta 0.0495", "got": "FAIL"},
 {"check": "mesh_census", "mutant": "delivered STL with its last triangle removed: 3 naked edges", "got": "FAIL"},
 {"check": "underside grid classifier (REQ-02)", "mutant": "0.5-deep pocket x 45..49, z -20..-10 in the underside: 55 grid points not material", "got": "FAIL"},
 {"check": "flank-plane apex (REQ-03)", "mutant": "rig relocated +0.5 in Z: apex 43.001", "got": "FAIL"},
]
findings = [
 {"id": "F1", "gate": "REQ-08", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "kN", "required": "holds 3.06 kN on four screws with no yield or crack (bench)", "margin": None,
  "at": "plate section at x 0 through the hub window (y 135..150)", "blocks": False, "risk": "MEDIUM",
  "risk_basis": "spec 4's hand calculation uses the full 120 x 15 plate section (Z 4500 mm3, sigma 10.5 MPa, factor 3.8), but between the screw lines the window leaves 47.5 of the 120 (z -60..-30 and 42.5..60): Z 1781 mm3, sigma 26.6 MPa simply supported, factor about 1.5 against an unsourced 40 MPa for PLA (lower with end fixity from the walls); the M3 heads also bear on 3.0 of plate across the layers.",
  "fix_direction": "Redo A-02 with the window section (and the head pull-through) before the test; if the factor stays near 1.5, thicken the plate or add ribs beside the window, or raise the test pressure in steps behind a shield."},
 {"id": "F2", "gate": "REQ-03", "kind": "OBSERVATION", "measured": 42.5006, "unit": "mm", "required": "apex z 42.51 +- 0.15", "margin": 0.1406,
  "at": "window apex (0, 135..150, 42.50)", "blocks": False, "risk": "LOW",
  "risk_basis": "the delivered apex has +0.141 margin; spec 1.2's band holds the R 30.0 +- 0.1 stack only through the 0.005 band (R 29.9 gives apex 42.358 against 42.36), and pair-B at R 29.9 is exactly 10.870; no function depends on the apex.",
  "fix_direction": "None for the part; if the spec is revised again, widen the apex band to +- 0.16 or state it as a consequence of R."},
]
least = [
 {"item": "1. REQ-03 has no tolerance on the window radius", "answer": "Spec 1.2 now carries apex +- 0.15 and pair-B >= 10.87. Measured R 30.000, apex 42.501 (+0.141), pair-B 10.970 (+0.100): PASS. The REPORT's window_r sweep values (apex 42.359 / 42.642, pair-B 10.870) now pass, the low apex only inside the 0.005 band (F2)."},
 {"item": "2. The D-03a exception is located by position", "answer": "Independent route: the four 3.4 holes plugged (all four axes measured 0.000 off nominal) and the census re-run: least 45.100 deg at the window flank, 0 samples below 45; the 216 samples below 45 on the unplugged part are all on the crowns. Sections y 136.5 and x 44 show only the crowns. The REPORT's swept-locator FAILs are a script artefact, not an overhang."},
 {"item": "3. OD-G10 is not a sound solid", "answer": "Confirmed brep_valid 0 on the posed OD-G10 (housing and OD-G04 are 1). Every OD-G10 row used the spec's clearance > 0, not inside fallback: least 13.689 (U-03, lift), 11.755 (REQ-04a), 28.689 (REQ-04b), never inside; the clearance check FAILs on its mutant."},
]
v = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20261002-od-t01-pressure-test-rig", "target": "od_t01_rig_v01", "spec_version": "1.2",
     "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"}, "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
     "summary": "One valid 240 x 150 x 120 solid; every hard row of spec 1.2 re-measured and met (least margins: REQ-03 pair-B +0.100, D-03a +0.100 deg, D-01b +1.000, REQ-04a +6.755), resting on A-01, A-05, A-07, A-08, A-09, A-10, A-11, A-12; REQ-08 strength is INCONCLUSIVE and the spec's hand calculation overstates the factor (about 1.5, not 3.8, at the window section).",
     "files": [{"path": p, "sha256": h, "matches_report": True} for p, h in files],
     "gates": gates, "feature_census": census, "plausibility": plaus, "positive_controls": controls, "findings": findings,
     "least_sure_answers": least, "assumptions_relied_on": ["A-01", "A-05", "A-07", "A-08", "A-09", "A-10", "A-11", "A-12"]}
# minimal schema validation
s = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
def check(obj, sch, path="$"):
    t = sch.get("type"); errs = []
    if "anyOf" in sch:
        if not any(not check(obj, alt, path) for alt in sch["anyOf"]): errs.append(f"{path}: anyOf")
        return errs
    tm = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
    if t == "number":
        if not (isinstance(obj, (int, float)) and not isinstance(obj, bool)): errs.append(f"{path}: not number")
    elif t and not isinstance(obj, tm[t]): errs.append(f"{path}: not {t}"); return errs
    if "enum" in sch and obj not in sch["enum"]: errs.append(f"{path}: {obj} not in enum")
    if "pattern" in sch:
        import re
        if not re.search(sch["pattern"], obj): errs.append(f"{path}: pattern")
    if t == "object":
        for k in sch.get("required", []):
            if k not in obj: errs.append(f"{path}: missing {k}")
        if sch.get("additionalProperties") is False:
            for k in obj:
                if k not in sch["properties"]: errs.append(f"{path}: extra {k}")
        for k, sub in sch.get("properties", {}).items():
            if k in obj: errs += check(obj[k], sub, f"{path}.{k}")
    if t == "array":
        for i, it in enumerate(obj): errs += check(it, sch["items"], f"{path}[{i}]")
    return errs
errs = check(v, s); print("schema errors:", errs)
assert {g["gate"] for g in gates} == {"U-01","U-02","U-03","U-04","U-05","U-06","U-07","U-08","D-01a","D-01b","D-02","D-03a","D-03b","D-04a","D-06a","D-07","J-05","REQ-01","REQ-02","REQ-03","REQ-04","REQ-05","REQ-06","REQ-07","REQ-08"}
(J / "reviews/RV01_od_t01_rig_v01.json").write_text(json.dumps(v, indent=2, ensure_ascii=False) + "\n")
json.dump(v, open(J / "reviews/RV01_work/verdict_data.json", "w"))
