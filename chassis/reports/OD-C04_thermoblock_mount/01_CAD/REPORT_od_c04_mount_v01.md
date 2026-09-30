# REPORT — od_c04_mount v01 (20260930-od-c04-thermoblock-mount)

Designer: Claude Code designer subagent, claude-opus-5-5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` (package WP-02, with the spec 1.1 amendments of brief WP-03) · 2026-09-30 UTC · package WP-03 (J3), build attempt 1 of 2, fix cycles used 1 of 3

Concept C1: rear plate on a foot, two Ø12.0 × 1.90 screw standoffs with metal spacers. Every number below is measured by `01_CAD/check_od_c04_mount.py` from the re-imported STEP files; none is echoed from the parameters. These are self-checks: no HARD gate is cleared until the reviewer measures it.

Input hashes checked before the build: `00_Spec/inputs/OD-H11_thermoblock.step` e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff, `params.json` 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c5203, `ports.json` 77fbb8b2a53e929216ddea4752a7b18e67f6f57ba1ba3864ec24e179cf224fd5, `README.md` 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0: all match the brief.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c04_mount.py` | c896c7d5e9de2d76862a6869385a41badc70806be54574bdb6702897ca6d8fe5 | parametric build (mount, spacers, check-assembly placement by joints) |
| `01_CAD/check_od_c04_mount.py` | 1cb150e9a0407b9e9ccce9ae191734b5c0300eac45ac033b9631608619176fa9 | checks, written before the build (D3); fix cycle 1 corrected two selectors (§8 item 13) |
| `01_CAD/sweep_od_c04_mount.py` | ac8e57bf1b69ca74c25cc1597991444c60ead80cf3c98fcfcb2d697997f79f27 | robustness sweep driver (D7) |
| `01_CAD/sections_od_c04_mount.py` | 274dae75a9f4b0da61b1aa0165b817b40efd9eec9d430647760ebf7529294d78 | section writer (D6) |
| `02_STEP_STL/od_c04_mount_C1_v01.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 | AP242 via tools.core.write_step, label od_c04_mount; re-imported for every measurement |
| `02_STEP_STL/od_c04_assembly_C1_v01.step` | f301128de7df7c8b6190ea54cefaddbaecbfd090377cf96be15fca0818175e2a | AP242 check assembly: od_c04_mount, OD-H11_thermoblock, spacer_S1_assumed_A05, spacer_S2_assumed_A05 |
| `02_STEP_STL/od_c04_mount_C1_v01.stl` | c579d4159966a522cb84282e97aefcbaec22cbb9ece844241cd0ba8e9e1b13f7 | binary STL, cached triangulation cleared; tolerance 0.01 mm / angular 0.23097 rad, 8516 triangles, sagitta 0.00627 mm |
| `03_Sections/od_c04_mount_v01_left_xS1.png` | 48457a0eb641e7f3e0655a0fad8401d8ac35fc2db8989fd3d7cd6905b8add91a | section x = -19.62 mm, cut area 725.6 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_left_xS2.png` | 7ed90bedac941c6f521bf04a6166cddaf0daf4e326397db4a315bd3644dbbf9d | section x = 25.01 mm, cut area 725.6 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_left_xGusset.png` | 646d299e0969133bb4aedeb8aa2791f0258c0245ccfdfd075096fa1ec0ace1a6 | section x = 46.00 mm, cut area 929.5 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_left_xFrameHoles.png` | 56488e256c571e6ea6a00b7bb895c073647caa6fe394b5af3baaed8d046efc38 | section x = 40.00 mm, cut area 695.2 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_front_yFoot.png` | a2458bcae6da5aca42ee212809d589798a8ee7230eeb8fe45db48605af1a8c54 | section y = -68.00 mm, cut area 4960.0 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_top_zStandoffs.png` | 0d4121a3c428eae55f529b81862af305f15fb1b63ae315efd7e3cad4cc496f24 | section z = -11.00 mm, cut area 753.1 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_left_asm_xS1.png` | 22616d2b8774b890a7421147c1d471588470ed97e4e20f3a64107a3af5afbf7f | section x = -19.62 mm, cut area 3404.8 mm², nothing_clipped 0 |
| `03_Sections/od_c04_mount_v01_left_asm_xS2.png` | 73ae433c317ebd33629ef99e7a64a977f774e26c6ccacfe9533fcf7900e2d7a1 | section x = 25.01 mm, cut area 1953.9 mm², nothing_clipped 0 |
| `01_CAD/check_v01/check_results_v01.json` | 7857c10cbfa5bc4c4a544e6a6f8789a4d854248d0c3f00fc75777d3d4cb48259 | every gate row and fact from the check run on the delivered files |
| `01_CAD/check_v01/sections_v01.json` | bec9bf1a40472d8ce4672fb4832dbe0e27cd04688927547240e1cf109bfb6089 | section log |
| `01_CAD/check_v01/remesh_check.stl` | 0cc3d677816f3d8f2d18cb4ea77f27992382c61e2470e4f93f3f370dcf0456db | the check's own re-mesh of the re-imported STEP (U-07 corroboration, not a deliverable) |
| `01_CAD/build_record_v01.json` | 8725dfedd9b26a7d25cc66de980b52e7e00577994e4cad98eb2ef11629a3121c | parameters, fillet radius achieved, measured seats, joint placements |
| `01_CAD/sweep_v01/sweep_summary_v01.json` | 511c9f73792aca0e9654b6855d437bbf1aef4206931b217aa056da3335196a6a | sweep summary; per-variant exports and check_results.json in 01_CAD/sweep_v01/<variant>/ |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 (OCCT 7.9.3) · repo commit 70826895ab7666f9e5aee3f77ce88f099995f3c1 · tools venv `${OGUZ_WORK}/venv` via `tools/run.py`

## 3. Gate self-check

Bands from GATES.md §0: 0.005 mm, 0.001°, 0.001 mm³, 0 for counts. Margin is signed, positive inside the limit. Sub-rows are named `<gate>.<item>`. Summary by §5 row:

| §5 row | Self-check | Key reading |
|---|---|---|
| U-01 | PASS | 1 solid, brep_valid 1, naked edges 0 |
| U-02 | PASS | 100.000 × 110.000 × 50.000; position x −50.000 … 50.000, y −70.000 … 40.000, z −17.000 … 33.000 |
| U-03 (a) clearance rows | PASS (assumed: A-01, A-03, A-05) | mount/OD-H11 10.100 mm; each spacer to mount and to OD-H11 0.000 mm; spacer/mount interference 0.000 mm³ |
| U-03 (a) boolean rows | INCONCLUSIVE (by the row, A-14) | common volume with OD-H11 refused: OD-H11 brep_valid 0 (BOPAlgo_InvalidCurveOnSurface) |
| U-03 (b) | N/A | no motion variable |
| U-04 | PASS | AP242 read back, 1 solid, volume delta 5.8e-11 mm³, faces delta 0, label `od_c04_mount` unchanged, valid after |
| U-05 | PASS | 24 planar, 10 cylindrical (4 convex, 6 concave), 2 toroidal; 6 bores; 2 standoffs 1.900 high; 2 gussets |
| U-06 (soft) | PASS | min_wall wide 4.000 |
| U-07 | PASS | sagitta 0.00627 mm ≤ 0.01; delivered STL 1 body, 0 naked edges, winding consistent |
| U-08 | N/A | no threads |
| D-01a, D-01b, D-06a | PASS | min_wall 4.000 mm (standoff wall, bore Ø4.0 to Ø12.0) |
| D-02 | PASS (assumed: A-09) | 100.0 / 110.0 / 50.0 against 220 / 220 / 250 |
| D-03a | PASS (assumed: A-12) | least downward angle 50.000° (teardrop roofs; nothing below 45°; sampling bound 0.009°) |
| D-03b | PASS (self-check; reviewer from sections) | no downward face under 45°, so no bridge: span 0 |
| D-04a | PASS (assumed: A-04) | frame holes Ø3.400 ≥ 3.25; standoff holes Ø4.000 ≥ 3.75 |
| D-07 | N/A | clearance holes only |
| E-06 | PASS (self-check; reviewer) | root fillet R 1.0 (torus) on both standoffs; standoff 1.90 high, no gusset |
| REQ-01 | PASS (assumed: A-01) | 10.100 mm at (−13.620, 20.180, −10.100) on the S1 tip to (−13.620, 20.180, 0.000) on the base face |
| REQ-02 | PASS (assumed: A-03) | Ø4.000, offset 0.000, through (z −17.000 … −10.100) at both points |
| REQ-03 | PASS (assumed: A-03, A-05) | both tips z −10.100; spacers 10.100 and 37.700, clearance 0.000 at both ends |
| REQ-04 | PASS | front face z −12.000 (flat), back face z −17.000 |
| REQ-05 | PASS (assumed: A-10) | underside y −70.000, foot 4.000 thick |
| REQ-06 | PASS (assumed: A-10) | four Ø3.400 bores along Y, offset 0.000, through |
| REQ-07 | PASS (assumed: A-02, A-06) | common volume with r 45.0 keep-out about (−8.330, −14.130), z 0 … 47.64: 0.000 mm³ (clearance 6.870); about the origin 0.000 mm³ |
| REQ-08 | INCONCLUSIVE | bench gate, until the first heating run (A-08) |
| exactly_one_solid | PASS | 1 |
| feature_census | PASS | as U-05 |
| envelope_within_spec | PASS | size and position as U-02, reported apart |

Every row as measured:

| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | count | == 1 | 0 | — | PASS | — |
| U-01.solid_count | 1 | count | == 1 | 0 | — | PASS | — |
| U-01.brep_valid | 1 | bool | == 1 | 0 | — | PASS | — |
| U-01.naked_edges | 0 | count | == 0 | 0 | — | PASS | — |
| U-02.size_x | 100 | mm | in [99.9, 100.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size.size_x | 100 | mm | in [99.9, 100.1] | 0.1 | — | PASS | — |
| U-02.size_y | 110 | mm | in [109.9, 110.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size.size_y | 110 | mm | in [109.9, 110.1] | 0.1 | — | PASS | — |
| U-02.size_z | 50 | mm | in [49.9, 50.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size.size_z | 50 | mm | in [49.9, 50.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_x | -50 | mm | in [-50.1, -49.9] | 0.1 | — | PASS — position against the datum, reported apart from size (U-02) | — |
| envelope_within_spec.position.max_x | 50 | mm | in [49.9, 50.1] | 0.1 | — | PASS — position against the datum, reported apart from size (U-02) | — |
| envelope_within_spec.position.min_y | -70 | mm | in [-70.1, -69.9] | 0.1 | — | PASS — position against the datum, reported apart from size (U-02) | — |
| envelope_within_spec.position.max_y | 40 | mm | in [39.9, 40.1] | 0.1 | — | PASS — position against the datum, reported apart from size (U-02) | — |
| envelope_within_spec.position.min_z | -17 | mm | in [-17.1, -16.9] | 0.1 | — | PASS — position against the datum, reported apart from size (U-02) | — |
| envelope_within_spec.position.max_z | 33 | mm | in [32.9, 33.1] | 0.1 | — | PASS — position against the datum, reported apart from size (U-02) | — |
| D-02.size_x | 100 | mm | <= 220.0 | 120 | — | PASS (assumed: A-09) | A-09 |
| D-02.size_y | 110 | mm | <= 220.0 | 110 | — | PASS (assumed: A-09) | A-09 |
| D-02.size_z | 50 | mm | <= 250.0 | 200 | — | PASS (assumed: A-09) | A-09 |
| U-04.schema | 1 | bool | == 1 | 0 | — | PASS | — |
| U-04.solids | 1 | count | == 1 | 0 | — | PASS | — |
| U-04.volume_delta | 5.82e-11 | mm3 | <= 0 | -5.82e-11 | — | PASS | — |
| U-04.faces_delta | 0 | count | == 0 | 0 | — | PASS | — |
| U-04.labels | 1 | bool | == 1 | 0 | — | PASS | — |
| U-04.valid_after | 1 | bool | == 1 | 0 | — | PASS | — |
| U-05.plane_faces | 24 | count | == 24 | 0 | — | PASS | — |
| feature_census.plane_faces | 24 | count | == 24 | 0 | — | PASS | — |
| U-05.cylinder_faces | 10 | count | == 10 | 0 | — | PASS | — |
| feature_census.cylinder_faces | 10 | count | == 10 | 0 | — | PASS | — |
| U-05.cone_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census.cone_faces | 0 | count | == 0 | 0 | — | PASS | — |
| U-05.sphere_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census.sphere_faces | 0 | count | == 0 | 0 | — | PASS | — |
| U-05.torus_faces | 2 | count | == 2 | 0 | — | PASS | — |
| feature_census.torus_faces | 2 | count | == 2 | 0 | — | PASS | — |
| U-05.bspline_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census.bspline_faces | 0 | count | == 0 | 0 | — | PASS | — |
| U-05.other_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census.other_faces | 0 | count | == 0 | 0 | — | PASS | — |
| U-05.concave_cylinders | 6 | count | == 6 | 0 | — | PASS | — |
| feature_census.concave_cylinders | 6 | count | == 6 | 0 | — | PASS | — |
| U-05.convex_cylinders | 4 | count | == 4 | 0 | — | PASS | — |
| feature_census.convex_cylinders | 4 | count | == 4 | 0 | — | PASS | — |
| U-05.bores | 6 | count | == 6 | 0 | — | PASS | — |
| feature_census.bores | 6 | count | == 6 | 0 | — | PASS | — |
| U-05.standoffs | 2 | count | == 2 | 0 | — | PASS | — |
| U-05.gussets | 2 | count | == 2 | 0 | [(-46.0, -56.0, -2.0), (46.0, -56.0, -2.0)] | PASS | — |
| REQ-02.S1.diameter | 4 | mm | in [3.9, 4.1] | 0.1 | (-19.6200, 20.1800, -17.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-02.S1.offset | 0 | mm | <= 0.1 | 0.1 | (-19.6200, 20.1800, -17.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-02.S1.through | 1 | bool | == 1 | 0 | (-19.6200, 20.1800, -17.0000) mm | PASS (assumed: A-03) | A-03 |
| D-04a.S1 | 4 | mm | >= 3.75 | 0.25 | (-19.6200, 20.1800, -17.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.S2.diameter | 4 | mm | in [3.9, 4.1] | 0.1 | (25.0100, 9.0800, -17.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-02.S2.offset | 0 | mm | <= 0.1 | 0.1 | (25.0100, 9.0800, -17.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-02.S2.through | 1 | bool | == 1 | 0 | (25.0100, 9.0800, -17.0000) mm | PASS (assumed: A-03) | A-03 |
| D-04a.S2 | 4 | mm | >= 3.75 | 0.25 | (25.0100, 9.0800, -17.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06.x-40_z-8.diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x-40_z-8.offset | 0 | mm | <= 0.1 | 0.1 | (-40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x-40_z-8.through | 1 | bool | == 1 | 0 | (-40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-10) | A-10 |
| D-04a.x-40_z-8 | 3.4 | mm | >= 3.25 | 0.15 | (-40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06.x+40_z-8.diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x+40_z-8.offset | 0 | mm | <= 0.1 | 0.1 | (40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x+40_z-8.through | 1 | bool | == 1 | 0 | (40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-10) | A-10 |
| D-04a.x+40_z-8 | 3.4 | mm | >= 3.25 | 0.15 | (40.0000, -70.0000, -8.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06.x-40_z+26.diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x-40_z+26.offset | 0 | mm | <= 0.1 | 0.1 | (-40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x-40_z+26.through | 1 | bool | == 1 | 0 | (-40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-10) | A-10 |
| D-04a.x-40_z+26 | 3.4 | mm | >= 3.25 | 0.15 | (-40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06.x+40_z+26.diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x+40_z+26.offset | 0 | mm | <= 0.1 | 0.1 | (40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-10) | A-10 |
| REQ-06.x+40_z+26.through | 1 | bool | == 1 | 0 | (40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-10) | A-10 |
| D-04a.x+40_z+26 | 3.4 | mm | >= 3.25 | 0.15 | (40.0000, -70.0000, 26.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-04.front_z | -12 | mm | in [-12.1, -11.9] | 0.1 | — | PASS — largest horizontal face above the bed face | — |
| REQ-04.front_flat | 0 | mm | <= 0.0 | 0 | — | PASS | — |
| REQ-04.back_z | -17 | mm | in [-17.1, -16.9] | 0.1 | — | PASS — lowest horizontal face (the bed face) | — |
| REQ-05.underside_y | -70 | mm | in [-70.1, -69.9] | 0.1 | — | PASS (assumed: A-10) | A-10 |
| REQ-05.thickness | 4 | mm | in [3.9, 4.1] | 0.1 | (0.0000, -66.0000, 10.9770) mm | PASS (assumed: A-10) | A-10 |
| REQ-03.S1.tip_z | -10.1 | mm | in [-10.2, -10.0] | 0.1 | — | PASS (assumed: A-03, A-05) | A-03, A-05 |
| REQ-03.S2.tip_z | -10.1 | mm | in [-10.2, -10.0] | 0.1 | — | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-05.S1.standoff_height | 1.9 | mm | == 1.9 | -4.44e-16 | — | PASS | — |
| U-05.S2.standoff_height | 1.9 | mm | == 1.9 | -4.44e-16 | — | PASS | — |
| REQ-01 | 10.1 | mm | >= 10.0 | 0.1 | (-13.6200, 20.1800, -10.1000) mm | PASS (assumed: A-01) | A-01 |
| U-03a.mount/OD-H11.clearance | 10.1 | mm | >= 10.0 | 0.1 | (-13.6200, 20.1800, -10.1000) mm | PASS (assumed: A-01, A-03, A-05) | A-01, A-03, A-05 |
| U-03a.mount/OD-H11.interference | — | mm3 | <= 0 | — | — | INCONCLUSIVE — INCONCLUSIVE by the row: OD-H11 is unsound for booleans (A-14); solid 1 of b: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface | A-01, A-03, A-05 |
| U-03a.S1/mount.clearance | 0 | mm | == 0.0 | 0 | (-17.6200, 20.1800, -10.1000) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-03a.S1/mount.interference | 0 | mm3 | <= 0 | 0 | — | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-03a.S1/OD-H11.clearance | 0 | mm | == 0.0 | 0 | (-20.5399, 18.4041, 0.0000) mm | PASS (assumed: A-01, A-03, A-05) | A-01, A-03, A-05 |
| U-03a.S1/OD-H11.interference | — | mm3 | <= 0 | — | — | INCONCLUSIVE — INCONCLUSIVE by the row: OD-H11 is unsound for booleans (A-14); solid 1 of b: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface | A-01, A-03, A-05 |
| REQ-03.S1.spacer/mount.clearance | 0 | mm | == 0.0 | 0 | (-17.6200, 20.1800, -10.1000) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| REQ-03.S1.spacer/OD-H11.clearance | 0 | mm | == 0.0 | 0 | (-20.5399, 18.4041, 0.0000) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| REQ-03.S1.spacer_length | 10.1 | mm | == 10.1 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03a.S2/mount.clearance | 0 | mm | == 0.0 | 0 | (27.0100, 9.0800, -10.1000) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-03a.S2/mount.interference | 0 | mm3 | <= 0 | 0 | — | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-03a.S2/OD-H11.clearance | 0 | mm | == 0.0 | 0 | (28.5100, 9.0800, 27.6000) mm | PASS (assumed: A-01, A-03, A-05) | A-01, A-03, A-05 |
| U-03a.S2/OD-H11.interference | — | mm3 | <= 0 | — | — | INCONCLUSIVE — INCONCLUSIVE by the row: OD-H11 is unsound for booleans (A-14); solid 1 of b: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface | A-01, A-03, A-05 |
| REQ-03.S2.spacer/mount.clearance | 0 | mm | == 0.0 | 0 | (27.0100, 9.0800, -10.1000) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| REQ-03.S2.spacer/OD-H11.clearance | 0 | mm | == 0.0 | 0 | (28.5100, 9.0800, 27.6000) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| REQ-03.S2.spacer_length | 37.7 | mm | == 37.7 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03b | — |  | no motion variable | — | — | N/A — U-03 (b): the part has no motion variable (N/A by the row) | — |
| REQ-07 | 0 | mm3 | <= 0 | 0 | — | PASS (assumed: A-02, A-06) — common volume with the keep-out cylinder r 45.0 about (-8.330, -14.130), z 0 .. 47.64 | A-02, A-06 |
| REQ-07.clearance_to_keepout | 6.87 | mm | >= 0.0 | 6.87 | (-8.3300, -66.0000, 33.0000) mm | PASS (assumed: A-02, A-06) — distance from the mount to the keep-out cylinder (corroboration) | A-02, A-06 |
| D-01a | 4 | mm | >= 0.8 | 3.2 | (-24.4971, 23.6749, -10.8875) mm | PASS | — |
| D-01b | 4 | mm | >= 2.0 | 2 | (-24.4971, 23.6749, -10.8875) mm | PASS | — |
| D-06a | 4 | mm | >= 1.0 | 3 | (-24.4971, 23.6749, -10.8875) mm | PASS | — |
| U-06 | 4 | mm | >= 2.0 | 2 | (-24.4971, 23.6749, -10.8875) mm | PASS — SOFT | — |
| D-03a | 50 | deg | >= 45.0 | 5 | (-41.3023, -66.0000, -6.9073) mm | PASS (assumed: A-12) | A-12 |
| D-03b | 0 | mm | <= 5.0 | 5 | — | PASS — reviewer, from sections | — |
| E-06 | 2 | count | == 2 | 0 | — | PASS — reviewer; torus face at each standoff root | — |
| U-07.stl_max_sagitta | 0.0063 | mm | <= 0.01 | 0.0037 | (30.0909, 4.4285, -11.9875) mm | PASS | — |
| U-07.delivered_bodies | 1 | count | == 1 | 0 | — | PASS | — |
| U-07.delivered_naked_edges | 0 | count | == 0 | 0 | — | PASS | — |
| U-07.delivered_winding | 1 | bool | == 1 | 0 | — | PASS | — |
| U-08 | — |  | threads cosmetic | — | — | N/A — no threaded feature on this target (N/A by the row) | — |
| D-07 | — |  | fit-critical bores | — | — | N/A — clearance holes only (N/A by the row) | — |
| REQ-08 | — |  | holds through a heating cycle | — | — | INCONCLUSIVE — bench gate: INCONCLUSIVE until the first run | A-08 |

## 4. Robustness sweep (D7)

Each fit-critical parameter of plan §4 at low and high, one at a time, plus nominal: 17 builds in `01_CAD/sweep_v01/`, each exported through `write_step` / `write_stl` and checked by the same `run()` of the check script. No motion variable, so nothing is swept together. Every run built one valid solid and passed every inequality gate of §5; REQ-01's worst reading over the sweep is 10.000 mm (tip_z −10.00, margin 0.000, inside the band). A parameter moved to its tolerance limit reads a margin of 0.000 on its own row by construction.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin | Other readings |
|---|---|---|---|---|---|
| plate_front_z | −12.10 · −12.00 · −11.90 | yes (17 of 17 runs, each one valid solid) | REQ-04.front_z | 0.000 (−12.10 / −11.90, at the band edge) | U-05 standoff height reads 2.00 / 1.80 (the 1.90 follows the tip and the plate face); REQ-01 10.100 |
| plate_back_z | −17.10 · −17.00 · −16.90 | yes (17 of 17 runs, each one valid solid) | U-02.size_z | 0.000 (50.10 / 49.90) | REQ-04.back_z 0.000; REQ-01 10.100 |
| foot_y (underside) | −70.10 · −70.00 · −69.90 | yes (17 of 17 runs, each one valid solid) | U-02.size_y | 0.000 (110.10 / 109.90) | REQ-05.underside_y 0.000; REQ-01 10.100 |
| frame_hole_d | 3.30 · 3.40 · 3.50 | yes (17 of 17 runs, each one valid solid) | REQ-06 diameter | 0.000 (3.30 / 3.50) | D-04a 0.050 at 3.30; D-03a 50.000° |
| frame_hole_xz (diagonal 0.10) | −0.0707/−0.0707 · 0 · +0.0707/+0.0707 | yes (17 of 17 runs, each one valid solid) | REQ-06 offset | −0.0000005 (0.1000005, inside the band) | — |
| standoff_xy (diagonal 0.10) | −0.0707/−0.0707 · 0 · +0.0707/+0.0707 | yes (17 of 17 runs, each one valid solid) | REQ-02 offset | −0.0000005 (0.1000005, inside the band) | REQ-01 10.100; spacer contacts 0.000 |
| standoff_bore_d | 3.90 · 4.00 · 4.10 | yes (17 of 17 runs, each one valid solid) | REQ-02 diameter | 0.000 (3.90 / 4.10) | D-04a 0.150 at 3.90; D-01b 3.950 at 4.10 |
| tip_z | −10.20 · −10.10 · −10.00 | yes (17 of 17 runs, each one valid solid) | REQ-03 tip_z / REQ-01 | REQ-03 0.000; REQ-01 0.000 at −10.00 (10.000 mm, PASS in the band), 0.200 at −10.20 | with the spec-length spacers fixed: at −10.20 spacer|mount clearance 0.100 (FAIL of the = 0 rows), at −10.00 spacer|mount interference 2.592 mm³ each (FAIL); U-05 height 1.80 / 2.00 |

Rows that pass only at nominal: the exact-contact rows (U-03 (a) spacer|mount clearance = 0 and interference ≤ 0, REQ-03 spacer|mount clearance = 0) fail at tip_z ±0.10 with fixed spacer lengths, and the U-05 standoff height 1.90 reads 1.80 / 2.00 when the tip or the plate face moves by 0.10. Both are the tolerance stack of REQ-03 and REQ-04 against fixed spacers, not a defect of the nominal geometry; see §9 item 3.

## 5. Build facts

- Envelope 100.000 × 110.000 × 50.000 mm (x −50.000 … 50.000, y −70.000 … 40.000, z −17.000 … 33.000); volume 74 659.46 mm³; mass 79.89 g at 1070 kg/m³ (ASA, A-08); centre of mass (0.010, −28.545, −8.309) (`mass_properties` on the re-imported STEP).
- Fillets: standoff root fillets requested 1.0 → achieved 1.0 on both standoffs (first rung of the ladder 1.0 / 0.8 / 0.5; no rung rejected); plate corner R 5.0 at the two y +40 corners (sketch fillet, measured convex cylinders R 5.0).
- Placements (check assembly `02_STEP_STL/od_c04_assembly_C1_v01.step`, parts `od_c04_mount`, `OD-H11_thermoblock`, `spacer_S1_assumed_A05`, `spacer_S2_assumed_A05`):
  - OD-H11: RigidJoint `mount_frame` (mount, origin) → `step_origin` (OD-H11, origin), axis +Z: identity pose, as the brief states.
  - spacer_S1: RigidJoint `seat_S1` on OD-H11 → `seat_end` of the spacer, axis +Z. Axis from `locate_bore` on OD-H11 (Ø3.60 bore at (−19.620, 20.180), offset 0.000 from the spec point, blind, z 3.0 … 8.0); seat height measured by a Ø7.0 / Ø4.0 probe annulus 1.0 below the base face and `clearance` to OD-H11: seat z 0.000 (nearest casting point (−20.540, 18.404, 0.000), on the base face). Spacer spans z −10.100 … 0.000.
  - spacer_S2: RigidJoint `seat_S2` on OD-H11 → `seat_end`, axis +Z. Axis from `locate_bore` (Ø3.50 bore at (25.010, 9.080), offset 0.000, open end at z 27.600 on the mid-lug underside); probe seat z 27.600, equal to the bore's open end. Spacer spans z −10.100 … 27.600.
- STL: `write_stl` at tolerance 0.01 mm, angular 0.23097 rad (= 4·acos(1 − 0.01/6.0)), cached triangulation cleared, 8 516 triangles, sagitta 0.00627 mm at export; the check re-meshed the re-imported STEP at the same settings: 8 516 triangles, sagitta 0.00627 mm; `mesh_census` of the delivered STL: 1 body, 0 naked edges, consistent winding, volume 74 659.57 mm³.
- REQ-07 about the origin (reported beside the gated axis reading, spec 1.1 / brief): common volume with the r 45.0 cylinder about (0, 0), z 0 … 47.64: 0.000 mm³; clearance to it 10.100 mm (at the S2 tip, below the cylinder's end). About the measured axis: 0.000 mm³, clearance 6.870 mm (the foot's inside face y −66.0 against r 45.0 about y −14.130). `radial_profile(side="inner", r_max=45)` about the measured axis, 36 angles × 48 levels over z 0 … 47.64: 1 728 of 1 728 rays read "no material between 0 and 45 mm", which the function returns as INCONCLUSIVE by its contract; that is the expected reading the row names, recorded, not gated.
- OD-H11 soundness, re-measured on the assembly STEP: solid_count 1, brep_valid 0, naked_edges 0 (A-14); every boolean against it returned INCONCLUSIVE ("brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface").

## 6. Plausibility (§P, D6)

Sections: `03_Sections/od_c04_mount_v01_left_xS1.png`, `_left_xS2.png`, `_left_xGusset.png`, `_left_xFrameHoles.png`, `_front_yFoot.png`, `_top_zStandoffs.png`, and the assembly sections `_left_asm_xS1.png`, `_left_asm_xS2.png`; `nothing_clipped` 0 on all eight.

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | Yes: the foot underside y −70.0 sits on OD-C01 with −Y down (A-07), the plate stands vertical behind the thermoblock, and the thermoblock hangs on two screws through the standoffs and spacers with its axis horizontal; the load path is two screws in bending over a 12.0 plate-to-base gap and a 37.7 spacer column at S2 (strength not calculated, A-11). |
| P2 | Function chains | Yes: the pipes and terminals (+Y) face up and away from the foot, the outlet face (+Z) toward the group head is open, and the mount sits only behind the base face and under the body with ≥ 10.1 mm of air; no water or cable path crosses the mount. |
| P3 | Motion | Not applicable: no moving parts (U-03 b). |
| P4 | Human factors | Yes, with an order: the two thermoblock screws go in from the plate's back (−Z) through the Ø4.0 bores; the four foot screws go down through the foot into OD-C01 and should be fitted before the thermoblock, because the thermoblock stands over the z 26 pair (plan R6). |
| P5 | Next to a real product | Nothing absurd: an L bracket with a rear plate and two short bosses is a normal heater mount; the one unusual element is the 37.7 mm metal spacer column at S2, which the sections show standing clear of the body wall. |
| P6 | Floating, embedded, mirrored, upside-down | None: one solid; OD-H11 10.100 mm away at the nearest point; spacers touch mount and casting with 0 clearance and 0.000 mm³ interference with the mount; bore positions offset 0.000 from the spec points (not mirrored); teardrop apexes point +Z, the build direction; the foot is at −Y (down). |

## 7. Library and tools used

- Cards: UNO10 U5 tank heat-set (tags fdm, boss), as read at D1 (plan §2); no card matches a heat-shielded mount with spacers (finding, unchanged).
- `tools.core`: `read_step`, `write_step` (AP242, deliverable and assembly), `compare_step` (U-04), `validity` (U-01, spacers, OD-H11), `write_stl` and its sagitta (U-07), `common_volume` (U-03 interference, REQ-07), `fillet_ladder` (root fillets).
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `min_wall`, `min_wall_wide`, `overhang_census`, `radial_profile`, `mesh_census`, `mass_properties`.
- `tools.drawing`: `write_sections` with its `nothing_clipped` reading.
- New code (job code, in `01_CAD/` only): the build, check, sweep and section scripts. No `tools/` function was missing.

## 8. Deviations from the plan

Spec 1.1 amendments (brief WP-03), built as stated:

1. Standoff tips: both at z −10.10 (plan: −10.00 with Q1/Q3 open); standoffs Ø12.0, 1.90 proud of the plate front face z −12.0, no gussets on them (spec 1.1 §4, Q1 option a, Q3).
2. Spacers: SP1 Ø7.0 × 10.10 (z −10.10 … 0.00, on the base face) and SP2 Ø7.0 × 37.70 (z −10.10 … 27.60, on the mid-lug underside), Ø4.0 bores, named `spacer_S1_assumed_A05` and `spacer_S2_assumed_A05` (plan: `spacer_S1`, `spacer_S2`, length 10.0 / 37.6).
3. REQ-03: tip faces at z −10.10 ± 0.10 and spacer clearance 0 at both ends (plan: spacer 10.0 ± 0.10 to each seat).
4. REQ-07 and every r, θ about the measured axis (−8.330, −14.130), with the origin reading beside it (§5).
5. U-03 booleans against OD-H11 recorded INCONCLUSIVE by the row (A-14); the spacer|mount and spacer|OD-H11 pairs are `clearance = 0` rows.
6. Census re-tallied from the frozen feature list: 24 planar (plate and foot 8, gussets 3 each, standoff tips 2, teardrop roofs 2 each), 10 cylindrical (convex: 2 plate corners, 2 standoff sides; concave: 2 standoff bores, 4 teardrop arcs), 2 toroidal (root fillets), 6 bores.

Other changes against the plan:

7. File names: the plan named `check_od_c04_mount_v01.py`, `check_assembly_v01.py` and `build_assembly_v01.py`; the brief names `check_od_c04_mount.py` and `build_od_c04_mount.py`, so the assembly placement is `build_assembly()` in the build script and the assembly rows are in the one check script.
8. REQ-07 check: the plan subtracted the standoff and spacer columns from the keep-out cylinder; at tip −10.10 nothing lies in z 0 … 47.64 to except, so the whole cylinder is used. `radial_profile` was also run and recorded (§5).
9. S1 seat: measured by a probe annulus and `clearance` (seat z 0.000), because the S1 bore itself is blind at z 3.0 … 8.0 and its end is not the seat; S2 uses the same probe and agrees with its bore's open end (27.600).
10. Extra rows the plan did not list: U-05 standoff height (1.900, both), U-05 standoff and gusset counts by geometry, REQ-04 front-face flatness, REQ-07 clearance to the keep-out, U-07 census of the delivered STL.
11. Sweep of position parameters: each feature moved 0.10 along the xy (or xz) diagonal (0.0707 per axis), the edge of the spec's offset ≤ 0.10 zone, rather than 0.10 on each axis (which is 0.141 off, outside the tolerance).
12. Section pictures carry a location suffix (`_xS1`, `_yFoot`, …) after `<part>_v01_<plane>` so several planes of one view do not overwrite each other.
13. Fix cycle 1 (checks only, no geometry change): the first check run read U-05 standoffs 0 and E-06 0 because the predicates took `Face.center()` of a cylinder or torus (a point on the surface) as a point on its axis; they now read the surface's own axis. The part, assembly and STL files were not rebuilt; the check was re-run on the same exports (hashes unchanged).

## 9. What I am least sure of

1. REQ-01 at S1 has 0.100 mm of margin at nominal and 0.000 at the tip's high tolerance (10.000 mm): the gap is measured to a scanned casting whose own deviation is p95 0.474 / max 2.71 mm (A-01), so the real air gap at the S1 tip can be below 10.0 by more than the whole margin. Calipers on the base face and the S1 hole (A-01, A-03) retire it.
2. Strength and seating are not calculated (A-11, A-05, plan R3): the 0.45 kg thermoblock hangs 12 mm in front of the plate on two screws, one through a 37.70 mm Ø7.0/Ø4.0 metal column at S2, and the S1 spacer bears on only a crescent (about 120°) of the base face because the rest of its end lies over the U-notch. The geometry passes; whether the joint is stiff enough is a bench question.
3. The contact rows are exact only at nominal: with fixed-length spacers (10.10, 37.70), a standoff tip at its ±0.10 limit leaves a 0.100 mm gap or a 2.592 mm³ overlap per spacer (sweep, tip_z). In a real assembly the screw clamp would move the mount by that amount instead, which moves the S1 gap to the casting by ±0.10 as well; a spacer cut to fit, or a tip tolerance tighter than ±0.10, would close this.

## 10. Stop

Not stopped.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c04-thermoblock-mount",
 "part": "od_c04_mount",
 "tag": "v01",
 "spec_version": "1.1",
 "files": [
  {
   "path": "01_CAD/build_od_c04_mount.py",
   "sha256": "c896c7d5e9de2d76862a6869385a41badc70806be54574bdb6702897ca6d8fe5"
  },
  {
   "path": "01_CAD/check_od_c04_mount.py",
   "sha256": "1cb150e9a0407b9e9ccce9ae191734b5c0300eac45ac033b9631608619176fa9"
  },
  {
   "path": "01_CAD/sweep_od_c04_mount.py",
   "sha256": "ac8e57bf1b69ca74c25cc1597991444c60ead80cf3c98fcfcb2d697997f79f27"
  },
  {
   "path": "01_CAD/sections_od_c04_mount.py",
   "sha256": "274dae75a9f4b0da61b1aa0165b817b40efd9eec9d430647760ebf7529294d78"
  },
  {
   "path": "02_STEP_STL/od_c04_mount_C1_v01.step",
   "sha256": "31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221"
  },
  {
   "path": "02_STEP_STL/od_c04_assembly_C1_v01.step",
   "sha256": "f301128de7df7c8b6190ea54cefaddbaecbfd090377cf96be15fca0818175e2a"
  },
  {
   "path": "02_STEP_STL/od_c04_mount_C1_v01.stl",
   "sha256": "c579d4159966a522cb84282e97aefcbaec22cbb9ece844241cd0ba8e9e1b13f7"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_left_xS1.png",
   "sha256": "48457a0eb641e7f3e0655a0fad8401d8ac35fc2db8989fd3d7cd6905b8add91a"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_left_xS2.png",
   "sha256": "7ed90bedac941c6f521bf04a6166cddaf0daf4e326397db4a315bd3644dbbf9d"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_left_xGusset.png",
   "sha256": "646d299e0969133bb4aedeb8aa2791f0258c0245ccfdfd075096fa1ec0ace1a6"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_left_xFrameHoles.png",
   "sha256": "56488e256c571e6ea6a00b7bb895c073647caa6fe394b5af3baaed8d046efc38"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_front_yFoot.png",
   "sha256": "a2458bcae6da5aca42ee212809d589798a8ee7230eeb8fe45db48605af1a8c54"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_top_zStandoffs.png",
   "sha256": "0d4121a3c428eae55f529b81862af305f15fb1b63ae315efd7e3cad4cc496f24"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_left_asm_xS1.png",
   "sha256": "22616d2b8774b890a7421147c1d471588470ed97e4e20f3a64107a3af5afbf7f"
  },
  {
   "path": "03_Sections/od_c04_mount_v01_left_asm_xS2.png",
   "sha256": "73ae433c317ebd33629ef99e7a64a977f774e26c6ccacfe9533fcf7900e2d7a1"
  },
  {
   "path": "01_CAD/check_v01/check_results_v01.json",
   "sha256": "7857c10cbfa5bc4c4a544e6a6f8789a4d854248d0c3f00fc75777d3d4cb48259"
  },
  {
   "path": "01_CAD/check_v01/sections_v01.json",
   "sha256": "bec9bf1a40472d8ce4672fb4832dbe0e27cd04688927547240e1cf109bfb6089"
  },
  {
   "path": "01_CAD/check_v01/remesh_check.stl",
   "sha256": "0cc3d677816f3d8f2d18cb4ea77f27992382c61e2470e4f93f3f370dcf0456db"
  },
  {
   "path": "01_CAD/build_record_v01.json",
   "sha256": "8725dfedd9b26a7d25cc66de980b52e7e00577994e4cad98eb2ef11629a3121c"
  },
  {
   "path": "01_CAD/sweep_v01/sweep_summary_v01.json",
   "sha256": "511c9f73792aca0e9654b6855d437bbf1aef4206931b217aa056da3335196a6a"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "7.9.3.1 (OCCT 7.9.3)",
  "repo_commit": "70826895ab7666f9e5aee3f77ce88f099995f3c1"
 },
 "gates": [
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
   "gate": "U-02.size_x",
   "measured": 100.00000000000003,
   "unit": "mm",
   "required": "in [99.9, 100.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size.size_x",
   "measured": 100.00000000000003,
   "unit": "mm",
   "required": "in [99.9, 100.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_y",
   "measured": 110.0,
   "unit": "mm",
   "required": "in [109.9, 110.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size.size_y",
   "measured": 110.0,
   "unit": "mm",
   "required": "in [109.9, 110.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_z",
   "measured": 50.0,
   "unit": "mm",
   "required": "in [49.9, 50.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size.size_z",
   "measured": 50.0,
   "unit": "mm",
   "required": "in [49.9, 50.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_x",
   "measured": -50.0,
   "unit": "mm",
   "required": "in [-50.1, -49.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_x",
   "measured": 50.00000000000003,
   "unit": "mm",
   "required": "in [49.9, 50.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_y",
   "measured": -70.0,
   "unit": "mm",
   "required": "in [-70.1, -69.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_y",
   "measured": 40.0,
   "unit": "mm",
   "required": "in [39.9, 40.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_z",
   "measured": -17.0,
   "unit": "mm",
   "required": "in [-17.1, -16.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_z",
   "measured": 33.0,
   "unit": "mm",
   "required": "in [32.9, 33.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02.size_x",
   "measured": 100.00000000000003,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 120.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "D-02.size_y",
   "measured": 110.0,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 110.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "D-02.size_z",
   "measured": 50.0,
   "unit": "mm",
   "required": "<= 250.0",
   "margin": 200.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "U-04.schema",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.solids",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.volume_delta",
   "measured": 5.820766091346741e-11,
   "unit": "mm3",
   "required": "<= 0",
   "margin": -5.820766091346741e-11,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.faces_delta",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.labels",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.valid_after",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.plane_faces",
   "measured": 24,
   "unit": "count",
   "required": "== 24",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.plane_faces",
   "measured": 24,
   "unit": "count",
   "required": "== 24",
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
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.torus_faces",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
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
   "gate": "U-05.concave_cylinders",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.concave_cylinders",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.convex_cylinders",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.convex_cylinders",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
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
   "gate": "U-05.standoffs",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.gussets",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": "[(-46.0, -56.0, -2.0), (46.0, -56.0, -2.0)]",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-02.S1.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(-19.6200, 20.1800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.S1.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-19.6200, 20.1800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.S1.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-19.6200, 20.1800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "D-04a.S1",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.75",
   "margin": 0.25,
   "at": "(-19.6200, 20.1800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-02.S2.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(25.0100, 9.0800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.S2.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(25.0100, 9.0800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.S2.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(25.0100, 9.0800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "D-04a.S2",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.75",
   "margin": 0.25,
   "at": "(25.0100, 9.0800, -17.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06.x-40_z-8.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(-40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x-40_z-8.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x-40_z-8.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "D-04a.x-40_z-8",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(-40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06.x+40_z-8.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x+40_z-8.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x+40_z-8.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "D-04a.x+40_z-8",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(40.0000, -70.0000, -8.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06.x-40_z+26.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(-40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x-40_z+26.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x-40_z+26.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "D-04a.x-40_z+26",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(-40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06.x+40_z+26.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x+40_z+26.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-06.x+40_z+26.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "D-04a.x+40_z+26",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(40.0000, -70.0000, 26.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04.front_z",
   "measured": -12.0,
   "unit": "mm",
   "required": "in [-12.1, -11.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-04.front_flat",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-04.back_z",
   "measured": -17.0,
   "unit": "mm",
   "required": "in [-17.1, -16.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05.underside_y",
   "measured": -70.0,
   "unit": "mm",
   "required": "in [-70.1, -69.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-05.thickness",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(0.0000, -66.0000, 10.9770) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-03.S1.tip_z",
   "measured": -10.1,
   "unit": "mm",
   "required": "in [-10.2, -10.0]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S2.tip_z",
   "measured": -10.1,
   "unit": "mm",
   "required": "in [-10.2, -10.0]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-05.S1.standoff_height",
   "measured": 1.9000000000000004,
   "unit": "mm",
   "required": "== 1.9",
   "margin": -4.440892098500626e-16,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.S2.standoff_height",
   "measured": 1.9000000000000004,
   "unit": "mm",
   "required": "== 1.9",
   "margin": -4.440892098500626e-16,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01",
   "measured": 10.1,
   "unit": "mm",
   "required": ">= 10.0",
   "margin": 0.1,
   "at": "(-13.6200, 20.1800, -10.1000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03a.mount|OD-H11.clearance",
   "measured": 10.1,
   "unit": "mm",
   "required": ">= 10.0",
   "margin": 0.1,
   "at": "(-13.6200, 20.1800, -10.1000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.mount|OD-H11.interference",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-01",
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S1|mount.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(-17.6200, 20.1800, -10.1000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S1|mount.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S1|OD-H11.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(-20.5399, 18.4041, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S1|OD-H11.interference",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-01",
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S1.spacer|mount.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(-17.6200, 20.1800, -10.1000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S1.spacer|OD-H11.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(-20.5399, 18.4041, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S1.spacer_length",
   "measured": 10.1,
   "unit": "mm",
   "required": "== 10.1",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S2|mount.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(27.0100, 9.0800, -10.1000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S2|mount.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S2|OD-H11.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(28.5100, 9.0800, 27.6000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "U-03a.S2|OD-H11.interference",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-01",
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S2.spacer|mount.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(27.0100, 9.0800, -10.1000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S2.spacer|OD-H11.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(28.5100, 9.0800, 27.6000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-05"
   ]
  },
  {
   "gate": "REQ-03.S2.spacer_length",
   "measured": 37.7,
   "unit": "mm",
   "required": "== 37.7",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "U-03b",
   "measured": null,
   "unit": "",
   "required": "no motion variable",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "REQ-07",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-06"
   ]
  },
  {
   "gate": "REQ-07.clearance_to_keepout",
   "measured": 6.869999999999997,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": 6.87,
   "at": "(-8.3300, -66.0000, 33.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-06"
   ]
  },
  {
   "gate": "D-01a",
   "measured": 3.999999999999859,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 3.2,
   "at": "(-24.4971, 23.6749, -10.8875) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 3.999999999999859,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 2.0,
   "at": "(-24.4971, 23.6749, -10.8875) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-06a",
   "measured": 3.999999999999859,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 3.0,
   "at": "(-24.4971, 23.6749, -10.8875) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06",
   "measured": 3.999999999999859,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 2.0,
   "at": "(-24.4971, 23.6749, -10.8875) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03a",
   "measured": 49.99999999998059,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": 5.0,
   "at": "(-41.3023, -66.0000, -6.9073) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "D-03b",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": 5.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "E-06",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.stl_max_sagitta",
   "measured": 0.006269949994348233,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.00373005,
   "at": "(30.0909, 4.4285, -11.9875) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.delivered_bodies",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.delivered_naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.delivered_winding",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-08",
   "measured": null,
   "unit": "",
   "required": "threads cosmetic",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "D-07",
   "measured": null,
   "unit": "",
   "required": "fit-critical bores",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "REQ-08",
   "measured": null,
   "unit": "",
   "required": "holds through a heating cycle",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-08"
   ]
  }
 ],
 "sweep": [
  {
   "parameter": "plate_front_z",
   "values": [
    -12.1,
    -12.0,
    -11.9
   ],
   "all_built": true,
   "worst_gate": "REQ-04.front_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "plate_back_z",
   "values": [
    -17.1,
    -17.0,
    -16.9
   ],
   "all_built": true,
   "worst_gate": "U-02.size_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "foot_y_min",
   "values": [
    -70.1,
    -70.0,
    -69.9
   ],
   "all_built": true,
   "worst_gate": "U-02.size_y",
   "worst_margin": 0.0
  },
  {
   "parameter": "frame_hole_d",
   "values": [
    3.3,
    3.4,
    3.5
   ],
   "all_built": true,
   "worst_gate": "REQ-06.diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "frame_hole_xz_diagonal",
   "values": [
    -0.1,
    0.0,
    0.1
   ],
   "all_built": true,
   "worst_gate": "REQ-06.offset",
   "worst_margin": -4.55e-07
  },
  {
   "parameter": "standoff_xy_diagonal",
   "values": [
    -0.1,
    0.0,
    0.1
   ],
   "all_built": true,
   "worst_gate": "REQ-02.offset",
   "worst_margin": -4.55e-07
  },
  {
   "parameter": "standoff_bore_d",
   "values": [
    3.9,
    4.0,
    4.1
   ],
   "all_built": true,
   "worst_gate": "REQ-02.diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "tip_z",
   "values": [
    -10.2,
    -10.1,
    -10.0
   ],
   "all_built": true,
   "worst_gate": "U-03a.S#|mount.interference (fixed-length spacers)",
   "worst_margin": -2.591813939
  }
 ],
 "least_sure": [
  "REQ-01 at S1 has 0.100 mm of margin at nominal and 0.000 at the tip's high tolerance (10.000 mm): the gap is measured to a scanned casting whose own deviation is p95 0.474 / max 2.71 mm (A-01), so the real air gap at the S1 tip can be below 10.0 by more than the whole margin. Calipers on the base face and the S1 hole (A-01, A-03) retire it.",
  "Strength and seating are not calculated (A-11, A-05, plan R3): the 0.45 kg thermoblock hangs 12 mm in front of the plate on two screws, one through a 37.70 mm Ø7.0/Ø4.0 metal column at S2, and the S1 spacer bears on only a crescent (about 120°) of the base face because the rest of its end lies over the U-notch. The geometry passes; whether the joint is stiff enough is a bench question.",
  "The contact rows are exact only at nominal: with fixed-length spacers (10.10, 37.70), a standoff tip at its ±0.10 limit leaves a 0.100 mm gap or a 2.592 mm³ overlap per spacer (sweep, tip_z). In a real assembly the screw clamp would move the mount by that amount instead, which moves the S1 gap to the casting by ±0.10 as well; a spacer cut to fit, or a tip tolerance tighter than ±0.10, would close this."
 ],
 "stopped": false
}
```
