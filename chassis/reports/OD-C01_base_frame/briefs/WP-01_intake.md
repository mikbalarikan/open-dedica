# WP-01 — intake brief (20260930-od-c01-base-frame)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C01 is the 3D-printed base frame (floor plate) of the Open Dedica espresso machine: the plate every printed mount stands on and screws into, which sets the machine's footprint, carries the drip tray at the front under the group head, and separates with the bulkhead OD-C02 (next job) the wet zone from the electric zone. Three mounts already exist and each defines its own foot: the pump cradle OD-C03 (spec 1.2, delivered STEP), the thermoblock mount OD-C04 (spec 1.2, delivered STEP) and the group head carrier OD-C05 (spec 1.0, in design). Each spec fixes the foot underside plane, the four Ø3.4 screw holes in the foot, and the frame in which the OEM part it holds sits; the delivered STEP files of OD-C03 and OD-C04 and the OD-G01 housing v02 STEP, with the pump OD-H01 and thermoblock OD-H11 STEP files, are the solids that OD-C01's layout must place. The drip tray OD-C21/C22, the tank dock OD-C06, the valve mount OD-C07 and the electronics bay OD-C08 are not scanned or designed; everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-C03_pump_cradle.step
- 00_Spec/inputs/OD-C04_thermoblock_mount.step
- 00_Spec/inputs/OD-G01_housing_C1_v02.step
- 00_Spec/inputs/OD-H01_ulka_ep5_pump.step
- 00_Spec/inputs/OD-H11_thermoblock.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-C03_pump_cradle/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C04_thermoblock_mount/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v1.0.md
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md
- 00_Spec/inputs/reports/OD-H11_thermoblock/README.md
- 00_Spec/inputs/reports/OD-H11_thermoblock/export_check.json

The five STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown, csv and json file fully. Each of the three DESIGN_SPEC files gives, in its §2 (coordinate frame and which direction is down or up in the machine), §4 C1 (the foot plate: thickness, extent, the four hole positions, the envelope), §5 (the foot plane and frame hole rows) and §6 (the OD-C01 interface row, the thermoblock zone, the group head height, the machine orientation rows), what OD-C01 must provide under that part; the OD-H01 and OD-H11 READMEs give the OEM parts' frames and envelopes; REQUEST.md the Usta's request, the standing instruction and the layout intent; PROJECT_RULES.md the chassis order of work, the scan-to-STEP rules, the chassis design rules (two zones, anti-vibration, thermal map, serviceability, the ≥ 95 mm group head height, the 0.4 m³ envelope figure, sensor bosses, safety), the water path and the drip tray issue; bom_rows.csv the bill-of-materials rows that touch this part (the printed chassis parts, the tray, the feet, the OEM parts the mounts hold, the fasteners).

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension OD-C01 must provide or clear must appear as its own X-## row, per mount: the foot underside plane and its direction in that part's frame, the foot thickness and extent, the four hole positions and diameter, the part's envelope, the OEM part's envelope and frame in that mount's frame (pump: its axis, length, the frame plates; thermoblock: its axis, the outlet face, the ≥ 10 mm rule, the zone the carrier assumes), the group head axis height above the floor and the housing's lowest point, the C05 wall and foot extents, and every "OD-C01 must" statement of the three specs' §6 rows. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (material and printer per part, the two-zone rule, the drainage path, the thermal map, the group head height, the feet, removable panels, the machine order of work, fasteners, the tray's role) goes in section 3 as an X-## row with its quote. Everything the inputs do not give — the machine footprint and overall height, where each mount sits on the plate (their relative positions and the front direction), the drip tray's size, height and position, the water tank's size and dock, the flowmeter and valve positions, the electronics path and its bay, the feet, the Kobra Max 3 and K1C build volumes, the plate's own print orientation and whether it prints in one piece — goes in section 4 as questions, never resolved. Conflicts between the three specs (for example which way is "down" in each frame, or two parts claiming the same floor area once placed) go in section 4 too.

## Environment

Workspace: ${OGUZ_JOBS}/20260930-od-c01-base-frame (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template.
