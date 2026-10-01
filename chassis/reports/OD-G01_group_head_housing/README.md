# OD-G01 printed group head housing — design job record

This folder is the record of the CAD job that designs `OD-G01`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20260930-od-g01-group-head-housing/` so that any session, on any
machine, can continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frame, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every dimension of the reference parts as an `X-##` row |
| `briefs/` | the subagent briefs sent so far (`WP-01` intake, `WP-02` designer plan) |
| `01_CAD/`, `02_STEP_STL/`, `reviews/` | added as the job advances: plan, scripts, REPORT, exports, the verdict |

Inputs are not copied here: the job reads the reference STEP files from
`step/OD-G09_group_head_bayonet_cup.step`, `step/OD-G04_brewing_gasket_support.step`,
`step/OD-G10_portafilter.step` and their reports under `step/reports/` (their
SHA-256 values are in `00_Spec/INTAKE_v01.md` and `briefs/WP-02_designer.md`).

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-G01_group_head_housing $OGUZ_JOBS/20260930-od-g01-group-head-housing`,
   then copy the three reference STEP files and their report folders into
   `00_Spec/inputs/` exactly as `briefs/WP-01_intake.md` lists them, and check
   the hashes.
4. `uv run tools/jobstate.py check 20260930-od-g01-group-head-housing`, then
   `show`: `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-G01_group_head_housing.step`,
`.stl`, and the parametric build script under `chassis/src/`, per
[docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
