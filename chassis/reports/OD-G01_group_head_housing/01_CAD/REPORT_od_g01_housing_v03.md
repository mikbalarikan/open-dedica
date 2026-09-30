# REPORT — od_g01_housing v03 (20260930-od-g01-group-head-housing)

Designer: Claude Code, Opus 5 · spec version 1.3 · plan `01_CAD/DESIGN_PLAN.md` with the WP-03, WP-05 and WP-06 amendments · 2026-09-30 UTC

**Outcome: SUBMITTED.** The geometry is v02's, unchanged and re-exported: the
`Params` structure and the `build()` function of `01_CAD/build_od_g01_housing_v03.py`
are byte for byte those of `01_CAD/build_od_g01_housing_v02.py` (SHA-256
`68209698cc98d041d3ba5b9450646086130964f21cfce1814f0c7fc46efb3fb5`), and the STEP
this round writes differs from v02's in one line of the file header only (§5). What
changed is the measurement: spec 1.3 §5 U-03(a) makes the locked pose of OD-G10 the
**measured** first contact of the ear tops with the lug undersides along +Z, and
probes 0.20 mm along **−Z** from it. Measured on the re-imported v03 STEP:

- the locked rim z is **−11.251029 mm**, inside A-14's expected −11.20 ± 0.10 by
  0.048971 mm;
- the designed contact there reads **0.0000000 mm** (1.99e−15);
- the 0.20 mm probe along −Z reads **0.1997125 mm**, inside §5's [0.19, 0.21] by
  0.009712 mm.

Every §5 row that a tool can answer now passes. Six rows stay INCONCLUSIVE and none
of them is new: four for a `tools/measure` function that does not exist (D-03a,
D-03b, E-06, the boss-OD half of D-05a), one for the OD-T01 bench test (REQ-12), and
the OD-G10 boolean, which spec §5 itself answers by distance because that input is
not a sound solid (A-28). No fix cycle was needed. A self-check clears nothing: the
reviewer's own measurement does.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_g01_housing_v03.py` | 47c9d449bda0330e987f7e147b019118146ae789e59b39461d9f3fe1e3132896 | parametric script; `Params` and `build()` byte-identical to v02's (§8) |
| `01_CAD/check_od_g01_housing_v03.py` | 8cb806508af12af3da089562ab6bef779ac8334a5b977773102190f6f0050617 | checks, written before the build was run (D3); spec 1.3's U-03(a) rows |
| `01_CAD/assemble_od_g01_check_v03.py` | 7fad3c08c8b31007bf90431b6487ba64aed20c260414f1d818e66ee06430a505 | the spec §5 joints, the measured locked pose, the lug and OD-G04 feature pieces, the three-leg lock path |
| `01_CAD/sections_od_g01_v03.py` | 9808c27f8779fdc41a57620ca8d79220b15af52717af26f36199236ee0de3918 | D6 sections |
| `01_CAD/probe_placed_v03.py` | 9524359825a0aeed72f2cc9ea4a40a4208bc1464ca8d642bb9014caa4c28815b | diagnostic: the mating parts measured where the joints put them |
| `01_CAD/probe_oem_contact_v03.py` | f3448bba50b72416bc878d54f4f8d4f9b69edfb805f8606357e29dba80fd87be | diagnostic: spec 1.3's own U-03(a) rows applied to the OEM pair OD-G09 \| OD-G10 |
| `01_CAD/probe_sweep_contact_v03.py` | 4d194d904dc97cc5af57ffdaff82a5fc4f7e3dec64edc8a9be1fa4cd127f343d | diagnostic: spec 1.3's U-03(a) rows re-measured on the v02 sweep solids (§4) |
| `01_CAD/measured_v03.json` | b647e9fd9d18ccc70237e0f6e30278e9645db344408ea9cad417a12f8d345540 | every gate row with its measurement and detail |
| `01_CAD/sections_v03.json` | 0792e6d763592583b762f5a2762a4809111c98876754c6c2de6e956e6ac38991 | the sections with `nothing_clipped` |
| `01_CAD/probe_placed_v03.json` | b3ac0b9a988849c5700bd8cf670df7d635d46a343f12beda270c6535d54357ec | §5's placement measurements |
| `01_CAD/probe_oem_contact_v03.json` | 2ce30fe3420fb5a327ed5946ff4dd53732c6c3e80167538237d9f804c593f8b3 | §3's OEM comparison, measured |
| `01_CAD/probe_sweep_contact_v03.json` | b6e34805b3d6f39094e9ff673ce4cbcb639ee3001c109c4680ff7033014d4f37 | §4's U-03(a) sweep readings, measured |
| `02_STEP_STL/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | AP242 (`tools.core.write_step`), re-imported for every measurement |
| `02_STEP_STL/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | check assembly: housing + OD-G04 seated + OD-G10 at the measured locked pose (rim z −11.251029) |
| `02_STEP_STL/od_g01_housing_C1_v03.stl` | 0e8fe8e265284ca76cff363dbbd2ab6df5c8485d8e4e8610f58ad29295f38cec | triangulation cleared first; tolerance 0.002 mm, angular 0.08616775 rad, 135 024 triangles, measured sagitta 0.0094356 mm. Byte-identical to the v02 STL |
| `03_Sections/od_g01_housing_v03_front.png` | 440317bad3e524ec54b9dab46a13aabb1ff480cd8bc50d39768596cea1232fb1 | section y = 0 (lug 1 at +24°, the gap at 180°), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_v03_top.png` | 9c37e36c00ede2a0b82f02c086a4e4a3f41111a2e271569079514f7a754a81c2 | section z = −15.94 (pockets, lip ring, keyhole and its two lobes, pair-B recesses, carrier bosses), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_v03_left.png` | b1a5f5ca4e8ea8891288192d75d01f3fad3bc93fdb140a10b777cb3935b2627a | section x = 0, `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_stopblock_v03_front.png` | f101901d79a301a8fb48524e44a207f7ec1661c93dd410bd6f32e0502aeb7a95 | section through a stop block (lug 1 + 2.9°), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_lugunderside_v03_front.png` | 46f4ccc995a5ca0143b7d2faef5f1287687440e53cc411a90702c9722aad7d06 | section through REQ-04's shallow-plane ray (lug 1 + 20°), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_insertboss_v03_front.png` | 2a6022aaa1f071911d3a9b21fcbc1a3d629bdd507e975801444a4cbe32ddcdba | section through two carrier insert bosses, `nothing_clipped` 0 |

Cited, not written this round (§4 and §8): `01_CAD/build_od_g01_housing_v02.py`
`68209698cc98d041d3ba5b9450646086130964f21cfce1814f0c7fc46efb3fb5`,
`01_CAD/sweep_od_g01_v02.py`
`47d725aa0f2f540b4a0f8eea3400820fdb99d8eedbac376d1bdc12eeacb1db07`,
`01_CAD/sweep_v02/sweep_v02.json`
`b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3`, and the 40 sweep
STEPs beside it.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 (pinned, D-023) · OCP 7.9.3.1.1 (OCCT 7.9.3) ·
numpy 2.5.3 · repo commit `18c4ddc`. Input hashes checked against the brief before
any other work: all three match (`OD-G09`
2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906, `OD-G04`
19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2, `OD-G10`
3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257).

## 3. Gate self-check

Every value is measured by `check_od_g01_housing_v03.py` on the B-rep of the
re-imported `02_STEP_STL/od_g01_housing_C1_v03.step`; limits are spec 1.3 §5's, bands
are GATES §0's (0.005 mm, 0.001 deg, 0.001 mm³, 0.00002 rad, 0 for counts and 1/0
facts). Where a gate has several rays or sub-rows, the row below is the worst of them
and `01_CAD/measured_v03.json` holds them all. The table carries 49 rows; the JSON
block at the end carries the full 54 the check script emits, which differ only in
that the table shows OD-G04's three tabs, its two pair-A bosses and its two pair-B
bosses as one row each and leaves out the OD-G04 feature summary row.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | size 100.0000002 × 100.0000002 × 28.2400002 mm | each in [spec ± 0.1] | +0.0999998 | — | PASS | — |
| U-03 | worst of all its rows below; every row that a tool can answer passes | see the rows below | −0.0000000 (1.99e−15, the designed contact) | (30.8756, −7.0938, −6.4508) | PASS (assumed: A-13, A-14, A-19) | A-13, A-14, A-19 |
| U-03 (a) housing\|OD-G04 | 0.000 mm³ | ≤ 0 mm³ | 0.000 | — | PASS (assumed: A-13) | A-13 |
| U-03 (a) designed contact, OD-G04 flange on the floor | 0.0000000 mm | = 0 | 0.000 | (13.0586, 6.4522, −19.9400) | PASS (assumed: A-13) | A-13 |
| U-03 (a) OD-G04 tabs | 0.5800000 mm (tab 1; tabs 2 and 3 the same to 1e−14) | ≥ 0.5 | +0.080 | (29.3402, 19.2656, −15.4600) | PASS (assumed: A-12, A-13) | A-12, A-13 |
| U-03 (a) OD-G04 bead | 0.5236629 mm | ≥ 0.5 | +0.023663 | (−27.1722, −16.3267, −15.1700) | PASS (assumed: A-09, A-13) | A-09, A-13 |
| U-03 (a) OD-G04 pair A | 1.0100000 mm | ≥ 0.5 | +0.510 | (19.9992, −0.1745, −19.9500) | PASS (assumed: A-11, A-12) | A-11, A-12 |
| U-03 (a) OD-G04 pair B | 0.5400000 mm | ≥ 0.5 | +0.040 | (−10.2981, 18.3360, −22.2400) | PASS (assumed: A-12) | A-12 |
| U-03 (a) OD-G04 hub | 2.9700000 mm | ≥ 0.5 | +2.470 | (12.5183, −3.5061, −19.9500) | PASS (assumed: A-24) | A-24 |
| U-03 (a) locked rim z, the measured first contact along +Z at the locked clock | **−11.251029 mm** | A-14 expects −11.20 ± 0.10 | +0.048971 | clock 60.26°, bisection over 24 steps | PASS (assumed: A-14) | A-14 |
| U-03 (a) designed contact, ear tops on the lug undersides at that pose | **0.0000000 mm** (1.99e−15) | = 0 | −0.0000000 | (30.8756, −7.0938, −6.4508) | PASS (assumed: A-14) | A-14 |
| U-03 (a) OD-G10 displaced 0.20 along **−Z** from that pose | **0.1997125 mm** | in [0.19, 0.21] | +0.009712 | (30.8731, −7.1046, −6.4513) | PASS (assumed: A-14, A-19) | A-14, A-19 |
| U-03 (a) housing\|OD-G10 boolean | INCONCLUSIVE: `common_volume` refuses the pair, the OD-G10 input reads `brep_valid` 0 | ≤ 0 mm³ | — | — | INCONCLUSIVE (A-28) | A-28 |
| U-03 (b) lock path, 43 poses | 0.4945157 mm worst of the 36 poses outside the last 0.5 mm of approach; 0.0000000 mm worst of the 7 inside it | ≥ 0.30 outside, ≥ 0 inside | +0.194516 / +0.0000000 | (−3.3115, 31.5065, 0.0000) | PASS (assumed: A-14, A-19) | A-14, A-19 |
| U-04 | schema 1, solids 1, labels 1, faces_delta 0, volume_delta 3.6e−09 mm³, valid_after 1 | as stated | −4e−09 mm³ | — | PASS | — |
| U-05 | 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 2 Ø9 pass-through + 2 Ø9 recesses, 2 Ø3.8 through-holes, 4 Ø4.0 insert bores | = the spec's counts | 0 | — | PASS | — |
| U-06 (Soft) | min_wall wide (45° opposition) 1.1500000 mm | ≥ 1.0 | +0.150 | (32.1295, 18.5500, 0.0000) | PASS | — |
| U-07 | sagitta 0.0094356 mm at tolerance 0.002 mm, angular 0.08616775 rad, 135 024 triangles | sagitta ≤ 0.01, tol ≤ 0.01, a ≤ 0.08616775 | +0.00056 (sagitta), 0.000 (angular) | — | PASS | — |
| U-08 | faces the census cannot name: 0; every insert bore a plain cylinder Ø4.000 | = 0 (N/A by its row: no thread) | 0 | — | PASS | — |
| D-01a | min_wall 1.5300000 mm, the web between the Ø26 opening and a pair-B Ø9 recess | ≥ 0.8 | +0.730 | (7.2695, −10.7775, −19.9400) | PASS | — |
| D-01b | min_wall 1.5300000 mm | ≥ 1.0 | +0.530 | same | PASS (assumed: A-05) | A-05 |
| D-02 | 100.0000002 × 100.0000002 × 28.2400002 mm | ≤ 220 × 220 × 250 | +119.9999998 | — | PASS (assumed: A-16) | A-16 |
| D-03a | no overhang measurement in `tools/measure` (GATES: reviewer, from sections) | ≥ 45° or supported by A-22 | — | sections, §6 | INCONCLUSIVE | A-22 |
| D-03b | no bridge measurement in `tools/measure` (GATES: reviewer, from sections) | span ≤ 5 | — | sections, §6 | INCONCLUSIVE | — |
| D-04a | Ø3.8000000 mm, both pair-B screw holes | ≥ 3.75 | +0.050 | (−9.3129, 16.5955, −24.9400) | PASS (assumed: A-26) | A-26 |
| D-05a | material across each Ø4.0 insert axis 10.3000000 mm, worst of 288 rays | ≥ 8.0 | +2.300 | (44.0000, 44.0000, −19.5900) | PASS (assumed: A-17) | A-17 |
| D-05a boss OD | no boss-OD measurement in `tools/measure` (GATES: reviewer) | OD ≥ 8.0 | — | — | INCONCLUSIVE | A-17 |
| D-05b | Ø4.0000000 mm, length 5.7000000 mm from the rear face, all four | Ø in [3.95, 4.05], depth ≥ 5.7 | +2.7e−15 (depth) | (44.0000, 44.0000, −24.9400) | PASS (assumed: A-17) | A-17 |
| D-06a | min_wall 1.5300000 mm | ≥ 1.0 | +0.530 | (7.2695, −10.7775, −19.9400) | PASS | — |
| D-07 | N/A by its row (no reamed fit bore); the Ø26 opening to the OD-G04 hub as placed measures 2.9700000 mm | ≥ 2.9 radial clearance | +0.070 | (12.5183, −3.5061, −19.9500) | PASS (assumed: A-24) | A-24 |
| J-05 | wall around each insert axis 3.1500000 mm, worst of 288 rays | ≥ 3.0 | +0.150 | (44.0000, 44.0000, −19.5900) | PASS | — |
| E-06 | no boss-root measurement in `tools/measure` (GATES: reviewer); the root fillet achieved is R 0.6 on all four bosses (§5) | a root fillet on every boss | — | sections, §6 | INCONCLUSIVE | — |
| REQ-01 | inner radius over start + 8°…40°, z −5.0…−1.0: min 31.680, max 31.680 mm (99 angles × 40 levels) | in [31.58, 31.78] | +0.100 | (30.6005, −8.1994, −4.9500) | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner radius in the gaps, z −13.0…+2.0: min 37.100, max 37.100 mm (84 angles × 75 levels) | in [37.05, 37.15] | +0.050 | (30.0145, 21.8068, −12.9000) | PASS (assumed: A-03) | A-03 |
| REQ-03 | z −3.0: 31.680 at start + 1°, + 27°, + 40°; 37.100 at start − 1° and + 55°, all three lugs (15 rays) | ≤ 31.78 / ≥ 37.05 | +0.050 | (33.6240, −15.6791, −3.0000) | PASS (assumed: A-04) | A-04 |
| REQ-04 | start + 20°: 31.680 at z −5.7, 37.100 at z −6.7; start + 47°: 31.680 at z −3.2, 37.100 at z −4.2 (12 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (31.6028, −2.2099, −5.7000) | PASS (assumed: A-05) | A-05 |
| REQ-05 | start + 2.9°: 31.680 at z −9.0, 37.100 at z −11.0 (6 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (29.5560, −11.4047, −9.0000) | PASS (assumed: A-06) | A-06 |
| REQ-06 | Ø26.000 mm, axis offset 0.000 mm, through = 1 | Ø 26.0 ± 0.1, on the axis, through | +0.100 | (0.0000, 0.0000, −24.9400) | PASS (assumed: A-10, A-11) | A-10, A-11 |
| REQ-07 | two Ø3.800 through-holes at r 19.03, θ 119.3° / 304.0°, offset 2.6e−07; recesses Ø9.000 × 2.300 deep from the floor | offset ≤ 0.10, Ø9.0 ± 0.1, 2.30 ± 0.10 | +0.100 (offset) | (−9.3129, 16.5955, −24.9400) | PASS (assumed: A-12, A-26) | A-12, A-26 |
| REQ-08 | four Ø4.000 bores at (±44, ±44), offset 0.000 mm | offset ≤ 0.10 | +0.100 | (44.0000, 44.0000, −24.9400) | PASS (assumed: A-18) | A-18 |
| REQ-09 | outer radius 43.100 mm at every 5° over z −19.0…+3.0 (72 × 220 rays); inner max 37.100 in the gaps; wall 6.000 mm | ≥ 43.05 / ≤ 37.15 / ≥ 5.9 | +0.050 | (43.1000, 0.0000, −18.9500) | PASS (assumed: A-21) | A-21 |
| REQ-10 | 23 poses, rim z −5.000 → −11.701 at the insertion clock: 0.8239 → 0.4945 mm | ≥ 0.30 at every pose | +0.194516 | (−3.3115, 31.5065, 0.0000) | PASS (assumed: A-19) | A-19 |
| REQ-11 | Ø26 bore length 5.000 mm | 5.00 ± 0.10 | +0.100 | (0.0000, 0.0000, −24.9400) | PASS (assumed: A-10) | A-10 |
| REQ-12 | not a geometric gate: the OD-T01 bench test answers it (spec §5, §7) | 15 bar on a Ø51 basket (3.06 kN) | — | — | INCONCLUSIVE | A-21 |
| REQ-13 | two Ø9.000 through-holes at r 15.500, θ 359.5° / 179.0°, offset 4.1e−07, through = 1 | Ø9.0 ± 0.1, offset ≤ 0.10 | +0.100 | (15.4994, −0.1353, −24.9400) | PASS (assumed: A-11) | A-11 |
| exactly_one_solid | 1 | = 1 | 0 | — | PASS | — |
| feature_census | planes 40, cylinders 30 (23 concave, 9 convex), tori 7, B-splines 15, other 0, bores 15; every counted feature at the spec's count | = the spec's counts | 0 | — | PASS | — |
| envelope_within_spec | size 100.0000002 × 100.0000002 × 28.2400002 mm; position min (−50.0000001, −50.0000001, −24.9400001), max (50.0000001, 50.0000001, 3.3000001) | size in [spec ± 0.1]; position apart | +0.0999998 | — | PASS | — |

**The census, item by item** (U-05, `bore_census` and `locate_bore` on the
re-imported STEP): Ø26.0 × 5.00 through ×1 on the axis; Ø9.0 × 5.00 through ×2
(pair-A pass-throughs at (15.4994, −0.1353) and (−15.4976, 0.2705), each merged with
the Ø26 opening into one keyhole lobe); Ø9.0 × 2.30 blind ×2 (pair-B recesses from
the floor at (−9.3129, 16.5955) and (10.6414, −15.7766)); Ø3.8 × 2.70 through ×2
(pair-B screw holes on the same two axes); Ø4.0 × 5.70 through ×4 at (±44, ±44).
Lugs, stop blocks and pockets are counted from the material each puts on a located
ray: 31.68 at start + 27° and z −3.0 for the three lugs, 31.68 at z −9.0 with 37.10
at z −11.0 at start + 2.9° for the three stop blocks, 35.10 at z −16.0 with 31.70 at
z −17.6 at start + 26.75° for the three pockets.

**The three ear tops at the measured locked pose, lug by lug** (a located
diagnostic, not a gate; the housing cut into its three lug sectors). Spec §5 U-03(a)
names one designed-contact pair, "the three ear tops on the lug undersides", and
gates it at `clearance = 0`; that pair row is the gated one above and reads
0.0000000 mm. Measured lug by lug at rim z −11.251029: **lug 1 0.0000000**, **lug 2
0.0903189**, **lug 3 0.0210511** mm. The three cannot all be 0 at one pose: A-25 puts
OD-G10's ears at 120.5 / 120.5 / 119° while §4 C1 puts the housing's lugs at a
symmetric 120° pitch, so two ears stand off by the pitch error while the third makes
first contact. This is the same fact v02 reported, read now at the true contact pose
instead of at a fixed −11.20 where two lugs were already touching; §9 carries it.

**The same rows on the OEM pair** (`01_CAD/probe_oem_contact_v03.json`, a diagnostic:
spec 1.3's own definition applied to OD-G09 | OD-G10 at the same locked clock). The
OEM cup first contacts at rim z **−11.261751**, 0.061751 mm below A-14's −11.20 and
0.010723 mm below this housing's own contact, and its 0.20 mm probe along −Z reads
**0.1997295 mm**. The housing and the cup it reproduces therefore read the same row
to 1.7e−05 mm, which is the strongest evidence in this REPORT that the geometry is
faithful and that spec 1.3's wording describes the real pair. (For comparison, the
spec 1.2 readings at the fixed −11.20: OEM 0.0000 at +0.20 and 0.1381 at −0.20.)

**The lock path (U-03(b), L-09, L-10)**, 43 poses in three legs, each pose carrying
the travel it still has to make:

| Leg | Poses | Swept | Clearance |
|---|---|---|---|
| insertion, at the insertion clock 122.5° (ears centred in the gaps) | 23 | rim z −5.000 → −11.701 | 0.8239 → 0.4945 mm, falling monotonically; the nearest point is the portafilter's drafted outer wall against the lug 2 start corner at r 31.68, z 0.000 |
| rotation, at rim z −11.701 | 14 | clock 122.5° → 60.26° | 0.5060 → 0.2765 mm at the stop (the same wall against the lug inner faces, then the ear leading edge against the stop block) |
| seating, at the locked clock | 6 | rim z −11.701 → −11.251 | 0.2765 → 0.0000000 mm, the ear tops onto the lug undersides |

Seven of the 43 poses lie inside the 0.5 mm of approach that spec §5 U-03(b) exempts
(the last rotation pose, 0.45 mm of travel from the final pose, and the six seating
poses); the worst of those is 0.0000000 mm against the required ≥ 0. The worst of the
other 36 is 0.4945157 mm against the required ≥ 0.30. The rotation depth (0.45 mm
below the measured locked pose) is a derivation, recorded in §8.

## 4. Robustness sweep (D7)

**The 40-run sweep of round 2 stands and is cited, not re-run**, as WP-06 directs:
the build script is unchanged (§8 item 1 and the byte comparison in §5), so the 40
sweep solids in `01_CAD/sweep_v02/` are exactly the solids a v03 sweep would build.
The sweep driver is `01_CAD/sweep_od_g01_v02.py`
(`47d725aa0f2f540b4a0f8eea3400820fdb99d8eedbac376d1bdc12eeacb1db07`) and its results
are `01_CAD/sweep_v02/sweep_v02.json`
(`b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3`). From it: **all
40 runs built exactly one valid solid, and every geometric row passed in every run**,
low and high, for the 20 fit-critical parameters below.

| Parameter | Low · nominal · high | All built, one solid | Worst geometric row of the two runs | Worst margin |
|---|---|---|---|---|
| `bore_r` | 37.05 · 37.10 · 37.15 | yes | REQ-02 PASS_ASSUMED 37.0500 mm in `bore_r_lo` | +0.0000 |
| `lug_inner_r` | 31.58 · 31.68 · 31.78 | yes | REQ-01 PASS_ASSUMED 31.5800 mm in `lug_inner_r_lo` | −0.0000 (on the band edge, inside GATES §0's 0.005) |
| `lug_span` | 53.75 · 54.00 · 54.25 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `lug_starts` | −0.25° · 0 · +0.25° on all three starts | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `stop_end_off` | 5.26 · 5.76 · 6.26 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `stop_bottom_z` | −10.82 · −10.52 · −10.22 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `shelf_z` | −14.20 · −14.10 · −14.00 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `pocket_floor_z` | −17.40 · −17.30 · −17.20 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `pocket_riser_r` | 34.95 · 35.10 · 35.25 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `pocket_start_off` | −5.5 · −5.0 · −4.5 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `pocket_end_off` | 58.0 · 58.5 · 59.0 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `lip_upper_r` | 31.65 · 31.70 · 31.75 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `lip_lower_r` | 31.25 · 31.30 · 31.35 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `plate_t` | 4.90 · 5.00 · 5.10 | yes | U-02 PASS `size_z` 28.3400 mm in `plate_t_hi` | −0.0000 (on the band edge) |
| `keyhole_d` | 25.95 · 26.00 · 26.05 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `pair_b_r` | 18.98 · 19.03 · 19.08 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `carrier_xy` | 43.95 · 44.00 · 44.05 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `insert_d` | 3.98 · 4.00 · 4.02 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `insert_depth` | 5.70 · 5.70 · 6.00 | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |
| `under_knots` (the lug underside) | every knot −0.3 · 0 · +0.3 (A-05's own bracket) | yes | D-05b PASS_ASSUMED 5.7000 mm | +0.0000 |

**What does not carry over, and what was re-measured.** The sweep's two U-03(a)
probe rows were measured under spec 1.2's definition — a fixed locked pose at −11.20
and a displacement the 1.2 wording put along +Z — so they are superseded by spec 1.3
and are not quoted here. Rather than re-run 40 builds, spec 1.3's U-03(a) rows were
re-measured directly **on the sweep STEPs that already exist**, by
`01_CAD/probe_sweep_contact_v03.py` → `01_CAD/probe_sweep_contact_v03.json`: 12
cases, the six sweep parameters that can reach the ear-top contact or the stop block
(`lug_inner_r`, `lug_starts`, `lug_span`, `stop_end_off`, `stop_bottom_z`,
`under_knots`), low and high. Each case is a fresh bisection for the locked pose and
a fresh probe 0.20 mm along −Z from it.

| Case | Locked rim z, measured | Inside A-14 ±0.10 | Probe along −Z | In [0.19, 0.21] |
|---|---|---|---|---|
| `lug_inner_r_lo` (31.58) | −11.252304 | yes | 0.1997103 | yes |
| `lug_inner_r_hi` (31.78) | −11.249762 | yes | 0.1997146 | yes |
| `lug_starts_lo` (−0.25°) | −11.243830 | yes | 0.1997138 | yes |
| `lug_starts_hi` (+0.25°) | −11.258242 | yes | **0.1382296** | **no** |
| `lug_span_lo` / `_hi` | −11.251029 (both) | yes | 0.1997125 (both) | yes |
| `stop_end_off_lo` / `_hi` | −11.251029 (both) | yes | 0.1997125 (both) | yes |
| `stop_bottom_z_lo` / `_hi` | −11.251029 (both) | yes | 0.1997125 (both) | yes |
| `under_knots_lo` (−0.3) | **−11.551029** | **no** (−0.351 from A-14) | 0.1997125 | yes |
| `under_knots_hi` (+0.3) | **−10.951029** | **no** (+0.249 from A-14) | 0.1997126 | yes |

**What the sweep and the re-measurement found.**

- **The geometry is robust over every band.** No REQ row and no process row leaves
  its limit anywhere in the 40 runs. The two −0.0000 margins are values modelled
  exactly at a limit — `lug_inner_r` at REQ-01's low end and `plate_t` at U-02's
  `size_z` limit — and they pass inside GATES §0's 0.005 mm band; anything past those
  bands fails them. D-05b's +0.0000 is the same thing by construction: A-17's 5.70 mm
  insert hole in a 5.00 mm slab plus a 0.70 mm boss has no depth to spare, and no
  swept parameter changes it.
- **Spec 1.3's probe holds in 11 of the 12 re-measured cases**, at 0.19971 ± 0.00001
  mm, because the probe is now referred to the pose it is measured from: the ear-top
  contact opens by 0.20 × cos(the underside tilt), whatever height the contact sits
  at. That is why `under_knots` ±0.3 — the one lever that moves the contact by
  0.3 mm — still reads 0.19971.
- **The one case out of band is `lug_starts_hi`, and the nearest point moves to
  another pair.** At +0.25° on all three lug starts the probe reads 0.1382296 mm at
  (−6.5921, 30.9866, **−10.52**) — the stop-block bottom level, not a lug underside.
  The ear leading edge sits 0.5° short of the stop at the locked clock (A-14); moving
  the lug start +0.25° closes that gap to 0.25°, which at r 31.68 is
  0.25° × π/180 × 31.68 = 0.13823 mm, the measured value to five decimals. Nothing
  overlaps there (the reading is a positive distance and the contact row still reads
  0), and the delivered part at nominal reads 0.1997125; but the row is sensitive to
  a quarter-degree of lug clocking through the ear-to-stop gap, not through the
  contact. §9 carries it.
- **A-14's ±0.10 band on the locked rim z is the binding row, not the probe.**
  A-05's own ±0.3 bracket on the underside moves the measured contact to −11.551 and
  −10.951, both outside A-14's [−11.30, −11.10]; at nominal the measurement is
  −11.251029, inside by 0.048971 mm. So the underside level, which A-05 gives as a
  scan measurement, has about ±0.05 mm of room against A-14 before the locked-rim-z
  row fails.
- **The lock path stays clear in every run that walks it.** No sweep case puts a pose
  under 0.30 mm outside the 0.5 mm of approach spec §5 U-03(b) exempts.

## 5. Build facts

- **The geometry is v02's, re-exported.** `Params` and `build()` in
  `01_CAD/build_od_g01_housing_v03.py` hash identically to the same block of
  `01_CAD/build_od_g01_housing_v02.py`
  (`68209698cc98d041d3ba5b9450646086130964f21cfce1814f0c7fc46efb3fb5`); the file
  differs only in its docstring, `VERSION = 3` and the two lines of `main()` listed
  in §8 item 1. The exported STEP `55478e0b…332f37399` differs from the v02 STEP
  `f8865cd1…0cd4407b02` in **one line**, line 4 of the file header:
  `FILE_NAME('od_g01_housing_C1_v02.step', …)` against
  `FILE_NAME('od_g01_housing_C1_v03.step', …)`. Both files are 437 578 bytes and
  every other byte is the same, so the brief's expectation of an identical hash holds
  for the geometry but not for the whole file: the AP242 writer puts the output file
  name in the header, and the output name is what this round changes. The STL is
  byte-identical, hash and all (`0e8fe8e2…9295f38cec`). The check assembly STEP is a
  new file because OD-G10 moved 0.051029 mm to the measured locked pose.
- Envelope 100.0000002 × 100.0000002 × 28.2400002 mm, from min (−50.0000001,
  −50.0000001, −24.9400001) to max (50.0000001, 50.0000001, 3.3000001); volume
  90 216.792 mm³; mass 96.532 g at 1070 kg/m³ (A-15, reported, not gated); centre of
  mass (−0.0026, −0.0020, −15.9444) mm.
- Fillets, requested → achieved: four carrier boss roots **R 1.0 → R 0.6** (R 1.0 and
  R 0.8 each raised ValueError; the boss stands only 0.70 above the floor); the
  shelf-to-bore concave circle **R 0.8 → R 0.8** (first rung); the seven lug root
  edges **R 0.6, 0.5, 0.4, 0.3 → none achieved**, those edges stay sharp (OCCT refuses
  every rung where a lug side face meets the bore wall beside the lofted underside).
  No §5 row reads those edges. A failed rung edits the shape it is handed, so every
  ladder runs on a copy and a ladder that finds no radius returns the untouched part.
- Placements, every frame from a measured feature of the mating part, never a
  bounding box (L-02), and every position below read back off the placed solid
  (`01_CAD/probe_placed_v03.json`). **OD-G04**: its own plate back face (its z = 0)
  and its tab 1 centre (its report measures −3.3°) → rotate +6.05° about Z, translate
  z −6.82, so its flange bottom face (its z −13.12) lands on the floor z −19.94.
  Measured on the placed solid: envelope z −22.940 … −5.730, tab centres at 2.75° /
  122.75° / 242.75° with a tab tip radius of 34.5191 at z −15.50, bead 31.1763 at
  z −15.17, pair A reaching z −22.940 and spanning r 12.01 … 18.99, pair B reaching
  z −21.700, hub bottom −22.550 with OD 20.06. **OD-G10**: its cup rim end face (its
  z = 0) and its ear 1 centre (59.5° from the handle) → 180° about +X, then +60.26°
  about Z (locked) or +122.5° (insertion), then the rim face to the pose's z. The
  locked z is not a parameter of this build: it is the measured first contact,
  −11.251029. Measured at that pose: min_z −11.251 with ear centres at 0.76° /
  119.76° / 240.26°, which are the three lug engagement spans; at the insertion pose
  min_z −11.701 with ear centres at 63.0° / 182.0° / 302.5°, which are the three gap
  centres.
- The check assembly STEP holds the three parts as placed, labelled
  `od_g01_housing`, `od_g04_brewing_gasket_support`, `od_g10_portafilter`.

## 6. Plausibility (§P, D6)

| # | Question | Answer, from the six sections |
|---|---|---|
| P1 | Gravity | Yes: the rear slab is the mounting flange and four M3 inserts at (±44, ±44) take it to OD-C05; the three lugs hang over the ears and the brew load runs ears → lug undersides → cup wall → slab → carrier, one continuous section in the front and lug-underside cuts. |
| P2 | Function chains | Yes: water enters OD-G04's hub tube through the Ø26 opening, which runs straight through the 5.00 slab to the rear face; the two OEM screws run from the rear through the Ø3.8 holes into pair B, and OD-G04's pair A passes the two Ø9 lobes — all visible in the top section, where the Ø26 circle and its two lobes read as the OEM keyhole. |
| P3 | Motion | Yes: the portafilter enters along −Z through three 66° gaps and turns 62.24° to the stop blocks; measured clearance stays ≥ 0.4945 mm over the whole insertion, ≥ 0.2765 mm through the rotation, and closes to 0 only on the final 0.45 mm of seating (§3). |
| P4 | Human factors | Yes: one opening, one insertion direction, three ears into three gaps with a stop block that ends the turn; screws, inserts and the water connection are all reached from the flat square rear face. |
| P5 | Absurdity next to a real product | No: as a Ø86.2 cup on a 100 mm square flange 28.24 tall, with a keyhole opening and two screw seats in the plate, it reads like the OEM group head it reproduces. The one thing a domain engineer would ask about is the 5.00 mm of slab now standing between the hub tube and the water connection (A-24), where the OEM has 2.50. |
| P6 | Nothing floating, embedded, mirrored or upside-down | Yes: one solid with every feature attached; lug 1 starts at 336° counter-clockwise as spec §2 fixes it, the mouth is at +3.30 and the rear face at −24.94, and the keyhole lobes sit at 359.5° and 179.0° against the pair-B recesses at 119.3° and 304.0°, which the top section shows. |

**What the sections show for D-03a and D-03b** (the reviewer's rows; listed, not
gated). Printed mouth up, six faces of the part face downward: the three lug
undersides — the shallow plane stands 2.5° from horizontal at the bore and 2.9° at
the lug inner radius, the ramp 29° and 33° at the same two radii, so both are under
the 45° limit — and the three stop-block bottoms at z −10.52, which are horizontal.
All six are supported by decision (A-22), and no other face of the part faces
downward. The shelf at −14.10, the three pocket floors at −17.30, the riser tops, the
slab top at −19.94, the four boss tops at −19.24, the two recess floors at −22.24,
the front face at +3.30 and the three lug top pads all face +Z; the lip ring's step
at z −17.70 faces +Z as well, because the lower lip wall (R 31.30) stands inside the
upper one (R 31.70); and the cup wall, the lug sides, the lip walls, the riser, the
keyhole, its two lobes, the recesses, the screw holes and the insert bores are all
upright. Nothing in the part bridges: the longest unsupported horizontal span is
zero.

## 7. Library and tools used

Cards (D1, two by tag, read at J2): `library/uno10/CARD.md#u4-puck` — the polar
(r, θ, z) profile map, and its recorded lesson that a press-turn joint must be swept
over rotation and axial position together, which §3's three-leg lock path follows;
and `library/uno10/CARD.md#u5-tank-heat-set` — the heat-set boss arrangement, and
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
boss-OD measurement (the second half of D-05a), a boss-root check (E-06), and a local
wall measurement (J-05 is answered from `radial_extent`'s own material stretches on
288 rays around the four insert axes, a located B-rep measurement, with the
whole-part `min_wall` reported beside it). Two more stand from v01: no boolean row
can be gated against an input solid that reads `brep_valid = 0` (OD-G10, A-28), and
no tool in `tools/` repairs or re-sews such a solid. Nothing new is missing this
round: spec 1.3's measured locked pose is a bisection on `measure.clearance`, which
exists.

Job code written this round, all in `01_CAD/` and none in the repository:
`build_od_g01_housing_v03.py`, `check_od_g01_housing_v03.py`,
`assemble_od_g01_check_v03.py`, `sections_od_g01_v03.py`, `probe_placed_v03.py`,
`probe_oem_contact_v03.py`, `probe_sweep_contact_v03.py`. No v01 or v02 file was
overwritten (L-11).

## 8. Deviations from the plan

**The WP-03 and WP-05 amendments (specs 1.1 and 1.2), still in force and built as
the briefs state them** — unchanged from REPORT v02 §8, repeated here so this REPORT
answers on its own:

| Plan row | Built |
|---|---|
| F02 slab 4.00 | 5.00 thick, z −24.94 … −19.94; envelope z 28.24 |
| F05, F06 lip ring R 30.82 / R 31.33 | R 31.70 from the shelf z −14.10 down to −17.70, R 31.30 below it to the floor |
| F07 pockets, floor −16.80 between R 34.39 and the bore | a notch between the lip wall R 31.70 and a riser at R 35.10, floor z −17.30, open to the shelf |
| F10 keyhole | Ø26.0 straight through the 5.00 slab; spec 1.2 drops the rear counterbore WP-03 added |
| F11 lobes (slots on θ 133° and 310°) | two Ø9.0 through-holes at r 15.5, θ 359.5° and 179.0°, each merging with the Ø26 opening into one keyhole lobe |
| F12, F13 OD-G04 insert bosses and Ø4.0 bores | two Ø9.0 × 2.30 recesses from the floor with Ø3.8 through-holes at r 19.03, θ 119.3° and 304.0°: no inserts there, the OEM's own screws from the rear |
| F14, F15 carrier inserts | Ø4.0 × 5.70 from the rear face at (±44, ±44), with a 0.70 boss on the floor side |
| F09 lug underside | the OEM's two planes and nothing else: the shallow plane from (+7°, −6.57) to (+41.8°, −5.59) and one straight ramp to (+54°, −1.15) |
| §5 OD-G04 joint +4.74°, seat z −7.28 | +6.05° about Z, its plate back face at housing z −6.82, so its flange bottom rests on the floor |
| §6 REQ-10 at 0.8 | 0.30 over the insertion path |
| §6 census | spec 1.2's list, without the counterbore |

**Carried from REPORT v02 §8, unchanged because the geometry is unchanged:** the
carrier boss OD is 10.30, not the plan's 8.00 (J-05 needs 3.0 mm of wall round a
Ø4.0 hole, which is 10.0 across; measured wall 3.1500, material across 10.3000); the
carrier insert bores have no mouth chamfer (plan F15), because a 0.5 × 45° chamfer
shortens the Ø4.0 cylinder to 5.20 and fails D-05b as `locate_bore` measures it; the
lug root fillets of plan F18 are not achieved; the STL is meshed at 0.002 mm, not the
plan's 0.01, because at 0.01 the mesher's own sagitta measures over U-07's limit on
the lofted underside faces; REQ-09's outer profile uses a z step that avoids z = 0.0
exactly; and the sweep's `lip_upper_r` range is ±0.05, not the plan's ±0.08, because
the U-05 pocket predicate written at D3 recognises a pocket by material at r ≤ 31.75.

**This round differs from the plan and from v02 as follows:**

1. **The scripts carry `v03` in their names, and the build script is a copy.**
   `01_CAD/build_od_g01_housing_v03.py` is `…_v02.py` with the docstring updated,
   `VERSION = 2` → `3` (which moves the STEP, STL, assembly and `measured_*.json`
   names), the two module imports in `main()` moved to the v03 check and assemble
   modules, and one changed line: the assembly is written with OD-G10 at
   `out["detail"]["assembly"]["g10_locked_rim_z"]`, the pose the checks have just
   measured, instead of v02's constant −11.20. The `Params` structure and the
   `build()` function are byte-identical (§5). The briefs name
   `01_CAD/build_od_g01_housing.py` and `01_CAD/check_od_g01_housing.py`; those files
   are v01's and are hashed into REPORT v01, so overwriting them would break that
   record.
2. **The locked pose is a measurement, not a number** (spec 1.3 §5 U-03(a)).
   `assemble_od_g01_check_v03.py` no longer carries a locked rim z: it carries
   `first_contact_rim_z()`, a 24-step bisection on `measure.clearance` between a rim
   height that is clear (−13.5) and one that is touching (−10.5), and A-14's −11.20
   ± 0.10 survives only as the band the measurement is reported against and as the
   centre of that bracket. Everything downstream takes the measured value as an
   argument: the contact row, the probe, the per-lug diagnostics, the lock path's end
   pose and the rotation depth, the check assembly STEP, and `probe_placed_v03.py`.
   If the bisection cannot answer, every row that rests on it is INCONCLUSIVE.
3. **The probe is gated in one direction only.** Spec 1.3 names −Z; the check gates
   that row and measures the +Z reading beside it as a reported diagnostic (0.0000 mm
   at rim −11.051029, which is what shows the contact is a contact). v02 gated both
   and failed both.
4. **The lock path moved with the pose.** Its end is the measured locked rim z
   −11.251029 and the rotation depth is 0.45 mm below it, −11.701029, so the
   insertion leg now runs 0.051 mm deeper than v02's and REQ-10's worst pose reads
   0.4945157 mm instead of v02's 0.4970. **The rotation depth is a derivation**:
   0.45 mm below the locked pose, deep enough that the ear tops turn clear of the lug
   undersides and inside the 0.5 mm of approach spec §5 U-03(b) exempts, so the
   exempt part of the path is the seating leg and the last rotation pose.
5. **The three ear tops are gated as one pair and reported lug by lug**, as in v02
   (spec §5 names one designed-contact pair, and A-25's 120.5 / 120.5 / 119° ears
   cannot all reach a symmetric 120° lug pitch at one pose). Read at the true contact
   pose the three now measure 0.0000000 / 0.0903189 / 0.0210511 mm, where at v02's
   fixed −11.20 they measured 0 / 0.03936 / 0.
6. **D7 was not re-run; it was cited and extended** (§4). WP-06 directs that the v02
   sweep stands for an unchanged build script. Its two superseded U-03(a) rows were
   re-measured under spec 1.3 on the sweep STEPs that already exist, in 12 cases, by
   `probe_sweep_contact_v03.py` — no rebuild.
7. **Three diagnostic probes beyond the plan's file list** (`probe_placed_v03.py`,
   `probe_oem_contact_v03.py`, `probe_sweep_contact_v03.py`). None answers a gate;
   they are the measurements §3, §4 and §5 quote. v02's four probes were not re-run;
   two of them (`probe_g10_v02.py`, `probe_contact_v02.py`) answered questions spec
   1.3 has settled.
8. **No fix cycle was used.** The checks were written first, the build was run once,
   and every row that a tool can answer passed on that run. (The first invocation of
   the build was stopped by the operator's own background time limit after it had
   written the STEP and the STL and before the checks finished; it was re-run
   unchanged and the STEP and STL came out byte for byte the same, the writer being
   deterministic at the pinned timestamp. Nothing was changed between the two runs,
   so it is not a fix cycle.)
9. The plan's §7 R1 and R2 (the OD-G04 overlap and REQ-10 at 0.8) are answered by
   the ledger rows the briefs quote: both measure clear (0.000 mm³ and 0.4945 mm).

## 9. What I am least sure of

1. **Only one ear top touches at the measured locked pose.** At rim z −11.251029 lug
   1 reads 0.0000000 mm while lug 2 stands 0.0903189 and lug 3 0.0210511 mm off. This
   is A-25 (ears at 120.5 / 120.5 / 119°) against §4 C1's symmetric 120° lug pitch,
   and it is a fact about the two parts, not a modelling error — but spec §5 U-03(a)
   gates "the three ear tops on the lug undersides" as one pair, and the measurement
   says the bayonet makes first contact on one lug of three. If the real assembly
   loads through all three, it does so after 0.09 mm of deflection somewhere (the
   gasket, A-27, is the obvious candidate and is unmeasured); if it does not,
   REQ-12's bench load runs through one lug, not the ledger's 3.06 kN / 3. Reading
   this at the true contact pose is what changed the numbers from v02's 0 / 0.039 /
   0: at the fixed −11.20 two lugs were already past contact, which hid it.
2. **`lug_starts_hi` puts U-03(a)'s probe out of band through a different pair**
   (§4). At +0.25° on all three lug starts the probe reads 0.1382296 mm at the
   stop-block bottom, because the ear leading edge sits 0.5° from the stop at the
   locked clock and a quarter-degree of lug clocking eats half of it. The delivered
   part at nominal reads 0.1997125 and nothing overlaps in either case, but the
   locked-clock gap between the ear leading edge and the stop block is only 0.276 mm
   at nominal and is the smallest clearance anywhere on the lock path outside the
   seating leg. A-14 fixes that 0.5° and A-04 fixes the lug starts; both are OPEN and
   both are to be retired with a protractor on the donor.
3. **Everything that rests on OD-G10's boolean.** Its STEP is not a valid solid by
   `tools.core.validity` (A-28), so U-03(a)'s boolean at the locked pose is
   INCONCLUSIVE and will stay so for the reviewer. The distance evidence is now
   strong — the housing and the OEM cup read the same probe to 1.7e−05 mm (§3) — but
   no boolean confirms that nothing interpenetrates somewhere the nearest-point
   distance cannot see.
4. Smaller, all measured: D-05b's depth margin is 2.7e−15 by construction (A-17's
   5.70 hole in a 5.00 slab plus a 0.70 boss), which also means each insert bore
   breaks through the boss top and opens on the cup floor — the 5.7 mm insert fills it
   exactly, and nothing in §5 reads the opening, but it is a hole into the wet side;
   U-03(a)'s bead (+0.0237) and pair B (+0.040) margins are thin and move with A-09,
   A-12 and A-17; the seven lug root edges are sharp; and A-14's ±0.10 band on the
   locked rim z leaves the underside level (A-05) about ±0.05 mm of room (§4).

## 10. Stop

Not stopped. Spec 1.3's correction is confirmed by measurement: with the locked pose
read as the first contact and the probe displaced along −Z, the housing reads
0.1997125 mm and the OEM cup it reproduces reads 0.1997295 mm on the identical row,
both inside [0.19, 0.21]. No hard gate is unmet by a measurement; the six
INCONCLUSIVE rows are the four the missing `tools/measure` functions leave to the
reviewer, the OD-T01 bench test (REQ-12), and the OD-G10 boolean that spec §5 itself
answers by distance (A-28). Of the 49 rows of §3, 43 pass (13 outright, 30 resting on
an open ledger row) and 6 are INCONCLUSIVE; none fails. Fix cycles used: 0 of 3.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-g01-group-head-housing",
 "part": "od_g01_housing",
 "tag": "v03",
 "spec_version": "1.3",
 "files": [
  {
   "path": "01_CAD/build_od_g01_housing_v03.py",
   "sha256": "47c9d449bda0330e987f7e147b019118146ae789e59b39461d9f3fe1e3132896"
  },
  {
   "path": "01_CAD/check_od_g01_housing_v03.py",
   "sha256": "8cb806508af12af3da089562ab6bef779ac8334a5b977773102190f6f0050617"
  },
  {
   "path": "01_CAD/assemble_od_g01_check_v03.py",
   "sha256": "7fad3c08c8b31007bf90431b6487ba64aed20c260414f1d818e66ee06430a505"
  },
  {
   "path": "01_CAD/sections_od_g01_v03.py",
   "sha256": "9808c27f8779fdc41a57620ca8d79220b15af52717af26f36199236ee0de3918"
  },
  {
   "path": "01_CAD/probe_placed_v03.py",
   "sha256": "9524359825a0aeed72f2cc9ea4a40a4208bc1464ca8d642bb9014caa4c28815b"
  },
  {
   "path": "01_CAD/probe_oem_contact_v03.py",
   "sha256": "f3448bba50b72416bc878d54f4f8d4f9b69edfb805f8606357e29dba80fd87be"
  },
  {
   "path": "01_CAD/probe_sweep_contact_v03.py",
   "sha256": "4d194d904dc97cc5af57ffdaff82a5fc4f7e3dec64edc8a9be1fa4cd127f343d"
  },
  {
   "path": "01_CAD/measured_v03.json",
   "sha256": "b647e9fd9d18ccc70237e0f6e30278e9645db344408ea9cad417a12f8d345540"
  },
  {
   "path": "01_CAD/sections_v03.json",
   "sha256": "0792e6d763592583b762f5a2762a4809111c98876754c6c2de6e956e6ac38991"
  },
  {
   "path": "01_CAD/probe_placed_v03.json",
   "sha256": "b3ac0b9a988849c5700bd8cf670df7d635d46a343f12beda270c6535d54357ec"
  },
  {
   "path": "01_CAD/probe_oem_contact_v03.json",
   "sha256": "2ce30fe3420fb5a327ed5946ff4dd53732c6c3e80167538237d9f804c593f8b3"
  },
  {
   "path": "01_CAD/probe_sweep_contact_v03.json",
   "sha256": "b6e34805b3d6f39094e9ff673ce4cbcb639ee3001c109c4680ff7033014d4f37"
  },
  {
   "path": "02_STEP_STL/od_g01_housing_C1_v03.step",
   "sha256": "55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399"
  },
  {
   "path": "02_STEP_STL/od_g01_assembly_C1_v03.step",
   "sha256": "9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2"
  },
  {
   "path": "02_STEP_STL/od_g01_housing_C1_v03.stl",
   "sha256": "0e8fe8e265284ca76cff363dbbd2ab6df5c8485d8e4e8610f58ad29295f38cec"
  },
  {
   "path": "03_Sections/od_g01_housing_v03_front.png",
   "sha256": "440317bad3e524ec54b9dab46a13aabb1ff480cd8bc50d39768596cea1232fb1"
  },
  {
   "path": "03_Sections/od_g01_housing_v03_top.png",
   "sha256": "9c37e36c00ede2a0b82f02c086a4e4a3f41111a2e271569079514f7a754a81c2"
  },
  {
   "path": "03_Sections/od_g01_housing_v03_left.png",
   "sha256": "b1a5f5ca4e8ea8891288192d75d01f3fad3bc93fdb140a10b777cb3935b2627a"
  },
  {
   "path": "03_Sections/od_g01_housing_stopblock_v03_front.png",
   "sha256": "f101901d79a301a8fb48524e44a207f7ec1661c93dd410bd6f32e0502aeb7a95"
  },
  {
   "path": "03_Sections/od_g01_housing_lugunderside_v03_front.png",
   "sha256": "46f4ccc995a5ca0143b7d2faef5f1287687440e53cc411a90702c9722aad7d06"
  },
  {
   "path": "03_Sections/od_g01_housing_insertboss_v03_front.png",
   "sha256": "2a6022aaa1f071911d3a9b21fcbc1a3d629bdd507e975801444a4cbe32ddcdba"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "7.9.3.1.1 (OCCT 7.9.3)",
  "numpy": "2.5.3",
  "repo_commit": "18c4ddc"
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
   "at": "(0.0000, 0.0000, -24.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10",
    "A-11"
   ]
  },
  {
   "gate": "REQ-11",
   "measured": 5.0,
   "unit": "mm",
   "required": "in [4.9, 5.1]",
   "margin": 0.1,
   "at": "(0.0000, 0.0000, -24.9400) mm",
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
    "A-11"
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
   "at": "(31.6028, -2.2099, -5.7000) mm",
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
   "measured": 1.5299999999977973,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 0.73,
   "at": "(7.2695, -10.7775, -19.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 1.5299999999977973,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 0.53,
   "at": "(7.2695, -10.7775, -19.9400) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ]
  },
  {
   "gate": "D-06a",
   "measured": 1.5299999999977973,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 0.53,
   "at": "(7.2695, -10.7775, -19.9400) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06",
   "measured": 1.15,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 0.15,
   "at": "(32.1295, 18.5500, 0.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 3.637978807091713e-09,
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
   "gate": "U-03",
   "measured": 1.9860273225978185e-15,
   "unit": "mm",
   "required": "== 0.0",
   "margin": -1.9860273225978185e-15,
   "at": "(30.8756, -7.0938, -6.4508) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
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
   "at": "(19.9992, -0.1745, -19.9500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) pairA2",
   "measured": 1.009999999999109,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 0.51,
   "at": "(-19.9970, 0.3490, -19.9500) mm",
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
   "at": "(12.5183, -3.5061, -19.9500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) locked rim z",
   "measured": -11.251028716564178,
   "unit": "mm",
   "required": "in [-11.299999999999999, -11.1]",
   "margin": 0.048971283,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) ear tops on the lug undersides",
   "measured": 1.9860273225978185e-15,
   "unit": "mm",
   "required": "== 0.0",
   "margin": -1.9860273225978185e-15,
   "at": "(30.8756, -7.0938, -6.4508) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) od_g10 moved 0.20 along -Z",
   "measured": 0.1997124662918752,
   "unit": "mm",
   "required": "in [0.19, 0.21]",
   "margin": 0.009712466,
   "at": "(30.8731, -7.1046, -6.4513) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) housing|od_g10 boolean",
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
   "gate": "U-03 (b) lock path",
   "measured": 1.9860273225978185e-15,
   "unit": "mm",
   "required": ">= 0.0",
   "margin": 1.9860273225978185e-15,
   "at": "(30.8756, -7.0938, -6.4508) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "REQ-10",
   "measured": 0.4945156750356085,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.194515675,
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
   "at": "(12.5183, -3.5061, -19.9500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-24"
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
  }
 ],
 "sweep": [
  {
   "parameter": "bore_r",
   "values": [
    37.05,
    37.1,
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
    31.68,
    31.78
   ],
   "all_built": true,
   "worst_gate": "REQ-01",
   "worst_margin": -0.0,
   "u03a_spec_1_3_remeasured": {
    "locked_rim_z_mm": [
     -11.252303838729858,
     -11.24976235628128
    ],
    "locked_rim_z_in_a14_band": [
     true,
     true
    ],
    "probe_minus_z_mm": [
     0.19971030900301787,
     0.1997146361827531
    ],
    "probe_in_band": [
     true,
     true
    ]
   }
  },
  {
   "parameter": "lug_span",
   "values": [
    53.75,
    54.0,
    54.25
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0,
   "u03a_spec_1_3_remeasured": {
    "locked_rim_z_mm": [
     -11.251028716564178,
     -11.251028716564178
    ],
    "locked_rim_z_in_a14_band": [
     true,
     true
    ],
    "probe_minus_z_mm": [
     0.1997124662918752,
     0.1997124662918752
    ],
    "probe_in_band": [
     true,
     true
    ]
   }
  },
  {
   "parameter": "lug_starts",
   "values": [
    -0.25,
    0.0,
    0.25
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0,
   "u03a_spec_1_3_remeasured": {
    "locked_rim_z_mm": [
     -11.24383020401001,
     -11.258242428302765
    ],
    "locked_rim_z_in_a14_band": [
     true,
     true
    ],
    "probe_minus_z_mm": [
     0.1997137724409129,
     0.13822963813566266
    ],
    "probe_in_band": [
     true,
     false
    ]
   }
  },
  {
   "parameter": "stop_end_off",
   "values": [
    5.26,
    5.76,
    6.26
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0,
   "u03a_spec_1_3_remeasured": {
    "locked_rim_z_mm": [
     -11.251028716564178,
     -11.251028716564178
    ],
    "locked_rim_z_in_a14_band": [
     true,
     true
    ],
    "probe_minus_z_mm": [
     0.1997124662918752,
     0.1997124662918752
    ],
    "probe_in_band": [
     true,
     true
    ]
   }
  },
  {
   "parameter": "stop_bottom_z",
   "values": [
    -10.82,
    -10.52,
    -10.22
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0,
   "u03a_spec_1_3_remeasured": {
    "locked_rim_z_mm": [
     -11.251028716564178,
     -11.251028716564178
    ],
    "locked_rim_z_in_a14_band": [
     true,
     true
    ],
    "probe_minus_z_mm": [
     0.1997124662918752,
     0.1997124662918752
    ],
    "probe_in_band": [
     true,
     true
    ]
   }
  },
  {
   "parameter": "shelf_z",
   "values": [
    -14.2,
    -14.1,
    -14.0
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "pocket_floor_z",
   "values": [
    -17.4,
    -17.3,
    -17.2
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "pocket_riser_r",
   "values": [
    34.95,
    35.1,
    35.25
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "pocket_start_off",
   "values": [
    -5.5,
    -5.0,
    -4.5
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "pocket_end_off",
   "values": [
    58.0,
    58.5,
    59.0
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "lip_upper_r",
   "values": [
    31.65,
    31.7,
    31.75
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "lip_lower_r",
   "values": [
    31.25,
    31.3,
    31.35
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "plate_t",
   "values": [
    4.9,
    5.0,
    5.1
   ],
   "all_built": true,
   "worst_gate": "U-02 size_z",
   "worst_margin": -0.0
  },
  {
   "parameter": "keyhole_d",
   "values": [
    25.95,
    26.0,
    26.05
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "pair_b_r",
   "values": [
    18.98,
    19.03,
    19.08
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "carrier_xy",
   "values": [
    43.95,
    44.0,
    44.05
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_d",
   "values": [
    3.98,
    4.0,
    4.02
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_depth",
   "values": [
    5.7,
    5.7,
    6.0
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0
  },
  {
   "parameter": "under_knots",
   "values": [
    -0.3,
    0.0,
    0.3
   ],
   "all_built": true,
   "worst_gate": "D-05b",
   "worst_margin": 0.0,
   "u03a_spec_1_3_remeasured": {
    "locked_rim_z_mm": [
     -11.551028788089752,
     -10.951028823852539
    ],
    "locked_rim_z_in_a14_band": [
     false,
     false
    ],
    "probe_minus_z_mm": [
     0.19971253771465403,
     0.1997125734260445
    ],
    "probe_in_band": [
     true,
     true
    ]
   }
  }
 ],
 "sweep_source": {
  "path": "01_CAD/sweep_v02/sweep_v02.json",
  "sha256": "b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3",
  "note": "the round-2 sweep, cited because the build script is unchanged; its two U-03(a) probe rows are superseded by spec 1.3 and were re-measured on the same solids by probe_sweep_contact_v03.py"
 },
 "least_sure": [
  "only one ear top touches at the measured locked pose: lug 1 0.0000000, lug 2 0.0903189, lug 3 0.0210511 mm (A-25's ear pitch against a symmetric 120 deg lug pitch)",
  "lug_starts +0.25 deg puts U-03(a)'s probe at 0.1382296 mm through the ear-to-stop-block gap, not through the ear-top contact; at nominal the row reads 0.1997125 mm",
  "the housing|OD-G10 boolean stays INCONCLUSIVE because the OD-G10 input reads brep_valid 0 (A-28); only distances answer U-03(a) against it",
  "D-05b's depth margin is 2.7e-15 by construction, so each insert bore opens on the cup floor"
 ],
 "stopped": false,
 "fix_cycles_used": 0,
 "fix_cycles_cap": 3,
 "sweep_note": "worst_gate and worst_margin are the worst geometric row of the two runs in the cited round-2 sweep; u03a_spec_1_3_remeasured is this round's measurement of spec 1.3's U-03(a) rows on the same sweep solids (probe_sweep_contact_v03.py), [low, high]"
}
```

