# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20260930-od-c03-pump-cradle · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 · target `od_c03_cradle_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed pump cradle OD-C03 of the Open Dedica
espresso machine: the plan `01_CAD/DESIGN_PLAN.md` (with the amendments of
`briefs/WP-03_designer.md`, which is part of the plan), the REPORT
`01_CAD/REPORT_od_c03_cradle_v01.md`, and the exported files listed below.
Never the designer's scripts (`01_CAD/*.py`, `01_CAD/probes/`, `01_CAD/sweep_v01/`).

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row),
REQ-01 … REQ-09 (REQ-09 is a bench gate: INCONCLUSIVE); the §P list P1–P6; the
feature census against the plan (as amended: 2 ribs, 2 post blocks, 4 slots, 4
holes, 1 foot); positive controls for every check family used.

The assumed sleeve solid (spec A-03) is the designer's own construction, named
`od_h02_sleeve_assumed_A03` in the check assembly: gate REQ-04 and U-03 against it
as the spec writes them, and rate what rests on it.

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `01_CAD/REPORT_od_c03_cradle_v01.md` | 2cafaad31f8bf134745d0d350e9b1b63dc0a15862c0acd893cf7d885410cd76a |
| `01_CAD/DESIGN_PLAN.md` | 7e86466421a4ad81e87dd87bb93215966e3a0b974e33869163b55aaa42bd6540 |
| `01_CAD/check_od_c03_cradle_v01.json` | c46068d7c469414f7200ce8d8ec57a51b2fe9225c8b3a77e604541410d67e66d |
| `01_CAD/sections_od_c03_cradle_v01.json` | 7856b0a860c0b51701464b361ed6701bfc03ab554caa575d6af5c498bb13ea77 |
| `02_STEP_STL/od_c03_assembly_C1_v01.step` | 6ce49e9220d6737d0cd9e95d385b1f7de80ced7e64e7616e562e47bb5280cebf |
| `02_STEP_STL/od_c03_cradle_C1_v01.step` | c4b028e130a3ee29324c5cd31543e44ec7ee6bb5e2489f8dc55c6b018a4aefbd |
| `02_STEP_STL/od_c03_cradle_C1_v01.stl` | b95aab55d1efb1706f41bb7c4c2a9e8c6e50a2ccf0a8e9fa3a5bd38af6dcae8c |
| `03_Sections/od_c03_cradle_v01_assembly_xy_z18p0.png` | f42595ad12ffb6770772bbec40dd72a2d5ed9219a0afdcee64b55c1753dfce90 |
| `03_Sections/od_c03_cradle_v01_assembly_yz_x0p0.png` | bd8a2a1c5c74aa52dee5cefd3191443ea60fcf37d0d1328c315acc1267adf1f2 |
| `03_Sections/od_c03_cradle_v01_xy_z18p0.png` | 6026c0bc98de01d1247d3738a1097fd6d831ca283b5cd6fa2587a615babd3f22 |
| `03_Sections/od_c03_cradle_v01_xy_z28p0.png` | dcb202aa0c0badf040899673aa6f03fbb7d39d4c8be76dacb6ccaa4e5c5a8119 |
| `03_Sections/od_c03_cradle_v01_xz_y38p5.png` | 144b0776717f332a26987361ac900c06299c71a04f252aa55b5bb9d56395a115 |
| `03_Sections/od_c03_cradle_v01_xz_y7p0.png` | 6ef1f55c114f986b4c186561af43e4f5e40eb8868f7c12733fe82830688dba65 |
| `03_Sections/od_c03_cradle_v01_yz_x0p0.png` | 25df58f08d72acfef2676a63b60cd810b20396cfb9118b1e18a5352e4cd24072 |
| `03_Sections/od_c03_cradle_v01_yz_x31p5.png` | f464a2577d1dc4ff079f4acd9a0f0cbe0fdf4aea79170d3b544c4207aba31986 |
| `03_Sections/od_c03_cradle_v01_yz_x34p0.png` | f51f03846c0f003bef9cf8caff76b7567f719b8b315de9378650950208eae4b1 |

Reference solid (input, for the assembly rows):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 |

OD-H01 is placed at the identity pose (joint at the origin, axis +Z); the REPORT
reads it sound (validity 1/1/0).

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c03-pump-cradle` (`/home/claude/oguz-jobs/20260930-od-c03-pump-cradle`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_c03_cradle_v01.md`, `.json`, and `RV01_work/`); if
the Write tool refuses a file, write it with Bash.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
