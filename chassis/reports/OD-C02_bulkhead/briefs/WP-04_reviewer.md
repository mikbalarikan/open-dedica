# WP-04 — reviewer brief (J4, the one review of build v02)

Job: 20260930-od-c02-bulkhead · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 · target `od_c02_bulkhead_v02` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v02 of the printed wet/electric bulkhead OD-C02 of the Open
Dedica espresso machine: the plans `01_CAD/DESIGN_PLAN.md` and `01_CAD/DESIGN_PLAN_v02.md`
with the amendments of `briefs/WP-03_designer.md` (part of the plan), the REPORT
`01_CAD/REPORT_od_c02_bulkhead_v02.md`, and the exported files listed below. Never
the designer's scripts (`01_CAD/*.py`, `01_CAD/*.sh`, `01_CAD/probe/`,
`01_CAD/sweep_v02/`). Build v01 was stopped by the designer on spec 1.0 faults and
is not under review. The build was made to spec 1.1; spec 1.2 changed two ledger
sentences only (A-04, A-05 aligned to §4), no geometry: review against 1.2 and
write `"spec_version": "1.2"` in the JSON twin.

The machine frame: X right, +Y up, +Z front, the plate's top face y 0. The
bulkhead stands on the OD-C01 plate over its four Ø4.0 holes at x 65 and is
screwed from below (M3 × 12 through the plate into inserts in the bulkhead's
base rail, spec A-01, A-03): weigh that choice in §P (assembly order, the feet
lifting the plate, the head under the plate). The neighbours are placed as
OD-C01 spec §4 states; the carrier OD-C05 is a foot box x ±55 (not built yet).
Print: standing on its rear end z −240, build direction +Z (spec A-10): weigh a
210 tall, 4 thick wall on a 12 × 215 footprint (bed adhesion, warp).

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (contact with the plate, coaxial bores, clearances to every
neighbour; the OD-H11 boolean INCONCLUSIVE by OD-C04 A-14), U-04 (the part; on the
assembly the designer reads OD-H11's round trip INCONCLUSIVE, rule on it), U-05,
U-06 (Soft), U-07 (the 3MF `02_STEP_STL/od_c02_bulkhead_C1_v02.3mf` was written by
the orchestrator from the designer's STL and re-parsed: 2308 triangles; check it
against the STL), U-08 (N/A), D-01a, D-01b (the sweep found the top-rail bore
floor 2.0 above the rail's underside at nominal, margin 0: read it yourself),
D-02, D-03a (with the named exception on the six bore crowns; the window gables at
45°: read the analytic angle), D-03b, D-04a (N/A), D-05a, D-05b, D-06a, D-07 (N/A),
J-05, E-06, REQ-01 … REQ-09 (REQ-09 Soft bench: INCONCLUSIVE with a risk
rating); the §P list; the feature census against the plan as amended (1 wall, 1
base rail, 1 top rail, 4 gabled windows, 4 + 2 Ø4.0 blind bores); positive
controls for every check family used.

Weigh the REPORT's least-sure items and the open assumptions: A-01 / A-03 (screws
from below), A-04 (the windows' places against wires nobody has routed), A-06
(215 tall against a ≈ 260 machine), A-07 (1 mm into the bay zone), A-10 (the
standing print), A-11 / REQ-09 (a 4 mm wall with two rails), A-12 (the dam and the
drains).

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `briefs/WP-02_designer.md` | bef551ec52f093c4bbd91cdf068d216441d7f1a81bbf51bbd165a0ab39787936 |
| `briefs/WP-03_designer.md` | 1639c07d87977f3afe27cec6e1ca4437aab9388e474f9151600686ae1a2813d5 |
| `01_CAD/DESIGN_PLAN.md` | 119de1e798b8c65da5e8bbb882fdb86e1b358b0a7813cb16654dc2d406cf4005 |
| `01_CAD/DESIGN_PLAN_v02.md` | cc39c89c991d21038ed6167b5f5e017f902c3f91749e65d43e3cbb4b6dcc1e25 |
| `01_CAD/REPORT_od_c02_bulkhead_v02.md` | afcf6b68b21166862ac6c388f4403e643c095951d8fa2663f3f50817c039fb82 |
| `01_CAD/check_od_c02_bulkhead_v02.json` | e25653f36074ef4e2736981b5bdb438118182f14636df42c47b1d90b37572a96 |
| `01_CAD/build_record_v02.json` | 29df8e6a1c410cd24d54753d03be262990cb0cff5dc05c726a6ff5c5c72dfcbc |
| `01_CAD/sections_v02.json` | a0f85af79cea879c5ad317fd9ed49d3bd93642812fa08ff24524b531373004cc |
| `01_CAD/sweep_v02/sweep_summary_v02.json` | 835489ee99be3c15d6499678b7a8ff3bb01d16089de7df9c8a8aaaa660d62b7f |
| `02_STEP_STL/od_c02_assembly_C1_v02.step` | 7d2e760590973fdfe529338231b117a9fc456d246b886a0217c4785f61d37141 |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.3mf` | 8a82334c463566c6ac2d57616d59a2c432be3dd9a9246526e926670b183cf082 |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.stl` | e48afe62c8beb97acc76da990d75ab7e4e2bfbd5416b9cf3f38a0f65d573e18e |
| `03_Sections/od_c02_bulkhead_v02_front_asm_y40_pump_axis.png` | f013d41ef5d0c98d37a90ae94eb02a03ea7cd6ef70b82ddb01b76c3a449a039f |
| `03_Sections/od_c02_bulkhead_v02_front_y100_wall.png` | 14bfe4d6a099cb3832034ff85ff3d82d6b18a1d2a70b229d86b9bcd25b85b898 |
| `03_Sections/od_c02_bulkhead_v02_front_y150_windows.png` | b2a0a80267cae4db912369f30bd052b7b5b1aec2b6dd50c35a6c7f6d9c7c867a |
| `03_Sections/od_c02_bulkhead_v02_front_y200_wall.png` | d0974d6fee694379e4370f32499ddef043fc7af70e1a13ae4d703e0dc523e201 |
| `03_Sections/od_c02_bulkhead_v02_front_y212_top_bores.png` | 4d472eef3c953d7249ec311a58892d8ac81f371e358f51572507171c789f0d18 |
| `03_Sections/od_c02_bulkhead_v02_front_y3_base_bores.png` | 845b6fe1ef45980aafaed39bcc59e34cd031d53f9d76cc217880e0acf1f7c5aa |
| `03_Sections/od_c02_bulkhead_v02_front_y60_w4.png` | 67770763500038249dbd13652416a4afded07a77a9be51a2749f444bb28d8d76 |
| `03_Sections/od_c02_bulkhead_v02_left_x61_wet_flanges.png` | 7f78fceaf2d86621f41e452eb974cfdc627c2bc96a3d7c47a8c756010133ee76 |
| `03_Sections/od_c02_bulkhead_v02_left_x65_wall.png` | fb921d6914156ef9ff1fadff749db60e84e55bbc93e12bc403535d892982455d |
| `03_Sections/od_c02_bulkhead_v02_left_x69_elec_flanges.png` | 89844a2326846b78986d24dc4eec7751d373c7e2b9ef97b5688696091c32a51e |
| `03_Sections/od_c02_bulkhead_v02_top_asm_z-200_pump.png` | f02d101427d33129088396da8473f1bf14396f81867ef017a561028783077b3c |
| `03_Sections/od_c02_bulkhead_v02_top_asm_z-45_screw_path.png` | f494d9f8b8fca5bea96f09ac4171ce34336ba78d62a3547180026ba3e58dfe40 |
| `03_Sections/od_c02_bulkhead_v02_top_asm_z-50_carrier.png` | f73c749d94eeeda70dae26c79aae7d2de7973bb84749a1c05601b2cf1faa1eb9 |
| `03_Sections/od_c02_bulkhead_v02_top_z-100_profile.png` | 884bfe8bddc10a43dad4d631ffa872134e69b66d9749c2890441964275db6181 |
| `03_Sections/od_c02_bulkhead_v02_top_z-105_base_bore.png` | 8aa3df8c1f4f1ebcd95f632ce9fe49eacf25949e553bb5badeefa34db4b35f61 |
| `03_Sections/od_c02_bulkhead_v02_top_z-200_w1.png` | 8c9c069d503e55f8a4aa1af609e1a8450d14e1ca121432c58f9c59d06c75bdc6 |
| `03_Sections/od_c02_bulkhead_v02_top_z-210_top_bore.png` | 6efa7be178935b633b7e648afffc48c98f7620499a9e7ca2403c6d494f5ae959 |
| `03_Sections/od_c02_bulkhead_v02_top_z-45_base_bore.png` | 6cd48f161cb614a7f64f0846e39834cfc11ba9a92105745cec668b88caaacfd1 |
| `03_Sections/od_c02_bulkhead_v02_top_z-55_w4.png` | 64b41b5f4c20dd8daf318c6f2a06d772ae6a1875195803fd7f8cab354fb6247a |
| `03_Sections/od_c02_bulkhead_v02_top_z-60_top_bore_w3.png` | d3bde5253d819d70a8fa5d20b5664dcfb786efa67b48fb8fd81a9f235322df78 |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.3mf` | 8a82334c463566c6ac2d57616d59a2c432be3dd9a9246526e926670b183cf082 |

Reference solids (inputs, for the assembly rows): as `briefs/WP-02_designer.md`
lists them with their hashes and joints.

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c02-bulkhead` (`/home/claude/oguz-jobs/20260930-od-c02-bulkhead`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_c02_bulkhead_v02.md`, `.json`, and `RV01_work/`); if
the Write tool refuses a file, write it with Bash. `min_wall` and
`overhang_census` may need `spacing=0.7` on the large faces.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
