# OD-T01 group head bench pressure-test rig — build scripts

Job `20261002-od-t01-pressure-test-rig` (record: `chassis/reports/OD-T01_pressure_test_rig/`),
build v01 to DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-T01_pressure_test_rig/reviews/RV01_od_t01_rig_v01.md`). Finding F1
(MEDIUM, REQ-08 soft): the hub window leaves 47.5 of the plate's 120 width
between the screw lines, so spec §4's strength factor 3.8 is about 1.5 at
15 bar; a 25 mm plate is proposed as v02. Test procedure:
`../../OD-T01_TEST_PROCEDURE.md`.

The rig is a closed frame: a 15 mm plate (y 135–150) the housing's rear face
seats under, held by four M3 × 8 from above into its inserts at (±44, ±44) as on
OD-C05; a R 30 hub window with a 45.1° teardrop roof; two walls (x ±75…90, cut
back to z +40 so the portafilter handle swings free); a base with four Ø4.5
bench holes at (±105, ±40). Envelope 240 × 150 × 120.

| File | What it is |
|---|---|
| `build_od_t01_rig.py` | parametric build123d model; writes STEP (AP242), STL and the check assembly |
| `check_od_t01_rig.py` | the designer's gate checks (spec §5) on the re-imported STEP and assembly |
| `sweep_od_t01_rig.py` | REQ-04's portafilter rotation and insertion sweeps |
| `sections_od_t01_rig.py` | the section cuts the review reads |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261002-od-t01-pressure-test-rig`
(inputs in its `00_Spec/inputs/`).

Delivered files: `OD-T01_pressure_test_rig.step` and `.stl` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_t01_rig_C1_v01.step` /
`.stl` (SHA-256 cc6b1c72…9f5c / 1b2985d1…d3a5); the `.3mf` is written from that
STL (5752 triangles, volume 959 184 mm³ unchanged).

Print: PLA on the Kobra Max 3 (A-08, A-09), lying on its rear face (z −60) on the
bed, build direction +Z, no supports (A-10); a brim if the long profile lifts.
Open assumptions A-01 … A-12 are in the spec's §6.
