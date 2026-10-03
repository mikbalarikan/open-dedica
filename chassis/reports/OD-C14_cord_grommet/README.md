# OD-C14 printed cord grommet — design job record

This folder is the record of the CAD job that designs `OD-C14`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20261002-od-c14-cord-grommet/` so that any session, on any machine,
can continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract (version 1.2; 1.0 and 1.1 kept beside it) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every value as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `bom_rows.csv`, `SOURCING_GUIDE_s6.md` | the inputs written or extracted for this job (the rest are repository files, below) |
| `briefs/` | the subagent briefs |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | plan, scripts, REPORT, exports, sections, the verdict |

The grommet is a split bushing in two identical PLA halves around the Ø7 mains
cord in OD-C11's Ø12 cord hole, closed by a cable tie (spec §4).

Repository inputs are not copied here: the job reads `chassis/OD-C11_back_panel.step`,
`chassis/OD-C01_base_frame.step`, `chassis/OD-C08_electronics_bay_tray.step`,
`chassis/reports/OD-C11_back_panel/00_Spec/DESIGN_SPEC.md` (as `OD-C11_DESIGN_SPEC.md`)
and `chassis/README.md` (as `CHASSIS_README.md`); SHA-256 values in
`00_Spec/INTAKE_v01.md` §1.

## Resume

1. Clone both repositories side by side (`oguz-atolye` and `open-dedica`).
2. Toolchain: `uv` with Python 3.13 (`uv python install 3.13`); set the four
   `OGUZ_*` variables outside both checkouts, for example
   `export OGUZ_WORK=$HOME/oguz-work OGUZ_JOBS=$HOME/oguz-jobs OGUZ_DELIVERY=$HOME/oguz-delivery OGUZ_ARTIFACTS=$HOME/oguz-artifacts`,
   then from the `oguz-atolye` root run `uv run tools/run.py python -c "import build123d"` once.
3. `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C14_cord_grommet $OGUZ_JOBS/20261002-od-c14-cord-grommet`,
   copy the repository inputs above into `00_Spec/inputs/` and check their hashes.
4. `uv run tools/jobstate.py check 20261002-od-c14-cord-grommet`, then `show`;
   continue from `next_action` under `atolye/PLAYBOOK.md`.

State: J5_DELIVER after RV01 (approved on assumptions); next, the merge, then J6
with the physical outcome pending the first fitting.
