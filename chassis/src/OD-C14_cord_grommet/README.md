# OD-C14 cord grommet — build scripts

Job `20261002-od-c14-cord-grommet` (record: `chassis/reports/OD-C14_cord_grommet/`),
build v01 to DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`,
no blocking finding (`reports/OD-C14_cord_grommet/reviews/RV01_od_c14_grommet_v01.md`).
The grommet is split along its axis into two identical halves (the BOM's qty 2):
laid round the Ø7 mains cord, pushed into OD-C11's Ø12 cord hole from outside until
the Ø20 flange meets the wall, and closed onto the cord by one 4.8 mm cable tie in
the groove just inside the wall. Each half is cut 0.4 short of the axis, so the tie
squeezes the cord by 0.4 from each side; the tie, wider than the hole, takes the
cord's pull. Print two.

| File | What it is |
|---|---|
| `build_od_c14_grommet.py` | parametric build123d model of the half and the check assembly; writes STEP (AP242) and STL |
| `check_od_c14_grommet.py` | the designer's gate checks (spec §5) on the re-imported STEP and assembly |
| `sections_od_c14_grommet.py` | the section pictures |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261002-od-c14-cord-grommet`.

Delivered files: `OD-C14_cord_grommet.step` and `.stl` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_c14_grommet_half_C1_v01.step`
/ `.stl` (SHA-256 in `../../reports/OD-C14_cord_grommet/briefs/WP-04_reviewer.md`);
the `.3mf` is written from that STL (1658 triangles). The part is modelled at its
installed place in the machine frame (the upper half, cord axis at x 95, y 30).

Print: PLA (the Usta, 2026-10-02, "for now"; the BOM says TPU) on the K1C,
standing on the flange's outer face, no supports. Fit: halves round the cord
outside the machine, push in, tie head upward, pull tight, cut the tail. Open
assumptions A-01 … A-08 are in the spec's §6; the first fitting answers REQ-05
(does the tied grommet hold a firm pull without turning).
