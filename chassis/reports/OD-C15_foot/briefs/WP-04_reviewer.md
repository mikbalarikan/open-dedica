# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20261001-od-c15-feet · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-01; SHA-256 a24c23f25b2f02b916d89beb76e3db5c899d02d518c3775c402b5ed27e0e496f) · concept C1 · target `od_c15_foot_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed TPU foot OD-C15 of the Open Dedica
espresso machine (four per machine, under the four Ø3.4 feet holes of the base
frame OD-C01, each held by an M3×12 button-head screw from the plate top into an
M3 hex nut captive in the foot): the plan `01_CAD/DESIGN_PLAN.md` (with the
answers of `briefs/WP-03_designer.md`, which are part of the plan), the REPORT
`01_CAD/REPORT_od_c15_foot_v01.md`, the sections in `03_Sections/`, and the
exported files below. Never the designer's scripts (`01_CAD/*.py`,
`01_CAD/sweep_v01/`, `01_CAD/check_*`, `01_CAD/*_stdout*`, `01_CAD/*.json`).

Spec 1.2 differs from 1.1 (the build's spec) only in REQ-03's parenthetical
per-side range (0.16 → 0.165, the arithmetic of its own limits); the geometry was
not rebuilt. Rate the REPORT's §4 sweep finding against spec 1.2 and its §9 list.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row),
J-05, J-06, REQ-01 … REQ-07; the §P list P1–P6; the feature census against the
plan (spec U-05); positive controls for every check family used. The joint of
spec §2 (foot x → X, y → +Z, z → −Y, origins (±110, −6, +90) and (±110, −6, −295)
in the OD-C01 frame) is to be checked by your own placement against the OD-C01
input, not taken from the assembly file.

## Files (relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `02_STEP_STL/od_c15_foot_C1_v01.step` | 830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7 | the part, AP242, one named solid |
| `02_STEP_STL/od_c15_foot_C1_v01.stl` | cc66c8c8961c9becda42111b1d3c0246c81940d4fc9fb98fe94036c4d8e4f20c | the mesh (U-07) |
| `02_STEP_STL/od_c15_assembly_C1_v01.step` | e3228ea2f667eeb98ef1add9c37c38c8bbab9adb7d7a85bed61105f58d261d8f | the check assembly (plate, foot_1…4, screw_1…4, nut_1…4) |
| `01_CAD/REPORT_od_c15_foot_v01.md` | df020639538f2faa6f406485432f0d52f25ebf3cf57fbc8ae6f9dfbbb089a242 | the designer's self-check (placed by the orchestrator, text unchanged but for the model name) |
| `03_Sections/*.png` | REPORT §1 | five sections |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | the reference solid for the assembly rows |

## Environment

Workspace `/home/claude/oguz-env/jobs/20261001-od-c15-feet`; run
`source /home/claude/oguz-env/env.sh` in every shell command that runs Python,
then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1, OCCT 7.9.3). Write only under `reviews/`
(`RV01_od_c15_foot_v01.md`, `.json`, and `RV01_work/`). Templates:
`atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
Tools documentation: `tools/README.md`.
