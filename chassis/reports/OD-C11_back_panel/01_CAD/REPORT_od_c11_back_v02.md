# REPORT — od_c11_back v02 (20261001-od-c11-back-panel)

Designer: Claude Code, claude-opus-5-5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` as amended by `01_CAD/DESIGN_PLAN_v02.md` · 2026-10-01 UTC · brief WP-03, build attempt 2 of 2, fix cycles used 0 of 3 · outcome STOPPED (section 10)

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN_v02.md` | 8859dd8b56efde148a9fe7452499be6324dd1bac0ab1d1389d88d8a2f9e9562a | plan amendment for spec 1.1 (v01 plan stands otherwise) |
| `01_CAD/build_od_c11_back_v02.py` | c08d544ac93a6a1a5764f11a9cab5fbd3f15494927a47ba0a5d003f12bcb1639 | parametric script, every §4 value a named parameter |
| `01_CAD/check_od_c11_back_v02.py` | 25d0f09641042c3f13f3311f4709f7d931acc7ee6351d07ce34e4d5913aed374 | checks: v01 predicates with spec 1.1 thresholds, plus the U-03 hole-rim predicate |
| `01_CAD/build_record_v02.json` | ad379d41a70fa0ec2673a4e1656c998054dc9e27b9c9d0d2248f1704fbaad5bd | parameters, export hashes, STL settings, placements |
| `01_CAD/check_od_c11_back_v02.json` | 1cc21b59eeaa7a29f84292ab18667a5cc804fa89a4f31f727782db106f718945 | every gate row and fact, measured on the re-imported STEP files |
| `01_CAD/check_od_c11_back_v02.log` | 4e740a9ce2acf3f50449e5d8f6b24eb1e122602111f1fb049cbfdfa74e3f7ff1 | the same rows, one line each |
| `01_CAD/sections_od_c11_back_v02.py` | eb7aadc86d6a1095aaea1bf59033b03148b3b224331fab4a038ebb072eb74ce4 | D6 sections from the re-imported STEP |
| `01_CAD/sections_v02.json` | a4a9d819f4e6532be204c82036cf4e68e3fb92848f3f792dac07a98421e94182 | section planes, cut areas, nothing_clipped |
| `01_CAD/sweep_od_c11_back_v02.sh` | ccb829629f77db96fc4596748b2874496f46518e35b18cdf2858f09db5b561c8 | D7 sweep driver (15 runs into 01_CAD/sweep_v02/) |
| `01_CAD/sweep_summary_v02.py` | 58710744b028dc170505746211769b8c8b6eed09bffe8348b596af503d0f1053 | D7 summary |
| `01_CAD/sweep_v02/sweep_summary.json` | 07af9c7f4c97d1950833009efd16870b74e19091d76922b571988a455a410f62 | per-run solids, faces, rows not passing, worst mm margin, STEP hash |
| `01_CAD/probe/probe_passthrough_block_v02.py` | a7551bbce9193626c7358df13b6267390c5c9027a418195bf5cfde8cf018e2ce | fact: pass-through area blocked by the outer gussets |
| `01_CAD/probe/probe_passthrough_block_v02.json` | d824ed349f4e64b9631a650a5d15e3b986240b7618e454112866b58611d20a54 | its results |
| `02_STEP_STL/od_c11_assembly_C1_v02.step` | 98d3336367f3897e435fbfc32eb2c148593003b09435a06ea820ebb31385d381 | AP242 check assembly: od_c11_back, od_c01_frame, od_c02_bulkhead, od_c03_cradle, od_h01_pump as placed |
| `02_STEP_STL/od_c11_back_C1_v02.step` | 80803f53c7ca267565115d46c61c4280e95baaef6afd800eeae0afa1e3e16235 | AP242 (tools.core.write_step), part od_c11_back, re-imported for every measurement |
| `02_STEP_STL/od_c11_back_C1_v02.stl` | 1d8ab9b3fd0b0201dca3a2482a364fd995bb89b18ea4c99b04603cc4ea101915 | binary, meshed afresh (cached triangulation cleared); tolerance 0.01 mm / angular 0.20 rad, 3944 triangles |
| `03_Sections/od_c11_assembly_feethole_x110_v02_left.png` | d5f756e56fb2c511f23140e3fff9435515046e40ba944e7a5877858bc4b22ccb | section, nothing clipped (check assembly) |
| `03_Sections/od_c11_back_bosses_y207_v02_front.png` | 402327420d32335f3fd18d09fbfa6578d39656d2c1a924c6f27f8ad34599b30f | section, nothing clipped |
| `03_Sections/od_c11_back_flanges_y2_v02_front.png` | 4fce63347b7a3b4df7870519c162630e0237584f6d4aa2e450e561b812969d04 | section, nothing clipped |
| `03_Sections/od_c11_back_gusset_x102_v02_left.png` | f19b8440172fd6b53be550ca4791cf0ed1e43c457fe1a21d9c33de9b0f1e4ecf | section, nothing clipped |
| `03_Sections/od_c11_back_gusset_x74_v02_left.png` | 44d0bba56e9e64e1cd329ac26a23f4472ed0eb93a7fe3fd3028331e40790c38c | section, nothing clipped |
| `03_Sections/od_c11_back_gusset_xm102_v02_left.png` | 5ec4b1e460edf16f34abe5ff3ce4c739c9b5729cedb5457fa5eb5f6c33226702 | section, nothing clipped |
| `03_Sections/od_c11_back_gussets_z290_v02_top.png` | e4ee78be296e75b426ebf88fb7dcffb4c4282f752180b6e3c404cf1c81b7a9d7 | section, nothing clipped |
| `03_Sections/od_c11_back_hole_x81_v02_left.png` | 1c84f7a205a4d6a022f3508280f1ab765b67e3f3fe5e94b29a2e92b25a9e2675 | section, nothing clipped |
| `03_Sections/od_c11_back_hole_x95_v02_left.png` | 8709e241ba789525e2696ccb4278d5f8ca155d019ac01905b169d91d6af49dfc | section, nothing clipped |
| `03_Sections/od_c11_back_insert_x90_v02_left.png` | 6dd11dbf5c767033681d69653ce43c4fed3c30e649700c82efd0378768dffb4f | section, nothing clipped |
| `03_Sections/od_c11_back_ledge_y213_v02_front.png` | 6f3dbbecb9dd959684168feb5f977706494dfefa344b6ddb33b380c29079ab1b | section, nothing clipped |
| `03_Sections/od_c11_back_passthroughs_y30_v02_front.png` | 43e6f47675b56602f4e17c1949ebb150c9cd8dc24afb2db62f6770d616a24e6e | section, nothing clipped |
| `03_Sections/od_c11_back_tube_xm100_v02_left.png` | cfaf644c2fa64140d98e79e448c70047fcb5b0c4568e62e04a77bed0f4147ce4 | section, nothing clipped |
| `03_Sections/od_c11_back_vents_y140_v02_front.png` | c68aaf2410bfc3041489ca2e889918076922bab293003f9bf0e26e58a439746a | section, nothing clipped |
| `03_Sections/od_c11_back_wall_y200_v02_front.png` | 876d1e3bccea0597ef2797aed25de0595627812be56c0c8584c8a7d63bc8df8b | section, nothing clipped |
| `03_Sections/od_c11_back_wall_y50_v02_front.png` | e14edd7220d5c4772229ee0620af6c32d68b080cadf06cf8072fb66c7e7a4718 | section, nothing clipped |
| `03_Sections/od_c11_back_wall_z300p5_v02_top.png` | 13616bba5a7fc885b054cb05f3f2200afd08abaa9973e57f053ea0c7931a6967 | section, nothing clipped |

Every section measured `nothing_clipped` = 0 (`01_CAD/sections_v02.json`). The sweep's 15 runs (STEP, STL, assembly, build record, check JSON and log each) are under `01_CAD/sweep_v02/<run>/`; their STEP hashes are in `sweep_summary.json`. No v01 file was overwritten.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3) · ocpsvg 0.6.0 · repo commit 10929db1408d89144bd4af9cad971440427933d0 (unchanged since v01)

## 3. Gate self-check

`01_CAD/check_od_c11_back_v02.py` measured these rows on the re-imported STEP files: 225 rows in the JSON, of which 91 PASS, 120 PASS_ASSUMED, 8 FAIL, 4 INCONCLUSIVE and 2 N/A. The table shows the worst row of each §5 ID and shows U-03 row by row. Bands are from GATES.md §0: mm 0.005, deg 0.001, mm³ 0.001, rad 0.00002, counts and mm² 0.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | 1 solid, brep_valid 1, naked edges 0 | 1, 1, 0 | 0 | — | PASS | — |
| U-02 | 232.000 × 215.000 × 25.000; position x −116.000 … 116.000, y 0.000 … 215.000, z −302.000 … −277.000 | each size in [spec − 0.1, spec + 0.1]; position ± 0.1 | +0.100 (each) | — | PASS | — |
| U-03 (a) plate contact | clearance 0.000; common volume 0.000 mm³ | = 0; ≤ 0 | 0 | (116, 0, −302) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) footprint inside the outline | 0.000 mm² outside; least distance to the outline 0.780 | = 0; ≥ 0.5 | +0.280 | wall corner to the R 10 arc | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) underside over plate material | 0.000 mm² of the 2067.683 mm² footprint over plate holes (the v01 failure is gone) | = 0 | 0 | — | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| **U-03 (a) footprint ≥ 3.0 from every existing hole's edge (new in 1.1)** | **2.300**: the wall's foot (inner edge z −299) lies 4.000 from the centres of the feet holes Ø3.400 at (±110, −295), so 2.300 from their rims. 26 plate holes were checked. The flanges alone keep 4.300. | ≥ 3.0 | **−0.700** | (±110, 0, −295) | **FAIL** | A-01, A-02, A-07 |
| U-03 (a) under each flange hole | plate material missing under a Ø3.4 plug 0.000 mm³ (all four); nearest existing plate hole 31.780 (x ±81) and 19.849 (x ±95) | ≤ 0; ≥ 6.0 | +13.849 | (±95, 0, −282) to (±110, −295) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) neighbours | OD-C03 43.863, OD-H01 61.540, OD-C02 37.014; common volume 0.000 mm³ each | ≥ 20.0; ≤ 0 | +17.014 | flange corner (72, 0, −277) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (b) | lowered from +40.0 to 0 in 2.0 steps (21 poses): worst common volume 0.000 mm³ with OD-C01, OD-C02, OD-C03 and OD-H01 | ≤ 0 at every step | 0 | every pose | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-04 | part: AP242, 1 solid, volume delta 1.4e-9 mm³, faces delta 0, label kept, valid after; assembly: 5 solids, labels kept, faces delta 0, valid after, per-child volume delta ≤ 4.3e-9 mm³ | in [0, 0] mm³; 0; 1 | −4e-9 (inside the band) | — | PASS | — |
| **U-05 / feature_census** | **planar 49** (plan 46), cylindrical 19 (concave 19), cone/sphere/torus/B-spline/other 0, bores 9; **Ø12 along Z through: 1** (plan 3: the cord hole and the −100 tube hole now end on a gusset notch floor); 4 Ø3.4 along Y through, 2 Ø4.0 along Y blind, 10 R 2.0 slot ends, 4 gusset hypotenuses, 2 boss undersides, 2 flange fronts, 3 ledge-underside pieces, 2 ledge ends, 1 wall outer face | plan §3 counts | **−3 (planar); −2 (through Ø12)** | — | **FAIL** | — |
| **U-06 (Soft)** | **`min_wall_wide` 0.136** (spacing 0.7) | ≥ 2.0 | −1.864 | (100.29, 31.90, −297.88): the 1.0 notch the cord hole's cutter leaves in the +X outer gusset | **FAIL (Soft)** | — |
| U-07 | tolerance 0.01; angular 0.20 rad; max sagitta 0.00710 on a fresh re-mesh of the re-imported STEP; mesh 1 body, 0 naked edges, winding 1 | ≤ 0.01; ≤ 0.23097 rad; ≤ 0.01 | +0.00290 (sagitta) | (−103.77, 25.34, −300.5) | PASS | — |
| U-08 | no threads | N/A by its row | — | — | N/A | — |
| D-01a | `min_wall` 3.000 (spacing 0.7) | ≥ 0.8 | +2.200 | (104, 30, −298) | PASS | — |
| D-01b | 3.000 | ≥ 2.0 | +1.000 | (104, 30, −298) | PASS | — |
| D-02 | 232.0 × 215.0 on the bed, 25.0 tall | ≤ 420 × 420, ≤ 500 | +188.0 | — | PASS (assumed: A-09) | A-09 |
| **D-03a** | **refill not as planned** (6 holes refilled, 60 faces against 57 planned, 1 solid), so the census outside the exception was not run. Diagnostic: the whole part reads 0.0° at (−104.0, 25.56, −298.0), and the per-face split finds 2 downward faces at 0.0° outside the named exception (the two gusset-notch floors at z −298); the exception crowns read 0.0° (4 flange-hole faces, 2 insert-bore faces) | ≥ 45° | — | (−104, 25.6, −298) | **INCONCLUSIVE** | A-08 |
| **D-03b** | reviewer row. Designer reading: horizontal holes bridge 3.400 and 4.000; **`flat_ceiling_spans` 15.453** (the notch floor at z −298 in the −X outer gusset, a ceiling in the print) | ≤ 5.0 | **−10.453** | (−100.0, 32.05, −298.0) | **FAIL** (designer reading) | A-08 |
| D-04a | 3.400 (all four) | ≥ 3.25 | +0.150 | (±81 / ±95, 0, −282) | PASS | — |
| D-05a | across X 12.000, across Z 15.000 (both bosses) | ≥ 8.0 | +4.000 | (84 … 96, 210, −293) | PASS (assumed: A-05) | A-05 |
| D-05b | Ø4.000, depth 6.000 (both) | Ø in [3.95, 4.05]; depth in [5.9, 6.1] and ≥ 5.7 | +0.050 | (±90, 209, −293) | PASS (assumed: A-05) | A-05 |
| D-06a | 3.000 | ≥ 1.0 | +2.000 | (104, 30, −298) | PASS | — |
| D-07 | no fit-critical bores | N/A by its row | — | — | N/A | — |
| J-05 | +X 4.000, −X 4.000, +Z 4.000, −Z 7.000 (both bores) | ≥ 3.0 | +1.000 | (96, 210, −293) | PASS | — |
| E-06 | reviewer row. Designer reading: one solid; each boss is a 12 × 8 × 12 block fused to the wall and to the ledge's underside; each flange (32 × 22) is fused to the wall and tied by two 4.0 gussets (16 × 30 legs) at its ends. The outer gussets carry a 1.0 notch where the pass-through cutters enter them (sections x ±102, z −290) | reviewer, from sections | — | — | INCONCLUSIVE (reviewer row) | — |
| E-11 | reviewer row. Designer reading: the five slots open the wall behind the bay (centre lines clear through the wall). The cord hole at (95, 30) has 3.917 of its 113.097 mm² opening blocked by the +X outer gusset 1.1 behind the wall; the −100 tube hole has 29.454 mm² (26 %) blocked by the −X outer gusset (`01_CAD/probe/probe_passthrough_block_v02.json`) | reviewer, from sections | — | — | INCONCLUSIVE (reviewer row) | A-03, A-06 |
| REQ-01 | four holes Ø3.400, offset 0.000, length 4.000, through; underside one planar face at y 0.000 | Ø 3.4 ± 0.1; ≤ 0.10; 4.0 ± 0.1; 1 face at 0.00 ± 0.10 | +0.100 | (±81 / ±95, 0, −282) | PASS (assumed: A-01) | A-01 |
| REQ-02 | outer face −302.000 and inner face −299.000 at y 50 and y 200 (x −40, 0, 40); x −116.000 / 116.000 | ± 0.10; ± 0.1 | +0.100 | — | PASS (assumed: A-02) | A-02 |
| **REQ-03** | Ø12.000, offset 0.000; **through 0**: the bore runs z −302 … −298 and ends closed on the +X outer gusset's notch floor | 12.0 ± 0.1; ≤ 0.10; through | **−1 (through)** | (95, 30, −302) | **FAIL** | A-03 |
| **REQ-04** | (−84, 30): Ø12.000, offset 0.000, through. **(−100, 30): Ø12.000, offset 0.000, through 0**: the bore ends closed on the −X outer gusset's notch floor at z −298 | 12.0 ± 0.1; ≤ 0.10; through | **−1 (through, at −100)** | (−100, 30, −302) | **FAIL** | A-04 |
| REQ-05 | max z −277.000; common volume with the box x ±70, y 0 … 100, z −298.8 … −250: 0.000 mm³ | ≤ −277.0; = 0 | 0.000 | — | PASS (assumed: A-07) | A-07 |
| REQ-06 | five slots: width 4.000, height 80.000, centres x 78/86/94/102/110 at 0.000 off, y 100.000 … 180.000 | ± 0.1 each | +0.100 | rays at (x_c, 140, −300.5) | PASS (assumed: A-06) | A-06 |
| REQ-07 | two bores Ø4.000, depth 6.000, offset 0.000, blind; top one planar face at y 215.000 spanning z −302.000 … −287.000 | Ø 4.0 ± 0.05; 6.0 ± 0.1; ≤ 0.10; 1 face over z −299 … −287 | +0.050 | (±90, 209, −293) | PASS (assumed: A-05) | A-05 |
| REQ-08 | common volume of the four Ø6 cylinders y 4 … 260 with the panel 0.000 mm³ each (they touch the flange top at y 4 by construction, clearance 0.000) | = 0 | 0 | — | PASS | — |
| REQ-09 (Soft) | bench gate, not geometric | answered by the first print | — | — | INCONCLUSIVE (by its row) | A-11 |
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| feature_census | as U-05 | plan §3 | −3 | — | FAIL | — |
| envelope_within_spec | sizes as U-02; position min/max x, y, z each within ± 0.1 of ±116.0, 0 … 215.0, −302.0 … −277.0 (reported apart) | ± 0.1 | +0.100 | — | PASS | — |

Facts beside the gates (not gated): each new insert site lies 23.000 from the plate's edge. A screw head Ø5.7 on a feet hole at (±110, −295) would reach z −297.85, 1.15 short of the wall's inner face.

## 4. Robustness sweep (D7)

Every fit-critical parameter in the plan was rebuilt at its spec tolerance limits, exported into `01_CAD/sweep_v02/<run>/` and run through the same checks. Every run built one solid of 68 faces. Every run gives the same nine rows not passing: U-05 and feature_census planar 49, U-05 Ø12 through 1, REQ-03 through, REQ-04 (−100) through, D-03b flat ceiling about 15.45, U-03 hole rim, U-06 (Soft) 0.136, and D-03a INCONCLUSIVE. None of these depends on a swept parameter. The table gives the worst margin of the parameter's own rows.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| flange_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 diameter at both ends | 0.000 (at the limit, PASS); D-04a +0.050 at low |
| flange_hole_dx (holes moved along X) | −0.1 · 0 · +0.1 | yes | REQ-01 offset 0.100 at both ends | 0.000 (at the limit, PASS); nearest plate hole 19.774 at high (+13.774) |
| insert_d | 3.95 · 4.0 · 4.05 | yes | REQ-07 / D-05b diameter at both ends | 0.000 (at the limit, PASS); J-05 3.975 at high (+0.975) |
| insert_depth | 5.9 · 6.0 · 6.1 | yes | REQ-07 / D-05b depth at both ends | 0.000 (at the limit, PASS) |
| pass_d | 11.9 · 12.0 · 12.1 | yes | REQ-03 / REQ-04 diameter at both ends | 0.000 (at the limit, PASS); D-03b flat ceiling 15.481 at high |
| wall_z (both faces moved, the gussets with them) | −0.1 · 0 · +0.1 | yes | **REQ-05 tank-zone box (z −298.8): 0.000 mm³ at both ends (PASS; the v01 sweep failure is gone).** U-02 size_z 24.9 / 25.1 at the limit; U-03 hole rim 2.400 at low, 2.200 at high (FAIL, −0.800); footprint to outline 0.704 at low (+0.204) | 0.000 (REQ-05, U-02); −0.800 (U-03 rim at high) |
| y_top | 214.9 · 215.0 · 215.1 | yes | REQ-07 top and U-02 size_y at both ends | 0.000 (at the limit, PASS) |

Reading: the part's swept rows pass at every tolerance limit. It does not pass at nominal, because of the two spec conflicts in section 10.

## 5. Build facts

- Envelope 232.000 × 215.000 × 25.000 mm (x −116 … 116, y 0 … 215, z −302 … −277); volume 166 258.822 mm³; mass 211.149 g at 1270 kg/m³ (A-10); centre of mass (−2.485, 109.652, −299.345).
- STL (for the orchestrator's 3MF): 3944 triangles, bounding box (−116.0, 0.0, −302.0) … (116.0, 215.0, −277.0), size 232.0 × 215.0 × 25.0; tolerance 0.01 mm, angular 0.20 rad, sagitta 0.00710 mm; one closed body. Meshed afresh with the cached triangulation cleared (`tools.core.write_stl`).
- Fillets: none (the spec names none); the ladder was not used.
- Placements (assembly), unchanged from v01: OD-C01 and OD-C02 by RigidJoint at the identity. OD-C03 and OD-H01 by RigidJoint at `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`, read back as position (0, 40, −205), orientation (0, 90, 180).

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The panel stands upright on the plate's top face along its rear edge on its 3 mm foot and two 22-deep flanges, and prints flat on its outer face. It rests and mounts the way it is used. |
| P2 | Function chains | The vents sit behind the bay. The tube chain is broken at (−100, 30): a tube passing the wall meets the −X outer gusset's face (x −100 … −104) 1 mm behind it, with 26 % of the opening blocked (section x −102, z −290). The cord hole is 3.5 % blocked at its edge by the +X outer gusset. |
| P3 | Motion clearance | No moving parts. The panel lowers along −Y onto the plate clear of every neighbour at all 21 poses (U-03 (b)). |
| P4 | Human factors | Fixed from v01: a straight Ø6 driver reaches all four flange screws from y 260 with nothing in its way (REQ-08, 0.000 mm³), and the screws sit 5.0 in front of the ledge. |
| P5 | Next to a real product | An ordinary appliance back panel. Two features look wrong next to a real product: the 1 mm notches the pass-throughs leave in the outer gussets, and a tube hole half covered by a rib. |
| P6 | Floating, embedded, mirrored, upside-down | Nothing floats (one solid) and nothing is embedded in a placed neighbour (common volume 0). The flanges now stay off the feet holes (0.000 mm² over holes), but the wall's foot passes 2.3 from their rims (section x 110). |

## 7. Library and tools used

- Card: UNO10 U5 tank heat-set (size and position gated apart), as in v01. No precedent files were read in v02.
- `tools.core`: `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`. `tools.measure`: `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, `min_wall_wide` (spacing 0.7), `overhang_census` (build +Z, spacing 0.7), `flat_ceiling_spans` (spacing 0.7), `radial_extent`, `clearance`, `mass_properties`, `mesh_census`. `tools.result.gate`. `tools.drawing.write_sections`.
- New job code in v02 (in `01_CAD/`, never in the repo): the U-03 hole-rim distance (centre-to-footprint distance minus radius, for every plate bore along Y) and the pass-through blockage probe. No `tools/measure` function was missing.
- `tools.drawing.write_sections` raised "a wire of the cut face has no area" on a top-view cut of the check assembly at z −295. That cut was dropped; the x 110 assembly section shows the same place.

## 8. Deviations from the plan

1. DESIGN_PLAN_v02.md was written after the first nominal export and check. Its §3 note on the failed cutter premise and its §7 risks record what that measurement found; the parameter and check changes it lists are the ones spec 1.1 set before the build.
2. The gusset's flange leg is again a separate 16.0 parameter (`gusset_leg_flange`), measured from the wall's inner face, because the flange is now 22 deep (spec §4 keeps the 16.0 leg).
3. The v01 tilted-driver fact beside REQ-08 is dropped, because REQ-08 now runs to y 260 itself.
4. Sections: new cuts at z −290, x 95, x 81, x 102 and x −102 replace the v01 cuts at x 100 and x 112 to follow the moved holes and gussets.

## 9. What I am least sure of

1. How to read the new U-03 (a) clause, "the footprint ≥ 3.0 from the edge of every existing OD-C01 hole". On its words it covers the wall's foot, and it fails: 2.300 to the feet-hole rims. A-01's "the flanges end 4.3 from their edge" suggests the author measured the flanges only, which pass at 4.300. I gated the words.
2. REQ-03 and REQ-04 "through". I built the plan's cutter (z −303 … −298, 1.0 past the wall). Where the outer gussets now sit, it leaves a 1.0 notch with a closed floor, so `bore_census` reads two holes as not through. A cutter that stops at z −299 would read the holes as through the wall, but their openings would still face the gussets (26 % and 3.5 % blocked). The defect is the spec's overlap, not the cutter depth. Changing the cutter, or cutting the hole on through the gusset, would only hide it.
3. D-03a is INCONCLUSIVE by its own guard (refill 60 faces against 57 planned). The diagnostic shows 0.0° downward faces outside the named exception at the same notch floors, so on this geometry the row would fail.

## 10. Stop

STOPPED (D9). Two hard conflicts inside spec 1.1's own geometry; no fix cycle can resolve either without changing a spec §4 value (0 of 3 used). This was the last build attempt under the cap.

**Stop 1: U-03 (a), the footprint ≥ 3.0 from the edge of every existing OD-C01 hole.**
- Measured: 2.300 (margin −0.700). The wall's foot (§4: z −302 … −299 over x ±116, A-02) passes 4.000 from the centres of the OD-C01 feet holes Ø3.400 at (±110, −295). The flanges alone keep 4.300. The wall plane at its +0.1 limit gives 2.200.
- Trade-off options:
  1. Read the clause as applying to the flanges, or sign the wall foot at 2.3 as a U-18 exception. No geometry change. Confirm that nothing of the feet sits on the plate's top face within 0.7 of the wall: an ISO 7380 head Ø5.7 there would reach z −297.85, 1.15 clear of the wall.
  2. Lower the threshold to ≥ 2.0 in §5 (spec change).
  3. In the same OD-C01 revision that adds the four inserts (A-01), move the feet holes so their rims lie ≥ 3.0 in front of z −299 (centre at z ≥ −294.3).
  4. Not advised: notch the wall's foot around each feet hole, which weakens the foot at the plate corner.

**Stop 2: the outer gussets overlap the pass-throughs (REQ-03, REQ-04 through; U-05; D-03b; D-03a; U-06 Soft; E-11 and P2).**
- Measured: spec 1.1 moved the outer gussets to x ±(100 … 104), y 4 … 34 against the wall. The tube hole Ø12 at (−100, 30) spans x −106 … −94, y 24 … 36, so its axis lies on the −X gusset's inner face and 29.454 of its 113.097 mm² opening is blocked. The cord hole at (95, 30) reaches x 101, and 3.917 mm² is blocked. As built, REQ-03 and REQ-04 (−100) read not through, planar faces 49 (46 planned), Ø12 through bores 1 (3 planned), a 15.453 flat ceiling (D-03b reading), and `min_wall_wide` 0.136 at the notch.
- Trade-off options (each is a §4 change):
  1. Shorten the outer gussets' wall leg from 30.0 to ≤ 18.0 (top at y ≤ 22, 2.0 below the holes), keeping the 16.0 flange leg.
  2. Raise the three pass-throughs from y 30 to y ≥ 42 (bottom ≥ 2.0 above the gussets' top at y 34), which changes A-03 and A-04.
  3. Move the outer gussets inboard between the screw heads, x ±(86 … 90) (2.15 from both heads at ±81 and ±95). They then hit the −84 tube hole (x −90 … −78) and the cord hole (x 89 … 101), so this needs option 1 or 2 as well.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20261001-od-c11-back-panel",
 "part": "od_c11_back",
 "tag": "v02",
 "spec_version": "1.1",
 "files": [
  {
   "path": "01_CAD/DESIGN_PLAN_v02.md",
   "sha256": "8859dd8b56efde148a9fe7452499be6324dd1bac0ab1d1389d88d8a2f9e9562a"
  },
  {
   "path": "01_CAD/build_od_c11_back_v02.py",
   "sha256": "c08d544ac93a6a1a5764f11a9cab5fbd3f15494927a47ba0a5d003f12bcb1639"
  },
  {
   "path": "01_CAD/check_od_c11_back_v02.py",
   "sha256": "25d0f09641042c3f13f3311f4709f7d931acc7ee6351d07ce34e4d5913aed374"
  },
  {
   "path": "01_CAD/build_record_v02.json",
   "sha256": "ad379d41a70fa0ec2673a4e1656c998054dc9e27b9c9d0d2248f1704fbaad5bd"
  },
  {
   "path": "01_CAD/check_od_c11_back_v02.json",
   "sha256": "1cc21b59eeaa7a29f84292ab18667a5cc804fa89a4f31f727782db106f718945"
  },
  {
   "path": "01_CAD/check_od_c11_back_v02.log",
   "sha256": "4e740a9ce2acf3f50449e5d8f6b24eb1e122602111f1fb049cbfdfa74e3f7ff1"
  },
  {
   "path": "01_CAD/sections_od_c11_back_v02.py",
   "sha256": "eb7aadc86d6a1095aaea1bf59033b03148b3b224331fab4a038ebb072eb74ce4"
  },
  {
   "path": "01_CAD/sections_v02.json",
   "sha256": "a4a9d819f4e6532be204c82036cf4e68e3fb92848f3f792dac07a98421e94182"
  },
  {
   "path": "01_CAD/sweep_od_c11_back_v02.sh",
   "sha256": "ccb829629f77db96fc4596748b2874496f46518e35b18cdf2858f09db5b561c8"
  },
  {
   "path": "01_CAD/sweep_summary_v02.py",
   "sha256": "58710744b028dc170505746211769b8c8b6eed09bffe8348b596af503d0f1053"
  },
  {
   "path": "01_CAD/sweep_v02/sweep_summary.json",
   "sha256": "07af9c7f4c97d1950833009efd16870b74e19091d76922b571988a455a410f62"
  },
  {
   "path": "01_CAD/probe/probe_passthrough_block_v02.py",
   "sha256": "a7551bbce9193626c7358df13b6267390c5c9027a418195bf5cfde8cf018e2ce"
  },
  {
   "path": "01_CAD/probe/probe_passthrough_block_v02.json",
   "sha256": "d824ed349f4e64b9631a650a5d15e3b986240b7618e454112866b58611d20a54"
  },
  {
   "path": "02_STEP_STL/od_c11_assembly_C1_v02.step",
   "sha256": "98d3336367f3897e435fbfc32eb2c148593003b09435a06ea820ebb31385d381"
  },
  {
   "path": "02_STEP_STL/od_c11_back_C1_v02.step",
   "sha256": "80803f53c7ca267565115d46c61c4280e95baaef6afd800eeae0afa1e3e16235"
  },
  {
   "path": "02_STEP_STL/od_c11_back_C1_v02.stl",
   "sha256": "1d8ab9b3fd0b0201dca3a2482a364fd995bb89b18ea4c99b04603cc4ea101915"
  },
  {
   "path": "03_Sections/od_c11_assembly_feethole_x110_v02_left.png",
   "sha256": "d5f756e56fb2c511f23140e3fff9435515046e40ba944e7a5877858bc4b22ccb"
  },
  {
   "path": "03_Sections/od_c11_back_bosses_y207_v02_front.png",
   "sha256": "402327420d32335f3fd18d09fbfa6578d39656d2c1a924c6f27f8ad34599b30f"
  },
  {
   "path": "03_Sections/od_c11_back_flanges_y2_v02_front.png",
   "sha256": "4fce63347b7a3b4df7870519c162630e0237584f6d4aa2e450e561b812969d04"
  },
  {
   "path": "03_Sections/od_c11_back_gusset_x102_v02_left.png",
   "sha256": "f19b8440172fd6b53be550ca4791cf0ed1e43c457fe1a21d9c33de9b0f1e4ecf"
  },
  {
   "path": "03_Sections/od_c11_back_gusset_x74_v02_left.png",
   "sha256": "44d0bba56e9e64e1cd329ac26a23f4472ed0eb93a7fe3fd3028331e40790c38c"
  },
  {
   "path": "03_Sections/od_c11_back_gusset_xm102_v02_left.png",
   "sha256": "5ec4b1e460edf16f34abe5ff3ce4c739c9b5729cedb5457fa5eb5f6c33226702"
  },
  {
   "path": "03_Sections/od_c11_back_gussets_z290_v02_top.png",
   "sha256": "e4ee78be296e75b426ebf88fb7dcffb4c4282f752180b6e3c404cf1c81b7a9d7"
  },
  {
   "path": "03_Sections/od_c11_back_hole_x81_v02_left.png",
   "sha256": "1c84f7a205a4d6a022f3508280f1ab765b67e3f3fe5e94b29a2e92b25a9e2675"
  },
  {
   "path": "03_Sections/od_c11_back_hole_x95_v02_left.png",
   "sha256": "8709e241ba789525e2696ccb4278d5f8ca155d019ac01905b169d91d6af49dfc"
  },
  {
   "path": "03_Sections/od_c11_back_insert_x90_v02_left.png",
   "sha256": "6dd11dbf5c767033681d69653ce43c4fed3c30e649700c82efd0378768dffb4f"
  },
  {
   "path": "03_Sections/od_c11_back_ledge_y213_v02_front.png",
   "sha256": "6f3dbbecb9dd959684168feb5f977706494dfefa344b6ddb33b380c29079ab1b"
  },
  {
   "path": "03_Sections/od_c11_back_passthroughs_y30_v02_front.png",
   "sha256": "43e6f47675b56602f4e17c1949ebb150c9cd8dc24afb2db62f6770d616a24e6e"
  },
  {
   "path": "03_Sections/od_c11_back_tube_xm100_v02_left.png",
   "sha256": "cfaf644c2fa64140d98e79e448c70047fcb5b0c4568e62e04a77bed0f4147ce4"
  },
  {
   "path": "03_Sections/od_c11_back_vents_y140_v02_front.png",
   "sha256": "c68aaf2410bfc3041489ca2e889918076922bab293003f9bf0e26e58a439746a"
  },
  {
   "path": "03_Sections/od_c11_back_wall_y200_v02_front.png",
   "sha256": "876d1e3bccea0597ef2797aed25de0595627812be56c0c8584c8a7d63bc8df8b"
  },
  {
   "path": "03_Sections/od_c11_back_wall_y50_v02_front.png",
   "sha256": "e14edd7220d5c4772229ee0620af6c32d68b080cadf06cf8072fb66c7e7a4718"
  },
  {
   "path": "03_Sections/od_c11_back_wall_z300p5_v02_top.png",
   "sha256": "13616bba5a7fc885b054cb05f3f2200afd08abaa9973e57f053ea0c7931a6967"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "cadquery-ocp-novtk 7.9.3.1.1",
  "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"
 },
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
   "measured": 2.3,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": -0.7,
   "at": "(-110.0000, 0.0000, -295.0000) mm",
   "status": "FAIL",
   "assumes": [
    "A-01",
    "A-02",
    "A-07"
   ],
   "worst_row": "U-03.footprint_to_plate_hole_rim"
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
   "measured": 49,
   "unit": "count",
   "required": "== 46",
   "margin": -3.0,
   "at": null,
   "status": "FAIL",
   "assumes": [],
   "worst_row": "U-05.plane_faces"
  },
  {
   "gate": "U-06",
   "measured": 0.1359999999962759,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": -1.864,
   "at": "(100.2857, 31.9000, -297.8800) mm",
   "status": "FAIL",
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
   "at": "(104.0000, 30.0000, -298.0000) mm",
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
   "at": "(104.0000, 30.0000, -298.0000) mm",
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
   "measured": null,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-08"
   ],
   "worst_row": "D-03a"
  },
  {
   "gate": "D-03b",
   "measured": 15.452607113116542,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": -10.452607113,
   "at": "(-100.0000, 32.0500, -298.0000) mm",
   "status": "FAIL",
   "assumes": [
    "A-08"
   ],
   "worst_row": "D-03b.flat_ceiling_span",
   "note": "designer reading; reviewer row"
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(81.0000, 0.0000, -282.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "D-04a.x81_z-282.diameter"
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
   "at": "(104.0000, 30.0000, -298.0000) mm",
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
   "measured": 0,
   "unit": "bool",
   "required": "== 1",
   "margin": -1.0,
   "at": "(95.0000, 30.0000, -302.0000) mm",
   "status": "FAIL",
   "assumes": [
    "A-03"
   ],
   "worst_row": "REQ-03.x95_y30.through"
  },
  {
   "gate": "REQ-04",
   "measured": 0,
   "unit": "bool",
   "required": "== 1",
   "margin": -1.0,
   "at": "(-100.0000, 30.0000, -302.0000) mm",
   "status": "FAIL",
   "assumes": [
    "A-04"
   ],
   "worst_row": "REQ-04.x-100_y30.through"
  },
  {
   "gate": "REQ-05",
   "measured": -277.0,
   "unit": "mm",
   "required": "<= -277.0",
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
   "worst_row": "REQ-08.x81_z-282"
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
   "measured": 49,
   "unit": "count",
   "required": "== 46",
   "margin": -3.0,
   "at": null,
   "status": "FAIL",
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
  {
   "parameter": "flange_hole_d",
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
   "parameter": "flange_hole_dx",
   "values": [
    -0.1,
    0.0,
    0.1
   ],
   "all_built": true,
   "worst_gate": "REQ-01 offset",
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
   "worst_gate": "REQ-07 diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_depth",
   "values": [
    5.9,
    6.0,
    6.1
   ],
   "all_built": true,
   "worst_gate": "REQ-07 depth",
   "worst_margin": 0.0
  },
  {
   "parameter": "pass_d",
   "values": [
    11.9,
    12.0,
    12.1
   ],
   "all_built": true,
   "worst_gate": "REQ-03 diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "wall_z",
   "values": [
    -0.1,
    0.0,
    0.1
   ],
   "all_built": true,
   "worst_gate": "U-03 hole rim at high (FAIL, mm); REQ-05 box 0.000 mm3 at both ends",
   "worst_margin": -0.8
  },
  {
   "parameter": "y_top",
   "values": [
    214.9,
    215.0,
    215.1
   ],
   "all_built": true,
   "worst_gate": "REQ-07 top y",
   "worst_margin": 0.0
  }
 ],
 "least_sure": [
  "U-03 (a) new clause: on its words it covers the wall foot (2.300 to the feet-hole rims, FAIL); the flanges alone keep 4.300",
  "REQ-03 / REQ-04 'through': the plan's 1.0 overshoot leaves a closed notch in the outer gussets; a cutter ending at z -299 would read through but the openings stay 26 % / 3.5 % blocked by the gussets",
  "D-03a INCONCLUSIVE by its refill guard (60 faces vs 57); the diagnostic shows 0.0 deg downward faces outside the exception at the notch floors"
 ],
 "stopped": true
}
```
