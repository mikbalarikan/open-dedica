# WP-05 — reviewer brief (J4, the one review of build v01)

Job: 20260930-od-c07-valve-flowmeter-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 · target `od_c07_mount_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed valve and flowmeter mount OD-C07 of the
Open Dedica espresso machine: the plan `01_CAD/DESIGN_PLAN.md` (with the
amendments of `briefs/WP-03_designer.md` and `briefs/WP-04_designer.md`, which
are part of the plan), the REPORT `01_CAD/REPORT_od_c07_mount_v02.md` (v02 is the
report of record; `REPORT_od_c07_mount_v01.md` records the first attempt's stop on
U-03(b), answered by spec 1.2 with an unchanged part), the sections in
`03_Sections/`, and the exported files listed below. Never the designer's scripts
(`01_CAD/*.py`, `01_CAD/sweep_*`, `01_CAD/check_out_*`).

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b, with the spec 1.2 path for OD-H22: a −Y slide at
5.0 above the seat from y +45 to 0, then a 5.0 drop), U-04, U-05, U-06 (Soft),
U-07, U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c,
D-04d, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-01, J-02, J-03, J-04, J-05,
J-06 (N/A by its row), E-06, REQ-01 … REQ-09; the §P list P1–P6; the feature
census against the plan (15 features, spec U-05); positive controls for every
check family used. Rate the REPORT's §4 finding that six fit parameters pass only
at nominal (seat heights against the fixed OEM poses, the leg/window edge, the
deck thickness, the recess radius) and its §9 list. The deck wedges between the
screw clearance holes and the slit ends (1.79 / 1.90, under D-01b's 1.5 in spec
1.2) are to be measured by you from a section, not taken from the REPORT.

## Files (relative to the workspace; SHA-256 as the REPORT lists them)

| File | SHA-256 | Role |
|---|---|---|
| `02_STEP_STL/od_c07_mount_C1_v01.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | the part, AP242, one named solid |
| `02_STEP_STL/od_c07_assembly_C1_v01.step` | 50d126c13b945edca3cfd9a5082189ddbd6380bfbb6e59cd24bc71c546f6c9d7 | the check assembly (mount + OD-H22 + OD-H24 as placed) |
| `02_STEP_STL/od_c07_mount_C1_v01.stl` | 41bccd61c1fb0e82a7a8171c85da2128d0c01ca6906f80c03c5ffebf83de3c38 | the mesh (U-07) |
| `01_CAD/REPORT_od_c07_mount_v02.md` | 2b4a50f0a3ed54a9479c22234f6d1087d1970658c05c81416bf24f72ab8a5084 | the designer's self-check |
| `03_Sections/*.png` | (REPORT v02 §1) | eight sections |

Reference solids (inputs, for the assembly rows; place them by the spec §2
joints: OD-H24 datum frame = mount frame + (0, 0, 10.0), OD-H22 datum frame =
mount frame + (62.0, 0, 48.0)):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 |
| `00_Spec/inputs/OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a |

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount`; run
`source $HOME/oguz.env` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1, OCCT 7.9.3). Write only under `reviews/`
(`RV01_od_c07_mount_v01.md`, `.json`, and `RV01_work/`). Templates:
`atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
Tools documentation: `tools/README.md`.
