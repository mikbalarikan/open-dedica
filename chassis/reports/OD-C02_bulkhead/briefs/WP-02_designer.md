# WP-02 — designer brief, J3 package with its own plan (build v01)

Job: 20260930-od-c02-bulkhead · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c02_bulkhead_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package with its own plan**: the part is a wall with two rails, two ribs,
four windows and ten small bores, so the plan and the build go in one package.
First run D0–D2 and write `01_CAD/DESIGN_PLAN.md` (measure the inputs it needs:
the OD-C01 plate's top face and its four bulkhead inserts at (65, −45 / −105 /
−165 / −225); the wet-side neighbours as OD-C01 §4 places them, each one's +X
extent and its nearest point to the plane x = 59 and to the windows' collars at
x 61; write the placements as probe scripts under `01_CAD/probe/` with JSON
results, as the OD-C01 job did). Then, without stopping unless a spec value
cannot be met, run D3–D9 and build. Write `01_CAD/build_od_c02_bulkhead.py`
(parametric, every §4 parameter a named value) and `01_CAD/check_od_c02_bulkhead.py`.
Export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c02_bulkhead_C1_v01.step`, the check assembly (bulkhead + OD-C01 +
OD-C03 + OD-H01 + OD-C04 + OD-H11 + OD-G01 + the carrier's foot box
`od_c05_foot_reference_A02` x ±55, y 0 … 210, z −70 … −26) into
`02_STEP_STL/od_c02_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_c02_bulkhead_C1_v01.stl`; re-import and measure; sections into
`03_Sections/` with `_v01` in their names; the sweep into `01_CAD/sweep_v01/`; the
check results into `01_CAD/check_od_c02_bulkhead_v01.json`; the REPORT into
`01_CAD/REPORT_od_c02_bulkhead_v01.md` with its JSON block. The 3MF is the
orchestrator's step (report the STL's triangle count, volume and bounding box).
Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9). If the Write tool refuses a
file, write it with Bash.

Notes from the OD-C01 and OD-C05 jobs: `min_wall` and `overhang_census` refuse
large faces at the default spacing (use 0.7 and say so); `overhang_census` cannot
close a curved face tangent at exactly 45° (report the analytic angle of each
window gable beside the census); gate REQ-04's round part with `locate_bore` on
the lower half-circle and the gable from sections; the named-exception faces are
selected by position and reported apart; OD-H11 is unsound (`brep_valid` 0), so
its booleans are INCONCLUSIVE by the row and its clearance is gated on distance.
Print orientation is **standing on the rear end z −240, build direction +Z**:
`overhang_census(build_dir=(0,0,1))`.

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A by its row), D-01a, D-01b (≥ 1.75 by the spec row), D-02,
D-03a and D-03b (with the named exception), D-04a, D-05a, D-05b, D-06a, D-07 (N/A),
J-05, E-06, REQ-01 … REQ-09 (REQ-09 Soft bench: INCONCLUSIVE, say so); plus
`exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | the plate, identity pose (frame = machine frame) |
| `00_Spec/inputs/OD-C03_pump_cradle.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | placed per OD-C01 spec §4 (x → +Z, y → −Y, z → +X at (0, 40, −205)) |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | at OD-C03's identity |
| `00_Spec/inputs/OD-C04_thermoblock_mount.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 | identity rotation at (0, 70, −140) |
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | at OD-C04's identity; unsound |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | x → X, y → +Z, z → −Y at (0, 180.06, 32) |
| `00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md` | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | the layout and joints (§4), A-04 |
| `00_Spec/inputs/reports/OD-C01_base_frame/REPORT_od_c01_frame_v02.md` | 78a03e899b024380df0d0bce9495ad3184ed13a0c454b8a2815a113e4d3bea7b | the measured placements |
| `00_Spec/INTAKE_v01.md` | 286637f9f4a7866dab73eff67bc32b02ca2c2ef791f08c566c53aac147453ce7 | the intake rows |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c02-bulkhead` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`, `atolye/templates/REPORT.md`. Library
index: `library/INDEX.md` (at most two cards). Tools documentation: `tools/README.md`.
Precedent for the scripts' shape and the placements:
`${OGUZ_JOBS}/20260930-od-c01-base-frame/01_CAD/` (its probes and `build_od_c01_frame_v02.py`).

## Findings to fix

None (first package).
