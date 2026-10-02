# INTAKE v01 — 20261001-od-c10-top-panel

Intake: Claude Code, claude-sonnet-5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-10-01

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
| 1 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP AP242 | N/A | listed and hashed only (intake rule 6); geometry not read, measured later by `tools/measure` |
| 2 | 00_Spec/inputs/OD-C02_bulkhead.step | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | 150003 | STEP AP242 | N/A | listed and hashed only; geometry not read |
| 3 | 00_Spec/inputs/OD-C05_group_head_carrier.step | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | 186262 | STEP AP242 | N/A | listed and hashed only; geometry not read |
| 4 | 00_Spec/inputs/OD-C07_valve_flowmeter_mount.step | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | 386750 | STEP AP242 | N/A | listed and hashed only; geometry not read |
| 5 | 00_Spec/inputs/REQUEST.md | 4c437e51d5f19c34811fa2c10c1b5e51726af24bcd43d1e83608f620c87f5929 | 2248 | Markdown | 1 (unpaginated) | read in full |
| 6 | 00_Spec/inputs/PROJECT_RULES.md | c5cab0228c9ca51387c64711bc66f418f02ca18ff8c3772a876a99d923c3d4e4 | 10791 | Markdown | 1 (unpaginated) | read in full |
| 7 | 00_Spec/inputs/bom_rows.csv | acccda358aba82ed9dfbaabb68e15b2179ab7db4f4188ad640a0f913431d03ce | 1952 | CSV | 18 rows | read in full |
| 8 | 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | 25226 | Markdown | 1 (unpaginated) | read in full |
| 9 | 00_Spec/inputs/reports/OD-C02_bulkhead/DESIGN_SPEC_v1.2.md | d98773838192515ee097b92e5ebe38006324ba0031743c408da7093c893b63be | 20686 | Markdown | 1 (unpaginated) | read in full |
| 10 | 00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v2.2.md | 3accd3b00bf26544ea0aed71e72f23387afb3af447e8f26f2f0bb325dd3377bd | 27945 | Markdown | 1 (unpaginated) | read in full |
| 11 | 00_Spec/inputs/reports/OD-C07_valve_flowmeter_mount/DESIGN_SPEC_v1.2.md | 33ff74a908766d31ec66d1a291d3d31c971173c3555461d03aaa01e568c95ce9 | 28353 | Markdown | 1 (unpaginated) | read in full |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C01 plate outline, x extent | x −120 … +120 | mm | −120.00 … +120.00 | — | #8 | §4 C1 | text | — |
| X-02 | OD-C01 plate outline, z extent | z −305 … +100 | mm | −305.00 … +100.00 | — | #8 | §4 C1 | text | — |
| X-03 | OD-C01 plate outline, corner radius | corners R 10 | mm | R10.00 | — | #8 | §4 C1 | text | — |
| X-04 | OD-C01 plate top face (floor plane, y = 0) | y = 0, plate y −6.0 … 0 | mm | y 0.00 (plate −6.00 … 0.00) | ±0.10 (REQ-07) | #8 | §2, §4 C1, REQ-07 | text / gate table | — |
| X-05 | Machine height (assumption) | machine height ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet | mm | ≈260.00 | — | #8 | §6 A-16 | text | top panel's own contribution to the 260 figure is not itemised — see §4 gap 8 |
| X-06 | Bulkhead wall, height (y) | wall rises y 0 … 215.0 | mm | 0.00 … 215.00 | — | #9 | §4 C1 | text | — |
| X-07 | Bulkhead top rail, x extent | x 59.5 … 70.5 (11 wide, centred on the wall) | mm | 59.50 … 70.50 | — | #9 | §4 C1 | text | — |
| X-08 | Bulkhead top rail, y extent | y 207.0 … 215.0 | mm | 207.00 … 215.00 | — | #9 | §4 C1 | text | — |
| X-09 | Bulkhead top rail, z extent | along the whole length, z −240.0 … −30.0 | mm | −240.00 … −30.00 | — | #9 | §4 C1 | text | — |
| X-10 | Bulkhead top rail, top face y | top rail's top face at y = 215.0 | mm | 215.00 | ±0.1 | #9 | §5 REQ-06 | gate table | — |
| X-11 | Bulkhead top-panel insert bore 1 | Ø4.0 blind bore along −Y from y 215.0, depth 6.0, at (x 65.0, z −60.0) | mm | Ø4.00, depth 6.00, at (x 65.00, z −60.00) | Ø±0.05, depth ±0.1, offset ≤0.10 | #9 | §4 C1, §5 REQ-07 | gate table | fit-critical; CAD-stated, not yet built or measured |
| X-12 | Bulkhead top-panel insert bore 2 | Ø4.0 blind bore along −Y from y 215.0, depth 6.0, at (x 65.0, z −210.0) | mm | Ø4.00, depth 6.00, at (x 65.00, z −210.00) | Ø±0.05, depth ±0.1, offset ≤0.10 | #9 | §4 C1, §5 REQ-07 | gate table | fit-critical; CAD-stated, not yet built or measured |
| X-13 | Bulkhead electric-zone boundary | the wall centred on x = 65, wet face x = 63.0, electric face x = 67.0; electric zone x ≥ 70 (base rail to x 71, top rail to x 70.5) | mm | wet face 63.00, electric face 67.00, bay zone x ≥ 70.00 | ±0.10 (REQ-02) | #9 | §1, §2, §5 REQ-02, REQ-08 | text / gate table | — |
| X-14 | Carrier plate, underside y (= housing's rear face, as placed in machine frame) | housing's rear face at y 205.0 | mm | 205.00 | — | #8 | §4 C1 (A-01) | text | carrier not yet built; A-01 OPEN |
| X-15 | Carrier plate, top y (as placed in machine frame) | carrier's plate z −26 … +82 at y 205 … 210 | mm | top y 210.00 | — | #8 | §4 C1 (A-01) | text | carrier not yet built; A-01 OPEN |
| X-16 | Carrier plate outline (housing frame) | plate spans x ±55.0, y −102.0 … +50.0, 5.0 thick along Z (z −29.94 … −24.94) | mm | x ±55.00, y −102.00 … +50.00, thickness 5.00 | ±0.10 (REQ-03) | #10 | §4 C4, §5 REQ-03 | text / gate table | housing frame, not machine frame |
| X-17 | Carrier hub window | R 30.0 about the axis, innermost material at r ≥ 30.0 at every 10° over z −29.94 … −24.94 | mm, deg | r ≥ 30.00 | — | #10 | §4 C4, §5 REQ-04 | gate table | housing frame; fit-critical, not confirmable without a build |
| X-18 | Carrier hatch | 80.0 × 32.0 (x ±40.0, y −96.0 … −64.0), corners R 4.0, over the column | mm | 80.00 × 32.00, corner R4.00 | — | #10 | §4 C4 | text | housing frame |
| X-19 | Carrier housing-screw holes (reach the housing's inserts from above) | four Ø3.4 through-holes along Z at (x ±44.0, y ±44.0), each with a Ø6.5 × 2.0 counterbore from the top face | mm | Ø3.40, at (x ±44.00, y ±44.00); counterbore Ø6.50 × 2.00 | Ø±0.1 (REQ-01), counterbore ±0.1 (REQ-02), offset ≤0.10 | #10 | §4 C4, §5 REQ-01, REQ-02 | gate table | housing frame |
| X-20 | Carrier foot screws into OD-C01 (reached from above through the hatch) | four Ø3.4 through-holes along Z at (x ±35.0, y −72.0) and (x ±35.0, y −92.0); machine frame (x ±35, z −40) and (x ±35, z −60), the pattern of spec 1.x | mm | Ø3.40, housing (x ±35.00, y −72.00/−92.00) = machine (x ±35.00, z −40.00/−60.00) | ±0.1 (REQ-06), offset ≤0.10 | #10 | §4 C4, §5 REQ-06 | gate table | housing frame and machine frame both given by source |
| X-21 | Water connection / OD-G04 hub tube above the hub (housing frame) | hub tube top at housing z −22.55, OD 20.06; fits within r ≤ 30 of the axis above the housing, through the plate's window; not scanned | mm | z −22.55, OD 20.06, r ≤ 30.00 | — | #10 | §6 A-06 | text | unconfirmed (OEM parts not scanned); how far this rises above the carrier plate (y 210) is not stated — see §4 gap 1 |
| X-22 | Carrier's housing + portafilter height above the floor | housing's rear face 205.0 above the floor, mouth face at 176.76; portafilter spouts hang to ≈ housing z 44.9, 135.2 above the floor | mm | 205.00 / 176.76 / 135.2 above floor | — | #10 | §6 A-03 | text | unconfirmed; tray not scanned |
| X-23 | Valve mount, no-material-above plane (OPV reachable) | no mount material above z 48.1 (mount frame); none within r 12 of the valve axis above the deck top | mm | z ≤ 48.10, r ≥ 12.00 keep-out | — | #11 | §5 REQ-08 | gate table | mount frame; z maps to machine y by the OD-C01 joint (local z → +Y) |
| X-24 | OPV height (drive tube top) | the drive tube top sits at z 61.7 in the open (mount frame) | mm | z 61.70 | — | #11 | §4 C1, §6 A-10 | text | mount frame; unconfirmed, donor-derived |
| X-25 | Valve mount envelope | 119 × 50 × 48 (x −25 … 94, y ±25, z 0 … 48) | mm | 119.00 × 50.00 × 48.00 | ±0.1 (U-02) | #11 | §2, §5 U-02 | gate table | mount frame |
| X-26 | Valve mount pose in OD-C01 (machine) frame | rotation local x → −Z, local y → −X, local z → +Y; origin (−92, 0, −60); bottom face lands on y 0 | mm, deg | origin (−92.00, 0.00, −60.00) | — | #6, #8 | PROJECT_RULES "OD-000 placements"; OD-C01 §4 A-17 | text | OD-C07 spec at RV01 REVISE, not yet fully approved (A-17 OPEN) |
| X-27 | Drip tray zone (not designed) | the tray stands on the plate within x ±75, z −15 … +85, under the mouth at (0, 32); cup rest top ≤ 36.9 above the plate | mm | x ±75.00, z −15.00 … +85.00, cup rest ≤ 36.90 | — | #8 | §4 C1, §6 A-06 | text | reserved zone, OPEN; not scanned |
| X-28 | Water tank zone (not designed) | the tank with its dock OD-C06 stands within x ±70, z −305 … −250, lifted out upward | mm | x ±70.00, z −305.00 … −250.00 | — | #8 | §4 C1, §6 A-07 | text | reserved zone, OPEN; not scanned |
| X-29 | Electronics bay zone (not designed) | OD-C08 within x 70 … 120, z −240 … −30, behind the bulkhead | mm | x 70.00 … 120.00, z −240.00 … −30.00 | — | #8 | §4 C1, §6 A-08 | text | reserved zone, OPEN |
| X-30 | Kobra Max 3 build volume (OD-C01's own assumption) | 420 × 420 × 500 (Anycubic specification, not in the machine file) | mm | 420.00 × 420.00 × 500.00 | — | #8 | §6 A-09 | text | "memory of the spec sheet," unconfirmed; see §4 gap 6 |
| X-31 | Creality K1C build volume (OD-C02's and OD-C05's own assumption) | 220 × 220 × 250 (Creality specification, not in the machine file) | mm | 220.00 × 220.00 × 250.00 | — | #9, #10 | OD-C02 §6 A-08; OD-C05 §6 A-08 | text | "memory of the spec sheet," unconfirmed; see §4 gap 6 |
| X-32 | Thermoblock casting clearance under the group head / bulkhead | thermoblock casting ≤ x 50 (bulkhead A-02); casting ≥ 16.5 above the plate; ≥ 13 mm air to the bulkhead wall at x ≤ 50 | mm | x ≤ 50.00; ≥16.50 above plate; ≥13 mm air | — | #8, #9 | OD-C01 §4; OD-C02 §3, §6 A-02 | text | context for the thermal-map requirement; OD-C10 is not adjacent to this zone per any source read |
| X-33 | Carrier foot/wall occupied volume near the bulkhead top rail (machine frame) | carrier's foot x ±55, z −70 … −26; its wall z −26 … −20 up to y 210; its plate z −26 … +82 at y 205 … 210 | mm | x ±55.00; z −70.00…−26.00 (foot), −26.00…−20.00 (wall, up to y210.00); z −26.00…+82.00 at y 205…210 (plate) | — | #8 | §4 C1 (A-01) | text | carrier not yet built; A-01 OPEN |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-40 | BOM identity, material, process | `OD-C10,OD-C00,PRINT,Top panel (removable — 4 screws),,,1,DESIGN,ASA,printed,print,,proposed` | #7 | bom_rows.csv row "OD-C10" |
| X-41 | Removable with 4 screws, OPV reachable | "SOURCING_GUIDE §6 rule 4: top and back panels removable with 4 screws each; OPV reachable." | #5 | REQUEST.md, body |
| X-42 | Bulkhead provides the top-panel inserts | "OD-C02 provides two M3 inserts for the top panel in its top rail (spec 1.2 REQ-07, A-05)." | #5 | REQUEST.md, body |
| X-43 | Serviceability — screws reached through the top panel | "OD-C05 spec 2.2 A-14: the housing screws and the carrier's foot screws are reached from above through the removable top panel" | #5 | REQUEST.md, body |
| X-44 | Hot water tube / water connection rise into the hub window | "A-06 and A-07: the water connection and the hot water tube (TUBE 7) rise above the carrier's plate (top y 210) into the hub window" | #5 | REQUEST.md, body |
| X-45 | OPV adjusted with the top panel off | "OD-C07 spec A-10: the OPV is adjusted from above with the top panel off." | #5 | REQUEST.md, body |
| X-46 | The Usta's words on the water tank (verbatim) | "water tank is transparent hard to scan we can just use the tray that step converted as reference and i will hold water tank on the table myself no need to design for it now" | #5 | REQUEST.md, "The Usta's words" |
| X-47 | The Usta's words, scope ("what can start now") | "what can start now please initiate it" | #5 | REQUEST.md, "The Usta's words" |
| X-48 | Standing instruction — order of work and ledger discipline | "Design every 3D-printable part of open-dedica (OD-G01, OD-C01 … C16, OD-T01) with the pipeline, in the order of `chassis/README.md`; ask the Usta only where a decision is needed; write open questions as `A-##` rows in the ledger and proceed. Every scan- or report-derived value is an assumption until the Usta confirms it; calipers beat scans." | #5 | REQUEST.md, "Standing instruction" |
| X-49 | Data class | "Data class PUBLIC (CC BY 4.0)." | #5 | REQUEST.md, "Standing instruction" |
| X-50 | Two-zone layout rule | "Two-zone layout. Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #6 | PROJECT_RULES.md §6 rule 1 |
| X-51 | Thermal map / materials rule | "Respect the thermal map. Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #6 | PROJECT_RULES.md §6 rule 3 |
| X-52 | Serviceability rule (full) | "Serviceability is the point. The Dedica's worst trait (thesis: \"very difficult to disassemble\") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #6 | PROJECT_RULES.md §6 rule 4 |
| X-53 | Safety spec | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #6 | PROJECT_RULES.md §6 rule 7 |
| X-54 | Chassis hardware standard | "M3 heat-set inserts + M3 screws (the thesis tapped printed holes; inserts are better)" | #6 | PROJECT_RULES.md §3.10 |
| X-55 | Machine printer profiles | "Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into `oguz-atolye/atolye/machines/`." | #6 | PROJECT_RULES.md, "Order of work" footer |
| X-56 | Order of work for OD-C10 | "`OD-C10`, `OD-C11` top and back panels \| OD-C01, OD-C02 \| —" (row 11 of the order-of-work table) | #6 | PROJECT_RULES.md, "Order of work" table |
| X-57 | Deliverable set for every printed part | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #6 | PROJECT_RULES.md, chassis/README goal |
| X-58 | Fasteners BOM rows | `OD-F01,OD-000,STD,M3 heat-set insert (Ø4.0 bore × 6; 26 in the chassis),,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo` / `OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo` | #7 | bom_rows.csv rows "OD-F01", "OD-F02" |
| X-59 | Acrylic sheet BOM row (adjacent panels' optional material) | `OD-F03,OD-000,STD,Acrylic sheet 3 mm (optional skins),,,per design,—,PMMA,local laser / leftover stock,25,,todo` | #7 | bom_rows.csv row "OD-F03" |
| X-60 | Carrier serviceability detail | "the housing is removed downward after the four screws are driven out from above, reached through the removable top panel; the four foot screws are driven through the hatch with a long M3 driver (≈ 200 reach); the gaskets are changed with the housing off the carrier" | #10 | §6 A-14 |
| X-61 | OPV access detail (from OD-C07 itself) | "OPV access: nothing of the mount above z 48 (the drive tube top sits at z 61.7 in the open)." | #11 | §4 C1 |
| X-62 | Bulkhead's own statement of the top panel interface it provides | "...and gives the top panel OD-C10 two insert bosses." | #9 | §1 Intent |
| X-63 | Bulkhead assumption naming OD-C10 as the retiring party | "OD-C10 screws down into two M3 inserts in the bulkhead's top rail at (65, z −60 / −210); the panel is not designed" / "Risk if wrong: the panel's pattern differs" / "Retire by: OD-C10 design" | #9 | §6 A-05 |
| X-64 | OD-C01's height assumption naming the top panel | "machine height ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet" | #8 | §6 A-16 |
| X-65 | OD-C02's height assumption naming the top panel | "the wall 215 tall: the machine ≈ 260 with feet (OD-C01 A-16), the carrier's plate top at y 210, the top panel above 215" / "Risk if wrong: the top panel does not meet the wall or the wall is too tall" / "Retire by: OD-C10 / OD-000" | #9 | §6 A-06 |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-21, X-44, X-15, X-18 | No input states how high the hot water tube (TUBE 7) loop or the water connection / OD-G04 hub tube rises above the carrier plate (top y 210) into the hub window before OD-C10 must clear it: the hub tube's own top (X-21, z −22.55 housing frame) reads as *below* the plate's underside (z −24.94), not above it, so the rise above y 210 is not given by any source read. What height must OD-C10 clear here? |
| 2 | X-06, X-08, X-33 | Nothing in the inputs states what supports the top panel's edges away from the bulkhead (the bulkhead gives two inserts only, on one edge, X-11/X-12/X-42/X-62/X-63); is the panel a cantilever off the bulkhead, or does it rest on the side/front/back panels, the carrier, or something else? |
| 3 | — | No input describes how OD-C10 meets the side panels (OD-C12/C13), the back panel (OD-C11), or the front panel (OD-C09): none of the four are designed yet (per the brief and the order-of-work table, X-56). What is the panel-to-panel joint (overlap, step, gasket, fasteners)? |
| 4 | X-28, X-46 | The water tank "on the table for now" (X-46) is not inside a designed dock; no input states whether or how OD-C10 must provide (or avoid) access to the tank once the top panel is on. Does the tank sit under, beside, or clear of the panel's footprint? |
| 5 | X-32, X-51 | The thermal-map rule (X-51) requires ASA/ABS near heat and allows PETG elsewhere; no input states the top panel's distance to the thermoblock casting (x ≤ 50, X-32) or any other heat source, so whether OD-C10 counts as "near heat" for material choice is not given. |
| 6 | X-30, X-31 | Both the Kobra Max 3 (X-30, 420×420×500) and K1C (X-31, 220×220×250) build volumes are recorded in the other parts' specs as "memory of the spec sheet, not in the machine file" (OD-C01 A-09, OD-C02/OD-C05 A-08) — i.e. themselves unconfirmed assumptions, not read from `oguz-atolye/atolye/machines/` profiles. Which machine and which (confirmed) build volume does OD-C10 print on? |
| 7 | X-01, X-02 | OD-C10 must cover a 240 × 405 mm plate (X-01, X-02); no input states whether the top panel is required to print in one piece or may be split, and on which machine/material it would need to split. |
| 8 | X-05, X-64, X-65 | OD-C01 (X-05/X-64) and OD-C02 (X-65) both cite a machine height "≈ 260" that includes "the top panel and clearance" above the bulkhead's 215 mm top rail, but neither gives the top panel's own thickness, height, or the clearance value; the arithmetic (6 + 175 + 43.1 + top panel + clearance ≈ 260) leaves ≈ 35.9 mm unassigned between the panel and clearance. What is OD-C10's own height/thickness budget? |
| 9 | X-41, X-42, X-11, X-12 | The requirement is "4 screws" (X-41, X-52) but the only fastening points any input provides are the bulkhead's two top-rail inserts (X-11, X-12, X-42); no input names the other two screws' location, or what they go into. Where do the remaining two screws land? |
| 10 | X-04, X-26 | OD-C01 §2 states "the group head axis is the line (x 0, y 175) along Z," while the same document's §4 places the carrier's (and hence the axis') origin via the housing-frame mapping at (0, 180.06, 32.0) with the axis fixed at x=0 and the mapped z=32.0, not y=175; the two statements of the axis's position in the OD-C01 frame are not reconciled by the source and are carried here unresolved. Does this affect where OD-C10's hub-window clearance must sit? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None. All eleven listed inputs opened and read (or, for the four STEP files, listed and hashed per the brief and intake rule 6 — their geometry is not read here and is measured later by `tools/measure`).
