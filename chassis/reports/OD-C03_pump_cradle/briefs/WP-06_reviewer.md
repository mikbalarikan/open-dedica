# WP-06 — reviewer brief (J4, the one review of build v02)

Job: 20260930-od-c03-pump-cradle · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 · target `od_c03_cradle_v02` · review RV02 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v02 (the round after RV01, `reviews/REVISE_PACKET_RV01.md`) of the printed pump cradle OD-C03 of the Open Dedica
espresso machine: the plan `01_CAD/DESIGN_PLAN.md` (with the amendments of
`briefs/WP-03_designer.md` and `briefs/WP-05_designer.md`, which are part of the plan), the REPORT
`01_CAD/REPORT_od_c03_cradle_v02.md`, and the exported files listed below.
Never the designer's scripts (`01_CAD/*.py`, `01_CAD/probes/`, `01_CAD/sweep_v01/`, `01_CAD/sweep_v02/`). The v01 files stay as the previous round's record; review v02 only..

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row),
REQ-01 … REQ-09 (REQ-09 is a Soft bench gate in spec 1.2: INCONCLUSIVE with a risk rating, never a blocking finding); the §P list P1–P6; the
feature census against the plan (as amended: 2 ribs, 2 post blocks, 4 slots, 4
holes, 1 foot); positive controls for every check family used.

The assumed sleeve solid (spec A-03) is the designer's own construction, named
`od_h02_sleeve_assumed_A03` in the check assembly: gate REQ-04 and U-03 against it
as the spec writes them, and rate what rests on it. Check that RV01's F2 is answered (rib 1 at z −3 … 3 brackets OD-H01's centre of mass, REPORT §7) and re-rate F3 … F6 against spec 1.2's A-07, A-03, A-01 and the zero-margin rows.

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `01_CAD/REPORT_od_c03_cradle_v02.md` | 3404a729616141242016ad439668c65a1960cbe6f99f2a449e5a903848d93a85 |
| `01_CAD/DESIGN_PLAN.md` | 7e86466421a4ad81e87dd87bb93215966e3a0b974e33869163b55aaa42bd6540 |
| `01_CAD/check_od_c03_cradle_v02.json` | 915202548c8c46c3b2f9adc0103ab2a63f915384913fd9fecf131d8b83373921 |
| `01_CAD/sections_od_c03_cradle_v02.json` | 50193e6b41dfdbea8d7d5c3ddeb9642399d2836d3821802b58ecb37b45e3d007 |
| `02_STEP_STL/od_c03_assembly_C1_v02.step` | 8e1a6ea8ff66acecdd2cffdde41c1d7635541f4b34e9034f55ce6c4efaf43a14 |
| `02_STEP_STL/od_c03_cradle_C1_v02.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 |
| `02_STEP_STL/od_c03_cradle_C1_v02.stl` | 529a0cc2033cddb00ee16715448a8e0e546f08eb05eb6bd1e6c20ce8a3776be4 |
| `03_Sections/od_c03_cradle_v02_assembly_xy_z0p0.png` | e36596521f8a6c8d0cca5d8bcddc8c58cf6708fc2192c48223fe1fc9379b7b24 |
| `03_Sections/od_c03_cradle_v02_assembly_xy_z28p0.png` | 4e58b33781602ce7e7833dbfa77a0f16055c3ba4fd5c22052b318775e65b2083 |
| `03_Sections/od_c03_cradle_v02_assembly_yz_x0p0.png` | 86a77ec2317d2f64fdfc5878ebac31b9492b3dd6837bcd53db906ae3348123cf |
| `03_Sections/od_c03_cradle_v02_xy_z0p0.png` | 51dc7f09bbf3b3e95a6b6623decb2430445b9504e50ab4a9decb1f602895faa7 |
| `03_Sections/od_c03_cradle_v02_xy_z17p0.png` | 603139490d9c8a947e45d2f8aeb257b0a6ecad102d47e89d3987367439825df3 |
| `03_Sections/od_c03_cradle_v02_xy_z28p0.png` | 4364ee45b5b8a12674cf4f0d509e7dd901cde4352e25421d9acff4333d056502 |
| `03_Sections/od_c03_cradle_v02_xz_y38p5.png` | 8ad305e86b536a0132bfac697ec2d0f56694afd3187a5fe40e7332ff48a602cc |
| `03_Sections/od_c03_cradle_v02_xz_y7p0.png` | 1f44f2bbdb0390b6380bf0f7b29e18f4b0a10364e5ee45ef2899a237491ee3c5 |
| `03_Sections/od_c03_cradle_v02_yz_x0p0.png` | 3f1dbbc197ea6daef045738ba8ad42f889c5aa3f93ad38d2eb65a687163d7328 |
| `03_Sections/od_c03_cradle_v02_yz_x31p5.png` | 1f75434f7b2887c7321dbc50545af88d24e5f705f7e0d5fdc7a233177a588504 |
| `03_Sections/od_c03_cradle_v02_yz_x34p0.png` | 577bc611c4691e5ddcc7118f907404b2a8eee2303356ef7c6fc4dbfbd73e1fd5 |

Reference solid (input, for the assembly rows):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 |

OD-H01 is placed at the identity pose (joint at the origin, axis +Z); the REPORT
reads it sound (validity 1/1/0).

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c03-pump-cradle` (`/home/claude/oguz-jobs/20260930-od-c03-pump-cradle`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV02_od_c03_cradle_v02.md`, `.json`, and `RV02_work/`); if
the Write tool refuses a file, write it with Bash.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
