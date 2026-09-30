# WP-06 — designer brief, J3 package (round 2, build attempt 2: re-measure v02's geometry as v03 under spec 1.3)

Job: 20260930-od-g01-group-head-housing · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.3 (ratified 2026-09-30) · concept C1 (chosen) · target `od_g01_housing_v03` · round 2, build attempt 2 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02). Write the checks first
(`01_CAD/check_od_g01_housing.py`), then the build (`01_CAD/build_od_g01_housing.py`)
and the placement of OD-G04 and OD-G10 for the U-03 and REQ-10 checks; export
through `tools.core.write_step` (AP242) into `02_STEP_STL/od_g01_housing_C1_v03.step`,
the check assembly into `02_STEP_STL/od_g01_assembly_C1_v03.step`, the STL into
`02_STEP_STL/od_g01_housing_C1_v03.stl`; re-import and measure; sections into
`03_Sections/`; the sweep into `01_CAD/sweep_v03/`; the REPORT into
`01_CAD/REPORT_od_g01_housing_v03.md` with its JSON block. Return the block your
skill defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with
the measured failure (D9).

## Attempt 2 of round 2: what changed

Your round-2 build (`01_CAD/REPORT_od_g01_housing_v02.md`, the findings to fix)
passed every geometric row and stopped only on U-03(a)'s 0.20 mm probe, whose
spec 1.2 wording displaced OD-G10 along +Z, the direction that drives the ear
tops into the lug undersides. Spec 1.3 corrects the row and nothing else:

| Item | Spec 1.3 |
|---|---|
| U-03(a) housing|OD-G10 | the locked pose is the measured first contact of the three ear tops with the lug undersides as OD-G10 moves along +Z at the locked clock (report the rim z; A-14 expects −11.20 ± 0.10); `clearance = 0` there; `clearance` in [0.19, 0.21] with OD-G10 displaced 0.20 along **−Z** from that pose |
| A-14 | the locked rim height is the measured contact (v02: −11.251), no longer a fixed −11.20 |
| Geometry | **unchanged**: run `01_CAD/build_od_g01_housing_v02.py` as it is (record its SHA-256 in the REPORT; if you copy it to a v03 name, the copy must be byte-identical apart from the output names) and export the v03 files; with the pinned timestamp the v03 STEP should hash the same as v02's, which you state in REPORT §5 |
| Checks | re-run every §5 row on the re-imported v03 STEP under spec 1.3 (`check_od_g01_housing_v03.py`), the assembly and the path (`assemble_od_g01_check_v03.py`), the sections (v03 names) |
| D7 sweep | the v02 sweep stands when the build script is unchanged: cite `01_CAD/sweep_v02/sweep_v02.json` and its hash in REPORT §4 and state why; do not re-run 40 builds for an unchanged script |
| REPORT | `01_CAD/REPORT_od_g01_housing_v03.md`, every §5 row answered, the JSON block with tag v03 |

The WP-03 and WP-05 amendments stay in force. If the probe still misses
[0.19, 0.21] at the measured contact pose, stop with the measured value (D9):
that would be a fact about the geometry, not the wording.

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

REPORT v02 §10: U-03(a) 0.20 mm probe 0.149 against [0.19, 0.21] (a wording error, corrected by spec 1.3).
