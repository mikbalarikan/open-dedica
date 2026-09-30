# OD-C01 printed base frame — design job record

This folder is the record of the CAD job that designs `OD-C01`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20260930-od-c01-base-frame/` so that any session, on any
machine, can continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frame, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every dimension of the reference part as an `X-##` row |
| `briefs/` | the subagent briefs sent so far |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | added as the job advances: plan, scripts, REPORT, exports, sections, the verdict |

Inputs are not copied here: the job reads the delivered `chassis/OD-C03_pump_cradle.step`
and `chassis/OD-C04_thermoblock_mount.step`, the OD-G01 housing's build v02 STEP
(`chassis/reports/OD-G01_group_head_housing/02_STEP_STL/od_g01_housing_C1_v02.step`),
the library STEP files `step/OD-H01_ulka_ep5_pump.step` and `step/OD-H11_thermoblock.step`
with their reports under `step/reports/` (`README.md`; for OD-H11 also `export_check.json`),
the specs of the three mounts (`chassis/reports/OD-C03_pump_cradle/00_Spec/DESIGN_SPEC.md`
1.2, `OD-C04_thermoblock_mount` 1.2, `OD-C05_group_head_carrier` 1.0), the BOM rows of
`docs/bom.csv` that touch the part, and two files the orchestrator wrote from the
project's own documents (`REQUEST.md`, `PROJECT_RULES.md`); their SHA-256 values are
in `00_Spec/INTAKE_v01.md` §1.

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C01_base_frame $OGUZ_JOBS/20260930-od-c01-base-frame`,
   then rebuild `00_Spec/inputs/` exactly as `briefs/WP-01_intake.md` lists it
   (the STEP, the report files, the scan notes, the BOM rows, `REQUEST.md` and
   `PROJECT_RULES.md`) and check the hashes against `00_Spec/INTAKE_v01.md` §1.
4. `uv run tools/jobstate.py check 20260930-od-c01-base-frame`, then
   `show`: `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-C01_base_frame.step`,
`.stl`, and the parametric build script under `chassis/src/`, per
[docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
