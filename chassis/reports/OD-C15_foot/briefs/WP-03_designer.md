# WP-03 — designer brief, J3 package (build)

Job: 20261001-od-c15-feet · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-01; SHA-256 8be93063444f24fe758d3d181dbca1e0369534f16ed985d80944ab79126584d9) · concept C1 (chosen) · target `od_c15_foot_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 on your plan `01_CAD/DESIGN_PLAN.md` (SHA-256
1770a3c3b6f65e7bee64734873ee94039d3a0bdd82fd55322948db116204ccdf), as amended by
spec 1.1 below. Checks first (`01_CAD/check_od_c15_foot.py`), then the build
(`01_CAD/build_od_c15_foot.py`) and the check assembly
(`01_CAD/build_check_assembly.py`); export to `02_STEP_STL/od_c15_foot_C1_v01.step`,
`.stl` and `02_STEP_STL/od_c15_assembly_C1_v01.step`; sections to `03_Sections/`;
the sweep into `01_CAD/sweep_v01/`; the REPORT `01_CAD/REPORT_od_c15_foot_v01.md`
(template `atolye/templates/REPORT.md`) answering every §5 row and the §P list.

## Answers to the plan's §7 questions (spec 1.1, §7 and §8)

- **Q1** → option (a): the bed-edge chamfer (z 0) is 0.50 along the axis × 0.29
  radial, 60° from horizontal (REQ-04); the top-face annulus therefore runs to
  Ø17.42 (REQ-01). D-03a is gated with `overhang_census` on that face.
- **Q2** → yes: J-05 is measured on the ring z 2.5 … 10 only; D-04c on the screw
  shank below the seat only. Both rows now say so.
- **Q3** → the 3MF is written at J5 from the reviewed STL by the orchestrator;
  not your deliverable.

## Gate IDs (spec 1.1 §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row),
J-05, J-06, REQ-01 … REQ-07; plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | mating part for the check assembly, in its own (machine) frame |

## Environment

Workspace: `/home/claude/oguz-env/jobs/20261001-od-c15-feet`. Run
`source /home/claude/oguz-env/env.sh` in every shell command that runs Python,
then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`.
Traps: `library/BUILD123D-NOTES.md`. Write only under `01_CAD/`, `02_STEP_STL/`,
`03_Sections/`.

## Findings to fix

None (first build).
