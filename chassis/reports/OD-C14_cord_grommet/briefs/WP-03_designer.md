# WP-03 — designer brief, J3 package (build)

Job: 20261002-od-c14-cord-grommet · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-02; SHA-256 8a02f52c3e2153b0ba0b77512dcffdbe93b60d075bb79daa542cd69d8c41ae19) · concept C1 · target `od_c14_grommet_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 on your plan `01_CAD/DESIGN_PLAN.md` (SHA-256
731a84955f7533b49d2a0e8f4f4228dffdf0576d64d39782f92c1ed512810e4b), as amended by spec 1.1 below.
Checks first (`01_CAD/check_od_c14_grommet.py`), then the build
(`01_CAD/build_od_c14_grommet.py`) and the check assembly; export to
`02_STEP_STL/od_c14_grommet_half_C1_v01.step`, `.stl` and
`02_STEP_STL/od_c14_assembly_C1_v01.step`; sections to `03_Sections/`; the
sweep into `01_CAD/sweep_v01/`; the REPORT `01_CAD/REPORT_od_c14_grommet_v01.md`
(template `atolye/templates/REPORT.md`) answering every §5 row and the §P list.

## Answers to the plan's §7 questions (spec 1.1, §8)

- **Q1** → 60° from horizontal governs: the flank is 0.5 radial over 0.866 axial (the groove and collar diameters changed, Q4).
- **Q2** → the tie-head box is x 92.5 … 97.5, y 36.45 … 42.45, z −298.8 … −293.8 (5 along X and Z, 6 along Y, on the band at +Y); it and the tie envelope sit 0.20 ± 0.05 from the wall's flat inner face (the axial play, designed) and ≥ 0.5 from OD-C11's gussets and flange.
- **Q3** → yes: one split plane carried by two faces.
- **Q4** → the sweep range is right; spec 1.1 gives margin instead: neck and collar Ø11.3 (0.35 per side), groove Ø10.3 (wall 1.65 nominal, 1.60 at the corner).
- **Q5** → the neck runs to z −298.8, 0.2 beyond the inner face; the groove is z −298.8 … −293.6; the flank ends at z −292.734; the collar ends at z −291.0. The envelope is unchanged.

## Gate IDs (spec 1.1 §5)

U-01 … U-07, U-08 (N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04d, D-06a,
D-07 (N/A), J-06, E-11, REQ-01 … REQ-05 (REQ-05 Soft, bench); plus
`exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs

As WP-02 (OD-C11 and OD-C01 STEPs, hashes unchanged).

## Environment

Workspace: `/root/oguz-jobs/20261002-od-c14-cord-grommet`. Run `source /root/oguz-env/env.sh` in every shell command
that runs Python, then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`.
Traps: `library/BUILD123D-NOTES.md`. Write only under `01_CAD/`,
`02_STEP_STL/`, `03_Sections/`. Do not call any mcp__hearthbot__ tool.

## Findings to fix

None (first build).
