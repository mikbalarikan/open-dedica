# OD-C09 front panel with button bezel — build scripts

Job `20261002-od-c09-front-panel` (record: `chassis/reports/OD-C09_front_panel/`),
build v01 to DESIGN_SPEC 1.1, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`,
no blocking finding (`reports/OD-C09_front_panel/reviews/RV01_od_c09_front_v01.md`).
F1 (MEDIUM) stiffness is a bench check on the first print; F2 (MEDIUM) the
portafilter handle keeps 2.5 to the window's right edge at a lock of +10° past
the new-gasket position, 0.8 at +11° and touches at +12°, so check the lock angle
as the gasket wears (A-05).

The panel is a 3.0 PLA fascia at z +94 … +97, x ±116, y 0 … 215 in the machine
frame, standing on OD-C01 inside its front edge:
- brew opening: the tray slot x ±75, y 0 … 50 and the window x −57.5 … +75,
  y 0 … 188, framed by 10-deep return ribs;
- two floor flanges (4.0 thick, z +72 … +94) with gussets, held by four M3 × 8
  ISO 7380 from above into four new OD-C01 inserts at (±85, +77) and (±95, +77);
- the OEM button board OD-E02 on two Ø11 bosses (M3 inserts, two M3 × 18 ISO 4762
  from the board's back), its three buttons through three Ø15 holes in a column on
  the left pillar: 1 cup at the top, 2 cups at y 140, steam at the bottom;
- the steam knob's place (Ø32 about (+95.5, 140)) kept free on the right pillar
  for the phase-2 steam job;
- OD-C10's front skirt rests on the top edge (y 215).

| File | What it is |
|---|---|
| `build_od_c09_front.py` | parametric build123d model; writes STEP (AP242), STL and the check assembly |
| `check_od_c09_front.py` | the designer's gate checks (spec §5) on the re-imported STEP and assembly |
| `sweep_od_c09_front.py` | D7 robustness sweep (33 runs) |
| `sections_od_c09_front.py` | the section cuts the review reads |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261002-od-c09-front-panel`
(inputs in its `00_Spec/inputs/`).

Delivered files: `OD-C09_front_panel.step` and `.stl` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_c09_front_C1_v01.step` /
`.stl` (SHA-256 0d688d24…148ab5 / 086c7c7e…740498); the `.3mf` is written from
that STL (3932 triangles, volume unchanged).

Print: PLA on the Kobra Max 3 (A-10, A-11), lying on its front face, build
direction −Z, no supports (A-09); a brim if the 232 × 215 plate lifts. About
119 g. Assembly order (A-14): screw the panel to the plate, then fit the board
from behind with the lid off. Open assumptions A-01 … A-14 are in the spec's §6.
