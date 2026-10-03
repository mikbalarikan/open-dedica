# OD-C10 top panel — build scripts

Job `20261001-od-c10-top-panel` (record: `chassis/reports/OD-C10_top_panel/`),
build v01, checked against DESIGN_SPEC 1.2 (REPORT v01b), reviewed once: RV01
`APPROVED_ASSUMPTION_CONDITIONAL` (`reports/OD-C10_top_panel/reviews/RV01_od_c10_top_v01.md`).
The lid is a 3 mm skin at y 247 … 250 over the OD-C01 plate outline (x ±120,
z −305 … +100, R 10 corners) with a 3 mm skirt down to y 215, four Ø12 screw
columns with Ø3.4 holes and Ø6.5 counterbores (M3 × 8 from above into inserts:
two in OD-C02's top rail at (65, −60), (65, −210), two in OD-C11's ledge at
(±90, −293)), ribs, and two Ø10 rest pads 0.5 above the carrier OD-C05 at
(±48, 30). The rear skirt rests on OD-C11's wall top along a line and two corner
patches (accepted by the Usta, spec 1.2). It prints upside down on the Kobra
Max 3 (240 × 405 on the bed, A-09), PETG (A-10).

Review notes: the lid's centre of mass lies 24 mm outside its four-column
polygon on −X and the front-left corner spans 245 mm free, so with the side
panels absent it settles onto the −X rest pad; stiffness is a bench check at
first print (RV01 F1). The seating is exact only at nominal (F2).

| File | What it is |
|---|---|
| `build_od_c10_top.py` | parametric build123d model of the lid and the check assembly (OD-C01, OD-C02, OD-C05, OD-C07, OD-C11 as placed); writes STEP (AP242) and STL |
| `check_od_c10_top_v01b.py` | the designer's gate checks (spec 1.2 §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261001-od-c10-top-panel`.

Delivered files: `OD-C10_top_panel.step`, `.stl` and `.3mf` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_c10_top_C1_v01.*` (SHA-256
in `../../reports/OD-C10_top_panel/briefs/WP-04_reviewer.md`).
