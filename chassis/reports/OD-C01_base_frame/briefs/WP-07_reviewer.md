# WP-07 — reviewer brief (J4, the one review of build v03)

Job: 20260930-od-c01-base-frame · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.3 (ratified 2026-10-05) · concept C1 · revision B · target `od_c01_frame_v03` · review RV02 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v03 of the printed base frame OD-C01 of the Open Dedica
espresso machine (revision B): the plan `01_CAD/DESIGN_PLAN.md` with the amendments
of `briefs/WP-03_designer.md`, `WP-04_designer.md` and `WP-06_designer.md` (all part
of the plan), the REPORT `01_CAD/REPORT_od_c01_frame_v03.md`, and the exported files
below. Never the designer's scripts (`01_CAD/*.py`, `01_CAD/probe/`,
`01_CAD/sweep_v0*/` except the summary named below). Build v02 was reviewed in
`reviews/RV01_od_c01_frame_v02.md` (approved on assumptions); v03 should differ from
it only by eighteen new Ø4.0 insert through-holes and the material (PLA, no geometry
change). Confirm that, and that nothing else moved.

Machine frame: X right, +Y up, +Z the front, the plate's top face y 0. The group head
axis is vertical with the mouth down. Read the plausibility list against a real
espresso machine (the De'Longhi Dedica the project copies).

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a,
D-07 (N/A), J-05, E-06 (N/A), REQ-01 … REQ-14 (REQ-09 Soft bench: INCONCLUSIVE with a
risk rating). U-03's 1.3 clause: the delivered OD-C08, OD-C11 and OD-C09 at the
identity, OD-C16 six times at the poses of A-19 (right: translate (117, 0, z_c); left:
rotate 180° about Y then translate (−117, 0, z_c); z_c ∈ {−262, −15, +62}), and the
delivered OD-C07 by the A-17 joint: contacts, interference with the plate, and each
of their plate-facing Ø3.4 holes coaxial with its plate hole, offset ≤ 0.20 (the sum
of two 0.10 position bands). U-07: the 3MF `02_STEP_STL/od_c01_frame_C1_v03.3mf` was
written by the orchestrator from the designer's STL and re-parsed (11676 triangles,
volume 579003.60 mm³); check it against the STL. Also the §P list; the feature census
(1 plate, 38 Ø4.0, 4 Ø3.4, 2 Ø8.0 through-holes); positive controls for every check
family used.

OD-H11 reads `brep_valid = 0` (OD-C04 A-14): its booleans are INCONCLUSIVE by the
rows; gate its rows on distance. Weigh the REPORT's least-sure items and the
assumptions the new holes rest on (A-18 … A-20, A-11 inserts in the 6.0 plate,
A-10 PLA). The designer noted, ungated: OD-C11 stands inside the A-07 tank-zone
prism and OD-C09 inside the A-06 tray-zone prism; rate whether that matters (the
tank dock OD-C06 is deferred and the tank stands on the table; the tray is not
scanned). Note too that four of the Ø4.0 holes (x 65) serve OD-C02 as clearance holes
for M3×12 screws from below (OD-C02 spec 1.1), not as insert holes.

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `00_Spec/DESIGN_SPEC.md` | e3a5f212e3a5c329fb4b8ae87356740db1e539d56dc81b5b215df718e8f18368 |
| `01_CAD/REPORT_od_c01_frame_v03.md` | 3b09d9015d14397d628740c11e4cd38c696123a52bdd3c55b746e08edac14bea |
| `01_CAD/DESIGN_PLAN.md` | 086dde812dcc207fa171977fb45f9d2ed5a8df324099bce8c813eb3651aa7217 |
| `briefs/WP-03_designer.md` | b34294f10520e24cccaf90a702191bde0628805841af037bc0208de0980f9004 |
| `briefs/WP-04_designer.md` | 4634cd15f8906089a3129561831220145920ddd5cadd8ed6136513298254d513 |
| `briefs/WP-06_designer.md` | 9d08d2e7b473137e82f3f90698bba294f6224fecdd65d19ba284f3f2e57e63e3 |
| `01_CAD/check_od_c01_frame_v03.json` | 7f8fa24be207662026f7bc852ce2256e3bd286036899d51f6058b27a7a1119d4 |
| `01_CAD/build_record_v03.json` | 14578f5f82db4d6dfa67dc7fa3b182cfa0c69d3dab0b0cbe951909a010865467 |
| `01_CAD/sections_v03.json` | d8918c006e9da6c26ac5721ed910194fbd20fce75a608d1f0c2bdb1fa976ee93 |
| `02_STEP_STL/od_c01_assembly_C1_v03.step` | 44d2120be386438de18bc05f260043f49dbb9ae18ba7a4157fc553a0e56c4e74 |
| `02_STEP_STL/od_c01_frame_C1_v03.3mf` | 73ea066873137a834f4c45d25787160c2fbeaf5cc9cd4820272ed54206d0eef3 |
| `02_STEP_STL/od_c01_frame_C1_v03.step` | 87877a649306995965d4640f54cbf83c20715888b29eb057b18e2f2d2933d29b |
| `02_STEP_STL/od_c01_frame_C1_v03.stl` | 34d24746c62a6e1220544ce465d2714aa8f3b9631e3bf08d18e69937616af963 |
| `reviews/RV01_od_c01_frame_v02.md` | 3d8995d95670709f5d9bbd344d687c5a0f4ce3668ce6d566af3e66f7159d381d |
| `03_Sections/od_c01_frame_v03_front_y-3_plan.png` | 7d6f599a34c0bbeee9f4012a6b815e575487de91e5ea2be222f154d43622bde7 |
| `03_Sections/od_c01_frame_v03_left_asm_x0.png` | 70c30fc569dba04d15c1a50a149cc844c3cbc0cedb0b17440f27cd797dae0611 |
| `03_Sections/od_c01_frame_v03_left_asm_x104.5_bracket.png` | 0d93703808c768959e4b3171f11bf89f58cb2667c251fe7eec832480481b8c40 |
| `03_Sections/od_c01_frame_v03_left_asm_x37.png` | 7f12af3967d25e52c3c88980841a4c1a4e9497151b90669cf8595c419d97c607 |
| `03_Sections/od_c01_frame_v03_left_x-113_valve.png` | eea2934ba4efbe8404daa09a2f6fbcf36b521319415680fc0a8c0d4d97e8f9f0 |
| `03_Sections/od_c01_frame_v03_left_x104.5_bracket.png` | 50bed4d6b8455b898069704953ad9b856259dea34e2452bc6e4bd1648f216afa |
| `03_Sections/od_c01_frame_v03_left_x37_c03.png` | ac99353f6fba109133214c9dd4b569b8f2fa0fe7808a7244cca539c39ffb6914 |
| `03_Sections/od_c01_frame_v03_left_x65_bulkhead.png` | b710ecbd27a57bb08fba112d071b0447474caac1b68ce5987470a005c2908650 |
| `03_Sections/od_c01_frame_v03_top_asm_z-148.png` | 2929204c12633513553169b939bef3ef7e435748aea764a8d8d9a2b44b7078e3 |
| `03_Sections/od_c01_frame_v03_top_asm_z-222_tray.png` | 320ccc296297ec9af3b42fbbdb00e953ec5262430807ea93a43d1472ce90c23f |
| `03_Sections/od_c01_frame_v03_top_asm_z-282_back.png` | a19d71f522eb6fd7f8d7749fc59b21505e22c9e1b583f6d4abde22ab4c9432ce |
| `03_Sections/od_c01_frame_v03_top_asm_z32_mouth.png` | 1f23645267dfadda1a6a93935d52058153399dd5cf57d84b1741da3668b0d9b4 |
| `03_Sections/od_c01_frame_v03_top_asm_z77_front.png` | 975f75d72a2ad33d1d57180301c1523afa267d54a561658b65cd07f7948d749b |
| `03_Sections/od_c01_frame_v03_top_z-120_drain.png` | aba7a87f4f858f26bdcd077f2636ee5c98930c9e22370cb19fbb99fbe1ebb60c |
| `03_Sections/od_c01_frame_v03_top_z-148_c04.png` | 0693ecca7e582dfaaff3ad238987f4054b314bf57296bede62baced45087c6b6 |
| `03_Sections/od_c01_frame_v03_top_z-222_tray.png` | 2fd0be4476f99d1c5e9c9f53f4fc075d26bc96b8e85c0ba6320ee5eb6bf2fd31 |
| `03_Sections/od_c01_frame_v03_top_z-282_back.png` | df046b935f0e07c04eed32a043c4ea07d7f6e7796533ba06ab24d7e9a656847e |
| `03_Sections/od_c01_frame_v03_top_z-40_carrier.png` | 0ffdd5a8db8e668da25944e00cb1927af09043addfe1bb4384f9d0b9883d8811 |
| `03_Sections/od_c01_frame_v03_top_z-42_valve.png` | 62b18e2313115bcf28e8eebdae376b71f85501e9633ef03fa40496ce019d0758 |
| `03_Sections/od_c01_frame_v03_top_z-78_tray.png` | f1b37ade024371d3907c1c83256b022137f9177fdecdf8c7f1f7805a6f55ef3a |
| `03_Sections/od_c01_frame_v03_top_z62_bracket.png` | 8b717a71e9141a704ad122deb7adf9ea04eb25352086125246bc45b3ee3810a3 |
| `03_Sections/od_c01_frame_v03_top_z77_front.png` | 1418afd62d03e83cf712612de9246f21f635363c62c8ae7765c51982847318ba |
| `03_Sections/od_c01_frame_v03_top_z90_feet.png` | 3ca693901b367b58f4db43b24dd8231ff13df9bb86f3096e3e805181ac77bb26 |
| `01_CAD/sweep_v03/sweep_summary_v03.json` | dfa7b5270131c3ab10226f0f33a5659fe53e3ff339b884a15309ffcfee4a9867 |

Reference solids (inputs, for the assembly rows):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-C03_pump_cradle.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 |
| `00_Spec/inputs/OD-C04_thermoblock_mount.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 |
| `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c |
| `00_Spec/inputs/OD-C08_electronics_bay_tray.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 |
| `00_Spec/inputs/OD-C09_front_panel.step` | 0d688d24b7954e959291b171fa6e464dd30834e3f737eb73b696dfc992148ab5 |
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db |
| `00_Spec/inputs/OD-C16_corner_bracket.step` | 39faff6ce71326fc8d562d8c3daa42cd938fdf24f4dbe0933d82e9cae569c9fc |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 |
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 |
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff |

## Environment

Workspace `/home/claude/oguz-jobs/20260930-od-c01-base-frame`; run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV02_od_c01_frame_v03.md`, `.json`, and `RV02_work/`); if the
Write tool refuses a file, write it with Bash. `min_wall` and `overhang_census` need
`spacing=0.7` on this plate. Templates: `atolye/templates/VERDICT.md`; schema
`atolye/schemas/verdict.schema.json`.
