# OD-C12 / OD-C13 side panels and OD-C16 corner bracket — build scripts

Job `20261002-od-c12-c13-c16-side-panels` (record: `chassis/reports/OD-C12_C13_C16_side_panels/`),
build v01 to DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`,
no blocking finding (`reports/OD-C12_C13_C16_side_panels/reviews/RV01_od_side_panels_v01.md`).

The two side panels are printed 3.0 mm plates, 385 × 215, standing on the base plate
OD-C01 with their outer faces flush with its side edges (x ±120) and ending square at
z −295 and +90. The lid OD-C10's side skirts rest on the panel tops; a 60° wedge lip on
each panel's inner rail locates the skirt with 0.40 of play. OD-C12 (left) is the
mirror of OD-C13 (right) plus a 0.9 relief over the valve mount OD-C07. Each panel's
foot is held by three OD-C16 brackets (z −262, −15, +62): one M3×8 down through the
bracket into a new insert in OD-C01, one M3×8 through the panel from outside into the
insert in the bracket.

| File | What it is |
|---|---|
| `params_od_side_panels.py` | every dimension of the three parts (spec §4) |
| `build_od_c13_right.py`, `build_od_c12_left.py`, `build_od_c16_bracket.py` | parametric build123d models; write STEP (AP242) and STL |
| `placements_od_side_panels.py`, `assemble_od_side_panels.py` | bracket poses and the check assembly with the delivered neighbours |
| `check_*.py`, `checklib_od_side_panels.py` | the designer's gate checks (spec §5) on the re-imported STEPs and the assembly |
| `sweep_od_side_panels.py` | the robustness sweep (tolerance corners) |
| `sections_od_side_panels.py`, `measure_refs_v01.py`, `report_tables_v01.py` | section pictures, reference measurements, REPORT tables |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261002-od-c12-c13-c16-side-panels`.

Delivered files in `chassis/`: `OD-C13_right_side_panel`, `OD-C12_left_side_panel`
and `OD-C16_corner_bracket` `.step` / `.stl` are byte-identical copies of the reviewed
`02_STEP_STL/*_C1_v01` files (SHA-256 in `../../reports/OD-C12_C13_C16_side_panels/briefs/WP-04_reviewer.md`);
each `.3mf` is written from its STL. The panels are modelled in the machine frame at
their installed place. The bracket is modelled in its own frame (block x −19 … 0,
y 0 … 16, z ±8): right side at (117, 0, z_c), left side turned 180° about Y at
(−117, 0, z_c), z_c ∈ {−262, −15, +62}.

Print: PLA (the Usta, 2026-10-02, "for now"; the BOM says ASA / PETG; no geometry
change for a later reprint). Panels on the Kobra Max 3, flat on the outer face, no
supports, with a brim against warp. Brackets (print six) on the K1C on their
underside. OD-C01 needs six new M3 inserts at (±104.5, −262 / −15 / +62) before
the brackets go on. Open assumptions are in the spec's §6; the first print answers
REQ-08 (no visible flex or drumming with the lid on).
