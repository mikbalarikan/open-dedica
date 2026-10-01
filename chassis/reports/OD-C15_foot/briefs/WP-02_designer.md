# WP-02 — designer brief, J2 package (plan only)

Job: 20261001-od-c15-feet · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-01) · concept C1 (chosen) · target `od_c15_foot_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md` (template
`atolye/templates/DESIGN_PLAN.md`). Build nothing. The orchestrator checks that
every spec feature (§4 C1) and every §5 gate row has a planned feature and check
before the J3 package is sent. Measure the reference solid OD-C01 at D1 as much as
you need to plan the joint (the feet holes, the plate underside, the corner arcs,
the outline; the values the spec carries as A-01); a spec value your measurement
contradicts is a question in the plan's §7, never a silent change.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row),
J-05, J-06, REQ-01 … REQ-07; plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | mating part, imported and placed in the check assembly in its own frame (the machine frame: X right, +Y up, +Z front, plate top y = 0); the four feet are placed on it by the joint of spec §2 |

The OD-C01 frame is the machine frame; confirm the plate top at y 0, the
underside at y −6.0 and the four Ø3.4 feet holes at (±110, +90) and (±110, −295)
by measurement before you plan the joint on them. Place the feet by the measured
hole axes (`locate_bore`), never by bounding boxes. The fastener envelopes of U-03
(screw head, shank, nut) are part of the check assembly, not of the part file.

## Environment

Workspace: `/home/claude/oguz-env/jobs/20261001-od-c15-feet`. Run
`source /home/claude/oguz-env/env.sh` in every shell command that runs Python,
then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1, OCCT 7.9.3 in the tools venv). Library index:
`library/INDEX.md` (at most two cards); traps: `library/BUILD123D-NOTES.md`.
Tools documentation: `tools/README.md`. Write only under `01_CAD/`.

## Findings to fix

None (first package).
