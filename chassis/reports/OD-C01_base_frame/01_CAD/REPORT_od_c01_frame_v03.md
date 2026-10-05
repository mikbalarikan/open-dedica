# REPORT — od_c01_frame v03 (20260930-od-c01-base-frame)

Designer: Claude Code, Opus 5 · spec version 1.3 · plan `01_CAD/DESIGN_PLAN.md` with the notes of briefs WP-03 and WP-04 and the amendments of brief WP-06 · brief WP-06 (J3, revision B, build attempt 1 of 2, fix_cycles 3) · 2026-10-05 UTC

Every number below was measured by `01_CAD/check_od_c01_frame_v03.py` on the re-imported STEP files `02_STEP_STL/od_c01_frame_C1_v03.step` and `02_STEP_STL/od_c01_assembly_C1_v03.step`. The full rows (568, each with measured value, margin, location and reason) are in `01_CAD/check_od_c01_frame_v03.json`; §3 gives each §5 row's governing (least-margin) sub-row. The five new input hashes of WP-06 were re-checked before the build: every one matches. The v01 and v02 files are untouched; v03 has its own scripts (`*_v03.py`), started from the v02 scripts and changed only where WP-06's amendments say.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c01_frame_v03.py` | a4362d041c6b9d3a81eec3b5b9c30bf926e99a675303f4981be4abd2abe5db9c | parametric script (plate and check assembly), Algebra mode |
| `01_CAD/check_od_c01_frame_v03.py` | dd5443a9f53e3093f0b9829cb6d245e2d4c4b98f246578c0b075cfd43697d4ed | checks, written before the build (D3); the v02 script plus the spec 1.3 rows |
| `01_CAD/sections_od_c01_frame_v03.py` | 4a07abee31949ecbca5c480ca47a0ecc4a81c8cfa313f87cab8b64ed88c83992 | D6 sections |
| `01_CAD/sweep_od_c01_frame_v03.py` | 32dff3c0e0cca22e97ba414a63e2343e588ca33326e5a131bb7f27d0e5a3f741 | D7 sweep |
| `01_CAD/probe/probe_newparts_v03.py` | 2ce21957220abb63eca46531cc287f6b83e3eedf727a1ee07ef1468f2a5898ba | pre-build probe of the five new inputs as placed (not a gate) |
| `01_CAD/probe/probe_newparts_v03.json` | 63871224aac81215445c5d835d2d2b030a2dc135dddcf2b664de84f0abbcbdb7 | probe readings: validity, envelopes, Y-axis bores of the placed inputs |
| `01_CAD/build_record_v03.json` | 14578f5f82db4d6dfa67dc7fa3b182cfa0c69d3dab0b0cbe951909a010865467 | parameters, export hashes, placements |
| `01_CAD/check_od_c01_frame_v03.json` | 7f8fa24be207662026f7bc852ce2256e3bd286036899d51f6058b27a7a1119d4 | check results (568 rows, facts) |
| `01_CAD/check_od_c01_frame_v03.log` | 4a59ab539921f1a497353144ccfec6ea902829faea6750ec987bbbf848080821 | check console |
| `01_CAD/sections_v03.json` | d8918c006e9da6c26ac5721ed910194fbd20fce75a608d1f0c2bdb1fa976ee93 | section planes, cut areas, nothing_clipped |
| `01_CAD/sweep_v03/sweep_summary_v03.json` | dfa7b5270131c3ab10226f0f33a5659fe53e3ff339b884a15309ffcfee4a9867 | sweep: per-variant status, worst margin per gate row |
| `01_CAD/sweep_v03_run.log` | 0ff89c22200aabf77d22e8d4a57d0d01044ab7905a3c296a3df74f14e64d02bc | sweep console |
| `02_STEP_STL/od_c01_frame_C1_v03.step` | 87877a649306995965d4640f54cbf83c20715888b29eb057b18e2f2d2933d29b | AP242 (`tools.core.write_step`), one solid `od_c01_frame` |
| `02_STEP_STL/od_c01_assembly_C1_v03.step` | 44d2120be386438de18bc05f260043f49dbb9ae18ba7a4157fc553a0e56c4e74 | AP242 check assembly, 17 labelled solids (§5) |
| `02_STEP_STL/od_c01_frame_C1_v03.stl` | 34d24746c62a6e1220544ce465d2714aa8f3b9631e3bf08d18e69937616af963 | binary STL, `tools.core.write_stl` after clearing the triangulation; tolerance 0.01 mm / angular 0.20 rad; 11 676 triangles |
| `03_Sections/od_c01_frame_v03_top_z-40_carrier.png` | 0ffdd5a8db8e668da25944e00cb1927af09043addfe1bb4384f9d0b9883d8811 | z = -40.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z-148_c04.png` | 0693ecca7e582dfaaff3ad238987f4054b314bf57296bede62baced45087c6b6 | z = -148.00 mm; cut 1345.52 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_x37_c03.png` | ac99353f6fba109133214c9dd4b569b8f2fa0fe7808a7244cca539c39ffb6914 | x = 37.00 mm; cut 2382.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_x65_bulkhead.png` | b710ecbd27a57bb08fba112d071b0447474caac1b68ce5987470a005c2908650 | x = 65.00 mm; cut 2334.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z-120_drain.png` | aba7a87f4f858f26bdcd077f2636ee5c98930c9e22370cb19fbb99fbe1ebb60c | z = -120.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z90_feet.png` | 3ca693901b367b58f4db43b24dd8231ff13df9bb86f3096e3e805181ac77bb26 | z = 90.00 mm; cut 1399.20 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z-42_valve.png` | 62b18e2313115bcf28e8eebdae376b71f85501e9633ef03fa40496ce019d0758 | z = -42.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_x-113_valve.png` | eea2934ba4efbe8404daa09a2f6fbcf36b521319415680fc0a8c0d4d97e8f9f0 | x = -113.00 mm; cut 2376.47 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_front_y-3_plan.png` | 7d6f599a34c0bbeee9f4012a6b815e575487de91e5ea2be222f154d43622bde7 | y = -3.00 mm; cut 96499.79 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z-222_tray.png` | 2fd0be4476f99d1c5e9c9f53f4fc075d26bc96b8e85c0ba6320ee5eb6bf2fd31 | z = -222.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z-78_tray.png` | f1b37ade024371d3907c1c83256b022137f9177fdecdf8c7f1f7805a6f55ef3a | z = -78.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z-282_back.png` | df046b935f0e07c04eed32a043c4ea07d7f6e7796533ba06ab24d7e9a656847e | z = -282.00 mm; cut 1344.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z77_front.png` | 1418afd62d03e83cf712612de9246f21f635363c62c8ae7765c51982847318ba | z = 77.00 mm; cut 1344.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_z62_bracket.png` | 8b717a71e9141a704ad122deb7adf9ea04eb25352086125246bc45b3ee3810a3 | z = 62.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_x104.5_bracket.png` | 50bed4d6b8455b898069704953ad9b856259dea34e2452bc6e4bd1648f216afa | x = 104.50 mm; cut 2326.25 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_asm_x0.png` | 70c30fc569dba04d15c1a50a149cc844c3cbc0cedb0b17440f27cd797dae0611 | x = 0.00 mm; cut 9598.61 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_asm_z-148.png` | 2929204c12633513553169b939bef3ef7e435748aea764a8d8d9a2b44b7078e3 | z = -148.00 mm; cut 2534.19 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_asm_x37.png` | 7f12af3967d25e52c3c88980841a4c1a4e9497151b90669cf8595c419d97c607 | x = 37.00 mm; cut 7467.34 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_asm_z32_mouth.png` | 1f23645267dfadda1a6a93935d52058153399dd5cf57d84b1741da3668b0d9b4 | z = 32.00 mm; cut 2106.22 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_asm_z-222_tray.png` | 320ccc296297ec9af3b42fbbdb00e953ec5262430807ea93a43d1472ce90c23f | z = -222.00 mm; cut 3951.29 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_asm_z-282_back.png` | a19d71f522eb6fd7f8d7749fc59b21505e22c9e1b583f6d4abde22ab4c9432ce | z = -282.00 mm; cut 1545.60 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_top_asm_z77_front.png` | 975f75d72a2ad33d1d57180301c1523afa267d54a561658b65cd07f7948d749b | z = 77.00 mm; cut 1982.68 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v03_left_asm_x104.5_bracket.png` | 0d93703808c768959e4b3171f11bf89f58cb2667c251fe7eec832480481b8c40 | x = 104.50 mm; cut 4775.35 mm²; nothing clipped (0) |

The sweep exports (11 variants: plate STEP, assembly STEP, STL, build record, check results) are under `01_CAD/sweep_v03/<variant>/` and are not deliverables. The new cut areas agree with hand arithmetic from spec §4: z −222 and z −78 cut two Ø4.0 holes each, 240 × 6 − 2 × 4.0 × 6 = 1392.00; z −282 and z +77 cut four, 1440 − 96 = 1344.00; x 104.5 cuts the three bracket holes through their axes and the two OD-C08 holes at x 106 as 2.6458 chords: 2430 − 72 − 2 × 2.6458 × 6 = 2326.25.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · ocpsvg 0.6.0 · numpy 2.5.3 · repo commit d60daa486a25b3d2b51cf68356b01f501c4c3873

## 3. Gate self-check

Bands are from GATES §0: mm 0.005, mm³ 0.001, degrees 0.001, counts and 1/0 facts 0. Margins are signed (positive inside). `min_wall`, `min_wall_wide` and `overhang_census` ran at **spacing 0.7 mm** (plan §4); every value marked "sp 0.7" came from that spacing.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | == 1 | 0 | — | PASS | — |
| feature_census | 6 planar; 48 cylindrical (44 concave, 4 convex); 0 cone / sphere / torus / B-spline / other; 44 bores | WP-06: 6 planar, 48 cylindrical (44 concave, 4 convex), 44 bores | 0 | — | PASS | — |
| envelope_within_spec | size 240.000 × 6.000 × 405.000; position x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000 | each ± 0.1 | +0.1 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | 240.000 × 6.000 × 405.000; position reported apart (above) | each in [spec − 0.1, spec + 0.1] | +0.1 | — | PASS | — |
| U-03 (a) plate\|OD-C03 | clearance 0.000; common volume 0.000 mm³; four holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.10 | 0; 0; +0.10 | (−2, 0, −171) | PASS (assumed: A-03) | A-03 |
| U-03 (a) plate\|OD-C04 | clearance 0.000; 0.000 mm³; four holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.10 | 0; 0; +0.10 | (−38, 0, −114) | PASS (assumed: A-02) | A-02 |
| U-03 (a) plate\|OD-H01 | clearance 16.250; 0.000 mm³ | ≥ 2.0; ≤ 0 | +14.25 | | PASS (assumed: A-03) | A-03 |
| U-03 (a) plate\|OD-H11 | clearance 16.4925; boolean INCONCLUSIVE (OD-H11 brep_valid 0, OD-C04 A-14), as the row states | ≥ 10.0 | +6.4925 | | PASS (assumed: A-02); boolean INCONCLUSIVE by the row | A-02 |
| U-03 (a) OD-C03\|OD-C04 | clearance 8.000 | ≥ 2.0 | +6.0 | | PASS (assumed: A-02, A-03) | A-02, A-03 |
| U-03 (a) OD-H11 max z | −89.210 | ≤ −85.0 | +4.21 | | PASS (assumed: A-02) | A-02 |
| U-03 (a) OD-G01 v02 pose | read back: rear face max_y 205.000, a downward planar face at y 176.760 (the mouth), x −50.000 … 50.000, z −18.000 … 82.000 (all within 1e-7) | spec §4 joint values | ≥ −1e-7 (in band) | | PASS (assumed: A-01) | A-01 |
| U-03 (a) OD-G01 v02 to everything else | clearance to the plate 176.760, OD-C03 211.057, OD-H01 201.111, OD-C04 155.916, OD-H11 110.780, carrier foot box 173.401, **OD-C09 8.776**, OD-C08 118.164, OD-C07 162.240, OD-C11 269.067, the six OD-C16 brackets 170.680 … 304.223; common volume 0.000 mm³ with every sound solid; with OD-H11 INCONCLUSIVE by the row | ≥ 2.0; ≤ 0 | +6.776 (least, to OD-C09) | | PASS (assumed: A-01) | A-01 |
| U-03 (a) plate\|OD-C07 (A-17, now delivered) | clearance 0.000; 0.000 mm³; its four Ø3.400 footprint holes coaxial with the plate's Ø4.0 holes, offset 0.000 each | = 0; ≤ 0; ≤ 0.20 | 0; 0; +0.20 | (−113 / −71, 0, −42 / −148.5) | PASS (assumed: A-17) | A-17 |
| U-03 (a) plate\|OD-C08 (identity, A-18) | clearance 0.000; 0.000 mm³; four Ø3.400 flange holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.20 | 0; 0; +0.20 | (88 / 106, 0, −222 / −78) | PASS (assumed: A-18) | A-18 |
| U-03 (a) plate\|OD-C11 (identity, A-18) | clearance 0.000; 0.000 mm³; four Ø3.400 flange holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.20 | 0; 0; +0.20 | (±81 / ±95, 0, −282) | PASS (assumed: A-18) | A-18 |
| U-03 (a) plate\|OD-C09 (identity, A-20) | clearance 0.000; 0.000 mm³; four Ø3.400 flange holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.20 | 0; 0; +0.20 | (±85 / ±95, 0, +77) | PASS (assumed: A-20) | A-20 |
| U-03 (a) plate\|OD-C16 × 6 (A-19) | each bracket: clearance 0.000; 0.000 mm³; its Ø3.400 hole coaxial with the plate's Ø4.0 hole, offset 0.000 (the Ø6.5 counterbore is excluded by a diameter-filtered census) | = 0; ≤ 0; ≤ 0.20 | 0; 0; +0.20 | (±104.5, 0, −262 / −15 / +62) | PASS (assumed: A-19) | A-19 |
| U-03 (a) plate\|carrier foot box (x ±55, y 0 … 4, z −70 … −26) | clearance 0.000; 0.000 mm³ | = 0; ≤ 0 | 0 | (−33, 0, −40) | PASS (assumed: A-01) | A-01 |
| U-03 (a) assembly path (L-10) | OD-C03, OD-C04, the foot box, OD-C07, OD-C08, OD-C09, OD-C11 and the six brackets each lowered along −Y: clearance to the plate 10.000, 1.000, 0.100, 0.000 at lifts 10, 1, 0.1, 0 (52 rows) | = lift | ≥ −5.7e-15 (in band) | | PASS (assumed: A-01 … A-03, A-17 … A-20) | A-01 … A-03, A-17 … A-20 |
| U-03 (b) | — | N/A by the row | — | — | N/A | — |
| U-04 part | AP242; 1 solid; volume delta 1.59e-7 mm³; faces delta 0 (54); label `od_c01_frame` kept; valid after 1 | 1; 1; ≤ 0; 0; 1; 1 | −1.6e-7 (in band) | — | PASS | — |
| U-04 assembly | AP242; **17 solids**; faces delta 0; 17 labels kept; per part volume delta ≤ 4.3e-9 mm³, faces delta 0, valid after 1 for every sound part (plate, OD-C03, OD-H01, OD-C04, OD-G01, OD-C07, OD-C08, OD-C09, OD-C11, six OD-C16, foot box). OD-H11: faces delta 0, validity unchanged (0 → 0), **volume delta 0.0524 mm³ INCONCLUSIVE by OD-C04 A-14** (second generation 2.9e-9) | as above | — | — | PASS for the part and 16 of 17 assembly parts; OD-H11 volume row and the whole-assembly volume INCONCLUSIVE | — |
| U-05 | 1 plate; **38 Ø4.000**, 4 Ø3.400, 2 Ø8.000 through-holes; 44 bores; 6 planar and 48 cylindrical faces | 1; 38; 4; 2 | 0 | — | PASS | — |
| U-06 (Soft) | `min_wall` wide 5.000 (sp 0.7) | ≥ 2.0 | +3.0 | (−115, −5.7, −42) | PASS | — |
| U-07 | STL sagitta 0.0049723 at tol 0.01, angular 0.20 rad (limit 0.2310); delivered STL 11 676 triangles, 1 body, 0 naked edges, consistent winding. 3MF clause: orchestrator step (WP-06) | ≤ 0.01; ≤ 0.2310 | +0.0050277; +0.0310 | | PASS (sagitta); 3MF: orchestrator step | — |
| U-08 | — | N/A by the row | — | — | N/A | — |
| D-01a | `min_wall` 5.000 (sp 0.7) | ≥ 0.8 | +4.2 | (−115, −5.7, −42): web from the OD-C07 hole x −113 to the edge x −120 | PASS | — |
| D-01b | 5.000 (sp 0.7) | ≥ 2.0 | +3.0 | same | PASS | — |
| D-02 | 240.0 × 405.0 on the bed, 6.0 tall | ≤ 420 × 420 × 500 | +15.0 (z) | — | PASS (assumed: A-09) | A-09 |
| D-03a | least downward angle 90.0° off the bed (sp 0.7, build +Y) | ≥ 45° | +45.0 | — | PASS (assumed: A-14) | A-14 |
| D-03b | no downward face off the bed (D-03a), so span 0.0; every hole vertical (sections) | ≤ 5 | +5.0 | — | PASS (reviewer confirms from sections) | — |
| D-04a | four feet holes Ø3.400 | ≥ 3.25 | +0.15 | (±110, −6, 90 / −295) | PASS (assumed: A-12) | A-12 |
| D-05a | 14.000 across (least material radius 7.000 about an insert axis; **4218 rays on all thirty-eight holes**, 0 unread) | ≥ 8.0 | +6.0 | (−113, −0.5, −42) at 180°, toward the edge x −120 | PASS (assumed: A-11) | A-11 |
| D-05b | **38 holes** Ø4.000, length 6.000, through | 4.0 ± 0.05; ≥ 5.7 | +0.05; +0.3 | | PASS (assumed: A-11) | A-11 |
| D-06a | 5.000 (sp 0.7) | ≥ 1.0 | +4.0 | (−115, −5.7, −42) | PASS | — |
| D-07 | — | N/A by the row | — | — | N/A | — |
| J-05 | `min_wall` 5.000 (sp 0.7); located ring wall 5.000 around the **thirty-eight** insert holes (least per hole: 5.000 at the two OD-C07 holes, 6.000 at the four OD-C09 holes, ≥ 7.9 at every other new hole) | ≥ 3.0 | +2.0; +2.0 | ring: (−113, −0.5, −42) at 180° | PASS | — |
| E-06 | — | N/A by the row | — | — | N/A | — |
| REQ-01 | 4 × Ø4.000 through, length 6.000, offset 0.000 at (±35, −40), (±35, −60) | 4.0 ± 0.05; ≤ 0.10 | +0.05; +0.10 | | PASS (assumed: A-01, A-11) | A-01, A-11 |
| REQ-02 | 4 × Ø4.000 through, offset 0.000; coaxial with OD-C04 (U-03) | same | +0.05; +0.10 | | PASS (assumed: A-02, A-11) | A-02, A-11 |
| REQ-03 | 4 × Ø4.000 through, offset 0.000; coaxial with OD-C03 (U-03) | same | +0.05; +0.10 | | PASS (assumed: A-03, A-11) | A-03, A-11 |
| REQ-04 | 4 × Ø4.000 through, offset 0.000 at (65, −45 / −105 / −165 / −225) | same | +0.05; +0.10 | | PASS (assumed: A-04, A-11) | A-04, A-11 |
| REQ-05 | 4 × Ø3.400 through, offset 0.000 | 3.4 ± 0.1; ≤ 0.10 | +0.10; +0.10 | | PASS (assumed: A-12) | A-12 |
| REQ-06 | 2 × Ø8.000 through, offset 0.000 | 8.0 ± 0.1; ≤ 0.10 | +0.10; +0.10 | | PASS (assumed: A-13) | A-13 |
| REQ-07 | max_y 0.000; thickness 6.000; 1 planar +Y face, own y extent 0.000, area 96 499.789 mm² (derived for 44 holes 96 499.789, information) | 0.00 ± 0.10; 6.0 ± 0.1; 1 plane | +0.10; +0.10; 0 | | PASS (assumed: A-01 … A-03 on top_y) | A-01 … A-03 |
| REQ-08 | OD-H11 max z −89.210; clearance(plate, OD-H11) 16.4925 | ≤ −85.0; ≥ 10.0 | +4.21; +6.4925 | | PASS (assumed: A-02) | A-02 |
| REQ-09 (Soft) | not geometric (bench) | flat in service | — | — | INCONCLUSIVE; risk MEDIUM (§9) | A-10, A-14 |
| REQ-10 | 4 × Ø4.000 through, offset 0.000 at (−113, −42), (−71, −42), (−113, −148.5), (−71, −148.5); **coaxial with the delivered OD-C07 as placed by A-17, offset 0.000 each** | 4.0 ± 0.05; ≤ 0.10; coaxial ≤ 0.20 | +0.05; +0.10; +0.20 | | PASS (assumed: A-17, A-11) | A-17, A-11 |
| REQ-11 | 4 × Ø4.000 through, length 6.000, offset 0.000 at (88, −222), (106, −222), (88, −78), (106, −78); coaxial with OD-C08's flange holes 0.000; nearest centre to centre **18.000** each; to the outline **32.000 / 14.000 / 32.000 / 14.000** (the side x = 120) | 4.0 ± 0.05; ≤ 0.10; ≥ 6.0; ≥ 8.0 | +0.05; +0.10; +12.0; +6.0 | | PASS (assumed: A-18, A-11) | A-18, A-11 |
| REQ-12 | 4 × Ø4.000 through, offset 0.000 at (±81, −282), (±95, −282); coaxial with OD-C11 0.000; nearest centre to centre **14.000** each; to the outline **23.000** each (the side x = ±120 for the ±95 pair is 25.0; the rear edge z = −305 gives 23.0) | 4.0 ± 0.05; ≤ 0.10; ≥ 6.0 (WP-06); ≥ 8.0 | +0.05; +0.10; +8.0; +15.0 | | PASS (assumed: A-18, A-11) | A-18, A-11 |
| REQ-13 | 6 × Ø4.000 through, offset 0.000 at (±104.5, −262), (±104.5, −15), (±104.5, +62); coaxial with the six OD-C16 brackets 0.000; nearest centre to centre **22.142** (z −262), **49.601** right / **28.306** left (z −15), **17.755** (z +62); to the outline **15.500** each (the side x = ±120) | 4.0 ± 0.05; ≤ 0.10; ≥ 6.0; ≥ 8.0 | +0.05; +0.10; +11.755; +7.5 | | PASS (assumed: A-19, A-11) | A-19, A-11 |
| REQ-14 | 4 × Ø4.000 through, offset 0.000 at (±85, +77), (±95, +77); coaxial with OD-C09 0.000; nearest centre to centre **10.000** each (the pair 85 / 95); to the outline **23.000** each (the front edge z = +100; the R 10 corner arc about (±110, +90) is 27.5 away) | 4.0 ± 0.05; ≤ 0.10; ≥ 6.0; ≥ 8.0 | +0.05; +0.10; +4.0; +15.0 | | PASS (assumed: A-20, A-11) | A-20, A-11 |

Hole spacing is measured, not derived: the centre-to-centre figure is the distance from this hole's measured `bore_census` axis to the nearest other measured axis, and the outline figure is `clearance` from a vertex on that axis to each of the plate's eight outline faces (four straight sides, four R 10 corner arcs; the nearest feature is named in `01_CAD/check_od_c01_frame_v03.json` under `facts.new_hole_spacing`). The least readings over the eighteen new holes are **10.000 centre to centre** (REQ-14) and **14.000 to the outline** (REQ-11 at x 106).

## 4. Robustness sweep (D7)

Ten variants plus a nominal rebuild, one parameter at a time (plan §4; the hole-shift variants move all eight hole groups, the eighteen new holes included). The mounts, the housing and the ten parts of spec 1.3 stay at their fixed joints; every variant runs the full predicate set, the assembly, pose, coaxiality, spacing and path rows included. **All 11 built exactly one solid and no gate row failed in any variant.** The only rows not passed are the six that are INCONCLUSIVE or an orchestrator step by their own rows, in every variant alike: the two OD-H11 booleans, OD-H11's assembly volume row, the whole-assembly volume, the 3MF clause, and REQ-09.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| plate_t (top held at y 0) | 5.9 · 6.0 · 6.1 | yes | U-02 / REQ-07 / envelope size_y | 0.0 (on the tolerance edge, in band); D-05b depth +0.2 at 5.9 |
| insert_d (all thirty-eight) | 3.95 · 4.00 · 4.05 | yes | REQ-01 … REQ-04, REQ-10 … REQ-14, D-05b diameter | 0.0 (on the tolerance edge, in band); J-05 ring 4.975 (+1.975) at 4.05 |
| foot_d | 3.30 · 3.40 · 3.50 | yes | REQ-05 diameter; D-04a 3.30 | 0.0; +0.05 |
| drain_d | 7.90 · 8.00 · 8.10 | yes | REQ-06 diameter | 0.0 |
| all hole groups shifted (dx, dz) | (−0.05, −0.05) · 0 · (+0.05, +0.05) | yes | REQ-01 … REQ-14 offset and U-03 coaxiality 0.0707; J-05 ring 4.9506 and `min_wall` 4.950 at the OD-C07 hole x −113.05; REQ-11 to the outline 13.950 | +0.0293; J-05 +1.951; REQ-11 +5.95 |

D-05a reads 14.000 in every variant: its rays start on the spec axes, so the edge at x −120 stays 7.0 away; the shifted hole wall shows in the J-05 ring wall instead. The centre-to-centre readings are unchanged by the shift (10.000 at worst), because every hole group moves together. The STL sagitta is 0.0049723 at worst (+0.0050277). The part passes over the whole swept range, not only at nominal.

## 5. Build facts

- Envelope 240.000 × 6.000 × 405.000 mm (x −120 … 120, y −6 … 0, z −305 … 100). Volume **578 998.736 mm³**. Mass **717.96 g at 1240 kg/m³** (PLA, spec 1.3 §3, A-10; v02 read 737.05 g at PETG 1270 and 580 355.904 mm³, so revision B removes 1357.168 mm³ of material). Centre of mass (0.038, −3.000, −102.370).
- Fillets: none. The four R 10.0 corners are sketch arcs (`RectangleRounded`), as plan §3. No fillet ladder was needed.
- STL (the reference for the orchestrator's 3MF): **11 676 triangles** (header and `mesh_census` agree), 583 884 bytes, **volume 579 003.604 mm³** (`mesh_census`; B-rep 578 998.736), **bounding box x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000** (read from the STL vertices), 1 body, 0 naked edges, consistent winding; tolerance 0.01 mm, angular 0.20 rad; written by `tools.core.write_stl` after clearing the cached triangulation.
- Placements (each a `RigidJoint` on the plate at the spec §4 joint, connected to the component's own STEP origin; read back from the assembly STEP):
  - OD-C03 and OD-H01: `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`, unchanged.
  - OD-C04 and OD-H11: identity at (0, 70, −140), unchanged.
  - OD-G01 v02: `Location(Plane(origin=(0, 180.06, 32.0), x_dir=(1, 0, 0), z_dir=(0, −1, 0)))`, unchanged; read back x −50.000 … 50.000, y 176.760 … 205.000, z −18.000 … 82.000.
  - **OD-C07 (new in the assembly, A-17):** `Location(Plane(origin=(−92, 0, −60), x_dir=(0, 0, −1), z_dir=(0, 1, 0)))` — local x → −Z, y → −X, z → +Y, a proper rotation. Read back: envelope x −117.000 … −67.000, y 0.000 … 48.000, z −154.000 … −35.000; its four Ø3.400 footprint holes at (−113, −42), (−71, −42), (−113, −148.5), (−71, −148.5), each 4.000 long from y 0.
  - **OD-C08, OD-C09, OD-C11 (new, A-18, A-20):** identity. Read back: OD-C08 x 73.000 … 112.000, y 0.000 … 92.000, z −230.000 … −70.000 with four Ø3.400 flange holes at (88 / 106, −222 / −78); OD-C09 x ±116.000, y 0.000 … 215.000, z 72.000 … 97.000 with four Ø3.400 holes at (±85 / ±95, +77); OD-C11 x ±116.000, y 0.000 … 215.000, z −302.000 … −277.000 with four Ø3.400 holes at (±81 / ±95, −282).
  - **OD-C16 × 6 (new, A-19):** right side `Location((117, 0, z_c))`; left side `Location((−117, 0, z_c)) * Location((0,0,0), (0, 180, 0))` (180° about Y), z_c ∈ {−262, −15, +62}. Read back: right brackets x 98.000 … 117.000, left −117.000 … −98.000, y 0.000 … 16.000, z z_c ± 8.000; each bracket's Ø3.400 hole on (±104.5, z_c), 3.000 long from y 0, with its Ø6.5 counterbore above it.
  - Carrier foot box `od_c05_foot_reference_A01`: x ±55, y 0 … 4, z −70 … −26, a reference solid of the check assembly only (A-01).
- Reserved zones (spec §4, A-05 … A-08; prisms over the zone; heights: tray 36.9, valve 48, tank and electronics 400; `clearance` of each placed solid; 0 means the solid stands inside the prism; **reported, not gated**):

  | Zone | OD-C03 | OD-H01 | OD-C04 | OD-H11 | OD-G01 | foot box | OD-C07 | OD-C08 | OD-C09 | OD-C11 | OD-C16 (least of six) |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | tray x ±75, z −15 … +85 | 150.0 | 163.15 | 92.0 | 74.21 | 139.86 | 11.0 | 20.0 | 55.0 | **0.0** | 262.0 | 23.0 |
  | tank x ±70, z −305 … −250 | **5.0** | 17.80 | 93.0 | 110.0 | 232.0 | 180.0 | 96.0 | 20.22 | 322.06 | **0.0** | 28.0 |
  | valve x −117 … −67, z −154 … −35 | 58.05 | 44.01 | 17.0 | 24.26 | 138.73 | 12.0 | **0.0** | 140.0 | 107.0 | 123.0 | 12.0 |
  | electronics x 70 … 120, z −240 … −30 | 28.0 | **14.5** | 20.0 | 27.16 | 26.41 | 15.0 | 137.0 | **0.0** | 102.0 | 37.0 | 7.0 |

  OD-C07 stands in the valve zone and OD-C08 in the electronics zone, as A-05 and A-08 intend (spec 1.3: the electronics zone now holds OD-C08, measured x 73 … 112, z −230 … −70). Two readings are for the orchestrator's record, not gates: **OD-C11's wall and flanges (z −302 … −277, x ±116) stand inside the tank zone prism** (A-07 reserves x ±70, z −305 … −250 for a tank whose dock is deferred and which stands on the table), and **OD-C09's wall and flanges (z 72 … 97) stand inside the tray zone prism** (A-06 reserves x ±75, z −15 … +85 for a tray not yet scanned). Neither touches the other's holes; both are the delivered parts' own geometry, not this plate's.
- Hole webs (measured from `bore_census` axis positions: centre distance − r1 − r2): the two closest holes on the plate are now **6.000** apart wall to wall, the OD-C09 pairs (±85, +77) to (±95, +77); then 10.000 (OD-C11's pairs), 13.755 (bracket +62 to OD-C09's x ±95), 14.000 (OD-C08's pairs), 16.000 (the carrier pairs, the v02 minimum). The thinnest wall of the part is still the **5.000** web from (−113, −42) and (−113, −148.5) to the edge x −120, which sets `min_wall`.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The plate lies flat and all sixteen placed parts stand on its top face (clearance 0, interference 0 mm³); the feet at (±110, +90 / −295) enclose every placed part and the centre of mass (0.04, −102.37), so the machine cannot tip on its feet. |
| P2 | Function chains | Part foot → M3 × 8 from above → heat-set insert in a Ø4.0 plate hole coaxial with the part's Ø3.4 hole (offset 0.000 on all thirty-eight); the OD-C16 bracket adds the second link, its own Ø4.0 insert bore taking the panel's screw sideways; plate → feet through the four Ø3.4 holes; a leak → the two Ø8.0 drains at x −80, one under OD-C07's hose window. |
| P3 | Motion clearance | Nothing on this part moves; lowered straight down, each of the thirteen seated parts meets no plate material before y 0 (clearance = lift at 10, 1, 0.1, 0; 52 rows). |
| P4 | Human factors | Inserts are driven from the top into through-holes; screws go in from above, the feet screws too (A-12); the new holes keep ≥ 14.0 to the plate's outline, so a driver and an insert iron reach them with the panels off; the group head mouth faces down at y 176.76 over the tray zone. |
| P5 | Absurdity next to a real product | A 240 × 405 × 6 mm, 718 g printed base with 44 holes under a compact espresso machine whose panels, tray, bay and brackets all screw into it is in proportion; for its span it is thin (REQ-09, §9). |
| P6 | Floating, embedded, mirrored, upside-down | Every seated part touches y 0 with 0 mm³ overlap; the OEM parts float above by design (16.25, 16.49); the six brackets sit three per side at x ±117 with their counterbores up (section x 104.5), the left ones turned 180° about Y, so neither side is mirrored into the plate; the back panel is at z −302 … −277 and the front panel at z +72 … +97, each on its own end of the plate. |

## 7. Library and tools used

- Cards: none (plan §2: nothing matched).
- `tools.core`: `read_step`, `write_step` (AP242, part and assembly), `write_stl`, `compare_step`, `validity`, `common_volume`, `file_sha256`.
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `min_wall` / `min_wall_wide` (spacing 0.7), `overhang_census` (build_dir (0, 1, 0), spacing 0.7), `radial_extent` (D-05a, J-05 rings), `mesh_census`, `mass_properties`.
- `tools.drawing`: `write_sections` with `nothing_clipped`. `tools.result.gate` for every comparison.
- New code in the job scripts (not in the repository): `_census_dia`, a bore census filtered to one diameter, so `locate_bore` cannot pick the OD-C16 bracket's Ø6.5 counterbore instead of its Ø3.4 hole; `_outline_faces`, which selects the plate's four straight sides and four R 10 corner arcs by geometry (horizontal plane normals; cylinders whose axis is not a bore axis); `_spacing_rows`, which gates the REQ-11 … REQ-14 spacing clauses from those measurements.
- Missing tool: nothing in `tools/` writes or reads a 3MF; the 3MF clause of U-07 is the orchestrator's step (WP-06), with the STL facts in §5 as its reference.
- K-2 (v01, still true): OD-H11's lowest point sits 16.4925 above the plate, 0.0075 under spec §3/§4's rounded 16.5; REQ-08 (≥ 10.0) holds by +6.4925.

## 8. Deviations from the plan

1. **Amendments of WP-06 (not deviations, recorded for traceability):** thirty-eight insert holes (F05c tray, F05d back panel, F05e brackets, F05f front panel), census 48 cylindrical faces / 44 bores, top-face area rederived for 44 holes (96 499.789 mm²), the check assembly extended with OD-C07, OD-C08, OD-C09, OD-C11 and the six OD-C16 brackets, PLA 1240 kg/m³ for the mass figure.
2. **Versioned scripts:** v03 uses `build_od_c01_frame_v03.py`, `check_od_c01_frame_v03.py`, `sections_od_c01_frame_v03.py`, `sweep_od_c01_frame_v03.py`, so the v01 and v02 files stay as they are (WP-06: "leave every v01 and v02 file as it is").
3. **One fix cycle used (1 of 3), on the check script, not on the geometry.** The first sweep run reported `REQ-11 … REQ-14 centre_distance` FAIL (measured 0.0707) in the two hole-shift variants: the predicate excluded a hole's own axis by exact equality with its nominal position, so a shifted hole read as its own nearest neighbour. The predicate now takes the measured axis nearest the nominal position as the hole itself and measures to every other axis. The nominal export was not rebuilt and the delivered STEP and STL are byte-identical to the first export (`build_record_v03.json`); the nominal check and the whole sweep were re-run with the corrected predicate.
4. **Six OD-C16 poses are a single parametric table** (`c16_locations`), the left side built as a 180° rotation about Y followed by the translation, as spec §2 of the side-panel spec and A-19 state; the assembly labels carry the pose (`od_c16_l_z-262_bracket`), with `z-262` rather than `z−262` because the AP242 writer accepts letters, digits, `_` and `-` only.
5. Carried from v02 and unchanged: the foot box in the assembly STEP, no 3MF written (orchestrator step), U-04 on the assembly gated per part with OD-H11's volume row INCONCLUSIVE (A-14), D-03b derived from D-03a, the assembly built inside the build script. Six plate sections and four assembly sections were added for the new holes and parts.

## 9. What I am least sure of

1. **The 5.0 web from the OD-C07 outer inserts (x −113) to the left edge** is still the plate's thinnest wall, and revision B does not touch it: J-05 +2.0, D-05a 14.000 across. With an M3 × 5.7 × Ø4.6 heat-set insert (A-11) melted into the Ø4.0 hole, about 4.7 of material is left to a free edge, now in PLA rather than PETG (A-10), which softens sooner under the iron. The gate is met; the risk is a print-and-press one.
2. **REQ-09 (Soft) flatness, now with eighteen more holes.** An unribbed 240 × 405 × 6 PLA plate printed flat may lift at the corners; the six bracket holes sit 15.5 from a side edge and the OD-C09 and OD-C11 holes 23.0 from the front and rear edges, exactly where a warped corner shows most, and a hole pair only 6.000 apart wall to wall (±85 / ±95, +77) sits in the front edge zone. INCONCLUSIVE, risk MEDIUM; the first print answers it, and C2 (ribbed) is the deferred geometric answer.
3. **The spacing clause for REQ-12.** Spec §5 REQ-12 names only "≥ 8.0 from the plate edge"; the ≥ 6.0 centre-to-centre figure gated here comes from the WP-06 amendment table (and from the identical clause in REQ-11, REQ-13 and REQ-14). The measurement is 14.000, so the row passes either way, but the reviewer should read it against the spec's own wording.
4. **U-04 on the check assembly for OD-H11:** its volume changes 0.0524 mm³ on the first write (unsound input, OD-C04 A-14; second generation 2.9e-9), gated INCONCLUSIVE, not FAIL. The plate itself round-trips with a 1.6e-7 mm³ delta.

## 10. Stop

Not stopped.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c01-base-frame",
 "part": "od_c01_frame",
 "tag": "v03",
 "spec_version": "1.3",
 "files": [
  {
   "path": "01_CAD/build_od_c01_frame_v03.py",
   "sha256": "a4362d041c6b9d3a81eec3b5b9c30bf926e99a675303f4981be4abd2abe5db9c"
  },
  {
   "path": "01_CAD/check_od_c01_frame_v03.py",
   "sha256": "dd5443a9f53e3093f0b9829cb6d245e2d4c4b98f246578c0b075cfd43697d4ed"
  },
  {
   "path": "01_CAD/sections_od_c01_frame_v03.py",
   "sha256": "4a07abee31949ecbca5c480ca47a0ecc4a81c8cfa313f87cab8b64ed88c83992"
  },
  {
   "path": "01_CAD/sweep_od_c01_frame_v03.py",
   "sha256": "32dff3c0e0cca22e97ba414a63e2343e588ca33326e5a131bb7f27d0e5a3f741"
  },
  {
   "path": "01_CAD/probe/probe_newparts_v03.py",
   "sha256": "2ce21957220abb63eca46531cc287f6b83e3eedf727a1ee07ef1468f2a5898ba"
  },
  {
   "path": "01_CAD/probe/probe_newparts_v03.json",
   "sha256": "63871224aac81215445c5d835d2d2b030a2dc135dddcf2b664de84f0abbcbdb7"
  },
  {
   "path": "01_CAD/build_record_v03.json",
   "sha256": "14578f5f82db4d6dfa67dc7fa3b182cfa0c69d3dab0b0cbe951909a010865467"
  },
  {
   "path": "01_CAD/check_od_c01_frame_v03.json",
   "sha256": "7f8fa24be207662026f7bc852ce2256e3bd286036899d51f6058b27a7a1119d4"
  },
  {
   "path": "01_CAD/check_od_c01_frame_v03.log",
   "sha256": "4a59ab539921f1a497353144ccfec6ea902829faea6750ec987bbbf848080821"
  },
  {
   "path": "01_CAD/sections_v03.json",
   "sha256": "d8918c006e9da6c26ac5721ed910194fbd20fce75a608d1f0c2bdb1fa976ee93"
  },
  {
   "path": "01_CAD/sweep_v03/sweep_summary_v03.json",
   "sha256": "dfa7b5270131c3ab10226f0f33a5659fe53e3ff339b884a15309ffcfee4a9867"
  },
  {
   "path": "01_CAD/sweep_v03_run.log",
   "sha256": "0ff89c22200aabf77d22e8d4a57d0d01044ab7905a3c296a3df74f14e64d02bc"
  },
  {
   "path": "02_STEP_STL/od_c01_frame_C1_v03.step",
   "sha256": "87877a649306995965d4640f54cbf83c20715888b29eb057b18e2f2d2933d29b"
  },
  {
   "path": "02_STEP_STL/od_c01_assembly_C1_v03.step",
   "sha256": "44d2120be386438de18bc05f260043f49dbb9ae18ba7a4157fc553a0e56c4e74"
  },
  {
   "path": "02_STEP_STL/od_c01_frame_C1_v03.stl",
   "sha256": "34d24746c62a6e1220544ce465d2714aa8f3b9631e3bf08d18e69937616af963"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-40_carrier.png",
   "sha256": "0ffdd5a8db8e668da25944e00cb1927af09043addfe1bb4384f9d0b9883d8811"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-148_c04.png",
   "sha256": "0693ecca7e582dfaaff3ad238987f4054b314bf57296bede62baced45087c6b6"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_x37_c03.png",
   "sha256": "ac99353f6fba109133214c9dd4b569b8f2fa0fe7808a7244cca539c39ffb6914"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_x65_bulkhead.png",
   "sha256": "b710ecbd27a57bb08fba112d071b0447474caac1b68ce5987470a005c2908650"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-120_drain.png",
   "sha256": "aba7a87f4f858f26bdcd077f2636ee5c98930c9e22370cb19fbb99fbe1ebb60c"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z90_feet.png",
   "sha256": "3ca693901b367b58f4db43b24dd8231ff13df9bb86f3096e3e805181ac77bb26"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-42_valve.png",
   "sha256": "62b18e2313115bcf28e8eebdae376b71f85501e9633ef03fa40496ce019d0758"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_x-113_valve.png",
   "sha256": "eea2934ba4efbe8404daa09a2f6fbcf36b521319415680fc0a8c0d4d97e8f9f0"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_front_y-3_plan.png",
   "sha256": "7d6f599a34c0bbeee9f4012a6b815e575487de91e5ea2be222f154d43622bde7"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-222_tray.png",
   "sha256": "2fd0be4476f99d1c5e9c9f53f4fc075d26bc96b8e85c0ba6320ee5eb6bf2fd31"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-78_tray.png",
   "sha256": "f1b37ade024371d3907c1c83256b022137f9177fdecdf8c7f1f7805a6f55ef3a"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z-282_back.png",
   "sha256": "df046b935f0e07c04eed32a043c4ea07d7f6e7796533ba06ab24d7e9a656847e"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z77_front.png",
   "sha256": "1418afd62d03e83cf712612de9246f21f635363c62c8ae7765c51982847318ba"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_z62_bracket.png",
   "sha256": "8b717a71e9141a704ad122deb7adf9ea04eb25352086125246bc45b3ee3810a3"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_x104.5_bracket.png",
   "sha256": "50bed4d6b8455b898069704953ad9b856259dea34e2452bc6e4bd1648f216afa"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_asm_x0.png",
   "sha256": "70c30fc569dba04d15c1a50a149cc844c3cbc0cedb0b17440f27cd797dae0611"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_asm_z-148.png",
   "sha256": "2929204c12633513553169b939bef3ef7e435748aea764a8d8d9a2b44b7078e3"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_asm_x37.png",
   "sha256": "7f12af3967d25e52c3c88980841a4c1a4e9497151b90669cf8595c419d97c607"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_asm_z32_mouth.png",
   "sha256": "1f23645267dfadda1a6a93935d52058153399dd5cf57d84b1741da3668b0d9b4"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_asm_z-222_tray.png",
   "sha256": "320ccc296297ec9af3b42fbbdb00e953ec5262430807ea93a43d1472ce90c23f"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_asm_z-282_back.png",
   "sha256": "a19d71f522eb6fd7f8d7749fc59b21505e22c9e1b583f6d4abde22ab4c9432ce"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_top_asm_z77_front.png",
   "sha256": "975f75d72a2ad33d1d57180301c1523afa267d54a561658b65cd07f7948d749b"
  },
  {
   "path": "03_Sections/od_c01_frame_v03_left_asm_x104.5_bracket.png",
   "sha256": "0d93703808c768959e4b3171f11bf89f58cb2667c251fe7eec832480481b8c40"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "cadquery-ocp-novtk 7.9.3.1.1",
  "repo_commit": "d60daa486a25b3d2b51cf68356b01f501c4c3873"
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
   "gate": "feature_census",
   "measured": 44,
   "unit": "count",
   "required": "6 planar, 48 cylindrical (44 concave, 4 convex), 0 other, 44 bores",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 240.0,
   "unit": "mm",
   "required": "240.0 x 6.0 x 405.0 each +-0.1; position x +-120, y -6..0, z -305..100",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01",
   "measured": 1,
   "unit": "count",
   "required": "solid_count 1, brep_valid 1, naked_edges 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": 240.0,
   "unit": "mm",
   "required": "240.0 x 6.0 x 405.0 each in [spec-0.1, spec+0.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03a",
   "measured": 0.0,
   "unit": "mm",
   "required": "contacts = 0; interference <= 0 mm3; coaxial <= 0.10 (mounts) / <= 0.20 (1.3 parts); OD-H01 >= 2.0; OD-H11 >= 10.0; OD-C03|OD-C04 >= 2.0; OD-G01 >= 2.0 to everything",
   "margin": 0.0,
   "at": "every seated part on y 0",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02",
    "A-03",
    "A-17",
    "A-18",
    "A-19",
    "A-20"
   ]
  },
  {
   "gate": "U-03b",
   "measured": null,
   "unit": "",
   "required": "N/A by the row (no motion variable)",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 1.591397449374199e-07,
   "unit": "mm3",
   "required": "volume delta <= 0 (band 0.001); faces delta 0; labels kept; valid after",
   "margin": -1.6e-07,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 44,
   "unit": "count",
   "required": "1 plate; 38 Dia 4.0, 4 Dia 3.4, 2 Dia 8.0 through-holes; 44 bores",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06",
   "measured": 4.999999999899995,
   "unit": "mm",
   "required": ">= 2.0 (Soft)",
   "margin": 3.0,
   "at": "(-115.0, -5.7, -42.0)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 0.0049723151243391,
   "unit": "mm",
   "required": "stl_max_sagitta <= 0.01; angular <= 0.2310 rad",
   "margin": 0.005028,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.3mf",
   "measured": null,
   "unit": "",
   "required": "the 3MF carries the same mesh",
   "margin": null,
   "at": null,
   "status": "ORCHESTRATOR_STEP",
   "assumes": []
  },
  {
   "gate": "U-08",
   "measured": null,
   "unit": "",
   "required": "N/A by the row (no threads)",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "D-01a",
   "measured": 4.999999999899995,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 4.2,
   "at": "(-115.0, -5.7, -42.0)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 4.999999999899995,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 3.0,
   "at": "(-115.0, -5.7, -42.0)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02",
   "measured": 405.0,
   "unit": "mm",
   "required": "<= 420 x 420 x 500",
   "margin": 15.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "D-03a",
   "measured": 90.0,
   "unit": "deg",
   "required": ">= 45",
   "margin": 45.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "D-03b",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 5",
   "margin": 5.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(+-110, -6, +90 / -295)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "D-05a",
   "measured": 14.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 6.0,
   "at": "(-113.0, -0.5, -42.0) at 180 deg",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 4.0,
   "unit": "mm",
   "required": "38 holes 4.0 +- 0.05, depth >= 5.7, through",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11"
   ]
  },
  {
   "gate": "D-06a",
   "measured": 4.999999999899995,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 4.0,
   "at": "(-115.0, -5.7, -42.0)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-07",
   "measured": null,
   "unit": "",
   "required": "N/A by the row",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "J-05",
   "measured": 4.999999999899995,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 2.0,
   "at": "(-115.0, -5.7, -42.0); ring 5.000 at (-113, -0.5, -42)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "E-06",
   "measured": null,
   "unit": "",
   "required": "N/A by the row",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "REQ-01",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10",
   "margin": 0.05,
   "at": "(+-35, -40 / -60)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-11"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with OD-C04",
   "margin": 0.05,
   "at": "(+-40, -148 / -114)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-11"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with OD-C03",
   "margin": 0.05,
   "at": "(-4 / 37, -239 / -171)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-11"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10",
   "margin": 0.05,
   "at": "(65, -45 / -105 / -165 / -225)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-11"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 3.4,
   "unit": "mm",
   "required": "4 x Dia 3.4 +- 0.1 through, offset <= 0.10",
   "margin": 0.1,
   "at": "(+-110, +90 / -295)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 8.0,
   "unit": "mm",
   "required": "2 x Dia 8.0 +- 0.1 through, offset <= 0.10",
   "margin": 0.1,
   "at": "(-80, -120 / -230)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 0.0,
   "unit": "mm",
   "required": "max_y 0.00 +- 0.10; 6.0 +- 0.1 thick; one top plane",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-08",
   "measured": -89.20999999999998,
   "unit": "mm",
   "required": "OD-H11 max_z <= -85.0; clearance >= 10.0",
   "margin": 4.21,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": null,
   "unit": "",
   "required": "flat in service (Soft, bench)",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-10",
    "A-14"
   ]
  },
  {
   "gate": "REQ-10",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with OD-C07 as placed",
   "margin": 0.05,
   "at": "(-113 / -71, -42 / -148.5)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-17",
    "A-11"
   ]
  },
  {
   "gate": "REQ-11",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with OD-C08; >= 6.0 centre to centre, >= 8.0 to the outline",
   "margin": 0.05,
   "at": "(88 / 106, -222 / -78)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-18",
    "A-11"
   ]
  },
  {
   "gate": "REQ-12",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with OD-C11; >= 8.0 to the outline",
   "margin": 0.05,
   "at": "(+-81 / +-95, -282)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-18",
    "A-11"
   ]
  },
  {
   "gate": "REQ-13",
   "measured": 4.0,
   "unit": "mm",
   "required": "6 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with the six OD-C16 brackets; >= 6.0 centre to centre, >= 8.0 to the outline",
   "margin": 0.05,
   "at": "(+-104.5, -262 / -15 / +62)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-19",
    "A-11"
   ]
  },
  {
   "gate": "REQ-14",
   "measured": 4.0,
   "unit": "mm",
   "required": "4 x Dia 4.0 +- 0.05 through, offset <= 0.10, coaxial with OD-C09; >= 6.0 centre to centre, >= 8.0 to the outline",
   "margin": 0.05,
   "at": "(+-85 / +-95, +77)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-20",
    "A-11"
   ]
  }
 ],
 "sweep": [
  {
   "parameter": "plate_t",
   "values": [
    5.9,
    6.0,
    6.1
   ],
   "all_built": true,
   "worst_gate": "U-02.size_y / REQ-07.thickness",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_d",
   "values": [
    3.95,
    4.0,
    4.05
   ],
   "all_built": true,
   "worst_gate": "REQ-01..REQ-04, REQ-10..REQ-14 / D-05b diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "foot_d",
   "values": [
    3.3,
    3.4,
    3.5
   ],
   "all_built": true,
   "worst_gate": "REQ-05 diameter; D-04a 3.30",
   "worst_margin": 0.0
  },
  {
   "parameter": "drain_d",
   "values": [
    7.9,
    8.0,
    8.1
   ],
   "all_built": true,
   "worst_gate": "REQ-06 diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "hole position (all 44 holes shifted dx, dz)",
   "values": [
    -0.05,
    0.0,
    0.05
   ],
   "all_built": true,
   "worst_gate": "REQ-01..REQ-14 offset 0.0707",
   "worst_margin": 0.029289322
  }
 ],
 "least_sure": [
  "the 5.0 web from the OD-C07 outer inserts (x -113) to the left edge is still the plate's thinnest wall (J-05 +2.0, D-05a 14.0 across); a Dia 4.6 hot insert 5.0 from a free PLA edge can bulge it (A-11, A-17)",
  "the plate now carries 44 holes in a 240 x 405 x 6 unribbed PLA plate: REQ-09 (Soft, bench) is INCONCLUSIVE and the eighteen new holes, six of them within 15.5 of a side edge, take material out of the corners most likely to lift",
  "U-04 on the check assembly for OD-H11: its volume changes 0.0524 mm3 on the first write (unsound input, OD-C04 A-14; second generation 2.9e-9), gated INCONCLUSIVE, never passed"
 ],
 "stopped": false
}
```
