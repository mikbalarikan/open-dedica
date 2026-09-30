# RV01 — od_g01_housing_v03 (20260930-od-g01-group-head-housing) — 2026-09-30 UTC

Reviewer: Claude Code, Opus 5 · independent re-measurement; designer numbers are not trusted
Spec 1.3 · plan `01_CAD/DESIGN_PLAN.md` with the WP-03, WP-05 and WP-06 amendments · report `01_CAD/REPORT_od_g01_housing_v03.md`

**VERDICT: REVISE**
Blocking findings: 1 · open assumptions relied on: A-02, A-03, A-04, A-05, A-06, A-10, A-11, A-12, A-13, A-14, A-16, A-17, A-18, A-19, A-21, A-22, A-26

Every §5 row a measurement can answer was re-measured on the exported STEP and passes.
The one blocking row is REQ-12, the 15 bar / 3.06 kN brew load, which spec §5 and §7
answer only by the OD-T01 bench test: no geometry closes it, so it is INCONCLUSIVE, and
an INCONCLUSIVE hard gate blocks by the rule, not by its risk (D-026, PLAYBOOK §6). Six
further deviations are rated and none of them blocks. The Usta can accept REQ-12
knowingly (D-022); nothing in this build needs to change for it.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | yes |
| `02_STEP_STL/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | yes |
| `02_STEP_STL/od_g01_housing_C1_v03.stl` | 0e8fe8e265284ca76cff363dbbd2ab6df5c8485d8e4e8610f58ad29295f38cec | yes |
| `01_CAD/REPORT_od_g01_housing_v03.md` | f9778dac49d98bbf78c4a5fe2e1ef6c998e0e79aa1e6eb90531fdeb9663ce1af | yes |
| `01_CAD/DESIGN_PLAN.md` | 3033b42551718f76820f8d5704056a67b49453f3fcb6d7201937ed32507daf28 | yes |
| `briefs/WP-03_designer.md` | 92ecbb01206d649428b59f59332e77ab22408c08934151eaf5d097ec5172394a | yes |
| `briefs/WP-05_designer.md` | d6a55ab2fd286a8ac23075eb12b63806deb648481bd25dc50090a510cd0c06cd | yes |
| `briefs/WP-06_designer.md` | afb09dc7dfbf5b4af3a672c88a13ea805cd8b60969d73f04e13f4fedcb5b02da | yes |
| `01_CAD/REPORT_od_g01_housing_v02.md` | 02ee81dea9dc7fd9d2dd249cc32481fa96c61e6c89c627df5d8c59466742d5b6 | yes |
| `01_CAD/sweep_v02/sweep_v02.json` | b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3 | yes |
| `03_Sections/od_g01_housing_v03_front.png` | 440317bad3e524ec54b9dab46a13aabb1ff480cd8bc50d39768596cea1232fb1 | yes |
| `03_Sections/od_g01_housing_v03_top.png` | 9c37e36c00ede2a0b82f02c086a4e4a3f41111a2e271569079514f7a754a81c2 | yes |
| `03_Sections/od_g01_housing_v03_left.png` | b1a5f5ca4e8ea8891288192d75d01f3fad3bc93fdb140a10b777cb3935b2627a | yes |
| `03_Sections/od_g01_housing_stopblock_v03_front.png` | f101901d79a301a8fb48524e44a207f7ec1661c93dd410bd6f32e0502aeb7a95 | yes |
| `03_Sections/od_g01_housing_lugunderside_v03_front.png` | 46f4ccc995a5ca0143b7d2faef5f1287687440e53cc411a90702c9722aad7d06 | yes |
| `03_Sections/od_g01_housing_insertboss_v03_front.png` | 2a6022aaa1f071911d3a9b21fcbc1a3d629bdd507e975801444a4cbe32ddcdba | yes |
| `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` | 2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906 | yes (input) |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | yes (input) |
| `00_Spec/inputs/OD-G10_portafilter.step` | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 | yes (input) |

Every hash was computed here and equals the one the brief and the REPORT list; the
delivery must carry exactly these bytes. Completeness: every §5 row is answered in the
REPORT and every listed file is present, so the submission was reviewed, not returned.

**Method.** All gate values come from my own scripts in `reviews/RV01_work/`, run on the
re-imported `od_g01_housing_C1_v03.step` B-rep; the STL only corroborates (D-025). OD-G04
and OD-G10 were placed by this review from the joints spec §5 and the WP-03/WP-06
amendments state (OD-G04 +6.05° about Z, back face to z −6.82; OD-G10 180° about +X, then
+60.26° locked or +122.5° insertion, rim to the pose's z), not read from the designer's
assembly. The locked rim height was found by my own 26-step bisection on `clearance`. No
CAD code of the designer was read. Limits are spec §5's, bands GATES §0's (0.005 mm,
0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts).

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0; 92 faces, all in one shell | 1 / 1 / 0 | 0 | whole part | PASS | `validity` | — |
| U-02 | 100.0000002 × 100.0000002 × 28.2400002 mm; position min (−50.0000001, −50.0000001, −24.9400001), max (50.0000001, 50.0000001, 3.3000001) | each size in [spec − 0.1, spec + 0.1] | +0.0999998 | envelope | PASS | `envelope` | — |
| U-03 | designed contact ear tops → lug undersides 1.99e−15 mm; other rows in the note below | = 0 at the designed contacts; ≥ 0.5 at the seated OD-G04 features; [0.19, 0.21] at the 0.20 mm −Z probe; ≥ 0.30 on the path outside the last 0.5 mm, ≥ 0 inside | −0.0000000 | (30.8756, −7.0938, −6.4508) lug 1 underside | PASS (assumed: A-13, A-14, A-19) | `interference`, `clearance`, own 55-pose path and 66-pose (clock, depth) grid | A-13, A-14, A-19 |
| U-04 | schema AP242 = 1, solids 1, volume_delta 0.0 mm³, faces_delta 0, labels 1, valid_after 1; no stray shell or face outside the solid | re-read unchanged, valid after re-import | 0 | file header and body | PASS | `compare_step`, topology count | — |
| U-05 | 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 2 Ø9 pair-A through-holes, 2 Ø9 recesses, 2 Ø3.8 through-holes, 4 Ø4.0 insert bores; 15 bores in all | = the spec's counts | 0 | §3 below | PASS | `feature_census`, `bore_census`, `locate_bore`, `radial_extent` | — |
| U-06 (Soft) | min_wall wide (45°) 1.1500000 mm | ≥ 1.0 | +0.150 | (32.1295, 18.5500, 0.0000) lug 1 ramp end at the bore | PASS | `min_wall` `detail["wide"]` | — |
| U-07 | delivered STL: two-way deviation from the B-rep 0.0094758 mm; 135 024 triangles, one closed shell, winding out, mesh volume 90 216.199 mm³ against the B-rep's 90 216.792; my own re-export at the REPORT's 0.002 mm / 0.08616775 rad gives the same 135 024 triangles and max_sagitta 0.0094356 mm | sagitta ≤ 0.01; a ≤ 0.08616775 rad | +0.0005242 | whole mesh | PASS | `mesh_deviation`, `mesh_census`, `write_stl` + `mesh_sagitta` (own export) | — |
| U-08 | no helical, thread-named or unnameable face: 40 planes, 30 cylinders, 7 tori, 15 B-splines, 0 other; every insert bore a plain cylinder Ø4.000 | N/A by its row: this target has no thread | — | whole part | N/A: the row names threaded parts and this one has none | `feature_census`, `bore_census` | — |
| D-01a | min_wall 1.5300000 mm (web between the Ø26 opening and a pair-B Ø9 recess); STL corroborates at 1.5316095 ≥ 1.53 − 0.0095 − 0.000006 | ≥ 0.8 | +0.730 | (7.2695, −10.7775, −19.9400) | PASS | `min_wall`, `min_wall_mesh` | — |
| D-01b | min_wall 1.5300000 mm | ≥ 1.0 | +0.530 | same | PASS (assumed: A-05) | `min_wall` | A-05 |
| D-02 | 100.0000002 × 100.0000002 × 28.2400002 mm, mouth up | ≤ 220 × 220 × 250 | +119.9999998 | envelope | PASS (assumed: A-16) | `envelope` | A-16 |
| D-03a | every downward face measured from the B-rep: 3 lug shallow planes at 2.43°, 3 more at 2.51°, 3 ramps at 29.39°, 3 stop-block bottoms at 0.00° (z −10.52), and the rear face at 0.00° (z −24.94, on the bed). Downward faces under 45° that A-22 does not support and that are not the bed face: **0** | ≥ 45° from horizontal, or supported by A-22 | 0 | 13 downward faces, 0.5 mm sampling | PASS (assumed: A-22) | own face-normal scan (`face_samples`), 92 faces | A-22 |
| D-03b | longest unsupported horizontal span 0.0 mm: the only horizontal downward faces are the three stop-block bottoms (supported, A-22) and the bed face | span ≤ 5 | +5.0 | z −10.52 and z −24.94 | PASS | own face-normal scan | — |
| D-04a | Ø3.8000000 mm, both pair-B screw holes | ≥ 3.75 | +0.050 | (−9.3129, 16.5955, −24.9400) and (10.6414, −15.7766, −24.9400) | PASS (assumed: A-26) | `bore_census`, `locate_bore` | A-26 |
| D-05a | boss OD 10.3000000 mm at all four inserts (convex cylinder r 5.15); least material radius round the axis 5.1500000 over 288 rays at four heights, so 10.30 across | material ≥ 8.0 across | +2.300 | (44.0000, 44.0000, −19.4900) and the other three | PASS (assumed: A-17) | `radial_extent` ring, cylinder census | A-17 |
| D-05b | Ø4.0000000 mm; length 5.7000000 mm from the rear face, all four | Ø 4.0 ± 0.05; depth ≥ 5.7 | +0.0000000 (depth), +0.050 (Ø) | (±44, ±44, −24.9400) | PASS (assumed: A-17) | `bore_census`, `locate_bore` | A-17 |
| D-06a | min_wall 1.5300000 mm | ≥ 1.0 | +0.530 | (7.2695, −10.7775, −19.9400) | PASS | `min_wall` | — |
| D-07 | N/A by its row (no reamed fit bore; the insert holes are insert-formed). Measured beside it: Ø26 opening to the OD-G04 hub as placed 2.9700000 mm | ≥ 2.9 radial clearance | +0.070 | (12.5183, −3.5061, −19.9500) | N/A: the row names reamed fit bores and this part has none | `locate_bore`, `clearance` | A-24 |
| J-05 | wall round each insert hole 3.1500000 mm at the boss, 3.1717093 in the slab, worst of 288 rays each | ≥ 3.0 (M3) | +0.150 | (44.0000, 44.0000, −19.4900) | PASS | `radial_extent` ring | — |
| E-06 | four insert bosses, four root fillets: R 0.600 tori centred at (±44, ±44, −19.34), six faces grouped 2 / 2 / 1 / 1 by axis | a root fillet on every insert boss | 0 | the four boss roots | PASS | own torus census on the B-rep | — |
| REQ-01 | inner radius over start + 8°…40°, z −5.0…−1.0: min 31.6800000, max 31.6800000 (99 angles × 40 levels, 3 960 rays, none unread) | in [31.58, 31.78] | +0.100 | (30.6005, −8.1994, −4.9500) | PASS (assumed: A-02) | `radial_profile` | A-02 |
| REQ-02 | inner radius in the gaps, z −13.0…+2.0: min 37.1000000, max 37.1000000 (165 angles × 75 levels, 12 375 rays, none unread) | in [37.05, 37.15] | +0.050 | (30.0145, 21.8068, −12.9000) | PASS (assumed: A-03) | `radial_profile` | A-03 |
| REQ-03 | z −3.0: 31.6800000 at start + 1°, + 27°, + 40°; 37.1000000 at start − 1° and + 55°, all three lugs (15 rays) | ≤ 31.78 / ≥ 37.05 | +0.050 | (33.6240, −15.6791, −3.0000) gap ray | PASS (assumed: A-04) | `radial_extent` | A-04 |
| REQ-04 | start + 20°: 31.6800000 at z −5.7, 37.1000000 at z −6.7; start + 47°: 31.6800000 at z −3.2, 37.1000000 at z −4.2 (12 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (31.6028, −2.2099, −5.7000) | PASS (assumed: A-05) | `radial_extent` | A-05 |
| REQ-05 | start + 2.9°: 31.6800000 at z −9.0, 37.1000000 at z −11.0 (6 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (29.5560, −11.4047, −9.0000) | PASS (assumed: A-06) | `radial_extent` | A-06 |
| REQ-06 | Ø26.0000000 mm, axis offset 0.0000000, through = 1, on the cup axis | Ø 26.0 ± 0.1, on the axis, through | +0.100 | (0.0000, 0.0000, −24.9400) | PASS (assumed: A-10, A-11) | `bore_census`, `locate_bore` | A-10, A-11 |
| REQ-07 | two Ø3.8000000 through-holes at r 19.03, θ 119.3° / 304.0°, offsets 2.6e−07 and 4.7e−08; Ø9.0000000 recesses 2.3000000 deep from the floor | offset ≤ 0.10; Ø 9.0 ± 0.1; 2.30 ± 0.10 | +0.0999997 | (−9.3129, 16.5955, −24.9400) | PASS (assumed: A-12, A-26) | `locate_bore` | A-12, A-26 |
| REQ-08 | four Ø4.0000000 bores at (±44, ±44), offsets 0.0000000 | offset ≤ 0.10 | +0.100 | (44.0000, 44.0000, −24.9400) | PASS (assumed: A-18) | `locate_bore` | A-18 |
| REQ-09 | outer radius 43.1000000 at every 5° over z −19.0…+3.0 (72 × 220 rays, none unread); inner max 37.1000000 in the gaps; wall 6.0000000 | ≥ 43.05 / ≤ 37.15 / ≥ 5.9 | +0.050 | (43.1000, 0.0000, −18.9500) | PASS (assumed: A-21) | `radial_profile` | A-21 |
| REQ-10 | 25 insertion poses at the insertion clock, rim z −5.000 → −11.701029: 0.8239 → 0.4945157 mm | ≥ 0.30 at every pose | +0.1945157 | (−3.3115, 31.5065, 0.0000) lug 2 start corner | PASS (assumed: A-19) | `clearance` over own poses | A-19 |
| REQ-11 | Ø26 bore length 5.0000000 mm (z −24.94 … −19.94) | 5.00 ± 0.10 | +0.100 | (0.0000, 0.0000, −24.9400) | PASS (assumed: A-10) | `locate_bore` | A-10 |
| REQ-12 | not answerable from geometry: the row is the OD-T01 bench test and no test record exists | 15 bar on a Ø51 basket (3.06 kN) | — | the three lugs and their roots | INCONCLUSIVE | — (bench test) | A-21 |
| REQ-13 | two Ø9.0000000 through-holes at r 15.500, θ 359.5° / 179.0°, offsets 3.6e−07 and 4.1e−07, through = 1 | Ø 9.0 ± 0.1, offset ≤ 0.10 | +0.0999996 | (15.4994, −0.1353, −24.9400) | PASS (assumed: A-11) | `locate_bore` | A-11 |

**U-03, row by row** (one §5 row, so one entry above; these are the measurements behind it,
all on my own placement):

| Sub-row | Measured | Required | Margin |
|---|---|---|---|
| (a) `interference` housing \| OD-G04 | 0.000 mm³ | ≤ 0 | 0.000 |
| (a) designed contact: OD-G04 flange bottom on the floor | 0.0000000 mm at (13.0586, 6.4522, −19.9400), not inside | = 0 | 0.000 |
| (a) OD-G04 tabs (cut out of the placed solid at r ≥ 31.6) | 0.5800000 mm, tab tip 34.519 against the riser 35.10 | ≥ 0.5 | +0.080 |
| (a) OD-G04 bead (r 30.9…31.6) | 0.5236629 mm at (26.1248, 17.9551, −15.1700) | ≥ 0.5 | +0.0236629 |
| (a) OD-G04 pair A (r 4.2 about each axis, below the flange) | 1.0100000 mm | ≥ 0.5 | +0.510 |
| (a) OD-G04 pair B | 0.5400000 mm, boss bottom −21.70 over the recess floor −22.24 | ≥ 0.5 | +0.040 |
| (a) OD-G04 hub tube | 2.9700000 mm | ≥ 0.5 | +2.470 |
| (a) locked rim z, my own 26-step bisection of the first contact along +Z at clock 60.26° | −11.2510287 mm | A-14 expects −11.20 ± 0.10 | +0.0489713 |
| (a) designed contact: the three ear tops on the lug undersides at that pose | 1.99e−15 mm at (30.8756, −7.0938, −6.4508) | = 0 | −0.0000000 |
| (a) OD-G10 displaced 0.20 mm along −Z from that pose | 0.1997125 mm | in [0.19, 0.21] | +0.0097125 |
| (a) OD-G10 displaced 0.20 mm along +Z (diagnostic) | 0.0000000 mm | — | — |
| (a) boolean housing \| OD-G10 | INCONCLUSIVE: `common_volume` refuses the pair, OD-G10 reads `brep_valid` 0 (BOPAlgo_InvalidCurveOnSurface) | the ratified row answers by `clearance` (A-28) | — |
| (b) lock path, 55 poses (25 insertion, 20 rotation, 10 seating) | worst outside the last 0.5 mm of travel 0.4945157 mm; worst inside it 0.0000000 mm | ≥ 0.30 outside, ≥ 0 inside | +0.1945157 / +0.0000000 |
| (b) joint (clock, depth) grid, 66 further poses | at full depth (rim −11.70) the grid reads 0.4946 mm at the insertion clock and ≥ 0.5089 mm from 115° to 62.5°, then 0.2765 mm at the stop; on the path the 19 rotation poses outside the exemption stay ≥ 0.5027 mm. Turning before the rim passes −11.45 closes on the lug undersides, which is how a bayonet works, not a fault | evidence for L-09 / L-10 | — |

Per lug at the locked pose, the housing cut into three 120° sectors: **lug 1 0.0000000**,
**lug 2 0.0903189**, **lug 3 0.0210511** mm — see finding F2.

## 3. Feature census against the plan

Plan `01_CAD/DESIGN_PLAN.md` §3 as amended by WP-03 (spec 1.1), WP-05 (spec 1.2) and
WP-06 (spec 1.3).

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 cup outer wall, outer Ø86.2 | convex cylinder r 43.10, z −19.94…+3.30 | r 43.100 on 72 angles × 220 levels; front face at z +3.3000001 | PASS |
| F02 rear slab 100 × 100, corners R 8, 5.00 thick (amended) | square 100 ± 0.1, four R 8 corner arcs, z −24.94…−19.94 | 100.0000002 × 100.0000002; four convex cylinders r 8.0 at (±42, ±42); Ø26 bore length 5.000 through the slab | PASS |
| F04 main bore Ø74.20 straight, flat front face | concave cylinder r 37.10 to the shelf | r 37.100 (Ø74.2 × 16.6, open both ends after the R 0.8 shelf round) | PASS |
| F05 / F06 lip ring R 31.70 / R 31.30 (amended) | two concave cylinders, step at z −17.70 | Ø63.4 × 3.60 (z −17.70…−14.10) and Ø62.6 × 2.24 (z −19.94…−17.70) | PASS |
| F07 three pockets, riser R 35.10, floor −17.30 (amended) | 3 concave cylinders r 35.10, floor at −17.30 | Ø70.2 × 3.20 spanning 190.5° in three pieces; rays read 35.100 at z −16.0 and 31.700 at z −17.6 at start + 26.75° on all three | PASS |
| F08 three lugs, inner R 31.68, span 54° | 3 concave cylinders r 31.68 | r 31.680 at start + 1°, + 27°, + 40° and 37.100 at start − 1°, + 55°, all three | PASS |
| F09 lug underside (two planes) and stop block | 3 lofted undersides, 3 stop-block bottoms at z −10.52 | 9 downward B-spline faces (2.43° / 2.51° shallow, 29.39° ramp) and 3 horizontal faces at z −10.52; REQ-04 and REQ-05 rays as required | PASS |
| F10 keyhole Ø26.0 through the slab, no counterbore (amended) | 1 through-bore Ø26.0 × 5.00 on the axis | Ø26.000 × 5.000, offset 0.0, through | PASS |
| F11 two Ø9.0 pair-A pass-throughs at r 15.5, θ 359.5° / 179.0° (amended) | 2 through-holes merging with the Ø26 | Ø9.000 × 5.000 through at (15.4994, −0.1353) and (−15.4976, 0.2705), 262° span where they merge | PASS |
| F12 / F13 pair-B recesses and screw holes (amended) | 2 × Ø9.0 × 2.30 blind from the floor, 2 × Ø3.8 through | Ø9.000 × 2.300 blind and Ø3.800 × 2.700 through on both axes at r 19.03, θ 119.3° / 304.0° | PASS |
| F14 four carrier insert bosses on the floor side | 4 bosses, OD sized by J-05 (spec §4: ≥ 10.0 across) | 4 convex cylinders r 5.15 (OD 10.30), rising z −19.94…−19.24 | PASS |
| F15 four Ø4.0 × 5.70 insert bores from the rear, no mouth chamfer (amended) | 4 bores Ø4.0, depth 5.7; no cone faces | 4 × Ø4.000 × 5.700, offsets 0.0; 0 cone faces | PASS |
| F16 boss root fillets, ladder [1.0, 0.8, 0.6, 0.4] | a root fillet on each of the four bosses | R 0.600 tori at all four roots (6 faces: 2 / 2 / 1 / 1) | PASS |
| F17 shelf-to-bore fillet, ladder [0.8, 0.6, 0.4] | one concave round below z −13.0 | torus major 36.3, minor 0.8 at z −13.30 | PASS |
| F18 lug root fillets, ladder [0.8, 0.6, 0.4] | a round where each lug side meets the bore wall | none achieved: `min_internal_radius` 0.0, first sharp concave edge at (33.9188, 15.0308, −3.3700) on the bore wall; 48 sharp concave edges in the part | FAIL (finding F4; not a §5 U-05 feature and not in spec §4 C1, so it does not block) |
| F19 body named `od_g01_housing` | the label survives the export | label `od_g01_housing` read back from the STEP | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

Answered from my own toolkit sections in `reviews/RV01_work/` (housing front, top, left; a
lug section; a boss section; the delivered assembly cut through the cup axis) and from the
measurements above. No render was used.

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | In use +Z is horizontal and faces the user (spec §2); the housing hangs on its rear slab, which is the mounting flange, through four M3 inserts at (±44, ±44) whose bosses are tied into the slab with R 0.6 roots, and the brew load runs ear → lug underside → cup wall → slab → carrier through one continuous section. | YES |
| P2 | Function chains connected and aimed? | Water: OD-G04's Ø20.06 hub passes the Ø26.000 × 5.000 opening with 2.970 mm of radial room and ends 2.39 mm inside the slab, so the connection is reached from the rear face (A-24); fasteners: the two OEM screws come from the rear through the Ø3.800 holes into pair B (0.540 mm clear) and pair A passes the two Ø9.000 lobes (1.010 mm clear). | YES |
| P3 | Moving parts oriented for their motion, with clearance? | The portafilter enters along −Z through three 66° gaps (≥ 0.4945 mm over 25 poses), turns 62.24° at depth (≥ 0.5027 mm over the 19 rotation poses outside the last 0.45 mm of travel, 0.2765 mm at the stop block) and seats 0.45 mm to contact; my (clock, depth) grid shows the turn frees up only once the rim is below −11.45, which is the bayonet's own sequence. | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | One opening, one insertion direction, three ears into three gaps ended by a stop block; screws, inserts and the water connection are all reached from the flat square rear face, and the handle swings clear of the housing at the locked clock in the assembly section. | YES |
| P5 | Next to a comparable real product, does anything look absurd? | No: a Ø86.2 cup on a 100 mm square flange 28.24 tall with a keyhole plate and two screw seats reads like the OEM group head it reproduces; the one thing a domain engineer would ask about is the 5.00 mm slab where the OEM has 2.50, which A-24 records as open. | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | One solid, 92 faces, no naked edge; lug 1 starts at 336° counter-clockwise as spec §2 fixes it, the mouth is at +3.3000001 and the rear face at −24.9400001, the keyhole lobes lie at 359.5° / 179.0° and the pair-B recesses at 119.3° / 304.0° in the top section, and OD-G04 seats flange-down while OD-G10 enters rim-first. | YES |

## 5. Positive controls

Every mutant is this job's own part, built from the exported STEP by
`reviews/RV01_work/rv_i_controls.py` and `rv_i2_controls.py`; each check was then run on it.

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` (U-01) | one face taken off the exported solid | FAIL: solid_count 0, naked_edges 2 |
| `envelope` (U-02, D-02) | 0.30 mm pad on the +X side of the flange | FAIL: size_x 100.3000001 against [99.9, 100.1] |
| `clearance` (U-03, REQ-10, D-04c rows) | pocket riser moved 0.30 mm inward (R 35.10 → 34.80) | FAIL: OD-G04 tab clearance 0.2800000 against ≥ 0.5 |
| `interference` / `common_volume` (U-03a) | pocket riser moved 0.70 mm inward | FAIL: housing \| OD-G04 7.9331089 mm³ against ≤ 0 |
| `compare_step` (U-04) | one Ø4.0 insert bore filled with material | FAIL: volume_delta 71.6283156 mm³, faces_delta 3 |
| `bore_census`, `feature_census` (U-05) | the same filled bore | FAIL: 14 bores against 15 |
| `locate_bore` (REQ-06…REQ-08, REQ-11, REQ-13, D-04a, D-05b) | a pair-B screw hole moved 0.5 mm in X | FAIL: offset 0.5000001 against ≤ 0.10 |
| `radial_profile`, `radial_extent` (REQ-01…REQ-05, REQ-09) | lug inner radius cut back 0.30 mm | FAIL: REQ-01 min and max 31.9800000 against [31.58, 31.78]; REQ-03 ray 31.9800000 |
| `min_wall` and its 45° reading (D-01a, D-01b, D-06a, U-06) | a pair-B recess widened Ø9.0 → Ø10.6 | FAIL: min_wall 0.7300000 against ≥ 0.8, wide 0.7300000 against ≥ 1.0 |
| `radial_extent` ring, cylinder census (D-05a, J-05) | one boss replaced by a plain Ø6.8 boss | FAIL: wall 1.4000000 against ≥ 3.0; 6.8000000 across against ≥ 8.0 |
| own torus census (E-06) | the same boss, root fillet removed | FAIL: 1 boss root with a fillet against 4 |
| own face-normal scan (D-03a, D-03b) | a horizontal ledge added inside the bore at z −13.0 | FAIL: one downward face at 0.000° that A-22 does not support, at (−36.853, −4.205, −13.000) |
| `mesh_sagitta` / `write_stl` (U-07) | the same B-rep meshed at the spec's own 0.01 mm | FAIL: max_sagitta 0.0431441 against ≤ 0.01 |
| `mesh_census` (V-05) | the delivered STL with one triangle dropped | FAIL: naked_edges 3 against 0, volume unmeasurable |

Every check family used in §2 has a control that FAILs, so no gate row rests on a check
that cannot fail on this part.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-12 | HARD_GATE_INCONCLUSIVE | no measurement → 15 bar on a Ø51 basket (3.06 kN) on OD-T01 | — | the three lugs and their roots | yes | UNKNOWN | No geometric check answers a strength row; A-21 records that no strength calculation exists and spec §5 defers the row to a bench test that has not been run, so the evidence cannot tell whether the part holds. | Run the OD-T01 bench test on a printed part and record it, or have the Usta accept the row knowingly (D-022); nothing in the CAD closes it. |
| F2 | U-03 | OBSERVATION | one of three ear tops touches at the locked pose: 0.0000000 / 0.0903189 / 0.0210511 mm → the spec's designed contact "the three ear tops on the lug undersides" | −0.0903189 on lug 2 | lug 2 (−9.1585, 30.3273, −6.4582), lug 3 (−21.5419, −23.2286, −6.4480) | no | MEDIUM | Spec 1.3 defines the locked pose as the **first** contact, so the gated pair reads 0 and U-03 passes as ratified; but A-25's ears at 120.5 / 120.5 / 119° cannot all meet a symmetric 120° lug pitch, so the 3.06 kN brew load starts on one lug and only spreads after 0.09 mm is taken up somewhere — the gasket (A-27) is the candidate and is unmeasured, and REQ-12 is untested. | Clock the three lugs to the measured ear pitch, or confirm on the donor that the gasket takes up 0.09 mm before load; either way retire A-25 and A-27 first. |
| F3 | U-03 | OBSERVATION | boolean housing \| OD-G10 INCONCLUSIVE → interference ≤ 0 mm³ | — | housing \| OD-G10 at the locked pose | no | UNKNOWN | `clearance` reads 0 both for a pair that touches and for one that interpenetrates without the nearest points parting, and the OD-G10 input fails `brep_valid` (A-28), so no volume check can rule an overlap out; the 55-pose path (nothing under 0.2765 mm until the last 0.45 mm of travel, a pure translation) is the strongest evidence available and it is indirect. | Rebuild OD-G10 as a sound solid in open-dedica, then re-run `interference` at the locked pose; no change to this part is implied. |
| F4 | plan F18 | OBSERVATION | no lug root fillet achieved: `min_internal_radius` 0.0 mm → the plan's ladder [0.8, 0.6, 0.4] | −0.4 against the smallest rung | first sharp concave edge (33.9188, 15.0308, −3.3700), seven lug root edges | no | MEDIUM | The lug root is the section the whole brew load passes through (A-21) and it is left sharp, which is a stress riser in an FDM part whose layers run across it; no §5 row reads these edges and spec §4 C1 does not state a fillet, so it is not a missing spec feature, but REQ-12 is exactly the row that would find it. | Cut the lug side faces back from the bore by the fillet radius so a round can be built there, or carry the sharp root into the OD-T01 test and judge it from the result. |
| F5 | U-07 | OBSERVATION | STL meshed at 0.002 mm → the row's own "STL at tol 0.01" | — | whole mesh | no | LOW | The delivered mesh is finer than the row asks and passes the gated value (0.0094758 ≤ 0.01); I measured the same B-rep at the row's own 0.01 mm and the sagitta comes out 0.0431441, so the row as written cannot meet its own sagitta limit on this geometry and the deviation is the only way to pass it. | Amend U-07's stated tolerance for this job to 0.002 mm so the row is self-consistent; the delivered file needs no change. |
| F6 | D-05b | OBSERVATION | insert hole depth 5.7000000 mm, open at both ends → depth ≥ 5.7 | +0.0000000 | (±44, ±44), z −24.94…−19.24 | no | LOW | A-17's 5.70 mm hole in a 5.00 mm slab plus a 0.70 mm boss leaves no depth margin and each bore breaks through the boss top, so an insert pressed past flush leaves the far end; the opening sits at r 62.2, outside the cup wall at r 43.1, so it is on the flange's front face and not a water path. | Raise the boss 0.3–0.5 mm, or state the insert seating depth in the print notes. |
| F7 | U-03 | OBSERVATION | ear leading edge to the stop block 0.2764566 mm at the locked clock → ≥ 0.30 outside the last 0.5 mm of travel | −0.0235434, exempt because the pose lies 0.45 mm from the final one | (−23.6314, −21.0993, −10.5200) stop-block face | no | LOW | This is the tightest non-contact gap anywhere on the lock path and it is exempt only by the 0.5 mm approach rule; A-04's ±0.25° on the lug starts moves it by 0.138 mm (0.25° × 31.68 mm), so the stop angle, not the fit, is what a clocking error changes — nothing overlaps at either end of that band. | Retire A-04 and A-14 with a protractor on the donor cup before the first print. |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. Only one ear top touches at the measured locked pose (0 / 0.0903189 / 0.0210511) | Confirmed independently: my own bisection puts first contact at rim z −11.2510287 and my own sector cut of the housing reads 0.0000000 / 0.0903189 / 0.0210511 mm on lugs 1 / 2 / 3. The ratified row gates one pair and it reads 0, so U-03 passes; the load-path consequence is finding F2, rated MEDIUM, for the Usta to accept or fix. |
| 2. `lug_starts_hi` (+0.25°) puts the U-03(a) probe out of band through the stop-block pair | The sensitivity is real and I measured its nominal side: the ear leading edge stands 0.2764566 mm from the stop block at the locked clock, and 0.25° at r 31.68 is 0.138 mm, which is the number the designer's sweep reports. I did not re-run the sweep (one review, no rebuild). The delivered part at nominal reads 0.1997125 mm on the probe, inside [0.19, 0.21]; the row is sensitive to lug clocking through the stop, not through the contact. Finding F7, LOW. |
| 3. Everything resting on OD-G10's boolean | Confirmed: `common_volume` refuses the pair (OD-G10 `brep_valid` 0, BOPAlgo_InvalidCurveOnSurface) exactly as A-28 says, so the row stands on distance alone. My own 55-pose path and 66-pose (clock, depth) grid add that nothing on the way in comes under 0.2765 mm until the last 0.45 mm, which is a pure translation — strong but indirect. Finding F3, UNKNOWN. |
| 4. The smaller ones: D-05b's zero depth margin and the bore opening on the cup floor; the bead and pair-B margins; the sharp lug roots; A-14's ±0.10 band | Depth 5.7000000 with zero margin and a through bore: confirmed, finding F6 — but the opening is at r 62.2, outside the cup wall at r 43.1, so it is on the flange's front face and not "a hole into the wet side" as the REPORT calls it. Bead 0.5236629 (+0.0237) and pair B 0.5400000 (+0.040): confirmed, both above the 0.5 floor. Sharp lug roots: confirmed, 48 sharp concave edges, finding F4. A-14: my own first contact is −11.2510287, inside the ±0.10 band by 0.0489713, so the underside level (A-05) has about 0.05 mm of room before the row fails — the same conclusion the REPORT draws. |

## 8. Notes on the method

- The STL cannot be reproduced byte for byte: my own export of the same B-rep at the
  REPORT's tolerance (0.002 mm, 0.08616775 rad) gives the same 135 024 triangles, the same
  file size and the same measured sagitta 0.0094356 mm, but a different triangulation, so
  OCCT's parallel mesher is not deterministic here. The delivered mesh was therefore
  accepted on measurement — one closed shell, winding out, two-way deviation 0.0094758 mm,
  mesh volume within 0.593 mm³ of the B-rep — not on bytes.
- `step_roundtrip` cannot be run on a part read back out of its own STEP (the writer
  refuses a part that sits in an assembly), so U-04 was answered with `compare_step`
  against the delivered file plus a topology count: 1 solid, 1 shell, 92 faces, none
  outside the solid.
- The delivered check assembly was measured as placed as well: its housing has the same
  volume as the part file (90 216.7916544 mm³), OD-G10's rim sits at z −11.2510288 — the
  pose my own bisection found — and housing \| OD-G04 reads 0.000 mm³ of interference with
  a 0 mm designed contact on the floor.
- The cited D7 record `01_CAD/sweep_v02/sweep_v02.json` hashes as the REPORT states; of its
  40 runs all 40 built and no row outside the U-03 family, which spec 1.3 re-words, is
  anything but PASS or PASS_ASSUMED. That supports the REPORT's §4 claim; it is not a gate
  row of this review.
