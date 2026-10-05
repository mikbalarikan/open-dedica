<!-- Placed by the orchestrator: a session hook blocked the designer's write of this file; the text below is the designer's returned report, verbatim except for the model name in the Designer line. -->
# REPORT — od_c09_front v01 (20261002-od-c09-front-panel)

Designer: Claude Code (designer subagent) · spec version 1.1 (SHA-256 6aaf9a01…d655f, matches the brief) · plan `01_CAD/DESIGN_PLAN.md` (SHA-256 277daf91…71071, matches the brief) · 2026-10-03 UTC · package WP-03, J3, build attempt 1 of 2, fix cycles 2 of 3

`01_CAD/check_od_c09_front.py` measured every number below on the re-imported STEP `02_STEP_STL/od_c09_front_C1_v01.step`. This was a full run with no cache, saved as `01_CAD/check_od_c09_front_v01.json`. The reference solids were placed by the spec §2 poses. These are self-checks, so none of them clears a HARD gate (PLAYBOOK rule 3). Every input SHA-256 in the brief (the WP-02 table) was checked and matches.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c09_front.py` | 780f573bc0ded727d2449673370124b625fd7b23caf20d069f6e325ba8ad4d57 | parametric script, build123d Algebra mode |
| `01_CAD/check_od_c09_front.py` | 5886cccc39461cf1ca804ab1e97fbeacfd2c1fa8169b060ae4326cf4856007e0 | checks, written before the build (D3); corrections in §8 |
| `01_CAD/sections_od_c09_front.py` | 2b8b4fb1b4e1282fd5fe421a1a82d73a3ebacc1c3b5c621c089f5bdb7744943f | D6 sections |
| `01_CAD/sweep_od_c09_front.py` | 89bbdfbbcf5d8fb5fc0310677640869844bdf3db1cbc0f0678cb04c1fc58679f | D7 sweep driver |
| `01_CAD/report_tables_od_c09_front.py` | 44527962197d307773811ce19f696ace821ed10a7739d714e0bced6cc781ecc7 | builds tables from the JSON; measures nothing |
| `01_CAD/check_od_c09_front_v01.json` | 11ae15209effd70a777e3d8ec9d4a905df1a756de16def2aa55d08665be719fa | every gate row of the gated run |
| `01_CAD/check_od_c09_front_v01.log` | 1d396f12ec1befed3bfd15ce4007f58462707623bd233a99010f0daeec8710c4 | gated run console |
| `01_CAD/od_c09_front_C1_v01.stl_meta.json` | e8e09be5ee8676d0caef475035cb7e97853bd6c962589e3cc4775abcd4bef8d5 | STL tolerances and triangle count |
| `01_CAD/sections_v01.json` | 2d2abef67393b432d712126c6a574712eedfd04a657d8770bc86715d39c42326 | section log; nothing_clipped 0 for all 18 |
| `01_CAD/report_tables_v01.md`, `01_CAD/report_gates_v01.json` | 50c3846f473ba35b378b1e5e3501e8ea32c72e3f297e5a11ae6adb1b8fcd2d1a, 454e5ec0666c1a41af8d4f5665324a792df52cb90786e614f857d26cefb5ab83 | every row, generated |
| `01_CAD/sweep_v01/SHA256SUMS` | 504a1e8310a2a31de739a14d7bb0f74a8d17b40e4240803ad80cef3be5e30585 | hashes of the 33 sweep STEPs, JSONs, logs and the cache |
| `01_CAD/sweep_v01/sweep_summary.json` | d99aa073b84be9eed3783cb47dd2460fd2a380f6770257247f27bc7f677ef0ba | per-run summary |
| `01_CAD/sweep_v01/ref_cache.json` | 618a647c5e16456c3f00f92d94554423d012681155d723e0cd5dc43ba53f4a6f | sweep-only cache of reference-to-reference clearances |
| `01_CAD/sweep_v01_run.log` | b51bdfbb946df43c29779c63bcc864bacf83722dbd9035b1919366bb246b96a5 | sweep console |
| `02_STEP_STL/od_c09_front_C1_v01.step` | 0d688d24b7954e959291b171fa6e464dd30834e3f737eb73b696dfc992148ab5 | AP242 (tools.core.write_step), re-imported for every measurement |
| `02_STEP_STL/od_c09_front_C1_v01.stl` | 086c7c7e4f1c98472b1800dfce3bf73e83ef240311986df454bd2e1a7c740498 | exported after clearing the cached triangulation: tolerance 0.01 mm, angular 0.15 rad, 3932 triangles |
| `02_STEP_STL/od_c09_assembly_C1_v01.step` | e451a3854cb1dd22d29c9ba8871367f3be17341e9e3c06fecdffc3701406984c | check assembly: the panel, OD-C01, OD-C05, OD-G01 housing, OD-G04, OD-G10 locked, OD-C10, OD-E02 |
| `03_Sections/od_c09_front_v01_z95p5.png` | 17413ea95fe15aa055589abad29f8f8074e16e38b65aac6f7170eeca2ecb3ee0 | opening, button holes |
| `03_Sections/od_c09_front_v01_z89p0.png` | bd370989425d7f06a73714abce98df7cfec521b6278d94265276ad9fee57a500 | ribs, bosses, flanges, gussets |
| `03_Sections/od_c09_front_v01_y100.png` | 089ec0abb06502e8ce92c855b93b0442788956e7192fc616c3a278950670ab0c | wall planes |
| `03_Sections/od_c09_front_v01_y200.png` | 32f0a3323f0fa49db494130ec7ba4c543b1c898ca022472cc42d065241d51cc1 | wall planes, top bar |
| `03_Sections/od_c09_front_v01_y2p0.png` | 9d2dd54a80250f96e7a84b76fe6becc3bcbd8583d2018371e6dc8ef44d93623f | flanges, flange holes |
| `03_Sections/od_c09_front_v01_y153p2.png` | 4111ce82f779703582da9005e0812ce462f584d665f0fbbb29abfbe4b434a14b | upper boss |
| `03_Sections/od_c09_front_v01_y153p2_with_E02.png` | c5c7e7dc95f9ead12f5be78970dd67ba891cf91454c23000274e4666b65869a4 | upper boss with the board |
| `03_Sections/od_c09_front_v01_y127p3.png` | 15405c29594a5fe4b1902e93afeb4766d500d91ba2e86ffcfef48232f38f759e | lower boss |
| `03_Sections/od_c09_front_v01_y127p3_with_E02.png` | 5ce90602d626bff4581952fb6fba3994f5302e38de2b88a552530f677f3af17d | lower boss with the board |
| `03_Sections/od_c09_front_v01_x-95.png` | e884afe651cc525ac0a28b5939a914283120005a4548cf8815f50d9419109f0f | flange hole, button holes |
| `03_Sections/od_c09_front_v01_x-85.png` | 085961e5dbb540c3895566d63c8321f04fb845827ddd479d0a6267a8cbc8247f | flange hole |
| `03_Sections/od_c09_front_v01_x85.png` | 07e36cec980e4c6b0fab52a2c4ec429faf6773758aeacdb5f5a22f2f304d1f11 | flange hole |
| `03_Sections/od_c09_front_v01_x95.png` | 25bd03f9216f357007a990a2625ca1a10da09672c5181b728c040e3e9d442b79 | flange hole |
| `03_Sections/od_c09_front_v01_x-78.png` | b9e0be69524a99fa8d3e9fa96820d541c70d462d082abe437ba94859c165d633 | inner left gusset, R4 / R5 |
| `03_Sections/od_c09_front_v01_x102.png` | 366c2e0296e5fa39d710eafe054e1af61e887d6ee8ed76201a21f9cce64501e4 | outer right gusset |
| `03_Sections/od_c09_front_v01_x-91.png` | 1c4b54e4172da903d23ad1fbea810c00761d5be9c12d3251ebeecfe94367d236 | both bosses, insert bores |
| `03_Sections/od_c09_front_v01_x-91_with_E02.png` | 511893a6f4c33787baf23ed4c749e9c9a213c3cfa8c9f9d1dfcea9a871b0f509 | bosses with the board |
| `03_Sections/od_c09_front_v01_x36.png` | b873a31f64e19a6f8af2f7f230f7b59910cf1335657c7c28238270ac4683b34b | top bar and R1 where the handle passes |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 (OCCT 7.9.3) · tools venv via `tools/run.py` · repo commit 10929db

## 3. Gate self-check

Each line gives the binding item of a §5 row. Every item of every row is in `01_CAD/check_od_c09_front_v01.json` and in `01_CAD/report_tables_v01.md`. Margins are signed: positive means inside the limit.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 solid | 1 | 0 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1, 1, 0 | 0 | — | PASS | — |
| U-02 | 232.000 × 215.000 × 25.000 mm | each spec ± 0.1 | 0.100 | — | PASS | — |
| envelope_within_spec | size as U-02; position (reported apart) x −116.000 … +116.000, y 0.000 … 215.000, z +72.000 … +97.000 | ± 0.1 | 0.100 | — | PASS | — |
| U-03 (a) contacts | wall foot, flange L, flange R on OD-C01 0.0000; OD-C10 skirt on wall top 0.0000; boss ends on OD-E02 0.0001 / 0.0001 mm | = 0 (band 0.005) | −0.0001 | (−93.925, 157.927, 85.485) | PASS (assumed: A-01, A-02, A-03, A-07) | A-01, A-02, A-03, A-07 |
| U-03 (a) interference | 15 sound pairs 0.000 mm³. 12 pairs with OD-G10 or OD-E02 use the §5 fallback: all have clearance > 0 and none is inside. Least values: OD-G10 to housing 3.6e-15 mm (a reference pair); panel to OD-G10 14.021 mm; panel moved +0.005 along Z to OD-E02 0.0051 mm | ≤ 0 mm³ / clearance > 0 and not inside | 0 | — | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-03 (a) footprint, holes | foot to plate edge and corner arcs 0.780; flanges to OD-C01 holes 4.300 / 4.300; wall foot to OD-C01 holes 2.300; flange-hole centres to OD-C01 hole centres 19.849 mm | ≥ 0.5; ≥ 3.0; ≥ 2.0; ≥ 6.0 | 0.280; 1.300; 0.300; 13.849 | (116, 0, 97); (±104, 0, 90); (−110, 0, 94) | PASS (assumed: A-01, A-02) | A-01, A-02 |
| U-03 (a) brew area | panel to OD-C05 12.000, to housing 8.776, to OD-G04 18.053 mm | ≥ 2.0 | 6.776 | (−44.0, 191.0, 84.0) | PASS (assumed: A-05) | A-05 |
| U-03 (a) OD-C15 keep-outs | 0.000 / 0.000 mm³ (they touch the wall's inner face at zero gap, by design) | ≤ 0 | 0 | — | PASS | — |
| U-03 (b) | lowered from +40.0 in 21 steps of 2.0: OD-C01, OD-C05, housing and OD-G04 0.000 mm³ at every step; OD-G10 clearance > 0 and never inside, least 14.021 mm at the seat | ≤ 0 at every step | 0 | — | PASS (assumed: A-05) | A-05 |
| U-04 | AP242, 1 solid, volume delta 1.9e-9 mm³, faces delta 0, label `od_c09_front`, valid after re-import | per row | 0 | — | PASS | — |
| U-05 / feature_census | 1 wall with 1 opening (4 of 4 open probes); R1…R5, 2 flanges and 4 gussets present (12 of 12 probes); 4 gusset hypotenuse planes; 9 bores (4 Ø3.4 along Y, 3 Ø15 along Z, 2 Ø4.0 blind along Z); 2 Ø11 boss axes; 2 collar reliefs; faces 40 plane + 13 cylinder | counts per plan | 0 | — | PASS | — |
| U-06 (Soft) | min_wall wide 3.000 mm | ≥ 2.0 | 1.000 | (−115.776, 0.224, 97.0) | PASS | — |
| U-07 | STL tolerance 0.01 mm, angular 0.15 rad (bound 4·acos(1 − 0.01/8.6907) = 0.19191 rad; R_max is the B3 relief); max sagitta 0.00489 mm; 3932 triangles; the delivered STL matches a fresh mesh of the re-imported STEP byte for byte | ≤ 0.01; ≤ bound | 0.0051 | (−97.248, 132.612, 96.25) | PASS | — |
| U-08 | N/A by its row (no threads) | — | — | — | N/A | — |
| D-01a | min_wall 3.000 mm at spacing 0.45 (the tool refused 0.4 on the 232 × 215 face and named 0.45) | ≥ 0.8 | 2.200 | (−115.776, 0.224, 97.0) | PASS | — |
| D-01b | 3.000 mm | ≥ 2.0 | 1.000 | same | PASS (assumed: A-11) | A-11 |
| D-02 | 232.0 × 215.0 on the bed, 25.0 tall | ≤ 420 × 420 × 500 | 188.0 / 205.0 / 475.0 | — | PASS (assumed: A-10) | A-10 |
| D-03a | least downward angle 90.0° (no downward face off the bed) with the four flange-hole crowns excluded; the crowns, the named exception, read 0.0° at (−95.0, 4.0, 75.3) | ≥ 45° | 45.0 | — | PASS (assumed: A-09) | A-09 |
| D-03b | flange-hole bridges 3.400 mm each; elsewhere `flat_ceiling_spans` reads 0.000 (a lead) | ≤ 5 | 1.600 | (±85 / ±95, 0, 77) | PASS (assumed: A-09) | A-09 |
| D-04a | four flange holes Ø3.400 mm | ≥ 3.25 | 0.150 | — | PASS | — |
| D-05a | material across each insert bore: upper 10.774, lower 10.958 mm | ≥ 8.0 | 2.774 | upper boss, 90°, 1.5 from the end | PASS (assumed: A-03) | A-03 |
| D-05b | both bores Ø4.000, depth 6.000, blind | 4.0 ± 0.05; 6.0 ± 0.1 | 0.050; 0.100 | — | PASS (assumed: A-03) | A-03 |
| D-06a | min_wall 3.000 mm | ≥ 1.0 | 2.000 | as D-01a | PASS | — |
| D-07 | N/A by its row | — | — | — | N/A | — |
| J-05 | wall around the insert bore: upper 3.050, lower 3.288 mm (both at the collar reliefs) | ≥ 3.0 | 0.050 | (−92.277, 158.135, 85.585) | PASS (assumed: A-03) | A-03 |
| E-01 | panel without bosses to OD-E02 1.136 mm; each boss from 0.5 in front of its end face 0.5000 / 0.5000; side gap at end + 2.0 0.5000 / 0.5000 (the collar reliefs, radius = collar + 0.5) | ≥ 0.5 | 0.636; −4e-13 | (−94.678, 146.038, 94.0); (−90.573, 158.714, 85.985) | PASS (assumed: A-03) | A-03 |
| E-05 | insert bore axis to the posed board hole axis 0.0000 / 0.0000 mm (board holes Ø3.538 at (−91.0555, 153.2349) and Ø3.441 at (−90.9987, 127.2515)) | ≤ 0.10 | 0.100 | — | PASS (assumed: A-03) | A-03 |
| E-06 | self-check: both bosses run into the wall, and all four gussets sit on flange and wall (6 of 6 ties); see sections `x-91`, `x-78`, `x102`, `y153p2`, `y127p3` | reviewer, from sections | — | — | PASS (self-check only) | — |
| REQ-01 | four holes Ø3.400, offset 0.000, length 4.000, through; underside faces at y 0.000 … 0.000 | Ø3.4 ± 0.1, ≤ 0.10, 4.0 ± 0.1; y 0 ± 0.10 | 0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-02 | outer face 97.000 and inner face 94.000 at (−100, 100), (+100, 100), (−100, 200), (0, 200), (+100, 200); x −116.000 / +116.000; top face 215.000 | ± 0.10 | 0.100 | — | PASS (assumed: A-02) | A-02 |
| REQ-03 | edges at z 95.5: slot x −75.000 / +75.000; window x −57.500 / +75.000; window top y 188.000; slot top y 50.000; shrunk boxes ∩ panel 0.000 / 0.000 mm³ | ± 0.1; = 0 | 0.100; 0 | — | PASS (assumed: A-05, A-06) | A-05, A-06 |
| REQ-04 | B2 foremost point z 98.565 (1.565 proud); B1 95.333 and B3 95.345 (1.667 / 1.655 recessed); hole offsets B1 0.0000, B2 0.0000, B3 0.0000 mm | B2 ≥ 97.5; B1, B3 ≥ 95.0; ≤ 0.25 | 1.065; 0.333; 0.250 | B1 (−95.080, 161.441, 95.333) | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-05 (a) | OD-G10 at φ −55 … +10 every 5° (14 poses): least gap to the panel 2.511 mm at φ +10 (the window's right edge); to OD-E02 28.669 mm at φ −55 | ≥ 2.0 | 0.511 | (75.0, 160.297, 97.0) | PASS (assumed: A-05) | A-05 |
| REQ-05 (b) | φ −50, lowered 15, axis carried z 32 → 182 every 5.0 (31 poses): clearance > 0 and never inside at every pose; least 11.689 mm to the panel (axis at z 67), 29.915 mm to OD-E02 | clearance > 0, not inside | — | (10.710, 188.0, 95.284) | PASS (assumed: A-05) | A-05 |
| REQ-06 | six Ø6 driver cylinders ∩ panel: 0.000 mm³ each | = 0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-07 | min z 72.000; tray box ∩ panel 0.000 mm³; knob place ∩ panel 0.000 mm³ | ≥ 72.0; = 0 | 0 | — | PASS (assumed: A-06, A-13) | A-06, A-13 |
| REQ-08 (Soft) | bench test, not geometric. Risk rated medium: a 3 mm PLA wall 232 × 215 mm with its side edges free until the side panels exist (A-12) | first print | — | — | INCONCLUSIVE | A-12 |

## 4. Robustness sweep (D7)

Each run rebuilt the part with one fit-critical parameter at its low or high value, wrote it into `01_CAD/sweep_v01/`, and ran the same predicates with every stage. Two things differ from the delivered run:

- The sweep runs write no STL, so U-07 reads "no STL given" there. U-07 gates the delivered STL only.
- Clearances between two reference solids (OD-G10 or OD-E02 against another reference) do not involve the panel. The sweep reads them from `sweep_v01/ref_cache.json`, which the sweep's nominal run filled and which is keyed by the inputs' SHA-256.

REQ-05 and U-03 (b) are already sweeps of their motion variables taken together (L-09, L-10).

| Parameter | Low · nominal · high | All built, one solid | Not PASS (excluding U-07 and REQ-08) | Worst margin |
|---|---|---|---|---|
| win_x_left | −57.6 · −57.5 · −57.4 | yes | none | REQ-05 (a) 2.511 |
| opening_x_right | 74.9 · 75.0 · 75.1 | yes | none | REQ-05 (a) 2.435 (low): margin 0.435 |
| win_top_y | 187.9 · 188.0 · 188.1 | yes | none | housing gap 8.681 (high) |
| slot_x_left | −75.1 · −75.0 · −74.9 | yes | none | — |
| slot_top_y | 49.9 · 50.0 · 50.1 | yes | none | — |
| flange_hole_d | 3.3 · 3.4 · 3.5 | yes | none | D-04a 3.300 (low): margin 0.050; D-03b 3.5 (high) |
| flange_hole_x | ±0.1 shift | yes | none | REQ-01 offset 0.100 = limit (by construction) |
| flange_hole_z | 76.9 · 77.0 · 77.1 | yes | none | as above |
| insert_bore_d | 3.95 · 4.0 · 4.05 | yes | none | J-05 upper 3.025 (high): margin 0.025 |
| insert_bore_depth | 5.9 · 6.0 · 6.1 | yes | none | D-05b at its limits |
| button_hole_d | 14.8 · 15.0 · 15.2 | yes | none | E-01 panel without bosses 1.036 (low) |
| boss_end_z | 85.385 · 85.485 · 85.585 | yes | low: U-03 panel|OD-E02 clearance 0 (boss 0.1 into the board), E-01 0.400; high: U-03 boss contacts 0.1001 | designed contact: holds at nominal only |
| boss_d | 10.9 · 11.0 · 11.1 | yes | none | D-05a 10.724 (low) |
| wall_z (in and out together) | −0.1 · 0 · +0.1 | yes | low: U-03 OD-C15 keep-outs 0.238 mm³ each | footprint 0.704 (high) |
| wall_top_y | 214.9 · 215.0 · 215.1 | yes | low: U-03 OD-C10 contact 0.100; high: U-03 panel ∩ OD-C10 1.181 mm³ | designed contact: holds at nominal only |
| wall_x_half | 115.95 · 116.0 · 116.05 | yes | none | U-02 at ± 0.1 |

All 33 runs built one valid solid. The only failures are on the spec's zero-gap contacts and touches: the boss ends on OD-E02, the OD-C10 skirt on the top edge, and the OD-C15 keep-outs on the inner face. A ±0.1 change breaks any of them by definition, so these rows pass at nominal only. Every other gate passes at every swept value. The worst margin of every gate is listed in `01_CAD/report_tables_v01.md` ("Sweep worst margin per gate").

## 5. Build facts

- Envelope 232.000 × 215.000 × 25.000 mm at x ±116, y 0 … 215, z +72 … +97. Volume 95 755.1 mm³. Mass 118.7 g at 1240 kg/m³ (PLA, A-11).
- Fillets: none. The spec names none and asks for square corners at the opening, so no fillet ladder was used.
- Placements in the check assembly:
  - OD-C01 and OD-C10 are at the identity.
  - OD-C05 and the three OD-G01 solids use the housing pose: housing x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0).
  - OD-E02 uses the board pose: board x → −Y, y → −X, z → −Z, origin (−99.0, 140.0, 69.35).
  - OD-G10 was identified by measurement (largest max Z, 182.08). The housing was identified by volume against the housing-alone file (90 216.79 mm³ for both).
  - The bosses sit on the posed board's measured screw-hole axes, and the button holes on the measured cap axes at z 95.5.
  - The check assembly carries no screw envelopes.
- Reference soundness: OD-C01, OD-C05, OD-C10, the housing and OD-G04 have `brep_valid` 1. OD-G10 and OD-E02 have `brep_valid` 0, so every row with them uses the §5 `clearance` fallback.

## 6. Plausibility (§P, D6)

| # | Question | Designer's answer, from the sections |
|---|---|---|
| P1 | Gravity | Yes. The wall's foot and both flanges stand on the plate's top face (contacts 0.000), held by four M3 screws from above. The lid's front skirt rests on the top edge (`y2p0`, `x-85`, `x95`). |
| P2 | Function chains | Yes. The brew opening clears the portafilter's whole travel, and the tray slot is open at the plate along +Z. The buttons act through the wall onto the board, which is held on two bosses (`z95p5`, `x-91_with_E02`). No airflow or cable run belongs to this part. |
| P3 | Motion clearance | Yes. The portafilter swings φ −55 … +10 with at least 2.511 to the panel, and is carried in along +Z with at least 11.689. The tray slot box is free (`z95p5`, `x36`). |
| P4 | Human factors | Mostly. Three Ø15 holes form a column on the left pillar. B2 stands 1.565 proud; B1 and B3 sit 1.66 recessed, which spec 1.1 accepts (A-04). A fingertip reaches a 1.7-deep Ø15 recess. The handle passes through the window's right half. |
| P5 | Absurdity next to a real product | No. A flat fascia with a framed brew opening and a button column is common on single-group machines. |
| P6 | Floating, embedded, mirrored, upside-down | None. It is one solid. Ribs, bosses and gussets are on the rear side. The caps point out through the holes (`y153p2_with_E02`, `y127p3_with_E02`). The flanges point back over the plate, the mirror of OD-C11 as intended. |

## 7. Library and tools used

- Card: UNO10 U5 tank heat-set (read at J2). No second card matched.
- `tools.core`: `read_step`, `solids`, `solid_count`, `validity`, `brep_valid`, `write_step` (AP242, pinned timestamp), `compare_step`, `write_stl`, `common_volume`.
- `tools.measure`: `envelope`, `bore_census`, `locate_bore`, `feature_census`, `clearance`, `interference`, `radial_extent`, `radial_profile`, `min_wall` (with its `wide` reading for U-06), `overhang_census(build_dir=(0, 0, −1))`, `flat_ceiling_spans`.
- `tools.drawing.write_sections`: 18 pictures, `nothing_clipped` 0 in every one.
- `tools.result.gate` with the GATES §0 bands.
- New job code, all under `01_CAD/`:
  - the §2 poses, plus the OD-G10 rotation and carry;
  - the §5 fallback for OD-G10 and OD-E02;
  - exact line probes for the REQ-02 face planes and the REQ-03 edges;
  - point-classification probes for the feature census;
  - the sweep driver with its reference-pair cache, and the table script.
- No `tools/measure` function was missing.

## 8. Deviations from the plan

1. **Fix cycle 1 (geometry).** In the first dry-run build all four gussets were extruded along −X: the triangle's winding gives its face a −X normal. This put material at x 72 … 76, inside the tray slot. It was found on a scratch STEP before any export (D-03a 0°, REQ-03 16.7 mm³, REQ-07 672 mm³, U-05 8 of 12). The fix states the extrusion direction explicitly.
2. **Fix cycle 2 (parameters).** The first sweep showed that `win_x_right` at −0.1 opened a 0.1-wide ceiling under rib R2 (D-03a 0°). The cause: the tray slot's right edge and the window's right edge are one plane in spec §4, but the build had them as two parameters. They are now one parameter, `opening_x_right`, and the left slot edge is `slot_x_left`. At nominal the exported STEP, STL and assembly are byte-identical to the earlier export.
3. **Check-script corrections, all made before the gated run:**
   - one opening probe point moved into the slot, to (−66, 25);
   - the underside is read only on −Y faces below the flanges' top (y < 4.0);
   - the D-03a plug for each horizontal hole is exactly the hole's length (y 0 … 4);
   - the `min_wall` wide reading is read by its field name;
   - the flange-to-hole clip stops 0.4 short of the wall's low limit;
   - debugging stages and the sweep's reference-pair cache were added.

   The gated run used every stage and no cache.
4. The STL angular tolerance is 0.15 rad, not the plan's 0.2. R_max is 8.6907 (the relief), not 7.5, so the bound is 0.19191 rad.
5. U-03 (a) reads panel to OD-E02 with the panel moved 0.005 along +Z, because the boss ends are designed contacts.
6. `min_wall` ran at 0.45, the spacing the tool named after refusing 0.4, as the plan's risk 6 expected.
7. Sweep changes:
   - `wall_x_half` is swept ±0.05, not ±0.1: a ±0.1 change at each end is ±0.2 on the 232.0 size, outside U-02.
   - `win_x_right` and `slot_x_half` are replaced by `opening_x_right` and `slot_x_left` (item 2).

## 9. What I am least sure of

1. **Zero-margin rows that hold only because the spec makes them contacts.** The boss ends seat on a scanned surface (A-03): contact 0.0001, and the surface is flat only on each hole's −X side. Each boss's side gap is exactly the relief's 0.5, and the upper boss keeps 3.050 of wall (J-05 margin 0.050; 0.025 with a Ø4.05 bore). The OD-C15 keep-outs and the OD-C10 skirt touch at zero gap. Moving any of these by 0.1 breaks the row. The first fit has to confirm the seat.
2. **The §5 fallback on unsound solids.** The pair OD-G10 to housing reads 3.6e-15 mm: the locked portafilter touches the housing, and "> 0" passes on floating-point noise. It is a pair of delivered parts, not this panel, but the rule cannot tell a touch from a shallow overlap there.
3. **REQ-05 (a) at φ +10** (A-05, gasket wear). The gap is 2.511 at nominal and 2.435 with the right edge 0.1 to the left. Past +5° it closes about 1.7 mm per degree, so a lock a few degrees past +10° would touch the window's edge.

## 10. Stop

Not stopped.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20261002-od-c09-front-panel",
  "part": "od_c09_front",
  "tag": "v01",
  "spec_version": "1.1",
  "files": [
    {"path": "02_STEP_STL/od_c09_front_C1_v01.step", "sha256": "0d688d24b7954e959291b171fa6e464dd30834e3f737eb73b696dfc992148ab5"},
    {"path": "02_STEP_STL/od_c09_front_C1_v01.stl", "sha256": "086c7c7e4f1c98472b1800dfce3bf73e83ef240311986df454bd2e1a7c740498"},
    {"path": "02_STEP_STL/od_c09_assembly_C1_v01.step", "sha256": "e451a3854cb1dd22d29c9ba8871367f3be17341e9e3c06fecdffc3701406984c"},
    {"path": "01_CAD/build_od_c09_front.py", "sha256": "780f573bc0ded727d2449673370124b625fd7b23caf20d069f6e325ba8ad4d57"},
    {"path": "01_CAD/check_od_c09_front.py", "sha256": "5886cccc39461cf1ca804ab1e97fbeacfd2c1fa8169b060ae4326cf4856007e0"},
    {"path": "01_CAD/check_od_c09_front_v01.json", "sha256": "11ae15209effd70a777e3d8ec9d4a905df1a756de16def2aa55d08665be719fa"},
    {"path": "01_CAD/sweep_v01/SHA256SUMS", "sha256": "504a1e8310a2a31de739a14d7bb0f74a8d17b40e4240803ad80cef3be5e30585"},
    {"path": "01_CAD/sections_v01.json", "sha256": "2d2abef67393b432d712126c6a574712eedfd04a657d8770bc86715d39c42326"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "7.9.3.1", "repo_commit": "10929db"},
  "gates": [
    {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-01", "measured": 1, "unit": "count", "required": "1 solid, brep_valid 1, naked 0", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-02", "measured": 232.0, "unit": "mm", "required": "232.0 x 215.0 x 25.0 +- 0.1", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "envelope_within_spec", "measured": 232.0, "unit": "mm", "required": "size and position +- 0.1", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-03", "measured": 0.0001, "unit": "mm", "required": "contacts = 0; interference <= 0; footprint >= 0.5; holes >= 3.0 / 2.0 / 6.0; brew >= 2.0", "margin": -0.0001, "at": "(-93.925, 157.927, 85.485)", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03", "A-05", "A-07"]},
    {"gate": "U-04", "measured": 1.9e-09, "unit": "mm3", "required": "<= 0", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-05", "measured": 9, "unit": "count", "required": "plan counts", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "feature_census", "measured": 9, "unit": "count", "required": "plan counts", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-06", "measured": 3.0, "unit": "mm", "required": ">= 2.0", "margin": 1.0, "at": "(-115.776, 0.224, 97.0)", "status": "PASS", "assumes": []},
    {"gate": "U-07", "measured": 0.00489, "unit": "mm", "required": "<= 0.01", "margin": 0.0051, "at": "(-97.248, 132.612, 96.25)", "status": "PASS", "assumes": []},
    {"gate": "U-08", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "D-01a", "measured": 3.0, "unit": "mm", "required": ">= 0.8", "margin": 2.2, "at": "(-115.776, 0.224, 97.0)", "status": "PASS", "assumes": []},
    {"gate": "D-01b", "measured": 3.0, "unit": "mm", "required": ">= 2.0", "margin": 1.0, "at": "(-115.776, 0.224, 97.0)", "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "D-02", "measured": 232.0, "unit": "mm", "required": "<= 420 x 420 x 500", "margin": 188.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-10"]},
    {"gate": "D-03a", "measured": 90.0, "unit": "deg", "required": ">= 45 (flange-hole crowns excluded)", "margin": 45.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-09"]},
    {"gate": "D-03b", "measured": 3.4, "unit": "mm", "required": "<= 5", "margin": 1.6, "at": "(+-85 / +-95, 0, 77)", "status": "PASS_ASSUMED", "assumes": ["A-09"]},
    {"gate": "D-04a", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": null, "status": "PASS", "assumes": []},
    {"gate": "D-05a", "measured": 10.774, "unit": "mm", "required": ">= 8.0", "margin": 2.774, "at": "upper boss, 90 deg", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "D-05b", "measured": 4.0, "unit": "mm", "required": "4.0 +- 0.05, depth 6.0 +- 0.1", "margin": 0.05, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "D-06a", "measured": 3.0, "unit": "mm", "required": ">= 1.0", "margin": 2.0, "at": "(-115.776, 0.224, 97.0)", "status": "PASS", "assumes": []},
    {"gate": "D-07", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "J-05", "measured": 3.05, "unit": "mm", "required": ">= 3.0", "margin": 0.05, "at": "(-92.277, 158.135, 85.585)", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "E-01", "measured": 0.5, "unit": "mm", "required": ">= 0.5", "margin": -4e-13, "at": "(-90.573, 158.714, 85.985)", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "E-05", "measured": 0.0, "unit": "mm", "required": "<= 0.10", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "E-06", "measured": 6, "unit": "count", "required": "reviewer, from sections", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "REQ-01", "measured": 3.4, "unit": "mm", "required": "3.4 +- 0.1, offset <= 0.10, 4.0 +- 0.1, y 0 +- 0.10", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "REQ-02", "measured": 97.0, "unit": "mm", "required": "97.00 / 94.00 / +-116.0 / 215.00 +- 0.10", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-02"]},
    {"gate": "REQ-03", "measured": 0.0, "unit": "mm3", "required": "edges +- 0.1; boxes = 0", "margin": 0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-05", "A-06"]},
    {"gate": "REQ-04", "measured": 98.565, "unit": "mm", "required": "B2 >= 97.5; B1, B3 >= 95.0; offset <= 0.25", "margin": 0.333, "at": "B1 (-95.080, 161.441, 95.333)", "status": "PASS_ASSUMED", "assumes": ["A-03", "A-04"]},
    {"gate": "REQ-05", "measured": 2.511, "unit": "mm", "required": "(a) >= 2.0; (b) clearance > 0, not inside", "margin": 0.511, "at": "(75.0, 160.297, 97.0)", "status": "PASS_ASSUMED", "assumes": ["A-05"]},
    {"gate": "REQ-06", "measured": 0.0, "unit": "mm3", "required": "= 0", "margin": 0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-14"]},
    {"gate": "REQ-07", "measured": 72.0, "unit": "mm", "required": "min z >= 72.0; boxes = 0", "margin": 0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-06", "A-13"]},
    {"gate": "REQ-08", "measured": null, "unit": "", "required": "bench (Soft)", "margin": null, "at": null, "status": "INCONCLUSIVE", "assumes": ["A-12"]}
  ],
  "sweep": [
    {"parameter": "opening_x_right", "values": [74.9, 75.0, 75.1], "all_built": true, "worst_gate": "REQ-05", "worst_margin": 0.435},
    {"parameter": "insert_bore_d", "values": [3.95, 4.0, 4.05], "all_built": true, "worst_gate": "J-05", "worst_margin": 0.025},
    {"parameter": "flange_hole_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "D-04a", "worst_margin": 0.05},
    {"parameter": "button_hole_d", "values": [14.8, 15.0, 15.2], "all_built": true, "worst_gate": "E-01", "worst_margin": 0.536},
    {"parameter": "boss_end_z", "values": [85.385, 85.485, 85.585], "all_built": true, "worst_gate": "U-03 (designed contact)", "worst_margin": -0.1},
    {"parameter": "wall_top_y", "values": [214.9, 215.0, 215.1], "all_built": true, "worst_gate": "U-03 (designed contact)", "worst_margin": -1.181},
    {"parameter": "wall_z", "values": [-0.1, 0.0, 0.1], "all_built": true, "worst_gate": "U-03 (OD-C15 keep-out touch)", "worst_margin": -0.238},
    {"parameter": "win_x_left, win_top_y, slot_x_left, slot_top_y, flange_hole_x, flange_hole_z, insert_bore_depth, boss_d, wall_x_half", "values": [], "all_built": true, "worst_gate": "none failing", "worst_margin": 0.0}
  ],
  "least_sure": [
    "zero-gap designed contacts (boss ends on the scanned board, skirt, OD-C15 keep-outs) hold at nominal only; boss side gap 0.500 and J-05 margin 0.050 by construction",
    "the clearance > 0 fallback passes the OD-G10 to housing reference pair on 3.6e-15 mm",
    "REQ-05 (a) margin 0.511 at phi +10, 0.435 with the right edge 0.1 lower"
  ],
  "stopped": false
}
```
