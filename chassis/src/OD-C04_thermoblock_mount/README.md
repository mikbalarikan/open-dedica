# OD-C04 thermoblock mount — build scripts

Job `20260930-od-c04-thermoblock-mount` (record: `chassis/reports/OD-C04_thermoblock_mount/`),
build v01 to DESIGN_SPEC 1.1 (spec 1.2 changed only the heat bench gate's class),
reviewed once: RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(`reports/OD-C04_thermoblock_mount/reviews/RV01_od_c04_mount_v01.md`). Every
interface value rests on the assumptions A-01 … A-14 of the spec's §6 until the
Usta confirms it with calipers; the air gap to the thermoblock is 10.10 mm against
a scan with 0.47 mm p95 error (RV01 F2).

| File | What it is |
|---|---|
| `build_od_c04_mount.py` | parametric build123d model of the part, the two assumed spacers and the check assembly with OD-H11; writes STEP (AP242) and STL |
| `check_od_c04_mount.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount`.

Delivered files (SHA-256): see `../../reports/OD-C04_thermoblock_mount/briefs/WP-04_reviewer.md`
for the reviewed STEP and STL; `OD-C04_thermoblock_mount.step` and `.stl` in
`chassis/` are byte-identical copies of the reviewed
`02_STEP_STL/od_c04_mount_C1_v01.step` and `.stl`.
