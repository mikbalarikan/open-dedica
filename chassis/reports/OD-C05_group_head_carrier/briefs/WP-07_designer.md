# WP-07 — designer brief, J3 package (build v04, spec 2.2)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 2.2 (ratified 2026-09-30) · concept C4 (column) · target `od_c05_carrier_v04` · build attempt 1 of 2 (counters reset by the another_round decision after the v03 halt) · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against `01_CAD/DESIGN_PLAN_v02.md` with the WP-06
amendments and the two below (spec 2.2 turns the foot's roof and the rear
window's gable the right way up for the plate-on-bed print: your v03 K-6 and K-7,
option 1). Start from your v03 scripts; change only what the amendments name.
Export into `02_STEP_STL/od_c05_carrier_C4_v04.step`, `..._assembly_C4_v04.step`,
`..._carrier_C4_v04.stl`; sections with `_v04`; the sweep into `01_CAD/sweep_v04/`;
results into `01_CAD/check_od_c05_carrier_v04.json`; the REPORT into
`01_CAD/REPORT_od_c05_carrier_v04.md`. Leave every earlier file as it is. The 3MF is
the orchestrator's step (report the STL's triangle count, volume and bounding box).
Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9).

## Plan amendments (spec 2.2 §4, §5)

| Item | v04 |
|---|---|
| Foot roof (was the tent) | two 45° faces from z +154.06 at the front and rear walls' inner faces (y −58 and y −98) rising in the print (toward +Z) to the ridge along X at y −78.0, z +174.06: the foot is 26.0 thick at the walls and 6.0 at the ridge; the ridge is the highest line, so no bridge and no ceiling. Foot counterbores Ø6.5 from the roof face down to the floor at z +176.06: 8.0 deep at y −72, 16.0 deep at y −92 (REQ-05, REQ-06 unchanged in their thresholds) |
| Rear window | x ±10, z +110 … +140, 45° gable toward +Z with the apex at z +150.0 (below the roof's start at 154.06 on the rear wall) |
| Everything else | as v03: plate, hatch, hub window, column walls, front gussets, print orientation +Z, the named exception on the eight counterbore floors |
| Sections | as WP-06 plus x = 0 through the rear window's gable and the roof's ridge |
| U-05 census | recount for the roof (two faces meeting at a ridge) and the window's gable; confirm on the build |

## Inputs and environment

As in `briefs/WP-03_designer.md`, `WP-05_designer.md`, `WP-06_designer.md`; your v03
scripts and REPORT.

## Findings to fix (v03 REPORT §10)

| Finding | What v04 does |
|---|---|
| K-6 rear window's flat 20 ceiling at z +160 | window moved to z +110 … +140, gable toward +Z |
| K-7 roof ridge as a 102 bridge in the air | roof turned: ridge at the top of the print |
| U-06 sweep knife edge at y_rear −101.9 (Soft) | note in REPORT §7; the counterbore rims sit 4.0 inside the rear wall at nominal |
