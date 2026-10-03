<!-- Placed verbatim by the orchestrator from the designer hand-back: the harness refused the subagent write. Model name removed. -->
# REPORT — od_side_panels v01: OD-C13 right panel, OD-C12 left panel, OD-C16 bracket, check assembly (20261002-od-c12-c13-c16-side-panels)

Designer: Claude Code, designer doctrine · spec version 1.1 (SHA-256 121c01a1…c222, checked) · plan `01_CAD/DESIGN_PLAN.md` (SHA-256 83911646…1498, checked) as amended by spec 1.1 · package WP-03, J3, build attempt 1 of 2 · 2026-10-03 UTC

Resume note. A container restart stopped the first run of this package after the exports, checks, sections and sweep were written, but before the REPORT. This run did the following:
- Read every script and result, and checked every input hash against the brief.
- Re-ran the three part checks and the assembly check on the exported STEPs (`01_CAD/results_v01/rerun/`) and compared them row by row with the first run. They are identical: 131, 135 and 85 part rows and 199 assembly rows, with no status or value differences, and the assembly JSON is byte-identical.
- Checked the 15 section pictures: all match the hashes in `results_v01/sections_v01.json`.
- Confirmed that all 36 sweep builds and their checks are present.

Nothing was rebuilt or re-exported.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 83911646533081bdd7b41f52a15d45f295aad1c0f69f63fc03f13481131c1498 | J2 plan (spec 1.0), amended by spec 1.1 (§8) |
| `01_CAD/params_od_side_panels.py` | 46d85bfd03cdfe52e0a1dd8aef1448b69f2f5e34e5d61d6ee82d2599699e298d | one parameter structure (spec 1.1) |
| `01_CAD/build_od_c13_right.py` | fc30bca53e1f87c148415c05b98f01531ee34c315eeeb1be7787e60e5bba2940 | build plus shared export (AP242 via `tools.core`, STL) |
| `01_CAD/build_od_c12_left.py` | 34be8ebed1a5406a5bf9e810e30032159f700890a607fd338b2c28bf7865227a | mirror of OD-C13 plus relief |
| `01_CAD/build_od_c16_bracket.py` | 71be0d79785f2a3302d2ab3d374e5dde7ac51997e8dbbb4c0baef59dedfc9246 | bracket, own frame |
| `01_CAD/checklib_od_side_panels.py` | d1c4b1cc91fa968bbd19bad236c4e1b17c9cc90ff9c54ef29c00935e325eccfe | shared predicates, GATES §0 bands |
| `01_CAD/check_od_c13_right.py` | 47eaa97b08195ec71d76f2c07b60029f8201548c90d1ea5ced949297e8190c9f | checks, written before the build (D3) |
| `01_CAD/check_od_c12_left.py` | 021721f813f0ff941923465e657aa5bb8dfda9e7273b0a745eef3a9cb6e54c20 | checks, written before the build (D3) |
| `01_CAD/check_od_c16_bracket.py` | 90cb20e16bd71a048a9908f84644adc88cc7c5fbe62893bae33a8d70dedacc1c | checks, written before the build (D3) |
| `01_CAD/check_od_side_panels_assembly.py` | bdde1baa5a5dabb796b08eb13f81161e4c8c5fbc0f16a878ebe99396b6ec3ebe | U-03 (a)(b), REQ-05 at the poses, REQ-06, REQ-07 |
| `01_CAD/placements_od_side_panels.py` | 176c5b14fb3ae5e027b59e206a90978d6afb7688368e2ed72f081179003bd861 | §2 joints |
| `01_CAD/assemble_od_side_panels.py` | 24a97b3f614ab9b426251c0c42ac1237b1c5ff6c0644145c2cb80730cac83348 | check assembly writer |
| `01_CAD/sections_od_side_panels.py` | 19c5b0de2bdb066ff7716a1973b2d6e835bc98621fc10aec60f5d6953f51367a | D6 sections |
| `01_CAD/sweep_od_side_panels.py` | 42fd15c16bd6cf12a062bdcf82754f53a99926c951aee89af52eb3f91b7c225c | D7 sweep |
| `01_CAD/report_tables_v01.py` | 5fc49e3a598d73b56dc673d0269b2dd48bec8a4cd623301d279a9437c0ac7231 | result JSON to report tables |
| `01_CAD/measure_refs_v01.py` | 0cbd59b068fcd1fbff775a180eaa8564e7393a2b482f58a95df97df5571d5939 | D1 reference measurement |
| `01_CAD/results_v01/SHA256SUMS_v01.txt` | 04694a436776a3fd234c79f5d6ba48a5713cad291811270e6a144ebe8c179a92 | manifest of the 57 result files (every check row, re-run, export facts, sweep) |
| `01_CAD/results_v01/sweep_worst_v01.txt` | 97fe52565218ac9786219621ca9c8099e83f3cecbd6ce5e1d7f3cb0934778999 | worst sweep margin per part and gate |
| `01_CAD/sweep_v01/SHA256SUMS_v01.txt` | d746e42ca09843ca1bde375a3a2abefa1cf158e45c0005e9240dd4685d68cdba | manifest of the 108 sweep files (36 STEP, 36 STL, 36 facts) |
| `02_STEP_STL/od_c13_right_C1_v01.step` | bb029af485a12941c364302b8a2f98c5b9c2436f73aea68e66bb8ed69be11a71 | AP242, re-imported for every measurement |
| `02_STEP_STL/od_c13_right_C1_v01.stl` | 50beff9b3ddbc572d9020309e4c5e758830331a360c52d55ae1ca117d0dccf88 | tol 0.01 / angular 0.434074 rad (R_max 1.7), 536 triangles |
| `02_STEP_STL/od_c12_left_C1_v01.step` | 972343ab6af3684acf9000208761baa390e489cabe30d238c62ffa36e62f8408 | AP242 |
| `02_STEP_STL/od_c12_left_C1_v01.stl` | 872489a1afefcb39e725b3339595770184b17368deab05e7e9f1eaca66ee5d55 | tol 0.01 / angular 0.434074 rad, 552 triangles |
| `02_STEP_STL/od_c16_bracket_C1_v01.step` | 39faff6ce71326fc8d562d8c3daa42cd938fdf24f4dbe0933d82e9cae569c9fc | AP242 |
| `02_STEP_STL/od_c16_bracket_C1_v01.stl` | 0519dcb42e099fdc6433cc371989b0806ac74bd2e77aa7c43d3891c5ac6f19d5 | tol 0.01 / angular 0.313866 rad (R_max 3.25), 588 triangles |
| `02_STEP_STL/od_side_assembly_C1_v01.step` | aee5a94315143eb416bbe9111e5ef4a8e32e828ee70c522d6e015ac9fd7a58b7 | check assembly, 19 labelled solids |
| `03_Sections/od_c13_right_v01_top.png` | 5c24e60dbe490ef3ac99eb708a5d318178852a590fa9672210a540818bd0517f | z −100: wall, rail, lip; nothing clipped |
| `03_Sections/od_c13_right_v01_front.png` | 449fda210a8c7c8be9d672ae2cfbaef98d494ebcdae66ea3e76da9daf648026a | y 50 |
| `03_Sections/od_c13_right_v01_left.png` | d3d8b0bdfcced044b36584bfa3f32719c096f7481c7b9f0de0aa727cb6aa5df0 | x 118.5, holes |
| `03_Sections/od_c13_right_y200_v01_front.png` | c679b2d18e51aeb9cef2005a3d01546134658d45feeb2af53afa21ccbc1ed597 | y 200 |
| `03_Sections/od_c13_right_z-262_v01_top.png` | 3224bd3a8a074008be636fc38110cdef4b876f0f1579e2b6b69dcb8dd57c21d5 | rear hole |
| `03_Sections/od_c12_left_v01_top.png` | 1e381136a060b0ba10a12868494b1fe9c233afdab42124bc9d60a449851ece02 | z −100: relief, wall, rail, lip |
| `03_Sections/od_c12_left_v01_front.png` | 94ea164c4472e4f7fc1661659fdb0486d91799362e3915cee7cd92c76d33956e | y 30 through the relief |
| `03_Sections/od_c12_left_v01_left.png` | f528e1122567b109ab82f831caf5227837d8deb95ab11b84dc64e9e73745fa49 | x −118.5 |
| `03_Sections/od_c12_left_y200_v01_front.png` | c2c268e5c8db00436c1ba7fa170a6a64a300231f575af921edc34cae959c4138 | y 200 |
| `03_Sections/od_c12_left_z-15_v01_top.png` | 91569b9f02dab8831aca4fca0f393be3fce5904ef04d57a4876bb7e78f79f369 | middle hole |
| `03_Sections/od_c16_bracket_v01_top.png` | 57755b9b21108056a69f5efbf5026a8cf7ff4d4da33b5af605bddf30c1ca3f9c | z 0: counterbore, hole, insert bore |
| `03_Sections/od_c16_bracket_v01_front.png` | 48631aa47639915be66225c8f5ccaaec878c66f11f9450f480d675ac0b3238c5 | y 10, across the insert bore |
| `03_Sections/od_c16_bracket_v01_left.png` | ed25b09cd2d0ba6d016d22e9b227c4bb5e990f70465b1411b0457f10f35ae762 | x −3, insert-bore crown |
| `03_Sections/od_side_assembly_z-15_v01_top.png` | 70d51c9841ced6522ef61c05eda9477441edd7e023eb155dd19f959ad14bdbc7 | machine at z −15 |
| `03_Sections/od_side_assembly_z-262_v01_top.png` | 260f41a3008f50d7e60765780ae4b070171fffd08235f6de42a23a090890c2a0 | machine at z −262 |

All 15 sections: `nothing_clipped` = 0 (none clipped). Every row of every check, with its location and signed margin, is in `01_CAD/results_v01/check_*.json` and `01_CAD/results_v01/rerun/check_*.json`.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 · repo commit 10929db1408d89144bd4af9cad971440427933d0 (`tools.core`, `tools.measure`, `tools.drawing`, `tools.result`) · STEP timestamp pinned 2026-10-02T00:00:00

## 3. Gate self-check

Each status is the worst row for that gate and part. Bands are GATES §0: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. These are self-checks; no HARD gate is cleared until the reviewer has measured it.

### 3.1 OD-C13 right panel

| Gate | Measured | Required | Margin | Status | Assumes |
|---|---|---|---|---|---|
| exactly_one_solid | 1 | 1 | 0 | PASS | — |
| U-01 | solids 1, brep_valid 1, naked edges 0 | 1/1/0 | 0 | PASS | — |
| U-02 / envelope_within_spec size | 10.000 × 218.8105 × 385.000 | spec ± 0.1 | +0.0995 | PASS | — |
| U-02 position (apart) | x 110.000…120.000, y 0.000…218.8105, z −295.000…+90.000 | ± 0.1 | +0.0995 | PASS | — |
| U-03 | see 3.4 | | | PASS (assumed) | A-01…A-05, A-14 |
| U-04 | AP242, 1 solid, volume delta 1.6e-8 mm³, faces delta 0, label kept, valid after | | 0 | PASS | — |
| U-05 / feature_census | planes 11, cylinders 3 (concave 3), bores 3 along X, others 0 | 11/3/3 | 0 | PASS | — |
| U-06 (Soft) | 3.000 | ≥ 2.0 | +1.000 | PASS | — |
| U-07 | sagitta 0.0050; angular 0.434074 = 4·acos(1 − 0.01/1.7); delivered STL = fresh mesh (536 triangles, 1 body, 0 naked) | ≤ 0.01 | +0.0050 | PASS | — |
| U-08 | — | N/A by its row | — | N/A | — |
| D-01a / D-01b / D-06a | 3.000 mm | ≥ 0.8 / 2.0 / 1.0 | +2.2 / +1.0 / +2.0 | PASS | — |
| D-02 | 385.0 × 218.81 on the bed, 10.0 tall | ≤ 420 × 420 × 500 | +35.0 | PASS (assumed: A-09) | A-09 |
| D-03a | 60.000 deg, `overhang_census(build_dir=(−1,0,0))`; the lip slope is the only downward face | ≥ 45 | +15.0 | PASS | A-11 |
| D-03b | flat ceiling 0.000 (reviewer from sections) | ≤ 5 | +5.0 | PASS | A-11 |
| D-04a | 3.400 (×3) | ≥ 3.25 | +0.150 | PASS | — |
| D-04d | 0.400 | ≥ 0.30 | +0.100 | PASS (assumed: A-02, A-14) | A-02, A-14 |
| D-07 | — | N/A by its row | — | N/A | — |
| E-06 | 1 solid; lip, rail and wall one section (z −100) | reviewer | — | PASS (designer reading) | — |
| REQ-01 | outer face x 120.000 over z −295…+90; sections at y 50 and y 200 (7 stations each): outer 120.000, inner 117.000; one underside plane y 0.000; top face y 215.000 over x 116.600…120.000; square ends at −295.000 / +90.000; footprint outside plate 0.000 mm³ | ± 0.10 / ± 0.05 | +0.050 | PASS | A-01 |
| REQ-02 | wedge x 110.000…116.600, base y 215.000, apex (110.000, 218.8105), z −280.000…+80.000; slope 60.000 deg; gap 0.400; lid material in x 109.5…117 over the lip zone 0.000 mm³ | ± 0.1, 60 ± 1, 0.40 ± 0.05, 0 | +0.050 | PASS (assumed: A-02, A-14) | A-02, A-14 |
| REQ-03 | Ø3.400 ×3, offset 0.000, through, at (y 10, z −262/−15/+62) | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | PASS | — |
| REQ-04 | — | OD-C12 only | — | N/A here | — |
| REQ-08 (Soft) | not geometric; risk MEDIUM | first print | — | INCONCLUSIVE | A-13 |

### 3.2 OD-C12 left panel

| Gate | Measured | Required | Margin | Status | Assumes |
|---|---|---|---|---|---|
| exactly_one_solid / U-01 | 1 solid, valid, 0 naked | | 0 | PASS | — |
| U-02 / envelope_within_spec | 10.000 × 218.8105 × 385.000; x −120.000…−110.000, y 0…218.8105, z −295…+90 | ± 0.1 | +0.0995 | PASS | — |
| U-04 | volume delta 2.3e-8 mm³, faces 0, label kept, valid | | 0 | PASS | — |
| U-05 / feature_census | planes 15 (11 + 4 relief), cylinders 3, bores 3 along X | 15/3/3 | 0 | PASS | — |
| U-06 (Soft) | 2.100 (wall at the relief) | ≥ 2.0 | +0.100 | PASS | — |
| U-07 | sagitta 0.0050; angular 0.434074; 552 triangles, 1 body, 0 naked | ≤ 0.01 | +0.0050 | PASS | — |
| U-08, D-07 | — | N/A by their rows | — | N/A | — |
| D-01a / D-01b / D-06a | 2.100 mm | ≥ 0.8 / 2.0 / 1.0 | +1.3 / +0.1 / +1.1 | PASS | — |
| D-02 | 385.0 × 218.81, 10.0 tall | ≤ A-09 | +35.0 | PASS (assumed: A-09) | A-09 |
| D-03a | 60.000 deg, build_dir (1,0,0); relief opens upward | ≥ 45 | +15.0 | PASS | A-11 |
| D-03b | 0.000 | ≤ 5 | +5.0 | PASS | A-11 |
| D-04a | 3.400 ×3 | ≥ 3.25 | +0.150 | PASS | — |
| D-04d | 0.400 | ≥ 0.30 | +0.100 | PASS (assumed: A-02, A-14) | A-02, A-14 |
| E-06 | 1 solid (z −100 section) | reviewer | — | PASS (designer reading) | — |
| REQ-01 | as OD-C13, mirrored; stations inside the relief left to REQ-04 | | +0.050 | PASS | A-01 |
| REQ-02 | as OD-C13, mirrored; gap 0.400 | | +0.050 | PASS (assumed: A-02, A-14) | A-02, A-14 |
| REQ-03 | Ø3.400 ×3, offset 0.000, through | | +0.100 | PASS | — |
| REQ-04 | one floor face x −117.900 over y 0.000…55.000, z −160.000…−29.000; wall 2.100; clearance to OD-C07 0.900 | −117.90 ± 0.05; ± 0.1; ≥ 0.5 | +0.050; +0.400 | PASS (assumed: A-04) | A-04 |
| REQ-08 (Soft) | not geometric | | — | INCONCLUSIVE | A-13 |

### 3.3 OD-C16 bracket (own frame)

| Gate | Measured | Required | Margin | Status | Assumes |
|---|---|---|---|---|---|
| exactly_one_solid / U-01 | 1 solid, valid, 0 naked | | 0 | PASS | — |
| U-02 / envelope_within_spec | 19.000 × 16.000 × 16.000; x −19.000…0.000, y 0.000…16.000, z −8.000…+8.000 | ± 0.1 | +0.100 | PASS | — |
| U-04 | volume delta 7e-12 mm³, faces 0, label kept, valid | | 0 | PASS | — |
| U-05 / feature_census | planes 8, cylinders 3; bores: Ø3.4 along Y through, Ø6.5 along Y open at y 16 with floor at y 3, Ø4.0 along X open at x 0, blind | plan F21…F24 | 0 | PASS | — |
| U-06 (Soft) | 3.000 | ≥ 2.0 | +1.000 | PASS | — |
| U-07 | sagitta 0.0050; angular 0.313866 (R_max 3.25); 588 triangles, 1 body, 0 naked | ≤ 0.01 | +0.0050 | PASS | — |
| U-08, D-07 | — | N/A by their rows | — | N/A | — |
| D-01a / D-01b / D-06a | 3.000 at (−13.40, 3.0, −3.07), the counterbore floor | ≥ 0.8 / 2.0 / 1.0 | +2.2 / +1.0 / +2.0 | PASS | — |
| D-02 | 19 × 16 × 16 | ≤ A-10 | +201.0 | PASS (assumed: A-10) | A-10 |
| D-03a | planes 90.000 deg (no downward plane above the bed); the only cylinder not along Y is the insert bore; its crown reads 0.000 deg at (−6.0, 12.0, 0.0) and is the named exception | ≥ 45 outside the exception | +45.0 | PASS | A-11 |
| D-03b | crown bridge 4.000; flat ceilings 0.000 | ≤ 5 | +1.000 | PASS (assumed: A-11) | A-11 |
| D-04a | 3.400 | ≥ 3.25 | +0.150 | PASS | — |
| D-05a | 12.000 across the insert bore (`radial_profile`, 24 angles) | ≥ 8.0 | +4.000 | PASS (assumed: A-12) | A-12 |
| D-05b | Ø4.000, depth 6.000, blind, open at x 0 | 4.0 ± 0.05; 6.0 ± 0.1; ≥ 5.7 | +0.050 | PASS (assumed: A-12) | A-12 |
| J-05 | radial wall 4.000; axial web (bore floor to counterbore) 3.250. The global min_wall of 3.000 is reported alongside, not as a substitute | ≥ 3.0 | +0.250 | PASS | — |
| E-06 | 1 solid block | | — | PASS | — |
| REQ-05 (part) | block 19.000 × 16.000 × 16.000; Ø3.400 along Y at (−12.5, 0), offset 0.000, through; counterbore Ø6.500, offset 0.000, from y 16.000 to floor y 3.000, closed; insert bore Ø4.000 along −X from x 0.000 at (10, 0), offset 0.000 | ± 0.1, ≤ 0.10 | +0.100 | PASS | — |

### 3.4 Check assembly (rows on the parts as placed)

| Gate | Measured | Required | Margin | Status | Assumes |
|---|---|---|---|---|---|
| assembly file | 19 labelled solids, one each; equal to the part files placed by the §2 joints (max delta 1.3e-9) | equal | 0 | PASS | — |
| U-03 (a) contacts, 16 pairs (panels on OD-C01, panels under OD-C10, brackets on OD-C01, brackets on their panels) | clearance 0.000; interference 0.000 mm³ | = 0; ≤ 0 | 0 | PASS (assumed: A-01, A-02) | A-01, A-02 |
| U-03 (a) lip to OD-C10 | 0.400 each | 0.40 ± 0.05 | +0.050 | PASS (assumed: A-02, A-14) | A-02, A-14 |
| U-03 (a) all other pairs (100) | least 0.900 (OD-C12 to OD-C07); then 3.000 (panels to OD-C11), 5.000 (OD-C13 to OD-C08), 6.000 (panels to feet) | ≥ 0.5 | +0.400 | PASS (assumed: A-03, A-04, A-05) | A-03, A-04, A-05 |
| U-03 (a) coaxiality (6) | 0.000 | ≤ 0.10 | +0.100 | PASS | — |
| U-03 (b) brackets down from +20 (6 × 11 poses) | 0.000 mm³ | ≤ 0 | 0 | PASS | — |
| U-03 (b) panels inward from 20 outside (2 × 11 poses) | 0.000 mm³ | ≤ 0 | 0 | PASS | — |
| U-03 (b) OD-C10 down from +40 (21 poses) | 0.000 mm³ | ≤ 0 | 0 | PASS | — |
| REQ-05 (poses) | plate holes at (±104.5, z_c), offset 0.000 | ≤ 0.10 | +0.100 | PASS (assumed: A-01, A-07) | A-01, A-07 |
| REQ-06 | edge 15.500; existing OD-C01 hole 28.306; handed-over insert 22.142; Ø8 disc missing 0.000 mm³ (all six) | ≥ 8.0; ≥ 6.0; ≥ 6.0; 0 | +7.500 | PASS (assumed: A-01) | A-01 |
| REQ-07 | four foot keep-outs 0.000 mm³; six driver-access cylinders (r 4, y 16…215) 0.000; six panel-screw access cylinders (r 4, 20 outside) 0.000 | 0 | 0 | PASS (assumed: A-05) | A-05 |

## 4. Robustness sweep (D7)

All 36 low/high builds were exported to `01_CAD/sweep_v01/`, re-imported and checked with the same predicates. Every one is a single valid solid. There is no FAIL and no INCONCLUSIVE apart from the Soft bench row. Positions were moved together on the 0.10 circle along both diagonals (L-09). Readings at the band limits are −5e-7, which is inside the band.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| lip_outer_x (both panels) | 116.55 · 116.60 · 116.65 | yes | REQ-02 gap 0.450 / 0.350; D-04d 0.350 | 0.000 (at limit); +0.050 |
| lid path, high lip | — | — | U-03 (b) OD-C10 from +40 | 0.000 mm³ PASS |
| panel_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-03 at limits; D-04a 3.300 | 0.000; +0.050 |
| panel hole position | ±0.10 (both diagonals) | yes | REQ-03 offset 0.100; coaxial to nominal bracket 0.100 | 0.000 |
| relief_floor_x | −117.85 · −117.90 · −117.95 | yes | REQ-04 at limits; D-01b 2.050; OD-C07 clearance ≥ 0.850 | 0.000; +0.050 |
| br_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-05 at limits; D-04a 3.300 | 0.000; +0.050 |
| bracket hole position | ±0.10 | yes | REQ-05 hole/counterbore offset 0.100; plate holes at poses 0.100 | 0.000 |
| cbore_d | 6.4 · 6.5 · 6.6 | yes | REQ-05 at limits | 0.000 |
| cbore_floor_y | 2.9 · 3.0 · 3.1 | yes | REQ-05 at limits; D-01b 2.900 | 0.000; +0.900 |
| insert_bore_d | 3.95 · 4.00 · 4.05 | yes | D-05b at limits; D-03b 4.050 | 0.000; +0.950 |
| insert_bore_depth | 5.9 · 6.0 · 6.1 | yes | D-05b at limits; J-05 web 3.150 | 0.000; +0.150 |
| insert bore position | ±0.10 | yes | REQ-05 offset 0.100; D-05a 11.859; coaxial 0.100 | 0.000; +3.859 |
| **stack: panel hole +0.10, insert bore −0.10** | — | yes | U-03 coaxiality 0.200 (right), 0.141 (left) | **−0.100 FAIL in this case** |

`wall_inner_x` was not swept, because it is the designed contact plane of the §2 poses (plan note 1). Each part passes on its own at both ends of every band. Coaxiality passes at nominal and when only one part is off, but not when both parts sit at their worst in opposite directions (§9).

## 5. Build facts

- OD-C13: envelope 10.000 × 218.8105 × 385.000; volume 277 970.18 mm³; 344.7 g at 1240 kg/m³ (PLA, A-08).
- OD-C12: envelope 10.000 × 218.8105 × 385.000; volume 271 485.68 mm³; 336.6 g.
- OD-C16: envelope 19.000 × 16.000 × 16.000; volume 4 329.98 mm³; 5.37 g each, 32.2 g for six.
- Fillets: none planned and none made. The spec gives none, and adding any would change the U-05 census.
- Placements: §2 joints as `Location(Plane(origin, x_dir, z_dir))`, with right-handedness asserted and no bounding boxes.
  - OD-C01, C02, C08, C10, C11 and both panels: identity.
  - OD-C05: x→X, z→−Y at (0, 180.06, 32.0).
  - OD-C07: x→−Z, z→+Y at (−92, 0, −60).
  - OD-C15 ×4: x→X, z→−Y at (±110, −6, +90 / −295).
  - OD-C16 right side: x→X, z→Z at (117, 0, z_c). Left side: x→−X, z→−Z at (−117, 0, z_c). z_c ∈ {−262, −15, +62}.
  - Confirmed by measurement: contacts 0.000, coaxiality 0.000, plate holes 0.000.
- Print orientation (A-11): panels lie on their outer face, building −X (OD-C13) and +X (OD-C12). The bracket sits on its underside, building +Y.

## 6. Plausibility (§P, D6)

| # | Question | Designer's answer |
|---|---|---|
| P1 | Gravity | Yes. The panels stand on the plate top (contact 0.000). The lid's side skirts rest on the panel tops at y 215. The brackets sit on the plate. Nothing hangs from a screw alone. |
| P2 | Function chains | No airflow, liquid or drive passes through the panels. They are closed walls, 5.0 from the electronics tray and 3.0 from OD-C11, so OD-C11's vents remain the bay exhaust (A-08). No cable run crosses a new part. |
| P3 | Motion clearance | No moving parts. All three assembly paths read 0.000 mm³ at every 2.0 step. |
| P4 | Human factors | Yes. Screws go in from outside and from above along clear straight axes (access 0.000 mm³). The order brackets → panels → lid is the only order that fits. The proud button heads are covered by A-07. |
| P5 | Absurdity next to a real product | None. A 3 mm printed side wall with a top rail and a lid-locating lip is a common printed-enclosure side. A domain engineer would remark on the visible screw heads and on the ≈ 4 × 4 rear-corner opening (A-03). |
| P6 | Floating / embedded / mirrored / upside-down | None. Every designed contact reads 0.000, interference is 0.000 mm³, the left relief is on the inner face over OD-C07 (x −117.9), and the lips point up inside the skirt. |

## 7. Library and tools used

- Library card: UNO10 U5 tank heat-set (blind insert bore; keep size and position apart). Its mouth chamfer is not used.
- `tools.core`: read_step, write_step (AP242, D-024), step_roundtrip / compare_step, write_stl, validity, common_volume.
- `tools.measure`: envelope, feature_census, bore_census, locate_bore, min_wall (detail["wide"]), overhang_census, flat_ceiling_spans, clearance, radial_extent, radial_profile, mesh_census.
- `tools.drawing`: write_sections, with nothing_clipped.
- `tools.result`: gate, Result, inconclusive.
- New job code (under `01_CAD/` only): placement helper, assembly-path stepper, REQ-07 cylinders, J-05 / D-05a composition, coaxiality offset between two bore axes, sweep driver, report-table generator.
- No `tools/measure` function is missing, and no gate is INCONCLUSIVE for lack of a tool.

## 8. Deviations from the plan (the plan was written against spec 1.0; the build follows 1.1)

1. Q1: the lip is now a wedge on a rail at x 110…117. The lip triangle is (110, 215), (116.6, 215), (110, 218.81) over z −280…+80, with the apex derived as 215 + 6.6/tan 60° = 218.8105. The plan expected D-03a/D-03b to fail on the panels; they now read 60.000 deg and 0.000.
2. Q2: the panel ends are square, so the wall is a box x 117…120, z −295…+90. The arc profile, `end_arc_x` and the corner arcs are dropped. As a result:
   - The census changes: OD-C13 has 11 planes and 3 cylinders (plan 12/5); OD-C12 has 15 and 3 (plan 16/5).
   - The REQ-01 arc readings are replaced by square-end checks.
   - U-07's R_max becomes 1.7, so the angular tolerance is 0.434074 rad (plan 0.1789).
3. Q4: the relief floor is at x −117.9 (wall 2.1, ± 0.05), and its sweep is ± 0.05 (plan ± 0.10).
4. The envelopes follow 1.1: 10.0 × 218.81 × 385.0.
5. Added a check that there is no lid material in x ±(109.5…117) over the lip zone (brief, Q1). The slope is now read both from the face normal and by `overhang_census`.
6. The assembly STEP is named `od_side_assembly_C1_v01.step`, as the brief asks (plan: `od_side_panels_C1_v01.step`).
7. U-04 compares each export with the part rebuilt in memory.
8. Two cases added to the sweep: the opposite-direction coaxiality stack, and the lid path with the tightest lip.

## 9. What I am least sure of

1. **Coaxiality tolerance stack.** REQ-03 and REQ-05 each allow 0.10 of position, and U-03 allows 0.10 between the two axes. With both parts at their worst in opposite directions the offset reads 0.200 on the right and 0.141 on the left (nominal 0.000). In practice a Ø3.4 hole round an M3 screw floats 0.2 radially, so the screw still starts. Whether to split the bands (for example ± 0.05 each) is a spec decision; I did not change any gate.
2. **Lip gap.** The gap of 0.400 rests on A-02 and A-14: OD-C10's skirt inner face is assumed to be a straight plane at x ±117.000. The ± 0.05 lip sweep lands exactly on REQ-02's limits (0.350 / 0.450). Lowering the lid with the tightest lip reads 0.000 mm³.
3. **Panel min_wall sampling.** min_wall on the panels is sampled at 1.0 mm, the sampler's limit on a 385 × 215 face. It reads 2.1 and 3.0 exactly, but it does not report the lip wedge's 60° apex edge at (±110, 218.81). The reviewer should read that edge from the z −100 sections.

## 10. Stop

Not stopped. Fix cycles used: 0 of 3. Every Hard §5 row is PASS or PASS (assumed: A-##) on each part file and in the check assembly. U-08 and D-07 are N/A by their own rows. REQ-08 is Soft and INCONCLUSIVE (bench, A-13).

(JSON block: `{"schema":"oguz-report-v1","job_id":"20261002-od-c12-c13-c16-side-panels","part":"od_side_panels","tag":"v01","spec_version":"1.1","files": <§1 table paths and hashes>,"versions":{"python":"3.13.7","build123d":"0.11.1","ocp":"7.9.3.1","repo_commit":"10929db1408d89144bd4af9cad971440427933d0"},"gates": <the gates list above, per part, with measured/unit/margin/status/assumes from §3>,"sweep": <the §4 rows>,"least_sure": <§9 items 1-3>,"stopped":false}`. The fully expanded block exists in my draft and can be written out on request. Every value in it is the one shown in §3 and §4.)