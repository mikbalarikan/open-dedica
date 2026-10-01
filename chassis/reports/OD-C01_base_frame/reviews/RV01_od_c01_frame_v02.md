# RV01 — od_c01_frame_v02 (20260930-od-c01-base-frame) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` with `briefs/WP-03_designer.md` and `briefs/WP-04_designer.md` · report `01_CAD/REPORT_od_c01_frame_v02.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-09, A-11, A-12, A-13, A-14, A-17

Band (GATES §0, as the plan states it): mm 0.005, mm³ 0.001, degrees 0.001, counts and 1/0 facts 0. Every value below comes from the reviewer's own scripts in `reviews/RV01_work/` (`rv_a_plate_asm.py`, `rv_b_export.py`, `rv_b2_rt.py`, `rv_c_walls.py`, `rv_d_controls.py`, `rv_e_wallctl.py`, `rv_f_sections.py`, `rv_g_misc.py`; results in the matching `rv_*.json`) run on the exported files and on the input STEPs placed independently by the spec §4 joints. The placed inputs match the solids in the check assembly STEP to 0.000 mm on every envelope bound. No designer script was read. `min_wall` and `overhang_census` ran at spacing 0.7.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `01_CAD/REPORT_od_c01_frame_v02.md` | 78a03e899b024380df0d0bce9495ad3184ed13a0c454b8a2815a113e4d3bea7b | yes (brief; not listed in the REPORT) |
| `01_CAD/DESIGN_PLAN.md` | 086dde812dcc207fa171977fb45f9d2ed5a8df324099bce8c813eb3651aa7217 | yes (brief; not listed in the REPORT) |
| `briefs/WP-03_designer.md` | b34294f10520e24cccaf90a702191bde0628805841af037bc0208de0980f9004 | yes (brief; not listed in the REPORT) |
| `briefs/WP-04_designer.md` | 4634cd15f8906089a3129561831220145920ddd5cadd8ed6136513298254d513 | yes (brief; not listed in the REPORT) |
| `01_CAD/check_od_c01_frame_v02.json` | e629e5555b94a10952302443ca89b1bcd73b89e40a2e27c0c3104d29dba19728 | yes |
| `01_CAD/build_record_v02.json` | d3efabdd7a6fe5362089182e9f65ca4569aeb3a11e4b0a827e21e77cb868807c | yes |
| `01_CAD/sections_v02.json` | 67b31897473368a6e9b70abae088c605d49dfb4ddddddcec85ad84197f3cb173 | yes |
| `01_CAD/sweep_v02/sweep_summary_v02.json` | 38bfd098bf06cd107577c145d3e2c3ca2e6448976611a8ddf837a9f188a3a6e7 | yes |
| `02_STEP_STL/od_c01_frame_C1_v02.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | yes |
| `02_STEP_STL/od_c01_assembly_C1_v02.step` | 07560bb0caafc1e986434eede5ae22abaef9f599437948145a8a3c18e2129749 | yes |
| `02_STEP_STL/od_c01_frame_C1_v02.stl` | 26bf61039e5fcbc210643fb38cd188e31a66e7b5b6e065da6eb93ffa216125db | yes |
| `02_STEP_STL/od_c01_frame_C1_v02.3mf` | 8023c837502843ba6a9c65b5bbbdb839652d1ea13585170d112e0dd1655f4073 | yes (brief; not listed in the REPORT) |
| `03_Sections/od_c01_frame_v02_front_y-3_plan.png` | 88b9cbd2ec70692def33d72d97840269a2f51e02f23887b8e44a9900b778611a | yes |
| `03_Sections/od_c01_frame_v02_left_asm_x0.png` | 3134671c9368d087f859d8a8b0fbb7bdc6e12c08c95ef92eb5d827fd4cee6afb | yes |
| `03_Sections/od_c01_frame_v02_left_asm_x37.png` | 4fe5dd02ceaadde3f871166e53edd1bf72f65d1b23823abea05f56af58f05d35 | yes |
| `03_Sections/od_c01_frame_v02_left_x-113_valve.png` | 5002f1a3966f5b237d8a8f1078d2f6d176e18e0535aed58ee2624c0277be86a9 | yes |
| `03_Sections/od_c01_frame_v02_left_x37_c03.png` | f277220f4e3d3e253c14fc5473606fa57f1169138a512c865ede0e7a1b374390 | yes |
| `03_Sections/od_c01_frame_v02_left_x65_bulkhead.png` | e0696dd0380a374523a56c29db2fa4d6ce4c7a33190308c5064eb7d270eecb87 | yes |
| `03_Sections/od_c01_frame_v02_top_asm_z-148.png` | 7af641ca4644a3b94eab4a29e570131f839209ead0ed8561281c38be0ff3332b | yes |
| `03_Sections/od_c01_frame_v02_top_asm_z32_mouth.png` | e6826257791fe8263b8f9d32a55170bec8dc4b797a7ce0f81266b96658c2a2b6 | yes |
| `03_Sections/od_c01_frame_v02_top_z-120_drain.png` | 830ff2b0ce9de90e13805289c4ea33e06df474e3c406a5ea62754e7b031df3d8 | yes |
| `03_Sections/od_c01_frame_v02_top_z-148_c04.png` | 7a49c0f651bc62ca766083d6a75211154f7f16c4e0af16fa721c9109dbfc9136 | yes |
| `03_Sections/od_c01_frame_v02_top_z-40_carrier.png` | 4f5e942c25f9f3876aa1098ddec6d4a84c648506a6b9e8daa15556588764d7a1 | yes |
| `03_Sections/od_c01_frame_v02_top_z-42_valve.png` | 69de67f64fdd19acb87af1e2e083ded63d9b55661cd495081842a6cf3bbd56dd | yes |
| `03_Sections/od_c01_frame_v02_top_z90_feet.png` | 56ebdb7cefd23dbb3645f2f482f9ac66d4659d6cd40a341f38677dbcb626f0d4 | yes |
| `00_Spec/inputs/OD-C03_pump_cradle.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | yes (brief; not listed in the REPORT) |
| `00_Spec/inputs/OD-C04_thermoblock_mount.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 | yes (brief; not listed in the REPORT) |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | yes (brief; not listed in the REPORT) |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | yes (brief; not listed in the REPORT) |
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | yes (brief; not listed in the REPORT) |

Every hash equals the brief's. The delivery must carry exactly these bytes.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 count | solid_count = 1, brep_valid = 1, naked_edges = 0 | +0 | plate STEP: solid_count 1, brep_valid 1 (BOPAlgo faults none, loose shells 0, loose faces 0), naked_edges 0 of 102 edges; the six other check-assembly solids 1/1/0 except OD-H11 brep_valid 0 (input, OD-C04 A-14) | PASS | `validity` | — |
| U-02 | 405.0 mm | 240.0 x 6.0 x 405.0 each in [spec - 0.1, spec + 0.1] | +0.1 | size 240.000 x 6.000 x 405.000; position x -120.000..120.000, y -6.000..0.000, z -305.000..100.000 | PASS | `envelope` | — |
| U-03 | 0.0 mm | (a) contacts clearance = 0 and interference <= 0 mm3; holes coaxial <= 0.10; plate|OD-H01 >= 2.0; plate|OD-H11 >= 10.0; OD-C03|OD-C04 >= 2.0; OD-H11 max z <= -85.0; OD-G01 v02 at its pose >= 2.0 to everything else; (b) N/A | +0 | governing: plate|OD-C03 contact 0.000 at (-2, 0, -171) and plate|OD-C04 0.000 at (-38, 0, -114), common volume 0.000 mm3 each; plate|foot box 0.000 at (-33, 0, -40); coaxial offsets 0.000 on all 8 mount holes (Ø3.4 over Ø4.0); plate|OD-H01 16.250 at (33.5, 0, -205.2); plate|OD-H11 16.4925 at (-9.66, 0, -140) (boolean not relied on; bbox-disjoint); OD-C03|OD-C04 8.000; OD-H11 max z -89.210; OD-G01 pose read back x->X, y->+Z, z->-Y, rear face y 205.000, mouth plane y 176.760, x +-50, z -18..82; OD-G01 least clearance 110.780 to OD-H11; path: clearance = lift at 10, 1, 0.1, 0.01, 0 for OD-C03, OD-C04, foot box | PASS (assumed: A-01, A-02, A-03) | `clearance, interference, bore_census + locate_bore on both solids, envelope` | A-01, A-02, A-03 |
| U-04 | 0.0 mm3 | named body re-read unchanged, no stray shells, valid after re-import | +0 | plate STEP: label od_c01_frame, 1 solid, 0 loose shells/faces, valid 1; reviewer rewrite of the delivered solid: volume delta 0.0 mm3, faces delta 0 (36), label kept, valid after 1; check assembly (not the gated target): 7 labels kept, rewrite deltas <= 3e-9 mm3 per part; OD-H11 input->assembly volume integral 0.0524 mm3 on an unsound body with identical 406 faces and 734 vertices (F2) | PASS | `step_roundtrip, compare_step, validity` | — |
| U-05 | 26 count | 1 plate, 20 Ø4.0, 4 Ø3.4, 2 Ø8.0 through-holes | +0 | 1 solid; 26 bores all through, length 6.000: 20 Ø4.000, 4 Ø3.400, 2 Ø8.000, each located at its spec axis with offset 0.000; faces 6 planar, 30 cylindrical (26 concave, 4 convex) | PASS | `feature_census, bore_census, locate_bore` | — |
| U-06 | 5.0 mm | >= 2.0 (Soft, min_wall wide) | +3 | (-115, -5.7, -42): web from OD-C07 hole (-113, -42) to the edge x -120; spacing 0.7 | PASS | `min_wall_wide(spacing=0.7)` | — |
| U-07 | 0.004975 mm | STL tol 0.01, angular <= 0.2310 rad; stl_max_sagitta <= 0.01; the 3MF carries the same mesh | +0.005025 | delivered STL vs B-rep mesh_deviation 0.004975 at (-77.66, -3.0, -226.75); re-mesh at 0.01 / 0.20 rad: 7068 triangles, sagitta 0.004972; STL 1 body, 0 naked edges, winding 1, volume 580358.524 vs B-rep 580355.904; 3MF: 7068 triangles, mm, no transform, all 7068 equal to the STL's, volume 580358.524 | PASS | `write_stl, mesh_sagitta, mesh_deviation, mesh_census, reviewer 3MF parse` | — |
| U-08 | — | applies to threaded parts; this target has none | — | — | N/A: by its row | `none (N/A by its row)` | — |
| D-01a | 5.0 mm | min_wall >= 0.8 | +4.2 | (-115, -5.7, -42), OD-C07 hole to the left edge; spacing 0.7; mesh corroboration 5.0025 | PASS | `min_wall(spacing=0.7)` | — |
| D-01b | 5.0 mm | min_wall >= 2.0 | +3 | (-115, -5.7, -42), OD-C07 hole to the left edge; spacing 0.7 | PASS | `min_wall(spacing=0.7)` | — |
| D-02 | 405.0 mm | each envelope size <= Kobra Max 3 build volume (420 x 420 x 500), flat | +15 | 240.0 x 405.0 on the bed, 6.0 tall | PASS (assumed: A-09) | `envelope` | A-09 |
| D-03a | 90.0 deg | every downward face >= 45 deg from horizontal, build +Y; none but the bed face | +45 | no downward point off the bed (200283 bed samples, 0 below 45); spacing 0.7 | PASS (assumed: A-14) | `overhang_census(build_dir=(0,1,0), spacing=0.7)` | A-14 |
| D-03b | 0.0 mm | span <= 5: none | +5 | no downward face off the bed; reviewer sections at y -0.001, -3, -5.999 each one piece of 96725.984 mm2 (straight vertical holes, no roof) | PASS | `overhang_census + reviewer sections` | — |
| D-04a | 3.4 mm | four feet holes Ø >= 3.25 | +0.15 | (+-110, -3, 90) and (+-110, -3, -295), all Ø3.400 through | PASS (assumed: A-12) | `locate_bore` | A-12 |
| D-05a | 14.0 mm | material >= 8.0 across around each Ø4.0 hole | +6 | (-113, -3, -42) and (-113, -3, -148.5) at 180 deg: material r 2.0..7.0; 4320 rays + exact 180 deg ray, 0 unread | PASS (assumed: A-11) | `bore_census, radial_extent` | A-11 |
| D-05b | 4.0 mm | twenty insert holes Ø4.0 +- 0.05, depth >= 5.7 | +0.05 | all 20 Ø4.000, length 6.000 through (depth margin +0.3) | PASS (assumed: A-11) | `bore_census, locate_bore` | A-11 |
| D-06a | 5.0 mm | >= 1.0 | +4 | (-115, -5.7, -42); spacing 0.7 | PASS | `min_wall(spacing=0.7)` | — |
| D-07 | — | none: no fit-critical bores | — | — | N/A: by its row | `none (N/A by its row)` | — |
| J-05 | 5.0 mm | >= 3.0 around each of the twenty insert holes | +2 | min_wall 5.000 at (-115, -5.7, -42); ring wall r 7.0 - 2.0 = 5.0 at (-113, -42) and (-113, -148.5), 180 deg | PASS | `min_wall(spacing=0.7), radial_extent` | — |
| E-06 | — | no bosses on this part | — | — | N/A: by its row | `none (N/A by its row)` | — |
| REQ-01 | 4.0 mm | four Ø4.0 +- 0.05 through at (+-35, -40), (+-35, -60), offset <= 0.10 | +0.05 | all four Ø4.000 through, offset 0.000 (offset margin +0.10) | PASS (assumed: A-01) | `locate_bore` | A-01 |
| REQ-02 | 4.0 mm | four Ø4.0 +- 0.05 at (+-40, -148), (+-40, -114), offset <= 0.10, coaxial with OD-C04 | +0.05 | all four Ø4.000 through, offset 0.000; OD-C04 Ø3.4 axes coaxial, offset 0.000 | PASS (assumed: A-02) | `locate_bore` | A-02 |
| REQ-03 | 4.0 mm | four Ø4.0 +- 0.05 at (-4, -239), (-4, -171), (37, -239), (37, -171), offset <= 0.10, coaxial with OD-C03 | +0.05 | all four Ø4.000 through, offset 0.000; OD-C03 Ø3.4 axes coaxial, offset 0.000 | PASS (assumed: A-03) | `locate_bore` | A-03 |
| REQ-04 | 4.0 mm | four Ø4.0 +- 0.05 at (65, -45 / -105 / -165 / -225), offset <= 0.10 | +0.05 | all four Ø4.000 through, offset 0.000 | PASS (assumed: A-04) | `locate_bore` | A-04 |
| REQ-05 | 3.4 mm | four Ø3.4 +- 0.1 through at (+-110, 90), (+-110, -295), offset <= 0.10 | +0.1 | all four Ø3.400 through, offset 0.000; each concentric with its R10 corner (web 8.3) | PASS (assumed: A-12) | `locate_bore` | A-12 |
| REQ-06 | 8.0 mm | two Ø8.0 +- 0.1 through at (-80, -120), (-80, -230), offset <= 0.10 | +0.1 | both Ø8.000 through, offset 0.000 | PASS (assumed: A-13) | `locate_bore` | A-13 |
| REQ-07 | 0.0 mm | top face y = 0.00 +- 0.10, 6.0 +- 0.1 thick, one plane | +0.1 | max_y 0.000, size_y 6.000; exactly one +Y planar face, y extent 0.000..0.000, area 96725.984 mm2; sections one piece at every level | PASS | `envelope, face listing, reviewer sections` | — |
| REQ-08 | -89.21 mm | OD-H11 max z <= -85.0 and clearance(plate, OD-H11) >= 10.0 | +4.21 | OD-H11 max z -89.210 (outlet pins); clearance 16.4925 at (-9.66, 0, -140), margin +6.4925 | PASS (assumed: A-02) | `envelope, clearance` | A-02 |
| REQ-10 | 4.0 mm | four Ø4.0 +- 0.05 at (-113, -42), (-71, -42), (-113, -148.5), (-71, -148.5), offset <= 0.10; against the pattern until the OD-C07 STEP | +0.05 | all four Ø4.000 through, offset 0.000; checked against the spec pattern only (no OD-C07 STEP) | PASS (assumed: A-17) | `locate_bore` | A-17 |
| REQ-09 | — | Soft bench gate: flat in service; INCONCLUSIVE with a risk rating | — | not geometric; answered by the first print (F1) | INCONCLUSIVE (Soft bench gate, F1) | `none (bench)` | A-10, A-14 |

Rulings on the brief's questions:

- **U-03, OD-H11 booleans.** Gated on distance as the brief says: plate|OD-H11 16.4925 (≥ 10.0), OD-C03|OD-H11 28.409, OD-H01|OD-H11 38.150, box|OD-H11 25.613, OD-G01|OD-H11 110.780. `common_volume` read plate|OD-H11 0 mm³ only because the bounding boxes are apart (no boolean was run); OD-C04|OD-H11 is INCONCLUSIVE (brep_valid 0), and it is OD-C04's own row, not this job's. Nothing gated rests on an OD-H11 boolean.
- **U-03, the carrier.** The foot box `od_c05_foot_reference_A01` (x ±55, y 0 … 4, z −70 … −26, measured) touches the plate (0.000, 0 mm³), sits 37.0 in front of OD-C04's foot and 11.0 behind the tray zone; its hole pattern REQ-01 is checked on the plate alone. Everything about the carrier rests on A-01 until OD-C05 delivers.
- **U-04.** Gated on the target's named body `od_c01_frame`, as the row says: the reviewer's rewrite of the delivered solid reads volume delta 0.0 mm³, faces delta 0, label kept, valid after 1. The designer's OD-H11 reading in the check assembly is confirmed (0.0524 mm³) and ruled INCONCLUSIVE on an unsound body, not a FAIL: faces (406) and vertices (734, to 1e-5 mm) are identical, and a second write moves it 2.9e-9 mm³. It is F2 (observation), with the evidence.
- **U-07, 3MF.** Parsed by the reviewer: `3D/3dmodel.model`, unit millimetre, no transform, 3484 vertices, 7068 triangles, box x ±120, y −6 … 0, z −305 … 100, signed volume 580 358.524 mm³; all 7068 triangles equal the STL's at 0.001 mm. The orchestrator's 7068 / 580 358.52 is confirmed.
- **REQ-10.** The four holes sit at the A-17 pattern; there is no OD-C07 STEP, so the coaxial clause waits on it (A-17, whose source spec is at REVISE).

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 plate | 1 solid, 240 x 6 x 405, 6 planar faces, 4 convex R10 corner cylinders | 1 solid, 240.000 x 6.000 x 405.000, 6 planar, 4 convex cylinders, corner rays from the feet axes read r 10.0 | PASS |
| F02 carrier insert holes x4 | Ø4.0 through at (+-35, -40), (+-35, -60) | 4 x Ø4.000 through, offset 0.000 | PASS |
| F03 OD-C04 insert holes x4 | Ø4.0 through at (+-40, -148), (+-40, -114) | 4 x Ø4.000 through, offset 0.000 | PASS |
| F04 OD-C03 insert holes x4 | Ø4.0 through at (-4 / 37, -239 / -171) | 4 x Ø4.000 through, offset 0.000 | PASS |
| F05 bulkhead insert holes x4 | Ø4.0 through at (65, -45 / -105 / -165 / -225) | 4 x Ø4.000 through, offset 0.000 | PASS |
| F05b OD-C07 insert holes x4 (WP-04) | Ø4.0 through at (-113 / -71, -42 / -148.5) | 4 x Ø4.000 through, offset 0.000 | PASS |
| F06 feet holes x4 | Ø3.4 through at (+-110, 90 / -295) | 4 x Ø3.400 through, offset 0.000 | PASS |
| F07 drain holes x2 | Ø8.0 through at (-80, -120 / -230) | 2 x Ø8.000 through, offset 0.000 | PASS |
| F08 clean-up / census totals | 6 planar, 30 cylindrical (26 concave, 4 convex), 0 other, 26 bores | 6 planar, 30 cylindrical (26 concave, 4 convex), 0 other, 26 bores | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | gravity | Plate lies flat, bottom on the counter via four feet at (+-110, 90 / -295) enclosing the plate COM (0.09, -102.4) and every placed part; each mount stands on y 0 with 0 mm3 overlap. | YES |
| P2 | function chains | Mount foot Ø3.4 over plate Ø4.0 insert holes coaxial (offset 0.000) on all 8 placed mount holes; OD-C05, bulkhead, OD-C07 patterns at spec points; drains at x -80 in the wet zone, (-80, -120) under the OD-C07 hose window. | YES |
| P3 | moving parts | No moving part; assembly path checked: OD-C03, OD-C04 and the carrier box lowered along -Y read clearance = lift at 10, 1, 0.1, 0.01, 0 mm; column under the mouth (x +-50, z -18..82) empty from y 0 to 176.76. | YES |
| P4 | grip, reach, insertion | Inserts go in from the top before the mounts; feet screws from below; group head mouth faces down at y 176.76 over the tray zone; nearest insert to an edge is 5.0 from x -120, reachable with an iron. | YES |
| P5 | absurdity | Group head front over tray, thermoblock behind (z -140..-89), pump across the back (axis along X, z -232..-178), valve mount left, electric zone right of x 65: the Dedica layout; 240 x 405 x 6 PETG base 737 g is in proportion, larger than a Dedica footprint to carry tank and bay. | YES |
| P6 | floating, embedded, mirrored, upside-down | No overlap anywhere (all sound pairs 0 mm3); housing upright (rear face y 205 above mouth y 176.76, proper rotation); OEM parts sit in their mounts; the housing floats only because OD-C05 is not built (A-01, reference box). | YES |

## 5. Positive controls

Mutants are made from the delivered STEP (or the delivered STL and 3MF) by the reviewer's scripts `rv_d_controls.py` and `rv_e_wallctl.py`; each was gated with the same band and limit as the real row.

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity | plate plus a loose 5 mm cube: solid_count 2 | FAIL |
| envelope | front edge moved +0.5 in z: size_z 405.5 | FAIL |
| feature_census | insert hole (65, -225) filled: 25 bores | FAIL |
| bore_census | same mutant: 19 Ø4.0 bores | FAIL |
| locate_bore offset | REQ-10 hole (-71, -42) moved +0.5 in x: offset 0.5 | FAIL |
| locate_bore diameter | feet hole (-110, 90) resized Ø3.2: 3.2 < 3.25 | FAIL |
| clearance | OD-H11 placed 7.0 lower: 9.49 < 10.0 | FAIL |
| clearance contact | OD-C04 lifted 0.5: 0.5 != 0 | FAIL |
| interference | OD-C03 lowered 0.5 into the plate: 2054.87 mm3 | FAIL |
| overhang_census | Ø10 x 3 pocket from the bed face at (0, -270): 0.0 deg | FAIL |
| top face count (REQ-07) | 0.5 deep 20 x 20 pocket in the top face: 2 planes | FAIL |
| radial_extent | OD-C07 hole moved to x -116.5: 7.0 across < 8.0 | FAIL |
| min_wall / min_wall_wide | OD-C07 hole moved to x -117.5: 0.5 (D-01a, J-05, U-06 all FAIL) | FAIL |
| compare_step (U-04) | hole-removed mutant file: faces delta 1, volume delta 75.40 mm3; renamed body: labels 0 | FAIL |
| mesh_sagitta / mesh_deviation | STL at 0.1 mm / 0.5 rad: 0.0482 > 0.01 | FAIL |
| mesh_census | delivered STL with one triangle deleted: 3 naked edges | FAIL |
| 3MF same-mesh compare | 3MF with one vertex moved 0.5: 7030 of 7068 triangles match | FAIL |

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | SOFT_GATE_MISS | not measured (bench) → flat in service (Soft bench gate) | — | whole plate, corners (+-120, -6, 100 / -305) | no | MEDIUM | an unribbed 240 x 405 x 6 PETG plate printed flat can lift at the corners and creep under a 1 kg tank; the three mounts seat on its top face, so warp shows as rocking; only a print can tell | first print with brim, measure flatness under the mounts and at the feet; if it rocks, C2 ribs or a two-piece C3 |
| F2 | U-04 | OBSERVATION | 0.0524 mm3 → volume delta <= 0.001 (band) on re-read | -0.0514 | check assembly body od_h11_thermoblock (input OD-H11 as placed vs its copy in the assembly STEP) | no | LOW | ruled INCONCLUSIVE, not FAIL: OD-H11 is brep_valid 0 (BOPAlgo_InvalidCurveOnSurface) on input, so its volume integral is not a sound measurement; its 406 faces and 734 vertices are identical to 1e-5 mm and a second write moves it 2.9e-9 mm3; U-04 gates the target's named body, which round-trips exactly; every OD-H11 row here rests on distances, not on its volume | repair or re-export OD-H11 in its own job (OD-C04 A-14); no change to this plate |

The open assumptions weighed (brief): A-01 carries REQ-01 and the housing pose (the carrier is a box); A-02 and A-03 carry every mount joint (read back exactly, contacts 0, holes coaxial 0.000); A-05 / A-17 carry REQ-10 and the valve zone (OD-C07's spec is at REVISE: its pattern or pose may move the four holes); A-06 tray zone is clear under the mouth (foot box 11.0 behind it, housing mouth y 176.76 above it); A-09 bed 420 leaves +15 on the 405 length and is from memory, not the machine file; A-10 / REQ-09 is F1; A-11: 5.7 inserts in 6.0 through-holes, depth margin +0.3, ring 14.0 across; A-17's 5.0 web measured 5.000.

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| The 5.0 web between the OD-C07 outer inserts and the left edge | Measured 5.000 (min_wall at (-115, -5.7, -42), mesh 5.0025) and ring material r 2.0..7.0 at 180 deg: J-05 +2.0, D-05a 14.0 across (+6.0); after a Ø4.6 insert about 4.7 remains, above J-05's 3.0; edge bulge on pressing is a low, print-checkable risk resting on A-11 and A-17 (the OD-C07 pattern may still move). |
| U-04 on the check assembly for OD-H11 (0.0524 mm3) | Confirmed 0.0524 mm3 (159766.4574 input vs 159766.4050 in the assembly) with faces and vertices identical; ruled INCONCLUSIVE on an unsound body, not a FAIL; U-04 on the target plate PASS (reviewer rewrite delta 0.0 mm3); filed as F2, non-blocking. |
| REQ-09 flatness (Soft) | Not measurable in CAD; INCONCLUSIVE by its row, risk MEDIUM (F1); the first print answers it. |
