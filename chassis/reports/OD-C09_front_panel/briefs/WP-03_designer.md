# WP-03 — designer brief, J3 package (build)

Job: 20261002-od-c09-front-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-02; SHA-256 6aaf9a01a7577144ffae18502862f79c6b25debc12ace188c4d0cc15a86d655f) · concept C1 (chosen) · target `od_c09_front_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 on your plan `01_CAD/DESIGN_PLAN.md` (SHA-256
277daf919fa3fd2dc2ff89c8a16e546b29a9df55086fcfd079d13adc35381071), as amended by
spec 1.1 below. Checks first (`01_CAD/check_od_c09_front.py`), then the build
(`01_CAD/build_od_c09_front.py`) and the check assembly; export to
`02_STEP_STL/od_c09_front_C1_v01.step`, `.stl` and
`02_STEP_STL/od_c09_assembly_C1_v01.step`; sections to `03_Sections/`; the sweep
into `01_CAD/sweep_v01/`; the REPORT `01_CAD/REPORT_od_c09_front_v01.md`
(template `atolye/templates/REPORT.md`) answering every §5 row and the §P list.

## Answers to the plan's §7 questions (spec 1.1, §7 and §8)

- **Q1** → option (b), refined: the OD-E02 pose stays as §2. REQ-04 now asks B2's
  foremost point ≥ +97.5 and B1's and B3's sloped tops ≥ +95.0 (≤ 2.0 recessed
  in their Ø15 holes). Moving the board forward would put it into the wall.
- **Q2** → both boss end faces at z +85.485, the measured flat; a designed
  contact on the flat part of each face.
- **Q3** → M3 × 18 ISO 4762 (DIN 912) socket head, 4.78 into the insert; A-03
  says so. The screws are not in the part file; the check assembly may carry
  their envelopes.
- **Q4** → Ø11 bosses, each with a relief around the neighbouring cap collar at
  the collar's radius + 0.5; J-05 (≥ 3.0 around the bore) and E-01 (≥ 0.5) both
  hold. U-05 counts the two reliefs.
- **Q5** → accepted: three round Ø15 holes on the measured cap axes.
- **Q6** → the `clearance` fallback (`clearance > 0`, `detail["inside"] == False`)
  for every interference row involving OD-G10 or OD-E02 (REQ-05 says so).
- **Q7** → accepted as written; E-01's check cell now states it.

## Gate IDs (spec 1.1 §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A), D-01a,
D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-01,
E-05, E-06, REQ-01 … REQ-07, REQ-08 (Soft, bench); plus `exactly_one_solid`,
`feature_census`, `envelope_within_spec`.

## Inputs

As WP-02 (same files and SHA-256 values in `00_Spec/inputs/`).

## Environment

Workspace: `/root/oguz-jobs/20261002-od-c09-front-panel`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Traps:
`library/BUILD123D-NOTES.md`. Write only under `01_CAD/`, `02_STEP_STL/`,
`03_Sections/`. Do not call any mcp__hearthbot__ tool. If a file write is blocked
by a hook, return the file's full text in your answer instead.

## Findings to fix

None (first build).
