# WP-02 — designer brief, J2 package (plan only)

Job: 20261002-od-c14-cord-grommet · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-02) · concept C1 (chosen) · target `od_c14_grommet_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md` (template
`atolye/templates/DESIGN_PLAN.md`). Build nothing. Measure the reference solid
OD-C11 at D1 as much as you need to plan the joint (the cord hole's axis and
diameter, the wall's faces, the gusset and flange near the hole); a spec value
your measurement contradicts is a question in the plan's §7, never a silent
change. Every spec feature (§4 C1) and every §5 row needs a planned feature and
check.

## Gate IDs (spec §5)

U-01 … U-07, U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b, D-04d,
D-06a, D-07 (N/A by its row), J-06, E-11, REQ-01 … REQ-05 (REQ-05 Soft, bench);
plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | mating part, identity (machine frame) |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | reference solid, identity |

Place the halves by the measured hole axis (`locate_bore`), never by bounding
boxes. The cord and tie envelopes are part of the check assembly, not of the
part file.

## Environment

Workspace: `/root/oguz-jobs/20261002-od-c14-cord-grommet`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1). Library index: `library/INDEX.md` (at most two cards);
traps: `library/BUILD123D-NOTES.md`; tools: `tools/README.md`. Write only under
`01_CAD/`. Do not call any mcp__hearthbot__ tool.

## Findings to fix

None (first package).
