# REPORT — od_c05_carrier v02 (20260930-od-c05-group-head-carrier)

Designer: Claude Code, Opus 5.5 · spec version 2.0 · plan `01_CAD/DESIGN_PLAN_v02.md` (written in this package, D2) · brief WP-05 (J3 with its own plan, build attempt 1 of 2, fix_cycles 3) · 2026-09-30 UTC

**Outcome: STOPPED (D9).** D-03a and D-03b (Hard) cannot be met with the spec 2.0 geometry in the spec's print orientation. The cause is conflicts K-3 and K-4 of the plan §8, measured here on the exported STEP. §10 gives the options. Every other §5 row passes on the build and in every sweep run.

`01_CAD/check_od_c05_carrier_v02.py` measures every number below from the re-imported STEP files (`01_CAD/check_od_c05_carrier_v02.json`). The exceptions are rows that say they come from the build log (`01_CAD/build_od_c05_carrier_v02.json`). These self-checks clear no HARD gate; only the reviewer's measurement does.

The input hashes match the brief: OD-G01 f8865cd1…4407b02, OD-G04 19b4a140…98d6ad2. The v01 plan and all v01 files are untouched.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN_v02.md` | c580be8de01b9060e96b8ed8b64640c34fefa5a7d71c5fb7e319cf4985cba6bf | plan for C4 (D2), conflicts K-3, K-4, K-5 in §8 |
| `01_CAD/build_od_c05_carrier_v02.py` | 529d338fa7e53d7b2c477cda522791959930e43282deef5292b0b6cbbd3215d7 | parametric script (Algebra mode, one Params structure) |
| `01_CAD/check_od_c05_carrier_v02.py` | b0ad4b026d2262c9a04a977d10d7edaedca71462187f1150427a1604ab25f661 | checks, written before the build (D3) |
| `01_CAD/sections_od_c05_carrier_v02.py` | d84bd3d2284a3f16f4cb836648cd0c87b78014fdccfaa6e3a9dd42e063e6735f | D6 sections from the exported STEP files |
| `01_CAD/sweep_od_c05_carrier_v02.py` | faef751091238559801f993c6925fa37b04bc345dd2f128a603bde3e9ed7c6e7 | D7 sweep driver |
| `01_CAD/sweep_summary_v02.py` | af7679c68d52563082fc82b4fcc75e62dee7e7be2ab94911eb1d49635fba250e | sweep summary and SHA256SUMS writer |
| `02_STEP_STL/od_c05_carrier_C4_v02.step` | 2aea239c16edd93100c1dedcdd82daa4fb26c45a85c9419702be87b7063efb71 | AP242 (`tools.core.write_step`), label `od_c05_carrier`, re-imported for every measurement |
| `02_STEP_STL/od_c05_assembly_C4_v02.step` | a7f792a32b8085d23d93e412f49e1832e72f7842c610378bd5d8c0455ed30eaa | AP242 check assembly: carrier + OD-G01 (identity) + OD-G04 (+6.05° about Z, then z −6.82) |
| `02_STEP_STL/od_c05_carrier_C4_v02.stl` | d9b49b0690cebbd9029f82fca39df29f985fe3d3a70709dfb33662c9933be8ac | binary STL from the re-imported STEP, cached triangulation cleared; tol 0.01 mm / angular 0.20 rad; 3808 triangles; volume 211163.077 mm³; bbox (−55.0, −102.0, −29.94) … (55.0, 50.0, 180.06) |
| `01_CAD/check_od_c05_carrier_v02.json` | 9db01143b1bcde1e573eee681ab25c195ae81ca7431c5507934b12f3e8f6c634 | check results: every gate row and the facts (analytic downward-face list included) |
| `01_CAD/build_od_c05_carrier_v02.json` | 57e3711be9c289e1b1a4712b442020a58a7976da366ea26ccf1b6162b7d6cf6b | build log: parameters, export round trip, STL writer detail |
| `01_CAD/sections_od_c05_carrier_v02.json` | c127996bfdc3bde6db62cde30b5f5c34b777ba4063690857f455a8dd247ffd2c | section log: plane, point, nothing_clipped |
| `01_CAD/sweep_v02/SHA256SUMS_v02.txt` | 7512c397088f5b57cb25ff402a10efef6ea3c5d39fc67689a25e19941526af36 | SHA-256 of the 106 other sweep files (21 runs × part STEP, assembly STEP, STL, build log, check JSON; plus summary) |
| `01_CAD/sweep_v02/summary_v02.json` | 2349eca8f591fd64797fabcaa7ba97cb5b7a77cc6117105884df24bf3931a70e | per run: one solid, rows not passing, worst margin per gate |
| `03_Sections/od_c05_carrier_y0_v02_front.png` | e1ad969bc8178aa7a2cda58c22c9962c1cf7ad5e37a501da1070c1526f4fa4cf | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x0_v02_left.png` | d5273b74d7096089fc0e90c58bfb0a3c365626b57656013ca8a2f4f873b63ffe | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x44_v02_left.png` | 5516d2c68ee45a35f17fa8e300b12ec1cb209d5fa256f8f3134637c066283abe | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x53_v02_left.png` | 2b2f8e48467bb381692f85a53bb5f06cd7cd41fad6749840e8ae9b08b2903cd9 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_zm27p44_v02_top.png` | 3199702f7f22ee5a4986232e038fd0da2b5c481b1500bb923a7f47b3521a9dc8 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_z178_v02_top.png` | 6c0e2a0406b5d7ba91e0c9b6732fc34c1408094216bbad3dcbfa38b600266133 | section, nothing_clipped 0 |
| `03_Sections/od_c05_assembly_y0_v02_front.png` | 1dd90de7da02b81bee865695c08343e99dd28e42df5066ef0a50e7052b48ee53 | section, nothing_clipped 0 |
| `03_Sections/od_c05_assembly_x0_v02_left.png` | 6e8a34ae5c2fcd2124c57ed4e677ca9fd433a0c8ad198f09b1c511d7a37ad1c8 | section, nothing_clipped 0 |

The section images draw +Z (the mouth, down in the machine) upward on the page, so the machine appears upside down in them.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · OCCT 7.9.3 · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (tools used unmodified)

## 3. Gate self-check

The band is from GATES.md §0: 0.005 mm, 0.001°, 0.001 mm³, and 0 for counts and 1/0 facts. U-07's angular tolerance uses 0.00002 rad. Limits come from spec 2.0 §5 only. Margins are signed and positive inside the limit, so a pass inside the band shows its small negative margin.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | whole part | PASS | — |
| U-02 | 110.000 × 152.000 × 210.000 mm | each ± 0.1 | +0.100 each | — | PASS | — |
| envelope_within_spec | x −55.000 … 55.000, y −102.000 … 50.000, z −29.940 … 180.060 | x ±55.0, y −102.0 … +50.0, z −29.94 … +180.06, each ± 0.1 | +0.100 each | — | PASS | — |
| U-03 (a) carrier\|OD-G01 | contact clearance 0.000 mm; interference 0.000 mm³; four hole axes 0.000 from the insert bore axes (inserts located at (±44.000, ±44.000)) | contact = 0; ≤ 0 mm³; ≤ 0.10 | 0; 0; +0.100 | contact at (−42.0, 50.0, −24.94); OD-G01 validity 1/1/0 | PASS (assumed: A-01) | A-01 |
| U-03 (a) carrier\|OD-G04 | clearance 5.000 mm; interference 0.000 mm³ | ≥ 2.0; ≤ 0 | +3.000; 0 | carrier (21.2132, 21.2132, −24.94), OD-G04 (21.2132, 21.2132, −19.94); OD-G04 validity 1/1/0 | PASS (assumed: A-06) | A-06 |
| U-03 (b) | — | N/A by its row (no motion variable) | — | — | N/A | — |
| U-04 | schema AP242, 1 solid, volume delta 0.000 mm³, faces delta 0, valid after 1, label `od_c05_carrier` | re-read unchanged, no stray shells, valid | 0 | — | PASS | — |
| U-05 / feature_census | 24 planar, 15 cylindrical (13 concave, 2 convex R 6.000 about (±49, 44)), 13 bores, no other kind; the 12 bores along Z located one by one | plan §3: 24 / 15 / 13 / 2 / 13 | 0 | §5 below | PASS | — |
| U-06 (Soft) | 2.750 mm | ≥ 2.0 | +0.750 | (−44.0, 50.0, −29.94), counterbore to the plate's front edge | PASS | — |
| U-07 | sagitta 0.00493 mm (B-rep re-meshed at the export settings); STL 1 body, 0 naked edges, winding 1; angular 0.20 rad | tol 0.01, angular ≤ 0.2310 rad, sagitta ≤ 0.01 | +0.00507 | (20.8218, −21.5906, −27.44), window arc | PASS | — |
| U-08 | — | threaded parts only | — | — | N/A: no threads, by its row | — |
| D-01a | 2.750 mm | ≥ 0.8 | +1.950 | (−44.0, 50.0, −29.94) | PASS | — |
| D-01b | 2.750 mm | ≥ 2.0 | +0.750 | same | PASS | — |
| D-02 | 152.0 × 210.0 on the bed, 110.0 tall | ≤ 220 × 220, ≤ 250 | +68.0, +10.0, +140.0 | x −55 face down | PASS (assumed: A-08) | A-08 |
| **D-03a** | **0.000°** outside the named exception (`overhang_census(build_dir=(1,0,0))`, 7257 samples below 45°); analytic listing: two faces at 0.000°, one at 3.325° | ≥ 45° | **−45.000** | +X gusset inner faces x = +51: rear (51.0, −98.0, 176.06), front (51.0, −32.0, −4.94); corner R 6 about (−49, 44) at (−54.990, 44.348, −24.94) | **FAIL** | A-13 |
| **D-03b** | **56.569 mm** outside the named exception (two horizontal 800 mm² triangles, longest line between their carried legs) | ≤ 5 | **−51.569** | +X gussets, faces centred (51.0, −38.667, −11.607) and (51.0, −71.333, 162.727) | **FAIL** | — |
| D-03a / D-03b named exception | 12 bore faces along Z found by position; least 0.000° (crowns, as the exception says); widest crown 6.500 mm | reported apart; crowns ≤ 6.6 | +0.100 (crown span) | (±44, ±44) plate, (±35, −72 / −92) foot | inside the named exception | A-13 |
| D-04a | 3.400 mm (all eight) | ≥ 3.25 | +0.150 | (±44, ±44); (±35, −72 / −92) | PASS | — |
| D-06a | 2.750 mm | ≥ 1.0 | +1.750 | (−44.0, 50.0, −29.94) | PASS | — |
| D-07 | — | fit bores only | — | — | N/A: clearance holes only, by its row | — |
| E-06 | four gussets, each 3200.000 mm³ (40 × 40 / 2 × 4), four inner faces at \|x\| 51, one solid | plate tied to the wall, wall to the foot, no free boss | 0 | x ±(51 … 55); front y −52 … −12, z −24.94 … 15.06; rear y −98 … −58, z 136.06 … 176.06 | PASS | — |
| REQ-01 | Ø3.400, through, 3.000 long, offset 0.000 from nominal and from the OD-G01 inserts | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-01) | A-01 |
| REQ-02 | Ø6.500 × 2.000 deep, open at z −29.940, coaxial 0.000 | Ø6.5 ± 0.1, 2.0 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-09) | A-09 |
| REQ-03 | top z −29.940 (min_z and the four counterbore ends); underside z −24.940 (counterbore start + 2.000 + 3.000) | ± 0.10 | +0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-04 | innermost material on the whole ray 30.000 mm over 36 angles × 5 levels (180 rays); θ 0° 42.426 (gable apex); θ 90° 30.000 | ≥ 30.0; 42.43 at θ 0°; 30.0 at θ 90° | −3.6e-15 (inside the band) | least at θ 70°, z −29.9 (10.2606, 28.1908) | PASS (assumed: A-06) | A-06 |
| REQ-05 | underside z 180.060 (max_z); foot 4.000 thick (each foot hole's length) | ± 0.10; 4.0 ± 0.1 | +0.100 | foot holes z 176.06 … 180.06 | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-06 | Ø3.400 through, offset 0.000 (all four) | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | (±35, −72), (±35, −92) | PASS (assumed: A-04) | A-04 |
| REQ-07 | min_y −102.000 | ≥ −102.0 | 0.000 | foot rear face | PASS (assumed: A-05) | A-05 |
| REQ-08 | housing to the front gussets 1.000 mm; housing to the wall 2.000 mm (plate contact reported under U-03) | ≥ 1.0; ≥ 2.0 | 0.000; 0.000 | housing (−50.0, −42.0, −24.94) to gusset face x −51; housing (−42.0, −50.0, −24.94) to wall face y −52 | PASS (assumed: A-01) | A-01 |
| REQ-09 (Soft) | — | no visible flex (bench) | — | — | INCONCLUSIVE (Soft bench gate, answered by the first print; risk HIGH, §9) | A-11 |

REQ-08 method: the carrier re-imported from the STEP is cut by position below the contact plane (z > −24.94) into the front piece (y > −52, the two front gussets, 6400.000 mm³) and the wall piece (y < −52, wall, foot, rear gussets). `clearance` of OD-G01 to each is measured with the nearest points.

D-03a, the analytic angles (RV01 F3): the two gable flats are 45.000000000° and the R 30 arc is 45.000000000° at its tangent lines. They are exact, not sampled. The census counts them at 45° without a sampling bound because the least lies elsewhere (0°).

## 4. Robustness sweep (D7)

21 runs into `01_CAD/sweep_v02/`, each built and checked with the same predicates. Every run built one valid solid. In **every** run, nominal included, the only rows not passing are D-03a (0.000°, both predicates) and D-03b (56.569 mm). No swept parameter touches the +X gussets' inner faces or the −X front corner. The table shows the worst margin among the rows that pass.

| Parameter | Low · nominal · high | All built, one solid | Worst passing gate | Worst margin |
|---|---|---|---|---|
| hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 Ø at the tolerance ends; D-04a at 3.3 | 0.000; +0.050 |
| hole_xy | 43.95 · 44.00 · 44.05 | yes | REQ-01 offset; D-01b | +0.050; +0.700 (2.700 at 44.05) |
| cb_d | 6.4 · 6.5 · 6.6 | yes | D-03b crown span (exception) at 6.6; D-01b | 0.000; +0.700 (2.700 at 6.6) |
| cb_depth | 1.9 · 2.0 · 2.1 | yes | REQ-02 depth at the tolerance ends | 0.000 |
| hub_r | 30.0 · 30.1 (one-sided) | yes | REQ-04 innermost 30.100 | +0.100 |
| wall_y_front | −52.0 · −52.1 (one-sided) | yes | REQ-08 housing to wall 2.100 | +0.100 |
| foot_t | 3.9 · 4.0 · 4.1 | yes | REQ-05 thickness at the tolerance ends | 0.000 |
| foot_y_rear | −102.0 · −101.9 (one-sided) | yes | U-02 size_y 151.900; REQ-07 +0.100 | 0.000 |
| foot_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-06 Ø at the tolerance ends; D-04a at 3.3 | 0.000; +0.050 |
| foot_hole_x | 34.95 · 35.00 · 35.05 | yes | REQ-06 offset | +0.050 |
| foot_hole_y | −72/−92 ± 0.05 | yes | REQ-06 offset | +0.050 |
| gusset_x_in | 51.0 · 51.1 (one-sided) | yes | REQ-08 housing to gussets 1.100; E-06 volume 3120.000 as predicted for 3.9 thick | +0.100 |

REQ-07 and REQ-08 sit at margin 0.000 at nominal by construction (spec values at the limit). The one-sided rungs show that each moves the right way.

## 5. Build facts

- Envelope 110.000 × 152.000 × 210.000 mm; volume 211160.186 mm³; mass 225.94 g at 1070 kg/m³ (§3, A-12); centre of mass (−0.151, −46.996, 64.783).
- Fillets: none through a ladder. The two front corners are sketch arcs R 6.000 about (±49.0, 44.0), measured.
- Placements: OD-G01 at the identity, checked by `locate_bore` (inserts (±44.000, ±44.000), hole offsets 0.000) and by the contact at z −24.94 (clearance 0.000, interference 0.000). OD-G04 rotated +6.05° about Z, then translated z −6.82 (OD-G01 REPORT v02 §5). Clearance 5.000 through the window; unchanged from v01.
- Fix cycle 1: the first build read θ 0° = 30.000 and 22 planar faces. The gable polygon was wound clockwise and the window came out as a plain circle. The polygon was re-wound counter-clockwise and the part rebuilt and re-exported. Every number in this REPORT comes from the second export.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | Yes: with −Z up, the plate lies on the housing's rear face (now its top) and the housing hangs under it with its axis vertical and mouth down; the wall stands behind it on the foot on the floor z +180.06 (sections x 0, assembly x 0). |
| P2 | Function chains | Yes: the window (innermost r 30.000, apex 42.426 toward +X) clears the housing's openings (r ≤ 20.93) and OD-G04 (5.000); the four holes are coaxial with the inserts (0.000); TUBE 7 passes over the wall's top edge into the window from above (A-07). |
| P3 | Motion clearance | Yes: no carrier motion. The front gussets stand at \|x\| ≥ 51 and y ≤ −12, behind the axis, so the portafilter handle, which locks toward the front, keeps clear of them. The handle is not modelled, so this is a reading of the geometry. |
| P4 | Human factors | Yes: the housing screws are driven from above into the plate's counterbores. The foot screws are driven from above at 14 and 34 behind the wall, clear of the rear gussets (\|x\| ≥ 51 against x ±35). |
| P5 | Absurdity | No absurdity in the layout: it is a gallows bracket behind and over the group head, as in a Dedica. The thin 6 mm wall, 205 tall between small gussets, looks flexible for a part that takes the portafilter's locking push (§9). |
| P6 | Floating, embedded, mirrored, upside down | None: one solid; interference 0 with both neighbours. The counterbores face up toward the screw heads, and the gable points along the build direction +X. |

## 7. Library and tools used

- Cards: none (nothing matched in `library/INDEX.md`, as at v01).
- `tools.core`: `validity`, `write_step` (AP242), `read_step`, `compare_step`, `write_stl`, `mesh_sagitta`, `common_volume`. `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `interference`, `min_wall` (with `detail["wide"]`), `overhang_census(build_dir=(1,0,0))`, `radial_extent` (whole ray, inner), `mesh_census`, `mass_properties`; `tools.measure.wall.load_mesh` (STL bbox, reported only). `tools.drawing.write_sections`. `tools.result.gate`.
- New job code (in the check script, not the repo): the analytic downward-face list for D-03a (plane normals; cylinder normals over the u range, bounds included) and the D-03b bridge span, both taken from it. The census is the gate and the list corroborates it. Both read 0.000° here. The D-03b bridge measure is the largest distance between the vertices of a horizontal downward face; no `tools/measure` function measures bridge spans.
- REQ-09 geometry (RV01 F2): the plate is 5.0 thick and cantilevers 96 from the wall's front face (y −52) to the front screws (y +44). The wall is 6.0 × 110 and 210 tall. Its free height between the front gussets' lower end (z +15.06) and the rear gussets' upper end (z +136.06) is 121.0. The four gussets have 40 legs.

## 8. Deviations from the plan

1. **Check script, after the first sweep pass:** the E-06 gusset boxes now follow the swept wall front face and foot top (`--expect`). With boxes fixed at the nominal position, the foot_t and wall_y_front rungs read 15.98 mm³ outside the box, an artefact of the check. Those three runs were checked again with the final script. The other 18 sweep checks came from the previous version, which gives identical output at their rungs because the boxes sit at nominal there. The limits did not change.
2. **Section y = 0:** the brief and plan call it "the L profile". A y = 0 plane cuts only the plate, since the wall is at y −58 … −52, so the L profile of plate, wall, foot and gussets is shown in sections x = 0, x = 44 and x = 53. The y = 0 section still shows the plate with the window's asymmetry toward +X.
3. Otherwise none: the census came out as predicted (24 / 15 / 13 / 2 / 13), and the placements are those of plan §5.

## 9. What I am least sure of

1. **Whether option 1 of §10 is acceptable for the gussets.** A 40 × 40 triangular ceiling carried on two legs is a long bridge: up to 56.6 along the hypotenuse direction, against D-03b's 5. It will sag in the first layers, and the front pair's sagging face is 1.0 from the housing's sides (REQ-08 at margin 0.000), so droop there eats the clearance. I would not take the exception without a test print of one gusset.
2. **REQ-09, risk HIGH.** Hand estimate, not a gate. Take a 50 N push on the portafilter along Z at the axis, 55 from the wall's mid-plane, and assume ASA E ≈ 2 GPa. The 121 free height of the 6 × 110 wall section (I ≈ 1980 mm⁴) turns by about M·L/(E·I) ≈ 2750 × 121 / (2000 × 1980) ≈ 0.08 rad (about 5°), several mm at the axis, before the plate's own bending. The gussets stiffen only 40 at each end. Visible flex under the locking push is likely. Closing the section (full-height side walls in place of the gussets) or a thicker wall would help, and both are spec changes.
3. **The REQ-07 and REQ-08 margins of 0.000** are exact by construction. A printed part that grows by the usual FDM +0.1 to +0.2 on outer faces takes the 1.0 gusset gap to about 0.8 to 0.9, and the gap is closer still if the +X gussets' ceiling droops (item 1).

## 10. Stop

**Gate: D-03a (Hard), with D-03b (Hard).** Measured on `02_STEP_STL/od_c05_carrier_C4_v02.step` with build direction +X (spec §5 D-03a threshold, §4, A-13).

- **K-3, the gussets at x +51 … +55:** each inner face at x = +51 has the outward normal −X and faces the bed at **0.000°**. D-03a requires ≥ 45°, margin −45.000. Each face is a 40 × 40 right triangle of 800.000 mm², carried only along its two legs, a bridge of **56.569** (D-03b ≤ 5, margin −51.569). Nothing of the part lies under these faces at x < +51. The −X pair's inner faces face up. None of the six axis-aligned orientations clears the spec geometry (plan §8): ±X flips the problem to the other gusset pair; +Z leaves the foot's top face as a 44 × 110 shelf at 0°; −Z the plate's underside at 0°; ±Y the wall's rear or front face at 0°.
- **K-4, the front corner R 6.0 about (−49.0, 44.0):** a convex round next to the bed face x = −55. Its lower half faces down from 0° at the bed line to 45° at 1.76 above it. The least off the bed is **3.325°** at (−54.990, 44.348, −24.94). D-03a requires ≥ 45°, margin −41.675. The corner about (+49.0, 44.0) faces up.
- **K-5 (text only):** spec §5 D-03a's check column still reads `build_dir=(0,1,0)` from spec 1.x. The threshold, §4, A-13 and the brief say +X, which is what was measured.

No fix cycle can clear K-3 or K-4 without changing a spec value (gusset position or thickness, the corner shape, the print orientation) or the named exception. Fix cycles used: 1 of 3, on the gable winding (§5).

Trade-off options for the Usta (none taken):
- K-3:
  1. Extend the named exception (D-03a, D-03b) to the two +X gusset ceilings. No geometry change: v02 goes to review as it stands. Risk: sag, §9 item 1.
  2. Allow slicer support under those two faces only: about 106-tall support columns in the housing's side gap and over the foot. This changes "nothing supported".
  3. A concept change: stiffening that starts on the bed side or has 45° undersides in the print, for example full-height side walls at |x| 51 … 55 (which also answers REQ-09), or two printed parts.
- K-4:
  1. The −X corner (or both, for symmetry) becomes a 45° chamfer 6 × 6, or an R 6 arc with a 45° flat tangent to the bed face.
  2. Extend the named exception to that corner (a 1.76-tall droop at the bed).
  3. Square front corners.

The cheapest route is K-3 option 1 together with K-4 option 2: no geometry change, and v02 is complete for review. If K-4 option 1 or 3 is chosen, v03 needs only the corner changed. Every other row passes, and the scripts and sweep carry over.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20260930-od-c05-group-head-carrier",
  "part": "od_c05_carrier",
  "tag": "v02",
  "spec_version": "2.0",
  "files": [
    {"path": "01_CAD/DESIGN_PLAN_v02.md", "sha256": "c580be8de01b9060e96b8ed8b64640c34fefa5a7d71c5fb7e319cf4985cba6bf"},
    {"path": "01_CAD/build_od_c05_carrier_v02.py", "sha256": "529d338fa7e53d7b2c477cda522791959930e43282deef5292b0b6cbbd3215d7"},
    {"path": "01_CAD/check_od_c05_carrier_v02.py", "sha256": "b0ad4b026d2262c9a04a977d10d7edaedca71462187f1150427a1604ab25f661"},
    {"path": "01_CAD/sections_od_c05_carrier_v02.py", "sha256": "d84bd3d2284a3f16f4cb836648cd0c87b78014fdccfaa6e3a9dd42e063e6735f"},
    {"path": "01_CAD/sweep_od_c05_carrier_v02.py", "sha256": "faef751091238559801f993c6925fa37b04bc345dd2f128a603bde3e9ed7c6e7"},
    {"path": "01_CAD/sweep_summary_v02.py", "sha256": "af7679c68d52563082fc82b4fcc75e62dee7e7be2ab94911eb1d49635fba250e"},
    {"path": "02_STEP_STL/od_c05_carrier_C4_v02.step", "sha256": "2aea239c16edd93100c1dedcdd82daa4fb26c45a85c9419702be87b7063efb71"},
    {"path": "02_STEP_STL/od_c05_assembly_C4_v02.step", "sha256": "a7f792a32b8085d23d93e412f49e1832e72f7842c610378bd5d8c0455ed30eaa"},
    {"path": "02_STEP_STL/od_c05_carrier_C4_v02.stl", "sha256": "d9b49b0690cebbd9029f82fca39df29f985fe3d3a70709dfb33662c9933be8ac"},
    {"path": "01_CAD/check_od_c05_carrier_v02.json", "sha256": "9db01143b1bcde1e573eee681ab25c195ae81ca7431c5507934b12f3e8f6c634"},
    {"path": "01_CAD/build_od_c05_carrier_v02.json", "sha256": "57e3711be9c289e1b1a4712b442020a58a7976da366ea26ccf1b6162b7d6cf6b"},
    {"path": "01_CAD/sections_od_c05_carrier_v02.json", "sha256": "c127996bfdc3bde6db62cde30b5f5c34b777ba4063690857f455a8dd247ffd2c"},
    {"path": "01_CAD/sweep_v02/SHA256SUMS_v02.txt", "sha256": "7512c397088f5b57cb25ff402a10efef6ea3c5d39fc67689a25e19941526af36"},
    {"path": "01_CAD/sweep_v02/summary_v02.json", "sha256": "2349eca8f591fd64797fabcaa7ba97cb5b7a77cc6117105884df24bf3931a70e"},
    {"path": "03_Sections/od_c05_carrier_y0_v02_front.png", "sha256": "e1ad969bc8178aa7a2cda58c22c9962c1cf7ad5e37a501da1070c1526f4fa4cf"},
    {"path": "03_Sections/od_c05_carrier_x0_v02_left.png", "sha256": "d5273b74d7096089fc0e90c58bfb0a3c365626b57656013ca8a2f4f873b63ffe"},
    {"path": "03_Sections/od_c05_carrier_x44_v02_left.png", "sha256": "5516d2c68ee45a35f17fa8e300b12ec1cb209d5fa256f8f3134637c066283abe"},
    {"path": "03_Sections/od_c05_carrier_x53_v02_left.png", "sha256": "2b2f8e48467bb381692f85a53bb5f06cd7cd41fad6749840e8ae9b08b2903cd9"},
    {"path": "03_Sections/od_c05_carrier_zm27p44_v02_top.png", "sha256": "3199702f7f22ee5a4986232e038fd0da2b5c481b1500bb923a7f47b3521a9dc8"},
    {"path": "03_Sections/od_c05_carrier_z178_v02_top.png", "sha256": "6c0e2a0406b5d7ba91e0c9b6732fc34c1408094216bbad3dcbfa38b600266133"},
    {"path": "03_Sections/od_c05_assembly_y0_v02_front.png", "sha256": "1dd90de7da02b81bee865695c08343e99dd28e42df5066ef0a50e7052b48ee53"},
    {"path": "03_Sections/od_c05_assembly_x0_v02_left.png", "sha256": "6e8a34ae5c2fcd2124c57ed4e677ca9fd433a0c8ad198f09b1c511d7a37ad1c8"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "cadquery-ocp-novtk 7.9.3.1.1", "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"},
  "gates": [
    {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-01", "measured": "1/1/0", "unit": "count/bool/count", "required": "1/1/0", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-02", "measured": "110.000 x 152.000 x 210.000", "unit": "mm", "required": "each +-0.1", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "envelope_within_spec", "measured": "x -55..55, y -102..50, z -29.94..180.06", "unit": "mm", "required": "each +-0.1", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-03 carrier|OD-G01", "measured": "contact 0.000; interference 0.000; offsets 0.000", "unit": "mm / mm3", "required": "= 0; <= 0; <= 0.10", "margin": 0.0, "at": "(-42.0, 50.0, -24.94)", "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "U-03 carrier|OD-G04", "measured": 5.000, "unit": "mm", "required": ">= 2.0; interference <= 0", "margin": 3.0, "at": "(21.2132, 21.2132, -24.94)", "status": "PASS_ASSUMED", "assumes": ["A-06"]},
    {"gate": "U-03b", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "U-04", "measured": "volume delta 0.000, faces delta 0, valid 1, label kept", "unit": "mm3 / count", "required": "unchanged", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-05", "measured": "24 planar, 15 cyl (13/2), 13 bores; 12 bores located", "unit": "count", "required": "plan v02 section 3", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "feature_census", "measured": "24/15/13/2/13", "unit": "count", "required": "24/15/13/2/13", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-06", "measured": 2.750, "unit": "mm", "required": ">= 2.0 (Soft)", "margin": 0.75, "at": "(-44.0, 50.0, -29.94)", "status": "PASS", "assumes": []},
    {"gate": "U-07", "measured": 0.00493, "unit": "mm", "required": "<= 0.01; angular 0.20 <= 0.2310", "margin": 0.00507, "at": "(20.8218, -21.5906, -27.44)", "status": "PASS", "assumes": []},
    {"gate": "U-08", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "D-01a", "measured": 2.750, "unit": "mm", "required": ">= 0.8", "margin": 1.95, "at": "(-44.0, 50.0, -29.94)", "status": "PASS", "assumes": []},
    {"gate": "D-01b", "measured": 2.750, "unit": "mm", "required": ">= 2.0", "margin": 0.75, "at": "(-44.0, 50.0, -29.94)", "status": "PASS", "assumes": []},
    {"gate": "D-02", "measured": "152.0 x 210.0 on the bed, 110.0 tall", "unit": "mm", "required": "<= 220 x 220, <= 250", "margin": 10.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-08"]},
    {"gate": "D-03a", "measured": 0.000, "unit": "deg", "required": ">= 45 (build +X, twelve bores excepted)", "margin": -45.0, "at": "(51.0, -98.0, 176.06) and (51.0, -32.0, -4.94); corner 3.325 at (-54.990, 44.348, -24.94)", "status": "FAIL", "assumes": ["A-13"]},
    {"gate": "D-03b", "measured": 56.569, "unit": "mm", "required": "<= 5 (crowns <= 6.6 excepted: 6.500)", "margin": -51.569, "at": "+X gusset inner faces x = 51", "status": "FAIL", "assumes": []},
    {"gate": "D-04a", "measured": 3.400, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "all eight holes", "status": "PASS", "assumes": []},
    {"gate": "D-06a", "measured": 2.750, "unit": "mm", "required": ">= 1.0", "margin": 1.75, "at": "(-44.0, 50.0, -29.94)", "status": "PASS", "assumes": []},
    {"gate": "D-07", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "E-06", "measured": "4 gussets x 3200.000", "unit": "mm3", "required": "tied, no free boss", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "REQ-01", "measured": "3.400, offset 0.000", "unit": "mm", "required": "3.4 +-0.1, <= 0.10", "margin": 0.1, "at": "(+-44, +-44)", "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "REQ-02", "measured": "6.500 x 2.000, coaxial 0.000", "unit": "mm", "required": "6.5 +-0.1, 2.0 +-0.1", "margin": 0.1, "at": "(+-44, +-44)", "status": "PASS_ASSUMED", "assumes": ["A-09"]},
    {"gate": "REQ-03", "measured": "top -29.940, underside -24.940", "unit": "mm", "required": "+-0.10", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "REQ-04", "measured": 30.000, "unit": "mm", "required": ">= 30.0 every 10 deg; 42.43 at 0 deg", "margin": 0.0, "at": "(10.2606, 28.1908, -29.9)", "status": "PASS_ASSUMED", "assumes": ["A-06"]},
    {"gate": "REQ-05", "measured": "180.060; 4.000 thick", "unit": "mm", "required": "+-0.10; 4.0 +-0.1", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-03", "A-04"]},
    {"gate": "REQ-06", "measured": "3.400, offset 0.000", "unit": "mm", "required": "3.4 +-0.1, <= 0.10", "margin": 0.1, "at": "(+-35, -72 / -92)", "status": "PASS_ASSUMED", "assumes": ["A-04"]},
    {"gate": "REQ-07", "measured": -102.000, "unit": "mm", "required": ">= -102.0", "margin": 0.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-05"]},
    {"gate": "REQ-08", "measured": "gussets 1.000; wall 2.000", "unit": "mm", "required": ">= 1.0; >= 2.0", "margin": 0.0, "at": "(-50.0, -42.0, -24.94); (-42.0, -50.0, -24.94)", "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "REQ-09", "measured": null, "unit": "", "required": "Soft bench: no visible flex", "margin": null, "at": null, "status": "INCONCLUSIVE", "assumes": ["A-11"]}
  ],
  "sweep": [
    {"parameter": "hole_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "REQ-01 diameter", "worst_margin": 0.0},
    {"parameter": "hole_xy", "values": [43.95, 44.0, 44.05], "all_built": true, "worst_gate": "REQ-01 offset", "worst_margin": 0.05},
    {"parameter": "cb_d", "values": [6.4, 6.5, 6.6], "all_built": true, "worst_gate": "D-03b crown span (exception)", "worst_margin": 0.0},
    {"parameter": "cb_depth", "values": [1.9, 2.0, 2.1], "all_built": true, "worst_gate": "REQ-02 depth", "worst_margin": 0.0},
    {"parameter": "hub_r", "values": [30.0, 30.1], "all_built": true, "worst_gate": "REQ-04", "worst_margin": 0.0},
    {"parameter": "wall_y_front", "values": [-52.0, -52.1], "all_built": true, "worst_gate": "REQ-08 wall", "worst_margin": 0.0},
    {"parameter": "foot_t", "values": [3.9, 4.0, 4.1], "all_built": true, "worst_gate": "REQ-05 thickness", "worst_margin": 0.0},
    {"parameter": "foot_y_rear", "values": [-102.0, -101.9], "all_built": true, "worst_gate": "U-02 size_y", "worst_margin": 0.0},
    {"parameter": "foot_hole_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "REQ-06 diameter", "worst_margin": 0.0},
    {"parameter": "foot_hole_x", "values": [34.95, 35.0, 35.05], "all_built": true, "worst_gate": "REQ-06 offset", "worst_margin": 0.05},
    {"parameter": "foot_hole_y", "values": [-0.05, 0.0, 0.05], "all_built": true, "worst_gate": "REQ-06 offset", "worst_margin": 0.05},
    {"parameter": "gusset_x_in", "values": [51.0, 51.1], "all_built": true, "worst_gate": "REQ-08 gussets", "worst_margin": 0.0}
  ],
  "least_sure": [
    "Whether a 40 x 40 triangular ceiling bridged 56.6 is acceptable under a named exception; its droop eats the 1.0 gusset gap",
    "REQ-09: hand estimate about 5 deg of wall rotation under a 50 N push at the axis; visible flex likely (risk HIGH)",
    "REQ-07 and REQ-08 at margin 0.000 by construction; FDM growth takes the 1.0 gusset gap to about 0.8 to 0.9"
  ],
  "stopped": true
}
```

Every row in the JSON block's `gates` except D-03a and D-03b passes, is N/A by its own row, or is the Soft REQ-09 bench gate. In every sweep run the D-03a and D-03b rows read the same as at nominal: 0.000° and 56.569 mm.
