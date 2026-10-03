# WP-02 — designer brief, J2 package (plan only)

Job: 20261002-od-c09-front-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-02; SHA-256 8206704f73b45520eef7f7c6ad068dd696a2aa1bf68ece959f7815d83e1ba69c) · concept C1 (chosen) · target `od_c09_front_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md` (template
`atolye/templates/DESIGN_PLAN.md`). Build nothing. The orchestrator checks that
every spec feature (§4 C1) and every §5 gate row has a planned feature and check
before the J3 package is sent. Measure the reference solids at D1 as much as you
need to plan: OD-C01's front edge, corner arcs and feet holes; the brew-area set
placed by spec §2 (carrier, housing, OD-G04, OD-G10) and its extents near the
panel; OD-C10's front skirt; and above all OD-E02 as posed by spec §2: its
extents, each cap's axis, radius and foremost point, the board's surface around
its two screw holes (flatness to Ø11, level), the hole axes, and the clearance of
every part of the board to the wall, ribs and bosses. Also derive OD-G10's
sweep (REQ-05) far enough to know it passes. A spec value your measurement
contradicts, or a feature the spec leaves to the plan (the button holes' size
for the tilted caps, the boss end levels, the screw length, how E-01 excludes the
two designed contacts), is a question or a stated derivation in the plan's §7,
never a silent change.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A by its
row), J-05, E-01, E-05, E-06, REQ-01 … REQ-07, REQ-08 (Soft, bench); plus
`exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | the plate, machine frame, identity |
| `00_Spec/inputs/OD-C05_group_head_carrier.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | carrier, housing frame, placed by spec §2 |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | housing + OD-G04 + OD-G10 locked, housing frame, placed by spec §2 |
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | the housing alone (same frame) |
| `00_Spec/inputs/OD-C10_top_panel.step` | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | top panel, machine frame, identity |
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | the back panel this one mirrors (reference only) |
| `00_Spec/inputs/OD-E02_control_board.step` | 4e570b4abc68a538efecbf89022738dd0e2527dcb466ceee9b721b353b005385 | the button board, its datum frame, posed by spec §2 |
| `00_Spec/inputs/OD-S03_steam_knob.step` | 8f1472d086e4d7bd9530976869d4ba97faef3e4af394718269431fbe8a263af5 | phase 2 knob (reference for the reserved place only) |

Place every imported part by the poses of spec §2 (rotations and origins), never
by bounding boxes. `od_g01_assembly_C1_v03.step` holds three solids; identify
OD-G10 by measurement (it is the one reaching housing y ≈ 150). Its OD-G10 solid
may not be a sound solid (OD-G01 REPORT): if a boolean on it fails, say so and
plan the fallback (for example `clearance` only, or its convex pieces).

## Environment

Workspace: `/root/oguz-jobs/20261002-od-c09-front-panel`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>` (build123d
0.11.1, OCCT 7.9.3 in the tools venv). Library index: `library/INDEX.md` (at most
two cards); traps: `library/BUILD123D-NOTES.md`. Tools documentation:
`tools/README.md`. Write only under `01_CAD/`. Do not call any mcp__hearthbot__ tool.

## Findings to fix

None (first package).
