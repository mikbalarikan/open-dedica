# OD-C09 printed front panel with button bezel — design job record

This folder is the record of the CAD job that designs `OD-C09`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20261002-od-c09-front-panel/` so that any session, on any machine, can
continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract: intent, frames and poses, concept C1, gate table (§5), assumptions ledger (§6) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every value the part touches as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `bom_rows.csv`, other extracts | the inputs written or extracted for this job (the rest are repository files, below) |
| `briefs/` | the subagent briefs |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | plan, scripts, REPORT, exports, sections, the verdict |

The panel is a 3 mm wall standing on OD-C01's front edge (the mirror of the back
panel OD-C11), with a brew opening for the portafilter and the drip tray, return
ribs along the opening, two floor flanges screwed into four new OD-C01 inserts,
and the OEM button board OD-E02 held behind three button holes on the left pillar.

Repository inputs are not copied here; the job reads them under these names in
`00_Spec/inputs/` (the exact list with SHA-256 values is `00_Spec/INTAKE_v01.md` §1):

- `chassis/OD-C01_base_frame.step`, `chassis/OD-C05_group_head_carrier.step` (same names)
- `chassis/OD-C10_top_panel.step`, `chassis/OD-C11_back_panel.step` (same names)
- `chassis/reports/OD-G01_group_head_housing/02_STEP_STL/od_g01_assembly_C1_v03.step` and `od_g01_housing_C1_v03.step` (same names)
- `step/OD-E02_control_board.step`, `step/OD-S03_steam_knob.step` (same names); `step/reports/OD-E02_control_board/deliver/README.md` as `OD-E02_REPORT.md`, `step/reports/OD-S03_steam_knob/README.md` as `OD-S03_REPORT.md`
- the `00_Spec/DESIGN_SPEC.md` of OD-C01, OD-C05, OD-C10, OD-C11, OD-C15 and OD-G01 as `OD-Cnn_DESIGN_SPEC.md` / `OD-G01_DESIGN_SPEC.md`; `chassis/README.md` as `CHASSIS_README.md`

## Status (2026-10-03)

J6_CLOSE (PR #52 merged 2026-10-05). Build v01 (spec 1.1) RV01 `APPROVED_ASSUMPTION_CONDITIONAL`, no blocking finding (F1 stiffness on the bench, F2 the handle's lock angle past +11°, F3–F5 low). J6 waits on the first print.

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
3. Recreate the workspace: `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C09_front_panel $OGUZ_JOBS/20261002-od-c09-front-panel`,
   then copy the repository inputs into `00_Spec/inputs/` under the names above,
   and check the hashes against `00_Spec/INTAKE_v01.md` §1.
4. `uv run tools/jobstate.py check 20261002-od-c09-front-panel`, then `show`:
   `next_action` says what comes next. Continue under `atolye/PLAYBOOK.md`.
5. When the job advances, copy the new files back into this folder and commit.

Deliverables, when the review approves them, go to `chassis/OD-C09_front_panel.step`,
`.stl`, `.3mf`, and the parametric build script under `chassis/src/OD-C09_front_panel/`,
per [docs/PART_NUMBERING.md](../../../docs/PART_NUMBERING.md).
