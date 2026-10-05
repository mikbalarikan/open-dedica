# OD-T01 group head bench pressure-test rig — design job record

This folder is the record of the CAD job that designs `OD-T01`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20261002-od-t01-pressure-test-rig/` so that any session, on any machine, can
continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frames and poses, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every value the part touches as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `bom_rows.csv`, other extracts | the inputs written or extracted for this job (the rest are repository files, below) |
| `briefs/` | the subagent briefs |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | plan, scripts, REPORT, exports, sections, the verdict |

The rig is a closed printed frame (plate, two walls, base) that holds the printed
group head housing OD-G01 mouth down by its four inserts, exactly as the carrier
OD-C05 does, so the housing with OD-G04 and a locked OD-G10 can be pressurised
with water on the bench. Its result closes OD-G01 REQ-12.

Repository inputs are not copied here; the job reads them under these names in
`00_Spec/inputs/` (the exact list with SHA-256 values is `00_Spec/INTAKE_v01.md` §1):

- `chassis/reports/OD-G01_group_head_housing/02_STEP_STL/od_g01_assembly_C1_v03.step` and `od_g01_housing_C1_v03.step` (same names)
- `chassis/OD-C05_group_head_carrier.step`; `step/OD-G04_brewing_gasket_support.step`, `step/OD-G10_portafilter.step` (same names)
- `chassis/reports/OD-G01_group_head_housing/00_Spec/DESIGN_SPEC.md` as `OD-G01_DESIGN_SPEC.md`, its `reviews/RV01_od_g01_housing_v03.md` as `OD-G01_RV01.md` and `reviews/REVISE_PACKET_RV01.md` as `OD-G01_REVISE_PACKET_RV01.md`; OD-C05's spec as `OD-C05_DESIGN_SPEC.md`; `chassis/README.md` as `CHASSIS_README.md`

## Status (2026-10-03)

J6_CLOSE (PR #52 merged 2026-10-05). Build v01 (15 mm plate) RV01 approved on assumptions with F1: the plate's factor through the hub window was ≈ 1.5. The Usta chose a 25 mm plate: spec 1.3, build v02 (attempt 2 of 2), RV02 `APPROVED_ASSUMPTION_CONDITIONAL` (F1 MEDIUM: screw-head bearing ≈ 47 MPa and infill, answered in the test procedure). J6 waits on the bench test.

## Resume

1. Clone both repositories side by side (`oguz-atolye` and `open-dedica`), on the
   working branch named in the session's task.
2. Toolchain: `uv` with Python 3.13 (`uv python install 3.13`). Set the workshop
   variables outside both checkouts, for example on Linux:
   ```
   export OGUZ_WORK=$HOME/oguz-work OGUZ_JOBS=$HOME/oguz-jobs OGUZ_DELIVERY=$HOME/oguz-delivery OGUZ_ARTIFACTS=$HOME/oguz-artifacts
   ```
   then from the `oguz-atolye` root run
   `uv run tools/run.py python -c "import build123d"` once: it creates the venv
   (build123d 0.11.1, OCCT 7.9.3).
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-T01_pressure_test_rig $OGUZ_JOBS/20261002-od-t01-pressure-test-rig`,
   then copy the repository inputs into `00_Spec/inputs/` under the names above,
   and check the hashes against `00_Spec/INTAKE_v01.md` §1.
4. `uv run tools/jobstate.py check 20261002-od-t01-pressure-test-rig`, then `show`:
   `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-T01_pressure_test_rig.step`,
`.stl`, `.3mf`, the parametric build script under `chassis/src/OD-T01_pressure_test_rig/`,
and the test procedure `chassis/OD-T01_TEST_PROCEDURE.md`.
