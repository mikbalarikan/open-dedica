# WP-02 — designer brief, J2 package (plan only)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c05_carrier_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md`. Build
nothing. The orchestrator checks that every spec feature (§4 C1) and every §5 gate
row has a planned feature and check before the J3 package is sent.

Things the plan must settle by measuring the OD-G01 STEP (spec A-01): its rear face
plane (expected z −24.94), the four insert bores (expected Ø4.0 × 5.7 at (±44, ±44),
opening on the rear face toward −Z), the flange outline (100 × 100, corner radius),
the hub opening and anything on the rear face that protrudes behind z −24.94 (there
should be nothing: the carrier's front face is a full-face contact). Also place
OD-G04 as the OD-G01 REPORT v02 §5 places it (plate back face at housing z −6.82,
clocked +6.05° about Z; the REPORT and the OD-G01 spec §4 / A-12 / A-13 give the
joint) and measure where its hub tube and boss pairs end behind the housing's floor
(expected hub bottom z −22.55, inside the slab, INTAKE X-36 … X-38): the U-03 row
against OD-G04 depends on it, and if anything of OD-G04 reaches behind z −24.94 the
hub window's r ≤ 30 must be checked against it. Report whether `validity` reads
sound for OD-G01 v02 and OD-G04, since U-03's boolean depends on it. If any spec
value cannot be met, stop and report the measured conflict; never change a spec
value yourself. OD-H11 is an input for reference only: it is not placed and not
gated (spec A-05, REQ-07).

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b (with the named exception of §5), D-04a, D-06a, D-07 (N/A by its
row), E-06, REQ-01 … REQ-09 (REQ-09 is a Soft bench gate: the plan says so); plus
`exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | the housing the carrier holds; same frame as the carrier (spec §2), placed at the identity pose. Measure it for A-01, REQ-01, REQ-03, U-03 |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | the gasket support whose hub passes through the housing; placed by the joint the OD-G01 REPORT v02 §5 states (frame: plate back face z = 0, +Z outward normal of that face, material in −Z, origin on the cup axis, +X through tab 1) |
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | reference only, not placed (A-05) |
| `00_Spec/inputs/reports/OD-G01_group_head_housing/REPORT_v02.md` | 02ee81dea9dc7fd9d2dd249cc32481fa96c61e6c89c627df5d8c59466742d5b6 | the housing's measured build: §5 placement of OD-G04, the gate table rows for the rear slab and inserts |
| `00_Spec/inputs/reports/OD-G01_group_head_housing/DESIGN_SPEC_v1.3.md` | 55841f6ba178ac7250a22e156b55941002437a794ce008f231c1ea090138e44b | the housing's spec: §2 frame, §4 C1, A-12, A-13, A-17, A-18, A-24 |
| `00_Spec/INTAKE_v01.md` | (hashed in the job record) | the intake rows X-01 … X-83 |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c05-group-head-carrier` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`. Library index: `library/INDEX.md`
(at most two cards). Tools documentation: `tools/README.md`. If the Write tool
refuses a file, write it with Bash.

## Findings to fix

None (first package).
