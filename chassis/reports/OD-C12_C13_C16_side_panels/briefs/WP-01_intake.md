# WP-01 — intake brief (20261002-od-c12-c13-c16-side-panels)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C12 (left) and OD-C13 (right) are the 3D-printed side panels of the Open Dedica espresso machine, standing on the printed base frame OD-C01 along its two side edges, under the top panel OD-C10's skirt, beside the back panel OD-C11; OD-C16 are the printed corner brackets that fasten them. All neighbours are delivered parts of this project: their STEPs and specs are inputs.

## Inputs (all under 00_Spec/inputs/, read-only)

REQUEST.md, bom_rows.csv, CHASSIS_README.md, SOURCING_GUIDE_s6.md, C08_C11_integration_notes.md, C15_integration_notes.md, OD-C01_DESIGN_SPEC.md, OD-C07_DESIGN_SPEC.md, OD-C08_DESIGN_SPEC.md, OD-C10_DESIGN_SPEC.md, OD-C11_DESIGN_SPEC.md, OD-C15_DESIGN_SPEC.md, and the STEP files OD-C01_base_frame.step, OD-C02_bulkhead.step, OD-C05_group_head_carrier.step, OD-C07_valve_flowmeter_mount.step, OD-C08_electronics_bay_tray.step, OD-C10_top_panel.step, OD-C11_back_panel.step, OD-C15_foot.step.

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully.

## Output

00_Spec/INTAKE_v01.md from the template /home/claude/oguz-atolye/atolye/templates/INTAKE.md. In section 2, one X-## row per value, with the frame stated in the "What" cell (all these parts use the OD-C01 machine frame: X right, +Y up, +Z front, plate top y 0, or say which joint maps them into it), for every value a side panel or a bracket near the plate's side edges could touch or depend on:

- OD-C01: plate outline, thickness, top/bottom levels, corner radii and centres, every hole and insert position with |x| ≥ 60 (feet holes, the C07/C08/C11 inserts, drains), the insert type and bore, material, printer, build volume figure.
- OD-C10: outline, skirt thickness and its bottom level, skin levels, columns, ribs (positions and reach), rest pads, the F1 finding (centre of mass, rest pad), what the lid expects of the side panels (A-04).
- OD-C11: wall planes, x extent, height, flanges, gussets, ledge, pass-throughs, vents, the feet-hole margin.
- OD-C07: its joint into the machine frame, envelope, the zone it occupies (OD-C01 A-05: x −117 … −67).
- OD-C08: its envelope in the machine frame and its flange inserts.
- OD-C15: the feet positions, the screw-head keep-out (A-09), the foot joint.
- OD-C02 and OD-C05: their envelopes and joints as the specs give them.
- Fasteners (inserts, screws) and their sizes from bom_rows.csv and the specs.

Section 3: every requirement in REQUEST.md, bom_rows.csv, CHASSIS_README.md, SOURCING_GUIDE_s6.md and the two integration-notes files that bears on side panels or corner brackets (material, quantity, acrylic vs printed, printers, serviceability, thermal rules, definition of done, keep-outs).

Section 4: gaps the spec will need and no input gives, as questions, never resolved (for example: how a panel is fixed, panel thickness, the front panel OD-C09's plane, the corners where side meets back and front, material limits of PLA near heat, which printer prints a ~400 mm panel, what the bracket count is with printed panels).

## Environment

Workspace: /root/oguz-jobs/20261002-od-c12-c13-c16-side-panels (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template. Do not call any mcp__hearthbot__ tool.
