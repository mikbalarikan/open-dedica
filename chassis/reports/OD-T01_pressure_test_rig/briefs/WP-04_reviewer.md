# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20261002-od-t01-pressure-test-rig · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-03; SHA-256 0036578bbb64a9fe6fac276b06938b135a37e9afc9de4e906ac8d5cfaa6db9f4) · concept C1 · target `od_t01_rig_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the bench pressure-test rig OD-T01 of the Open Dedica
espresso machine: a printed closed frame (plate, two walls, base) that holds the
printed group head housing OD-G01 mouth down by its four M3 inserts, as the
machine's carrier OD-C05 does, so the housing with OD-G04 and a locked OD-G10 can
be pressurised with water on the bench. Review the plan `01_CAD/DESIGN_PLAN.md`
(with the answers of `briefs/WP-03_designer.md`, which are part of the plan), the
REPORT `01_CAD/REPORT_od_t01_rig_v01.md`, the sections in `03_Sections/`, and the
exported files below. Never the designer's scripts (`01_CAD/*.py`, `01_CAD/d1_*`,
`01_CAD/sweep_v01/`, `01_CAD/*.json`, `01_CAD/*.log`).

Spec 1.2 differs from 1.1 (the build's spec) only in REQ-03's apex band (± 0.15)
and pair-B threshold (≥ 10.87, A-12 head ≤ Ø17.7), so its tolerances stack with
R 30.0 ± 0.1; the geometry was not rebuilt. Rate the REPORT's §4 sweep findings
against spec 1.2 and its §9 list.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-06a, D-07 (N/A by its row), J-05 (N/A
by its row), REQ-01 … REQ-07, REQ-08 (Soft, bench: INCONCLUSIVE with a rating);
the §P list P1–P6; the feature census against the plan (spec U-05); positive
controls for every check family used. Place the housing set by spec §2 yourself
(housing x → X, y → +Z, z → −Y, origin (0, 110.06, 0)) from
`od_g01_assembly_C1_v03.step`, identifying its three solids by measurement; do not
take the poses from the designer's assembly file. OD-G10 is not a sound solid:
spec REQ-04 reads its interference rows as `clearance > 0` with
`detail["inside"] == False`.

## Files (relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `02_STEP_STL/od_t01_rig_C1_v01.step` | cc6b1c721fd34f74232c4cee504c95c0852573fa351411ca12a02c27904c9f5c | the part, AP242, one named solid |
| `02_STEP_STL/od_t01_rig_C1_v01.stl` | 1b2985d19a6fe86930bdf4ec448b78576ec830f6ee1f5c513a1ae2e63077d3a5 | the mesh (U-07) |
| `02_STEP_STL/od_t01_assembly_C1_v01.step` | 407386d44f5483aa2d2e6eab7eb72a47749aafbdb06252de5dbecfc3acf7774b | the designer's check assembly (for comparison only) |
| `01_CAD/REPORT_od_t01_rig_v01.md` | d44d3356664af278e29003e388db94c2aec862bc9a2b4a574604a3f50ca056b1 | the designer's self-check (placed by the orchestrator, text unchanged but for the model name) |
| `01_CAD/DESIGN_PLAN.md` | 544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d | the plan |
| `03_Sections/*.png` | REPORT §1 | five sections |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | housing + OD-G04 + OD-G10, housing frame |
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | the housing alone |

## Environment

Workspace `/root/oguz-jobs/20261002-od-t01-pressure-test-rig`; run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1, OCCT 7.9.3). Run long commands in the foreground with a
generous timeout. Write only under `reviews/` (`RV01_od_t01_rig_v01.md`, `.json`,
and `RV01_work/`); if a file write is blocked by a hook, return the file's full
text in your answer instead. Templates: `atolye/templates/VERDICT.md`; schema
`atolye/schemas/verdict.schema.json`. Tools documentation: `tools/README.md`.
Do not call any mcp__hearthbot__ tool.
