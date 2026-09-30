# REPORT — od_g01_housing v02 (20260930-od-g01-group-head-housing)

Designer: Claude Code, Opus 5 · spec version 1.2 · plan `01_CAD/DESIGN_PLAN.md` with the WP-03 and WP-05 amendments · 2026-09-30 UTC

**Outcome: STOPPED (D9).** The part is built, exported and measured, and every §5
row is answered below. The four rows that stopped v01 (D-01a, D-01b, D-06a and the
soft U-06, all at the rear counterbore that spec 1.2 drops) now pass: `min_wall`
reads **1.530 mm** at 25° opposition and **1.150 mm** at the 45° opposition U-06
reads.

One hard row fails: **U-03(a)'s 0.20 mm probe of the locked pose**. This housing
first meets OD-G10 at rim z **−11.25103**, 0.051 mm below the ledger's locked rim z
−11.20 (A-14), so the probe reads **0.14876 mm** where §5 asks for [0.19, 0.21]; and
the +Z direction the row names is measurably the direction that drives OD-G10
**into** the designed contact, where the probe reads **0.0000 mm**. Nothing inside a
spec §5 band moves either, and the OEM pair OD-G09 | OD-G10 reads 0.13806 mm on the
same probe: §10 has every measurement and the options.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_g01_housing_v02.py` | 68209698cc98d041d3ba5b9450646086130964f21cfce1814f0c7fc46efb3fb5 | parametric script, build123d Algebra mode, one Params structure |
| `01_CAD/check_od_g01_housing_v02.py` | 31fe6c47380894a08ef046a7510f7b8cd883bf0b2b83e4f312961d59583d2127 | checks, written before the build (D3) |
| `01_CAD/assemble_od_g01_check_v02.py` | 8fa361df8073645ee2e1be6438d78c62dc545a0b47e58720f9e95936cbac066d | the spec §5 joints, the lug pieces and the OD-G04 feature pieces, the three-leg lock path |
| `01_CAD/sweep_od_g01_v02.py` | 47d725aa0f2f540b4a0f8eea3400820fdb99d8eedbac376d1bdc12eeacb1db07 | D7 sweep driver |
| `01_CAD/sections_od_g01_v02.py` | c3147966b9a1cf469b112520d9d40989428019551b939a75861d1cd3ea631eb3 | D6 sections |
| `01_CAD/probe_g10_v02.py` | 17f238afdb1feb513ecf5f01e18c896c6a166d8d3e57df6ec10a6330dbe584db | diagnostic run at D3, on the v01 STEP, before the v02 build: which way OD-G10 separates from the lug undersides. Its numbers are v01's and are not quoted as v02 measurements |
| `01_CAD/probe_contact_v02.py` | 5b7f880b68556dc6fa71ae025dbdfc7101fa6887354fa6a9735f95e6670d009a | diagnostic: the contact rim z against `lug_inner_r` and against the underside level |
| `01_CAD/probe_oem_contact_v02.py` | 7a9723aad088af2fc1646b654118cda8cc5128f358372cbd6bdb5709a42e7e3f | diagnostic: where the OEM pair OD-G09 \| OD-G10 meets at the same clock |
| `01_CAD/probe_placed_v02.py` | 2c322c268c55f55320d05cc65df582a5900f91508d61f7847c2246ad25e12583 | diagnostic: the mating parts measured where the joints put them |
| `01_CAD/measured_v02.json` | 3ec1095a4c9d481e4d3bb600851887b788632baba0bdff26d5e416430c07b9c1 | every gate row with its measurement and detail |
| `01_CAD/sections_v02.json` | 8ac2652ce8a8d77b8dece0738fd30c847517be545f045e43edfa90b5b8f6383f | the sections with `nothing_clipped` |
| `01_CAD/probe_contact_v02.json` | 150bcd56744d949c34a2d5b22823e672ffdf0320b61a26e4a923b6a993fe8eb0 | §10's first table, measured |
| `01_CAD/probe_oem_contact_v02.json` | bb51b4f9008c8ae74fc0867cc51cef6ccc6984df9e65e79ed1dacff3dc6f818d | §10's OEM reading, measured |
| `01_CAD/probe_placed_v02.json` | 725f807f7b323f0124a78c7c5b6d9412a89a2481b958ec0f6ee82a2fd66bbf6d | §5's placement measurements |
| `01_CAD/sweep_v02/sweep_v02.json` | b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3 | D7 results, one entry per case |
| `02_STEP_STL/od_g01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | AP242 (`tools.core.write_step`), re-imported for every measurement |
| `02_STEP_STL/od_g01_assembly_C1_v02.step` | 8b9ce55fd306c63c99851656675d38bd0c002d17a1661d7001c1fc0fafb51c11 | check assembly: housing + OD-G04 seated + OD-G10 at the locked pose |
| `02_STEP_STL/od_g01_housing_C1_v02.stl` | 0e8fe8e265284ca76cff363dbbd2ab6df5c8485d8e4e8610f58ad29295f38cec | triangulation cleared first; tolerance 0.002 mm, angular 0.08616775 rad, 135 024 triangles, measured sagitta 0.0094356 mm |
| `03_Sections/od_g01_housing_v02_front.png` | e093e24a22505eec2a31579e039dc3eac4d000efa0505ec25fe4a79fa8de8d43 | section y = 0 (lug 1 at +24°, the gap at 180°), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_v02_top.png` | 257bfa6f80a0f0fc2ba23abf426116f99e03679532ab92c44b800f31d3d595cc | section z = −15.94 (pockets, lip ring, keyhole and its two lobes, pair-B recesses, carrier bosses), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_v02_left.png` | d59834cb90d931630ce625423151969db9d61d5c71e7c9da3b4434b62266a875 | section x = 0, `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_stopblock_v02_front.png` | 42cbe97b09a9c2a5e9f99e8428c360edb8fd2220a0fcaf048140a6127103c146 | section through a stop block (lug 1 + 2.9°), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_lugunderside_v02_front.png` | 3c50912bd8b618c0f1a9a45c5a8f48487e8cd2217e77ba2f0646e81e4a35ff55 | section through REQ-04's shallow-plane ray (lug 1 + 20°), `nothing_clipped` 0 |
| `03_Sections/od_g01_housing_insertboss_v02_front.png` | b2727c9912264d12197e1a746ba7c64c965f19d827bca0f84efffd708ff32137 | section through two carrier insert bosses, `nothing_clipped` 0 |

The `01_CAD/sweep_v02/` folder also holds one STEP per sweep case, named after the
case; they are working files of §4, not deliverables.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 (pinned, D-023) · OCP 7.9.3.1.1 (OCCT 7.9.3) ·
numpy 2.5.3 · repo commit `18c4ddc`. Input hashes checked against the brief before
any other work: all three match (`OD-G09` 2f11c1b7…a831906, `OD-G04`
19b4a140…098d6ad2, `OD-G10` 3a525af1…ea187b257).

## 3. Gate self-check

Every value is measured by `check_od_g01_housing_v02.py` on the B-rep of the
re-imported `02_STEP_STL/od_g01_housing_C1_v02.step`; limits are spec 1.2 §5's,
bands are GATES §0's (0.005 mm, 0.001 deg, 0.001 mm³, 0.00002 rad, 0 for counts and
1/0 facts). Where a gate has several rays or sub-rows, the row below is the worst of
them and `01_CAD/measured_v02.json` holds them all. The table below carries 49 rows;
the JSON block at the end carries the full 54 the check script emits, which differ
only in that the table shows OD-G04's three tabs, its two pair-A bosses and its two
pair-B bosses as one row each and leaves out the OD-G04 feature summary row. A
self-check clears nothing: the reviewer's own measurement does.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | size 100.0000002 × 100.0000002 × 28.2400002 mm | each in [spec ± 0.1] | +0.0999998 | — | PASS | — |
| U-03 | **FAIL** on the 0.20 mm probe rows below; every other U-03 row passes | see the rows below | −0.041242918 (best failing row) | (30.8737, −7.1018, −6.4512) | **FAIL** | A-13, A-14, A-19 |
| U-03 (a) housing\|OD-G04 | 0.000 mm³ | ≤ 0 mm³ | 0.000 | — | PASS (assumed: A-13) | A-13 |
| U-03 (a) designed contact, OD-G04 flange on the floor | 0.000 mm | = 0 | 0.000 | (13.0586, 6.4522, −19.9400) | PASS (assumed: A-13) | A-13 |
| U-03 (a) OD-G04 tabs | 0.5800 mm (tab 1; tabs 2 and 3 the same) | ≥ 0.5 | +0.080 | (29.3402, 19.2656, −15.4600) | PASS (assumed: A-12, A-13) | A-12, A-13 |
| U-03 (a) OD-G04 bead | 0.52366 mm | ≥ 0.5 | +0.02366 | (−27.1722, −16.3267, −15.1700) | PASS (assumed: A-09, A-13) | A-09, A-13 |
| U-03 (a) OD-G04 pair A | 1.0100 mm | ≥ 0.5 | +0.510 | (19.9992, −0.1745, −19.9500) | PASS (assumed: A-11, A-12) | A-11, A-12 |
| U-03 (a) OD-G04 pair B | 0.5400 mm | ≥ 0.5 | +0.040 | (−10.2981, 18.3360, −22.2400) | PASS (assumed: A-12) | A-12 |
| U-03 (a) OD-G04 hub | 2.9700 mm | ≥ 0.5 | +2.470 | (12.5183, −3.5061, −19.9500) | PASS (assumed: A-24) | A-24 |
| U-03 (a) designed contact, ear tops on the lug undersides | 0.0000 mm | = 0 | 0.000 | (35.2699, −7.0355, −6.3997) | PASS (assumed: A-14) | A-14 |
| U-03 (a) OD-G10 moved 0.20 along **+Z** (the row as §5 writes it) | 0.0000 mm | in [0.19, 0.21] | −0.190 | (35.2699, −7.0355, −6.1997) | **FAIL** | A-14, A-19 |
| U-03 (a) OD-G10 moved 0.20 along **−Z** (the direction that opens the contact) | 0.14876 mm | in [0.19, 0.21] | −0.041243 | (30.8737, −7.1018, −6.4512) | **FAIL** | A-14, A-19 |
| U-03 (a) housing\|OD-G10 boolean | INCONCLUSIVE: `common_volume` refuses the pair, the OD-G10 input reads `brep_valid` 0 | ≤ 0 mm³ | — | — | INCONCLUSIVE (A-28) | A-28 |
| U-03 (b) lock path, 43 poses | 0.4970 mm worst before the last 0.5 mm of approach; 0.0000 mm worst inside it | ≥ 0.30 before, ≥ 0 inside | +0.19702 / 0.000 | (−3.3115, 31.5065, 0.0000) | PASS (assumed: A-14, A-19) | A-14, A-19 |
| U-04 | schema 1, solids 1, labels 1, faces_delta 0, volume_delta 3.6e−09 mm³, valid_after 1 | as stated | −4e−09 mm³ | — | PASS | — |
| U-05 | 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 2 Ø9 pass-through + 2 Ø9 recesses, 2 Ø3.8 through-holes, 4 Ø4.0 insert bores | = the spec's counts | 0 | — | PASS | — |
| U-06 (Soft) | min_wall wide (45°) 1.150 mm | ≥ 1.0 | +0.150 | (32.1295, 18.5500, 0.0000) | PASS | — |
| U-07 | sagitta 0.0094356 mm at tolerance 0.002 mm, angular 0.08616775 rad, 135 024 triangles | sagitta ≤ 0.01, tol ≤ 0.01, a ≤ 0.08616775 | +0.00056 (sagitta), 0.000 (angular) | — | PASS | — |
| U-08 | faces the census cannot name: 0; every insert bore a plain cylinder Ø4.000 | = 0 (N/A by its row: no thread) | 0 | — | PASS | — |
| D-01a | min_wall 1.5300 mm, the web between the Ø26 opening and a pair-B Ø9 recess | ≥ 0.8 | +0.730 | (7.2695, −10.7775, −19.9400) | PASS | — |
| D-01b | min_wall 1.5300 mm | ≥ 1.0 | +0.530 | same | PASS (assumed: A-05) | A-05 |
| D-02 | 100.0000002 × 100.0000002 × 28.2400002 mm | ≤ 220 × 220 × 250 | +119.9999998 | — | PASS (assumed: A-16) | A-16 |
| D-03a | no overhang measurement in `tools/measure` (GATES: reviewer, from sections) | ≥ 45° or supported by A-22 | — | sections, §6 | INCONCLUSIVE | A-22 |
| D-03b | no bridge measurement in `tools/measure` (GATES: reviewer, from sections) | span ≤ 5 | — | sections, §6 | INCONCLUSIVE | — |
| D-04a | Ø3.8000 mm, both pair-B screw holes | ≥ 3.75 | +0.050 | (−9.3129, 16.5955, −24.9400) | PASS (assumed: A-26) | A-26 |
| D-05a | material across each Ø4.0 insert axis 10.300 mm, worst of 288 rays | ≥ 8.0 | +2.300 | (44.0000, 44.0000, −19.5900) | PASS (assumed: A-17) | A-17 |
| D-05a boss OD | no boss-OD measurement in `tools/measure` (GATES: reviewer) | OD ≥ 8.0 | — | — | INCONCLUSIVE | A-17 |
| D-05b | Ø4.0000 mm, length 5.7000 mm from the rear face, all four | Ø in [3.95, 4.05], depth ≥ 5.7 | +2.7e−15 (depth) | (44.0000, 44.0000, −24.9400) | PASS (assumed: A-17) | A-17 |
| D-06a | min_wall 1.5300 mm | ≥ 1.0 | +0.530 | (7.2695, −10.7775, −19.9400) | PASS | — |
| D-07 | Ø26 opening to the OD-G04 hub as placed 2.9700 mm | N/A by its row; ≥ 2.9 | +0.070 | (12.5183, −3.5061, −19.9500) | PASS (assumed: A-24) | A-24 |
| J-05 | wall around each insert axis 3.1500 mm, worst of 288 rays | ≥ 3.0 | +0.150 | (44.0000, 44.0000, −19.5900) | PASS | — |
| E-06 | no boss-root measurement in `tools/measure` (GATES: reviewer); the root fillet achieved is R 0.6 on all four bosses | a root fillet on every boss | — | sections, §6 | INCONCLUSIVE | — |
| REQ-01 | inner radius over start + 8°…40°, z −5.0…−1.0: min 31.680, max 31.680 mm (99 angles × 40 levels) | in [31.58, 31.78] | +0.100 | (30.6005, −8.1994, −4.9500) | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner radius in the gaps, z −13.0…+2.0: min 37.100, max 37.100 mm (84 angles × 75 levels) | in [37.05, 37.15] | +0.050 | (30.0145, 21.8068, −12.9000) | PASS (assumed: A-03) | A-03 |
| REQ-03 | z −3.0: 31.680 at start + 1°, + 27°, + 40°; 37.100 at start − 1° and + 55°, all three lugs (15 rays) | ≤ 31.78 / ≥ 37.05 | +0.050 | (33.6240, −15.6791, −3.0000) | PASS (assumed: A-04) | A-04 |
| REQ-04 | start + 20°: 31.680 at z −5.7, 37.100 at z −6.7; start + 47°: 31.680 at z −3.2, 37.100 at z −4.2 (12 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (31.6028, −2.2099, −5.7000) | PASS (assumed: A-05) | A-05 |
| REQ-05 | start + 2.9°: 31.680 at z −9.0, 37.100 at z −11.0 (6 rays) | ≤ 31.78 / ≥ 34.0 | +0.100 | (29.5560, −11.4047, −9.0000) | PASS (assumed: A-06) | A-06 |
| REQ-06 | Ø26.000 mm, axis offset 0.000 mm, through = 1 | Ø 26.0 ± 0.1, on the axis, through | +0.100 | (0.0000, 0.0000, −24.9400) | PASS (assumed: A-10, A-11) | A-10, A-11 |
| REQ-07 | two Ø3.800 through-holes at r 19.03, θ 119.3° / 304.0°, offset 2.6e−07; recesses Ø9.000 × 2.300 deep from the floor | offset ≤ 0.10, Ø9.0 ± 0.1, 2.30 ± 0.10 | +0.100 (offset) | (−9.3129, 16.5955, −24.9400) | PASS (assumed: A-12, A-26) | A-12, A-26 |
| REQ-08 | four Ø4.000 bores at (±44, ±44), offset 0.000 mm | offset ≤ 0.10 | +0.100 | (44.0000, 44.0000, −24.9400) | PASS (assumed: A-18) | A-18 |
| REQ-09 | outer radius 43.100 mm at every 5° over z −19.0…+3.0 (72 × 220 rays); inner max 37.100 in the gaps; wall 6.000 mm | ≥ 43.05 / ≤ 37.15 / ≥ 5.9 | +0.050 | (43.1000, 0.0000, −18.9500) | PASS (assumed: A-21) | A-21 |
| REQ-10 | 23 poses, rim z −5.000 → −11.650 at the insertion clock: 0.8239 → 0.4970 mm | ≥ 0.30 at every pose | +0.197024 | (−3.3115, 31.5065, 0.0000) | PASS (assumed: A-19) | A-19 |
| REQ-11 | Ø26 bore length 5.000 mm | 5.00 ± 0.10 | +0.100 | (0.0000, 0.0000, −24.9400) | PASS (assumed: A-10) | A-10 |
| REQ-12 | not a geometric gate: the OD-T01 bench test answers it | 15 bar on a Ø51 basket (3.06 kN) | — | — | INCONCLUSIVE | A-21 |
| REQ-13 | two Ø9.000 through-holes at r 15.500, θ 359.5° / 179.0°, offset 4.1e−07, through = 1 | Ø9.0 ± 0.1, offset ≤ 0.10 | +0.100 | (15.4994, −0.1353, −24.9400) | PASS (assumed: A-11) | A-11 |
| exactly_one_solid | 1 | = 1 | 0 | — | PASS | — |
| feature_census | planes 40, cylinders 30 (23 concave, 9 convex), tori 7, B-splines 15, other 0, bores 15; every counted feature at the spec's count | = the spec's counts | 0 | — | PASS | — |
| envelope_within_spec | size 100.0000002 × 100.0000002 × 28.2400002 mm; position min (−50.0000001, −50.0000001, −24.9400001), max (50.0000001, 50.0000001, 3.3000001) | size in [spec ± 0.1]; position apart | +0.0999998 | — | PASS | — |

**The census, item by item** (U-05, `bore_census` and `locate_bore` on the
re-imported STEP): Ø26.0 × 5.00 through ×1; Ø9.0 × 5.00 through ×2 (pair-A
pass-throughs, each merged with the Ø26 opening into one keyhole lobe over 262° of
its own circle); Ø9.0 × 2.30 blind ×2 (pair-B recesses from the floor); Ø3.8 × 2.70
through ×2 (pair-B screw holes); Ø4.0 × 5.70 through ×4 (carrier inserts). Lugs,
stop blocks and pockets are counted from the material each puts on a located ray:
31.68 at start + 27° and z −3.0 for the three lugs, 31.68 at z −9.0 with 37.10 at
z −11.0 at start + 2.9° for the three stop blocks, 35.10 at z −16.0 with 31.70 at
z −17.6 at start + 26.75° for the three pockets.

**The three ear tops, lug by lug** (a located diagnostic, not a gate). Spec §5
U-03(a) names one designed-contact pair, "the three ear tops on the lug undersides",
and gates it at `clearance = 0`; that pair row is the gated one above and reads
0.0000 mm. The same distance measured against the housing cut into its three lug
sectors reads **lug 1 0.0000**, **lug 2 0.03936**, **lug 3 0.0000** mm. The three
cannot all be 0 at one pose: A-25 puts OD-G10's ears at 120.5 / 120.5 / 119° while
§4 C1 puts the housing's lugs at a symmetric 120° pitch, so one ear stands off by
the pitch error. §9 carries this.

**The lock path (U-03(b), L-09, L-10)**, 43 poses in three legs, each pose carrying
the travel it still has to make:

| Leg | Poses | Swept | Clearance |
|---|---|---|---|
| insertion, at the insertion clock 122.5° (ears centred in the gaps) | 23 | rim z −5.000 → −11.650 | 0.8239 → 0.4970 mm, falling monotonically; the nearest point is the portafilter's drafted outer wall against the lug 2 start corner at r 31.68, z 0.000 |
| rotation, at rim z −11.650 | 14 | clock 122.5° → 60.26° | 0.5085 → 0.5113 (the same wall against the lug inner faces) → 0.2765 mm at the stop |
| seating, at the locked clock | 6 | rim z −11.650 → −11.200 | 0.2765 → 0.0000 mm, the ear tops onto the lug undersides |

The only poses under 0.30 mm are the last rotation pose (0.2765 mm, the ear leading
edge 0.5° short of the stop block as A-14 places it, 0.45 mm of travel from the
final pose) and the seating leg, both inside the 0.5 mm of approach spec §5 U-03(b)
exempts, where it asks for ≥ 0. The rotation depth (0.45 mm below the locked pose)
is a derivation, recorded in §8.

## 4. Robustness sweep (D7)

Every run rebuilds the part, exports its STEP into `01_CAD/sweep_v02/` (never into
`02_STEP_STL/`) and runs the same predicates of `check_od_g01_housing_v02.py` on the
re-imported file: the geometric rows on every case, and the rows that need OD-G10 as
placed (U-03, REQ-10) on the cases that can move the ear passage. **All 40 runs
built exactly one valid solid, and every geometric row passed in every run.** The
sweep walks the same three-leg lock path more coarsely than the delivered STEP does
(25 poses against 43), so the "at least 40 poses" part of U-03(b) is asserted only
on the delivered STEP; the clearances along the path are gated in both.

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

**What the sweep found.**

- **The geometry is robust over every band.** No REQ row and no process row leaves
  its limit anywhere in the 40 runs. The two −0.0000 margins are values modelled
  exactly at a limit — `lug_inner_r` at REQ-01's low end and `plate_t` at U-02's
  `size_z` limit — and they pass inside GATES §0's 0.005 mm band; anything past
  those bands fails them. D-05b's +0.0000 is the same thing by construction: A-17's
  5.70 mm insert hole in a 5.00 mm slab plus a 0.70 mm boss has no depth to spare,
  and no swept parameter changes it.
- **U-03's 0.20 mm probe fails in every run that places OD-G10**, for the reason of
  §10 and by about the same amount. The −Z reading runs from **0.1382 mm**
  (`lug_starts_hi`, +0.25° on all three lug starts) through 0.1488 mm at nominal to
  **0.1559 mm** (`lug_starts_lo`); `lug_inner_r` moves it between 0.1475 and 0.1500.
  The +Z reading is 0.0000 mm in every one of them. No fit-critical parameter inside
  its band carries the row.
- **The lug underside is the one lever, and A-05's own ±0.3 bracket overshoots it.**
  At `under_knots` −0.3 the −Z probe reads 0.0000 (the ears press 0.35 mm into the
  lugs); at +0.3 it reads 0.2765, but the designed contact has opened to 0.2486 mm,
  so the ear tops no longer touch the lug undersides at the locked pose and U-03(a)'s
  contact row fails instead. The value that satisfies both is +0.051, measured in
  `01_CAD/probe_contact_v02.json` and offered as option 2 of §10.
- **The lock path stays clear in every run that walks it.** No case puts a pose
  under 0.30 mm outside the 0.5 mm of approach spec §5 U-03(b) exempts.

## 5. Build facts

- Envelope 100.0000002 × 100.0000002 × 28.2400002 mm, from min (−50.0000001,
  −50.0000001, −24.9400001) to max (50.0000001, 50.0000001, 3.3000001); volume
  90 216.792 mm³; mass 96.532 g at 1070 kg/m³ (A-15, reported, not gated); centre of
  mass (−0.0026, −0.0020, −15.9444) mm.
- Fillets, requested → achieved: four carrier boss roots **R 1.0 → R 0.6** (R 1.0
  and R 0.8 each failed; the boss stands only 0.70 above the floor); the
  shelf-to-bore concave circle **R 0.8 → R 0.8** (first rung); the seven lug root
  edges **R 0.6, 0.5, 0.4, 0.3 → none achieved**, those edges stay sharp (OCCT
  refuses every rung where a lug side face meets the bore wall beside the lofted
  underside). No §5 row reads those edges. A failed rung edits the shape it is
  handed, so every ladder runs on a copy and a ladder that finds no radius returns
  the untouched part.
- Placements, every frame from a measured feature of the mating part, never a
  bounding box (L-02), and every position below read back off the placed solid
  (`01_CAD/probe_placed_v02.json`). **OD-G04**: its own plate back face (its z = 0)
  and its tab 1 centre (its report measures −3.3°) → rotate +6.05° about Z,
  translate z −6.82, so its flange bottom face (its z −13.12) lands on the floor
  z −19.94. Measured on the placed solid: envelope z −22.940 … −5.730, tab centres
  at 2.75° / 122.75° / 242.75° with a tab tip radius of 34.5191 at z −15.50, bead
  31.1763 at z −15.17, pair A reaching z −22.940 and spanning r 12.01 … 18.99, pair
  B reaching z −21.700, hub bottom −22.550 with OD 20.06. **OD-G10**: its cup rim
  end face (its z = 0) and its ear 1 centre (59.5° from the handle) → 180° about +X,
  then +60.26° about Z (locked) or +122.5° (insertion), then the rim face to the
  pose's z. Measured: at the locked pose min_z −11.200 with ear centres at 0.76° /
  119.76° / 240.26°, which are the three lug engagement spans; at the insertion pose
  min_z −11.650 with ear centres at 63.0° / 182.0° / 302.5°, which are the three gap
  centres.
- The check assembly STEP holds the three parts as placed, labelled
  `od_g01_housing`, `od_g04_brewing_gasket_support`, `od_g10_portafilter`.

## 6. Plausibility (§P, D6)

| # | Question | Answer, from the six sections |
|---|---|---|
| P1 | Gravity | Yes: the rear slab is the mounting flange and four M3 inserts at (±44, ±44) take it to OD-C05; the three lugs hang over the ears and the brew load runs ears → lug undersides → cup wall → slab → carrier, one continuous section in the front and lug-underside cuts. |
| P2 | Function chains | Yes: water enters OD-G04's hub tube through the Ø26 opening, which now runs straight through the 5.00 slab to the rear face; the two OEM screws run from the rear through the Ø3.8 holes into pair B, and OD-G04's pair A passes the two Ø9 lobes — all visible in the top section, where the Ø26 circle and its two lobes read as the OEM keyhole. |
| P3 | Motion | Yes: the portafilter enters along −Z through three 66° gaps and turns 62.24° to the stop blocks; measured clearance stays ≥ 0.4970 mm over the whole insertion and rotation and closes to 0 only on the final 0.45 mm of seating (§3). |
| P4 | Human factors | Yes: one opening, one insertion direction, three ears into three gaps with a stop block that ends the turn; screws, inserts and the water connection are all reached from the flat square rear face. |
| P5 | Absurdity next to a real product | No: as a Ø86.2 cup on a 100 mm square flange 28.24 tall, with a keyhole opening and two screw seats in the plate, it reads like the OEM group head it reproduces. The one thing a domain engineer would ask about is the 5.00 mm of slab now standing between the hub tube and the water connection (A-24), where the OEM has 2.50. |
| P6 | Nothing floating, embedded, mirrored or upside-down | Yes: one solid with every feature attached; lug 1 starts at 336° counter-clockwise as spec §2 fixes it, the mouth is at +3.30 and the rear face at −24.94, and the keyhole lobes sit at 359.5° and 179.0° against the pair-B recesses at 119.3° and 304.0°, which the top section shows. |

**What the sections show for D-03a and D-03b** (the reviewer's rows; listed, not
gated). Printed mouth up, six faces of the part face downward: the three lug
undersides — the shallow plane stands 2.5° from horizontal at the bore and 2.9° at
the lug inner radius, the ramp 29° and 33° at the same two radii, so both are under
the 45° limit — and the three stop-block bottoms at z −10.52, which are horizontal.
All six are supported by decision (A-22), and no other face of the part faces
downward. The shelf at −14.10, the three pocket floors at −17.30, the riser tops,
the slab top at −19.94, the four boss tops at −19.24, the two recess floors at
−22.24, the front face at +3.30 and the three lug top pads all face +Z; the lip
ring's step at z −17.70 faces +Z as well, because the lower lip wall (R 31.30)
stands inside the upper one (R 31.70); and the cup wall, the lug sides, the lip
walls, the riser, the keyhole, its two lobes, the recesses, the screw holes and the
insert bores are all upright. Nothing in the part bridges: the longest unsupported
horizontal span is zero.

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
boss-OD measurement (the second half of D-05a), a boss-root check (E-06), and a
local wall measurement (J-05 is answered from `radial_extent`'s own material
stretches on 288 rays around the four insert axes, a located B-rep measurement, with
the whole-part `min_wall` reported beside it). Two more stand from v01: no boolean
row can be gated against an input solid that reads `brep_valid = 0` (OD-G10, A-28),
and no tool in `tools/` repairs or re-sews such a solid.

Job code written this round, all in `01_CAD/` and none in the repository:
`build_od_g01_housing_v02.py`, `check_od_g01_housing_v02.py`,
`assemble_od_g01_check_v02.py`, `sweep_od_g01_v02.py`, `sections_od_g01_v02.py`,
`probe_g10_v02.py`, `probe_contact_v02.py`, `probe_oem_contact_v02.py`,
`probe_placed_v02.py`.

## 8. Deviations from the plan

**The WP-03 amendments (spec 1.1), still in force, and spec 1.2's changes on top of
them, built as the briefs state them:**

| Plan row | Built |
|---|---|
| F02 slab 4.00 | 5.00 thick, z −24.94 … −19.94; envelope z 28.24 |
| F05, F06 lip ring R 30.82 / R 31.33 | R 31.70 from the shelf z −14.10 down to −17.70, R 31.30 below it to the floor |
| F07 pockets, floor −16.80 between R 34.39 and the bore | a notch between the lip wall R 31.70 and a riser at R 35.10, floor z −17.30, open to the shelf (spec 1.2 §4 C1) |
| F10 keyhole | Ø26.0 straight through the 5.00 slab: spec 1.2 drops the rear counterbore WP-03 added, which is the feature that stopped v01 |
| F11 lobes (slots on θ 133° and 310°) | two Ø9.0 through-holes at r 15.5, θ 359.5° and 179.0°, each merging with the Ø26 opening into one keyhole lobe |
| F12, F13 OD-G04 insert bosses and Ø4.0 bores | two Ø9.0 × 2.30 recesses from the floor with Ø3.8 through-holes at r 19.03, θ 119.3° and 304.0° (REQ-07, D-04a): no inserts there, the OEM's own screws from the rear |
| F14, F15 carrier inserts | Ø4.0 × 5.70 from the rear face at (±44, ±44), with a 0.70 boss on the floor side |
| F09 lug underside | the OEM's two planes and nothing else: the shallow plane from (+7°, −6.57) to (+41.8°, −5.59) and one straight ramp to (+54°, −1.15). Spec 1.2 rejects v01's knots at +50° and +53°; the gate rays moved instead (REQ-03 at start + 1°, + 27°, + 40°; REQ-04 at start + 20° and + 47° with ±0.5 brackets) |
| §5 OD-G04 joint +4.74°, seat z −7.28 | +6.05° about Z, its plate back face at housing z −6.82, so its flange bottom rests on the floor |
| §6 U-03(a) | the contact list of spec 1.2: the ear tops on the lug undersides and OD-G04's flange bottom on the floor at `clearance = 0`; tabs, pair A, pair B, bead and hub at `clearance ≥ 0.5`; the OD-G10 boolean INCONCLUSIVE (A-28) |
| §6 REQ-10 at 0.8 | 0.30 over the insertion path |
| §6 census | spec 1.2's list, without the counterbore |

**Beyond those, this round differs from the plan as follows:**

1. **The scripts carry `v02` in their names.** The brief names
   `01_CAD/check_od_g01_housing.py` and `01_CAD/build_od_g01_housing.py`; those files
   are v01's and are hashed into REPORT v01, so overwriting them would break that
   record. Every script of this round is the same name with `_v02`, and the geometry
   outputs carry exactly the paths the brief names.
2. **Carrier boss OD 10.30, not the plan's 8.00.** J-05 asks for 3.0 mm of wall
   around a Ø4.0 hole, which is 10.0 across; the plan's 8.00 came from D-05a alone.
   Measured wall 3.1500 mm, material across 10.300 mm. Spec 1.2 §4 C1 adopts it.
3. **No mouth chamfer on the carrier insert bores** (plan F15). A 0.5 × 45° chamfer
   at the rear face shortens the Ø4.0 cylinder to 5.20 mm and fails D-05b's "depth
   ≥ 5.7 from the rear face" as `locate_bore` measures it. Built without it; measured
   5.7000 mm. Spec 1.2 §4 C1 adopts it.
4. **The lug root fillets are not achieved** (plan F18). The ladder 0.6 / 0.5 / 0.4 /
   0.3 mm found no radius on the seven edges where a lug side face meets the bore
   wall beside the lofted underside; they stay sharp. No §5 row reads them.
5. **The STL is meshed at 0.002 mm, not the plan's 0.01.** Asked for U-07's 0.01 the
   mesher's own sagitta measures over the row's limit on the lofted underside faces;
   at 0.002 it measures 0.0094356 mm with 135 024 triangles. The tolerance asked for
   and the angular tolerance both stay inside U-07's limits.
6. **REQ-09's outer profile uses a z step that avoids z = 0.0 exactly**: a ray at a
   lug side angle and at the lug top plane runs along two faces at once and cannot be
   read either side.
7. **U-03(b) is walked as a three-leg path, not as the plan's interpolation.** The
   plan's 45 poses interpolated between the insertion and locked poses turn the ears
   into the lugs before they are deep enough (v01 measured clearance 0 from its sixth
   pose). The path here is insertion at the insertion clock, then rotation at the
   rotation depth, then the seating rise, 43 poses, each carrying the travel it still
   has to make. **The rotation depth is a derivation**: 0.45 mm below the locked
   pose, which is deep enough that the ear tops turn clear of the lug undersides
   (0.399 mm by measurement, from the contact rim z of §10) and inside the 0.5 mm of
   approach spec §5 U-03(b) exempts, so the exempt part of the path is the seating
   leg and the last rotation pose.
8. **The three ear tops are gated as one pair and reported lug by lug.** The plan
   gates "the three ear tops ... as `clearance == 0`"; spec §5 names one
   designed-contact pair, and A-25's 120.5 / 120.5 / 119° ears cannot all reach a
   symmetric 120° lug pitch at one pose (measured: 0.0000 / 0.03936 / 0.0000 mm). The
   pair row is gated, the three are reported beside it (§3).
9. **The sweep's `lip_upper_r` range is ±0.05 (31.65 … 31.75), not the plan's
   ±0.08.** The U-05 pocket predicate, written at D3, recognises a pocket by material
   at r ≤ 31.75 below the pocket floor; at a lip wall of 31.78 it stops recognising
   them. That is a limit of the predicate, recorded in v01's sweep and repeated here
   rather than quietly widened.
10. **Four diagnostic probes beyond the plan's file list** (`probe_g10_v02.py`,
    `probe_contact_v02.py`, `probe_oem_contact_v02.py`, `probe_placed_v02.py`). None
    answers a gate; they are the measurements §5 and §10 quote.
11. The plan's §7 R1 and R2 (the OD-G04 overlap and REQ-10 at 0.8) are answered by
    the ledger rows the briefs quote: both now measure clear (0.000 mm³ and
    0.4970 mm).
12. **One fix cycle of the three was used, and it changed the check script, not the
    part.** The first run gated the three per-lug ear contacts and read lug 2 at
    0.03936 mm; the cycle moved those three to located diagnostics for the reason in
    item 8, and gave the sweep a flag that leaves U-03(b)'s "at least 40 poses" to
    the delivered STEP. Everything was then re-exported and re-measured from
    scratch; the STEP, the STL and the assembly STEP came out byte for byte the same
    (the writer is deterministic at a pinned timestamp) and every measured value is
    unchanged.

## 9. What I am least sure of

1. **The 0.051 mm between this housing's ear-top contact and the ledger's locked
   pose, and the direction of U-03(a)'s 0.20 mm probe** (§10). Two separate
   questions sit on top of each other: which way the probe moves, and whose number is
   wrong. The measurements say the probe's +Z drives OD-G10 into the designed
   contact, and that the OEM pair itself contacts 0.062 mm below the ledger's locked
   rim z. I have not moved either the underside (A-05) or the locked pose (A-14),
   because which of them is right is a fact about the OEM assembly.
2. **The three ear tops cannot all touch at one pose.** A-25's ear pitch (120.5 /
   120.5 / 119°) against §4 C1's symmetric 120° lugs leaves lug 2 standing 0.03936 mm
   off at the locked pose. If U-03(a) is meant as three separate contacts, the
   housing needs three different lug underside levels, which contradicts §4 C1; if it
   is meant as one pair, as it is gated here, then the bayonet loads on two lugs of
   three and REQ-12's bench test carries more than the ledger's 3.06 kN / 3 per lug.
3. **Everything that rests on OD-G10's boolean.** Its STEP is not a valid solid by
   `tools.core.validity` (A-28), so U-03(a)'s boolean at the locked pose is
   INCONCLUSIVE and will stay so for the reviewer. The distance evidence says the fit
   is right to 0.05 mm, but no boolean confirms it.
4. Smaller, all measured: D-05b's depth margin is 2.7e−15 by construction (A-17's
   5.70 hole in a 5.00 slab plus a 0.70 boss), which also means each insert bore
   breaks through the boss top and opens on the cup floor — the 5.7 mm insert fills
   it exactly, and nothing in §5 reads the opening, but it is a hole into the wet
   side; U-03(a)'s bead (+0.0237) and pair B (+0.040) margins are thin and move with
   A-09, A-12 and A-17; and the seven lug root edges are sharp.

## 10. Stop

**The gate that cannot be met: U-03(a), the 0.20 mm probe of the locked pose.**
Spec 1.2 §5 U-03 answers the OD-G10 pair by distance because the boolean is
INCONCLUSIVE (A-28), and asks for two readings at the locked pose: `clearance = 0`
at the three ear tops, and `clearance` in [0.19, 0.21] "with OD-G10 lifted 0.20
along +Z from the locked pose (an overlap would read below 0.19)". The first reads
0.0000 mm and passes. The second fails in both senses of the displacement:

| Row | Measured | Required | Margin | At |
|---|---|---|---|---|
| OD-G10 moved 0.20 along **+Z**, as the row writes it | **0.0000 mm** | in [0.19, 0.21] | −0.190 | (35.2699, −7.0355, −6.1997) |
| OD-G10 moved 0.20 along **−Z** | **0.14876 mm** | in [0.19, 0.21] | −0.041243 | (30.8737, −7.1018, −6.4512) |

**Why +Z reads zero.** The ears sit under the lugs, so the contact is an up-facing
ear top against a down-facing lug underside, and +Z drives one into the other.
Measured on this housing at the locked clock: the two solids stand clear at every
rim height below **−11.25103** and touch at every height above it (bisection on the
distance, 20 steps, `01_CAD/measured_v02.json`); the distance reads 0.14876 mm at
rim −11.400, 0.0000 mm at the locked rim −11.200 and 0.0000 mm again at rim −11.000.
The same reading on the OEM pair confirms the direction:
OD-G09 against OD-G10 reads 0.0000 mm at the locked pose lifted +0.20 and 0.13806 mm
at the same pose moved −0.20. The row's own parenthesis — "an overlap would read
below 0.19" — only works when the displacement opens the designed contact, and the
direction that opens it is −Z.

**Why −Z still reads 0.149.** This housing first meets OD-G10 at rim z −11.2510,
**0.0510 mm below** the ledger's locked rim z −11.20 (A-14), so a 0.20 mm opening
move reads 0.20 − 0.051.

**Nothing inside a spec §5 band moves it** (`01_CAD/probe_contact_v02.json`, each
row a rebuild and a fresh bisection):

| Change | First contact, rim z | Clearance at locked − 0.20 |
|---|---|---|
| `lug_inner_r` 31.58 (REQ-01 low) | −11.25232 | 0.14748 mm |
| `lug_inner_r` 31.68 (A-02 nominal, as built) | −11.25104 | 0.14876 mm |
| `lug_inner_r` 31.78 (REQ-01 high) | −11.24977 | 0.15002 mm |

REQ-01's whole band moves the contact 0.0025 mm of the 0.0510 mm needed. REQ-02
(the bore), REQ-04 (the underside brackets, ±0.5) and REQ-05 (the stop) do not touch
the contact height at all: the contact lies on the shallow plane at lug 1 + 11.1°,
whose level A-05 fixes.

**And the OEM pair fails the same row by more**
(`01_CAD/probe_oem_contact_v02.json`): OD-G09 against OD-G10 at the same locked
clock first touches at rim z **−11.26176**, 0.0618 mm below the ledger's locked
pose, and its own −0.20 probe reads **0.13806 mm**. The housing is 0.0107 mm nearer
the [0.19, 0.21] window than the OEM cup it is built to reproduce, so the 0.05 mm
sits in the locked pose, not in the housing.

**The options, each measured:**

| Option | Change | Measured | What it costs |
|---|---|---|---|
| as specified | — | +Z 0.0000, −Z 0.14876 | FAIL |
| 1 | read the probe in the direction that opens the designed contact (−Z), and retire A-14's locked rim z from −11.20 to this housing's own contact, −11.25104 | the probe then reads 0.20000 and the contact row stays 0.0000; no geometry changes | A-14 changes; the locked pose in the check assembly STEP moves 0.051 mm, and A-27's gasket compression is read from the same pose |
| 2 | read the probe along −Z, and raise A-05's lug underside by 0.051 mm at all three of its points | measured on a rebuild: first contact −11.20004, probe **0.19968 mm**, inside [0.19, 0.21] | §4 C1 and A-05 change: the underside stops reproducing the OEM's measured planes, and the OEM cup itself is then 0.062 mm away from the same pose. REQ-04's ±0.5 brackets still hold |
| 3 | widen U-03(a)'s window | — | a changed threshold, which is not the designer's to make |

Which of A-05 (the underside, measured off the scan) and A-14 (the locked rim z,
derived) is the one to move is a fact about the OEM assembly, not a design choice,
so it is not made here. The direction of the probe is the second question, and it is
answered by measurement above.

**Everything else is built and measured.** Of the 49 rows in §3, 40 pass, 3 fail
(all three on the one probe: the U-03 summary row and its two displacement rows) and
6 are INCONCLUSIVE — four for a `tools/measure` function that does not exist, one
for the OD-T01 bench test, and one because OD-G10's input STEP is not a sound solid.
The four rows that stopped v01 (D-01a, D-01b, D-06a, U-06) now pass: `min_wall`
reads 1.5300 mm at 25° opposition, at the web between the Ø26 hub opening and a
pair-B Ø9 recess, and 1.150 mm at the 45° opposition U-06 reads, at the lug ramp end
that A-05 and D-01b's stated reason predict.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-g01-group-head-housing",
 "part": "od_g01_housing",
 "tag": "v02",
 "spec_version": "1.2",
 "files": [
  {
   "path": "01_CAD/build_od_g01_housing_v02.py",
   "sha256": "68209698cc98d041d3ba5b9450646086130964f21cfce1814f0c7fc46efb3fb5"
  },
  {
   "path": "01_CAD/check_od_g01_housing_v02.py",
   "sha256": "31fe6c47380894a08ef046a7510f7b8cd883bf0b2b83e4f312961d59583d2127"
  },
  {
   "path": "01_CAD/assemble_od_g01_check_v02.py",
   "sha256": "8fa361df8073645ee2e1be6438d78c62dc545a0b47e58720f9e95936cbac066d"
  },
  {
   "path": "01_CAD/sweep_od_g01_v02.py",
   "sha256": "47d725aa0f2f540b4a0f8eea3400820fdb99d8eedbac376d1bdc12eeacb1db07"
  },
  {
   "path": "01_CAD/sections_od_g01_v02.py",
   "sha256": "c3147966b9a1cf469b112520d9d40989428019551b939a75861d1cd3ea631eb3"
  },
  {
   "path": "01_CAD/probe_g10_v02.py",
   "sha256": "17f238afdb1feb513ecf5f01e18c896c6a166d8d3e57df6ec10a6330dbe584db"
  },
  {
   "path": "01_CAD/probe_contact_v02.py",
   "sha256": "5b7f880b68556dc6fa71ae025dbdfc7101fa6887354fa6a9735f95e6670d009a"
  },
  {
   "path": "01_CAD/probe_oem_contact_v02.py",
   "sha256": "7a9723aad088af2fc1646b654118cda8cc5128f358372cbd6bdb5709a42e7e3f"
  },
  {
   "path": "01_CAD/probe_placed_v02.py",
   "sha256": "2c322c268c55f55320d05cc65df582a5900f91508d61f7847c2246ad25e12583"
  },
  {
   "path": "01_CAD/measured_v02.json",
   "sha256": "3ec1095a4c9d481e4d3bb600851887b788632baba0bdff26d5e416430c07b9c1"
  },
  {
   "path": "01_CAD/sections_v02.json",
   "sha256": "8ac2652ce8a8d77b8dece0738fd30c847517be545f045e43edfa90b5b8f6383f"
  },
  {
   "path": "01_CAD/probe_contact_v02.json",
   "sha256": "150bcd56744d949c34a2d5b22823e672ffdf0320b61a26e4a923b6a993fe8eb0"
  },
  {
   "path": "01_CAD/probe_oem_contact_v02.json",
   "sha256": "bb51b4f9008c8ae74fc0867cc51cef6ccc6984df9e65e79ed1dacff3dc6f818d"
  },
  {
   "path": "01_CAD/probe_placed_v02.json",
   "sha256": "725f807f7b323f0124a78c7c5b6d9412a89a2481b958ec0f6ee82a2fd66bbf6d"
  },
  {
   "path": "01_CAD/sweep_v02/sweep_v02.json",
   "sha256": "b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3"
  },
  {
   "path": "02_STEP_STL/od_g01_housing_C1_v02.step",
   "sha256": "f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02"
  },
  {
   "path": "02_STEP_STL/od_g01_assembly_C1_v02.step",
   "sha256": "8b9ce55fd306c63c99851656675d38bd0c002d17a1661d7001c1fc0fafb51c11"
  },
  {
   "path": "02_STEP_STL/od_g01_housing_C1_v02.stl",
   "sha256": "0e8fe8e265284ca76cff363dbbd2ab6df5c8485d8e4e8610f58ad29295f38cec"
  },
  {
   "path": "03_Sections/od_g01_housing_v02_front.png",
   "sha256": "e093e24a22505eec2a31579e039dc3eac4d000efa0505ec25fe4a79fa8de8d43"
  },
  {
   "path": "03_Sections/od_g01_housing_v02_top.png",
   "sha256": "257bfa6f80a0f0fc2ba23abf426116f99e03679532ab92c44b800f31d3d595cc"
  },
  {
   "path": "03_Sections/od_g01_housing_v02_left.png",
   "sha256": "d59834cb90d931630ce625423151969db9d61d5c71e7c9da3b4434b62266a875"
  },
  {
   "path": "03_Sections/od_g01_housing_stopblock_v02_front.png",
   "sha256": "42cbe97b09a9c2a5e9f99e8428c360edb8fd2220a0fcaf048140a6127103c146"
  },
  {
   "path": "03_Sections/od_g01_housing_lugunderside_v02_front.png",
   "sha256": "3c50912bd8b618c0f1a9a45c5a8f48487e8cd2217e77ba2f0646e81e4a35ff55"
  },
  {
   "path": "03_Sections/od_g01_housing_insertboss_v02_front.png",
   "sha256": "b2727c9912264d12197e1a746ba7c64c965f19d827bca0f84efffd708ff32137"
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
   "measured": 0.0,
   "unit": "mm",
   "required": "in [0.19, 0.21]",
   "margin": -0.19,
   "at": "(35.2699, -7.0355, -6.1997) mm",
   "status": "FAIL",
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
   "gate": "U-03 (a) od_g10 moved 0.20 along +Z",
   "measured": 0.0,
   "unit": "mm",
   "required": "in [0.19, 0.21]",
   "margin": -0.19,
   "at": "(35.2699, -7.0355, -6.1997) mm",
   "status": "FAIL",
   "assumes": [
    "A-13",
    "A-14",
    "A-19"
   ]
  },
  {
   "gate": "U-03 (a) od_g10 moved 0.20 along -Z",
   "measured": 0.14875708192189296,
   "unit": "mm",
   "required": "in [0.19, 0.21]",
   "margin": -0.041242918,
   "at": "(30.8737, -7.1018, -6.4512) mm",
   "status": "FAIL",
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
   "measured": 0.0,
   "unit": "mm",
   "required": ">= 0.0",
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
   "measured": 0.49702413154124403,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.197024132,
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
    37.15
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.19,
   "worst_case": "bore_r_lo"
  },
  {
   "parameter": "lug_inner_r",
   "values": [
    31.58,
    31.78
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.19,
   "worst_case": "lug_inner_r_lo"
  },
  {
   "parameter": "lug_span",
   "values": [
    53.75,
    54.25
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.19,
   "worst_case": "lug_span_lo"
  },
  {
   "parameter": "lug_starts",
   "values": [
    "low",
    "high"
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.19,
   "worst_case": "lug_starts_lo"
  },
  {
   "parameter": "stop_end_off",
   "values": [
    5.26,
    6.26
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.19,
   "worst_case": "stop_end_off_lo"
  },
  {
   "parameter": "stop_bottom_z",
   "values": [
    -10.82,
    -10.22
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.19,
   "worst_case": "stop_bottom_z_lo"
  },
  {
   "parameter": "shelf_z",
   "values": [
    -14.2,
    -14.0
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "shelf_z_lo"
  },
  {
   "parameter": "pocket_floor_z",
   "values": [
    -17.4,
    -17.2
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "pocket_floor_z_lo"
  },
  {
   "parameter": "pocket_riser_r",
   "values": [
    34.95,
    35.25
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "pocket_riser_r_lo"
  },
  {
   "parameter": "pocket_start_off",
   "values": [
    -5.5,
    -4.5
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "pocket_start_off_lo"
  },
  {
   "parameter": "pocket_end_off",
   "values": [
    58.0,
    59.0
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "pocket_end_off_lo"
  },
  {
   "parameter": "lip_upper_r",
   "values": [
    31.65,
    31.75
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "lip_upper_r_lo"
  },
  {
   "parameter": "lip_lower_r",
   "values": [
    31.25,
    31.35
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "lip_lower_r_lo"
  },
  {
   "parameter": "plate_t",
   "values": [
    4.9,
    5.1
   ],
   "all_built": true,
   "worst_gate": "U-02",
   "worst_margin": -2e-07,
   "worst_case": "plate_t_hi"
  },
  {
   "parameter": "keyhole_d",
   "values": [
    25.95,
    26.05
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "keyhole_d_lo"
  },
  {
   "parameter": "pair_b_r",
   "values": [
    18.98,
    19.08
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "pair_b_r_lo"
  },
  {
   "parameter": "carrier_xy",
   "values": [
    43.95,
    44.05
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "carrier_xy_lo"
  },
  {
   "parameter": "insert_d",
   "values": [
    3.98,
    4.02
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "insert_d_lo"
  },
  {
   "parameter": "insert_depth",
   "values": [
    5.7,
    6.0
   ],
   "all_built": true,
   "worst_gate": "U-01",
   "worst_margin": 0.0,
   "worst_case": "insert_depth_lo"
  },
  {
   "parameter": "under_knots",
   "values": [
    "low",
    "high"
   ],
   "all_built": true,
   "worst_gate": "U-03",
   "worst_margin": -0.248613365,
   "worst_case": "under_knots_hi"
  }
 ],
 "least_sure": [
  "U-03(a)'s 0.20 mm probe: this housing meets OD-G10 at rim z -11.25103, 0.051 mm below the ledger's locked rim z -11.20 (A-14), and the +Z the row names is the direction that drives OD-G10 into the designed contact. Which of A-05 (the underside) and A-14 (the locked pose) is the one to move is a fact about the OEM assembly.",
  "The three ear tops cannot all touch at one pose: A-25's 120.5 / 120.5 / 119 deg ears against a symmetric 120 deg lug pitch leave lug 2 standing 0.03936 mm off at the locked pose.",
  "Every row that rests on OD-G10's boolean is INCONCLUSIVE (A-28): its input STEP reads brep_valid 0 and no tool in tools/ repairs it.",
  "D-05b's depth margin is zero by construction, which also means each Ø4.0 insert bore breaks through its boss top and opens on the cup floor; U-03(a)'s bead (+0.0237) and pair B (+0.040) margins are thin; the seven lug root edges took no fillet."
 ],
 "stopped": true,
 "stop": {
  "gate": "U-03",
  "measured_mm": {
   "probe_plus_z": 0.0,
   "probe_minus_z": 0.14875708192189296,
   "first_contact_rim_z": -11.25103,
   "ledger_locked_rim_z": -11.2,
   "oem_pair_first_contact_rim_z": -11.261757,
   "oem_pair_probe_minus_z": 0.13806153806144053
  },
  "question": "Does U-03(a)'s 0.20 mm probe displace OD-G10 along -Z, the direction that opens the designed contact, and is the locked pose A-14's rim z -11.20 or this housing's own contact at -11.25103?"
 }
}
```
