# WP-01 — intake brief (20261002-od-t01-pressure-test-rig)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-T01 is the bench pressure-test rig of the Open Dedica project: a printed stand plus bought fittings that holds the printed group head housing OD-G01 (with the OEM gasket support OD-G04 and the OEM portafilter OD-G10 locked in it) the way the machine's carrier OD-C05 holds it, so that the housing can be pressurised with water on the bench to the brew pressure before it goes into the machine. OD-G01's review left its brew-load row (REQ-12) to this bench test, and the Usta accepted OD-G01 with that deviation documented.

## Inputs (all under 00_Spec/inputs/, read-only)

REQUEST.md, bom_rows.csv, CHASSIS_README.md, SOURCING_GUIDE_extract.md, OD-G01_DESIGN_SPEC.md, OD-G01_RV01.md, OD-G01_REVISE_PACKET_RV01.md, OD-C05_DESIGN_SPEC.md; STEP files: od_g01_housing_C1_v03.step, od_g01_assembly_C1_v03.step, OD-C05_group_head_carrier.step, OD-G04_brewing_gasket_support.step, OD-G10_portafilter.step.

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully.

## Output

00_Spec/INTAKE_v01.md from the template /home/claude/oguz-atolye/atolye/templates/INTAKE.md. Extract as X-## rows, each with its frame named in the "What" cell:

- OD-G01: its frame, envelope, rear face and front face levels, the four insert bores (positions, diameter, depth), the Ø26 hub opening and the pair-B screw recesses, the bayonet lugs and stop blocks, the brew load and its derivation (REQ-12, A-21), material and print, and every RV01 finding and REVISE-packet line on the bench test (what it must show, at what pressure, how the result is recorded).
- OD-C05: how it holds OD-G01 (plate thickness, counterbores, screw, insert engagement, hub window, the reasons), the housing-to-machine mapping, anything on the water connection above the hub (A-06, A-07).
- OD-G04 and OD-G10: what the specs and reports say about their placement and extents (the locked pose is in od_g01_assembly_C1_v03.step).
- Pressure and safety figures: the pump's maximum pressure, the safety spec (piping rating, temperature), the M1 definition, the pressure-test step in the build order.
- Every requirement in REQUEST.md, bom_rows.csv (OD-T01 "printed + fittings"; the group head parts and fasteners) and CHASSIS_README.md that bears on this rig, in section 3.

Gaps the spec will need and no input gives go in section 4 as questions, never resolved: the test pressure and hold time, the pressure source (hand test pump or the Ulka pump), the gauge and fittings, how water reaches the hub, the blind basket, how the rig is held on the bench, the height under the portafilter, the rig's own strength, the PLA material (the Usta: "all printed in pla for now") and the printer.

## Environment

Workspace: /root/oguz-jobs/20261002-od-t01-pressure-test-rig (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template. Do not call any mcp__hearthbot__ tool.
