# OD-C05 group head carrier — build scripts

Job `20260930-od-c05-group-head-carrier` (record: `chassis/reports/OD-C05_group_head_carrier/`),
build v04 to DESIGN_SPEC 2.2 (concept C4), reviewed twice: RV01 on v01 `REVISE`
(the OD-G01 spec's machine-orientation sentence was wrong; the group head is
vertical, mouth down), RV02 on v04 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C05_group_head_carrier/reviews/RV02_od_c05_carrier_v04.md`). The
carrier is a 5 mm plate under the OD-G01 housing (four M3 screws with Ø6.5
counterbores, a Ø60 hub window, an 80 × 32 service hatch) on a closed column
(front wall 6, side and rear walls 4, a gabled rear window) that ends in a foot
on the OD-C01 plate with four M3 screws at (±35, y −72/−92) into heat-set inserts.
It prints standing on the plate with the foot up; the eight counterbore floors
are the named flat-ceiling exception of spec §5, and the whole pose of the
housing in the machine rests on A-01 … A-14 of the spec's §6 until the Usta
confirms it. RV02 F2: in the machine the foot's inside is an undrained trough
with the screw heads at its lowest points, a drain or a gasket is the Usta's call.

| File | What it is |
|---|---|
| `build_od_c05_carrier_v04.py` | parametric build123d model of the carrier and the check assembly (OD-G01 housing, OD-C01 plate); writes STEP (AP242) and STL |
| `check_od_c05_carrier_v04.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-c05-group-head-carrier`.

Delivered files (SHA-256): see `../../reports/OD-C05_group_head_carrier/briefs/WP-08_reviewer.md`
for the reviewed STEP, STL and 3MF; `OD-C05_group_head_carrier.step`, `.stl` and
`.3mf` in `chassis/` are byte-identical copies of the reviewed
`02_STEP_STL/od_c05_carrier_C4_v04.*`.
