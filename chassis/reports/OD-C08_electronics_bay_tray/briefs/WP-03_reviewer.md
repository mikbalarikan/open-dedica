# WP-03 — reviewer brief (J4, the one review of build v01)

Job: 20261001-od-c08-electronics-bay-tray · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-10-01) · concept C1 · target `od_c08_tray_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed electronics bay tray OD-C08 of the Open
Dedica espresso machine: the plan `01_CAD/DESIGN_PLAN.md`, the REPORT
`01_CAD/REPORT_od_c08_tray_v01.md`, and the exported files listed below. Never
the designer's scripts (`01_CAD/*.py`, `01_CAD/*.sh`, `01_CAD/probe/*.py`,
`01_CAD/sweep_v01/`), only their JSON results where a row needs them.

The machine frame: X right, +Y up, +Z front, the plate's top face y 0. The tray
is a wall parallel to the bulkhead OD-C02 (x 59 … 71) at x 73 … 76 with a floor
flange screwed from above into four **new** M3 inserts in OD-C01 (spec A-01: not
in the OD-C01 STEP yet; the plate rows rest on the plate's material under each
hole). It carries the **original** power PCB OD-E01 on edge (the Usta keeps the
OEM board for this stage): board x → −Z, y → +Y, z → +X, origin (84, 80, −100),
on four standoffs (two M3 screws into inserts at H1/H2, two pins at H5/H6).
OD-E01 is a scan (BAND_NOT_MET, A-02): weigh its envelope accordingly. Print:
lying on the wall's outer face x 73, build direction +X, PETG on the K1C (A-08,
A-09, A-10).

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-08 (U-08 N/A), U-06 Soft; D-01a, D-01b (the designer reads the web
above the tie slots at 2.0, margin 0: read it yourself), D-02, D-03a and D-03b
(named exception on the four flange-hole crowns), D-04a, D-04c, D-04d, D-05a,
D-05b, D-06a, D-07 (N/A), J-05 (the designer reads 3.0, margin 0), E-01, E-05,
E-06, E-11, REQ-01 … REQ-06 (REQ-06 Soft bench: INCONCLUSIVE with a risk
rating); `exactly_one_solid`, `feature_census` against the plan,
`envelope_within_spec`; the §P plausibility list; positive controls for every
check family used. U-07: the 3MF `02_STEP_STL/od_c08_tray_C1_v01.3mf` was written
by the orchestrator from the designer's STL and re-parsed (3244 triangles,
70594.55 mm³, watertight, bbox x 73 … 112, y 0 … 92, z −230 … −70): check it
against the STL.

Weigh the REPORT's least-sure items: the sweep finds that a standoff off its
position by 0.10 (inside REQ-02 and E-05) takes the pin gap to 0.23, under D-04d's
0.30, so D-04d tolerates about 0.03 of position error; J-05 drops to 2.975 with a
Ø4.05 bore; the seat at the measured solder face x 82.438. And the open
assumptions A-01 … A-13, chiefly A-01 (new OD-C01 inserts and screws from above
between the wall and the board), A-02 / A-05 (the scanned board and the mains
side 6.44 from the wall), A-11 (wires, mains entry, venting), A-12 (the board
held by two screws and two pins).

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `briefs/WP-02_designer.md` | 58b210d802aa9760ae11931b2b98566a6470b8ed39787bf2f9bb5d98686f2749 |
| `00_Spec/DESIGN_SPEC.md` | 5b559450a15d3ba56badbcd51d47b76caa9d1bd3f23199995378a976a18fd8f3 |
| `00_Spec/INTAKE_v01.md` | 26641f69474020f9ce379adaca2c9524290261022cf1629857f9fff479a36dae |
| `01_CAD/DESIGN_PLAN.md` | 08cce6b90703d0d0ed6b62e0feddab77f624b354940881f46850d45c7261ae31 |
| `01_CAD/REPORT_od_c08_tray_v01.md` | 7e73a0d3bb2d03f52ffc3fb42a51d7cb8fcf3ae5715feac378510aab77fc1b86 |
| `01_CAD/check_od_c08_tray_v01.json` | da444cc036634ea24054fd722d287573ea26bac7d0e6f017f72220c0b620e948 |
| `01_CAD/build_record_v01.json` | 8d22e681e824e45c355c244679e40590dc5e36d5c09bc1d845139848610fde0a |
| `01_CAD/sections_v01.json` | 309152fa51687e8cb051bb8a840f7c0c01f0a2fe984676249b9b753800fa9131 |
| `01_CAD/probe/probe_inputs.json` | 7fe1a3f885bfaf224d456ae218addcf5cd431ab627e57a5dfa88fd299f8688eb |
| `02_STEP_STL/od_c08_assembly_C1_v01.step` | 21e6f254048e2239216b63e493d764510f7e002180ba0498bf91406c56ecc9aa |
| `02_STEP_STL/od_c08_tray_C1_v01.3mf` | 24ac0b1122c6a5ee18293ef45d9dab17485d05515f3b034c7658fe5de802d945 |
| `02_STEP_STL/od_c08_tray_C1_v01.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 |
| `02_STEP_STL/od_c08_tray_C1_v01.stl` | 2ac2db7f63d8ffc91c9d0e3af809a9964152b68826eba5e76eb237d36c22df49 |
| `03_Sections/od_c08_tray_v01_front_asm_y80_board_H1_H5.png` | 996fd9d4516e9b6391123a22f4c36d3392ce12b469a6dc005aa07e2d8f1e0c7e |
| `03_Sections/od_c08_tray_v01_front_y2_flange.png` | 69064a409d082daa490977cc3b47c2b14bccdf6013e4c5d54512355dbc93a162 |
| `03_Sections/od_c08_tray_v01_front_y80_H1_H5.png` | c124b9824d3e7fd860f9dd9a58c29e2c174c23d5d77723deadc398966d72eb65 |
| `03_Sections/od_c08_tray_v01_front_y88_slots.png` | 21be331cd7d3f2d1e67a8b8f45753e8a6b858adc35918a35604a78bcc654e14a |
| `03_Sections/od_c08_tray_v01_left_x74.5_wall.png` | 938e82334fc516d77bbabf4ec542c1600bef598486982dafd1b6d79b5b6d742c |
| `03_Sections/od_c08_tray_v01_left_x79.4_standoffs.png` | 8e42662377d3ae8f3ac12a832bac1e4944a42a1492c32e53c12e3290d1b6c9dd |
| `03_Sections/od_c08_tray_v01_left_x83.5_pins.png` | 2ac719bf7346a7ffacd956665fe81b00c016cac25d085ea82be1e73ee9f28bfb |
| `03_Sections/od_c08_tray_v01_top_asm_z-100_board_H1_H2.png` | 4659069f7949a636389f7d5b3f2e43ed3004f3a92d609160ba0b25035257f4e5 |
| `03_Sections/od_c08_tray_v01_top_asm_z-157.5_board_pins.png` | 717a12a29c878423261e43a050a429dfd04de8abaef2fb1badb632ea7d5da7cc |
| `03_Sections/od_c08_tray_v01_top_asm_z-222_screw_path.png` | 548f6f5712e012d3781b1a9e2d1c9c83a3667f9cb8e34733469ff405561d3c42 |
| `03_Sections/od_c08_tray_v01_top_z-100_H1_H2_inserts.png` | 20cbcd2153a170545f1de4f2085ee04e3b7014bfaeeb6ed70174438c2c7cedae |
| `03_Sections/od_c08_tray_v01_top_z-157.5_H5_H6_pins.png` | 6382c2eac986e610923cc35051ee2b58640baec50d25ff3951d3e2055563b390 |
| `03_Sections/od_c08_tray_v01_top_z-168_tie_slot.png` | 35837c7db250dc05aa90c995cabed425ad244eed0d06e129a5ec08649684c060 |
| `03_Sections/od_c08_tray_v01_top_z-222_rear_holes.png` | 9bdd66c0d58ea9762fe1e4f49557f8c4e7078761b89e156a4986682a3673b360 |
| `03_Sections/od_c08_tray_v01_top_z-78_front_holes.png` | cd04361ebe0c1996483b7043af58981a8c864a1503aaf008255c75be176591ba |
| `03_Sections/od_c08_tray_v01_top_z-86.5_gusset.png` | 96fa67317ccca30d1a0196c23823493e18c85d0fd84d54a435bee6583a281294 |

The sweep results are under `01_CAD/sweep_v01/` (JSON only). Reference solids
(inputs, for the assembly rows): as `briefs/WP-02_designer.md` lists them with
their hashes and joints.

## Environment

Workspace `${OGUZ_JOBS}/20261001-od-c08-electronics-bay-tray`; run
`. $HOME/oguz-env/env.sh` first in every shell command, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_c08_tray_v01.md`, `.json`, and `RV01_work/`); if the
Write tool refuses a file, write it with Bash. `min_wall` and `overhang_census`
may need `spacing=0.7` on the large faces. Templates: `atolye/templates/VERDICT.md`;
schema `atolye/schemas/verdict.schema.json`. Do not call any `mcp__hearthbot__*`
tool; your hand-back goes to the orchestrator only.
