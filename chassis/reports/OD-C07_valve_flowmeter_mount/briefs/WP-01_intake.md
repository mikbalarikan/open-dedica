# WP-01 — intake brief (20260930-od-c07-valve-flowmeter-mount)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C07 is the 3D-printed mount (PETG) that carries three OEM hydraulic parts of the Open Dedica espresso machine inside the printed chassis: the anti-drip valve OD-H21, the 3-way valve OD-H22 (the over-pressure valve, "OPV", whose spring must stay reachable without disassembly), and the flowmeter OD-H24. The mount fixes each part by the mounting features the OEM chassis used (screw ears, a plug-in spigot with latch lugs, a flange with slots) and itself mounts to the base frame OD-C01 with M3 heat-set inserts. The three STEP files are scan rebuilds; their reports hold every rebuilt parameter.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/CHASSIS_README.md
- 00_Spec/inputs/WATER_FLOW.md
- 00_Spec/inputs/SOURCING_GUIDE.md
- 00_Spec/inputs/OD-H21_antidrip_valve.step
- 00_Spec/inputs/OD-H22_3way_valve.step
- 00_Spec/inputs/OD-H24_flowmeter.step
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/README.md
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/DELIVER_README.md
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/PARAM_TABLE.md
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/INTAKE_CARD.md
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/DECISIONS.md
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/limitations.json
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/alignment.json
- 00_Spec/inputs/reports/OD-H21_antidrip_valve/overlay_z.png
- 00_Spec/inputs/reports/OD-H22_3way_valve/README.md
- 00_Spec/inputs/reports/OD-H22_3way_valve/DELIVER_README.md
- 00_Spec/inputs/reports/OD-H22_3way_valve/PARAM_TABLE.md
- 00_Spec/inputs/reports/OD-H22_3way_valve/params.json
- 00_Spec/inputs/reports/OD-H22_3way_valve/MODELING_PLAN.md
- 00_Spec/inputs/reports/OD-H22_3way_valve/INTAKE_CARD.md
- 00_Spec/inputs/reports/OD-H22_3way_valve/DECISIONS.md
- 00_Spec/inputs/reports/OD-H22_3way_valve/limitations.json
- 00_Spec/inputs/reports/OD-H22_3way_valve/alignment.json
- 00_Spec/inputs/reports/OD-H22_3way_valve/overlay.png
- 00_Spec/inputs/reports/OD-H22_3way_valve/photo_4.png
- 00_Spec/inputs/reports/OD-H24_flowmeter/README.md
- 00_Spec/inputs/reports/OD-H24_flowmeter/params.json
- 00_Spec/inputs/reports/OD-H24_flowmeter/tubes.json
- 00_Spec/inputs/reports/OD-H24_flowmeter/export_check.json
- 00_Spec/inputs/reports/OD-H24_flowmeter/views_cad.png
- 00_Spec/inputs/reports/OD-H24_flowmeter/views_scan.png

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown, csv, and json file fully and view every png. The PARAM_TABLE.md, DELIVER_README.md §5 and params.json files hold the rebuilt parameters of each reference part (one row per value, with the run's rule, ± and critical tag: keep those in the Flags column); README.md and DECISIONS.md hold the deviation results and the run's own limitations; limitations.json the machine-readable limitations; INTAKE_CARD.md the feature enumeration, the functional interfaces (its §4 table) and the datum frame; alignment.json the frame; REQUEST.md the Usta's request and the project rules; bom_rows.csv the bill-of-materials rows; WATER_FLOW.md the tube connections of the three parts; SOURCING_GUIDE.md §3.5, §3.6 and §6 the valve, flowmeter and chassis rules; CHASSIS_README.md the order of work and the definition of done.

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension of the three reference parts that a mount could touch must appear as its own X-## row, with the part's own datum frame stated in the "What" cell:

- OD-H22: flange plate (disc radius, ear shape, ear hole positions and radius, plate thickness = flange floor z, rim top z, rim wall), back face and its normal, the stem and gussets below the flange (radii, z levels), the port axes (elevation, axis points, end t), port lip / sleeve / clip block sizes, the drive tube and collar above the flange (radii, top z), the tilt finding.
- OD-H21: nozzle (spigot) radius, tip and shoulder levels, the corner lugs (half sizes, corner radius, angle, z range), the latch windows (z range, angles, cut depths), the nut (radius, ribs, shoulder and top levels), the bands and body radius, the cap ring and cap (radii, levels), the side outlet (axis, tube, collar, thread, O-ring, end level), the barb (axis, radii, end level), the datum definition and the tilt findings.
- OD-H24: the body revolve levels and radii (rim, cup with its draft, skirt, flange underside and top, hub), the four arc windows and four tangential outer slots (radii, angles, floors, sizes), the connector (position, angle, size, pin pitch, top level), the two pipes (axes, profiles, tip positions, bores), the pins under the base, the datum definition, the warp finding.
- Every deviation gate result and limitation of the three runs that bears on using the STEP as a mating reference (scale unverified, scan-only, band misses, unscanned regions, tilt, warp).

Also every requirement in REQUEST.md, bom_rows.csv, CHASSIS_README.md, WATER_FLOW.md and SOURCING_GUIDE.md that bears on this part (material, process, fasteners, OPV access, two-zone rule, drainage, anti-vibration, thermal map, tube connections, printers, definition of done) as X-## rows in section 3. Gaps that the spec will need and no input gives (how each part was fixed in the OEM chassis, the orientation of each part in the machine, the tube routes, the position of OD-C01's floor, the flowmeter slot function) go in section 4 as questions, never resolved.

## Environment

Workspace: ${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template.
