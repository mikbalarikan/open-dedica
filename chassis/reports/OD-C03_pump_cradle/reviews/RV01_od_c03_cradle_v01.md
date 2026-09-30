# RV01 — od_c03_cradle_v01 (20260930-od-c03-pump-cradle) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.1 · plan `01_CAD/DESIGN_PLAN.md` (with the amendments of `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_c03_cradle_v01.md`

**VERDICT: REVISE**
Blocking findings: 1 (F1, REQ-09 HARD_GATE_INCONCLUSIVE, bench gate) · open assumptions relied on: A-01, A-03, A-06, A-07, A-10, A-11, A-13

Every geometric §5 row re-measures PASS or PASS (assumed) from the exported files. The one blocking finding is REQ-09. It is a Hard row that only a bench run can answer. By rule an INCONCLUSIVE Hard gate blocks, and no rebuild of the geometry can clear it. The decision on it is the Usta's (F1). Findings F2 to F6 are non-blocking observations, rated MEDIUM or LOW. They are for the Usta to accept knowingly.

Tolerance bands (GATES §0 as the plan carries them): 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts. Every comparison goes through `tools.result.gate`. Reviewer scripts, mutants and sections are in `reviews/RV01_work/` (`checks.py` is the one gate code, run on the delivery and on every mutant).

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `01_CAD/REPORT_od_c03_cradle_v01.md` | 2cafaad31f8bf134745d0d350e9b1b63dc0a15862c0acd893cf7d885410cd76a | yes |
| `01_CAD/DESIGN_PLAN.md` | 7e86466421a4ad81e87dd87bb93215966e3a0b974e33869163b55aaa42bd6540 | yes |
| `01_CAD/check_od_c03_cradle_v01.json` | c46068d7c469414f7200ce8d8ec57a51b2fe9225c8b3a77e604541410d67e66d | yes |
| `01_CAD/sections_od_c03_cradle_v01.json` | 7856b0a860c0b51701464b361ed6701bfc03ab554caa575d6af5c498bb13ea77 | yes |
| `02_STEP_STL/od_c03_assembly_C1_v01.step` | 6ce49e9220d6737d0cd9e95d385b1f7de80ced7e64e7616e562e47bb5280cebf | yes |
| `02_STEP_STL/od_c03_cradle_C1_v01.step` | c4b028e130a3ee29324c5cd31543e44ec7ee6bb5e2489f8dc55c6b018a4aefbd | yes |
| `02_STEP_STL/od_c03_cradle_C1_v01.stl` | b95aab55d1efb1706f41bb7c4c2a9e8c6e50a2ccf0a8e9fa3a5bd38af6dcae8c | yes |
| `03_Sections/od_c03_cradle_v01_assembly_xy_z18p0.png` | f42595ad12ffb6770772bbec40dd72a2d5ed9219a0afdcee64b55c1753dfce90 | yes |
| `03_Sections/od_c03_cradle_v01_assembly_yz_x0p0.png` | bd8a2a1c5c74aa52dee5cefd3191443ea60fcf37d0d1328c315acc1267adf1f2 | yes |
| `03_Sections/od_c03_cradle_v01_xy_z18p0.png` | 6026c0bc98de01d1247d3738a1097fd6d831ca283b5cd6fa2587a615babd3f22 | yes |
| `03_Sections/od_c03_cradle_v01_xy_z28p0.png` | dcb202aa0c0badf040899673aa6f03fbb7d39d4c8be76dacb6ccaa4e5c5a8119 | yes |
| `03_Sections/od_c03_cradle_v01_xz_y38p5.png` | 144b0776717f332a26987361ac900c06299c71a04f252aa55b5bb9d56395a115 | yes |
| `03_Sections/od_c03_cradle_v01_xz_y7p0.png` | 6ef1f55c114f986b4c186561af43e4f5e40eb8868f7c12733fe82830688dba65 | yes |
| `03_Sections/od_c03_cradle_v01_yz_x0p0.png` | 25df58f08d72acfef2676a63b60cd810b20396cfb9118b1e18a5352e4cd24072 | yes |
| `03_Sections/od_c03_cradle_v01_yz_x31p5.png` | f464a2577d1dc4ff079f4acd9a0f0cbe0fdf4aea79170d3b544c4207aba31986 | yes |
| `03_Sections/od_c03_cradle_v01_yz_x34p0.png` | f51f03846c0f003bef9cf8caff76b7567f719b8b315de9378650950208eae4b1 | yes |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | yes |

All hashes match the brief and REPORT §1 (the OD-H01 input matches the brief). Completeness: every §5 row is answered in the REPORT and every listed file is present. The delivered STL is byte-identical to a fresh `write_stl` of the delivered STEP at 0.01 mm / 0.1 rad.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 count | solid_count = 1, brep_valid = 1, naked_edges = 0 | 0 | whole part: solid_count 1, brep_valid 1 (BOP faults 0), naked_edges 0 of 144 edges | PASS | `validity` | — |
| U-02 | 80 mm | 80.0 x 40.0 x 52.0 each in [spec - 0.1, spec + 0.1]; position reported apart | +0.1 | size_x 80.000 (size_y 40.000, size_z 52.000, each margin +0.100); position x -40.000..40.000, y 0.000..40.000, z -10.000..42.000, as the spec datum | PASS | `envelope` | — |
| U-03 | 6.9e-13 mm | (a) cradle|OD-H01 clearance >= 2.0 and interference <= 0; cradle|sleeve clearance = 0 and interference <= 0 mm3; (b) no motion variable | -6.9e-13 | cradle|sleeve 6.9e-13 at (-18.844, 18.844, 15.000) on the rib 1 saddle arc edge (r 26.650, theta 135.0), interference 0.0 mm3; cradle|OD-H01 2.300 at (-29.500, 0.000, 33.000) to the -X side plate (-27.200, 0.000, 33.000), interference 0.0 mm3; OD-H01 sound 1/1/0; (b) no motion variable; insertion path along +Y from -60 mm: minimum 2.300, sleeve first touches at the final pose | PASS (assumed: A-01, A-03) | `clearance, interference` | A-01, A-03 |
| U-04 | 0 mm3 | named body re-read unchanged, no stray shells, valid after re-import | +0.001 | compare_step of the re-read part with its file: schema AP242 1, solids 1, volume_delta 0.0 mm3, faces_delta 0, labels 1 (od_c03_cradle), valid_after 1; file holds 1 MANIFOLD_SOLID_BREP, 1 CLOSED_SHELL, 0 OPEN_SHELL, 54 ADVANCED_FACE, length unit MM | PASS | `compare_step` | — |
| U-05 | 48 count | 2 saddle ribs, 2 post blocks, 4 strap slots, 4 dia 3.4 through-holes, 1 foot plate | 0 | planes 48, cylinders 6 (6 concave: 2 saddle arcs r 26.650, 4 bores dia 3.400), bores 4, other kinds 0; by position: 2 ribs (faces z 15/21/25/31), 2 post inner faces |x| 29.5, 4 through-slots (line probes along X at x +-31.5, z 18/28), 1 foot underside y 40.0 | PASS | `feature_census, bore_census, locate_bore` | — |
| U-06 | 2 mm | >= 2.0 (min_wall wide, soft) | -3.1e-15 | (-33.318, 6.101, 33.000): -X post end face z 33 to the side of the z 28 slot (z 31); inside the 0.005 band | PASS | `min_wall_wide` | — |
| U-07 | 0.005 mm | STL at tol 0.01, angular <= 4*acos(1 - 0.01/32.0) = 0.1000026 rad; stl_max_sagitta <= 0.01 | +0.005 | delivered STL is byte-identical to a fresh write_stl of the delivered STEP at 0.01 mm / 0.1 rad (2540 triangles); sagitta 0.00489; mesh_deviation both ways 0.00489 at (-16.159, 21.192, 18.000) on saddle 1; mesh_census 1 body, 0 naked edges, winding 1, volume 25164.19 mm3 vs B-rep 25162.51 | PASS | `write_stl, mesh_sagitta, mesh_deviation, mesh_census` | — |
| U-08 | — | applies to threaded parts; this target has none | — | — | N/A: by its row | `none (N/A by its row)` | — |
| D-01a | 2 mm | >= 0.8 | +1.2 | (-33.318, 6.101, 33.000) slot end ligament | PASS | `min_wall` | — |
| D-01b | 2 mm | >= 2.0 | -3.1e-15 | (-33.318, 6.101, 33.000) slot end ligament, -X post; the same 2.000 at all four slot ends; inside the 0.005 band | PASS | `min_wall` | — |
| D-02 | 80 mm | each envelope size <= the Kobra Max 3 build volume, foot down (420 x 420 x 500 per A-10) | +340 | size_x 80.0 <= 420 (+340.0); size_z 52.0 <= 420 (+368.0); height size_y 40.0 <= 500 (+460.0) | PASS (assumed: A-10) | `envelope` | A-10 |
| D-03a | 45 deg | every downward face >= 45 deg from horizontal, build_dir (0,-1,0) | 0 | (-29.500, 5.750, 21.000): the eight slot gable roof planes, 45.000 deg, sampling bound 0.0 (planes only); 0 samples below 45 | PASS (assumed: A-13) | `overhang_census` | A-13 |
| D-03b | 0 mm | span <= 5 | +5 | no downward-facing horizontal face off the bed (normal +Y, y < 39.99): largest bridge span 0.0; sections x +-31.5 show every slot roofed by a 45 deg gable to an apex edge at y 2.75 | PASS | `face census by normal and envelope; reviewer sections` | — |
| D-04a | 3.4 mm | >= 3.25 | +0.15 | all four holes dia 3.400: (-34.0, 37.0, -4.0), (-34.0, 37.0, 37.0), (34.0, 37.0, -4.0), (34.0, 37.0, 37.0) | PASS | `locate_bore` | — |
| D-04c | 2.3 mm | >= 0.5 per side to OD-H01 (REQ-03 raises it to 2.0) | +1.8 | (-29.500, 0.000, 33.000) -X post to -X side plate | PASS (assumed: A-01) | `clearance` | A-01 |
| D-06a | 2 mm | >= 1.0 | +1 | (-33.318, 6.101, 33.000) slot end ligament | PASS | `min_wall` | — |
| D-07 | — | fit-critical bores: none on this part (the four holes are clearance holes) | — | — | N/A: by its row | `none (N/A by its row)` | — |
| REQ-01 | 26.65 mm | inner radius, theta 50..130 every 5 deg, z 15.5..20.5 and 25.5..30.5: min and max in [26.60, 26.70] | +0.05 | both windows 850 rays each, 0 unread: min 26.650 at (17.130, 20.415, 15.550), max 26.650 at (-15.286, 21.830, 15.550); same in 25.5..30.5 | PASS (assumed: A-03) | `radial_profile` | A-03 |
| REQ-02 | 26.65 mm | inner r <= 26.70 at theta 50/130, z 18/28; no material r <= 32.0 at theta 40/140; rib faces z 15.0, 21.0, 25.0, 31.0 +-0.10 | +0.05 | inner 26.650 at theta 50 and 130, z 18 and 28 (+0.050); theta 40/140 window r <= 32 reads INCONCLUSIVE 'no material' as the spec expects, first material on the whole ray 38.510 (the post at x +-29.5, +6.510); rib faces 15.000, 21.000, 25.000, 31.000 (+0.100); sector edge at 45.0 (theta 44.75 first material 41.35 = post) | PASS (assumed: A-06) | `radial_extent, face envelopes, sections` | A-06 |
| REQ-03 | 2.3 mm | clearance(cradle, OD-H01) >= 2.0 at the identity pose | +0.3 | (-29.500, 0.000, 33.000) on the -X post inner face to (-27.200, 0.000, 33.000) on the -X side plate; +X post 2.650; the input STEP placed by the reviewer at identity reads the same as the assembly's copy (common volume = full 114903.27 mm3) | PASS (assumed: A-01, A-03) | `clearance` | A-01, A-03 |
| REQ-04 | 6.9e-13 mm | clearance(cradle, sleeve) = 0 with the nearest points on the saddle arcs; interference <= 0 mm3 | -6.9e-13 | (-18.844, 18.844, 15.000) r 26.650 theta 135.0 on the saddle 1 arc; rib 2 alone 6.9e-13 at (-18.844, 18.844, 25.000); interference 0.0 mm3 | PASS (assumed: A-03) | `clearance, interference` | A-03 |
| REQ-05 | 6 mm | four through-slots along X, clear >= 6.0 (Z) x 2.5 (Y), centres y 7.0 +-0.5 and z 18.0/28.0 +-0.5, 45 deg gable roofs, ligament >= 2.0 | 0 | each of the 4 slots (x +-31.5, z 18/28): clear Z 6.000 (+0.000), clear Y 2.500 (+0.000), centre y 7.000, z 18.000/28.000, through 4.0 along X; ligaments 2.000 at the block ends (+0.000), 4.000 between slots, 2.750 above the apex; roofs 45.000 deg | PASS (assumed: A-07, A-13) | `line probes along X/Y/Z, envelope, overhang_census, min_wall` | A-07, A-13 |
| REQ-06 | 29.5 mm | post inner faces |x| = 29.5 +-0.1, z 13.0..33.0 +-0.1; post clearance to OD-H01 >= 2.0 | +0.1 | inner faces x -29.500 and 29.500, z 13.000..33.000 both (+0.100); clearance -X post 2.300 at (-29.5, 0.0, 13.0), +X post 2.650 at (29.5, 0.0, 33.0) | PASS (assumed: A-06) | `envelope, clearance` | A-06 |
| REQ-07 | 3.4 mm | four dia 3.4 +-0.1 through-holes along Y at (x +-34.0, z -4.0) and (x +-34.0, z 37.0), offset <= 0.10 | +0.1 | all four: dia 3.400, axis (0,1,0), offset 0.000 (+0.100), length 3.0, through 1 | PASS (assumed: A-11) | `bore_census, locate_bore` | A-11 |
| REQ-08 | 40 mm | foot underside y = 40.00 +-0.10 (envelope max_y), 3.0 +-0.1 thick | +0.1 | max_y 40.000; foot top plane y 37.000, thickness 3.000 (+0.100); sections x 0 and x 34 | PASS (assumed: A-11) | `envelope, face envelope, sections` | A-11 |
| REQ-09 | — | no unacceptable vibration to the chassis with the OEM sleeve fitted; bench gate, INCONCLUSIVE until the first run | — | — | INCONCLUSIVE | `none (bench)` | A-03, A-05 |

Motion and assembly: there is no motion variable (U-03 b, ties not modelled). I checked the assembly path by moving OD-H01 and the sleeve along +Y from −60 mm to the final pose. The clearance to OD-H01 falls to 2.300 at Δy −10 mm and stays there. The sleeve first touches the saddles at the final pose (6.000 at −10, 0.071 at −0.1, 0 at 0).

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 foot plate | 80.0 x 3.0 x 52.0, x +-40, y 37.0..40.0, z -10..42 (as amended) | top plane y 37.000, underside y 40.000 (1 face), x -40..40, z -10..42 | PASS |
| F02 rib 1 with web | z 15.0..21.0, inner arc r 26.65 over theta 45..135, outer ends r 32.0, web faces x +-22.627 to the foot | faces z 15.000/21.000, cylinder r 26.650 on (0,0,z), arc ends (+-18.844, 18.844), web x +-22.627 from y 22.627 to 37 | PASS |
| F03 rib 2 with web | z 25.0..31.0, same profile | faces z 25.000/31.000, cylinder r 26.650, same profile | PASS |
| F04 post blocks x2 | |x| 29.5..33.5, y 0.0..37.0, z 13.0..33.0 | 2 blocks, inner faces |x| 29.500, outer 33.500, top y 0.000, z 13.000..33.000 | PASS |
| F05 strap slots x4 | 2 per block, 6.0 x 2.5 clear, centres y 7.0, z 18/28, 45 deg gables, through along X | 4 through-slots, 6.000 x 2.500, floor y 8.250, sides y 5.750..8.250, gable apex y 2.750, 45.000 deg | PASS |
| F06 frame holes x4 | dia 3.4 through along Y at (+-34.0, z -4.0) and (+-34.0, z 37.0) | 4 bores dia 3.400, axis Y, offset 0.000, through | PASS |
| F07 check assembly | od_c03_cradle + OD-H01 + od_h02_sleeve_assumed_A03 at identity | 3 named children at identity; cradle equals the part file (common 25162.51 = full volume), OD-H01 equals the input (common 114903.27 = full), sleeve 2 solids 13993.08 mm3 | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | Yes with the ties: foot down (+Y), saddles under the sleeve, load path saddle-web-foot-4 screws; but the pump's centre of mass (uniform-density model z 7.23; coil centre z 12.85) lies outside the saddle span z 15..31, so it stays seated only under tie tension (F2) | YES |
| P2 | Function chains connected and aimed (air, drive, liquid, cable)? | Tie path exists: slot, up the 2.30/2.65 gap between post and side plate, over the plate corner (r 31.41 at theta 210) and the sleeve top, down the other side; the −Y side at z 15.6..20.4 is coil only (r <= 23.72); the tie bears on the metal plates (F3) | YES |
| P3 | Moving parts oriented for their motion, with clearance? | No moving part; the vibrating pump keeps 2.300 (-X post), 2.650 (+X post), 2.788 (ribs to coil); insertion along +Y keeps >= 2.300 from -60 mm to the pose | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | A dia 5.5 driver cylinder straight down each hole clears OD-H01 by >= 4.05 mm; screw heads clear the post ends by 1.25 in z; the 6.0 x 2.5 slots and 2.30 gaps pass a 4.8 x 1.4 tie | YES |
| P5 | Next to a comparable real product, does anything look absurd? | 80 x 52 x 40 mm, 31.96 g PETG cradle for a 0.5 kg vibratory pump: in proportion with OEM pump brackets | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | Cradle is one solid, in the spec frame, saddle facing the pump; only the assumed sleeve model is embedded in the coil (1427.17 mm3, an A-03 model limit, F4) | YES |

Evidence: my own sections in `reviews/RV01_work/sections/` (assembly at z 18.0 and x 0.0, cradle at x −31.5). I also cut numeric sections through the B-rep at z 18/23/28, x 0/±31.5/34 and y 7/38.5 (`m3_rows.json`). The radial probes of OD-H01 over the tie bands and the driver cylinders are in `m4_pump.py`.

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity (U-01) | M01 loose 2 x 2 x 2 box beside the part: solid_count 2; M18 part with one face removed: naked_edges 4 | FAIL |
| envelope (U-02, D-02, REQ-08) | M02 foot grown to z 42.5: size_z 52.5; M03 part moved +0.2 in Y: max_y 40.2 | FAIL |
| feature_census / bore_census (U-05) | M04 hole (-34, -4) filled: bores 3 | FAIL |
| locate_bore (REQ-07, D-04a) | M05 hole (-34, -4) moved 0.5 to z -3.5: offset 0.500; M06 same hole dia 3.1: REQ-07 and D-04a FAIL | FAIL |
| min_wall / min_wall_wide (D-01a, D-01b, D-06a, U-06) | M07 -X z18 slot cut into its end ligament, 0.6 left: 0.600 | FAIL |
| overhang_census (D-03a, REQ-05 roofs) | M08 -X z18 slot gable filled to a flat ceiling: 0.0 deg | FAIL |
| bridge span from downward faces (D-03b) | M08 flat 6.0 ceiling: span 6.0 | FAIL |
| clearance >= (REQ-03, D-04c, U-03, REQ-06) | M09 -X post inner face moved in 0.5 to x -29.0: 1.800 | FAIL |
| interference (REQ-04, U-03) | M10 saddle 1 radius 26.55: 24.51 mm3 | FAIL |
| clearance = 0 (REQ-04, U-03) | M11 both saddles opened to r 26.75: 0.100 | FAIL |
| radial_profile (REQ-01) | M10 saddle 1 at 26.55: min 26.550; M11 at 26.75: max 26.750 | FAIL |
| radial_extent (REQ-02) | M12 rib 1 extended to theta 37.5: window at theta 40 finds material, first material 26.650 < 32; M11: 26.750 at theta 50/130 | FAIL |
| face envelopes (REQ-02 faces, REQ-06 faces, REQ-08 thickness) | M13 rib 1 face moved to z 21.3: 21.300; M09 post face at 29.0 | FAIL |
| slot line probes (REQ-05, U-05 slots) | M14 -X z18 slot narrowed to 5.5: clear 5.500; M07 ligament 0.600; M09 slots through 2 of 4 | FAIL |
| compare_step (U-04) | M15 part compared with a written hole-filled STEP: volume_delta 45.50 mm3, faces_delta 3 | FAIL |
| mesh_sagitta / mesh_deviation (U-07) | M16 STL of the part at tol 0.1 / 0.5 rad: sagitta 0.0486, deviation 0.0486 | FAIL |
| mesh_census (U-07, V-05) | M17 delivered STL with one triangle dropped: naked_edges 3 | FAIL |

Every mutant is built from the delivered STEP by `reviews/RV01_work/controls.py`, using a fresh read each time, and run through the same `checks.run`. M04 to M06 plug the hole with a 5 mm cylinder, which also stands 1 mm proud of the underside. Their size_y and REQ-08 fails are that side effect. The targeted rows (bores 3, offset 0.500, diameter 3.1) fail as intended.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | HARD_GATE_INCONCLUSIVE | not measured → no unacceptable vibration to the chassis with the OEM sleeve fitted (bench) | — | — | yes | UNKNOWN | a Hard §5 row that no geometric check can answer; the evidence cannot tell, and F3 shows the ties bear on the metal frame, a path around the rubber sleeve | no geometry change clears it: bench-test the first print with the OEM sleeve, or the Usta reclassifies REQ-09 in spec §5 as a post-print gate outside the CAD review |
| F2 | P1 | OBSERVATION | 7.23 mm → pump centre of mass over the saddle span z 15.0..31.0 | -7.77 | (−0.07, −0.87, 7.23) uniform-density centre of mass of OD-H01; coil centre z 12.85 | no | MEDIUM | the pump extends to z -66.45 on the outlet side while both saddles sit at z 15..31; seated only by tie tension (about 3 N static at the z 28 tie), rocking on the rib 1 edge under vibration is plausible | spec: add a strapless saddle near z 0..6 (clear of the -Y features, which only constrain the strap path) or move rib 1 toward -Z so the span brackets the centre of mass |
| F3 | P2 | OBSERVATION | 31.41 mm → tie rides on the sleeve (spec §4 C1) | — | side plate corners (-27.2, -16.2) and (26.85, -16.2), r 31.41 at theta 210 over z 15.6..30.4 | no | MEDIUM | the tie climbs the outer faces of the side plates in the 2.30/2.65 gaps and crosses their corners before the sleeve, so frame-tie-post is a path that bypasses the rubber; a closed loop through two side slots also has to cross the pump twice | spec: route the strap under the saddle (slots in the foot or web) or add a rubber pad where the tie crosses the plate corners; confirm at the REQ-09 bench test |
| F4 | REQ-04 | OBSERVATION | 6.9e-13 mm → clearance = 0, interference <= 0 against the A-03 sleeve | -6.9e-13 | (-18.844, 18.844, 15.000) | no | MEDIUM | the equality holds only at r 26.650 exactly (reviewer controls: 26.55 gives 24.51 mm3, 26.75 a 0.100 gap), FDM holds about +-0.1 to 0.2, and the sleeve model overlaps OD-H01 by 1427.17 mm3 as two separate arcs | measure OD-H02 (retire A-03) and restate REQ-04 as a banded interference or gap the rubber tolerates |
| F5 | REQ-03 | OBSERVATION | 2.3 mm → >= 2.0 | +0.3 | (-29.500, 0.000, 33.000) to the -X side plate | no | MEDIUM | margin 0.300 is below the scan p95 deviation 0.448 (A-01, max 2.49), so the real plate may sit inside 2.0 | calipers on the frame plates (A-01, A-04); if they read wider, move post_x_in outward in the spec |
| F6 | D-01b | OBSERVATION | 2 mm → >= 2.0 (also U-06 and REQ-05 ligament; REQ-05 clear 6.0 x 2.5; D-03a 45 deg) | -3.1e-15 | (-33.318, 6.101, 33.000) slot end ligaments, all four | no | LOW | zero margin by the spec's own dimensions; a 2.0 ligament is five 0.4 perimeters and a 2.5 slot passes a 1.4 tie, so function does not hang on the last 0.1 | spec: 22.0 post block or 5.8-wide slots to give margin; none needed in the build |

Tool note (not a part finding): `tools.measure.min_wall` reports `detail['solids'] = 4` on this one-solid part. In `wall.py` the loop variable `found` is re-bound to the ray-hit tuple before `len(found)` is taken. The measured wall is not affected: `validity` reads solid_count 1.

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| REQ-03 margin 0.300 at the -X post is below the scan p95 0.448 (A-01) | Confirmed: 2.300 at (-29.5, 0.0, 13..33) to the -X plate x -27.20, +X 2.650; the insertion path keeps 2.300. Rated F5 MEDIUM; calipers retire it. |
| REQ-04 contact and the sleeve shape rest wholly on A-03; the assumed sleeve overlaps the coil by 1427.2 mm3 | Confirmed: contact 6.9e-13 on both saddles, interference 0.0; the sleeve model is two arcs sharing 1427.17 mm3 with OD-H01; +-0.10 on the radius gives 24.51 mm3 or 0.100 gap (F4). |
| Zero-margin rows: slot ligament 2.000, slot clear 6.0 x 2.5, gable roofs 45.000 deg; ties bear on the side plates | Confirmed: ligaments 2.000 (min_wall 1.999999999999997), clear 6.000 x 2.500, roofs 45.000 deg, all inside the bands (F6 LOW); the tie path crosses the plate corners at r 31.41 (F3 MEDIUM). |
