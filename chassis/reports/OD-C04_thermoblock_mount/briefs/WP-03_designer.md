# WP-03 — designer brief, J3 package (build)

Job: 20260930-od-c04-thermoblock-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c04_mount_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02). Write the checks first
(`01_CAD/check_od_c04_mount.py`), then the build (`01_CAD/build_od_c04_mount.py`)
and the placement of OD-H11 and the two spacer solids for the U-03, REQ-01 and
REQ-03 checks; export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c04_mount_C1_v01.step`, the check assembly into
`02_STEP_STL/od_c04_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_c04_mount_C1_v01.stl`; re-import and measure; sections into
`03_Sections/`; the sweep into `01_CAD/sweep_v01/`; the REPORT into
`01_CAD/REPORT_od_c04_mount_v01.md` with its JSON block (if the Write tool refuses
a file, write it with Bash). Return the block your skill defines. At the fix-cycle
cap, or when a hard gate cannot be met, stop with the measured failure (D9).

## Plan amendments (spec 1.1, checked by the orchestrator)

Your J2 plan stands, with these answers to its Q1–Q3 from spec 1.1 (its §2, §4,
§5 U-03, REQ-03, REQ-07 and §6 rows A-02 … A-05, A-14). Build to them and list
each as a deviation from the plan in REPORT §8; do not rewrite the plan.

| Plan row | Amendment |
|---|---|
| tip_z S1, S2 | both −10.10 ± 0.10 (Q1 option a, Q3): standoffs Ø12.0, 1.90 proud of the plate front face z −12.0, no gussets |
| spacers | SP1 Ø7.0 × 10.10 (z −10.10 … 0.00, seat on the base face), SP2 Ø7.0 × 37.70 (z −10.10 … 27.60, seat on the mid-lug underside), Ø4.0 bores, named `spacer_S1_assumed_A05` and `spacer_S2_assumed_A05` |
| REQ-03 | tip faces at z −10.10 ± 0.10; spacer clearance 0 at both ends |
| REQ-07 and every r, θ | about the measured body axis (x −8.330, y −14.130), as your plan proposes (Q2); report the origin reading beside it |
| U-03 boolean | OD-H11 is unsound (brep_valid 0, A-14): the boolean against it is INCONCLUSIVE by the row, recorded as such; the spacer|mount and spacer|OD-H11 pairs stay `clearance = 0` rows |
| §6 census | 1 plate, 1 foot, 2 gussets (plate-to-foot), 2 standoffs, 2 Ø4.0 bores, 4 Ø3.4 bores; re-tally the planar faces from the frozen feature list |

The OD-H11 joint (identity at the origin, axis +Z) stands. If the built mount
reads under 10.0 to OD-H11 anywhere, that is a FAIL to fix within the fix cycles,
or a stop with the measured clearance (D9), never a changed spec value.

## Gate IDs to check (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-06a, D-07 (N/A by its row), E-06, REQ-01 … REQ-08
(REQ-08 bench: INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs (paths relative to the workspace; full 64-character SHA-256)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | the thermoblock, placed at the identity pose by a joint at the origin, axis +Z (unsound for booleans, A-14) |
| `00_Spec/inputs/reports/OD-H11_thermoblock/params.json` | 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c5203 | the thermoblock's parameters |
| `00_Spec/inputs/reports/OD-H11_thermoblock/ports.json` | 77fbb8b2a53e929216ddea4752a7b18e67f6f57ba1ba3864ec24e179cf224fd5 | pipe and terminal axes |
| `00_Spec/inputs/reports/OD-H11_thermoblock/README.md` | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0 | the thermoblock's frame definition and feature tree |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/REPORT.md`. Tools documentation: `tools/README.md`.

## Findings to fix

None (first build). Deviations from the plan go in REPORT §8.
