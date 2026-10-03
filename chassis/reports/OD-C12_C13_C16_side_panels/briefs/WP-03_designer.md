# WP-03 — designer brief, J3 package (build)

Job: 20261002-od-c12-c13-c16-side-panels · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-02; SHA-256 121c01a1c9e37e9e27c9b01b056af59be637d73ebeeb36864e9e03d50acfc222) · concept C1 · target `od_side_panels_v01` (part files `od_c12_left`, `od_c13_right`, `od_c16_bracket`) · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 on your plan `01_CAD/DESIGN_PLAN.md` (SHA-256
83911646533081bdd7b41f52a15d45f295aad1c0f69f63fc03f13481131c1498), as amended by spec 1.1 below.
Checks first, then the builds and the check assembly; export to
`02_STEP_STL/od_c12_left_C1_v01.step`, `od_c13_right_C1_v01.step`,
`od_c16_bracket_C1_v01.step` with their `.stl`, and
`02_STEP_STL/od_side_assembly_C1_v01.step`; sections to `03_Sections/`; the
sweep into `01_CAD/sweep_v01/`; the REPORT `01_CAD/REPORT_od_side_panels_v01.md`
(template `atolye/templates/REPORT.md`) answering every §5 row, per part where
a row applies to several, and the §P list.

## Answers to the plan's §7 questions (spec 1.1, §8)

- **Q1** → neither supports nor a new orientation nor a strip: the lip becomes a
  printable wedge. Rail x ±(110.0 … 117.0), y 205 … 215; lip section the
  triangle (±110.0, 215.0), (±116.6, 215.0), (±110.0, 218.81), z −280 … +80: its
  sloped face is 60° from the bed in the flat print; its outer edge keeps 0.40
  to the skirt's inner face. Check with `overhang_census` that it reads 60°, and
  that the lid has nothing in x ±(109.5 … 117) within the lip's zone.
- **Q2** → the panel ends are square at z −295.0 and +90.0 (where the corner
  arcs begin); no arc faces on the panels. Envelope 10.0 × 218.81 × 385.0.
- **Q3** → the REQ-02 range z −280 … +80 governs.
- **Q4** → OD-C12's relief floor at x −117.9 (0.9 deep, wall 2.1, ± 0.05).

## Gate IDs (spec 1.1 §5)

U-01 … U-07, U-08 (N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04d,
D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-06, REQ-01 … REQ-08 (REQ-08 Soft,
bench); plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`,
for each part file.

## Inputs

As WP-02 (the eight reference STEPs, hashes unchanged).

## Environment

Workspace: `/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels`. Run `source /root/oguz-env/env.sh` in every shell command
that runs Python, then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`.
Traps: `library/BUILD123D-NOTES.md`. Write only under `01_CAD/`,
`02_STEP_STL/`, `03_Sections/`. Do not call any mcp__hearthbot__ tool.

## Findings to fix

None (first build).
