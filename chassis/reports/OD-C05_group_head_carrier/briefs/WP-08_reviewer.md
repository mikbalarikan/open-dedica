# WP-08 — reviewer brief (J4, the one review of build v04)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 2.2 (ratified 2026-09-30) · concept C4 (column) · target `od_c05_carrier_v04` · review RV02 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v04 of the printed group head carrier OD-C05: the plan
`01_CAD/DESIGN_PLAN_v02.md` with the amendments of `briefs/WP-05_designer.md`,
`WP-06_designer.md` and `WP-07_designer.md` (all part of the plan), the REPORT
`01_CAD/REPORT_od_c05_carrier_v04.md`, and the exported files listed below. Never
the designer's scripts (`01_CAD/*.py`, `01_CAD/probe/`, `01_CAD/sweep_v0*/`).
History: v01 (spec 1.2, concept C1) was reviewed by RV01 and blocked on
plausibility F1 (the group head on its side); spec 2.0 turned the axis vertical
(−Z of the housing frame up, the mouth down, +Y the front) and concept C4 put a
plate over the housing's rear face on a closed column behind it; v02 and v03
stopped on print-orientation faults of the spec itself (fixed in 2.1 and 2.2).
Read `reviews/RV01_od_c05_carrier_v01.md` for the earlier findings F2 … F5 and
check what v04 did with them (RV01 §6; the REPORT's §7 / §9).

The frame is the housing's (OD-G01 v02 at the identity pose): +Z is down in the
machine, the floor is z +180.06, the housing's rear face (the plate's contact)
z −24.94, +Y toward the user. OD-G04 is rotated +6.05° about Z and translated
z −6.82. Print: the plate's top face (z −29.94) on the bed, build direction +Z.
Read the plausibility list against a real espresso machine (the Dedica): the
housing hangs under the plate, the portafilter goes in from below, the column
stands behind the housing on the base frame, the hot water tube enters the column
through the rear window and reaches the hub through the hatch and the hub window.
Weigh, outside the gates, the designer's own risk: the foot's inside is a
V-trough in the machine whose counterbores could collect drips on the screw heads.

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-08 (U-08 N/A), U-07 with the 3MF `02_STEP_STL/od_c05_carrier_C4_v04.3mf`
(written by the orchestrator from the designer's STL and re-parsed: 5232
triangles; check it against the STL), D-01a, D-01b, D-02, D-03a and D-03b (the
named exception: the eight counterbore floors; read the roof's and the window
gable's analytic angles, and confirm the ridge is the highest line of the roof
and the window apex the highest point of the window in the print), D-04a,
D-06a, D-07 (N/A), E-06, REQ-01 … REQ-09 (REQ-09 Soft bench: INCONCLUSIVE with a
risk rating, with your own hand estimate of the closed column's torsion and the
plate's 96 cantilever against RV01 F2 and the v02 REPORT §9); the §P list; the
feature census against the plan as amended (1 plate with hub window and hatch,
front / two side / rear walls, rear window with gable, roofed foot, 2 gussets,
4 + 4 Ø3.4 holes, 4 + 4 Ø6.5 counterbores); positive controls for every check
family used.

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `01_CAD/REPORT_od_c05_carrier_v04.md` | c6fca509698cac42c292c4bd7950f3346b5e78d1eeead09e494c2392261e61c2 |
| `01_CAD/DESIGN_PLAN_v02.md` | c580be8de01b9060e96b8ed8b64640c34fefa5a7d71c5fb7e319cf4985cba6bf |
| `briefs/WP-05_designer.md` | a063c978322b35727ee18290245023daf8454a1508c2f73784d17b74877d89a8 |
| `briefs/WP-06_designer.md` | c37d317a9179a587d52d2172317bd420df894b4108848b88e53ed02ec42b0ad2 |
| `briefs/WP-07_designer.md` | e373fcd3502d6f9da392eb2a21f69bfb24494505d8202c4a90ebf31faf09ff88 |
| `01_CAD/check_od_c05_carrier_v04.json` | 1ac98922997de08a8e8e091a4a25e7c60ae4027607b3b9c62d455480e67a9cd2 |
| `01_CAD/build_od_c05_carrier_v04.json` | 69b57eae4df14bd02a0304a3e2fba05ccdf7bca2f25b4ed5ed841f8ab66e9305 |
| `01_CAD/sections_od_c05_carrier_v04.json` | 14e458b76b293399eba666f9a31af492f62203139a3b109e6d1312b513e04b9e |
| `01_CAD/sweep_v04/summary_v04.json` | 5dfed2547113a8f451e599ebe392d37ccaf459dee48e95c278b3d7156ff15bbe |
| `02_STEP_STL/od_c05_assembly_C4_v04.step` | 70390d91f1aa6ff710208065366aa3598675796fd76e782113f842cb59cd1a77 |
| `02_STEP_STL/od_c05_carrier_C4_v04.3mf` | 7fd7f6a12c0d3920f4c28c761c9f22a2e038b28fab69e49ff0a052096b53b6d7 |
| `02_STEP_STL/od_c05_carrier_C4_v04.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 |
| `02_STEP_STL/od_c05_carrier_C4_v04.stl` | 7ecc4de80bd2b69533b534d660a74e9f3d25e6f14c0f954f93392913605eea2b |
| `03_Sections/od_c05_assembly_x0_v04_left.png` | 475e12a2a6a556d925960dd2cf7041f5d7ed3e4545aebcb649c511acc443b058 |
| `03_Sections/od_c05_assembly_y0_v04_front.png` | eb9f08ce9cc6b29882e96be22ff353afa8bcf6bb8cf4f6f996a5c9272beaa535 |
| `03_Sections/od_c05_carrier_x0_v04_left.png` | 903fe49d7fc2203c6a4651494e820b246d74eb28f6b7c338a762873bdcc7c3a1 |
| `03_Sections/od_c05_carrier_x35_v04_left.png` | 30678270d27ed691fb8ee5e9dd15310a625c41d7d2a8ed9acd6dd7f98d8c46f0 |
| `03_Sections/od_c05_carrier_x53_v04_left.png` | b488b7150c4393ae341f980278b5888c24c35aa20101b8b85afa7f8f47c309f7 |
| `03_Sections/od_c05_carrier_y0_v04_front.png` | f5552864272d7f34b61fcac837579274d104e2f7e442c121a7a7ed230c64bf17 |
| `03_Sections/od_c05_carrier_ym100_v04_front.png` | 1b78bca5d37f8e5081c08b7a94eedc719cb26883f5e90c56b3de28ea4ffea8a8 |
| `03_Sections/od_c05_carrier_ym80_v04_front.png` | e3740700304349f4be0dfbcf20a62f885135b188a48ed7841a10141d54c9dd58 |
| `03_Sections/od_c05_carrier_z165_v04_top.png` | 06837f88f50a34f09375c73c3f864eacd4daf25eaa6341a378e27e9a0f7bd4d5 |
| `03_Sections/od_c05_carrier_zm27p44_v04_top.png` | 1fcc9436a60d3f14205e980d7ed5d025fbe3c0d77c0667050f0c9d809ee66b3c |
| `reviews/RV01_od_c05_carrier_v01.md` | e97b9778da1930dad125cc7e0080d5d270119ac47742e4bc66aedbf0f95ad8c4 |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 |

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c05-group-head-carrier` (`/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV02_od_c05_carrier_v04.md`, `.json`, and `RV02_work/`); if
the Write tool refuses a file, write it with Bash.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
