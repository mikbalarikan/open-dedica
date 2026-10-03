# OD-C10 printed top panel — design job record

This folder is the record of the CAD job that designs `OD-C10`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20261001-od-c10-top-panel/` so that any session, on any machine, can
continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frame, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every dimension and requirement as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `PROJECT_RULES.md`, `bom_rows.csv` | the three inputs written for this job from the Usta's words and the repository (the rest are repository files, below) |
| `briefs/` | the subagent briefs sent so far |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | added as the job advances: plan, scripts, REPORT, exports, sections, the verdict |

The top panel is a lid over the whole machine, held by four M3 screws from above: two into the bulkhead `OD-C02`'s top-rail inserts, two into the back panel `OD-C11`'s ledge inserts. It leaves 37 mm of headroom over the group head carrier `OD-C05` for the hot water tube's loop. The water tank stays on the table for now (the Usta, 2026-10-01), so the lid covers the whole footprint (spec A-07).

Repository inputs are not copied here. `00_Spec/inputs/` holds, besides the three
files above: `OD-C01_base_frame.step`, `OD-C02_bulkhead.step`, `OD-C05_group_head_carrier.step` and `OD-C07_valve_flowmeter_mount.step` (from `chassis/`); under `reports/`: `OD-C01_base_frame/DESIGN_SPEC_v1.2.md`, `OD-C02_bulkhead/DESIGN_SPEC_v1.2.md`, `OD-C05_group_head_carrier/DESIGN_SPEC_v2.2.md` and `OD-C07_valve_flowmeter_mount/DESIGN_SPEC_v1.2.md` (each part's `00_Spec/DESIGN_SPEC.md`). Their SHA-256 values are in `00_Spec/INTAKE_v01.md` §1.

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C10_top_panel $OGUZ_JOBS/20261001-od-c10-top-panel`,
   then copy the repository inputs into `00_Spec/inputs/` as listed above and in
   `briefs/WP-01_intake.md`, and check the hashes against `00_Spec/INTAKE_v01.md` §1.
4. `uv run tools/jobstate.py check 20261001-od-c10-top-panel`, then `show`: `next_action` says what
   comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-C10_top_panel.step`,
`.stl`, `.3mf`, and the parametric build script under `chassis/src/OD-C10_top_panel/`, per
[docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
