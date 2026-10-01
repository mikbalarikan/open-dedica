# OD-C15 printed TPU foot — design job record

This folder is the record of the CAD job that designs `OD-C15`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20261001-od-c15-feet/` so that any session, on any machine, can
continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frame and joint to OD-C01, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every OD-C01 value a foot touches as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `bom_rows.csv`, `SOURCING_GUIDE_s*.md` | the inputs written or extracted for this job (the rest are repository files, below) |
| `briefs/` | the subagent briefs |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | plan, scripts, REPORT, exports, sections, the verdict |

The foot is a round TPU puck (Ø18 × 10) under each of OD-C01's four Ø3.4 feet
holes, held by an M3×12 button-head screw from the plate top into an M3 hex nut
captive in the foot.

Repository inputs are not copied here: the job reads `chassis/OD-C01_base_frame.step`
(as `OD-C01_base_frame.step`), `chassis/reports/OD-C01_base_frame/00_Spec/DESIGN_SPEC.md`
(as `OD-C01_DESIGN_SPEC.md`), `chassis/reports/OD-C01_base_frame/reviews/RV01_od_c01_frame_v02.md`
(as `OD-C01_RV01.md`) and `chassis/README.md` (as `CHASSIS_README.md`); the exact
list with SHA-256 values is `00_Spec/INTAKE_v01.md` §1.

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C15_foot $OGUZ_JOBS/20261001-od-c15-feet`,
   then copy the repository inputs into `00_Spec/inputs/` under the names above,
   and check the hashes against `00_Spec/INTAKE_v01.md` §1.
4. `uv run tools/jobstate.py check 20261001-od-c15-feet`, then `show`:
   `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-C15_foot.step`,
`.stl`, `.3mf`, and the parametric build script under `chassis/src/OD-C15_foot/`,
per [docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
