# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20260930-od-g01-group-head-housing · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 · target `od_g01_housing_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed group-head housing OD-G01 of the Open
Dedica espresso machine: the plan `01_CAD/DESIGN_PLAN.md` (with the amendments
of `briefs/WP-03_designer.md`, which is part of the plan), the REPORT
`01_CAD/REPORT_od_g01_housing_v01.md`, and the exported files listed below.
Never the designer's scripts.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its
row), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A by
its row), J-05, E-06, REQ-01 … REQ-13; the §P list P1–P6; the feature census
against the plan; positive controls for every check family used.

## Files (relative to the workspace; SHA-256 as the REPORT lists them)

FILES_TABLE

Reference solids (inputs, for the assembly rows and the overlay):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` | 2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906 |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 |
| `00_Spec/inputs/OD-G10_portafilter.step` | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 |

`validity(OD-G09)` reads `brep_valid = 0` (the plan's R7): nothing is gated on
the OEM cup; OD-G04 and OD-G10 are the mating solids for U-03 and REQ-10, placed
by the joints the plan's §5 and the WP-03 amendments state.

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-g01-group-head-housing`; run
`source the OGUZ env file` in every shell command that runs Python, then
`cd <repo> && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_g01_housing_v01.md`, `.json`, and `RV01_work/`).
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
