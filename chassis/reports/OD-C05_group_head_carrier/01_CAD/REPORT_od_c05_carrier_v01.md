# REPORT — od_c05_carrier v01 (20260930-od-c05-group-head-carrier)

Designer: Claude Code, Opus 5.5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` (WP-02, written to spec 1.0) with the WP-03 amendments (spec 1.1) · brief WP-03 (J3, build attempt 1 of 2, fix_cycles 3) · 2026-09-30 UTC

`01_CAD/check_od_c05_carrier.py` measures every number below from the re-imported STEP files (`01_CAD/check_od_c05_carrier_v01.json`). The exceptions are rows that say they come from the build log (`01_CAD/build_od_c05_carrier_v01.json`: the round trip at export and the STL writer). These self-checks clear no HARD gate; only the reviewer's measurement does.

Input hashes were checked against the brief before any work. OD-G01 f8865cd1…4407b02, OD-G04 19b4a140…98d6ad2 and DESIGN_PLAN 41b80f84…232eced all match.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c05_carrier.py` | b3b0e94005cd76ed4838f55d018ef12e15b9c3d4618fa793c659ac7f5e87d116 | parametric build script (Algebra mode, one Params structure) |
| `01_CAD/check_od_c05_carrier.py` | fb421a41acd836988eaf2d5f1fbce8eaa6c053b7d8197aea7b9d905b48dd03e5 | checks, written before the build (D3) |
| `01_CAD/sections_od_c05_carrier.py` | bafeca772ffe8a5ccd67cf2696a49639d6b5ee34045203f8b2d6f5657c26a8d0 | D6 sections from the exported STEP files |
| `01_CAD/sweep_od_c05_carrier.py` | 62caaf0ceb90bd7f10e3f36eba666d94721d56fc923742797bf002a336918171 | D7 sweep driver |
| `02_STEP_STL/od_c05_carrier_C1_v01.step` | 3555600be58771b0efba7b2f2b5a48439bb442db58d5b5eb92fdd6a6fe410362 | AP242, re-imported for every measurement |
| `02_STEP_STL/od_c05_assembly_C1_v01.step` | b6fdbea9466703e81d63938840ce82853cddcac9c4f537d7e5d721f55817e1c3 | AP242 check assembly: carrier + OD-G01 (identity) + OD-G04 (+6.05° Z, z −6.82) |
| `02_STEP_STL/od_c05_carrier_C1_v01.stl` | aee6d05a1573742d131cb949e86b98acceb6fca179dc2cd46394a4918c8fe48a | binary STL, cached triangulation cleared; tol 0.01 mm / angular 0.20 rad; 4264 triangles; volume 108716.928 mm³ |
| `01_CAD/check_od_c05_carrier_v01.json` | 1c57b36c81835e0774266f800d9c3d333f0e66638e2d4bbcbf7ca2105866e03d | check results (every gate row and the facts) |
| `01_CAD/build_od_c05_carrier_v01.json` | d3457f40ea3fcf9a7d10e3ae7f1ca808c85d1f6dabbeb4a2917994211bd75102 | build log: parameters, export round trip, STL writer detail |
| `01_CAD/sections_od_c05_carrier_v01.json` | 298b88918bd3cc23b4e1d8a25083b5d7591753fa30ca7d2a21fcd9f9d2c7f8bc | section log: plane, point, nothing_clipped |
| `01_CAD/sweep_v01/SHA256SUMS_v01.txt` | 2cbc6e99df38bb23293aa1e11ff4d629748c4a97060ac7eea4453f29fb1805ca | SHA-256 of all 100 sweep files (20 runs × part STEP, assembly STEP, STL, build log, check JSON) |
| `03_Sections/od_c05_assembly_x0_v01_left.png` | 45c952415736c7a6bdad835d995b0f4f21af525050efb8a02efac15f14e57ecf | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x0_v01_left.png` | ff005505cf4bffe0b1fe8002cbaea64f9961c2a69184a484a0d6a1e25b9a13dd | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x35_v01_left.png` | edf5390642a14c4dd97241fd525ae097c3ad1305768cdb093727a3c0eab477c8 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x44_v01_left.png` | 7972feb30a6f1a93646deca2bfe23305cc489a611111c9b6e3650f34375062d7 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x48_v01_left.png` | 7d95e4c21d402ead81af662b28df7eea4e04ca042f7f0061b88683c8584e762c | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_y44_v01_front.png` | 400b0fbacba5c85ebc25ca1aecfeaa2fa5ee024be96bbc49e77ea8eb8fefdbfe | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_ym110_v01_front.png` | 537c6d019dd9ff66a5758ad7a169dd3a47c903e395f3bf67883901129cd82dec | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_zm27p44_v01_top.png` | 49e475ca672c694dab36d477b1545de225eb4103a352b13575cf50d62f827d83 | section, nothing_clipped 0 |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · OCCT 7.9.3 · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (tools used unmodified)

## 3. Gate self-check

The band is from GATES.md §0: 0.005 mm, 0.001°, 0.001 mm³, and 0 for counts and 1/0 facts. U-07's angular tolerance uses 0.00002 rad. Limits come from spec 1.1 §5 only. Margins are signed and positive inside the limit, so a pass inside the band shows its small negative margin.

Summary per §5 row:

| §5 row | Status | Measured (worst sub-row) |
|---|---|---|
| exactly_one_solid | PASS | 1 solid |
| U-01 | PASS | solid_count 1, brep_valid 1, naked_edges 0 |
| U-02 / envelope_within_spec | PASS | 100.000 × 225.000 × 45.000 mm (each margin +0.1); position x −50.000 … 50.000, y −175.000 … 50.000, z −69.940 … −24.940 |
| U-03 (a) | PASS (assumed: A-01, A-06) | **carrier/OD-G01:** clearance 0.000 mm (the designed face contact at z −24.94); interference 0.000 mm³; the four carrier holes sit 0.000 mm from the OD-G01 insert-bore axes, measured on the OD-G01 solid in the check assembly. **carrier/OD-G04:** clearance 5.000 mm (margin +3.0), nearest points (21.2132, 21.2132, −24.94) on the carrier and (21.2132, 21.2132, −19.94) on OD-G04; interference 0.000 mm³. OD-G01 and OD-G04 validity read 1/1/0 before the booleans |
| U-03 (b) | N/A | no motion variable |
| U-04 | PASS | re-read: AP242, 1 solid, label `od_c05_carrier`, valid after; built versus file at export (build log): volume delta 1.70e-9 mm³, faces delta 0, labels 1, valid 1 |
| U-05 / feature_census | PASS | 20 planar, 16 cylindrical (14 concave, 2 convex R 6.000), 0 of any other kind, 14 bores; each hole located: 4 × Ø3.400 through along Z, 4 × Ø6.500 × 2.000 counterbores, 4 × Ø3.400 through along Y |
| U-06 (Soft) | PASS | `min_wall` detail["wide"] 2.750 mm at (50.000, 44.006, −28.361) |
| U-07 | PASS | STL at tol 0.01 mm, angular 0.20 rad (limit 0.23097); max sagitta 0.00498 mm (margin +0.00502); **4264 triangles**; one closed body with consistent winding; **STL volume 108716.928 mm³** (B-rep 108712.078 mm³). The 3MF is the orchestrator's, made from this STL |
| U-08 | N/A | no threads |
| D-01a | PASS | min_wall 2.750 mm (≥ 0.8, margin +1.95) at the web between the Ø6.5 counterbore and the side face x 50, at (50.000, 44.006, −28.361) |
| D-01b | PASS | 2.750 mm (≥ 2.0, margin +0.75); sweep worst 2.679 mm (hole_xy 44.05); 2.700 mm at the Ø6.6 counterbore rung (2.70 was predicted) |
| D-02 | PASS (assumed: A-08) | 100.0 × 45.0 on the bed and 225.0 tall, inside 220 × 220 × 250 (margins 120, 175, 25) |
| D-03a | **INCONCLUSIVE** | **Outside the named exception:** `overhang_census(build_dir=(0,1,0))` finds a least of 45.0000° at (17.6777, −92.3223, −24.94), on the lower window's gable/arc tangent line. That value lies inside the tool's own sampling bound of 0.0090°, so the tool returns INCONCLUSIVE; no sample is under 45° (`below_min_deg` 0). **Diagnostics (not gates):** the planar downward faces alone read exactly 45.0000° (bound 0). The two window arcs alone read a least of 45.00000027° with bound 0.009°: INCONCLUSIVE at spacing 0.5 mm and at 0.1 mm alike. **Named exception, reported apart:** 8 faces excluded by position; least 0.0° at the counterbore crown (−44.0, −40.75, −29.94); 524 samples under 45° |
| D-03b | PASS at nominal (the reviewer confirms from the sections) | **Outside the named exception:** no downward sample under 45° (`below_min_deg` 0), so no bridge: 0 mm (≤ 5). **Inside the named exception:** the widest crown is the Ø6.500 counterbore (≤ 6.5, margin 0.000). **Sweep:** at the REQ-02 upper tolerance, Ø6.6, the crown reads 6.6 and **FAILS the exception's ≤ 6.5** (see §4 and §9) |
| D-04a | PASS | all eight holes Ø3.400 (≥ 3.25, margin +0.15); sweep worst 3.300 (margin +0.05) |
| D-06a | PASS | 2.750 mm (≥ 1.0) |
| D-07 | N/A | no fit bores |
| E-06 | PASS (the reviewer confirms) | one solid; the two gusset inner faces at x ±46.0 tie the wall's rear face to the foot (sections x = 48 and x = 0) |
| REQ-01 | PASS (assumed: A-01) | four Ø3.400 holes through along Z; axis offset 0.000 from (±44, ±44) and 0.000 from the OD-G01 insert-bore axes |
| REQ-02 | PASS (assumed: A-09) | four Ø6.500 counterbores, 2.000 deep, open at z −29.940, coaxial within 0.000 |
| REQ-03 | PASS (assumed: A-01) | front face z −24.940 (`envelope` max_z); rear face z −29.940 (the counterbores' open ends); hole plus counterbore length 5.000 at all four |
| REQ-04 | PASS (assumed: A-06) | 108 rays (every 10° at z −29.5, −27.44, −25.4, r ≤ 30): 0 with material; every ray reads "no material", which is the expected reading. Positive controls: at θ 90° the first material is 42.4264 (the apex); at θ 0° it is 30.0000 |
| REQ-05 | PASS (assumed: A-03, A-04) | underside y −175.000 (`envelope` min_y); foot 4.000 thick (the length of each Y hole) |
| REQ-06 | PASS (assumed: A-04) | four Ø3.400 holes through along Y, offsets 0.000 from (±35, z −40 / −60) |
| REQ-07 | PASS (assumed: A-05) | `envelope` min_z −69.940 (≥ −70.0, margin +0.06) |
| REQ-08 | PASS (assumed: A-07) | 108 rays about (0, −110) over r ≤ 25: 0 with material. Controls: θ 90° 35.3553 (apex at y −74.645); θ 270° 25.0000. Nothing else is missing below y −50 (the census finds no bore or face beyond the plan's) |
| REQ-09 | INCONCLUSIVE (Soft bench) | not geometric; the first print answers it. Risk MEDIUM: 225 tall, 5.0 wall, two gussets with 40 mm legs, and the locking torque reacted through four M3 screws 88 mm apart (A-11) |

All check rows (from `01_CAD/check_od_c05_carrier_v01.json`):

| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | count | == 1 | 0 | — | PASS | — |
| U-01 solid_count | 1 | count | == 1 | 0 | — | PASS | — |
| U-01 brep_valid | 1 | bool | == 1 | 0 | — | PASS | — |
| U-01 naked_edges | 0 | count | == 0 | 0 | — | PASS | — |
| U-02 size_x | 100 | mm | in [99.9, 100.1] | 0.1 | — | PASS | — |
| U-02 size_y | 225 | mm | in [224.9, 225.1] | 0.1 | — | PASS | — |
| U-02 size_z | 45 | mm | in [44.9, 45.1] | 0.1 | — | PASS | — |
| envelope_within_spec min_x | -50 | mm | in [-50.1, -49.9] | 0.1 | — | PASS | — |
| envelope_within_spec max_x | 50 | mm | in [49.9, 50.1] | 0.1 | — | PASS | — |
| envelope_within_spec min_y | -175 | mm | in [-175.1, -174.9] | 0.1 | — | PASS | — |
| envelope_within_spec max_y | 50 | mm | in [49.9, 50.1] | 0.1 | — | PASS | — |
| envelope_within_spec min_z | -69.94 | mm | in [-70.03999999999999, -69.84] | 0.1 | — | PASS | — |
| envelope_within_spec max_z | -24.94 | mm | in [-25.040000000000003, -24.84] | 0.1 | — | PASS | — |
| D-02 bed x | 100 | mm | <= 220.0 | 120 | — | PASS (assumed: A-08) | A-08 |
| D-02 bed z | 45 | mm | <= 220.0 | 175 | — | PASS (assumed: A-08) | A-08 |
| D-02 height y | 225 | mm | <= 250.0 | 25 | — | PASS (assumed: A-08) | A-08 |
| REQ-03 front face z | -24.94 | mm | in [-25.040000000000003, -24.84] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| REQ-05 underside y | -175 | mm | in [-175.1, -174.9] | 0.1 | — | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-07 min_z | -69.94 | mm | >= -70.0 | 0.06 | — | PASS (assumed: A-05) | A-05 |
| U-04 schema | 1 | bool | == 1 | 0 | — | PASS | — |
| U-04 solids | 1 | count | == 1 | 0 | — | PASS | — |
| U-04 volume_delta | 0 | mm3 | <= 0.0 | 0 | — | PASS | — |
| U-04 faces_delta | 0 | count | == 0 | 0 | — | PASS | — |
| U-04 valid_after | 1 | bool | == 1 | 0 | — | PASS | — |
| U-04 name od_c05_carrier | 1 | bool | == 1 | 0 | — | PASS | — |
| feature_census plane_faces | 20 | count | == 20 | 0 | — | PASS | — |
| feature_census cylinder_faces | 16 | count | == 16 | 0 | — | PASS | — |
| feature_census cone_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census sphere_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census torus_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census bspline_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census other_faces | 0 | count | == 0 | 0 | — | PASS | — |
| feature_census concave_cylinders | 14 | count | == 14 | 0 | — | PASS | — |
| feature_census convex_cylinders | 2 | count | == 2 | 0 | — | PASS | — |
| feature_census bores | 14 | count | == 14 | 0 | — | PASS | — |
| U-05/REQ-01 hole (+44,+44) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (44.0000, 44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| D-04a hole Z (+44,+44) | 3.4 | mm | >= 3.25 | 0.15 | (44.0000, 44.0000, -27.9400) mm | PASS | — |
| REQ-01 hole (+44,+44) offset from nominal | 0 | mm | <= 0.1 | 0.1 | (44.0000, 44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 hole (+44,+44) through | 1 | bool | == 1 | 0 | (44.0000, 44.0000, -27.9400) mm | PASS | — |
| U-03a/REQ-01 hole (+44,+44) offset from OD-G01 insert | 0 | mm | <= 0.1 | 0.1 | (44.0000, 44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| U-05/REQ-02 cb (+44,+44) dia | 6.5 | mm | in [6.4, 6.6] | 0.1 | (44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (+44,+44) depth | 2 | mm | in [1.9, 2.1] | 0.1 | (44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (+44,+44) coaxial | 0 | mm | <= 0.1 | 0.1 | (44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-03 rear face z (cb (+44,+44) open end) | -29.94 | mm | in [-30.040000000000003, -29.84] | 0.1 | (44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-03 wall through (+44,+44) (hole + cb length) | 5 | mm | in [4.9, 5.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| U-05/REQ-01 hole (-44,+44) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-44.0000, 44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| D-04a hole Z (-44,+44) | 3.4 | mm | >= 3.25 | 0.15 | (-44.0000, 44.0000, -27.9400) mm | PASS | — |
| REQ-01 hole (-44,+44) offset from nominal | 0 | mm | <= 0.1 | 0.1 | (-44.0000, 44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 hole (-44,+44) through | 1 | bool | == 1 | 0 | (-44.0000, 44.0000, -27.9400) mm | PASS | — |
| U-03a/REQ-01 hole (-44,+44) offset from OD-G01 insert | 0 | mm | <= 0.1 | 0.1 | (-44.0000, 44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| U-05/REQ-02 cb (-44,+44) dia | 6.5 | mm | in [6.4, 6.6] | 0.1 | (-44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (-44,+44) depth | 2 | mm | in [1.9, 2.1] | 0.1 | (-44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (-44,+44) coaxial | 0 | mm | <= 0.1 | 0.1 | (-44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-03 rear face z (cb (-44,+44) open end) | -29.94 | mm | in [-30.040000000000003, -29.84] | 0.1 | (-44.0000, 44.0000, -29.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-03 wall through (-44,+44) (hole + cb length) | 5 | mm | in [4.9, 5.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| U-05/REQ-01 hole (+44,-44) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (44.0000, -44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| D-04a hole Z (+44,-44) | 3.4 | mm | >= 3.25 | 0.15 | (44.0000, -44.0000, -27.9400) mm | PASS | — |
| REQ-01 hole (+44,-44) offset from nominal | 0 | mm | <= 0.1 | 0.1 | (44.0000, -44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 hole (+44,-44) through | 1 | bool | == 1 | 0 | (44.0000, -44.0000, -27.9400) mm | PASS | — |
| U-03a/REQ-01 hole (+44,-44) offset from OD-G01 insert | 0 | mm | <= 0.1 | 0.1 | (44.0000, -44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| U-05/REQ-02 cb (+44,-44) dia | 6.5 | mm | in [6.4, 6.6] | 0.1 | (44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (+44,-44) depth | 2 | mm | in [1.9, 2.1] | 0.1 | (44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (+44,-44) coaxial | 0 | mm | <= 0.1 | 0.1 | (44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-03 rear face z (cb (+44,-44) open end) | -29.94 | mm | in [-30.040000000000003, -29.84] | 0.1 | (44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-03 wall through (+44,-44) (hole + cb length) | 5 | mm | in [4.9, 5.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| U-05/REQ-01 hole (-44,-44) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-44.0000, -44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| D-04a hole Z (-44,-44) | 3.4 | mm | >= 3.25 | 0.15 | (-44.0000, -44.0000, -27.9400) mm | PASS | — |
| REQ-01 hole (-44,-44) offset from nominal | 0 | mm | <= 0.1 | 0.1 | (-44.0000, -44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 hole (-44,-44) through | 1 | bool | == 1 | 0 | (-44.0000, -44.0000, -27.9400) mm | PASS | — |
| U-03a/REQ-01 hole (-44,-44) offset from OD-G01 insert | 0 | mm | <= 0.1 | 0.1 | (-44.0000, -44.0000, -27.9400) mm | PASS (assumed: A-01) | A-01 |
| U-05/REQ-02 cb (-44,-44) dia | 6.5 | mm | in [6.4, 6.6] | 0.1 | (-44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (-44,-44) depth | 2 | mm | in [1.9, 2.1] | 0.1 | (-44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-02 cb (-44,-44) coaxial | 0 | mm | <= 0.1 | 0.1 | (-44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-09) | A-09 |
| REQ-03 rear face z (cb (-44,-44) open end) | -29.94 | mm | in [-30.040000000000003, -29.84] | 0.1 | (-44.0000, -44.0000, -29.9400) mm | PASS (assumed: A-01) | A-01 |
| REQ-03 wall through (-44,-44) (hole + cb length) | 5 | mm | in [4.9, 5.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| U-05/REQ-06 foot hole (+35, z -40) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (35.0000, -175.0000, -40.0000) mm | PASS (assumed: A-04) | A-04 |
| D-04a foot hole (+35, z -40) | 3.4 | mm | >= 3.25 | 0.15 | (35.0000, -175.0000, -40.0000) mm | PASS | — |
| REQ-06 foot hole (+35, z -40) offset | 0 | mm | <= 0.1 | 0.1 | (35.0000, -175.0000, -40.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06 foot hole (+35, z -40) through | 1 | bool | == 1 | 0 | (35.0000, -175.0000, -40.0000) mm | PASS | — |
| REQ-05 foot thickness at (+35, z -40) | 4 | mm | in [3.9, 4.1] | 0.1 | (35.0000, -175.0000, -40.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| U-05/REQ-06 foot hole (-35, z -40) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-35.0000, -175.0000, -40.0000) mm | PASS (assumed: A-04) | A-04 |
| D-04a foot hole (-35, z -40) | 3.4 | mm | >= 3.25 | 0.15 | (-35.0000, -175.0000, -40.0000) mm | PASS | — |
| REQ-06 foot hole (-35, z -40) offset | 0 | mm | <= 0.1 | 0.1 | (-35.0000, -175.0000, -40.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06 foot hole (-35, z -40) through | 1 | bool | == 1 | 0 | (-35.0000, -175.0000, -40.0000) mm | PASS | — |
| REQ-05 foot thickness at (-35, z -40) | 4 | mm | in [3.9, 4.1] | 0.1 | (-35.0000, -175.0000, -40.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| U-05/REQ-06 foot hole (+35, z -60) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (35.0000, -175.0000, -60.0000) mm | PASS (assumed: A-04) | A-04 |
| D-04a foot hole (+35, z -60) | 3.4 | mm | >= 3.25 | 0.15 | (35.0000, -175.0000, -60.0000) mm | PASS | — |
| REQ-06 foot hole (+35, z -60) offset | 0 | mm | <= 0.1 | 0.1 | (35.0000, -175.0000, -60.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06 foot hole (+35, z -60) through | 1 | bool | == 1 | 0 | (35.0000, -175.0000, -60.0000) mm | PASS | — |
| REQ-05 foot thickness at (+35, z -60) | 4 | mm | in [3.9, 4.1] | 0.1 | (35.0000, -175.0000, -60.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| U-05/REQ-06 foot hole (-35, z -60) dia | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-35.0000, -175.0000, -60.0000) mm | PASS (assumed: A-04) | A-04 |
| D-04a foot hole (-35, z -60) | 3.4 | mm | >= 3.25 | 0.15 | (-35.0000, -175.0000, -60.0000) mm | PASS | — |
| REQ-06 foot hole (-35, z -60) offset | 0 | mm | <= 0.1 | 0.1 | (-35.0000, -175.0000, -60.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-06 foot hole (-35, z -60) through | 1 | bool | == 1 | 0 | (-35.0000, -175.0000, -60.0000) mm | PASS | — |
| REQ-05 foot thickness at (-35, z -60) | 4 | mm | in [3.9, 4.1] | 0.1 | (-35.0000, -175.0000, -60.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| D-01a min_wall | 2.75 | mm | >= 0.8 | 1.95 | (50.0000, 44.0059, -28.3610) mm | PASS | — |
| D-01b min_wall | 2.75 | mm | >= 2.0 | 0.75 | (50.0000, 44.0059, -28.3610) mm | PASS | — |
| D-06a min feature | 2.75 | mm | >= 1.0 | 1.75 | (50.0000, 44.0059, -28.3610) mm | PASS | — |
| U-06 (Soft) min_wall wide | 2.75 | mm | >= 2.0 | 0.75 | (50.0000, 44.0059, -28.3610) mm | PASS | — |
| D-03a overhang outside the named exception | — | deg | >= 45.0 | — | (17.6777, -92.3223, -24.9400) mm | INCONCLUSIVE: the least, 45.0000°, lies within its sampling bound (0.0090°) above min_deg; a finer spacing settles it | A-13 |
| D-03a exception faces counted (8 expected) | 8 | count | >= 8 | 0 | — | PASS | — |
| D-03b bridge span outside the named exception | 0 | mm | <= 5.0 | 5 | — | PASS | — |
| D-03b named exception crown span | 6.5 | mm | <= 6.5 | 0 | — | PASS | — |
| REQ-04 rays with material r<=30 (108 rays) | 0 | count | == 0 | 0 | — | PASS (assumed: A-06) | A-06 |
| REQ-04 control theta 90 apex | 42.4264 | mm | == 42.42640687119285 | -8.53e-13 | (0.0000, 42.4264, -27.4400) mm | PASS | — |
| REQ-04 control theta 0 | 30 | mm | == 30.0 | -3.55e-15 | (30.0000, 0.0000, -27.4400) mm | PASS | — |
| REQ-08 rays with material r<=25 (108 rays) | 0 | count | == 0 | 0 | — | PASS (assumed: A-07) | A-07 |
| REQ-08 control theta 90 apex | 35.3553 | mm | == 35.35533905932738 | -2.63e-12 | (0.0000, -74.6447, -27.4400) mm | PASS | — |
| REQ-08 control theta 270 | 25 | mm | == 25.0 | -1.78e-14 | (-0.0000, -135.0000, -27.4400) mm | PASS | — |
| E-06 gusset inner faces (one solid) | 2 | count | == 2 | 0 | — | PASS | — |
| U-03a carrier/OD-G01 contact clearance | 0 | mm | == 0.0 | 0 | (-50.0000, -42.0000, -24.9400) mm | PASS (assumed: A-01) | A-01 |
| U-03a carrier/OD-G01 interference | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01) | A-01 |
| U-03a carrier/OD-G04 clearance | 5 | mm | >= 2.0 | 3 | (21.2132, 21.2132, -24.9400) mm | PASS (assumed: A-06) | A-06 |
| U-03a carrier/OD-G04 interference | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-06) | A-06 |
| U-03 assembly carrier equals part file | 2.33e-10 | mm3 | <= 0.0 | -2.33e-10 | — | PASS | — |
| U-03b | — |  | N/A | — | — | N/A: no motion variable (spec section 5 U-03 b) | — |
| U-07 stl_max_sagitta (B-rep re-meshed at the export settings) | 0.005 | mm | <= 0.01 | 0.005 | (10.1765, -132.8296, -27.4400) mm | PASS | — |
| U-07 stl bodies | 1 | count | == 1 | 0 | — | PASS | — |
| U-07 stl naked_edges | 0 | count | == 0 | 0 | — | PASS | — |
| U-07 stl winding | 1 | bool | == 1 | 0 | — | PASS | — |
| U-07 angular tolerance used | 0.2 | rad | <= 0.2309721947249083 | 0.031 | — | PASS | — |
| U-08 | — |  | N/A | — | — | N/A: no threads on this part (spec section 5 U-08) | — |
| D-07 | — |  | N/A | — | — | N/A: clearance holes only, no fit bores (spec section 5 D-07) | — |
| REQ-09 | — |  | Soft bench: no visible flex | — | — | INCONCLUSIVE: Soft bench gate, not geometric: answered by the first print | A-11 |

## 4. Robustness sweep (D7)

Every run was rebuilt by `build_od_c05_carrier.py --set` and exported, with its assembly and STL, into `01_CAD/sweep_v01/`. `check_od_c05_carrier.py` then checked each run (`check_<run>.json`) with the same gate limits; only the positive-control values follow the run's own radii. There were 20 runs: nominal plus every fit-critical rung of plan §4. Every run built one valid solid and matched the feature census (20 / 16 / 14 / 2 / 14). In every run, D-03a reads the same INCONCLUSIVE (least 45.0000°, 0 samples under 45°) and REQ-09 stays INCONCLUSIVE. The table gives the gate each parameter drives.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 Ø 3.300 / 3.500 (at the ± 0.1 limit); D-04a 3.300 | 0.000 (REQ-01); +0.050 (D-04a) |
| hole_xy (all four together) | 43.95 · 44.00 · 44.05 | yes | U-03a/REQ-01 offset from the OD-G01 insert 0.0707; D-01b 2.679 at 44.05 | +0.029 (REQ-01); +0.679 (D-01b) |
| cb_d | 6.4 · 6.5 · 6.6 | yes | **D-03b exception crown span 6.600 at Ø6.6: FAIL**; D-01b 2.700 at Ø6.6; REQ-02 Ø at the ± 0.1 limit | **−0.100 (D-03b)**; +0.700 (D-01b); 0.000 (REQ-02) |
| cb_depth | 1.9 · 2.0 · 2.1 | yes | REQ-02 depth 1.900 / 2.100 (at the ± 0.1 limit); REQ-03 wall length 5.000 | 0.000 |
| hub_r (one-sided, a floor) | 30.0 · 30.1 | yes | REQ-04 0 rays with material; OD-G04 clearance 5.000; control apex 42.568 | 0 (count); +3.0 |
| low_r (one-sided, a floor) | 25.0 · 25.1 | yes | REQ-08 0 rays with material | 0 (count) |
| foot_t (underside fixed at −175) | 3.9 · 4.0 · 4.1 | yes | REQ-05 thickness 3.900 / 4.100 (at the ± 0.1 limit) | 0.000 |
| foot_z_rear (one-sided) | −69.94 · −69.99 | yes | REQ-07 min_z −69.990; U-02 size_z 45.050 | +0.010 (REQ-07); +0.050 (U-02) |
| foot_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-06 Ø at the ± 0.1 limit; D-04a 3.300 | 0.000 (REQ-06); +0.050 (D-04a) |
| foot_hole_x | 34.95 · 35.00 · 35.05 | yes | REQ-06 offset 0.050 | +0.050 |
| foot_hole_z (both rows together) | −40.05/−60.05 · −40/−60 · −39.95/−59.95 | yes | REQ-06 offset 0.050 | +0.050 |
| z_front | −24.94 only (plan §4: the contact plane) | — | U-03a contact 0.000 at nominal | 0 |

**The part passes every HARD row except D-03a (INCONCLUSIVE) at nominal and at every rung, with one exception.** At cb_d = 6.6, the upper limit of REQ-02's Ø6.5 ± 0.1, the named exception's bridge "≤ 6.5 by construction" (spec §5, D-03b) is exceeded: the crown measures 6.6. The rung is the spec's own tolerance, and the delivered geometry is at nominal Ø6.5. So this is a conflict between two spec values, not a build fault; see §9.

## 5. Build facts

- **Envelope and mass:** 100.000 × 225.000 × 45.000 mm (x ±50.000, y −175.000 … 50.000, z −69.940 … −24.940). Volume 108712.078 mm³; mass 116.32 g at 1070 kg/m³ (ASA, A-12); centre of mass (0.000, −89.075, −31.651).
- **Fillets:** no edge went through `fillet_ladder`. The two top corners are 2D sketch arcs R 6.0 about (±44, 44) (spec 1.1 K-1) and measure as the two convex cylinders R 6.000. Nothing else is rounded; the wall-to-foot root is sharp, as the plan says.
- **Placements:** the joints were checked, not assumed.
  - OD-G01 build v02 sits at the identity (spec §2 frame). Its four insert bores were located on the OD-G01 solid in the check assembly at (±44.0000, ±44.0000), and the carrier holes sit 0.000 from them. Its rear face lies on the carrier's front face: clearance 0.000, interference 0.000 mm³.
  - OD-G04 is rotated +6.05° about Z, then moved z −6.82 (OD-G01 REPORT v02 §5, plan §5). Its clearance to the carrier is 5.000 mm.
  - The check assembly STEP holds `od_c05_carrier` (the re-imported part), `od_g01_housing` and `od_g04_brewing_gasket_support`. The carrier in it matches the part file (volume delta 2.3e-10 mm³).
- **Export:**
  - STEP: AP242 through `tools.core.write_step`, header timestamp pinned to 2026-09-30T12:00:00.
  - STL: through `tools.core.write_stl` from the re-imported STEP, with the cached triangulation cleared. Tolerance 0.01 mm, angular 0.20 rad, 4264 triangles, max sagitta 0.00498 mm, STL volume 108716.928 mm³ (for the orchestrator's 3MF check).

## 6. Plausibility (§P, D6)

Sections, each with `nothing_clipped` 0: x = 0, x = 35, x = 44, x = 48, y = 44, y = −110, z = −27.44, and the assembly at x = 0.

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | Yes. The foot underside is the OD-C01 floor plane y −175, held down by four M3 screws. The wall stands up from the foot and the housing hangs on the wall's front face. The carrier's centre of mass (z −31.65) lies over the foot (z −69.94 … −24.94). |
| P2 | Function chains | Yes. The Ø60 hub window lies behind the housing's Ø26 hub opening and the OD-G04 hub tube (5.0 clear) and leaves room for the water connection (A-06). The lower window at (0, −110) is the TUBE 7 route and the tool access (A-07). The screws run from behind the wall into the housing inserts. |
| P3 | Motion | Yes; nothing on this part moves. The portafilter turns in front of the housing (z > 0), and nothing of the carrier lies in front of z −24.94. |
| P4 | Human factors | Yes. The four housing screws are driven from behind through the Ø6.5 counterbores, reached through the lower window and the back panel (A-14). The foot screws go in vertically from above the foot top. |
| P5 | Absurdity | Nothing absurd seen. A 5 mm printed wall with two gussets carrying a group head of about 100 g is in proportion with the sheet-metal brackets of small espresso machines. The 225 height follows from the 175 axis height (A-03). |
| P6 | Floating, embedded, mirrored, upside-down | None. It is one solid, with interference 0 against both neighbours. The counterbores open on the rear face z −29.94, away from the housing. The window gables point up (+Y), the print direction. |

## 7. Library and tools used

- **Cards:** none (plan §2: nothing in `library/INDEX.md` matched).
- **Tools:**
  - `tools.core`: `write_step`, `read_step`, `compare_step`, `validity`, `write_stl`, `mesh_sagitta`.
  - `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall` (with `detail["wide"]`), `overhang_census`, `radial_extent`, `clearance`, `interference`, `mesh_census`, `mass_properties`.
  - `tools.drawing`: `write_sections`, with its `nothing_clipped` check.
  - `tools.result.gate` makes every comparison.
- **New code, in the job only (none in the repo):**
  - `exception_face` in the check selects the eight named-exception faces by position: a cylinder with its axis along Z, within 0.2 of (±44, ±44), radius 1.5 … 3.5.
  - `solid_of` builds a solid from the part's faces less those eight (orientation kept), so `overhang_census` reads the rest.
  - `sweep_od_c05_carrier.py` drives the sweep; `sections_od_c05_carrier.py` writes the sections.
- **Missing tool (D-03a):**
  - `overhang_census` cannot settle a curved face whose least angle lies on its boundary at exactly `min_deg`. Its refinement always leaves a residual bound between 0.005° and 0.01°. By design, a least within that bound above 45° is INCONCLUSIVE, whatever the spacing (measured at 0.5 and at 0.1 mm).
  - The two window arcs are tangent to their 45° gables, so they meet exactly 45.000° along the tangent lines.
  - D-03a can only close once some tool reads the least angle exactly on a face's boundary edges, or on an analytic cylinder whose axis is square to the build direction. No local predicate stands in for the gate.

## 8. Deviations from the plan

1. **Spec 1.1 amendments**, built as the brief lists them:
   - y_floor −175.0: the wall runs y −175.0 … +50.0 and the foot y −175.0 … −171.0.
   - Gussets on the wall from y −171.0 to −131.0 and on the foot from z −29.94 to −69.94.
   - Top corners R 6.0 about (±44, 44) (K-1 option 2).
   - Lower window R 25.0 about (0, −110.0), apex −74.645; its probes and its section moved to y −110.
   - U-02 and envelope_within_spec at 100 × 225 × 45, y −175 … +50; D-02 225 tall.
   - D-03a with the named exception excluded by position (K-2 option 1).
   - The census's two convex cylinders are now R 6.
2. **D-03b** also gets a measured value: the census finds no sample under 45° outside the exception, so there is no bridge there. The reviewer's reading from the sections, as the plan names, still applies.
3. **U-04:** the check re-reads the delivered STEP (schema, one solid, label, valid, and volume and face count against a second re-import). The built-versus-file comparison (`compare_step` on the built shape) runs at export and is kept in the build log. The plan named `step_roundtrip`, which writes the file itself.
4. **U-07:** `mesh_sagitta` is read on the re-imported part, meshed again at the export settings. It gives the same value `write_stl` returned (0.00498 mm). The 3MF is not written here (brief).
5. **E-06:** a measured corroboration is added to the reviewer's check: the two gusset inner faces at x ±46 on the one solid.
6. **Sections:** planes x = 44 (the Z holes and counterbores in profile) and z = −27.44 (the wall mid-plane) are added. The lower-window plane is y = −110 (spec 1.1).
7. **Feature census:** the plan's counts were predictions, and the build matches them exactly (20 planar, 16 cylindrical, 14 concave, 2 convex, 14 bores).

## 9. What I am least sure of

1. **D-03a stays INCONCLUSIVE.**
   - Everything the tool can read says 45.000°: the planar gables read exactly 45.0000°, the arcs 45.00000027° at the least, and no sample is under 45°.
   - But the tool cannot settle a curved face tangent at exactly the limit (§7).
   - The geometry cannot move off 45° without changing the gable apexes, which are spec values.
   - The reviewer and the orchestrator need to decide how this row is closed: a tool extension, or a reading from the sections.
2. **D-03b at the REQ-02 tolerance.**
   - The named exception says the crowns are "≤ 6.5 by construction". REQ-02 allows the counterbore Ø6.5 ± 0.1.
   - At Ø6.6 the crown bridge is 6.6, which fails the exception's limit by 0.1.
   - The nominal part passes (6.500, margin 0.000). As built and swept, it passes D-03b only at Ø ≤ 6.5.
   - This needs a spec answer: either the exception reads ≤ 6.6, or REQ-02 becomes Ø6.5 +0 / −0.1.
3. **The face-exclusion helper, and printing.**
   - `solid_of` puts the faces other than the eight exception faces on an open shell inside a solid. The census uses only face orientation and vertex heights, and the bed read −175.0 with 18731 bed samples, the same as in the exception run. Still, the tool was not written for an open shell, and the reviewer should confirm the exclusion with their own method.
   - Separately, REQ-09 (Soft): a 225 tall, 5 mm ASA wall may warp on the bed or flex under the locking torque.

## 10. Stop

Not stopped. No HARD row reads FAIL on the delivered (nominal) geometry. D-03a is INCONCLUSIVE because a tool capability is missing (§7), not because of a measured failure. The Ø6.6 sweep rung fails the D-03b exception limit, which is a spec-value conflict (§9, item 2).

Fix cycles used: 0 of 3. The geometry was exported once. After that, only the check script's logic changed (the D-03b value and the D-03a diagnostics), and every check result in this REPORT comes from the final check script.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c05-group-head-carrier",
 "part": "od_c05_carrier",
 "tag": "v01",
 "spec_version": "1.1",
 "files": [
  {
   "path": "01_CAD/build_od_c05_carrier.py",
   "sha256": "b3b0e94005cd76ed4838f55d018ef12e15b9c3d4618fa793c659ac7f5e87d116"
  },
  {
   "path": "01_CAD/check_od_c05_carrier.py",
   "sha256": "fb421a41acd836988eaf2d5f1fbce8eaa6c053b7d8197aea7b9d905b48dd03e5"
  },
  {
   "path": "01_CAD/sections_od_c05_carrier.py",
   "sha256": "bafeca772ffe8a5ccd67cf2696a49639d6b5ee34045203f8b2d6f5657c26a8d0"
  },
  {
   "path": "01_CAD/sweep_od_c05_carrier.py",
   "sha256": "62caaf0ceb90bd7f10e3f36eba666d94721d56fc923742797bf002a336918171"
  },
  {
   "path": "02_STEP_STL/od_c05_carrier_C1_v01.step",
   "sha256": "3555600be58771b0efba7b2f2b5a48439bb442db58d5b5eb92fdd6a6fe410362"
  },
  {
   "path": "02_STEP_STL/od_c05_assembly_C1_v01.step",
   "sha256": "b6fdbea9466703e81d63938840ce82853cddcac9c4f537d7e5d721f55817e1c3"
  },
  {
   "path": "02_STEP_STL/od_c05_carrier_C1_v01.stl",
   "sha256": "aee6d05a1573742d131cb949e86b98acceb6fca179dc2cd46394a4918c8fe48a"
  },
  {
   "path": "01_CAD/check_od_c05_carrier_v01.json",
   "sha256": "1c57b36c81835e0774266f800d9c3d333f0e66638e2d4bbcbf7ca2105866e03d"
  },
  {
   "path": "01_CAD/build_od_c05_carrier_v01.json",
   "sha256": "d3457f40ea3fcf9a7d10e3ae7f1ca808c85d1f6dabbeb4a2917994211bd75102"
  },
  {
   "path": "01_CAD/sections_od_c05_carrier_v01.json",
   "sha256": "298b88918bd3cc23b4e1d8a25083b5d7591753fa30ca7d2a21fcd9f9d2c7f8bc"
  },
  {
   "path": "01_CAD/sweep_v01/SHA256SUMS_v01.txt",
   "sha256": "2cbc6e99df38bb23293aa1e11ff4d629748c4a97060ac7eea4453f29fb1805ca"
  },
  {
   "path": "03_Sections/od_c05_assembly_x0_v01_left.png",
   "sha256": "45c952415736c7a6bdad835d995b0f4f21af525050efb8a02efac15f14e57ecf"
  },
  {
   "path": "03_Sections/od_c05_carrier_x0_v01_left.png",
   "sha256": "ff005505cf4bffe0b1fe8002cbaea64f9961c2a69184a484a0d6a1e25b9a13dd"
  },
  {
   "path": "03_Sections/od_c05_carrier_x35_v01_left.png",
   "sha256": "edf5390642a14c4dd97241fd525ae097c3ad1305768cdb093727a3c0eab477c8"
  },
  {
   "path": "03_Sections/od_c05_carrier_x44_v01_left.png",
   "sha256": "7972feb30a6f1a93646deca2bfe23305cc489a611111c9b6e3650f34375062d7"
  },
  {
   "path": "03_Sections/od_c05_carrier_x48_v01_left.png",
   "sha256": "7d95e4c21d402ead81af662b28df7eea4e04ca042f7f0061b88683c8584e762c"
  },
  {
   "path": "03_Sections/od_c05_carrier_y44_v01_front.png",
   "sha256": "400b0fbacba5c85ebc25ca1aecfeaa2fa5ee024be96bbc49e77ea8eb8fefdbfe"
  },
  {
   "path": "03_Sections/od_c05_carrier_ym110_v01_front.png",
   "sha256": "537c6d019dd9ff66a5758ad7a169dd3a47c903e395f3bf67883901129cd82dec"
  },
  {
   "path": "03_Sections/od_c05_carrier_zm27p44_v01_top.png",
   "sha256": "49e475ca672c694dab36d477b1545de225eb4103a352b13575cf50d62f827d83"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "cadquery-ocp-novtk 7.9.3.1.1",
  "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"
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
   "gate": "U-01 solid_count",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01 brep_valid",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01 naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02 size_x",
   "measured": 100.0000000000012,
   "unit": "mm",
   "required": "in [99.9, 100.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02 size_y",
   "measured": 225.0,
   "unit": "mm",
   "required": "in [224.9, 225.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02 size_z",
   "measured": 45.000000000000014,
   "unit": "mm",
   "required": "in [44.9, 45.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec min_x",
   "measured": -50.000000000001194,
   "unit": "mm",
   "required": "in [-50.1, -49.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec max_x",
   "measured": 50.0,
   "unit": "mm",
   "required": "in [49.9, 50.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec min_y",
   "measured": -175.0,
   "unit": "mm",
   "required": "in [-175.1, -174.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec max_y",
   "measured": 50.0,
   "unit": "mm",
   "required": "in [49.9, 50.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec min_z",
   "measured": -69.94000000000001,
   "unit": "mm",
   "required": "in [-70.03999999999999, -69.84]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec max_z",
   "measured": -24.939999999999998,
   "unit": "mm",
   "required": "in [-25.040000000000003, -24.84]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02 bed x",
   "measured": 100.0000000000012,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 120.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "D-02 bed z",
   "measured": 45.000000000000014,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 175.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "D-02 height y",
   "measured": 225.0,
   "unit": "mm",
   "required": "<= 250.0",
   "margin": 25.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "REQ-03 front face z",
   "measured": -24.939999999999998,
   "unit": "mm",
   "required": "in [-25.040000000000003, -24.84]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-05 underside y",
   "measured": -175.0,
   "unit": "mm",
   "required": "in [-175.1, -174.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-04"
   ]
  },
  {
   "gate": "REQ-07 min_z",
   "measured": -69.94000000000001,
   "unit": "mm",
   "required": ">= -70.0",
   "margin": 0.06,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "U-04 schema",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04 solids",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04 volume_delta",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04 faces_delta",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04 valid_after",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04 name od_c05_carrier",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census plane_faces",
   "measured": 20,
   "unit": "count",
   "required": "== 20",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census cylinder_faces",
   "measured": 16,
   "unit": "count",
   "required": "== 16",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census cone_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census sphere_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census torus_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census bspline_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census other_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census concave_cylinders",
   "measured": 14,
   "unit": "count",
   "required": "== 14",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census convex_cylinders",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census bores",
   "measured": 14,
   "unit": "count",
   "required": "== 14",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05/REQ-01 hole (+44,+44) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a hole Z (+44,+44)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(44.0000, 44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01 hole (+44,+44) offset from nominal",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01 hole (+44,+44) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(44.0000, 44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03a/REQ-01 hole (+44,+44) offset from OD-G01 insert",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-02 cb (+44,+44) dia",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (+44,+44) depth",
   "measured": 2.0,
   "unit": "mm",
   "required": "in [1.9, 2.1]",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (+44,+44) coaxial",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-03 rear face z (cb (+44,+44) open end)",
   "measured": -29.94,
   "unit": "mm",
   "required": "in [-30.040000000000003, -29.84]",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03 wall through (+44,+44) (hole + cb length)",
   "measured": 5.0,
   "unit": "mm",
   "required": "in [4.9, 5.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-01 hole (-44,+44) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a hole Z (-44,+44)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(-44.0000, 44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01 hole (-44,+44) offset from nominal",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01 hole (-44,+44) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-44.0000, 44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03a/REQ-01 hole (-44,+44) offset from OD-G01 insert",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-02 cb (-44,+44) dia",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (-44,+44) depth",
   "measured": 2.0,
   "unit": "mm",
   "required": "in [1.9, 2.1]",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (-44,+44) coaxial",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-03 rear face z (cb (-44,+44) open end)",
   "measured": -29.94,
   "unit": "mm",
   "required": "in [-30.040000000000003, -29.84]",
   "margin": 0.1,
   "at": "(-44.0000, 44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03 wall through (-44,+44) (hole + cb length)",
   "measured": 5.0,
   "unit": "mm",
   "required": "in [4.9, 5.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-01 hole (+44,-44) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a hole Z (+44,-44)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(44.0000, -44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01 hole (+44,-44) offset from nominal",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01 hole (+44,-44) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(44.0000, -44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03a/REQ-01 hole (+44,-44) offset from OD-G01 insert",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-02 cb (+44,-44) dia",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (+44,-44) depth",
   "measured": 2.0,
   "unit": "mm",
   "required": "in [1.9, 2.1]",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (+44,-44) coaxial",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-03 rear face z (cb (+44,-44) open end)",
   "measured": -29.94,
   "unit": "mm",
   "required": "in [-30.040000000000003, -29.84]",
   "margin": 0.1,
   "at": "(44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03 wall through (+44,-44) (hole + cb length)",
   "measured": 5.0,
   "unit": "mm",
   "required": "in [4.9, 5.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-01 hole (-44,-44) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a hole Z (-44,-44)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(-44.0000, -44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01 hole (-44,-44) offset from nominal",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01 hole (-44,-44) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-44.0000, -44.0000, -27.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03a/REQ-01 hole (-44,-44) offset from OD-G01 insert",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -27.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-02 cb (-44,-44) dia",
   "measured": 6.5,
   "unit": "mm",
   "required": "in [6.4, 6.6]",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (-44,-44) depth",
   "measured": 2.0,
   "unit": "mm",
   "required": "in [1.9, 2.1]",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-02 cb (-44,-44) coaxial",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-03 rear face z (cb (-44,-44) open end)",
   "measured": -29.94,
   "unit": "mm",
   "required": "in [-30.040000000000003, -29.84]",
   "margin": 0.1,
   "at": "(-44.0000, -44.0000, -29.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-03 wall through (-44,-44) (hole + cb length)",
   "measured": 5.0,
   "unit": "mm",
   "required": "in [4.9, 5.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-05/REQ-06 foot hole (+35, z -40) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(35.0000, -175.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "D-04a foot hole (+35, z -40)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(35.0000, -175.0000, -40.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06 foot hole (+35, z -40) offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(35.0000, -175.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06 foot hole (+35, z -40) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(35.0000, -175.0000, -40.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05 foot thickness at (+35, z -40)",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(35.0000, -175.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-04"
   ]
  },
  {
   "gate": "U-05/REQ-06 foot hole (-35, z -40) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(-35.0000, -175.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "D-04a foot hole (-35, z -40)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(-35.0000, -175.0000, -40.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06 foot hole (-35, z -40) offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-35.0000, -175.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06 foot hole (-35, z -40) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-35.0000, -175.0000, -40.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05 foot thickness at (-35, z -40)",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(-35.0000, -175.0000, -40.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-04"
   ]
  },
  {
   "gate": "U-05/REQ-06 foot hole (+35, z -60) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(35.0000, -175.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "D-04a foot hole (+35, z -60)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(35.0000, -175.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06 foot hole (+35, z -60) offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(35.0000, -175.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06 foot hole (+35, z -60) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(35.0000, -175.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05 foot thickness at (+35, z -60)",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(35.0000, -175.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-04"
   ]
  },
  {
   "gate": "U-05/REQ-06 foot hole (-35, z -60) dia",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(-35.0000, -175.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "D-04a foot hole (-35, z -60)",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(-35.0000, -175.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06 foot hole (-35, z -60) offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(-35.0000, -175.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-06 foot hole (-35, z -60) through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-35.0000, -175.0000, -60.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05 foot thickness at (-35, z -60)",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(-35.0000, -175.0000, -60.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-04"
   ]
  },
  {
   "gate": "D-01a min_wall",
   "measured": 2.749999989747004,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 1.94999999,
   "at": "(50.0000, 44.0059, -28.3610) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b min_wall",
   "measured": 2.749999989747004,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 0.74999999,
   "at": "(50.0000, 44.0059, -28.3610) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-06a min feature",
   "measured": 2.749999989747004,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 1.74999999,
   "at": "(50.0000, 44.0059, -28.3610) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06 (Soft) min_wall wide",
   "measured": 2.749999989747004,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 0.74999999,
   "at": "(50.0000, 44.0059, -28.3610) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03a overhang outside the named exception",
   "measured": null,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": null,
   "at": "(17.6777, -92.3223, -24.9400) mm",
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "D-03a exception faces counted (8 expected)",
   "measured": 8,
   "unit": "count",
   "required": ">= 8",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03b bridge span outside the named exception",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": 5.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03b named exception crown span",
   "measured": 6.5,
   "unit": "mm",
   "required": "<= 6.5",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-04 rays with material r<=30 (108 rays)",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-04 control theta 90 apex",
   "measured": 42.426406871192,
   "unit": "mm",
   "required": "== 42.42640687119285",
   "margin": -8.526512829121202e-13,
   "at": "(0.0000, 42.4264, -27.4400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-04 control theta 0",
   "measured": 29.999999999999996,
   "unit": "mm",
   "required": "== 30.0",
   "margin": -3.552713678800501e-15,
   "at": "(30.0000, 0.0000, -27.4400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-08 rays with material r<=25 (108 rays)",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-08 control theta 90 apex",
   "measured": 35.35533905933001,
   "unit": "mm",
   "required": "== 35.35533905932738",
   "margin": -2.6290081223123707e-12,
   "at": "(0.0000, -74.6447, -27.4400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-08 control theta 270",
   "measured": 24.999999999999982,
   "unit": "mm",
   "required": "== 25.0",
   "margin": -1.7763568394002505e-14,
   "at": "(-0.0000, -135.0000, -27.4400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "E-06 gusset inner faces (one solid)",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03a carrier|OD-G01 contact clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(-50.0000, -42.0000, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03a carrier|OD-G01 interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03a carrier|OD-G04 clearance",
   "measured": 5.0000000000000036,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 3.0,
   "at": "(21.2132, 21.2132, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "U-03a carrier|OD-G04 interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "U-03 assembly carrier equals part file",
   "measured": 2.3283064365386963e-10,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": -2.3283064365386963e-10,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03b",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "U-07 stl_max_sagitta (B-rep re-meshed at the export settings)",
   "measured": 0.0049837223672576205,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.005016278,
   "at": "(10.1765, -132.8296, -27.4400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07 stl bodies",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07 stl naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07 stl winding",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07 angular tolerance used",
   "measured": 0.2,
   "unit": "rad",
   "required": "<= 0.2309721947249083",
   "margin": 0.030972195,
   "at": null,
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
   "gate": "REQ-09",
   "measured": null,
   "unit": "",
   "required": "Soft bench: no visible flex",
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
   "parameter": "hole_d",
   "values": [
    3.3,
    3.4,
    3.5
   ],
   "all_built": true,
   "worst_gate": "REQ-01 diameter at the ±0.1 limit",
   "worst_margin": 0.0
  },
  {
   "parameter": "hole_xy",
   "values": [
    43.95,
    44.0,
    44.05
   ],
   "all_built": true,
   "worst_gate": "U-03a/REQ-01 offset from the OD-G01 insert 0.0707",
   "worst_margin": 0.029289
  },
  {
   "parameter": "cb_d",
   "values": [
    6.4,
    6.5,
    6.6
   ],
   "all_built": true,
   "worst_gate": "D-03b named exception crown span 6.6 (FAIL at 6.6)",
   "worst_margin": -0.1
  },
  {
   "parameter": "cb_depth",
   "values": [
    1.9,
    2.0,
    2.1
   ],
   "all_built": true,
   "worst_gate": "REQ-02 depth at the ±0.1 limit",
   "worst_margin": 0.0
  },
  {
   "parameter": "hub_r",
   "values": [
    30.0,
    30.1
   ],
   "all_built": true,
   "worst_gate": "REQ-04 rays with material 0",
   "worst_margin": 0.0
  },
  {
   "parameter": "low_r",
   "values": [
    25.0,
    25.1
   ],
   "all_built": true,
   "worst_gate": "REQ-08 rays with material 0",
   "worst_margin": 0.0
  },
  {
   "parameter": "foot_t",
   "values": [
    3.9,
    4.0,
    4.1
   ],
   "all_built": true,
   "worst_gate": "REQ-05 thickness at the ±0.1 limit",
   "worst_margin": 0.0
  },
  {
   "parameter": "foot_z_rear",
   "values": [
    -69.94,
    -69.99
   ],
   "all_built": true,
   "worst_gate": "REQ-07 min_z -69.99",
   "worst_margin": 0.01
  },
  {
   "parameter": "foot_hole_d",
   "values": [
    3.3,
    3.4,
    3.5
   ],
   "all_built": true,
   "worst_gate": "REQ-06 diameter at the ±0.1 limit",
   "worst_margin": 0.0
  },
  {
   "parameter": "foot_hole_x",
   "values": [
    34.95,
    35.0,
    35.05
   ],
   "all_built": true,
   "worst_gate": "REQ-06 offset 0.05",
   "worst_margin": 0.05
  },
  {
   "parameter": "foot_hole_z",
   "values": [
    [
     -40.05,
     -60.05
    ],
    [
     -40.0,
     -60.0
    ],
    [
     -39.95,
     -59.95
    ]
   ],
   "all_built": true,
   "worst_gate": "REQ-06 offset 0.05",
   "worst_margin": 0.05
  }
 ],
 "least_sure": [
  "D-03a INCONCLUSIVE: overhang_census cannot settle the window arcs tangent at exactly 45 deg (least 45.0000, bound 0.009, 0 samples under 45)",
  "D-03b named exception (<= 6.5) fails at the REQ-02 upper tolerance cb_d 6.6 (crown 6.6); nominal passes with margin 0",
  "the face-exclusion helper solid_of (open shell) used to run overhang_census without the eight exception faces; REQ-09 warp and flex risk"
 ],
 "stopped": false
}
```
