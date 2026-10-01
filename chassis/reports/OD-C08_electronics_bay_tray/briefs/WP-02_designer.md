# WP-02 — designer brief, J3 package with its own plan (build v01)

Job: 20261001-od-c08-electronics-bay-tray · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-01) · concept C1 (chosen) · target `od_c08_tray_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package with its own plan**: the part is an upright wall on a floor
flange with four gussets, four standoffs (two with insert bores, two with
locating pins) and two tie-slot pairs, so the plan and the build go in one
package. First run D0–D2 and write `01_CAD/DESIGN_PLAN.md` (measure the inputs it
needs and write the placements as probe scripts under `01_CAD/probe/` with JSON
results: OD-E01 at the joint of spec §4 — confirm on the placed solid that H1,
H2, H5, H6 land where §4 says (`locate_bore` on the board), the solder face's x,
the board's outline and its highest point in x; what of OD-E01 lies on the
solder side below the board (anything at x < 82.44 other than the board itself:
report it, the standoffs must clear it); the OD-C01 plate's top face in the zone
and the OD-C02 rails' +X faces). Then, without stopping unless a spec value
cannot be met, run D3–D9 and build. Write `01_CAD/build_od_c08_tray.py`
(parametric, every §4 parameter a named value) and `01_CAD/check_od_c08_tray.py`.
Export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c08_tray_C1_v01.step`; the check assembly (tray + OD-E01 at its
joint + OD-C01 + OD-C02) into `02_STEP_STL/od_c08_assembly_C1_v01.step`; the STL
into `02_STEP_STL/od_c08_tray_C1_v01.stl`; re-import and measure; sections into
`03_Sections/` with `_v01` in their names; the sweep into `01_CAD/sweep_v01/`; the
check results into `01_CAD/check_od_c08_tray_v01.json`; the REPORT into
`01_CAD/REPORT_od_c08_tray_v01.md` with its JSON block. The 3MF is the
orchestrator's step (report the STL's triangle count, volume and bounding box).
Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9). If the Write tool refuses a
file, write it with Bash.

The four new OD-C01 inserts this tray screws into (spec A-01) do not exist in
the OD-C01 STEP: gate U-03 (a) and REQ-01 on the plate's material under each
flange hole (the hole's footprint over solid plate, ≥ 6.0 from every existing
hole, ≥ 8.0 from the plate's edge), and say so in the REPORT. OD-E01 is one
fused envelope solid (4.8 MB STEP, 1233 faces): booleans against it may be slow
or INCONCLUSIVE; gate its clearances on distance and report any boolean that
fails as INCONCLUSIVE with the reason. The pins sit inside the board's holes: the
D-04d gap is the clearance from each pin to the board solid.

Notes from earlier chassis jobs (OD-C01, OD-C02, OD-C07): `min_wall` and
`overhang_census` refuse large faces at the default spacing (use 0.7 and say
so); the named-exception faces (the crowns of the four Ø3.4 flange holes,
horizontal in the print) are selected by position and reported apart. Print
orientation is **lying on the wall's outer face x 73, build direction +X**:
`overhang_census(build_dir=(1,0,0))`.

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A by its row), D-01a, D-01b, D-02, D-03a and D-03b (with the
named exception), D-04a, D-04c, D-04d, D-05a, D-05b, D-06a, D-07 (N/A), J-05,
E-01, E-05, E-06, E-11, REQ-01 … REQ-06 (REQ-06 Soft bench: INCONCLUSIVE, say
so); plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/DESIGN_SPEC.md` | 5b559450a15d3ba56badbcd51d47b76caa9d1bd3f23199995378a976a18fd8f3 | the contract (1.0) |
| `00_Spec/INTAKE_v01.md` | 26641f69474020f9ce379adaca2c9524290261022cf1629857f9fff479a36dae | the intake rows |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | the plate, identity (frame = machine frame) |
| `00_Spec/inputs/OD-C02_bulkhead.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | identity |
| `00_Spec/inputs/OD-E01_power_pcb.step` | 90780af378d48baf22b43b378b4484c6ef252a1b68ecb224330bec32f3bfd869 | datum frame; placed by spec §4 (board x → −Z, y → +Y, z → +X, origin (84, 80, −100)) |
| `00_Spec/inputs/reports/OD-E01_power_pcb/PARAM_TABLE.md` | 99827b0fdcb2acdfcdf85b4bae17e76e21782ea185e121d5b00e42e1d6a41b51 | the board's measured parameters |

## Environment

Workspace: `${OGUZ_JOBS}/20261001-od-c08-electronics-bay-tray`; run
`. $HOME/oguz-env/env.sh` in every shell command first. Run any Python through
`uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`, `atolye/templates/REPORT.md`.
Library index: `library/INDEX.md` (at most two cards); traps:
`library/BUILD123D-NOTES.md`. Tools documentation: `tools/README.md`. Precedent
for the scripts' shape and placements (another job, read-only):
`/home/claude/open-dedica/chassis/reports/OD-C02_bulkhead/01_CAD/`.

Do not call any `mcp__hearthbot__*` tool; your hand-back goes to the orchestrator only.

## Findings to fix

None (first package).
