# WP-03 — designer brief, J3 package (build)

Job: 20260930-od-c03-pump-cradle · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c03_cradle_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02). Write the checks first
(`01_CAD/check_od_c03_cradle.py`), then the build (`01_CAD/build_od_c03_cradle.py`)
and the placement of OD-H01 and the assumed sleeve solid for the U-03, REQ-03 and
REQ-04 checks; export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c03_cradle_C1_v01.step`, the check assembly into
`02_STEP_STL/od_c03_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_c03_cradle_C1_v01.stl`; re-import and measure; sections into
`03_Sections/`; the sweep into `01_CAD/sweep_v01/`; the REPORT into
`01_CAD/REPORT_od_c03_cradle_v01.md` with its JSON block. Return the block your
skill defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with
the measured failure (D9).

## Plan amendments (spec 1.1, checked by the orchestrator)

Your J2 plan stands, with these amendments from spec 1.1 (its §4 C1, §5 and §6
rows A-03, A-04, A-06, A-07, A-11). Build to them and list each as a deviation
from the plan in REPORT §8; do not rewrite the plan. Your C-01 is answered by the
post block.

| Plan row | Amendment |
|---|---|
| foot | z −10.0 … 42.0 (envelope 80.0 × 40.0 × 52.0; U-02, D-02) |
| hole_xz | (±34.0, −4.0) and (±34.0, 37.0) (REQ-07, A-11) |
| rib1_z0, rib2_z0 | ribs over z 15.0 … 21.0 and 25.0 … 31.0 (REQ-01 windows z 15.5 … 20.5 and 25.5 … 30.5; REQ-02 at z 18.0 and 28.0; faces 15, 21, 25, 31) |
| post_w | one post block per side, z 13.0 … 33.0, 4.0 thick, inner face |x| 29.5, top y 0.0 (REQ-06); two slots per block, 6.0 × 2.5 clear, centred y 7.0 and z 18.0 / 28.0, 45° gable roofs, ligament ≥ 2.0 beside each slot (REQ-05, D-01b) |
| sleeve (A-03) | the tube ID 47.3, OD 53.3, z −6.0 … 32.0, cut back to |x| ≤ 23.5 so it clears both side plates; name it `od_h02_sleeve_assumed_A03` |
| §6 census | 2 saddle ribs, 2 post blocks, 4 slots, 4 Ø3.4 through-holes, 1 foot plate; re-tally the planar faces from the frozen feature list |

The OD-H01 joint (identity at the origin, axis +Z) stands. If the built cradle
reads under 2.0 to OD-H01 anywhere, that is a FAIL to fix within the fix cycles,
or a stop with the measured clearance (D9), never a changed spec value.

## Gate IDs to check (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row), REQ-01 … REQ-09
(REQ-09 bench: INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | the pump, placed at the identity pose by a joint at the origin, axis +Z (sound: validity 1/1/0, plan §2a) |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/params.json` | 21e02bf5c06fefb1f4fa9d4ade7810cfdcdc89ec533a29939c6aa624ba61c43c | the pump's parameters |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md` | 52b06473b31a2365a638bf0daa993d2dfa32f1121a0caefbb74ff58c72657fa2 | the pump's frame definition |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c03-pump-cradle` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/REPORT.md`. Tools documentation: `tools/README.md`.

## Findings to fix

None (first build). Deviations from the plan go in REPORT §8.
