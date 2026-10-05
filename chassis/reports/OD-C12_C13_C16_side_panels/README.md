# OD-C12, OD-C13 printed side panels and OD-C16 corner bracket — design job record

This folder is the record of the CAD job that designs `OD-C12`, `OD-C13` and `OD-C16`, run under the
OGUZ Atölye pipeline ([mikbalarikan/oguz-atolye](https://github.com/mikbalarikan/oguz-atolye),
`atolye/PLAYBOOK.md`). It mirrors the job workspace
`${OGUZ_JOBS}/20261002-od-c12-c13-c16-side-panels/` so that any session, on any machine,
can continue the job from git: cloud containers lose their job folders.

| File | What |
|---|---|
| `JOB.md`, `EVENTS.jsonl` | job state and the append-only event record (written only by `tools/jobstate.py`) |
| `00_Spec/DESIGN_SPEC.md` | the contract (version 1.2; 1.0 and 1.1 kept beside it) |
| `00_Spec/INTAKE_v01.md` | intake: every input hashed, every value as an `X-##` row |
| `00_Spec/inputs/REQUEST.md`, `bom_rows.csv`, `SOURCING_GUIDE_s6.md`, the neighbours' integration notes | the inputs written or extracted for this job (the rest are repository files, below) |
| `briefs/` | the subagent briefs |
| `01_CAD/`, `02_STEP_STL/`, `03_Sections/`, `reviews/` | plan, scripts, REPORT, exports, sections, the verdict |

The panels are 3.0 mm PLA plates on OD-C01's side edges; the lid OD-C10 rests on
their tops and a 60° wedge lip locates it; three OD-C16 brackets per side fasten each
panel's foot to six new inserts in OD-C01 (spec §4).

Repository inputs are not copied here: the job reads the delivered STEP and spec of
OD-C01, OD-C02, OD-C05, OD-C07, OD-C08, OD-C10, OD-C11 and OD-C15 from `chassis/`
and `chassis/reports/` (as `00_Spec/inputs/<part>.step` and `<part>_DESIGN_SPEC.md`)
and `chassis/README.md` (as `CHASSIS_README.md`); SHA-256 values in
`00_Spec/INTAKE_v01.md` §1 and `briefs/WP-04_reviewer.md`.

## Resume

1. Clone both repositories side by side (`oguz-atolye` and `open-dedica`).
2. Toolchain: `uv` with Python 3.13 (`uv python install 3.13`); set the four
   `OGUZ_*` variables outside both checkouts, for example
   `export OGUZ_WORK=$HOME/oguz-work OGUZ_JOBS=$HOME/oguz-jobs OGUZ_DELIVERY=$HOME/oguz-delivery OGUZ_ARTIFACTS=$HOME/oguz-artifacts`,
   then from the `oguz-atolye` root run `uv run tools/run.py python -c "import build123d"` once.
3. `mkdir -p $OGUZ_JOBS && cp -r <open-dedica>/chassis/reports/OD-C12_C13_C16_side_panels $OGUZ_JOBS/20261002-od-c12-c13-c16-side-panels`,
   copy the repository inputs above into `00_Spec/inputs/` and check their hashes.
4. `uv run tools/jobstate.py check 20261002-od-c12-c13-c16-side-panels`, then `show`;
   continue from `next_action` under `atolye/PLAYBOOK.md`.

State: J5_DELIVER after RV01 (approved on assumptions); next, the merge, then J6
with the physical outcome pending the first prints (REQ-08 stiffness, A-14 lip fit).
