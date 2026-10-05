# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20261002-od-c09-front-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-02; SHA-256 6aaf9a01a7577144ffae18502862f79c6b25debc12ace188c4d0cc15a86d655f) · concept C1 · target `od_c09_front_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the front panel OD-C09 of the Open Dedica espresso
machine: a printed PLA fascia, 3 mm wall at z 94 … 97 in the machine frame, that
stands on the base frame OD-C01 along its front edge, frames the brew area (the
group head housing OD-G01 vertical, mouth down, OD-G10 locked), leaves the drip
tray slot open, and carries the OEM button board OD-E02 on two bosses with its
three buttons through three Ø15 holes in a column on the left pillar. Review the
plan `01_CAD/DESIGN_PLAN.md` (with the answers of `briefs/WP-03_designer.md`,
which are part of the plan), the REPORT `01_CAD/REPORT_od_c09_front_v01.md`, the
sections in `03_Sections/`, and the exported files below. Never the designer's
scripts or their outputs (`01_CAD/*.py`, `01_CAD/*.json`, `01_CAD/*.log`,
`01_CAD/report_tables_v01.md`, `01_CAD/sweep_v01/`).

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-08 (U-06 Soft, U-08 N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b,
D-04a, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05, E-01, E-05, E-06 (from
the sections), REQ-01 … REQ-07, REQ-08 (Soft, bench: INCONCLUSIVE with a rating);
the §P list P1–P6; the feature census against the plan (U-05); positive controls
for every check family used; the REPORT's §4 sweep and §9 list rated.

Place every reference solid by spec §2 yourself, never from the designer's
assembly file: OD-C01 and OD-C10 at the identity; OD-C05 and the OD-G01 assembly
(identify its three solids by measurement) by housing x → X, y → +Z, z → −Y,
origin (0, 180.06, 32.0); OD-E02 by board x → −Y, y → −X, z → −Z, origin
(−99.0, 140.0, 69.35); OD-G10's motions as REQ-05 states. OD-G10 and OD-E02 are not
sound solids: spec §5 reads their interference rows as `clearance > 0` with
`detail["inside"] == False`.

## Files (relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `02_STEP_STL/od_c09_front_C1_v01.step` | 0d688d24b7954e959291b171fa6e464dd30834e3f737eb73b696dfc992148ab5 | the part, AP242, one named solid |
| `02_STEP_STL/od_c09_front_C1_v01.stl` | 086c7c7e4f1c98472b1800dfce3bf73e83ef240311986df454bd2e1a7c740498 | the mesh (U-07) |
| `02_STEP_STL/od_c09_assembly_C1_v01.step` | e451a3854cb1dd22d29c9ba8871367f3be17341e9e3c06fecdffc3701406984c | the designer's check assembly (for comparison only) |
| `01_CAD/REPORT_od_c09_front_v01.md` | 4111981b095a097442344f43de874e8172be09113c9d67cf14bb97283fed886f | the designer's self-check (placed by the orchestrator, text unchanged but for the model name) |
| `01_CAD/DESIGN_PLAN.md` | 277daf919fa3fd2dc2ff89c8a16e546b29a9df55086fcfd079d13adc35381071 | the plan |
| `briefs/WP-03_designer.md` | 4d4f43edce5a941c21c97f89a2928cd2a33d34d2dd57dca23373f1f91e2cf4cc | the plan's answers |
| `03_Sections/*.png` | REPORT §1 | eighteen sections |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | machine frame |
| `00_Spec/inputs/OD-C05_group_head_carrier.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | housing frame |
| `00_Spec/inputs/OD-C10_top_panel.step` | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | machine frame |
| `00_Spec/inputs/OD-E02_control_board.step` | 4e570b4abc68a538efecbf89022738dd0e2527dcb466ceee9b721b353b005385 | board frame |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | housing + OD-G04 + OD-G10, housing frame |
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | the housing alone |
| `00_Spec/inputs/OD-C15_DESIGN_SPEC.md` | — | the feet keep-outs U-03 names |

## Environment

Workspace `/root/oguz-jobs/20261002-od-c09-front-panel`; run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1, OCCT 7.9.3). Run long commands in the foreground with a
generous timeout. Write only under `reviews/` (`RV01_od_c09_front_v01.md`, `.json`,
and `RV01_work/`); if a file write is blocked by a hook, return the file's full
text in your answer instead. Templates: `atolye/templates/VERDICT.md`; schema
`atolye/schemas/verdict.schema.json`. Tools documentation: `tools/README.md`.
Do not call any mcp__hearthbot__ tool.
