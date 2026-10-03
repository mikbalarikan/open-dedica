# REPORT — od_c14_grommet_half v01 (20261002-od-c14-cord-grommet)

Designer: Claude Code · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` (SHA-256 731a8495…0e4b, as amended by spec 1.1 §8) · brief WP-03 (J3, build attempt 1 of 2) · 2026-10-02 UTC

<!-- Placed by the orchestrator: the designer's write of this file was refused by a session hook; the text below is the designer's returned text unchanged but for the model name. -->

`01_CAD/check_od_c14_grommet.py` measured every number below on the re-imported STEPs `02_STEP_STL/od_c14_grommet_half_C1_v01.step` and `02_STEP_STL/od_c14_assembly_C1_v01.step`. The full rows are in `01_CAD/check_v01/check_results.json`. The input hashes match the brief: spec 8a02f52c…ae19, plan 731a8495…0e4b, OD-C11 8ac0df9c…0d33db, OD-C01 7b5688af…195805.

## 1. Files
| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c14_grommet.py` | e4b67832fde0ce3ec8fbdd31f6e537cb1bdb3fe591f7dac5b6459962569e0650 | parametric build; `--sweep` writes the D7 runs |
| `01_CAD/check_od_c14_grommet.py` | 93fe817c0f812dd476c9cb0a7c5c77fa67455ea1d1342e110ffdc1e272550019 | checks, written before the build (D3); `--run` checks one sweep run |
| `01_CAD/sections_od_c14_grommet.py` | 3b9f2b9a2ebc213f4de893377d3c5e6f0acad10dd78a4230331c5fd4e326c725 | D6 sections, from the re-imported STEPs |
| `01_CAD/check_v01/check_results.json` | 22def3a873b555ebed4bb5f49302e532256f688935c8e2dfc94d41bfd10be8ad | every measured row at nominal |
| `01_CAD/check_v01/remesh_of_reimported_step.stl` | check artifact | the U-07 sagitta re-mesh |
| `02_STEP_STL/od_c14_grommet_half_C1_v01.step` | 55ce2a3e6a68458e6f97f26a58b05d4691bd69f310105551f98b28fcdb0a0680 | AP242 (`write_step`); one solid `od_c14_grommet_half`; machine frame; open pose (upper half) |
| `02_STEP_STL/od_c14_grommet_half_C1_v01.stl` | 645a8dde3b824729be2fe225589561b529c879c2bf9fbb5b10d927f102eafaa8 | `write_stl` from a cleared triangulation; 0.01 mm / 0.10 rad; 1658 triangles; sagitta 0.00584 |
| `02_STEP_STL/od_c14_assembly_C1_v01.step` | a21a8f9d88d7f1ec8a97103c980ec2f16a798c9376a0d124be1c3b3b8a8b992b | AP242: od_c11_back_panel, od_c01_base_frame (identity), half_upper, half_lower (open pose), cord_envelope, tie_envelope, tie_head_box |
| `03_Sections/od_c14_grommet_half_v01_left.png` | 56108d9559b1ee885aa062b949379274060775d964aa6101c555539a77c70653 | x = 95.00; nothing_clipped 0 |
| `03_Sections/od_c14_grommet_half_v01_front.png` | 187921b977865fc094efd2b8d51df32285b37167c18eb885e34abef9f381e4d3 | y = 32.00; nothing_clipped 0 |
| `03_Sections/od_c14_grommet_half_v01_top.png` | 3c80b20f9ca84cc114c82dbe096547eb09c5e6b7e311c5f649299b49a2681ee2 | z = −296.60; nothing_clipped 0 |
| `03_Sections/od_c14_assembly_v01_left.png` | 7507bfb01cf3379719d5710e601889b489e194648de0d3c3c1673d7263e9339f | x = 95.00; OD-C11 and OD-C01 clipped to x 75…115, y −8…55, z −310…−280; nothing_clipped 0 |
| `03_Sections/od_c14_assembly_v01_front.png` | 2b323a0f3433b068624ea6671710db6458502ca6e12bae2ea881530f20c2678c | y = 32.00; same clip; 0 |
| `03_Sections/od_c14_assembly_v01_top.png` | e89040c07b9890ae86642e0cee84cff903a83220710cbd381ac4f2a645c659b9 | z = −296.60; same clip; 0 |
| `01_CAD/sweep_v01/build_log.json` | ad93ccd9ac53370407d50ea814c25766ecc3a1e681e7e8fd2c10d254ea0253d7 | 15 sweep builds, in `sweep_v01/<run>/` |

## 2. Versions
Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 (OCCT 7.9.3) · tools venv from `tools/uv.lock` · repo commit 10929db1408d89144bd4af9cad971440427933d0

## 3. Gate self-check
Bands (GATES §0): 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. Margins are signed, positive inside. A self-check clears no Hard gate.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | = 1 | 0 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1/1/0 | 0 | — | PASS | — |
| U-02 | 19.984 × 9.600 × 13.000; position x 85.008…104.992, y 30.400…40.000, z −304.000…−291.000, reported apart (x is ±0.008 because of the split chord) | spec ± 0.1 | 0.084 / 0.100 / 0.100 | — | PASS | — |
| envelope_within_spec | as U-02 | as U-02 | 0.084 | — | PASS | — |
| U-03 (a) | flange to the OD-C11 outer face 0.000/0.000 (upper/lower); bore to cord 0.000/0.000; tie to groove floor 0.000/0.000; half beyond the flange to OD-C11 0.350/0.350; tie and head box to the inner face 0.200/0.200; halves 0.800; to OD-C11 gussets and floor flange: half 8.411/3.010, tie 3.000, head 14.677; to OD-C01: half 30.400/20.000, tie 23.550, head 36.450; tie OD 12.900; interference 0.000 mm³ in all 21 pairs | contacts 0; ≥ 0.30; 0.20 ± 0.05; 0.80 ± 0.05; ≥ 0.5; ≥ 10; > 12.0; ≤ 0 | 0.050 | neck (100.636, 30.400, −301.900) | PASS (assumed: A-01, A-02, A-04, A-05) | A-01, A-02, A-04, A-05 |
| U-03 (b) | halves 0.000 mm and 0.000 mm³; neck to OD-C11 0.364/0.364; squeeze 0.400 at z −301.0, −296.2 and −291.8, both halves | 0, ≤ 0; ≥ 0.30; 0.40 ± 0.05 | 0.064; 0.050 | (100.636, 30.000, −301.900) | PASS (assumed: A-01, A-02, A-05) | A-01, A-02, A-05 |
| U-03 (c) | 11 poses, dz −20…0 in steps of 2.0, both halves against OD-C11 and OD-C01: worst 0.000 mm³; least clearance 0.350 (collar in the hole at dz −10) | ≤ 0 mm³ | 0 | — | PASS | — |
| U-04 | schema 1; solids 1; volume delta 4.7e-11 mm³; faces delta 0; labels 1; valid after re-import 1 | 1; 1; ≤ 0; 0; 1; 1 | 0 | — | PASS | — |
| U-05 / feature_census | plane 6 (bed face, wall face, neck step at −298.8, collar top, and the split face as 2 faces at y 30.40); cylinder 5 (convex 4, concave 1); cone 3 (the flank and 2 chamfers); everything else 0; bores 0 | plan counts | 0 | — | PASS | — |
| U-06 (Soft) | 45° wall 1.650 | ≥ 1.6 | 0.050 | groove floor (90.029, 31.346, −298.614) | PASS | — |
| U-07 | tol 0.01; ang 0.10 ≤ 4·acos(1 − 0.01/10.000) = 0.1789; sagitta 0.00584; delivered STL: 1658 triangles, 1 body, 0 naked edges, winding 1, volume 538.32 mm³, deviation 0.00584 | sagitta ≤ 0.01 | 0.0042 | (97.819, 34.598, −293.167) | PASS | — |
| U-08 | N/A by its row | — | — | — | N/A | — |
| D-01a | min_wall 1.650 | ≥ 0.8 | 0.850 | groove floor | PASS | — |
| D-01b | min_wall 1.650 (mesh check 1.6485) | ≥ 1.6 | 0.050 | groove floor | PASS (assumed: A-03) | A-03 |
| D-02 | 19.984 × 9.600 × 13.000 standing on the flange | ≤ 220 × 220 × 250 | 200.0 | — | PASS (assumed: A-07) | A-07 |
| D-03a | 59.886° at the upper edge of the bed-side chamfer; flank 60.000°; build_dir +Z | ≥ 45° | 14.886 | (91.549, 30.581, −303.500) | PASS (assumed: A-06) | A-06 |
| D-03b | flat_ceiling_spans 0.0; the reviewer gates this from sections | ≤ 5 | 5.0 | — | PASS (assumed: A-06) | A-06 |
| D-04d | neck to the hole 0.350/0.350 (B-rep); hole r 6.000 − neck/collar r max 5.650 = 0.350; least on the path 0.350 | ≥ 0.30 | 0.050 | (100.636, 30.400, −301.900) | PASS (assumed: A-01) | A-01 |
| D-06a | 1.650 | ≥ 1.0 | 0.650 | groove floor | PASS | — |
| D-07 | N/A by its row | — | — | — | N/A | — |
| J-06 | bore_census 0; bspline + other faces 0 | none | 0 | — | PASS | — |
| E-11 | the reviewer gates this from sections. Supplied: squeeze 0.400; tie 0.200 off the inner face, OD 12.9 over the Ø12.0 hole; flange on the outer face 0.000; both bore ends chamfered | present | — | — | PASS (assumed: A-02, A-04, A-05) | A-02, A-04, A-05 |
| REQ-01 | radial_profile over 10°…170° at 0.2 mm levels: flange 10.000, neck 5.650, groove 5.150, collar 5.650; spread 0.000 in every band; axis offset of every cylinder and cone 0.000; z −304.000 / −302.000 / −298.800 / −293.600 / −292.734 / −291.000; flank 60.000° | Ø ± 0.1 or ± 0.05; z ± 0.1; 60 ± 1°; offset ≤ 0.05 | 0.025 | — | PASS (assumed: A-01) | A-01 |
| REQ-02 | bore r 3.500 at 20°, 90° and 160° × 3 z levels; split face 2 faces in one plane at y 30.400; chamfers in 0.500 × 0.500, out 0.290 radial × 0.500 axial | 3.50 ± 0.05; 30.40 ± 0.02; ± 0.1 | 0.020 | — | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-03 | lower half = the half turned 180° (common volume 538.5545 = the half's); closed pair 19.984 × 19.200 × 13.000 | 20.0 / 19.2 / 13.0 ± 0.1 | 0.084 | — | PASS | — |
| REQ-04 | groove width 5.200; tie OD 12.900; head box to OD-C11 features 14.677 | 5.2 ± 0.1; > 12.0; ≥ 0.5 | 0.100 | (97.500, 36.450, −298.800) | PASS (assumed: A-04) | A-04 |
| REQ-05 (Soft) | bench check; risk MEDIUM: the PLA halves are stiff (A-03), so all the grip comes from the tie's 0.4 closing per side (A-05) | first fitting | — | — | INCONCLUSIVE | A-05 |

## 4. Robustness sweep (D7)
Each run moves one parameter to an end of its REQ band. All 15 runs built one valid solid and passed U-01, U-02, U-04, U-05, U-07, D-01a/b, D-02, D-03a, D-04d, D-06a, J-06, REQ-02, REQ-03, REQ-04 and U-03(c). In every run the tie envelope and head box follow the measured groove.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| neck_d | 11.25 · 11.30 · 11.35 | yes | D-04d 0.325 (high); U-03b neck 0.339 | +0.025 |
| neck_len | 3.1 · 3.2 · 3.3 (neck end −298.9/−298.8/−298.7) | yes | U-03a play 0.100 / 0.300 | −0.050 FAIL at both ends. The REQ-01 neck (low) and groove (high) radial bands read INCONCLUSIVE because the moved step face lies inside the nominal probe band |
| groove_d | 10.25 · 10.30 · 10.35 | yes | D-01b 1.625 (low) | +0.025 |
| groove_w | 5.1 · 5.2 · 5.3 | yes | REQ-04 width and flank-end z at the band ends | 0.000 |
| collar_d | 11.25 · 11.30 · 11.35 | yes | D-04d collar 0.325 (high) | +0.025 |
| bore_d | 6.9 · 7.0 · 7.1 | yes | D-01b 1.600 (high); squeeze 0.450 / 0.350 | U-03a bore on cord FAIL: 6.10 mm³ overlap (low) / 0.050 gap (high) |
| split_y | 0.38 · 0.40 · 0.42 | yes | halves gap 0.760 / 0.840 | U-03b at the 0.4 closed pose FAIL: 2.70 mm³ overlap / 0.040 gap |

Three rows pass only at nominal: the U-03a axial play (neck_len), the U-03a bore-on-cord contact (bore_d), and the U-03b closed-pose touch (split_y). Run results are in `sweep_v01/<run>/check_results.json`. The nominal run (22def3a8…) is byte-identical to `check_v01`. Other runs: bore_d_high 9bb853ee0ed8f7c16ec130d5d93e9c4529a68016085ebebc92e813d376eaf8d6, bore_d_low ba2377baabf278c9b3fb0083495ad3c154e6932690e6257f394f0e109ff26243, collar_d_high c02eb52113c5977a209741d0ea25a99f1f37a8faa03fedb3a6c01c056a6ffab2, collar_d_low e2f82c49806913af488106991a9093b47dbdaa2c0073c7b8e5408e6a40828bba, groove_d_high f2fa9a6ac52cfe1ea830dfb45dcceb79956b91d766650b27357d4628aa67cb8d, groove_d_low d258d3a98cac75874d8890d8006c3ee028dab67b9232a8c2519b6de585227217, groove_w_high 8f22305f4f9da2595768e9c3ad2cf7fa1ee2a52fd4e91081d35377988ce7d13a, groove_w_low 0ef39a4fcaf5e600e53a32d692661f7cebec72105552651fdf8ae92f5f617362, neck_d_high 172298eb73920bd9a3a65cbd0aeec50da76172b4daf798ef13231e397b881c90, neck_d_low d80736a17cfa05c697a303b2abf123cf91fe6e8d020c7c2bd1d3502c5a006f57, neck_len_high ab4d7dec2dde81d36ec71b339cc6b9853f46c701820d203b0fb4a4725f46300a, neck_len_low b045cfafa83d99736d5833d06c6b636cc654f254f0ad5b486329aa2895680b9c, split_y_high 11400b1aacf2e0e9629d03cee9eea4313eb88abce1621aa4191c0868ae513446, split_y_low 4048bb3320f84a6c8086c31572cc326a80f386cfcf1a2f4e58f80e22529d0e61.

## 5. Build facts
- Envelope 19.984 × 9.600 × 13.000; volume 538.55 mm³; mass 0.668 g at 1240 kg/m³ (A-03); centre of mass (95.000, 33.916, −299.749).
- Fillets: none specified, none modelled. All edges are sharp except the two bore chamfers.
- Placements: the half sits on one joint at the OD-C11 hole as measured by `locate_bore` (Ø12.000, start (95, 30, −302), axis (0, 0, 1), through; the build refuses an axis more than 1e-6 off Z). The lower half is the upper turned 180° about that axis. OD-C11 and OD-C01 are at the identity. The cord is Ø7.0 on the axis, z −330…−260. The tie envelope runs Ø10.300/12.900 over z −298.8…−294.0, with its inner face on the measured groove floor and its outer side on the neck-side face. The head box spans x 92.5…97.5, y 36.45…42.45, z −298.8…−293.8.

## 6. Plausibility (§P)
| # | Question | Answer |
|---|---|---|
| P1 | Gravity | Yes. The flange bears on the outer face and the tie inside, so the part works in any orientation. It prints on the flange's flat face. |
| P2 | Function chains | Yes. The cord runs straight along the hole axis through the bore, with nothing across its path (sections x 95 and z −296.6). |
| P3 | Motion clearance | Yes. The insertion along +Z is clear at all 11 poses (0 mm³), with a least gap of 0.35. |
| P4 | Human factors | Yes. The halves go round the cord and are pushed in from outside until the flange stops them. The tie head sits upward, away from the gusset, and can be reached from inside. |
| P5 | Next to a real product | Nothing looks absurd. It reads as a normal split strain-relief bushing. |
| P6 | Floating, embedded, mirrored, upside-down | None. The contacts read 0.000 with 0 mm³ in every pair. The lower half is the upper turned 180°, not mirrored. The flange is outside and the collar inside. |

## 7. Library and tools used
- Cards: none matched (as found at D1).
- `tools.core`: read_step, validity, write_step, compare_step, write_stl and mesh_sagitta.
- `tools.measure`: bore_census, locate_bore, envelope, feature_census, radial_profile, radial_extent, clearance, interference, min_wall (with its wide reading), overhang_census, flat_ceiling_spans, mesh_census, mesh_deviation, min_wall_mesh, mass_properties, features.cylinder.
- `tools.drawing.write`: write_sections and nothing_clipped. `tools.result.gate` makes every comparison.
- Only job-local code was written (box clips, face selection by type and position, cone axes read with BRepAdaptor_Surface). No missing tool.

## 8. Deviations from the plan
1. The spec 1.1 values replace the plan's 1.0 values: Ø11.3 neck and collar, Ø10.3 groove, neck end −298.8, flank 60° to −292.734, tie at z −298.8…−294.0, head box per Q2.
2. The tie envelope is placed on the measured groove rather than on the inner face, because spec 1.1 puts it 0.20 off that face. At nominal it lands exactly on the spec's z.
3. U-04 compares the STEP with the same solid rebuilt in memory from the run's parameters.
4. REQ-01 coaxiality is read from the B-rep axes of every cylinder and cone, in addition to the radial spread.
5. Sections are drawn for both the half and the assembly. The assembly pictures and the U-03(c) path both use clipped copies of OD-C11 and OD-C01. The path clip is x 70…120, y 5…55, z −330…−280, with at least 5 mm margin around every pose.
6. Fix cycle 1: the first assembly export shared one shape between the two halves, so the STEP named one product `half_lower` twice and U-03 read INCONCLUSIVE. The halves are now separate deep copies. The half's STEP did not change (same SHA-256).
7. D-04d is also read along the assembly path.

## 9. What I am least sure of
1. The axial play band (U-03a, 0.20 ± 0.05) is tighter than REQ-01's ± 0.1 on the neck end, so the row passes only at nominal. The spec bands disagree, and the spec must say which one governs.
2. The cord contact and the closed pose are rigid definitions applied to a compliant cord. Bore r ± 0.05 gives a 6.1 mm³ overlap or a 0.05 gap, and split_y ± 0.02 gives a 2.7 mm³ overlap or a 0.04 gap at the fixed 0.4 closing. D-01b sits at 1.600 exactly (margin 0.000) at bore_d high.
3. REQ-05 and A-03: the grip, and whether the parts resist turning, rest on the tie's tension and on PLA holding at the 1.65 groove wall. Only the first fitting can answer this.

## 10. Stop
Not stopped on any gate. Only the REPORT file write was refused (see the return block).
