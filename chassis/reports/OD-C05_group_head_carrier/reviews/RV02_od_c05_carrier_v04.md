# RV02 — od_c05_carrier_v04 (20260930-od-c05-group-head-carrier) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 2.2 · plan `01_CAD/DESIGN_PLAN_v02.md` with the amendments of `briefs/WP-05_designer.md`, `WP-06_designer.md`, `WP-07_designer.md` · report `01_CAD/REPORT_od_c05_carrier_v04.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-03, A-04, A-05, A-06, A-08, A-09, A-13

I re-measured every §5 row from the exported STEP, and the STL and 3MF, with my own scripts in `reviews/RV02_work/` (m1 … m8; my mutants are in `mutants/` and my sections in `sections/`). Comparisons use the GATES §0 band as the plan and REPORT state it: 0.005 mm, 0.001°, 0.001 mm³, and 0 for counts.

- Every Hard row reads PASS or PASS (assumed).
- U-08 and D-07 are N/A by their own rows.
- REQ-09 is the Soft bench gate. It reads INCONCLUSIVE with risk LOW (F1).
- The plausibility list answers YES on all six items.
- Every check family I used FAILs on its mutant.
- Five findings, none blocking. The most important is F2: in the machine, the foot's inside is an undrained trough.

No CAD code was read.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c05_carrier_C4_v04.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | yes |
| `02_STEP_STL/od_c05_assembly_C4_v04.step` | 70390d91f1aa6ff710208065366aa3598675796fd76e782113f842cb59cd1a77 | yes |
| `02_STEP_STL/od_c05_carrier_C4_v04.stl` | 7ecc4de80bd2b69533b534d660a74e9f3d25e6f14c0f954f93392913605eea2b | yes. My own `write_stl` of the STEP at 0.01 mm / 0.20 rad is byte-identical |
| `02_STEP_STL/od_c05_carrier_C4_v04.3mf` | 7fd7f6a12c0d3920f4c28c761c9f22a2e038b28fab69e49ff0a052096b53b6d7 | yes (brief; the orchestrator's file). 5232 triangles, the STL's own set |
| `01_CAD/REPORT_od_c05_carrier_v04.md` | c6fca509698cac42c292c4bd7950f3346b5e78d1eeead09e494c2392261e61c2 | yes (brief) |
| `01_CAD/DESIGN_PLAN_v02.md` | c580be8de01b9060e96b8ed8b64640c34fefa5a7d71c5fb7e319cf4985cba6bf | yes |
| `briefs/WP-05_designer.md` | a063c978322b35727ee18290245023daf8454a1508c2f73784d17b74877d89a8 | yes (brief) |
| `briefs/WP-06_designer.md` | c37d317a9179a587d52d2172317bd420df894b4108848b88e53ed02ec42b0ad2 | yes (brief) |
| `briefs/WP-07_designer.md` | e373fcd3502d6f9da392eb2a21f69bfb24494505d8202c4a90ebf31faf09ff88 | yes (brief) |
| `01_CAD/check_od_c05_carrier_v04.json` | 1ac98922997de08a8e8e091a4a25e7c60ae4027607b3b9c62d455480e67a9cd2 | yes |
| `01_CAD/build_od_c05_carrier_v04.json` | 69b57eae4df14bd02a0304a3e2fba05ccdf7bca2f25b4ed5ed841f8ab66e9305 | yes |
| `01_CAD/sections_od_c05_carrier_v04.json` | 14e458b76b293399eba666f9a31af492f62203139a3b109e6d1312b513e04b9e | yes |
| `01_CAD/sweep_v04/summary_v04.json` | 5dfed2547113a8f451e599ebe392d37ccaf459dee48e95c278b3d7156ff15bbe | yes |
| `03_Sections/od_c05_assembly_x0_v04_left.png` | 475e12a2a6a556d925960dd2cf7041f5d7ed3e4545aebcb649c511acc443b058 | yes |
| `03_Sections/od_c05_assembly_y0_v04_front.png` | eb9f08ce9cc6b29882e96be22ff353afa8bcf6bb8cf4f6f996a5c9272beaa535 | yes |
| `03_Sections/od_c05_carrier_x0_v04_left.png` | 903fe49d7fc2203c6a4651494e820b246d74eb28f6b7c338a762873bdcc7c3a1 | yes |
| `03_Sections/od_c05_carrier_x35_v04_left.png` | 30678270d27ed691fb8ee5e9dd15310a625c41d7d2a8ed9acd6dd7f98d8c46f0 | yes |
| `03_Sections/od_c05_carrier_x53_v04_left.png` | b488b7150c4393ae341f980278b5888c24c35aa20101b8b85afa7f8f47c309f7 | yes |
| `03_Sections/od_c05_carrier_y0_v04_front.png` | f5552864272d7f34b61fcac837579274d104e2f7e442c121a7a7ed230c64bf17 | yes |
| `03_Sections/od_c05_carrier_ym100_v04_front.png` | 1b78bca5d37f8e5081c08b7a94eedc719cb26883f5e90c56b3de28ea4ffea8a8 | yes |
| `03_Sections/od_c05_carrier_ym80_v04_front.png` | e3740700304349f4be0dfbcf20a62f885135b188a48ed7841a10141d54c9dd58 | yes |
| `03_Sections/od_c05_carrier_z165_v04_top.png` | 06837f88f50a34f09375c73c3f864eacd4daf25eaa6341a378e27e9a0f7bd4d5 | yes |
| `03_Sections/od_c05_carrier_zm27p44_v04_top.png` | 1fcc9436a60d3f14205e980d7ed5d025fbe3c0d77c0667050f0c9d809ee66b3c | yes |
| `reviews/RV01_od_c05_carrier_v01.md` | e97b9778da1930dad125cc7e0080d5d270119ac47742e4bc66aedbf0f95ad8c4 | yes (brief) |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | yes (input) |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | yes (input) |

The submission is complete:
- Every §5 row is answered in the REPORT §3.
- Every listed file is present, and its hash matches the brief (and the REPORT where it lists the file).
- The delivery must carry exactly the STEP, STL and 3MF bytes above.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0; 1 shell, 0 free shells, 0 free faces | 1 / 1 / 0 | 0 | whole part | PASS | `validity` | — |
| U-02 | 110.000 × 152.000 × 210.000 mm | each in [spec − 0.1, spec + 0.1] | +0.100 each | x −55.000 … 55.000, y −102.000 … 50.000, z −29.940 … 180.060 (datum as §4) | PASS | `envelope` | — |
| U-03 | (a) carrier\|OD-G01: contact clearance 0.000 mm at the plate underside; interference 0.000 mm³; the four hole axes 0.000 from the insert bore axes. Inserts are Ø4.000 × 5.700 at (±44.000, ±44.000), z −24.94 … −19.24. Housing sides: 1.000 to the gussets, 2.000 to the front wall. Carrier\|OD-G04: clearance 5.000 mm, interference 0.000 mm³; OD-G01\|OD-G04 0.000 mm³. (b) N/A: no motion variable | contact = 0; ≤ 0 mm³; coaxial ≤ 0.10; OD-G04 ≥ 2.0 | 0 (contact, interference); +0.100 (coaxial); +3.000 (OD-G04) | contact (−42.0, 50.0, −24.94); OD-G04 nearest carrier (30.0, 0.0, −24.94) and OD-G04 (30.0, 0.0, −19.94). Path: the housing offered along −Z from 40 mm to the seat reads interference 0 at every step (40, 30, 20, 10, 5, 2, 1, 0.5, 0.1, 0), with side clearance 1.000 all the way. Delivered assembly: carrier and OD-G04 share their full volume with my placement (+6.05° about Z, then z −6.82); the housing has the same volume, centroid and 92 faces as the input at identity | PASS (assumed: A-01, A-06) | `clearance`, `interference` (`common_volume`), `bore_census` + `locate_bore` on both solids | A-01, A-06 |
| U-04 | label `od_c05_carrier`, AP242, unit MM, 1 solid, 1 shell, no stray shell or face. File against its re-read: volume delta 0.000 mm³, faces delta 0, valid 1. My `step_roundtrip` of the re-read body: volume delta 1.4e-9 mm³, faces delta 0, labels 1, valid after 1 | re-read unchanged, no stray shells, valid | +0.001 | — | PASS | `read_step`, `compare_step`, `step_roundtrip` | — |
| U-05 | 36 planar, 21 cylindrical (21 concave, 0 convex), 0 other; 17 bores. The 16 bores along Z were located one by one, plus the Ø60.000 hub window | plan as amended: see §3 | 0 | §3 | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 (Soft) | 2.750 mm (wide, 45°) | ≥ 2.0 | +0.750 | (−44.0, 50.0, −29.94): plate counterbore to the plate's front edge | PASS | `min_wall` `detail["wide"]`, `min_wall_wide` | — |
| U-07 | sagitta 0.004995 mm. Delivered STL: 5232 triangles, 1 body, 0 naked edges, winding 1, volume 414605.350 mm³ (B-rep 414599.036); `mesh_deviation` 0.004946 mm both ways. My re-mesh at 0.01 mm / 0.20 rad is byte-identical. 3MF: unit millimetre, 1 object, 5232 triangles, matched one-to-one with the STL's within 1.4e-6 mm, same winding, volume 414605.353 mm³ | tol 0.01; angular ≤ 4·acos(1 − 0.01/6.0) = 0.23097 rad (0.20 used); sagitta ≤ 0.01; 3MF the same mesh | +0.005005 | sagitta at (−38.245, −92.007, 160.053), foot counterbore rim | PASS | `write_stl`, `mesh_sagitta`, `mesh_census`, `mesh_deviation`, 3MF parse and triangle match | — |
| U-08 | — | threaded parts only | — | — | N/A: no threads, by its row | — | — |
| D-01a | 2.750 mm | ≥ 0.8 | +1.950 | (−44.0, 50.0, −29.94) | PASS | `min_wall` | — |
| D-01b | 2.750 mm | ≥ 2.0 | +0.750 | same | PASS | `min_wall` | — |
| D-02 | 110.0 × 152.0 on the bed, 210.0 tall | ≤ 220 × 220, ≤ 250 | +40.0 (height); +68.0, +110.0 on the bed | plate top z −29.94 on the bed | PASS (assumed: A-08) | `envelope` | A-08 |
| D-03a | 45.000° outside the named exception. `overhang_census(build_dir=(0,0,1))` ran on the part with the eight counterbores plugged back to the plate top and the roof planes (a valid closed solid): MEASURED 45.000, 25544 downward samples, 0 below 45°, sampling bound 0.000°, least on a plane. My analytic listing of every B-rep face gives four downward faces outside the exception, all at 45.000000°: the roof faces with normals (0, ±0.7071, −0.7071) and the window gable flats with normals (±0.7071, 0, −0.7071). Named exception: 8 flat rings at 0.000° (24.104 mm² each), at z −27.94 on (±44, ±44) and z +176.06 on (±35, −72 / −92), found by position. The whole part unplugged reads 0.000° at a plate counterbore floor, which is the exception | ≥ 45°; the eight counterbore floors excepted | 0.000 | census least at (−10.0, −98.0, 140.0), gable flat's lower corner | PASS (assumed: A-13) | `overhang_census` on the plugged part; analytic face listing; sections x 0, x 35, y −100 | A-13 |
| D-03b | Widest bridge 6.500 mm, inside the named exception (the floors bridge the Ø6.500 counterbores). Outside it: 0 flat downward faces and 0 valley edges. Two peak edges: the roof ridge (−51 … 51, −78.0, 174.06), 102.0 long, and the window apex (0, −102 … −98, 150.0). Each is the highest line of its two faces, which rise to it from both sides | ≤ 5; exception ≤ 6.6 | +0.100 (exception); +5.0 outside | counterbores (±44, ±44, −29.94 … −27.94) and (±35, −72 / −92, … 176.06) | PASS | flat-ceiling and valley/peak finder on the analytic listing; sections x 0, x 35, y −100 | — |
| D-04a | 3.400 mm (all eight) | ≥ 3.25 | +0.150 | (±44, ±44); (±35, −72 / −92) | PASS | `locate_bore` | — |
| D-06a | 2.750 mm | ≥ 1.0 | +1.750 | (−44.0, 50.0, −29.94) | PASS | `min_wall` | — |
| D-07 | — | fit bores only | — | — | N/A: clearance holes only, by its row | — | — |
| E-06 | Two gussets at \|x\| 51 … 55, each 3200.000 mm³ (40 × 40 / 2 × 4) inside the one solid. The plate's rear part is the column's lid (section x 0). No free boss | tied to the front wall and the column, no free boss | — | x ±(51 … 55), y −52 … −12, z −24.94 … 15.06 | PASS | `common_volume` with the gusset boxes; `validity`; sections x 0, x 53 | — |
| REQ-01 | Ø3.400 × 3.000, through. Offset 0.000 from nominal (±44, ±44) and 0.000 from the OD-G01 insert axes in the check assembly | Ø3.4 ± 0.1, offset ≤ 0.10 | +0.100 | (±44, ±44, −27.94 … −24.94) | PASS (assumed: A-01) | `bore_census` + `locate_bore` on both solids | A-01 |
| REQ-02 | Ø6.500 × 2.000 deep, open at z −29.940, coaxial 0.000 | Ø6.5 ± 0.1, 2.0 ± 0.1, coaxial | +0.100 | (±44, ±44, −29.94 … −27.94) | PASS (assumed: A-09) | `bore_census`, `locate_bore`; section z −27.44 | A-09 |
| REQ-03 | Top face z −29.940 (envelope min_z; planar face, normal −Z). Underside z −24.940: two planar faces, normal +Z, 8036.25 mm² in front of the column and 1533.74 mm² inside it. Counterbore 2.000 + hole 3.000 = 5.000 | ± 0.10 | +0.100 | — | PASS (assumed: A-01) | `envelope`, face listing, `locate_bore` | A-01 |
| REQ-04 | Innermost material on the whole ray: 30.000 mm at all 180 rays (36 angles × z −29.9, −29.44, −27.44, −25.44, −24.98), every one MEASURED | ≥ 30.0 at every 10° | −3.6e-15 (inside band) | least at θ 10°, (29.5442, 5.2094, −29.9) | PASS (assumed: A-06) | `radial_extent(side="inner")`, whole ray | A-06 |
| REQ-05 | Underside z 180.060 (max_z; planar face, normal +Z). 4.000 of foot under each head (each foot hole z 176.06 … 180.06). Counterbore floors at z 176.060 | ± 0.10; 4.0 ± 0.1; 176.06 ± 0.10 | +0.100 | (±35, −72 / −92) | PASS (assumed: A-03, A-04) | `envelope`, `locate_bore`, face listing | A-03, A-04 |
| REQ-06 | Holes Ø3.400 through, offset 0.000. Counterbores Ø6.500, coaxial 0.000, floors z 176.060, open in the roof face. Rim lowest points (exact ellipse) at z 164.810 (y −72 pair) and 156.810 (y −92 pair); depth at the axis 8.0 / 16.0 | Ø3.4 ± 0.1, offset ≤ 0.10; Ø6.5 ± 0.1; floor 176.06 ± 0.10 | +0.100 | (±35, −72), (±35, −92) | PASS (assumed: A-04) | `bore_census` + `locate_bore`; edge sampling | A-04 |
| REQ-07 | min_y −102.000 | ≥ −102.0 | 0.000 | rear face y −102 (plate, column, foot) | PASS (assumed: A-05) | `envelope` | A-05 |
| REQ-08 | Housing to the gussets 1.000 mm, to the front wall 2.000 mm. The carrier was cut at z ≥ −24.94 into y > −52 (6400.000 mm³) and y < −52 (351841.945 mm³); the plate contact is under U-03 | ≥ 1.0; ≥ 2.0 | 0.000; 0.000 | housing (−50, −42, −24.94) to gusset (−51, −42, −24.94); housing (−42, −50, −24.94) to wall (−42, −52, −24.94) | PASS (assumed: A-01) | `clearance` on the pieces cut by position | A-01 |
| REQ-09 (Soft) | — | no visible flex (bench) | — | column y −102 … −52, plate y −52 … +50 | INCONCLUSIVE (Soft bench gate, answered by the first print; risk LOW, F1) | hand estimate, §7 | A-11 |

**How the analytic listing reads the print.** Plate on the bed, build +Z. Only 13 faces point down (normal·Z < 0):
- the bed face;
- the eight exception rings;
- the two roof planes: z 154.06 at the walls up to 174.06 at the ridge;
- the two gable flats: z 140.0 up to 150.0.

Each pair shares exactly one edge, and that edge is at the pair's largest z. Their horizontal normal components point toward each other, so the edge is a peak (the print's highest line) and not a valley. Every cylinder axis is along Z, so every cylindrical wall is vertical. The hatch, both windows and the hub window have no ceiling.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| Plate with hub window and hatch | z −29.94 … −24.94, x ±55, y −102 … 50, square corners; hub window R 30 round, through; hatch x ±40, y −96 … −64, 4 × R 4 | top −29.940 and underside −24.940; bore Ø60.000 about (0, 0), 360°, through, 5.000 long; 4 concave cylinders R 4.000; hatch open in sections x 0 and x 35 | PASS |
| Column: front wall | y −58 … −52, 6.0, x ±55 | wall face y −52 at 2.000 from the housing; section x 0 | PASS |
| Column: two side walls | \|x\| 51 … 55, 4.0, y −102 … −58 | inner faces x ±51; section z 165; `min_wall` over them ≥ 2.75 | PASS |
| Column: rear wall with rear window and gable | y −102 … −98, 4.0; window x ±10, z 110 … 140, 45° gable to apex z 150 | window bottom z 110.000 (80.0 mm², facing up in the print); two gable flats at 45.000000°, from z 140.0 at x ±10 to the apex z 150.0; section y −100 | PASS |
| Foot with roof | underside z 180.06; roof two 45° faces from z 154.06 at y −58 and y −98 to the ridge (y −78, z 174.06) | two planes at 45.000000°, z 154.06 … 174.06, sharing the ridge (±51, −78, 174.06); underside z 180.060 | PASS |
| Gussets ×2 | 4.0 at \|x\| 51 … 55, legs 40 | 3200.000 mm³ each | PASS |
| Plate holes ×4 + counterbores ×4 | Ø3.4 through and Ø6.5 × 2.0 at (±44, ±44) | 4 × Ø3.400 × 3.000 through; 4 × Ø6.500 × 2.000; offsets 0.000 | PASS |
| Foot holes ×4 + counterbores ×4 | Ø3.4 through at (±35, −72 / −92), Ø6.5 to floors z 176.06 | 4 × Ø3.400 × 4.000 through; 4 × Ø6.500 to z 176.060; offsets 0.000 | PASS |
| Totals (REPORT §3 recount, confirmed) | 36 planar, 21 cylindrical (21 / 0), 17 bores, 1 solid, no other kind | 36 / 21 / 21 / 0 / 17, 1 solid, 57 faces | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | In the machine (−Z up): the plate lies on the housing's rear face and the housing hangs below it, axis vertical, mouth down. The closed column stands behind the housing on the floor plane z 180.06 (my sections x 0 and assembly x 0). In the print (plate on the bed, +Z up): the roof and window are pointed vaults whose ridge and apex are their highest lines | YES |
| P2 | Function chains connected and aimed (air, drive, liquid, cable)? | The four holes are coaxial with the inserts (0.000). The hub window is round at r 30.000, clearing OD-G04 by 5.000 and the housing's rear openings. TUBE 7's route is open all the way: the rear window (20 wide, z 110 … 150), up the column (102 × 40 inside), out of the hatch (80 × 32) and into the hub window from above. The four foot-screw axes lie inside the hatch | YES |
| P3 | Moving parts oriented for their motion, with clearance? | The carrier does not move. The housing seats along −Z with interference 0 over the whole path and 1.000 of side clearance. The gussets sit at \|x\| ≥ 51 and y ≤ −12, at least 52 from the axis, behind the portafilter, whose handle points +Y | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | The housing screws go in from above into the plate counterbores, and the portafilter goes in from below. The foot screws are driven through the hatch, 206.0 from the plate's top face to the counterbore floors; that is at the edge of A-14's ≈ 200 driver (F5) | YES |
| P5 | Next to a comparable real product, does anything look absurd? | Nothing absurd: a flat bracket over the group head on a closed tower behind it, 444 g of ASA. In the machine, though, the foot's inside is an undrained trough under the hatch (F2) | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | One solid, and interference 0 with both neighbours. The roof ridge and window apex point +Z (the print's up), and the counterbores open away from their mating faces | YES |

## 5. Positive controls

My own mutants of this part, cut from the exported STEP (`reviews/RV02_work/m6_controls.py`, `m6b_controls_fix.py`, `mutants/`).

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` (U-01) | one face dropped, open shell: solid_count 0, naked_edges 7 | FAIL |
| `envelope` (U-02, D-02, REQ-03, REQ-05, REQ-07) | rear lip to y −102.5: size_y 152.5, min_y −102.5. Post to z 225.06: size_z 255.0 > 250. Pad under the top: min_z −30.44 | FAIL |
| `compare_step` / `step_roundtrip` (U-04) | counterbore (+44, −44) filled, compared with the delivered file: volume delta 57.287 mm³, faces delta 1 | FAIL |
| `feature_census` (U-05) | counterbore (+44, −44) filled: 20 cylinders, 16 bores | FAIL |
| `bore_census` + `locate_bore` (U-03, U-05, D-04a, REQ-01, REQ-02, REQ-05, REQ-06) | hole and counterbore (+44, +44) moved 0.5: offset 0.500. Foot hole (35, −72) at Ø3.2: 3.200. Foot counterbore (−35, −92) 1.0 deeper: hole 3.000 long, floor z 177.06. Plate counterbore (−44, 44) 2.5 deep: 2.500. Filled counterbore: that position reads Ø3.4 | FAIL |
| `min_wall` with its wide reading (D-01a, D-01b, D-06a, U-06) | +X side wall thinned to 1.5 over 20 × 30: 1.500 at (55.0, −70.28, 50.11), wide 1.500 | FAIL |
| `overhang_census`, plugged part (D-03a) | pointed window through the front wall with 44.0° gables: 44.000 at (0, −52.0, 89.66). Known-good 45.0° twin: 45.000 | FAIL |
| analytic face listing (D-03a) | the same 44.0° window: 44.000000°. Known-good 45.0° twin: 45.000000° | FAIL |
| flat-ceiling and valley finder (D-03b) | flat-topped slot 20 × 20 through the front wall: one flat ceiling, 20.0 × 6.0. V-notched window: a valley edge at (0, −58 … −52, 70). Nominal: 0 flats, 0 valleys, 2 peaks | FAIL |
| `radial_extent`, whole ray, inner (REQ-04) | 4 × 5 bar into the hub window to r 26 at θ 90°: 26.000 | FAIL |
| `clearance` (U-03, REQ-08) | carrier −0.5 along Z: contact 0.500 ≠ 0. Carrier +3.1 along Z: OD-G04 1.900 < 2.0. Gusset bump to x −50.5: 0.500 < 1.0. Front-wall bump to y −51.5 at the flange: 1.500 < 2.0 | FAIL |
| `interference` / `common_volume` (U-03, E-06) | carrier +3.1 along Z: 21900.579 mm³ with OD-G01. Both gussets removed: 0.000 mm³ in each gusset box | FAIL |
| `write_stl` / `mesh_sagitta` (U-07) | the STEP meshed at 0.1 mm / 0.5 rad: 0.0489 | FAIL |
| `mesh_deviation` (U-07) | the same coarse STL: 0.0489 | FAIL |
| `mesh_census` (U-07) | the delivered STL with one triangle dropped: 3 naked edges | FAIL |
| 3MF / STL triangle match (U-07) | coarse STL (2176 triangles) against the 3MF (5232) | FAIL |

Tool notes (no bearing on the gates):
- `min_wall` reports `detail["solids"]` as 4 on this one solid, because the loop reuses the variable `found`.
- `bore_census` puts the start of the y −72 foot counterbores at z 164.732. The exact lowest point of the rim ellipse is 164.810, and the air just below it probes OUT.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | OBSERVATION | — → no visible flex (Soft, bench) | — | column y −102 … −52; plate y −52 … +50 | no | LOW | Soft bench gate, INCONCLUSIVE. Hand estimates are far below visible flex (§7): column torsion 1.8e-3 rad (0.10°) under 10 N·m, 0.2° under 20 N·m; sway ≤ 0.14 mm under a 50 N push at 210; the plate root with gussets deflects ≈ 0.02 mm under 100 N at the axis | Bench the first print (lock the portafilter and push the handle); if the column warms from TUBE 7, re-check with the machine hot (A-12) |
| F2 | P5 (outside the gates; the designer's risk, REPORT §9 item 1) | OBSERVATION | undrained trough → none specified | — | foot interior: lowest line in the machine (−78, 174.06); counterbore floors 176.06 | no | MEDIUM | Water that falls through the hatch can pool on the screw heads, 2 mm below the ridge, and wick into OD-C01. Sources are a leak or condensate at the water connection above the plate, or TUBE 7 inside the column. The V-trough (≈ 41 ml over 102 × 40 × 20) and the four counterbores (≈ 0.27 / 0.53 ml each) have no outlet | A spec change for Oğuz / the Usta: a drain along Z at the ridge line through the 6.0 of foot (it prints as a vertical hole) with a path in OD-C01 to the drip tray, or a cover over the hatch; confirm with the OD-C01 layout |
| F3 | U-06 | OBSERVATION | 2.750 (wide, 45°) → ≥ 2.0 | +0.750 | ridge-side rims of the four foot counterbores, e.g. (−35.10, −75.25, 171.34) | no | LOW | Each rim meets the 45° roof in a 45° feather edge, exactly on the wide reading's opposition limit. At 46° `min_wall` reads 0.032 there. In the print it is a feathered lip above the screw head; the head bears on the floor at z 176.06, so no load rests on it | None required. If wanted, a spec change: a 0.5 flat or chamfer at the rim, or a counterbore started from a local spot face |
| F4 | D-03a, D-03b (named exception) | OBSERVATION | least 0.000°, widest 6.500 → excepted (≤ 6.6) | +0.100 | the eight counterbore floors | no | LOW | The PASS relies on the named exception (U-18). Spec 2.2 records it for the Usta to confirm with §5, and that confirmation is still pending. Rings 1.55 wide over a Ø6.5 counterbore are normal FDM practice | The Usta confirms §5 with the exception |
| F5 | REQ-07, REQ-08 (margins); A-14 (reach) | OBSERVATION | REQ-07 −102.000, REQ-08 1.000 / 2.000 → at the limits; driver reach 206.0 → A-14 ≈ 200 | 0.000 | rear face y −102; gusset and wall faces; foot counterbore floors | no | LOW | The spec sets these at the limit, and the band absorbs float noise only. FDM growth of 0.1–0.2 on the carrier and on the printed housing takes the gusset gap to about 0.6–0.8, still free. The foot-screw heads sit 203–204.4 below the plate's top face, beyond A-14's ≈ 200 driver; 250 mm hex drivers are common | A-14: name a ≥ 210 mm reach driver. Optional spec change: give REQ-08 a print-growth allowance |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1 Drips in the foot's V-trough | Confirmed from the geometry. In the machine the ridge line (−78, 174.06) is the trough bottom, and the four counterbore floors (176.06) lie 2.0 lower, with no outlet. Rated MEDIUM, non-blocking, outside the gates (F2); it needs a spec decision, not a designer fix. |
| 2 45° wedges at the foot counterbore rims (U-06) | Confirmed. The wide reading is 2.750 at the nominal 45°, and at 46° `min_wall` finds a 0.032 feather at (−35.10, −75.25, 171.34). U-06 PASS as the row defines it (F3, LOW). |
| 3 REQ-09, risk MEDIUM | My hand estimate, compared with RV01 F2 and the v02 REPORT §9. Closed column (Bredt): A = 106 × 45 = 4770 mm², ∮ds/t = 106/6 + 106/4 + 2 · 45/4 = 66.7, J = 4A²/∮ = 1.37e6 mm⁴. With G ≈ 0.75 GPa and L ≈ 179 (plate to roof), 10 N·m twists it 1.8e-3 rad (0.10°), against ≈ 0.3 rad for the open 6 × 110 wall of spec 1.x (RV01 F2) and ≈ 5° in v02 §9. Shear flow 0.26 MPa. Bending: I ≈ 2.1e6 mm⁴ across X and ≈ 0.63e6 mm⁴ across Y. A 50 N push at 210 gives 0.04 / 0.14 mm (E ≈ 1.8 GPa), with ≤ 0.4 MPa across the layers. The 96 mm plate cantilever (RV01 F2): the housing is bolted rigidly at the four screws, so the free plate is the 8.0 from the front wall to the rear screws, backed by the gussets (I ≈ 1.5e5 mm⁴ at the wall root): ≈ 0.02 mm under 100 N at the axis. Screw bearing under 20 N·m is ≈ 80 N per screw (≈ 8 MPa on the 3.0 plate). I rate the risk LOW, not MEDIUM (F1); the first print answers it, preferably hot. |

RV01's findings F2 … F5, carried to v04:
- **F2 (REQ-09):** closed. The closed column replaces the open wall; see item 3.
- **F3 (`overhang_census` at exactly 45°):** gone on this part. There are no curved faces at 45°, and the census on the plugged part reads MEASURED 45.000 with sampling bound 0.000.
- **F4 (window check could not fail):** closed. REQ-04 is gated on the whole-ray innermost radius, and its control FAILs at r 26.
- **F5 (R 6 corners outside the housing outline):** gone. The plate's corners are square, 5.0 beyond the housing's sides, appearance only.
