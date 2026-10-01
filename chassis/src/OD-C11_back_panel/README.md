# OD-C11 back panel — build scripts

Job `20261001-od-c11-back-panel` (record: `chassis/reports/OD-C11_back_panel/`),
build v03 to DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C11_back_panel/reviews/RV01_od_c11_back_v03.md`). Builds v01 and v02
stopped on spec faults (recorded in the job; the Usta ordered the third build).
The panel is a 3 mm wall at z −302 … −299 over x ±116, 215 tall, on the plate's
rear edge, with two floor flanges screwed from above into four new M3 inserts in
OD-C01 at (±81, −282), (±95, −282), four gussets, a top ledge with two Ø4.0 × 6
insert bores at (±90, −293) for the top panel OD-C10's rear screws, three Ø12
pass-throughs (mains cord at (95, 30), tank and bypass tubes at (−100, 30),
(−84, 30); the water tank stands on the table) and five vent slots behind the
electronics bay. It prints lying on its outer face on the Kobra Max 3, PETG.

Review notes: the wall's foot stands 2.3 from the rims of OD-C01's feet holes at
(±110, −295) (spec 1.2 allows ≥ 2.0), so the OD-C15 feet's screw heads (Ø5.7)
clear the wall by 1.15; the panel's stiffness is a bench check at first print
(RV01 F1).

| File | What it is |
|---|---|
| `build_od_c11_back_v03.py` | parametric build123d model of the panel and the check assembly (OD-C01, OD-C02, OD-C03 + OD-H01 as placed); writes STEP (AP242) and STL |
| `check_od_c11_back_v03.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261001-od-c11-back-panel`.

Delivered files: `OD-C11_back_panel.step`, `.stl` and `.3mf` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_c11_back_C1_v03.*` (SHA-256
in `../../reports/OD-C11_back_panel/briefs/WP-05_reviewer.md`).
