# WP-05 — reviewer brief (J4, the one review of build v02)

Job: 20260930-od-c01-base-frame · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 · target `od_c01_frame_v02` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v02 of the printed base frame OD-C01 of the Open Dedica
espresso machine: the plan `01_CAD/DESIGN_PLAN.md` with the amendments of
`briefs/WP-03_designer.md` and `briefs/WP-04_designer.md` (both part of the plan),
the REPORT `01_CAD/REPORT_od_c01_frame_v02.md`, and the exported files listed
below. Never the designer's scripts (`01_CAD/*.py`, `01_CAD/probe/`,
`01_CAD/sweep_v0*/`). Build v01 was superseded by spec 1.1 and 1.2 before any
review and is not under review; ignore its files.

Spec 1.2's machine frame: X right, +Y up, +Z the front, the plate's top face y 0.
The group head axis is vertical with the mouth down (OD-C05 spec 2.0, RV01 F1 of
that job): OD-G01 v02 is placed by the rotation local x → X, y → +Z, z → −Y at
(0, 180.06, 32.0). Read the plausibility list against a real espresso machine
(the De'Longhi Dedica the project copies): the group head at the front over the
tray zone, the thermoblock behind it, the pump across the back, the valve and
flowmeter mount on the left, the electric zone on the right behind the bulkhead
line x = 65.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a: contacts with OD-C03 and OD-C04, coaxial holes, the OD-H01
and OD-H11 clearances, OD-H11 max z, the OD-G01 pose and clearance; b N/A by its
row), U-04 (the part; on the check assembly the designer reads OD-H11's round
trip INCONCLUSIVE at 0.0524 mm³ by OD-C04 A-14: rule on that reading), U-05,
U-06 (Soft), U-07 (the 3MF `02_STEP_STL/od_c01_frame_C1_v02.3mf` was written by
the orchestrator from the designer's STL and re-parsed: 7068 triangles, volume
580358.52 mm³; check it against the STL), U-08 (N/A), D-01a, D-01b, D-02,
D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-06 (N/A),
REQ-01 … REQ-10 (REQ-09 is a Soft bench gate: INCONCLUSIVE with a risk rating;
REQ-10 checks against the OD-C07 pattern, there is no OD-C07 STEP yet, A-17);
the §P list; the feature census against the plan as amended (1 plate, 20 Ø4.0,
4 Ø3.4, 2 Ø8.0 through-holes); positive controls for every check family used.

OD-H11 reads `brep_valid = 0` (OD-C04 A-14): its booleans are INCONCLUSIVE by
the rows; gate its rows on distance measurements. The carrier OD-C05 is not
built yet (its v02 is in design): the assembly holds its foot outline as the
reference box `od_c05_foot_reference_A01` (x ±55, y 0 … 4, z −70 … −26); rate
what rests on it. Weigh the REPORT's least-sure items and the open assumptions
the layout rests on: A-01 (the housing pose and height), A-02 (thermoblock
joint), A-03 (pump joint), A-05 / A-17 (the OD-C07 pose, whose spec is itself
at REVISE), A-06 (the tray zone under the mouth), A-09 (Kobra Max 3 bed),
A-10 / REQ-09 (PETG warp on a 405 plate), A-11 (5.7 inserts in a 6.0 plate),
A-17's 5.0 web from the OD-C07 holes to the plate's edge.

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `01_CAD/REPORT_od_c01_frame_v02.md` | 78a03e899b024380df0d0bce9495ad3184ed13a0c454b8a2815a113e4d3bea7b |
| `01_CAD/DESIGN_PLAN.md` | 086dde812dcc207fa171977fb45f9d2ed5a8df324099bce8c813eb3651aa7217 |
| `briefs/WP-03_designer.md` | b34294f10520e24cccaf90a702191bde0628805841af037bc0208de0980f9004 |
| `briefs/WP-04_designer.md` | 4634cd15f8906089a3129561831220145920ddd5cadd8ed6136513298254d513 |
| `01_CAD/check_od_c01_frame_v02.json` | e629e5555b94a10952302443ca89b1bcd73b89e40a2e27c0c3104d29dba19728 |
| `01_CAD/build_record_v02.json` | d3efabdd7a6fe5362089182e9f65ca4569aeb3a11e4b0a827e21e77cb868807c |
| `01_CAD/sections_v02.json` | 67b31897473368a6e9b70abae088c605d49dfb4ddddddcec85ad84197f3cb173 |
| `01_CAD/sweep_v02/sweep_summary_v02.json` | 38bfd098bf06cd107577c145d3e2c3ca2e6448976611a8ddf837a9f188a3a6e7 |
| `02_STEP_STL/od_c01_frame_C1_v02.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 |
| `02_STEP_STL/od_c01_assembly_C1_v02.step` | 07560bb0caafc1e986434eede5ae22abaef9f599437948145a8a3c18e2129749 |
| `02_STEP_STL/od_c01_frame_C1_v02.stl` | 26bf61039e5fcbc210643fb38cd188e31a66e7b5b6e065da6eb93ffa216125db |
| `02_STEP_STL/od_c01_frame_C1_v02.3mf` | 8023c837502843ba6a9c65b5bbbdb839652d1ea13585170d112e0dd1655f4073 |
| `03_Sections/od_c01_frame_v02_front_y-3_plan.png` | 88b9cbd2ec70692def33d72d97840269a2f51e02f23887b8e44a9900b778611a |
| `03_Sections/od_c01_frame_v02_left_asm_x0.png` | 3134671c9368d087f859d8a8b0fbb7bdc6e12c08c95ef92eb5d827fd4cee6afb |
| `03_Sections/od_c01_frame_v02_left_asm_x37.png` | 4fe5dd02ceaadde3f871166e53edd1bf72f65d1b23823abea05f56af58f05d35 |
| `03_Sections/od_c01_frame_v02_left_x-113_valve.png` | 5002f1a3966f5b237d8a8f1078d2f6d176e18e0535aed58ee2624c0277be86a9 |
| `03_Sections/od_c01_frame_v02_left_x37_c03.png` | f277220f4e3d3e253c14fc5473606fa57f1169138a512c865ede0e7a1b374390 |
| `03_Sections/od_c01_frame_v02_left_x65_bulkhead.png` | e0696dd0380a374523a56c29db2fa4d6ce4c7a33190308c5064eb7d270eecb87 |
| `03_Sections/od_c01_frame_v02_top_asm_z-148.png` | 7af641ca4644a3b94eab4a29e570131f839209ead0ed8561281c38be0ff3332b |
| `03_Sections/od_c01_frame_v02_top_asm_z32_mouth.png` | e6826257791fe8263b8f9d32a55170bec8dc4b797a7ce0f81266b96658c2a2b6 |
| `03_Sections/od_c01_frame_v02_top_z-120_drain.png` | 830ff2b0ce9de90e13805289c4ea33e06df474e3c406a5ea62754e7b031df3d8 |
| `03_Sections/od_c01_frame_v02_top_z-148_c04.png` | 7a49c0f651bc62ca766083d6a75211154f7f16c4e0af16fa721c9109dbfc9136 |
| `03_Sections/od_c01_frame_v02_top_z-40_carrier.png` | 4f5e942c25f9f3876aa1098ddec6d4a84c648506a6b9e8daa15556588764d7a1 |
| `03_Sections/od_c01_frame_v02_top_z-42_valve.png` | 69de67f64fdd19acb87af1e2e083ded63d9b55661cd495081842a6cf3bbd56dd |
| `03_Sections/od_c01_frame_v02_top_z90_feet.png` | 56ebdb7cefd23dbb3645f2f482f9ac66d4659d6cd40a341f38677dbcb626f0d4 |

Reference solids (inputs, for the assembly rows):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-C03_pump_cradle.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 |
| `00_Spec/inputs/OD-C04_thermoblock_mount.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 |
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff |

The joints are in spec §4: OD-C03 rotated local x → +Z, y → −Y, z → +X at
(0, 40, −205) with OD-H01 at its identity; OD-C04 at the identity rotation at
(0, 70, −140) with OD-H11 at its identity; OD-G01 as above.

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c01-base-frame` (`/home/claude/oguz-jobs/20260930-od-c01-base-frame`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_c01_frame_v02.md`, `.json`, and `RV01_work/`); if
the Write tool refuses a file, write it with Bash. `min_wall` and
`overhang_census` need `spacing=0.7` on this plate (the designer's finding).
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
