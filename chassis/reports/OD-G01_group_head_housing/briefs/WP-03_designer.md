# WP-03 — designer brief, J3 package (build)

Job: 20260930-od-g01-group-head-housing · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 (chosen) · target `od_g01_housing_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02). Write the checks first
(`01_CAD/check_od_g01_housing.py`), then the build (`01_CAD/build_od_g01_housing.py`)
and the placement of OD-G04 and OD-G10 for the U-03 and REQ-10 checks; export
through `tools.core.write_step` (AP242) into `02_STEP_STL/od_g01_housing_C1_v01.step`,
the check assembly into `02_STEP_STL/od_g01_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_g01_housing_C1_v01.stl`; re-import and measure; sections into
`03_Sections/`; the sweep into `01_CAD/sweep_v01/`; the REPORT into
`01_CAD/REPORT_od_g01_housing_v01.md` with its JSON block. Return the block your
skill defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with
the measured failure (D9).

## Plan amendments (spec 1.1, checked by the orchestrator)

Your J2 plan `01_CAD/DESIGN_PLAN.md` is checked and stands, with these amendments
from spec 1.1 (its §4 C1, §5 and §6 rows A-08 … A-13, A-24, A-26, A-27). Build to
them and list each as a deviation from the plan in REPORT §8; do not rewrite the
plan.

| Plan row | Amendment |
|---|---|
| F02 slab | 5.00 thick, z −24.94 … −19.94; envelope z 28.24 (U-02, D-02) |
| F05, F06 lip ring | upper R 31.70 (z −17.70 … −15.60), lower R 31.30 (z −19.94 … −17.70) |
| F07 pockets | floor z −17.30, riser R 35.00, same sectors |
| F10 keyhole | Ø26.0 through the slab, plus a rear counterbore Ø34.0 × 2.50 from the rear face (REQ-13); the Ø26 bore length is then 2.50 (REQ-11) |
| F11 lobes | two Ø9.0 through-holes at r 15.5, θ 359.5° and 179.0° (OD-G04 boss pair A pass-throughs; they merge with the Ø26 opening) |
| F12, F13 OD-G04 bosses | no inserts there: two Ø9.0 × 2.30 recesses from the floor and Ø3.8 through-holes at r 19.03, θ 119.3° and 304.0° (REQ-07, D-04a) |
| F14, F15 carrier inserts | Ø4.0 × 5.7 from the rear face at (±44, ±44); the boss on the floor side is now 0.70 high (5.7 − 5.0), OD 8.0 |
| §5 OD-G04 joint | clock +6.05° (tab 1 centre −3.3° in its frame onto pocket 1's sector centre 2.75°); seat: its flange bottom face (its z −13.12) on the floor z −19.94, so its back face is at housing z −6.82 |
| §6 U-03(a) | designed contacts: the three ear tops on the lug undersides at the locked pose, and OD-G04's flange bottom on the floor (`clearance = 0`); tabs, pair A, pair B, bead and hub `clearance ≥ 0.5` |
| §6 REQ-10 | `clearance ≥ 0.30` at every pose of the insertion path, rim z from −5.0 to the first-contact height, at least 5 poses |
| §6 census | 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 1 Ø34 counterbore, 2 Ø9 pass-through holes, 2 Ø9 recesses, 2 Ø3.8 through-holes, 4 Ø4.0 insert bores |

The OD-G10 joint of §5 (clock +60.26°, locked rim z −11.20, insertion clock
+122.5°) stands. Your R1 and R2 are answered by the ledger rows above; if the
built housing still overlaps OD-G04 or OD-G10 at these poses, that is a FAIL to
fix within the fix cycles, or a stop with the measured overlap (D9), never a
changed pose.

## Gate IDs to check (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05, E-06,
REQ-01 … REQ-13; plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` | 2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906 | reference: the OEM cup the housing reproduces; same frame as the housing (spec §2). Measure it to derive the parameters the spec gives as A-## rows, and to compare the housing with it |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | mating part, imported and placed by joint (spec A-12, A-13) |
| `00_Spec/inputs/OD-G10_portafilter.step` | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 | mating part, imported and placed by joint at the insertion pose and the locked pose (spec A-14, A-19) |
| `00_Spec/inputs/reports/*/PARAM_TABLE.md` | (hashed in `00_Spec/INTAKE_v01.md` §1) | the reverse-engineering parameters of each reference part, with their confidence tags |

Frames of the imported parts (from their reports): OD-G04 has z = 0 at its back
face with +Z the outward normal of that face (material in −Z), origin on the cup
axis, +X through tab 1 (tab 1 centre measured at −3.3°). OD-G10 has z = 0 at its rim
end face with +Z pointing out of its cup opening (material in −Z), origin on the cup
axis, +X toward the handle; its ears are centred at 59.5°, 180°, 300.5° from the
handle. Both must be placed by measured features (their tabs / ears and faces),
never by bounding boxes.

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-g01-group-head-housing` with
`OGUZ_WORK=${OGUZ_WORK}`, `OGUZ_JOBS=${OGUZ_JOBS}`
(`source the OGUZ env file`). Run any Python through
`uv run tools/run.py python <script>` from the repository root
`<repo>` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`. Library index: `library/INDEX.md`
(at most two cards). Tools documentation: `tools/README.md`.

## Findings to fix

None (first build). Deviations from the plan go in REPORT §8.
