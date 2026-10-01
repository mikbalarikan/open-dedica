# REPORT — od_g01_housing v01 (20260930-od-g01-group-head-housing)

Designer: Claude Code, Opus 5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` with the WP-03 amendments · 2026-09-30 UTC

**Outcome: STOPPED (D9).** The part is built, exported and measured, and every §5
row is answered below. Four rows fail on one feature: the rear face of the slab
carries a **0.130 mm** web between REQ-13's Ø34.0 counterbore wall and REQ-07's
Ø3.8 screw hole, and a **0.200 mm** flake between the Ø9.0 recess floor and the
counterbore ceiling. No value inside spec 1.1's own tolerances lifts either above
D-01a's 0.8 (§10 shows the arithmetic and three measured options).

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_g01_housing.py` | cebb644b9dc98d1a695acbdd0b3c5c2cd401d8fb2588560ac6c17a1f3aa04883 | parametric script, build123d Algebra mode, one Params structure |
| `01_CAD/check_od_g01_housing.py` | d6e525753b9717b7d69a24330b0358b64d5a0560a9e7371705b0f30be573c6e5 | checks, written before the build (D3) |
| `01_CAD/assemble_od_g01_check.py` | 40afd4f319916d553f67233b8e5aa41d8b8ac9d6e3fe2e04b1f8f0de5883544c | the spec §5 joints and the U-03(a) feature pieces |
| `01_CAD/sweep_od_g01_v01.py` | c727c0417f7e7cfe50b51b4aa05a6a54afc88bd00c6553cf00ad7ec22615cedf | D7 sweep driver |
| `01_CAD/sections_od_g01_v01.py` | fda04c138a9f234aa298c5f77f363545fb7230e83175c10a794f0afeb701f169 | D6 sections |
| `01_CAD/tradeoff_od_g01_v01.py` | eab7cf029b998483a6fbdd9183c89a7b9d0c9c372d3e82d0bd5a2f4c87ba8ec0 | the measured options of §10 |
| `01_CAD/probe_inputs_v01.py` | 2dc1a4703f20de85aa6cc52ed7000c976b16a9b723931bdc56e64e7b31f2c2f5 | diagnostic probe of the three reference solids in the housing frame |
| `01_CAD/measured_v01.json` | 2e4776fbd06ad231c4e0637e869647e028b03a498d90092209b13f82423ad5e5 | every gate row with its measurement and detail |
| `01_CAD/sections_v01.json` | 2afbd86153db0d8d84afb4062b0abec2849be68cf98eaa02e5c2a9848947e33b | the sections with nothing_clipped |
| `01_CAD/tradeoff_v01.json` | d61f87f9b5c20dd487d3b9f7b13dd48c85855d3cf26dfdfff91a6329289d3953 | §10's options, measured |
| `01_CAD/sweep_v01/sweep_v01.json` | d122308695630b272a755c8b47fd9786a2adcfa01ba54e1b9844ddfb25745cb7 | D7 results, one entry per case |
| `01_CAD/sweep_v01/motion_v01.json` | 62ec1e86484cb940434bb62c0464263d2377d79fabf980b7d9f5cf42fa24fcf7 | the lock path, swept |
| `02_STEP_STL/od_g01_housing_C1_v01.step` | 9b5d10575a0f250df84988b459fa603b941ff812a603c83b1bdd86f6170b96e5 | AP242 (tools.core.write_step), re-imported for every measurement |
| `02_STEP_STL/od_g01_assembly_C1_v01.step` | f6458ce820aaf7639c164e2bc54f25d23e06b09a144b8b92f4f4a8804851369b | check assembly: housing + OD-G04 seated + OD-G10 at the locked pose |
| `02_STEP_STL/od_g01_housing_C1_v01.stl` | e799b9aeaf84bbb3ccc5c9d9465f8c4e0d37a3bb90848ec33dd4a538b1e87ca3 | triangulation cleared first; tolerance 0.002 mm, angular 0.08616775 rad, 135 974 triangles, measured sagitta 0.00944 mm |
| `03_Sections/od_g01_housing_v01_front.png` | a8c4451a69926ba96f3304ef13b3c6e46aa7e7c40c2fef56816bbadfd0df07e7 | section y = 0 (lug 1 underside, gap at 180°), nothing_clipped 0 |
| `03_Sections/od_g01_housing_v01_top.png` | addfed5d9bd1cbc680567105fe9507cf4c2082c0ced6501795c0513e3a12dfba | section z = −15.87 (pockets, lip ring, keyhole, inserts), nothing_clipped 0 |
| `03_Sections/od_g01_housing_v01_left.png` | ed0cf20756146a01f95f940ec8b0c44e86fd8962ee22551a49b683f271492bb6 | section x = 0, nothing_clipped 0 |
| `03_Sections/od_g01_housing_stopblock_v01_front.png` | 0baca9a6f03cf7c15f89885d5877edb518caa34a394a11afdf314d7e5f4df7bb | section through a stop block (lug 1 + 2.9°), nothing_clipped 0 |
| `03_Sections/od_g01_housing_insertboss_v01_front.png` | c8d9f25cf54f535c1868818b13ad10ae2c9bcd1605e77aac023bd746f904e618 | section through two carrier insert bosses, nothing_clipped 0 |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 (pinned, D-023) · OCP 7.9.3.1.1 (OCCT 7.9.3) ·
numpy 2.5.3 · repo commit `3fa319f`. Input hashes checked against the brief before
any other work: all three match (`OD-G09` 2f11c1b7…, `OD-G04` 19b4a140…, `OD-G10`
3a525af1…).

## 3. Gate self-check

Every value is measured by `check_od_g01_housing.py` on the B-rep of the
re-imported `02_STEP_STL/od_g01_housing_C1_v01.step`; limits are spec §5's, bands
are GATES §0's (0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts). Where
a gate has several rays or several sub-rows, the row below is the worst of them and
`01_CAD/measured_v01.json` holds them all. A self-check clears nothing: the
reviewer's own measurement does.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | size_x 100.0000002, size_y 100.0000002, size_z 28.2400002 mm | each in [spec ± 0.1] | +0.0999998 | — | PASS | — |
| U-03 (a) housing\|OD-G04 | 0.000 mm³ | ≤ 0 mm³ | 0.000 | — | PASS (assumed: A-13) | A-13 |
| U-03 (a) designed contact, OD-G04 flange on the floor | 0.000 mm | = 0 | 0.000 | (13.059, 6.452, −19.940) | PASS (assumed: A-13) | A-13 |
| U-03 (a) OD-G04 tabs | 0.580 mm (tab 1; tabs 2 and 3 the same) | ≥ 0.5 | +0.080 | (29.340, 19.266, −15.460) | PASS (assumed: A-12, A-13) | A-12, A-13 |
| U-03 (a) OD-G04 bead | 0.5237 mm | ≥ 0.5 | +0.0237 | (−27.172, −16.327, −15.170) | PASS (assumed: A-09, A-13) | A-09, A-13 |
| U-03 (a) OD-G04 pair A | 1.010 mm | ≥ 0.5 | +0.510 | (12.578, 3.287, −22.440) | PASS (assumed: A-11, A-12) | A-11, A-12 |
| U-03 (a) OD-G04 pair B | 0.540 mm | ≥ 0.5 | +0.040 | (−10.298, 18.336, −22.240) | PASS (assumed: A-12) | A-12 |
| U-03 (a) OD-G04 hub | 2.970 mm | ≥ 0.5 | +2.470 | (−12.487, 3.615, −21.725) | PASS (assumed: A-24) | A-24 |
| U-03 (a) housing\|OD-G10 locked, boolean | INCONCLUSIVE (the input solid is not sound) | ≤ 0 mm³ | — | — | INCONCLUSIVE | A-14, A-19 |
| U-03 (a) designed contact, ear tops on the lug undersides | 0.000 mm | = 0 | 0.000 | (35.270, −7.036, −6.400) | PASS (assumed: A-14) | A-14 |
| U-03 (b) lock path | boolean INCONCLUSIVE; measured clearance ≥ 0.2765 mm over the 8 + 13 poses of the two-leg path | ≤ 0 mm³ | — | rotation leg, clock 60.26° | INCONCLUSIVE | A-14, A-19 |
| U-04 | schema 1, solids 1, labels 1, faces_delta 0, volume_delta 4.1e−09 mm³, valid_after 1 | as stated | −4e−09 mm³ | — | PASS | — |
| U-05 | 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 1 Ø34 counterbore, 4 Ø9 (2 pass-through + 2 recesses), 2 Ø3.8, 4 Ø4.0 | = the plan's counts | 0 | — | PASS | — |
| U-06 (Soft) | min_wall wide (45°) 0.130 mm | ≥ 1.0 | −0.870 | (9.579, −14.201, −24.940) | **FAIL** | — |
| U-07 | sagitta 0.00944 mm at tolerance 0.002 mm, angular 0.08616775 rad, 135 974 triangles | sagitta ≤ 0.01, tol ≤ 0.01, a ≤ 0.08616775 | +0.00056 (sagitta), 0.000 (angular) | — | PASS | — |
| U-08 | faces the census cannot name: 0; every insert bore a plain cylinder Ø4.000 | = 0 (N/A by its row: no thread) | 0 | — | PASS | — |
| D-01a | min_wall 0.130 mm, cylinder to cylinder | ≥ 0.8 | −0.670 | (9.579, −14.201, −24.940) | **FAIL** | — |
| D-01b | min_wall 0.130 mm | ≥ 1.0 | −0.870 | same | **FAIL** | A-05 |
| D-02 | 100.0000002 × 100.0000002 × 28.2400002 mm | ≤ 220 × 220 × 250 | +119.9999998 | — | PASS (assumed: A-16) | A-16 |
| D-03a | no overhang measurement in `tools/measure` (GATES: reviewer, from sections) | ≥ 45° or supported by A-22 | — | sections, §6 | INCONCLUSIVE | A-22 |
| D-03b | no bridge measurement in `tools/measure` (GATES: reviewer, from sections) | span ≤ 5 | — | sections, §6 | INCONCLUSIVE | — |
| D-04a | Ø3.800 mm, both pair-B screw holes | ≥ 3.75 | +0.050 | (−9.313, 16.595, −24.940) | PASS (assumed: A-26) | A-26 |
| D-05a | material across each Ø4.0 insert axis 10.300 mm (288 rays) | ≥ 8.0 | +2.300 | (44, 44, −19.590) | PASS (assumed: A-17) | A-17 |
| D-05a boss OD | no boss-OD measurement in `tools/measure` (GATES: reviewer) | OD ≥ 8.0 | — | — | INCONCLUSIVE | A-17 |
| D-05b | Ø4.000 mm, depth 5.700 mm from the rear face, all four | Ø in [3.95, 4.05], depth ≥ 5.7 | +0.000 (depth) | (44, 44, −24.940) | PASS (assumed: A-17) | A-17 |
| D-06a | min_wall 0.130 mm | ≥ 1.0 | −0.870 | (9.579, −14.201, −24.940) | **FAIL** | — |
| D-07 | Ø26 opening to the OD-G04 hub as placed 2.970 mm | N/A by its row; ≥ 2.9 | +0.070 | (−12.487, 3.615, −21.725) | PASS (assumed: A-24) | A-24 |
| J-05 | wall around each insert axis 3.150 mm, worst of 288 rays | ≥ 3.0 | +0.150 | (44, 44, −19.590) | PASS (assumed: A-17) | A-17 |
| E-06 | no boss-root measurement in `tools/measure` (GATES: reviewer); root fillet achieved R 0.6 on all four bosses | a root fillet on every boss | — | sections, §6 | INCONCLUSIVE | — |
| REQ-01 | inner radius over start + 8°…40°, z −5.0…−1.0: min 31.680, max 31.680 mm (99 angles × 40 levels) | in [31.58, 31.78] | +0.100 | (30.601, −8.199, −4.950) | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner radius in the gaps, z −13.0…+2.0: min 37.100, max 37.100 mm (84 angles × 75 levels) | in [37.05, 37.15] | +0.050 | (30.015, 21.807, −12.900) | PASS (assumed: A-03) | A-03 |
| REQ-03 | z −3.0: 31.680 at start + 1°, + 27°, + 53°; 37.100 at start − 1° and + 55°, all three lugs (15 rays) | ≤ 31.78 / ≥ 37.05 | +0.050 | (33.624, −15.679, −3.000) | PASS (assumed: A-04) | A-04 |
| REQ-04 | start + 20°: 31.680 at z −5.9, 37.100 at z −7.0; start + 50°: 31.680 at z −2.3, 37.100 at z −3.2 (12 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (31.603, −2.210, −5.900) | PASS (assumed: A-05) | A-05 |
| REQ-05 | start + 2.9°: 31.680 at z −9.0, 37.100 at z −11.0 (6 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (29.556, −11.405, −9.000) | PASS (assumed: A-06) | A-06 |
| REQ-06 | Ø26.000 mm, axis offset 0.000 mm, through = 1 | Ø 26.0 ± 0.1, on the axis, through | +0.100 | (0, 0, −22.440) | PASS (assumed: A-10, A-11) | A-10, A-11 |
| REQ-07 | two Ø3.800 through-holes at r 19.03, θ 119.3° / 304.0°, offset 0.000; recesses Ø9.000 × 2.300 deep | offset ≤ 0.10, Ø9.0 ± 0.1, 2.30 ± 0.10 | +0.100 (offset) | (−9.313, 16.595, −24.940) | PASS (assumed: A-12, A-26) | A-12, A-26 |
| REQ-08 | four Ø4.000 bores at (±44, ±44), offset 0.000 mm | offset ≤ 0.10 | +0.100 | (44, 44, −24.940) | PASS (assumed: A-18) | A-18 |
| REQ-09 | outer radius 43.100 mm at every 5° over z −19.0…+3.0 (72 × 220 rays); inner max 37.100 in the gaps; wall 6.000 mm | ≥ 43.05 / ≤ 37.15 / ≥ 5.9 | +0.050 | (43.100, 0.000, −18.950) | PASS (assumed: A-21) | A-21 |
| REQ-10 | 7 poses, rim z −5.000 → −11.252 at the insertion clock: 0.8239 → 0.5166 mm | ≥ 0.30 at every pose | +0.2166 | (−3.312, 31.507, 0.000) | PASS (assumed: A-19) | A-19 |
| REQ-11 | Ø26 bore length 2.500 mm | 2.50 ± 0.10 | +0.100 | (0, 0, −22.440) | PASS (assumed: A-10) | A-10 |
| REQ-13 | counterbore Ø34.000 × 2.500 deep from the rear face; two Ø9.000 through-holes at r 15.500, θ 359.5° / 179.0°, offset 0.000 | Ø34.0 ± 0.1, 2.50 ± 0.10, Ø9.0 ± 0.1, offset ≤ 0.10 | +0.100 | (15.499, −0.135, −24.940) | PASS (assumed: A-11, A-24) | A-11, A-24 |
| REQ-12 | not a geometric gate: the OD-T01 bench test answers it | 15 bar on a Ø51 basket (3.06 kN) | — | — | INCONCLUSIVE | A-21 |
| exactly_one_solid | 1 | = 1 | 0 | — | PASS | — |
| feature_census | planes 42, cylinders 32 (25 concave, 9 convex), tori 7, B-splines 21, other 0, bores 16; every counted feature at the plan's count | = the plan | 0 | — | PASS | — |
| envelope_within_spec | size 100.0000002 × 100.0000002 × 28.2400002 mm; position min (−50.0000001, −50.0000001, −24.9400001), max (50.0000001, 50.0000001, 3.3000001) | size in [spec ± 0.1]; position apart | +0.0999998 | — | PASS | — |

**The two walls that fail.** `min_wall` finds 0.130 mm between two cylinder faces
at (9.579, −14.201, −24.940), which is r 17.13 on the rear face: the web between
REQ-13's counterbore wall (r 17.000) and REQ-07's Ø3.8 screw hole at r 19.03
(inner edge r 17.130). The second thin region is measured from the located bores:
the Ø9.0 recess ends at z −22.240 and the Ø34 counterbore starts at z −22.440, so
0.200 mm of slab is left wherever the two overlap in plan, which they do over a
lens of about 13 mm² (computed from the two measured circles, not measured on a
face). §10 has the options.

**Why the OD-G10 boolean is INCONCLUSIVE.** `tools.core.common_volume` refuses the
pair: "solid 1 of b: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface".
`validity(OD-G10)` on the input STEP itself reads `solid_count 1, naked_edges 0,
brep_valid 0`, so no boolean row can be gated against it, by the designer or by the
reviewer; distance measurements are unaffected. Beside the gate, as a diagnostic:
the raw common solid at the ledger's locked pose holds **two lumps, 0.3317 and
0.0618 mm³**, both inside z −6.456…−6.090 and r ≤ 35.57 — the ear tops on the lug
undersides, that is the designed contact, pressed 0.0515 mm past the housing's own
first contact, which is measured by bisection on clearance at the locked clock at
**rim z −11.2515** against the ledger's locked rim z −11.20.

## 4. Robustness sweep (D7)

Every run rebuilds the part, exports its STEP into `01_CAD/sweep_v01/` (never into
`02_STEP_STL/`) and runs the same predicates on the re-imported file: the geometric
rows on every case, and the rows that need OD-G10 as placed on the cases that can
move the ear passage. `min_wall` is not re-run per case: the wall that fails is set
by REQ-07 and REQ-13, which no swept parameter moves, and it is answered in §3 and
§10.

| Parameter | Low · high (nominal in `build_od_g01_housing.py`) | All built, one solid | Worst row of the two runs | Worst margin |
|---|---|---|---|---|
| `bore_r` | 37.05 · 37.15 | yes | REQ-02 PASS_ASSUMED 37.05 in `bore_r_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | 0.0 |
| `lug_inner_r` | 31.58 · 31.78 | yes | REQ-01 PASS_ASSUMED 31.58 in `lug_inner_r_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | -0.0 |
| `lug_span` | 53.75 · 54.25 | yes | U-03 (a) housing\|od_g04 PASS_ASSUMED 0.0 in `lug_span_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | 0.0 |
| `lug_starts` | −0.25° · +0.25° on all three starts | yes | REQ-03 FAIL 37.1 in `lug_starts_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | -5.32 |
| `stop_end_off` | 5.26 · 6.26 | yes | U-03 (a) housing\|od_g04 PASS_ASSUMED 0.0 in `stop_end_off_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | 0.0 |
| `stop_bottom_z` | -10.82 · -10.22 | yes | U-03 (a) housing\|od_g04 PASS_ASSUMED 0.0 in `stop_bottom_z_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | 0.0 |
| `shelf_z` | -14.2 · -14.0 | yes | U-03 (a) housing\|od_g04 PASS_ASSUMED 0.0 in `shelf_z_lo` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | 0.0 |
| `pocket_floor_z` | -17.4 · -17.2 | yes | D-05b PASS_ASSUMED 5.7 in `pocket_floor_z_lo` | 0.0 |
| `pocket_riser_r` | 34.95 · 35.25 | yes | D-05b PASS_ASSUMED 5.7 in `pocket_riser_r_lo` | 0.0 |
| `pocket_start_off` | -5.5 · -4.5 | yes | D-05b PASS_ASSUMED 5.7 in `pocket_start_off_lo` | 0.0 |
| `pocket_end_off` | 58.0 · 59.0 | yes | D-05b PASS_ASSUMED 5.7 in `pocket_end_off_lo` | 0.0 |
| `lip_upper_r` | 31.65 · 31.78 | yes | U-05 FAIL 0 in `lip_upper_r_hi` | -3.0 |
| `lip_lower_r` | 31.25 · 31.35 | yes | D-05b PASS_ASSUMED 5.7 in `lip_lower_r_lo` | 0.0 |
| `plate_t` | 4.9 · 5.1 | yes | U-02 PASS 28.34 in `plate_t_hi` | -0.0 |
| `keyhole_d` | 25.95 · 26.05 | yes | D-05b PASS_ASSUMED 5.7 in `keyhole_d_lo` | 0.0 |
| `pair_b_r` | 18.98 · 19.08 | yes | D-05b PASS_ASSUMED 5.7 in `pair_b_r_lo` | 0.0 |
| `carrier_xy` | 43.95 · 44.05 | yes | D-05b PASS_ASSUMED 5.7 in `carrier_xy_lo` | 0.0 |
| `insert_d` | 3.98 · 4.02 | yes | D-05b PASS_ASSUMED 5.7 in `insert_d_lo` | 0.0 |
| `insert_depth` | 5.7 · 6.0 | yes | D-05b PASS_ASSUMED 5.7 in `insert_depth_lo` | 0.0 |
| `under_knots` | every knot −0.3 · +0.3 (A-05's ±0.3 bracket) | yes | REQ-03 FAIL 37.1 in `under_knots_hi` (and U-03 (a) housing\|od_g10 locked INCONCLUSIVE) | -5.32 |

**What the sweep found.** All 40 runs built exactly one valid solid, and 36 of them
pass every row they ran. Four do not, and three of those are worth the reviewer's
time:

- **`lug_starts` at −0.25°**: REQ-03's start + 53° ray reads 37.100 instead of
  ≤ 31.78 (margin −5.32). The lug is there; the ray, placed at the nominal start,
  lands 0.25° further along the steep lead-in the gate rows force (deviation 4),
  where the underside has already risen above z −3.0. This is the same 0.2 mm
  window as §9's first point, seen from the other side: the lug layout has no
  angular margin at that ray.
- **`under_knots` at ±0.3** (A-05's own bracket): low, REQ-04 fails at start + 50°
  (31.680 where ≥ 34.0 is wanted at z −3.2, margin −2.32); high, REQ-03 fails at
  start + 53° **and** the designed contact opens — `clearance(housing, OD-G10
  locked)` reads 0.2486 mm where U-03(a) wants 0, so the ears no longer touch the
  lug undersides at the ledger's locked pose. The lug underside therefore has about
  ±0.1 mm of room, not A-05's ±0.3.
- **`lip_upper_r` at 31.78**: U-05 and `feature_census` read 0 pockets instead of 3.
  The pockets are there (the riser probe still reads ≥ 34.5 at their centres); it is
  the census predicate that stops recognising them, because it looks for material at
  r ≤ 31.75 below the pocket floor and the lip wall has moved out to 31.78. That is
  a limit of the predicate, written at D3 against the nominal lip radius, and it is
  reported rather than quietly widened.
- **`plate_t` at ±0.10**: U-02's `size_z` (28.3400002 against the band's 28.34) and
  REQ-11's web (2.3999999999999986 against 2.40) land exactly on their limits and
  pass only inside GATES §0's band; anything past ±0.10 on the slab fails both.

Every case that places OD-G10 leaves U-03(a)'s boolean INCONCLUSIVE for the reason
in §3.

**The lock path (U-03(b), L-09, L-10)**, `01_CAD/sweep_v01/motion_v01.json`:

- The two-leg assembly path is clear all the way. Leg 1, descent at the insertion
  clock 122.5° (ears centred in the gaps), rim −5.000 → −11.690: clearance 0.8239,
  0.7727, 0.7215, 0.6703, 0.6191, 0.5678, 0.5166 mm at −11.252, and 0.4951 mm at
  −11.690. Leg 2, rotation at rim −11.690 from clock 122.5° to the locked 60.26°,
  13 poses: 0.4951 → 0.5093 → 0.5849 → **0.2765 mm**, the smallest at the locked
  clock. Both legs sweep the variable that moves and hold the other, and together
  they cover the path from first approach to the final pose.
- A straight joint interpolation between the two end poses (clock 122.5° → 60.26°
  while the rim goes −5.0 → −11.20, 22 poses) reads clearance 0 from pose 6
  (clock 104.72°, rim −6.771) onward. That interpolation is **not** the assembly
  path: it turns the ears into the lugs before they are deep enough. It is reported
  because L-09 asks for the variables to be swept together and this is what the
  joint sweep measures.
- The boolean along either path is INCONCLUSIVE for the reason in §3.

## 5. Build facts

- Envelope 100.0000002 × 100.0000002 × 28.2400002 mm, from min (−50.0000001,
  −50.0000001, −24.9400001) to max (50.0000001, 50.0000001, 3.3000001); volume
  89 502.778 mm³; mass 95.768 g at 1070 kg/m³ (A-15, reported, not gated); centre
  of mass (−0.0026, −0.0019, −15.8691) mm.
- Fillets, requested → achieved: four carrier boss roots **R 1.0 → R 0.6** (R 1.0
  and R 0.8 each failed; the boss stands only 0.70 above the floor); the
  shelf-to-bore concave circle **R 0.8 → R 0.8** (first rung); the seven lug root
  edges **R 0.6, 0.5, 0.4, 0.3 → none achieved**, those edges stay sharp (OCCT
  refuses every rung where a lug side face meets the bore wall beside the lofted
  underside). No §5 row reads those edges. A failed rung edits the shape it is
  handed, so every ladder runs on a copy and a ladder that finds no radius returns
  the untouched part.
- Placements, every frame from a measured feature of the mating part, never a
  bounding box (L-02). **OD-G04**: its own plate back face (its z = 0) and its tab 1
  centre (its report measures −3.3°) → rotate +6.05° about Z, translate z −6.82, so
  its flange bottom face (its z −13.12) lands on the floor z −19.94; measured on the
  placed solid: envelope z −22.940…−5.730, tab tip radius 34.5191 at z −15.500,
  bead peak 31.1759 at z −15.170, pair A at r 15.5 / θ −0.5° and 179.0° reaching
  z −22.940, pair B at r 19.03 / θ 119.32° and 304.03° reaching z −21.700, hub
  bottom −22.550. **OD-G10**: its cup rim end face (its z = 0) and its ear 1 centre
  (59.5° from the handle) → 180° about +X, then +60.26° about Z (locked) or +122.5°
  (insertion), then the rim to the pose's z.
- The check assembly STEP holds the three parts as placed, labelled
  `od_g01_housing`, `od_g04_brewing_gasket_support`, `od_g10_portafilter`.

## 6. Plausibility (§P, D6)

| # | Question | Answer, from the five sections |
|---|---|---|
| P1 | Gravity | Yes: the rear slab is the mounting flange and four M3 inserts at (±44, ±44) take it to OD-C05; the three lugs hang over the ears and the brew load runs ears → lug undersides → cup wall → slab → carrier, one continuous section in the front cut. |
| P2 | Function chains | Yes: water enters OD-G04's hub tube through the Ø26 opening and leaves the rear through the Ø34 counterbore to OD-H14/H15 (A-24); the two OEM screws run from the rear through the Ø3.8 holes into pair B, and OD-G04's pair A passes the two Ø9 lobes — all visible in the top section. |
| P3 | Motion | Yes: the portafilter enters along −Z through three 66° gaps and turns 62.24° to the stop blocks; measured clearance stays ≥ 0.2765 mm over the two-leg path and the ear tops land on the lug undersides at the stop (§4). |
| P4 | Human factors | Yes: one opening, one insertion direction, three ears into three gaps with a stop block that ends the turn; screws, inserts and the water connection are all reached from the flat square rear face. |
| P5 | Absurdity next to a real product | No, with one exception: as a Ø86.2 cup on a 100 mm square flange 28.24 tall it reads like the OEM group head it reproduces, but a domain engineer would point straight at the rear face, where the counterbore wall and a screw hole are 0.13 mm apart (§10). |
| P6 | Nothing floating, embedded, mirrored or upside-down | Yes: one solid with every feature attached; lug 1 starts at 336° counter-clockwise as spec §2 fixes it, the mouth is at +3.30 and the rear face at −24.94, and the keyhole lobes sit at 359.5° and 179.0° against the pair-B recesses at 119.3° and 304.0°, which the top section shows. |

## 7. Library and tools used

Cards (D1, two by tag, read at J2): `library/uno10/CARD.md#u4-puck` — the polar
(r, θ, z) profile map, and its recorded lesson that a press-turn joint must be swept
over rotation and axial position together, which §4's lock path follows; and
`library/uno10/CARD.md#u5-tank-heat-set` — the heat-set boss arrangement, and
keeping "how big" and "where" apart in the envelope rows (L-12).

`tools/` used: `core.read_step`, `core.write_step` (AP242, D-024), `core.write_stl`,
`core.mesh_sagitta`, `core.step_roundtrip` / `compare_step`, `core.validity`,
`core.common_volume`, `core.fillet_ladder`; `measure.envelope`,
`measure.feature_census`, `measure.bore_census`, `measure.locate_bore`,
`measure.min_wall`, `measure.radial_extent`, `measure.radial_profile`,
`measure.interference`, `measure.clearance`, `measure.mass_properties`;
`result.gate`; `drawing.write_sections`, `drawing.nothing_clipped`.

**`tools/measure` functions this target needed and does not have** (named again from
DESIGN_PLAN §2): an overhang measurement (D-03a), a bridge measurement (D-03b), a
boss-OD measurement (the second half of D-05a), a boss-root check (E-06), and a
local wall measurement (J-05 is answered from `radial_extent`'s own material
stretches on 288 rays around the four insert axes, a located B-rep measurement, with
the whole-part `min_wall` reported beside it). One more is new from this job: **no
boolean row can be gated against an input solid that reads `brep_valid = 0`**
(OD-G10), and no tool in `tools/` repairs or re-sews such a solid.

Job code written, all in `01_CAD/` and none in the repository:
`build_od_g01_housing.py`, `check_od_g01_housing.py`, `assemble_od_g01_check.py`,
`sweep_od_g01_v01.py`, `sections_od_g01_v01.py`, `tradeoff_od_g01_v01.py`,
`probe_inputs_v01.py`.

## 8. Deviations from the plan

The WP-03 amendments (slab 5.00, lip ring 31.70 / 31.30, pockets at −17.30 with a
riser, keyhole plus rear counterbore, Ø9 lobes, pair-B recesses with Ø3.8 holes,
carrier inserts 5.7 deep from the rear with a boss, the OD-G04 joint at +6.05° and
the flange seat, U-03(a)'s contact list, REQ-10 at 0.30, the census) were built as
the brief states them. Beyond those:

1. **The lip ring's upper section runs to the shelf.** The amendment reads "upper
   R 31.70 (z −17.70 … −15.60)"; built R 31.70 from z −17.70 up to the shelf
   z −14.10. Measured reason: OD-G04's bead peaks at r 31.1759 at housing z −15.170
   and keeps r > 30.8 up to z −13.9 — that is **above** −15.60, where A-09's own
   derivation (bead + 0.5) puts the 31.70 wall; and the OEM's shelf edge is fitted
   as an arc tangent to the shelf plane and the lip wall (OD-G09 PARAM_TABLE
   `SHELF_EDGE_FILLET_R`), so nothing stands between them. Measured bead clearance
   as built: 0.5237 mm.
2. **The pocket is built inward of the riser.** §4 C1 reads "floor z −17.30 between
   R 35.00 and the bore"; built as the notch between the lip wall (r 31.70) and the
   riser (r 35.10), floor −17.30, open to the shelf. Measured reason: OD-G04's tabs
   reach r 34.5191 over z −16.34…−14.58 as placed, which is inside solid material
   under the literal reading, and A-08's own derivation ("R 35.00 so the tabs keep
   0.5 clearance") only works with the riser outside the tab tip. The OEM cup is
   built the same way (OD-G09 PARAM_TABLE: pocket inner floor fitted over
   r 31.8…34.0, riser at r 34.391).
3. **Pocket riser R 35.10, not 35.00.** The tab tip measures 34.5191 on the placed
   solid, so R 35.00 gives 0.481 mm and misses §6 U-03(a)'s 0.5. Measured tab
   clearance at 35.10: 0.580 mm.
4. **Lug underside knots at +50° and +53°.** The plan's single straight ramp from
   (+41.8°, −5.59) to (+54°, −1.15) puts the inner-face lower edge at −1.51 at +53°,
   where REQ-03 requires material at z −3.0. Built with knots (+41.8, −5.59),
   (+50, −3.10), (+53, −3.10), (+54, −1.15): the only shape that meets REQ-03
   (material at z −3.0 at +53°) and REQ-04 (no material at z −3.2 at +50°) together
   while keeping A-05's three measured points. A-05 measures the lower edge only;
   the rest of the underside is not observed.
5. **Carrier boss OD 10.30, not 8.00.** J-05 asks for 3.0 of wall around a Ø4.0
   hole, which is 10.0 across; the plan's 8.00 came from D-05a alone. Measured wall
   3.150 mm, material across 10.300 mm.
6. **No mouth chamfer on the carrier insert bores.** A 0.5 × 45° chamfer at the rear
   face shortens the Ø4.0 cylinder to 5.20 mm and fails D-05b's "depth ≥ 5.7 from
   the rear face" as `locate_bore` measures it. Built without it; measured 5.700 mm.
7. **Lug root fillets not achieved** (§5). The underside is a ruled loft trimmed by
   the bore cylinder, which is why the census shows 21 B-spline faces (three lug
   undersides, six ruled patches each, trimmed); the ruled surface sits within about
   0.01 mm of the ideal z = f(θ) surface, and REQ-04 and REQ-05 read it at ±0.3
   brackets.
8. **The STL is meshed at 0.002 mm, not 0.01.** Asked for U-07's 0.01 the mesher's
   own sagitta measures 0.0431 mm, over the row's limit; at 0.002 it measures
   0.00944 mm with 135 974 triangles. The tolerance asked for and the angular
   tolerance both stay inside U-07's limits.
9. **REQ-09's coarse sweep sampling** uses a z step that avoids z = 0.0 exactly: a
   ray at a lug side angle and at the lug top plane runs along two faces at once and
   cannot be read either side, which made the first sweep runs INCONCLUSIVE.
10. The plan's REQ-10 threshold (0.8) and its OD-G04 joint (+4.74°, seat −7.28) are
    superseded by spec 1.1 and the brief; the plan's §7 R1 and R2 are answered by
    the ledger rows the brief quotes, and both now measure clear (§3).

## 9. What I am least sure of

1. **The lug underside between +41.8° and +54°** (deviation 4). REQ-03's "+53°" ray
   and REQ-04's "+50°" ray leave a 0.2 mm window for the inner-face lower edge
   there, and the OEM's own line fit (OD-G09 `RAMP_Z_AT_54`, fitted over +43…+53)
   puts that edge about 1.5 mm higher. The built lug therefore hangs lower at its
   entry than the scan says, which changes the lead-in and the cam that draws the
   portafilter down. If REQ-03 was meant as a layout check that the ramp end may
   miss, the ramp should go back to one straight line and REQ-03's +53° ray should
   move or go.
2. **The two readings in deviations 1 and 2** (the lip ring up to the shelf; the
   pocket inward of the riser). Both rest on measurements of OD-G04 and of the OEM
   cup rather than on the spec's wording, and both shape the cavity around the
   gasket support. If the literal reading was meant, the tabs have nowhere to sit
   and U-03(a) fails by more than 1.5 mm, so this is the Usta's word to say, not
   mine.
3. **Everything that rests on OD-G10's boolean.** Its STEP is not a valid solid by
   `tools.core.validity` (measured), so U-03(a)'s boolean at the locked pose and
   U-03(b)'s sweep are INCONCLUSIVE and will stay so for the reviewer. The distance
   evidence says the fit is right (first contact at rim −11.2515 against the
   ledger's −11.20; path clearances 0.82 → 0.28), but no boolean confirms it.
4. Smaller: D-05b's depth margin is 0.000 by construction (A-17's 5.7 hole in a 5.00
   slab), and U-03(a)'s bead (+0.0237) and pair B (+0.040) margins are thin; all
   three move with A-09, A-12 and A-17.

## 10. Stop

**The gate that cannot be met: D-01a (≥ 0.8), with D-01b and D-06a (≥ 1.0) and the
soft U-06 on the same feature.** Measured `min_wall` **0.130 mm** at
(9.579, −14.201, −24.940) — the web between REQ-13's Ø34.0 counterbore wall
(r 17.000) and REQ-07's Ø3.8 screw hole at r 19.03 (inner edge r 17.130) — and a
second region of **0.200 mm** between the Ø9.0 recess floor (measured z −22.240)
and the counterbore ceiling (measured z −22.440), wherever the two overlap in plan
— a lens of about 13 mm², computed from the two measured circles.

Neither can be lifted inside spec 1.1's own tolerances:

| What is in the way | Best case inside §5 | Needed |
|---|---|---|
| counterbore wall to screw hole | Ø33.9 (REQ-13 − 0.1) with the hole at r 19.13 and Ø3.75 (REQ-07's offset, D-04a): **0.255 mm** | 0.8 |
| recess floor to counterbore ceiling | recess 2.20 deep (REQ-07 − 0.10) and counterbore 2.40 (REQ-13 − 0.10) in a 5.00 slab: **0.400 mm** | 0.8 |

Three options, each built from the same model and measured
(`01_CAD/tradeoff_v01.json`; the files sit in `01_CAD/sweep_v01/`):

| Option | Change | Measured min_wall | D-01a | D-01b | What it costs |
|---|---|---|---|---|---|
| as specified | — | 0.130 mm at the counterbore wall | FAIL | FAIL | — |
| 1 | counterbore Ø32.2 × 1.70 deep | **1.000 mm** at the recess floor | PASS | PASS | REQ-13 (Ø and depth) and REQ-11 change: the web at the Ø26 opening becomes 3.30 mm, not 2.50 |
| 2 | no rear counterbore: Ø26.0 through the 5.00 slab | **1.530 mm** at the keyhole wall | PASS | PASS | REQ-11 and REQ-13 change; the water connection (A-24, envelope unknown) meets a 5.00 mm web instead of 2.50 |
| 3 | slab 6.50 with counterbore Ø32.2 × 2.50 | **0.800 mm** at the insert bore ceiling | PASS | FAIL | U-02 and D-02 change (envelope 29.74 tall), REQ-13's Ø changes, and D-01b still fails |

Every option needs a ratified change to §5 rows, and options 1 and 2 turn on A-24
(the water connection's envelope, still unknown) and A-26 (the OEM screw). Which one
is right is a fact about the machine, not a design choice, so it is not made here.

The rest of the target is built and measured: of the 45 rows in §3, 34 pass, 4 fail
on the one feature above, and 7 are INCONCLUSIVE — four for a `tools/measure`
function that does not exist, one for the OD-T01 bench test, and two because
OD-G10's input STEP is not a sound solid.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-g01-group-head-housing",
 "part": "od_g01_housing",
 "tag": "v01",
 "spec_version": "1.1",
 "files": [
  {
   "path": "01_CAD/build_od_g01_housing.py",
   "sha256": "cebb644b9dc98d1a695acbdd0b3c5c2cd401d8fb2588560ac6c17a1f3aa04883"
  },
  {
   "path": "01_CAD/check_od_g01_housing.py",
   "sha256": "d6e525753b9717b7d69a24330b0358b64d5a0560a9e7371705b0f30be573c6e5"
  },
  {
   "path": "01_CAD/assemble_od_g01_check.py",
   "sha256": "40afd4f319916d553f67233b8e5aa41d8b8ac9d6e3fe2e04b1f8f0de5883544c"
  },
  {
   "path": "01_CAD/sweep_od_g01_v01.py",
   "sha256": "c727c0417f7e7cfe50b51b4aa05a6a54afc88bd00c6553cf00ad7ec22615cedf"
  },
  {
   "path": "01_CAD/sections_od_g01_v01.py",
   "sha256": "fda04c138a9f234aa298c5f77f363545fb7230e83175c10a794f0afeb701f169"
  },
  {
   "path": "01_CAD/tradeoff_od_g01_v01.py",
   "sha256": "eab7cf029b998483a6fbdd9183c89a7b9d0c9c372d3e82d0bd5a2f4c87ba8ec0"
  },
  {
   "path": "01_CAD/probe_inputs_v01.py",
   "sha256": "2dc1a4703f20de85aa6cc52ed7000c976b16a9b723931bdc56e64e7b31f2c2f5"
  },
  {
   "path": "01_CAD/measured_v01.json",
   "sha256": "2e4776fbd06ad231c4e0637e869647e028b03a498d90092209b13f82423ad5e5"
  },
  {
   "path": "01_CAD/sections_v01.json",
   "sha256": "2afbd86153db0d8d84afb4062b0abec2849be68cf98eaa02e5c2a9848947e33b"
  },
  {
   "path": "01_CAD/tradeoff_v01.json",
   "sha256": "d61f87f9b5c20dd487d3b9f7b13dd48c85855d3cf26dfdfff91a6329289d3953"
  },
  {
   "path": "01_CAD/sweep_v01/sweep_v01.json",
   "sha256": "d122308695630b272a755c8b47fd9786a2adcfa01ba54e1b9844ddfb25745cb7"
  },
  {
   "path": "01_CAD/sweep_v01/motion_v01.json",
   "sha256": "62ec1e86484cb940434bb62c0464263d2377d79fabf980b7d9f5cf42fa24fcf7"
  },
  {
   "path": "02_STEP_STL/od_g01_housing_C1_v01.step",
   "sha256": "9b5d10575a0f250df84988b459fa603b941ff812a603c83b1bdd86f6170b96e5"
  },
  {
   "path": "02_STEP_STL/od_g01_assembly_C1_v01.step",
   "sha256": "f6458ce820aaf7639c164e2bc54f25d23e06b09a144b8b92f4f4a8804851369b"
  },
  {
   "path": "02_STEP_STL/od_g01_housing_C1_v01.stl",
   "sha256": "e799b9aeaf84bbb3ccc5c9d9465f8c4e0d37a3bb90848ec33dd4a538b1e87ca3"
  },
  {
   "path": "03_Sections/od_g01_housing_v01_front.png",
   "sha256": "a8c4451a69926ba96f3304ef13b3c6e46aa7e7c40c2fef56816bbadfd0df07e7"
  },
  {
   "path": "03_Sections/od_g01_housing_v01_top.png",
   "sha256": "addfed5d9bd1cbc680567105fe9507cf4c2082c0ced6501795c0513e3a12dfba"
  },
  {
   "path": "03_Sections/od_g01_housing_v01_left.png",
   "sha256": "ed0cf20756146a01f95f940ec8b0c44e86fd8962ee22551a49b683f271492bb6"
  },
  {
   "path": "03_Sections/od_g01_housing_stopblock_v01_front.png",
   "sha256": "0baca9a6f03cf7c15f89885d5877edb518caa34a394a11afdf314d7e5f4df7bb"
  },
  {
   "path": "03_Sections/od_g01_housing_insertboss_v01_front.png",
   "sha256": "c8d9f25cf54f535c1868818b13ad10ae2c9bcd1605e77aac023bd746f904e618"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "7.9.3.1.1 (OCCT 7.9.3)",
  "repo_commit": "3fa319f"
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
   "assumes": []
  },
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
   "gate": "U-02",
   "measured": 100.0000002,
   "unit": "mm",
   "required": "in [99.9, 100.1]",
   "margin": 0.0999998,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 100.0000002,
   "unit": "mm",
   "required": "in [99.9, 100.1]",
   "margin": 0.0999998,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02",
   "measured": 100.0000002,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 119.9999998,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "U-05",
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
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-08",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(0.0000, 0.0000, -22.4400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10",
    "A-11"
   ]
  },
  {
   "gate": "REQ-11",
   "measured": 2.5,
   "unit": "mm",
   "required": "in [2.4, 2.6]",
   "margin": 0.1,
   "at": "(0.0000, 0.0000, -22.4400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-13",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(15.4994, -0.1353, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11",
    "A-24"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-9.3129, 16.5955, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12",
    "A-26"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.8,
   "unit": "mm",
   "required": ">= 3.75",
   "margin": 0.05,
   "at": "(-9.3129, 16.5955, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-26"
   ]
  },
  {
   "gate": "REQ-08",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(44.0000, 44.0000, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-18"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 5.700000000000003,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 2.6645352591003757e-15,
   "at": "(44.0000, 44.0000, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-17"
   ]
  },
  {
   "gate": "J-05",
   "measured": 3.1500000000000004,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.15,
   "at": "(44.0000, 44.0000, -19.5900) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-05a",
   "measured": 10.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 2.3,
   "at": "(44.0000, 44.0000, -19.5900) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-17"
   ]
  },
  {
   "gate": "REQ-01",
   "measured": 31.68,
   "unit": "mm",
   "required": "in [31.58, 31.78]",
   "margin": 0.1,
   "at": "(30.6005, -8.1994, -4.9500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 37.1,
   "unit": "mm",
   "required": "in [37.05, 37.15]",
   "margin": 0.05,
   "at": "(30.0145, 21.8068, -12.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": 43.1,
   "unit": "mm",
   "required": ">= 43.05",
   "margin": 0.05,
   "at": "(43.1000, 0.0000, -18.9500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-21"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 37.1,
   "unit": "mm",
   "required": ">= 37.05",
   "margin": 0.05,
   "at": "(33.6240, -15.6791, -3.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 31.68,
   "unit": "mm",
   "required": "<= 31.78",
   "margin": 0.1,
   "at": "(31.6028, -2.2099, -5.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 31.68,
   "unit": "mm",
   "required": "<= 31.78",
   "margin": 0.1,
   "at": "(29.5560, -11.4047, -9.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "D-01a",
   "measured": 0.12999999999779743,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": -0.67,
   "at": "(9.5790, -14.2014, -24.9400) mm",
   "status": "FAIL",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 0.12999999999779743,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": -0.87,
   "at": "(9.5790, -14.2014, -24.9400) mm",
   "status": "FAIL",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-06a",
   "measured": 0.12999999999779743,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": -0.87,
   "at": "(9.5790, -14.2014, -24.9400) mm",
   "status": "FAIL",
   "assumes": []
  },
  {
   "gate": "U-06",
   "measured": 0.12999999999779743,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": -0.87,
   "at": "(9.5790, -14.2014, -24.9400) mm",
   "status": "FAIL",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 4.147295840084553e-09,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": -4e-09,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 0.08616774972430835,
   "unit": "rad",
   "required": "<= 0.08616774972430835",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03 (a) housing|od_g04",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) g04 flange on the floor",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(13.0586, 6.4522, -19.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) g04 features",
   "measured": 0.5236628659635519,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.023662866,
   "at": "(-27.1722, -16.3267, -15.1700) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) tab1",
   "measured": 0.5799999999999945,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.08,
   "at": "(29.3402, 19.2656, -15.4600) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) tab2",
   "measured": 0.5799999999999915,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.08,
   "at": "(-1.3535, 35.0739, -15.4600) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) tab3",
   "measured": 0.579999999999993,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.08,
   "at": "(-29.6981, -18.7091, -15.4600) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) bead",
   "measured": 0.5236628659635519,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.023662866,
   "at": "(-27.1722, -16.3267, -15.1700) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) pairA1",
   "measured": 1.009999999999689,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.51,
   "at": "(12.5776, 3.2871, -22.4400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) pairA2",
   "measured": 1.009999999998751,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.51,
   "at": "(-12.4872, 3.6152, -22.4400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) pairB1",
   "measured": 0.5399999999999956,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.04,
   "at": "(-10.2981, 18.3360, -22.2400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) pairB2",
   "measured": 0.5399999999999956,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.04,
   "at": "(11.7690, -17.4285, -22.2400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) hub",
   "measured": 2.969999999991279,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 2.47,
   "at": "(-12.4872, 3.6152, -21.7250) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) housing|od_g10 locked",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) ear tops on the lug undersides",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(35.2699, -7.0355, -6.3997) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "REQ-10",
   "measured": 0.5166134919014554,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.216613492,
   "at": "(-3.3115, 31.5065, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-19"
   ]
  },
  {
   "gate": "D-07",
   "measured": 2.969999999991279,
   "unit": "mm",
   "required": ">= 2.9",
   "margin": 0.07,
   "at": "(-12.4872, 3.6152, -21.7250) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "D-03a",
   "measured": null,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "D-03b",
   "measured": null,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "E-06",
   "measured": null,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "REQ-12",
   "measured": null,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "D-05a boss OD",
   "measured": null,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": []
  },
  {
   "gate": "U-03 (b) lock path",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": "two-leg path, 8 + 13 poses (01_CAD/sweep_v01/motion_v01.json)",
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-14",
    "A-19"
   ]
  }
 ],
 "sweep": [
  {
   "parameter": "bore_r",
   "values": [
    37.05,
    37.15
   ],
   "all_built": true,
   "worst_gate": "REQ-02",
   "worst_margin": 0.0
  },
  {
   "parameter": "lug_inner_r",
   "values": [
    31.58,
    31.78
   ],
   "all_built": true,
   "worst_gate": "REQ-01",
   "worst_margin": -3.552713678800501e-15
  },
  {
   "parameter": "lug_span",
   "values": [
    53.75,
    54.25
   ],
   "all_built": true,
   "worst_gate": "U-03 (a) housing|od_g04",
   "worst_margin": 0.0
  },
  {
   "parameter": "lug_starts",
   "values": [
    [
     335.75,
     95.75,
     215.75
    ],
    [
     336.25,
     96.25,
     216.25
    ]
   ],
   "all_built": true,
   "worst_gate": "REQ-03",
   "worst_margin": -5.32
  },
  {
   "parameter": "stop_end_off",
   "values": [
    5.26,
    6.26
   ],
   "all_built": true,
   "worst_gate": "U-03 (a) housing|od_g04",
   "worst_margin": 0.0
  },
  {
   "parameter": "stop_bottom_z",
   "values": [
    -10.82,
    -10.22
   ],
   "all_built": true,
   "worst_gate": "U-03 (a) housing|od_g04",
   "worst_margin": 0.0
  },
  {
   "parameter": "shelf_z",
   "values": [
    -14.2,
    -14.0
   ],
   "all_built": true,
   "worst_gate": "U-03 (a) housing|od_g04",
   "worst_margin": 0.0
  },
  {
   "parameter": "pocket_floor_z",
   "values": [
    -17.4,
    -17.2
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "pocket_riser_r",
   "values": [
    34.95,
    35.25
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "pocket_start_off",
   "values": [
    -5.5,
    -4.5
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "pocket_end_off",
   "values": [
    58.0,
    59.0
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "lip_upper_r",
   "values": [
    31.65,
    31.78
   ],
   "all_built": true,
   "worst_gate": "U-05",
   "worst_margin": -3.0
  },
  {
   "parameter": "lip_lower_r",
   "values": [
    31.25,
    31.35
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "plate_t",
   "values": [
    4.9,
    5.1
   ],
   "all_built": true,
   "worst_gate": "U-02",
   "worst_margin": -2e-07
  },
  {
   "parameter": "keyhole_d",
   "values": [
    25.95,
    26.05
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "pair_b_r",
   "values": [
    18.98,
    19.08
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "carrier_xy",
   "values": [
    43.95,
    44.05
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "insert_d",
   "values": [
    3.98,
    4.02
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "insert_depth",
   "values": [
    5.7,
    6.0
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "under_knots",
   "values": [
    [
     [
      5.76,
      -6.905
     ],
     [
      7.0,
      -6.87
     ],
     [
      41.8,
      -5.89
     ],
     [
      50.0,
      -3.4
     ],
     [
      53.0,
      -3.4
     ],
     [
      54.0,
      -1.45
     ],
     [
      56.0,
      -0.72
     ]
    ],
    [
     [
      5.76,
      -6.305000000000001
     ],
     [
      7.0,
      -6.2700000000000005
     ],
     [
      41.8,
      -5.29
     ],
     [
      50.0,
      -2.8000000000000003
     ],
     [
      53.0,
      -2.8000000000000003
     ],
     [
      54.0,
      -0.8499999999999999
     ],
     [
      56.0,
      -0.12
     ]
    ]
   ],
   "all_built": true,
   "worst_gate": "REQ-03",
   "worst_margin": -5.32
  }
 ],
 "least_sure": [
  "The lug underside between +41.8 and +54 degrees: REQ-03's +53 ray and REQ-04's +50 ray leave a 0.2 mm window for the inner-face lower edge, the OEM's own fit puts that edge about 1.5 mm higher, and the sweep fails REQ-03 at a lug-start shift of 0.25 degrees and REQ-04 at an underside shift of 0.3 mm.",
  "Two readings of spec 1.1 that the measurements forced: the lip ring's R 31.70 wall run up to the shelf at z -14.10, and the tab pocket built inward of the R 35.10 riser.",
  "Everything resting on OD-G10's boolean: its input STEP reads brep_valid = 0, so U-03(a)'s boolean at the locked pose and U-03(b)'s sweep are INCONCLUSIVE for the reviewer too; the distance evidence (first contact at rim -11.2515 against the ledger's -11.20) is all there is."
 ],
 "stopped": true
}
```
