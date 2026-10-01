# OD-C02 bulkhead — build scripts

Job `20260930-od-c02-bulkhead` (record: `chassis/reports/OD-C02_bulkhead/`),
build v02 to DESIGN_SPEC 1.2, reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C02_bulkhead/reviews/RV01_od_c02_bulkhead_v02.md`). The bulkhead is a
4 mm wall on x 63…67 (wet side toward −X, electronics side toward +X), 215 tall
and 210 long, with a 12-wide base rail carrying four Ø4.0 × 6 blind heat-set
insert bores from below (M3 × 12 screws through the OD-C01 plate), a top rail with
two Ø4.0 × 6 bores from above, and four Ø14 windows with a 45° gable so the part
prints standing on its rear end with no support. The wall's position, the
window uses, and the screw length rest on the assumptions A-01 … A-13 of the
spec's §6 until the Usta confirms them; an M3 × 12 ends exactly on the base-bore
floor (RV01 F2), so a shorter screw or a deeper bore is the Usta's call.

| File | What it is |
|---|---|
| `build_od_c02_bulkhead_v02.py` | parametric build123d model of the bulkhead and the check assembly (OD-C01 plate, OD-C03 + OD-H01, OD-C04 + OD-H11); writes STEP (AP242) and STL |
| `check_od_c02_bulkhead_v02.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-c02-bulkhead`.

Delivered files (SHA-256): see `../../reports/OD-C02_bulkhead/briefs/WP-04_reviewer.md`
for the reviewed STEP, STL and 3MF; `OD-C02_bulkhead.step`, `.stl` and `.3mf` in
`chassis/` are byte-identical copies of the reviewed `02_STEP_STL/od_c02_bulkhead_C1_v02.*`.
