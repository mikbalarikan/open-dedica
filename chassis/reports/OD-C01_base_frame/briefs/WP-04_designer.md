# WP-04 — designer brief, J3 package (build v02, spec 1.2)

Job: 20260930-od-c01-base-frame · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c01_frame_v02` · build attempt 2 of 2 (the spec changed twice after v01 was briefed; the ledger counts it as the second build) · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan `01_CAD/DESIGN_PLAN.md` (D2, package
WP-02) with the notes of `briefs/WP-03_designer.md` (part of the plan) and the
amendments below. v01 (`01_CAD/REPORT_od_c01_frame_v01.md`) passed every row but was
built to spec 1.0; it is superseded, not reviewed. Start from your v01 scripts:
change what the amendments name, keep everything else. Export into
`02_STEP_STL/od_c01_frame_C1_v02.step`, `02_STEP_STL/od_c01_assembly_C1_v02.step`,
`02_STEP_STL/od_c01_frame_C1_v02.stl`; sections with `_v02`; the sweep into
`01_CAD/sweep_v02/`; results into `01_CAD/check_od_c01_frame_v02.json`; the REPORT
into `01_CAD/REPORT_od_c01_frame_v02.md`. Leave every v01 file as it is. The 3MF is
the orchestrator's step (report the STL's triangle count, volume and bounding box).
Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9).

## Plan amendments (spec 1.1 and 1.2, checked by the orchestrator)

| Plan row | Amendment |
|---|---|
| Insert holes (F02 … F05) | **twenty** Ø4.0 through-holes: the sixteen of the plan plus four for the OD-C07 valve and flowmeter mount at (x −113.0, z −42.0), (x −71.0, z −42.0), (x −113.0, z −148.5), (x −71.0, z −148.5) (spec 1.1 §4, REQ-10, A-17). U-05: 20 Ø4.0 + 4 Ø3.4 + 2 Ø8.0 = 26 bores, 30 cylindrical faces (26 concave, 4 convex); D-05a, D-05b, J-05 on all twenty; REQ-10 `locate_bore` on the four (no OD-C07 STEP yet: against the pattern) |
| Top face area (U-05 census) | rederive for 26 holes |
| Zones (reported, not gated) | valve zone x −117 … −67, z −154 … −35; tray zone x ±75, z −15 … +85; report the nearest hole-to-hole web (the new holes to the drain at (−80, −120) and to the feet hole at (−110, +90)) and hole-to-edge web (x −113 to the edge −120: 5.0) |
| Housing pose in the check assembly (U-03) | the group head is vertical (spec 1.2 §4, A-01): place OD-G01 v02 by the proper rotation local x → X, local y → +Z, local z → −Y with its origin at (0, 180.06, 32.0); read back its envelope (expected rear face y 205.0, mouth face y 176.76, x ±50, z −18 … +82) and its clearance to everything else (≥ 2.0). The carrier foot reference box becomes x ±55, y 0 … 4, z −70 … −26 (`od_c05_foot_reference_A01`); report the box's gap to OD-C04's foot (z −107) and to the tray zone |
| Everything else | as the plan and WP-03: OD-C03, OD-C04, OD-H01, OD-H11 joints unchanged; the plate's outline, feet, drains unchanged; OD-H11 booleans INCONCLUSIVE (A-14); spacing 0.7 |

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b,
D-06a, D-07 (N/A), J-05, E-06 (N/A), REQ-01 … REQ-10 (REQ-09 Soft bench:
INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs and environment

As in `briefs/WP-02_designer.md` and `briefs/WP-03_designer.md`; your v01 scripts
and REPORT.

## Findings to fix

None (v01 was not reviewed; superseded by the spec changes above).
