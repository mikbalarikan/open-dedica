# REPORT — od_c11_back v01 (20261001-od-c11-back-panel)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · plan `01_CAD/DESIGN_PLAN.md` · 2026-10-01 UTC · brief WP-02, build attempt 1 of 2, fix cycles used 0 of 3 · outcome STOPPED (section 10)

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 83422ec39aec1276e2f24e41550686ba1e43e74bb195622457f45d26a1c4371b | the plan (D2) |
| `01_CAD/probe/probe_placements_v01.py` | 84b393b69e9862b71dbd42754042273abbddfa0d0182e4678eaeffba4d5d79ff | D2 probe of the plate and the placed neighbours |
| `01_CAD/probe/probe_placements_v01.json` | 1adaad3a686be702f1ac1231a94facc081084067b26d1274d61becc65418cd10 | its results |
| `01_CAD/probe/versions_v01.py` | 06ff355b92cf96f5b7388ad2c303837d84f9ec911ee1c8632e2438cf5ad81c6d | D0 versions |
| `01_CAD/build_od_c11_back.py` | 1e719c5f6ff33869188874dd8d236578eca6ac9157342a37eba1510e6ccfa05c | parametric script, every §4 value a named parameter |
| `01_CAD/check_od_c11_back.py` | 7a041c291dcaeec372c5d5fb57842121d7e0f496607fc8bebd60904f5553fb09 | checks, written before the build (D3) |
| `01_CAD/build_record_v01.json` | 19926f8b40684a61208fe6f29ce273aa1859cac80f8c7d56737224d68022af0c | parameters, export hashes, STL settings, placements |
| `01_CAD/check_od_c11_back_v01.json` | bb323d29f3ccc469556ede3ba403d1e491fc6a5295dab67aea01d80824f91a45 | every gate row and fact, measured on the re-imported STEP files |
| `01_CAD/check_od_c11_back_v01.log` | eff16ba278e5034373a360ac0982b40a677410dbacab303db002d54da2f0835c | the same rows, one line each |
| `01_CAD/sections_od_c11_back.py` | 7be37dba3753f026dedf8966550820a0828a5179d550942df45490c66b80a3e0 | D6 sections from the re-imported STEP |
| `01_CAD/sections_v01.json` | 44b616462761b883f5b1713e872b617af59e0e9e2dc7138d66f6552fd2175078 | section planes, cut areas, nothing_clipped |
| `01_CAD/sweep_od_c11_back_v01.sh` | 5df003a81c4124bcb997f3c55d4b464942f23f10d2369149c52fee4876558589 | D7 sweep driver (15 runs into `01_CAD/sweep_v01/`) |
| `01_CAD/sweep_summary_v01.py` | 13aefc6122b701a14cee5f30486af87760b124e78168aaf30b0f42d7baf756c2 | D7 summary |
| `01_CAD/sweep_v01/sweep_summary.json` | 24577ee2a75d5f713a591303e25d90f5e5a6580bf66666e1d407338a53c909d2 | per-run solids, faces, rows not passing, worst mm margin |
| `02_STEP_STL/od_c11_back_C1_v01.step` | c9f06a48aa93293b08d0aaa4a0af0f62acdba36ff3aada3e86b169c9dad70f75 | AP242 (`tools.core.write_step`), part `od_c11_back`, re-imported for every measurement |
| `02_STEP_STL/od_c11_assembly_C1_v01.step` | 31d348eeca439c0c30929d3e220df9472c3e38f1fe8e8d6fc3153b7831377e3b | AP242 check assembly: `od_c11_back`, `od_c01_frame`, `od_c02_bulkhead`, `od_c03_cradle`, `od_h01_pump` as placed |
| `02_STEP_STL/od_c11_back_C1_v01.stl` | 5be03f3a87de47318730cc1e578c303960dcad8736d47b48a31fac5b86a51e58 | binary, meshed afresh (cached triangulation cleared); tolerance 0.01 mm / angular 0.20 rad, 3920 triangles |
| `03_Sections/od_c11_back_wall_z300p5_v01_top.png` | cc93da667d573e22fd7eeaf9911bb9b18c07d46ff21b5b05a2ce75b00c12f0a2 | z −300.5: every hole and slot through the wall |
| `03_Sections/od_c11_back_flanges_y2_v01_front.png` | b771a1084739f31510e733149b4c7b389875ff33b3521e1f955c42d7d05b84a1 | y 2: flanges, four flange holes |
| `03_Sections/od_c11_back_passthroughs_y30_v01_front.png` | 6d61c1a22dff3f8de43e521c8546af2b966839d39cf72dd7d77a6cef79ff52b2 | y 30: cord and tube holes, gussets |
| `03_Sections/od_c11_back_wall_y50_v01_front.png` | 52929dd92d2824c7d392a4a271bd3101e8deedf75e253cfa8dcf9f3a9b6f16f8 | y 50: wall plane (REQ-02) |
| `03_Sections/od_c11_back_vents_y140_v01_front.png` | 1a1cc8a168471ea6884a91a58eeff8ec7628b2c02616a660cb7b7ea3cc5df3a2 | y 140: five vent slots |
| `03_Sections/od_c11_back_wall_y200_v01_front.png` | 2b1573ce79810fb9e6246715f16d4767a137c18d76de537563a4f50274df9ae7 | y 200: wall plane (REQ-02) |
| `03_Sections/od_c11_back_bosses_y207_v01_front.png` | 5d48fe737f0dd743abe2ca5145b579be7bf6bf88baadf111bf2f8696ba465451 | y 207: the two bosses on the wall |
| `03_Sections/od_c11_back_ledge_y213_v01_front.png` | f709d6fd308198f146814b5dedcb6fac94e7b6afa246e49e7a8e622b112864a9 | y 213: ledge and the two insert bores |
| `03_Sections/od_c11_back_insert_x90_v01_left.png` | 57aecc5ea21b1793aef142d54789ca7f347a038433723ba776d8be58e007ef6c | x 90: boss, bore, ledge, wall |
| `03_Sections/od_c11_back_hole_x100_v01_left.png` | e54ac5f28cf5951dc266c600a99618d0ce7973cefc83926051ac25482756d863 | x 100: flange hole along Y, cord hole, slot |
| `03_Sections/od_c11_back_gusset_x112_v01_left.png` | c3918b8f31f0337929093571f1d3637df9d04b5f181a4f67150d24d6d67c9b42 | x 112: outer gusset |
| `03_Sections/od_c11_back_gusset_x74_v01_left.png` | ebaccad8d996d40387eb41a44769621e045e1fc0bbe8cb6138f1d3730b793f82 | x 74: inner gusset |
| `03_Sections/od_c11_back_tube_xm100_v01_left.png` | e9d3381713eef12893ccbd3fed6cb1014111a9eb7431d3940537544d60746b29 | x −100: tube hole and flange hole |
| `03_Sections/od_c11_assembly_feethole_x110_v01_left.png` | 70358f674e154634032810127128f4e99d39e26d5beb5a1ed02bcd84b3afa377 | check assembly at x 110: the flange over OD-C01's feet hole (section 10) |

Every section measured `nothing_clipped` = 0 (`01_CAD/sections_v01.json`). The sweep's 15 runs (STEP, STL, assembly, build record, check JSON and log each) are under `01_CAD/sweep_v01/<run>/`, with their STEP hashes in `sweep_summary.json`.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3) · ocpsvg 0.6.0 · repo commit 10929db1408d89144bd4af9cad971440427933d0

## 3. Gate self-check

Measured by `01_CAD/check_od_c11_back.py` on the re-imported STEP files (224 rows in the JSON: 95 PASS, 123 PASS_ASSUMED, 1 FAIL, 3 INCONCLUSIVE, 2 N/A). The table shows the worst row of each §5 ID, and shows U-03 row by row. Bands from GATES.md §0 (mm 0.005, deg 0.001, mm³ 0.001, rad 0.00002, counts and mm² 0).

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | 1 solid, brep_valid 1, naked edges 0 | 1, 1, 0 | 0 | — | PASS | — |
| U-02 | 232.000 × 215.000 × 19.000; position x −116.000 … 116.000, y 0.000 … 215.000, z −302.000 … −283.000 | each size in [spec − 0.1, spec + 0.1]; position ± 0.1 | +0.100 (each) | — | PASS | — |
| U-03 (a) plate contact | clearance 0.000; common volume 0.000 mm³ | = 0; ≤ 0 | 0 | (116, 0, −302) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) footprint inside the outline | 0.000 mm² outside; least distance to the outline 0.780 | = 0; ≥ 0.5 | +0.280 | wall corner (116, 0, −302) to the R 10 arc | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| **U-03 (a) underside wholly over plate material** | **18.158 mm² of footprint over plate holes** (of 2003.683 mm²; over material 1985.525) | = 0 | **−18.158** | the two feet holes Ø3.4 at (±110, −295), each wholly under a flange | **FAIL** | A-01, A-02, A-07 |
| U-03 (a) under each flange hole | plate material missing under a Ø3.4 plug on each measured axis 0.000 mm³; nearest existing plate hole 29.428 (x ±81) and 11.180 (x ±100) | ≤ 0; ≥ 6.0 | +5.180 | (±100, 0, −290) to (±110, −295) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) neighbours | OD-C03 48.415, OD-H01 66.117, OD-C02 43.012; common volume 0.000 mm³ each | ≥ 20.0; ≤ 0 | +23.012 | flange corner (72, 0, −283) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (b) | lowered from +40.0 to 0 in 2.0 steps (21 poses): worst common volume 0.000 mm³ with OD-C01, OD-C02, OD-C03 and OD-H01 | ≤ 0 at every step | 0 | every pose | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-04 | part: schema AP242, 1 solid, volume delta 1.9e-9 mm³, faces delta 0, label kept, valid after; assembly: 5 solids, labels kept, faces delta 0, valid after, per-child volume delta ≤ 4.3e-9 mm³ | in [0, 0] mm³; 0; 1 | −4e-9 (inside the band) | — | PASS | — |
| U-05 | planar 46, cylindrical 19 (concave 19, convex 0), cone/sphere/torus/B-spline/other 0, bores 9 (4 Ø3.400 along Y through, 2 Ø4.000 along Y blind, 3 Ø12.000 along Z through), 10 R 2.0 slot ends, 4 gusset hypotenuses, 2 boss undersides, 2 flange fronts, 3 ledge-underside pieces, 2 ledge ends, 1 wall outer face | plan §3 counts | 0 | — | PASS | — |
| U-06 (Soft) | `min_wall_wide` 3.000 (spacing 0.7) | ≥ 2.0 | +1.000 | (76, 34, −302) | PASS | — |
| U-07 | angular tolerance 0.20 rad; tolerance 0.01; max sagitta 0.00499 on a fresh re-mesh of the re-imported STEP; mesh 1 body, 0 naked edges, winding 1 | ≤ 0.23097 rad; ≤ 0.01; ≤ 0.01 | +0.00501 (sagitta) | (−105.82, 31.45, −301.25) | PASS | — |
| U-08 | no threads | N/A by its row | — | — | N/A | — |
| D-01a | `min_wall` 3.000 (spacing 0.7; the brief notes that the default spacing refuses the large faces) | ≥ 0.8 | +2.200 | (116, 0, −299) | PASS | — |
| D-01b | 3.000 | ≥ 2.0 | +1.000 | (116, 0, −299) | PASS | — |
| D-02 | 232.0 × 215.0 on the bed, 19.0 tall | ≤ 420 × 420, ≤ 500 | +188.0 | — | PASS (assumed: A-09) | A-09 |
| D-03a | 90.0° outside the named exception (the six horizontal holes refilled by position: 6 holes, 57 faces, 1 solid); whole part 0.0° (sampling bound 0.006°), only at the crowns: 4 flange-hole faces least 0.0°, 2 insert-bore faces least 0.0°, no other downward face | ≥ 45° | +45.0 | — (nothing downward off the bed) | PASS (assumed: A-08) | A-08 |
| D-03b | reviewer row; designer reading: horizontal holes bridge 3.400 and 4.000; `flat_ceiling_spans` 0.000 (no flat ceiling) | ≤ 5.0 | +1.000 | — | PASS (assumed: A-08), designer reading | A-08 |
| D-04a | 3.400 (all four) | ≥ 3.25 | +0.150 | (±81 / ±100, 0, −290) | PASS | — |
| D-05a | across X 12.000, across Z 15.000 (rays at y 210 from the measured axes) | ≥ 8.0 | +4.000 | (84 … 96, 210, −293) | PASS (assumed: A-05) | A-05 |
| D-05b | Ø4.000, depth 6.000 (both) | Ø in [3.95, 4.05]; depth in [5.9, 6.1] and ≥ 5.7 | +0.050 | (±90, 209, −293) | PASS (assumed: A-05) | A-05 |
| D-06a | 3.000 | ≥ 1.0 | +2.000 | (116, 0, −299) | PASS | — |
| D-07 | no fit-critical bores | N/A by its row | — | — | N/A | — |
| J-05 | +X 4.000, −X 4.000, +Z 4.000, −Z 7.000 (both bores) | ≥ 3.0 | +1.000 | (96, 210, −293) | PASS | — |
| E-06 | reviewer row; designer reading: one solid; each boss is a 12 × 8 × 12 block fused to the wall's inner face over 12 × 8 and to the ledge's underside over 12 × 12; each flange is fused to the wall over 42 × 4 and tied by two 4.0 gussets (16 × 30 legs) at its ends (sections x 74, x 90, x 112, y 207) | reviewer, from sections | — | — | INCONCLUSIVE (reviewer row) | — |
| E-11 | reviewer row; designer reading: the Ø12 cord hole at (95, 30) takes the grommet OD-C14 (not designed); the five slots open the wall behind the bay, each slot's centre line clear through the wall (rays found no material) (sections z −300.5, y 140) | reviewer, from sections | — | — | INCONCLUSIVE (reviewer row) | A-03, A-06 |
| REQ-01 | four holes Ø3.400, offset 0.000, length 4.000, through; underside one planar face at y 0.000 | Ø 3.4 ± 0.1; ≤ 0.10; 4.0 ± 0.1; 1 face at 0.00 ± 0.10 | +0.100 | (±81 / ±100, 0, −290) | PASS (assumed: A-01) | A-01 |
| REQ-02 | outer face −302.000 and inner face −299.000 at y 50 and y 200 (x −40, 0, 40); x −116.000 / 116.000 | ± 0.10; ± 0.1 | +0.100 | — | PASS (assumed: A-02) | A-02 |
| REQ-03 | Ø12.000, offset 0.000, through | 12.0 ± 0.1; ≤ 0.10 | +0.100 | (95, 30, −302) | PASS (assumed: A-03) | A-03 |
| REQ-04 | Ø12.000 (both), offset 0.000, through | 12.0 ± 0.1; ≤ 0.10 | +0.100 | (−100 / −84, 30, −302) | PASS (assumed: A-04) | A-04 |
| REQ-05 | max z −283.000; common volume with the box x ±70, y 0 … 100, z −299 … −250: 0.000 mm³ | ≤ −283.0; = 0 | 0.000 | — | PASS (assumed: A-07) | A-07 |
| REQ-06 | five slots: width 4.000, height 80.000, centres x 78/86/94/102/110 at 0.000 off, y 100.000 … 180.000 | ± 0.1 each | +0.100 | rays at (x_c, 140, −300.5) | PASS (assumed: A-06) | A-06 |
| REQ-07 | two bores Ø4.000, depth 6.000, offset 0.000, blind; top one planar face at y 215.000 spanning z −302.000 … −287.000 | Ø 4.0 ± 0.05; 6.0 ± 0.1; ≤ 0.10; 1 face over z −299 … −287 | +0.050 | (±90, 209, −293) | PASS (assumed: A-05) | A-05 |
| REQ-08 | common volume of the four Ø6 cylinders y 4 … 211 with the panel 0.000 mm³ (touching: clearance 0.000 at the bosses' faces x ±84 and the flange top y 4) | = 0 | 0 | — | PASS | — |
| REQ-09 (Soft) | bench gate, not geometric | answered by the first print | — | — | INCONCLUSIVE (by its row) | A-11 |
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| feature_census | as U-05 | plan §3 | 0 | — | PASS | — |
| envelope_within_spec | sizes as U-02; position min/max x, y, z each within ± 0.1 of ±116.0, 0 … 215.0, −302.0 … −283.0 (reported apart) | ± 0.1 | +0.100 | — | PASS | — |

Facts beside the gates (not gated): the four new insert sites lie 15.000 from the plate's edge (the brief's ≥ 8.0, not a §5 threshold). A straight Ø6 driver line from y 4 to y 260 on each screw axis shares 113.097 mm³ with the panel, because the ledge (z −299 … −287) lies over every screw at z −290; the same line tilted 2° toward +Z shares 0.000 mm³. Mass properties are in section 5.

## 4. Robustness sweep (D7)

Every fit-critical parameter in the plan was rebuilt at its spec tolerance limits, exported into `01_CAD/sweep_v01/<run>/` and run through the same checks. Every run built one solid of 65 faces. Every run fails `U-03 (a) underside wholly over plate material` at the same 18.158 mm², because the flanges' extent is not a swept parameter; that row is left out of the "worst" column below.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| flange_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 diameter at both ends | 0.000 (at the limit, PASS); D-04a +0.050 at low |
| flange_hole_dx (holes moved along X) | −0.1 · 0 · +0.1 | yes | REQ-01 offset 0.100 at both ends | 0.000 (at the limit, PASS); nearest plate hole 11.091 at high (+5.091) |
| insert_d | 3.95 · 4.0 · 4.05 | yes | REQ-07 / D-05b diameter at both ends | 0.000 (at the limit, PASS); J-05 3.975 at high (+0.975) |
| insert_depth | 5.9 · 6.0 · 6.1 | yes | REQ-07 / D-05b depth at both ends | 0.000 (at the limit, PASS); depth ≥ 5.7 +0.200 at low |
| pass_d | 11.9 · 12.0 · 12.1 | yes | REQ-03 / REQ-04 diameter at both ends | 0.000 (at the limit, PASS) |
| wall_z (both faces moved) | −0.1 · 0 · +0.1 | yes | **REQ-05 tank-zone box at high: FAIL, 1400.000 mm³** (the inner face at −298.9 reaches 0.1 into the box, which starts at z −299 with no tolerance); low: REQ-02 and U-02 at the limit | −1400.000 mm³ at high; 0.000 at low; footprint to outline 0.704 (+0.204) at low |
| y_top | 214.9 · 215.0 · 215.1 | yes | REQ-07 top and U-02 size_y at both ends | 0.000 (at the limit, PASS) |

Reading: the part passes at nominal and at every tolerance limit except the wall plane at its high limit. There, REQ-02's ± 0.10 on the inner face overlaps REQ-05's box edge at z −299. This comes from the spec's tolerances, not from the build, and the nominal sits exactly on REQ-05's limit (margin 0.000).

## 5. Build facts

- Envelope 232.000 × 215.000 × 19.000 mm (x −116 … 116, y 0 … 215, z −302 … −283); volume 166 041.565 mm³; mass 210.873 g at 1270 kg/m³ (A-10); centre of mass (−2.506, 109.799, −299.452).
- STL (for the orchestrator's 3MF): 3920 triangles, mesh volume 166 043.487 mm³, bounding box (−116.0, 0.0, −302.0) … (116.0, 215.0, −283.0), size 232.0 × 215.0 × 19.0; tolerance 0.01 mm, angular 0.20 rad, sagitta 0.00499 mm; one closed body.
- Fillets: none (the spec names none); the ladder was not used.
- Placements (assembly): OD-C01 and OD-C02 by RigidJoint at the identity. OD-C03 and OD-H01 by RigidJoint at `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`, a proper rotation that the probe measured as local x → (0, 0, 1), y → (0, −1, 0), z → (1, 0, 0). OD-C03's foot underside lands on y 0.000000. Probe rear-most z: OD-C03 −245.0, OD-H01 −232.2, OD-C02 −240.0.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The panel stands upright on the plate's top face along its rear edge, carried by its 3 mm foot and two 16-deep floor flanges, and prints flat on its outer face. It rests and mounts the way it is used. |
| P2 | Function chains | The cord exits on the electric side (Ø12 at x 95, behind the bay x 70 … 120). The tubes exit on the wet side toward the flowmeter on the left (Ø12 at x −100 and −84). The vents sit behind the bay (x 76 … 112, y 100 … 180). Each chain is aimed at its zone. |
| P3 | Motion clearance | No moving parts. The panel lowers along −Y onto the plate clear of every neighbour at all 21 poses (U-03 (b)). |
| P4 | Human factors | Questionable: the four screws sit under the top ledge (z −299 … −287 over the screws at z −290), so a straight driver from above meets the ledge (113.1 mm³ shared). A driver tilted 2° toward the front clears (0.0 mm³). The top panel must come off first (A-01). |
| P5 | Next to a real product | A 3 mm rear panel with grommet holes and a vent field looks like an ordinary appliance back panel. Its large unribbed field may drum (REQ-09, A-11). |
| P6 | Floating, embedded, mirrored, upside-down | Nothing floats (one solid) and nothing is embedded in the placed neighbours (common volume 0). However, each flange covers an OD-C01 feet hole, so a feet screw head or nut on the plate's top face would be embedded in the flange (section 10). |

## 7. Library and tools used

- Card: UNO10 U5 tank heat-set (size and position gated apart). Precedent: the OD-C02 scripts (the shape of the build and check scripts, the joints, refill by position).
- `tools.core`: `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`. `tools.measure`: `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, `min_wall_wide` (spacing 0.7), `overhang_census` (build +Z, spacing 0.7), `flat_ceiling_spans` (spacing 0.7), `radial_extent`, `clearance`, `mass_properties`, `mesh_census`. `tools.result.gate`. `tools.drawing.write_sections`.
- New job code (in `01_CAD/`, never in the repo): the planar-face readings (underside, top, census by position), the footprint against the plate's top face and outline (face intersection areas and wire distance), the plugs under the flange holes, the lowering path, the keep-out and driver cylinders, the refill of the six exception holes and the per-face split of the downward faces. No `tools/measure` function was missing.

## 8. Deviations from the plan

1. The gusset's leg along the flange is now derived as the flange's depth (flange_z1 − wall_z_in, 16.0 at nominal, §4) instead of being a separate 16.0 parameter. Without this, the wall-plane sweep would push a gusset tip past z −283. The change was made after the first export; the rebuilt part, STL and assembly are byte-identical to the delivered files (SHA-256 compared), and the parameter's key was removed from `build_record_v01.json`.
2. The tilted-driver fact beside REQ-08 now starts the tilted cylinder 0.1 higher, so its end cap does not dip into the flange top. The check was run again on the same files before this REPORT, and no gate changed.
3. Section files are named `<part>_<cut>_v01_<view>.png` so that several cuts along one view can coexist.

## 9. What I am least sure of

1. How to read U-03 (a), "the panel's underside lies wholly over plate material". By its parenthetical (inside the outline, ≥ 0.5 from the edge) the row passes (0.780). By its words it fails, because each flange (x ±72 … ±114, z −299 … −283) covers a Ø3.4 OD-C01 feet hole at (±110, −295) (18.158 mm² in all). I gated the words and stopped. The reviewer should judge which reading the spec means and whether the feet's fastener can sit under a flange.
2. Driver access: REQ-08 passes as written (y 4 … 211), but the ledge covers every screw axis, so assembly needs a tilted or ball-end driver. Nothing in §5 measures above y 211.
3. The REQ-02 / REQ-05 tolerance stack: with the inner face at its +0.1 limit, the wall enters the tank-zone box by 1400 mm³, and the nominal sits at REQ-05's limit with margin 0.000. REQ-08 at x ±81 is also exactly tangent to the bosses (clearance 0.000), so a boolean on another kernel build could read a sliver.

## 10. Stop

STOPPED (D9): a hard gate that the spec's own geometry cannot meet.

- Gate: U-03 (a), "the panel's underside lies wholly over plate material".
- Measured: 18.158 mm² of the panel's footprint (2003.683 mm²) lies over plate holes instead of material. These are OD-C01's two feet holes, Ø3.400 at (±110, −295), each wholly under a floor flange (flange x ±72 … ±114, z −299 … −283 per §4). Inside the outline the footprint keeps 0.780 from the edge (≥ 0.5), so only the "plate material" clause fails. The feet holes belong to OD-C15, which is not designed, and neither A-01 nor A-02 covers them. Whatever fastens a foot through that hole (a screw head or a nut on the plate's top face) would sit inside the flange.
- Not fixed: the flanges' extent and the outer gussets' position are spec §4 values. Changing them, or adding a relief, is a spec change and not a fix cycle (0 of 3 used).
- Trade-off options for the orchestrator and the Usta:
  1. Accept, reading the row by its parenthetical (footprint inside the outline), and confirm that the feet fasten from below with no hardware on the plate's top face. Record it as a signed exception. No geometry change.
  2. Add a relief pocket in each flange's underside over the feet hole, for example Ø8.0 × 2.0 deep about (±110, −295), which clears an ISO 7380 M3 head (Ø5.7 × 1.65). The footprint then no longer covers the holes. This adds two features (U-05 counts) and leaves 2.0 of flange over each pocket, under the outer gusset.
  3. Shorten the flanges so they end inboard of the feet holes (x1 ≤ ±105). The outer gussets then move inboard, and the outer flange holes move from x ±100 to stay ≥ 2.1 from the gussets. This changes the REQ-01 positions and the four new OD-C01 insert sites (A-01).
  4. Move OD-C01's feet holes clear of the flanges in the same OD-C01 revision that adds the four inserts (A-01).

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20261001-od-c11-back-panel",
  "part": "od_c11_back",
  "tag": "v01",
  "spec_version": "1.0",
  "files": [
    {"path": "01_CAD/DESIGN_PLAN.md", "sha256": "83422ec39aec1276e2f24e41550686ba1e43e74bb195622457f45d26a1c4371b"},
    {"path": "01_CAD/probe/probe_placements_v01.py", "sha256": "84b393b69e9862b71dbd42754042273abbddfa0d0182e4678eaeffba4d5d79ff"},
    {"path": "01_CAD/probe/probe_placements_v01.json", "sha256": "1adaad3a686be702f1ac1231a94facc081084067b26d1274d61becc65418cd10"},
    {"path": "01_CAD/probe/versions_v01.py", "sha256": "06ff355b92cf96f5b7388ad2c303837d84f9ec911ee1c8632e2438cf5ad81c6d"},
    {"path": "01_CAD/build_od_c11_back.py", "sha256": "1e719c5f6ff33869188874dd8d236578eca6ac9157342a37eba1510e6ccfa05c"},
    {"path": "01_CAD/check_od_c11_back.py", "sha256": "7a041c291dcaeec372c5d5fb57842121d7e0f496607fc8bebd60904f5553fb09"},
    {"path": "01_CAD/build_record_v01.json", "sha256": "19926f8b40684a61208fe6f29ce273aa1859cac80f8c7d56737224d68022af0c"},
    {"path": "01_CAD/check_od_c11_back_v01.json", "sha256": "bb323d29f3ccc469556ede3ba403d1e491fc6a5295dab67aea01d80824f91a45"},
    {"path": "01_CAD/check_od_c11_back_v01.log", "sha256": "eff16ba278e5034373a360ac0982b40a677410dbacab303db002d54da2f0835c"},
    {"path": "01_CAD/sections_od_c11_back.py", "sha256": "7be37dba3753f026dedf8966550820a0828a5179d550942df45490c66b80a3e0"},
    {"path": "01_CAD/sections_v01.json", "sha256": "44b616462761b883f5b1713e872b617af59e0e9e2dc7138d66f6552fd2175078"},
    {"path": "01_CAD/sweep_od_c11_back_v01.sh", "sha256": "5df003a81c4124bcb997f3c55d4b464942f23f10d2369149c52fee4876558589"},
    {"path": "01_CAD/sweep_summary_v01.py", "sha256": "13aefc6122b701a14cee5f30486af87760b124e78168aaf30b0f42d7baf756c2"},
    {"path": "01_CAD/sweep_v01/sweep_summary.json", "sha256": "24577ee2a75d5f713a591303e25d90f5e5a6580bf66666e1d407338a53c909d2"},
    {"path": "02_STEP_STL/od_c11_back_C1_v01.step", "sha256": "c9f06a48aa93293b08d0aaa4a0af0f62acdba36ff3aada3e86b169c9dad70f75"},
    {"path": "02_STEP_STL/od_c11_assembly_C1_v01.step", "sha256": "31d348eeca439c0c30929d3e220df9472c3e38f1fe8e8d6fc3153b7831377e3b"},
    {"path": "02_STEP_STL/od_c11_back_C1_v01.stl", "sha256": "5be03f3a87de47318730cc1e578c303960dcad8736d47b48a31fac5b86a51e58"},
    {"path": "03_Sections/od_c11_back_wall_z300p5_v01_top.png", "sha256": "cc93da667d573e22fd7eeaf9911bb9b18c07d46ff21b5b05a2ce75b00c12f0a2"},
    {"path": "03_Sections/od_c11_back_flanges_y2_v01_front.png", "sha256": "b771a1084739f31510e733149b4c7b389875ff33b3521e1f955c42d7d05b84a1"},
    {"path": "03_Sections/od_c11_back_passthroughs_y30_v01_front.png", "sha256": "6d61c1a22dff3f8de43e521c8546af2b966839d39cf72dd7d77a6cef79ff52b2"},
    {"path": "03_Sections/od_c11_back_wall_y50_v01_front.png", "sha256": "52929dd92d2824c7d392a4a271bd3101e8deedf75e253cfa8dcf9f3a9b6f16f8"},
    {"path": "03_Sections/od_c11_back_vents_y140_v01_front.png", "sha256": "1a1cc8a168471ea6884a91a58eeff8ec7628b2c02616a660cb7b7ea3cc5df3a2"},
    {"path": "03_Sections/od_c11_back_wall_y200_v01_front.png", "sha256": "2b1573ce79810fb9e6246715f16d4767a137c18d76de537563a4f50274df9ae7"},
    {"path": "03_Sections/od_c11_back_bosses_y207_v01_front.png", "sha256": "5d48fe737f0dd743abe2ca5145b579be7bf6bf88baadf111bf2f8696ba465451"},
    {"path": "03_Sections/od_c11_back_ledge_y213_v01_front.png", "sha256": "f709d6fd308198f146814b5dedcb6fac94e7b6afa246e49e7a8e622b112864a9"},
    {"path": "03_Sections/od_c11_back_insert_x90_v01_left.png", "sha256": "57aecc5ea21b1793aef142d54789ca7f347a038433723ba776d8be58e007ef6c"},
    {"path": "03_Sections/od_c11_back_hole_x100_v01_left.png", "sha256": "e54ac5f28cf5951dc266c600a99618d0ce7973cefc83926051ac25482756d863"},
    {"path": "03_Sections/od_c11_back_gusset_x112_v01_left.png", "sha256": "c3918b8f31f0337929093571f1d3637df9d04b5f181a4f67150d24d6d67c9b42"},
    {"path": "03_Sections/od_c11_back_gusset_x74_v01_left.png", "sha256": "ebaccad8d996d40387eb41a44769621e045e1fc0bbe8cb6138f1d3730b793f82"},
    {"path": "03_Sections/od_c11_back_tube_xm100_v01_left.png", "sha256": "e9d3381713eef12893ccbd3fed6cb1014111a9eb7431d3940537544d60746b29"},
    {"path": "03_Sections/od_c11_assembly_feethole_x110_v01_left.png", "sha256": "70358f674e154634032810127128f4e99d39e26d5beb5a1ed02bcd84b3afa377"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "cadquery-ocp-novtk 7.9.3.1.1", "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"},
  "gates": [
    {
      "gate": "U-01",
      "measured": 1,
      "unit": "count",
      "required": "== 1",
      "margin": 0.0,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "U-01.solid_count"
    },
    {
      "gate": "U-02",
      "measured": 232.0,
      "unit": "mm",
      "required": "in [231.9, 232.1]",
      "margin": 0.1,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "U-02.size_x"
    },
    {
      "gate": "U-03",
      "measured": 18.158405537748877,
      "unit": "mm2",
      "required": "<= 0.0",
      "margin": -18.158405538,
      "at": "feet holes D3.4 at (+-110, -295) under the flanges",
      "status": "FAIL",
      "assumes": [
        "A-01",
        "A-02",
        "A-07"
      ],
      "worst_row": "U-03.footprint_over_plate_holes_area"
    },
    {
      "gate": "U-04",
      "measured": 4.307366907596588e-09,
      "unit": "mm3",
      "required": "in [0.0, 0.0]",
      "margin": -4e-09,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "U-04.assembly.od_h01_pump.volume_delta"
    },
    {
      "gate": "U-05",
      "measured": 46,
      "unit": "count",
      "required": "== 46",
      "margin": 0.0,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "U-05.plane_faces"
    },
    {
      "gate": "U-06",
      "measured": 3.0,
      "unit": "mm",
      "required": ">= 2.0",
      "margin": 1.0,
      "at": "(76.0000, 34.0000, -302.0000) mm",
      "status": "PASS",
      "assumes": [],
      "worst_row": "U-06(Soft)"
    },
    {
      "gate": "U-07",
      "measured": 1,
      "unit": "count",
      "required": "== 1",
      "margin": 0.0,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "U-07.mesh.bodies"
    },
    {
      "gate": "U-08",
      "measured": null,
      "unit": "",
      "required": "N/A",
      "margin": null,
      "at": null,
      "status": "NOT_APPLICABLE",
      "assumes": [],
      "worst_row": "U-08"
    },
    {
      "gate": "D-01a",
      "measured": 3.0,
      "unit": "mm",
      "required": ">= 0.8",
      "margin": 2.2,
      "at": "(116.0000, 0.0000, -299.0000) mm",
      "status": "PASS",
      "assumes": [],
      "worst_row": "D-01a"
    },
    {
      "gate": "D-01b",
      "measured": 3.0,
      "unit": "mm",
      "required": ">= 2.0",
      "margin": 1.0,
      "at": "(116.0000, 0.0000, -299.0000) mm",
      "status": "PASS",
      "assumes": [],
      "worst_row": "D-01b"
    },
    {
      "gate": "D-02",
      "measured": 232.0,
      "unit": "mm",
      "required": "<= 420.0",
      "margin": 188.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-09"
      ],
      "worst_row": "D-02.size_x"
    },
    {
      "gate": "D-03a",
      "measured": 90.0,
      "unit": "deg",
      "required": ">= 45.0",
      "margin": 45.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-08"
      ],
      "worst_row": "D-03a"
    },
    {
      "gate": "D-03b",
      "measured": 4.0,
      "unit": "mm",
      "required": "<= 5.0",
      "margin": 1.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-08"
      ],
      "worst_row": "D-03b.widest_insert_bore"
    },
    {
      "gate": "D-04a",
      "measured": 3.4,
      "unit": "mm",
      "required": ">= 3.25",
      "margin": 0.15,
      "at": "(81.0000, 0.0000, -290.0000) mm",
      "status": "PASS",
      "assumes": [],
      "worst_row": "D-04a.x81_z-290.diameter"
    },
    {
      "gate": "D-05a",
      "measured": 12.0,
      "unit": "mm",
      "required": ">= 8.0",
      "margin": 4.0,
      "at": "[(96.0, 210.0, -293.0), (84.0, 210.0, -293.0)]",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-05"
      ],
      "worst_row": "D-05a.x90_z-293.across_x"
    },
    {
      "gate": "D-05b",
      "measured": 4.0,
      "unit": "mm",
      "required": "in [3.95, 4.05]",
      "margin": 0.05,
      "at": "(90.0000, 209.0000, -293.0000) mm",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-05"
      ],
      "worst_row": "D-05b.x90_z-293.diameter"
    },
    {
      "gate": "D-06a",
      "measured": 3.0,
      "unit": "mm",
      "required": ">= 1.0",
      "margin": 2.0,
      "at": "(116.0000, 0.0000, -299.0000) mm",
      "status": "PASS",
      "assumes": [],
      "worst_row": "D-06a"
    },
    {
      "gate": "D-07",
      "measured": null,
      "unit": "",
      "required": "N/A",
      "margin": null,
      "at": null,
      "status": "NOT_APPLICABLE",
      "assumes": [],
      "worst_row": "D-07"
    },
    {
      "gate": "J-05",
      "measured": 4.0,
      "unit": "mm",
      "required": ">= 3.0",
      "margin": 1.0,
      "at": "(96.0000, 210.0000, -293.0000) mm",
      "status": "PASS",
      "assumes": [],
      "worst_row": "J-05.x90_z-293.+x"
    },
    {
      "gate": "E-06",
      "measured": null,
      "unit": "",
      "required": "reviewer",
      "margin": null,
      "at": null,
      "status": "INCONCLUSIVE",
      "assumes": [],
      "worst_row": "E-06"
    },
    {
      "gate": "E-11",
      "measured": null,
      "unit": "",
      "required": "reviewer",
      "margin": null,
      "at": null,
      "status": "INCONCLUSIVE",
      "assumes": [
        "A-03",
        "A-06"
      ],
      "worst_row": "E-11"
    },
    {
      "gate": "REQ-01",
      "measured": 1,
      "unit": "count",
      "required": "== 1",
      "margin": 0.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-01"
      ],
      "worst_row": "REQ-01.underside_faces"
    },
    {
      "gate": "REQ-02",
      "measured": -116.0,
      "unit": "mm",
      "required": "in [-116.1, -115.9]",
      "margin": 0.1,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-02"
      ],
      "worst_row": "REQ-02.min_x"
    },
    {
      "gate": "REQ-03",
      "measured": 1,
      "unit": "bool",
      "required": "== 1",
      "margin": 0.0,
      "at": "(95.0000, 30.0000, -302.0000) mm",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-03"
      ],
      "worst_row": "REQ-03.x95_y30.through"
    },
    {
      "gate": "REQ-04",
      "measured": 1,
      "unit": "bool",
      "required": "== 1",
      "margin": 0.0,
      "at": "(-100.0000, 30.0000, -302.0000) mm",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-04"
      ],
      "worst_row": "REQ-04.x-100_y30.through"
    },
    {
      "gate": "REQ-05",
      "measured": -283.0,
      "unit": "mm",
      "required": "<= -283.0",
      "margin": 0.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-07"
      ],
      "worst_row": "REQ-05.max_z"
    },
    {
      "gate": "REQ-06",
      "measured": 4.0,
      "unit": "mm",
      "required": "in [3.9, 4.1]",
      "margin": 0.1,
      "at": "[(80.0, 140.0, -300.5), (76.0, 140.0, -300.5)]",
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-06"
      ],
      "worst_row": "REQ-06.x78.width"
    },
    {
      "gate": "REQ-07",
      "measured": 1,
      "unit": "count",
      "required": "== 1",
      "margin": 0.0,
      "at": null,
      "status": "PASS_ASSUMED",
      "assumes": [
        "A-05"
      ],
      "worst_row": "REQ-07.top_faces"
    },
    {
      "gate": "REQ-08",
      "measured": 0.0,
      "unit": "mm3",
      "required": "<= 0.0",
      "margin": 0.0,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "REQ-08.x81_z-290"
    },
    {
      "gate": "REQ-09",
      "measured": null,
      "unit": "",
      "required": "bench",
      "margin": null,
      "at": null,
      "status": "INCONCLUSIVE",
      "assumes": [
        "A-11"
      ],
      "worst_row": "REQ-09(Soft)"
    },
    {
      "gate": "exactly_one_solid",
      "measured": 1,
      "unit": "count",
      "required": "== 1",
      "margin": 0.0,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "exactly_one_solid"
    },
    {
      "gate": "feature_census",
      "measured": 46,
      "unit": "count",
      "required": "== 46",
      "margin": 0.0,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "feature_census.plane_faces"
    },
    {
      "gate": "envelope_within_spec",
      "measured": 232.0,
      "unit": "mm",
      "required": "in [231.9, 232.1]",
      "margin": 0.1,
      "at": null,
      "status": "PASS",
      "assumes": [],
      "worst_row": "envelope_within_spec.size_x"
    }
  ],
  "sweep": [
    {"parameter": "flange_hole_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "REQ-01 diameter", "worst_margin": 0.0},
    {"parameter": "flange_hole_dx", "values": [-0.1, 0.0, 0.1], "all_built": true, "worst_gate": "REQ-01 offset", "worst_margin": 0.0},
    {"parameter": "insert_d", "values": [3.95, 4.0, 4.05], "all_built": true, "worst_gate": "REQ-07 diameter", "worst_margin": 0.0},
    {"parameter": "insert_depth", "values": [5.9, 6.0, 6.1], "all_built": true, "worst_gate": "REQ-07 depth", "worst_margin": 0.0},
    {"parameter": "pass_d", "values": [11.9, 12.0, 12.1], "all_built": true, "worst_gate": "REQ-03 diameter", "worst_margin": 0.0},
    {"parameter": "wall_z", "values": [-0.1, 0.0, 0.1], "all_built": true, "worst_gate": "REQ-05 tank-zone box (FAIL at high, mm3)", "worst_margin": -1400.0},
    {"parameter": "y_top", "values": [214.9, 215.0, 215.1], "all_built": true, "worst_gate": "REQ-07 top y", "worst_margin": 0.0}
  ],
  "least_sure": [
    "U-03 (a): the flanges cover OD-C01's feet holes at (+-110, -295); the row fails on its words (18.158 mm2 over holes) and passes on its parenthetical (0.780 inside the outline)",
    "Driver access: the ledge covers every screw axis; a straight driver shares 113.1 mm3, a 2 degree tilt clears",
    "REQ-02 / REQ-05 tolerance stack: the wall at its +0.1 limit enters the tank-zone box by 1400 mm3; REQ-08 tangent at x +-81"
  ],
  "stopped": true
}
```
