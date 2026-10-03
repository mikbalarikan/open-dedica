import json
J = "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_od_c14_grommet_v01.json"
def g(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return dict(gate=gate, measured=measured, unit=unit, required=required, margin=margin, at=at, status=status, method=method, assumes=list(assumes))
gates = [
 g("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "whole half; brep_valid 1, naked_edges 0, free shells 0, free faces 0", "PASS", "validity"),
 g("U-02", 19.984, "mm", "20.0 x 9.6 x 13.0 each in [spec - 0.1, spec + 0.1]; position reported apart", 0.084, "size_x at the split-face chord; sizes 19.984 x 9.600 x 13.000; position x 85.008..104.992, y 30.400..40.000, z -304.000..-291.000", "PASS", "envelope"),
 g("U-03", 0.8, "mm", "(a) contacts = 0, half-OD-C11 >= 0.30, tie/head to inner face 0.20 +/- 0.10, halves 0.80 +/- 0.05, to gussets/flange >= 0.5, to OD-C01 >= 10, tie OD > 12.0; (b) halves touch, half-OD-C11 >= 0.30, squeeze 0.40 +/- 0.07; (c) path interference <= 0", 0.05, "governing: halves gap 0.800 at (98.769, 30.4/29.6, -304.0); also (a) flange 0.000, bore-cord 0.000, tie-groove 0.000, neck-hole 0.350 (100.636, 30.4, -301.9), tie 0.200 and head 0.200 to inner face (z -298.8 vs -299.0), gussets/flange 8.411/3.010/2.9995/14.677, OD-C01 30.4/20.0/23.55/36.45, tie OD 12.900, 21 pairs 0 mm3; (b) split offsets 0.400/0.400, halves 0.000 mm and 0 mm3, neck-hole 0.364 (margin 0.064), squeeze 0.400/0.400 (margin 0.07); (c) 41 poses dz -20..0 step 0.5 x closing 0/0.2/0.4, worst 0 mm3 against OD-C11 and OD-C01, least gap 0.350", "PASS_ASSUMED", "clearance, interference, common_volume, radial_extent, envelope", ["A-01", "A-02", "A-04"]),
 g("U-04", 1.1e-13, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "re-read: 1 solid labelled od_c14_grommet_half, AP242, mm, 0 free shells, 0 free faces; write_step + re-read of that solid: volume delta 1.1e-13, faces delta 0, labels 1, valid_after 1", "PASS", "compare_step, step_roundtrip"),
 g("U-05", 14, "count", "flange, neck, groove, flank, collar and end faces, 1 split face (y 30.4), 1 half-bore r 3.5, 2 bore chamfers", 0, "plane 6, cylinder 5 (convex 4, concave 1), cone 3, other 0, bores 0; each face matched to its plan feature by axis and radius", "PASS", "feature_census, radial_extent"),
 g("U-06", 1.65, "mm", ">= 1.6 (min_wall wide)", 0.05, "(90.029, 31.346, -298.614) groove floor", "PASS", "min_wall_wide"),
 g("U-07", 0.00584, "mm", "STL at tol 0.01, angular <= 0.1789 rad; stl_max_sagitta <= 0.01", 0.00416, "(95.806, 35.333, -293.167) collar flank; delivered STL 1658 triangles, 1 body, 0 naked edges, winding 1, volume 538.319 mm3; re-mesh at 0.01 / 0.10 rad gives 1658 triangles and sagitta 0.00584", "PASS", "mesh_deviation, mesh_census, write_stl"),
 g("U-08", None, "count", "threads cosmetic: applies to threaded parts; this target has none", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("D-01a", 1.65, "mm", ">= 0.8", 0.85, "(90.029, 31.346, -298.614) groove floor", "PASS", "min_wall"),
 g("D-01b", 1.65, "mm", ">= 1.6", 0.05, "(90.029, 31.346, -298.614) groove floor; mesh corroborates 1.6485", "PASS_ASSUMED", "min_wall", ["A-03"]),
 g("D-02", 19.984, "mm", "20.0 x 9.6 x 13.0 within the K1C build volume (220 x 220 x 250), standing on the flange", 200.016, "envelope 19.984 x 9.600 x 13.000", "PASS_ASSUMED", "envelope", ["A-07"]),
 g("D-03a", 59.886, "deg", ">= 45 deg from horizontal, build_dir +Z", 14.886, "(91.549, 30.581, -303.500) bed-side bore chamfer; flank 60.000", "PASS_ASSUMED", "overhang_census", ["A-06"]),
 g("D-03b", 0.0, "mm", "bridge span <= 5", 5.0, "no flat ceiling; sections x 95, y 32, z -296.6 show none", "PASS_ASSUMED", "flat_ceiling_spans; reviewer sections", ["A-06"]),
 g("D-04d", 0.35, "mm", "neck and collar to the 12.0 hole >= 0.30 per side, open pose", 0.05, "(100.636, 30.400, -301.900) neck at the split edge; collar on the path 0.350; hole 12.000 measured", "PASS_ASSUMED", "clearance, radial_profile", ["A-01"]),
 g("D-06a", 1.65, "mm", ">= 1.0", 0.65, "(90.029, 31.346, -298.614) groove floor", "PASS", "min_wall"),
 g("D-07", None, "count", "none: the bore is a clamp on a compliant cord, sized by REQ-02", None, None, "NOT_APPLICABLE", "N/A by its row"),
 g("J-06", 0, "count", "printed threads none", 0, "bore_census 0; B-spline and other faces 0", "PASS", "bore_census, feature_census"),
 g("E-11", 0.4, "mm", "cord gripped by the closed halves, tie on the inner face against pull-out, flange on the outer face against push-in, both bore ends chamfered", 0.07, "squeeze 0.400 both halves; tie 0.200 off the inner face with OD 12.9 over the 12.0 hole; flange 0.000 on the outer face; chamfers r 3.5->4.0 (inside) and 3.5->3.79 (outside); reviewer sections", "PASS_ASSUMED", "reviewer sections; radial_extent, clearance", ["A-02", "A-04", "A-05"]),
 g("REQ-01", 11.3, "mm", "flange 20.0 +/- 0.1; neck, groove, collar diameters +/- 0.05; flank 60 +/- 1 deg; z +/- 0.1; coaxial <= 0.05", 0.05, "neck/collar 11.300, groove 10.300, flange 20.000, spread 0.000 over 10..170 deg; z -304.000/-302.000/-298.800/-293.600/-292.734/-291.000; flank 60.000 deg; every axis at (95.000, 30.000)", "PASS_ASSUMED", "radial_profile, radial_extent, envelope", ["A-01"]),
 g("REQ-02", 30.4, "mm", "bore r 3.50 +/- 0.05; split plane y 30.40 +/- 0.02; chamfers 0.5 x 45 and 0.50 x 0.29 +/- 0.1", 0.02, "split face 2 faces at y 30.400; bore r 3.500 (min = max over 17 angles x 120 levels); inside chamfer 0.50 radial x 0.50 axial; outside 0.29 radial x 0.50 axial", "PASS_ASSUMED", "radial_profile, radial_extent, envelope, feature_census", ["A-02", "A-05"]),
 g("REQ-03", 19.984, "mm", "pair at the closed pose: outline of REQ-01 across X, 0.8 less across Y", 0.084, "my own 180 deg copy about the measured hole axis; closed union 19.984 x 19.200 x 13.000, one valid solid", "PASS", "envelope"),
 g("REQ-04", 5.2, "mm", "groove 5.2 +/- 0.1 at the floor; tie OD 12.9 > 12.0; head box >= 0.5 from OD-C11 features other than the inner face", 0.1, "groove floor z -298.800..-293.600; tie OD 12.900; head box to gussets/flange 14.677 at (97.5, 36.45, -298.8)", "PASS_ASSUMED", "envelope, clearance", ["A-04"]),
 g("REQ-05", None, "bool", "Soft: holds against a firm hand pull and does not turn; bench, INCONCLUSIVE with a risk rating", None, None, "INCONCLUSIVE", "bench (not geometric)", ["A-05"]),
]
census = [
 dict(feature="F02 flange", expected="convex cylinder r 10.0, z -304..-302; bed and wall faces", found="cylinder r 10.000 z -304.000..-302.000; planes z -304.000, -302.000", status="PASS"),
 dict(feature="F03 neck", expected="convex cylinder r 5.65 (spec 1.1), z -302..-298.8", found="cylinder r 5.650 z -302.000..-298.800; step plane z -298.800", status="PASS"),
 dict(feature="F04 tie groove", expected="convex cylinder r 5.15, 5.2 wide", found="cylinder r 5.150 z -298.800..-293.600", status="PASS"),
 dict(feature="F05 collar flank", expected="cone 60 deg from horizontal, r 5.15->5.65", found="cone semi-angle 30.000 (60.000 from horizontal) z -293.600..-292.734", status="PASS"),
 dict(feature="F06 collar", expected="convex cylinder r 5.65 to z -291.0, top plane", found="cylinder r 5.650 z -292.734..-291.000; plane z -291.000", status="PASS"),
 dict(feature="F07 bore", expected="1 concave cylinder r 3.5 (half-bore, 0 bores)", found="concave cylinder r 3.500 z -303.5..-291.5; bore_census 0", status="PASS"),
 dict(feature="F08 inside bore chamfer", expected="cone 0.5 x 45", found="cone 45.000, r 3.5->4.0 over z -291.5..-291.0", status="PASS"),
 dict(feature="F09 outside bore chamfer", expected="cone 0.50 axial x 0.29 radial", found="cone semi 30.11, r 3.79->3.5 over z -304.0..-303.5", status="PASS"),
 dict(feature="F11 split face", expected="1 plane at y 30.40 in 2 faces", found="2 planar faces, normal +Y, y 30.400", status="PASS"),
]
plaus = [
 dict(question="P1 gravity", answer="Flange bears on the wall's outer face (0.000) and the tie sits inside, so the grommet holds in any orientation; it prints standing on the flat flange face.", status="YES"),
 dict(question="P2 function chains", answer="The cord runs straight through the bore on the measured hole axis, 2.50 from the hole wall, with nothing across its path (sections x 95, z -296.6).", status="YES"),
 dict(question="P3 moving parts", answer="Insertion swept together with closing (41 dz poses x 3 closings): 0 mm3 against OD-C11 and OD-C01, least gap 0.350; closed halves touch at 0 mm3.", status="YES"),
 dict(question="P4 human factors", answer="Halves go round the cord and push in along +Z until the flange stops them; the tie head sits at +Y, 14.7 clear of the gusset and reachable from inside.", status="YES"),
 dict(question="P5 comparable product", answer="It reads as an ordinary split strain-relief bushing with a cable tie: 20 mm flange, 13 mm long, for a 7 mm cord.", status="YES"),
 dict(question="P6 floating/embedded/mirrored/upside-down", answer="All contacts 0.000 with 0 mm3; the copy is my own 180 deg rotation (not a mirror); the flange is outside and the collar inside.", status="YES"),
]
controls = [
 ("validity", "collar-top face removed (open shell): naked_edges 4"),
 ("envelope", "flange resized to 21.2 dia: size_x 21.185"),
 ("feature_census", "tie groove filled to 11.3 dia: cylinder faces 4"),
 ("bore_census", "3 dia through-hole in the flange at (95, 37.5): bores 1"),
 ("radial_profile", "bore radius 3.50 -> 3.60: max 3.600"),
 ("radial_extent", "bore r 3.60: closed-pose squeeze 0.300"),
 ("min_wall", "groove floor thinned to 1.40 (9.8 dia): 1.400"),
 ("min_wall_wide", "same mutant, 45 deg reading: 1.400"),
 ("overhang_census", "flat ledge ring on the collar top to 15 dia: 0.0 deg"),
 ("flat_ceiling_spans", "11 mm bridge on two posts above the flange: 9.0"),
 ("clearance", "half moved 0.5 along +X: neck to hole 0.000"),
 ("interference", "half moved 0.5 along +X: 1.194 mm3 into OD-C11"),
 ("common_volume", "same relocated half against OD-C11: 1.194 mm3"),
 ("mesh_sagitta", "STL written at 0.1 mm / 0.5 rad: 0.0457"),
 ("mesh_deviation", "same coarse STL against the B-rep: 0.0457"),
 ("mesh_census", "delivered STL with 10 triangles removed: naked edges 12"),
 ("compare_step", "bore r 3.60 solid against the delivered STEP: volume delta 12.56 mm3"),
]
findings = [
 dict(id="F1", gate="REQ-05", kind="SOFT_GATE_MISS", measured=None, unit="bool", required="Soft: holds against a firm hand pull and does not turn in the hole (bench)", margin=None, at=None, blocks=False, risk="MEDIUM",
      risk_basis="Grip and anti-rotation rest only on the tie closing stiff PLA halves by 0.400 per side (A-03, A-05); a round 11.3 neck in the 12.0 hole has nothing keyed against turning.",
      fix_direction="Answer by the first fitting (pull and twist test); if it slips or turns, cut the halves further from the axis or add a key to the neck, or print in TPU as the BOM says."),
 dict(id="F2", gate="D-01b", kind="OBSERVATION", measured=1.575, unit="mm", required=">= 1.6", margin=-0.025, at="groove floor, combined REQ tolerance corner (groove 10.25 dia, bore r 3.55); delivered part reads 1.650", blocks=False, risk="LOW",
      risk_basis="The delivered nominal wall is 1.650 (margin +0.05); only the combined corner of REQ-01 and REQ-02, which the one-at-a-time sweep did not build, would give 1.575, and the spec's D-01b basis states 1.60 at that corner.",
      fix_direction="Correct the D-01b basis arithmetic in the spec, or tighten the groove or bore tolerance so the combined corner holds 1.60; no geometry change needed for this build."),
]
least = [
 dict(item="1. Axial play band 0.20 +/- 0.05 tighter than REQ-01's +/- 0.1", answer="Spec 1.2 sets 0.20 +/- 0.10. I measure 0.200 (tie and head to the inner face); the REPORT's neck_len ends at 0.100 and 0.300 now sit on the band edges and pass. Resolved."),
 dict(item="2. Rigid cord contact and closed pose against bore and split tolerances; D-01b 1.600 at bore high", answer="Spec 1.2 sizes the cord on the measured bore (r 3.500, tangent 0.000) and moves each half by its measured split offset (0.400 / 0.400): halves touch at 0 mm3, squeeze 0.400. At the REPORT's sweep ends the squeeze equals the split offset, 0.38 to 0.42, inside 0.40 +/- 0.07. The D-01b corner is F2 (1.575 at the combined corner, not built)."),
 dict(item="3. REQ-05 and A-03: grip, anti-rotation, PLA at the 1.65 groove wall", answer="Geometry cannot answer this. The groove wall measures 1.650 and nothing keys the neck against turning, so F1 stays MEDIUM until the first fitting."),
]
doc = dict(schema="oguz-verdict-v1", review_id="RV01", job_id="20261002-od-c14-cord-grommet", target="od_c14_grommet_v01", spec_version="1.2",
  reviewer=dict(runtime="claude-code", model="claude-opus-5-5"), verdict="APPROVED_ASSUMPTION_CONDITIONAL",
  summary="Half re-measured from its STEP: one valid solid 19.984 x 9.600 x 13.000; at the open pose the neck clears the hole by 0.350, the halves are 0.800 apart and the tie sits 0.200 off the wall; at the closed pose the squeeze is 0.400; the insertion path reads 0 mm3; least wall 1.650; least overhang 59.886 deg; all 17 positive controls FAIL; no blocking finding; passes rest on A-01 to A-07.",
  files=[dict(path=p, sha256=h, matches_report=True) for p, h in [
   ("02_STEP_STL/od_c14_grommet_half_C1_v01.step", "55ce2a3e6a68458e6f97f26a58b05d4691bd69f310105551f98b28fcdb0a0680"),
   ("02_STEP_STL/od_c14_grommet_half_C1_v01.stl", "645a8dde3b824729be2fe225589561b529c879c2bf9fbb5b10d927f102eafaa8"),
   ("02_STEP_STL/od_c14_assembly_C1_v01.step", "a21a8f9d88d7f1ec8a97103c980ec2f16a798c9376a0d124be1c3b3b8a8b992b")]],
  gates=gates, feature_census=census, plausibility=plaus,
  positive_controls=[dict(check=c, mutant=m, got="FAIL") for c, m in controls],
  findings=findings, least_sure_answers=least,
  assumptions_relied_on=["A-01", "A-02", "A-03", "A-04", "A-05", "A-06", "A-07"])
json.dump(doc, open(J, "w"), indent=1, ensure_ascii=False)
import jsonschema
jsonschema.validate(doc, json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json")))
print("valid")
