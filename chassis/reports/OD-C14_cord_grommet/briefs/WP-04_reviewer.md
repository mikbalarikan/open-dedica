# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20261002-od-c14-cord-grommet · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-02; SHA-256 180292d0a129ba1bd3b66256ec490ebe5728b9bb6e51e15c5fbc7e5bdfd62b7d) · concept C1 · target `od_c14_grommet_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed split cord grommet OD-C14 of the Open
Dedica espresso machine: one half (the part file), used twice (the second turned
180° about the cord's axis), seated in the delivered back panel OD-C11's Ø12 cord
hole at (x 95, y 30) around the Ø7.0 mains cord and closed by a cable tie in a
groove inside the wall. Read the plan `01_CAD/DESIGN_PLAN.md` (with the answers
of `briefs/WP-03_designer.md`, which are part of the plan), the REPORT
`01_CAD/REPORT_od_c14_grommet_v01.md`, the sections in `03_Sections/`, and the
exported files below. Never the designer's scripts or their outputs
(`01_CAD/*.py`, `01_CAD/check_v01/`, `01_CAD/sweep_v01/`).

Spec 1.2 differs from 1.1 (the build's spec) only in U-03's derived bands (the
axial play 0.20 ± 0.10, the closed pose by the measured split offset, the squeeze
0.40 ± 0.07, the cord envelope on the measured bore); the geometry was not
rebuilt. Rate the REPORT's §4 sweep findings against spec 1.2. The REPORT was
placed by the orchestrator because a session hook refused the designer's write;
its text is the designer's, unchanged but for the model name.

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-07, U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b, D-04d,
D-06a, D-07 (N/A by its row), J-06, E-11, REQ-01 … REQ-05 (REQ-05 Soft, bench);
the §P list; the feature census against the plan; positive controls for every
check family used. Build your own check assembly from the part file and the two
inputs (the copy turned 180° about the measured hole axis, your own cord, tie and
head envelopes per spec §5), not from the designer's assembly file.

## Files (relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `02_STEP_STL/od_c14_grommet_half_C1_v01.step` | 55ce2a3e6a68458e6f97f26a58b05d4691bd69f310105551f98b28fcdb0a0680 | the part, AP242, one named solid |
| `02_STEP_STL/od_c14_grommet_half_C1_v01.stl` | 645a8dde3b824729be2fe225589561b529c879c2bf9fbb5b10d927f102eafaa8 | the mesh (U-07) |
| `02_STEP_STL/od_c14_assembly_C1_v01.step` | a21a8f9d88d7f1ec8a97103c980ec2f16a798c9376a0d124be1c3b3b8a8b992b | the designer's check assembly (for reference) |
| `01_CAD/REPORT_od_c14_grommet_v01.md` | 35dc2fd807e1ced5acbf8d11287cab2da29d9a6633e7226b106f74738db4e821 | the designer's self-check |
| `01_CAD/DESIGN_PLAN.md` | 731a84955f7533b49d2a0e8f4f4228dffdf0576d64d39782f92c1ed512810e4b | the plan |
| `03_Sections/*.png` | REPORT §1 | six sections |
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | reference solid, identity |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | reference solid, identity |

## Environment

Workspace `/root/oguz-jobs/20261002-od-c14-cord-grommet`; run `source /root/oguz-env/env.sh` in every shell command that
runs Python, then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`.
Write only under `reviews/` (`RV01_od_c14_grommet_v01.md`, `.json`, and
`RV01_work/`). Templates: `atolye/templates/VERDICT.md`; schema
`atolye/schemas/verdict.schema.json`. Tools: `tools/README.md`. Do not call
any mcp__hearthbot__ tool. If a file write is refused, return its full text in
your reply instead.
