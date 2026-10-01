# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20260930-od-c05-group-head-carrier · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 · target `od_c05_carrier_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed group head carrier OD-C05 of the Open
Dedica espresso machine: the plan `01_CAD/DESIGN_PLAN.md` (with the amendments of
`briefs/WP-03_designer.md`, which is part of the plan), the REPORT
`01_CAD/REPORT_od_c05_carrier_v01.md`, and the exported files listed below.
Never the designer's scripts (`01_CAD/*.py`, `01_CAD/probe/`, `01_CAD/sweep_v01/`).

The build was made to spec 1.1; spec 1.2 changed one wording only: the named
exception's bridge limit reads ≤ 6.6 (REQ-02's upper tolerance) instead of
≤ 6.5, after the sweep's Ø6.6 rung showed the mismatch (REPORT §9 item 2). No
geometry changed. Review against 1.2 and write `"spec_version": "1.2"` in the
JSON twin.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a: contact with OD-G01, clearance to OD-G04, hole-to-insert
offsets; b N/A by its row), U-04, U-05, U-06 (Soft), U-07 (the 3MF
`02_STEP_STL/od_c05_carrier_C1_v01.3mf` was written by the orchestrator from the
designer's STL and re-parsed: 4264 triangles, volume 108716.928 mm³; check it
against the STL), U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b,
D-04a, D-06a, D-07 (N/A by its row), E-06, REQ-01 … REQ-09 (REQ-09 is a Soft
bench gate: INCONCLUSIVE with a risk rating); the §P list; the feature census
against the plan as amended (1 wall with R 6 top corners about (±44, 44), 1 foot,
2 gussets, 2 windows with 45° gables, 4 Ø3.4 through-holes along Z with 4 Ø6.5 × 2.0
counterbores from the rear face, 4 Ø3.4 through-holes along Y); positive controls
for every check family used.

Two rows need your own reading:

- **D-03a.** The designer's `overhang_census` reads INCONCLUSIVE because the two
  window arcs are tangent to their 45° gables and the tool cannot settle a curved
  face whose least angle lies exactly at the limit (REPORT §7, §9 item 1); no
  sample is under 45°, the gables read 45.0000°. The spec row names "reviewer
  from sections" as a check: read the sections `x0` and `zm27p44`, and settle the
  row by your own method (for example the tangent direction of each arc at its
  junction with the gable, or the analytic angle of the cylinder at the gable's
  tangent point). The eight horizontal hole and counterbore crowns are the named
  exception of §5 (D-03a and D-03b): confirm that the designer's exclusion took
  exactly those eight faces and nothing else, by your own method (REPORT §9 item 3).
- **D-03b.** Nominal crowns 6.5, the exception's limit now 6.6; nothing else
  bridges. Confirm from the sections.

Weigh the REPORT's least-sure items and everything that rests on the open
assumptions: A-01 (the OD-G01 v02 flange is the reference; unchanged since spec
1.2 of that job), A-03 (axis 175 from the OD-C01 layout), A-05 (nothing behind
z −70), A-06 (r ≤ 30 window), A-09 (M3 × 8 through a 2.0 counterbore into a 5.7
insert: check the screw arithmetic), A-11 / REQ-09 (a 225 tall, 5 thick ASA wall
with two 40 × 40 gussets under the locking torque).

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `01_CAD/REPORT_od_c05_carrier_v01.md` | 6f730d02d7f9fa1fcee9826332e42473b2408e2a86c1b1e7f5a544362a305356 |
| `01_CAD/DESIGN_PLAN.md` | 41b80f841cb6ee700fe5dc7590b8b1db5403458e469af64b5673cf5f0232eced |
| `briefs/WP-03_designer.md` | (the plan amendments) |
| `01_CAD/check_od_c05_carrier_v01.json` | 1c57b36c81835e0774266f800d9c3d333f0e66638e2d4bbcbf7ca2105866e03d |
| `01_CAD/build_od_c05_carrier_v01.json` | d3457f40ea3fcf9a7d10e3ae7f1ca808c85d1f6dabbeb4a2917994211bd75102 |
| `01_CAD/sections_od_c05_carrier_v01.json` | 298b88918bd3cc23b4e1d8a25083b5d7591753fa30ca7d2a21fcd9f9d2c7f8bc |
| `01_CAD/sweep_v01/SHA256SUMS_v01.txt` | 2cbc6e99df38bb23293aa1e11ff4d629748c4a97060ac7eea4453f29fb1805ca |
| `02_STEP_STL/od_c05_carrier_C1_v01.step` | 3555600be58771b0efba7b2f2b5a48439bb442db58d5b5eb92fdd6a6fe410362 |
| `02_STEP_STL/od_c05_assembly_C1_v01.step` | b6fdbea9466703e81d63938840ce82853cddcac9c4f537d7e5d721f55817e1c3 |
| `02_STEP_STL/od_c05_carrier_C1_v01.stl` | aee6d05a1573742d131cb949e86b98acceb6fca179dc2cd46394a4918c8fe48a |
| `02_STEP_STL/od_c05_carrier_C1_v01.3mf` | (written by the orchestrator; hash in the ledger) |
| `03_Sections/od_c05_assembly_x0_v01_left.png` | 45c952415736c7a6bdad835d995b0f4f21af525050efb8a02efac15f14e57ecf |
| `03_Sections/od_c05_carrier_x0_v01_left.png` | ff005505cf4bffe0b1fe8002cbaea64f9961c2a69184a484a0d6a1e25b9a13dd |
| `03_Sections/od_c05_carrier_x35_v01_left.png` | edf5390642a14c4dd97241fd525ae097c3ad1305768cdb093727a3c0eab477c8 |
| `03_Sections/od_c05_carrier_x44_v01_left.png` | 7972feb30a6f1a93646deca2bfe23305cc489a611111c9b6e3650f34375062d7 |
| `03_Sections/od_c05_carrier_x48_v01_left.png` | 7d95e4c21d402ead81af662b28df7eea4e04ca042f7f0061b88683c8584e762c |
| `03_Sections/od_c05_carrier_y44_v01_front.png` | 400b0fbacba5c85ebc25ca1aecfeaa2fa5ee024be96bbc49e77ea8eb8fefdbfe |
| `03_Sections/od_c05_carrier_ym110_v01_front.png` | 537c6d019dd9ff66a5758ad7a169dd3a47c903e395f3bf67883901129cd82dec |
| `03_Sections/od_c05_carrier_zm27p44_v01_top.png` | 49e475ca672c694dab36d477b1545de225eb4103a352b13575cf50d62f827d83 |

Reference solids (inputs, for the assembly rows):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 |

OD-G01 sits at the identity pose (spec §2); OD-G04 is rotated +6.05° about Z and
translated z −6.82 (plan §5, from the OD-G01 REPORT v02 §5).

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c05-group-head-carrier` (`/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_c05_carrier_v01.md`, `.json`, and `RV01_work/`); if
the Write tool refuses a file, write it with Bash.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
