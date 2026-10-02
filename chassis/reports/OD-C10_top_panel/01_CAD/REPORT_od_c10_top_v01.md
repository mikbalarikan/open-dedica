# REPORT — od_c10_top v01 (20261001-od-c10-top-panel)

Designer: Claude Code (Claude Agent SDK), claude-opus-5-5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` · 2026-10-01 UTC

Outcome: **STOPPED (D9)** on U-03 (a): OD-C11's wall top is touched over two areas at
the lid's rear corners, besides the one line §5 names as a designed contact. §4's
geometry forces this. Every other §5 row passes or is N/A or INCONCLUSIVE by its own
row. §10 gives the measured failure and the options. The OD-C11 reference is its
**unreviewed** build v02 STEP (that build stopped on its outer gussets and a feet-hole
margin; its wall, ledge and insert bores measured here are as its spec says, probe JSON).

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 0d0fc1a890e8431278bdd05ace29f67e8403dfa7a030ea4c36ce7c460171c0f7 | plan (D2), written before any geometry |
| `01_CAD/probe/probe_inputs_v01.py` | d33bb85f6da334f17afe84f1222a992b5241e63a477bc09fa595d9edc5c250ee | probe of the five references as placed |
| `01_CAD/probe/probe_inputs_v01.json` | 3a98e3cbba9874791dcce5a43f76278b6563cc2d36d41caf71200c112a7f239b | probe results |
| `01_CAD/probe/versions_v01.py` | 06ff355b92cf96f5b7388ad2c303837d84f9ec911ee1c8632e2438cf5ad81c6d | D0 versions |
| `01_CAD/build_od_c10_top.py` | fcd39277c772b39e5cffb9a5a2d9940e89208c51d74c717ac8b0b39099a32a5f | parametric script, every §4 value a named parameter |
| `01_CAD/check_od_c10_top.py` | 552739d24925a52940db07ad1caa5b4f13e8661e2839a5a2e50112415c951c50 | checks, written before the build (D3), corrected as §8 says |
| `01_CAD/build_record_v01.json` | 61569d261817da34b2749064f9ad75e21f8b834ea6198d6ba439e83cbc12d197 | build facts, STL settings, placements |
| `01_CAD/check_od_c10_top_v01.json` | ea4ac7fd33dc6bab94fd6f1abef6aea53ebbfdbf954e71379b04be0e1c890366 | every gate row and fact (242 rows) |
| `01_CAD/check_od_c10_top_v01.log` | 4946aa7217bf5d4e3c818e83821ebaa5e786d2b7ade2e9425ec5377432546146 | the check's printout |
| `01_CAD/sections_od_c10_top.py` | 652ef3c71fc1cf491abd1682d210ea5684e49ec42e257b184e001781eb0cbe8e | D6 sections |
| `01_CAD/sections_v01.json` | 49b94714e3466d9229f3041509586bd50241c525a23732262fe6d9fe8a84474d | section cut areas, nothing clipped = 0 for all 16 |
| `01_CAD/sweep_od_c10_top_v01.sh` | 642e9a7e614b891006e02f89e64356ce4c906286541e3d5daf33c43095ec8c60 | D7 sweep driver (17 runs into `01_CAD/sweep_v01/`) |
| `01_CAD/sweep_summary_v01.py` | a10fdcd0bd2eaf726c22e1197df7c37d2e1bf25dadc53190172d2e2f4796c0ab | sweep summary |
| `01_CAD/sweep_v01/sweep_summary.json` | a5cc8955aa98f885fc4db48a25fd9da034bca30c78f65bde028b57549b0daf18 | per run: rows not passing, worst margin per gate family |
| `01_CAD/report_tables_v01.py` | 62288a855087f7b12173bb1378a4b9f85add76458bdd3ff7967d07002bb2141d | generates §3 and the JSON gate rows from the check JSON |
| `01_CAD/report_rows_v01.json` | ba5e62cedfd987ed0d4d274b9360af4f144530c6761a2cb1d4fd602a87468928 | the JSON gate rows below |
| `02_STEP_STL/od_c10_top_C1_v01.step` | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | AP242 (`tools.core.write_step`), re-imported for every measurement |
| `02_STEP_STL/od_c10_assembly_C1_v01.step` | d5881320038a66454cfb9d8a2b89aba4ca38c4cc69cd9182cad4eb6a9ef3c9d9 | check assembly AP242: lid + OD-C01 + OD-C02 + OD-C05 + OD-C07 + OD-C11 as placed |
| `02_STEP_STL/od_c10_top_C1_v01.stl` | 2e3f1c736115fe1b6efca9110229357fca8c840fe8786f4b0ccced3e39d93bc9 | `tools.core.write_stl` (cached triangulation cleared); tolerance 0.01 mm / angular 0.17 rad; 5164 triangles; measured sagitta 0.00538 mm; mesh volume 433996.82 mm³; bbox x −120 … 120, y 210.5 … 250, z −305 … 100 (240 × 39.5 × 405) |
| `03_Sections/od_c10_top_cols_x65_v01_left.png` | 9e63029fa3a1a33ab21d16719e713ee1510d6c801fb7323e5e7fd3e55eee32ab | both bulkhead column axes |
| `03_Sections/od_c10_top_col_z-60_v01_top.png` | e146b098c66eb8a8ab67ffe37eb361b800fd7190fd692bdd5201e047bf6d3858 | bulkhead column (65, −60) axis and its two ribs |
| `03_Sections/od_c10_top_col_z-210_v01_top.png` | 2aa0f9576829183e7aef8caab96e0f2a6cf0226b9a4747377bf2c587e8aaa0ce | bulkhead column (65, −210) axis and its two ribs |
| `03_Sections/od_c10_top_cols_z-293_v01_top.png` | 128aa96e47bbea1176cea850e617f56a365291a18db34b58969291019e68e8bd | both rear column axes |
| `03_Sections/od_c10_top_col_x90_v01_left.png` | 464acc51c567575adcc4999a94586b1b2460691cb496cb345bc76b6d2478e209 | rear column (90, −293) axis, the pocket, the rear skirt |
| `03_Sections/od_c10_top_col_x-90_v01_left.png` | c3cbc6040f945fb77b8bd5b908c69a5a20f74e9b0c010c8d9262865bf0dc31ea | rear column (−90, −293) axis |
| `03_Sections/od_c10_top_rearrib_x94_v01_left.png` | 61e4bf68f172944a5426f3ef61ffddfac118a2178dabf2347c944d062b311a58 | a rear rib into the rear skirt |
| `03_Sections/od_c10_top_pads_z30_v01_top.png` | ebddc98b1be7b5a6882331365e8d8d171907474da89da592e092b39dc467bec6 | both pads, the headroom over the hub |
| `03_Sections/od_c10_top_plan_y230_v01_front.png` | bef87b584ef2298fa2bda237db2b370f9c94c4f44dc2f559129764f84cbd1afb | plan: skirt, columns, ribs, pads |
| `03_Sections/od_c10_top_holes_y216p5_v01_front.png` | 297f6b993b1e5837585c73f1189b248cf211c055856be56f7bea96f438b1664e | the four Ø3.4 holes |
| `03_Sections/od_c10_top_skin_y248p5_v01_front.png` | 0d578a5695b336da330ed0dfe723b40d44ef9de5b1894ee38bb85f1056aaff52 | the skin and the four counterbores |
| `03_Sections/od_c10_assembly_cols_x65_v01_left.png` | c6702fec12c6a21d010c0961dd8e07e3f8e69cacc1f0fc3258e94b949206d910 | bulkhead columns on OD-C02's rail |
| `03_Sections/od_c10_assembly_cols_z-293_v01_top.png` | 082ba947ac1d2a4730cd006dde741c8d22cbe428ba6713cfdede5531a7e26db6 | rear columns on OD-C11's ledge |
| `03_Sections/od_c10_assembly_pads_z30_v01_top.png` | b76a8149f36bb4dfed43d1f80a5ca4f2d50a9eaae9153fe4fff5584ee4b748c6 | pads 0.5 above OD-C05's plate |
| `03_Sections/od_c10_assembly_corner_z-300p5_v01_top.png` | c55987e90d7c4bce645c4248d145703d8653c6d1f4dfb7409e8eaceeb10e4e21 | rear corners: the skirt arcs over OD-C11's wall top (the stop) |
| `03_Sections/od_c10_assembly_corner_x113_v01_left.png` | eb7d44b9d4cb016737b8b8cad260922ab5097af70fd6817fc4a6d9771f1076db | through the +X corner contact patch |

The 3MF is the orchestrator's step. It needs: STL 5164 triangles, volume 433996.82 mm³
(B-rep 434010.64 mm³), bbox 240 × 39.5 × 405 mm (x −120 … 120, y 210.5 … 250, z −305 … 100).

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · tools venv as
pinned (`tools/uv.lock`) · repo commit 10929db1408d89144bd4af9cad971440427933d0

## 3. Gate self-check

These rows are generated from `01_CAD/check_od_c10_top_v01.json` (`report_tables_v01.py`),
measured on the re-imported STEP files. Band (GATES.md §0): mm 0.005, mm³ 0.001, deg 0.001,
rad 0.00002, counts and every other unit 0. A self-check clears no HARD gate.

Summary by §5 row:

| §5 row | Status | Measured (worst) |
|---|---|---|
| U-01 | PASS | 1 solid, brep_valid 1, naked edges 0 |
| U-02 | PASS | 240.000 × 39.500 × 405.000; position x −120 … 120, y 210.5 … 250, z −305 … 100 |
| U-03 | **FAIL** | (a) at the rear corners the lid touches OD-C11's wall top over 2 × 5.907 = 11.813 mm². With the named line contact and the column volumes set aside, `clearance_away` is 0.000 (required ≥ 0.5) at (−110.84, 215.0, −301.95). Every other part of (a) passes (§3 rows). (b) descent from +40 in 2.0 steps: 0.000 mm³ with every reference at every step |
| U-04 | PASS | part and assembly: AP242, solids 1 / 6, volume delta ≤ 1.1e-7 mm³, faces delta 0, labels kept, valid after |
| U-05 | PASS | 59 planes, 22 cylinders (12 concave, 10 convex), 0 other; 8 bores (4 Ø3.4 through, 4 Ø6.5 blind); 4 columns, 2 pads, 36 rib faces, 3 skin underside faces, 1 skirt bottom face |
| U-06 (Soft) | PASS | min_wall wide 2.750 |
| U-07 | PASS | tolerance 0.01, angular 0.17 ≤ 0.1789, sagitta 0.00538 (delivered) and 0.00538 (re-meshed from the re-imported STEP); 1 closed shell |
| U-08 | N/A | by its row |
| D-01a | PASS | 2.750 ≥ 0.8 |
| D-01b | PASS | 2.750 ≥ 2.0 (the column wall round the Ø6.5 counterbore, rear column (−90, −293)) |
| D-02 | PASS (assumed: A-09) | 240 and 405 ≤ 420 on the bed, 39.5 ≤ 500 tall |
| D-03a | PASS (assumed: A-08) | 90.0° with the four counterbores refilled by position (nothing downward); whole part 0.0° on the four floors only (the named exception, 4 × 24.104 = 96.415 mm²) |
| D-03b | PASS (assumed: A-08) | designer reading: widest flat ceiling 3.139 ≤ 5 (the four counterbore floors only, carried round their outer edge); the row is the reviewer's, from sections |
| D-04a | PASS | four holes Ø3.400 ≥ 3.25 |
| D-05a, D-05b, D-07, J-05 | N/A | by their rows |
| D-06a | PASS | 2.750 ≥ 1.0 |
| E-06 | INCONCLUSIVE (reviewer row) | designer evidence: one solid; 2 ribs per column found by position (12 bulkhead rib faces, 24 rear rib faces); the rear ribs run 1.0 into the rear skirt; pads and columns fused to the skin (sections) |
| REQ-01 | PASS (assumed: A-06) | one top face at y 250.000; skin 3.000 at five points |
| REQ-02 | PASS (assumed: A-04) | x ±120.000, z −305.000 / 100.000; corners R 10.000 at 12 rays; skirt 3.000 at the 4 corners and 12 side points; skirt bottom y 215.000 |
| REQ-03 | PASS (assumed: A-01, A-05) | columns Ø12.000, offset 0.000, bottoms y 215.000; holes Ø3.400 through, coaxial with OD-C02's inserts (offset 0.000); counterbores Ø6.500, floors y 218.000 |
| REQ-04 | PASS (assumed: A-02, A-05) | the same for (±90, −293) against OD-C11 v02's inserts (offset 0.000) |
| REQ-05 | PASS (assumed: A-03) | pads Ø10.000, offset 0.000, bottoms y 210.500; clearance to OD-C05 0.500; r from the hub axis 43.042 ≥ 40; edge to the nearest housing-screw counterbore 33.940 ≥ 20 |
| REQ-06 | PASS (assumed: A-06) | 0.000 mm³ in the box x ±42, y 200 … 247, z −70 … 70 |
| REQ-07 | PASS | counterbores Ø6.500, mouths at y 250.000; a Ø6.0 driver from 0.05 above each floor: 0.000 mm³ |
| REQ-08 (Soft) | INCONCLUSIVE | bench gate by its row (first print); risk in §9 |
| exactly_one_solid | PASS | 1 |
| feature_census | PASS | as U-05 |
| envelope_within_spec | PASS | sizes and position as U-02 |

Every row as measured:

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01.solid_count | 1 count | == 1 | 0 | — | PASS | — |
| U-01.brep_valid | 1 bool | == 1 | 0 | — | PASS | — |
| U-01.naked_edges | 0 count | == 0 | 0 | — | PASS | — |
| exactly_one_solid | 1 count | == 1 | 0 | — | PASS | — |
| U-02.size_x | 240 mm | in [239.9, 240.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_x | 240 mm | in [239.9, 240.1] | 0.1 | — | PASS | — |
| U-02.size_y | 39.5 mm | in [39.4, 39.6] | 0.1 | — | PASS | — |
| envelope_within_spec.size_y | 39.5 mm | in [39.4, 39.6] | 0.1 | — | PASS | — |
| U-02.size_z | 405 mm | in [404.9, 405.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_z | 405 mm | in [404.9, 405.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_x | -120 mm | in [-120.1, -119.9] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_x | 120 mm | in [119.9, 120.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_y | 210.5 mm | in [210.4, 210.6] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_y | 250 mm | in [249.9, 250.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_z | -305 mm | in [-305.1, -304.9] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_z | 100 mm | in [99.9, 100.1] | 0.1 | — | PASS | — |
| D-02.size_x | 240 mm | <= 420.0 | 180 | — | PASS (assumed: A-09) | A-09 |
| D-02.size_z | 405 mm | <= 420.0 | 15 | — | PASS (assumed: A-09) | A-09 |
| D-02.size_y | 39.5 mm | <= 500.0 | 460.5 | — | PASS (assumed: A-09) | A-09 |
| REQ-01.max_y | 250 mm | in [249.9, 250.1] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-02.min_x | -120 mm | in [-120.1, -119.9] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-02.max_x | 120 mm | in [119.9, 120.1] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-02.min_z | -305 mm | in [-305.1, -304.9] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-02.max_z | 100 mm | in [99.9, 100.1] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-01.top_faces | 1 count | == 1 | 0 | — | PASS (assumed: A-06) | A-06 |
| REQ-01.top_face_y | 250 mm | in [249.9, 250.1] | 0.1 | (-120.0000, 250.0000, -305.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x0_z-150 | 3 mm | in [2.9, 3.1] | 0.1 | (0.0000, 248.5000, -150.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x-100_z-100 | 3 mm | in [2.9, 3.1] | 0.1 | (-100.0000, 248.5000, -100.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x100_z0 | 3 mm | in [2.9, 3.1] | 0.1 | (100.0000, 248.5000, 0.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x0_z0 | 3 mm | in [2.9, 3.1] | 0.1 | (0.0000, 248.5000, 0.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x-80_z80 | 3 mm | in [2.9, 3.1] | 0.1 | (-80.0000, 248.5000, 80.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-02.corner_r.x110_z-295.a15 | 10 mm | in [9.9, 10.1] | 0.1 | (119.6593, 230.0000, -297.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z-295.a45 | 10 mm | in [9.9, 10.1] | 0.1 | (117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z-295.a75 | 10 mm | in [9.9, 10.1] | 0.1 | (112.5882, 230.0000, -304.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x110_z-295 | 3 mm | in [2.9, 3.1] | 0.1 | (117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z90.a285 | 10 mm | in [9.9, 10.1] | 0.1 | (112.5882, 230.0000, 99.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z90.a315 | 10 mm | in [9.9, 10.1] | 0.1 | (117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z90.a345 | 10 mm | in [9.9, 10.1] | 0.1 | (119.6593, 230.0000, 92.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x110_z90 | 3 mm | in [2.9, 3.1] | 0.1 | (117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z-295.a105 | 10 mm | in [9.9, 10.1] | 0.1 | (-112.5882, 230.0000, -304.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z-295.a135 | 10 mm | in [9.9, 10.1] | 0.1 | (-117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z-295.a165 | 10 mm | in [9.9, 10.1] | 0.1 | (-119.6593, 230.0000, -297.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x-110_z-295 | 3 mm | in [2.9, 3.1] | 0.1 | (-117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z90.a195 | 10 mm | in [9.9, 10.1] | 0.1 | (-119.6593, 230.0000, 92.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z90.a225 | 10 mm | in [9.9, 10.1] | 0.1 | (-117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z90.a255 | 10 mm | in [9.9, 10.1] | 0.1 | (-112.5882, 230.0000, 99.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x-110_z90 | 3 mm | in [2.9, 3.1] | 0.1 | (-117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+x.at0_-150 | 3 mm | in [2.9, 3.1] | 0.1 | (120.0000, 230.0000, -150.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+x.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (120.0000, 230.0000, 0.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+x.at0_60 | 3 mm | in [2.9, 3.1] | 0.1 | (120.0000, 230.0000, 60.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-x.at0_-150 | 3 mm | in [2.9, 3.1] | 0.1 | (-120.0000, 230.0000, -150.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-x.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-120.0000, 230.0000, -0.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-x.at0_60 | 3 mm | in [2.9, 3.1] | 0.1 | (-120.0000, 230.0000, 60.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-z.at-40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-40.0000, 230.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-z.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (0.0000, 230.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-z.at40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (40.0000, 230.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+z.at-40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-40.0000, 230.0000, 100.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+z.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-0.0000, 230.0000, 100.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+z.at40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (40.0000, 230.0000, 100.0000) mm | PASS (assumed: A-04) | A-04 |
| U-05.skirt_bottom_faces | 1 count | == 1 | 0 | — | PASS | — |
| REQ-02.skirt_bottom_y | 215 mm | in [214.9, 215.1] | 0.1 | (-120.0000, 215.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| U-05.plane_faces | 59 count | == 59 | 0 | — | PASS | — |
| feature_census.plane_faces | 59 count | == 59 | 0 | — | PASS | — |
| U-05.cylinder_faces | 22 count | == 22 | 0 | — | PASS | — |
| feature_census.cylinder_faces | 22 count | == 22 | 0 | — | PASS | — |
| U-05.concave_cylinders | 12 count | == 12 | 0 | — | PASS | — |
| feature_census.concave_cylinders | 12 count | == 12 | 0 | — | PASS | — |
| U-05.convex_cylinders | 10 count | == 10 | 0 | — | PASS | — |
| feature_census.convex_cylinders | 10 count | == 10 | 0 | — | PASS | — |
| U-05.cone_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.cone_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.sphere_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.sphere_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.torus_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.torus_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.bspline_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.bspline_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.other_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.other_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.bores | 8 count | == 8 | 0 | — | PASS | — |
| feature_census.bores | 8 count | == 8 | 0 | — | PASS | — |
| U-05.bores_d34_y_through | 4 count | == 4 | 0 | — | PASS | — |
| U-05.bores_d65_y_blind | 4 count | == 4 | 0 | — | PASS | — |
| U-05.column_cylinders | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.column_cylinders | 4 count | == 4 | 0 | — | PASS | — |
| U-05.pad_cylinders | 2 count | == 2 | 0 | — | PASS | — |
| feature_census.pad_cylinders | 2 count | == 2 | 0 | — | PASS | — |
| U-05.bulk_rib_sides | 8 count | == 8 | 0 | — | PASS | — |
| feature_census.bulk_rib_sides | 8 count | == 8 | 0 | — | PASS | — |
| U-05.bulk_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.bulk_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| U-05.rear_rib_sides | 16 count | == 16 | 0 | — | PASS | — |
| feature_census.rear_rib_sides | 16 count | == 16 | 0 | — | PASS | — |
| U-05.rear_rib_bottoms | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.rear_rib_bottoms | 4 count | == 4 | 0 | — | PASS | — |
| U-05.rear_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.rear_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| U-05.skin_under_faces | 3 count | == 3 | 0 | — | PASS | — |
| feature_census.skin_under_faces | 3 count | == 3 | 0 | — | PASS | — |
| REQ-03.x65_z-60.column_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (71.0000, 215.5000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.5000, -66.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (59.0000, 215.0000, -66.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.hole_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.hole_through | 1 bool | == 1 | 0 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| D-04a.x65_z-60.hole_d | 3.4 mm | >= 3.25 | 0.15 | (65.0000, 215.0000, -60.0000) mm | PASS | — |
| REQ-03.x65_z-60.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.cbore_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-60.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS | — |
| REQ-03.x65_z-60.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-60.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (65.0000, 250.0000, -60.0000) mm | PASS | — |
| REQ-07.x65_z-60.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-03.x65_z-210.column_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (71.0000, 215.5000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.5000, -216.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (59.0000, 215.0000, -216.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.hole_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.hole_through | 1 bool | == 1 | 0 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| D-04a.x65_z-210.hole_d | 3.4 mm | >= 3.25 | 0.15 | (65.0000, 215.0000, -210.0000) mm | PASS | — |
| REQ-03.x65_z-210.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.cbore_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-210.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS | — |
| REQ-03.x65_z-210.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-210.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (65.0000, 250.0000, -210.0000) mm | PASS | — |
| REQ-07.x65_z-210.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-04.x90_z-293.column_offset | 0 mm | <= 0.1 | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (96.0000, 215.5000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (90.0000, 215.5000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (84.0000, 215.0000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.hole_offset | 0 mm | <= 0.1 | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.hole_through | 1 bool | == 1 | 0 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| D-04a.x90_z-293.hole_d | 3.4 mm | >= 3.25 | 0.15 | (90.0000, 215.0000, -293.0000) mm | PASS | — |
| REQ-04.x90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.cbore_offset | 0 mm | <= 0.1 | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS | — |
| REQ-04.x90_z-293.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x90_z-293.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (90.0000, 250.0000, -293.0000) mm | PASS | — |
| REQ-07.x90_z-293.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-04.x-90_z-293.column_offset | 0 mm | <= 0.1 | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (-84.0000, 215.5000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (-90.0000, 215.5000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (-96.0000, 215.0000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.hole_offset | 0 mm | <= 0.1 | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.hole_through | 1 bool | == 1 | 0 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| D-04a.x-90_z-293.hole_d | 3.4 mm | >= 3.25 | 0.15 | (-90.0000, 215.0000, -293.0000) mm | PASS | — |
| REQ-04.x-90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.cbore_offset | 0 mm | <= 0.1 | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x-90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS | — |
| REQ-04.x-90_z-293.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x-90_z-293.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (-90.0000, 250.0000, -293.0000) mm | PASS | — |
| REQ-07.x-90_z-293.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-05.x48_z30.pad_offset | 0 mm | <= 0.1 | 0.1 | (48.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.pad_d_x | 10 mm | in [9.9, 10.1] | 0.1 | (53.0000, 220.0000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.pad_d_z | 10 mm | in [9.9, 10.1] | 0.1 | (48.0000, 220.0000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.pad_bottom_y | 210.5 mm | in [210.45, 210.55] | 0.05 | (43.0000, 210.5000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_offset | 0 mm | <= 0.1 | 0.1 | (-48.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_d_x | 10 mm | in [9.9, 10.1] | 0.1 | (-43.0000, 220.0000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_d_z | 10 mm | in [9.9, 10.1] | 0.1 | (-48.0000, 220.0000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_bottom_y | 210.5 mm | in [210.45, 210.55] | 0.05 | (-53.0000, 210.5000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-06.headroom_interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-06) | A-06 |
| D-03b.flat_ceiling_span | 3.1386 mm | <= 5.0 | 1.8614 | (66.5000, 218.0000, -60.8000) mm | PASS (assumed: A-08) | A-08 |
| U-03.seat.x65_z-60.c02.clearance | 0 mm | == 0.0 | 0 | (67.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x65_z-60.c02.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x65_z-60 | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-03.x65_z-60.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| U-03.seat.x65_z-210.c02.clearance | 0 mm | == 0.0 | 0 | (67.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x65_z-210.c02.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x65_z-210 | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-03.x65_z-210.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| U-03.seat.x90_z-293.c11.clearance | 0 mm | == 0.0 | 0 | (96.0000, 215.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x90_z-293.c11.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x90_z-293 | 0 mm | <= 0.1 | 0.1 | (90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-04.x90_z-293.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| U-03.seat.x-90_z-293.c11.clearance | 0 mm | == 0.0 | 0 | (-84.0000, 215.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x-90_z-293.c11.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x-90_z-293 | 0 mm | <= 0.1 | 0.1 | (-90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-04.x-90_z-293.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (-90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| U-03.c05.clearance | 0.5 mm | in [0.45, 0.55] | 0.05 | (-43.0000, 210.5000, 30.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c05.clearance_without_pads | 6.4031 mm | >= 0.5 | 5.9031 | (59.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c05.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-05.x48_z30.clearance_to_c05 | 0.5 mm | in [0.45, 0.55] | 0.05 | (53.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.clearance_to_c05 | 0.5 mm | in [0.45, 0.55] | 0.05 | (-43.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.hub_r | 43.0416 mm | >= 40.0 | 3.0416 | — | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.to_counterbores | 33.94 mm | >= 20.0 | 13.94 | (44.0000, 210.0000, -12.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.hub_r | 43.0416 mm | >= 40.0 | 3.0416 | — | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.to_counterbores | 33.94 mm | >= 20.0 | 13.94 | (-44.0000, 210.0000, -12.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03.c07.clearance | 167.2991 mm | >= 3.0 | 164.2991 | (-117.0000, 215.0000, -114.9500) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.plate.clearance | 210.5 mm | >= 3.0 | 207.5 | (-43.0000, 210.5000, 30.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c02.clearance_away | 14.3309 mm | >= 0.5 | 13.8309 | (70.8611, 229.3264, -208.5000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.clearance_line_contact | 0 mm | == 0.0 | 0 | (-110.0000, 215.0000, -302.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.clearance_away | 0 mm | >= 0.5 | -0.5 | (-110.8352, 215.0000, -301.9500) mm | FAIL | A-01, A-02, A-03 |
| U-03.c11.skirt_contact_area_off_the_line | 11.8133 mm2 | <= 0.0 | -11.8133 | [[[-116.0, -110.0], [-302.0, -299.0]], [[109.999999992409... | FAIL | A-01, A-02, A-03 |
| U-03(b).plate.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c02.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c05.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c07.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c11.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-04.part.schema | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.part.solids | 1 count | == 1 | 0 | — | PASS | — |
| U-04.part.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.part.faces_delta | 0 count | == 0 | 0 | — | PASS | — |
| U-04.part.labels | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.part.valid_after | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.schema | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.solids | 6 count | == 6 | 0 | — | PASS | — |
| U-04.assembly.faces_delta | 0 count | == 0 | 0 | — | PASS | — |
| U-04.assembly.labels | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.valid_after | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.od_c10_top.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c01_frame.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c02_bulkhead.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c05_carrier.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c07_valve_mount.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c11_back.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| D-01a | 2.75 mm | >= 0.8 | 1.95 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| D-01b | 2.75 mm | >= 2.0 | 0.75 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| D-06a | 2.75 mm | >= 1.0 | 1.75 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| U-06(Soft) | 2.75 mm | >= 2.0 | 0.75 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| D-03a | 90 deg | >= 45.0 | 45 | — | PASS (assumed: A-08) | A-08 |
| U-07.mesh.bodies | 1 count | == 1 | 0 | — | PASS | — |
| U-07.mesh.naked_edges | 0 count | == 0 | 0 | — | PASS | — |
| U-07.mesh.winding | 1 bool | == 1 | 0 | — | PASS | — |
| U-07.angular_tolerance | 0.17 rad | <= 0.17890034867493382 | 0.0089 | — | PASS | — |
| U-07.tolerance | 0.01 mm | <= 0.01 | 0 | — | PASS | — |
| U-07.max_sagitta | 0.0054 mm | <= 0.01 | 0.0046 | (-84.4084, 215.5000, -295.1609) mm | PASS | — |
| U-07.max_sagitta_delivered | 0.0054 mm | <= 0.01 | 0.0046 | — | PASS | — |
| U-08 | — | N/A | — | — | N/A | — |
| D-05a | — | N/A | — | — | N/A | — |
| D-05b | — | N/A | — | — | N/A | — |
| D-07 | — | N/A | — | — | N/A | — |
| J-05 | — | N/A | — | — | N/A | — |
| E-06 | — | reviewer | — | — | INCONCLUSIVE | — |
| REQ-08(Soft) | — | bench | — | — | INCONCLUSIVE | A-04, A-11 |

## 4. Robustness sweep (D7)

Seventeen runs into `01_CAD/sweep_v01/<run>/`: nominal plus low and high of each
fit-critical parameter. Each run rebuilds, exports, re-imports and runs the same
predicates, the descent (U-03 (b)) included. The two counterbore runs also run the wall
scan and the whole-part census. Every run built one valid solid with 81 faces. The two
U-03 C11 corner rows of §10 fail in every run except `skirt_bottom_y_hi` (there the patch
gap reads 0.100, still under 0.5). The table lists what else each parameter moves.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| hole_d | 3.3 · 3.4 · 3.5 | yes | D-04a (at 3.3) | +0.05 mm; REQ-03/04 hole_d at the band edge (0.000) |
| cbore_d | 6.4 · 6.5 · 6.6 | yes | D-01b / U-06 (at 6.6) | +0.70 mm (wall 2.70) |
| cbore_floor_y | 217.9 · 218.0 · 218.1 | yes | REQ-03/04 cbore_floor_y | 0.000 (band edge); REQ-07 driver path 0.000 mm³ |
| col_dx, col_dz | −0.1 · 0 · +0.1 | yes | REQ-03/04 column, hole and counterbore offsets; U-03 coaxial | 0.000 (offset 0.100 at the 0.10 limit) |
| col_bottom_y | 214.95 · 215.0 · 215.05 | yes | U-03 seats (designed contacts) | **passes only at nominal**: at 215.05 each seat reads clearance 0.050 (required = 0); at 214.95 each column overlaps its seat by 4.87 (OD-C02) and 5.03 mm³ (OD-C11) |
| pad_bottom_y | 210.45 · 210.5 · 210.55 | yes | REQ-05 / U-03 clearance to OD-C05 | 0.000 (0.450 and 0.550 at the band edges) |
| skirt_bottom_y | 214.9 · 215.0 · 215.1 | yes | U-03 OD-C11 | **passes only at nominal and only on the line contact**: at 214.9 the skirt overlaps OD-C11's wall by 1.181 mm³ (the corner patches × 0.1); at 215.1 the skirt stands 0.100 off OD-C11's wall, patches and line alike (`clearance_away` 0.100, still < 0.5); the whole-lid `U-03.c11.clearance_line_contact` row stays 0 there through the column seats, so it does not single out the line |

Designed contacts (clearance = 0) pass only at nominal. That is in the nature of a
contact row, not a weakness peculiar to this build. A column printed 0.05 short or long
seats the screw clamp all the same.

## 5. Build facts

- Envelope 240.000 × 39.500 × 405.000 mm; B-rep volume 434010.64 mm³; mass 551.2 g at
  1270 kg/m³ (PETG, A-10); centre of mass (0.98, 242.77, −105.21)
- Fillets: none in the spec, none built (the corner radii R 10 / R 7 are sketch arcs, not fillets)
- Placements (RigidJoint on the lid → each part's own frame, `build_record_v01.json`):
  OD-C01, OD-C02, OD-C11 at the identity; OD-C05 at Location(Plane(origin (0, 180.06, 32),
  x_dir (1, 0, 0), z_dir (0, −1, 0))), giving orientation (90, 0, 0), plate top measured at
  y 210.000; OD-C07 at Location(Plane(origin (−92, 0, −60), x_dir (0, 0, −1), z_dir
  (0, 1, 0))), giving orientation (−90, 0, 90), highest point measured at y 48.000. The local
  axes map as the brief states (probe `c05_axes`, `c07_axes`)
- Ribs (plan §4 derivations): bulkhead columns 2 × 2 triangular ribs along ±X, 3.0 thick,
  root y 222 on the axis, 20 along the skin; rear columns 2 × 2 ribs parallel to Z at
  x = xc ± 4.0, 3.0 thick, bottom y 216 (1.0 above OD-C11's ledge), from 1.0 inside the
  rear skirt to 20 in front of the axis

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The lid (551 g) stands on its four column bottoms, on OD-C02's rail and OD-C11's ledge, and on the rear skirt's bottom edge on OD-C11's wall. The pads hang 0.5 over the carrier and take a hand load only. Nothing rests on a free edge. |
| P2 | Function chains | The screw goes in from above through the Ø6.5 counterbore. Its head bears on 3.0 of column floor and its shank passes the Ø3.4 hole into an insert coaxial within 0.000. A hand pressing the skin goes to the pads, then to the carrier's plate after 0.5. |
| P3 | Motion clearance | The only motion is lowering along −Y onto the seats. Over 21 poses from +40 to 0 the overlap is 0.000 mm³ with every reference; the lid's inside clears the carrier by 37 over the hub. |
| P4 | Human factors | A Ø6 driver reaches every head unobstructed (0 mm³). The lid lifts off by its skirt. All four screws sit along the right-hand bulkhead line and the rear, so the left and front edges are free until the side and front panels exist (A-04). |
| P5 | Absurdity next to a real product | A 240 × 405 × 39.5 printed lid with 3.0 walls and screw bosses is ordinary for an espresso-machine top cover. The asymmetric screw layout (x 65 and the rear) is unusual but is what the spec asks. |
| P6 | Floating, embedded, mirrored, upside-down | One solid. Zero overlap with every reference. Not mirrored: the columns at x +65 sit on the bulkhead (x 59 … 71) and the rear pair on OD-C11's inserts at ±90. Not upside down: the top face is at y 250 and the columns hang down. |

## 7. Library and tools used

- Cards: none read; nothing in `library/INDEX.md` matched (finding, plan §2).
- `tools.core`: `read_step`, `write_step` (AP242, pinned timestamp), `write_stl`,
  `validity`, `compare_step`, `common_volume`. `tools.measure`: `envelope`,
  `feature_census`, `bore_census`, `locate_bore`, `clearance`, `radial_extent`,
  `min_wall` / `min_wall_wide` (spacing 0.7: the default refuses the large skin face, as
  the brief says), `overhang_census(build_dir=(0, −1, 0))`, `flat_ceiling_spans`,
  `mesh_census`, `mass_properties`. `tools.drawing.write_sections` (nothing clipped = 0
  on all 16 pictures).
- New job code (in `01_CAD/`, none in the repo): counterbore refill by position for
  D-03a; exclusion volumes on the measured column axes, pads and rear skirt for U-03 (a);
  the contact patches by face intersection; references cropped to x ±125, y 200 … 300,
  z −310 … 105 (it holds the lid's whole swept box, y 210.5 … 290) for the clearance and
  descent booleans; the REPORT table generator.
- Tool finding: in `tools/measure/wall.py` `min_wall`, the name `found` is reused inside
  the sample loop for the ray hit (a 4-tuple). `detail["solids"]` then reports 4 on this
  one-solid part. The scan iterates the original list, so the measured wall stands; only
  the count in detail is wrong. Not changed (not this role's code).

## 8. Deviations from the plan

1. Check script, before any gate was recorded: the column-diameter rays started their
   window at r 2.5 and crossed the hole-wall material (1.7 … 6.0), so they read
   INCONCLUSIVE. The window now starts on the axis and stops at r 8.5. No geometry change.
2. Check script, after the first sweep (**fix cycle 1 of 3**, check only, no geometry
   change, nothing re-exported). The sweep showed three predicates that read the nominal
   position instead of the part as built:
   - the rib-face selection and the U-03 (a) column exclusion volumes now follow the
     measured column axes;
   - the seat interference rows now measure the column piece, not the whole lid;
   - the REQ-07 driver now runs from 0.05 above each counterbore's measured floor on its
     measured axis.
   The nominal check and the whole sweep were then re-run. All the numbers above are
   from the corrected script.
3. The census counts in plan §3 held exactly (81 faces). The plan's rib description held.
   Nothing else deviates.
4. Known limit of the check, not changed: `U-03.c11.clearance_line_contact` is the whole lid's
   clearance to OD-C11, which the rear column seats also hold at 0. The line is shown by
   that row's nearest point at nominal and by the contact-face intersection (its
   patches), not by a row of its own.

## 9. What I am least sure of

1. **U-03 (a) at OD-C11's wall corners (the stop).** The reading here is strict: the
   rear skirt's corner arcs lying on the wall top over 11.81 mm² is contact off the
   named line. Someone could read "the rear skirt meets OD-C11's wall top" as covering
   the patches. That is the Usta's call (§10), not mine. The reference is also OD-C11's
   unreviewed v02; if OD-C11's wall changes, the patches change with it.
2. **Stiffness (REQ-08, A-11).** A 3.0 PETG skin 240 × 405 held at x 65 and along the
   rear only, its left and front edges free until OD-C09/C12/C13 exist. The left half
   overhangs about 185 mm beyond the bulkhead line with only the 32 mm skirt for depth,
   and the pads support only over the carrier. Sag and rattle risk at the free left-front
   corner: HIGH until the side and front panels land.
3. **The ribs are my design choice.** Their size and placement are derived in plan §4
   from the spec's 3.0 thickness and the clearances; no load case sizes them. The rear
   ribs leave a closed 5.0-wide pocket behind each rear column (open toward OD-C11's
   ledge). It prints, but it traps dirt. The reviewer should judge E-06 from
   `od_c10_top_col_z-60_v01_top.png`, `od_c10_top_plan_y230_v01_front.png` and
   `od_c10_top_rearrib_x94_v01_left.png`.

## 10. Stop

**Gate:** U-03 (a), Hard: "panel to OD-C02 and OD-C11 away from the column bottoms
≥ 0.5, except the rear skirt's bottom inner edge (y 215, z −302), which meets the top
outer edge of OD-C11's wall along x ±116 as a designed line contact".

**Measured:**
- `U-03.c11.clearance_away` = **0.000 mm** (required ≥ 0.5, margin −0.5) at
  (−110.84, 215.0, −301.95). This is the lid less its four column volumes (r 6.05) and
  less the rear skirt behind z −301.95, against OD-C11.
- `U-03.c11.skirt_contact_area_off_the_line` = **11.813 mm²**: two patches of 5.907 mm²
  each, at x 110 … 116 and x −116 … −110, z −302 … −299, y 215. There the skirt's
  bottom face lies on OD-C11's wall top.
- The line contact itself: whole-lid clearance to OD-C11 0.000, nearest point (−110.0, 215.0, −302.0) on the line, interference 0.000 mm³. That row is the whole lid's least distance, so the column seats would also hold it at 0 (§8 item 4).
- With the rear skirt and its corner arcs (z ≤ −295) set aside, the clearance is 3.000.
  So the patches are the only shortfall.

**Why it cannot be met inside spec 1.1:** the lid's corners are R 10 about (±110, −295)
(§4, REQ-02 ± 0.1). The skirt is 3.0 thick all round (REQ-02), so its inner corner is
R 7 about the same centre. Its bottom is y 215.00 ± 0.10 (REQ-02). OD-C11's wall top is
y 215 over x ±116, z −302 … −299. Wherever r from the corner centre is between 7 and 10
inside that rectangle, the skirt sits on the wall: the region x 110 … 116 where r ≥ 7,
about 5.9 mm² per corner. A thinner skirt there breaks REQ-02's 3.0. A raised bottom
there breaks REQ-02's y 215. The sweep confirms it: at a skirt bottom of 215.1 the
patches still read 0.100, and at 214.9 they overlap by 1.18 mm³.

**Options:**
1. **Spec 1.2 names the patches as part of the designed contact.** U-03 (a)'s exception
   would read "the rear skirt's bottom face on the top of OD-C11's wall: the line along
   x ±116 and its corner arcs over x ±110 … ±116", with clearance 0 and interference ≤ 0.
   No geometry change. This v01 is then reviewable as built, since every other row passes.
   It is the same flat-on-flat contact at y 215, and it adds bearing at the rear corners.
   Cheapest.
2. **A relief in the lid.** The skirt's bottom is raised by ≥ 0.5 over the two rear
   corner arcs where they lie over OD-C11's wall (x ±110 … ±117, z −305 … −299). REQ-02
   would have to allow it, because the bottom is then no longer one plane at y 215. It
   costs one build attempt, and the line contact stays as §5 has it.
3. **A change in OD-C11 (its own job, unreviewed and stopped).** Stop the wall top at
   x ±110, or relieve its top outer corners 0.5 over x ±110 … ±116. This lid stays as
   built. It needs OD-C11's spec changed and a new OD-C11 STEP as this job's reference.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20261001-od-c10-top-panel",
  "part": "od_c10_top",
  "tag": "v01",
  "spec_version": "1.1",
  "files": [{"path": "01_CAD/DESIGN_PLAN.md", "sha256": "0d0fc1a890e8431278bdd05ace29f67e8403dfa7a030ea4c36ce7c460171c0f7"}, {"path": "01_CAD/probe/probe_inputs_v01.py", "sha256": "d33bb85f6da334f17afe84f1222a992b5241e63a477bc09fa595d9edc5c250ee"}, {"path": "01_CAD/probe/probe_inputs_v01.json", "sha256": "3a98e3cbba9874791dcce5a43f76278b6563cc2d36d41caf71200c112a7f239b"}, {"path": "01_CAD/probe/versions_v01.py", "sha256": "06ff355b92cf96f5b7388ad2c303837d84f9ec911ee1c8632e2438cf5ad81c6d"}, {"path": "01_CAD/build_od_c10_top.py", "sha256": "fcd39277c772b39e5cffb9a5a2d9940e89208c51d74c717ac8b0b39099a32a5f"}, {"path": "01_CAD/check_od_c10_top.py", "sha256": "552739d24925a52940db07ad1caa5b4f13e8661e2839a5a2e50112415c951c50"}, {"path": "01_CAD/build_record_v01.json", "sha256": "61569d261817da34b2749064f9ad75e21f8b834ea6198d6ba439e83cbc12d197"}, {"path": "01_CAD/check_od_c10_top_v01.json", "sha256": "ea4ac7fd33dc6bab94fd6f1abef6aea53ebbfdbf954e71379b04be0e1c890366"}, {"path": "01_CAD/check_od_c10_top_v01.log", "sha256": "4946aa7217bf5d4e3c818e83821ebaa5e786d2b7ade2e9425ec5377432546146"}, {"path": "01_CAD/sections_od_c10_top.py", "sha256": "652ef3c71fc1cf491abd1682d210ea5684e49ec42e257b184e001781eb0cbe8e"}, {"path": "01_CAD/sections_v01.json", "sha256": "49b94714e3466d9229f3041509586bd50241c525a23732262fe6d9fe8a84474d"}, {"path": "01_CAD/sweep_od_c10_top_v01.sh", "sha256": "642e9a7e614b891006e02f89e64356ce4c906286541e3d5daf33c43095ec8c60"}, {"path": "01_CAD/sweep_summary_v01.py", "sha256": "a10fdcd0bd2eaf726c22e1197df7c37d2e1bf25dadc53190172d2e2f4796c0ab"}, {"path": "01_CAD/sweep_v01/sweep_summary.json", "sha256": "a5cc8955aa98f885fc4db48a25fd9da034bca30c78f65bde028b57549b0daf18"}, {"path": "01_CAD/report_tables_v01.py", "sha256": "62288a855087f7b12173bb1378a4b9f85add76458bdd3ff7967d07002bb2141d"}, {"path": "01_CAD/report_rows_v01.json", "sha256": "ba5e62cedfd987ed0d4d274b9360af4f144530c6761a2cb1d4fd602a87468928"}, {"path": "02_STEP_STL/od_c10_top_C1_v01.step", "sha256": "0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f"}, {"path": "02_STEP_STL/od_c10_assembly_C1_v01.step", "sha256": "d5881320038a66454cfb9d8a2b89aba4ca38c4cc69cd9182cad4eb6a9ef3c9d9"}, {"path": "02_STEP_STL/od_c10_top_C1_v01.stl", "sha256": "2e3f1c736115fe1b6efca9110229357fca8c840fe8786f4b0ccced3e39d93bc9"}, {"path": "03_Sections/od_c10_top_cols_x65_v01_left.png", "sha256": "9e63029fa3a1a33ab21d16719e713ee1510d6c801fb7323e5e7fd3e55eee32ab"}, {"path": "03_Sections/od_c10_top_col_z-60_v01_top.png", "sha256": "e146b098c66eb8a8ab67ffe37eb361b800fd7190fd692bdd5201e047bf6d3858"}, {"path": "03_Sections/od_c10_top_col_z-210_v01_top.png", "sha256": "2aa0f9576829183e7aef8caab96e0f2a6cf0226b9a4747377bf2c587e8aaa0ce"}, {"path": "03_Sections/od_c10_top_cols_z-293_v01_top.png", "sha256": "128aa96e47bbea1176cea850e617f56a365291a18db34b58969291019e68e8bd"}, {"path": "03_Sections/od_c10_top_col_x90_v01_left.png", "sha256": "464acc51c567575adcc4999a94586b1b2460691cb496cb345bc76b6d2478e209"}, {"path": "03_Sections/od_c10_top_col_x-90_v01_left.png", "sha256": "c3cbc6040f945fb77b8bd5b908c69a5a20f74e9b0c010c8d9262865bf0dc31ea"}, {"path": "03_Sections/od_c10_top_rearrib_x94_v01_left.png", "sha256": "61e4bf68f172944a5426f3ef61ffddfac118a2178dabf2347c944d062b311a58"}, {"path": "03_Sections/od_c10_top_pads_z30_v01_top.png", "sha256": "ebddc98b1be7b5a6882331365e8d8d171907474da89da592e092b39dc467bec6"}, {"path": "03_Sections/od_c10_top_plan_y230_v01_front.png", "sha256": "bef87b584ef2298fa2bda237db2b370f9c94c4f44dc2f559129764f84cbd1afb"}, {"path": "03_Sections/od_c10_top_holes_y216p5_v01_front.png", "sha256": "297f6b993b1e5837585c73f1189b248cf211c055856be56f7bea96f438b1664e"}, {"path": "03_Sections/od_c10_top_skin_y248p5_v01_front.png", "sha256": "0d578a5695b336da330ed0dfe723b40d44ef9de5b1894ee38bb85f1056aaff52"}, {"path": "03_Sections/od_c10_assembly_cols_x65_v01_left.png", "sha256": "c6702fec12c6a21d010c0961dd8e07e3f8e69cacc1f0fc3258e94b949206d910"}, {"path": "03_Sections/od_c10_assembly_cols_z-293_v01_top.png", "sha256": "082ba947ac1d2a4730cd006dde741c8d22cbe428ba6713cfdede5531a7e26db6"}, {"path": "03_Sections/od_c10_assembly_pads_z30_v01_top.png", "sha256": "b76a8149f36bb4dfed43d1f80a5ca4f2d50a9eaae9153fe4fff5584ee4b748c6"}, {"path": "03_Sections/od_c10_assembly_corner_z-300p5_v01_top.png", "sha256": "c55987e90d7c4bce645c4248d145703d8653c6d1f4dfb7409e8eaceeb10e4e21"}, {"path": "03_Sections/od_c10_assembly_corner_x113_v01_left.png", "sha256": "eb7d44b9d4cb016737b8b8cad260922ab5097af70fd6817fc4a6d9771f1076db"}],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "cadquery-ocp-novtk 7.9.3.1.1", "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"},
  "gates": [{"gate": "U-01.solid_count", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-01.brep_valid", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-01.naked_edges", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-02.size_x", "measured": 240.0, "unit": "mm", "required": "in [239.9, 240.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.size_x", "measured": 240.0, "unit": "mm", "required": "in [239.9, 240.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-02.size_y", "measured": 39.5, "unit": "mm", "required": "in [39.4, 39.6]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.size_y", "measured": 39.5, "unit": "mm", "required": "in [39.4, 39.6]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-02.size_z", "measured": 405.0, "unit": "mm", "required": "in [404.9, 405.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.size_z", "measured": 405.0, "unit": "mm", "required": "in [404.9, 405.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.position.min_x", "measured": -120.0, "unit": "mm", "required": "in [-120.1, -119.9]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.position.max_x", "measured": 120.0, "unit": "mm", "required": "in [119.9, 120.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.position.min_y", "measured": 210.5, "unit": "mm", "required": "in [210.4, 210.6]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.position.max_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.position.min_z", "measured": -305.0, "unit": "mm", "required": "in [-305.1, -304.9]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "envelope_within_spec.position.max_z", "measured": 100.0, "unit": "mm", "required": "in [99.9, 100.1]", "margin": 0.1, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "D-02.size_x", "measured": 240.0, "unit": "mm", "required": "<= 420.0", "margin": 180.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-09"]}, {"gate": "D-02.size_z", "measured": 405.0, "unit": "mm", "required": "<= 420.0", "margin": 15.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-09"]}, {"gate": "D-02.size_y", "measured": 39.5, "unit": "mm", "required": "<= 500.0", "margin": 460.5, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-09"]}, {"gate": "REQ-01.max_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-02.min_x", "measured": -120.0, "unit": "mm", "required": "in [-120.1, -119.9]", "margin": 0.1, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.max_x", "measured": 120.0, "unit": "mm", "required": "in [119.9, 120.1]", "margin": 0.1, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.min_z", "measured": -305.0, "unit": "mm", "required": "in [-305.1, -304.9]", "margin": 0.1, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.max_z", "measured": 100.0, "unit": "mm", "required": "in [99.9, 100.1]", "margin": 0.1, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-01.top_faces", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-01.top_face_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "(-120.0000, 250.0000, -305.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-01.skin_t.x0_z-150", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(0.0000, 248.5000, -150.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-01.skin_t.x-100_z-100", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-100.0000, 248.5000, -100.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-01.skin_t.x100_z0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(100.0000, 248.5000, 0.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-01.skin_t.x0_z0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(0.0000, 248.5000, 0.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-01.skin_t.x-80_z80", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-80.0000, 248.5000, 80.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "REQ-02.corner_r.x110_z-295.a15", "measured": 9.999999967235793, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.099999967, "at": "(119.6593, 230.0000, -297.5882) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x110_z-295.a45", "measured": 9.999999976014935, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.099999976, "at": "(117.0711, 230.0000, -302.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x110_z-295.a75", "measured": 9.999999991220857, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.099999991, "at": "(112.5882, 230.0000, -304.6593) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.corner_x110_z-295", "measured": 2.999999981381878, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.099999981, "at": "(117.0711, 230.0000, -302.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x110_z90.a285", "measured": 9.999999991220857, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.099999991, "at": "(112.5882, 230.0000, 99.6593) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x110_z90.a315", "measured": 9.999999976014935, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.099999976, "at": "(117.0711, 230.0000, 97.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x110_z90.a345", "measured": 9.999999967235793, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.099999967, "at": "(119.6593, 230.0000, 92.5882) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.corner_x110_z90", "measured": 2.999999981381878, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.099999981, "at": "(117.0711, 230.0000, 97.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x-110_z-295.a105", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-112.5882, 230.0000, -304.6593) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x-110_z-295.a135", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-117.0711, 230.0000, -302.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x-110_z-295.a165", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-119.6593, 230.0000, -297.5882) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.corner_x-110_z-295", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-117.0711, 230.0000, -302.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x-110_z90.a195", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-119.6593, 230.0000, 92.5882) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x-110_z90.a225", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-117.0711, 230.0000, 97.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.corner_r.x-110_z90.a255", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-112.5882, 230.0000, 99.6593) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.corner_x-110_z90", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-117.0711, 230.0000, 97.0711) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.+x.at0_-150", "measured": 2.9999999999899956, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(120.0000, 230.0000, -150.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.+x.at0_0", "measured": 2.9999999999899956, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(120.0000, 230.0000, 0.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.+x.at0_60", "measured": 2.9999999999899956, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(120.0000, 230.0000, 60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.-x.at0_-150", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-120.0000, 230.0000, -150.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.-x.at0_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-120.0000, 230.0000, -0.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.-x.at0_60", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-120.0000, 230.0000, 60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.-z.at-40_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-40.0000, 230.0000, -305.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.-z.at0_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(0.0000, 230.0000, -305.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.-z.at40_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(40.0000, 230.0000, -305.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.+z.at-40_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-40.0000, 230.0000, 100.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.+z.at0_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(-0.0000, 230.0000, 100.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "REQ-02.skirt_t.+z.at40_0", "measured": 3.0, "unit": "mm", "required": "in [2.9, 3.1]", "margin": 0.1, "at": "(40.0000, 230.0000, 100.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "U-05.skirt_bottom_faces", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "REQ-02.skirt_bottom_y", "measured": 215.0, "unit": "mm", "required": "in [214.9, 215.1]", "margin": 0.1, "at": "(-120.0000, 215.0000, -305.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-04"]}, {"gate": "U-05.plane_faces", "measured": 59, "unit": "count", "required": "== 59", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.plane_faces", "measured": 59, "unit": "count", "required": "== 59", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.cylinder_faces", "measured": 22, "unit": "count", "required": "== 22", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.cylinder_faces", "measured": 22, "unit": "count", "required": "== 22", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.concave_cylinders", "measured": 12, "unit": "count", "required": "== 12", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.concave_cylinders", "measured": 12, "unit": "count", "required": "== 12", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.convex_cylinders", "measured": 10, "unit": "count", "required": "== 10", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.convex_cylinders", "measured": 10, "unit": "count", "required": "== 10", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.cone_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.cone_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.sphere_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.sphere_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.torus_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.torus_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.bspline_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.bspline_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.other_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.other_faces", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.bores", "measured": 8, "unit": "count", "required": "== 8", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.bores", "measured": 8, "unit": "count", "required": "== 8", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.bores_d34_y_through", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.bores_d65_y_blind", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.column_cylinders", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.column_cylinders", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.pad_cylinders", "measured": 2, "unit": "count", "required": "== 2", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.pad_cylinders", "measured": 2, "unit": "count", "required": "== 2", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.bulk_rib_sides", "measured": 8, "unit": "count", "required": "== 8", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.bulk_rib_sides", "measured": 8, "unit": "count", "required": "== 8", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.bulk_rib_hyp", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.bulk_rib_hyp", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.rear_rib_sides", "measured": 16, "unit": "count", "required": "== 16", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.rear_rib_sides", "measured": 16, "unit": "count", "required": "== 16", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.rear_rib_bottoms", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.rear_rib_bottoms", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.rear_rib_hyp", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.rear_rib_hyp", "measured": 4, "unit": "count", "required": "== 4", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-05.skin_under_faces", "measured": 3, "unit": "count", "required": "== 3", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "feature_census.skin_under_faces", "measured": 3, "unit": "count", "required": "== 3", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "REQ-03.x65_z-60.column_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.column_d_face", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(65.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.column_d_x", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(71.0000, 215.5000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.column_d_z", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(65.0000, 215.5000, -66.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.column_bottom_y", "measured": 215.0, "unit": "mm", "required": "in [214.95, 215.05]", "margin": 0.05, "at": "(59.0000, 215.0000, -66.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.hole_d", "measured": 3.4, "unit": "mm", "required": "in [3.3, 3.5]", "margin": 0.1, "at": "(65.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.hole_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.hole_through", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "(65.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "D-04a.x65_z-60.hole_d", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(65.0000, 215.0000, -60.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-03.x65_z-60.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(65.0000, 218.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-60.cbore_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 218.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-07.x65_z-60.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(65.0000, 218.0000, -60.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-03.x65_z-60.cbore_floor_y", "measured": 218.0, "unit": "mm", "required": "in [217.9, 218.1]", "margin": 0.1, "at": "(65.0000, 218.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-07.x65_z-60.cbore_mouth_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "(65.0000, 250.0000, -60.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-07.x65_z-60.driver_path_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "REQ-03.x65_z-210.column_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 215.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.column_d_face", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(65.0000, 215.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.column_d_x", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(71.0000, 215.5000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.column_d_z", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(65.0000, 215.5000, -216.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.column_bottom_y", "measured": 215.0, "unit": "mm", "required": "in [214.95, 215.05]", "margin": 0.05, "at": "(59.0000, 215.0000, -216.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.hole_d", "measured": 3.4, "unit": "mm", "required": "in [3.3, 3.5]", "margin": 0.1, "at": "(65.0000, 215.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.hole_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 215.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.hole_through", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "(65.0000, 215.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "D-04a.x65_z-210.hole_d", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(65.0000, 215.0000, -210.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-03.x65_z-210.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(65.0000, 218.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-03.x65_z-210.cbore_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 218.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-07.x65_z-210.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(65.0000, 218.0000, -210.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-03.x65_z-210.cbore_floor_y", "measured": 218.0, "unit": "mm", "required": "in [217.9, 218.1]", "margin": 0.1, "at": "(65.0000, 218.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "REQ-07.x65_z-210.cbore_mouth_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "(65.0000, 250.0000, -210.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-07.x65_z-210.driver_path_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "REQ-04.x90_z-293.column_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.column_d_face", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.column_d_x", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(96.0000, 215.5000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.column_d_z", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(90.0000, 215.5000, -299.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.column_bottom_y", "measured": 215.0, "unit": "mm", "required": "in [214.95, 215.05]", "margin": 0.05, "at": "(84.0000, 215.0000, -299.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.hole_d", "measured": 3.4, "unit": "mm", "required": "in [3.3, 3.5]", "margin": 0.1, "at": "(90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.hole_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.hole_through", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "(90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "D-04a.x90_z-293.hole_d", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(90.0000, 215.0000, -293.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-04.x90_z-293.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(90.0000, 218.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x90_z-293.cbore_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(90.0000, 218.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-07.x90_z-293.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(90.0000, 218.0000, -293.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-04.x90_z-293.cbore_floor_y", "measured": 218.0, "unit": "mm", "required": "in [217.9, 218.1]", "margin": 0.1, "at": "(90.0000, 218.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-07.x90_z-293.cbore_mouth_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "(90.0000, 250.0000, -293.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-07.x90_z-293.driver_path_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "REQ-04.x-90_z-293.column_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(-90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.column_d_face", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(-90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.column_d_x", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(-84.0000, 215.5000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.column_d_z", "measured": 12.0, "unit": "mm", "required": "in [11.9, 12.1]", "margin": 0.1, "at": "(-90.0000, 215.5000, -299.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.column_bottom_y", "measured": 215.0, "unit": "mm", "required": "in [214.95, 215.05]", "margin": 0.05, "at": "(-96.0000, 215.0000, -299.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.hole_d", "measured": 3.4, "unit": "mm", "required": "in [3.3, 3.5]", "margin": 0.1, "at": "(-90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.hole_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(-90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.hole_through", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "(-90.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "D-04a.x-90_z-293.hole_d", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(-90.0000, 215.0000, -293.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-04.x-90_z-293.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(-90.0000, 218.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-04.x-90_z-293.cbore_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(-90.0000, 218.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-07.x-90_z-293.cbore_d", "measured": 6.5, "unit": "mm", "required": "in [6.4, 6.6]", "margin": 0.1, "at": "(-90.0000, 218.0000, -293.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-04.x-90_z-293.cbore_floor_y", "measured": 218.0, "unit": "mm", "required": "in [217.9, 218.1]", "margin": 0.1, "at": "(-90.0000, 218.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "REQ-07.x-90_z-293.cbore_mouth_y", "measured": 250.0, "unit": "mm", "required": "in [249.9, 250.1]", "margin": 0.1, "at": "(-90.0000, 250.0000, -293.0000) mm", "status": "PASS", "assumes": []}, {"gate": "REQ-07.x-90_z-293.driver_path_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "REQ-05.x48_z30.pad_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(48.0000, 210.5000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x48_z30.pad_d_x", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(53.0000, 220.0000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x48_z30.pad_d_z", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(48.0000, 220.0000, 25.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x48_z30.pad_bottom_y", "measured": 210.5, "unit": "mm", "required": "in [210.45, 210.55]", "margin": 0.05, "at": "(43.0000, 210.5000, 25.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.pad_offset", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(-48.0000, 210.5000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.pad_d_x", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-43.0000, 220.0000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.pad_d_z", "measured": 10.0, "unit": "mm", "required": "in [9.9, 10.1]", "margin": 0.1, "at": "(-48.0000, 220.0000, 25.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.pad_bottom_y", "measured": 210.5, "unit": "mm", "required": "in [210.45, 210.55]", "margin": 0.05, "at": "(-53.0000, 210.5000, 25.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-06.headroom_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-06"]}, {"gate": "D-03b.flat_ceiling_span", "measured": 3.1385840240914478, "unit": "mm", "required": "<= 5.0", "margin": 1.861415976, "at": "(66.5000, 218.0000, -60.8000) mm", "status": "PASS_ASSUMED", "assumes": ["A-08"]}, {"gate": "U-03.seat.x65_z-60.c02.clearance", "measured": 0.0, "unit": "mm", "required": "== 0.0", "margin": 0.0, "at": "(67.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.seat.x65_z-60.c02.interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.coaxial.x65_z-60", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 209.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "REQ-03.x65_z-60.coaxial_with_insert", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 209.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "U-03.seat.x65_z-210.c02.clearance", "measured": 0.0, "unit": "mm", "required": "== 0.0", "margin": 0.0, "at": "(67.0000, 215.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.seat.x65_z-210.c02.interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.coaxial.x65_z-210", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 209.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "REQ-03.x65_z-210.coaxial_with_insert", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(65.0000, 209.0000, -210.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-05"]}, {"gate": "U-03.seat.x90_z-293.c11.clearance", "measured": 0.0, "unit": "mm", "required": "== 0.0", "margin": 0.0, "at": "(96.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.seat.x90_z-293.c11.interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.coaxial.x90_z-293", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(90.0000, 209.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "REQ-04.x90_z-293.coaxial_with_insert", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(90.0000, 209.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "U-03.seat.x-90_z-293.c11.clearance", "measured": 0.0, "unit": "mm", "required": "== 0.0", "margin": 0.0, "at": "(-84.0000, 215.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.seat.x-90_z-293.c11.interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.coaxial.x-90_z-293", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(-90.0000, 209.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "REQ-04.x-90_z-293.coaxial_with_insert", "measured": 0.0, "unit": "mm", "required": "<= 0.1", "margin": 0.1, "at": "(-90.0000, 209.0000, -293.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-02", "A-05"]}, {"gate": "U-03.c05.clearance", "measured": 0.5, "unit": "mm", "required": "in [0.45, 0.55]", "margin": 0.05, "at": "(-43.0000, 210.5000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c05.clearance_without_pads", "measured": 6.4031242374328485, "unit": "mm", "required": ">= 0.5", "margin": 5.903124237, "at": "(59.0000, 215.0000, -60.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c05.interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "REQ-05.x48_z30.clearance_to_c05", "measured": 0.5, "unit": "mm", "required": "in [0.45, 0.55]", "margin": 0.05, "at": "(53.0000, 210.5000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.clearance_to_c05", "measured": 0.5, "unit": "mm", "required": "in [0.45, 0.55]", "margin": 0.05, "at": "(-43.0000, 210.5000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x48_z30.hub_r", "measured": 43.041648597857254, "unit": "mm", "required": ">= 40.0", "margin": 3.041648598, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x48_z30.to_counterbores", "measured": 33.940046219457976, "unit": "mm", "required": ">= 20.0", "margin": 13.940046219, "at": "(44.0000, 210.0000, -12.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.hub_r", "measured": 43.041648597857254, "unit": "mm", "required": ">= 40.0", "margin": 3.041648598, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "REQ-05.x-48_z30.to_counterbores", "measured": 33.940046219457976, "unit": "mm", "required": ">= 20.0", "margin": 13.940046219, "at": "(-44.0000, 210.0000, -12.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]}, {"gate": "U-03.c07.clearance", "measured": 167.29913329123374, "unit": "mm", "required": ">= 3.0", "margin": 164.299133291, "at": "(-117.0000, 215.0000, -114.9500) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.plate.clearance", "measured": 210.5, "unit": "mm", "required": ">= 3.0", "margin": 207.5, "at": "(-43.0000, 210.5000, 30.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c02.clearance_away", "measured": 14.330925825473228, "unit": "mm", "required": ">= 0.5", "margin": 13.830925825, "at": "(70.8611, 229.3264, -208.5000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c11.clearance_line_contact", "measured": 0.0, "unit": "mm", "required": "== 0.0", "margin": 0.0, "at": "(-110.0000, 215.0000, -302.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c11.interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c11.clearance_away", "measured": 0.0, "unit": "mm", "required": ">= 0.5", "margin": -0.5, "at": "(-110.8352, 215.0000, -301.9500) mm", "status": "FAIL", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03.c11.skirt_contact_area_off_the_line", "measured": 11.813263962572325, "unit": "mm2", "required": "<= 0.0", "margin": -11.813263963, "at": "[[[-116.0, -110.0], [-302.0, -299.0]], [[109.999999992409...", "status": "FAIL", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03(b).plate.worst_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "dy 40", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03(b).c02.worst_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "dy 40", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03(b).c05.worst_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "dy 40", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03(b).c07.worst_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "dy 40", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-03(b).c11.worst_interference", "measured": 0.0, "unit": "mm3", "required": "<= 0.0", "margin": 0.0, "at": "dy 40", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]}, {"gate": "U-04.part.schema", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.part.solids", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.part.volume_delta", "measured": 1.0972144082188606e-07, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": -1.1e-07, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.part.faces_delta", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.part.labels", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.part.valid_after", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.schema", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.solids", "measured": 6, "unit": "count", "required": "== 6", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.faces_delta", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.labels", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.valid_after", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.od_c10_top.volume_delta", "measured": 1.0972144082188606e-07, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": -1.1e-07, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.od_c01_frame.volume_delta", "measured": 0.0, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.od_c02_bulkhead.volume_delta", "measured": 4.656612873077393e-10, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": -4.656612873077393e-10, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.od_c05_carrier.volume_delta", "measured": 1.3387762010097504e-09, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": -1e-09, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.od_c07_valve_mount.volume_delta", "measured": 1.1641532182693481e-09, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": -1e-09, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-04.assembly.od_c11_back.volume_delta", "measured": 2.3283064365386963e-10, "unit": "mm3", "required": "in [0.0, 0.0]", "margin": -2.3283064365386963e-10, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "D-01a", "measured": 2.7499999999774873, "unit": "mm", "required": ">= 0.8", "margin": 1.95, "at": "(-92.9792, 247.0000, -294.2989) mm", "status": "PASS", "assumes": []}, {"gate": "D-01b", "measured": 2.7499999999774873, "unit": "mm", "required": ">= 2.0", "margin": 0.75, "at": "(-92.9792, 247.0000, -294.2989) mm", "status": "PASS", "assumes": []}, {"gate": "D-06a", "measured": 2.7499999999774873, "unit": "mm", "required": ">= 1.0", "margin": 1.75, "at": "(-92.9792, 247.0000, -294.2989) mm", "status": "PASS", "assumes": []}, {"gate": "U-06(Soft)", "measured": 2.7499999999774873, "unit": "mm", "required": ">= 2.0", "margin": 0.75, "at": "(-92.9792, 247.0000, -294.2989) mm", "status": "PASS", "assumes": []}, {"gate": "D-03a", "measured": 90.0, "unit": "deg", "required": ">= 45.0", "margin": 45.0, "at": "\u2014", "status": "PASS_ASSUMED", "assumes": ["A-08"]}, {"gate": "U-07.mesh.bodies", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-07.mesh.naked_edges", "measured": 0, "unit": "count", "required": "== 0", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-07.mesh.winding", "measured": 1, "unit": "bool", "required": "== 1", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-07.angular_tolerance", "measured": 0.17, "unit": "rad", "required": "<= 0.17890034867493382", "margin": 0.008900349, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-07.tolerance", "measured": 0.01, "unit": "mm", "required": "<= 0.01", "margin": 0.0, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-07.max_sagitta", "measured": 0.005384670409338475, "unit": "mm", "required": "<= 0.01", "margin": 0.00461533, "at": "(-84.4084, 215.5000, -295.1609) mm", "status": "PASS", "assumes": []}, {"gate": "U-07.max_sagitta_delivered", "measured": 0.005384670399172438, "unit": "mm", "required": "<= 0.01", "margin": 0.00461533, "at": "\u2014", "status": "PASS", "assumes": []}, {"gate": "U-08", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": "\u2014", "status": "N/A", "assumes": []}, {"gate": "D-05a", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": "\u2014", "status": "N/A", "assumes": []}, {"gate": "D-05b", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": "\u2014", "status": "N/A", "assumes": []}, {"gate": "D-07", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": "\u2014", "status": "N/A", "assumes": []}, {"gate": "J-05", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": "\u2014", "status": "N/A", "assumes": []}, {"gate": "E-06", "measured": null, "unit": "", "required": "reviewer", "margin": null, "at": "\u2014", "status": "INCONCLUSIVE", "assumes": []}, {"gate": "REQ-08(Soft)", "measured": null, "unit": "", "required": "bench", "margin": null, "at": "\u2014", "status": "INCONCLUSIVE", "assumes": ["A-04", "A-11"]}],
  "sweep": [{"parameter": "hole_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "D-04a", "worst_margin": 0.05}, {"parameter": "cbore_d", "values": [6.4, 6.5, 6.6], "all_built": true, "worst_gate": "D-01b", "worst_margin": 0.7}, {"parameter": "cbore_floor_y", "values": [217.9, 218.0, 218.1], "all_built": true, "worst_gate": "REQ-03.cbore_floor_y", "worst_margin": 0.0}, {"parameter": "col_dx", "values": [-0.1, 0.0, 0.1], "all_built": true, "worst_gate": "REQ-03.column_offset", "worst_margin": 0.0}, {"parameter": "col_dz", "values": [-0.1, 0.0, 0.1], "all_built": true, "worst_gate": "REQ-03.column_offset", "worst_margin": 0.0}, {"parameter": "col_bottom_y", "values": [214.95, 215.0, 215.05], "all_built": true, "worst_gate": "U-03.seat (designed contact, nominal only)", "worst_margin": -5.0265}, {"parameter": "pad_bottom_y", "values": [210.45, 210.5, 210.55], "all_built": true, "worst_gate": "REQ-05.clearance_to_c05", "worst_margin": 0.0}, {"parameter": "skirt_bottom_y", "values": [214.9, 215.0, 215.1], "all_built": true, "worst_gate": "U-03.c11.interference (corner patches)", "worst_margin": -1.1813}],
  "least_sure": ["U-03 (a) at OD-C11's wall corners: the strict reading of the named line contact, against an unreviewed OD-C11 v02", "REQ-08 stiffness: 3.0 PETG skin held at x 65 and the rear only, left and front edges free until OD-C09/C12/C13 exist", "The ribs are a design choice derived from clearances, not a load case; a 5.0 pocket behind each rear column"],
  "stopped": true
}
```
