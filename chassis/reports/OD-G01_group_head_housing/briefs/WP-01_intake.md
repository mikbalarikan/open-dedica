# WP-01 — intake brief (20260930-od-g01-group-head-housing)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-G01 is the 3D-printed group-head housing of the Open Dedica espresso machine: the open replacement for the housing molded into the De'Longhi Dedica EC685 case. It must lock the OEM 51 mm portafilter (OD-G10) with its three bayonet ears, seat the OEM brewing gasket support (OD-G04) with its two fixing screws, pass the support's hub through its plate to the thermoblock connection, and mount to the printed chassis. OD-G09 is the scan-rebuilt OEM cup: the reference geometry for OD-G01.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-G04_brewing_gasket_support.step
- 00_Spec/inputs/OD-G09_group_head_bayonet_cup.step
- 00_Spec/inputs/OD-G10_portafilter.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/bom_group_head_rows.csv
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/DECISIONS.md
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/PARAM_TABLE.md
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/README.md
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/SCAN_README.md
- 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/limitations.json
- 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/DECISIONS.md
- 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/PARAM_TABLE.md
- 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/README.md
- 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/SCAN_README.md
- 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/limitations.json
- 00_Spec/inputs/reports/OD-G10_portafilter/DECISIONS.md
- 00_Spec/inputs/reports/OD-G10_portafilter/PARAM_TABLE.md
- 00_Spec/inputs/reports/OD-G10_portafilter/README.md
- 00_Spec/inputs/reports/OD-G10_portafilter/SCAN_README.md
- 00_Spec/inputs/reports/OD-G10_portafilter/limitations.json

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown, csv and json file fully: the PARAM_TABLE.md files hold the rebuilt parameters of each reference part (one row per value, with the run's confidence tag: keep that tag in the Flags column), the README.md and DECISIONS.md files hold the deviation results and the run's own limitations, limitations.json the machine-readable limitations, SCAN_README.md the scanner and mesh facts, REQUEST.md the Usta's request and the project's rules, bom_group_head_rows.csv the bill-of-materials rows of the group head.

## Output

00_Spec/INTAKE_v01.md from the template /home/user/oguz-atolye/atolye/templates/INTAKE.md. Every dimension of the three reference parts that touches OD-G01 must appear as its own X-## row: cup bore diameters and heights, lug count, angular positions, radial depth, ramp, lip ring, floor and plate levels, plate thickness, water opening shape, screw boss positions and hole diameters (OD-G09); flange, plate, tabs, bosses, hub tube (OD-G04); ear count, ear swept diameter, ear height, cup rim diameter (OD-G10). Also every requirement in REQUEST.md and the csv (material, process, safety, chassis rules) as X-## rows in section 3. Conflicts between the three reports (for example a boss PCD that differs between OD-G09 and OD-G04) go in section 4 as questions, never resolved.

## Environment

Workspace: /home/user/oguz-jobs/20260930-od-g01-group-head-housing (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template.
