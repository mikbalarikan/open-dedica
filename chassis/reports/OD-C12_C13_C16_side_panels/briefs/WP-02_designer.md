# WP-02 — designer brief, J2 package (plan only)

Job: 20261002-od-c12-c13-c16-side-panels · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-02) · concept C1 (chosen) · target `od_side_panels_v01` (three part files: `od_c12_left`, `od_c13_right`, `od_c16_bracket`) · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md` (template
`atolye/templates/DESIGN_PLAN.md`) covering all three parts and the check
assembly. Build nothing. Measure the reference solids at D1 as much as you need
to plan the joints and to confirm the spec's interface values: OD-C01's outline,
corner arcs, top face and existing holes near the six new insert positions;
OD-C10's side skirts (inner face x ±117, bottom y 215) and that nothing else of
the lid lies within the lip's zone; OD-C11's wall ends; OD-C07's outermost x as
placed (does it reach x −117?); OD-C08's extent; the OD-C15 foot poses. A spec
value your measurement contradicts is a question in the plan's §7, never a
silent change. Every spec feature (§4 C1) and every §5 row needs a planned
feature and check.

## Gate IDs (spec §5)

U-01 … U-07, U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b, D-04a,
D-04d, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05, E-06, REQ-01 …
REQ-08 (REQ-08 Soft, bench); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`, for each part file.

## Inputs (paths relative to the workspace; joints in spec §2)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | reference solid |
| `00_Spec/inputs/OD-C02_bulkhead.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | reference solid |
| `00_Spec/inputs/OD-C05_group_head_carrier.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | reference solid |
| `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | reference solid |
| `00_Spec/inputs/OD-C08_electronics_bay_tray.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 | reference solid |
| `00_Spec/inputs/OD-C10_top_panel.step` | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | reference solid |
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | reference solid |
| `00_Spec/inputs/OD-C15_foot.step` | 830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7 | reference solid |

Place every reference solid by the joint the spec gives (identity unless §2
says otherwise), and the brackets by the six poses of §2. Never place by
bounding boxes.

## Environment

Workspace: `/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1). Library index: `library/INDEX.md` (at most two cards);
traps: `library/BUILD123D-NOTES.md`; tools: `tools/README.md`. Write only under
`01_CAD/`. Do not call any mcp__hearthbot__ tool.

## Findings to fix

None (first package).
