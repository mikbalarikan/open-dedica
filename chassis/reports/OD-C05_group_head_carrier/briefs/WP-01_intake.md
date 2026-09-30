# WP-01 — intake brief (20260930-od-c05-group-head-carrier)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C05 is the 3D-printed group head carrier of the Open Dedica espresso machine: the bracket that takes the printed group head housing OD-G01 by the four M3 heat-set inserts in its rear flange, passes the OD-G04 hub tube and the hot water tube behind the housing, holds the group head at least 95 mm above the drip tray, and ties down to the printed base frame OD-C01 (not designed yet). OD-G01 is at its third build round in its own job; its rear flange has not changed since its spec 1.2, and its build v02 STEP is the reference geometry here, with its spec 1.3 and its REPORT v02 as the reports. OD-G04 (the gasket support whose hub tube passes through the housing) and OD-H11 (the thermoblock behind the group head) are scan-rebuilt STEP files with their reports. The drip tray OD-C21, the 3-way valve connector OD-H23 and TUBE 7 are not scanned; everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-G01_housing_C1_v02.step
- 00_Spec/inputs/OD-G04_brewing_gasket_support.step
- 00_Spec/inputs/OD-H11_thermoblock.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-G01_group_head_housing/DESIGN_SPEC_v1.3.md
- 00_Spec/inputs/reports/OD-G01_group_head_housing/REPORT_v02.md
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/README.md
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/deliver_README.md
- 00_Spec/inputs/reports/OD-H11_thermoblock/README.md
- 00_Spec/inputs/reports/OD-H11_thermoblock/params.json
- 00_Spec/inputs/reports/OD-H11_thermoblock/ports.json
- 00_Spec/inputs/reports/OD-H11_thermoblock/export_check.json
- 00_Spec/inputs/scan/OD-H11_thermoblock/README.md
- 00_Spec/inputs/scan/OD-H11_thermoblock/calipers.md

The three STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown, csv and json file fully. The OD-G01 spec (§2 frame, §4 C1, §5 rows REQ-06, REQ-08, REQ-11, D-05a, D-05b, J-05, §6 rows A-10, A-11, A-12, A-17, A-18, A-24, A-26, §7 the Q10 decision) and its REPORT v02 (§1 files, the gate table rows for the rear slab, the inserts, the hub opening and the envelope, §5 placement of OD-G04, §8 deviations) give the housing's rear interface: the slab, the rear face plane, the insert positions and hole sizes, the hub opening, the pair-B screw holes driven from the rear, the OD-G04 hub position and its bottom z as placed, the envelope. The OD-G04 reports give the hub tube (outer radius, bottom z in its own frame, the frame definition) and the plate. The OD-H11 reports give the thermoblock's frame, envelope, the water pipes and terminals (ports.json: positions and directions), and the deviation numbers. REQUEST.md holds the Usta's request and the standing instruction; PROJECT_RULES.md the chassis order of work, the sourcing guide's thermoblock and group head sections, the chassis design rules (the ≥ 10 mm air gap, the ≥ 95 mm group head height, the two-zone layout, materials), the water path (TUBE 7 from OD-H23 port C to the group head) and the safety note; bom_rows.csv the bill-of-materials rows that touch this part.

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension a carrier could touch or must clear must appear as its own X-## row: the OD-G01 rear flange (slab thickness and z range, the 100 × 100 square and its corner radius, the rear face z, the four insert positions, hole diameter and depth, the boss on the floor side, the Ø26 hub opening, the two pair-B screw holes and their recesses, the outer wall Ø86.2 and the front face z, the envelope), the OD-G04 hub tube (outer radius, bottom z, the stepped bore) and where the housing's REPORT places OD-G04 (its back face z, hub bottom z), the OD-H11 envelope, frame, pipes and terminals, and the deviation numbers of every scan. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (material, process, the ≥ 10 mm air gap to the thermoblock, the ≥ 95 mm group head height, the wet/electric separation and drainage, serviceability, the M3 insert and screw standard, the chassis order-of-work and blockers) goes in section 3 as an X-## row with its quote. Everything the inputs do not give — the thermoblock's position and orientation relative to the housing, the drip tray height and the tray's position under the group head, TUBE 7's route, bend radius and the OD-H23 connector's size and position, OD-C01's mounting interface and its floor level, the housing's orientation about its own axis in the machine, the machine's front and up directions in the OD-G01 frame, the print orientation and machine — goes in section 4 as questions, never resolved. Conflicts between the OD-G01 spec and its REPORT, or between params.json and README.md, go in section 4 too.

## Environment

Workspace: ${OGUZ_JOBS}/20260930-od-c05-group-head-carrier (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template.
