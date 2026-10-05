# INTAKE v01 — 20261002-od-c09-front-panel

Intake: Claude Code, claude-sonnet-5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-10-02

<!--
Everything the job's inputs say, as tables, one row per value (PLAYBOOK §1 intake,
J0). Nothing here is confirmed: the orchestrator turns §2 and §3 rows into A-##
ledger rows in DESIGN_SPEC §6, and only the Usta confirms one (rule 5). Values
keep their original form and source. No prose summaries, no averaging, no
resolved conflicts, no persona text. A new batch of inputs gets a new version;
an earlier version is never overwritten.
-->

## §1 Files

| # | Path (relative to the workspace) | SHA-256 | Bytes | Type | Pages or views | Read how |
|---|---|---|---|---|---|---|
| 1 | 00_Spec/inputs/REQUEST.md | 72f3919c939dcbcdcded6e3db1c8af51f5755da864530f93880b85e97e7714b7 | 1266 | Markdown (chat excerpt) | 1 | full text |
| 2 | 00_Spec/inputs/bom_rows.csv | 6e64cdcdfd876155639582e4e6afa5ef47864c8ae3b415d34a2e08de938eefac | 2136 | CSV (BOM rows) | 20 rows | full text |
| 3 | 00_Spec/inputs/CHASSIS_README.md | ac5e9383209553c87b271dfc55c0776d75dfc25899dbf176afdd5668a2603443 | 8917 | Markdown | 1 | full text |
| 4 | 00_Spec/inputs/SOURCING_GUIDE_s6.md | e4615a5d9955cc95284bdf3d5b6d92fb8ef1c2f41630f37171c5c6c76a84bd22 | 3303 | Markdown (excerpt of §6-7) | 1 | full text |
| 5 | 00_Spec/inputs/OD-C01_DESIGN_SPEC.md | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | 25226 | Markdown (DESIGN_SPEC v1.2) | 1 | full text |
| 6 | 00_Spec/inputs/OD-C05_DESIGN_SPEC.md | 3accd3b00bf26544ea0aed71e72f23387afb3af447e8f26f2f0bb325dd3377bd | 27945 | Markdown (DESIGN_SPEC v2.2) | 1 | full text |
| 7 | 00_Spec/inputs/OD-C10_DESIGN_SPEC.md | e2eda540dd141c27a3ca8f7a84f2d05cfbf99a1d8df283c03bff28000c4ee966 | 21802 | Markdown (DESIGN_SPEC v1.2) | 1 | full text |
| 8 | 00_Spec/inputs/OD-C11_DESIGN_SPEC.md | 6da33456e123942bb92e7419ff190f6e01522b0580d36d510fa9c5eee6d61245 | 22734 | Markdown (DESIGN_SPEC v1.2) | 1 | full text |
| 9 | 00_Spec/inputs/OD-C15_DESIGN_SPEC.md | a24c23f25b2f02b916d89beb76e3db5c899d02d518c3775c402b5ed27e0e496f | 16838 | Markdown (DESIGN_SPEC v1.2) | 1 | full text |
| 10 | 00_Spec/inputs/OD-G01_DESIGN_SPEC.md | 55841f6ba178ac7250a22e156b55941002437a794ce008f231c1ea090138e44b | 25091 | Markdown (DESIGN_SPEC v1.3) | 1 | full text |
| 11 | 00_Spec/inputs/OD-E02_REPORT.md | ce5f0ea18403cd05e70140fed694c52ca876c9a94c20d54783430bfd17a5d4c3 | 47093 | Markdown (RE delivery report) | 1 | full text |
| 12 | 00_Spec/inputs/OD-S03_REPORT.md | a99481cad07731fd0c61536dbed077658c6a8c2990f76ed1a432611bbdf8e057 | 4089 | Markdown (RE delivery report, summary) | 1 | full text |
| 13 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP | — | listed and hashed only (intake rule 6); geometry measured later |
| 14 | 00_Spec/inputs/OD-C05_group_head_carrier.step | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | 186262 | STEP | — | listed and hashed only |
| 15 | 00_Spec/inputs/OD-C10_top_panel.step | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | 297471 | STEP | — | listed and hashed only |
| 16 | 00_Spec/inputs/OD-C11_back_panel.step | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | 236640 | STEP | — | listed and hashed only |
| 17 | 00_Spec/inputs/OD-E02_control_board.step | 4e570b4abc68a538efecbf89022738dd0e2527dcb466ceee9b721b353b005385 | 1869814 | STEP | — | listed and hashed only |
| 18 | 00_Spec/inputs/OD-S03_steam_knob.step | 8f1472d086e4d7bd9530976869d4ba97faef3e4af394718269431fbe8a263af5 | 598058 | STEP | — | listed and hashed only |
| 19 | 00_Spec/inputs/od_g01_assembly_C1_v03.step | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | 3455355 | STEP | — | listed and hashed only |
| 20 | 00_Spec/inputs/od_g01_housing_C1_v03.step | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | 437578 | STEP | — | listed and hashed only |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C01: plate outline, x | x −120 … +120 | mm | −120.00 … +120.00 | — | #5 | §4 C1 | text | — |
| X-02 | OD-C01: plate outline, z | z −305 … +100 | mm | −305.00 … +100.00 | — | #5 | §4 C1 | text | — |
| X-03 | OD-C01: plate thickness / y range | 6.0 thick, y −6.0 … 0 | mm | 6.00; −6.00 … 0.00 | — | #5 | §4 C1 | text | — |
| X-04 | OD-C01: top face level (floor plane) | y = 0 (the plate's top face) | mm | 0.00 | ± 0.10 (REQ-07) | #5 | §2, REQ-07 | text | — |
| X-05 | OD-C01: corner radii and centres | corners R 10 about (±110, −295) and (±110, +90) | mm | R 10.00 about (±110.00, −295.00) and (±110.00, +90.00) | — | #5 | §4 C1 | text | — |
| X-06 | OD-C01: machine frame definition | X to the user's right, +Y up, +Z toward the user (front); origin on the group head axis' vertical, on the floor plane; y = 0 is the plate's top face | — | — | — | #5 | §2 | text | — |
| X-07 | OD-C01: feet holes, front pair (z > 0) | four Ø3.4 through-holes at (x ±110.0, z +90.0) [and (x ±110.0, z −295.0), rear pair] | mm | Ø3.40 at (±110.00, +90.00) and (±110.00, −295.00) | ± 0.1 (REQ-05) | #5 | §4, §5 REQ-05 | text | — |
| X-08 | OD-C15 keep-out above each foot hole | a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) holds the screw head | mm | Ø8.00 × 2.00, y 0.00 … 2.00 | — | #3, #9 | CHASSIS_README "Keep-outs"; OD-C15 spec A-09 | text | — |
| X-09 | OD-C01: drip tray zone | the drip tray x ±75, z −15 … +85 on the plate under the mouth at (0, 32) | mm | x ±75.00, z −15.00 … +85.00, centre (0.00, 32.00) | — | #5 | §4 A-06 | text | flag: not scanned, assumption |
| X-10 | OD-C01: drip tray cup-rest top level | cup rest top ≤ 36.9 above the plate | mm | ≤ 36.90 | — | #5 | §4 A-06 | text | flag: not scanned, assumption |
| X-11 | OD-C01: reserved zone, water tank (rear, not front) | x ±70, z −305 … −250 | mm | x ±70.00, z −305.00 … −250.00 | — | #5 | §4 A-07 | text | — |
| X-12 | OD-C01: reserved zone, valve/flowmeter mount (left, not front) | x −117 … −67, z −154 … −35 | mm | x −117.00 … −67.00, z −154.00 … −35.00 | — | #5 | §4 A-05, A-17 | text | — |
| X-13 | OD-C01: reserved zone, electronics bay (right, not front) | x 70 … 120, z −240 … −30 | mm | x 70.00 … 120.00, z −240.00 … −30.00 | — | #5 | §4 A-08 | text | — |
| X-14 | OD-C01: machine height estimate | machine height ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet | mm | ≈ 260.00 | — | #5 | §6 A-16 | text | flag: not confirmed |
| X-15 | OD-C10: lid outline | x ±120.0, z −305.0 … +100.0, vertical corner edges R 10.0 (the plate's corners) | mm | x ±120.00, z −305.00 … +100.00, R 10.00 | ± 0.1 (REQ-02) | #7 | §4 C1 | text | — |
| X-16 | OD-C10: top skin | 3.0 thick, y 247.0 … 250.0 | mm | 3.00 thick, y 247.00 … 250.00 | — | #7 | §4 C1 | text | — |
| X-17 | OD-C10: skirt | 3.0 thick along the whole perimeter, from the skin down to y 215.0 (32.0 tall below the skin) | mm | 3.00 thick, to y 215.00, 32.00 tall | — | #7 | §4 C1 | text | — |
| X-18 | OD-C10: bulkhead screw columns | two, Ø12.0, at (x 65.0, z −60.0) and (x 65.0, z −210.0), from the skin's underside down to y 215.0 | mm | Ø12.00 at (65.00, −60.00) and (65.00, −210.00) | ± 0.1 (REQ-03) | #7 | §4 C1 | text | — |
| X-19 | OD-C10: back-panel screw columns | two, Ø12.0, at (x ±90.0, z −293.0), over the back panel's ledge inserts | mm | Ø12.00 at (±90.00, −293.00) | ± 0.1 (REQ-04) | #7 | §4 C1 | text | — |
| X-20 | OD-C10: column bore | each column: Ø3.4 through-hole on axis, Ø6.5 counterbore from top face y 250.0 down to y 218.0 | mm | Ø3.40 through; Ø6.50 counterbore to y 218.00 | ± 0.1 | #7 | §4 C1 | text | — |
| X-21 | OD-C10: rest pads | two, Ø10.0, at (x ±48.0, z 30.0), from the skin down to y 210.5 (0.5 above the carrier's top face) | mm | Ø10.00 at (±48.00, 30.00), to y 210.50 | ± 0.1 (REQ-05) | #7 | §4 C1 | text | — |
| X-22 | OD-C10: where the panels end / what rests on what (front and side edges) | "the lid's bottom edge meets the side, front and back panels at y 215"; the side panels OD-C12/C13 (outer faces x ±120) and the front panel OD-C09 (outer face z +100) are not designed and must reach y 215 under the skirt; until they exist the left and front edges are free | mm | y = 215.00 | — | #7 | §4 C1; §6 A-04 | text | flag: assumption, OD-C09 not yet designed |
| X-23 | OD-C10/keep-out: zone reserved for OD-C09, OD-C12, OD-C13 | "those panels end at y 215 under the lid's 3 mm skirt (x ±117 … ±120, z −305 … +100)" | mm | y = 215.00; x ±117.00 … ±120.00; z −305.00 … +100.00 | — | #3 | CHASSIS_README "Keep-outs for later parts" | text | — |
| X-24 | OD-C10: material and printer | PETG (BOM: ASA; a 240 × 405 lid warps in ASA on the open Kobra), density 1270 kg/m³, on the Kobra Max 3 | — | — | — | #7 | §3; §6 A-10 | text | flag: conflicts with BOM (see §4 gap) |
| X-25 | OD-C11: wall | 3.0 thick, z −302.0 … −299.0, x −116.0 … +116.0, from the plate y 0 up to y 215.0 | mm | 3.00 thick, z −302.00 … −299.00, x ±116.00, y 0.00 … 215.00 | ± 0.1 (REQ-02) | #8 | §4 C1 | text | — |
| X-26 | OD-C11: floor flanges | two, 4.0 thick, y 0 … 4.0, z −299.0 … −277.0 (22 deep), at x −104.0 … −72.0 and +72.0 … +104.0 | mm | 4.00 thick, y 0.00 … 4.00, z −299.00 … −277.00, x −104.00 … −72.00 / +72.00 … +104.00 | — | #8 | §4 C1 | text | — |
| X-27 | OD-C11: flange holes | two per flange, Ø3.4 through-holes along Y at (x ±81.0, z −282.0) and (x ±95.0, z −282.0) | mm | Ø3.40 at (±81.00, −282.00) and (±95.00, −282.00) | ± 0.1 (REQ-01) | #8 | §4 C1 | text | — |
| X-28 | OD-C11: gussets | two per flange, 4.0 thick, at its ends (x ±72.0 … ±76.0 and x ±100.0 … ±104.0); leg up the wall 30.0 (inner, top y 34) and 18.0 (outer, top y 22) | mm | 4.00 thick; legs 30.00 / 18.00 | — | #8 | §4 C1 | text | — |
| X-29 | OD-C11: top ledge | 4.0 thick, y 211.0 … 215.0, z −299.0 … −287.0 (12 deep), along x −114.0 … +114.0 | mm | 4.00 thick, y 211.00 … 215.00, z −299.00 … −287.00, x ±114.00 | — | #8 | §4 C1 | text | — |
| X-30 | OD-C11: insert bosses for OD-C10's rear screws | two, Ø4.0 × 6.0 blind bores along −Y from y 215.0 at (x ±90.0, z −293.0) | mm | Ø4.00 × 6.00, at (±90.00, −293.00) | ± 0.05 (REQ-07) | #8 | §4 C1 | text | — |
| X-31 | OD-C11: cord pass-through | one Ø12.0 hole through the wall at (x 95.0, y 30.0), for the mains cord OD-E06 in grommet OD-C14 | mm | Ø12.00 at (95.00, 30.00) | ± 0.1 (REQ-03) | #8 | §4 C1 | text | — |
| X-32 | OD-C11: tube pass-throughs | two Ø12.0 holes through the wall at (x −100.0, y 30.0) and (x −84.0, y 30.0) | mm | Ø12.00 at (−100.00, 30.00) and (−84.00, 30.00) | ± 0.1 (REQ-04) | #8 | §4 C1 | text | — |
| X-33 | OD-C11: vent slots | five, 4.0 wide × 80.0 tall, centres x 78.0, 86.0, 94.0, 102.0, 110.0, from y 100.0 to 180.0 | mm | 4.00 × 80.00, centres 78/86/94/102/110, y 100.00 … 180.00 | ± 0.1 (REQ-06) | #8 | §4 C1 | text | — |
| X-34 | OD-C11: print orientation | lying on the outer face z = −302 on the bed, build direction +Z | — | — | — | #8 | §4 C1; §6 A-08 | text | — |
| X-35 | OD-C11: material and printer | PETG (BOM: ASA; a 232 × 215 panel warps in ASA on the open Kobra; the panel is far from the heat), density 1270 kg/m³, on the Kobra Max 3 | — | — | — | #8 | §3; §6 A-10 | text | flag: conflicts with BOM (see §4 gap) |
| X-36 | OD-C11: wall standoff from the plate edges (a number a mirrored front panel would reuse) | the wall at z −302 … −299 stands 3 inside the rear edge (z −305), its ends 4 inside the side edges (x ±120, i.e. to x ±116) | mm | 3.00 inside the rear edge; 4.00 inside the side edges | — | #8 | §6 A-02 | text | — |
| X-37 | OD-C05/OD-C01: housing/carrier frame mapping to the machine frame | local x → X, local y → +Z, local z → −Y, origin at (0, 180.06, 32.0) | mm | origin (0.00, 180.06, 32.00) | — | #5, #6 | OD-C01 §4 A-01; OD-C05 §2 | text | — |
| X-38 | OD-G01/OD-C01: housing rear face in the machine frame | the housing's rear face (its local z −24.94) lies at y 205.0 | mm | 205.00 | — | #5 | §4 A-01 | text | — |
| X-39 | OD-G01/OD-C01: housing mouth face in the machine frame | the housing's mouth face (its local z +3.30) at y 176.76 | mm | 176.76 | — | #5 | §4 A-01 | text | — |
| X-40 | OD-C05: carrier's foot extent | the carrier's foot occupies x ±55, z −70 … −26 | mm | x ±55.00, z −70.00 … −26.00 | — | #5 | §4 A-01 | text | — |
| X-41 | OD-C05: carrier's wall and plate extent | the carrier's wall z −26 … −20 up to y 210; its plate z −26 … +82 at y 205 … 210 | mm | wall z −26.00 … −20.00 to y 210.00; plate z −26.00 … +82.00 at y 205.00 … 210.00 | — | #5 | §4 A-01 | text | — |
| X-42 | OD-G01: housing extent in the machine frame | the housing occupies x ±50, z −18 … +82 | mm | x ±50.00, z −18.00 … +82.00 | — | #5 | §4 A-01 | text | — |
| X-43 | OD-G10/OD-C05: portafilter spout height | the portafilter spouts hang to y ≈ 135.2 | mm | ≈ 135.20 | — | #6 | §4 C4; §6 A-03 | derived (rim on shelf + reach) | flag: derived, not caliper-confirmed |
| X-44 | OD-C05/SOURCING_GUIDE: mug rule | group head height ≥ 95 mm above the tray (SOURCING_GUIDE §6 rule 5); OD-C05's figure reads 98.3 while the tray's top stands ≤ 36.9 above the floor | mm | ≥ 95.00; actual ≈ 98.30 | — | #4, #6 | SOURCING_GUIDE §6 rule 5; OD-C05 §6 A-03 | text | — |
| X-45 | OD-G01: bayonet lug angular layout | three lugs of 54° span at 120° pitch, starts 336°, 96°, 216° (centre 3°) | deg | span 54.00°, pitch 120.00°, starts 336.00°/96.00°/216.00° | — | #10 | §4 C1 | text | flag: scan-derived (A-04), not caliper-confirmed |
| X-46 | OD-G01: stop block | over the first 5.76° of each lug, reaching down to z = −10.52 | deg, mm | 5.76° from lug start; z −10.52 | — | #10 | §4 C1 | text | flag: scan-derived (A-06) |
| X-47 | OD-G01: brew water condition near the housing | brew water at up to 125 °C and 15 bar reaches the gasket support inside the housing | °C, bar | 125.00 °C; 15.00 bar | — | #10 | §3 Environment | text | — |
| X-48 | SOURCING_GUIDE: thermal map near the housing/thermoblock | thermoblock and its 192 °C TCO stay clear of printed walls; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural | °C | 192.00 °C | — | #4 | §6 rule 3 | text | — |
| X-49 | OD-C05: thermoblock keep-out from the carrier | nothing of the carrier lies at machine z < −85 (housing y < −117); ≥ 10 mm air gap to the thermoblock | mm | ≥ 10.00 mm; machine z ≥ −85.00 | — | #6 | §4 REQ-07; §6 A-05 | text | — |
| X-50 | OD-E02: datum frame definition | origin = middle button collar axis ∩ back cover floor plane; primary plane = back cover floor (fit rms 0.0218 / max 0.0997); secondary axis = middle button collar (fit rms 0.0294 / max 0.0954); clock: +X end face of the housing rim/steps → +X, angle 111.4904° | mm, deg | rms 0.0218/max 0.0997; rms 0.0294/max 0.0954; 111.4904° | — | #11 | §4 | text | flag: scan-derived |
| X-51 | OD-E02: bounding box (datum frame) | max [38.16, 16.1729, 18.9511]; min [-38.6285, -37.4736, -29.2147]; size [76.7885, 53.6465, 48.1658] | mm | as given | — | #11 | §2 table | table | flag: scan-derived, fit-critical values not confirmable from a scan |
| X-52 | OD-E02: button cap B1 | ellipse [cx −26.5135, cy −4.7522, r1 5.9182, r2 6.3589, θ 13.7633°]; top_normal [−0.3412, −0.0601, −0.9381]; top_offset 31.9729 | mm, deg | as given | ± 0.0326 (ellipse), ± 0.0391 (top) | #11 | §5 params `cap_B1_*` | table (scan params) | flag: scan-derived, fit-critical, not confirmable from a scan |
| X-53 | OD-E02: button cap B2 (middle) | radius 6.3395; axis_dir [-0.0128, -0.009, 0.9999]; axis_xy0 [-0.2362, -0.2446]; top_normal [0.0103, 0.0055, -0.9999]; top_offset 29.1492 | mm | as given | ± 0.04 (r), ± 0.03 (axis), ± 0.0362 (top) | #11 | §5 params `cap_B2_*` | table (scan params) | flag: scan-derived, fit-critical, not confirmable from a scan; "the loose button cap itself sits 1.6 deg tilted in its bore" |
| X-54 | OD-E02: button cap B3 | ellipse [cx 26.5737, cy −5.2348, r1 5.934, r2 6.3955, θ −10.9268°]; top_normal [0.3498, -0.0781, -0.9336]; top_offset 32.1747 | mm, deg | as given | ± 0.0419 (ellipse), ± 0.0392 (top) | #11 | §5 params `cap_B3_*` | table (scan params) | flag: scan-derived, fit-critical, not confirmable from a scan |
| X-55 | OD-E02: screw hole L | position xy [-13.2349, -7.9445]; through radius 1.7688; counterbore radius 3.788; front top z −11.8357 | mm | as given | ± 0.03 (xy), ± 0.05 (through r), ± 0.03 (cb r), ± 0.3 (top z) | #11 | §5 params `screw_L_*` | table (scan params) | flag: scan-derived, fit-critical, not confirmable from a scan |
| X-56 | OD-E02: screw hole R | position xy [12.7485, -8.0013]; through radius 1.7206; counterbore radius 3.7418; front top z −12.4694 | mm | as given | ± 0.03 (xy), ± 0.05 (through r), ± 0.03 (cb r), ± 0.3 (top z) | #11 | §5 params `screw_R_*` | table (scan params) | flag: scan-derived, fit-critical, not confirmable from a scan |
| X-57 | OD-E02: screw counterbore floor level | screw_cb_floor_z = −2.9158 | mm | −2.9158 | ± 0.0265 | #11 | §5 params `screw_cb_floor_z` | table (scan params) | flag: scan-derived |
| X-58 | OD-E02: mounting tab | tab_hole [-0.218, -32.7639, 1.6428]; tab_end_y −37.4736; tab_top_plane [-0.0019, 0.0114, 0.9999, 18.5383]; tab_under_plane [0.0014, -0.0116, -0.9999, -16.0036]; tab_flange_bottom_z −1.9598 | mm | as given | ± 0.0325 (hole), ± 0.05 (end_y), ± 0.0225/0.02 (planes), ± 0.05 (flange z) | #11 | §5 params `tab_*` | table (scan params) | flag: scan-derived, fit-critical (hole), not confirmable from a scan |
| X-59 | OD-E02: latch hoop H1 | [-28.7075, -19.6107, -26.872, -21.4957, -3.4558, 4.688, -20.3633]; ramp_plane [0.0056, -0.7617, 0.6479, 12.8228] | mm | as given | ± 0.08 (hoop), ± 0.0559 (ramp) | #11 | §5 params `hoop_H1*` | table (scan params) | flag: scan-derived |
| X-60 | OD-E02: latch hoop H2 | [19.2954, 28.3688, 21.0902, 26.4221, -2.5416, 4.7268, -20.3846]; ramp_plane [0.0681, 0.8036, -0.5913, -12.589] | mm | as given | ± 0.08 (hoop), ± 0.0658 (ramp) | #11 | §5 params `hoop_H2*` | table (scan params) | flag: scan-derived |
| X-61 | OD-E02: latch hoop H3 | [-20.7166, -11.687, -18.9135, -13.5487, -2.6655, 4.6764, 16.1729]; ramp_plane [0.0023, 0.4089, 0.9126, 3.2873] | mm | as given | ± 0.08 (hoop), ± 0.0316 (ramp) | #11 | §5 params `hoop_H3*` | table (scan params) | flag: scan-derived |
| X-62 | OD-E02: latch hoop H4 | [19.3352, 28.3032, 21.1156, 26.4588, -3.0193, 4.7127, 8.7329]; ramp_plane [0.0117, 0.3336, 0.9426, -0.3117] | mm | as given | ± 0.08 (hoop), ± 0.0309 (ramp) | #11 | §5 params `hoop_H4*` | table (scan params) | flag: scan-derived |
| X-63 | OD-E02: hoop bottom level | hoop_bottom_z = −5.5662 | mm | −5.5662 | ± 0.0265 | #11 | §5 params `hoop_bottom_z` | table (scan params) | flag: scan-derived |
| X-64 | OD-E02: report limitation L1 | "Scan-only: no calipers, so Tier-1 did not run (absent, not passed) and absolute scale is not caliper-verified" | — | — | — | #11 | §11 L1 | text | flag: scan-only, scale not caliper-verified |
| X-65 | OD-E02: report limitation L2 | "Unscanned regions are modelled from assumptions: connector shroud interior depth, shroud-to-rim slot floor, screw through-bores, cap-collar recess ceilings" accepted by the owner | — | — | — | #11 | §11 L2 | text | flag: assumed geometry in unscanned regions |
| X-66 | OD-E02: delivery verdict | `BAND_NOT_MET`; accepted by Ikbal (owner, question card), 2026-09-28; "Not fit for: manufacture or tooling of any part of the assembly until the functional interfaces (caps, collars, screw holes, tab hole, connector shroud) are calipered" | — | — | — | #11 | header; §13 | text | — |
| X-67 | OD-S03: what it is | steam-valve knob: chrome cap with lever and drafted slot pocket, chrome collar, white four-rib stem, chrome threaded sleeve with splined bore | — | — | — | #12 | header table | text | — |
| X-68 | OD-S03: size (bounding box, datum frame) | datum bbox 40.96 × 26.44 × 38.10 mm; volume 11 655.6 mm³; 83 faces, 1 valid closed solid | mm, mm³ | 40.96 × 26.44 × 38.10; 11655.60 | — | #12 | "Delivered STEP" section | text | flag: scan-derived |
| X-69 | OD-S03: how it mounts | threaded sleeve with splined bore (chrome); "confirm with calipers: sleeve thread OD and pitch, bore Ø and spline count, cap OD, overall height" before designing the front panel / steam-knob opening | — | — | — | #12 | "Deviation gate" notes | text | flag: not caliper-confirmed, explicitly flagged by the source as needing calipers |
| X-70 | OD-S03: phase | "Phase 2 part (steam system is not in v1)" | — | — | — | #12 | "Deviation gate" notes | text | — |
| X-71 | OD-S03: frame | datum: cap crown face = Z 0 (+Z toward the sleeve), origin on the sleeve/cap axis, lever toward +X | — | — | — | #12 | "Delivered STEP" table | text | — |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-72 | Material standing instruction: PLA for now, project-wide | "all printed in pla for now" | #1 | REQUEST.md, the Usta's answer 2026-10-02 22:58 UTC |
| X-73 | OD-C09 BOM row (material, process, qty, status) | `OD-C09,OD-C00,PRINT,Front panel with button bezel,,,1,DESIGN,ASA,printed,print,#8,proposed` | #2 | bom_rows.csv row "OD-C09" |
| X-74 | Hand-over scope and axis decision | "design OD-C09 and OD-T01; both were blocked on OD-G01, which the Usta has now accepted; material PLA for now; the group head stands vertical, mouth down" | #1 | REQUEST.md, coordinator hand-over 2026-10-02 22:59 UTC |
| X-75 | Chassis order-of-work entry for OD-C09 | "`OD-C09` front panel with button bezel \| OD-G01 mouth, OD-E02 buttons, OD-S03 knob (phase 2) \| —" | #3 | CHASSIS_README.md, "Order of work" table, row 10 |
| X-76 | Thermal rule (process/material near heat) | "Thermoblock and its 192 °C TCO stay clear of printed walls; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #4 | SOURCING_GUIDE_s6.md §6 rule 3 |
| X-77 | Serviceability rule | "Serviceability is the point. […] top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #4 | SOURCING_GUIDE_s6.md §6 rule 4 |
| X-78 | Mug rule / envelope limit | "Design for the mug. Group head height ≥ 95 mm above tray […]; keep the 0.4 m³ envelope limit from the thesis spec." | #4 | SOURCING_GUIDE_s6.md §6 rule 5 |
| X-79 | Anti-vibration rule | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #4 | SOURCING_GUIDE_s6.md §6 rule 2 |
| X-80 | Safety spec (piping/TCO/PAT/RCD) | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #4 | SOURCING_GUIDE_s6.md §6 rule 7 |
| X-81 | Two-zone layout rule | "Two-zone layout. Wet zone […] physically separated from the electric zone […]: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #4 | SOURCING_GUIDE_s6.md §6 rule 1 |
| X-82 | Side-panel material decision (context for OD-C09's neighbours) | "3/ printed" (answering "acrylic or printed side panels (decides C12, C13, C16)") | #1 | REQUEST.md, the Usta's answer 2026-10-02 22:58 UTC |
| X-83 | OD-G01 acceptance (unblocks this job) | "2/ accept" (answering "the OD-G01 card: accept, another round, or stop") | #1 | REQUEST.md, the Usta's answer 2026-10-02 22:58 UTC |
| X-84 | Standing instruction on process | "Usta'ya yalnız karar gereken yerde sor; açık soruları `A-##` satırı olarak ledger'a yaz ve ilerle." | #1 | REQUEST.md, standing project instruction |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-72, X-73 | The Usta's standing answer says "all printed in pla for now," but `bom_rows.csv` lists OD-C09's material as ASA (status "proposed," unchanged since the PLA instruction): does OD-C09 print in PLA (as OD-C01/C05/C10/C11/C15 were specified, each overriding their own BOM row of ASA/PETG) or ASA? |
| 2 | X-09, X-10 | The drip tray (OD-C21/C22) is not scanned; its real footprint and cup-rest height are assumptions carried by OD-C01 (A-06). What is the drip tray's real size, so the front panel's lower edge and any tray-facing clearance can be set? |
| 3 | X-22, X-23 | OD-C12/OD-C13 (side panels) are not yet designed; only their notional outer face (x ±120, inside to ±117 under the lid) and OD-C01's plate edge are known. What is the side panels' actual wall position, so OD-C09's side edges and their joint to the side panels can be set? |
| 4 | X-22, X-23, X-72 | No input states how OD-C09 is fixed to the base frame OD-C01 (screws, inserts, a slot, or another method) or whether it is meant to be removable like OD-C10/OD-C11 (4 screws each, X-77). How is the front panel fixed to the plate? |
| 5 | X-50 … X-66 | OD-E02 (the button board) is delivered as one fused scan solid with a verdict of `BAND_NOT_MET`, accepted by the owner only for "envelope, packaging and fit studies," not for fit-critical or tooling use. No input states where in the front panel the board sits (position, orientation, depth) or how it is held (snap, screws into the bezel, a carrier). Where does the button board sit and how is it held? |
| 6 | X-42, X-45, X-46 | The portafilter OD-G10 locks into the housing OD-G01 from below and its handle reaches out through the front panel's opening, but no input gives the handle's position, length, or its swept arc as it is inserted/locked/removed. What is the portafilter handle's sweep through the front, so the panel's cut-out can clear it? |
| 7 | X-67 … X-71 | OD-S03 (steam knob) is explicitly phase 2, and its report itself asks for caliper confirmation (sleeve thread OD/pitch, bore Ø, spline count, cap OD, overall height) "before designing the front panel / steam-knob opening." Where does the steam knob sit in/through the front panel, and is a phase-2 placeholder opening wanted now or deferred entirely? |
| 8 | X-73, X-76, X-78, X-80 | The project's material/process rule reads "PLA nowhere structural," yet the hand-over (X-72, X-74) sets PLA for every printed part "for now," and OD-C09 sits near the group head housing OD-G01, which itself carries brew water up to 125 °C / 15 bar (X-47) with a 192 °C thermoblock TCO nearby (X-48, X-76). Is PLA acceptable this close to the group head's heat, or does OD-C09 need a different material from the rest of the chassis? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None.
