# INTAKE v01 — 20261001-od-c11-back-panel

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
| 1 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP | — | listed and hashed only (intake rule 6); geometry measured later with `tools/measure` |
| 2 | 00_Spec/inputs/OD-C02_bulkhead.step | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | 150003 | STEP | — | listed and hashed only |
| 3 | 00_Spec/inputs/OD-C03_pump_cradle.step | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | 192751 | STEP | — | listed and hashed only |
| 4 | 00_Spec/inputs/OD-H01_ulka_ep5_pump.step | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | 824180 | STEP | — | listed and hashed only |
| 5 | 00_Spec/inputs/OD-W03_tank_seat.step | 55162e2d263cfba9123e09ec6d70d0076a4ff5fe1c609601282f005dc51c69ba | 560657 | STEP | — | listed and hashed only |
| 6 | 00_Spec/inputs/REQUEST.md | 90aec8a3262c3d94080ab8b7578f9adf86395104f31f8cbd0cd535a678a44555 | 2063 | Markdown | 1 page | read fully |
| 7 | 00_Spec/inputs/PROJECT_RULES.md | c5cab0228c9ca51387c64711bc66f418f02ca18ff8c3772a876a99d923c3d4e4 | 10791 | Markdown | 1 page | read fully |
| 8 | 00_Spec/inputs/bom_rows.csv | 81b88f699521a75c6c5f1f210674ad82c90e0f3883628ac3cd39add3c05d410b | 2462 | CSV | — | read fully |
| 9 | 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | 25226 | Markdown | 1 page (§1–§8) | read fully |
| 10 | 00_Spec/inputs/reports/OD-C02_bulkhead/DESIGN_SPEC_v1.2.md | d98773838192515ee097b92e5ebe38006324ba0031743c408da7093c893b63be | 20686 | Markdown | 1 page (§1–§8) | read fully |
| 11 | 00_Spec/inputs/reports/OD-C03_pump_cradle/DESIGN_SPEC_v1.2.md | 0bd94d9b6060ec4ea387fce26d20bdab5ac05c5829bd9993828dae677982584b | 17683 | Markdown | 1 page (§1–§8) | read fully |
| 12 | 00_Spec/inputs/reports/OD-W03_tank_seat/DELIVER_README.md | 78b5519453bc82316d4ff96174e6e5e1f1c716a5a6c07512a568bc9186663b0c | 36905 | Markdown | 1 page (§1–§16) | read fully |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C01 plate outline (C1 chosen concept) | one solid, 6.0 thick, y −6.0 … 0, spanning x −120 … +120 and z −305 … +100, corners R 10 | mm | 6.0 thick; x −120…+120; z −305…+100; R 10 | — | #9 | §4 C1 | text | — |
| X-02 | OD-C01 rear edge (z) | z = −305 | mm | −305 | — | #9 | §4 C1; also §7 REQ-02 envelope | text | — |
| X-03 | OD-C01 plate thickness | 6.0 | mm | 6.0 | ±0.1 (U-02 envelope band) | #9 | §4 C1, §5 U-02, REQ-07 | text | — |
| X-04 | OD-C01 plate corner radius | R 10 | mm | 10 | — | #9 | §4 C1 | text | — |
| X-05 | OD-C01 plate top face / floor plane (y) | y = 0.00 | mm | 0.00 | ±0.10 | #9 | §2, §5 REQ-07 | text | — |
| X-06 | OD-C01 feet holes (x, z) — within 40 mm of rear edge z −305 | four Ø3.4 through-holes at (x ±110, z +90) and (x ±110, z −295); only (x ±110, z −295) lies within 40 mm of the rear edge (distance 10) | mm | Ø3.4; x ±110; z +90 / −295 | ±0.1 (REQ-05) | #9 | §4 C1 "Feet holes"; §5 REQ-05 | text | flagged: the +90 pair is 395 mm from the rear edge, not within the 40 mm band; kept for identification only |
| X-07 | OD-C01 insert holes nearest the rear edge (bulkhead line) | four Ø4.0 insert holes at (x 65, z −45 / −105 / −165 / −225) | mm | Ø4.0; x 65; z −45/−105/−165/−225 | ±0.05 (REQ-04) | #9 | §4 C1 "Insert holes"; §5 REQ-04 | text | the closest, z −225, is 80 mm from the rear edge z −305: outside the 40 mm band, listed because it is the nearest insert hole set |
| X-08 | OD-C01 pump cradle insert holes (x, z) | four Ø4.0 through-holes at (x −4, z −239), (x −4, z −171), (x 37, z −239), (x 37, z −171) | mm | Ø4.0; values as listed | ±0.05 (REQ-03) | #9 | §4 C1; §5 REQ-03 | text | closest z −239 is 66 mm from rear edge; outside the 40 mm band |
| X-09 | OD-C01 drain holes (x, z) | two Ø8.0 through-holes at (x −80, z −120) and (x −80, z −230) | mm | Ø8.0; x −80; z −120/−230 | ±0.1 (REQ-06) | #9 | §4 C1 "Drain holes"; §5 REQ-06 | text | closest z −230 is 75 mm from rear edge; outside the 40 mm band |
| X-10 | OD-C07 valve/flowmeter mount insert holes (x, z) | four Ø4.0 through-holes at (x −113, z −42), (x −71, z −42), (x −113, z −148.5), (x −71, z −148.5) | mm | Ø4.0; values as listed | ±0.05 (REQ-10) | #9 | §4 C1 "OD-C07 valve and flowmeter mount"; §5 REQ-10 | text | closest z −148.5 is 156.5 mm from rear edge; outside the 40 mm band; A-17 OPEN |
| X-11 | Pump cradle OD-C03 foot, rear-most extent (placed in machine frame) | foot occupies x −10 … 42, z −245 … −165 | mm | x −10…42; z −245…−165 | — | #9 | §4 C1 "OD-C03 pump cradle" | text | rear-most z −245 is 60 mm from the rear edge z −305 |
| X-12 | Pump OD-H01 body extent (placed in machine frame, x only) | the pump spans x −66.45 … +55.5 with its outlet toward −X | mm | x −66.45…+55.5 | — | #9 | §4 C1 "OD-C03 pump cradle" | text | no z (depth toward the rear edge) extent of the pump body itself is stated anywhere read; see §4 gap |
| X-13 | OD-C03 own build envelope (local frame, before placement) | 80.0 × 40.0 × 52.0 (x ±40.0, y 0.0…40.0, z −10.0…42.0) | mm | 80.0 × 40.0 × 52.0 | ±0.1 (U-02) | #11 | §4 C1; §5 U-02 | text | local frame, not machine frame; OD-C01 spec's placed foot box (X-11) is the already-transformed value |
| X-14 | Bulkhead OD-C02 rear end (z) | wall z −240.0 … −30.0; base rail and top rail along the same z span; envelope z −240 … −30 | mm | −240…−30 | ±0.1 (U-02) | #10 | §4 C1; §5 U-02 | text | rear-most z −240 is 65 mm from the OD-C01 rear edge z −305 |
| X-15 | Bulkhead OD-C02 height | wall from the plate y 0 up to y 215.0; top rail y 207.0 … 215.0 | mm | y 0…215.0 | ±0.1 (REQ-06) | #10 | §4 C1; §5 REQ-06 | text | A-06 OPEN: machine ≈ 260 tall with feet |
| X-16 | Machine height (assumption, OD-C01) | machine height ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet | mm | ≈260 | — | #9 | §6 A-16 | text | flagged: unconfirmed assumption (A-16 OPEN); "plus feet" height not quantified |
| X-17 | Machine height (assumption, OD-C02, cross-reference) | the machine ≈ 260 with feet (OD-C01 A-16); the carrier's plate top at y 210, top panel above 215 | mm | ≈260; y 210; y 215 | — | #10 | §6 A-06 | text | flagged: unconfirmed assumption (A-06 OPEN) |
| X-18 | Water tank zone (reserved, OD-C01) | OD-W01 with its dock OD-C06 stands within x ±70, z −305 … −250 | mm | x ±70; z −305…−250 | — | #9 | §4 C1 "Reserved zones"; §6 A-07 | text | A-07 OPEN; touches the rear edge z −305 directly |
| X-19 | Electronics zone (reserved, OD-C01) | the electronics bay x 70 … 120, z −240 … −30 (A-08) | mm | x 70…120; z −240…−30 | — | #9 | §4 C1 "Reserved zones"; §6 A-08 | text | A-08 OPEN |
| X-20 | Electronics zone intrusion limit (OD-C02) | nothing of the bulkhead at x > 71.0; base rail reaches x 71 (1 mm into the bay zone x ≥ 70); top rail reaches x 70.5 | mm | x ≤ 71.0 / 70.5 | — | #10 | §5 REQ-08; §6 A-07 | text | A-07 OPEN |
| X-21 | Drip tray zone (reserved, OD-C01) | x ±75, z −15 … +85 on the plate under the mouth at (0, 32); cup rest top ≤ 36.9 above the plate | mm | x ±75; z −15…+85; ≤36.9 | — | #9 | §4 C1 "Reserved zones"; §6 A-06 | text | A-06 OPEN; not near the rear edge, included for the overall plate layout picture |
| X-22 | Tank seat OD-W03 — flange / envelope (datum frame STEP) | bbox max [42.408, 14.574, 28.312]; min [−42.388, −14.858, −3.1]; size [84.796, 29.432, 31.412] | mm | as given | — | #12 | §2 Deliverables table (`OD-W03_datum.step`) | table | scan-derived, BAND_NOT_MET (verdict); not caliper-confirmed (L1) |
| X-23 | Tank seat OD-W03 — hose nipple (barb) shank radius, cups A / B | barb_shank_r [2.683, 2.549] | mm | 2.683 / 2.549 (radius) | ±0.14 | #12 | §5 parameter table | table | scan-derived, flagged: not caliper-confirmed (L1); Tier-1 ungated (coverage 0/12) |
| X-24 | Tank seat OD-W03 — hose nipple (barb) tip radius, cups A / B | barb_tip_r [2.871, 2.751] | mm | 2.871 / 2.751 (radius) | ±0.12 | #12 | §5 parameter table | table | scan-derived, not caliper-confirmed |
| X-25 | Tank seat OD-W03 — hose nipple lip radius, cups A / B | barb_lip_r [3.439, 3.419] | mm | 3.439 / 3.419 (radius) | ±0.07; "critical: yes" | #12 | §5 parameter table | table | scan-derived, flagged critical per the source table; not caliper-confirmed |
| X-26 | Tank seat OD-W03 — hose nipple bore radius | 1.214 | mm | 1.214 (radius) | ±0.21 | #12 | §5 parameter table | table | scan-derived, not caliper-confirmed |
| X-27 | Tank seat OD-W03 — cup pitch (spacing between the two hose nipples) | 38.97 | mm | 38.97 | ±0.01; "critical: yes" | #12 | §5 parameter table; also intake/alignment.json#clock.detail.separation_mm | table | scan-derived, flagged critical; not caliper-confirmed |
| X-28 | Tank seat OD-W03 — ear lug fixing holes | lug_hole_r [2.079, 2.107]; lug_hole_cx [−38.553, 38.508]; lug_hole_cy [−0.08, −0.142] | mm | radius 2.079/2.107; cx −38.553/38.508; cy −0.08/−0.142 | ±0.1; "critical: yes" (radius) | #12 | §5 parameter table | table | scan-derived, flagged critical; not caliper-confirmed |
| X-29 | Tube OD-W11 (tank → flowmeter) length code | Tube L270 (tank → flowmeter), silicone | — | L270 | — | #8 | row OD-W11 | table | no diameter given in this row |
| X-30 | Tube OD-W12 length code | Tube L150, silicone | — | L150 | — | #8 | row OD-W12 | table | no diameter given; relation to the back panel's tube pass-throughs not stated |
| X-31 | Routing-reserve tube OD-F04 | Food-safe silicone tube 4×2 mm (routing reserve), 1 m | mm | 4×2 mm | — | #8 | row OD-F04 | table | "4×2 mm" not broken into OD/ID by the source; qty 1 m |
| X-32 | Water flow path — tube callouts (no sizes) | tube 1 pump→3-way valve; tube 2 valve→thermoblock; TUBE 3 valve→tank (bypass/over-pressure return); tube 4 thermoblock→connector; tube 5/6/7 group/steam (phase 2 / coffee path) | — | — | — | #7 | "From docs/WATER_FLOW.md" table | table | TUBE 3 (the bypass return through the back panel per REQUEST.md) carries no diameter in any input read |

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-33 | BOM identity and scope | "OD-C11, Back panel (removable — 4 screws), ASA, printed" | #6 | REQUEST.md, line 3 (BOM row quote) |
| X-34 | BOM row (csv), OD-C11 | `OD-C11,OD-C00,PRINT,Back panel (removable — 4 screws),,,1,DESIGN,ASA,printed,print,,proposed` | #8 | bom_rows.csv, row OD-C11 |
| X-35 | Order of work | "chassis/README order of work row 11" (REQUEST.md); PROJECT_RULES.md order-of-work table row 11: "`OD-C10`, `OD-C11` top and back panels" / Designed against: "`OD-C01`, `OD-C02`" / Blocked by: "—" | #6, #7 | REQUEST.md line 3; PROJECT_RULES.md "Order of work" table, row 11 |
| X-36 | Removable with 4 screws | "SOURCING_GUIDE §6 rule 4: top and back panels removable with 4 screws each" | #6 | REQUEST.md, line 4 |
| X-37 | Serviceability rule | "**Serviceability is the point.** The Dedica's worst trait (thesis: "very difficult to disassemble") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #7 | PROJECT_RULES.md, "6. Chassis Design Rules", rule 4 |
| X-38 | Two-zone layout rule | "**Two-zone layout.** Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #7 | PROJECT_RULES.md, rule 1 |
| X-39 | Anti-vibration rule | "**Copy OEM anti-vibration.** Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #7 | PROJECT_RULES.md, rule 2 |
| X-40 | Thermal map / material-by-zone rule | "**Respect the thermal map.** Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #7 | PROJECT_RULES.md, rule 3 |
| X-41 | Mains safety spec | "**Safety spec carries over:** piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #7 | PROJECT_RULES.md, rule 7 |
| X-42 | Group head / mug clearance rule | "**Design for the mug.** Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec." | #7 | PROJECT_RULES.md, rule 5 |
| X-43 | Chassis hardware standard | "M3 heat-set inserts + M3 screws (the thesis tapped printed holes; inserts are better)" | #7 | PROJECT_RULES.md, "3.10 Chassis hardware" |
| X-44 | Fastener BOM rows | "OD-F01,OD-000,STD,M3 heat-set insert (Ø4.0 bore × 6; 26 in the chassis),,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo" / "OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo" | #8 | bom_rows.csv, rows OD-F01, OD-F02 |
| X-45 | Mains cord row | "OD-E06,OD-E00,OEM,Power supply cord with plug (region-specific; AU code shown),53,5013276449,1,ENVELOPE,,FixPart / generic,8,,todo" | #8 | bom_rows.csv, row OD-E06 |
| X-46 | IEC inlet alternative row | "OD-E60,OD-E00,STD,IEC inlet with fuse (alternative to OD-E06),,,1,VENDOR,,TME / AliExpress,4,,todo" | #8 | bom_rows.csv, row OD-E60 |
| X-47 | Cord / IEC inlet text | "The mains cord OD-E06 (or the IEC inlet OD-E60) and the cable grommet OD-C14 leave the machine" | #6 | REQUEST.md, line 4-5 |
| X-48 | Cable grommet row | "OD-C14,OD-C00,PRINT,Cable strain relief / grommet,,,2,DESIGN,TPU,printed,print,,proposed" | #8 | bom_rows.csv, row OD-C14 |
| X-49 | Tube entry text | "the water tank stands on the table for now, so its two tubes (OD-W11 to the flowmeter, TUBE 3 back from the 3-way valve) enter the machine from outside" | #6 | REQUEST.md, line 5-7 |
| X-50 | Tank seat as reference | "its two tubes (tank → flowmeter OD-W11, and the bypass return TUBE 3) therefore enter the machine from outside" / "the tank seat OD-W03 (BOM name "Tray gasket", the "tray" the Usta refers to) is the scanned reference for the tank's ports" | #6 | REQUEST.md, "Orchestrator's reading of the request" |
| X-51 | Tube rows (csv) | "OD-W11,OD-W00,OEM,Tube L270 (tank → flowmeter),31,5313219841,1,ENVELOPE,silicone,4delonghi,4,,todo" / "OD-W12,OD-W00,OEM,Tube L150,33,5313236101,1,ENVELOPE,silicone,FixPart,4,,todo" | #8 | bom_rows.csv, rows OD-W11, OD-W12 |
| X-52 | Routing-reserve tube row | "OD-F04,OD-000,STD,Food-safe silicone tube 4×2 mm (routing reserve),,,1 m,ENVELOPE,silicone,AliExpress,5,,todo" | #8 | bom_rows.csv, row OD-F04 |
| X-53 | Tank seat BOM row | "OD-W03,OD-W01,OEM,Tray gasket (water tank seat — white seat with 2 barbed ports + black double gasket),30,5313236391,1,SCAN,,4delonghi,3,#37,modeled" | #8 | bom_rows.csv, row OD-W03 |
| X-54 | Usta's words (verbatim, project thread "Chassis C08 C10 C11", 2026-10-01 10:58Z) | "what can start now please initiate it" / "water tank is transparent hard to scan we can just use the tray that step converted as reference and i will hold water tank on the table myself no need to design for it now" / "c08 i will use original pcb for this stage" | #6 | REQUEST.md, "The Usta's words" |
| X-55 | Standing instruction | "Design every 3D-printable part of open-dedica (OD-G01, OD-C01 … C16, OD-T01) with the pipeline, in the order of `chassis/README.md`; ask the Usta only where a decision is needed; write open questions as `A-##` rows in the ledger and proceed. Every scan- or report-derived value is an assumption until the Usta confirms it; calipers beat scans." | #6 | REQUEST.md, "Standing instruction" |
| X-56 | Data class | "Data class PUBLIC (CC BY 4.0)." | #6 | REQUEST.md, "Standing instruction" |
| X-57 | Machine profiles / printers | "Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into `oguz-atolye/atolye/machines/`." | #7 | PROJECT_RULES.md, "Order of work" section, after the table |
| X-58 | K1C build volume (assumption carried from OD-C02) | "220 × 220 × 250 (Creality specification, not in the machine file)" | #10 | OD-C02 spec, §6 A-08 |
| X-59 | Kobra Max 3 build volume (assumption carried from OD-C01) | "420 × 420 × 500 (Anycubic specification, not in the machine file)" | #9 | OD-C01 spec, §6 A-09 |
| X-60 | OD-C01 material note (cross-reference) | "PETG (BOM says ASA; the large flat plate prints in PETG on the open Kobra, SOURCING_GUIDE §6 rule 3, A-10)" | #9 | OD-C01 spec, §3 process table |
| X-61 | OD-C02 material | "ASA (BOM: ASA)" | #10 | OD-C02 spec, §3 process table |
| X-62 | Side/top/dock/bay/grommet/feet not designed | "the side panels OD-C12/C13, the top panel OD-C10, the tank dock OD-C06, the electronics bay OD-C08, the grommet OD-C14 and the feet OD-C15 are not designed: everything about them is a gap for section 4" | brief | WP-01_intake.md, "What the job is for" |
| X-63 | Delivered neighbours confirmed | "Delivered neighbours: OD-C01 base frame (spec 1.2), OD-C02 bulkhead (spec 1.2), OD-C03, OD-C04, OD-C05 (spec 2.2), OD-C07; all in the OD-C01 machine frame (X right, +Y up, +Z front, plate top y = 0)." | #6 | REQUEST.md, "Orchestrator's reading of the request" |
| X-64 | Top panel inserts in the bulkhead (interface OD-C11 will sit alongside) | "two Ø4.0 ± 0.05 blind bores along −Y from y 215.0, depth 6.0 ± 0.1, at (x 65.0, z −60.0) and (65.0, −210.0)" for OD-C10 | #10 | OD-C02 spec, §5 REQ-07 |

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-33, X-34, X-57, X-60, X-61 | The BOM (bom_rows.csv, REQUEST.md) names OD-C11's material as ASA; the machine-profile note (X-57) assigns "large panels: PETG" to the open Kobra Max 3, while K1C (enclosed) is named for ASA/PC; OD-C01's own spec overrode its BOM-listed ASA to PETG for warp reasons on the open Kobra (X-60). Which printer and material does OD-C11 use — K1C/ASA as the BOM states, or does the same open-bed warp concern that moved OD-C01 to PETG apply to the back panel? |
| 2 | X-01, X-14, X-15, X-19, X-20 | What does OD-C11 fasten to? No input gives a back-panel interface: no insert pattern, standoff, or edge the panel screws into on OD-C01, OD-C02, or the (undesigned) side/top panels. The bulkhead OD-C02 ends at z −240 (65 mm forward of the rear edge z −305) and the plate's insert pattern stops at z −225; nothing read states what structure exists at z −240…−305 for the panel's 4 screws to land in. |
| 3 | X-45, X-46, X-47 | What are the mains cord (OD-E06) or IEC inlet (OD-E60) pass-through size and position on OD-C11? No input gives a cable diameter, a cutout size, or a location. |
| 4 | X-29, X-30, X-31, X-32, X-49, X-50 | What are the two tank tubes' (OD-W11 to the flowmeter, and TUBE 3 the bypass return) pass-through sizes and positions on OD-C11? No input gives an outer tube diameter for OD-W11 or TUBE 3 (OD-W12's "L150" code is likewise undimensioned), nor a position relative to the tank seat OD-W03's two hose nipples (X-23…X-27) or the panel. |
| 5 | X-48 | What is the cable grommet OD-C14's size, shape, and mounting (it is "proposed" in the BOM, material TPU, qty 2, and is itself a separate not-yet-designed part per the brief)? Does OD-C11 carry a grommet boss/hole, and where? |
| 6 | X-38, X-41 | Does OD-C11 need ventilation (for the electric zone behind it, or the two-zone drainage/safety rules X-38, X-41), and if so what openings, sizes, and positions? No input states a ventilation requirement or opening for the back panel specifically. |
| 7 | X-18, X-62 | How does OD-C11 meet the side panels OD-C12/C13 and the top panel OD-C10? None of the three are designed (BOM status "proposed"); no edge profile, overlap, or joint is given for the back panel's left, right, or top edges. |
| 8 | X-62 | The feet OD-C15 are not designed (BOM "proposed", material TPU, qty 4). Do the back panel's bottom screws or edge interact with the feet or with OD-C01's existing feet holes (X-06) in any way? |
| 9 | X-33, X-60, X-61 | OD-C11's material is ASA per the BOM/REQUEST (X-33, X-34); is this confirmed, or does it get the same per-part review (as OD-C01's A-10, OD-C02's A-09) the Usta has not yet ratified? |
| 10 | X-58, X-59 | Both the K1C (X-58) and Kobra Max 3 (X-59) build volumes are recorded only as "memory of the spec sheet, not in the machine file" in the OD-C01 and OD-C02 assumption ledgers; no input gives a confirmed, sourced build volume for either printer. Which machine prints OD-C11, and what is its confirmed build volume? |
| 11 | X-12 | No input states the pump OD-H01's rear-most (z, toward the back panel) extent — only its x-span (x −66.45 … +55.5) is given in the OD-C01 spec text that was read. Is a pump z-extent needed for OD-C11's clearance, and if so where is it recorded? |
| 12 | X-22 … X-28 | The OD-W03 tank-seat STEP is delivered at verdict BAND_NOT_MET (accepted by Ikbal on a decision card, not by the Usta of this job) with declared interior/underside invention (wall_t 1.2 mm assumed) and zero of 12 Tier-1 dimensions caliper-confirmed (L1). Every X-22…X-28 row taken from it is scan-derived and explicitly "Not fit for hose, seal or fixing-hole fit decisions" per its own §13 claim boundary. Does OD-C11's tube/port layout proceed on these scan values, or does it wait for calipers? |
| 13 | X-37, X-62 | PROJECT_RULES X-37 says "gaskets replaceable without unhousing the thermoblock" as part of serviceability; does OD-C11 carry any gasket or seal itself, or is this only about other parts? No input names a gasket for the back panel. |

## §5 Unreadable

None. Every file listed in the brief under 00_Spec/inputs/ was located and either hashed (the five STEP files, per intake rule 6) or read in full (the seven markdown/csv files).
