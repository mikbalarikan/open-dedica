# WP-01 — intake brief (20260930-od-c02-bulkhead)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C02 is the 3D-printed bulkhead of the Open Dedica espresso machine: a wall standing on the base frame OD-C01 along the plane x = 65 that separates the wet zone (pump, thermoblock, group head, valves, tank) from the electric zone (the electronics bay at x ≥ 70), carries the drainage path, and passes the wires that cross between the zones. OD-C01 is delivered and fixes the bulkhead's foot interface; the tube runs, the electronics bay OD-C08, the panels OD-C10 … C13 and the wiring are not designed or scanned: everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-C01_base_frame.step
- 00_Spec/inputs/OD-C03_pump_cradle.step
- 00_Spec/inputs/OD-C04_thermoblock_mount.step
- 00_Spec/inputs/OD-G01_housing_C1_v02.step
- 00_Spec/inputs/OD-H01_ulka_ep5_pump.step
- 00_Spec/inputs/OD-H11_thermoblock.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C01_base_frame/REPORT_od_c01_frame_v02.md
- 00_Spec/inputs/reports/OD-C04_thermoblock_mount/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v2.1.md

The six STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully. The OD-C01 spec gives, in its §2 (machine frame), §4 C1 (the layout: every mount's joint and footprint, the bulkhead line and its four insert holes, the reserved zones, the drain holes, the plate's outline and thickness) and §6 (A-04 the bulkhead interface, A-05 … A-08 the zones, A-16 the machine height), what OD-C02 must stand on and separate; its REPORT v02 gives the measured positions of the placed neighbours (envelopes and clearances). The OD-C04 and OD-C05 specs give the parts nearest the wall (the thermoblock's terminals and pipes; the carrier's column and hatch) in their own frames with the joints OD-C01 §4 states. REQUEST.md gives the Usta's request, the standing instruction and the interface as OD-C01 fixed it; PROJECT_RULES.md the chassis order of work, the chassis design rules (the two zones, the thermal map, drainage, serviceability, safety, the removable panels), the water path and the electrical parts; bom_rows.csv the bill-of-materials rows that touch this part (the bulkhead, the electronics bay, the panels, the electrical and water parts whose wires or tubes cross, the fasteners).

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension OD-C02 must meet or clear must appear as its own X-## row: the wall plane, its z extent and the four insert positions and diameter (OD-C01 A-04, REQ-04), the plate's top face and thickness, every neighbour's extent toward x = 65 as OD-C01 places it (the pump's +X end, the thermoblock mount's foot edge at x 50, the carrier's column at x 55, the electronics zone from x 70), the machine height and the reserved zones, the drain holes, the tube diameters and wire gauges the inputs give, the thermoblock's terminal side and the pump's terminal side. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (the two-zone rule, drainage, the thermal map and the hot parts' distances, serviceability, safety and electrical separation, materials and printers, the panels that attach to the bulkhead) goes in section 3 as an X-## row with its quote. Everything the inputs do not give — the wall's height and thickness, which wires cross and where, the tube runs, how the panels and the electronics bay attach to it, the K1C and Kobra Max 3 build volumes, whether the wall prints in one piece, the drainage lip's shape, sealing — goes in section 4 as questions, never resolved.
