# RV01 — od_side_panels_v01 (20261002-od-c12-c13-c16-side-panels) — 2026-10-03 UTC

Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with the answers of `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_side_panels_v01.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-05, A-07, A-09, A-10, A-11, A-12, A-14

Method: every row re-measured with my own calls to `tools/measure` and `tools/core` on the exported STEP and STL, read back from file; my own check assembly built from the three part files and the eight inputs at the spec 1.2 §2 poses (not from the designer's assembly file); bands from GATES §0 (0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts). No designer script or result was read. Work scripts, results and sections: `reviews/RV01_work/` (r00…r09, `*.json`, `sections/`).

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c13_right_C1_v01.step` | bb029af485a12941c364302b8a2f98c5b9c2436f73aea68e66bb8ed69be11a71 | yes |
| `02_STEP_STL/od_c13_right_C1_v01.stl` | 50beff9b3ddbc572d9020309e4c5e758830331a360c52d55ae1ca117d0dccf88 | yes |
| `02_STEP_STL/od_c12_left_C1_v01.step` | 972343ab6af3684acf9000208761baa390e489cabe30d238c62ffa36e62f8408 | yes |
| `02_STEP_STL/od_c12_left_C1_v01.stl` | 872489a1afefcb39e725b3339595770184b17368deab05e7e9f1eaca66ee5d55 | yes |
| `02_STEP_STL/od_c16_bracket_C1_v01.step` | 39faff6ce71326fc8d562d8c3daa42cd938fdf24f4dbe0933d82e9cae569c9fc | yes |
| `02_STEP_STL/od_c16_bracket_C1_v01.stl` | 0519dcb42e099fdc6433cc371989b0806ac74bd2e77aa7c43d3891c5ac6f19d5 | yes |

Also hash-checked against the brief and used: `01_CAD/REPORT_od_side_panels_v01.md` (6b4597a7…b243b112), `01_CAD/DESIGN_PLAN.md` (83911646…1c1498), `00_Spec/DESIGN_SPEC.md` 1.2 (72b8690c…f7c16), and the eight input STEPs (all match the brief). The designer's assembly file `od_side_assembly_C1_v01.step` (aee5a943…a58b7) is present and was not used for any row. The delivery must carry exactly the six files above.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 bool | solid_count = 1, brep_valid = 1, naked_edges = 0, each part file | 0 | OD-C13, OD-C12, OD-C16 files each: 1 solid, brep_valid 1, naked edges 0 | PASS | `validity` | — |
| U-02 | 218.8105 mm | each size in [spec - 0.1, spec + 0.1] | 0.0995 | OD-C13 and OD-C12 size_y 218.8105 (spec 218.81); OD-C13 10.000 x 218.8105 x 385.000 at x 110..120, y 0..218.8105, z -295..+90; OD-C12 the same at x -120..-110; OD-C16 19.000 x 16.000 x 16.000 at x -19..0, y 0..16, z -8..+8 (margin 0.100) | PASS | `envelope` | — |
| U-03 | 0.4 mm | (a) designed contacts clearance = 0, interference <= 0; lip to OD-C10 0.40 +- 0.05; other pairs clearance >= 0.5; coaxiality <= 0.20; (b) path interference <= 0 mm3 | 0.05 | governing: lip to OD-C10 skirt 0.4000 at (+-116.6, 215.0, -280.0) both panels; 16 designed contacts clearance 0.000 and interference 0.000 mm3; 100 other pairs least 0.900 (OD-C12 to OD-C07, margin +0.400), then 3.000 (panels to OD-C11), 5.000 (OD-C13 to OD-C08); 116 pairs interference 0.000 mm3; six insert-bore to panel-hole axis offsets 0.000 (<= 0.20, margin +0.200); (b) six brackets down from +20, two panels in from 20 outside, OD-C10 down from +40, steps 1.0: 0.000 mm3 at every step | PASS (assumed: A-01, A-02, A-03, A-04, A-05) | `clearance, interference (common_volume), locate_bore; own path stepper` | A-01, A-02, A-03, A-04, A-05 |
| U-04 | 5.82e-11 mm3 | named body re-read unchanged, no stray shells, valid after re-import | -5.82e-11 | each part file: AP242, unit MM, label kept (od_c13_right, od_c12_left, od_c16_bracket), 1 solid, faces delta 0, valid after; volume delta <= 5.8e-11 mm3 (band 0.001) | PASS | `step_roundtrip, compare_step` | — |
| U-05 | 3 count | per spec 1.2 and the plan as amended: OD-C13 11 planes / 3 concave cylinders / 3 bores; OD-C12 15 / 3 / 3; OD-C16 8 / 3 / 3 | 0 | OD-C13 11/3/3, OD-C12 15/3/3, OD-C16 8/3/3; every plan feature located (section 3) | PASS | `feature_census, bore_census, locate_bore` | — |
| U-06 | 2.1 mm | >= 2.0 (min_wall wide, 45 deg) | 0.1 | OD-C12 wall at the relief (-120.0, 54.6, -29.5); OD-C13 3.000, OD-C16 3.000 | PASS | `min_wall detail wide (spacing 0.6 panels, 0.4 bracket)` | — |
| U-07 | 0.004993 mm | STL tol 0.01, angular <= 4 acos(1 - 0.01/R_max); stl_max_sagitta <= 0.01 | 0.005007 | delivered STLs: deviation 0.004993 (both panels, R_max 1.7, angular limit 0.434074 rad), 0.004988 (bracket, R_max 3.25, limit 0.313866 rad); one closed shell, winding 1, volume > 0; triangle counts 536 / 552 / 588 equal to a fresh mesh at those settings | PASS | `mesh_deviation, mesh_census, write_stl (fresh, for comparison)` | — |
| U-08 | — | applies to threaded parts; these targets have none | — | no threads modelled on any part | N/A: by its row | `N/A by its row` | — |
| D-01a | 2.1 mm | >= 0.8 | 1.3 | OD-C12 relief wall (-120.0, 54.6, -29.5); OD-C13 3.000; OD-C16 3.000 (counterbore floor) | PASS | `min_wall` | — |
| D-01b | 2.1 mm | >= 2.0 | 0.1 | OD-C12 relief wall (-120.0, 54.6, -29.5); OD-C13 3.000 (wall); OD-C16 3.000 at (-13.40, 3.0, -3.07), counterbore floor | PASS | `min_wall` | — |
| D-02 | 385 mm | panels <= Kobra Max 3 (A-09: 420 x 420 x 500) lying on the outer face; bracket <= K1C (A-10: 220 x 220 x 250) | 35 | panels 385.0 x 218.81 on the bed, 10.0 tall; bracket 19 x 16 x 16 (margin 201.0) | PASS (assumed: A-09, A-10) | `envelope` | A-09, A-10 |
| D-03a | 60 deg | >= 45 from horizontal in the sec. 4 print orientation; bracket insert-bore crown excluded (named exception) | 15 | OD-C13 build -X and OD-C12 build +X: least 60.000 on the lip slope (116.6, 215.0, 80.0); OD-C16 build +Y outside the exception 90.000 (nothing downward); exception: crown 0.000 at (-6.0, 12.0, 0.0) | PASS (assumed: A-11) | `overhang_census (spacing 0.6 panels, 0.5 bracket)` | A-11 |
| D-03b | 4 mm | span <= 5 | 1 | OD-C16 insert-bore crown Ø4.000 at (-3, 12, 0), from own sections x -3 and z 0.3; flat ceilings 0.000 on all three parts | PASS (assumed: A-11) | `own sections; flat_ceiling_spans corroborates` | A-11 |
| D-04a | 3.4 mm | >= 3.25 | 0.15 | six panel holes Ø3.400 along X at (+-118.5, 10, -262/-15/+62); bracket hole Ø3.400 along Y at (-12.5, 1.5, 0) | PASS | `bore_census, locate_bore` | — |
| D-04d | 0.4 mm | >= 0.30 per side | 0.1 | lip toe (+-116.6, 215.0) to OD-C10 skirt inner face x +-117.0, both panels | PASS (assumed: A-02, A-14) | `clearance` | A-02, A-14 |
| D-05a | 12 mm | >= 8.0 across around the insert bore | 4 | least outer radius 6.000 toward the top face (y 16) about the bore axis (0, 10, 0) along -X, 24 angles x 24 levels over x 0..-6 | PASS (assumed: A-12) | `radial_profile, bore_census` | A-12 |
| D-05b | 4 mm | Ø4.0 +- 0.05, depth 6.0 +- 0.1 (>= 5.7) | 0.05 | insert bore Ø4.000, length 6.000, open at x 0, closed (flat floor) at x -6.0, axis (y 10, z 0) | PASS (assumed: A-12) | `bore_census, locate_bore` | A-12 |
| D-06a | 2.1 mm | >= 1.0 | 1.1 | least wall OD-C12 relief 2.100; lip wedge apex edge read from sections (finding F2) | PASS | `min_wall; own sections` | — |
| D-07 | — | none: the insert bore is formed by the insert, the rest are clearance holes | — | no fit-critical bore on these parts | N/A: by its row | `N/A by its row` | — |
| J-05 | 3.25 mm | >= 3.0 around the bracket's insert bore | 0.25 | web from the bore floor (x -6) to the counterbore wall (x -9.25), exact face distance; to top face 4.000, sides 6.000, underside 8.000; global min_wall 3.000 (counterbore floor, not around this bore) | PASS | `exact face-to-face distance (BRepExtrema) from the bore faces; min_wall beside it` | — |
| E-06 | 1 count | bracket one solid block; lip tied into rail, rail into wall | 0 | each part one solid; sections z -100 and z +60 (both panels) one closed region through wall, rail and lip; bracket section z 0.3 one region | PASS | `validity, own sections` | — |
| REQ-01 | 215 mm | outer x +-120.00 +- 0.10, inner +-117.00 +- 0.10; underside y 0.00 +- 0.05; top y 215.00 +- 0.05 over x +-(116.6..120); ends z -295.00 / +90.00 +- 0.10; footprint over plate | 0.05 | sections y 50 and y 200: outer 120.000, inner 117.000 over z -295..+90 (OD-C12 inner face at the relief left to REQ-04); one underside plane y 0.000; one top face y 215.000 over x 116.6..120; ends -295.000 / +90.000; footprint prism 6930.0 / 6222.6 mm3 all inside OD-C01 | PASS (assumed: A-01) | `envelope of faces, own sections, common_volume` | A-01 |
| REQ-02 | 0.4 mm | wedge (+-110, 215), (+-116.6, 215), (+-110, 218.81) +- 0.1; slope 60 +- 1 deg; z -280..+80 +- 0.1; clearance to OD-C10 0.40 +- 0.05 | 0.05 | sections z -100 and +60, both panels: vertices (+-110.000, 215.000), (+-116.600, 215.000), (+-110.000, 218.8105); slope 60.0001 deg from the panel plane; z -280.000..+80.000; gap 0.4000 | PASS (assumed: A-02, A-14) | `own sections, envelope, clearance` | A-02, A-14 |
| REQ-03 | 0 mm | three Ø3.4 +- 0.1 through along X at (y 10, z -262/-15/+62), offset <= 0.10 | 0.1 | both panels: Ø3.400, offset 0.000, through, length 3.0 | PASS (assumed: A-07) | `bore_census, locate_bore` | A-07 |
| REQ-04 | -117.9 mm | inner face x -117.90 +- 0.05 over y 0..55, z -160..-29 (+- 0.1); clearance(OD-C12, OD-C07) >= 0.5 | 0.05 | relief floor one plane x -117.900, y 0.000..55.000, z -160.000..-29.000; clearance to OD-C07 0.900 (margin +0.400) | PASS (assumed: A-04) | `envelope of the floor face, own sections, clearance` | A-04 |
| REQ-05 | 3 mm | block 19 x 16 x 16; Ø3.4 through along Y at (-12.5, 0) offset <= 0.10; Ø6.5 +- 0.1 counterbore floor y 3.00 +- 0.10; Ø4.0 bore along -X at (y 10, z 0) offset <= 0.10; plate holes at (+-104.5, z_c) +- 0.10 | 0.1 | counterbore Ø6.500 floor y 3.000; hole Ø3.400 offset 0.000 through; insert bore offset 0.000; six placed plate holes at (+-104.5, z_c) offset 0.000 | PASS (assumed: A-01, A-07) | `bore_census, locate_bore, envelope` | A-01, A-07 |
| REQ-06 | 15.5 mm | >= 8.0 to the plate edge; >= 6.0 to every OD-C01 hole and handed-over insert; plate solid in a Ø8 circle | 7.5 | all six (+-104.5, z_c): edge 15.500; nearest OD-C01 bore 28.306 ((-113, -42) Ø4.0); nearest handed-over insert 22.142 ((+-95, -282)); Ø8 x 6 disc 301.593 of 301.593 mm3 in OD-C01 | PASS (assumed: A-01) | `bore_census of OD-C01, own distance arithmetic, common_volume` | A-01 |
| REQ-07 | 0 mm3 | interference = 0 of the foot keep-outs, the driver-access and the panel-screw access cylinders | 0 | 4 keep-outs x 8 new parts, 6 driver cylinders (r 4, y 16..215) x 16 solids, 6 panel-screw cylinders (r 4, 20 outside) x 19 solids: all 0.000 mm3 | PASS (assumed: A-05) | `common_volume` | A-05 |
| REQ-08 | — | Soft: no visible flex or drumming with the lid on; a hand on a side does not shift the lid (bench) | — | not geometric; answered by the first print (finding F1) | INCONCLUSIVE (Soft, bench) | `bench (none in CAD)` | A-13 |

Notes on the table:

- Each row is one §5 row across the three part files and the assembly; the governing value (smallest margin) is in Measured and the other readings in At.
- Panels were sampled at 0.6 mm (`min_wall`, `overhang_census`, `flat_ceiling_spans`): at 0.4 / 0.5 the toolkit refuses the 385 × 215 face as undersampled and names 0.58 as the spacing that fits; at 1.0 (`min_wall`) the readings were the same (3.000 / 2.100).
- D-03a on the bracket: `overhang_census(build_dir=(0,1,0))` on the part as exported reads 0.000° at (−6.0, 12.0, 0.0), the crown of the Ø4.0 insert bore, which is the named exception (Usta U-18). Excluded by position (the bore filled back for the reading), the least is 90.000°: nothing else faces down. The crown bridges 4.0 (D-03b, within 5).
- U-03 (b) used 1.0 steps (≤ 2.0): 6 × 21 bracket poses against every input and the brackets already seated, 2 × 21 panel poses against the inputs (lid off) and the six brackets, 41 lid poses against everything.
- U-07: the delivered STLs are not byte-equal to a fresh mesh of the re-imported STEP at the REPORT's settings (triangle order differs; on OD-C12 the hole tessellation too), but the triangle counts agree (536 / 552 / 588) and the measured deviation of each delivered mesh is ≤ 0.004993 against 0.01; mesh boxes within 4.6e-6 of the B-rep (float32), volumes within 0.33 mm³ (chords inside the holes) (V-05).

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| OD-C13 F01-F02 wall with 2 square end faces | faces x 117 and x 120 over y 0..215, z -295..+90; ends z -295 and z +90 | found: one inner face x 117.000, one outer x 120.000, underside y 0, ends z -295.000 and +90.000 | PASS |
| OD-C13 F03 top rail | x 110..117, y 205..215, z -280..+80 | underside y 205.000 over x 110..117, z -280..+80; ends at z -280.000 / +80.000 | PASS |
| OD-C13 F04 lip wedge (one 60 deg face) | triangle (110, 215), (116.6, 215), (110, 218.81), z -280..+80 | one sloped plane, normal (0.5, 0.866, 0), x 110..116.6, y 215..218.8105; 60.0001 deg | PASS |
| OD-C13 F05 merged faces | 11 planes, 3 cylinders | 11 planes, 3 concave cylinders, 0 other | PASS |
| OD-C13 F06 holes x3 | Ø3.4 through along X at (y 10, z -262/-15/+62) | 3 bores Ø3.400 x 117..120, through, offset 0.000 | PASS |
| OD-C12 F11-F12 mirrored panel | mirror of OD-C13 at x -120..-110 | same faces mirrored; slope normal (-0.5, 0.866, 0); 3 bores Ø3.400 through | PASS |
| OD-C12 F13 relief | floor x -117.9, y 0..55, z -160..-29, 4 faces | floor plane x -117.900, y 0..55, z -160..-29; faces y 55, z -160, z -29; 15 planes | PASS |
| OD-C16 F21 block | x -19..0, y 0..16, z -8..+8 | 19.000 x 16.000 x 16.000 at that position; 8 planes, 3 cylinders | PASS |
| OD-C16 F22 plate-screw hole | Ø3.4 through along Y at (x -12.5, z 0) | Ø3.400 y 0..3, through, offset 0.000 | PASS |
| OD-C16 F23 counterbore | Ø6.5 from y 16 to floor y 3 | Ø6.500 y 3..16, open at y 16, closed at y 3.000 | PASS |
| OD-C16 F24 insert bore | Ø4.0 x 6.0 blind along -X from x 0 at (y 10, z 0) | Ø4.000 x -6..0, open at x 0, flat floor x -6.000, offset 0.000 | PASS |

The plan was written against spec 1.0 (12 / 5 and 16 / 5 face counts with arc ends and a box lip); the expected counts above follow spec 1.1/1.2 §4 and the WP-03 answers (square ends, 60° wedge on a 7 × 10 rail), derived by me from the spec geometry: wall 6 faces, rail underside and two shared end faces, the shared x 110 face, the slope (11); the relief adds four (15).

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | gravity | Panels stand on the plate top and the brackets on the plate (clearance 0.000, interference 0.000); the lid's side skirts rest on the panel tops at y 215; nothing hangs on a screw alone. | YES |
| P2 | function chains | No air, liquid, drive or cable passes through the new parts; the panels close the sides 5.000 from the electronics tray and 3.000 from OD-C11, whose vents stay the bay's exhaust. | YES |
| P3 | moving parts | No moving parts; every assembly path (brackets down, panels in, lid down) reads 0.000 mm3 at every 1.0 step. | YES |
| P4 | grip, reach, insertion | Bracket screws driven from above along a clear r 4 axis (panels and lid off); panel screws from outside along X with 20 clear; panels offered inward onto the brackets; lid lowered last; the order of spec sec. 4 is the only one that fits. | YES |
| P5 | nothing absurd | A 3 mm printed side wall with a top rail and a 60 deg locating lip on three corner brackets is ordinary printed-enclosure practice; the proud button heads and the rear-corner slit are ledgered (A-07, A-03). | YES |
| P6 | floating, embedded, mirrored, upside-down | Every designed contact reads 0.000 with no interference; the left panel is a true mirror with its relief on the inner face over OD-C07; the lips point up inside the skirts; the left brackets face their insert bores at x -117. | YES |

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity (solid_count) | bracket with a second solid beside it | FAIL |
| envelope | OD-C13 wall lengthened 0.5 at z +90 | FAIL |
| step_roundtrip/compare_step | bracket insert bore 0.5 deeper vs the delivered file | FAIL |
| feature_census (bores) | OD-C13 middle hole filled | FAIL |
| locate_bore (offset) | OD-C13 middle hole moved 0.5 in z | FAIL |
| bore_census/locate_bore (diameter) | bracket plate hole resized to 3.2 | FAIL |
| coaxiality (locate_bore x2) | OD-C13 middle hole moved 0.5 vs placed bracket R2 | FAIL |
| min_wall | OD-C12 relief floor moved to -118.5 (wall 1.5) | FAIL |
| J-05 exact face distance | bracket insert bore 7.0 deep (web to counterbore 2.25) | FAIL |
| overhang_census | OD-C13 block x110..113 hung under the rail (print -X) | FAIL |
| flat_ceiling_spans | same block: its x 113 face a 10 deep ceiling | FAIL |
| overhang_census (bracket, exception filled) | bracket with a 3 x 4 ledge off its outer face | FAIL |
| clearance (lip, D-04d) | OD-C13 relocated +0.2 in x | FAIL |
| clearance (designed contact) | OD-C13 relocated +0.2 in x vs bracket R2 | FAIL |
| clearance (other pairs) | OD-C12 relocated 0.5 inward vs OD-C07 | FAIL |
| interference/common_volume | bracket R2 relocated 0.5 down into OD-C01 | FAIL |
| assembly path stepper | lid lowered over OD-C13 relocated +0.5 in x | FAIL |
| interference (REQ-07 access) | bracket R2 with a 2 tall boss over its screw | FAIL |
| radial_profile | bracket top lowered to y 13 | FAIL |
| section wedge reading | OD-C13 lip with a bump raising its top at z -100 | FAIL |
| mesh_deviation | bracket STL at tol 0.1, 1.0 rad | FAIL |
| mesh_census (naked edges) | delivered bracket STL with one triangle removed | FAIL |
| REQ-06 distance arithmetic | insert position moved to (114, -15) | FAIL |
| E-06 one solid (validity + section) | OD-C13 lip lifted 0.5 off the rail | FAIL |

Every control was made from the exported STEP by my own script (`RV01_work/r06_controls.py`, results `controls.json`) and gated with the same comparison and band as the review. All FAIL, so no gate rests on a check that could not fail.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-08 | SOFT_GATE_MISS | not measured (bench) → Soft: no visible flex or drumming with the lid on; a hand on a side does not shift the lid | — | both panels, the free wall between brackets (z -262 to -15, 247 mm) under the lid | no | MEDIUM | a 3.0 PLA plate 385 x 215, held at three points along its foot and along its top only by the 0.40-gap lip in the skirt, may drum or bow between brackets; no calculation exists (A-13) | answer on the first print with a hand-load and tap test; if it drums, add a fourth bracket or a stiffening rib on the inner face clear of OD-C07 and OD-C08 |
| F2 | D-06a | OBSERVATION | 60 deg (apex included angle) → minimum feature >= 1.0 (min_wall); the lip wedge as spec sec. 4 defines it | — | lip apex edge (+-110.000, 218.8105) over z -280..+80, both panels | no | LOW | the spec's wedge ends in a 60 deg convex edge that min_wall cannot read (flank normals 120 deg apart); material normal to the slope is under 1.0 only within 1.155 of the edge; in the flat print the edge lies in the top layer and every layer of the lip is wider than the one below, and it carries no load (the skirt bears on y 215) | none needed for function; if a crisp edge is unwanted, a 0.5 flat or round on the apex in a later spec revision |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 9.1 coaxiality tolerance stack | Under spec 1.2 (offset <= 0.20) the stack cannot fail: with REQ-03 and REQ-05 each <= 0.10, two parallel axes are at most 0.20 apart, so the opposed extreme sits at zero margin and passes within the band; as built all six axis offsets measure 0.000 and the plate holes 0.000 from (+-104.5, z_c). No finding. |
| 9.2 lip gap | Measured 0.4000 on both panels from the wedge to OD-C10 as delivered (skirt inner faces at x +-117.000); lowering OD-C10 from +40 in 1.0 steps over panels and brackets reads 0.000 mm3 at every step; a +0.5 relocated panel makes the same stepper fail (1.04 mm3). The physical lid still rests on A-02 and A-14. |
| 9.3 lip apex not reached by min_wall | Read from my own sections at z -100 and z +60 on both panels: apex (+-110.000, 218.8105), toe (+-116.600, 215.000), slope 60.0001 deg from the panel plane (60 +- 1), included angle 60 deg; min_wall at 0.6 spacing reads 3.000 / 2.100 elsewhere and does not see the edge by design (flanks 120 deg apart). Rated as F2, LOW, non-blocking. |
