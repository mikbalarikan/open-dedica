# OD-C07 printed valve and flowmeter mount — design job record

This folder is the record of the CAD job that designs `OD-C07`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount/` so that any session, on any
machine, can continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frame, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every dimension of the reference parts as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `bom_rows.csv` | the two inputs written for this job (the rest are repository files, below) |
| `briefs/` | the subagent briefs sent so far |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | added as the job advances: plan, scripts, REPORT, exports, sections, the verdict |

The mount carries the 3-way valve `OD-H22` (OPV reachable from above) and the
flowmeter `OD-H24`. The anti-drip valve `OD-H21` is not carried: on 2026-09-30 the
Usta ruled that it plugs into the water path by its clipped spigot (spec §7).

Repository inputs are not copied here: the job reads
`step/OD-H21_antidrip_valve.step`, `step/OD-H22_3way_valve.step`,
`step/OD-H24_flowmeter.step` and files of their reports under `step/reports/`,
plus `docs/WATER_FLOW.md`, `docs/SOURCING_GUIDE.md` and `chassis/README.md`; the
exact list with SHA-256 values is `00_Spec/INTAKE_v01.md` §1 (paths there are
relative to `00_Spec/inputs/`; `DELIVER_README.md` is each report's
`deliver/README.md`, `CHASSIS_README.md` is `chassis/README.md`).

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C07_valve_flowmeter_mount $OGUZ_JOBS/20260930-od-c07-valve-flowmeter-mount`,
   then copy the repository inputs into `00_Spec/inputs/` exactly as
   `00_Spec/INTAKE_v01.md` §1 lists them, and check the hashes.
4. `uv run tools/jobstate.py check 20260930-od-c07-valve-flowmeter-mount`, then
   `show`: `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-C07_valve_flowmeter_mount.step`,
`.stl`, and the parametric build script under `chassis/src/`, per
[docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
