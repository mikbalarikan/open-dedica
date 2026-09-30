# RV02 — od_c03_cradle_v02 (20260930-od-c03-pump-cradle) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with the WP-03 and WP-05 amendments) · report `01_CAD/REPORT_od_c03_cradle_v02.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-03, A-06, A-07, A-10, A-11, A-13

od_c03_cradle_v02: one valid solid 80.000 x 40.000 x 52.000 mm; every Hard section 5 row PASS or PASS (assumed); REQ-03 2.300 mm at the -X post, REQ-04 saddle contact 6.9e-13 mm with 0.0 mm3 on both ribs, OD-H01 centroid z 7.232 inside the saddle span z -3..31 (RV01 F2 answered); REQ-09 Soft bench INCONCLUSIVE; 24 of 24 positive controls FAIL; no blocking finding.

Method: every row re-measured with `tools.measure` / `tools.core` on the delivered STEP files, re-imported (`reviews/RV02_work/checks.py`, `run_gates.py`, `m1`…`m6`), compared through `tools.result.gate` with the GATES.md §0 bands (0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts). No designer script, sweep file or check JSON value was used as evidence. OD-H01 read sound (1/1/0).

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `01_CAD/REPORT_od_c03_cradle_v02.md` | 3404a729616141242016ad439668c65a1960cbe6f99f2a449e5a903848d93a85 | yes (brief; the REPORT does not list its own or the plan's hash) |
| `01_CAD/DESIGN_PLAN.md` | 7e86466421a4ad81e87dd87bb93215966e3a0b974e33869163b55aaa42bd6540 | yes (brief; the REPORT does not list its own or the plan's hash) |
| `01_CAD/check_od_c03_cradle_v02.json` | 915202548c8c46c3b2f9adc0103ab2a63f915384913fd9fecf131d8b83373921 | yes |
| `01_CAD/sections_od_c03_cradle_v02.json` | 50193e6b41dfdbea8d7d5c3ddeb9642399d2836d3821802b58ecb37b45e3d007 | yes |
| `02_STEP_STL/od_c03_assembly_C1_v02.step` | 8e1a6ea8ff66acecdd2cffdde41c1d7635541f4b34e9034f55ce6c4efaf43a14 | yes |
| `02_STEP_STL/od_c03_cradle_C1_v02.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | yes |
| `02_STEP_STL/od_c03_cradle_C1_v02.stl` | 529a0cc2033cddb00ee16715448a8e0e546f08eb05eb6bd1e6c20ce8a3776be4 | yes |
| `03_Sections/od_c03_cradle_v02_assembly_xy_z0p0.png` | e36596521f8a6c8d0cca5d8bcddc8c58cf6708fc2192c48223fe1fc9379b7b24 | yes |
| `03_Sections/od_c03_cradle_v02_assembly_xy_z28p0.png` | 4e58b33781602ce7e7833dbfa77a0f16055c3ba4fd5c22052b318775e65b2083 | yes |
| `03_Sections/od_c03_cradle_v02_assembly_yz_x0p0.png` | 86a77ec2317d2f64fdfc5878ebac31b9492b3dd6837bcd53db906ae3348123cf | yes |
| `03_Sections/od_c03_cradle_v02_xy_z0p0.png` | 51dc7f09bbf3b3e95a6b6623decb2430445b9504e50ab4a9decb1f602895faa7 | yes |
| `03_Sections/od_c03_cradle_v02_xy_z17p0.png` | 603139490d9c8a947e45d2f8aeb257b0a6ecad102d47e89d3987367439825df3 | yes |
| `03_Sections/od_c03_cradle_v02_xy_z28p0.png` | 4364ee45b5b8a12674cf4f0d509e7dd901cde4352e25421d9acff4333d056502 | yes |
| `03_Sections/od_c03_cradle_v02_xz_y38p5.png` | 8ad305e86b536a0132bfac697ec2d0f56694afd3187a5fe40e7332ff48a602cc | yes |
| `03_Sections/od_c03_cradle_v02_xz_y7p0.png` | 1f44f2bbdb0390b6380bf0f7b29e18f4b0a10364e5ee45ef2899a237491ee3c5 | yes |
| `03_Sections/od_c03_cradle_v02_yz_x0p0.png` | 3f1dbbc197ea6daef045738ba8ad42f889c5aa3f93ad38d2eb65a687163d7328 | yes |
| `03_Sections/od_c03_cradle_v02_yz_x31p5.png` | 1f75434f7b2887c7321dbc50545af88d24e5f705f7e0d5fdc7a233177a588504 | yes |
| `03_Sections/od_c03_cradle_v02_yz_x34p0.png` | 577bc611c4691e5ddcc7118f907404b2a8eee2303356ef7c6fc4dbfbd73e1fd5 | yes |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | yes (brief and REPORT §1) |

Completeness: every §5 row is answered in the REPORT and every listed file is present with a matching SHA-256. The delivered STL is byte-identical to a fresh `write_stl` of the delivered STEP at 0.01 mm / 0.1 rad (SHA-256 529a0cc2…6be4).

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 count | solid_count = 1, brep_valid = 1, naked_edges = 0 | +0 | part file: solid_count 1, brep_valid 1, naked_edges 0; assembly: cradle 1/1/0, OD-H01 1/1/0, sleeve 2 solids valid, 0 naked | PASS | `validity` | — |
| U-02 | 80 mm | 80.0 x 40.0 x 52.0 each in [spec - 0.1, spec + 0.1]; position reported apart | +0.1 | size 80.000 x 40.000 x 52.000 (all margin +0.100); position x -40.000..40.000, y 0.000..40.000, z -10.000..42.000 (exact) | PASS | `envelope` | — |
| U-03 | 6.9e-13 mm | (a) cradle\|OD-H01 clearance >= 2.0 and interference <= 0; cradle\|sleeve clearance = 0 and interference <= 0; (b) no motion variable | -6.9e-13 | governing: cradle\|sleeve contact (-18.844, 18.844, -3.000) saddle arc of rib 1 (rib 2 also 6.9e-13), interference 0.0 mm3; cradle\|OD-H01 2.300 at (-29.500, 0.000, 33.000) -X post to -X side plate (-27.200, 0.000, 33.000), interference 0.0 mm3; (b) none; insertion path along +Y from 60 mm keeps >= 2.300 and 0.0 mm3 | PASS (assumed: A-01, A-03) | `clearance, interference (tools.core.common_volume)` | A-01, A-03 |
| U-04 | 0 mm3 | named body re-read unchanged, no stray shells, valid after re-import (volume_delta <= 0.001) | +0.001 | part: schema AP242, solids 1, volume_delta 0.0, faces_delta 0, label od_c03_cradle, valid_after 1, 0 free shells/faces; own re-write in RV02_work also 0.0 / 0; assembly: 4 solids, 3 labels unchanged, valid | PASS | `compare_step, step_roundtrip` | — |
| U-05 | 13 count | 2 saddle ribs, 2 post blocks, 4 strap slots, 4 d3.4 through-holes, 1 foot plate (plan as amended) | +0 | 13 of 13 plan features located; faces plane 48, cylinder 6, concave cylinders 6, convex 0, bores 4, other kinds 0 | PASS | `feature_census, bore_census, locate_bore, face positions` | — |
| U-06 | 2 mm | Soft: min_wall wide >= 2.0 | -3.1e-15 | (-33.318, 6.101, 33.000) slot ligament to the post block end face | PASS (Soft) | `min_wall_wide` | — |
| U-07 | 0.00489 mm | STL at tol 0.01, angular <= 4 acos(1 - 0.01/32.0) = 0.1000026 rad; stl_max_sagitta <= 0.01 | +0.00511 | (-18.477, 19.198, 1.500) saddle 1; fresh mesh at 0.01 / 0.1 rad is byte-identical to the delivered STL (2540 triangles); 1 body, 0 naked edges, winding 1; mesh_deviation 0.00489 | PASS | `write_stl, mesh_sagitta, mesh_census, mesh_deviation` | — |
| U-08 | — | applies to threaded parts; this target has none | — | — | N/A: by its row | `N/A by its row` | — |
| D-01a | 2 mm | min_wall >= 0.8 | +1.2 | (-33.318, 6.101, 33.000) slot ligament | PASS | `min_wall` | — |
| D-01b | 2 mm | min_wall >= 2.0 | -3.1e-15 | (-33.318, 6.101, 33.000) slot ligament (all four end ligaments 2.000) | PASS | `min_wall` | — |
| D-02 | 80 mm | each envelope size <= Kobra Max 3 volume foot down (420 x 420 x 500 per A-10) | +340 | 80.0 (X) <= 420, 52.0 (Z) <= 420, 40.0 (Y, vertical) <= 500 | PASS (assumed: A-10) | `envelope` | A-10 |
| D-03a | 45 deg | every downward face >= 45 deg from horizontal, build along -Y | +0 | (-29.500, 5.750, 20.000) slot gable roof; only the eight gable faces face down; sampling bound 0.0 | PASS (assumed: A-13) | `overhang_census(build_dir=(0,-1,0))` | A-13 |
| D-03b | 0 mm | span <= 5 | +5 | no flat downward face off the bed; gable apexes are edges (sections x = +-31.5) | PASS | `planar downward-face census and sections (reviewer)` | — |
| D-04a | 3.4 mm | four frame holes d >= 3.25 | +0.15 | (+-34.0, 37.0..40.0, -4.0) and (+-34.0, 37.0..40.0, 37.0) | PASS | `bore_census, locate_bore` | — |
| D-04c | 2.3 mm | >= 0.5 per side to OD-H01 (REQ-03 raises to 2.0) | +1.8 | (-29.500, 0.000, 33.000) -X post to the -X side plate | PASS (assumed: A-01) | `clearance` | A-01 |
| D-06a | 2 mm | >= 1.0 | +1 | (-33.318, 6.101, 33.000) slot ligament | PASS | `min_wall` | — |
| D-07 | — | the four d3.4 holes are clearance holes, not fit bores: none on this part | — | — | N/A: by its row | `N/A by its row` | — |
| REQ-01 | 26.65 mm | inner radius theta 50..130 step 5, z -2.5..2.5 and 25.5..30.5: min and max in [26.60, 26.70] | +0.05 | min 26.650 at (17.130, 20.415, -2.450), max 26.650 at (-15.286, 21.830, -2.450); window 2 identical; 50 levels x 17 angles each, none unread | PASS (assumed: A-03) | `radial_profile(side=inner, margin=0, z_step=0.1)` | A-03 |
| REQ-02 | 26.65 mm | z 0 and 28: inner <= 26.70 at theta 50 and 130; no material r <= 32.0 at theta 40 and 140; rib faces z -3, 3, 25, 31 +-0.10 | +0.05 | inner 26.650 at theta 50/130, z 0 and 28; theta 40/140 window: NoMaterial at both levels (expected; control FAILs on a lump at r 30); whole ray at z 28 first material 38.510 (post); material starts at theta 45.5, none at 44; rib faces -3.000, 3.000, 25.000, 31.000 (margin 0.100) from section x = 0 | PASS (assumed: A-06) | `radial_extent; YZ section at x = 0` | A-06 |
| REQ-03 | 2.3 mm | clearance(cradle, OD-H01) >= 2.0 at the identity pose | +0.3 | (-29.500, 0.000, 33.000) to (-27.200, 0.000, 33.000) -X side plate; also 2.300 at z 12.0; +X post 2.650; rib 1 and rib 2 2.788 to the coil at (-16.878, 16.868, -3.0 / 25.0); foot 13.250 | PASS (assumed: A-01, A-03) | `clearance (per face)` | A-01, A-03 |
| REQ-04 | 6.9e-13 mm | clearance(cradle, sleeve) = 0 on the saddle arcs; interference <= 0 | -6.9e-13 | (-18.844, 18.844, -3.000) rib 1 arc; rib 1 and rib 2 each 6.9e-13, interference 0.0 mm3; sleeve outer r = cradle inner r = 26.650 at theta 46, 90, 134 | PASS (assumed: A-03) | `clearance, interference` | A-03 |
| REQ-05 | 2 mm | 4 through-slots along X, clear >= 6.0 (Z) x 2.5 (Y), centres y 7.0 +-0.5, z 17.0/28.0 +-0.5, 45 deg gables, ligament >= 2.0 | +0 | all four slots (x +-31.5 sections): clear 6.000 x 2.500 (margin 0.000), centre y 7.000, z 17.000 / 28.000 (margin 0.500), roofs 45.000 deg (margin 0.000), through 4.0 (x 29.5..33.5); ligaments 2.000 at block ends (z 12..14, 31..33), 5.000 between slots | PASS (assumed: A-07, A-13) | `sections at x = +-31.5 and y = 7.0; overhang_census` | A-07, A-13 |
| REQ-06 | 29.5 mm | post inner faces \|x\| = 29.5 +-0.1, spanning z 12.0..33.0 +-0.1; clearance post\|OD-H01 >= 2.0 | +0.1 | inner faces x -29.500 and 29.500, z 12.000..33.000 (margin 0.100); clearance -X 2.300, +X 2.650 | PASS (assumed: A-06) | `planar face envelope, clearance` | A-06 |
| REQ-07 | 3.4 mm | four d3.4 +-0.1 through-holes along Y at (x +-34.0, z -4.0) and (x +-34.0, z 37.0), offset <= 0.10 | +0.1 | all four: d 3.400, axis +Y, offset 0.000, length 3.0, through | PASS (assumed: A-11) | `bore_census, locate_bore` | A-11 |
| REQ-08 | 40 mm | underside y = 40.00 +-0.10 (envelope max_y), 3.0 +-0.1 thick | +0.1 | max_y 40.000; foot top face y 37.000, thickness 3.000 (margin 0.100) | PASS (assumed: A-11) | `envelope; foot top face; section x = 34` | A-11 |
| REQ-09 | — | Soft: no unacceptable vibration to the chassis with the OEM sleeve (bench) | — | not geometric; answered by the first run | INCONCLUSIVE (Soft: bench, non-blocking) | `none (bench gate)` | A-03, A-05 |

U-03 (b): no motion variable (ties not modelled). The assembly path was checked anyway: OD-H01 with the sleeve lowered along +Y from 60 mm above to the final pose keeps ≥ 2.300 mm to the cradle and 0.0 mm³ at every step (−60 … 0 mm), and the sleeve first touches the saddles at the final pose.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 foot plate x1 | 1 plate x +-40, y 37..40, z -10..42 | top face y 37.000, underside y 40.000, x -40..40, z -10..42 | PASS |
| F02 saddle rib 1 with web | arc r 26.65 theta 45..135, z -3..3, web x +-22.627 to the foot | concave cylinder r 26.650 z -3..3, faces z -3.000 / 3.000, web faces x +-22.627 | PASS |
| F03 saddle rib 2 with web | arc r 26.65 theta 45..135, z 25..31 | concave cylinder r 26.650 z 25..31, faces z 25.000 / 31.000 | PASS |
| F04 post blocks x2 | x +-29.5..+-33.5, y 0..37, z 12..33 | 2 blocks, inner faces \|x\| 29.500, outer 33.500, top y 0.000, z 12.000..33.000 | PASS |
| F05 strap slots x4 | 6.0 x 2.5 clear, y 7.0, z 17 / 28, 45 deg gable, through X | 4 slots (2 per block), 6.000 x 2.500, y 7.000, z 17.000 / 28.000, gables 45.000 deg, apex y 2.750, through 4.0 | PASS |
| F06 frame holes x4 | d3.4 through along Y at (+-34, -4) and (+-34, 37) | 4 bores d 3.400, offset 0.000, through, length 3.0 | PASS |
| F07 check assembly | cradle + OD-H01 + od_h02_sleeve_assumed_A03 at identity | 3 labelled bodies; cradle identical to the part file (common volume = 25458.506 mm3); OD-H01 identical to the input (common volume 114903.269 mm3, centroid equal) | PASS |
| Face tally (plan section 6 as re-tallied) | plane 48, cylinder 6 (concave 6), bores 4, no other kinds | plane 48, cylinder 6, concave 6, convex 0, bores 4, cone/sphere/torus/bspline/other 0 | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | Foot on the OD-C01 floor plane y 40 (+Y down); OD-H01 centroid (-0.067, -0.872, 7.232) lies over the saddle span z -3.0..31.0 (10.23 inside rib 1's front face, 23.77 inside rib 2's rear face); load path saddle, web, foot, four M3 screws. | YES |
| P2 | Function chains connected and aimed (air, drive, liquid, cable)? | Tie path connected: slots 6.0 x 2.5 at y 7 on z 17 and 28 pass a 4.8 x 1.4 tie beyond the -Y features (z <= 13.6); the tie drops through the 2.30 / 2.65 post-to-plate gaps and crosses the plate corners at r 31.66 / 31.36 (A-07, F2). | YES |
| P3 | Moving parts oriented for their motion, with clearance? | No moving part; the vibrating pump keeps 2.300 to the -X post, 2.650 +X, 2.788 to both ribs; lowered along +Y from 60 mm it keeps >= 2.300 and 0.0 mm3, the sleeve touching only at the final pose. | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | The pump (x -27.20..26.85) drops between post faces 59.0 apart; the four holes are open from above; the nearest post corner is 4.03 from each rear hole axis, so an M3 head (r 2.75) and a driver shaft clear it. | YES |
| P5 | Next to a comparable real product, does anything look absurd? | An 80 x 52 x 40 mm, 32.3 g PETG two-saddle cradle for a 0.5 kg vibratory pump on a rubber sleeve is in proportion with OEM pump brackets. | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | One solid standing on its foot, saddle faces toward the pump (-Y), in the spec frame (OD-H01 in the assembly equals the input); the cradle is not embedded in anything. The assumed sleeve solid shares 1427.17 mm3 with OD-H01 (F6), an A-03 model limit outside the cradle. | YES |

Sections used (reviewer's own, `reviews/RV02_work/sections/`, each `nothing_clipped` 0; numeric outlines in `m3_sections.json`): cradle XY at z 0, 17, 28; YZ at x 0 and 31.5; XZ at y 7; check assembly XY at z 0, 17, 28 and YZ at x 0.

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity (solid_count) | delivered part plus a loose 5 mm cube | FAIL |
| validity (naked_edges) | delivered part with its foot end face removed (open shell) | FAIL |
| envelope (U-02) | foot extended 0.5 mm in +Z (z to 42.5) | FAIL |
| envelope max_y (REQ-08) | foot underside moved 0.3 mm down (y 40.3) | FAIL |
| feature_census, bore_census (U-05) | hole (-34, -4) filled | FAIL |
| locate_bore offset (REQ-07) | hole (-34, -4) moved 0.5 mm to z -3.5 | FAIL |
| locate_bore diameter (D-04a, REQ-07) | hole (34, 37) drilled 3.2 | FAIL |
| min_wall, min_wall_wide (D-01a/b, D-06a, U-06) | -X rear slot widened to z 32.5 (ligament 0.5) | FAIL |
| sections: slot ligament (REQ-05) | -X rear slot widened to z 32.5 (ligament 0.5) | FAIL |
| overhang_census (D-03a) | +X post: flat-roofed pocket y 12..14, z 15..22 cut through | FAIL |
| bridge_span from faces and sections (D-03b) | same pocket: 7.0 mm flat ceiling | FAIL |
| sections: slot clear section (REQ-05) | +X front slot floor raised 0.3 (clear 2.2) | FAIL |
| sections: rib faces (REQ-02) | rib 1 rear face moved to z 3.2 | FAIL |
| radial_profile (REQ-01) | both saddles opened to r 26.75 | FAIL |
| clearance == 0 (REQ-04, U-03 sleeve) | both saddles opened to r 26.75 | FAIL |
| radial_extent window (REQ-02) | 1 mm lump at r 30, theta 40, joined to the web | FAIL |
| interference (REQ-04, U-03) | saddle 1 closed to r 26.55 over its arc | FAIL |
| clearance (REQ-03, D-04c, U-03) | -X post inner face moved to x -29.0 | FAIL |
| post faces (REQ-06) | -X post inner face moved to x -29.0 | FAIL |
| compare_step (U-04) | hole (-34, -4) filled, compared with the delivered STEP | FAIL |
| mesh_sagitta (U-07) | STL at tolerance 0.1 / 0.5 rad | FAIL |
| mesh_deviation (U-07, V-05) | STL at tolerance 0.1 / 0.5 rad | FAIL |
| mesh_census (U-07) | delivered STL with its last triangle removed | FAIL |
| mass_properties com (P1) | OD-H01 moved 15 mm toward -Z | FAIL |

Every mutant was made from the delivered STEP by my own script (`RV02_work/controls.py`, results in `controls.json`) and run through the same predicate code as the gate table. The first bridge-span control (a 7.0 × 4.0 flat pocket) passed a metric that took the smaller face size; the metric was corrected to the larger size (conservative) and both the control and the gate table were re-run: the control now FAILs and the delivered part still reads 0.0 (no flat downward face).

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | SOFT_GATE_MISS | not measured → Soft: no unacceptable vibration to the chassis with the OEM sleeve fitted (bench) | — | — | no | UNKNOWN | a bench gate no geometric check can answer; the rubber path rests on A-03 and A-05, and the ties also bear on the steel side plates (F2), a path around the sleeve | bench-test the first print with the OEM sleeve and ties fitted; add a rubber pad under the tie at the plate corners if it buzzes |
| F2 | P2 (RV01 F3, A-07) | OBSERVATION | 31.66 mm → the tie rides on the sleeve (spec section 4 C1) | — | side plate corners (-27.20, -16.20) r 31.66 and (26.85, -16.20) r 31.36, over the tie bands z 14.6..19.4 and 25.6..30.4 | no | MEDIUM | the modelled sleeve (A-03) stops at \|x\| 23.5, so between the post slots and the sleeve the tie crosses bare steel plate corners; A-07 assumes the real sleeve covers them; a sheet edge can chafe the tie and carry vibration around the rubber | confirm on OD-H02 (scan or calipers); if the plates are bare, route the tie under the saddle or add a pad at the corners |
| F3 | REQ-04 (RV01 F4, A-03) | OBSERVATION | 6.9e-13 mm → clearance = 0 on the saddle arcs, interference <= 0 | -6.9e-13 | (-18.844, 18.844, -3.000) rib 1; rib 2 the same | no | MEDIUM | the zero gap holds only at r 26.650 exactly (controls: r 26.75 gives a 0.100 gap, r 26.55 on one arc 26.41 mm3); FDM holds about +-0.1..0.2; the coil under the saddles reads r 23.58..23.86 against the sleeve ID radius 23.65, so a real tube sleeve would stand up to 0.21 proud at theta 135 and 0.07 shy at theta 45 | retire A-03 with OD-H02 calipers; restate REQ-04 as a banded squeeze the rubber tolerates (for example 0.0..0.3 radial) |
| F4 | REQ-03 (RV01 F5, A-01, A-04) | OBSERVATION | 2.3 mm → >= 2.0 | +0.3 | (-29.500, 0.000, 12.0..33.0) -X post inner face to the -X side plate x -27.20 | no | MEDIUM | margin 0.300 is below the scan's p95 deviation 0.448 (A-01, max 2.49); the post face runs parallel to the plate over 21 x 37 mm, so a plate 0.3 further out touches along its length | calipers on the frame plates (A-01, A-04); if they read wider, move post_x_in outward in the spec |
| F5 | D-01b, U-06, REQ-05, D-03a (RV01 F6) | OBSERVATION | 2 mm → ligament >= 2.0; slot clear >= 6.0 x 2.5; roofs >= 45 deg | -3.1e-15 | (-33.318, 6.101, 33.000) and the other three block-end ligaments; all four slots | no | LOW | zero margin by the spec's own dimensions (21.0 block, 6.0 slots at z 17 / 28); a 2.0 ligament is five 0.4 perimeters in a 4.0-deep bar, and a 2.5 clear slot passes a 1.4 tie, so function does not hang on the last 0.1 | spec: a 22.0 block or 5.8 slots for margin; nothing needed in the build |
| F6 | P6 (A-03 sleeve model) | OBSERVATION | 1427.2 mm3 → not a section 5 pair (information): the assumed sleeve solid sits on OD-H01 without overlap | — | -Y arc 1163.18 mm3 (812.15 at z -6..5.5, 309.32 at z 5.5..13.6, the terminal block, spade tabs and slot box); +Y arc 263.99 mm3 (coil off-axis) | no | LOW | the overlap is between two reference bodies, not the cradle; it shows the A-03 tube cannot be the real sleeve on the -Y side, where the cradle does not touch it; the +Y part is F3 | model OD-H02 from a scan or calipers when it lands (A-03) |

RV01 findings in this round (brief): F1 (REQ-09) is now a Soft row, carried here as F1 SOFT_GATE_MISS, UNKNOWN, non-blocking. RV01 F2 (centre of mass ahead of the saddles) is answered: rib 1 measures z −3.000 … 3.000 and the OD-H01 centroid z 7.232 lies inside the span z −3.0 … 31.0, no finding. RV01 F3 → F2 here (MEDIUM, A-07), F4 → F3 (MEDIUM, A-03, now with the coil-radius evidence), F5 → F4 (MEDIUM, A-01, A-04), F6 → F5 (LOW, the spec's own zero-margin values); F6 here records the sleeve model's overlap with OD-H01 (LOW).

Tool note (not a part finding): `tools.measure.min_wall` still reports `detail['solids'] = 4` on this one-solid part; the measured wall is unaffected (`validity` reads solid_count 1).

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| REQ-03 margin 0.300 at the -X post is below the scan p95 0.448 (A-01) | Confirmed: 2.300 from the -X post inner face (x -29.500, z 12..33) to the -X side plate x -27.200, +X 2.650; the vertical insertion path keeps 2.300; a control with the post at x -29.0 reads 1.800 and FAILs. Rated F4 MEDIUM. |
| REQ-04 contact and the sleeve shape rest wholly on A-03; rib 1 sits 3.0 inside the assumed sleeve's front end | Confirmed: 6.9e-13 on each rib, 0.0 mm3; rib 1's front face z -3.000 is 3.0 inside the sleeve end z -6.0; the coil under the saddles reads r 23.58..23.86 against the sleeve ID 23.65, so the fit is uncertain by about 0.2 either way. Rated F3 MEDIUM. |
| F2 answered with the uniform-density centroid of the scan solid (z 7.23) | Confirmed: centroid z 7.232 in both the input and the assembly copy of OD-H01, inside z -3.0..31.0 with 10.23 to the nearer end; a real centroid would have to sit more than 10 mm toward the outlet to leave the span, which a coil and frame spanning z -12.4..37.65 make unlikely. RV01 F2 closed. |
