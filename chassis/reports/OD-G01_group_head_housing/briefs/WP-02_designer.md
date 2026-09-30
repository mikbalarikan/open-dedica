# WP-02 — designer brief, J2 package (plan only)

Job: 20260930-od-g01-group-head-housing · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_g01_housing_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md`. Build
nothing. The orchestrator checks that every spec feature (§4 C1) and every §5 gate
row has a planned feature and check before the J3 package is sent.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05, E-06,
REQ-01 … REQ-12; plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

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

None (first package).
