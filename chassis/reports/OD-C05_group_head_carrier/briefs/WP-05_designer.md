# WP-05 — designer brief, J3 package (plan and build v02, the round after RV01)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 2.0 (ratified 2026-09-30) · concept C4 (chosen) · target `od_c05_carrier_v02` · build attempt 1 of 2 (new target after the REVISE round) · fix_cycles 3

## Package

A **J3 package with its own plan**: RV01 (`reviews/RV01_od_c05_carrier_v01.md`)
found no geometric fault in v01 but blocked on plausibility F1: the frame of
spec 1.x hung the group head on its side. Spec 2.0 turns the axis vertical (§2,
A-02) and replaces concept C1 by **C4** (§4): a horizontal plate over the housing's
rear face, a wall behind the housing standing on a foot, four gussets, one hub
window, printed on its side. Because the concept is new, first run D0–D2 and write
`01_CAD/DESIGN_PLAN_v02.md` (the v01 plan stays as it is; reuse its measured input
facts §1 and its placements §5, which are unchanged: the housing frame is the same,
only "which way is up" changed), then, without stopping unless a spec value
cannot be met, run D3–D9 and build. Write `01_CAD/build_od_c05_carrier_v02.py`
and `01_CAD/check_od_c05_carrier_v02.py` (start from your v01 scripts: the
placements, the hole and counterbore checks, the window check and the exception
face selector carry over). Export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c05_carrier_C4_v02.step`, the check assembly (carrier + OD-G01 +
OD-G04 as placed) into `02_STEP_STL/od_c05_assembly_C4_v02.step`, the STL into
`02_STEP_STL/od_c05_carrier_C4_v02.stl`; re-import and measure; sections into
`03_Sections/` with `_v02` in their names; the sweep into `01_CAD/sweep_v02/`; the
check results into `01_CAD/check_od_c05_carrier_v02.json`; the REPORT into
`01_CAD/REPORT_od_c05_carrier_v02.md` with its JSON block. Leave every v01 file
as it is. The 3MF is the orchestrator's step (report the STL's triangle count,
volume and bounding box). Return the block your skill defines. At the fix-cycle
cap, or when a hard gate cannot be met, stop with the measured failure (D9). If
the Write tool refuses a file, write it with Bash.

## What changed against v01 (spec 2.0 §4, §5, §6)

| Item | v02 (spec 2.0) |
|---|---|
| Up direction | −Z of the housing frame is up, +Z (the mouth) down, +Y the front; the floor is the plane z = +180.06 (A-03). Build direction of the print: **+X** (on its side, x = −55 face on the bed, A-13) |
| Plate | 5.0 thick, z −29.94 … −24.94 (underside on the housing's rear face, the designed contact), x ±55, y −58 … +50, front corners R 6.0 about (±49, 44) |
| Holes and counterbores | four Ø3.4 along Z at (±44, ±44); Ø6.5 × 2.0 counterbores from the top face z −29.94 (screws from above) |
| Hub window | R 30.0 about the axis through the plate, 45° gable toward **+X**, apex (42.43, 0). REQ-04 gates the innermost material radius over the whole ray (RV01 F4): ≥ 30.0 at every 10°, 42.43 at θ 0° |
| Wall | 6.0 thick along Y, y −58 … −52, x ±55, z −29.94 … +180.06 |
| Foot | 4.0 thick, z +176.06 … +180.06, x ±55, y −102 … −58; four Ø3.4 along Z at (±35, −72) and (±35, −92) |
| Gussets ×4 | 4.0 thick at |x| 51 … 55; front pair under the plate (legs y −52 → −12 on the plate's underside, z −24.94 → +15.06 on the wall's front face); rear pair on the foot (legs y −58 → −98 on the foot's top z +176.06, z +176.06 → +136.06 on the wall's rear face); 45° hypotenuses |
| Dropped | the lower window, the R 6 corners about the top holes (the plate's front corners are R 6 about (±49, 44) now) |
| Envelope | 110.0 × 152.0 × 210.0: x ±55, y −102 … +50, z −29.94 … +180.06 (U-02, D-02: 152 × 210 on the bed, 110 tall) |
| Exception faces | the twelve bores along Z (4 holes, 4 counterbores, 4 foot holes): crowns excluded from `overhang_census(build_dir=(1,0,0))` by position and reported apart; the gable and every other face gated at ≥ 45°. In this print every other face is a prism along X: expect 90° or vertical everywhere except the gable at 45.000° (report its analytic angle as RV01 did, F3) |
| REQ-03 | plate underside z −24.94 (counterbore start −29.94 + hole length 3.0), top face z −29.94 = `envelope` min_z |
| REQ-05 | foot underside z +180.06 = `envelope` max_z, thickness 4.0 (foot hole length) |
| REQ-06 | the four foot holes at (±35, y −72 / −92), offset ≤ 0.10 |
| REQ-07 | `envelope` min_y ≥ −102.0 |
| REQ-08 | housing-to-carrier clearance off the contact plane: sides to the gussets ≥ 1.0, rear side (y −50) to the wall ≥ 2.0 (`clearance` with the nearest points; the contact at z −24.94 reported apart as U-03's 0.000) |
| U-05 census | 1 plate, 1 wall, 1 foot, 4 gussets, 1 hub window, 4 Ø3.4 + 4 Ø6.5 (plate), 4 Ø3.4 (foot): predict the face counts in the plan and confirm on the build |
| Sections | y = 0 (plate, wall, foot, gussets: the L profile), x = 0 (window, plate over the housing), x = 44 (holes and counterbores), x = 53 (a gusset pair), z = −27.44 (plate plan: window gable, holes), z = +178 (foot holes), assembly y = 0 and x = 0 with OD-G01 and OD-G04 |

Every other value is the spec's. If a built value fails a Hard row, fix within the
fix cycles or stop with the measured failure; never change a spec value.

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a and D-03b (with the named
exception), D-04a, D-06a, D-07 (N/A), E-06, REQ-01 … REQ-09 (REQ-09 Soft bench:
INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs (paths relative to the workspace)

As in `briefs/WP-03_designer.md` (OD-G01 v02 STEP f8865cd1…, OD-G04 STEP
19b4a140…), your v01 plan, probes and scripts, and `reviews/RV01_od_c05_carrier_v01.md`
(read its §6 findings F2 … F5 and carry F4's whole-ray reading into the check).

## Environment

As in `briefs/WP-03_designer.md`.

## Findings to fix (RV01 §6)

| Finding | What v02 does |
|---|---|
| F1 P1/P5 axis horizontal (blocking, HIGH) | spec 2.0: vertical axis, concept C4 |
| F2 REQ-09 open wall twists (MEDIUM, Soft) | C4's wall is 6.0 with four gussets; the plate cantilevers 96 to the front screws: report the geometry in REPORT §7, the bench answers it |
| F3 `overhang_census` at exactly 45° (LOW) | report the gable's analytic angle beside the census, as RV01 did |
| F4 window check cannot fail (LOW) | REQ-04 gated on the innermost radius over the whole ray |
| F5 R 6 corners outside the housing outline (LOW) | gone with C4 (the plate is wider than the housing) |
