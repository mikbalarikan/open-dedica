# WP-02 — designer brief, J3 package with its own plan (build v01)

Job: 20261001-od-c11-back-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-01) · concept C1 (chosen) · target `od_c11_back_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package with its own plan**: the part is a wall with two floor flanges,
four gussets, a top ledge with two insert bosses, three round pass-throughs and
five vent slots, so the plan and the build go in one package. First run D0–D2 and
write `01_CAD/DESIGN_PLAN.md` (measure the inputs it needs and write the
placements as probe scripts under `01_CAD/probe/` with JSON results: the OD-C01
plate's top face, rear edge and corner arcs near z −305 and its feet holes at
(±110, −295); OD-C03 with OD-H01 as OD-C01 §4 A-03 places them — their rear-most
z and their nearest point to the plane z −283; OD-C02's rear end). Then, without
stopping unless a spec value cannot be met, run D3–D9 and build. Write
`01_CAD/build_od_c11_back.py` (parametric, every §4 parameter a named value) and
`01_CAD/check_od_c11_back.py`. Export through `tools.core.write_step` (AP242)
into `02_STEP_STL/od_c11_back_C1_v01.step`; the check assembly (panel + OD-C01 +
OD-C02 + OD-C03 + OD-H01 as placed) into `02_STEP_STL/od_c11_assembly_C1_v01.step`;
the STL into `02_STEP_STL/od_c11_back_C1_v01.stl`; re-import and measure; sections
into `03_Sections/` with `_v01` in their names; the sweep into `01_CAD/sweep_v01/`;
the check results into `01_CAD/check_od_c11_back_v01.json`; the REPORT into
`01_CAD/REPORT_od_c11_back_v01.md` with its JSON block. The 3MF is the
orchestrator's step (report the STL's triangle count, volume and bounding box).
Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9). If the Write tool refuses a
file, write it with Bash.

The four new OD-C01 inserts this panel screws into (spec A-01) do not exist in
the OD-C01 STEP: gate U-03 (a) and REQ-01 on the plate's material under each
flange hole (the hole's footprint over solid plate, ≥ 6.0 from every existing
hole, ≥ 8.0 from the plate's edge), and say so in the REPORT.

Notes from earlier chassis jobs (OD-C01, OD-C02, OD-C07): `min_wall` and
`overhang_census` refuse large faces at the default spacing (use 0.7 and say
so); the named-exception faces (the crowns of the four Ø3.4 flange holes and the
two Ø4.0 boss bores, horizontal in the print) are selected by position and
reported apart; the OD-C03 placement is a proper rotation (local x → +Z,
y → −Y, z → +X, origin (0, 40, −205)) — build it with a `Location` from the
rotation matrix and check its foot underside lands on y 0. Print orientation is
**lying on the outer face z −302, build direction +Z**:
`overhang_census(build_dir=(0,0,1))`.

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A by its row), D-01a, D-01b, D-02, D-03a and D-03b (with the
named exception), D-04a, D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-06, E-11,
REQ-01 … REQ-09 (REQ-09 Soft bench: INCONCLUSIVE, say so); plus
`exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/DESIGN_SPEC.md` | be47ca714ff025b5276636ea8d2831d404b81addfb59fc0d3f50579de9054c5c | the contract (1.0) |
| `00_Spec/INTAKE_v01.md` | 716850a7c846399f660c89c4bf328f021fe13b06ad667ba7af43445a6f5324fc | the intake rows |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | the plate, identity (frame = machine frame) |
| `00_Spec/inputs/OD-C02_bulkhead.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | identity |
| `00_Spec/inputs/OD-C03_pump_cradle.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | local x → +Z, y → −Y, z → +X at (0, 40, −205) |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | at OD-C03's identity, then OD-C03's placement |
| `00_Spec/inputs/OD-W03_tank_seat.step` | 55162e2d263cfba9123e09ec6d70d0076a4ff5fe1c609601282f005dc51c69ba | reference only (hose nipples, INTAKE X-23 … X-27); not placed |

## Environment

Workspace: `${OGUZ_JOBS}/20261001-od-c11-back-panel`; run `. $HOME/oguz-env/env.sh`
in every shell command first (it sets OGUZ_WORK, OGUZ_JOBS, OGUZ_DELIVERY,
OGUZ_ARTIFACTS). Run any Python through `uv run tools/run.py python <script>`
from the repository root `/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3
in the tools venv). Templates: `atolye/templates/DESIGN_PLAN.md`,
`atolye/templates/REPORT.md`. Library index: `library/INDEX.md` (at most two
cards); traps: `library/BUILD123D-NOTES.md`. Tools documentation: `tools/README.md`.
Precedent for the scripts' shape and placements (another job, read-only):
`/home/claude/open-dedica/chassis/reports/OD-C02_bulkhead/01_CAD/`
(`build_od_c02_bulkhead_v02.py`, `check_od_c02_bulkhead_v02.py`, `probe/`).

## Findings to fix

None (first package).
