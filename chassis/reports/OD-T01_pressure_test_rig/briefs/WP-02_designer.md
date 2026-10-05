# WP-02 — designer brief, J2 package (plan only)

Job: 20261002-od-t01-pressure-test-rig · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-02; SHA-256 c7aa3b682f36aa223763ab81be97604421d457b1b002de7d6e6d39ff75ad641e) · concept C1 (chosen) · target `od_t01_rig_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md` (template
`atolye/templates/DESIGN_PLAN.md`). Build nothing. The orchestrator checks that
every spec feature (§4 C1) and every §5 gate row has a planned feature and check
before the J3 package is sent. Measure the reference solids at D1 as much as you
need to plan the joint: the housing's rear face, its four insert bores (axes,
depth), its square outline, OD-G04's hub tube and the pair-B screw heads near the
hub window, and OD-G10's extents at its locked pose and through the sweeps of
REQ-04. A spec value your measurement contradicts is a question in the plan's
§7, never a silent change.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-06a, D-07 (N/A by its row), J-05 (N/A
by its row), REQ-01 … REQ-07, REQ-08 (Soft, bench); plus `exactly_one_solid`,
`feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | the housing, housing frame, placed by spec §2 |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | housing + OD-G04 + OD-G10 locked, housing frame, placed by spec §2 |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | reference (its placed copy is in the assembly) |
| `00_Spec/inputs/OD-G10_portafilter.step` | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 | reference (its placed copy is in the assembly) |
| `00_Spec/inputs/OD-C05_group_head_carrier.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | the interface precedent (reference only) |

Place every imported part by the pose of spec §2, never by bounding boxes.
`od_g01_assembly_C1_v03.step` holds three solids; identify each by measurement.
Its OD-G10 solid may not be a sound solid (OD-G01 REPORT): if a boolean on it
fails, say so and plan the fallback.

## Environment

Workspace: `/root/oguz-jobs/20261002-od-t01-pressure-test-rig`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>` (build123d
0.11.1, OCCT 7.9.3 in the tools venv). Library index: `library/INDEX.md` (at most
two cards); traps: `library/BUILD123D-NOTES.md`. Tools documentation:
`tools/README.md`. Write only under `01_CAD/`. Do not call any mcp__hearthbot__ tool.

## Findings to fix

None (first package).
