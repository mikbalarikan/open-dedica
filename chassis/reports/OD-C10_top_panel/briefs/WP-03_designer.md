# WP-03 — designer brief, J3 re-check package (build v01 as built)

Job: 20261001-od-c10-top-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-01; 1.1 kept as `00_Spec/DESIGN_SPEC_v1.1.md`) · concept C1 · target `od_c10_top_v01` · build attempt 2 of 2 (counted by the job tool; no geometry change) · fix_cycles 3

## Package

The Usta accepted your v01 REPORT §10 option 1: the rear skirt's two corner
patches on OD-C11's wall top (x ±110 … ±116, z −302 … −299, y 215) are designed
contact. Spec 1.2 changes only U-03 (a)'s wording: the designed contact is the
line along x ±116 **and** the rear skirt's bottom face over its R 10 corner arcs
at x ±110 … ±116, `clearance = 0`, `interference ≤ 0`. No §4 value changes.

**Do not change the geometry and do not re-export the part.** Update
`01_CAD/check_od_c10_top.py` (versioned copy `check_od_c10_top_v01b.py`) so
U-03 (a) gates the clearance away from that whole contact region (≥ 0.5), the
contact patches' interference (≤ 0) and their area (report it), then re-run every
check on the existing `02_STEP_STL/od_c10_top_C1_v01.step` and assembly, confirm
their SHA-256 are unchanged (0f85c4d7…, d5881320…), write
`01_CAD/check_od_c10_top_v01b.json` and a new REPORT
`01_CAD/REPORT_od_c10_top_v01b.md` (outcome SUBMITTED if every Hard gate holds,
§10 replaced by the Usta's answer; never overwrite the v01 REPORT). Return the
block your skill defines.

## Gate IDs to check (spec §5)

As WP-02.

## Inputs

As `briefs/WP-02_designer.md`, with `00_Spec/DESIGN_SPEC.md` now
e2eda540dd141c27a3ca8f7a84f2d05cfbf99a1d8df283c03bff28000c4ee966 (1.2).

## Environment

As WP-02. Do not call any `mcp__hearthbot__*` tool; your hand-back goes to the
orchestrator only.

## Findings to fix

Your v01 stop (REPORT v01 §10): answered by spec 1.2's U-03 (a).
