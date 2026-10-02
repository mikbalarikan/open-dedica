# INTAKE v01 — 20261002-od-c12-c13-c16-side-panels

Intake: Claude Sonnet 5, Claude Code · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-10-02 UTC

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
| 1 | 00_Spec/inputs/REQUEST.md | 131baace66871acea0a7732fb0cb33b8dc1c2f1893f426a8dd4a41f7ff843134 | 1715 | Markdown | 1 | every line |
| 2 | 00_Spec/inputs/bom_rows.csv | e30b9e2d6cfa76fdddc81c823a7022ae18eefea50de7cc808a60936c756e8633 | 1225 | CSV | 12 rows | every row |
| 3 | 00_Spec/inputs/CHASSIS_README.md | ac5e9383209553c87b271dfc55c0776d75dfc25899dbf176afdd5668a2603443 | 8917 | Markdown | 1 | every line |
| 4 | 00_Spec/inputs/SOURCING_GUIDE_s6.md | 7c5705ead4480fa954c9646e6f78f6241a55a78f85dfb0bee439f0bc5844bb21 | 1541 | Markdown | 1 | every line |
| 5 | 00_Spec/inputs/C08_C11_integration_notes.md | 85a428546e502993bccaa3e5c26280a41517d61cfcb4af3f4d673c2747e83044 | 5141 | Markdown | 1 | every line |
| 6 | 00_Spec/inputs/C15_integration_notes.md | b6a6e77dfdfa05e9a1b666c83a4fcabde0331be80bb9ebb1d4a30bba59649d3b | 3193 | Markdown | 1 | every line |
| 7 | 00_Spec/inputs/OD-C01_DESIGN_SPEC.md | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | 25226 | Markdown | 1 (§1…§8) | every line |
| 8 | 00_Spec/inputs/OD-C07_DESIGN_SPEC.md | 33ff74a908766d31ec66d1a291d3d31c971173c3555461d03aaa01e568c95ce9 | 28353 | Markdown | 1 (§1…§8) | every line |
| 9 | 00_Spec/inputs/OD-C08_DESIGN_SPEC.md | 5b559450a15d3ba56badbcd51d47b76caa9d1bd3f23199995378a976a18fd8f3 | 21127 | Markdown | 1 (§1…§8) | every line |
| 10 | 00_Spec/inputs/OD-C10_DESIGN_SPEC.md | e2eda540dd141c27a3ca8f7a84f2d05cfbf99a1d8df283c03bff28000c4ee966 | 21802 | Markdown | 1 (§1…§8) | every line |
| 11 | 00_Spec/inputs/OD-C11_DESIGN_SPEC.md | 6da33456e123942bb92e7419ff190f6e01522b0580d36d510fa9c5eee6d61245 | 22734 | Markdown | 1 (§1…§8) | every line |
| 12 | 00_Spec/inputs/OD-C15_DESIGN_SPEC.md | a24c23f25b2f02b916d89beb76e3db5c899d02d518c3775c402b5ed27e0e496f | 16838 | Markdown | 1 (§1…§8) | every line |
| 13 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP | — | listed and hashed only (intake rule 6); geometry measured later by `tools/measure` |
| 14 | 00_Spec/inputs/OD-C02_bulkhead.step | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | 150003 | STEP | — | listed and hashed only |
| 15 | 00_Spec/inputs/OD-C05_group_head_carrier.step | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | 186262 | STEP | — | listed and hashed only |
| 16 | 00_Spec/inputs/OD-C07_valve_flowmeter_mount.step | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | 386750 | STEP | — | listed and hashed only |
| 17 | 00_Spec/inputs/OD-C08_electronics_bay_tray.step | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 | 171518 | STEP | — | listed and hashed only |
| 18 | 00_Spec/inputs/OD-C10_top_panel.step | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | 297471 | STEP | — | listed and hashed only |
| 19 | 00_Spec/inputs/OD-C11_back_panel.step | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | 236640 | STEP | — | listed and hashed only |
| 20 | 00_Spec/inputs/OD-C15_foot.step | 830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7 | 52248 | STEP | — | listed and hashed only |

Note: no `OD-C02_DESIGN_SPEC.md` or `OD-C05_DESIGN_SPEC.md` is among the inputs
(only their STEPs). Every OD-C02 and OD-C05 dimension below is as quoted inside
the OD-C01, OD-C10, OD-C11 or OD-C08 specs (text), not read from an OD-C02 or
OD-C05 spec of their own.

## §2 Dimensions

All values are in the OD-C01 machine frame (X right, +Y up, +Z toward the user/
front, plate top face y = 0) unless the "What" cell says otherwise. Every row is
a design value from a RATIFIED spec or a BOM/README row; none is scan-measured
and none is confirmed by the Usta (rule 5). No STEP geometry is reported here
(rule 6): geometry rows below are text values quoted from the markdown specs
that describe the STEPs.

### OD-C01 base frame

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | Plate outline | x ±120, z −305 … +100, corners R 10 about (±110, −295) and (±110, +90) | mm | x ±120.0, z −305.0 … +100.0, R10.0 | ±0.1 (U-02) | #7 | §4 C1, §5 U-02 | drawing callout (spec text) | — |
| X-02 | Plate thickness and y-levels | 6.0 thick, y −6.0 … 0 | mm | 6.00, y −6.0 … 0.0 | ±0.1 (REQ-07) | #7 | §4 C1, §2 frame, §5 REQ-07 | text | — |
| X-03 | Plate top face (floor plane) | y = 0 | mm | 0.00 | ±0.10 (REQ-07) | #7 | §5 REQ-07 | text | — |
| X-04 | Feet holes | four Ø3.4 through-holes at (x ±110.0, z +90.0) and (x ±110.0, z −295.0) | mm | Ø3.4; (±110.0, +90.0), (±110.0, −295.0) | ±0.1 Ø, offset ≤0.10 (REQ-05) | #7 | §4 C1, §5 REQ-05 | text | — |
| X-05 | Drain holes | two Ø8.0 through-holes at (x −80.0, z −120.0) and (x −80.0, z −230.0) | mm | Ø8.0; (−80.0, −120.0), (−80.0, −230.0) | ±0.1 Ø, offset ≤0.10 (REQ-06) | #7 | §4 C1, §5 REQ-06 | text | — |
| X-06 | Bulkhead line insert holes (OD-C02 foot, |x|=65≥60) | four Ø4.0 through-holes at (x 65.0, z −45.0), (65.0, −105.0), (65.0, −165.0), (65.0, −225.0) | mm | Ø4.0; z −45.0 / −105.0 / −165.0 / −225.0 at x 65.0 | ±0.05 Ø, offset ≤0.10 (REQ-04) | #7 | §4 C1 A-04, §5 REQ-04 | text | — |
| X-07 | OD-C07 valve-mount insert holes | four Ø4.0 through-holes at (x −113.0, z −42.0), (x −71.0, z −42.0), (x −113.0, z −148.5), (x −71.0, z −148.5) | mm | Ø4.0; (−113.0,−42.0), (−71.0,−42.0), (−113.0,−148.5), (−71.0,−148.5) | ±0.05 Ø, offset ≤0.10 (REQ-10) | #7 | §4 C1 A-17, §5 REQ-10 | text | — |
| X-08 | OD-C08 electronics-bay insert holes (not yet in the OD-C01 STEP) | eight **new** M3 heat-set inserts, Ø4.0 × 6 blind bores from the top (−Y axis): OD-C08 flange at (x 88, z −222), (106, −222), (88, −78), (106, −78) | mm | Ø4.0 × 6.0; (88,−222), (106,−222), (88,−78), (106,−78) | — | #5 | "OD-C01 change needed" | text | not in delivered OD-C01 STEP; a handed-over OD-C01 spec change |
| X-09 | OD-C11 back-panel insert holes (not yet in the OD-C01 STEP) | OD-C11 flanges: (±81, −282), (±95, −282) | mm | Ø4.0 × 6.0; (±81,−282), (±95,−282) | — | #5 | "OD-C01 change needed" | text | not in delivered OD-C01 STEP; a handed-over OD-C01 spec change |
| X-10 | New-insert geometry rule | each of the eight new inserts ≥ 6 from every existing hole and ≥ 8 from the edge; the plate is 6 thick, so a 6 deep bore from the top reaches the underside: OD-C01 revision decides through vs blind | mm | ≥6.0 hole-to-hole, ≥8.0 to edge, plate 6.0 thick | — | #3, #5 | CHASSIS_README "Interfaces to OD-C01"; C08_C11 notes | text | unresolved (through vs blind), see §4 |
| X-11 | Insert pattern as built (OD-C01 frame, x/z) — OD-C07 | x ±113, −71; z −42, −148.5 | mm | matches X-07 | — | #3 | CHASSIS_README table | text | — |
| X-12 | Insert pattern as built — OD-C08 (new, not in plate STEP yet) | x 88, 106; z −222, −78 | mm | matches X-08 | — | #3 | CHASSIS_README table | text | — |
| X-13 | Insert pattern as built — OD-C11 (new, not in plate STEP yet) | x ±81, ±95; z −282 | mm | matches X-09 | — | #3 | CHASSIS_README table | text | — |
| X-14 | Insert type and bore (project standard) | M3 heat-set inserts (OD-F01), Ø4.0 bore | mm | Ø4.0 | — | #7 | §2 interfaces table | text | — |
| X-15 | Insert length/depth assumption | M3 × 5.7 × Ø4.6 heat-set inserts in Ø4.0 through-holes of the 6.0 plate, driven from the top; screw tips may reach 0.3 below the plate | mm | 5.7 long, Ø4.6 OD | — | #7 | §6 A-11 | text | unconfirmed assumption (A-11, OPEN) |
| X-16 | OD-C07 insert bore spec (mount side, reused figure) | hole Ø4.0, depth 5.7, insert length 5.7 | mm | Ø4.0, depth 5.7 | — | #8 | §6 A-13 | text | unconfirmed assumption |
| X-17 | OD-C08 insert bore | Ø4.0 ± 0.05, depth 6.0 ± 0.1 (≥5.7) | mm | Ø4.0, depth 6.0 | ±0.05 Ø / ±0.1 depth | #9 | §5 D-05b | text | — |
| X-18 | OD-C11 insert bore | two Ø4.0 ± 0.05 blind bores, depth 6.0 ± 0.1 (≥5.7) | mm | Ø4.0, depth 6.0 | ±0.05 Ø / ±0.1 depth | #11 | §5 D-05b | text | — |
| X-19 | Plate material | PETG (BOM says ASA; the large flat plate prints in PETG on the open Kobra) | — | — | — | #7 | §3, §6 A-10 | text | unconfirmed assumption; BOM conflicts (X-55) |
| X-20 | Plate density | 1270 kg/m³ | kg/m³ | 1270 | — | #7 | §3 | text | — |
| X-21 | Printer / machine profile | machines/anycubic-kobra-max-3.toml | — | — | — | #7 | §3 | text | — |
| X-22 | Build volume figure (assumption, not in the machine file) | 420 × 420 × 500 (Anycubic specification) | mm | 420 × 420 × 500 | — | #7 | §6 A-09 | text | unconfirmed assumption (A-09, OPEN) |

### OD-C10 top panel

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-23 | Outline | x ±120.0, z −305.0 … +100.0, vertical corner edges R 10.0 about (±110,−295) and (±110,+90) | mm | x ±120.0, z −305.0…+100.0, R10.0 | ±0.1 (REQ-02) | #10 | §4 C1, §5 REQ-02 | text | — |
| X-24 | Top skin level and thickness | top face y 250.00 ± 0.10, skin 3.0 ± 0.1 thick (underside y 247.0) | mm | y 250.0 top skin, 3.0 thick, underside y 247.0 | ±0.1 | #10 | §4 C1, §5 REQ-01 | text | — |
| X-25 | Skirt thickness and bottom level | skirt 3.0 thick all round, bottom face y 215.00 ± 0.10 | mm | 3.0 thick, y 215.0 | ±0.1 | #10 | §4 C1, §5 REQ-02 | text | — |
| X-26 | Bulkhead screw columns | two Ø12.0 ± 0.1 columns at (x 65.0, z −60.0) and (65.0, −210.0); bottoms y 215.00 ± 0.05; Ø3.4 through-hole; Ø6.5 counterbore from y 250.0 to y 218.0 ± 0.1 | mm | Ø12.0; (65,−60),(65,−210); Ø3.4; Ø6.5, y250→218 | ±0.1 / ±0.05 | #10 | §5 REQ-03 | text | — |
| X-27 | Back-panel screw columns | two Ø12.0 ± 0.1 columns at (x ±90.0, z −293.0); same hole/counterbore as X-26 | mm | Ø12.0; (±90,−293) | ±0.1 | #10 | §5 REQ-04 | text | — |
| X-28 | Column ribs | each column tied into the skin by two ribs 3.0 thick; the rear two columns also tied into the rear skirt | mm | 3.0 thick, ×2 ribs per column | — | #10 | §4 C1, §5 E-06 | text | — |
| X-29 | Rest pads | two Ø10.0 ± 0.1 pads at (x ±48.0, z 30.0), bottoms y 210.50 ± 0.05; clearance to OD-C05 0.50 ± 0.05; ≥10 from the hub window edge, ≥20 from the housing-screw counterbores | mm | Ø10.0; (±48,30); y210.5; clearance 0.50 | ±0.1 / ±0.05 | #10 | §5 REQ-05 | text | — |
| X-30 | F1 finding (centre of mass, rest pad) | the lid's centre of mass is 24 mm outside its four-column polygon on −X, so it settles onto the −X rest pad (0.5 over OD-C05) until the side panels carry its edges | mm | 24 mm outside, on −X | — | #10 | §6 A-04; also #3 CHASSIS_README "Keep-outs for later parts" | text | design finding (RV01 F1), not a specified dimension |
| X-31 | What the lid expects of the side panels (A-04) | the lid is held at four columns (x 65, z −293 area); its skirt's bottom edge at y 215 meets the side panels OD-C12/C13 (outer faces x ±120) and the front panel OD-C09 (outer face z +100), which must reach y 215 under the skirt; until they exist the left and front edges are free | mm | skirt bottom y 215, side-panel outer face x ±120 | — | #10 | §6 A-04 | text | unconfirmed assumption (A-04, OPEN); matches REQUEST.md and CHASSIS_README keep-out wording |
| X-32 | Lid's side/front edges free until panels exist (same finding, project-level wording) | OD-C10's side and front edges are free until OD-C09, OD-C12 and OD-C13 exist: those panels end at y 215 under the lid's skirt (x ±117 … ±120, z −305 … +100) | mm | y 215; x ±117…±120; z −305…+100 | — | #3, #5, #1 | CHASSIS_README "Keep-outs for later parts"; C08_C11 notes "Interfaces and keep-outs"; REQUEST.md | text | — |
| X-33 | Headroom over the carrier | skin underside y 247.0 leaves 37.0 above the carrier's plate (y210) for the hot water tube's loop | mm | 37.0 | — | #10 | §4 C1, §5 REQ-06 | text | — |
| X-34 | Lid envelope / print orientation | envelope 240.0 × 39.5 × 405.0 (x ±120, y 210.5 … 250.0, z −305 … +100); printed upside down, build direction −Y | mm | 240.0 × 39.5 × 405.0 | ±0.1 (U-02) | #10 | §4 C1, §5 U-02 | text | — |

### OD-C11 back panel

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-35 | Wall plane and extent | outer face z −302.00 ± 0.10, inner face z −299.00 ± 0.10, x ±116.0 ± 0.1 | mm | z −302.0 (outer), −299.0 (inner); x ±116.0 | ±0.1 | #11 | §2 frame, §5 REQ-02 | text | — |
| X-36 | Wall height | from the plate y 0 up to y 215.0 (the bulkhead's height) | mm | y 0 … 215.0 | — | #11 | §4 C1 | text | — |
| X-37 | Floor flanges | two, 4.0 thick, y 0 … 4.0, z −299.0 … −277.0 (22 deep), at x −104.0 … −72.0 and +72.0 … +104.0 | mm | 4.0 thick; y0…4.0; z−299…−277; x−104…−72 / 72…104 | — | #11 | §4 C1 | text | — |
| X-38 | Flange holes | four Ø3.4 ± 0.1 through-holes along Y at (x ±81.0, z −282.0) and (x ±95.0, z −282.0), 4.0 ± 0.1 long | mm | Ø3.4; (±81,−282),(±95,−282); 4.0 long | ±0.1 | #11 | §5 REQ-01 | text | — |
| X-39 | Gussets | two per flange, 4.0 thick, at x ±72.0…±76.0 and x ±100.0…±104.0; inner gussets 30.0 leg up the wall (top y 34), outer gussets 18.0 leg (top y 22, revised in 1.2 from 30.0) | mm | 4.0 thick; legs 16.0 (flange top) × 30.0 or 18.0 (wall) | — | #11 | §4 C1 | text | revised across builds (1.1→1.2), see X-50 conflict |
| X-40 | Top ledge | 4.0 thick, y 211.0 … 215.0, z −299.0 … −287.0 (12 deep), x −114.0 … +114.0 | mm | 4.0 thick; y211…215; z−299…−287; x−114…114 | — | #11 | §4 C1 | text | — |
| X-41 | Insert bosses / OD-C10 insert bores | two, blocks x ±(84.0…96.0), y 203.0…211.0, z −299.0…−287.0; each Ø4.0 × 6.0 blind bore along −Y from y 215.0 at (x ±90.0, z −293.0) | mm | Ø4.0 × 6.0; (±90,−293) | ±0.05 Ø, offset ≤0.10 (REQ-07) | #11 | §5 REQ-07 | text | — |
| X-42 | Cord pass-through | one Ø12.0 ± 0.1 hole through the wall along Z at (x 95.0, y 30.0) | mm | Ø12.0; (95,30) | ±0.1, offset ≤0.10 | #11 | §5 REQ-03 | text | — |
| X-43 | Tube pass-throughs | two Ø12.0 ± 0.1 holes through the wall along Z at (x −100.0, y 30.0) and (x −84.0, y 30.0) | mm | Ø12.0; (−100,30), (−84,30) | ±0.1, offset ≤0.10 | #11 | §5 REQ-04 | text | — |
| X-44 | Vents | five slots 4.0 ± 0.1 × 80.0 ± 0.1 through the wall, centres x 78/86/94/102/110, y 100.0…180.0, ends R2.0 | mm | 4.0 × 80.0; x 78,86,94,102,110; y100…180 | ±0.1 | #11 | §5 REQ-06 | text | — |
| X-45 | Feet-hole margin (wall-foot clearance) | the wall's foot stands 2.300 from the feet holes' rims by §4's geometry (v02 REPORT); U-03 requires ≥ 2.0 | mm | 2.300 | ≥2.0 (U-03) | #11, #5 | §5 U-03 (1.2); C08_C11 notes "Interfaces and keep-outs" | text | this is a built/measured-from-CAD value reported in the spec text, not confirmed by the Usta |
| X-46 | Feet-hole margin (same finding, duplicate wording) | OD-C11's wall foot stands 2.3 from the rims of OD-C01's feet holes at (±110, −295): OD-C15's screw heads (Ø5.7) clear the wall by 1.15; the C15 keep-out cylinder (Ø8 × 2 above each hole) touches the wall's inner face (z −299) at 0.0 without overlap | mm | 2.3; screw-head clearance 1.15; keep-out touches at 0.0 | — | #5 | "Interfaces and keep-outs for later parts" | text | — |
| X-47 | Envelope / print orientation | envelope 232.0 × 215.0 × 25.0 (x ±116, y 0…215, z −302…−277); printed lying on the outer face, build direction +Z | mm | 232.0 × 215.0 × 25.0 | ±0.1 (U-02) | #11 | §4 C1, §5 U-02 | text | — |
| X-48 | Joint with side panels (A-12) | the top panel's skirt (outer z −305) closes over the wall's top; the side panels OD-C12/C13 meet the wall's ends at x ±116 (not designed) | mm | wall ends x ±116 | — | #11 | §6 A-12 | text | unconfirmed assumption (A-12, OPEN) |
| X-49 | Plate edge and corners at the back-panel line (A-02) | the delivered plate: rear edge z −305, corners R 10 about (±110, −295) (at x ±116 the edge lies at z −303.0); the wall at z −302…−299 stands 3 inside the rear edge, its ends 4 inside the side edges, leaving the strip for the side panels and their corners | mm | edge z −303.0 at x±116; wall 3 inside rear edge, 4 inside side edges | — | #11 | §6 A-02 | text | unconfirmed assumption (A-02, OPEN); explicitly flagged by OD-C11 as a question for the side-panel job |

### OD-C07 valve and flowmeter mount

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-50 | Joint into the OD-C01 machine frame | local x → −Z, y → −X, z → +Y (a proper rotation), origin at (−92, 0, −60) | mm | origin (−92, 0, −60) | — | #7 (A-17) and #8 (§2 implicit) | OD-C01 §4 A-17; OD-C07 §1 intent | text | — |
| X-51 | Mount envelope (own frame) | 119 × 50 × 48 (x −25…94, y ±25, z 0…48 in the mount's own frame) | mm | 119 × 50 × 48 | ±0.1 (U-02) | #8 | §4 C1, §5 U-02 | text | — |
| X-52 | Mount footprint/zone in the machine frame | footprint holes land at (x −113, z −42), (x −71, z −42), (x −113, z −148.5), (x −71, z −148.5); envelope occupies x −117…−67, z −154…−35, up to y 48 | mm | x −117…−67, z −154…−35, y ≤48 | — | #7 | §4 C1, A-17 | text | — |
| X-53 | Reserved zone per OD-C01 A-05 | OD-C07 within x −117 … −67, z −154 … −35, on the pump's outlet side | mm | x −117…−67, z −154…−35 | — | #7 | §4, §6 A-05 | text | matches X-52; cited twice (A-05 and A-17) in the same spec |
| X-54 | OPV reachability requirement | no mount material above z 48.1; none within r 12 of the valve axis above the deck top; the drive tube top sits at z 61.7 in the open (mount frame) | mm | z ≤48.1; r12; drive-tube top z 61.7 | — | #8 | §5 REQ-08 | text | relevant to side-panel/bracket keep-out near the OPV access path (reachable with the top panel off) |

### OD-C08 electronics bay tray

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-55 | Envelope in the machine frame | 39.0 × 92.0 × 160.0 (x 73.0 … 112.0, y 0.0 … 92.0, z −230.0 … −70.0) | mm | x 73…112, y0…92, z−230…−70 | ±0.1 (U-02) | #9 | §4 C1, §5 U-02 | text | — |
| X-56 | Occupied zone with the board (to the side-panel side) | OD-C08 occupies x 73 … 112, z −230 … −70, y 0 … 92 (with the board, to x ≈ 109.3) | mm | x≈109.3 with board | — | #5, #3 | C08_C11 notes "Interfaces and keep-outs"; CHASSIS_README | text | the OD-C08 spec itself gives 109.26 (X-57) |
| X-57 | Board heatsink reach (tallest part) | the tallest part (the heatsink, 25.262 above the board) reaching x 109.26 | mm | 109.26 | — | #9 | §4 C1 A-03 | text | scan-derived (OD-E01), not confirmed by calipers |
| X-58 | Flange inserts | four Ø3.4 through-holes along Y at (x 88.0, z −222.0), (x 106.0, z −222.0), (x 88.0, z −78.0), (x 106.0, z −78.0), for M3 × 8 screws into four new M3 inserts in OD-C01 | mm | Ø3.4; (88,−222),(106,−222),(88,−78),(106,−78) | offset ≤0.10 (REQ-01) | #9 | §4 C1, §5 REQ-01 | text | duplicates X-08/X-12; cited again here from OD-C08's own spec |
| X-59 | Zone-limit assumption toward the side panel (A-06) | the board within x 70 … 117 (**a side panel's inner face assumed at x ≥ 117**), z −240 … −30, ≥ 10 above the plate | mm | x 70…117 assumed inner face ≥117 | — | #9 | §6 A-06 | text | unconfirmed assumption (A-06, OPEN); directly names the side panel's assumed inner face |
| X-60 | Print orientation / envelope on the bed | lying on the wall's outer face (x 73 on the bed), build direction +X; on the bed 92 × 160, 39 tall | mm | 92 × 160 on bed, 39 tall | — | #9 | §4 C1 | text | — |

### OD-C15 feet

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-61 | Foot positions (machine frame) | joint origins (±110.0, −6.0, +90.0) and (±110.0, −6.0, −295.0); foot x → X, y → +Z, z → −Y | mm | (±110, −6, +90), (±110, −6, −295) | — | #12 | §2 frame | text | — |
| X-62 | Screw-head keep-out (A-09) | a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) holds the screw head (Ø5.7 × 1.65); handed to OD-C12, OD-C13, OD-C16 and OD-C06 | mm | Ø8.0 × 2.0; screw head Ø5.7 × 1.65 | — | #12 | §6 A-09 | text | explicitly named as a keep-out for this job's parts |
| X-63 | Same keep-out (duplicate wording) | OD-C01 A-09: a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) holds the screw head. OD-C11's wall foot clears it by 0.0 (touching, no overlap); OD-C12, OD-C13, OD-C16 and OD-C06 must leave it free | mm | Ø8.0 × 2.0; clearance 0.0 at OD-C11 | — | #3, #1 | CHASSIS_README "Keep-outs for later parts"; REQUEST.md | text | — |
| X-64 | Foot joint / counter level | counter face at y −16.0: the whole machine stands 16 mm above the counter at the plate top | mm | y −16.0 | — | #12 | §2 frame | text | — |
| X-65 | Foot envelope | Ø18.0 × 10.0 (body cylinder) | mm | Ø18.0 × 10.0 | ±0.1 (REQ-04) | #12 | §4 C1, §5 REQ-04 | text | — |
| X-66 | Screw and nut envelope (foot frame) | screw: head on y 0 … 1.65 at (±110, ±z), tip at y −12.0; nut: foot z 2.5 … 4.9 (y −8.5 … −10.9) | mm | head y0…1.65; tip y−12.0; nut z2.5…4.9 | — | #6, #12 | C15_integration_notes "OD-000 placement"; OD-C15 §5 REQ-07 | text | — |

### OD-C02 and OD-C05 (envelopes and joints, as the other specs give them — no OD-C02/C05 DESIGN_SPEC is an input)

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-67 | OD-C02 top rail | x 59.5 … 70.5, top face y 215.0, z −240 … −30; two Ø4.0 × 6.0 insert bores along −Y from y 215 at (65, −60) and (65, −210) | mm | x59.5…70.5; y215; z−240…−30 | — | #10 | OD-C10 spec §2 | text | from OD-C10's interfaces table, not an OD-C02 spec |
| X-68 | OD-C02 electric-side face and rails | electric face x = 67.0; base rail to x 71.0 (y 0 … 12); top rail to x 70.5 (y 207 … 215); wire windows Ø14 at (y 150, z −200 / −130 / −60), (y 60, z −55) | mm | x67.0; rails x71.0/x70.5; Ø14 windows | — | #9 | OD-C08 spec §2 | text | from OD-C08's interfaces table, not an OD-C02 spec |
| X-69 | OD-C02 bulkhead plane (base-frame perspective) | the plane x = 65 from z −240 to −30, with four insert holes (X-06) | mm | x=65, z−240…−30 | — | #7 | OD-C01 spec §4 A-04 | text | — |
| X-70 | OD-C02 rear end (back-panel perspective) | OD-C02 bulkhead (identity; rear end z −240, x 59 … 71, y 0 … 215) | mm | z−240; x59…71; y0…215 | — | #11 | OD-C11 spec §2 | text | — |
| X-71 | OD-C05 joint into the machine frame | local x → X, y → +Z, z → −Y, origin at (0, 180.06, 32.0) | mm | origin (0, 180.06, 32.0) | — | #7 | OD-C01 spec §4 A-01 | text | — |
| X-72 | OD-C05 foot/wall/plate envelope as placed | foot occupies x ±55, z −70 … −26; wall z −26 … −20 up to y 210; plate z −26 … +82 at y 205 … 210; housing occupies x ±50, z −18 … +82 | mm | x±55 (foot); x±50 (housing); z ranges above | — | #7 | OD-C01 spec §4 A-01 | text | — |
| X-73 | OD-C05 key y-levels | housing's rear face at y 205.0; mouth face at y 176.76; portafilter spouts hang to y ≈ 135.2 | mm | y205.0 (rear), y176.76 (mouth), y≈135.2 (spouts) | — | #7 | OD-C01 spec §4 A-01 | text | — |
| X-74 | OD-C05 plate top and features (from OD-C10's interfaces table) | plate top y 210.0 over x ±55, z −70 … +82; hub window R 30 about (0, 32); hatch x ±40, z −64 … −32; four counterbored housing-screw holes at (±44, −12) and (±44, 76) | mm | y210.0; R30 hub; hatch x±40, z−64…−32; holes (±44,−12/76) | — | #10 | OD-C10 spec §2 | text | — |
| X-75 | OD-C05 holes (OD-C01's own figure) | holes at (x ±35, z −40) and (x ±35, z −60) | mm | (±35,−40), (±35,−60) | — | #7 | OD-C01 spec §4 A-01 | text | — |

### Fasteners (bom_rows.csv and the specs)

| ID | What | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-76 | OD-F01 heat-set insert | M3 heat-set insert (Ø4.0 bore × 6; 38 in the chassis), qty ~50, brass M3, AliExpress, 10 EUR (set) | mm, EUR | Ø4.0 × 6 | — | #2 | bom_rows.csv row OD-F01 | table | — |
| X-77 | OD-F02 screw | M3×8 screw, qty ~50, ISO 7380 / DIN 912 A2, AliExpress | mm | M3×8 | — | #2 | bom_rows.csv row OD-F02 | table | — |
| X-78 | OD-F03 acrylic sheet (optional skins) | Acrylic sheet 3 mm (optional skins), qty per design, PMMA, local laser / leftover stock, 25 EUR | mm, EUR | 3 mm | — | #2 | bom_rows.csv row OD-F03 | table | not used per the Usta's "printed" ruling in REQUEST.md, but still a BOM row |
| X-79 | OD-F09 cable tie | Cable tie 4.8 mm (OD-C03 pump strap; OD-C08 loom slots 2 × 4), qty 4, PA66 UV-black, hardware store, 1 EUR | mm, EUR | 4.8 mm | — | #2 | bom_rows.csv row OD-F09 | table | — |
| X-80 | OD-C12 BOM row | Left side panel, qty 1, cad DESIGN, material "ASA / PETG or 3 mm acrylic", source printed, status proposed | — | — | — | #2 | bom_rows.csv row OD-C12 | table | conflicts with REQUEST.md's "printed… PLA" ruling, see §4 conflict |
| X-81 | OD-C13 BOM row | Right side panel, qty 1, cad DESIGN, material "ASA / PETG or 3 mm acrylic", source printed, status proposed | — | — | — | #2 | bom_rows.csv row OD-C13 | table | conflicts with REQUEST.md's "printed… PLA" ruling, see §4 conflict |
| X-82 | OD-C16 BOM row | "Corner bracket for acrylic skins (optional)", qty 16, cad DESIGN, material ASA / PETG, source printed, status proposed | — | — | — | #2 | bom_rows.csv row OD-C16 | table | BOM names it for acrylic skins only; REQUEST.md repurposes it as the fastening bracket for printed panels, see §3/§4 |
| X-83 | OD-F02 new quantity from integration notes | +12 (OD-C08 flange 4, OD-C11 flanges 4, OD-C10 lid 4); two OD-C08 board screws are **M3×6** (new row) | — | M3×8 (+12), M3×6 (new) | — | #5 | "docs/bom.csv" section | text | — |
| X-84 | OD-F01 new quantity from integration notes | +12 (8 in OD-C01, 2 in OD-C08 standoffs, 2 in OD-C11 ledge) | — | +12 | — | #5 | "docs/bom.csv" section | text | — |
| X-85 | OD-F10 / new M3×12 screw (feet) | M3×12 ISO 7380 A2 button head, one per foot, from the plate top; raise OD-F10's qty from 4 to 8 (include the 4 feet) or add a new row | mm | M3×12 | — | #6 | C15_integration_notes "docs/bom.csv" | text | — |
| X-86 | New hex nut row (OD-F12) | ISO 4032 M3 A2 hex nut ×4, captive in the feet (new row, e.g. OD-F12); optional nylon-insert nut ISO 10511 M3 then needs M3×16 | mm | M3 | — | #6 | C15_integration_notes "docs/bom.csv" | text | — |
| X-87 | OD-E06 power cord (region-specific) | Power supply cord with plug (AU code shown), qty 1, ENVELOPE cad, FixPart / generic, 8 EUR | — | — | — | #2 | bom_rows.csv row OD-E06 | table | relevant to OD-C11's cord pass-through near the side-panel corner |

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-88 | Material ruling: everything printed in PLA for now | "all printed in pla for now" | #1 | REQUEST.md, the Usta's message 2026-10-02 22:58 UTC |
| X-89 | Side panels are printed, not acrylic | "1/ merge\n2/ accept\n3/ printed\n4/ 7mm" — question 3 was "Acrylic or printed side panels. This decides how C12, C13 and C16 get designed." Answer: printed | #1 | REQUEST.md, the Usta's message |
| X-90 | Answer "4/ 7mm" (unexplained figure) | "4/ 7mm" | #1 | REQUEST.md, the Usta's message | 
| X-91 | Deliverables, printed panels | "OD-C12 left side panel and OD-C13 right side panel of the Open Dedica machine, 3D-printed (not 3 mm acrylic skins), in PLA." | #1 | REQUEST.md "What the job delivers" |
| X-92 | OD-C16 corner-bracket role, this job's design choice | "OD-C16 corner brackets: the BOM row says \"Corner bracket for acrylic skins (optional)\", qty 16; with printed panels the bracket is the part that fastens the panels to the base frame OD-C01 (this job's design choice, to be stated in the spec)." | #1 | REQUEST.md "What the job delivers" |
| X-93 | Per-part deliverable set (chassis-wide rule) | "Per part: parametric build script, STEP (mm, one named solid), STL and 3MF, and one independent review, as every chassis part (chassis/README.md \"Goal\")." | #1 | REQUEST.md "What the job delivers" |
| X-94 | Side panels must end at y 215 under the lid's skirt | "The top panel OD-C10 currently leans on a left rest pad until the side panels carry its edges (OD-C10 RV01 F1; C08_C11_integration_notes.md): the side panels should end at y 215 under the lid's 3 mm skirt (x ±117 … ±120)." | #1 | REQUEST.md "Constraints stated by the project" |
| X-95 | Keep-out above each foot hole | "Keep the Ø8 × 2 screw-head keep-out above each OD-C15 foot hole free (C15_integration_notes.md)." | #1 | REQUEST.md "Constraints stated by the project" |
| X-96 | Shared files belong to another thread | "The shared files (docs/bom.csv, chassis/README.md, OD-000) belong to another thread: this job hands its changes over in integration notes and edits none of them." | #1 | REQUEST.md "Constraints stated by the project" |
| X-97 | Goal: every printable part designed, reviewed, assembled | "Every custom part of the machine that is 3D-printable, designed and reviewed, and the whole machine delivered as an assembly" with "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #3 | CHASSIS_README.md "Goal" |
| X-98 | `validated` needs a print and fit check | "`validated` needs a print and a fit check by the Usta; the group head also needs the bench pressure test (`OD-T01`)." | #3 | CHASSIS_README.md "Goal" |
| X-99 | Order-of-work row for this job | "OD-C12, OD-C13 side panels; OD-C16 corner brackets | OD-C01 | acrylic option is the Usta's call" | #3 | CHASSIS_README.md order-of-work table, row 12 |
| X-100 | Two-zone layout rule | "Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains)… In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #4 | SOURCING_GUIDE_s6.md rule 1 |
| X-101 | Anti-vibration rule | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #4 | SOURCING_GUIDE_s6.md rule 2 |
| X-102 | Thermal-map rule | "Respect the thermal map. Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #4 | SOURCING_GUIDE_s6.md rule 3 |
| X-103 | Serviceability rule | "Serviceability is the point. … top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #4 | SOURCING_GUIDE_s6.md rule 4 |
| X-104 | Mug / envelope rule | "Design for the mug. Group head height ≥ 95 mm above tray … keep the 0.4 m³ envelope limit from the thesis spec." | #4 | SOURCING_GUIDE_s6.md rule 5 |
| X-105 | Pre-infusion / sensor-boss rule | "Pre-infusion & preheat are software. … Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one." | #4 | SOURCING_GUIDE_s6.md rule 6 |
| X-106 | Safety-spec rule | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #4 | SOURCING_GUIDE_s6.md rule 7 |
| X-107 | OD-C08/C10/C11 RV01 status, no blocking findings | "Three jobs, each reviewed once, all RV01 `APPROVED_ASSUMPTION_CONDITIONAL` with no blocking findings." | #5 | C08_C11_integration_notes.md intro |
| X-108 | Shared files are this (side-panel) job's to change | "The shared files below are yours to change; nothing listed here was edited by these jobs." | #5 | C08_C11_integration_notes.md intro |
| X-109 | OD-C01 needs 8 new inserts (handover) | "Eight **new** M3 heat-set inserts … in OD-C01, for screws driven from above" | #5 | C08_C11_integration_notes.md "OD-C01 change needed" |
| X-110 | docs/bom.csv regeneration instruction | "Then regenerate: `python tools/build_bom.py && python tools/build_progress.py`." | #5 | C08_C11_integration_notes.md "docs/bom.csv" |
| X-111 | OD-C10 side/front edges free until side+front panels exist | "The lid's side and front edges are free until the side panels OD-C12/C13 and front panel OD-C09 exist: they should end at y 215 under the lid's skirt (x ±117 … ±120, z −305 … +100 is the lid's 3 mm skirt)." | #5 | C08_C11_integration_notes.md "Interfaces and keep-outs for later parts" |
| X-112 | Tool note: common_volume false negative | "`tools.core.common_volume` returned 0 mm³ for a real 3.65 mm³ overlap in fused topology at a seat plane (OD-C08 RV01 F5): it should fail closed." | #5 | C08_C11_integration_notes.md "docs/HANDOVER.md" |
| X-113 | Keep-out handed to this job (C15 notes) | "Keep-out for later parts (spec A-09): a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) holds the screw head (Ø5.7 × 1.65). OD-C12, OD-C13, OD-C16 and OD-C06 must leave it free." | #6 | C15_integration_notes.md "chassis/README.md" |
| X-114 | OD-C01 A-12 superseded by OD-C15 A-02 | "OD-C01 A-12 (\"screwed from below into inserts of the feet\") is superseded by OD-C15 A-02 (screw from above, captive nut): worth a line on the OD-C01 row." | #6 | C15_integration_notes.md "chassis/README.md" |
| X-115 | Tool note: overhang_census inconclusive at 45° | "`overhang_census` is INCONCLUSIVE on a cone at exactly 45° (sampling bound ~0.01°), so specs should put printed chamfers at ≥ 46° or 60°" | #6 | C15_integration_notes.md "docs/HANDOVER.md" |
| X-116 | OD-C01 deliverable tier and intent (floor plane, reserved zones) | "Done means: one valid printable plate with a flat top face (the floor plane every mount's spec names), M3 heat-set insert holes under the three existing mounts' foot holes and along the bulkhead line, screw holes for four feet, two drain holes in the wet zone, reserved zones for the parts not yet designed, and every unconfirmed value in §6." | #7 | OD-C01 spec §1 |
| X-117 | OD-C10 deliverable intent (lid held at 4 columns, headroom) | "a lid over the whole machine that comes off to reach the group head housing's four screws and the carrier's foot screws … held by four M3 screws driven from above: two into the inserts the bulkhead OD-C02 provides … two into the inserts of the back panel OD-C11's top ledge." | #10 | OD-C10 spec §1 |
| X-118 | OD-C10 REQ-08 stiffness (soft gate, bench-checked without side panels) | "The lid does not sag visibly or rattle on its four columns with the side panels absent (the edges away from the bulkhead and back panel free, A-04); a hand on the lid bears on the pads; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print." | #10 | OD-C10 spec §5 REQ-08 |
| X-119 | OD-C11 deliverable intent (rear wall, 4 screws into new inserts) | "Done means: one valid printable solid standing on the OD-C01 plate inside its rear edge, held by four M3 screws driven from above into four new inserts in the plate, nothing of it in the pump's or the bulkhead's space, its pass-throughs and vents at the places of §4, and every unconfirmed value in §6." | #11 | OD-C11 spec §1 |
| X-120 | OD-C11 REQ-09 stiffness (soft gate, bench-checked without side panels) | "The panel does not drum or flex visibly with the top panel on and the side panels absent; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print." | #11 | OD-C11 spec §5 REQ-09 |
| X-121 | OD-C11 C2 concept (deferred): back panel fixed to side panels instead | "C2 — the back panel screwed to the side panels' rear edges from outside. Removable without the top panel, but it needs side panels with rear posts and inserts; deferred until OD-C12/C13 (and the acrylic option, chassis/README row 12) are decided." | #11 | OD-C11 spec §4 |
| X-122 | OD-C08 scope note: OD-C13 not designed here | "the side panel OD-C13 and the mains entry (back panel OD-C11) are not designed here: their rows are assumptions." | #9 | OD-C08 spec §1 |
| X-123 | OD-C08 A-06 names the assumed side-panel inner face | "the board within x 70 … 117 (a side panel's inner face assumed at x ≥ 117)" | #9 | OD-C08 spec §6 A-06 |
| X-124 | OD-C15 out-of-scope note naming this job's parts | "the side panels, corner brackets and other parts on the plate top (they receive the keep-out of A-09)" | #12 | OD-C15 spec §1 |
| X-125 | PETG material choice reasoning (pattern across sibling parts) | "a 232 × 215 panel warps in ASA on the open Kobra; the panel is far from the heat" (OD-C11); similar wording for OD-C01, OD-C10, OD-C08 | #11, #7, #10, #9 | each spec's §3 row | — |
| X-126 | Quantities: OD-C12/C13 qty 1 each; OD-C16 qty 16 | see X-80/X-81/X-82 | #2 | bom_rows.csv | — |

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-80, X-81, X-82, X-88, X-89, X-91 | The BOM (`bom_rows.csv`) still lists OD-C12/OD-C13 material as "ASA / PETG or 3 mm acrylic" and OD-C16 as "for acrylic skins (optional)", while REQUEST.md records the Usta's ruling as printed, PLA. Which governs the spec: the REQUEST.md ruling (printed, PLA) or the BOM's ASA/PETG wording? And does "all printed in pla for now" (X-88) override the chassis-wide pattern of PETG-for-large-flat-parts seen in OD-C01/OD-C10/OD-C11/OD-C08 (which were all built in PETG despite their own BOM rows saying ASA)? |
| 2 | X-90 | What does the Usta's answer "4/ 7mm" mean? REQUEST.md gives no fourth question text to pair it with (only questions 1–3 are named: "merge", "accept", "printed"). Is 7 mm a panel thickness, a gap, an overlap, or something else, and which open question does it answer? |
| 3 | X-45, X-46, X-49, X-48, X-35 | OD-C11's wall ends at x ±116 and its wall foot stands only 2.300 mm clear of the feet holes' rims (A-02, A-12, both OPEN, explicitly handed to "OD-C12/C13, OD-C16 designs"). What is the side panel's own outer/inner face position and corner geometry where it meets OD-C11's wall end at x ±116, and how much of the strip between x 116 and the lid's x ±117…±120 skirt line belongs to the side panel versus to OD-C11's end? |
| 4 | X-31, X-32, X-23, X-35 | The lid's outer outline is x ±120 (OD-C10) and OD-C11's wall is at x ±116; "the side panels … outer faces x ±120" (per OD-C10 A-04) is stated as an assumption, not a confirmed interface. What is the side panel's actual thickness and where exactly does its inner face sit (does it rest on OD-C11's wall end, overlap it, or stand independently on the plate)? |
| 5 | X-04, X-62, X-63, X-45, X-46 | The Ø8×2.0 screw-head keep-out sits above each foot hole at (±110, ±z); OD-C11's wall already "touches" this keep-out at 0.0 clearance (no overlap, X-63). Given the side panel and the OD-C16 bracket must also "leave it free" (X-62), what is the side panel's/bracket's own footprint near each corner, since no input states where the bracket or the panel's corner post actually sits relative to this cylinder? |
| 6 | X-56, X-57, X-59 | OD-C08's own spec (X-57) gives the board's heatsink reach as x ≈ 109.26; the integration notes and CHASSIS_README (X-56) round this to "x ≈ 109.3"; OD-C08's own assumption A-06 (X-59) assumes the side panel's inner face sits at x ≥ 117 mm, leaving a gap of only ≈ 7.7 mm between the heatsink and the assumed panel face. Does the side panel's design need to confirm or widen this clearance, and is the OD-C16 corner bracket required to stay clear of it too? |
| 7 | all (chassis-wide) | How is a panel fixed to the frame: screws into inserts in OD-C01's plate edge, into OD-C16 corner brackets only, tabs into OD-C11's and OD-C02's side faces, or some other method? No input states the side panel's own fixing scheme. |
| 8 | all (chassis-wide) | What is the side panel's thickness? No input gives it (REQUEST.md only rules out 3 mm acrylic and sets the material to PLA; no printed-panel thickness is stated anywhere). |
| 9 | X-31, X-111, OD-C09 references throughout | What is the front panel OD-C09's plane (its outer face position, height, and relationship to the side panels' front edge)? OD-C09 is repeatedly named as a neighbour ("the front panel OD-C09... are not designed") but no input gives its geometry; the side panels must meet it at the z +100 edge. |
| 10 | X-32, X-48, X-49 | Where exactly do the corners form: side panel to back panel (OD-C11, wall ends x ±116, z −302…−299) and side panel to front panel (OD-C09, undesigned)? No input states a corner joint design (lap, mitre, bracket-only) for either corner. |
| 11 | X-19, X-55 chassis-wide pattern, SOURCING_GUIDE rule 3 (X-102) | SOURCING_GUIDE rule 3 states "PLA nowhere structural," yet REQUEST.md's ruling sets the side panels and brackets to PLA. The side panels are structural (they must carry the lid's edge per OD-C10 A-04, X-31). Does the Usta intend PLA to carry structural load here, or is "for now" (X-88) a placeholder pending a later material decision? |
| 12 | X-21, chassis-wide ("Machine profiles") | Which printer prints a panel up to ~400 mm along one edge (matching OD-C01/OD-C10's z-span −305…+100 = 405 mm and OD-C11's 232 mm)? Is it the Anycubic Kobra Max 3 (as OD-C01/OD-C10 assume, build volume itself unconfirmed, A-09 in those specs) or another machine? |
| 13 | X-82, X-92, X-124, X-62/X-63 | With printed (not acrylic) panels, OD-C16's BOM qty is 16 "for acrylic skins (optional)." REQUEST.md repurposes it as the fastening bracket for printed panels but states the qty question is "this job's design choice." Does the bracket count stay 16, or does the printed-panel design choice change it (e.g. one bracket per corner × some multiple)? |
| 14 | X-45, X-46 (feet-hole margin) and X-69/X-07 (bulkhead-line holes at x=65) | The brief's criterion "every hole and insert position with |x| ≥ 60" includes the OD-C02 bulkhead-line holes at x=65 even though the brief's own parenthetical names only "feet holes, the C07/C08/C11 inserts, drains." Should the OD-C02 bulkhead-line insert holes (X-06) be treated as in scope for the side-panel/bracket spec, since OD-C02 itself is a named neighbour in the job's "What the job is for" line only indirectly (via OD-C01/OD-C08/OD-C11), not listed among OD-C12/C13/C16's direct neighbours? |
| 15 | X-10 | OD-C01's own plate is 6 mm thick and a 6 mm deep bore for the new OD-C08/OD-C11 inserts would reach the underside; "an OD-C01 revision decides through vs. blind (a boss below, or a 5.0 bore with a shorter insert)" is still open. Since the side-panel/bracket design also needs inserts near the edge (if bracket-fixed), should it assume through bores, blind bores, or bosses under the plate at its own insert locations? |

## §5 Unreadable

None: every markdown and csv file named in the brief was read in full. The eight
STEP files (`OD-C01_base_frame.step`, `OD-C02_bulkhead.step`,
`OD-C05_group_head_carrier.step`, `OD-C07_valve_flowmeter_mount.step`,
`OD-C08_electronics_bay_tray.step`, `OD-C10_top_panel.step`,
`OD-C11_back_panel.step`, `OD-C15_foot.step`) were listed and hashed only, per
intake rule 6; their geometry is deferred to `tools/measure` and is not reported
in §2. No `OD-C02_DESIGN_SPEC.md` or `OD-C05_DESIGN_SPEC.md` was among the
inputs; every OD-C02/OD-C05 value in §2 is quoted from another part's spec, not
read from an OD-C02 or OD-C05 spec of its own.
