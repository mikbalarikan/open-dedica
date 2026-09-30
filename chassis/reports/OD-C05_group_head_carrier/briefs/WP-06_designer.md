# WP-06 — designer brief, J3 package (build v03, spec 2.1)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 2.1 (ratified 2026-09-30) · concept C4 (column, 2.1) · target `od_c05_carrier_v03` · build attempt 2 of 2 (the ledger counts v02 as the first build of this round) · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against your plan `01_CAD/DESIGN_PLAN_v02.md` with the
amendments below (spec 2.1, which answers your v02 K-3, K-4 and §9: the wall
becomes a closed column, the part prints with the plate on the bed). Start from
your v02 scripts; change what the amendments name, keep the rest (placements,
hole checks, window check, exception-face selector by position). Export into
`02_STEP_STL/od_c05_carrier_C4_v03.step`, `02_STEP_STL/od_c05_assembly_C4_v03.step`,
`02_STEP_STL/od_c05_carrier_C4_v03.stl`; sections with `_v03`; the sweep into
`01_CAD/sweep_v03/`; results into `01_CAD/check_od_c05_carrier_v03.json`; the
REPORT into `01_CAD/REPORT_od_c05_carrier_v03.md`. Leave every v01 and v02 file as
it is. The 3MF is the orchestrator's step (report the STL's triangle count,
volume and bounding box). Return the block your skill defines. At the fix-cycle
cap, or when a hard gate cannot be met, stop with the measured failure (D9).

## Plan amendments (spec 2.1 §4, §5, §6; list each as a deviation in REPORT §8)

| Item | v03 |
|---|---|
| Print orientation, build direction | plate's top face (z −29.94) on the bed, **build direction +Z**; `overhang_census(build_dir=(0,0,1))`; D-02: 110 × 152 on the bed, 210 tall |
| Plate | y −102.0 … +50.0 (it is also the column's lid), x ±55, **square corners** (no R 6); hub window R 30.0 round, **no gable** (REQ-04: innermost radius over the whole ray ≥ 30.0 at every 10°); a **hatch** 80 × 32, x ±40, y −96 … −64, corners R 4.0 |
| Column | front wall 6.0 (y −58 … −52, x ±55), side walls 4.0 (|x| 51 … 55, y −102 … −58), rear wall 4.0 (y −102 … −98, x ±55), all from z −24.94 (the plate's underside) to the foot; rear window x ±10, z +130 … +160, 45° gable toward −Z with apex at z +120 |
| Foot | underside z +180.06 (x ±55, y −102 … −58); inside a 45° tent: two planes from z +176.06 at y −102 and y −58 rising to the ridge (y −80, z +154.06); four Ø3.4 holes at (±35, −72) and (±35, −92) with Ø6.5 counterbores from the tent face, floors at z +176.06 (14.0 deep at y −72, 10.0 at y −92); REQ-05 / REQ-06 as the spec rows now read |
| Gussets | the two front gussets only (|x| 51 … 55, legs 40, under the plate on the front wall); the rear gussets are gone |
| Named exception (D-03a / D-03b) | the eight counterbore floors (four on the plate at z −27.94, four in the tent at z +176.06): exclude by position, report their least angle apart; every other downward face must read ≥ 45° (expect the tent faces and the rear window gable at 45.000°, report the analytic angles too) |
| U-05 census | predict the counts in REPORT §3 from the feature list (1 plate with hub window and hatch, front/side/rear walls, rear window with gable, tented foot, 2 gussets, 4 + 4 Ø3.4 holes, 4 + 4 Ø6.5 counterbores) and confirm on the build |
| Sections | y = 0 (L profile: plate, front wall, gusset), y = −80 (column and tent ridge, hatch), x = 0 (hub window, hatch, rear window, tent), x = 35 (foot holes and counterbores), x = 53 (side wall, gusset), z = −27.44 (plate plan), z = +165 (foot plan through the tent), assembly y = 0 and x = 0 |
| REQ-09 | still Soft: report the closed section's hand estimate against your v02 §9 figure (A-11) |

Every other value is the spec's. If a built value fails a Hard row, fix within the
fix cycles or stop with the measured failure; never change a spec value.

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a and D-03b (with the named
exception), D-04a, D-06a, D-07 (N/A), E-06, REQ-01 … REQ-09 (REQ-09 Soft bench:
INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs and environment

As in `briefs/WP-03_designer.md` and `briefs/WP-05_designer.md`; your v02 plan,
scripts and REPORT.

## Findings to fix (v02 REPORT §8, §9)

| Finding | What v03 does |
|---|---|
| K-3 gusset ceilings in the +X print | print orientation +Z; rear gussets replaced by the column |
| K-4 R 6 corner overhang | corners squared |
| §9 REQ-09 ≈ 5° flex (HIGH) | closed column |
