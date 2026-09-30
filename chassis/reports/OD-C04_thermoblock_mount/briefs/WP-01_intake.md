# WP-01 — intake brief (20260930-od-c04-thermoblock-mount)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C04 is the 3D-printed thermoblock mount of the Open Dedica espresso machine: it holds the OEM cast-aluminium 1300 W thermoblock (OD-H11) inside the printed chassis with at least 10 mm of air between the thermoblock's skin and any printed wall, using the thermoblock's own mounting features, and bolts to the printed base frame (OD-C01, not designed yet). OD-H11 is the scan-rebuilt thermoblock: the reference geometry. The NTC fixing bracket OD-H17 and the TCO fixing bracket OD-H19, which clip onto the thermoblock, are not scanned; everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-H11_thermoblock.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-H11_thermoblock/README.md
- 00_Spec/inputs/reports/OD-H11_thermoblock/params.json
- 00_Spec/inputs/reports/OD-H11_thermoblock/export_check.json
- 00_Spec/inputs/reports/OD-H11_thermoblock/deviation_report.json
- 00_Spec/inputs/scan/OD-H11_thermoblock/README.md
- 00_Spec/inputs/scan/OD-H11_thermoblock/calipers.md

The STEP file is listed and hashed only (intake rule 6); its geometry is measured later. Read every markdown, csv and json file fully. params.json holds the rebuilt parameters of the thermoblock (one key per value, in the STEP's datum frame: base face at z = 0, body axis = +Z, top face at z = 47.64; angles θ about +Z); README.md holds the feature tree, the frame definition, the deviation results and the run's own assumptions; export_check.json the re-import facts (solid count, faces, volume, bbox); deviation_report.json the deviation numbers; the scan README and calipers.md the scanner facts and the empty caliper sheet; REQUEST.md the Usta's request and the standing instruction; PROJECT_RULES.md the chassis rules, the sourcing guide's thermoblock section (the ≥ 10 mm air gap, the OEM bracket geometry, the materials) and the safety note; bom_rows.csv the bill-of-materials rows that touch this part.

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension of OD-H11 that a mount could touch or must clear must appear as its own X-## row: the body cones (radii, sectors, chamfers), the two rib pads (angles, profile radii and z levels, the ear blocks and their chamfers), the ear notches and clip holes (widths, positions), the side block and its tabs, slots and pockets, every lug (extents, the Ø3.5 and Ø3.6 blind holes with their positions and depths), the three vertical grooves (radius, pitch radius, angles, z ranges), the three top pins (PCD, angles, diameters, top z), the central bore and counterbore, the water pipes (diameter, collar, clip flats, positions and directions), the heater terminals (positions, directions, diameters, spade tabs), the top and bottom pockets and dimples, the overall envelope and volume from export_check.json, and the deviation numbers. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (material, process, the ≥ 10 mm air gap, "mount it on its OEM bracket geometry", the TCO that must never be omitted, the wet/electric separation, the chassis order-of-work and blockers, fasteners) goes in section 3 as an X-## row with its quote. Everything the inputs do not give about OD-H17 and OD-H19 (their shape, where they clip, what they occupy), about which thermoblock features the OEM chassis screws into, about the thermoblock's orientation in the machine, and about OD-C01's mounting interface goes in section 4 as questions, never resolved. Conflicts between params.json and README.md go in section 4 too.

## Environment

Workspace: ${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template.
