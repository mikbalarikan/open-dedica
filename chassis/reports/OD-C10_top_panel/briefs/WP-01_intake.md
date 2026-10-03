# WP-01 — intake brief (20261001-od-c10-top-panel)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C10 is the 3D-printed removable top panel of the Open Dedica espresso machine (BOM: removable with 4 screws): the lid over the whole machine, which comes off to reach the group head housing's screws and the carrier's foot screws (OD-C05), the OPV on the valve mount (OD-C07) and the hot water tube's connection above the carrier. It sits over the base frame OD-C01 (plate x ±120, z −305 … +100) and screws into the two M3 inserts the bulkhead OD-C02 provides in its top rail. OD-C01, OD-C02, OD-C05 and OD-C07 are delivered; the side panels OD-C12/C13, the back panel OD-C11, the front panel OD-C09, the water tank (on the table for now) and the tube runs are not designed: everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-C01_base_frame.step
- 00_Spec/inputs/OD-C02_bulkhead.step
- 00_Spec/inputs/OD-C05_group_head_carrier.step
- 00_Spec/inputs/OD-C07_valve_flowmeter_mount.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C02_bulkhead/DESIGN_SPEC_v1.2.md
- 00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v2.2.md
- 00_Spec/inputs/reports/OD-C07_valve_flowmeter_mount/DESIGN_SPEC_v1.2.md

The four STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully. The OD-C01 spec gives the machine frame (§2), the plate outline and corner radius, the layout and every part's pose and height (§4 C1, A-01 … A-17, the machine height A-16); the OD-C02 spec gives the bulkhead's top rail (its extent and top face y), the two top-panel insert bores and their positions (REQ-07, A-05, A-06); the OD-C05 spec gives the carrier's plate (its outline, top face, the four counterbored housing-screw holes, the hub window, the hatch), the water connection and the hot water tube above it (A-06, A-07), serviceability from above (A-14), and its pose in the machine frame (OD-C01 §4 A-01: x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0)); the OD-C07 spec gives the OPV access from above (A-10), the mount's height and its pose (OD-C01 §4 A-17). REQUEST.md gives the Usta's words; PROJECT_RULES.md the chassis design rules (serviceability, thermal map, materials) and the order of work; bom_rows.csv the rows that touch this part.

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension OD-C10 must meet or clear must appear as its own X-## row: the plate outline (x, z extents, corner radius), the highest point of every delivered part in the machine frame as the specs state it (bulkhead top rail y and extent, carrier plate top y and outline, the hub window and hatch centres and sizes, the housing screws' positions, the valve mount's top and the OPV's height), the two bulkhead insert bores (position, diameter, depth), the zones of the parts not designed (tank, drip tray, electronics bay) and the machine height. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (removable with 4 screws, serviceability, OPV reachable, thermal map and materials, printers, insert and screw standard) goes in section 3 as an X-## row with its quote. Everything the inputs do not give — the height the tube loop and the water connection rise above the carrier plate, what supports the panel's edges away from the bulkhead, how it meets the side, front and back panels, the tank's access, the material near heat, the Kobra Max 3 and K1C build volumes, whether the panel prints in one piece — goes in section 4 as questions, never resolved.
