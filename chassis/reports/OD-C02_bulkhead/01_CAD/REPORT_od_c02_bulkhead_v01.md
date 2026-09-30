# REPORT — od_c02_bulkhead v01 (20260930-od-c02-bulkhead)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · plan `01_CAD/DESIGN_PLAN.md` · 2026-09-30 UTC · brief WP-02, build attempt 1 of 2 · **outcome: STOPPED (D9)**

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 119de1e798b8c65da5e8bbb882fdb86e1b358b0a7813cb16654dc2d406cf4005 | the plan (D2) |
| `01_CAD/probe/versions_v01.py` | 06ff355b92cf96f5b7388ad2c303837d84f9ec911ee1c8632e2438cf5ad81c6d | D0 versions |
| `01_CAD/probe/probe_placements_v01.py` | 0f524e795182d24b65b2470d8274c66cb0ad2ebad87e417a7b9a39c9180e9daa | D2 probe: plate, inserts, neighbours as placed |
| `01_CAD/probe/probe_placements_v01.json` | 49e722eb2c97c37133efd8b351fc29e35a377b72c281176ab3e8e2ca5be18883 | probe results |
| `01_CAD/check_od_c02_bulkhead.py` | 54e49e29975876224d3817c7ee8ba6fcfbe425ffad6662cca6253a109ee95d48 | checks, written before the build (D3); ray bounds and the assembly row corrected after the first run (section 8) |
| `01_CAD/build_od_c02_bulkhead.py` | 29dfaeb955eb3227a9d69fddc43c93549d6258a316d38f867753724cda72ff53 | parametric build script (D4) |
| `01_CAD/build_record_v01.json` | f813f4e36fa616d7a8be2d1a8a583699e91977d3dfdcdc01f5a6e2570ada8551 | build record: parameters, export hashes, placements |
| `01_CAD/check_od_c02_bulkhead_v01.json` | fb9a1e8e4344dfdd7d1d0bcbda8728e8a34508e936f9278ce644cce64d5e345f | check results (167 rows, facts) |
| `01_CAD/check_od_c02_bulkhead_v01.log` | 73badc04841523661e2f322bb1d7decb377011a97245566320071988bace91dd | check run log |
| `01_CAD/sections_od_c02_bulkhead.py` | 00dd32b9c26cf949064c5af73d93ff24b90e6d21a32f0f998a208f09b5734b26 | sections script (D6) |
| `01_CAD/sections_v01.json` | 46e96abb63b69cfcf195559397d173a0f2361433539b31e412ebb67f83333681 | sections log |
| `02_STEP_STL/od_c02_bulkhead_C1_v01.step` | 4a6e61c341ee0c4a36305339ba76d749b3848a5e8195e36d15dabce78cd0b2a8 | AP242, re-imported for every measurement |
| `02_STEP_STL/od_c02_assembly_C1_v01.step` | 293d8e15c5fd6932036fbf078e749a23f048f7bb03df2b8bd67e5635deeede90 | AP242 check assembly, 8 labelled solids |
| `02_STEP_STL/od_c02_bulkhead_C1_v01.stl` | eef22a334120b267b552fb465a4ae94eff46770dbc3edfaf06666c7a15cab96e | tolerance 0.01 mm / angular 0.20 rad, 4264 triangles, cached triangulation cleared by write_stl |
| `03_Sections/od_c02_bulkhead_v01_left_x65_wall.png` | 9ebff2b272dccd49190b5f7ad2d7915dc260b440b3b5701255936560ca5bd12d | left x = 65.00 mm through (65.0, 100.0, -135.0); cut 44007.72 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_left_x62_collars.png` | 80de168602adfc8de06bcfb184ef51fded0b1a695d1eccd1f7d5fd8dbbbf2940 | left x = 62.00 mm through (62.0, 100.0, -135.0); cut 4590.08 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_left_x71_ribs.png` | 0837a822afa048db39e0a627002f19195081b5eb0cee148ecb0a64aebd2c90c9 | left x = 71.00 mm through (71.0, 100.0, -135.0); cut 3240.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_z-45_cbore_w4.png` | 02f282044d2ebb29f9ede59a53fb2c4865b372ed550ceb4e12a4c74dc1a0d28a | top z = -45.00 mm through (65.0, 100.0, -45.0); cut 912.86 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_z-105_cbore.png` | 5bfded878a3a70a1305666e307abb4d3c5f76caae0a46c0099a8b7fc911f7ed6 | top z = -105.00 mm through (65.0, 100.0, -105.0); cut 934.40 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_z-60_insert_w3.png` | b75a42c7f5c1341aa19a11873bafe8399ac1b75802450ac011edc8c284cd02b6 | top z = -60.00 mm through (65.0, 100.0, -60.0); cut 928.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_z-70_rib.png` | 2badf38686c31553a1f8a82119110a74f03ac13b0ebaeea0130482845ed590c2 | top z = -70.00 mm through (65.0, 100.0, -70.0); cut 1975.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_z-200_rib_w1.png` | fddd1e1ee665067723fe7e8c0a8e4daa204f09325af44f965df62821c1f7da57 | top z = -200.00 mm through (65.0, 100.0, -200.0); cut 1927.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_z-100_profile.png` | 3d28685ed517d7827628f16bb083b6291d6d6644d5a45730cdb38dd6b1e6bdcc | top z = -100.00 mm through (65.0, 100.0, -100.0); cut 1000.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_y100_wall.png` | ade0f6ac94b50a30a09eeadae18d286e0bd8a6c21b0dfd433446c6f16e9673d4 | front y = 100.00 mm through (65.0, 100.0, -135.0); cut 880.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_y200_wall.png` | 16ae4aaa133a63943d7f9ba96391cbdf668291074472ca5f6dcadd05e24499e0 | front y = 200.00 mm through (65.0, 200.0, -135.0); cut 880.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_y150_windows.png` | 36dc000505ad29e328218a73efa41fcefc30c14ec40d82dffff7ca22d710a6ff | front y = 150.00 mm through (65.0, 150.0, -135.0); cut 656.97 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_y60_w4.png` | de20c00ef7092e7e09891469b20dd131ddcebe0e1daeb75af3b59dfd997b2f27 | front y = 60.00 mm through (65.0, 60.0, -135.0); cut 816.00 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_y8_cbores.png` | 0c2ab2e343c3fee04017ce10bad4385d38f76a68c342a4aab44ae8796cd81292 | front y = 8.00 mm through (65.0, 8.0, -135.0); cut 2177.27 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_y212_inserts.png` | 9baf049ac7fe58804441f0b7a9afa4ecdaff35c7066cdf3a12d167dddfa702a7 | front y = 212.00 mm through (65.0, 212.0, -135.0); cut 2284.87 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_asm_z-200_pump.png` | d576c8d2a14b18e5843b2e498fcb2712282a28750fb2f0e8240dbcbba6e0c6e1 | top z = -200.00 mm through (40.0, 100.0, -200.0); cut 6690.81 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_front_asm_y40_pump_axis.png` | 94e37f07a2aafd743183f64b8826fcfd93c0751150e77f4c94805d6e3b529ae5 | front y = 40.00 mm through (40.0, 40.0, -135.0); cut 12829.81 mm²; nothing clipped (0) |
| `03_Sections/od_c02_bulkhead_v01_top_asm_z-50_carrier.png` | afb82bb1a70444e2e1e4555529821ead7a869eb7f9e2bb48167958be35a91308 | top z = -50.00 mm through (40.0, 100.0, -50.0); cut 25519.31 mm²; nothing clipped (0) |

Inputs checked against the brief before any work: all nine SHA-256 match. `01_CAD/sweep_v01/_mesh_check/remesh_check.stl` is the check's scratch re-mesh for U-07, not a deliverable. No 3MF: the orchestrator's step. STL facts for it: 4264 triangles, mesh volume 213865.587 mm³ (B-rep 213862.736 mm³), bounding box [59.0, 0.0, -240.0] … [73.0, 215.0, -30.0] (size [14.0, 215.0, 210.0]).

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3) · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (clean)

## 3. Gate self-check

Every value is measured from the re-imported STEP (`check_od_c02_bulkhead_v01.json`, 167 rows: 55 PASS, 100 PASS (assumed), 4 FAIL, 5 INCONCLUSIVE, 3 N/A). One line per §5 row with its worst sub-row; every sub-row is in the JSON block. Bands from GATES §0 (mm 0.005, deg and mm³ 0.001, counts 0). `min_wall`, `min_wall_wide` and `overhang_census` ran at spacing 0.7 (the brief's note; largest step 0.697674 mm).

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 (3 rows; worst: `U-01.solid_count`) | 1 count | == 1 | 0 | — | PASS | — |
| U-02 (3 rows; worst: `U-02.size_x`) | 14 mm | in [13.9, 14.1] | 0.1 | — | PASS | — |
| U-03 (a) (17 rows; worst: `U-03.h11.interference`) | — mm3 | <= 0 mm3 | — | — | INCONCLUSIVE | A-01, A-02 |
| U-04 (15 rows; worst: `U-04.assembly.od_h11_thermoblock.volume_delta`) | 0.0524 mm3 | in [0, 0] mm3 | — | — | INCONCLUSIVE | — |
| U-05 (6 rows; worst: `U-05.bores`) | 10 count | == 10 | 0 | — | PASS | — |
| U-06 (Soft) (1 rows; worst: `U-06(Soft)`) | 0.2652 mm | >= 2.0 | -1.7348 | (66.7000, 55.8125, -30.1875) mm | FAIL | — |
| U-07 (5 rows; worst: `U-07.mesh.bodies`) | 1 count | == 1 | 0 | — | PASS | — |
| U-08 (1 rows; worst: `U-08`) | — | N/A | — | — | N/A | — |
| D-01a (1 rows; worst: `D-01a`) | 1.75 mm | >= 0.8 | 0.95 | (70.0000, 12.0000, -165.0000) mm | PASS | — |
| D-01b (1 rows; worst: `D-01b`) | 1.75 mm | >= 1.75 | 0 | (70.0000, 12.0000, -165.0000) mm | PASS | — |
| D-02 (3 rows; worst: `D-02.size_y`) | 215 mm | <= 220.0 | 5 | — | PASS (assumed: A-08) | A-08 |
| D-03a (1 rows; worst: `D-03a`) | 0 deg | >= 45.0 | -45 | (67.0000, 12.0000, -202.0000) mm | FAIL | A-10 |
| D-03b (1 rows; worst: `D-03b.rib_underside_span_y`) | 195 mm | <= 5.0 | -190 | — | FAIL | — |
| D-04a (4 rows; worst: `D-04a.z-45.diameter`) | 3.4 mm | >= 3.25 | 0.15 | (65.0000, 0.0000, -45.0000) mm | PASS | — |
| D-05a (2 rows; worst: `D-05a.x67.5_z-60.across_x`) | 11 mm | >= 8.0 | 3 | [(73.0, 212.0, -60.0), (62.0, 212.0, -60.0)] | PASS (assumed: A-05) | A-05 |
| D-05b (6 rows; worst: `D-05b.x67.5_z-60.diameter`) | 4 mm | in [3.95, 4.05] | 0.05 | (67.5000, 209.0000, -60.0000) mm | PASS (assumed: A-05) | A-05 |
| D-06a (1 rows; worst: `D-06a`) | 1.75 mm | >= 1.0 | 0.75 | (70.0000, 12.0000, -165.0000) mm | PASS | — |
| D-07 (1 rows; worst: `D-07`) | — | N/A | — | — | N/A | — |
| J-05 (4 rows; worst: `J-05.x67.5_z-60.elec`) | 3.5 mm | >= 3.0 | 0.5 | (73.0000, 212.0000, -60.0000) mm | PASS | — |
| E-06 (1 rows; worst: `E-06`) | — | reviewer | — | — | INCONCLUSIVE | — |
| REQ-01 (24 rows; worst: `REQ-01.hole.z-45.through`) | 1 bool | == 1 | 0 | (65.0000, 0.0000, -45.0000) mm | PASS (assumed: A-01, A-03) | A-01, A-03 |
| REQ-02 (9 rows; worst: `REQ-02.rail_wet_face_min_x`) | 59 mm | in [58.9, 59.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| REQ-03 (8 rows; worst: `REQ-03.underside_faces`) | 1 count | == 1 | 0 | — | PASS (assumed: A-01) | A-01 |
| REQ-04 (17 rows; worst: `REQ-04.w4.front_end_closed`) | 2 count | == 1 | -1 | — | FAIL | A-04 |
| REQ-05 (6 rows; worst: `REQ-05.min_x`) | 59 mm | >= 59.0 | 0 | — | PASS (assumed: A-02) | A-02 |
| REQ-06 (1 rows; worst: `REQ-06.max_y`) | 215 mm | in [214.9, 215.1] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-07 (8 rows; worst: `REQ-07.x67.5_z-60.blind`) | 0 bool | == 0 | 0 | (67.5000, 209.0000, -60.0000) mm | PASS (assumed: A-05) | A-05 |
| REQ-08 (2 rows; worst: `REQ-08.max_x`) | 73 mm | <= 73.0 | 0 | — | PASS (assumed: A-07) | A-07 |
| REQ-09 (Soft) (1 rows; worst: `REQ-09(Soft)`) | — | bench | — | — | INCONCLUSIVE | A-11 |
| exactly_one_solid (1 rows; worst: `exactly_one_solid`) | 1 count | == 1 | 0 | — | PASS | — |
| feature_census (3 rows; worst: `feature_census.bores`) | 10 count | == 10 | 0 | — | PASS | — |
| envelope_within_spec (9 rows; worst: `envelope_within_spec.size_x`) | 14 mm | in [13.9, 14.1] | 0.1 | — | PASS | — |

**U-03 (a) and REQ-05, on the parts as placed in the assembly STEP** (nearest point on the bulkhead in `At`):

| Row | Measured | Required | Margin | At | Status |
|---|---|---|---|---|---|
| `REQ-05.min_x` | 59 mm | >= 59.0 | 0 | — | PASS (assumed: A-02) |
| `U-03.plate.clearance` | 0 mm | == 0.0 | 0 | (70.0000, 0.0000, -30.0000) mm | PASS (assumed: A-01, A-02) |
| `U-03.plate.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.coax.z-45` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -45.0000) mm | PASS (assumed: A-01, A-02) |
| `U-03.coax.z-105` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -105.0000) mm | PASS (assumed: A-01, A-02) |
| `U-03.coax.z-165` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -165.0000) mm | PASS (assumed: A-01, A-02) |
| `U-03.coax.z-225` | 0 mm | <= 0.1 | 0.1 | (65.0000, -6.0000, -225.0000) mm | PASS (assumed: A-01, A-02) |
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
| `U-03.g01.clearance` | 20.3826 mm | >= 3.0 | 17.3826 | (62.0000, 207.0000, -30.0000) mm | PASS (assumed: A-01, A-02) |
| `REQ-05.g01.clearance` | 20.3826 mm | >= 3.0 | 17.3826 | (62.0000, 207.0000, -30.0000) mm | PASS (assumed: A-02) |
| `U-03.g01.interference` | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02) |
| `U-03.c05_box.clearance` | 4 mm | >= 4.0 | 0 | (59.0000, 0.0000, -30.0000) mm | PASS (assumed: A-01, A-02) |

The rail underside touches the plate at clearance 0.0 with 0.0 mm³ in common: the designed contact. Every bulkhead hole is coaxial with its plate insert (offset 0.0000). OD-H01 is nearest the wall face x 63 (7.5 mm, at the pump's +X end x 55.5, y 40); it stays 3.5 mm from the plane x 59 but above the rail (y 40 > 12). The carrier box sits exactly at 4.0 (margin 0.0). OD-H11: clearance gated on distance, boolean INCONCLUSIVE by the row.

**REQ-04, the windows** (round part from three `radial_extent` rays at 200°, 270° and 340° on the lower half-circle at x 65, because `bore_census` does not count a 180° arc; the apex from the ray at 90°, toward +Z; the collar from the ray at 270° at x 62):

| Row | Measured | Required | Margin | At | Status |
|---|---|---|---|---|---|
| `REQ-04.w1_y150_z-200.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -200.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w1_y150_z-200.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 150.0000, -200.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w1_y150_z-200.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -186.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w1_y150_z-200.collar_od` | 18 mm | in [17.9, 18.1] | 0.1 | (62.0000, 150.0000, -209.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -130.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 150.0000, -130.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -116.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w2_y150_z-130.collar_od` | 18 mm | in [17.9, 18.1] | 0.1 | (62.0000, 150.0000, -139.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -60.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 150.0000, -60.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.apex_above_centre` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 150.0000, -46.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w3_y150_z-60.collar_od` | 18 mm | in [17.9, 18.1] | 0.1 | (62.0000, 150.0000, -69.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4_y60_z-40.diameter` | 14 mm | in [13.9, 14.1] | 0.1 | (65.0000, 60.0000, -40.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4_y60_z-40.offset` | 0 mm | <= 0.1 | 0.1 | (65.0000, 60.0000, -40.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4_y60_z-40.apex_above_centre` | — mm | in [13.9, 14.1] | — | — | INCONCLUSIVE |
| `REQ-04.w4_y60_z-40.collar_od` | 18 mm | in [17.9, 18.1] | 0.1 | (62.0000, 60.0000, -49.0000) mm | PASS (assumed: A-04) |
| `REQ-04.w4.front_end_closed` | 2 count | == 1 | -1 | — | FAIL |

Gable roof rays at 60° and 120° (reported, not gated): w1_y150_z-200 60°: 10.2487 (design 10.2487); w1_y150_z-200 120°: 10.2487 (design 10.2487); w2_y150_z-130 60°: 10.2487 (design 10.2487); w2_y150_z-130 120°: 10.2487 (design 10.2487); w3_y150_z-60 60°: 10.2487 (design 10.2487); w3_y150_z-60 120°: 10.2487 (design 10.2487); w4_y60_z-40 60°: 10.2487 (design 10.2487); w4_y60_z-40 120°: 10.2487 (design 10.2487). Window 4's apex ray finds no material (the gable runs out through the front end), and the front end z −30 is two faces, at y 0 … 56 and y 64 … 215: the window is an 8.0 wide notch open to the front end, not a window. Its collar is cut open at z −30 too.

**D-03a: the downward faces split by region** (build +Z; a 9 × 9 diagnostic grid per face, beside the census, which takes no region). The census over the whole part: least 0° at (67.0000, 12.0000, -202.0000) mm, 10320 downward samples, 7428 below 45°, sampling bound 0.009334°, per kind {'cylinder': 2.142857, 'plane': 0.0}.

| Region (by position) | Faces | Least angle (deg) |
|---|---|---|
| collar outer round part | 4 | 0.0000 |
| exception: counterbore 6.5 crown | 4 | 0.0000 |
| exception: hole 3.4 crown | 4 | 0.0000 |
| exception: insert bore 4.0 crown | 2 | 0.0000 |
| rib underside | 2 | 0.0000 |
| window roof or collar | 8 | 45.0000 |

Outside the named exception, the rib undersides (z −72 and z −202, 5.0 × 195.0 flat ceilings at x 67 … 72, y 12 … 207) and the collars' round lower halves (R 9.0 outer cylinders, x 61 … 63) read 0.0°. The window gables are planar at exactly 45.0° analytically and by the census (no curved face is tangent at 45° in this outline; the lower half-circle of a window faces up). The named-exception crowns (the ten small horizontal bores) read 0.0°, as expected; the exception covers them (bridges ≤ 6.5 here).

## 4. Robustness sweep (D7)

Not run. The nominal part fails the hard gates D-03a, D-03b and REQ-04 through geometry that no fit-critical parameter moves (rib direction, collar shape, window 4 position). A sweep cannot pass them, and the package stops at D9. `01_CAD/sweep_v01/` holds only the check's scratch mesh.

## 5. Build facts

- Envelope 14.000 × 215.000 × 210.000 mm at x 59.000 … 73.000, y 0.000 … 215.000, z -240.000 … -30.000; volume 213862.7 mm³; mass 228.8 g at 1070 kg/m³ (A-09); centre of mass (65.30, 105.14, -135.36).
- Fillets: none in the spec; none requested.
- Placements (assembly STEP, 8 labelled solids): OD-C01 at the identity; OD-C03 and OD-H01 at the OD-C01 §4 joint (local x → +Z, y → −Y, z → +X, origin (0, 40, −205)); OD-C04 and OD-H11 at the identity rotation, origin (0, 70, −140); OD-G01 v02 (local x → X, y → +Z, z → −Y, origin (0, 180.06, 32)); each by a RigidJoint on the bulkhead's machine frame connected to the part's own STEP origin; the carrier foot box `od_c05_foot_reference_A02` x ±55, y 0 … 210, z −70 … −26 from the brief's values. The joints are the spec's rotations; the probe's measured placements agree (plate top face y 0.000, inserts at x 65 with offset 0.000; OD-H01 max x 55.5).
- STL: `write_stl` at 0.01 mm / 0.20 rad (≤ 0.2310), 4264 triangles, sagitta at export 0.004968 mm; the re-mesh of the re-imported STEP reads 0.005 mm. `mesh_census`: 1 body, 0 naked edges, consistent winding.
- U-04: the part re-reads with volume delta 4.66e-07 mm³, faces delta 0, valid after 1. The assembly: 8 solids, faces delta 0, labels kept; per part volume deltas ≤ 4.7e-7 mm³ except OD-H11 0.0524 mm³ (unsound input, INCONCLUSIVE by the row). The whole-assembly `valid_after` reads 0 (curve on surface 0.00116 mm against the 0.00052 limit), which comes from the imported parts, as in the OD-C01 job; the bulkhead's own file is valid after re-import.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The wall stands on its base rail on the plate (contact 0.0, no interference), but it cannot be screwed down: the four counterbores lie under the wall (P4), so nothing holds it to the plate. |
| P2 | Function chains | The leak dam works: one rail underside face over x 59 … 70, z −240 … −30. The wire path does not: rib 2 (z −202 … −198) runs across window 1's electric-side mouth and covers the window's axis (ray from the axis at x 69.5 finds material at 0.0: w1_y150_z-200 90°: 0; w1_y150_z-200 270°: 0; w2_y150_z-130 90°: 58; w2_y150_z-130 270°: 68; w3_y150_z-60 90°: no material; w3_y150_z-60 270°: 8; w4_y60_z-40 90°: no material; w4_y60_z-40 270°: 28), and window 4 is a notch open to the front end, not a window. |
| P3 | Motion | No moving parts. |
| P4 | Human factors | An M3 × 8 cannot be driven into any counterbore: on each counterbore axis above y 12.5 the ray meets 202.5 mm of wall and top rail (z -45: [[0.0, 42.601020514], [52.398979486, 202.5]]; z -105: [[0.0, 202.5]]; z -165: [[0.0, 202.5]]; z -225: [[0.0, 202.5]]; at z −45 the gap is window 4). Only two 1.25 wide crescents of each Ø6.5 mouth are open beside the wall. |
| P5 | Next to a real product | A domain engineer would flag the screw pockets buried under the wall and the rib crossing the pump's wire window at once. |
| P6 | Floating, embedded, mirrored, upside-down | One solid; nothing floating or embedded; the gables point +Z (the print's up, A-10); the assembly poses are the OD-C01 joints. |

## 7. Library and tools used

Card: UNO10 U5 tank heat-set (size and position kept apart in U-02). Precedent: the OD-C01 job's probe, build, check and sections scripts (named by the brief). Tools: `tools.core` `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`, `file_sha256`; `tools.measure` `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, `min_wall_wide`, `overhang_census`, `radial_extent`, `clearance`, `mass_properties`, `mesh_census`; `tools.result.gate`; `tools.drawing.write_sections`. New job code: the downward-face split by region (a diagnostic beside the D-03a census), planar-face readings of the rail underside and the front end, and the three-ray circle for the windows' round part. Missing tools: none for a gated number; D-03b has no tool (GATES), so the designer's reading uses the rib underside's B-rep face box; `bore_census` cannot see a 180° arc (the windows' round part), so `radial_extent` reads it.

## 8. Deviations from the plan

- Geometry: none. The build follows plan §3 and §4.
- Check script, corrected after its first run and before any geometry change (the STEP was not re-exported): the window and collar rays had bounds the material crossed (`radial_extent` refuses them), so the inner rays run unbounded and the collar ray is bounded at 12 mm; the assembly holds 8 solids, not 7 (the SPEC count was wrong), and U-04 on the assembly is now gated per part. D-03b is read from the rib underside's face box rather than left to the reviewer only.
- Sections: the planned cut at x 69.5 was refused by the tool ("a wire of the cut face has no area", where rib 2 crosses window 1's mouth), so it was taken at x 71 instead (the ribs and the top rail).
- The plan's census wording (14 bores) was corrected in the plan before the build: `bore_census` counts 10; the windows' round parts are read by rays.

## 9. What I am least sure of

1. **The gable reading.** The spec's "45° gable roof … apex 7.0 above the circle's top" is built literally: straight sides from the centre height up to 7.0, then the roof to an apex 14.0 above the centre. A tangent teardrop would put the apex 2.9 above the top. Window 4 fails either way: with the tangent teardrop, 0.10 mm of wall is left between its apex (z −30.10) and the front end, and its collar still cannot close.
2. **The D-03a named exception has no Usta signature yet** (GATES §X item 1; spec §5 records it "for the Usta to confirm"). I applied it as the brief says and report the crowns apart. D-03a fails outside it regardless.
3. **Margins at zero.** D-01b reads 1.75 at the limit (the counterbore's electric side, x 68.25 … 70, as the spec derived), the carrier box clearance 4.0 at the limit, and REQ-05 min_x 59.0 and REQ-08 max_x 73.0 at their limits. U-06 wide reads 0.27 at window 4's roof meeting the front end, a knife edge that exists only because window 4 runs out.

## 10. Stop

Stopped at D9 after the nominal build: three hard gates fail through §4's own geometry, and two function chains are broken. None can be fixed without changing a spec value, so no fix cycle was used (0 of 3).

1. **D-03a: 0.0° outside the named exception.** Measured on the rib undersides (z −72 and −202, x 67 … 72, y 12 … 207) and the four collars' round lower halves (R 9.0). §4 calls the ribs prisms along Z, but at 4.0 thick along Z they print as horizontal shelves. §4 calls the collars' faces vertical, but a round collar's underside faces down.
   Options:
   - (a) Ribs as prisms along Z (horizontal stiffeners at fixed y, printing as walls).
   - (b) Ribs as 45° gussets (at least 5.0 along Z at the root, not 4.0).
   - (c) Supports under the ribs and collars by the spec's decision (GATES D-03a allows it).
   - (d) Collars with a 45° keel at the bottom (a teardrop outline toward −Z), or no collars.
2. **D-03b: the rib undersides are 5.0 × 195.0 unsupported ceilings** (span 195.0 between the rails, a 5.0 cantilever off the wall). Same options as item 1.
3. **REQ-04: window 4 at (y 60, z −40) runs out of the front end z −30.** The apex ray finds no material, and the front end reads 2 faces (required 1). The window is an 8.0 notch, and its collar is cut open.
   Options:
   - (a) Move window 4 to z ≤ −47.8 with the literal gable (apex 14.0 + collar 2.83 + 1.0 wall).
   - (b) Move it to z ≤ −43.7 with a tangent teardrop (apex 9.9 + collar 2.83 + 1.0).
   - (c) Lengthen the wall toward the front beyond z −30 (a §4 envelope change, U-02; the plate runs to z +100).
4. **Function, not a §5 threshold (P2, P4): the counterbores are under the wall**, so the M3 screws of A-03 cannot be driven. REQ-01's numbers pass (Ø6.5, depth 8.0, offset 0.0), but 202.5 mm of wall and top rail stand on each counterbore axis.
   Options:
   - (a) Move the screw line off the wall onto a wider electric-side rail, with new OD-C01 inserts. REQ-05 holds the wet side at x ≥ 59, and A-07 / REQ-08 cap x at 73, so this changes OD-C01 and §4.
   - (b) Screws from below through OD-C01, with nuts or inserts in the rail. This changes OD-C01.
   - (c) Access pockets through the wall above each counterbore, driven at an angle. This changes §4 and weakens the wall.
   - (d) Bond or clip the rail to the plate instead.
5. **Function (P2): rib 2 at z −200 runs across window 1's mouth** at (y 150, z −200). The ray from the window axis at x 69.5 starts in rib material.
   Options:
   - (a) Move rib 2 to z ≤ −212 (e.g. −215, clear of window 1's collar at z −209 and of the insert bore, which is in the top rail).
   - (b) Move window 1.
   - (c) Cut the rib at the window.

Each option changes a §4 value or an OD-C01 interface, so the decision is the Usta's. The spec needs an amendment before build attempt 2.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c02-bulkhead",
 "part": "od_c02_bulkhead",
 "tag": "v01",
 "spec_version": "1.0",
 "files": [
  {
   "path": "01_CAD/DESIGN_PLAN.md",
   "sha256": "119de1e798b8c65da5e8bbb882fdb86e1b358b0a7813cb16654dc2d406cf4005"
  },
  {
   "path": "01_CAD/probe/versions_v01.py",
   "sha256": "06ff355b92cf96f5b7388ad2c303837d84f9ec911ee1c8632e2438cf5ad81c6d"
  },
  {
   "path": "01_CAD/probe/probe_placements_v01.py",
   "sha256": "0f524e795182d24b65b2470d8274c66cb0ad2ebad87e417a7b9a39c9180e9daa"
  },
  {
   "path": "01_CAD/probe/probe_placements_v01.json",
   "sha256": "49e722eb2c97c37133efd8b351fc29e35a377b72c281176ab3e8e2ca5be18883"
  },
  {
   "path": "01_CAD/check_od_c02_bulkhead.py",
   "sha256": "54e49e29975876224d3817c7ee8ba6fcfbe425ffad6662cca6253a109ee95d48"
  },
  {
   "path": "01_CAD/build_od_c02_bulkhead.py",
   "sha256": "29dfaeb955eb3227a9d69fddc43c93549d6258a316d38f867753724cda72ff53"
  },
  {
   "path": "01_CAD/build_record_v01.json",
   "sha256": "f813f4e36fa616d7a8be2d1a8a583699e91977d3dfdcdc01f5a6e2570ada8551"
  },
  {
   "path": "01_CAD/check_od_c02_bulkhead_v01.json",
   "sha256": "fb9a1e8e4344dfdd7d1d0bcbda8728e8a34508e936f9278ce644cce64d5e345f"
  },
  {
   "path": "01_CAD/check_od_c02_bulkhead_v01.log",
   "sha256": "73badc04841523661e2f322bb1d7decb377011a97245566320071988bace91dd"
  },
  {
   "path": "01_CAD/sections_od_c02_bulkhead.py",
   "sha256": "00dd32b9c26cf949064c5af73d93ff24b90e6d21a32f0f998a208f09b5734b26"
  },
  {
   "path": "01_CAD/sections_v01.json",
   "sha256": "46e96abb63b69cfcf195559397d173a0f2361433539b31e412ebb67f83333681"
  },
  {
   "path": "02_STEP_STL/od_c02_bulkhead_C1_v01.step",
   "sha256": "4a6e61c341ee0c4a36305339ba76d749b3848a5e8195e36d15dabce78cd0b2a8"
  },
  {
   "path": "02_STEP_STL/od_c02_assembly_C1_v01.step",
   "sha256": "293d8e15c5fd6932036fbf078e749a23f048f7bb03df2b8bd67e5635deeede90"
  },
  {
   "path": "02_STEP_STL/od_c02_bulkhead_C1_v01.stl",
   "sha256": "eef22a334120b267b552fb465a4ae94eff46770dbc3edfaf06666c7a15cab96e"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_left_x65_wall.png",
   "sha256": "9ebff2b272dccd49190b5f7ad2d7915dc260b440b3b5701255936560ca5bd12d"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_left_x62_collars.png",
   "sha256": "80de168602adfc8de06bcfb184ef51fded0b1a695d1eccd1f7d5fd8dbbbf2940"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_left_x71_ribs.png",
   "sha256": "0837a822afa048db39e0a627002f19195081b5eb0cee148ecb0a64aebd2c90c9"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_z-45_cbore_w4.png",
   "sha256": "02f282044d2ebb29f9ede59a53fb2c4865b372ed550ceb4e12a4c74dc1a0d28a"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_z-105_cbore.png",
   "sha256": "5bfded878a3a70a1305666e307abb4d3c5f76caae0a46c0099a8b7fc911f7ed6"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_z-60_insert_w3.png",
   "sha256": "b75a42c7f5c1341aa19a11873bafe8399ac1b75802450ac011edc8c284cd02b6"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_z-70_rib.png",
   "sha256": "2badf38686c31553a1f8a82119110a74f03ac13b0ebaeea0130482845ed590c2"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_z-200_rib_w1.png",
   "sha256": "fddd1e1ee665067723fe7e8c0a8e4daa204f09325af44f965df62821c1f7da57"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_z-100_profile.png",
   "sha256": "3d28685ed517d7827628f16bb083b6291d6d6644d5a45730cdb38dd6b1e6bdcc"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_y100_wall.png",
   "sha256": "ade0f6ac94b50a30a09eeadae18d286e0bd8a6c21b0dfd433446c6f16e9673d4"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_y200_wall.png",
   "sha256": "16ae4aaa133a63943d7f9ba96391cbdf668291074472ca5f6dcadd05e24499e0"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_y150_windows.png",
   "sha256": "36dc000505ad29e328218a73efa41fcefc30c14ec40d82dffff7ca22d710a6ff"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_y60_w4.png",
   "sha256": "de20c00ef7092e7e09891469b20dd131ddcebe0e1daeb75af3b59dfd997b2f27"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_y8_cbores.png",
   "sha256": "0c2ab2e343c3fee04017ce10bad4385d38f76a68c342a4aab44ae8796cd81292"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_y212_inserts.png",
   "sha256": "9baf049ac7fe58804441f0b7a9afa4ecdaff35c7066cdf3a12d167dddfa702a7"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_asm_z-200_pump.png",
   "sha256": "d576c8d2a14b18e5843b2e498fcb2712282a28750fb2f0e8240dbcbba6e0c6e1"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_front_asm_y40_pump_axis.png",
   "sha256": "94e37f07a2aafd743183f64b8826fcfd93c0751150e77f4c94805d6e3b529ae5"
  },
  {
   "path": "03_Sections/od_c02_bulkhead_v01_top_asm_z-50_carrier.png",
   "sha256": "afb82bb1a70444e2e1e4555529821ead7a869eb7f9e2bb48167958be35a91308"
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
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_x",
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
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
   "measured": 210.000000000002,
   "unit": "mm",
   "required": "in [209.9, 210.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_z",
   "measured": 210.000000000002,
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
   "measured": 73.0,
   "unit": "mm",
   "required": "in [72.9, 73.1]",
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
   "measured": -29.999999999998,
   "unit": "mm",
   "required": "in [-30.1, -29.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02.size_x",
   "measured": 14.0,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 206.0,
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
   "measured": 210.000000000002,
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
   "measured": 73.0,
   "unit": "mm",
   "required": "<= 73.0",
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
   "measured": 70.0,
   "unit": "mm",
   "required": "in [69.9, 70.1]",
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
   "gate": "REQ-03.rail_top_y.x68.5",
   "measured": 12.0,
   "unit": "mm",
   "required": "in [11.9, 12.1]",
   "margin": 0.1,
   "at": "(68.5000, 12.0000, -140.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05.bores",
   "measured": 10,
   "unit": "count",
   "required": "== 10",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.bores",
   "measured": 10,
   "unit": "count",
   "required": "== 10",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_d3.4",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_d6.5",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_d4",
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
   "gate": "U-05.collar_half_cylinders_r9",
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
   "gate": "feature_census.collar_half_cylinders_r9",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.hole.z-45.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-45.offset",
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
   "gate": "REQ-01.hole.z-45.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-04a.z-45.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(65.0000, 0.0000, -45.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.cbore.z-45.diameter",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-45.depth",
   "measured": 8.0,
   "unit": "mm",
   "required": "in [7.9, 8.1]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-45.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -45.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-105.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-105.offset",
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
   "gate": "REQ-01.hole.z-105.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-04a.z-105.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(65.0000, 0.0000, -105.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.cbore.z-105.diameter",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-105.depth",
   "measured": 8.0,
   "unit": "mm",
   "required": "in [7.9, 8.1]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-105.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-165.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-165.offset",
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
   "gate": "REQ-01.hole.z-165.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-04a.z-165.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(65.0000, 0.0000, -165.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.cbore.z-165.diameter",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-165.depth",
   "measured": 8.0,
   "unit": "mm",
   "required": "in [7.9, 8.1]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-165.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -165.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-225.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.hole.z-225.offset",
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
   "gate": "REQ-01.hole.z-225.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "D-04a.z-225.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(65.0000, 0.0000, -225.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.cbore.z-225.diameter",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-225.depth",
   "measured": 8.0,
   "unit": "mm",
   "required": "in [7.9, 8.1]",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-01.cbore.z-225.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 4.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-60.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-60.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-60.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-60.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.x67.5_z-60.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.x67.5_z-60.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.x67.5_z-60.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(67.5000, 209.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.x67.5_z-60.across_x",
   "measured": 11.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 3.0,
   "at": "[(73.0, 212.0, -60.0), (62.0, 212.0, -60.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.x67.5_z-60.elec",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(73.0000, 212.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.x67.5_z-60.wet",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(62.0000, 212.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-07.x67.5_z-210.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-210.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-210.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-07.x67.5_z-210.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.x67.5_z-210.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.x67.5_z-210.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05b.x67.5_z-210.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(67.5000, 209.0000, -210.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-05a.x67.5_z-210.across_x",
   "measured": 11.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 3.0,
   "at": "[(73.0, 212.0, -210.0), (62.0, 212.0, -210.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "J-05.x67.5_z-210.elec",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(73.0000, 212.0000, -210.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.x67.5_z-210.wet",
   "measured": 3.5,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.5,
   "at": "(62.0000, 212.0000, -210.0000) mm",
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
   "gate": "REQ-04.w1_y150_z-200.collar_od",
   "measured": 18.0,
   "unit": "mm",
   "required": "in [17.9, 18.1]",
   "margin": 0.1,
   "at": "(62.0000, 150.0000, -209.0000) mm",
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
   "gate": "REQ-04.w2_y150_z-130.collar_od",
   "measured": 18.0,
   "unit": "mm",
   "required": "in [17.9, 18.1]",
   "margin": 0.1,
   "at": "(62.0000, 150.0000, -139.0000) mm",
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
   "gate": "REQ-04.w3_y150_z-60.collar_od",
   "measured": 18.0,
   "unit": "mm",
   "required": "in [17.9, 18.1]",
   "margin": 0.1,
   "at": "(62.0000, 150.0000, -69.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-40.diameter",
   "measured": 14.0,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": 0.1,
   "at": "(65.0000, 60.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-40.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(65.0000, 60.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-40.apex_above_centre",
   "measured": null,
   "unit": "mm",
   "required": "in [13.9, 14.1]",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4_y60_z-40.collar_od",
   "measured": 18.0,
   "unit": "mm",
   "required": "in [17.9, 18.1]",
   "margin": 0.1,
   "at": "(62.0000, 60.0000, -49.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.w4.front_end_closed",
   "measured": 2,
   "unit": "count",
   "required": "== 1",
   "margin": -1.0,
   "at": null,
   "status": "FAIL",
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
   "at": "(70.0000, 0.0000, -30.0000) mm",
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
   "gate": "U-03.coax.z-45",
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
   "gate": "U-03.coax.z-105",
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
   "gate": "U-03.coax.z-165",
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
   "gate": "U-03.coax.z-225",
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
   "measured": 20.38263133809043,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 17.382631338,
   "at": "(62.0000, 207.0000, -30.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02"
   ]
  },
  {
   "gate": "REQ-05.g01.clearance",
   "measured": 20.38263133809043,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 17.382631338,
   "at": "(62.0000, 207.0000, -30.0000) mm",
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
   "measured": 4.663888830691576e-07,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -4.66e-07,
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
   "measured": 4.663888830691576e-07,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -4.66e-07,
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
   "measured": 1.75,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 0.95,
   "at": "(70.0000, 12.0000, -165.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 1.75,
   "unit": "mm",
   "required": ">= 1.75",
   "margin": 0.0,
   "at": "(70.0000, 12.0000, -165.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-06a",
   "measured": 1.75,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 0.75,
   "at": "(70.0000, 12.0000, -165.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06(Soft)",
   "measured": 0.2651650429449436,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": -1.734834957,
   "at": "(66.7000, 55.8125, -30.1875) mm",
   "status": "FAIL",
   "assumes": []
  },
  {
   "gate": "D-03a",
   "measured": 0.0,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": -45.0,
   "at": "(67.0000, 12.0000, -202.0000) mm",
   "status": "FAIL",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "D-03b.rib_underside_span_y",
   "measured": 195.0,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": -190.0,
   "at": null,
   "status": "FAIL",
   "assumes": []
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
   "measured": 0.004968065921546825,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.005031934,
   "at": "(67.0000, 156.6234, -202.2497) mm",
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
 "sweep": [],
 "least_sure": [
  "the window gable read literally (apex 7.0 above the circle's top, 14.0 above the centre: straight sides then a 45-degree roof) rather than a tangent teardrop (apex 2.9 above the top); window 4 fails either way",
  "the D-03a named exception carries no Usta signature yet (GATES section X); the crowns are reported apart and D-03a fails outside them regardless",
  "D-01b sits at margin 0.00 (1.75 at the counterbore's electric side, x 68.25 ... 70); U-06 wide 0.27 at window 4's roof meeting the front end"
 ],
 "stopped": true
}
```
