# WP-05 — designer brief, J3 package (build, round 2)

Job: 20260930-od-g01-group-head-housing · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 (chosen) · target `od_g01_housing_v02` · round 2, build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02). Write the checks first
(`01_CAD/check_od_g01_housing.py`), then the build (`01_CAD/build_od_g01_housing.py`)
and the placement of OD-G04 and OD-G10 for the U-03 and REQ-10 checks; export
through `tools.core.write_step` (AP242) into `02_STEP_STL/od_g01_housing_C1_v02.step`,
the check assembly into `02_STEP_STL/od_g01_assembly_C1_v02.step`, the STL into
`02_STEP_STL/od_g01_housing_C1_v02.stl`; re-import and measure; sections into
`03_Sections/`; the sweep into `01_CAD/sweep_v02/`; the REPORT into
`01_CAD/REPORT_od_g01_housing_v02.md` with its JSON block. Return the block your
skill defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with
the measured failure (D9).

## Round 2: what changed and what to keep

Round 1 (`01_CAD/REPORT_od_g01_housing_v01.md`, your own, which you may read as
findings) stopped on D-01a/D-01b/D-06a: 0.13 mm between the rear counterbore and
the pair-B screw holes. Spec 1.2 answers it and the rest of your §8 and §9:

| Item | Spec 1.2 |
|---|---|
| Rear counterbore | dropped: the Ø26.0 opening runs straight through the 5.00 slab (REQ-11 length 5.00 ± 0.10; REQ-13 is the two Ø9 pair-A holes only; A-24 revised) |
| Lip ring, pockets, riser | your deviations 1, 2, 3 are adopted: R 31.70 from the shelf down to −17.70, R 31.30 below; pocket as a notch between the lip wall and a riser at R 35.10, floor −17.30 (A-08, A-09) |
| Carrier insert bosses, no chamfer | your deviations 5 and 6 are adopted (§4 C1) |
| Lug underside | your deviation 4 is **rejected**: build the OEM's two planes (shallow plane, then one straight ramp from (+41.8°, −5.59) to (+54°, −1.15)), no knots. REQ-03's rays are now start + 1°, + 27°, + 40° (lug) and start − 1°, + 55° (gap) at z −3.0; REQ-04 brackets are start + 20°: −5.7 / −6.7 and start + 47°: −3.2 / −4.2 |
| U-03 against OD-G10 | its STEP cannot be healed (A-28): U-03(a) locked is `clearance = 0` at the three ear tops plus `clearance` in [0.19, 0.21] with OD-G10 lifted 0.20 along +Z; U-03(b) is `clearance ≥ 0.30` at every pose of the joint path except the last 0.5 mm of approach (≥ 0), at least 40 poses; report the boolean as INCONCLUSIVE beside them |
| Everything else | as round 1; the OD-G04 and OD-G10 joints stand; keep your scripts and re-run them, versioning every output `v02` |

Amendments to `01_CAD/DESIGN_PLAN.md` beyond the table above are the ones of
WP-03, still in force (slab 5.00, Ø9 lobes, pair-B recesses with Ø3.8 holes, the
OD-G04 joint at +6.05° with the flange seat, REQ-10 at 0.30, the census now
without the counterbore). List every difference from the plan in REPORT §8.

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

REPORT v01 §10: D-01a, D-01b, D-06a, U-06 at the counterbore (removed by spec 1.2). REPORT v01 §9.1: the underside knots (removed by spec 1.2).
