# WP-01 — intake brief (20261001-od-c11-back-panel)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C11 is the 3D-printed removable back panel of the Open Dedica espresso machine (BOM: removable with 4 screws): the rear wall of the machine at the base frame OD-C01's rear edge (plate x ±120, rear edge z −305), behind the pump cradle OD-C03 with the pump OD-H01 and behind the rear ends of the bulkhead OD-C02 and the electronics bay. The mains cord leaves through it, and for now the water tank stands on the table outside the machine, so its two tubes (to the flowmeter, and the bypass return) enter through it; the tank seat OD-W03 is the scanned reference for those tubes. OD-C01, OD-C02 and OD-C03 are delivered; the side panels OD-C12/C13, the top panel OD-C10, the tank dock OD-C06, the electronics bay OD-C08, the grommet OD-C14 and the feet OD-C15 are not designed: everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-C01_base_frame.step
- 00_Spec/inputs/OD-C02_bulkhead.step
- 00_Spec/inputs/OD-C03_pump_cradle.step
- 00_Spec/inputs/OD-H01_ulka_ep5_pump.step
- 00_Spec/inputs/OD-W03_tank_seat.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C02_bulkhead/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C03_pump_cradle/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-W03_tank_seat/DELIVER_README.md

The five STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully. The OD-C01 spec gives the machine frame (§2), the plate outline, thickness and corner radius, every hole near the rear edge (the feet holes, the pump cradle's inserts, the drain holes), the tank zone and the electronics zone (§4 C1, A-07, A-08, A-12, A-16); the OD-C02 spec gives the bulkhead's rear end and height; the OD-C03 spec gives the pump cradle and the pump's pose (OD-C01 §4 A-03: local x → +Z, y → −Y, z → +X, origin (0, 40, −205)) and the pump's rear-most extent; the OD-W03 README gives the tank seat's ports (hose nipples) and size. REQUEST.md gives the Usta's words; PROJECT_RULES.md the chassis design rules (serviceability, two zones, safety), the water path and the order of work; bom_rows.csv the rows that touch this part (the cord, the IEC inlet alternative, the grommet, the tubes, the fasteners).

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension OD-C11 must meet or clear must appear as its own X-## row: the plate outline and rear edge, thickness and corner radius; every plate hole within 40 mm of the rear edge; the rear-most extent of every delivered part (the pump cradle's foot, the pump body, the bulkhead's rear end) as the specs state it; the tank zone and electronics zone; the machine height; the tank seat's hose nipple diameters and spacing and the tube sizes the BOM or the specs give. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (removable with 4 screws, serviceability, two zones, mains safety, materials, printers, insert and screw standard) goes in section 3 as an X-## row with its quote. Everything the inputs do not give — what the panel fastens to, the cord and tube pass-through sizes and positions, the grommet, ventilation, how it meets the side and top panels, the feet, the material, the Kobra Max 3 and K1C build volumes — goes in section 4 as questions, never resolved.
