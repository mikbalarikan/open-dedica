# OD-C08 electronics bay tray — build scripts

Job `20261001-od-c08-electronics-bay-tray` (record: `chassis/reports/OD-C08_electronics_bay_tray/`),
build v01 to DESIGN_SPEC 1.0, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C08_electronics_bay_tray/reviews/RV01_od_c08_tray_v01.md`). The tray
carries the original power PCB OD-E01 on edge, parallel to the bulkhead OD-C02:
a 3 mm wall at x 73 … 76 (z −230 … −70, 92 tall) with a floor flange screwed from
above into four new M3 inserts in OD-C01 at (88, −222), (106, −222), (88, −78),
(106, −78), four gussets, two Ø10 standoffs with Ø4.0 × 6 insert bores (board
holes H1, H2) and two Ø6 standoffs with Ø1.8 × 2.5 pins (H5, H6), and four tie
slots. It prints lying on the wall's outer face. The board's position rests on
its scan (OD-E01, A-02) and the plate inserts on an OD-C01 change (A-01) until the
Usta confirms them.

Review notes for the build: an M3 × 8 through the board bottoms 0.44 past the
bore floor unless a washer ≥ 0.5 is fitted, or use M3 × 6 (RV01 F3); the pins
tolerate about 0.03 of position error, so calipers should check H5/H6 against
the scan (F4); the board's stiffness at the faston row is a bench check at first
assembly (F2).

| File | What it is |
|---|---|
| `build_od_c08_tray.py` | parametric build123d model of the tray and the check assembly (OD-C01 plate, OD-C02, OD-E01 as placed); writes STEP (AP242) and STL |
| `check_od_c08_tray.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261001-od-c08-electronics-bay-tray`.

Delivered files: `OD-C08_electronics_bay_tray.step`, `.stl` and `.3mf` in
`chassis/` are byte-identical copies of the reviewed
`02_STEP_STL/od_c08_tray_C1_v01.*` (SHA-256 in
`../../reports/OD-C08_electronics_bay_tray/briefs/WP-03_reviewer.md`).
