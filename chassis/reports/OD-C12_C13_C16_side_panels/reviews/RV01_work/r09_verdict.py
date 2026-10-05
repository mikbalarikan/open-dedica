"""RV01: write the JSON twin from the measurement files and validate it against the schema subset."""
import json, re, hashlib
from pathlib import Path
WS = Path("/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels")
W = WS / "reviews/RV01_work"
J = lambda n: json.load(open(W / n))
c13, c12, c16 = J("parts_c13.json"), J("parts_c12.json"), J("parts_c16.json")
ps, asm, path, ctr = J("print_sections.json"), J("assembly_a.json"), J("assembly_path.json"), J("controls.json")
sha = lambda p: hashlib.sha256((WS / p).read_bytes()).hexdigest()

files = [(p, sha(p)) for p in (
    "02_STEP_STL/od_c13_right_C1_v01.step", "02_STEP_STL/od_c13_right_C1_v01.stl",
    "02_STEP_STL/od_c12_left_C1_v01.step", "02_STEP_STL/od_c12_left_C1_v01.stl",
    "02_STEP_STL/od_c16_bracket_C1_v01.step", "02_STEP_STL/od_c16_bracket_C1_v01.stl")]
REPORTED = {"02_STEP_STL/od_c13_right_C1_v01.step": "bb029af485a12941c364302b8a2f98c5b9c2436f73aea68e66bb8ed69be11a71",
            "02_STEP_STL/od_c13_right_C1_v01.stl": "50beff9b3ddbc572d9020309e4c5e758830331a360c52d55ae1ca117d0dccf88",
            "02_STEP_STL/od_c12_left_C1_v01.step": "972343ab6af3684acf9000208761baa390e489cabe30d238c62ffa36e62f8408",
            "02_STEP_STL/od_c12_left_C1_v01.stl": "872489a1afefcb39e725b3339595770184b17368deab05e7e9f1eaca66ee5d55",
            "02_STEP_STL/od_c16_bracket_C1_v01.step": "39faff6ce71326fc8d562d8c3daa42cd938fdf24f4dbe0933d82e9cae569c9fc",
            "02_STEP_STL/od_c16_bracket_C1_v01.stl": "0519dcb42e099fdc6433cc371989b0806ac74bd2e77aa7c43d3891c5ac6f19d5"}

def g(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at,
            "status": status, "method": method, "assumes": list(assumes)}

others_least = min(v["clearance"]["measured"] for v in asm["others"].values())
dev = max(c13["mesh_deviation"]["measured"], c12["mesh_deviation"]["measured"], c16["mesh_deviation"]["measured"])
gates = [
    g("U-01", 1, "bool", "solid_count = 1, brep_valid = 1, naked_edges = 0, each part file", 0,
      "OD-C13, OD-C12, OD-C16 files each: 1 solid, brep_valid 1, naked edges 0", "PASS", "validity"),
    g("U-02", 218.8105, "mm", "each size in [spec - 0.1, spec + 0.1]", 0.0995,
      "OD-C13 and OD-C12 size_y 218.8105 (spec 218.81); OD-C13 10.000 x 218.8105 x 385.000 at x 110..120, y 0..218.8105, z -295..+90; OD-C12 the same at x -120..-110; OD-C16 19.000 x 16.000 x 16.000 at x -19..0, y 0..16, z -8..+8 (margin 0.100)",
      "PASS", "envelope"),
    g("U-03", 0.4, "mm", "(a) designed contacts clearance = 0, interference <= 0; lip to OD-C10 0.40 +- 0.05; other pairs clearance >= 0.5; coaxiality <= 0.20; (b) path interference <= 0 mm3", 0.05,
      f"governing: lip to OD-C10 skirt 0.4000 at (+-116.6, 215.0, -280.0) both panels; 16 designed contacts clearance 0.000 and interference 0.000 mm3; 100 other pairs least {others_least:.3f} (OD-C12 to OD-C07, margin +0.400), then 3.000 (panels to OD-C11), 5.000 (OD-C13 to OD-C08); 116 pairs interference 0.000 mm3; six insert-bore to panel-hole axis offsets 0.000 (<= 0.20, margin +0.200); (b) six brackets down from +20, two panels in from 20 outside, OD-C10 down from +40, steps 1.0: 0.000 mm3 at every step",
      "PASS_ASSUMED", "clearance, interference (common_volume), locate_bore; own path stepper", ["A-01", "A-02", "A-03", "A-04", "A-05"]),
    g("U-04", 5.82e-11, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", -5.82e-11,
      "each part file: AP242, unit MM, label kept (od_c13_right, od_c12_left, od_c16_bracket), 1 solid, faces delta 0, valid after; volume delta <= 5.8e-11 mm3 (band 0.001)",
      "PASS", "step_roundtrip, compare_step"),
    g("U-05", 3, "count", "per spec 1.2 and the plan as amended: OD-C13 11 planes / 3 concave cylinders / 3 bores; OD-C12 15 / 3 / 3; OD-C16 8 / 3 / 3", 0,
      "OD-C13 11/3/3, OD-C12 15/3/3, OD-C16 8/3/3; every plan feature located (section 3)", "PASS",
      "feature_census, bore_census, locate_bore"),
    g("U-06", 2.1, "mm", ">= 2.0 (min_wall wide, 45 deg)", 0.1,
      "OD-C12 wall at the relief (-120.0, 54.6, -29.5); OD-C13 3.000, OD-C16 3.000", "PASS", "min_wall detail wide (spacing 0.6 panels, 0.4 bracket)"),
    g("U-07", round(dev, 6), "mm", "STL tol 0.01, angular <= 4 acos(1 - 0.01/R_max); stl_max_sagitta <= 0.01", round(0.01 - dev, 6),
      "delivered STLs: deviation 0.004993 (both panels, R_max 1.7, angular limit 0.434074 rad), 0.004988 (bracket, R_max 3.25, limit 0.313866 rad); one closed shell, winding 1, volume > 0; triangle counts 536 / 552 / 588 equal to a fresh mesh at those settings",
      "PASS", "mesh_deviation, mesh_census, write_stl (fresh, for comparison)"),
    g("U-08", None, "count", "applies to threaded parts; these targets have none", None, "no threads modelled on any part", "NOT_APPLICABLE", "N/A by its row"),
    g("D-01a", 2.1, "mm", ">= 0.8", 1.3, "OD-C12 relief wall (-120.0, 54.6, -29.5); OD-C13 3.000; OD-C16 3.000 (counterbore floor)", "PASS", "min_wall"),
    g("D-01b", 2.1, "mm", ">= 2.0", 0.1, "OD-C12 relief wall (-120.0, 54.6, -29.5); OD-C13 3.000 (wall); OD-C16 3.000 at (-13.40, 3.0, -3.07), counterbore floor", "PASS", "min_wall"),
    g("D-02", 385.0, "mm", "panels <= Kobra Max 3 (A-09: 420 x 420 x 500) lying on the outer face; bracket <= K1C (A-10: 220 x 220 x 250)", 35.0,
      "panels 385.0 x 218.81 on the bed, 10.0 tall; bracket 19 x 16 x 16 (margin 201.0)", "PASS_ASSUMED", "envelope", ["A-09", "A-10"]),
    g("D-03a", 60.0, "deg", ">= 45 from horizontal in the sec. 4 print orientation; bracket insert-bore crown excluded (named exception)", 15.0,
      "OD-C13 build -X and OD-C12 build +X: least 60.000 on the lip slope (116.6, 215.0, 80.0); OD-C16 build +Y outside the exception 90.000 (nothing downward); exception: crown 0.000 at (-6.0, 12.0, 0.0)",
      "PASS_ASSUMED", "overhang_census (spacing 0.6 panels, 0.5 bracket)", ["A-11"]),
    g("D-03b", 4.0, "mm", "span <= 5", 1.0,
      "OD-C16 insert-bore crown Ø4.000 at (-3, 12, 0), from own sections x -3 and z 0.3; flat ceilings 0.000 on all three parts", "PASS_ASSUMED",
      "own sections; flat_ceiling_spans corroborates", ["A-11"]),
    g("D-04a", 3.4, "mm", ">= 3.25", 0.15, "six panel holes Ø3.400 along X at (+-118.5, 10, -262/-15/+62); bracket hole Ø3.400 along Y at (-12.5, 1.5, 0)", "PASS", "bore_census, locate_bore"),
    g("D-04d", 0.4, "mm", ">= 0.30 per side", 0.1, "lip toe (+-116.6, 215.0) to OD-C10 skirt inner face x +-117.0, both panels", "PASS_ASSUMED", "clearance", ["A-02", "A-14"]),
    g("D-05a", 12.0, "mm", ">= 8.0 across around the insert bore", 4.0,
      "least outer radius 6.000 toward the top face (y 16) about the bore axis (0, 10, 0) along -X, 24 angles x 24 levels over x 0..-6", "PASS_ASSUMED", "radial_profile, bore_census", ["A-12"]),
    g("D-05b", 4.0, "mm", "Ø4.0 +- 0.05, depth 6.0 +- 0.1 (>= 5.7)", 0.05, "insert bore Ø4.000, length 6.000, open at x 0, closed (flat floor) at x -6.0, axis (y 10, z 0)", "PASS_ASSUMED", "bore_census, locate_bore", ["A-12"]),
    g("D-06a", 2.1, "mm", ">= 1.0", 1.1, "least wall OD-C12 relief 2.100; lip wedge apex edge read from sections (finding F2)", "PASS", "min_wall; own sections"),
    g("D-07", None, "count", "none: the insert bore is formed by the insert, the rest are clearance holes", None, "no fit-critical bore on these parts", "NOT_APPLICABLE", "N/A by its row"),
    g("J-05", 3.25, "mm", ">= 3.0 around the bracket's insert bore", 0.25,
      "web from the bore floor (x -6) to the counterbore wall (x -9.25), exact face distance; to top face 4.000, sides 6.000, underside 8.000; global min_wall 3.000 (counterbore floor, not around this bore)",
      "PASS", "exact face-to-face distance (BRepExtrema) from the bore faces; min_wall beside it"),
    g("E-06", 1, "count", "bracket one solid block; lip tied into rail, rail into wall", 0,
      "each part one solid; sections z -100 and z +60 (both panels) one closed region through wall, rail and lip; bracket section z 0.3 one region", "PASS", "validity, own sections"),
    g("REQ-01", 215.0, "mm", "outer x +-120.00 +- 0.10, inner +-117.00 +- 0.10; underside y 0.00 +- 0.05; top y 215.00 +- 0.05 over x +-(116.6..120); ends z -295.00 / +90.00 +- 0.10; footprint over plate", 0.05,
      "sections y 50 and y 200: outer 120.000, inner 117.000 over z -295..+90 (OD-C12 inner face at the relief left to REQ-04); one underside plane y 0.000; one top face y 215.000 over x 116.6..120; ends -295.000 / +90.000; footprint prism 6930.0 / 6222.6 mm3 all inside OD-C01",
      "PASS_ASSUMED", "envelope of faces, own sections, common_volume", ["A-01"]),
    g("REQ-02", 0.4, "mm", "wedge (+-110, 215), (+-116.6, 215), (+-110, 218.81) +- 0.1; slope 60 +- 1 deg; z -280..+80 +- 0.1; clearance to OD-C10 0.40 +- 0.05", 0.05,
      "sections z -100 and +60, both panels: vertices (+-110.000, 215.000), (+-116.600, 215.000), (+-110.000, 218.8105); slope 60.0001 deg from the panel plane; z -280.000..+80.000; gap 0.4000",
      "PASS_ASSUMED", "own sections, envelope, clearance", ["A-02", "A-14"]),
    g("REQ-03", 0.0, "mm", "three Ø3.4 +- 0.1 through along X at (y 10, z -262/-15/+62), offset <= 0.10", 0.1,
      "both panels: Ø3.400, offset 0.000, through, length 3.0", "PASS_ASSUMED", "bore_census, locate_bore", ["A-07"]),
    g("REQ-04", -117.9, "mm", "inner face x -117.90 +- 0.05 over y 0..55, z -160..-29 (+- 0.1); clearance(OD-C12, OD-C07) >= 0.5", 0.05,
      "relief floor one plane x -117.900, y 0.000..55.000, z -160.000..-29.000; clearance to OD-C07 0.900 (margin +0.400)", "PASS_ASSUMED", "envelope of the floor face, own sections, clearance", ["A-04"]),
    g("REQ-05", 3.0, "mm", "block 19 x 16 x 16; Ø3.4 through along Y at (-12.5, 0) offset <= 0.10; Ø6.5 +- 0.1 counterbore floor y 3.00 +- 0.10; Ø4.0 bore along -X at (y 10, z 0) offset <= 0.10; plate holes at (+-104.5, z_c) +- 0.10", 0.1,
      "counterbore Ø6.500 floor y 3.000; hole Ø3.400 offset 0.000 through; insert bore offset 0.000; six placed plate holes at (+-104.5, z_c) offset 0.000",
      "PASS_ASSUMED", "bore_census, locate_bore, envelope", ["A-01", "A-07"]),
    g("REQ-06", 15.5, "mm", ">= 8.0 to the plate edge; >= 6.0 to every OD-C01 hole and handed-over insert; plate solid in a Ø8 circle", 7.5,
      "all six (+-104.5, z_c): edge 15.500; nearest OD-C01 bore 28.306 ((-113, -42) Ø4.0); nearest handed-over insert 22.142 ((+-95, -282)); Ø8 x 6 disc 301.593 of 301.593 mm3 in OD-C01",
      "PASS_ASSUMED", "bore_census of OD-C01, own distance arithmetic, common_volume", ["A-01"]),
    g("REQ-07", 0.0, "mm3", "interference = 0 of the foot keep-outs, the driver-access and the panel-screw access cylinders", 0.0,
      "4 keep-outs x 8 new parts, 6 driver cylinders (r 4, y 16..215) x 16 solids, 6 panel-screw cylinders (r 4, 20 outside) x 19 solids: all 0.000 mm3",
      "PASS_ASSUMED", "common_volume", ["A-05"]),
    g("REQ-08", None, "count", "Soft: no visible flex or drumming with the lid on; a hand on a side does not shift the lid (bench)", None,
      "not geometric; answered by the first print (finding F1)", "INCONCLUSIVE", "bench (none in CAD)", ["A-13"]),
]

census = [
    ("OD-C13 F01-F02 wall with 2 square end faces", "faces x 117 and x 120 over y 0..215, z -295..+90; ends z -295 and z +90", "found: one inner face x 117.000, one outer x 120.000, underside y 0, ends z -295.000 and +90.000", "PASS"),
    ("OD-C13 F03 top rail", "x 110..117, y 205..215, z -280..+80", "underside y 205.000 over x 110..117, z -280..+80; ends at z -280.000 / +80.000", "PASS"),
    ("OD-C13 F04 lip wedge (one 60 deg face)", "triangle (110, 215), (116.6, 215), (110, 218.81), z -280..+80", "one sloped plane, normal (0.5, 0.866, 0), x 110..116.6, y 215..218.8105; 60.0001 deg", "PASS"),
    ("OD-C13 F05 merged faces", "11 planes, 3 cylinders", "11 planes, 3 concave cylinders, 0 other", "PASS"),
    ("OD-C13 F06 holes x3", "Ø3.4 through along X at (y 10, z -262/-15/+62)", "3 bores Ø3.400 x 117..120, through, offset 0.000", "PASS"),
    ("OD-C12 F11-F12 mirrored panel", "mirror of OD-C13 at x -120..-110", "same faces mirrored; slope normal (-0.5, 0.866, 0); 3 bores Ø3.400 through", "PASS"),
    ("OD-C12 F13 relief", "floor x -117.9, y 0..55, z -160..-29, 4 faces", "floor plane x -117.900, y 0..55, z -160..-29; faces y 55, z -160, z -29; 15 planes", "PASS"),
    ("OD-C16 F21 block", "x -19..0, y 0..16, z -8..+8", "19.000 x 16.000 x 16.000 at that position; 8 planes, 3 cylinders", "PASS"),
    ("OD-C16 F22 plate-screw hole", "Ø3.4 through along Y at (x -12.5, z 0)", "Ø3.400 y 0..3, through, offset 0.000", "PASS"),
    ("OD-C16 F23 counterbore", "Ø6.5 from y 16 to floor y 3", "Ø6.500 y 3..16, open at y 16, closed at y 3.000", "PASS"),
    ("OD-C16 F24 insert bore", "Ø4.0 x 6.0 blind along -X from x 0 at (y 10, z 0)", "Ø4.000 x -6..0, open at x 0, flat floor x -6.000, offset 0.000", "PASS"),
]
plaus = [
    ("P1 gravity", "Panels stand on the plate top and the brackets on the plate (clearance 0.000, interference 0.000); the lid's side skirts rest on the panel tops at y 215; nothing hangs on a screw alone.", "YES"),
    ("P2 function chains", "No air, liquid, drive or cable passes through the new parts; the panels close the sides 5.000 from the electronics tray and 3.000 from OD-C11, whose vents stay the bay's exhaust.", "YES"),
    ("P3 moving parts", "No moving parts; every assembly path (brackets down, panels in, lid down) reads 0.000 mm3 at every 1.0 step.", "YES"),
    ("P4 grip, reach, insertion", "Bracket screws driven from above along a clear r 4 axis (panels and lid off); panel screws from outside along X with 20 clear; panels offered inward onto the brackets; lid lowered last; the order of spec sec. 4 is the only one that fits.", "YES"),
    ("P5 nothing absurd", "A 3 mm printed side wall with a top rail and a 60 deg locating lip on three corner brackets is ordinary printed-enclosure practice; the proud button heads and the rear-corner slit are ledgered (A-07, A-03).", "YES"),
    ("P6 floating, embedded, mirrored, upside-down", "Every designed contact reads 0.000 with no interference; the left panel is a true mirror with its relief on the inner face over OD-C07; the lips point up inside the skirts; the left brackets face their insert bores at x -117.", "YES"),
]
findings = [
    {"id": "F1", "gate": "REQ-08", "kind": "SOFT_GATE_MISS", "measured": None, "unit": "count",
     "required": "Soft: no visible flex or drumming with the lid on; a hand on a side does not shift the lid",
     "margin": None, "at": "both panels, the free wall between brackets (z -262 to -15, 247 mm) under the lid", "blocks": False, "risk": "MEDIUM",
     "risk_basis": "a 3.0 PLA plate 385 x 215, held at three points along its foot and along its top only by the 0.40-gap lip in the skirt, may drum or bow between brackets; no calculation exists (A-13)",
     "fix_direction": "answer on the first print with a hand-load and tap test; if it drums, add a fourth bracket or a stiffening rib on the inner face clear of OD-C07 and OD-C08"},
    {"id": "F2", "gate": "D-06a", "kind": "OBSERVATION", "measured": 60.0, "unit": "deg",
     "required": "minimum feature >= 1.0 (min_wall); the lip wedge as spec sec. 4 defines it",
     "margin": None, "at": "lip apex edge (+-110.000, 218.8105) over z -280..+80, both panels", "blocks": False, "risk": "LOW",
     "risk_basis": "the spec's wedge ends in a 60 deg convex edge that min_wall cannot read (flank normals 120 deg apart); material normal to the slope is under 1.0 only within 1.155 of the edge; in the flat print the edge lies in the top layer and every layer of the lip is wider than the one below, and it carries no load (the skirt bears on y 215)",
     "fix_direction": "none needed for function; if a crisp edge is unwanted, a 0.5 flat or round on the apex in a later spec revision"},
]
least = [
    ("9.1 coaxiality tolerance stack", "Under spec 1.2 (offset <= 0.20) the stack cannot fail: with REQ-03 and REQ-05 each <= 0.10, two parallel axes are at most 0.20 apart, so the opposed extreme sits at zero margin and passes within the band; as built all six axis offsets measure 0.000 and the plate holes 0.000 from (+-104.5, z_c). No finding."),
    ("9.2 lip gap", "Measured 0.4000 on both panels from the wedge to OD-C10 as delivered (skirt inner faces at x +-117.000); lowering OD-C10 from +40 in 1.0 steps over panels and brackets reads 0.000 mm3 at every step; a +0.5 relocated panel makes the same stepper fail (1.04 mm3). The physical lid still rests on A-02 and A-14."),
    ("9.3 lip apex not reached by min_wall", "Read from my own sections at z -100 and z +60 on both panels: apex (+-110.000, 218.8105), toe (+-116.600, 215.000), slope 60.0001 deg from the panel plane (60 +- 1), included angle 60 deg; min_wall at 0.6 spacing reads 3.000 / 2.100 elsewhere and does not see the edge by design (flanks 120 deg apart). Rated as F2, LOW, non-blocking."),
]
assum = sorted({a for row in gates for a in row["assumes"] if row["status"] == "PASS_ASSUMED"}, key=lambda s: int(s[2:]))
doc = {
    "schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20261002-od-c12-c13-c16-side-panels",
    "target": "od_side_panels_v01", "spec_version": "1.2",
    "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"},
    "verdict": "APPROVED_ASSUMPTION_CONDITIONAL",
    "summary": "Three valid single solids (OD-C13, OD-C12, OD-C16) re-measured from the exported STEP: every Hard row PASS or PASS_ASSUMED; lip gap 0.400, least other clearance 0.900 (OD-C12 to OD-C07), coaxiality 0.000, assembly path 0.000 mm3; REQ-08 Soft INCONCLUSIVE (bench); no blocking finding.",
    "files": [{"path": p, "sha256": h, "matches_report": h == REPORTED[p]} for p, h in files],
    "gates": gates,
    "feature_census": [{"feature": a, "expected": b, "found": c, "status": d} for a, b, c, d in census],
    "plausibility": [{"question": a, "answer": b, "status": c} for a, b, c in plaus],
    "positive_controls": [{"check": r["check"], "mutant": r["mutant"], "got": r["got"]} for r in ctr],
    "findings": findings,
    "least_sure_answers": [{"item": a, "answer": b} for a, b in least],
    "assumptions_relied_on": assum,
}

# ---- validate against the schema subset
schema = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
errs = []
def check(node, sch, where):
    if "anyOf" in sch:
        if not any(not _try(node, s) for s in sch["anyOf"]):
            errs.append(f"{where}: anyOf"); return
        return
    t = sch.get("type")
    tmap = {"object": dict, "array": list, "string": str, "boolean": bool}
    if t == "number":
        if not (isinstance(node, (int, float)) and not isinstance(node, bool)): errs.append(f"{where}: not number")
    elif t == "null":
        if node is not None: errs.append(f"{where}: not null")
    elif t and not isinstance(node, tmap[t]): errs.append(f"{where}: not {t}"); return
    if "enum" in sch and node not in sch["enum"]: errs.append(f"{where}: {node!r} not in enum")
    if "pattern" in sch and not re.search(sch["pattern"], node): errs.append(f"{where}: pattern")
    if t == "object":
        for k in sch.get("required", []):
            if k not in node: errs.append(f"{where}: missing {k}")
        if sch.get("additionalProperties") is False:
            for k in node:
                if k not in sch["properties"]: errs.append(f"{where}: extra {k}")
        for k, s in sch.get("properties", {}).items():
            if k in node: check(node[k], s, f"{where}.{k}")
    if t == "array":
        for i, v in enumerate(node): check(v, sch["items"], f"{where}[{i}]")
def _try(node, s):
    global errs
    saved = errs; errs = []
    check(node, s, ""); bad = bool(errs); errs = saved
    return bad
check(doc, schema, "$")
# self-consistency
assert all(r["assumes"] for r in gates if r["status"] == "PASS_ASSUMED")
assert not any(f["blocks"] for f in findings) and doc["verdict"] != "REVISE"
assert all(r["got"] == "FAIL" for r in doc["positive_controls"])
assert all(f["matches_report"] for f in doc["files"])
print("schema errors:", errs)
out = WS / "reviews/RV01_od_side_panels_v01.json"
out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
print(out, hashlib.sha256(out.read_bytes()).hexdigest(), len(gates), "gates", assum)
