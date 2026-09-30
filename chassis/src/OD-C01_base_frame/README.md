# OD-C01 base frame — build scripts

Job `20260930-od-c01-base-frame` (record: `chassis/reports/OD-C01_base_frame/`),
build v02 to DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C01_base_frame/reviews/RV01_od_c01_frame_v02.md`). The plate is a
240 × 405 × 6 floor with twenty Ø4.0 heat-set insert holes (OD-C05 carrier,
OD-C04 thermoblock mount, OD-C03 pump cradle, OD-C02 bulkhead line, OD-C07 valve
and flowmeter mount), four Ø3.4 feet holes and two Ø8 drain holes. The whole
machine layout (which mount sits where, the group head vertical at the front over
the tray zone, the thermoblock behind it, the pump across the back) rests on the
assumptions A-01 … A-17 of the spec's §6 until the Usta confirms it; the OD-C07
holes follow that job's spec, which is itself still under review.

| File | What it is |
|---|---|
| `build_od_c01_frame_v02.py` | parametric build123d model of the plate and the check assembly (OD-C03 + OD-H01, OD-C04 + OD-H11, OD-G01 at the carrier's pose, the carrier's foot box); writes STEP (AP242) and STL |
| `check_od_c01_frame_v02.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-c01-base-frame`.

Delivered files (SHA-256): see `../../reports/OD-C01_base_frame/briefs/WP-05_reviewer.md`
for the reviewed STEP, STL and 3MF; `OD-C01_base_frame.step`, `.stl` and `.3mf` in
`chassis/` are byte-identical copies of the reviewed `02_STEP_STL/od_c01_frame_C1_v02.*`.
Material: the spec says PETG on the Kobra Max 3 (the BOM row says ASA; A-10).
