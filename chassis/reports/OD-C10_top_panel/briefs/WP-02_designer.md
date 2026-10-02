# WP-02 — designer brief, J3 package with its own plan (build v01)

Job: 20261001-od-c10-top-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-01) · concept C1 (chosen) · target `od_c10_top_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package with its own plan**: the part is a lid (top skin, perimeter skirt,
four screw columns with counterbores, ribs, two rest pads), so the plan and the
build go in one package. First run D0–D2 and write `01_CAD/DESIGN_PLAN.md`
(measure the inputs it needs and write the placements as probe scripts under
`01_CAD/probe/` with JSON results: OD-C02's top-rail face y 215 and its two Ø4.0
insert bores at (65, −60) and (65, −210); OD-C11's ledge top y 215 and its two
Ø4.0 bores at (±90, −293), and its wall's top edge at z −302; OD-C05 as placed,
its plate top y 210, the housing screws' counterbores and the hub window; OD-C07
as placed, its highest point; OD-C01's outline and corner arcs). Then, without
stopping unless a spec value cannot be met, run D3–D9 and build. Write
`01_CAD/build_od_c10_top.py` (parametric, every §4 parameter a named value) and
`01_CAD/check_od_c10_top.py`. Export through `tools.core.write_step` (AP242)
into `02_STEP_STL/od_c10_top_C1_v01.step`; the check assembly (lid + OD-C01 +
OD-C02 + OD-C05 + OD-C07 + OD-C11 as placed) into
`02_STEP_STL/od_c10_assembly_C1_v01.step`; the STL into
`02_STEP_STL/od_c10_top_C1_v01.stl`; re-import and measure; sections into
`03_Sections/` with `_v01` in their names (at least one through each column
axis); the descent sweep into `01_CAD/sweep_v01/`; the check results into
`01_CAD/check_od_c10_top_v01.json`; the REPORT into
`01_CAD/REPORT_od_c10_top_v01.md` with its JSON block. The 3MF is the
orchestrator's step (report the STL's triangle count, volume and bounding box).
Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9) and give the trade-off
options. If the Write tool refuses a file, write it with Bash.

Placements (all solids are in the machine frame unless named): OD-C01, OD-C02
and OD-C11 at the identity. OD-C05 carrier: local x → X, y → +Z, z → −Y, origin
(0, 180.06, 32.0). OD-C07: local x → −Z, y → −X, z → +Y, origin (−92, 0, −60).
Build each with a `Location` from the rotation matrix and check a known face
lands where the spec says (the carrier's plate top at y 210.0). The OD-C11 STEP
is its unreviewed build v02 (that build stopped on its outer gussets near the
floor and a feet-hole margin; its wall, ledge and insert bores are as its spec
says): gate against it, and say in the REPORT that the reference is unreviewed.

Notes from earlier chassis jobs: `min_wall` and `overhang_census` refuse large
faces at the default spacing (use 0.7 and say so); the named-exception faces
(the four counterbore floors, normal +Y) are selected by position and reported
apart. Print orientation is **upside down, the top face y 250 on the bed, build
direction −Y**: `overhang_census(build_dir=(0,-1,0))`. The lid is large (240 ×
405): keep sweep and clearance runs on the reference solids near the lid
(crop by bounding box) so the checks finish.

## Gate IDs to check (spec §5)

U-01 … U-08 (as each row says, N/A where its row says so), D-01a, D-01b, D-02,
D-03a and D-03b (with the named exception), D-04a, D-05a (N/A), D-05b, D-06a,
D-07, J-05, E-06, REQ-01 … REQ-08 (REQ-08 Soft bench: INCONCLUSIVE, say so);
plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/DESIGN_SPEC.md` | 00efe32ca1dcd10d8410541d7991dac62510f454f02156fb5ddb8a117c2423b2 | the contract (1.1) |
| `00_Spec/INTAKE_v01.md` | 564b6330dd5a59098930fbe80bdd76406ae6966ebd7919401ecdedab70c49ba7 | the intake rows |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | the plate, identity |
| `00_Spec/inputs/OD-C02_bulkhead.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | identity |
| `00_Spec/inputs/OD-C05_group_head_carrier.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | placed as above |
| `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | placed as above |
| `00_Spec/inputs/OD-C11_back_panel_v02.step` | 80803f53c7ca267565115d46c61c4280e95baaef6afd800eeae0afa1e3e16235 | identity (unreviewed build v02) |

The sibling specs are under `00_Spec/inputs/reports/` (OD-C01 1.2, OD-C02 1.2,
OD-C05 2.2, OD-C07 1.2) for any value the probes need to confirm.

## Environment

Workspace: `${OGUZ_JOBS}/20261001-od-c10-top-panel`; run `. $HOME/oguz-env/env.sh`
in every shell command first (it sets OGUZ_WORK, OGUZ_JOBS, OGUZ_DELIVERY,
OGUZ_ARTIFACTS). Run any Python through `uv run tools/run.py python <script>`
from the repository root `/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3
in the tools venv). Templates: `atolye/templates/DESIGN_PLAN.md`,
`atolye/templates/REPORT.md`. Library index: `library/INDEX.md` (at most two
cards); traps: `library/BUILD123D-NOTES.md`. Tools documentation: `tools/README.md`.
Precedent for the scripts' shape (another job, read-only):
`${OGUZ_JOBS}/20261001-od-c11-back-panel/01_CAD/` (`build_od_c11_back_v02.py`,
`check_od_c11_back_v02.py`, `probe/`, `sweep_od_c11_back_v02.sh`).

Do not call any `mcp__hearthbot__*` tool; your hand-back goes to the orchestrator only.

## Findings to fix

None (first package).
