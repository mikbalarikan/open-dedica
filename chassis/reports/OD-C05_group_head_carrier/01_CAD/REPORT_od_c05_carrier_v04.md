# REPORT — od_c05_carrier v04 (20260930-od-c05-group-head-carrier)

Designer: Claude Code, Opus 5.5 · spec version 2.2 · plan `01_CAD/DESIGN_PLAN_v02.md` with the WP-06 and WP-07 amendments · brief WP-07 (J3, fix_cycles 3) · 2026-09-30 UTC

**Outcome: SUBMITTED.** Every §5 row passes on the exported STEP, and in every one of the 23 sweep runs. The exceptions are REQ-09, a Soft bench gate that reads INCONCLUSIVE by its row, and U-08 and D-07, which are N/A by their rows. Spec 2.2 turns the foot's roof and the rear window's gable to point toward +Z. In the print (plate on the bed, build +Z) the roof's ridge (y −78.0, z +174.06) and the window's apex (z +150.0) are now the highest lines of their features. D-03a reads 45.000° outside the named exception, and D-03b reads no bridge: 0 flat downward faces and 0 valley edges. The same finders, run on the v03 STEP as a control, still find its 102.000 valley and its 20.000 flat.

`01_CAD/check_od_c05_carrier_v04.py` measures every number below from the re-imported STEP files (`01_CAD/check_od_c05_carrier_v04.json`). The only exceptions are rows that say they come from the build log (`01_CAD/build_od_c05_carrier_v04.json`). These self-checks clear no HARD gate; only the reviewer's measurement does.

The input hashes match the brief (WP-07 → WP-03): OD-G01 f8865cd1…4407b02, OD-G04 19b4a140…98d6ad2, and the v02 plan c580be8d…4cba6bf. The spec `00_Spec/DESIGN_SPEC.md` was read at 3accd3b0…3377bd (version 2.2). Every v01, v02 and v03 file is untouched. The v03 STEP is read, never written, by the D-03b control.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c05_carrier_v04.py` | 63862f771efe937647a6b961dcc37146662eb5cd21ec316b9270ed629434e341 | parametric script (Algebra mode, one Params structure), from v03 with the roof and window changed |
| `01_CAD/check_od_c05_carrier_v04.py` | 7283e59de8a223ed5ed578e9547d758bd51a720cc9a66d2d698ebc091894f5eb | checks, written before the build (D3) |
| `01_CAD/sections_od_c05_carrier_v04.py` | 642f67e5503c1707fdd1d361021b623ab960e69b79fe255f2b5591d35b0ea8e7 | D6 sections from the exported STEP files |
| `01_CAD/sweep_od_c05_carrier_v04.py` | 6423567310a5167e4a3179ae50762c6ae985763e034f7e9148efb62db759142f | D7 sweep driver |
| `01_CAD/sweep_summary_v04.py` | 5af9ef4a91bc3596919ba8f9339d21645924dcc6c6803eb2fc0b4b680b8d1adc | sweep summary and SHA256SUMS writer |
| `02_STEP_STL/od_c05_carrier_C4_v04.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | AP242 (`tools.core.write_step`), label `od_c05_carrier`, re-imported for every measurement |
| `02_STEP_STL/od_c05_assembly_C4_v04.step` | 70390d91f1aa6ff710208065366aa3598675796fd76e782113f842cb59cd1a77 | AP242 check assembly: carrier + OD-G01 (identity) + OD-G04 (+6.05° about Z, then z −6.82) |
| `02_STEP_STL/od_c05_carrier_C4_v04.stl` | 7ecc4de80bd2b69533b534d660a74e9f3d25e6f14c0f954f93392913605eea2b | binary STL written from the re-imported STEP with the cached triangulation cleared; tol 0.01 mm / angular 0.20 rad; 5232 triangles; volume 414605.350 mm³; bbox (−55.0, −102.0, −29.94) … (55.0, 50.0, 180.06) |
| `01_CAD/check_od_c05_carrier_v04.json` | 1ac98922997de08a8e8e091a4a25e7c60ae4027607b3b9c62d455480e67a9cd2 | check results: every gate row, plus the facts (downward faces, peaks, roof, window, D-03b control) |
| `01_CAD/build_od_c05_carrier_v04.json` | 69b57eae4df14bd02a0304a3e2fba05ccdf7bca2f25b4ed5ed841f8ab66e9305 | build log: parameters, derived values, export round trip, STL writer detail |
| `01_CAD/sections_od_c05_carrier_v04.json` | 14e458b76b293399eba666f9a31af492f62203139a3b109e6d1312b513e04b9e | section log: plane, point, nothing_clipped |
| `01_CAD/sweep_v04/SHA256SUMS_v04.txt` | 6f9cd4abecb42b6f814d641a4fa63cbf7d5e59a6313b5f2f948b3a42d8917533 | SHA-256 of every other sweep file |
| `01_CAD/sweep_v04/summary_v04.json` | 5dfed2547113a8f451e599ebe392d37ccaf459dee48e95c278b3d7156ff15bbe | per run: one solid, rows not passing, worst margin per gate |
| `03_Sections/od_c05_carrier_y0_v04_front.png` | f5552864272d7f34b61fcac837579274d104e2f7e442c121a7a7ed230c64bf17 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_ym80_v04_front.png` | e3740700304349f4be0dfbcf20a62f885135b188a48ed7841a10141d54c9dd58 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x0_v04_left.png` | 903fe49d7fc2203c6a4651494e820b246d74eb28f6b7c338a762873bdcc7c3a1 | section through the rear window's gable and the roof's ridge, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x35_v04_left.png` | 30678270d27ed691fb8ee5e9dd15310a625c41d7d2a8ed9acd6dd7f98d8c46f0 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x53_v04_left.png` | b488b7150c4393ae341f980278b5888c24c35aa20101b8b85afa7f8f47c309f7 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_ym100_v04_front.png` | 1b78bca5d37f8e5081c08b7a94eedc719cb26883f5e90c56b3de28ea4ffea8a8 | section through the rear wall, showing the window's pointed arch (added), nothing_clipped 0 |
| `03_Sections/od_c05_carrier_zm27p44_v04_top.png` | 1fcc9436a60d3f14205e980d7ed5d025fbe3c0d77c0667050f0c9d809ee66b3c | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_z165_v04_top.png` | 06837f88f50a34f09375c73c3f864eacd4daf25eaa6341a378e27e9a0f7bd4d5 | section, nothing_clipped 0 |
| `03_Sections/od_c05_assembly_y0_v04_front.png` | eb9f08ce9cc6b29882e96be22ff353afa8bcf6bb8cf4f6f996a5c9272beaa535 | section, nothing_clipped 0 |
| `03_Sections/od_c05_assembly_x0_v04_left.png` | 475e12a2a6a556d925960dd2cf7041f5d7ed3e4545aebcb649c511acc443b058 | section, nothing_clipped 0 |

The section images draw +Z upward on the page. That is the print orientation (the bed at the bottom of the page, the plate on it), which shows the machine upside down.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · OCCT 7.9.3 · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (tools used unmodified)

## 3. Gate self-check

The band is from GATES.md §0: 0.005 mm, 0.001°, 0.001 mm³, and 0 for counts and 1/0 facts. U-07's angular tolerance uses 0.00002 rad. Every limit comes from spec 2.2 §5 only. Margins are signed and positive inside the limit, so a pass inside the band shows its small negative margin.

**U-05 census, recounted for spec 2.2 before the build (brief), then measured.** The roof keeps two planar faces that now meet at a ridge instead of a valley. The rear window keeps five planar faces: the bottom z +110 (now flat and facing up in the print), two sides, and two gable flats (now above the rectangle). The foot counterbores cut the roof faces without crossing the ridge: the y −72 pair lies on the front face (y −78 … −58) and the y −92 pair on the rear face (y −98 … −78). No face is split or added, so the count equals v03's:
- 36 planar faces: plate top z −29.94 (1); plate underside z −24.94, in front of the column and inside it (2); plate front edge y +50 (1); side faces x ±55 (2); rear face y −102 (1); foot underside z +180.06 (1); front wall front face y −52 (1); front wall rear face y −58 (1); rear wall inner face y −98 (1); side wall inner faces x ±51 (2); roof faces (2); hatch flats (4); rear window bottom, two sides and two gable flats (5); gusset inner faces x ±51 (2); gusset hypotenuses (2); counterbore floors, 4 on the plate at z −27.94 and 4 in the foot at z +176.06 (8).
- 21 cylindrical faces, all concave: 4 Ø3.4 plate holes, 4 Ø6.5 plate counterbores, 4 Ø3.4 foot holes, 4 Ø6.5 foot counterbores, the R 30 hub window (one full face), and the 4 R 4 hatch corners.
- 17 bores (the 16 along Z and the hub window). The 4 hatch corners are 90° concave arcs, not bores.
- No cone, sphere, torus, B-spline or other face. Measured: 36 / 21 / 21 concave / 0 convex / 17 bores, as predicted.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | whole part | PASS | — |
| U-02 | 110.000 × 152.000 × 210.000 mm | each ± 0.1 | +0.100 each | — | PASS | — |
| envelope_within_spec | x −55.000 … 55.000, y −102.000 … 50.000, z −29.940 … 180.060 | x ±55.0, y −102.0 … +50.0, z −29.94 … +180.06, each ± 0.1 | +0.100 each | — | PASS | — |
| U-03 (a) carrier\|OD-G01 | contact clearance 0.000 mm; interference 0.000 mm³; four hole axes 0.000 from the insert bore axes (inserts located at (±44.000, ±44.000)) | contact = 0; ≤ 0 mm³; ≤ 0.10 | 0; 0; +0.100 | contact at (−42.0, 50.0, −24.94); OD-G01 validity 1/1/0 | PASS (assumed: A-01) | A-01 |
| U-03 (a) carrier\|OD-G04 | clearance 5.000 mm; interference 0.000 mm³ | ≥ 2.0; ≤ 0 | +3.000; 0 | carrier (30.0, 0.0, −24.94), OD-G04 (30.0, 0.0, −19.94); OD-G04 validity 1/1/0 | PASS (assumed: A-06) | A-06 |
| U-03 (b) | — | N/A by its row (no motion variable) | — | — | N/A | — |
| U-04 | schema AP242, 1 solid, volume delta 0.000 mm³, faces delta 0, valid after 1, label `od_c05_carrier` | re-read unchanged, no stray shells, valid | 0 | — | PASS | — |
| U-05 / feature_census | 36 planar, 21 cylindrical (21 concave, 0 convex), 17 bores, no other kind; the 16 bores along Z located one by one | predicted above: 36 / 21 / 21 / 0 / 17 | 0 | REQ rows below | PASS | — |
| U-06 (Soft) | 2.750 mm | ≥ 2.0 | +0.750 | (−44.0, 50.0, −29.94), plate counterbore to the plate's front edge | PASS | — |
| U-07 | sagitta 0.00499 mm (the B-rep re-meshed at the export settings); STL 1 body, 0 naked edges, winding 1; angular 0.20 rad | tol 0.01, angular ≤ 0.2310 rad, sagitta ≤ 0.01 | +0.00501 | (−38.245, −92.007, 160.053) | PASS | — |
| U-08 | — | threaded parts only | — | — | N/A: no threads, by its row | — |
| D-01a | 2.750 mm | ≥ 0.8 | +1.950 | (−44.0, 50.0, −29.94) | PASS | — |
| D-01b | 2.750 mm | ≥ 2.0 | +0.750 | same | PASS | — |
| D-02 | 110.0 × 152.0 on the bed, 210.0 tall | ≤ 220 × 220, ≤ 250 | +110.0, +68.0, +40.0 | plate top z −29.94 on the bed | PASS (assumed: A-08) | A-08 |
| D-03a | 45.000° outside the named exception (`overhang_census(build_dir=(0,0,1))`: 24772 downward samples, 0 below 45°, sampling bound 0.000°). Analytic listing: 4 faces at 45.000000000°, namely the two roof faces (normals (0, ±1, −1)/√2) and the two window gable flats (normals (±1, 0, −1)/√2); no other downward face outside the exception | ≥ 45° | 0.000 (inside the band) | census least at (−10.0, −98.0, 140.0), a gable flat's lower corner | PASS (assumed: A-13) | A-13 |
| D-03b | 0.000 mm outside the named exception: 0 flat downward faces and 0 valley edges. Two peak edges, reported apart: the roof ridge, 102.000 long at (0, −78.0, 174.06), and the window apex, 4.000 long at (0, −100.0, 150.0). Both are highest lines, closed from both sides, not bridges | ≤ 5 | +5.000 | — | PASS | — |
| D-03b finder control (job code) | on the v03 STEP: valley 102.000 at (0, −80.0, 154.06); flat carried span 20.000 at (0, −100.0, 160.0) | must read 102.0 and 20.0 | 0; 0 | v03 file, read only | PASS (the finders can fail) | — |
| D-03a / D-03b named exception | 8 counterbore floors found by position (4 at z −27.94 on (±44, ±44), 4 at z +176.06 on (±35, −72 / −92)); least angle 0.000° (flat rings, 1.55 wide, 24.104 mm² each); counterbore bridged Ø6.500 | reported apart; span ≤ 6.6 | +0.100 (span) | as listed | inside the named exception | A-13 |
| D-04a | 3.400 mm (all eight) | ≥ 3.25 | +0.150 | (±44, ±44); (±35, −72 / −92) | PASS | — |
| D-06a | 2.750 mm | ≥ 1.0 | +1.750 | (−44.0, 50.0, −29.94) | PASS | — |
| D-07 | — | fit bores only | — | — | N/A: clearance holes only, by its row | — |
| E-06 | two front gussets, each 3200.000 mm³ (40 × 40 / 2 × 4), inner faces at \|x\| 51; the plate's rear part is the column's lid; one solid | plate tied to the column, no free boss | 0 | x ±(51 … 55), y −52 … −12, z −24.94 … 15.06 | PASS | — |
| REQ-01 | Ø3.400, through, 3.000 long, offset 0.000 from nominal and from the OD-G01 inserts | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-01) | A-01 |
| REQ-02 | Ø6.500 × 2.000 deep, open at z −29.940, coaxial 0.000 | Ø6.5 ± 0.1, 2.0 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-09) | A-09 |
| REQ-03 | top z −29.940 (min_z and the four counterbore open ends); underside z −24.940 (counterbore start + 2.000 + 3.000) | ± 0.10 | +0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-04 | innermost material on the whole ray 30.000 mm over 36 angles × 5 levels (180 rays); θ 0°, 90°, 270° each 30.000 (round) | ≥ 30.0 at every 10° | −3.6e-15 (inside the band) | least at θ 10°, (29.5442, 5.2094, −29.9) | PASS (assumed: A-06) | A-06 |
| REQ-05 | underside z 180.060 (max_z); 4.000 of foot under each head (each foot hole's length, z 176.06 … 180.06); counterbore floors z 176.060 | ± 0.10; 4.0 ± 0.1; 176.06 ± 0.10 | +0.100 | (±35, −72 / −92) | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-06 | holes Ø3.400 through, offset 0.000; counterbores Ø6.500, coaxial 0.000, floors z 176.060, open in the roof face (depth at the axis 8.000 at y −72 and 16.000 at y −92, from the roof plane measured on the B-rep, as §4 states) | Ø3.4 ± 0.1, ≤ 0.10; Ø6.5 ± 0.1; 176.06 ± 0.10 | +0.100 | (±35, −72), (±35, −92) | PASS (assumed: A-04) | A-04 |
| REQ-07 | min_y −102.000 | ≥ −102.0 | 0.000 | plate, column and foot rear face | PASS (assumed: A-05) | A-05 |
| REQ-08 | housing to the front gussets 1.000 mm; housing to the front wall 2.000 mm (the plate contact is reported under U-03) | ≥ 1.0; ≥ 2.0 | 0.000; 0.000 | housing (−50.0, −42.0, −24.94) to gusset face x −51; housing (−42.0, −50.0, −24.94) to wall face y −52 | PASS (assumed: A-01) | A-01 |
| REQ-09 (Soft) | — | no visible flex (bench) | — | — | INCONCLUSIVE (Soft bench gate, answered by the first print; risk MEDIUM, §9) | A-11 |

REQ-08 method: the carrier, re-imported from the STEP, is cut by position below the contact plane (z > −24.94) into the front piece (y > −52: the two gussets, 6400.000 mm³) and the column piece (y < −52, 351841.945 mm³). `clearance` of OD-G01 to each piece is measured with the nearest points.

§4 geometry read from the B-rep (reported only; §5 gives no row or tolerance for it):
- Roof: 2 faces, each at 45.000000000°, meeting the walls at z 154.060 (front and rear) and each other at the ridge (0, −78.0, 174.06), 102.000 long. §4 gives ridge y −78.0, z +174.06, and 154.06 at the walls.
- Rear window: bottom z 110.000; 2 gable flats at 45.000000000° from z 140.000 at x ±10.000 up to the apex z 150.000. §4 gives z +110 … +140, apex +150. The apex is 4.06 below the roof's start on the rear wall.

D-03b method (job code, §7): a flat downward face (under 1°) is carried on an edge when a point 0.05 below and 0.05 outside the edge's midpoint lies in the solid. Its span is twice the largest distance from a point of the face to its nearest carried edge. A valley edge is a straight edge between two planar downward faces that both rise away from it along +Z. A peak edge (new in v04) is the same pair of faces with both centres below the edge; it is listed, not gated. The gate and the v03 control call the same finder function.

## 4. Robustness sweep (D7)

23 runs into `01_CAD/sweep_v04/` (the v03 set, unchanged), each built and checked with the same predicates (`01_CAD/sweep_v04/summary_v04.json`). Every run built one valid solid with the predicted census (36 / 21 / 21 / 0 / 17). **No row fails in any run**; REQ-09 is INCONCLUSIVE by its row. In every run D-03a reads 45.000°, D-03b reads 0.000 (no flat, no valley), and U-06 reads ≥ 2.700. The table gives the gate each parameter moves and its worst margin.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 Ø at the tolerance ends; D-04a at 3.3 | 0.000; +0.050 |
| hole_xy | 43.95 · 44.00 · 44.05 (all four together) | yes | REQ-01 offset 0.071 (diagonal, from nominal and from the OD-G01 inserts); D-01b 2.700 at 44.05 | +0.029; +0.700 |
| cb_d | 6.4 · 6.5 · 6.6 | yes | REQ-02 Ø at the tolerance ends; D-03b exception span 6.600 at 6.6; D-01b 2.700 at 6.6 | 0.000; 0.000; +0.700 |
| cb_depth | 1.9 · 2.0 · 2.1 | yes | REQ-02 depth at the tolerance ends; REQ-03 underside −24.940 | 0.000; +0.100 |
| hub_r | 30.0 · 30.1 (one-sided) | yes | REQ-04 innermost 30.100; OD-G04 clearance 5.000 | +0.100; +3.000 |
| wall_y_front | −52.0 · −52.1 (one-sided) | yes | REQ-08 housing to front wall 2.100 | +0.100 |
| foot_t | 3.9 · 4.0 · 4.1 (underside fixed at +180.06) | yes | REQ-05 foot under the head at the tolerance ends; foot counterbore floors 176.16 / 175.96 (depth at the axis 8.1 / 16.1 and 7.9 / 15.9) | 0.000; 0.000 |
| y_rear | −102.0 · −101.9 (one-sided) | yes | U-02 size_y 151.900; REQ-07 −101.900; the rear roof face stays at 45.000° and meets the rear wall at z 154.160 | 0.000; +0.100 |
| foot_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-06 Ø at the tolerance ends; D-04a at 3.3 | 0.000; +0.050 |
| foot_cb_d | 6.4 · 6.5 · 6.6 | yes | REQ-06 counterbore Ø at the tolerance ends; D-03b exception span 6.600 | 0.000; 0.000 |
| foot_hole_x | 34.95 · 35.00 · 35.05 | yes | REQ-06 hole offset and counterbore coaxiality 0.050 | +0.050 |
| foot_hole_y | −72/−92 ± 0.05 together | yes | REQ-06 hole offset and counterbore coaxiality 0.050 | +0.050 |
| gusset_x_in | 51.0 · 51.1 (one-sided) | yes | REQ-08 housing to gussets 1.100; E-06 volume 3120.000, as derived for 3.9 thick | +0.100; 0.000 |

REQ-07 and REQ-08 sit at margin 0.000 at nominal by construction, because the spec puts those values at the limit. The one-sided rungs show that each moves in the safe direction.

The v03 U-06 finding at `y_rear_hi` (0.027) is gone: U-06 reads 2.750 at that rung. §7 explains why.

## 5. Build facts

- Envelope 110.000 × 152.000 × 210.000 mm; volume 414599.036 mm³; mass 443.62 g at 1070 kg/m³ (§3, A-12); centre of mass (0.000, −66.679, 75.901).
- Fillets: none through a ladder. The four hatch corners are sketch arcs R 4.000, measured as four concave cylinders R 4.000; the plate's corners are square.
- Derived values (build log, from the parameters): ridge z 174.06 = floor 180.06 − ridge_t 6.0; the roof at the front wall's rear face y −58 and at the rear wall's inner face y −98 is z 154.06; the roof at the foot hole axes is z 168.06 (y −72) and 160.06 (y −92); the counterbore depth at the axis is 8.0 and 16.0; the window apex is z 150.0. The build asserts that the ridge is above both wall lines and below the counterbore floors, and that the window apex is below the roof's start on the rear wall.
- Foot counterbore faces as `locate_bore` reads them: from z 164.732 to 176.06 at y −72 (11.328 along the axis, to the rim's lowest point on the wall side) and from z 156.810 to 176.06 at y −92 (19.250). The analytic rim lowest point at y −72 is 164.81; the 0.08 difference is the reading of the elliptical rim edge's extent and gates nothing (REQ-06 reads the floor).
- Placements: OD-G01 at the identity, checked by `locate_bore` (inserts (±44.000, ±44.000), hole offsets 0.000) and by the contact at z −24.94 (clearance 0.000, interference 0.000). OD-G04 is rotated +6.05° about Z, then translated z −6.82 (OD-G01 REPORT v02 §5), unchanged; clearance 5.000 from the window's edge at r 30.
- STL for the orchestrator's 3MF: 5232 triangles, volume 414605.350 mm³ (STL) against 414599.036 mm³ (B-rep), bounding box (−55.0, −102.0, −29.94) … (55.0, 50.0, 180.06); tol 0.01 mm, angular 0.20 rad, written from the re-imported STEP.
- Fix cycles: 1 of 3, a check-script correction only. On the first check run, the new D-03b finder control read the v03 flat as 60.670 instead of 20.000: my new helper lacked the main loop's "under 1°" filter and counted v03's 45° tent faces. I moved the gate and the control onto one shared finder function and re-ran the check on the same STEP. There was no geometry change and no re-export: every number in this REPORT comes from the one D5 export.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | Yes in the machine: with −Z up, the plate lies on the housing's rear face and the housing hangs under it, axis vertical and mouth down; the column stands behind it on the foot, on the floor z +180.06 (sections x 0 and assembly x 0). Yes in the print: the bed is at the bottom of each section, the roof is a pointed vault whose ridge is its highest line, and the window's point is at its top (sections x 0, x 35, y −100). |
| P2 | Function chains | Yes: the round window (innermost r 30.000) clears the housing's openings and OD-G04 (5.000); the four holes are coaxial with the inserts (0.000); TUBE 7 can enter through the rear window (z +110 … +150, machine y 30 … 70), rise in the column and leave through the hatch into the hub window from above (A-07); the foot screws are reached through the hatch (A-14). |
| P3 | Motion clearance | Yes: the carrier does not move. The front gussets stand at \|x\| ≥ 51 and y ≤ −12, behind the axis and clear of the portafilter handle, which locks toward the front (handle not modelled: this is a reading of the geometry). |
| P4 | Human factors | Yes, with a long driver: the housing screws are driven from above into the plate's counterbores. The foot screws are driven through the hatch (80 × 32) and down Ø6.5 counterbores 8.0 / 16.0 deep in the roof to floors at z +176.06, 206.0 below the plate's top face, against A-14's driver reach of about 200. The hatch (x ±40, y −96 … −64) clears the four foot screw axes. |
| P5 | Absurdity | None seen: a closed tower behind the group head carrying a flat plate, with a solid foot 26 thick at the walls and 6 at the centre line. In the machine the inside of the foot is a V-trough (lowest line at y −78). See §9 item 1 on drips. |
| P6 | Floating, embedded, mirrored, upside down | One solid, with interference 0 against both neighbours. Nothing is upside down for the print any more (v03 K-6 and K-7 closed): the roof and the window gable both point +Z, the print's up. |

## 7. Library and tools used

- Cards: none (nothing matched in `library/INDEX.md`, as at v01 … v03).
- `tools.core`: `validity`, `write_step` (AP242), `read_step`, `compare_step`, `write_stl`, `mesh_sagitta`, `common_volume`. `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `interference`, `min_wall` (with `detail["wide"]`), `overhang_census(build_dir=(0,0,1))`, `radial_extent` (whole ray, inner), `mesh_census`, `mass_properties`; `tools.measure.sampling.Inside` (point-in-solid probes); `tools.measure.wall.load_mesh` (STL bbox, triangles and volume, reported only). `tools.drawing.write_sections`. `tools.result.gate`.
- Job code in the check script (not the repo): the analytic downward-face list for D-03a (from v02); for D-03b, the carried-edge span of flat downward faces and the valley-edge finder (from v03), plus, new in v04, the peak-edge listing, the sloped-plane reader for the roof and gable, and the v03 finder control. No `tools/measure` function measures bridge spans; D-03b's check column says "reviewer, from sections", and sections x 0, x 35 and y −100 show the roof and the window.
- **U-06 note (brief, v03 §4 finding):** v03's knife edge came from the counterbores cutting the tent's faces vertically. At v04 each foot counterbore's rim still meets the roof face in a 45° wedge, but now on its ridge side (y −75.25 for the y −72 pair, 2.75 from the ridge; y −88.75 for the y −92 pair, 10.75 from the ridge). The wall-side rims are now obtuse (135°). The rear rim of the y −92 counterbores is at y −95.25, 2.75 from the rear wall's inner face y −98, not the 4.0 the brief states. Its lowest point is at z 156.810 on the B-rep, which fits 154.06 + 2.75. v04 builds the roof at 45° from the ridge, not through fixed wall points, so no swept parameter changes the wedge angle: the rear face meets the wall at z 154.160 at y_rear −101.9 instead of steepening. `min_wall`'s wide reading (opposition 45°) therefore reads 2.700 … 2.800 in all 23 runs. The wedges still sit exactly on that reading's 45° opposition (§9 item 2).

## 8. Deviations from the plan

Plan `DESIGN_PLAN_v02.md`, amended by WP-06 (spec 2.1, deviations 1 … 9 of the v03 REPORT §8, all carried) and by WP-07 (spec 2.2):
10. Foot roof in place of the tent: the parameters `ridge_y` −78.0 (was −80.0), `ridge_t` 6.0 (new; ridge z = 174.06) and `roof_slope` 1.0 (45°, new). Both faces are built from the ridge down to the walls at 45°, which gives 154.06 at y −58 and y −98 at nominal. This is my derivation of the §4 wording: it keeps both faces at exactly 45° when y_rear is swept.
11. Foot counterbores: the cylinder starts 1.0 below the roof's lowest line, in the column's air, and ends at the floor z +176.06 (was: from the tent's ridge). The spec depths 8.0 and 16.0 at the axis are measured.
12. Rear window: `win_z_lo` 110.0, `win_z_hi` 140.0, gable toward +Z with apex `win_z_hi` + `win_half_x` = 150.0 (was z +130 … +160, apex +120 toward −Z).
13. Sections: the WP-06 set plus y = −100 (the window's pointed arch in elevation). The x = 0 section is the one through the window's gable and the roof's ridge. The y = −80 section now passes 2.0 behind the ridge.
14. Check script: the peak-edge listing, the roof and window readings, the foot counterbore depth at the axis, and the D-03b finder control on the v03 STEP were added; the census was recounted and is unchanged.

## 9. What I am least sure of

1. **Drips in the foot's V-trough (P5, no gate).** In the machine (−Z up) the inside of the foot is a trough whose lowest line is the ridge (z +174.06). The four foot counterbores open on its slopes, with floors at z +176.06, lower still. Water or steam condensate entering through the hatch or the rear window (§3: drips possible) runs down the roof into the counterbores and pools on the screw heads. There is no drain hole, and the screws may wick it into OD-C01. The spec does not ask for a drain. I added none, because it would be a new feature, and I flag it for the Usta.
2. **The 45° wedges at the foot counterbore rims (U-06, Soft).** The four ridge-side rims meet the roof in a wedge of exactly 45°, which `min_wall`'s wide reading does not count (opposition 45°). A roof built a hair steeper than 45° would read it as a near-zero wall. The v04 roof is fixed at 45° from the ridge, so no swept parameter moves it, but the reviewer's own re-meshing or sampling could land on either side. In the print it is a feathered lip on the counterbore's rim: harmless to the screw. The margins exact by construction are unchanged: REQ-07 and REQ-08 at 0.000. FDM growth of +0.1 to +0.2 takes the 1.0 gusset gap to about 0.8 to 0.9.
3. **REQ-09, risk MEDIUM (unchanged from v03 §9 item 2).** The closed column is about 120 times stiffer than the v02 wall (6.5e-4 rad against 0.08 rad under 50 N at the axis; torsion 1.9e-3 rad under 10 N·m, A-11). The compliant part is the 5.0 plate cantilevering 96 to the front screws. The heavier foot (26 at the walls) adds stiffness only at the floor. The mass rises 0.44 g against v03 (443.62 g).

## 10. Stop

Not stopped.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20260930-od-c05-group-head-carrier",
  "part": "od_c05_carrier",
  "tag": "v04",
  "spec_version": "2.2",
  "files": [
    {
      "path": "01_CAD/build_od_c05_carrier_v04.py",
      "sha256": "63862f771efe937647a6b961dcc37146662eb5cd21ec316b9270ed629434e341"
    },
    {
      "path": "01_CAD/check_od_c05_carrier_v04.py",
      "sha256": "7283e59de8a223ed5ed578e9547d758bd51a720cc9a66d2d698ebc091894f5eb"
    },
    {
      "path": "01_CAD/sections_od_c05_carrier_v04.py",
      "sha256": "642f67e5503c1707fdd1d361021b623ab960e69b79fe255f2b5591d35b0ea8e7"
    },
    {
      "path": "01_CAD/sweep_od_c05_carrier_v04.py",
      "sha256": "6423567310a5167e4a3179ae50762c6ae985763e034f7e9148efb62db759142f"
    },
    {
      "path": "01_CAD/sweep_summary_v04.py",
      "sha256": "5af9ef4a91bc3596919ba8f9339d21645924dcc6c6803eb2fc0b4b680b8d1adc"
    },
    {
      "path": "02_STEP_STL/od_c05_carrier_C4_v04.step",
      "sha256": "7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1"
    },
    {
      "path": "02_STEP_STL/od_c05_assembly_C4_v04.step",
      "sha256": "70390d91f1aa6ff710208065366aa3598675796fd76e782113f842cb59cd1a77"
    },
    {
      "path": "02_STEP_STL/od_c05_carrier_C4_v04.stl",
      "sha256": "7ecc4de80bd2b69533b534d660a74e9f3d25e6f14c0f954f93392913605eea2b"
    },
    {
      "path": "01_CAD/check_od_c05_carrier_v04.json",
      "sha256": "1ac98922997de08a8e8e091a4a25e7c60ae4027607b3b9c62d455480e67a9cd2"
    },
    {
      "path": "01_CAD/build_od_c05_carrier_v04.json",
      "sha256": "69b57eae4df14bd02a0304a3e2fba05ccdf7bca2f25b4ed5ed841f8ab66e9305"
    },
    {
      "path": "01_CAD/sections_od_c05_carrier_v04.json",
      "sha256": "14e458b76b293399eba666f9a31af492f62203139a3b109e6d1312b513e04b9e"
    },
    {
      "path": "01_CAD/sweep_v04/SHA256SUMS_v04.txt",
      "sha256": "6f9cd4abecb42b6f814d641a4fa63cbf7d5e59a6313b5f2f948b3a42d8917533"
    },
    {
      "path": "01_CAD/sweep_v04/summary_v04.json",
      "sha256": "5dfed2547113a8f451e599ebe392d37ccaf459dee48e95c278b3d7156ff15bbe"
    },
    {
      "path": "03_Sections/od_c05_carrier_y0_v04_front.png",
      "sha256": "f5552864272d7f34b61fcac837579274d104e2f7e442c121a7a7ed230c64bf17"
    },
    {
      "path": "03_Sections/od_c05_carrier_ym80_v04_front.png",
      "sha256": "e3740700304349f4be0dfbcf20a62f885135b188a48ed7841a10141d54c9dd58"
    },
    {
      "path": "03_Sections/od_c05_carrier_x0_v04_left.png",
      "sha256": "903fe49d7fc2203c6a4651494e820b246d74eb28f6b7c338a762873bdcc7c3a1"
    },
    {
      "path": "03_Sections/od_c05_carrier_x35_v04_left.png",
      "sha256": "30678270d27ed691fb8ee5e9dd15310a625c41d7d2a8ed9acd6dd7f98d8c46f0"
    },
    {
      "path": "03_Sections/od_c05_carrier_x53_v04_left.png",
      "sha256": "b488b7150c4393ae341f980278b5888c24c35aa20101b8b85afa7f8f47c309f7"
    },
    {
      "path": "03_Sections/od_c05_carrier_ym100_v04_front.png",
      "sha256": "1b78bca5d37f8e5081c08b7a94eedc719cb26883f5e90c56b3de28ea4ffea8a8"
    },
    {
      "path": "03_Sections/od_c05_carrier_zm27p44_v04_top.png",
      "sha256": "1fcc9436a60d3f14205e980d7ed5d025fbe3c0d77c0667050f0c9d809ee66b3c"
    },
    {
      "path": "03_Sections/od_c05_carrier_z165_v04_top.png",
      "sha256": "06837f88f50a34f09375c73c3f864eacd4daf25eaa6341a378e27e9a0f7bd4d5"
    },
    {
      "path": "03_Sections/od_c05_assembly_y0_v04_front.png",
      "sha256": "eb9f08ce9cc6b29882e96be22ff353afa8bcf6bb8cf4f6f996a5c9272beaa535"
    },
    {
      "path": "03_Sections/od_c05_assembly_x0_v04_left.png",
      "sha256": "475e12a2a6a556d925960dd2cf7041f5d7ed3e4545aebcb649c511acc443b058"
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
      "margin": 0,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "U-01",
      "measured": "1/1/0",
      "unit": "count/bool/count",
      "required": "1/1/0",
      "margin": 0,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "U-02",
      "measured": "110.000 x 152.000 x 210.000",
      "unit": "mm",
      "required": "each +-0.1",
      "margin": 0.1,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "envelope_within_spec",
      "measured": "x -55..55, y -102..50, z -29.94..180.06",
      "unit": "mm",
      "required": "each +-0.1",
      "margin": 0.1,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "U-03 carrier|OD-G01",
      "measured": "contact 0.000; interference 0.000; offsets 0.000",
      "unit": "mm / mm3",
      "required": "= 0; <= 0; <= 0.10",
      "margin": 0.0,
      "at": "(-42.0, 50.0, -24.94)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-01"
      ]
    },
    {
      "gate": "U-03 carrier|OD-G04",
      "measured": 5.0,
      "unit": "mm",
      "required": ">= 2.0; interference <= 0",
      "margin": 3.0,
      "at": "(30.0, 0.0, -24.94)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-06"
      ]
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
      "gate": "U-04",
      "measured": "volume delta 0.000, faces delta 0, valid 1, label kept",
      "unit": "mm3 / count",
      "required": "unchanged",
      "margin": 0,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "U-05",
      "measured": "36 planar, 21 cyl (21/0), 17 bores; 16 bores along Z located",
      "unit": "count",
      "required": "predicted 36/21/21/0/17",
      "margin": 0,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "feature_census",
      "measured": "36/21/21/0/17",
      "unit": "count",
      "required": "36/21/21/0/17",
      "margin": 0,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "U-06",
      "measured": 2.75,
      "unit": "mm",
      "required": ">= 2.0 (Soft)",
      "margin": 0.75,
      "at": "(-44.0, 50.0, -29.94)",
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "U-07",
      "measured": 0.00499,
      "unit": "mm",
      "required": "<= 0.01; angular 0.20 <= 0.2310",
      "margin": 0.00501,
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
      "gate": "D-01a",
      "measured": 2.75,
      "unit": "mm",
      "required": ">= 0.8",
      "margin": 1.95,
      "at": "(-44.0, 50.0, -29.94)",
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "D-01b",
      "measured": 2.75,
      "unit": "mm",
      "required": ">= 2.0",
      "margin": 0.75,
      "at": "(-44.0, 50.0, -29.94)",
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "D-02",
      "measured": "110.0 x 152.0 on the bed, 210.0 tall",
      "unit": "mm",
      "required": "<= 220 x 220, <= 250",
      "margin": 40.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-08"
      ]
    },
    {
      "gate": "D-03a",
      "measured": 45.0,
      "unit": "deg",
      "required": ">= 45 (build +Z, eight counterbore floors excepted)",
      "margin": 0.0,
      "at": "(-10.0, -98.0, 140.0)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-13"
      ]
    },
    {
      "gate": "D-03b",
      "measured": 0.0,
      "unit": "mm",
      "required": "<= 5 (counterbore floors <= 6.6 excepted: 6.500)",
      "margin": 5.0,
      "at": "no flat, no valley; peaks: ridge (0,-78,174.06) 102.0, window apex (0,-100,150) 4.0",
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "D-04a",
      "measured": 3.4,
      "unit": "mm",
      "required": ">= 3.25",
      "margin": 0.15,
      "at": "all eight holes",
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "D-06a",
      "measured": 2.75,
      "unit": "mm",
      "required": ">= 1.0",
      "margin": 1.75,
      "at": "(-44.0, 50.0, -29.94)",
      "status": "PASS",
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
      "measured": "2 front gussets x 3200.000; plate is the column lid; one solid",
      "unit": "mm3",
      "required": "tied, no free boss",
      "margin": 0,
      "at": null,
      "status": "PASS",
      "assumes": []
    },
    {
      "gate": "REQ-01",
      "measured": "3.400, offset 0.000",
      "unit": "mm",
      "required": "3.4 +-0.1, <= 0.10",
      "margin": 0.1,
      "at": "(+-44, +-44)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-01"
      ]
    },
    {
      "gate": "REQ-02",
      "measured": "6.500 x 2.000, coaxial 0.000",
      "unit": "mm",
      "required": "6.5 +-0.1, 2.0 +-0.1",
      "margin": 0.1,
      "at": "(+-44, +-44)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-09"
      ]
    },
    {
      "gate": "REQ-03",
      "measured": "top -29.940, underside -24.940",
      "unit": "mm",
      "required": "+-0.10",
      "margin": 0.1,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-01"
      ]
    },
    {
      "gate": "REQ-04",
      "measured": 30.0,
      "unit": "mm",
      "required": ">= 30.0 every 10 deg, round",
      "margin": 0.0,
      "at": "(29.5442, 5.2094, -29.9)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-06"
      ]
    },
    {
      "gate": "REQ-05",
      "measured": "180.060; 4.000 under each head; cb floors 176.060",
      "unit": "mm",
      "required": "+-0.10; 4.0 +-0.1; 176.06 +-0.10",
      "margin": 0.1,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-03",
        "A-04"
      ]
    },
    {
      "gate": "REQ-06",
      "measured": "holes 3.400 offset 0.000; cb 6.500 coaxial 0.000, floors 176.060; depth at axis 8.000 / 16.000",
      "unit": "mm",
      "required": "3.4 +-0.1, <= 0.10; 6.5 +-0.1; 176.06 +-0.10",
      "margin": 0.1,
      "at": "(+-35, -72 / -92)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-04"
      ]
    },
    {
      "gate": "REQ-07",
      "measured": -102.0,
      "unit": "mm",
      "required": ">= -102.0",
      "margin": 0.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-05"
      ]
    },
    {
      "gate": "REQ-08",
      "measured": "gussets 1.000; front wall 2.000",
      "unit": "mm",
      "required": ">= 1.0; >= 2.0",
      "margin": 0.0,
      "at": "(-50.0, -42.0, -24.94); (-42.0, -50.0, -24.94)",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-01"
      ]
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
      "worst_gate": "REQ-01 diameter",
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
      "worst_gate": "REQ-01 offset",
      "worst_margin": 0.029
    },
    {
      "parameter": "cb_d",
      "values": [
        6.4,
        6.5,
        6.6
      ],
      "all_built": true,
      "worst_gate": "REQ-02 diameter; D-03b exception span",
      "worst_margin": 0.0
    },
    {
      "parameter": "cb_depth",
      "values": [
        1.9,
        2.0,
        2.1
      ],
      "all_built": true,
      "worst_gate": "REQ-02 depth",
      "worst_margin": 0.0
    },
    {
      "parameter": "hub_r",
      "values": [
        30.0,
        30.1
      ],
      "all_built": true,
      "worst_gate": "REQ-04",
      "worst_margin": 0.0
    },
    {
      "parameter": "wall_y_front",
      "values": [
        -52.0,
        -52.1
      ],
      "all_built": true,
      "worst_gate": "REQ-08 front wall",
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
      "worst_gate": "REQ-05 thickness; foot counterbore floor z",
      "worst_margin": 0.0
    },
    {
      "parameter": "y_rear",
      "values": [
        -102.0,
        -101.9
      ],
      "all_built": true,
      "worst_gate": "U-02 size_y; REQ-07",
      "worst_margin": 0.0
    },
    {
      "parameter": "foot_hole_d",
      "values": [
        3.3,
        3.4,
        3.5
      ],
      "all_built": true,
      "worst_gate": "REQ-06 diameter",
      "worst_margin": 0.0
    },
    {
      "parameter": "foot_cb_d",
      "values": [
        6.4,
        6.5,
        6.6
      ],
      "all_built": true,
      "worst_gate": "REQ-06 counterbore diameter; D-03b exception span",
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
      "worst_gate": "REQ-06 offset",
      "worst_margin": 0.05
    },
    {
      "parameter": "foot_hole_y",
      "values": [
        -0.05,
        0.0,
        0.05
      ],
      "all_built": true,
      "worst_gate": "REQ-06 offset",
      "worst_margin": 0.05
    },
    {
      "parameter": "gusset_x_in",
      "values": [
        51.0,
        51.1
      ],
      "all_built": true,
      "worst_gate": "REQ-08 gussets",
      "worst_margin": 0.0
    }
  ],
  "fix_cycles_used": 1,
  "least_sure": [
    "Drips: in the machine the foot's inside is a V-trough (lowest line y -78) and the four foot counterbores open on its slopes with floors lower still; no drain, none asked by the spec",
    "U-06 (Soft): the ridge-side rims of the foot counterbores meet the roof in exactly 45 deg wedges, on min_wall's wide opposition; 2.700..2.800 in all 23 runs",
    "REQ-09 risk MEDIUM: the 5.0 plate cantilevering 96 to the front screws is the compliant part; closed column 6.5e-4 rad"
  ],
  "stopped": false
}
```
