# WP-01 — intake brief (20261001-od-c08-electronics-bay-tray)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C08 is the 3D-printed electronics bay tray of the Open Dedica espresso machine: the part that holds the original OEM power PCB OD-E01 (electronics path 1, chosen by the Usta on 2026-10-01) in the electric zone of the base frame OD-C01 (x 70 … 120, z −240 … −30), behind the wet/electric bulkhead OD-C02 (wall x 63 … 67, rails to x 71). OD-C01 and OD-C02 are delivered; the side panel OD-C13, the top panel OD-C10, the back panel OD-C11, the wiring looms and the front control board's place (OD-E02, behind the front panel OD-C09) are not designed: everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-C01_base_frame.step
- 00_Spec/inputs/OD-C02_bulkhead.step
- 00_Spec/inputs/OD-E01_power_pcb.step
- 00_Spec/inputs/OD-E02_control_board.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C02_bulkhead/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-E01_power_pcb/DELIVER_README.md
- 00_Spec/inputs/reports/OD-E01_power_pcb/PARAM_TABLE.md
- 00_Spec/inputs/reports/OD-E02_control_board/DELIVER_README.md
- 00_Spec/inputs/reports/OD-E02_control_board/PARAM_TABLE.md

The four STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully (the PARAM_TABLE files are long: read them whole, extract the rows below). The OD-C01 spec gives the machine frame (§2), the layout with the electronics zone and the bulkhead line (§4 C1, A-04, A-08), the plate's outline, thickness and every hole already in it (§4, REQ-01 … REQ-10), and the insert and screw standard (A-11); the OD-C02 spec gives the bulkhead's faces, rails and wire windows (§4 C1, REQ-02 … REQ-08, A-04, A-07). The OD-E01 README and PARAM_TABLE give the power PCB's frame (datum: origin on mounting hole H1 at the board's top face, +Z out of the component side), board outline and thickness, every hole and slot, the tallest components (heatsink, capacitors, connectors and faston tabs) and the limitations of the scan (no calipers, invented solder side); the OD-E02 pair the same for the control board. REQUEST.md gives the Usta's words and the zone; PROJECT_RULES.md the electronics paths, the chassis design rules (two zones, thermal map, serviceability, safety) and the order of work; bom_rows.csv the rows that touch this part.

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension OD-C08 must meet or clear must appear as its own X-## row: the electronics zone's x and z extent, the plate's top face, thickness, outline near the zone (its x +120 edge, the corner radius) and every existing plate hole within 20 mm of the zone; the bulkhead's electric face x, its rail extents toward +X, its height and its wire windows (centre, diameter); the OD-E01 board outline (x/y min and max), thickness, every hole and slot with centre and radius, the heatsink's position and height, the tallest component height and where it is, the faston/terminal and connector positions as far as the table gives them, and its scan uncertainties; the OD-E02 envelope and its two screw holes. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (two zones, mains safety and separation, thermal map and materials, serviceability, insert and screw standard, printers) goes in section 3 as an X-## row with its quote. Everything the inputs do not give — how the board is fastened (screws, clips, which holes), board orientation, the wire routes and connector access, the mains entry, creepage and clearance distances, how the tray fastens to OD-C01/OD-C02, whether OD-E02 belongs to this tray, the K1C build volume — goes in section 4 as questions, never resolved.
