# WP-03 — designer brief, J3 package (build)

Job: 20261002-od-t01-pressure-test-rig · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-02; SHA-256 c3508387b397a31087963244b248b47ed6992e493e181961b4a48b6402517285) · concept C1 (chosen) · target `od_t01_rig_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 on your plan `01_CAD/DESIGN_PLAN.md` (SHA-256
544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d), as amended by
spec 1.1 below. Checks first (`01_CAD/check_od_t01_rig.py`), then the build
(`01_CAD/build_od_t01_rig.py`) and the check assembly; export to
`02_STEP_STL/od_t01_rig_C1_v01.step`, `.stl` and
`02_STEP_STL/od_t01_assembly_C1_v01.step`; sections to `03_Sections/`; the sweep
into `01_CAD/sweep_v01/`; the REPORT `01_CAD/REPORT_od_t01_rig_v01.md` (template
`atolye/templates/REPORT.md`) answering every §5 row and the §P list.

## Answers to the plan's §7 questions (spec 1.1, §7 and §8)

- **Q1** → the walls stop at z +40: each wall spans z −60 … +40 only; the plate
  and the base keep z −60 … +60 (the seat, the screws and the bench wings are
  unchanged). In the print (build +Z) the plate and base simply continue above
  the walls' end; no new overhang. REQ-04a keeps φ −60° … +15°, ≥ 5.0.
- **Q2** → the axis-distance check is accepted; the head size is ledgered as A-12
  (≤ Ø17.9). REQ-03 now says so.
- **Q3** → confirmed: every teardrop at 45.1° (window apex z +42.51, counterbore
  apex 4.61, bench-hole apex 3.19); §4, D-03a and REQ-03 carry these values.
- **Q4** → §2 now reads ≈ 34° (measured); no check changes.
- **Q5** → the fallback is accepted: every `interference` with OD-G10 is read as
  `clearance > 0` with `detail["inside"] == False` (REQ-04 says so), as OD-G01 A-28.

## Gate IDs (spec 1.1 §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A), D-01a,
D-01b, D-02, D-03a, D-03b, D-04a, D-06a, D-07 (N/A), J-05 (N/A), REQ-01 … REQ-07,
REQ-08 (Soft, bench); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs

As WP-02 (same files and SHA-256 values in `00_Spec/inputs/`).

## Environment

Workspace: `/root/oguz-jobs/20261002-od-t01-pressure-test-rig`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Traps:
`library/BUILD123D-NOTES.md`. Write only under `01_CAD/`, `02_STEP_STL/`,
`03_Sections/`. Do not call any mcp__hearthbot__ tool. If a file write is blocked
by a hook, return the file's full text in your answer instead.

## Findings to fix

None (first build).
