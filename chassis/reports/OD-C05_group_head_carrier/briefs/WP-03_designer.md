# WP-03 — designer brief, J3 package (build v01)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c05_carrier_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02, written to spec 1.0), with the
amendments below (spec 1.1, which settles the plan's §8 conflicts K-1 and K-2 and
takes the group head axis from the OD-C01 layout). Write `01_CAD/build_od_c05_carrier.py`
(parametric, every §4 parameter a named value) and `01_CAD/check_od_c05_carrier.py`.
Export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c05_carrier_C1_v01.step`, the check assembly (carrier + OD-G01 +
OD-G04 as placed) into `02_STEP_STL/od_c05_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_c05_carrier_C1_v01.stl`; re-import and measure; sections into
`03_Sections/` with `_v01` in their names; the sweep into `01_CAD/sweep_v01/`; the
check results into `01_CAD/check_od_c05_carrier_v01.json`; the REPORT into
`01_CAD/REPORT_od_c05_carrier_v01.md` with its JSON block. The 3MF is written by
the orchestrator from the STL (no 3MF library in the venv): report the STL's
triangle count and volume so it can be checked. Return the block your skill
defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with the
measured failure (D9). If the Write tool refuses a file, write it with Bash.

## Plan amendments (spec 1.1, checked by the orchestrator)

The plan stands, except these rows. Build to them and list each as a deviation
from the plan in REPORT §8; do not rewrite the plan.

| Plan row | Amendment (spec 1.1) |
|---|---|
| y_floor | −175.0 (the axis 175 above the floor: OD-C01 spec 1.0 §7, A-01; spec 1.1 §2, A-03). The foot underside is y −175.0 (REQ-05), the foot y −175.0 … −171.0 |
| F01 wall | y −175.0 … +50.0; the two top corners **R 6.0 about (±44.0, 44.0)**, concentric with the top holes (K-1 option 2: web to the Ø6.5 counterbore 2.75). corner_r = 6.0, centres (±44, 44) |
| F03 gussets | legs 40 unchanged: on the wall from y −171.0 to −131.0, on the foot from z −29.94 to −69.94 |
| low_c_y / low_apex_y | lower window R 25.0 about **(0, −110.0)**, apex y −74.64 (REQ-08); the REQ-08 probes and positive controls move with it (θ 90° inner = 35.36 from the new centre, θ 270° inner = 25.0); the section through it at y = −110 |
| U-02 / envelope_within_spec | 100.0 × 225.0 × 45.0; y −175.0 … +50.0 |
| D-02 | 100.0 × 45.0 on the bed, 225.0 tall (A-08) |
| D-03a | the crowns of the eight horizontal Ø3.4 holes and Ø6.5 counterbores along Z are the **named exception of §5** (K-2 option 1): exclude those eight cylindrical faces from the census by position, report their least angle separately inside the exception, and gate the rest at ≥ 45° |
| cb_d, cb_depth, hole_d, hole_xy | unchanged (Ø6.5 × 2.0, Ø3.4, (±44, ±44)); the sweep's Ø6.6 rung must now pass D-01b (predicted web 2.70) |
| §6 census | the two convex cylindrical faces are now R 6 (count unchanged) |

Nothing else changes: the OD-G01 joint (identity), the OD-G04 placement (+6.05°
about Z, then z −6.82), the hub window R 30 with its 45° gable, the foot holes at
(±35, z −40 / −60), the foot's rear edge at z −69.94, REQ-07's min_z ≥ −70.0.
Every other value is the plan's. If a built value fails a Hard row, fix within the
fix cycles or stop with the measured failure; never change a spec value.

## Gate IDs to check (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a (with the named exception), D-03b (with the named exception), D-04a,
D-06a, D-07 (N/A by its row), E-06, REQ-01 … REQ-09 (REQ-09 Soft bench:
INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | the housing, identity pose (sound: validity 1/1/0, plan §1) |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | the gasket support, placed per plan §5 |
| `01_CAD/DESIGN_PLAN.md` | 41b80f841cb6ee700fe5dc7590b8b1db5403458e469af64b5673cf5f0232eced | your plan (WP-02) |
| `01_CAD/probe/*` | (hashed in the plan) | your probes; reuse their placement code |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c05-group-head-carrier` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/REPORT.md`. Tools documentation: `tools/README.md`.
Precedent for the scripts' shape: `${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount/01_CAD/`.

## Findings to fix

None (first build).
