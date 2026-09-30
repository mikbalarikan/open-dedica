# OD-C02 printed wet/electric bulkhead — design job record

This folder is the record of the CAD job that designs `OD-C02`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20260930-od-c02-bulkhead/` so that any session, on any machine, can
continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frame, concept, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every dimension and requirement as an `X-##` row |
| `briefs/` | the subagent briefs sent so far |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | added as the job advances: plan, scripts, REPORT, exports, sections, the verdict |

Inputs are not copied here: the job reads the delivered `chassis/OD-C01_base_frame.step`
with that job's `DESIGN_SPEC.md` (1.2) and `REPORT_od_c01_frame_v02.md`, the delivered
OD-C03 and OD-C04 STEP files, the OD-G01 build v02 STEP, the library STEP files
`step/OD-H01_ulka_ep5_pump.step` and `step/OD-H11_thermoblock.step`, the OD-C04 and
OD-C05 specs, the BOM rows of `docs/bom.csv` that touch the part, and two files the
orchestrator wrote from the project's own documents (`REQUEST.md`, `PROJECT_RULES.md`);
their SHA-256 values are in `00_Spec/INTAKE_v01.md` §1.

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C02_bulkhead $OGUZ_JOBS/20260930-od-c02-bulkhead`,
   then rebuild `00_Spec/inputs/` exactly as `briefs/WP-01_intake.md` lists it and
   check the hashes against `00_Spec/INTAKE_v01.md` §1.
4. `uv run tools/jobstate.py check 20260930-od-c02-bulkhead`, then `show`:
   `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-C02_bulkhead.step`,
`.stl`, `.3mf` and the parametric build script under `chassis/src/`, per
[docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
