# RV02 — od_t01_rig_v02 (20261002-od-t01-pressure-test-rig) — 2026-10-03 UTC

Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.3 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`, `briefs/WP-05_designer.md`) · report `01_CAD/REPORT_od_t01_rig_v02.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-05, A-07, A-08, A-09, A-10, A-11, A-12

One valid 240 x 160 x 120 solid; every hard row of spec 1.3 re-measured and met (least margins REQ-03 pair-B +0.100, D-03a +0.100 deg, REQ-01 +0.100 with 5.000 under each head, REQ-04 +6.755); RV01 F1 and F2 closed; REQ-08 INCONCLUSIVE, rated MEDIUM for head bearing (about 47 MPa) the hand calculation omits.

All measurements were made with the reviewer's own scripts in `reviews/RV02_work/`: `rv_part.py`, `rv_print.py`, `rv_rt.py`, `rv_pose.py`, `rv_static.py`, `rv_motion.py`, `rv_sections.py`, `rv_controls.py` and `rv_control_flank.py`. Every one read the delivered STEP from disk. The housing set was posed from `od_g01_assembly_C1_v03.step` by spec §2: housing x → X, y → +Z, z → −Y, origin (0, 110.06, 0). That is +90° about X, a proper rotation, and the axis mapping was checked. The solids were identified by measurement: the housing is the 100 × 100 solid with four Ø4.0 bores at (±44, ±44); OD-G10 is the solid longer than 120 (185.1); OD-G04 is the remaining one. The designer's assembly file was not used for any gate. Bands are from GATES §0: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. No CAD code, sweep folder, designer JSON or log was read.

**RV01 follow-up.**
- **F1 (REQ-08, plate) is closed for the items it named.** The plate is y 135.000 … 160.000, and the counterbore floors are at y 140.000, which leaves 5.000 under each head. The measured window section at x 0 is 1187.5 mm², with Z 4948.1 mm³. That gives σ 9.59 MPa and a factor of 4.17 against 40 MPa, which agrees with spec 1.3 §4. Head pull-through is τ 8.5 MPa. REQ-08 is re-rated below (F1 of this review) for head bearing, which the hand calculation does not cover.
- **F2 (REQ-03 apex band) is closed.** The apex is at z 42.5006 against 42.51 ± 0.16, a margin of +0.151. At R 29.9 the apex falls at 42.359, inside 42.35 with +0.009 to spare, so the band now stacks with R ± 0.1 without relying on the 0.005 band.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_t01_rig_C1_v02.step` | 18c9de8f013cb7ce84eba3ce104ab6fb01fc84f79f8524140cfadb9d3feaf810 | yes |
| `02_STEP_STL/od_t01_rig_C1_v02.stl` | 183e58f0eda9287450d79d1a15aa3a4dabcf694449a6b82ae3a9ef9f24bfbd3f | yes |
| `02_STEP_STL/od_t01_assembly_C1_v02.step` | c6caa17478e570e0b9200d813ee69fa674d68d2f9d6a91db216f4a5a1f18c072 | yes |
| `01_CAD/REPORT_od_t01_rig_v02.md` | c7a125fa3d755d6dfa638d4d0253ddd2e21adf6d7c0c76b012de08095c1c77c9 | yes |
| `01_CAD/DESIGN_PLAN.md` | 544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d | yes |
| `00_Spec/DESIGN_SPEC.md` | 9f329e11a2b8eba3921e81eddcc593e203550b65c65d588e11b2d9bb11330195 | yes |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | yes |
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | yes |
| `reviews/RV01_od_t01_rig_v01.md` | ee5a1b930bf55f64d6e041b728d871428cedcfed869fcbb38a3c06e5c0dc1f9d | yes |
| `03_Sections/od_t01_rig_v02_z0_assembly.png` | 7b37fd6df626973922208a3ab41d34c29418313a9028223cf6a7826898dbe96b | yes |
| `03_Sections/od_t01_rig_v02_z44_assembly.png` | b93398a4d4617a43bebaaf6a8ba366fc9e450b97ad79cc4e571e42efce95cfb7 | yes |
| `03_Sections/od_t01_rig_v02_x44.png` | 20f241a6cdc4deef5b6397a1e7d0f2ea11895c2877f000c3cd60b41e9009cb33 | yes |
| `03_Sections/od_t01_rig_v02_x0.png` | 4d95cd78d17258d41d1f9b776a85cdfe45ad407591926a06a44c5d43d7cc5e5a | yes |
| `03_Sections/od_t01_rig_v02_y5.png` | 9ea632d7cbf6e3c9c9901269be5b5b54a501dc95b7e20ad5108fc6387a2efd29 | yes |
| `03_Sections/od_t01_rig_v02_y147.png` | 0ceb47485189140a97e0728a5c98ded17ff94b60b12e3d2f8ad0c89dd84df4df | yes |

The REPORT lists the first three files, the six sections and the REPORT itself. The brief lists the spec, the inputs, the plan and RV01, and every one matches the brief. The delivery must carry exactly the STEP and STL bytes above. A reviewer re-mesh of the STEP at 0.01 mm / 0.10 rad reproduces the delivered STL byte for byte.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 bool | solid_count = 1, brep_valid = 1, naked_edges = 0 | +0 | solid_count 1, brep_valid 1 (BRepCheck, volume, BOPAlgo: no faults), naked_edges 0; label od_t01_rig; AP242, mm | PASS | `validity` | — |
| U-02 | 240 mm | 240.0 x 160.0 x 120.0 each in [spec - 0.1, spec + 0.1]; position reported apart | +0.1 | size 240.000 x 160.000 x 120.000 (each margin +0.100); position x -120.000..120.000, y 0.000..160.000, z -60.000..60.000, on the datum | PASS | `envelope` | — |
| U-03 | 0 mm | (a) seat clearance = 0; interference <= 0 every pair; rig to housing elsewhere, OD-G04, OD-G10 >= 2.0; (b) dy 0..-30 steps <= 2.0: interference <= 0 | +0 | (a) seat clearance 0.000 at (21.25, 135.00, 21.18), plate underside / housing rear face; interference rig|housing 0.000 mm3, rig|OD-G04 0.000 mm3; rig below y 134.9 to housing 15.100 at (65.1, 134.9, 40.0) chamfer root (+13.1); rig to OD-G04 5.000 at (-21.25, 135.0, 21.18) over the pair-A boss (+3.000); rig to OD-G10 13.689, not inside (+11.689; common_volume INCONCLUSIVE on OD-G10, brep_valid 0, read by the spec's clearance fallback); (b) 31 poses dy 0..-30 every 1.0: interference rig|housing and rig|OD-G04 0.000 mm3 at every pose, OD-G10 least 13.689 at dy 0, never inside | PASS (assumed: A-01) | `clearance, interference (common_volume); OD-G10 clearance fallback per REQ-04` | A-01 |
| U-04 | 2.3e-10 mm3 | named body re-read unchanged, no stray shells, valid after re-import | -2.3e-10 | delivered STEP read: 1 solid, label od_t01_rig, AP242, valid; compare_step against the delivered file: volume delta 0.000, faces delta 0; reviewer re-export of the read solid: volume delta 2.3e-10 mm3 (inside the 0.001 band), faces delta 0 (54), labels equal, valid after | PASS | `compare_step, step_roundtrip` | — |
| U-05 | 13 count | plan counts: 1 plate, 2 walls (z -60..+40), 1 base, 4 corner chamfers, 4 x 3.4 holes + 4 x 6.5 counterbores (teardrop), 1 hub window (R 30 + teardrop), 4 x 4.5 bench holes (teardrop) | +0 | 13 bores (4 x 3.400 360 deg, 4 x 6.500, 1 x 60.000, 4 x 4.500, each teardrop bore 269.8 deg + 2 flanks); faces 41 planar + 13 concave cylinders, 0 other; 4 chamfer planes 10 x 10; wall inner faces x +-75 at z -60..40; see feature census | PASS | `feature_census, bore_census, locate_bore` | — |
| U-06 | 5 mm | >= 2.0 (Soft) | +3 | (-45.10, 135.00, -47.04) plate under the (-44, -44) counterbore | PASS | `min_wall_wide` | — |
| U-07 | 0.004997 mm | STL at tol 0.01, angular <= 4 acos(1 - 0.01/30) = 0.1033 rad; stl_max_sagitta <= 0.01 | +0.005003 | reviewer re-mesh of the STEP at 0.01 mm / 0.10 rad is byte-identical to the delivered STL (SHA 183e58f0...), so the STL is the D5 export from a cleared triangulation at the REPORT's tolerance; sagitta 0.0050 at (-21.63, 141.25, 20.78); 5752 triangles; mesh_census 1 body, 0 naked edges, winding consistent, volume +12.8 mm3 vs B-rep; mesh_deviation 0.0050; min_wall_mesh 5.000; 3MF at J5 | PASS | `write_stl, stl_max_sagitta, mesh_census, mesh_deviation, min_wall_mesh` | — |
| U-08 | — | applies to threaded parts; this target has none | — | — | N/A: the row applies to other parts | `N/A by the spec row` | — |
| D-01a | 5 mm | >= 0.8 | +4.2 | (-45.10, 135.00, -47.04) plate under a counterbore | PASS | `min_wall` | — |
| D-01b | 5 mm | >= 2.0 (webs between counterbores and window, and around bench holes, included) | +3 | (-45.10, 135.00, -47.04) plate under a counterbore; mesh corroboration min_wall_mesh 5.000 | PASS (assumed: A-08) | `min_wall` | A-08 |
| D-02 | 240 mm | each size <= Kobra Max 3 volume 420 x 420 x 500, lying on the rear face: 240 x 160 on the bed, 120 tall | +180 | bed 240.000 x 160.000 (margins +180, +260), height 120.000 (+380) | PASS (assumed: A-09) | `envelope` | A-09 |
| D-03a | 45.1 deg | >= 45 (build +Z); crowns of the four 3.4 holes excepted by position | +0.1 | least 45.100 at (21.25, 135.00, 21.18) window teardrop flank, on the reviewer's copy with the four 3.4 holes plugged (r 1.8, y 135..140); sampling bound 0.009 deg, 0 samples below 45; per kind cylinder 45.1, plane 45.1. Unplugged: least 0.0 at (-44.0, 135.0, -42.3) on a 3.4 crown; the 312 samples below 45 all vanish with the plugs | PASS (assumed: A-10) | `overhang_census(build_dir=(0,0,1))` | A-10 |
| D-03b | 3.4 mm | span <= 5: the four 3.4 crowns bridge <= 3.4; nothing else bridges | +0 | flat_ceiling_spans 0.000 (no flat ceiling anywhere); crowns are 3.400 bores (360 deg) along Y, 5.0 long, y 135..140, seen in reviewer sections y 137.5 and x 44; margin +1.600 against 5 | PASS (assumed: A-10) | `flat_ceiling_spans, bore_census, reviewer sections` | A-10 |
| D-04a | 3.4 mm | housing screw holes >= 3.25; bench holes >= 4.25 | +0.15 | 4 x 3.400 at (+-44, 135..140, +-44); 4 x 4.500 at (+-105, 0..10, +-40) (+0.250) | PASS | `bore_census, locate_bore` | — |
| D-06a | 5 mm | >= 1.0 | +4 | (-45.10, 135.00, -47.04) | PASS | `min_wall` | — |
| D-07 | — | none: clearance holes only | — | — | N/A: the row applies to other parts | `N/A by the spec row` | — |
| J-05 | — | applies to threaded holes in this part; it has none | — | — | N/A: the row applies to other parts | `N/A by the spec row` | — |
| REQ-01 | 5 mm | 4 x 3.4 +- 0.1 at (+-44, +-44), offset <= 0.10 from the posed insert bores, through; 6.5 +- 0.1 counterbores y 160.0 to y 140.00 +- 0.10; 5.0 +- 0.1 of plate under each head | +0.1 | plate under each head 5.000 (floor y 140.000 - underside 135.000); hole axes 0.000 off the posed insert-bore axes (4.000, y 129.3..135.0); 4 x 3.400 open both ends y 135.000..140.000; 4 x 6.500 y 140.000..160.000, floor closed; every sub-margin +0.100 | PASS (assumed: A-01) | `locate_bore, bore_census` | A-01 |
| REQ-02 | 135 mm | underside one plane at y 135.00 +- 0.10 over x +-50, z +-50; housing rear face on it | +0.1 | one -Y planar face at y 135.000 (x +-90, z +-60); 5712 grid points over x, z +-50 off the window and holes: material at y 135.002 and air at y 134.998 at every one; seat clearance 0.000 (U-03) | PASS (assumed: A-01) | `envelope, BRep classifier grid, clearance` | A-01 |
| REQ-03 | 10.97 mm | R 30.0 +- 0.1; roof 45.1 +- 1 deg toward +Z, apex z +42.51 +- 0.16; OD-G04 hub tube >= 2.0; pair-B axes >= 10.87 from the window face | +0.1 | pair-B axis (10.64, -15.78) to window face 10.970 at (16.78, 135.0, -24.87) (+0.100); other pair-B axis (-9.31, 16.60) 11.689; window 60.000 offset 0.000, through y 135..160 (R margin +0.100); flanks 45.100 deg (+1.000); apex z 42.5006 by radial_extent at y 135.5, 147.5, 159.5 (+0.1506); OD-G04 to rig 5.000 (+3.000) | PASS (assumed: A-05, A-12) | `bore_census, locate_bore, flank-plane normals, radial_extent, clearance, reviewer sections` | A-05, A-12 |
| REQ-04 | 11.755 mm | (a) phi -60..+15 deg, steps <= 5: clearance >= 5.0; (b) phi -50, dy -15, dz 0..200, steps <= 5.0: interference <= 0, read as clearance > 0 with inside False | +6.755 | (a) 76 poses every 1 deg: least 11.755 at phi +15 at (75.0, 90.4, 40.0), +X wall front end, never inside; phi > 0 turns the handle to +X (max_x 67.7 / 92.0 / 114.6 at -10 / 0 / +10); (b) 81 poses every 2.5: least 28.689 at dz 50, never inside; lift phi -50, dy -15..0 (16 poses): least 13.689; joint grid phi -60..+15 x dy -15..0 (176 poses): least 11.755, never inside | PASS (assumed: A-07) | `clearance (OD-G10 fallback)` | A-07 |
| REQ-05 | 52.296 mm | >= 50.0 above the base top y 10 | +2.296 | OD-G10 locked lowest point y 62.296 (reviewer pose) | PASS (assumed: A-07) | `envelope` | A-07 |
| REQ-06 | 0 mm3 | 4 x 4.5 +- 0.1 at (+-105, +-40), offset <= 0.10, through; four 8 cylinders y 10..300 interference = 0 | +0 | probes common volume 0.000 mm3 each; 4 x 4.500 offset 0.000, through y 0..10 (+0.100) | PASS (assumed: A-11) | `locate_bore, common_volume` | A-11 |
| REQ-07 | 0 mm3 | four 6 cylinders y 160..300 on the screw axes: interference = 0 | +0 | common volume 0.000 mm3 each; least clearance 0.250 to the counterbore teardrop rim at (46.30, 160.0, 46.29) | PASS | `common_volume, clearance` | — |
| REQ-08 | — | Soft: holds 3.06 kN on four screws with no visible yield or crack at the test pressure (bench) | — | not geometric; window section at x 0 measured Z 4948.1 mm3, sigma 9.59 MPa, factor 4.17; see F1 | INCONCLUSIVE (Soft, bench; rated in F1) | `bench test; A-02 hand calculation re-checked on the measured section` | A-02 |

Motion was swept as follows:
- U-03b: the housing set at dy 0 … −30, every 1.0 (31 poses).
- REQ-04a: φ −60° … +15°, every 1° (76 poses).
- REQ-04b: dz 0 … 200, every 2.5, at φ −50° and dy −15 (81 poses).
- The joining lift: φ −50°, dy −15 … 0, every 1.0 (16 poses).
- φ and dy swept together on a grid: φ −60° … +15° every 5°, dy −15 … 0 every 1.5 (176 poses).

Together these cover the insertion path from first contact (dz 200) to the locked pose, and any bayonet path that turns and lifts at once. Every OD-G10 row uses the spec's reading, `clearance > 0` with `inside == False`. OD-G10 is confirmed `brep_valid` 0, and `common_volume` reads it INCONCLUSIVE. No pose was inside.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 frame profile (plate, 2 walls, base, 4 chamfers) | plate y 135..160 x +-90 (spec 1.3); walls x +-(75..90) z -60..+40; base y 0..10 x +-120; 4 chamfer planes 10 x 10 at 45 deg | plate y 135.000..160.000 x +-90; walls x +-(75..90), end faces at z 40.000; base y 0..10 x +-120; 4 chamfer planes 10 x 10 at 45 deg; 41 planar faces | PASS |
| F02 hub window R 30 + teardrop | 1 bore 60.0 along Y through the plate, 2 flanks 45.1 deg, apex z 42.51 | 60.000, y 135..160, through, 269.8 deg; flanks 45.100 deg; apex z 42.5006 | PASS |
| F03 4 x 6.5 counterbore + teardrop | 4 bores 6.5, y 140.00..160 (spec 1.3), floor closed, 8 flanks, apex 4.61 | 4 x 6.500 at (+-44, +-44), y 140.000..160.000, floor closed; 8 flanks 45.100 deg; apex 4.604 from the axis | PASS |
| F04 4 x 3.4 hole (no teardrop) | 4 bores 3.4 360 deg, y 135..140 | 4 x 3.400, 360 deg, y 135.000..140.000, open into the counterbore | PASS |
| F05 4 x 4.5 bench hole + teardrop | 4 bores 4.5 through the base at (+-105, +-40), 8 flanks, apex 3.19 | 4 x 4.500, y 0..10 through; 8 flanks 45.100 deg; apex 3.188 | PASS |
| F06 name and export | body od_t01_rig, AP242 STEP, STL 0.01 mm / 0.10 rad | label od_t01_rig, AP242, mm; STL byte-identical to the reviewer re-mesh at 0.01 / 0.10 | PASS |
| F07 check assembly | rig + housing + OD-G04 + OD-G10 at the spec 2 pose | file present, hash matches the brief; not used for any gate (the reviewer posed the set from the v03 input) | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

These answers come from the reviewer's sections in `reviews/RV02_work/sections/`. With the housing set: z 0, z 44 and x 0. Rig only: y 147.5, y 137.5, y 5, x 44 and z 50. `nothing_clipped` reads 0 on all eight.

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | gravity | Base 240 x 120 on the bench at y 0, centre of mass (0, 85.8, -3.6) inside the footprint; the housing hangs under the plate on four screws and the brew load pulls it into them, as on OD-C05 (section z 0). | YES |
| P2 | function chains | Screw heads on 5.0 of plate, axes 0.000 off the inserts; hub reached through the R 30 window from above; load path plate - walls - base - bench holes is a closed ring (sections z 0, z 44, x 0). | YES |
| P3 | moving parts | OD-G10 turns phi -60..+15 with >= 11.755, goes in at phi -50 along +Z with >= 28.689, lifts with >= 13.689, and every phi x dy pose in between keeps >= 11.755; the housing set offers up 30 with no interference. | YES |
| P4 | grip, reach, insertion | Screw axes clear to y 300 (6 probes) down 20-deep counterbores, bench-screw axes clear to y 300 (8 probes); the handle leaves at the open front where the walls stop at z +40; 52.3 under the portafilter for a tray. | YES |
| P5 | absurdity | A 240 x 160 x 120 PLA frame of 1.42 kg holding a 100 x 100 group head reads as an ordinary bench test fixture. | YES |
| P6 | floating, embedded, mirrored, upside-down | Seat clearance 0.000 with 0.000 mm3 interference; the pose is a proper rotation (x->X, y->+Z, z->-Y, checked); teardrops point +Z, the build direction (section y 147.5); handle on +X at about 34 deg as in v03. | YES |

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity (solid_count) | rig plus a copy relocated 300 in X: 2 | FAIL |
| validity (naked_edges) | rig shell with one face removed: 6 | FAIL |
| envelope (U-02, D-02) | base resized +1.0 at +X: 241 | FAIL |
| feature_census / bore_census (U-05) | 3.4 hole at (44, 44) removed (plugged): 12 | FAIL |
| locate_bore offset (REQ-01) | 3.4 hole at (44, 44) relocated +0.5 in X: 0.5 | FAIL |
| locate_bore diameter (D-04a, REQ-01) | 3.4 hole at (44, 44) resized to 3.2: 3.2 | FAIL |
| min_wall (D-01a, D-01b, D-06a) | counterbore (-44, -44) deepened to y 135.6: 0.6 under the head: 0.6 | FAIL |
| min_wall_wide (U-06) | same deepened counterbore: 0.6 | FAIL |
| overhang_census (D-03a) | plugged copy with a 10-wide flat-roofed slot through the plate, x 55..65, z 0..5: 0 | FAIL |
| flat_ceiling_spans (D-03b) | same slot: 10 | FAIL |
| clearance (REQ-04 sweep) | block x 62..75, y 80..100, z 25..40 on the +X wall's inner front, phi -60..+15: 2.655 | FAIL |
| clearance (REQ-03 pair-B) | window filled and re-cut at R 29.5 (no teardrop): 10.47 | FAIL |
| clearance (U-03 seat contact) | housing relocated 0.2 down: 0.2 | FAIL |
| interference / common_volume (U-03, REQ-06, REQ-07) | housing relocated 0.5 up into the plate: 3436 | FAIL |
| interference / common_volume (REQ-07 probe) | boss r 4 on the (44, 44) screw axis above the plate: 141.4 | FAIL |
| compare_step (U-04) | deepened counterbore shape compared with the delivered STEP: 106.1 | FAIL |
| stl_max_sagitta (U-07) | rig re-meshed at 0.1 mm / 0.5 rad: 0.04945 | FAIL |
| mesh_census (U-07, V-05) | delivered STL with its last triangle removed: 3 | FAIL |
| mesh_deviation (U-07) | coarse STL (0.1 mm) against the delivered B-rep: 0.04945 | FAIL |
| min_wall_mesh (D-01b corroboration) | STL of the deepened counterbore mutant: 0.6 | FAIL |
| underside grid classifier (REQ-02) | 1.5-deep pocket x 45..49, z -20..-10 in the underside: 40 | FAIL |
| radial_extent apex (REQ-03) | rig relocated +0.5 in Z: 43 | FAIL |
| flank-plane normals (REQ-03 roof angle) | rig rotated 2 deg about Y: flanks 47.1 / 43.1 deg | FAIL |

Every check family used in §2 FAILs on its mutant, so no gate rests on a blind check. The mutants are built in `rv_controls.py` and `rv_control_flank.py`, and the mutant meshes are in `reviews/RV02_work/mutants/`.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-08 | SOFT_GATE_MISS | not measurable (bench) → Soft: holds 3.06 kN on four screws with no visible yield or crack at 15 bar (bench) | — | plate window section at x 0 (y 135..160) and the four counterbore floors at y 140 | no | MEDIUM | RV01 F1 is closed for bending and pull-through: measured window section Z 4948.1 mm3 gives sigma 9.59 MPa, a factor 4.17 against an unsourced 40 MPa, and pull-through tau 8.5 MPa on 5.0 of plate; but spec 4 does not check head bearing: 765 N per screw on the ISO 7380 head annulus (5.7 on a 3.4 hole, 16.4 mm2) is about 47 MPa, near printed PLA's compressive yield, so the heads may embed or creep during a 5 min hold at 15 bar; the 4.2 factor also presumes solid infill, which no spec row states. | Add the head bearing check to A-02 and the test procedure: specify 100 % infill (or many perimeters) round the counterbores, or put a steel washer under each head (Ø7 needs the counterbore opened to about Ø7.5), and record head sink and gauge drop at each pressure step. |

REQ-08 against spec 1.3 §4, from the reviewer's numbers:
- **Window section, bending.** At x 0 the plate keeps z −60 … −30 and +42.50 … +60, which is 47.5 of the 120, at 25.0 deep. The measured section is A 1187.5 mm², I 61 851 mm⁴, Z 4948.1 mm³. With M = 1.53 kN × 31 mm = 47.4 N·m, σ is 9.59 MPa, a factor of 4.17 against ≈ 40 MPa along the layers. This agrees with §4.
- **Pull-through.** The shear cylinder is Ø5.7 × 5.0, 89.5 mm², so τ = 765 N / 89.5 = 8.5 MPa. This agrees with §4.
- **Head bearing (not in §4).** The ISO 7380 M3 head (Ø5.7) bears on the floor annulus outside the Ø3.4 hole, 16.4 mm². At 765 N that is about 47 MPa, close to the compressive yield of printed PLA. The floor at y 140 is a vertical face in the print, so the bearing runs along the layers.

Bending and pull-through therefore have room, and the head seats are the likely first yield. That would show as heads sinking and the housing dropping, not as a sudden fracture, and the test is hydrostatic with low stored energy. Rated MEDIUM, not blocking (Soft).

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. REQ-03 pair-B at R 29.9 has zero margin | Confirmed by construction: nominal 10.970 (+0.100); R 29.9 gives 10.870, exactly the threshold. The window prints as a horizontal hole, which FDM tends to make undersize, so a printed window below R 29.9 is plausible; the need behind it (a head <= 17.7 clears by 2.0, A-12) has about 7.5 of room for ordinary M3/M3.5 heads. No deviation of the delivered part. |
| 2. D-03a margin 0.1 deg and the crown exception by position | Independent route: four plugs r 1.8 y 135..140 on the measured hole axes, census re-run: least 45.100 deg at the window flank, 0 samples below 45; the 312 sub-45 samples of the unplugged part are all on the crowns. Sections y 137.5 and x 44 show only the 3.4 crowns. The 20-deep counterbore teardrop roofs read 45.100 deg. PASS (assumed: A-10). |
| 3. REQ-08 rests on the hand moment and unsourced PLA strength; OD-G10 rows are the clearance fallback | Measured section Z 4948.1 mm3, sigma 9.59 MPa, factor 4.17, as spec 4; head bearing about 47 MPa is not in the hand calculation (F1, MEDIUM). OD-G10 brep_valid 0 confirmed; common_volume reads it INCONCLUSIVE; every OD-G10 row used clearance > 0 with inside False over 380 poses, never inside, least 11.755. |
