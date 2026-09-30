# OD-C03 pump cradle — build scripts

Job `20260930-od-c03-pump-cradle` (record: `chassis/reports/OD-C03_pump_cradle/`),
build v02 to DESIGN_SPEC 1.2, after one REVISE round (RV01 blocked on the
vibration bench gate alone; v02 moved the front saddle rib under the pump's centre
of mass). Reviewed once per build: RV02 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C03_pump_cradle/reviews/RV02_od_c03_cradle_v02.md`). Every interface
value rests on the assumptions A-01 … A-15 of the spec's §6 until the Usta confirms
it with calipers; the rubber sleeve OD-H02 (saddle radius 26.65) and the spring
OD-H03 are unscanned, and the post clearance to the frame side plate is 2.30 mm
against a scan with 0.45 mm p95 error (RV02 F3, F4).

| File | What it is |
|---|---|
| `build_od_c03_cradle_v02.py` | parametric build123d model of the cradle, the assumed sleeve solid and the check assembly with OD-H01; writes STEP (AP242) and STL |
| `check_od_c03_cradle_v02.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-c03-pump-cradle`.

`OD-C03_pump_cradle.step` and `.stl` in `chassis/` are byte-identical copies of the
reviewed `02_STEP_STL/od_c03_cradle_C1_v02.step` and `.stl` (hashes in
`reports/OD-C03_pump_cradle/briefs/WP-06_reviewer.md`).
