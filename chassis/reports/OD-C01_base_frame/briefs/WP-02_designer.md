# WP-02 — designer brief, J2 package (plan only)

Job: 20260930-od-c01-base-frame · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c01_frame_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md`. Build
nothing. The orchestrator checks that every spec feature (§4 C1) and every §5 gate
row has a planned feature and check before the J3 package is sent.

Things the plan must settle by measuring the inputs, each placed by the joint the
spec §4 states (write the placements as probe scripts under `01_CAD/probe/`, with
their JSON results, as the OD-C05 plan did):

1. **OD-C03 as placed** (rotation local x → +Z, y → −Y, z → +X; origin (0, 40, −205)):
   its foot underside plane (expected y = 0.00, normal −Y), the four Ø3.4 foot
   holes' axes and their (x, z) (expected (−4, −239), (−4, −171), (37, −239),
   (37, −171)), its envelope. Report whether the rotation is proper (determinant
   +1) and whether the delivered STEP is sound (`validity`).
2. **OD-C04 as placed** (identity rotation, origin (0, 70, −140)): foot underside
   (expected y 0.00), holes (expected (±40, −148), (±40, −114)), envelope.
3. **OD-H01 as placed** with OD-C03 (the same joint; the pump sits at OD-C03's
   identity): envelope, lowest point above the plate, extent in x (expected
   −66.45 … +55.5), clearance to the plate top face.
4. **OD-H11 as placed** with OD-C04: envelope (expected max z ≤ −85.0), lowest
   point above the plate (expected ≥ 16.5), the ≥ 10.0 clearance to the plate.
   OD-H11 is scan-derived and its boolean is INCONCLUSIVE by OD-C04 A-14: say so.
5. **OD-G01 v02 at the carrier's pose** (identity rotation, origin (0, 175, 0)):
   envelope (its mouth at z +3.30, lowest point y 131.9), and its clearance to
   every other placed solid. The OD-C05 carrier is not built yet: place its foot
   outline (x ±50, y 0 … 4, z −69.94 … −24.94) as a reference box for U-03 and
   say in the plan that the real solid replaces it when OD-C05 delivers (A-01).
6. The **gaps between neighbours** on the plate: OD-C03 to OD-C04, the carrier
   box to OD-C04, OD-H11 to the carrier box (the thermoblock zone, REQ-08), and
   whether any placed solid enters a reserved zone of §4 (tray, tank, valves,
   electronics) or crosses the bulkhead line x = 65.
7. Whether the sixteen Ø4.0 insert holes, the four Ø3.4 feet holes and the two Ø8
   drain holes keep J-05 (≥ 3.0 wall) and D-05a to each other and to the plate's
   edge; the nearest pair reported.

Every spec value is the spec's: if any cannot be met, stop and report the
measured conflict with options; never change a spec value yourself. The
OD-C05 spec became 1.1 after this job's intake (foot underside y −175 in the
carrier's frame, so that its origin at (0, 175, 0) puts the foot on y 0; holes
unchanged): use the values in this job's spec §4, which already carry it.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05,
E-06 (N/A by its row), REQ-01 … REQ-09 (REQ-09 is a Soft bench gate: the plan
says so); plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-C03_pump_cradle.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | the delivered pump cradle (its own frame: OD-H01's, +Y down, foot underside y +40) |
| `00_Spec/inputs/OD-C04_thermoblock_mount.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 | the delivered thermoblock mount (its own frame: OD-H11's, −Y down, foot underside y −70) |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | the housing at the carrier's pose |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | the pump, at OD-C03's identity |
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | the thermoblock, at OD-C04's identity |
| `00_Spec/inputs/reports/OD-C03_pump_cradle/DESIGN_SPEC_v1.2.md` | 0bd94d9b6060ec4ea387fce26d20bdab5ac05c5829bd9993828dae677982584b | OD-C03's frame (§2), foot and holes (§4, REQ-05, REQ-06) |
| `00_Spec/inputs/reports/OD-C04_thermoblock_mount/DESIGN_SPEC_v1.2.md` | 388f7fd170b4313cc53d5039d4db6f2eefdc79bca93c64c44ebe7e9563970b8c | OD-C04's frame, foot and holes, A-14 (OD-H11 boolean) |
| `00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v1.0.md` | 021f718529f8edaf1bd1c14da433cbe061acfa35db172aa471e3c6be651c4966 | OD-C05's frame, foot and holes (spec 1.0; 1.1 moved the foot to y −175, see above) |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md` | 52b06473b31a2365a638bf0daa993d2dfa32f1121a0caefbb74ff58c72657fa2 | the pump's frame |
| `00_Spec/inputs/reports/OD-H11_thermoblock/README.md` | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0 | the thermoblock's frame |
| `00_Spec/INTAKE_v01.md` | a949acf05d133da63dcc751bd73c7cdc2682783acd6b46217274c97179870856 | the intake rows |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c01-base-frame` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`. Library index: `library/INDEX.md`
(at most two cards). Tools documentation: `tools/README.md`. Precedent for the
plan's shape and probes: `${OGUZ_JOBS}/20260930-od-c05-group-head-carrier/01_CAD/`.
If the Write tool refuses a file, write it with Bash.

## Findings to fix

None (first package).
