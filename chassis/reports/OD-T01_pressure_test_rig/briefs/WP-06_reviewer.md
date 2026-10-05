# WP-06 — reviewer brief (J4, the one review of build v02)

Job: 20261002-od-t01-pressure-test-rig · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.3 (ratified 2026-10-03 by the Usta's decision; SHA-256 9f329e11a2b8eba3921e81eddcc593e203550b65c65d588e11b2d9bb11330195) · concept C1 · target `od_t01_rig_v02` · review RV02 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v02 of the bench pressure-test rig OD-T01 of the Open Dedica
espresso machine: a printed closed frame (plate, two walls, base) that holds the
printed group head housing OD-G01 mouth down by its four M3 inserts, as the
machine's carrier OD-C05 does, so the housing with OD-G04 and a locked OD-G10 can
be pressurised with water on the bench. Review the plan `01_CAD/DESIGN_PLAN.md`
(with the answers of `briefs/WP-03_designer.md` and `briefs/WP-05_designer.md`,
which are part of the plan), the REPORT `01_CAD/REPORT_od_t01_rig_v02.md`, the
`*_v02*` sections in `03_Sections/`, and the exported files below. Never the
designer's scripts or their outputs (`01_CAD/*.py`, `01_CAD/d1_*`,
`01_CAD/sweep_v0*/`, `01_CAD/*.json`, `01_CAD/*.log`).

Build v02 answers RV01 (`reviews/RV01_od_t01_rig_v01.md`): F1, the plate is now
25 thick (y 135 … 160) with counterbores to y 140 leaving 5.0 under M3 × 10 heads;
F2, the apex band is ± 0.16. Re-measure every row on v02, say whether F1 and F2
are closed, and re-rate REQ-08 against spec 1.3 §4's hand calculation (window
section and head pull-through).

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
| `02_STEP_STL/od_t01_rig_C1_v02.step` | 18c9de8f013cb7ce84eba3ce104ab6fb01fc84f79f8524140cfadb9d3feaf810 | the part, AP242, one named solid |
| `02_STEP_STL/od_t01_rig_C1_v02.stl` | 183e58f0eda9287450d79d1a15aa3a4dabcf694449a6b82ae3a9ef9f24bfbd3f | the mesh (U-07) |
| `02_STEP_STL/od_t01_assembly_C1_v02.step` | c6caa17478e570e0b9200d813ee69fa674d68d2f9d6a91db216f4a5a1f18c072 | the designer's check assembly (for comparison only) |
| `01_CAD/REPORT_od_t01_rig_v02.md` | c7a125fa3d755d6dfa638d4d0253ddd2e21adf6d7c0c76b012de08095c1c77c9 | the designer's self-check (placed by the orchestrator from the returned text) |
| `reviews/RV01_od_t01_rig_v01.md` | ee5a1b93…1f9d (on file) | the review of v01 |
| `01_CAD/DESIGN_PLAN.md` | 544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d | the plan |
| `03_Sections/*.png` | REPORT §1 | six v02 sections |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | housing + OD-G04 + OD-G10, housing frame |
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | the housing alone |

## Environment

Workspace `/root/oguz-jobs/20261002-od-t01-pressure-test-rig`; run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`
(build123d 0.11.1, OCCT 7.9.3). Run long commands in the foreground with a
generous timeout. Write only under `reviews/` (`RV02_od_t01_rig_v02.md`, `.json`,
and `RV02_work/`); if a file write is blocked by a hook, return the file's full
text in your answer instead. Templates: `atolye/templates/VERDICT.md`; schema
`atolye/schemas/verdict.schema.json`. Tools documentation: `tools/README.md`.
Do not call any mcp__hearthbot__ tool.
