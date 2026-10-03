# OD-T01 group head bench pressure-test rig — build scripts

Job `20261002-od-t01-pressure-test-rig` (record: `chassis/reports/OD-T01_pressure_test_rig/`).
Build v01 (15 mm plate, spec 1.2) was reviewed RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
with F1: through the hub window the plate's strength factor was ≈ 1.5, not 3.8. The
Usta chose a 25 mm plate (2026-10-03); build v02 to spec 1.3, reviewed RV02
`APPROVED_ASSUMPTION_CONDITIONAL` (`reports/OD-T01_pressure_test_rig/reviews/RV02_od_t01_rig_v02.md`):
RV01 F1/F2 closed (window section σ 9.6 MPa, factor ≈ 4.2); RV02 F1 (MEDIUM, bench)
flags the screw-head bearing (≈ 47 MPa on PLA) and unspecified infill, answered in
`../../OD-T01_TEST_PROCEDURE.md` (100 % infill, optional washers, watch the heads).

The rig is a closed frame: a 25 mm plate (y 135–160) the housing's rear face
seats under, held by four M3 × 10 ISO 7380 from above into its inserts at (±44, ±44)
as on OD-C05, through Ø6.5 counterbores leaving 5.0 of plate under each head; a
R 30 hub window with a 45.1° teardrop roof; two walls (x ±75…90, cut back to
z +40 so the portafilter handle swings free); a base with four Ø4.5 bench holes at
(±105, ±40). Envelope 240 × 160 × 120.

| File | What it is |
|---|---|
| `build_od_t01_rig_v02.py` | parametric build123d model; writes STEP (AP242), STL and the check assembly |
| `check_od_t01_rig_v02.py` | the designer's gate checks (spec §5) on the re-imported STEP and assembly |
| `sweep_od_t01_rig_v02.py` | REQ-04's portafilter rotation and insertion sweeps |
| `sections_od_t01_rig_v02.py` | the section cuts the review reads |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261002-od-t01-pressure-test-rig`
(inputs in its `00_Spec/inputs/`).

Delivered files: `OD-T01_pressure_test_rig.step` and `.stl` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_t01_rig_C1_v02.step` /
`.stl` (SHA-256 18c9de8f…f810 / 183e58f0…bd3f); the `.3mf` is written from that
STL (5752 triangles, volume 1 143 760 mm³ unchanged). The v01 files stay in the record.

Print: PLA on the Kobra Max 3 (A-08, A-09), lying on its rear face (z −60) on the
bed, build direction +Z, no supports (A-10), 100 % infill (RV02 F1); a brim if the long profile lifts. About 1.4 kg of PLA.
Open assumptions A-01 … A-12 are in the spec's §6.
