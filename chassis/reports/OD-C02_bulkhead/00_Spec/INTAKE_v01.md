# INTAKE v01 — 20260930-od-c02-bulkhead

Intake: Claude Code, Sonnet 5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-09-30

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
| 1 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP | — | listed and hashed only (intake rule 6); geometry measured later |
| 2 | 00_Spec/inputs/OD-C03_pump_cradle.step | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | 192751 | STEP | — | listed and hashed only |
| 3 | 00_Spec/inputs/OD-C04_thermoblock_mount.step | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 | 128306 | STEP | — | listed and hashed only |
| 4 | 00_Spec/inputs/OD-G01_housing_C1_v02.step | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | 437578 | STEP | — | listed and hashed only |
| 5 | 00_Spec/inputs/OD-H01_ulka_ep5_pump.step | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | 824180 | STEP | — | listed and hashed only |
| 6 | 00_Spec/inputs/OD-H11_thermoblock.step | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | 2400893 | STEP | — | listed and hashed only |
| 7 | 00_Spec/inputs/REQUEST.md | 028bb47758e4a5b808990249566bf41814d32ea291f0809c52b62dfe86e9a061 | 2171 | Markdown | 1 (full text) | read fully |
| 8 | 00_Spec/inputs/PROJECT_RULES.md | 78488c5959fb7173c53435053b2dfd57c6a8fb0cbf51bcd1a34244bf5dd12d07 | 9127 | Markdown | 1 (full text; excerpts of chassis/README.md, SOURCING_GUIDE.md §5/§6, WATER_FLOW.md, README.md safety note, issue #9) | read fully |
| 9 | 00_Spec/inputs/bom_rows.csv | bf80fe744a508d3e0e2198d53a41ba1c90f2c0f2e39fa2df538271a77f874c4a | 5546 | CSV | 55 rows | read fully |
| 10 | 00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | 25226 | Markdown | 1 (full text, §1–§8) | read fully |
| 11 | 00_Spec/inputs/reports/OD-C01_base_frame/REPORT_od_c01_frame_v02.md | 78a03e899b024380df0d0bce9495ad3184ed13a0c454b8a2815a113e4d3bea7b | 38096 | Markdown | 1 (full text, §1–§10 + JSON block) | read fully |
| 12 | 00_Spec/inputs/reports/OD-C04_thermoblock_mount/DESIGN_SPEC_v1.2.md | 388f7fd170b4313cc53d5039d4db6f2eefdc79bca93c64c44ebe7e9563970b8c | 17938 | Markdown | 1 (full text, §1–§8) | read fully |
| 13 | 00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v2.1.md | fb1885a818f925393ae756b31ea1c915452c053b17ec7a09555bd9a0b859095a | 27045 | Markdown | 1 (full text, §1–§8) | read fully |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | Machine frame | X to the user's right, +Y up, +Z toward the user (front); plate top face y = 0 | — | — | — | #7, #10 | REQUEST.md text; DESIGN_SPEC_v1.2 (OD-C01) §2 | text | — |
| X-02 | Bulkhead wall plane | x = 65 | mm | 65.00 | — | #7, #10 | REQUEST.md text; OD-C01 spec §4 A-04, REQ-04 | text | — |
| X-03 | Bulkhead z extent | z −240 to z −30 | mm | z −240.00 … −30.00 | — | #7, #10 | REQUEST.md text; OD-C01 spec §4 A-04 | text | — |
| X-04 | Bulkhead insert hole 1 position | (x 65, z −45) | mm | (65.00, −45.00) | offset ≤ 0.10 (REQ-04) | #7, #10, #11 | REQUEST.md; OD-C01 spec §4, §5 REQ-04; REPORT gate REQ-04 | text / gate row | — |
| X-05 | Bulkhead insert hole 2 position | (65, −105) | mm | (65.00, −105.00) | offset ≤ 0.10 (REQ-04) | #7, #10, #11 | same as X-04 | text / gate row | — |
| X-06 | Bulkhead insert hole 3 position | (65, −165) | mm | (65.00, −165.00) | offset ≤ 0.10 (REQ-04) | #7, #10, #11 | same as X-04 | text / gate row | — |
| X-07 | Bulkhead insert hole 4 position | (65, −225) | mm | (65.00, −225.00) | offset ≤ 0.10 (REQ-04) | #7, #10, #11 | same as X-04 | text / gate row | — |
| X-08 | Bulkhead insert hole diameter | Ø4.0 ± 0.05 | mm | 4.00 | ± 0.05 | #10, #11 | OD-C01 spec §5 REQ-04; REPORT gate REQ-04 (measured 4.000, offset 0.000) | gate row | — |
| X-09 | Insert type for bulkhead holes | M3 × 5.7 × Ø4.6 heat-set insert (A-11), through-hole Ø4.0 in a 6.0 plate | mm | — | — | #10 | OD-C01 spec §6 A-11 | text (assumption) | not confirmed |
| X-10 | Plate top face (floor plane) | y = 0.00 ± 0.10 | mm | 0.00 | ± 0.10 | #10, #11 | OD-C01 spec §5 REQ-07; REPORT gate REQ-07 (measured max_y 0.000) | gate row | — |
| X-11 | Plate thickness | 6.0 ± 0.1, y −6.0 … 0 | mm | 6.00 | ± 0.1 | #10, #11 | OD-C01 spec §4 C1, §5 REQ-07; REPORT §5 | text / gate row | — |
| X-12 | Plate envelope (for reference: this is OD-C01, not OD-C02) | 240.0 × 6.0 × 405.0 (x ±120, y −6…0, z −305…+100) | mm | 240.00 × 6.00 × 405.00 | ± 0.1 each | #10, #11 | OD-C01 spec §4 C1, §5 U-02; REPORT §5 | gate row | — |
| X-13 | Drain hole 1 position | (x −80, z −120) | mm | (−80.00, −120.00) | offset ≤ 0.10 (REQ-06) | #7, #10, #11 | REQUEST.md; OD-C01 spec §4, §5 REQ-06; REPORT gate REQ-06 | text / gate row | — |
| X-14 | Drain hole 2 position | (−80, −230) | mm | (−80.00, −230.00) | offset ≤ 0.10 (REQ-06) | #7, #10, #11 | REQUEST.md; OD-C01 spec §4, §5 REQ-06; REPORT gate REQ-06 | text / gate row | — |
| X-15 | Drain hole diameter | Ø8.0 ± 0.1 | mm | 8.00 | ± 0.1 | #10, #11 | OD-C01 spec §5 REQ-06; REPORT gate REQ-06 (measured 8.000) | gate row | — |
| X-16 | Electric zone | everything at x ≥ 70 | mm | x ≥ 70.00 | — | #7 | REQUEST.md text | text | — |
| X-17 | Electronics bay OD-C08 zone | x 70 … 120, z −240 … −30 | mm | x 70.00 … 120.00, z −240.00 … −30.00 | — | #7, #10 | REQUEST.md text; OD-C01 spec §4 A-08 (reserved zone, "reported, not gated") | text (reserved zone) | not confirmed |
| X-18 | Wet zone | everything at x < 65 | mm | x < 65.00 | — | #7 | REQUEST.md text | text | — |
| X-19 | Wires that must cross the bulkhead | pump, thermoblock heater and thermostat, the flowmeter's Hall sensor, the valve solenoid | — | — | — | #7 | REQUEST.md text | text | not confirmed; no wire gauges given |
| X-20 | Pump cradle OD-C03 foot | x −10 … 42, z −245 … −165 | mm | x −10.00 … 42.00, z −245.00 … −165.00 | — | #7, #10 | REQUEST.md text; OD-C01 spec §4 A-03 | text | — |
| X-21 | Pump OD-H01 envelope (placed) | pump spans x −66.45 … +55.5 at y ≈ 40 | mm | x −66.45 … 55.50, y ≈ 40.00 | — | #7 | REQUEST.md text | text | — |
| X-22 | Pump spade terminal side | "spade terminals on its −Y side" | — | — | — | #7 | REQUEST.md text (quote) | text | photo/scan-derived, not confirmed for fit |
| X-23 | Pump terminal block orientation as placed | "the terminal block (its −Y) up" | — | — | — | #10 | OD-C01 spec §4 A-03 | text | not confirmed |
| X-24 | Pump outlet direction as placed | "the outlet (its −Z) toward −X where the valves sit" | — | — | — | #10 | OD-C01 spec §4 A-03 | text | not confirmed |
| X-25 | Pump clearance to electronics zone (placed) | OD-H01 to electronics zone x 70…120, z −240…−30: 14.5 | mm | 14.50 | — | #11 | REPORT §5 reserved-zone table | measured (house tool, house rig) | reported, not gated |
| X-26 | Pump cradle clearance to electronics zone (placed) | OD-C03 to electronics zone: 28.0 | mm | 28.00 | — | #11 | REPORT §5 reserved-zone table | measured | reported, not gated |
| X-27 | Thermoblock mount OD-C04 foot | x ±50, z −157 … −107 | mm | x −50.00 … 50.00, z −157.00 … −107.00 | — | #7, #10 | REQUEST.md text; OD-C01 spec §4 A-02 | text | — |
| X-28 | Thermoblock mount foot edge toward bulkhead | x 50 | mm | 50.00 | — | #10 | OD-C01 spec §4 A-02 (foot x ±50) | text | — |
| X-29 | Thermoblock outlet pins reach | z −89.21 (its z 50.79 in its own frame) | mm | −89.21 | — | #10, #11 | OD-C01 spec §4, §5 REQ-08; REPORT gate REQ-08 (measured −89.210) | text / gate row | — |
| X-30 | Thermoblock casting behind-line assumption | casting stays behind z −85 (OD-C05 A-05 assumes) | mm | ≤ −85.00 | — | #10 | OD-C01 spec §4 | text (assumption) | not confirmed |
| X-31 | Thermoblock mount lowest point above plate | 16.5 above the plate (spec text); measured 16.4925 | mm | 16.50 (spec text); 16.4925 (measured) | — | #10, #11 | OD-C01 spec §4, §3; REPORT §3 gate U-03/REQ-08 | text / gate row | conflicts: 16.5 (spec prose, rounded) vs 16.4925 (measured, REPORT K-2 note: "0.0075 under spec §3/§4's rounded 16.5") |
| X-32 | Thermoblock/mount terminals and pipes direction | "the casting's terminals and pipes point up" | — | — | — | #7 | REQUEST.md text | text | not confirmed |
| X-33 | Thermoblock terminals/pipes orientation in mount frame | "+Y, INTAKE X-51 … X-84 face up (A-07)"; "−Y points down" | — | — | — | #12 | OD-C04 DESIGN_SPEC §2, A-07 | text (assumption) | not confirmed |
| X-34 | Thermoblock mount clearance to OD-H11 (air gap) | clearance(mount, OD-H11) ≥ 10.0, measured 16.4925 | mm | ≥ 10.00 (req); 16.4925 (measured) | — | #12 | OD-C04 spec §5 REQ-01 | text (requirement) | — |
| X-35 | Group head carrier OD-C05 foot | x ±55, z −70 … −26 | mm | x −55.00 … 55.00, z −70.00 … −26.00 | — | #7, #10 | REQUEST.md text; OD-C01 spec §4 A-01 | text | — |
| X-36 | Carrier column position toward bulkhead | column at x 55 (per side walls |x| 51…55 in OD-C05's own frame, mapped) | mm | 55.00 | — | #7, #13 | REQUEST.md text ("column to y 210"); OD-C05 spec §4 (side walls |x| 51.0…55.0) | text | — |
| X-37 | Carrier wall/column extent (machine frame) | wall z −26 … −20 up to y 210 | mm | z −26.00 … −20.00, up to y 210.00 | — | #10 | OD-C01 spec §4 A-01 | text | — |
| X-38 | Carrier plate (machine frame) | z −26 … +82 at y 205 … 210 | mm | z −26.00 … 82.00, y 205.00 … 210.00 | — | #10 | OD-C01 spec §4 A-01 | text | — |
| X-39 | Carrier clearance to electronics zone | 26.41 (OD-G01) | mm | 26.41 | — | #11 | REPORT §5 reserved-zone table | measured | reported, not gated |
| X-40 | Carrier foot box gap to tray zone | 11.0 | mm | 11.00 | — | #11 | REPORT §5 | measured | reported, not gated |
| X-41 | Machine overall height | ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet | mm | ≈ 260.00 | — | #7, #10 | REQUEST.md text ("OD-C01 A-16"); OD-C01 spec §6 A-16 | text (assumption) | not confirmed |
| X-42 | Water path: Pump → 3-way valve | TUBE 1, cold, up to 15 bar | — | — | — | #8 | PROJECT_RULES.md, WATER_FLOW.md table row 3 | table | — |
| X-43 | Water path: 3-way valve → Thermoblock | TUBE 2, cold, pressurised | — | — | — | #8 | PROJECT_RULES.md, WATER_FLOW.md table row 4 | table | — |
| X-44 | Water path: 3-way valve → tank (bypass) | TUBE 3, cold | — | — | — | #8 | PROJECT_RULES.md, WATER_FLOW.md table row 5 | table | — |
| X-45 | Water path: Thermoblock → 3-way valve connector port A | TUBE 4, hot; NTC OD-H16 and TCO 192 °C OD-H18 sit on the thermoblock | — | — | — | #8 | PROJECT_RULES.md, WATER_FLOW.md table row 6 | table | — |
| X-46 | Water path: Connector port C → Group head / portafilter | TUBE 7, hot, coffee path | — | — | — | #8 | PROJECT_RULES.md, WATER_FLOW.md table row 7 | table | — |
| X-47 | TUBE 7 diameter assumption (from OD-C05 job, not this job's input directly measured) | "the hot water tube (TUBE 7, ≈ Ø8 silicone, INTAKE X-77, X-78)" | mm | ≈ 8.00 | — | #13 | OD-C05 spec §6 A-07 | text (assumption) | not confirmed |
| X-48 | Routing-reserve tube (BOM) | Food-safe silicone tube 4×2 mm | mm | 4.00 × 2.00 | — | #9 | bom_rows.csv row OD-F04 | table (csv) | — |
| X-49 | Tube numbering note | "TUBE 1–7 follow the numbering of the community EC685M flow diagram...Only the first two tubes (OD-W11, OD-H25) have been matched to BOM lines so far. The rest will be matched to OD-W12…W15 during teardown." | — | — | — | #8 | PROJECT_RULES.md, WATER_FLOW.md text | text (quote) | not confirmed; tube runs do not exist yet (no scan) |
| X-50 | Reserved zone: drip tray | x ±75, z −15 … +85 on the plate under the mouth at (0, 32) | mm | x −75.00 … 75.00, z −15.00 … 85.00 | — | #10 | OD-C01 spec §4 A-06 | text (reserved zone) | not confirmed |
| X-51 | Reserved zone: water tank | x ±70, z −305 … −250 | mm | x −70.00 … 70.00, z −305.00 … −250.00 | — | #10 | OD-C01 spec §4 A-07 | text (reserved zone) | not confirmed |
| X-52 | Reserved zone: valve/flowmeter mount OD-C07 | x −117 … −67, z −154 … −35 | mm | x −117.00 … −67.00, z −154.00 … −35.00 | — | #10 | OD-C01 spec §4 A-05 | text (reserved zone) | not confirmed |
| X-53 | Fastener standard | M3 heat-set inserts (OD-F01) in OD-C01, M3 × 8 screws (OD-F02) | — | — | — | #7, #9, #10, #12, #13 | REQUEST.md, bom_rows.csv rows OD-F01/OD-F02, OD-C01/OD-C04/OD-C05 specs §2 | table / text | — |
| X-54 | K1C build volume (memory, not in machine file) | 220 × 220 × 250 (Creality specification) | mm | 220.00 × 220.00 × 250.00 | — | #12, #13 | OD-C04 spec §6 A-09; OD-C05 spec §6 A-08 | text (assumption, "memory of the spec sheet") | not confirmed; not read from an actual machine profile file |
| X-55 | Kobra Max 3 build volume (memory, not in machine file) | 420 × 420 × 500 (Anycubic specification) | mm | 420.00 × 420.00 × 500.00 | — | #10 | OD-C01 spec §6 A-09 | text (assumption, "memory of the spec sheet") | not confirmed; not read from an actual machine profile file |
| X-56 | OD-C02 material per BOM | ASA | — | — | — | #9 | bom_rows.csv row OD-C02 | table (csv) | — |
| X-57 | OD-C02 BOM description | "Wet/electric bulkhead with drainage path" | — | — | — | #9 | bom_rows.csv row OD-C02 | table (csv) | — |
| X-58 | OD-C02 BOM process/status | PRINT, DESIGN (cad column), "print" source, status "proposed" | — | — | — | #9 | bom_rows.csv row OD-C02 | table (csv) | — |
| X-59 | Bulkhead section cut area at x = 65 (OD-C01 plate) | cut 2334.00 mm² | mm² | 2334.00 | — | #11 | REPORT §1 file table (section od_c01_frame_v02_left_x65_bulkhead.png) | measured (section) | for reference only; this is OD-C01's plate cut at the bulkhead line, not OD-C02 itself |
| X-60 | Bulkhead insert holes web-to-edge / hole-to-hole context (OD-C01 plate) | "hole webs" table entries near drain and OD-C07 holes | mm | various (see REPORT §5) | — | #11 | REPORT §5 "Hole webs" | measured | informational; none of the listed webs is measured to the four bulkhead insert holes specifically |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-61 | Two-zone layout, printed bulkhead | "**Two-zone layout.** Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 1 |
| X-62 | Anti-vibration | "**Copy OEM anti-vibration.** Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 2 |
| X-63 | Thermal map | "**Respect the thermal map.** Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 3 |
| X-64 | Serviceability | "**Serviceability is the point.** The Dedica's worst trait (thesis: \"very difficult to disassemble\") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 4 |
| X-65 | Mug clearance / envelope | "**Design for the mug.** Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 5 |
| X-66 | Sensor bosses reserved from day one | "**Pre-infusion & preheat are software.** ... Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 6 |
| X-67 | Safety spec | "**Safety spec carries over:** piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §6 rule 7 |
| X-68 | Safety note (electrical/wet separation) | "⚠️ **Safety:** this machine runs on mains voltage (230 V / 120 V), heats water to ~125 °C and pressurizes it to 15 bar. Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA." | #8 | PROJECT_RULES.md, README.md safety note |
| X-69 | Order of work: OD-C02 | "OD-C02 wet/electric bulkhead | OD-C01, the tube runs | —" (row 8 of the chassis order-of-work table) | #8 | PROJECT_RULES.md, chassis/README.md order-of-work table |
| X-70 | Order of work: panels designed against OD-C01 and OD-C02 | "OD-C10, OD-C11 top and back panels | OD-C01, OD-C02 | —" (row 11); "OD-C12, OD-C13 side panels; OD-C16 corner brackets | OD-C01 | acrylic option is the Usta's call" (row 12) | #8 | PROJECT_RULES.md, chassis/README.md order-of-work table |
| X-71 | Order of work: electronics bay tray | "OD-C08 electronics bay tray | OD-E01, OD-E02 (path 1) or OD-E51…E58 (path 2) | the Usta picks the path" (row 9) | #8 | PROJECT_RULES.md, chassis/README.md order-of-work table |
| X-72 | Machine profiles named | "Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into oguz-atolye/atolye/machines/." | #8 | PROJECT_RULES.md, chassis/README.md |
| X-73 | Deliverable format per part | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #8 | PROJECT_RULES.md, chassis/README.md Goal |
| X-74 | Standing instruction: pipeline and assumption discipline | "design every 3D-printable part of Open Dedica (OD-G01, OD-C01…C16, OD-T01) with the oguz-atolye pipeline; each part needs a parametric build script, STEP, STL/3MF and an independent review verdict; every value from a scan or report is an A-## assumption until the Usta confirms it; calipers beat scans; data class PUBLIC (CC BY 4.0)." | #7 | REQUEST.md, standing instruction of the project, 2026-09-30 |
| X-75 | OD-C02 blocked-by note | "chassis/README.md row 8: designed after OD-C01 and the tube runs; the tube runs do not exist yet (no tube scan), so they are assumption rows." | #7 | REQUEST.md |
| X-76 | Drainage and wire-crossing requirement (job-specific) | "The bulkhead separates the two, carries the drainage path (a leak on the wet side reaches the drain holes at (x −80, z −120) and (−80, −230), never the electric side), and passes the wires that must cross (pump, thermoblock heater and thermostat, the flowmeter's Hall sensor, the valve solenoid) through sealed or raised openings." | #7 | REQUEST.md |
| X-77 | Material/process, OD-C02 BOM row | `OD-C02,OD-C00,PRINT,Wet/electric bulkhead with drainage path,,,1,DESIGN,ASA,printed,print,,proposed` | #9 | bom_rows.csv, row `OD-C02` |
| X-78 | Electronics bay BOM row | `OD-C08,OD-C00,PRINT,Electronics bay tray,,,1,DESIGN,PETG,printed,print,#8,proposed` | #9 | bom_rows.csv, row `OD-C08` |
| X-79 | Front panel BOM row | `OD-C09,OD-C00,PRINT,Front panel with button bezel,,,1,DESIGN,ASA,printed,print,#8,proposed` | #9 | bom_rows.csv, row `OD-C09` |
| X-80 | Top panel BOM row | `OD-C10,OD-C00,PRINT,Top panel (removable — 4 screws),,,1,DESIGN,ASA,printed,print,,proposed` | #9 | bom_rows.csv, row `OD-C10` |
| X-81 | Back panel BOM row | `OD-C11,OD-C00,PRINT,Back panel (removable — 4 screws),,,1,DESIGN,ASA,printed,print,,proposed` | #9 | bom_rows.csv, row `OD-C11` |
| X-82 | Left side panel BOM row | `OD-C12,OD-C00,PRINT,Left side panel,,,1,DESIGN,ASA / PETG or 3 mm acrylic,printed,print,,proposed` | #9 | bom_rows.csv, row `OD-C12` |
| X-83 | Right side panel BOM row | `OD-C13,OD-C00,PRINT,Right side panel,,,1,DESIGN,ASA / PETG or 3 mm acrylic,printed,print,,proposed` | #9 | bom_rows.csv, row `OD-C13` |
| X-84 | Pump BOM row | `OD-H01,OD-H00,OEM,Pump ULKA EP5/EX5 48 W 230 V 15 bar,40,AS00002825,1,SCAN,,AliExpress ULKA EP5 48W 230V / eBay / ulkapumps.com,12–25,#1,modeled` | #9 | bom_rows.csv, row `OD-H01` |
| X-85 | Thermoblock BOM row | `OD-H11,OD-H10,OEM,Thermoblock (generator 230 V 1300 W + plastic connector),60,5513226671,1,SCAN,aluminium casting,AliExpress EC680 thermoblock / espressocoffeeshop,25–40,#2,modeled` | #9 | bom_rows.csv, row `OD-H11` |
| X-86 | Anti-drip valve BOM row | `OD-H21,OD-H00,OEM,Anti-drip valve,39,7313260161,1,SCAN,,FixPart / 4delonghi,5,#41,modeled` | #9 | bom_rows.csv, row `OD-H21` |
| X-87 | 3-way valve BOM row | `OD-H22,OD-H00,OEM,3-way valve,43,AS00004266,1,SCAN,,4delonghi valve BARM30E,5,#6,modeled` | #9 | bom_rows.csv, row `OD-H22` |
| X-88 | 3-way valve connector BOM row | `OD-H23,OD-H00,OEM,3-way valve connector,75,AS00005380,1,CALIPER,,4delonghi,3,#6,todo` | #9 | bom_rows.csv, row `OD-H23` |
| X-89 | Flowmeter BOM row | `OD-H24,OD-H00,OEM,Flowmeter,45,5213225251,1,SCAN,,FixPart / 4delonghi,10–15,#7,modeled` | #9 | bom_rows.csv, row `OD-H24` |
| X-90 | Flowmeter-pump tube BOM row | `OD-H25,OD-H00,OEM,Flowmeter–pump tube,37,AS00005774,1,ENVELOPE,,FixPart,4,,todo` | #9 | bom_rows.csv, row `OD-H25` |
| X-91 | Electronics assembly BOM row (path choice) | `OD-E00,OD-000,ASM,Electronics (choose Path 1 OEM or Path 2 open controller),,,1,DESIGN,,,,#8,todo` | #9 | bom_rows.csv, row `OD-E00` |
| X-92 | Power PCB BOM row (Path 1) | `OD-E01,OD-E00,OEM,Power PCB 230 V — Path 1,59,AS00002829,1,SCAN,,AliExpress 4001101696035 / eBay,35–45,#33,modeled` | #9 | bom_rows.csv, row `OD-E01` |
| X-93 | Control board BOM row (Path 1) | `OD-E02,OD-E00,OEM,Control board assembly (front buttons) — Path 1,15,7313285189,1,SCAN,,FixPart / eBay,15–25,#34,modeled` | #9 | bom_rows.csv, row `OD-E02` |
| X-94 | ESP32 dev board BOM row (Path 2) | `OD-E51,OD-E00,ELEC,ESP32 dev board — Path 2,,,1,VENDOR,3.3 V WiFi,AliExpress,5–10,,todo` | #9 | bom_rows.csv, row `OD-E51` |
| X-95 | Heater SSR BOM row (Path 2) | `OD-E52,OD-E00,ELEC,SSR for heater — Path 2,,,1,VENDOR,≥25 A zero-cross mains-rated,RS / TME (no no-name for mains),8–15,,todo` | #9 | bom_rows.csv, row `OD-E52` |
| X-96 | Pump relay/SSR BOM row (Path 2) | `OD-E53,OD-E00,ELEC,Relay / SSR for pump — Path 2,,,1,VENDOR,≥2 A 230 V,RS / TME,5–12,,todo` | #9 | bom_rows.csv, row `OD-E53` |
| X-97 | Thermocouple BOM row (Path 2) | `OD-E54,OD-E00,ELEC,Thermocouple type K — Path 2,,,1,ENVELOPE,glass-braid,Pimoroni / AliExpress,20 (with OD-E55),,todo` | #9 | bom_rows.csv, row `OD-E54` |
| X-98 | MAX31855 board BOM row (Path 2) | `OD-E55,OD-E00,ELEC,MAX31855 thermocouple board — Path 2,,,1,VENDOR,,Pimoroni / AliExpress,(with OD-E54),,todo` | #9 | bom_rows.csv, row `OD-E55` |
| X-99 | Pressure transducer BOM row (Path 2, optional) | `OD-E56,OD-E00,ELEC,Pressure transducer (optional) — Path 2,,,1,VENDOR,0–300 PSI G1/4,per CaiJonas repo BOM,15,,todo` | #9 | bom_rows.csv, row `OD-E56` |
| X-100 | G1/4 tee BOM row (Path 2, optional) | `OD-E57,OD-E00,STD,G1/4 tee for pressure transducer (optional),,,1,VENDOR,brass; 15 bar / 125 °C rated,hardware / AliExpress,5,,todo` | #9 | bom_rows.csv, row `OD-E57` |
| X-101 | Logic PSU BOM row (Path 2) | `OD-E58,OD-E00,ELEC,Logic PSU — Path 2,,,1,VENDOR,5 V or 24 V,Mean Well-style,10,,todo` | #9 | bom_rows.csv, row `OD-E58` |
| X-102 | SSR heat-sink plate BOM row | `OD-E59,OD-E00,MFG,SSR heat-sink plate,,,1,DESIGN,aluminium,local shop / scrap,—,,proposed` | #9 | bom_rows.csv, row `OD-E59` |
| X-103 | M3 heat-set insert BOM row | `OD-F01,OD-000,STD,M3 heat-set insert,,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo` | #9 | bom_rows.csv, row `OD-F01` |
| X-104 | M3×8 screw BOM row | `OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo` | #9 | bom_rows.csv, row `OD-F02` |
| X-105 | Acrylic sheet BOM row (optional skins) | `OD-F03,OD-000,STD,Acrylic sheet 3 mm (optional skins),,,per design,—,PMMA,local laser / leftover stock,25,,todo` | #9 | bom_rows.csv, row `OD-F03` |
| X-106 | Silicone tube (routing reserve) BOM row | `OD-F04,OD-000,STD,Food-safe silicone tube 4×2 mm (routing reserve),,,1 m,ENVELOPE,silicone,AliExpress,5,,todo` | #9 | bom_rows.csv, row `OD-F04` |
| X-107 | High-temp epoxy (steam port blank) BOM row | `OD-F05,OD-000,STD,High-temp epoxy (steam port blank),,,1,—,125 °C / 15 bar,hardware store,8,,todo` | #9 | bom_rows.csv, row `OD-F05` |
| X-108 | Scan-to-STEP workflow (calipers beat scans) | "**Measure** critical interfaces with calipers: mounting hole patterns, boss diameters, tube spigots, connector pitch. Interfaces must be caliper-accurate — scans are for envelopes, calipers are for fits." | #8 | PROJECT_RULES.md, docs/SOURCING_GUIDE.md §5 step 2 |
| X-109 | OD-C01 REQ-04 (bulkhead interface as OD-C01 fixes it) | "REQ-04 | Bulkhead inserts | four Ø4.0 ± 0.05 through-holes at (x 65.0, z −45.0), (65.0, −105.0), (65.0, −165.0), (65.0, −225.0), offset ≤ 0.10" | #10 | OD-C01 DESIGN_SPEC_v1.2 §5 |
| X-110 | OD-C01 A-04 (bulkhead interface assumption OD-C02 must be designed to) | "A-04 | OD-C02 bulkhead interface | a wall on the plane x = 65 from z −240 to −30 (3 to 5 thick), standing on four M3 inserts at (65, −45), (65, −105), (65, −165), (65, −225); the electric zone is x ≥ 70 | OD-C02 must be designed to it" | #10 | OD-C01 DESIGN_SPEC_v1.2 §6 |
| X-111 | OD-C01 A-13 (drainage assumption, retired by OD-C02's design) | "A-13 | Drainage | two Ø8 drain holes in the wet zone let a leak leave the machine onto the counter under it; the tray zone drains by the tray; no channels on the flat plate (C2 later) | a leak reaches the electronics before a drain ... | Retire by: OD-C02's drainage path" | #10 | OD-C01 DESIGN_SPEC_v1.2 §6 |
| X-112 | OD-C01 A-08 (electronics bay assumption) | "A-08 | Electronics bay | OD-C08 with either path within x 70 … 120, z −240 … −30 behind the bulkhead, its own tray screwed to bulkhead and plate later | the bay is too small for path 1's OD-E01 (scanned)" | #10 | OD-C01 DESIGN_SPEC_v1.2 §6 |
| X-113 | Bulkhead suggested thickness (OD-C01's own assumption text) | "a wall on the plane x = 65 from z −240 to −30 (3 to 5 thick)" | mm (thickness) | 3.00 … 5.00 | — | #10 | OD-C01 DESIGN_SPEC_v1.2 §6 A-04 | text (assumption, OD-C01's own guess, not OD-C02's) | not confirmed |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-31 | OD-C01 spec/§4 prose gives the thermoblock mount's lowest-point clearance above the plate as "16.5"; the OD-C01 REPORT's measured gate value is 16.4925 (and its own K-2 note calls the spec figure "rounded"). Which value does OD-C02's design use, and does the 0.0075 mm difference matter for the bulkhead's z-extent (z −240 to −30) or nearby features? |
| 2 | X-02, X-03, X-113 | The bulkhead's wall plane (x = 65) and z extent (−240 to −30) are fixed by OD-C01 as the foot interface (REQ-04). Nothing in the inputs gives the wall's height (its y extent / top edge) or its thickness as a firm value: OD-C01's own A-04 row only guesses "3 to 5 thick" as an assumption about a part it did not design. What is the bulkhead's height and thickness? |
| 3 | X-19, X-42…X-49 | REQUEST.md names the wires that must cross (pump, thermoblock heater and thermostat, flowmeter's Hall sensor, valve solenoid) and PROJECT_RULES.md's water-flow table names TUBE 1–7, but no input gives which wires cross the bulkhead at which position, any wire gauge, or the tube runs' actual paths (chassis order-of-work row 8: "OD-C02 ... designed after OD-C01 and the tube runs"; the tube runs do not exist yet, no tube scan). Where do the wires and tubes cross the bulkhead, and what are their diameters/gauges? |
| 4 | X-70, X-71, X-77…X-83 | The chassis order-of-work table (PROJECT_RULES.md) says the top/back panels (OD-C10, OD-C11) are designed against OD-C01 and OD-C02, and the electronics bay tray OD-C08 sits behind the bulkhead "screwed to bulkhead and plate later" (OD-C01 A-08), but no input gives how the panels or the electronics bay tray attach to the bulkhead (fastener pattern, standoffs, flange). How do OD-C08, OD-C10, and OD-C11 attach to OD-C02? |
| 5 | X-54, X-55, X-72 | The OD-C01, OD-C04 and OD-C05 specs each state a K1C (220 × 220 × 250) or Kobra Max 3 (420 × 420 × 500) build volume as "memory of the spec sheet, not in the machine file," and PROJECT_RULES.md notes "build volumes to be read into oguz-atolye/atolye/machines/." No input gives a machine-profile file with confirmed build volumes for either printer. What are the confirmed K1C and Kobra Max 3 build volumes, and which machine does OD-C02 print on? |
| 6 | X-02, X-03, X-54, X-55 | The bulkhead spans z −240 to −30 (210 mm) at a single x = 65 plane; nothing in the inputs says whether the wall is meant to print in one piece or in sections, on which printer, or in which orientation. Does OD-C02 print in one piece, and on which machine? |
| 7 | X-13, X-14, X-15, X-76 | REQUEST.md and OD-C01 say the drain holes at (−80, −120) and (−80, −230) are in OD-C01's plate, and that OD-C02 "carries the drainage path" so a wet-side leak reaches them and never the electric side; no input gives the shape of any drainage lip, channel, or standoff on OD-C02 itself that would route a leak along the wall to those holes, or how the bulkhead's foot seals against the plate. What is the drainage lip's shape, and how (if at all) does the bulkhead seal to the floor plate and to the panels around the wire/tube openings? |
| 8 | X-19 | REQUEST.md says the wires that must cross "pass ... through sealed or raised openings," but no input defines what "sealed" means here (gasket, grommet, potting) or gives any opening size. What sealing method and opening dimensions does the bulkhead need for the wire/tube crossings? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None. All thirteen listed input files were present under `00_Spec/inputs/` and were read in full (the six STEP files per intake rule 6: listed and hashed only, geometry deferred to `tools/measure`; the seven markdown/CSV files read completely).
