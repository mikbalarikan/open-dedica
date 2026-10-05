# WP-01 — intake brief (20261002-od-c14-cord-grommet)

Role: intake · data class: PUBLIC (open-source project, CC BY 4.0; every input is public on GitHub) · attempt 1 of 1

## What the job is for

OD-C14 is the 3D-printed strain relief / grommet for the mains cord OD-E06 of the Open Dedica espresso machine, where the cord passes the delivered back panel OD-C11 through its Ø12 cord pass-through. Its neighbours are delivered parts: their STEPs and specs are inputs.

## Inputs (all under 00_Spec/inputs/, read-only)

REQUEST.md, bom_rows.csv, CHASSIS_README.md, SOURCING_GUIDE_s6.md, OD-C11_DESIGN_SPEC.md, and the STEP files OD-C11_back_panel.step, OD-C01_base_frame.step, OD-C08_electronics_bay_tray.step.

STEP files are listed and hashed only (intake rule 6); their geometry is measured later. Read every markdown and csv file fully.

## Output

00_Spec/INTAKE_v01.md from the template /home/claude/oguz-atolye/atolye/templates/INTAKE.md. Section 2: one X-## row per value, frame stated (the OD-C01 machine frame: X right, +Y up, +Z front, plate top y 0), for every value the grommet could touch or depend on: OD-C11's wall planes and thickness, the cord pass-through (diameter, position, axis), the neighbouring features near it (flanges, gussets with their sizes and tops, vents, ledge, pass-throughs), the plate below; the cord diameter the Usta measured; the cable tie and fastener rows in bom_rows.csv; OD-C11's assumption rows about the cord and grommet (A-03, E-11). Section 3: every requirement on the grommet from REQUEST.md, bom_rows.csv, CHASSIS_README.md, SOURCING_GUIDE_s6.md and OD-C11's spec (material, quantity, strain relief, the electric zone). Section 4: gaps as questions, never resolved (how the grommet is retained in a closed Ø12 hole, how it grips the cord, what qty 2 means, PLA instead of TPU, how it goes on a cord that already has its plug).

## Environment

Workspace: /root/oguz-jobs/20261002-od-c14-cord-grommet (paths relative to it). Hash with sha256sum. Do not read anything outside the workspace and the template. Do not call any mcp__hearthbot__ tool.
