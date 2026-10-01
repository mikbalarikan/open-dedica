# WP-03 — designer brief, J3 package (build v02, spec 1.1)

Job: 20260930-od-c02-bulkhead · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 · target `od_c02_bulkhead_v02` · build attempt 2 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against your plan `01_CAD/DESIGN_PLAN.md` with the
amendments below (spec 1.1 answers every item of your v01 REPORT §10). Start from
your v01 scripts; change what the amendments name, keep the placements and the
rest. Export into `02_STEP_STL/od_c02_bulkhead_C1_v02.step`,
`..._assembly_C1_v02.step`, `..._bulkhead_C1_v02.stl`; sections with `_v02`; the
sweep into `01_CAD/sweep_v02/`; results into `01_CAD/check_od_c02_bulkhead_v02.json`;
the REPORT into `01_CAD/REPORT_od_c02_bulkhead_v02.md`. Leave every v01 file as it
is. The 3MF is the orchestrator's step (report the STL's triangle count, volume
and bounding box). Return the block your skill defines. At the fix-cycle cap, or
when a hard gate cannot be met, stop with the measured failure (D9). This is the
last build attempt of the cap: a stop goes to the Usta.

## Plan amendments (spec 1.1 §4, §5)

| Item | v02 |
|---|---|
| Base fastening | no through-holes, no counterbores. Four Ø4.0 × 6.0 blind bores along +Y from the rail's underside (y 0) at (x 65, z −45 / −105 / −165 / −225) for heat-set inserts; the screws come from below through the plate's Ø4.0 holes (REQ-01: `locate_bore` coaxial with the plate's holes, offset ≤ 0.10; D-05a, D-05b, J-05 on all six bores) |
| Base rail | x 59.0 … 71.0 (12 wide, centred on the wall x 63 … 67), y 0 … 12 |
| Top rail | x 59.5 … 70.5 (11 wide, centred), y 207 … 215; the two Ø4.0 × 6.0 bores from the top at (x 65, z −60) and (65, −210) (REQ-07) |
| Ribs | none |
| Collars | none; the windows are plain Ø14 holes with their 45° gable toward +Z (apex 7.0 beyond the +Z edge) |
| Window 4 | (y 60, z −55): round part z −62 … −48, apex z −41 |
| Envelope | 12.0 × 215.0 × 210.0: x 59 … 71, y 0 … 215, z −240 … −30 (U-02, D-02: 12 × 215 on the bed, 210 tall); REQ-08 max_x ≤ 71 |
| D-01b | ≥ 2.0 (spec default) |
| D-04a | N/A by its row |
| Named exception | the crowns of the six horizontal Ø4.0 insert bores only (D-03a); D-03b: the bores bridge 4.0, the gables carry the windows |
| U-05 census | 1 wall, 1 base rail, 1 top rail, 4 gabled windows, 4 + 2 Ø4.0 blind bores: predict the face counts and confirm |
| Sections | as v01 less the ribs and collars, plus y = 3 (the base-rail bores) and z = −55 (window 4) |
| U-03 | the plate contact is the rail's underside less the four bore mouths |

Every other value is the spec's. If a built value fails a Hard row, fix within the
fix cycles or stop with the measured failure; never change a spec value.

## Inputs and environment

As in `briefs/WP-02_designer.md`; your v01 plan, probes, scripts and REPORT.

## Findings to fix (v01 REPORT §10)

| Finding | What v02 does |
|---|---|
| counterbores under the wall, no driver access | inserts in the rail, screws from below |
| ribs' undersides as 195 ceilings (D-03a, D-03b) | ribs dropped |
| collars' round undersides (D-03a) | collars dropped |
| window 4 out of the front end (REQ-04) | moved to z −55 |
| rib 2 across window 1 | gone with the ribs |
| D-01b margin 0 at the counterbore web; U-06 0.265 at window 4 | gone with the counterbores and the move |
