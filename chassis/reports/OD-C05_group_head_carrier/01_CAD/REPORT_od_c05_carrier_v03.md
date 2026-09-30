# REPORT — od_c05_carrier v03 (20260930-od-c05-group-head-carrier)

Designer: Claude Code, Opus 5.5 · spec version 2.1 · plan `01_CAD/DESIGN_PLAN_v02.md` with the WP-06 amendments · brief WP-06 (J3, build attempt 2 of 2, fix_cycles 3) · 2026-09-30 UTC

**Outcome: STOPPED (D9).** D-03a and D-03b (Hard) cannot be met by the spec 2.1 geometry in the spec 2.1 print orientation (plate on the bed, build direction +Z). Two features are drawn as they would print foot-down, but the part prints plate-down, so in the print they are upside down: (1) the **rear window's flat top edge at z +160** is a 20 × 4 ceiling at **0.000°**, bridging **20.000**; (2) the **foot's tent ridge** (y −80, z +154.06) is the lowest line of an inverted V, so its first layer starts in the air and bridges **102.000** between the side walls. The 45° tent faces themselves read 45.000°. §10 gives the options. Every other §5 row passes on the build and in every sweep run, except the Soft U-06 at one sweep rung (§4).

`01_CAD/check_od_c05_carrier_v03.py` measures every number below from the re-imported STEP files (`01_CAD/check_od_c05_carrier_v03.json`). The exceptions are rows that say they come from the build log (`01_CAD/build_od_c05_carrier_v03.json`). These self-checks clear no HARD gate; only the reviewer's measurement does.

The input hashes match the brief (WP-06 → WP-03): OD-G01 f8865cd1…4407b02, OD-G04 19b4a140…98d6ad2; the v02 plan c580be8d…4cba6bf. Spec `00_Spec/DESIGN_SPEC.md` read at fb1885a8…b859095a (version 2.1). Every v01 and v02 file is untouched.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c05_carrier_v03.py` | fca3301796906bdc4c8a975406d1cd5163cada8ae774fb6e5853c4a447f911bd | parametric script (Algebra mode, one Params structure) |
| `01_CAD/check_od_c05_carrier_v03.py` | 036cd4f2b519ff4afeb147f1c4ab02ecfeaf53edacc2d067b797168218b36567 | checks, written before the build (D3) |
| `01_CAD/sections_od_c05_carrier_v03.py` | 0a54cb584872723ecab1a128768df5090c05afc330c2e30d5ea92762f113a44c | D6 sections from the exported STEP files |
| `01_CAD/sweep_od_c05_carrier_v03.py` | 79b1f2c245ff8cdb09a451ed87f3a44db81c98e22c9e562abed6b78952142386 | D7 sweep driver |
| `01_CAD/sweep_summary_v03.py` | 847d23fc0db2acac131cf45e983240a3e89d3a797937b6f980576eca8c2c106c | sweep summary and SHA256SUMS writer |
| `02_STEP_STL/od_c05_carrier_C4_v03.step` | e60c40952bfb34ee69992b99b81b4ef429735f0b41d7a20087f432492dc61abc | AP242 (`tools.core.write_step`), label `od_c05_carrier`, re-imported for every measurement |
| `02_STEP_STL/od_c05_assembly_C4_v03.step` | cd0f36cf91cdb20b39f02793ab3faa88994e9da0ae7923328f4a363bfe3a21fd | AP242 check assembly: carrier + OD-G01 (identity) + OD-G04 (+6.05° about Z, then z −6.82) |
| `02_STEP_STL/od_c05_carrier_C4_v03.stl` | 952cfa5bdc2c1c869a2da947c7671a1fb8d2d9532c4f3048d0a22e1a1fd13cc9 | binary STL from the re-imported STEP, cached triangulation cleared; tol 0.01 mm / angular 0.20 rad; 5232 triangles; volume 414197.350 mm³; bbox (−55.0, −102.0, −29.94) … (55.0, 50.0, 180.06) |
| `01_CAD/check_od_c05_carrier_v03.json` | 8a6dbd7ae1489a8892bd3a7abccc1fa1b27a204bf1299fa2a377b1a36474480a | check results: every gate row and the facts (downward-face list, flat faces, valley edges) |
| `01_CAD/build_od_c05_carrier_v03.json` | 6d0fb8a85f036dea983f252a023512c67f9bb92fc3981bb9736f06cee6592e2f | build log: parameters, derived values, export round trip, STL writer detail |
| `01_CAD/sections_od_c05_carrier_v03.json` | 57319e2860222e7a7b75b6b53470653d84945b1bc11ebab29ec9731e2623885e | section log: plane, point, nothing_clipped |
| `01_CAD/sweep_v03/SHA256SUMS_v03.txt` | c2ef897b869dc7d6406db39febdab4176488b13354e4a54ec7a7f2054fe03669 | SHA-256 of every other sweep file |
| `01_CAD/sweep_v03/summary_v03.json` | 6cef08afdb93d960d3fcda1d84321d0c839d86164bc56f4062d30d0f263faa3b | per run: one solid, rows not passing, worst margin per gate |
| `03_Sections/od_c05_carrier_y0_v03_front.png` | 45b138f530192de08f58a74c7a301364032d9e34c934cbe967afe975c8e49a59 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_ym80_v03_front.png` | 45d50166499bd87a6a8ad7f84f29c7fdab136981b6f22f54d806c677a9c5abc0 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x0_v03_left.png` | 4d82d0bea354fa1709d08f109849957d20788b48a42ccee0417f765a7395e115 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x35_v03_left.png` | 519c85d9bc425b72652fdcfbb7851b8a0fdd02df44132f48b9ce3c1ea4445a74 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_x53_v03_left.png` | 855c8a16718ba1430a8c1a446eb7ed8410f5b964424a9c7db0dd032084ae4bea | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_zm27p44_v03_top.png` | af74a5e968bdd53be40cb097994dc06682af5a853c783a1d886ea6e42b79f636 | section, nothing_clipped 0 |
| `03_Sections/od_c05_carrier_z165_v03_top.png` | 0b62bb8b8875965b9aef8a99fa3111926fa00f7a9be3447e52251e7decc357e6 | section, nothing_clipped 0 |
| `03_Sections/od_c05_assembly_y0_v03_front.png` | 732b7ad434971f6afd2f767d448cb9578eb2407dca59231fd0ed7453ba919cb5 | section, nothing_clipped 0 |
| `03_Sections/od_c05_assembly_x0_v03_left.png` | e23ed10697d3ccf8a407a9a51babd288b77d1d88da10f215b2db3f94a01970ff | section, nothing_clipped 0 |

The section images draw +Z upward on the page. That is the print orientation (the bed at the bottom of the page, the plate on it) and the machine upside down.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · OCCT 7.9.3 · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (tools used unmodified)

## 3. Gate self-check

The band is from GATES.md §0: 0.005 mm, 0.001°, 0.001 mm³, and 0 for counts and 1/0 facts. U-07's angular tolerance uses 0.00002 rad. Limits come from spec 2.1 §5 only. Margins are signed and positive inside the limit, so a pass inside the band shows its small negative margin.

**U-05 census, predicted from the spec 2.1 feature list before the build (brief), then measured:**
- 36 planar faces: plate top z −29.94 (1); plate underside z −24.94, in front of the column and inside it (2); plate front edge y +50 (1); side faces x ±55, each one face over plate, side wall, front wall end and gusset (2); rear face y −102 over plate, rear wall and foot (1); foot underside z +180.06 (1); front wall front face y −52 (1); front wall rear face y −58 (1); rear wall inner face y −98 (1); side wall inner faces x ±51 (2); tent faces (2); hatch flats (4); rear window: top, two sides, two gable flats (5); gusset inner faces x ±51 (2); gusset hypotenuses (2); counterbore floors, 4 plate at z −27.94 and 4 foot at z +176.06 (8).
- 21 cylindrical faces, all concave: 4 Ø3.4 plate holes, 4 Ø6.5 plate counterbores, 4 Ø3.4 foot holes, 4 Ø6.5 foot counterbores, the R 30 hub window (one full face), the 4 R 4 hatch corners.
- 17 bores (the 16 along Z and the hub window); the 4 hatch corners are 90° concave arcs, not bores (`bore_census` concave_arcs 4).
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
| U-05 / feature_census | 36 planar, 21 cylindrical (21 concave, 0 convex), 17 bores, no other kind; the 16 bores along Z located one by one | predicted above: 36 / 21 / 21 / 0 / 17 | 0 | §5 below | PASS | — |
| U-06 (Soft) | 2.750 mm | ≥ 2.0 | +0.750 | (−44.0, 50.0, −29.94), plate counterbore to the plate's front edge; the 45° knife edges at the foot counterbore rims sit exactly on the reading's 45° opposition and are not counted (§4: 0.027 at y_rear −101.9) | PASS (at nominal only) | — |
| U-07 | sagitta 0.00499 mm (B-rep re-meshed at the export settings); STL 1 body, 0 naked edges, winding 1; angular 0.20 rad | tol 0.01, angular ≤ 0.2310 rad, sagitta ≤ 0.01 | +0.00501 | — | PASS | — |
| U-08 | — | threaded parts only | — | — | N/A: no threads, by its row | — |
| D-01a | 2.750 mm | ≥ 0.8 | +1.950 | (−44.0, 50.0, −29.94) | PASS | — |
| D-01b | 2.750 mm | ≥ 2.0 | +0.750 | same | PASS | — |
| D-02 | 110.0 × 152.0 on the bed, 210.0 tall | ≤ 220 × 220, ≤ 250 | +110.0, +68.0, +40.0 | plate top z −29.94 on the bed | PASS (assumed: A-08) | A-08 |
| **D-03a** | **0.000°** outside the named exception (`overhang_census(build_dir=(0,0,1))`, 473 samples below 45°, sampling bound 0.000°); analytic listing: one face at 0.000°, the two tent faces at 45.000° | ≥ 45° | **−45.000** | rear window top face z +160.0, x −10 … +10, y −102 … −98, centre (0.0, −100.0, 160.0), 80.000 mm² | **FAIL** | A-13 |
| **D-03b** | **102.000 mm** outside the named exception: the tent ridge, a line where both 45° faces rise away (first layer in the air, carried only at the side walls x ±51); also the rear window top, carried on 2 of its 4 edges (x ±10), span **20.000** | ≤ 5 | **−97.000** (ridge); −15.000 (window) | ridge (−51 … 51, −80.0, 154.06); window top centre (0.0, −100.0, 160.0) | **FAIL** | — |
| D-03a / D-03b named exception | 8 counterbore floors found by position (4 at z −27.94 on (±44, ±44), 4 at z +176.06 on (±35, −72 / −92)); least 0.000° (flat rings, as the exception says); counterbore bridged Ø6.500 | reported apart; ≤ 6.6 | +0.100 (span) | as listed | inside the named exception | A-13 |
| D-04a | 3.400 mm (all eight) | ≥ 3.25 | +0.150 | (±44, ±44); (±35, −72 / −92) | PASS | — |
| D-06a | 2.750 mm | ≥ 1.0 | +1.750 | (−44.0, 50.0, −29.94) | PASS | — |
| D-07 | — | fit bores only | — | — | N/A: clearance holes only, by its row | — |
| E-06 | two front gussets, each 3200.000 mm³ (40 × 40 / 2 × 4), inner faces at \|x\| 51; the plate's rear part is the column's lid; one solid | plate tied to the column, no free boss | 0 | x ±(51 … 55), y −52 … −12, z −24.94 … 15.06 | PASS | — |
| REQ-01 | Ø3.400, through, 3.000 long, offset 0.000 from nominal and from the OD-G01 inserts | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-01) | A-01 |
| REQ-02 | Ø6.500 × 2.000 deep, open at z −29.940, coaxial 0.000 | Ø6.5 ± 0.1, 2.0 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-09) | A-09 |
| REQ-03 | top z −29.940 (min_z and the four counterbore ends); underside z −24.940 (counterbore start + 2.000 + 3.000) | ± 0.10 | +0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-04 | innermost material on the whole ray 30.000 mm over 36 angles × 5 levels (180 rays); θ 0°, 90°, 270° each 30.000 (round, no gable) | ≥ 30.0 at every 10° | −3.6e-15 (inside the band) | least at θ 10°, z −29.9 (29.5442, 5.2094) | PASS (assumed: A-06) | A-06 |
| REQ-05 | underside z 180.060 (max_z); 4.000 of foot under each head (each foot hole's length, z 176.06 … 180.06); counterbore floors z 176.060 | ± 0.10; 4.0 ± 0.1; 176.06 ± 0.10 | +0.100 | (±35, −72 / −92) | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-06 | holes Ø3.400 through, offset 0.000; counterbores Ø6.500, coaxial 0.000, floors z 176.060 (from the tent face: 17.25 long at y −72, 13.33 at y −92 along the cylinder's highest rim line; 14.0 and 10.0 at the axis) | Ø3.4 ± 0.1, ≤ 0.10; Ø6.5 ± 0.1; 176.06 ± 0.10 | +0.100 | (±35, −72), (±35, −92) | PASS (assumed: A-04) | A-04 |
| REQ-07 | min_y −102.000 | ≥ −102.0 | 0.000 | plate, column and foot rear face | PASS (assumed: A-05) | A-05 |
| REQ-08 | housing to the front gussets 1.000 mm; housing to the front wall 2.000 mm (plate contact reported under U-03) | ≥ 1.0; ≥ 2.0 | 0.000; 0.000 | housing (−50.0, −42.0, −24.94) to gusset face x −51; housing (−42.0, −50.0, −24.94) to wall face y −52 | PASS (assumed: A-01) | A-01 |
| REQ-09 (Soft) | — | no visible flex (bench) | — | — | INCONCLUSIVE (Soft bench gate, answered by the first print; risk MEDIUM, §9) | A-11 |

REQ-08 method: the carrier re-imported from the STEP is cut by position below the contact plane (z > −24.94) into the front piece (y > −52, the two gussets, 6400.000 mm³) and the column piece (y < −52, 351433.945 mm³). `clearance` of OD-G01 to each is measured with the nearest points.

D-03a analytic angles (RV01 F3): the two tent faces are 45.000000000° (normals (0, ±1, −1)/√2 against +Z) and are counted by the census without a sampling bound, since the least lies elsewhere (0°). The rear window's gable flats face up in this print (normal components +Z) and are not downward faces. The hub window, hatch, holes, counterbore walls and all walls are vertical prisms.

D-03b method (job code, §7): a flat downward face (under 1°) is carried on an edge where a point 0.05 below and 0.05 outside the edge's midpoint is in the solid; its span is twice the largest distance from a point of the face to its nearest carried edge. A valley edge is a straight edge between two planar downward faces that both rise away from it along +Z; its first layer is a strand in the air, carried at its ends, and its span is its length. The census cannot see a valley: it is an edge, not a face, and both faces beside it read 45.000°.

## 4. Robustness sweep (D7)

23 runs into `01_CAD/sweep_v03/`, each built and checked with the same predicates (`01_CAD/sweep_v03/summary_v03.json`). Every run built one valid solid with the predicted census (36 / 21 / 21 / 0 / 17). In **every** run, nominal included, D-03a reads 0.000° (both predicates) and D-03b reads 102.000 mm: no swept parameter touches the rear window or the tent ridge. The one other row not passing in any run is U-06 (Soft) at `y_rear_hi` (below). The table gives the gate each parameter moves and its worst margin among passing rows.

| Parameter | Low · nominal · high | All built, one solid | Worst passing gate | Worst margin |
|---|---|---|---|---|
| hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 Ø at the tolerance ends; D-04a at 3.3 | 0.000; +0.050 |
| hole_xy | 43.95 · 44.00 · 44.05 (all four together) | yes | REQ-01 offset 0.071 (diagonal, from nominal and from the OD-G01 inserts); D-01b 2.700 at 44.05 | +0.029; +0.700 |
| cb_d | 6.4 · 6.5 · 6.6 | yes | REQ-02 Ø at the tolerance ends; D-03b exception span 6.600 at 6.6; D-01b 2.700 at 6.6 | 0.000; 0.000; +0.700 |
| cb_depth | 1.9 · 2.0 · 2.1 | yes | REQ-02 depth at the tolerance ends; REQ-03 underside −24.940 | 0.000; +0.100 |
| hub_r | 30.0 · 30.1 (one-sided) | yes | REQ-04 innermost 30.100; OD-G04 clearance 5.000 | +0.100; +3.000 |
| wall_y_front | −52.0 · −52.1 (one-sided) | yes | REQ-08 housing to front wall 2.100 | +0.100 |
| foot_t | 3.9 · 4.0 · 4.1 (underside fixed at +180.06) | yes | REQ-05 foot under the head at the tolerance ends; foot counterbore floors 176.16 / 175.96 | 0.000; 0.000 |
| y_rear | −102.0 · −101.9 (one-sided) | yes | U-02 size_y 151.900; REQ-07 −101.900 | 0.000; +0.100 |
| foot_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-06 Ø at the tolerance ends; D-04a at 3.3 | 0.000; +0.050 |
| foot_cb_d | 6.4 · 6.5 · 6.6 | yes | REQ-06 counterbore Ø at the tolerance ends; D-03b exception span 6.600 | 0.000; 0.000 |
| foot_hole_x | 34.95 · 35.00 · 35.05 | yes | REQ-06 hole offset and counterbore coaxial 0.050 | +0.050 |
| foot_hole_y | −72/−92 ± 0.05 together | yes | REQ-06 hole offset and counterbore coaxial 0.050 | +0.050 |
| gusset_x_in | 51.0 · 51.1 (one-sided) | yes | REQ-08 housing to gussets 1.100; E-06 volume 3120.000 as derived for 3.9 thick | +0.100; 0.000 |

**U-06 (Soft) at `y_rear_hi`: 0.027 mm** at (−35.096, −95.249, 169.420), the rear rim of a foot counterbore at y −92. The counterbores cut the tent's 45° faces vertically, so on the side of each rim toward the walls the tent face and the counterbore wall meet in a 45° knife edge (all four foot counterbores, at every rung). At nominal the wedge is exactly 45.000° and `min_wall`'s wide reading (opposition 45°) does not count it; at y_rear −101.9 the rear tent face steepens to 45.13° (the ridge stays at y −80, z +154.06), the wedge closes to 44.87°, and it is counted. The nominal U-06 PASS therefore rests on the wedge sitting exactly on the threshold. The edge is spec geometry ("a Ø6.5 counterbore from the tent face") and does not change a Hard row: D-01a, D-01b and D-06a read 2.700 … 2.800 in every run.

REQ-07 and REQ-08 sit at margin 0.000 at nominal by construction (spec values at the limit). The one-sided rungs show that each moves the right way.


## 5. Build facts

- Envelope 110.000 × 152.000 × 210.000 mm; volume 414191.036 mm³; mass 443.18 g at 1070 kg/m³ (§3, A-12); centre of mass (0.000, −66.883, 75.703).
- Fillets: none through a ladder. The four hatch corners are sketch arcs R 4.000 (measured: four concave cylinders R 4.000 about (±36, −92) and (±36, −68)); the plate's corners are square (K-4 closed).
- Derived values (build log, from the parameters): tent ridge z 154.06 at y −80.0 (45° from (−58, 176.06) and (−102, 176.06)); the tent meets the rear wall's inner face y −98 at z 172.06; rear window gable apex z 120.0.
- Placements: OD-G01 at the identity, checked by `locate_bore` (inserts (±44.000, ±44.000), hole offsets 0.000) and by the contact at z −24.94 (clearance 0.000, interference 0.000). OD-G04 rotated +6.05° about Z, then translated z −6.82 (OD-G01 REPORT v02 §5), unchanged from v02; clearance 5.000 from the window's edge at r 30.
- STL for the orchestrator's 3MF: 5232 triangles, volume 414197.350 mm³ (STL) against 414191.036 mm³ (B-rep), bounding box (−55.0, −102.0, −29.94) … (55.0, 50.0, 180.06); tol 0.01 mm, angular 0.20 rad, written from the re-imported STEP.
- Fix cycles: 0. A construction assertion in the build script (each feature's bounding box against its intended placement) caught the rear window prism extruded toward −Y on the first dry run, before any export; the extrude direction was set explicitly and the part was exported once. Every number in this REPORT comes from that one export.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | Yes in the machine: with −Z up the plate lies on the housing's rear face and the housing hangs under it, axis vertical, mouth down; the column stands behind it on the foot on the floor z +180.06 (sections x 0, assembly x 0). **No in the print:** the sections draw the print (bed at the bottom); the tent is an inverted V whose ridge hangs toward the bed, and the rear window's flat edge is on top (sections x 0, x 35). |
| P2 | Function chains | Yes: the round window (innermost r 30.000) clears the housing's openings and OD-G04 (5.000); the four holes are coaxial with the inserts (0.000); TUBE 7 can enter through the rear window, rise in the column and leave through the hatch into the window from above (A-07); the foot screws are reached through the hatch (A-14). |
| P3 | Motion clearance | Yes: no carrier motion. The front gussets stand at \|x\| ≥ 51 and y ≤ −12, behind the axis, clear of the portafilter handle, which locks toward the front (handle not modelled: a reading of the geometry). |
| P4 | Human factors | Yes, with a long driver: the housing screws are driven from above into the plate's counterbores; the foot screws are driven through the hatch (80 × 32) to counterbore floors at z +176.06, 206.0 below the plate's top face, against A-14's driver of about 200 reach (the driver needs slightly more than 206 of shank). The hatch clears the four foot screw axes at x ±35 (hatch x ±40) at y −72 and −92 (hatch y −96 … −64). |
| P5 | Absurdity | No absurdity in the machine: a closed tower behind the group head carrying a flat plate, like a Dedica's rear column. In the print, the two upside-down features are the absurdity §10 reports. |
| P6 | Floating, embedded, mirrored, upside down | One solid, interference 0 with both neighbours. **Upside down for the print:** the tent (ridge toward the bed) and the rear window's gable (on the side toward the bed, flat edge on top). In the machine they read the right way up, which is how they were specified. |

## 7. Library and tools used

- Cards: none (nothing matched in `library/INDEX.md`, as at v01 and v02).
- `tools.core`: `validity`, `write_step` (AP242), `read_step`, `compare_step`, `write_stl`, `mesh_sagitta`, `common_volume`. `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `interference`, `min_wall` (with `detail["wide"]`), `overhang_census(build_dir=(0,0,1))`, `radial_extent` (whole ray, inner), `mesh_census`, `mass_properties`; `tools.measure.sampling.Inside` (point-in-solid probes); `tools.measure.wall.load_mesh` (STL bbox, triangles, volume, reported only). `tools.drawing.write_sections`. `tools.result.gate`.
- New job code (in the check script, not the repo): the analytic downward-face list for D-03a (carried over from v02); for D-03b, the carried-edge span of a flat downward face and the valley-edge finder. No `tools/measure` function measures bridge spans or finds lines where a layer starts in the air; the gate rows D-03b says "reviewer, from sections", and the sections x 0 and x 35 show both findings.
- REQ-09 geometry and hand estimate (A-11): §9 item 2.

## 8. Deviations from the plan

Plan `DESIGN_PLAN_v02.md`, amended by WP-06 (spec 2.1). Each amendment built as the brief states:
1. Print orientation: plate top z −29.94 on the bed, build direction +Z; `overhang_census(build_dir=(0,0,1))` (plan: +X). D-02 now 110 × 152 on the bed, 210 tall.
2. Plate: y −102.0 … +50.0 (plan: −58 … +50), square corners (plan: R 6 about (±49, 44)); hub window round R 30.0 without the gable (plan: gable toward +X, apex 42.43); a hatch 80 × 32, x ±40, y −96 … −64, corners R 4.0 (new).
3. Column (new, in place of the single wall): front wall 6.0 (y −58 … −52), side walls 4.0 (\|x\| 51 … 55), rear wall 4.0 (y −102 … −98), from the plate's underside to the foot; rear window x ±10, z +130 … +160, 45° gable toward −Z, apex z +120.
4. Foot: underside z +180.06, x ±55, y −102 … −58, with the 45° tent inside (ridge y −80, z +154.06); four Ø6.5 counterbores from the tent face to floors at z +176.06 over the four Ø3.4 holes (plan: a flat 4.0 foot, no counterbores).
5. Gussets: the front pair only (plan: four).
6. Named exception: the eight counterbore floors (plan: the twelve bore crowns along Z).
7. Census: predicted in §3 above from the spec 2.1 feature list (plan §3: 24 / 15 / 13 / 2 / 13); measured as predicted.
8. Sweep: `foot_cb_d` added (REQ-06's new Ø6.5 ± 0.1); `foot_y_rear` became `y_rear` (the plate, column and foot share the rear face).
9. Sections as the brief lists them. The y = 0 plane passes in front of the column (the column is at y ≤ −52), so it cuts the plate and the hub window only; the L profile of plate, front wall and gusset is in sections x 0, x 35 and x 53.

## 9. What I am least sure of

1. **Whether the tent ridge would print at all.** It is a 102.0-long strand laid in the air between the side walls at z +154.06, then widened layer by layer at 45°. A slicer treats the first layer as a bridge; at 102 it will sag several millimetres, and every following layer builds on the sagged strand. I would not print it as specified. The census alone cannot see this (both faces read 45.000°); the valley-edge check is job code with no fixture, so the reviewer should confirm it from section x 0.
2. **REQ-09, risk MEDIUM (was HIGH at v02).** Hand estimates, ASA E ≈ 2 GPa, G ≈ 0.8 GPa. Same load case as the v02 §9 figure: 50 N along Z at the axis, 74.1 from the column section's centroid (y −74.1), over the full 205 height: the closed section's I about X ≈ 5.86e5 mm⁴ (against 1980 for the open 6 × 110 wall), rotation M·L/(E·I) ≈ 3706 × 205 / (2000 × 5.86e5) ≈ 6.5e-4 rad (0.04°), against the v02 figure of 0.08 rad (about 5°). Torsion under 10 N·m (A-11): Bredt J = 4·A_m²/Σ(s/t) with A_m 106 × 45, Σ(s/t) 66.7, J ≈ 1.37e6 mm⁴, twist ≈ 1.9e-3 rad (0.11°), matching A-11's 0.002. The column is no longer the weak part; the plate is: 5.0 thick, it cantilevers 96 from the front wall to the front screws, with the gussets only over the first 40 at its sides. Alone, under the same 50 N at the axis, it would turn by up to about 0.1 rad; screwed to the housing's 5.00 flange at four points 88 apart, it will turn much less, but I have no number for that composite.
3. **The knife edges at the foot counterbore rims (U-06, Soft).** Each Ø6.5 counterbore cut vertically into a 45° tent face leaves a 45° wedge on its rim toward the nearer wall. `min_wall` reads it as 0.027 as soon as the wedge closes below 45° (sweep rung y_rear −101.9) and not at nominal, where it is exactly 45°. It will print as a feathered lip on the rim; harmless to the screw, but the nominal U-06 PASS is on the threshold. Also exact by construction: REQ-07 and REQ-08 at margin 0.000; FDM growth of +0.1 to +0.2 takes the 1.0 gusset gap to about 0.8 to 0.9.

## 10. Stop

**Gate: D-03a (Hard), with D-03b (Hard).** Measured on `02_STEP_STL/od_c05_carrier_C4_v03.step` with build direction +Z (spec 2.1 §5 D-03a, §4, A-13).

- **K-6, the rear window's top edge.** Spec 2.1 puts the 45° gable toward −Z (apex z +120) and the rectangle's flat edge at z +160. Printing +Z from the plate, the gable is on the side toward the bed, where it is not needed, and the flat edge is on top: a downward face at **0.000°** (D-03a ≥ 45°, margin −45.000), 20.0 × 4.0 = 80.000 mm² at (0.0, −100.0, 160.0), carried only at x ±10, bridge **20.000** (D-03b ≤ 5, margin −15.000).
- **K-7, the tent's ridge.** Spec 2.1 makes the foot 4.0 at the walls and 26.0 at the ridge (ridge toward −Z, the machine's up). Printing +Z, the ridge is the tent's lowest line: the two 45° faces rise away from it toward the walls, so the first layer at z +154.06 is a strand in the air across the column's inside, carried only at the side walls x ±51, bridge **102.000** (D-03b ≤ 5, margin −97.000). The census reads the faces at 45.000° and the gate threshold is met face by face; the failure is the valley line between them. Spec 2.1 §4 ("prints without a ceiling") and D-03b ("the tent has no bridge") are contradicted by this measurement.
- Cause, common to both: they are drawn right way up for the machine (−Z up) but the print is upside down with respect to the machine (plate on the bed, build +Z). No other feature is affected: every other downward face is a named-exception counterbore floor.

No fix cycle can clear K-6 or K-7 without changing a spec value (the window's gable direction, the tent's direction or the print orientation) or the named exception. Fix cycles used: 0 of 3. This was build attempt 2 of 2.

Trade-off options for the Usta and Oğuz (none taken by the designer):
- K-6, rear window:
  1. Turn the gable toward +Z (spec change): rectangle z +130 … +160 with the apex at z +170 (the rear wall runs to +180.06 and the tent meets its inner face at +172.06, so the wall stays whole above the apex), or keep the apex inside the old extent: rectangle z +120 … +150, apex z +160. The window then prints as a pointed arch, no bridge. The tube opening's size is unchanged.
  2. Make it a round or teardrop hole (point toward +Z), for example Ø20 with a 45° point.
  3. Extend the named exception to a 20.0 bridge (a short, usual FDM bridge; a slight sag on the window's top edge, a tube opening, not a fit).
- K-7, tent:
  1. Turn the tent over (spec change): an A-roof whose ridge points toward +Z, for example 45° faces from the front wall's rear face (y −58) and the rear wall's inner face (y −98), both at z +154.06, up to a ridge along X at y −78, z +174.06. The foot is then 6.0 thick at the ridge and 26.0 at the walls, and each layer is carried by the one below. The counterbores at y −72 and −92 then start from the roof at z +168.06 and +160.06 and keep their floors at z +176.06 (4.0 of foot under the heads). The ridge height and position are spec values to set, not a designer's choice.
  2. A tent with its ridge along Y (at x 0) fails the same way, mirrored; only turning the V over clears it.
  3. Print foot-down (build −Z): the tent and the window then print correctly, but the plate's underside inside the column (a 102 × 40 lid) and the plate's front part (a 102 × 110 cantilever over the housing) become 0° ceilings. Worse; not recommended.
  4. Extend the named exception to a 102.0 bridge. Not recommended (§9 item 1).

The cheapest route is K-6 option 1 with K-7 option 1: two local changes to spec §4, no change to any other gate, the scripts and sweep carry over (the parameters `win_z_lo`, `win_z_hi`, the gable direction, and the tent's two planes are already named values in the build script). Every other Hard row passes at nominal and in every sweep run.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20260930-od-c05-group-head-carrier",
  "part": "od_c05_carrier",
  "tag": "v03",
  "spec_version": "2.1",
  "files": [
    {
      "path": "01_CAD/build_od_c05_carrier_v03.py",
      "sha256": "fca3301796906bdc4c8a975406d1cd5163cada8ae774fb6e5853c4a447f911bd"
    },
    {
      "path": "01_CAD/check_od_c05_carrier_v03.py",
      "sha256": "036cd4f2b519ff4afeb147f1c4ab02ecfeaf53edacc2d067b797168218b36567"
    },
    {
      "path": "01_CAD/sections_od_c05_carrier_v03.py",
      "sha256": "0a54cb584872723ecab1a128768df5090c05afc330c2e30d5ea92762f113a44c"
    },
    {
      "path": "01_CAD/sweep_od_c05_carrier_v03.py",
      "sha256": "79b1f2c245ff8cdb09a451ed87f3a44db81c98e22c9e562abed6b78952142386"
    },
    {
      "path": "01_CAD/sweep_summary_v03.py",
      "sha256": "847d23fc0db2acac131cf45e983240a3e89d3a797937b6f980576eca8c2c106c"
    },
    {
      "path": "02_STEP_STL/od_c05_carrier_C4_v03.step",
      "sha256": "e60c40952bfb34ee69992b99b81b4ef429735f0b41d7a20087f432492dc61abc"
    },
    {
      "path": "02_STEP_STL/od_c05_assembly_C4_v03.step",
      "sha256": "cd0f36cf91cdb20b39f02793ab3faa88994e9da0ae7923328f4a363bfe3a21fd"
    },
    {
      "path": "02_STEP_STL/od_c05_carrier_C4_v03.stl",
      "sha256": "952cfa5bdc2c1c869a2da947c7671a1fb8d2d9532c4f3048d0a22e1a1fd13cc9"
    },
    {
      "path": "01_CAD/check_od_c05_carrier_v03.json",
      "sha256": "8a6dbd7ae1489a8892bd3a7abccc1fa1b27a204bf1299fa2a377b1a36474480a"
    },
    {
      "path": "01_CAD/build_od_c05_carrier_v03.json",
      "sha256": "6d0fb8a85f036dea983f252a023512c67f9bb92fc3981bb9736f06cee6592e2f"
    },
    {
      "path": "01_CAD/sections_od_c05_carrier_v03.json",
      "sha256": "57319e2860222e7a7b75b6b53470653d84945b1bc11ebab29ec9731e2623885e"
    },
    {
      "path": "01_CAD/sweep_v03/SHA256SUMS_v03.txt",
      "sha256": "c2ef897b869dc7d6406db39febdab4176488b13354e4a54ec7a7f2054fe03669"
    },
    {
      "path": "01_CAD/sweep_v03/summary_v03.json",
      "sha256": "6cef08afdb93d960d3fcda1d84321d0c839d86164bc56f4062d30d0f263faa3b"
    },
    {
      "path": "03_Sections/od_c05_carrier_y0_v03_front.png",
      "sha256": "45b138f530192de08f58a74c7a301364032d9e34c934cbe967afe975c8e49a59"
    },
    {
      "path": "03_Sections/od_c05_carrier_ym80_v03_front.png",
      "sha256": "45d50166499bd87a6a8ad7f84f29c7fdab136981b6f22f54d806c677a9c5abc0"
    },
    {
      "path": "03_Sections/od_c05_carrier_x0_v03_left.png",
      "sha256": "4d82d0bea354fa1709d08f109849957d20788b48a42ccee0417f765a7395e115"
    },
    {
      "path": "03_Sections/od_c05_carrier_x35_v03_left.png",
      "sha256": "519c85d9bc425b72652fdcfbb7851b8a0fdd02df44132f48b9ce3c1ea4445a74"
    },
    {
      "path": "03_Sections/od_c05_carrier_x53_v03_left.png",
      "sha256": "855c8a16718ba1430a8c1a446eb7ed8410f5b964424a9c7db0dd032084ae4bea"
    },
    {
      "path": "03_Sections/od_c05_carrier_zm27p44_v03_top.png",
      "sha256": "af74a5e968bdd53be40cb097994dc06682af5a853c783a1d886ea6e42b79f636"
    },
    {
      "path": "03_Sections/od_c05_carrier_z165_v03_top.png",
      "sha256": "0b62bb8b8875965b9aef8a99fa3111926fa00f7a9be3447e52251e7decc357e6"
    },
    {
      "path": "03_Sections/od_c05_assembly_y0_v03_front.png",
      "sha256": "732b7ad434971f6afd2f767d448cb9578eb2407dca59231fd0ed7453ba919cb5"
    },
    {
      "path": "03_Sections/od_c05_assembly_x0_v03_left.png",
      "sha256": "e23ed10697d3ccf8a407a9a51babd288b77d1d88da10f215b2db3f94a01970ff"
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
      "required": ">= 2.0 (Soft); sweep y_rear_hi reads 0.027 at a foot counterbore rim",
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
      "measured": 0.0,
      "unit": "deg",
      "required": ">= 45 (build +Z, eight counterbore floors excepted)",
      "margin": -45.0,
      "at": "rear window top face (0.0, -100.0, 160.0)",
      "status": "FAIL",
      "assumes": [
        "A-13"
      ]
    },
    {
      "gate": "D-03b",
      "measured": 102.0,
      "unit": "mm",
      "required": "<= 5 (counterbore floors <= 6.6 excepted: 6.500)",
      "margin": -97.0,
      "at": "tent ridge (-51..51, -80.0, 154.06); rear window top 20.000",
      "status": "FAIL",
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
      "measured": "holes 3.400 offset 0.000; cb 6.500 coaxial 0.000, floors 176.060",
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
      "worst_gate": "U-02 size_y (U-06 Soft FAIL 0.027 at -101.9, knife edge at a foot counterbore rim)",
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
  "least_sure": [
    "The tent ridge: a 102.0 strand laid in the air between the side walls; the census cannot see it (both faces 45.000 deg); the valley-edge check is job code without fixtures",
    "REQ-09 risk MEDIUM: the closed column is about 120 times stiffer than the v02 wall (6.5e-4 rad against 0.08 rad); the 5.0 plate cantilevering 96 to the front screws is now the compliant part",
    "U-06 (Soft): 45 deg knife edges at the foot counterbore rims read 0.027 once the wedge closes below 45 deg (sweep y_rear -101.9); the nominal PASS sits on the threshold; REQ-07 and REQ-08 at margin 0.000 by construction"
  ],
  "stopped": true
}
```

