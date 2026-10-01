# OD-C15 foot — build scripts

Job `20261001-od-c15-feet` (record: `chassis/reports/OD-C15_foot/`), build v01 to
DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`, no findings
(`reports/OD-C15_foot/reviews/RV01_od_c15_foot_v01.md`). The foot is a TPU puck
Ø18 × 10 under each of OD-C01's four Ø3.4 feet holes, held by an M3×12 ISO 7380
button-head screw from the plate top into an ISO 4032 M3 hex nut captive in the
foot's pocket (across flats 5.60, open at the counter face). Print four.

| File | What it is |
|---|---|
| `build_od_c15_foot.py` | parametric build123d model of the foot; writes STEP (AP242) and STL |
| `build_check_assembly.py` | the check assembly: OD-C01 + four feet + screw and nut envelopes, placed by joints on the measured hole axes |
| `check_od_c15_foot.py` | the designer's gate checks (spec §5) on the re-imported STEP and assembly |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20261001-od-c15-feet`.

Delivered files: `OD-C15_foot.step` and `.stl` in `chassis/` are byte-identical
copies of the reviewed `02_STEP_STL/od_c15_foot_C1_v01.step` / `.stl` (SHA-256 in
`../../reports/OD-C15_foot/briefs/WP-04_reviewer.md`); the `.3mf` is written from
that STL (1194 triangles, volume unchanged).

Print: TPU 95A on the K1C (A-03), top face (the face against the plate) on the
bed, no supports; the nut enters from the counter side and the screw pulls it onto
its seat. Open assumptions A-01 … A-10 are in the spec's §6; the first printed
foot answers A-06 (does the nut hold against turning) and A-07 (creep: a drop of
medium threadlocker).
