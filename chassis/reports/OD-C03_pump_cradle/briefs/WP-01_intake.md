# WP-01 — intake brief (20260930-od-c03-pump-cradle)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C03 is the 3D-printed pump cradle of the Open Dedica espresso machine: it holds the OEM ULKA EP5 vibratory pump (OD-H01) inside the printed chassis, through the OEM rubber pump protector sleeve (OD-H02) and suspension spring (OD-H03) that damp its vibration, and bolts to the printed base frame (OD-C01, not designed yet). OD-H01 is the scan-rebuilt pump: the reference geometry. OD-H02 and OD-H03 are not scanned; everything about them is a gap for section 4.

## Inputs (all under 00_Spec/inputs/, read-only)

- 00_Spec/inputs/OD-H01_ulka_ep5_pump.step
- 00_Spec/inputs/REQUEST.md
- 00_Spec/inputs/PROJECT_RULES.md
- 00_Spec/inputs/bom_rows.csv
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/params.json
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/expected.json
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/export_check.json
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/validator_report.json
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/deviation_gate.json
- 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/alignment_T1.json
- 00_Spec/inputs/scan/OD-H01_ulka_ep5_pump/README.md
- 00_Spec/inputs/scan/OD-H01_ulka_ep5_pump/calipers.md

The STEP file is listed and hashed only (intake rule 6); its geometry is measured later. Read every markdown, csv and json file fully. params.json holds the rebuilt parameters of the pump (one key per value, in the STEP's datum frame: pump axis = +Z, outlet toward −Z, inlet fitting toward +Z, X = normal of the sheet-metal frame side plate, origin on the axis); README.md holds the model tree, the frame definition, the deviation results and the run's own assumptions; expected.json and validator_report.json the validator's expectations and results; export_check.json the re-import facts (solid count, faces, volume, bbox); deviation_gate.json the deviation numbers; alignment_T1.json the scan-to-datum transform; the scan README and calipers.md the scanner facts and the empty caliper sheet; REQUEST.md the Usta's request and the standing instruction; PROJECT_RULES.md the chassis rules, the sourcing guide's pump section (the OEM mounting concept: rubber sleeve + spring) and the safety note; bom_rows.csv the bill-of-materials rows that touch this part.

## Output

00_Spec/INTAKE_v01.md from the template <repo>/atolye/templates/INTAKE.md. Every dimension of OD-H01 that a cradle could touch or must clear must appear as its own X-## row: the coil (radius, centre offset, z range, fillet), the revolved body radii and their z levels (nozzle, taper steps, step, cone, body, rear washer, boss, ring, barbs, inlet tip), the wrench flats, the outlet bore, the sheet-metal U-frame (x, y, z extents, sheet thickness, outer bend radius, notches, slots), the diamond flange and its screws, the terminal block (extents, tabs, rib, slot box and its angle), the overall envelope and volume from export_check.json, and the deviation numbers. Every requirement in REQUEST.md, PROJECT_RULES.md and the csv (material, process, the sleeve-and-spring mounting concept, the wet/electric separation, the ≥ 10 mm rule where it applies, the chassis order-of-work and blockers, fasteners) goes in section 3 as an X-## row with its quote. Everything the inputs do not give about OD-H02 and OD-H03 (their dimensions, how the sleeve wraps the pump, where the spring sits, which end is fixed) and about OD-C01's mounting interface goes in section 4 as questions, never resolved. Conflicts between params.json, README.md and expected.json go in section 4 too.

## Environment

Workspace: ${OGUZ_JOBS}/20260930-od-c03-pump-cradle (paths in the intake file relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template.
