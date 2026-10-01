# WP-01 — intake brief (20261001-od-c15-feet)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C15 is a 3D-printed TPU foot of the Open Dedica espresso machine, four per machine, fixed under the printed base frame OD-C01 at its four feet holes. The foot carries the machine on the counter, damps vibration, and must not let the machine walk. The base frame is a delivered part of this project: its STEP, its spec and its review are inputs.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/CHASSIS_README.md
- 00_Spec/inputs/SOURCING_GUIDE_s3_10.md
- 00_Spec/inputs/SOURCING_GUIDE_s6.md
- 00_Spec/inputs/OD-C01_DESIGN_SPEC.md
- 00_Spec/inputs/OD-C01_RV01.md
- 00_Spec/inputs/OD-C01_base_frame.step

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully.

## Output

00_Spec/INTAKE_v01.md from the template <oguz-atolye>/atolye/templates/INTAKE.md (the template is at /home/claude/oguz-atolye/atolye/templates/INTAKE.md). Every value of OD-C01 that a foot could touch or depend on must appear as its own X-## row, with the OD-C01 frame stated in the "What" cell: plate size, thickness, top and bottom face levels, corner radius and corner positions, the feet holes (diameter, positions, tolerance, through), every other hole or feature of the plate near the feet or on its underside (insert holes, drain holes with positions and diameters), the plate's material and printer, the mass and centre of mass figures in the review, every OD-C01 assumption row that names the feet (A-12 and any other), and every review finding or open item that bears on the feet (flatness, warp at the corners).

Also every requirement in REQUEST.md, bom_rows.csv, CHASSIS_README.md and the two SOURCING_GUIDE extracts that bears on this part (material, quantity, OEM alternative parts, fasteners, anti-vibration, printers, definition of done) as X-## rows in section 3. Gaps that the spec will need and no input gives (the foot height, its diameter, how it is fixed and from which side, the screw length, the TPU grade, which printer prints TPU, what sits on the plate's top face above each foot hole, the machine's mass) go in section 4 as questions, never resolved.

## Environment

Workspace: /home/claude/oguz-env/jobs/20261001-od-c15-feet (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template. Do not call any mcp__hearthbot__ tool.
