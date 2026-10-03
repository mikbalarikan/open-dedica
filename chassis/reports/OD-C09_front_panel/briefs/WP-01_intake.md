# WP-01 — intake brief (20261002-od-c09-front-panel)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C09 is the 3D-printed front panel of the Open Dedica espresso machine, with a bezel for the OEM front button board OD-E02. It stands on the front edge of the printed base plate OD-C01, under the front skirt of the delivered top panel OD-C10, mirrors the delivered back panel OD-C11, and frames the brew area: the group head housing OD-G01 stands vertical with its mouth down on the carrier OD-C05, the portafilter OD-G10 locks into it from below and its handle reaches out through the front, and the drip tray zone lies on the plate under the mouth. The steam knob OD-S03 belongs to phase 2.

## Inputs (all under 00_Spec/inputs/, read-only)

REQUEST.md, bom_rows.csv, CHASSIS_README.md, SOURCING_GUIDE_s6.md, OD-C01_DESIGN_SPEC.md, OD-C05_DESIGN_SPEC.md, OD-C10_DESIGN_SPEC.md, OD-C11_DESIGN_SPEC.md, OD-C15_DESIGN_SPEC.md, OD-G01_DESIGN_SPEC.md, OD-E02_REPORT.md, OD-S03_REPORT.md; STEP files: OD-C01_base_frame.step, OD-C05_group_head_carrier.step, OD-C10_top_panel.step, OD-C11_back_panel.step, OD-E02_control_board.step, OD-S03_steam_knob.step, od_g01_assembly_C1_v03.step, od_g01_housing_C1_v03.step.

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully.

## Output

00_Spec/INTAKE_v01.md from the template /home/claude/oguz-atolye/atolye/templates/INTAKE.md. Extract as X-## rows, each with its frame named in the "What" cell:

- OD-C01: plate outline, thickness, face levels, corner radii and centres, every hole or insert near the front edge (z > 0 in the machine frame), the feet holes and the OD-C15 keep-out above them, the drip tray zone and every reserved zone touching the front, the machine frame definition.
- OD-C10: the lid's outline, skirt (thickness, levels, front skirt position), columns, rest pads, and everything it says about the front panel (where the panels end, what rests on what).
- OD-C11: its wall, flanges, holes, gussets, ledge, print orientation and material, every number a mirrored front panel would reuse, and its decisions on material and printer.
- OD-C05 and OD-G01: the housing's pose in the machine frame (the mapping and origin), the mouth's position and height, the housing's and the carrier's extents in the machine frame, the portafilter spout height and the mug rule, the bayonet lug angles and the stop blocks (G01 §4), the brew temperatures near the housing.
- OD-E02 (from its report): datum frame, bounding box, the three button caps (positions, radii, top offsets and tilts), the two screw holes (positions, radii, counterbore radii and which side), the mounting tab, the latch hoops, and the report's limitations (scan only, no calipers).
- OD-S03 (from its report): what it is, its size, how it mounts, what phase.
- OD-C15: the keep-out above each foot hole.
- Every requirement in REQUEST.md, bom_rows.csv, CHASSIS_README.md and SOURCING_GUIDE_s6.md that bears on this part (material, printer, removability, the thermal rule, serviceability, the mug rule, what is out of scope) as rows in section 3.

Gaps the spec will need and no input gives go in section 4 as questions, never resolved: the drip tray's real size (not scanned), the side panels' wall position (OD-C12/C13 are printed, not yet designed), how the panel is fixed to the plate, where the button board sits and how it is held, the portafilter's handle sweep through the front, the steam knob's place, PLA near the group head's heat.

## Environment

Workspace: /root/oguz-jobs/20261002-od-c09-front-panel (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template. Do not call any mcp__hearthbot__ tool.
