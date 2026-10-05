# OD-C01 base frame — build scripts

Job `20260930-od-c01-base-frame` (record: `chassis/reports/OD-C01_base_frame/`),
revision B: build v03 to DESIGN_SPEC 1.3, reviewed once: RV02
`APPROVED_ASSUMPTION_CONDITIONAL` (`reports/OD-C01_base_frame/reviews/RV02_od_c01_frame_v03.md`;
revision A, build v02, was RV01). The plate is a 240 × 405 × 6 floor with
thirty-eight Ø4.0 holes for M3 heat-set inserts driven from the top (OD-C05 carrier,
OD-C04 thermoblock mount, OD-C03 pump cradle, OD-C07 valve and flowmeter mount,
OD-C08 tray, OD-C11 back panel, six OD-C16 side-panel brackets, OD-C09 front panel;
the four at x 65 take OD-C02's M3×12 from below as clearance holes, no insert),
four Ø3.4 feet holes and two Ø8 drain holes. Revision B differs from A only by the
eighteen holes for OD-C08, OD-C11, OD-C16 and OD-C09 (RV02 confirms nothing else
moved). The layout rests on the assumptions A-01 … A-20 of the spec's §6 until the
Usta confirms them with calipers and the first print.

RV02 findings, none blocking: F1 REQ-09 flatness is a bench check (warp on a
405 mm plate, brim); F2 OD-C11 takes the rear 25 of the 55 mm tank zone (the tank
stands on the table for now); F3 the check assembly's re-read is invalid only
through the scanned OD-H11; F4 the four x 65 holes are clearance holes for OD-C02,
not inserts; F5 the OD-C07 holes leave a 5.0 web to the plate edge, now in PLA;
F6 OD-C09 touches the tray zone without sharing volume.

| File | What it is |
|---|---|
| `build_od_c01_frame_v03.py` | parametric build123d model of the plate and the check assembly (the mounts and their OEM parts, OD-G01 at the carrier's pose, OD-C07, OD-C08, OD-C09, OD-C11, six OD-C16); writes STEP (AP242) and STL |
| `check_od_c01_frame_v03.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-c01-base-frame`.

Delivered files: `OD-C01_base_frame.step`, `.stl` and `.3mf` in `chassis/` are
byte-identical copies of the reviewed `02_STEP_STL/od_c01_frame_C1_v03.*` (SHA-256 in
`../../reports/OD-C01_base_frame/briefs/WP-07_reviewer.md`). Material: PLA for now
(the Usta, 2026-10-02; 718 g at 1240 kg/m³); service material PETG or ASA (A-10).
Print flat on the Kobra Max 3, bottom face down, no supports, with a brim.
