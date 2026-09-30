# REPORT — od_c02_bulkhead v02 (20260930-od-c02-bulkhead)

Designer: Claude Code, claude-opus-5-5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` with the amendment `01_CAD/DESIGN_PLAN_v02.md` · 2026-09-30 UTC · brief WP-03, build attempt 2 of 2 · **outcome: SUBMITTED**

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 119de1e798b8c65da5e8bbb882fdb86e1b358b0a7813cb16654dc2d406cf4005 | the base plan (spec 1.0), unchanged since v01 |
| `01_CAD/DESIGN_PLAN_v02.md` | cc39c89c991d21038ed6167b5f5e017f902c3f91749e65d43e3cbb4b6dcc1e25 | plan amendment for spec 1.1 (brief WP-03), written before the v02 geometry |
| `01_CAD/check_od_c02_bulkhead_v02.py` | 82af3c8fc54ea1c70cbd12487fb09327120947174460762987a23c7b52160417 | checks, written before the v02 build (D3) |
| `01_CAD/build_od_c02_bulkhead_v02.py` | 55e2b085cbf0322b3467d9ef0a6e7a0fa9213eaa893a175db13316cde4eb8ceb | parametric build script (D4) |
| `01_CAD/build_record_v02.json` | 29df8e6a1c410cd24d54753d03be262990cb0cff5dc05c726a6ff5c5c72dfcbc | build record: parameters, export hashes, placements |
| `01_CAD/check_od_c02_bulkhead_v02.json` | e25653f36074ef4e2736981b5bdb438118182f14636df42c47b1d90b37572a96 | check results (197 rows, facts) |
| `01_CAD/check_od_c02_bulkhead_v02.log` | 9c0481c52a2a29c6770a3604cc554bf8822edbc8c630516ad8fa4c564080c8f1 | check run log |
| `01_CAD/sections_od_c02_bulkhead_v02.py` | 06bbc5c2f058c5431c281df6757fc6f1b81b5894d764942d563c627441d81908 | sections script (D6) |
| `01_CAD/sections_v02.json` | a0f85af79cea879c5ad317fd9ed49d3bd93642812fa08ff24524b531373004cc | sections log |
| `01_CAD/sweep_od_c02_bulkhead_v02.sh` | bcce3b94bd02b0be254bac1b9fef36e7885328f78ff5cf504ae63fcd13041bbb | sweep driver (D7) |
| `01_CAD/sweep_summary_v02.py` | c3d5f9a1d997e2027b742da91aa4907ce2f5434c8f813468cc8ad81e1e00aac4 | sweep summary script |
| `01_CAD/sweep_v02/sweep_summary_v02.json` | 835489ee99be3c15d6499678b7a8ff3bb01d16089de7df9c8a8aaaa660d62b7f | sweep results, 12 variants plus nominal |
| `01_CAD/probe/probe_assembly_path_v02.py` | 7ee3ee90222538458ecee5bedc11a701d085af0b70fcb222e06e3b0a9d4c9444 | assembly path probe (L-10), diagnostic |
| `01_CAD/probe/probe_assembly_path_v02.json` | 8680330350f598aa297c42c3fb9b7daee3c0523e8439146de27c972a6f112152 | assembly path probe results |
| `01_CAD/report_od_c02_bulkhead_v02.py` | 10de96625c73f8f52ca5c144751c5eca30ca632092581238210a4ae0ec122de0 | writes this REPORT from the JSON files |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | AP242, re-imported for every measurement |
| `02_STEP_STL/od_c02_assembly_C1_v02.step` | 7d2e760590973fdfe529338231b117a9fc456d246b886a0217c4785f61d37141 | AP242 check assembly, 8 labelled solids |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.stl` | e48afe62c8beb97acc76da990d75ab7e4e2bfbd5416b9cf3f38a0f65d573e18e | tolerance 0.01 mm / angular 0.2 rad, 2308 triangles, cached triangulation cleared by write_stl |
| `03_Sections/od_c02_bulkhead_v02_left_x65_wall.png` | fb921d6914156ef9ff1fadff749db60e84e55bbc93e12bc403535d892982455d | left x = 65.00 mm through (65.0, 100.0, -135.0); cut 44110.12 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_left_x61_wet_flanges.png` | 7f78fceaf2d86621f41e452eb974cfdc627c2bc96a3d7c47a8c756010133ee76 | left x = 61.00 mm through (61.0, 100.0, -135.0); cut 4200.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_left_x69_elec_flanges.png` | 89844a2326846b78986d24dc4eec7751d373c7e2b9ef97b5688696091c32a51e | left x = 69.00 mm through (69.0, 100.0, -135.0); cut 4200.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-45_base_bore.png` | 6cd48f161cb614a7f64f0846e39834cfc11ba9a92105745cec668b88caaacfd1 | top z = -45.00 mm through (65.0, 100.0, -45.0); cut 956.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-105_base_bore.png` | 8aa3df8c1f4f1ebcd95f632ce9fe49eacf25949e553bb5badeefa34db4b35f61 | top z = -105.00 mm through (65.0, 100.0, -105.0); cut 988.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-60_top_bore_w3.png` | d3bde5253d819d70a8fa5d20b5664dcfb786efa67b48fb8fd81a9f235322df78 | top z = -60.00 mm through (65.0, 100.0, -60.0); cut 892.81 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-210_top_bore.png` | 6efa7be178935b633b7e648afffc48c98f7620499a9e7ca2403c6d494f5ae959 | top z = -210.00 mm through (65.0, 100.0, -210.0); cut 988.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-200_w1.png` | 8c9c069d503e55f8a4aa1af609e1a8450d14e1ca121432c58f9c59d06c75bdc6 | top z = -200.00 mm through (65.0, 100.0, -200.0); cut 956.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-55_w4.png` | 64b41b5f4c20dd8daf318c6f2a06d772ae6a1875195803fd7f8cab354fb6247a | top z = -55.00 mm through (65.0, 100.0, -55.0); cut 900.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_z-100_profile.png` | 884bfe8bddc10a43dad4d631ffa872134e69b66d9749c2890441964275db6181 | top z = -100.00 mm through (65.0, 100.0, -100.0); cut 1012.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_y100_wall.png` | 14bfe4d6a099cb3832034ff85ff3d82d6b18a1d2a70b229d86b9bcd25b85b898 | front y = 100.00 mm through (65.0, 100.0, -135.0); cut 840.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_y200_wall.png` | d0974d6fee694379e4370f32499ddef043fc7af70e1a13ae4d703e0dc523e201 | front y = 200.00 mm through (65.0, 200.0, -135.0); cut 840.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_y150_windows.png` | b2a0a80267cae4db912369f30bd052b7b5b1aec2b6dd50c35a6c7f6d9c7c867a | front y = 150.00 mm through (65.0, 150.0, -135.0); cut 588.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_y60_w4.png` | 67770763500038249dbd13652416a4afded07a77a9be51a2749f444bb28d8d76 | front y = 60.00 mm through (65.0, 60.0, -135.0); cut 756.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_y3_base_bores.png` | 845b6fe1ef45980aafaed39bcc59e34cd031d53f9d76cc217880e0acf1f7c5aa | front y = 3.00 mm through (65.0, 3.0, -135.0); cut 2469.73 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_y212_top_bores.png` | 4d472eef3c953d7249ec311a58892d8ac81f371e358f51572507171c789f0d18 | front y = 212.00 mm through (65.0, 212.0, -135.0); cut 2284.87 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_asm_z-200_pump.png` | f02d101427d33129088396da8473f1bf14396f81867ef017a561028783077b3c | top z = -200.00 mm through (40.0, 100.0, -200.0); cut 5719.81 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_front_asm_y40_pump_axis.png` | f013d41ef5d0c98d37a90ae94eb02a03ea7cd6ef70b82ddb01b76c3a449a039f | front y = 40.00 mm through (40.0, 40.0, -135.0); cut 12789.81 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_asm_z-50_carrier.png` | f73c749d94eeeda70dae26c79aae7d2de7973bb84749a1c05601b2cf1faa1eb9 | top z = -50.00 mm through (40.0, 100.0, -50.0); cut 25464.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v02_top_asm_z-45_screw_path.png` | f494d9f8b8fca5bea96f09ac4171ce34336ba78d62a3547180026ba3e58dfe40 | top z = -45.00 mm through (40.0, 100.0, -45.0); cut 25472.00 mm²; nothing clipped (0) |

Inputs checked against the brief (WP-02 table, unchanged for WP-03) before any work: all nine SHA-256 match. Every v01 file is left as it was. `01_CAD/sweep_v02/<variant>/` holds each sweep run's STEP, STL, assembly, build record and check JSON (not deliverables); `01_CAD/sweep_v02/_mesh_check/remesh_check.stl` is the check's scratch re-mesh for U-07. No 3MF: the orchestrator's step. STL facts for it: 2308 triangles, mesh volume 208486.004 mm³ (B-rep 208484.106 mm³), bounding box [59.0, 0.0, -240.0] … [71.0, 215.0, -30.0] (size [12.0, 215.0, 210.0]).

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3) · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (clean)

## 3. Gate self-check

Every value is measured from the re-imported STEP (`check_od_c02_bulkhead_v02.json`, 197 rows: 4 INCONCLUSIVE, 4 N/A, 76 PASS, 113 PASS_ASSUMED). One line per §5 row with its worst sub-row; every sub-row is in the JSON block. Bands from GATES §0 (mm 0.005, deg and mm³ 0.001, counts 0). `min_wall`, `min_wall_wide` and `overhang_census` ran at spacing 0.7 (the WP-02 brief's note; largest step 0.697674 mm). These are self-checks: none clears a Hard gate.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 (3 rows; worst: `U-01.solid_count`) | 1 count | == 1 | 0 | — | PASS | — |
| U-02 (3 rows; worst: `U-02.size_x`) | 12 mm | in [11.9, 12.1] | 0.1 | — | PASS | — |
| U-03 (18 rows; worst: `U-03.h11.interference`) | — mm3 | <= 0 mm3 | — | — | INCONCLUSIVE | A-01, A-02 |
| U-04 (15 rows; worst: `U-04.assembly.od_h11_thermoblock.volume_delta`) | 0.0524 mm3 | in [0, 0] mm3 | — | — | INCONCLUSIVE | — |
| U-05 (13 rows; worst: `U-05.plane_faces`) | 36 count | == 36 | 0 | — | PASS | — |
| U-06 (1 rows; worst: `U-06(Soft)`) | 2 mm | >= 2.0 | 0 | (63.0000, 207.0000, -60.0000) mm | PASS | — |
| U-07 (5 rows; worst: `U-07.mesh.bodies`) | 1 count | == 1 | 0 | — | PASS | — |
| U-08 (1 rows; worst: `U-08`) | —  | N/A | — | — | N/A | — |
| D-01a (1 rows; worst: `D-01a`) | 2 mm | >= 0.8 | 1.2 | (63.0000, 207.0000, -60.0000) mm | PASS | — |
| D-01b (1 rows; worst: `D-01b`) | 2 mm | >= 2.0 | 0 | (63.0000, 207.0000, -60.0000) mm | PASS | — |
| D-02 (3 rows; worst: `D-02.size_y`) | 215 mm | <= 220.0 | 5 | — | PASS (assumed: A-08) | A-08 |
| D-03a (1 rows; worst: `D-03a`) | 45 deg | >= 45.0 | 0 | (67.0000, 150.0000, -186.0000) mm | PASS (assumed: A-10) | A-10 |
| D-03b (1 rows; worst: `D-03b.widest_bore_bridge`) | 4 mm | <= 5.0 | 1 | — | PASS | — |
| D-04a (1 rows; worst: `D-04a`) | —  | N/A | — | — | N/A | — |
| D-05a (6 rows; worst: `D-05a.top.x65_z-60.across_x`) | 11 mm | >= 8.0 | 3 | [(70.5, 212.0, -60.0), (59.5, 212.0, -60.0)] | PASS (assumed: A-05) | A-05 |
| D-05b (18 rows; worst: `D-05b.base.x65_z-45.diameter`) | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-05) | A-05 |
| D-06a (1 rows; worst: `D-06a`) | 2 mm | >= 1.0 | 1 | (63.0000, 207.0000, -60.0000) mm | PASS | — |
| D-07 (1 rows; worst: `D-07`) | —  | N/A | — | — | N/A | — |
| J-05 (12 rows; worst: `J-05.top.x65_z-60.elec`) | 3.5 mm | >= 3.0 | 0.5 | (70.5000, 212.0000, -60.0000) mm | PASS | — |
| E-06 (1 rows; worst: `E-06`) | —  | reviewer | — | — | INCONCLUSIVE | — |
| REQ-01 (20 rows; worst: `REQ-01.base.x65_z-45.blind`) | 0 bool | == 0 | 0 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-01, A-03) | A-01, A-03 |
| REQ-02 (9 rows; worst: `REQ-02.rail_wet_face_min_x`) | 59 mm | in [58.9, 59.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| REQ-03 (9 rows; worst: `REQ-03.underside_faces`) | 1 count | == 1 | 0 | — | PASS (assumed: A-01) | A-01 |
| REQ-04 (14 rows; worst: `REQ-04.w4.front_end_closed`) | 1 count | == 1 | 0 | — | PASS (assumed: A-04) | A-04 |
| REQ-05 (6 rows; worst: `REQ-05.min_x`) | 59 mm | >= 59.0 | 0 | — | PASS (assumed: A-02) | A-02 |
| REQ-06 (1 rows; worst: `REQ-06.max_y`) | 215 mm | in [214.9, 215.1] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-07 (8 rows; worst: `REQ-07.top.x65_z-60.blind`) | 0 bool | == 0 | 0 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-05) | A-05 |
| REQ-08 (2 rows; worst: `REQ-08.max_x`) | 71 mm | <= 71.0 | 0 | — | PASS (assumed: A-07) | A-07 |
| REQ-09 (1 rows; worst: `REQ-09(Soft)`) | —  | bench | — | — | INCONCLUSIVE | A-11 |
| exactly_one_solid (1 rows; worst: `exactly_one_solid`) | 1 count | == 1 | 0 | — | PASS | — |
| feature_census (11 rows; worst: `feature_census.plane_faces`) | 36 count | == 36 | 0 | — | PASS | — |
| envelope_within_spec (9 rows; worst: `envelope_within_spec.size_x`) | 12 mm | in [11.9, 12.1] | 0.1 | — | PASS | — |

Notes on the rows that are not a plain PASS:

- **U-03**: INCONCLUSIVE only through `U-03.h11.interference`, which the U-03 row itself makes INCONCLUSIVE (OD-H11 unsound, OD-C04 A-14); OD-H11 is gated on distance and every other U-03 sub-row reads PASS (assumed: A-01, A-02). **U-04**: the part round trip and every other assembly part pass; only OD-H11's volume changes on the write (0.0524 mm³, the unsound input, as in v01).
- **E-06** (reviewer row): one solid; both rails run the wall's whole length z −240 … −30 (sections `left_x61_wet_flanges`, `left_x69_elec_flanges`: each flange cut is 4200 mm² = 12 × 210 + 8 × 210); no boss stands free: every bore lies inside a rail. **REQ-09** (Soft bench): INCONCLUSIVE by its row, risk rating medium: a 4.0 wall 195 tall between the rails, held at four screws below and two above.
- **D-03a**: the gated number is `overhang_census` on the re-imported solid with the six named-exception bores refilled by position (6 bores found, refilled solid 34 faces as planned): least 45.0° at the window gables, planar and exact (sampling bound 0), no sample under 45°. Apart: the whole-part census reads 0° at (65, 0, -223) (a base-rail bore crown). The downward faces split by position:

| Region (by position) | Faces | Least angle (deg) |
|---|---|---|
| exception: base-rail insert bore 4.0 crown | 4 | 0 |
| exception: top-rail insert bore 4.0 crown | 2 | 0 |
| window roof | 8 | 45 |

- **D-03b** (reviewer row): the designer's reading is the widest horizontal bore measured by `bore_census`, 4.0 (the six insert bores, the named exception); the four windows carry the 45° gable, and nothing else bridges (no rib, no collar: sections `front_y150_windows`, `front_y60_w4`, `left_x65_wall`).

**U-03 (a), REQ-01 and REQ-05 on the parts as placed in the assembly STEP** (nearest point on the bulkhead in `At`):

| Row | Measured | Required | Margin | At | Status |
|---|---|---|---|---|---|
| `REQ-05.min_x` | 59 mm | >= 59.0 | 0 | — | PASS (assumed: A-02) |
| `U-03.plate.clearance` | 0 mm | == 0.0 | 0 | (67.0000, 0.0000, -225.0000) mm | PASS (assumed: A-01, A-02) |
| `U-03.plate.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.coax.x65_z-45` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -45.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-01.plate_coax.x65_z-45` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -45.0000) mm | PASS (assumed: A-01, A-03) |
| `U-03.coax.x65_z-105` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -105.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-01.plate_coax.x65_z-105` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -105.0000) mm | PASS (assumed: A-01, A-03) |
| `U-03.coax.x65_z-165` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -165.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-01.plate_coax.x65_z-165` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -165.0000) mm | PASS (assumed: A-01, A-03) |
| `U-03.coax.x65_z-225` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -225.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-01.plate_coax.x65_z-225` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -225.0000) mm | PASS (assumed: A-01, A-03) |
| `U-03.c03.clearance` | 17 mm | >= 3.0 | 14 | (59.0000, 0.0000, -240.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-05.c03.clearance` | 17 mm | >= 3.0 | 14 | (59.0000, 0.0000, -240.0000) mm | PASS (assumed: A-02) |
| `U-03.c03.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.h01.clearance` | 7.5 mm | >= 3.0 | 4.5 | (63.0000, 40.0000, -202.4000) mm | PASS (assumed: A-01, A-02) |
| `REQ-05.h01.clearance` | 7.5 mm | >= 3.0 | 4.5 | (63.0000, 40.0000, -202.4000) mm | PASS (assumed: A-02) |
| `U-03.h01.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.c04.clearance` | 9 mm | >= 3.0 | 6 | (59.0000, 0.0000, -157.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-05.c04.clearance` | 9 mm | >= 3.0 | 6 | (59.0000, 0.0000, -157.0000) mm | PASS (assumed: A-02) |
| `U-03.c04.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.h11.clearance` | 20.161 mm | >= 3.0 | 17.161 | (63.0000, 99.3565, -97.3000) mm | PASS (assumed: A-01, A-02) |
| `REQ-05.h11.clearance` | 20.161 mm | >= 3.0 | 17.161 | (63.0000, 99.3565, -97.3000) mm | PASS (assumed: A-02) |
| `U-03.h11.interference` | — mm3 | <= 0 mm3 | — | — | INCONCLUSIVE |
| `U-03.g01.clearance` | 18.6827 mm | >= 3.0 | 15.6827 | (59.5000, 207.0000, -30.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-05.g01.clearance` | 18.6827 mm | >= 3.0 | 15.6827 | (59.5000, 207.0000, -30.0000) mm | PASS (assumed: A-02) |
| `U-03.g01.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.c05_box.clearance` | 4 mm | >= 4.0 | 0 | (59.0000, 0.0000, -30.0000) mm | PASS (assumed: A-01, A-02) |

The coaxiality rows locate each plate hole at the bulkhead bore's measured axis point 3.0 below the plate top (y −3), so the offset is the distance between the two axes. The plate holes read z -45: Ø4, 6 long, through 1; z -105: Ø4, 6 long, through 1; z -165: Ø4, 6 long, through 1; z -225: Ø4, 6 long, through 1.

**The six insert bores and the four windows:**

| Row | Measured | Required | Margin | At | Status |
|---|---|---|---|---|---|
| `REQ-01.base.x65_z-45.diameter` | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-45.depth` | 6 mm | in [5.9, 6.1] | 0.1 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-45.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-45.blind` | 0 bool | == 0 | 0 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-01, A-03) |
| `D-05a.base.x65_z-45.across_x` | 12 mm | >= 8.0 | 4 | [(71.0, 3.0, -45.0), (59.0, 3.0, -45.0)] | PASS (assumed: A-05) |
| `J-05.base.x65_z-45.elec` | 4 mm | >= 3.0 | 1 | (71.0000, 3.0000, -45.0000) mm | PASS |
| `J-05.base.x65_z-45.wet` | 4 mm | >= 3.0 | 1 | (59.0000, 3.0000, -45.0000) mm | PASS |
| `REQ-01.base.x65_z-105.diameter` | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 0.0000, -105.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-105.depth` | 6 mm | in [5.9, 6.1] | 0.1 | (65.0000, 0.0000, -105.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-105.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 0.0000, -105.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-105.blind` | 0 bool | == 0 | 0 | (65.0000, 0.0000, -105.0000) mm | PASS (assumed: A-01, A-03) |
| `D-05a.base.x65_z-105.across_x` | 12 mm | >= 8.0 | 4 | [(71.0, 3.0, -105.0), (59.0, 3.0, -105.0)] | PASS (assumed: A-05) |
| `J-05.base.x65_z-105.elec` | 4 mm | >= 3.0 | 1 | (71.0000, 3.0000, -105.0000) mm | PASS |
| `J-05.base.x65_z-105.wet` | 4 mm | >= 3.0 | 1 | (59.0000, 3.0000, -105.0000) mm | PASS |
| `REQ-01.base.x65_z-165.diameter` | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 0.0000, -165.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-165.depth` | 6 mm | in [5.9, 6.1] | 0.1 | (65.0000, 0.0000, -165.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-165.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 0.0000, -165.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-165.blind` | 0 bool | == 0 | 0 | (65.0000, 0.0000, -165.0000) mm | PASS (assumed: A-01, A-03) |
| `D-05a.base.x65_z-165.across_x` | 12 mm | >= 8.0 | 4 | [(71.0, 3.0, -165.0), (59.0, 3.0, -165.0)] | PASS (assumed: A-05) |
| `J-05.base.x65_z-165.elec` | 4 mm | >= 3.0 | 1 | (71.0000, 3.0000, -165.0000) mm | PASS |
| `J-05.base.x65_z-165.wet` | 4 mm | >= 3.0 | 1 | (59.0000, 3.0000, -165.0000) mm | PASS |
| `REQ-01.base.x65_z-225.diameter` | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 0.0000, -225.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-225.depth` | 6 mm | in [5.9, 6.1] | 0.1 | (65.0000, 0.0000, -225.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-225.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 0.0000, -225.0000) mm | PASS (assumed: A-01, A-03) |
| `REQ-01.base.x65_z-225.blind` | 0 bool | == 0 | 0 | (65.0000, 0.0000, -225.0000) mm | PASS (assumed: A-01, A-03) |
| `D-05a.base.x65_z-225.across_x` | 12 mm | >= 8.0 | 4 | [(71.0, 3.0, -225.0), (59.0, 3.0, -225.0)] | PASS (assumed: A-05) |
| `J-05.base.x65_z-225.elec` | 4 mm | >= 3.0 | 1 | (71.0000, 3.0000, -225.0000) mm | PASS |
| `J-05.base.x65_z-225.wet` | 4 mm | >= 3.0 | 1 | (59.0000, 3.0000, -225.0000) mm | PASS |
| `REQ-07.top.x65_z-60.diameter` | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-05) |
| `REQ-07.top.x65_z-60.depth` | 6 mm | in [5.9, 6.1] | 0.1 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-05) |
| `REQ-07.top.x65_z-60.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-05) |
| `REQ-07.top.x65_z-60.blind` | 0 bool | == 0 | 0 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-05) |
| `D-05a.top.x65_z-60.across_x` | 11 mm | >= 8.0 | 3 | [(70.5, 212.0, -60.0), (59.5, 212.0, -60.0)] | PASS (assumed: A-05) |
| `J-05.top.x65_z-60.elec` | 3.5 mm | >= 3.0 | 0.5 | (70.5000, 212.0000, -60.0000) mm | PASS |
| `J-05.top.x65_z-60.wet` | 3.5 mm | >= 3.0 | 0.5 | (59.5000, 212.0000, -60.0000) mm | PASS |
| `REQ-07.top.x65_z-210.diameter` | 4 mm | in [3.95, 4.05] | 0.05 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-05) |
| `REQ-07.top.x65_z-210.depth` | 6 mm | in [5.9, 6.1] | 0.1 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-05) |
| `REQ-07.top.x65_z-210.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-05) |
| `REQ-07.top.x65_z-210.blind` | 0 bool | == 0 | 0 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-05) |
| `D-05a.top.x65_z-210.across_x` | 11 mm | >= 8.0 | 3 | [(70.5, 212.0, -210.0), (59.5, 212.0, -210.0)] | PASS (assumed: A-05) |
| `J-05.top.x65_z-210.elec` | 3.5 mm | >= 3.0 | 0.5 | (70.5000, 212.0000, -210.0000) mm | PASS |
| `J-05.top.x65_z-210.wet` | 3.5 mm | >= 3.0 | 0.5 | (59.5000, 212.0000, -210.0000) mm | PASS |
| `REQ-04.w1_y150_z-200.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -200.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w1_y150_z-200.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 150.0000, -200.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w1_y150_z-200.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -186.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -130.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 150.0000, -130.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -116.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -60.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 150.0000, -60.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -46.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4_y60_z-55.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 60.0000, -55.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4_y60_z-55.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 60.0000, -55.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4_y60_z-55.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 60.0000, -41.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4.front_end_closed` | 1 count | == 1 | 0 | — | PASS (assumed: A-04) |
| `REQ-04.no_collar` | 0 count | == 0 | 0 | — | PASS (assumed: A-04) |

Gable roof rays at 60° and 120° from the window axis (reported, not gated): w1_y150_z-200 60°: 10.2487 (design 10.2487); w1_y150_z-200 120°: 10.2487 (design 10.2487); w2_y150_z-130 60°: 10.2487 (design 10.2487); w2_y150_z-130 120°: 10.2487 (design 10.2487); w3_y150_z-60 60°: 10.2487 (design 10.2487); w3_y150_z-60 120°: 10.2487 (design 10.2487); w4_y60_z-55 60°: 10.2487 (design 10.2487); w4_y60_z-55 120°: 10.2487 (design 10.2487). The front end z −30 is one planar face of 1012 mm² (the whole I-profile): window 4 closes inside the wall, its apex 11.0 behind the front end.

## 4. Robustness sweep (D7)

Twelve variants, each rebuilt, exported into `01_CAD/sweep_v02/<variant>/`, and put through the same full check (assembly included). Every run built one valid solid.

| Parameter | Low · nominal · high | All built, one solid | Not passing (low / high) | Worst gate | Worst margin |
|---|---|---|---|---|---|
| bore_d | 3.95 · 4.0 · 4.05 | yes | none / none | U-04.assembly.od_h01_pump.volume_delta | 0 |
| bore_depth | 5.9 · 6.0 · 6.1 | yes | none / D-01b, U-06(Soft) | D-01b | -0.1 |
| bore_shift (dx, dz) | (-0.07, -0.07) · 0 · (+0.07, +0.07) | yes | none / none | U-04.assembly.od_h01_pump.volume_delta | 0 |
| wall_x0 / wall_x1 | 62.9 / 66.9 · 63.0 / 67.0 · 63.1 / 67.1 | yes | none / none | U-04.assembly.od_h01_pump.volume_delta | 0 |
| brail_x0 | 58.9 · 59.0 · 59.1 | yes | REQ-05.min_x, U-03.c05_box.clearance / none | REQ-05.min_x | -0.1 |
| brail_x1 | 70.9 · 71.0 · 71.1 | yes | none / REQ-08.max_x | REQ-08.max_x | -0.1 |

Worst margin per gate over the nominal build and the twelve variants (the OD-H11 rows INCONCLUSIVE by the row and the reviewer rows left out):

| Gate | Worst margin | Row | Variant | Status there |
|---|---|---|---|---|
| D-01a | 1.1 | `D-01a` | bore_depth_high | PASS |
| D-01b | -0.1 | `D-01b` | bore_depth_high | FAIL |
| D-02 | 5 | `D-02.size_y` | nominal | PASS_ASSUMED |
| D-03a | 0 | `D-03a` | nominal | PASS_ASSUMED |
| D-03b | 0.95 | `D-03b.widest_bore_bridge` | bore_d_high | PASS |
| D-05a | 3 | `D-05a.top.x65_z-60.across_x` | nominal | PASS_ASSUMED |
| D-05b | 0 | `D-05b.base.x65_z-45.diameter` | bore_d_low | PASS_ASSUMED |
| D-06a | 0.9 | `D-06a` | bore_depth_high | PASS |
| J-05 | 0.43 | `J-05.top.x65_z-60.wet` | bore_shift_low | PASS |
| REQ-01 | 0 | `REQ-01.base.x65_z-45.blind` | nominal | PASS_ASSUMED |
| REQ-02 | 0 | `REQ-02.wet_face_x.y100_z-100` | wall_low | PASS_ASSUMED |
| REQ-03 | 0 | `REQ-03.underside_faces` | nominal | PASS_ASSUMED |
| REQ-04 | 0 | `REQ-04.w4.front_end_closed` | nominal | PASS_ASSUMED |
| REQ-05 | -0.1 | `REQ-05.min_x` | brail_x0_low | FAIL |
| REQ-06 | 0.1 | `REQ-06.max_y` | nominal | PASS_ASSUMED |
| REQ-07 | 0 | `REQ-07.top.x65_z-60.blind` | nominal | PASS_ASSUMED |
| REQ-08 | -0.1 | `REQ-08.max_x` | brail_x1_high | FAIL |
| U-01 | 0 | `U-01.solid_count` | nominal | PASS |
| U-02 | 0 | `U-02.size_x` | brail_x0_low | PASS |
| U-03 | -0.1 | `U-03.c05_box.clearance` | brail_x0_low | FAIL |
| U-04 | 0 | `U-04.assembly.od_h01_pump.volume_delta` | nominal | PASS |
| U-05 | 0 | `U-05.plane_faces` | nominal | PASS |
| U-06 | -0.1 | `U-06(Soft)` | bore_depth_high | FAIL |
| U-07 | 0 | `U-07.mesh.bodies` | nominal | PASS |
| envelope_within_spec | 0 | `envelope_within_spec.size_x` | brail_x0_low | PASS |
| exactly_one_solid | 0 | `exactly_one_solid` | nominal | PASS |
| feature_census | 0 | `feature_census.plane_faces` | nominal | PASS |

Reading: the nominal part passes every gate. Three parameters pass only on one side of their band, each because the nominal sits on a spec limit: (1) **bore_depth 6.1** (inside REQ-07's ±0.1) leaves 1.9 between the top-rail bore floor and the top rail's underside at the wall-face line x 63 / 67, so D-01b and U-06 read 1.9 (FAIL); at 5.9 and 6.0 they read 2.1 and 2.0. (2) **brail_x0 58.9** fails REQ-05 (min_x ≥ 59.0) and the carrier-box clearance (3.9 < 4.0). (3) **brail_x1 71.1** fails REQ-08 (max_x ≤ 71.0). REQ-02's ±0.10 band on the rail's wet face is one-sided in practice (59.0 … 59.1), and so is the electric edge (70.9 … 71.0).

## 5. Build facts

- Envelope 12 × 215 × 210 mm at x 59 … 71, y 0 … 215, z -240 … -30; volume 208484.1 mm³; mass 223.1 g at 1070 kg/m³ (A-09); centre of mass (65.00, 103.26, -135.45).
- Fillets: none in the spec; none requested, none built.
- Features as the plan amendment §3: wall, base rail x 59 … 71, top rail x 59.5 … 70.5, four gabled windows cut x 62 … 68, four Ø4.0 × 6.0 bores from y 0, two from y 215. Census measured: plane_faces 36, cylinder_faces 10, concave_cylinders 10, bores 6; 4 bores open at y 0, 2 open at y 215.
- Placements (assembly STEP, 8 labelled solids), unchanged from v01: OD-C01 at the identity; OD-C03 and OD-H01 at the OD-C01 §4 joint (local x → +Z, y → −Y, z → +X, origin (0, 40, −205)); OD-C04 and OD-H11 at the identity rotation, origin (0, 70, −140); OD-G01 v02 (local x → X, y → +Z, z → −Y, origin (0, 180.06, 32)); each by a RigidJoint on the bulkhead's machine frame connected to the part's own STEP origin; the carrier foot box `od_c05_foot_reference_A02` x ±55, y 0 … 210, z −70 … −26 from the spec's values.
- STL: `write_stl` at 0.01 mm / 0.2 rad (≤ 0.2310), 2308 triangles, sagitta at export 0.004895 mm; the re-mesh of the re-imported STEP reads the same. `mesh_census`: 1 body, 0 naked edges, consistent winding.
- U-04: the part re-reads with volume delta 1.7e-10 mm³, faces delta 0, valid after 1; the assembly keeps 8 solids, faces and labels; per-part volume deltas ≤ 4.3e-9 mm³ except OD-H11 (0.0524 mm³, unsound input).

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The rail's underside sits on the plate's top face (clearance 0.0, 0.0 mm³ in common) and four M3 × 12 screws from below through the plate's Ø4.0 holes reach inserts in coaxial blind bores (axis offset 0.000; section `top_asm_z-45_screw_path`). In the print it stands on its 12 × 215 rear end, centre of mass at x 65.00, over the middle of the footprint. |
| P2 | Function chains | Dam: the underside is one face over x 59 … 71, z −240 … −30, holed only by the four blind bore mouths (closed by the inserts and screws). Wires: the four windows go through the wall with nothing in front of either mouth (no rib, no collar). Top panel: two blind bores open at y 215. |
| P3 | Motion and assembly path | No moving parts. The part is lowered along −Y onto the plate: the box it sweeps (its footprint from y 0 to y 400) keeps OD-H01 at 3.5, OD-C03 at 17, OD-C04 at 9, OD-H11 at 16.161, OD-G01 at 18.2488 and the carrier box at 4 mm (the rail passes the pump's +X end 3.5 away on the way down; the final pose keeps 7.5 at the wall face). |
| P4 | Human factors | Each screw is driven from below along the bore's axis through the plate, nothing on the path (the machine turned over, A-03); the inserts are pressed from the rail's underside and the top face, both open faces. |
| P5 | Next to a real product | A plain printed partition with rails and grommet windows, like a moulded appliance bulkhead; nothing a domain engineer would flag at once beyond the thin wall's stiffness (REQ-09). |
| P6 | Floating, embedded, mirrored, upside-down | One solid; nothing floating; nothing embedded in a neighbour (interference 0.0 everywhere measurable); the gables point +Z, the print's up (A-10); the assembly poses are the OD-C01 joints. |

## 7. Library and tools used

Card: UNO10 U5 tank heat-set (size and position kept apart in U-02). Precedent: the v01 scripts of this job. Tools: `tools.core` `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`, `file_sha256`; `tools.measure` `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, `min_wall_wide`, `overhang_census`, `radial_extent`, `clearance`, `mass_properties`, `mesh_census`; `tools.result.gate`; `tools.drawing.write_sections`. New job code: the refilled solid for the D-03a census outside the named exception and the per-face split by position; the axis-to-axis coaxiality point; the three-ray circle for the windows' round part; the assembly path box. Missing tools: none for a gated number; D-03b has no tool (reviewer row); `bore_census` cannot see a 180° arc, so `radial_extent` reads the windows.

## 8. Deviations from the plan

- Geometry: none against the plan amendment v02 (itself the brief's amendments to the base plan).
- Files: the v02 scripts carry `_v02` in their names and the plan amendment is a new file, so the v01 scripts and plan stay byte-identical to the v01 REPORT's hashes (the brief: leave every v01 file as it is).
- Sections: the v01 cuts at x 62 (collars) and x 71 (ribs) became x 61 and x 69 (the rail flanges); added z −200 (window 1), z −210 (top bore 2), z −55 (window 4), y 3 (the base bores) and the assembly cut z −45 through the screw path.
- Added after the sweep, as a diagnostic only: the assembly path probe (L-10).

## 9. What I am least sure of

1. D-01b and U-06 at margin 0.000 on the top-rail bores. The Ø4.0 bore on x 65 is exactly as wide as the wall (x 63 … 67), so the edge of its floor (y 209) lies 2.0 above the top rail's underside (y 207) along the wall-face lines; `min_wall` reads 2.000 at (63, 207, −60). A bore 6.1 deep, inside REQ-07's ±0.1, reads 1.9 and fails D-01b. The spec's D-01b row names 3.5 and 4.0 beside the bores but not this floor. A melted-in Ø4.6 insert widens the bore to x 62.7 … 67.3, over the flange, where 2.0 or more stays under it only while the bore is no deeper than 6.0.
2. The D-03a gate reads the census on a derived solid (the six named-exception bores refilled by position), because `overhang_census` takes no region; the whole-part census reads 0° at the bore crowns, and the exception is not yet signed by the Usta. The window gables read exactly 45.0° (margin 0, planar).
3. Three envelope rows sit on their limits by the spec's own numbers: REQ-05 min_x 59.0, REQ-08 max_x 71.0, and the carrier box at 4.0. Printed standing on z −240, the first layers' squish (elephant's foot) widens only the rear end, but any outward error on the rail's wet face breaks REQ-05 and the box clearance. The ledger text also lags §4 in two rows (A-05 names the top bores at x 67.5, A-04 window 4 at z −40); the build follows §4, REQ-07 and REQ-04 (x 65, z −55).

## 10. Stop

Not stopped. Fix cycles used: 0 of 3 (the nominal v02 build passed its checks on the first run).

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c02-bulkhead",
 "part": "od_c02_bulkhead",
 "tag": "v02",
 "spec_version": "1.1",
 "files": [
  {
   "path": "01_CAD/DESIGN_PLAN.md",
   "sha256": "119de1e798b8c65da5e8bbb882fdb86e1b358b0a7813cb16654dc2d406cf4005"
  },
  {
   "path": "01_CAD/DESIGN_PLAN_v02.md",
   "sha256": "cc39c89c991d21038ed6167b5f5e017f902c3f91749e65d43e3cbb4b6dcc1e25"
  },
  {
   "path": "01_CAD/check_od_c02_bulkhead_v02.py",
   "sha256": "82af3c8fc54ea1c70cbd12487fb09327120947174460762987a23c7b52160417"
  },
  {
   "path": "01_CAD/build_od_c02_bulkhead_v02.py",
   "sha256": "55e2b085cbf0322b3467d9ef0a6e7a0fa9213eaa893a175db13316cde4eb8ceb"
  },
  {
   "path": "01_CAD/build_record_v02.json",
   "sha256": "29df8e6a1c410cd24d54753d03be262990cb0cff5dc05c726a6ff5c5c72dfcbc"
  },
  {
   "path": "01_CAD/check_od_c02_bulkhead_v02.json",
   "sha256": "e25653f36074ef4e2736981b5bdb438118182f14636df42c47b1d90b37572a96"
  },
  {
   "path": "01_CAD/check_od_c02_bulkhead_v02.log",
   "sha256": "9c0481c52a2a29c6770a3604cc554bf8822edbc8c630516ad8fa4c564080c8f1"
  },
  {
   "path": "01_CAD/sections_od_c02_bulkhead_v02.py",
   "sha256": "06bbc5c2f058c5431c281df6757fc6f1b81b5894d764942d563c627441d81908"
  },
  {
   "path": "01_CAD/sections_v02.json",
   "sha256": "a0f85af79cea879c5ad317fd9ed49d3bd93642812fa08ff24524b531373004cc"
  },
  {
   "path": "01_CAD/sweep_od_c02_bulkhead_v02.sh",
   "sha256": "bcce3b94bd02b0be254bac1b9fef36e7885328f78ff5cf504ae63fcd13041bbb"
  },
  {
   "path": "01_CAD/sweep_summary_v02.py",
   "sha256": "c3d5f9a1d997e2027b742da91aa4907ce2f5434c8f813468cc8ad81e1e00aac4"
  },
  {
   "path": "01_CAD/sweep_v02/sweep_summary_v02.json",
   "sha256": "835489ee99be3c15d6499678b7a8ff3bb01d16089de7df9c8a8aaaa660d62b7f"
  },
  {
   "path": "01_CAD/probe/probe_assembly_path_v02.py",
   "sha256": "7ee3ee90222538458ecee5bedc11a701d085af0b70fcb222e06e3b0a9d4c9444"
  },
  {
   "path": "01_CAD/probe/probe_assembly_path_v02.json",
   "sha256": "8680330350f598aa297c42c3fb9b7daee3c0523e8439146de27c972a6f112152"
  },
  {
   "path": "01_CAD/report_od_c02_bulkhead_v02.py",
   "sha256": "10de96625c73f8f52ca5c144751c5eca30ca632092581238210a4ae0ec122de0"
  },
  {
   "path": "02_STEP_STL/od_c02_bulkhead_C1_v02.step",
   "sha256": "1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc"
  },
  {
   "path": "02_STEP_STL/od_c02_assembly_C1_v02.step",
   "sha256": "7d2e760590973fdfe529338231b117a9fc456d246b886a0217c4785f61d37141"
  },
  {
   "path": "02_STEP_STL/od_c02_bulkhead_C1_v02.stl",
   "sha256": "e48afe62c8beb97acc76da990d75ab7e4e2bfbd5416b9cf3f38a0f65d573e18e"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_left_x65_wall.png",
   "sha256": "fb921d6914156ef9ff1fadff749db60e84e55bbc93e12bc403535d892982455d"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_left_x61_wet_flanges.png",
   "sha256": "7f78fceaf2d86621f41e452eb974cfdc627c2bc96a3d7c47a8c756010133ee76"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_left_x69_elec_flanges.png",
   "sha256": "89844a2326846b78986d24dc4eec7751d373c7e2b9ef97b5688696091c32a51e"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-45_base_bore.png",
   "sha256": "6cd48f161cb614a7f64f0846e39834cfc11ba9a92105745cec668b88caaacfd1"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-105_base_bore.png",
   "sha256": "8aa3df8c1f4f1ebcd95f632ce9fe49eacf25949e553bb5badeefa34db4b35f61"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-60_top_bore_w3.png",
   "sha256": "d3bde5253d819d70a8fa5d20b5664dcfb786efa67b48fb8fd81a9f235322df78"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-210_top_bore.png",
   "sha256": "6efa7be178935b633b7e648afffc48c98f7620499a9e7ca2403c6d494f5ae959"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-200_w1.png",
   "sha256": "8c9c069d503e55f8a4aa1af609e1a8450d14e1ca121432c58f9c59d06c75bdc6"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-55_w4.png",
   "sha256": "64b41b5f4c20dd8daf318c6f2a06d772ae6a1875195803fd7f8cab354fb6247a"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_z-100_profile.png",
   "sha256": "884bfe8bddc10a43dad4d631ffa872134e69b66d9749c2890441964275db6181"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_y100_wall.png",
   "sha256": "14bfe4d6a099cb3832034ff85ff3d82d6b18a1d2a70b229d86b9bcd25b85b898"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_y200_wall.png",
   "sha256": "d0974d6fee694379e4370f32499ddef043fc7af70e1a13ae4d703e0dc523e201"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_y150_windows.png",
   "sha256": "b2a0a80267cae4db912369f30bd052b7b5b1aec2b6dd50c35a6c7f6d9c7c867a"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_y60_w4.png",
   "sha256": "67770763500038249dbd13652416a4afded07a77a9be51a2749f444bb28d8d76"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_y3_base_bores.png",
   "sha256": "845b6fe1ef45980aafaed39bcc59e34cd031d53f9d76cc217880e0acf1f7c5aa"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_y212_top_bores.png",
   "sha256": "4d472eef3c953d7249ec311a58892d8ac81f371e358f51572507171c789f0d18"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_asm_z-200_pump.png",
   "sha256": "f02d101427d33129088396da8473f1bf14396f81867ef017a561028783077b3c"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_front_asm_y40_pump_axis.png",
   "sha256": "f013d41ef5d0c98d37a90ae94eb02a03ea7cd6ef70b82ddb01b76c3a449a039f"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_asm_z-50_carrier.png",
   "sha256": "f73c749d94eeeda70dae26c79aae7d2de7973bb84749a1c05601b2cf1faa1eb9"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v02_top_asm_z-45_screw_path.png",
   "sha256": "f494d9f8b8fca5bea96f09ac4171ce34336ba78d62a3547180026ba3e58dfe40"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3)",
  "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"
 },
 "gates": [
  {
   "gate": "U-01.solid_count",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01.brep_valid",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01.naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "exactly_one_solid",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_x",
   "measured": 12.0,
   "unit": "mm",
   "required": "in [11.9, 12.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_x",
   "measured": 12.0,
   "unit": "mm",
   "required": "in [11.9, 12.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_y",
   "measured": 215.0,
   "unit": "mm",
   "required": "in [214.9, 215.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_y",
   "measured": 215.0,
   "unit": "mm",
   "required": "in [214.9, 215.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_z",
   "measured": 210.0,
   "unit": "mm",
   "required": "in [209.9, 210.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_z",
   "measured": 210.0,
   "unit": "mm",
   "required": "in [209.9, 210.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_x",
   "measured": 59.0,
   "unit": "mm",
   "required": "in [58.9, 59.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_x",
   "measured": 71.0,
   "unit": "mm",
   "required": "in [70.9, 71.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_y",
   "measured": 0.0,
   "unit": "mm",
   "required": "in [-0.1, 0.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_y",
   "measured": 215.0,
   "unit": "mm",
   "required": "in [214.9, 215.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_z",
   "measured": -240.0,
   "unit": "mm",
   "required": "in [-240.1, -239.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_z",
   "measured": -30.0,
   "unit": "mm",
   "required": "in [-30.1, -29.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02.size_x",
   "measured": 12.0,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 208.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "D-02.size_y",
   "measured": 215.0,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 5.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "D-02.size_z",
   "measured": 210.0,
   "unit": "mm",
   "required": "<= 250.0",
   "margin": 40.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "REQ-02.rail_wet_face_min_x",
   "measured": 59.0,
   "unit": "mm",
   "required": "in [58.9, 59.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-05.min_x",
   "measured": 59.0,
   "unit": "mm",
   "required": ">= 59.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "REQ-06.max_y",
   "measured": 215.0,
   "unit": "mm",
   "required": "in [214.9, 215.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-08.max_x",
   "measured": 71.0,
   "unit": "mm",
   "required": "<= 71.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02.wet_face_x.y100_z-100",
   "measured": 63.0,
   "unit": "mm",
   "required": "in [62.9, 63.1]",
   "margin": 0.1,
   "at": "(63.0000, 100.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.elec_face_x.y100_z-100",
   "measured": 67.0,
   "unit": "mm",
   "required": "in [66.9, 67.1]",
   "margin": 0.1,
   "at": "(67.0000, 100.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.wet_face_x.y100_z-170",
   "measured": 63.0,
   "unit": "mm",
   "required": "in [62.9, 63.1]",
   "margin": 0.1,
   "at": "(63.0000, 100.0000, -170.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.elec_face_x.y100_z-170",
   "measured": 67.0,
   "unit": "mm",
   "required": "in [66.9, 67.1]",
   "margin": 0.1,
   "at": "(67.0000, 100.0000, -170.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.wet_face_x.y200_z-100",
   "measured": 63.0,
   "unit": "mm",
   "required": "in [62.9, 63.1]",
   "margin": 0.1,
   "at": "(63.0000, 200.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.elec_face_x.y200_z-100",
   "measured": 67.0,
   "unit": "mm",
   "required": "in [66.9, 67.1]",
   "margin": 0.1,
   "at": "(67.0000, 200.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.wet_face_x.y200_z-170",
   "measured": 63.0,
   "unit": "mm",
   "required": "in [62.9, 63.1]",
   "margin": 0.1,
   "at": "(63.0000, 200.0000, -170.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.elec_face_x.y200_z-170",
   "measured": 67.0,
   "unit": "mm",
   "required": "in [66.9, 67.1]",
   "margin": 0.1,
   "at": "(67.0000, 200.0000, -170.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-08.wall_elec_face_x",
   "measured": 67.0,
   "unit": "mm",
   "required": "<= 70.0",
   "margin": 3.0,
   "at": "(67.0000, 100.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-03.underside_faces",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.underside_bore_mouths",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.underside_y",
   "measured": -0.0,
   "unit": "mm",
   "required": "in [-0.1, 0.1]",
   "margin": 0.1,
   "at": "(59.0000, 0.0000, -240.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.underside_x_from",
   "measured": 59.0,
   "unit": "mm",
   "required": "in [58.9, 59.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.underside_x_to",
   "measured": 71.0,
   "unit": "mm",
   "required": "in [70.9, 71.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.underside_z_from",
   "measured": -240.0,
   "unit": "mm",
   "required": "in [-240.1, -239.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.underside_z_to",
   "measured": -30.0,
   "unit": "mm",
   "required": "in [-30.1, -29.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.rail_top_y.x60",
   "measured": 12.0,
   "unit": "mm",
   "required": "in [11.9, 12.1]",
   "margin": 0.1,
   "at": "(60.0000, 12.0000, -140.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03.rail_top_y.x69",
   "measured": 12.0,
   "unit": "mm",
   "required": "in [11.9, 12.1]",
   "margin": 0.1,
   "at": "(69.0000, 12.0000, -140.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05.plane_faces",
   "measured": 36,
   "unit": "count",
   "required": "== 36",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.plane_faces",
   "measured": 36,
   "unit": "count",
   "required": "== 36",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.cylinder_faces",
   "measured": 10,
   "unit": "count",
   "required": "== 10",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.cylinder_faces",
   "measured": 10,
   "unit": "count",
   "required": "== 10",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.concave_cylinders",
   "measured": 10,
   "unit": "count",
   "required": "== 10",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.concave_cylinders",
   "measured": 10,
   "unit": "count",
   "required": "== 10",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.convex_cylinders",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.convex_cylinders",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.cone_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.cone_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.sphere_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.sphere_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.torus_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.torus_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bspline_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.bspline_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.other_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.other_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.bores",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_from_below",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_from_above",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.window_half_cylinders_r7",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.window_half_cylinders_r7",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.base.x65_z-45.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-45.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-45.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-45.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-45.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-45.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-45.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.base.x65_z-45.across_x",
   "measured": 12.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.0,
   "at": "[(71.0, 3.0, -45.0), (59.0, 3.0, -45.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.base.x65_z-45.elec",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(71.0000, 3.0000, -45.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.base.x65_z-45.wet",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(59.0000, 3.0000, -45.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.base.x65_z-105.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-105.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-105.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-105.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-105.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-105.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-105.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.base.x65_z-105.across_x",
   "measured": 12.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.0,
   "at": "[(71.0, 3.0, -105.0), (59.0, 3.0, -105.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.base.x65_z-105.elec",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(71.0000, 3.0000, -105.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.base.x65_z-105.wet",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(59.0000, 3.0000, -105.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.base.x65_z-165.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-165.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-165.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-165.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-165.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-165.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-165.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.base.x65_z-165.across_x",
   "measured": 12.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.0,
   "at": "[(71.0, 3.0, -165.0), (59.0, 3.0, -165.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.base.x65_z-165.elec",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(71.0000, 3.0000, -165.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.base.x65_z-165.wet",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(59.0000, 3.0000, -165.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.base.x65_z-225.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-225.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-225.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.base.x65_z-225.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-225.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-225.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.base.x65_z-225.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.base.x65_z-225.across_x",
   "measured": 12.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.0,
   "at": "[(71.0, 3.0, -225.0), (59.0, 3.0, -225.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.base.x65_z-225.elec",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(71.0000, 3.0000, -225.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.base.x65_z-225.wet",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(59.0000, 3.0000, -225.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-07.top.x65_z-60.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.top.x65_z-60.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.top.x65_z-60.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.top.x65_z-60.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.top.x65_z-60.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.top.x65_z-60.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.top.x65_z-60.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(65.0000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.top.x65_z-60.across_x",
   "measured": 11.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 3.0,
   "at": "[(70.5, 212.0, -60.0), (59.5, 212.0, -60.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.top.x65_z-60.elec",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(70.5000, 212.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.top.x65_z-60.wet",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(59.5000, 212.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-07.top.x65_z-210.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.top.x65_z-210.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.top.x65_z-210.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.top.x65_z-210.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.top.x65_z-210.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.top.x65_z-210.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.top.x65_z-210.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(65.0000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.top.x65_z-210.across_x",
   "measured": 11.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 3.0,
   "at": "[(70.5, 212.0, -210.0), (59.5, 212.0, -210.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.top.x65_z-210.elec",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(70.5000, 212.0000, -210.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.top.x65_z-210.wet",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(59.5000, 212.0000, -210.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03b.widest_bore_bridge",
   "measured": 4.0,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": 1.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-04.w1_y150_z-200.diameter",
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -200.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w1_y150_z-200.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -200.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w1_y150_z-200.apex_above_centre",
   "measured": 13.999999999999972,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -186.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w2_y150_z-130.diameter",
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -130.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w2_y150_z-130.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -130.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w2_y150_z-130.apex_above_centre",
   "measured": 13.999999999999991,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -116.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w3_y150_z-60.diameter",
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w3_y150_z-60.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w3_y150_z-60.apex_above_centre",
   "measured": 13.999999999999991,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 150.0000, -46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-55.diameter",
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 60.0000, -55.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-55.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 60.0000, -55.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-55.apex_above_centre",
   "measured": 13.999999999999991,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 60.0000, -41.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4.front_end_closed",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.no_collar",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "U-03.plate.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(67.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.plate.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.coax.x65_z-45",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-01.plate_coax.x65_z-45",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "U-03.coax.x65_z-105",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-01.plate_coax.x65_z-105",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "U-03.coax.x65_z-165",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-01.plate_coax.x65_z-165",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "U-03.coax.x65_z-225",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-01.plate_coax.x65_z-225",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, -6.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "U-03.c03.clearance",
   "measured": 17.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 14.0,
   "at": "(59.0000, 0.0000, -240.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-05.c03.clearance",
   "measured": 17.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 14.0,
   "at": "(59.0000, 0.0000, -240.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.c03.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.h01.clearance",
   "measured": 7.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 4.5,
   "at": "(63.0000, 40.0000, -202.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-05.h01.clearance",
   "measured": 7.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 4.5,
   "at": "(63.0000, 40.0000, -202.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.h01.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.c04.clearance",
   "measured": 9.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 6.0,
   "at": "(59.0000, 0.0000, -157.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-05.c04.clearance",
   "measured": 9.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 6.0,
   "at": "(59.0000, 0.0000, -157.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.c04.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.h11.clearance",
   "measured": 20.160978383825217,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 17.160978384,
   "at": "(63.0000, 99.3565, -97.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-05.h11.clearance",
   "measured": 20.160978383825217,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 17.160978384,
   "at": "(63.0000, 99.3565, -97.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.h11.interference",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0 mm3",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.g01.clearance",
   "measured": 18.682723775766473,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 15.682723776,
   "at": "(59.5000, 207.0000, -30.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-05.g01.clearance",
   "measured": 18.682723775766473,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 15.682723776,
   "at": "(59.5000, 207.0000, -30.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.g01.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03.c05_box.clearance",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 4.0",
   "margin": 0.0,
   "at": "(59.0000, 0.0000, -30.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "U-03(b)",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "U-04.part.solids",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.volume_delta",
   "measured": 1.7462298274040222e-10,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -1.7462298274040222e-10,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.faces_delta",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.valid_after",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.solids",
   "measured": 8,
   "unit": "count",
   "required": "== 8",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.faces_delta",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.labels",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_c02_bulkhead.volume_delta",
   "measured": 1.7462298274040222e-10,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -1.7462298274040222e-10,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_c01_frame.volume_delta",
   "measured": 0.0,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_c03_cradle.volume_delta",
   "measured": 0.0,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_h01_pump.volume_delta",
   "measured": 4.307366907596588e-09,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -4e-09,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_c04_mount.volume_delta",
   "measured": 0.0,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_h11_thermoblock.volume_delta",
   "measured": 0.05239051367971115,
   "unit": "mm3",
   "required": "in [0, 0] mm3",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_g01_housing.volume_delta",
   "measured": 5.093170329928398e-10,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -1e-09,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_c05_foot_reference_A02.volume_delta",
   "measured": 0.0,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01a",
   "measured": 2.0,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 1.2,
   "at": "(63.0000, 207.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 2.0,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 0.0,
   "at": "(63.0000, 207.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-06a",
   "measured": 2.0,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 1.0,
   "at": "(63.0000, 207.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06(Soft)",
   "measured": 2.0,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 0.0,
   "at": "(63.0000, 207.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03a",
   "measured": 45.0,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": 0.0,
   "at": "(67.0000, 150.0000, -186.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "U-07.mesh.bodies",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.mesh.naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.mesh.winding",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.angular_tolerance",
   "measured": 0.2,
   "unit": "rad",
   "required": "<= 0.2309721947249083",
   "margin": 0.030972195,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.max_sagitta",
   "measured": 0.004895066481245138,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.005104934,
   "at": "(64.0000, 155.6282, -204.1538) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-08",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "D-04a",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "D-07",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "E-06",
   "measured": null,
   "unit": "",
   "required": "reviewer",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "REQ-09(Soft)",
   "measured": null,
   "unit": "",
   "required": "bench",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-11"
   ]
  }
 ],
 "sweep": [
  {
   "parameter": "bore_d",
   "values": [
    3.95,
    4.0,
    4.05
   ],
   "all_built": true,
   "worst_gate": "U-04.assembly.od_h01_pump.volume_delta",
   "worst_margin": -4e-09,
   "failing": {
    "low": [],
    "nominal": [],
    "high": []
   }
  },
  {
   "parameter": "bore_depth",
   "values": [
    5.9,
    6.0,
    6.1
   ],
   "all_built": true,
   "worst_gate": "D-01b",
   "worst_margin": -0.1,
   "failing": {
    "low": [],
    "nominal": [],
    "high": [
     "D-01b",
     "U-06(Soft)"
    ]
   }
  },
  {
   "parameter": "bore_shift (dx, dz)",
   "values": [
    "(-0.07, -0.07)",
    "0",
    "(+0.07, +0.07)"
   ],
   "all_built": true,
   "worst_gate": "U-04.assembly.od_h01_pump.volume_delta",
   "worst_margin": -4e-09,
   "failing": {
    "low": [],
    "nominal": [],
    "high": []
   }
  },
  {
   "parameter": "wall_x0 / wall_x1",
   "values": [
    "62.9 / 66.9",
    "63.0 / 67.0",
    "63.1 / 67.1"
   ],
   "all_built": true,
   "worst_gate": "U-04.assembly.od_h01_pump.volume_delta",
   "worst_margin": -4e-09,
   "failing": {
    "low": [],
    "nominal": [],
    "high": []
   }
  },
  {
   "parameter": "brail_x0",
   "values": [
    58.9,
    59.0,
    59.1
   ],
   "all_built": true,
   "worst_gate": "REQ-05.min_x",
   "worst_margin": -0.1,
   "failing": {
    "low": [
     "REQ-05.min_x",
     "U-03.c05_box.clearance"
    ],
    "nominal": [],
    "high": []
   }
  },
  {
   "parameter": "brail_x1",
   "values": [
    70.9,
    71.0,
    71.1
   ],
   "all_built": true,
   "worst_gate": "REQ-08.max_x",
   "worst_margin": -0.1,
   "failing": {
    "low": [],
    "nominal": [],
    "high": [
     "REQ-08.max_x"
    ]
   }
  }
 ],
 "least_sure": [
  "D-01b and U-06 at margin 0.000 on the top-rail bores. The Ø4.0 bore on x 65 is exactly as wide as the wall (x 63 … 67), so the edge of its floor (y 209) lies 2.0 above the top rail's underside (y 207) along the wall-face lines; `min_wall` reads 2.000 at (63, 207, −60). A bore 6.1 deep, inside REQ-07's ±0.1, reads 1.9 and fails D-01b. The spec's D-01b row names 3.5 and 4.0 beside the bores but not this floor. A melted-in Ø4.6 insert widens the bore to x 62.7 … 67.3, over the flange, where 2.0 or more stays under it only while the bore is no deeper than 6.0.",
  "The D-03a gate reads the census on a derived solid (the six named-exception bores refilled by position), because `overhang_census` takes no region; the whole-part census reads 0° at the bore crowns, and the exception is not yet signed by the Usta. The window gables read exactly 45.0° (margin 0, planar).",
  "Three envelope rows sit on their limits by the spec's own numbers: REQ-05 min_x 59.0, REQ-08 max_x 71.0, and the carrier box at 4.0. Printed standing on z −240, the first layers' squish (elephant's foot) widens only the rear end, but any outward error on the rail's wet face breaks REQ-05 and the box clearance. The ledger text also lags §4 in two rows (A-05 names the top bores at x 67.5, A-04 window 4 at z −40); the build follows §4, REQ-07 and REQ-04 (x 65, z −55)."
 ],
 "stopped": false
}
```
