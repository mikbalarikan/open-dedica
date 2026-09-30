# INTAKE v01 — 20260930-od-c01-base-frame

Intake: Claude Code, claude-sonnet-5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-09-30 UTC

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
| 1 | 00_Spec/inputs/OD-C03_pump_cradle.step | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | 192751 | STEP | — | listed and hashed only (geometry measured later) |
| 2 | 00_Spec/inputs/OD-C04_thermoblock_mount.step | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 | 128306 | STEP | — | listed and hashed only (geometry measured later) |
| 3 | 00_Spec/inputs/OD-G01_housing_C1_v02.step | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | 437578 | STEP | — | listed and hashed only (geometry measured later) |
| 4 | 00_Spec/inputs/OD-H01_ulka_ep5_pump.step | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | 824180 | STEP | — | listed and hashed only (geometry measured later) |
| 5 | 00_Spec/inputs/OD-H11_thermoblock.step | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | 2400893 | STEP | — | listed and hashed only (geometry measured later) |
| 6 | 00_Spec/inputs/REQUEST.md | 9366df273cae1a47d969792640174964d4024951233c3c2e38eb6fdcb22160c1 | 2841 | Markdown | 1 | read fully |
| 7 | 00_Spec/inputs/PROJECT_RULES.md | 78488c5959fb7173c53435053b2dfd57c6a8fb0cbf51bcd1a34244bf5dd12d07 | 9127 | Markdown | 1 | read fully |
| 8 | 00_Spec/inputs/bom_rows.csv | bf80fe744a508d3e0e2198d53a41ba1c90f2c0f2e39fa2df538271a77f874c4a | 5546 | CSV | 55 rows | read fully |
| 9 | 00_Spec/inputs/reports/OD-C03_pump_cradle/DESIGN_SPEC_v1.2.md | 0bd94d9b6060ec4ea387fce26d20bdab5ac05c5829bd9993828dae677982584b | 17683 | Markdown | §1–§8 | read fully |
| 10 | 00_Spec/inputs/reports/OD-C04_thermoblock_mount/DESIGN_SPEC_v1.2.md | 388f7fd170b4313cc53d5039d4db6f2eefdc79bca93c64c44ebe7e9563970b8c | 17938 | Markdown | §1–§8 | read fully |
| 11 | 00_Spec/inputs/reports/OD-C05_group_head_carrier/DESIGN_SPEC_v1.0.md | 021f718529f8edaf1bd1c14da433cbe061acfa35db172aa471e3c6be651c4966 | 18934 | Markdown | §1–§8 | read fully |
| 12 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md | 52b06473b31a2365a638bf0daa993d2dfa32f1121a0caefbb74ff58c72657fa2 | 4549 | Markdown | 1 | read fully |
| 13 | 00_Spec/inputs/reports/OD-H11_thermoblock/README.md | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0 | 5385 | Markdown | 1 | read fully |
| 14 | 00_Spec/inputs/reports/OD-H11_thermoblock/export_check.json | ecba71c6aebb34c59dd7bcb61d67f09662d07954a724ae3729171bc1fc547a73 | 1326 | JSON | 1 | read fully |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C03 (pump cradle) foot underside plane and direction | y = +40.0, +Y points down in the C03 frame | mm | y = 40.00 | ±0.10 (REQ-08) | #9 | §2, §4 C1, REQ-08 | table / text | unconfirmed |
| X-02 | OD-C03 foot thickness | 3.0 (y 37.0…40.0) | mm | 3.00 | ±0.1 (REQ-08) | #9 | §4 C1, REQ-08 | table | unconfirmed |
| X-03 | OD-C03 foot / cradle envelope extent | x −40…+40, z −10…42; envelope 80.0 × 40.0 × 52.0 | mm | as given | spec ±0.1 (U-02) | #9 | §4 C1, U-02 | table | unconfirmed |
| X-04 | OD-C03 four frame screw holes | Ø3.4 through-holes along Y at (x ±34.0, z −4.0) and (x ±34.0, z 37.0) | mm | as given | Ø3.4 ±0.1, offset ≤0.10 (REQ-07) | #9 | §4 C1, REQ-07 | table | unconfirmed |
| X-05 | OD-C03 cradle envelope | 80.0 × 40.0 × 52.0 (x ±40.0, y 0.0…40.0, z −10.0…42.0) | mm | as given | spec ±0.1 (U-02) | #9 | §4 C1, U-02 | table | unconfirmed |
| X-06 | OD-C03 → OD-C01 interface (A-11): "OD-C01 must be designed to it" | four M3 inserts on a 68.0 × 41.0 pattern (x ±34.0, z −4.0 and 37.0 in the C03 frame); the foot underside at y = 40.0 is the frame's floor plane | mm | as given | — | #9 | §6 A-11 | assumptions ledger | unconfirmed; design choice, not measured |
| X-07 | OD-H01 pump axis / frame | Z is the pump axis, +Z toward the inlet hose fitting, outlet spigot at −Z; X is the normal of the sheet-metal frame's side plate; origin on the pump axis | — | — | — | #9, #12 | C03 spec §2; H01 README "Deliverables" | drawing/report text | unconfirmed; scan-derived |
| X-08 | OD-H01 pump envelope (datum bbox) | 54.05 × 55.15 × 121.95 | mm | 54.05 × 55.15 × 121.95 | — | #12 | "Deliverables" re-import check | scan → CAD rebuild | flagged: scan-derived, not caliper-confirmed |
| X-09 | OD-H01 sheet-metal U-frame (side plates the cradle must clear) | end plates at z −12.4 and 37.65; two side plates at x −27.20…−24.10 and x 23.75…26.85, both y ±16.20, z −12.17…37.42 | mm | as given | — | #9 | §6 A-04 (measured on the STEP, plan v01 §2a) | assumptions ledger | flagged: scan-derived, unconfirmed |
| X-10 | OD-H01 pump orientation in the machine (A-08) | axis horizontal; +Y (side opposite the terminal block) down; terminals up for wiring; outlet (−Z) toward the 3-way valve | — | — | — | #9 | §6 A-08 | assumptions ledger | unconfirmed; OD-C01 layout decision |
| X-11 | OD-H01 pump mass | ≈ 0.5 kg | kg | — | not calculated | #9 | §6 A-12 | assumptions ledger (ULKA EP5 datasheet memory) | unconfirmed |
| X-12 | OD-C04 (thermoblock mount) foot underside plane and direction | y = −70.0, −Y points down in the C04 frame | mm | y = −70.00 | ±0.10 (REQ-05) | #10 | §2, §4 C1, REQ-05 | table / text | unconfirmed |
| X-13 | OD-C04 foot thickness | 4.0 (y −70.0…−66.0) | mm | 4.00 | ±0.1 (REQ-05) | #10 | §4 C1, REQ-05 | table | unconfirmed |
| X-14 | OD-C04 foot / mount extent | x ±50, z −17.0…+33.0; envelope 100.0 × 110.0 × 50.0 | mm | as given | spec ±0.1 (U-02) | #10 | §4 C1, U-02 | table | unconfirmed |
| X-15 | OD-C04 four frame screw holes | Ø3.4 through-holes along Y at (x ±40.0, z −8.0) and (x ±40.0, z 26.0) | mm | as given | Ø3.4 ±0.1, offset ≤0.10 (REQ-06) | #10 | §4 C1, REQ-06 | table | unconfirmed |
| X-16 | OD-C04 mount envelope | 100.0 × 110.0 × 50.0 (x ±50, y −70…+40, z −17…+33) | mm | as given | spec ±0.1 (U-02) | #10 | §4 C1, U-02 | table | unconfirmed |
| X-17 | OD-C04 → OD-C01 interface (A-10): "OD-C01 must be designed to it; the group-head height follows" | four M3 inserts on an 80.0 × 34.0 pattern (x ±40.0, z −8.0 and 26.0 in the C04 frame); the foot underside at y = −70.0 is the frame's floor plane, 16.5 below the thermoblock's lowest point (y −53.5) | mm | as given | — | #10 | §6 A-10 | assumptions ledger | unconfirmed; design choice, not measured |
| X-18 | OD-H11 thermoblock axis and outlet face | Z parallel to the body axis, passing through (x −8.330, y −14.130); z = 0 is the base face; +Z toward the outlet (three-pin) face at z = 47.64, pins reach z = 50.79 | mm / deg | as given | — | #10 | §2; §6 A-02 | drawing text / assumptions ledger | flagged: measured on STEP, scan-derived, unconfirmed |
| X-19 | OD-H11 thermoblock envelope (datum bbox) | bbox_min (−43.27, −53.508, −0.0), bbox_max (42.839, 53.381, 50.79); volume 159766.5 mm³ | mm / mm³ | as given | — | #14 | export_check.json "datum" | JSON export report | flagged: scan-derived, unconfirmed |
| X-20 | ≥10 mm air-gap rule to the thermoblock (REQ-01) | `clearance(mount, OD-H11) ≥ 10.0` at the identity pose; source "Keep ≥10 mm air gap to any printed part" | mm | 10.00 | Hard gate | #10 | §5 REQ-01 (client INTAKE X-R05) | gate table | unconfirmed as applied to OD-C01 |
| X-21 | OD-H11 orientation in the machine (A-07) | axis horizontal, +Z toward the group head, −Y down, pipes and terminals up | — | — | — | #10 | §6 A-07 | assumptions ledger | unconfirmed; OD-C01 / OD-C05 layout decision |
| X-22 | OD-H11 thermoblock mass | ≈ 0.45 kg (159 767 mm³ aluminium) | kg | — | not calculated | #10 | §6 A-11 | assumptions ledger | unconfirmed |
| X-23 | OD-C05 (group head carrier) foot underside plane and direction | y = −150.0, +Y points up in the C05 frame (A-02) | mm | y = −150.00 | ±0.10 (REQ-05) | #11 | §2, §4 C1, REQ-05 | table / text | unconfirmed |
| X-24 | OD-C05 foot thickness | 4.0 (y −150.0…−146.0) | mm | 4.00 | ±0.1 (REQ-05) | #11 | §4 C1, REQ-05 | table | unconfirmed |
| X-25 | OD-C05 foot / carrier extent | x ±50, z −69.94…−24.94 (wall front face to rear-most gusset foot edge); envelope 100.0 × 200.0 × 45.0 | mm | as given | spec ±0.1 (U-02) | #11 | §4 C1, U-02 | table | unconfirmed |
| X-26 | OD-C05 four frame screw holes | Ø3.4 through-holes along Y at (x ±35.0, z −40.0) and (x ±35.0, z −60.0) | mm | as given | Ø3.4 ±0.1, offset ≤0.10 (REQ-06) | #11 | §4 C1, REQ-06 | table | unconfirmed |
| X-27 | OD-C05 carrier envelope | 100.0 × 200.0 × 45.0 (x ±50, y −150…+50, z −69.94…−24.94) | mm | as given | spec ±0.1 (U-02) | #11 | §4 C1, U-02 | table | unconfirmed |
| X-28 | OD-C05 → OD-C01 interface (A-04): "OD-C01 must be designed to it" | four M3 inserts on a 70.0 × 20.0 pattern (x ±35.0, z −40.0 and −60.0 in the C05 frame); the foot underside is the frame's floor plane, "the same plane OD-C03 and OD-C04 stand on" | mm | as given | — | #11 | §6 A-04 | assumptions ledger | unconfirmed; design choice, not measured |
| X-29 | Group head axis height above the floor / housing's lowest point (A-03) | axis 150.0 above the base frame's floor plane (y = −150.0 in the C05 frame); housing's lowest point (y −43.1) is 106.9 above the floor; ≥95 mm requirement (INTAKE X-66) holds while the tray's top stands ≤11.9 above the floor | mm | as given | — | #11 | §6 A-03 | assumptions ledger | unconfirmed; design choice, "OD-C01 must lower or raise the whole carrier" if wrong |
| X-30 | Thermoblock zone constraint on OD-C01 layout (A-05): "the thermoblock's own axis height and offset are OD-C01's to fix" | OD-H11 with its mount OD-C04 stays at z ≤ −85.0 in the C05 frame (behind the carrier foot's rear edge by ≥15), so no carrier surface is within 10 mm of the casting | mm | as given | — | #11 | §6 A-05 | assumptions ledger | unconfirmed; design choice for OD-C01 |
| X-31 | OD-C05 wall extent | wall 5.0 thick along Z, z −29.94…−24.94, spanning x −50…+50 and y −150.0…+50.0, top corners R8 | mm | as given | spec ±0.1 (REQ-03) | #11 | §4 C1, REQ-03 | table | unconfirmed |
| X-32 | OD-G01 housing rear flange envelope/frame (A-01, mating solid for OD-C05, informs OD-C01's neighbour geometry) | slab 5.00 thick, z −24.94…−19.94, 100 × 100 square with R8 corners, rear face z −24.94; four insert bores Ø4.0 × 5.7 at (x, y = ±44, ±44); Ø26 hub opening on the axis | mm | as given | — | #11 | §6 A-01 | assumptions ledger | flagged: OD-G01 job at third round, "A-18 note is stale"; unconfirmed |
| X-33 | Housing/carrier orientation in the machine (A-02) | +Y of the housing frame points up in the machine; the housing's clocking about its own axis is otherwise free | — | — | — | #11 | §6 A-02 | assumptions ledger | unconfirmed; OD-C01 must agree |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-34 | Pipeline deliverables per part | "each part needs a parametric build script, STEP, STL/3MF and an independent review verdict" | #6 | REQUEST.md, standing instruction |
| X-35 | Scan/report values are assumptions until confirmed | "every value from a scan or report is an A-## assumption until the Usta confirms it; calipers beat scans; a fit-critical value cannot be confirmed from an image" | #6 | REQUEST.md, standing instruction |
| X-36 | Data class | "data class PUBLIC (CC BY 4.0)" | #6 | REQUEST.md, standing instruction |
| X-37 | OD-C01 material and process | "This job: OD-C01 base frame / floor plate (bom.csv: ASA, printed)." | #6 | REQUEST.md line 12 |
| X-38 | OD-C01 designed against neighbour footprints and the tray | "designed against the footprints of rows 2 to 6 (OD-C05 carrier, OD-C03 pump cradle, OD-C04 thermoblock mount, OD-C07 valve and flowmeter mount, OD-C06 tank dock) and the drip tray OD-C21/C22" | #6 | REQUEST.md lines 12–14 |
| X-39 | Fastener / floor-plane interface, every mount | "Each of those parts expects M3 heat-set inserts in OD-C01 under its four Ø3.4 holes and its foot on OD-C01's floor plane." | #6 | REQUEST.md lines 24–25 |
| X-40 | Machine layout is OD-C01's own design choice | "The machine layout (where each sub-assembly sits on the floor plate, the front, the drip tray position and height, the overall footprint) is not fixed by any input: it is this job's design choice, recorded as assumptions for the parts that follow." | #6 | REQUEST.md lines 28–30 |
| X-41 | Two-zone separation with drainage | "the wet zone (tank, pump, thermoblock, valves) separated from the electric zone by a bulkhead (OD-C02, next job) with a drainage path to the tray" | #6 | REQUEST.md lines 31–32 |
| X-42 | Thermoblock/TCO air-gap requirement (project-wide restatement) | "the thermoblock and its TCO ≥ 10 mm from every printed wall" | #6 | REQUEST.md line 33 |
| X-43 | Group head height requirement (project-wide restatement) | "the group head ≥ 95 mm above the tray" | #6 | REQUEST.md line 34 |
| X-44 | Feet | "TPU feet or the OEM rubber feet pads" | #6 | REQUEST.md line 34 |
| X-45 | Removable panels | "top and back panels removable" | #6 | REQUEST.md lines 34–35 |
| X-46 | Printer/material split, build volumes not supplied | "The Anycubic Kobra Max 3 prints the large parts in PETG, the Creality K1C the enclosed ASA parts; neither build volume is in the inputs." | #6 | REQUEST.md lines 35–36 |
| X-47 | Chassis order-of-work row for OD-C01 | "`OD-C01` base frame / floor plate \| the footprints of 2–6; drip tray OD-C21/C22 \| drip tray not scanned" | #7 | PROJECT_RULES.md, chassis/README.md order-of-work table, row 7 |
| X-48 | Unscanned-neighbour rule | "Each part is designed against the scanned OEM parts it touches. A part whose OEM neighbour is not scanned yet carries that neighbour as an assumption row and is revisited when the scan lands." | #7 | PROJECT_RULES.md, chassis/README.md "Order of work" |
| X-49 | Chassis design rule 1 — two-zone layout | "Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #7 | PROJECT_RULES.md §6 rule 1 |
| X-50 | Chassis design rule 2 — anti-vibration | "Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #7 | PROJECT_RULES.md §6 rule 2 |
| X-51 | Chassis design rule 3 — thermal map | "Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #7 | PROJECT_RULES.md §6 rule 3 |
| X-52 | Chassis design rule 4 — serviceability | "top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #7 | PROJECT_RULES.md §6 rule 4 |
| X-53 | Chassis design rule 5 — mug clearance and envelope | "Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec." | #7 | PROJECT_RULES.md §6 rule 5 |
| X-54 | Chassis design rule 6 — sensor bosses | "Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one." | #7 | PROJECT_RULES.md §6 rule 6 |
| X-55 | Chassis design rule 7 — safety carries over | "piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #7 | PROJECT_RULES.md §6 rule 7 |
| X-56 | Safety note | "this machine runs on mains voltage (230 V / 120 V), heats water to ~125 °C and pressurizes it to 15 bar. Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA." | #7 | PROJECT_RULES.md, README.md safety note |
| X-57 | Drip tray sets the base footprint | "Why the chassis needs it: sets the chassis base footprint and cup height reference. Critical interfaces to measure with calipers: tray envelope and wall draft; float (08) guide geometry; cup rest grid (07/12) seating; locating features into the machine." | #7 | PROJECT_RULES.md, GitHub issue #9 |
| X-58 | Validate-before-trust rule | "Validate: print a check-fixture (a ring or cradle) for each critical part and test-fit the real component before trusting the model in the chassis assembly." | #7 | PROJECT_RULES.md, SOURCING_GUIDE §5 step 6 |
| X-59 | Water path bypass/return to tank | "3-way valve `OD-H22` → Water tank `OD-W01` \| TUBE 3 \| cold \| Bypass / over-pressure return" | #7 | PROJECT_RULES.md, docs/WATER_FLOW.md flow table row 5 |
| X-60 | BOM: OD-C01 base frame | "OD-C01,OD-C00,PRINT,Base frame / floor plate,,,1,DESIGN,ASA,printed,print,,proposed" | #8 | bom_rows.csv row (OD-C01) |
| X-61 | BOM: OD-C02 bulkhead (next job, touches OD-C01) | "OD-C02,OD-C00,PRINT,Wet/electric bulkhead with drainage path,,,1,DESIGN,ASA,printed,print,,proposed" | #8 | bom_rows.csv row (OD-C02) |
| X-62 | BOM: OD-C03 pump cradle material | "OD-C03,OD-C00,PRINT,Pump cradle (sleeve + spring suspension),,,1,DESIGN,PETG,printed,print,#1,proposed" | #8 | bom_rows.csv row (OD-C03) |
| X-63 | BOM: OD-C04 thermoblock mount material/note | "OD-C04,OD-C00,PRINT,Thermoblock mount (≥10 mm air gap to printed walls),,,1,DESIGN,ASA / PC,printed,print,#2,proposed" | #8 | bom_rows.csv row (OD-C04) |
| X-64 | BOM: OD-C05 group head carrier material | "OD-C05,OD-C00,PRINT,Group head carrier (ties OD-G00 to frame),,,1,DESIGN,ASA,printed,print,#3,proposed" | #8 | bom_rows.csv row (OD-C05) |
| X-65 | BOM: OD-C06 water tank dock material | "OD-C06,OD-C00,PRINT,Water tank dock / inlet seat,,,1,DESIGN,PETG,printed,print,#5,proposed" | #8 | bom_rows.csv row (OD-C06) |
| X-66 | BOM: OD-C07 valve/flowmeter mount material and note | "OD-C07,OD-C00,PRINT,Valve & flowmeter mount (OPV reachable without disassembly),,,1,DESIGN,PETG,printed,print,#6,proposed" | #8 | bom_rows.csv row (OD-C07) |
| X-67 | BOM: OD-C08 electronics bay tray material | "OD-C08,OD-C00,PRINT,Electronics bay tray,,,1,DESIGN,PETG,printed,print,#8,proposed" | #8 | bom_rows.csv row (OD-C08) |
| X-68 | BOM: OD-C15 feet material/qty | "OD-C15,OD-C00,PRINT,Foot (alternative to OD-C25/526),,,4,DESIGN,TPU,printed,print,,proposed" | #8 | bom_rows.csv row (OD-C15) |
| X-69 | BOM: OD-C21 drip tray status | "OD-C21,OD-C00,OEM,Drip tray (or printed replacement),09,5313249971,1,SCAN,,FixPart / printed,8–12,#9,todo" | #8 | bom_rows.csv row (OD-C21) |
| X-70 | BOM: OD-C25 rubber foot pad | "OD-C25,OD-C00,OEM,Rubber foot pad,34,5313229381,2,CALIPER,rubber,FixPart,4 (set),,todo" | #8 | bom_rows.csv row (OD-C25) |
| X-71 | BOM: OD-C26 rubber foot pad | "OD-C26,OD-C00,OEM,Rubber foot pad,76,5313274719,2,CALIPER,rubber,FixPart,(set),,todo" | #8 | bom_rows.csv row (OD-C26) |
| X-72 | BOM: OD-F01 fastener, quantity | "OD-F01,OD-000,STD,M3 heat-set insert,,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo" | #8 | bom_rows.csv row (OD-F01) |
| X-73 | BOM: OD-F02 fastener, quantity | "OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo" | #8 | bom_rows.csv row (OD-F02) |
| X-74 | Standing instruction on the review round | "spec ratifications, the concept, the gate classes, the REVISE round" confirmed by the Usta with "confirmed go" in the project thread | #9, #10, #11 | each DESIGN_SPEC §7 last row |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-01, X-12, X-23 | Each mount's spec states "down" differently in its own local frame (OD-C03: +Y down; OD-C04: −Y down; OD-C05: +Y up). None of the three specs states the global OD-C01 / machine frame these local frames are placed into. What is OD-C01's own coordinate frame, and how does each mount's local "down" map onto it? |
| 2 | X-06, X-17, X-28 | None of the three specs gives the mounts' positions or orientations relative to each other on the floor plate (only each mount's own local hole pattern and floor-plane height). Without a placed layout, whether two mounts' feet or envelopes would overlap once placed on OD-C01 cannot be determined from these inputs. What is the intended relative layout (front direction, X/Y offsets between OD-C03, OD-C04, OD-C05, and clearance margins) so overlap can be checked? |
| 3 | X-40 | The overall machine footprint and overall height are not given by any input (REQUEST.md: "The machine layout ... is not fixed by any input: it is this job's design choice"). What footprint and height should OD-C01 target, and against what constraint (e.g. the 0.4 m³ envelope of X-53)? |
| 4 | X-38, X-57, X-69 | The drip tray OD-C21/C22 is unscanned (bom status "todo"); its size, height and position on OD-C01 are not given anywhere in the inputs, only that it "sets the chassis base footprint and cup height reference." What tray envelope, position and height should OD-C01 assume until the scan lands? |
| 5 | X-38, X-65 | OD-C06 (water tank dock) is not designed; the water tank OD-W01/OD-W02 is not scanned. What tank size and dock position/zone should OD-C01 reserve? |
| 6 | X-38, X-66 | OD-C07 (valve and flowmeter mount) is not designed; OD-H21/OD-H22/OD-H24 positions relative to the other mounts are not given. What zone should OD-C01 reserve for the valve/flowmeter mount, and where relative to the pump and thermoblock? |
| 7 | X-41, X-61 | OD-C08 (electronics bay) and its path (OEM Path 1 OD-E01/E02 vs. open-controller Path 2 OD-E51…E58) are undecided in the BOM ("choose Path 1 OEM or Path 2 open controller"). Which electronics path, and what zone/bay should OD-C01 reserve on the electric side of the bulkhead? |
| 8 | X-44, X-68, X-70, X-71 | Three different foot options are listed (OD-C15 TPU printed feet ×4, OD-C25 and OD-C26 OEM rubber pads ×2 each) with no stated positions on the floor plate. Which foot option, how many, and where should they attach to OD-C01? |
| 9 | X-46 | Neither the Anycubic Kobra Max 3 nor the Creality K1C build volume is given in any input (each mount's own spec also flags this as an open assumption, e.g. C03 A-10, C04 A-09, C05 A-08, each sourced only from "memory of the spec sheet"). What are the confirmed build volumes, and does OD-C01 (a large floor plate) fit either machine in one piece? |
| 10 | X-37, X-46 | No input states OD-C01's own print orientation or whether the floor plate must print in one piece or be split (e.g. for build-volume reasons). What print orientation and split (if any) should OD-C01 use? |
| 11 | X-06, X-17, X-28 | Each mount spec (C03 §6 A-11, C04 §6 A-10, C05 §6 A-04) independently states "OD-C01 must be designed to it" for its own floor-plane height and hole pattern, and C05 additionally assumes its floor plane is "the same plane OD-C03 and OD-C04 stand on" — but no input confirms all three mounts actually share one common floor plane height in a single OD-C01 design. Should OD-C01 adopt one single floor plane for all three mounts, and is that assumption (C05 A-04) correct? |
| 12 | X-30 | OD-C05 assumes (A-05) that "the thermoblock's own axis height and offset are OD-C01's to fix," i.e. OD-C01 must place OD-C04 so the thermoblock casting stays at z ≤ −85 in the C05 frame. No input gives the actual thermoblock axis height/offset OD-C01 should use. What height and offset should OD-C01 place OD-C04 (and hence OD-H11) at, consistent with both the C04 foot (X-12…X-17) and the C05 keep-out (X-30)? |
| 13 | X-06, X-17, X-28, X-35 | Every mount's interface value (hole patterns, floor-plane heights, envelopes) is drawn from STEP files rebuilt from uncalibrated photogrammetry/structured-light scans (OD-H01 p95 0.448 mm / max 2.49 mm deviation; OD-H11 p95 0.474 mm / max 2.71 mm deviation; neither caliper-confirmed — see X-08, X-09, X-18, X-19). Should OD-C01's layout be designed with an explicit margin against this scan uncertainty, and if so how much? |
| 14 | X-32 | OD-C05 §6 A-01 notes the OD-G01 housing job "is at its third round with this geometry unchanged" and that an earlier flange note "is stale." Is the OD-G01 v02 STEP supplied here (input #3) final enough to design OD-C01's clearance/zone under the group head carrier against, or could the flange geometry still change? |
| 15 | (none — status note) | OD-C05 DESIGN_SPEC v1.0 header states "explicit confirmation of §5 and §6 pending" (unlike the C03/C04 specs, whose §7 record the Usta's "confirmed go"). Is the C05 spec's data (X-23…X-33) usable as-is for OD-C01's layout, or does it await the Usta's confirmation first? |
| 16 | X-41, X-49, X-59 | The two-zone/drainage requirement (X-41, X-49) and the water-flow bypass/return path (X-59) both touch OD-C01, but OD-C02 (the bulkhead that actually separates the zones) is explicitly out of scope for this job ("next job"). What drainage path geometry (slope, channel, drain point to the tray) should OD-C01 itself provide, versus leaving entirely to OD-C02? |
| 17 | X-42, X-53 | The 0.4 m³ envelope limit (X-53) and the ≥95 mm group-head-above-tray rule (X-43/X-29) are both named as constraints, but no input gives the machine's other dimensions (width, depth) needed to check whether a footprint holding all of OD-C03, OD-C04, OD-C05, the tray, the tank and the electronics bay stays inside 0.4 m³. Should this be treated as a hard constraint on OD-C01's footprint from the outset? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None. All fourteen listed inputs were read in full (the five STEP files listed and hashed only, per intake rule 6 and the brief).
