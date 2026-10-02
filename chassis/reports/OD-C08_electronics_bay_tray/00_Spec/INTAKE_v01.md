# INTAKE v01 — 20261001-od-c08-electronics-bay-tray

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
| 1 | `00_Spec/inputs/OD-C01_base_frame.step` | `7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805` | 134325 | STEP | — | listed and hashed only (brief: geometry measured later) |
| 2 | `00_Spec/inputs/OD-C02_bulkhead.step` | `1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc` | 150003 | STEP | — | listed and hashed only |
| 3 | `00_Spec/inputs/OD-E01_power_pcb.step` | `90780af378d48baf22b43b378b4484c6ef252a1b68ecb224330bec32f3bfd869` | 4815667 | STEP | — | listed and hashed only |
| 4 | `00_Spec/inputs/OD-E02_control_board.step` | `4e570b4abc68a538efecbf89022738dd0e2527dcb466ceee9b721b353b005385` | 1869814 | STEP | — | listed and hashed only |
| 5 | `00_Spec/inputs/REQUEST.md` | `c9f4fa32ea1f122a64005c23f2e52a168bfd1d3510d971bacfe0034981e638bc` | 2200 | Markdown | 1 | read whole |
| 6 | `00_Spec/inputs/PROJECT_RULES.md` | `c5cab0228c9ca51387c64711bc66f418f02ca18ff8c3772a876a99d923c3d4e4` | 10791 | Markdown | 1 | read whole |
| 7 | `00_Spec/inputs/bom_rows.csv` | `6d636418c38cbc6c35e902148134473ed1fff27880851fa40c1d372cc1a31ab4` | 2328 | CSV | 1 | read whole |
| 8 | `00_Spec/inputs/reports/OD-C01_base_frame/DESIGN_SPEC_v1.2.md` | `75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681` | 25226 | Markdown | 1 (§1…§8) | read whole |
| 9 | `00_Spec/inputs/reports/OD-C02_bulkhead/DESIGN_SPEC_v1.2.md` | `d98773838192515ee097b92e5ebe38006324ba0031743c408da7093c893b63be` | 20686 | Markdown | 1 (§1…§8) | read whole |
| 10 | `00_Spec/inputs/reports/OD-E01_power_pcb/DELIVER_README.md` | `11f0a0eecfd37bc972c41a37d8587b7e9804e126f841921a3b75449246811074` | 69333 | Markdown | 1 (§1…§16) | read whole |
| 11 | `00_Spec/inputs/reports/OD-E01_power_pcb/PARAM_TABLE.md` | `99827b0fdcb2acdfcdf85b4bae17e76e21782ea185e121d5b00e42e1d6a41b51` | 68827 | Markdown | 1 | read whole |
| 12 | `00_Spec/inputs/reports/OD-E02_control_board/DELIVER_README.md` | `ce5f0ea18403cd05e70140fed694c52ca876c9a94c20d54783430bfd17a5d4c3` | 47093 | Markdown | 1 (§1…§16) | read whole |
| 13 | `00_Spec/inputs/reports/OD-E02_control_board/PARAM_TABLE.md` | `ccde336ca5833ad182edb6ca04248c52bbd4ceb8348df46d0246d1c26b907e28` | 39837 | Markdown | 1 | read whole |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C01 electronics zone, x extent | 70 … 120 | mm | 70.00 … 120.00 | — | #8 | §4 A-08; also REQUEST.md relay | table (A-## ledger) | unconfirmed (OPEN in source ledger) |
| X-02 | OD-C01 electronics zone, z extent | −240 … −30 | mm | −240.00 … −30.00 | — | #8 | §4 A-08 | table | unconfirmed |
| X-03 | OD-C01 plate top face (floor plane) | y = 0.00 | mm | 0.00 | ±0.10 | #8 | §5 REQ-07 | table (gate) | — |
| X-04 | OD-C01 plate thickness | 6.0 | mm | 6.00 | ±0.1 | #8 | §5 REQ-07 | table (gate) | — |
| X-05 | OD-C01 plate outline, +X edge near zone | x = +120.0 | mm | 120.00 | within [spec−0.1, spec+0.1] | #8 | §5 U-02 (envelope) | table (gate) | — |
| X-06 | OD-C01 plate outline, corner radius | R 10 | mm | 10.00 | — | #8 | §4 C1 (plate text) | table (concept text, not a gated REQ row) | — |
| X-07 | OD-C01 plate hole (bulkhead line, nearest zone) | Ø4.0 at (x 65.0, z −45.0) | mm | Ø4.00 at (65.00, −45.00) | Ø±0.05, offset ≤0.10 | #8 | §5 REQ-04 | table (gate) | within 20 mm of zone x-edge (70; Δx=5) |
| X-08 | OD-C01 plate hole (bulkhead line) | Ø4.0 at (x 65.0, z −105.0) | mm | Ø4.00 at (65.00, −105.00) | Ø±0.05, offset ≤0.10 | #8 | §5 REQ-04 | table (gate) | within 20 mm of zone (Δx=5) |
| X-09 | OD-C01 plate hole (bulkhead line) | Ø4.0 at (x 65.0, z −165.0) | mm | Ø4.00 at (65.00, −165.00) | Ø±0.05, offset ≤0.10 | #8 | §5 REQ-04 | table (gate) | within 20 mm of zone (Δx=5) |
| X-10 | OD-C01 plate hole (bulkhead line) | Ø4.0 at (x 65.0, z −225.0) | mm | Ø4.00 at (65.00, −225.00) | Ø±0.05, offset ≤0.10 | #8 | §5 REQ-04 | table (gate) | within 20 mm of zone (Δx=5) |
| X-11 | OD-C02 bulkhead electric face, x | x = 67.00 | mm | 67.00 | ±0.10 | #9 | §5 REQ-02 | table (gate) | — |
| X-12 | OD-C02 bulkhead wet face, x | x = 63.00 | mm | 63.00 | ±0.10 | #9 | §5 REQ-02 | table (gate) | — |
| X-13 | OD-C02 base rail, +X extent toward bay | x = 71.0 (1 mm into bay zone x≥70) | mm | 71.00 | — | #9 | §4 C1; §6 A-07 | table (concept text + ledger) | — |
| X-14 | OD-C02 top rail, +X extent toward bay | x = 70.5 | mm | 70.50 | — | #9 | §4 C1; §6 A-07 | table (concept text) | — |
| X-15 | OD-C02 bulkhead height (top rail top face) | y = 215.0 | mm | 215.00 | ±0.1 | #9 | §5 REQ-06 | table (gate) | — |
| X-16 | OD-C02 wire window 1 (pump), centre/diam | Ø14.0 at (y 150.0, z −200.0) | mm | Ø14.00 at (150.00, −200.00) | Ø±0.1, offset ≤0.10 | #9 | §5 REQ-04 | table (gate) | — |
| X-17 | OD-C02 wire window 2 (thermoblock heater/thermostat) | Ø14.0 at (y 150.0, z −130.0) | mm | Ø14.00 at (150.00, −130.00) | Ø±0.1, offset ≤0.10 | #9 | §5 REQ-04 | table (gate) | — |
| X-18 | OD-C02 wire window 3 (group head side) | Ø14.0 at (y 150.0, z −60.0) | mm | Ø14.00 at (150.00, −60.00) | Ø±0.1, offset ≤0.10 | #9 | §5 REQ-04 | table (gate) | — |
| X-19 | OD-C02 wire window 4 (valve/flowmeter) | Ø14.0 at (y 60.0, z −55.0) | mm | Ø14.00 at (60.00, −55.00) | Ø±0.1, offset ≤0.10 | #9 | §5 REQ-04 | table (gate) | — |
| X-20 | OD-E01 board outline, x_min | −5.162 | mm | −5.162 | ±0.068 | #10, #11 | §5 table / PARAM_TABLE | scan (robust line fit) | fit-critical: photo/scan only, not confirmable for fit |
| X-21 | OD-E01 board outline, x_max | 95.002 | mm | 95.002 | ±0.06 | #10, #11 | §5 table / PARAM_TABLE | scan | fit-critical: scan only |
| X-22 | OD-E01 board outline, y_min | −56 | mm | −56.00 | ±0.093 | #10, #11 | §5 table / PARAM_TABLE | scan | fit-critical: scan only |
| X-23 | OD-E01 board outline, y_max | 3.869 | mm | 3.869 | ±0.094 | #10, #11 | §5 table / PARAM_TABLE | scan | fit-critical: scan only |
| X-24 | OD-E01 board thickness | 1.562 | mm | 1.562 | ±0.1 | #10, #11 | §5 table / PARAM_TABLE | scan (solder side not scanned) | fit-critical: scan only; solder side invented (L2) |
| X-25 | OD-E01 hole H1 (mounting, datum origin) | cx 0.003, cy 0.001, r 2.022 | mm | (0.003, 0.001), r 2.022 (Ø4.044) | ±0.019 | #10, #11 | §5 table / PARAM_TABLE | scan (IRLS circle) | scan only |
| X-26 | OD-E01 hole H2 | cx 0.013, cy −52.009, r 2.006 | mm | (0.013, −52.009), r 2.006 (Ø4.012) | ±0.035 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-27 | OD-E01 hole H3 | cx 11.396, cy −6.614, r 0.909 | mm | (11.396, −6.614), r 0.909 (Ø1.818) | ±0.054 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-28 | OD-E01 hole H4 | cx 11.378, cy −19.416, r 0.91 | mm | (11.378, −19.416), r 0.910 (Ø1.820) | ±0.043 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-29 | OD-E01 hole H5 | cx 57.519, cy 1.976, r 1.243 | mm | (57.519, 1.976), r 1.243 (Ø2.486) | ±0.038 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-30 | OD-E01 hole H6 | cx 57.511, cy −49.008, r 1.23 | mm | (57.511, −49.008), r 1.230 (Ø2.460) | ±0.022 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-31 | OD-E01 board slot, y extent | −27 / −25.7 | mm | −27.00 … −25.70 | ±0.1 | #10, #11 | §5 table / PARAM_TABLE | scan (height map) | scan only |
| X-32 | OD-E01 board slot, x end (round) | 2.2 | mm | 2.20 | ±0.1 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-33 | OD-E01 heatsink top z (overall height above board) | 25.262 | mm | 25.262 | ±0.034 | #10, #11 | §5 table / PARAM_TABLE | scan (median height map) | scan only; this is the tallest measured feature on the board |
| X-34 | OD-E01 heatsink bottom z (root on board) | 0 | mm | 0.00 | ±0.5 | #10, #11 | §5 table (`hs_bottom_z`) | assumed (not measurable on scan) | assumed, not scan — flag per source column |
| X-35 | OD-E01 heatsink hub, upper, position | cx 48.155, cy −7.889, R_hub 3.6 | mm | (48.155, −7.889), R 3.60 | ±0.1 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-36 | OD-E01 heatsink hub, lower, position | cx 48.07, cy −33.385, R_hub 3.5 | mm | (48.07, −33.385), R 3.50 | ±0.1 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-37 | OD-E01 heatsink spine, x extent | 47.3 / 49.2 | mm | 47.30 … 49.20 | ±0.1 | #10, #11 | §5 table / PARAM_TABLE | scan | scan only |
| X-38 | OD-E01 tallest component overall | heatsink, top z 25.262 at x ≈ 47–49, y ≈ −7…−33 | mm | 25.262 at (≈48, ≈−20) | ±0.034 | #10 | §5 table (`hs_top_z`) | scan | scan only; tallest of all measured features |
| X-39 | OD-E01 TO-220 (Q1) tab top z (second-tallest) | q1_tab z_top 21.618; tab x 46.077…47.485, y −26.479…−16.381 | mm | z 21.618; x 46.077…47.485, y −26.479…−16.381 | ±0.1 | #10, #11 | §5 table (`q1_tab`) | scan | scan only |
| X-40 | OD-E01 faston tab x positions (6 tabs) | 36.245, 51.223, 64.782, 71.218, 77.744, 88.097 | mm | 36.245 / 51.223 / 64.782 / 71.218 / 77.744 / 88.097 | ±0.05 | #10, #11 | §5 table (`faston_x`) | scan | scan only; fit-critical flag in source |
| X-41 | OD-E01 faston tab y positions (6 tabs) | −50.515, −50.523, −50.572, −50.57, −50.573, −50.558 | mm | −50.515 … −50.573 | ±0.05 | #10, #11 | §5 table (`faston_y`) | scan | scan only |
| X-42 | OD-E01 faston tab top z | 10.617 (mean of 6) | mm | 10.617 | ±0.014 | #10, #11 | §5 table (`faston_top_z`) | scan (mean-of-n) | scan only; fit-critical flag in source |
| X-43 | OD-E01 connector J1 envelope | x 7.217…12.734, y −39.147…−21.869, z_top 6.819 | mm | x 7.217…12.734, y −39.147…−21.869, z_top 6.819 | ±0.1 | #10, #11 | §5 table (`conn_J1`) | scan | scan only; cavity floor not reliably seen (no-data fraction 0.94) |
| X-44 | OD-E01 connector J2 envelope | x −3.384…2.195, y −46.385…−36.618, z_top 6.877 | mm | x −3.384…2.195, y −46.385…−36.618, z_top 6.877 | ±0.1 | #10, #11 | §5 table (`conn_J2`) | scan | scan only; cavity floor unreliable (no-data fraction 0.96) |
| X-45 | OD-E01 connector J3 envelope | x 6.602…11.489, y −4.53…2.711, z_top 5.791 | mm | x 6.602…11.489, y −4.53…2.711, z_top 5.791 | ±0.1 | #10, #11 | §5 table (`conn_J3`) | scan | scan only; cavity floor unreliable (no-data fraction 0.50) |
| X-46 | OD-E01 capacitor C3 (tall can) | axis (86.065, −12.313), r_body 5.089, z_top 13.371 | mm | (86.065, −12.313), r 5.089, h 13.371 | ±0.084 | #10, #11 | §5 table (`cap_C3`) | scan | scan only; fit-critical flag in source |
| X-47 | OD-E01 capacitor C4 (tall can) | axis (88.251, −22.392), r_body 5.095, z_top 13.392 | mm | (88.251, −22.392), r 5.095, h 13.392 | ±0.084 | #10, #11 | §5 table (`cap_C4`) | scan | scan only; fit-critical flag in source |
| X-48 | OD-E01 scan↔CAD deviation gate | scan→CAD p95 0.7629 / max 1.3653 mm vs band p95 0.3 / max 0.8 | mm | p95 0.763 / max 1.365 | — | #10 | §8 gate table | report (QA) | FAIL vs band; delivered only under owner ACCEPT-BAND (BAND_NOT_MET) |
| X-49 | OD-E01 solder side / board bottom | not scanned; invented flat face | — | — | — | #10 | §11 L2 | report (limitation) | not fit for solder-side or thickness-critical fits |
| X-50 | OD-E01 absolute scale | not caliper-verified; units assumed mm | — | — | — | #10 | §11 L1 | report (limitation) | no Tier-1 caliper run at all |
| X-51 | OD-E02 envelope (datum frame) | bbox max [38.16, 16.1729, 18.9511]; min [−38.6285, −37.4736, −29.2147]; size [76.7885, 53.6465, 48.1658] | mm | max (38.16, 16.17, 18.95); min (−38.63, −37.47, −29.21); size 76.79 × 53.65 × 48.17 | — | #12 | §2 table | scan (export_check.json) | fit-critical: scan only |
| X-52 | OD-E02 screw hole L, position and bores | centre (−13.2349, −7.9445); counterbore r 3.788; through-bore r 1.7688 | mm | (−13.235, −7.945); cb r 3.788 (Ø7.576); through r 1.769 (Ø3.538) | cb ±0.03, through ±0.05 | #12, #13 | §5 table (`screw_L_*`) | scan | scan only; fit-critical flag in source |
| X-53 | OD-E02 screw hole R, position and bores | centre (12.7485, −8.0013); counterbore r 3.7418; through-bore r 1.7206 | mm | (12.749, −8.001); cb r 3.742 (Ø7.484); through r 1.721 (Ø3.441) | cb ±0.03, through ±0.05 | #12, #13 | §5 table (`screw_R_*`) | scan | scan only; fit-critical flag in source |
| X-54 | OD-E02 screw hole L, front (offset) bore | centre (−12.9534, −7.8192), r 3.3781; top z −11.8357 (scan's deepest view; true depth unseen) | mm | (−12.953, −7.819), r 3.378; z −11.836 | ±0.05 (position/r), ±0.3 (z) | #12, #13 | §5 table (`screw_L_front`) | scan | scan only; bore continues deeper, unscanned |
| X-55 | OD-E02 screw hole R, front (offset) bore | centre (13.0483, −8.0557), r 3.3248; top z −12.4694 (scan's deepest view) | mm | (13.048, −8.056), r 3.325; z −12.469 | ±0.05 (position/r), ±0.3 (z) | #12, #13 | §5 table (`screw_R_front`) | scan | scan only; bore continues deeper, unscanned |
| X-56 | OD-E02 scan↔CAD deviation gate | scan→CAD p95 0.2365 / max 0.9223; CAD→scan observable p95 0.6326 / max 5.4217 vs band p95 0.3 / max 0.8 | mm | see left | — | #12 | §8 gate table | report (QA) | FAIL vs band; delivered only under owner ACCEPT-BAND (BAND_NOT_MET) |
| X-57 | OD-E02 unscanned/assumed regions | connector shroud interior, shroud-to-rim slot floor, screw through-bores, cap-collar recess ceilings | — | — | — | #12 | §11 L2, §12 | report (limitation) | holds almost all of the observable CAD↔scan band miss |

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-58 | Material: PETG, printed | "OD-C08, Electronics bay tray, PETG, printed" | #5 | REQUEST.md §BOM row |
| X-59 | Material (BOM row, duplicate) | row `OD-C08,OD-C00,PRINT,Electronics bay tray,,,1,DESIGN,PETG,printed,print,#8,proposed` | #7 | bom_rows.csv |
| X-60 | Location / zone | "OD-C08 with either path within x 70 … 120, z −240 … −30 behind the bulkhead, its own tray screwed to bulkhead and plate later" | #5 (relaying #8 A-08) | REQUEST.md |
| X-61 | Bulkhead keep-clear allowance for OD-C08 | "OD-C08 is not designed and can keep 3 mm from the wall" | #5 (relaying #9 A-07) | REQUEST.md |
| X-62 | Electronics path chosen | "c08 i will use original pcb for this stage" (the Usta, project thread "Chassis C08 C10 C11", 2026-10-01 10:58Z) | #5 | REQUEST.md, Usta's words |
| X-63 | Order-of-work row for this job | "`OD-C08` electronics bay tray \| OD-E01, OD-E02 (path 1) or OD-E51…E58 (path 2) \| the Usta picks the path" | #6 | PROJECT_RULES.md, chassis/README.md order of work row 9 |
| X-64 | Two-zone layout rule | "Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — ... In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #6 | PROJECT_RULES.md §6 rule 1 |
| X-65 | Thermal map / material rule | "SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #6 | PROJECT_RULES.md §6 rule 3 |
| X-66 | Serviceability rule | "Serviceability is the point. ... top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #6 | PROJECT_RULES.md §6 rule 4 |
| X-67 | Safety spec | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #6 | PROJECT_RULES.md §6 rule 7 |
| X-68 | Insert / screw standard | "M3 heat-set inserts + M3 screws (the thesis tapped printed holes; inserts are better)" | #6 | PROJECT_RULES.md §3.10 |
| X-69 | Fastener BOM: insert | `OD-F01,OD-000,STD,M3 heat-set insert (Ø4.0 bore × 6; 26 in the chassis),,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo` | #7 | bom_rows.csv |
| X-70 | Fastener BOM: screw | `OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo` | #7 | bom_rows.csv |
| X-71 | Printers / machine profiles | "Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into `oguz-atolye/atolye/machines/`." | #6 | PROJECT_RULES.md, chassis/README.md |
| X-72 | Data class | "Data class PUBLIC (CC BY 4.0)." | #5 | REQUEST.md, standing instruction |
| X-73 | Standing instruction, process | "Design every 3D-printable part of open-dedica ... with the pipeline, in the order of `chassis/README.md`; ask the Usta only where a decision is needed; write open questions as `A-##` rows in the ledger and proceed. Every scan- or report-derived value is an assumption until the Usta confirms it; calipers beat scans." | #5 | REQUEST.md, standing instruction |
| X-74 | Component mount path for electronics (BOM OD-E00) | `OD-E00,OD-000,ASM,Electronics (choose Path 1 OEM or Path 2 open controller),,,1,DESIGN,,,,#8,todo` | #7 | bom_rows.csv |
| X-75 | Power PCB BOM row | `OD-E01,OD-E00,OEM,Power PCB 230 V — Path 1,59,AS00002829,1,SCAN,,AliExpress 4001101696035 / eBay,35–45,#33,modeled` | #7 | bom_rows.csv |
| X-76 | Control board BOM row | `OD-E02,OD-E00,OEM,Control board assembly (front buttons) — Path 1,15,7313285189,1,SCAN,,FixPart / eBay,15–25,#34,modeled` | #7 | bom_rows.csv |
| X-77 | OD-C01 reserved electronics-bay zone (ledger row) | "OD-C08 with either path within x 70 … 120, z −240 … −30 behind the bulkhead, its own tray screwed to bulkhead and plate later" (risk: "the bay is too small for path 1's OD-E01 (scanned)") | #8 | §6 A-08 |
| X-78 | OD-C02 keep-clear allowance (ledger row) | "the base rail (to x 71) and the top rail (to x 70.5) reach ≤ 1 mm into the bay zone x ≥ 70; OD-C08 is not designed and can keep 3 mm from the wall" (risk: "the bay tray does not fit") | #9 | §6 A-07 |
| X-79 | OD-E01 claim boundary (fit use) | "Fit for: component-side envelope and clearance studies for an enclosure (lid heights, part positions, mounting holes, faston access), with the band miss and limitations above in mind" / "Not fit for: manufacture, tooling, PCB footprint or electrical work" | #10 | §13 |
| X-80 | OD-E02 claim boundary (fit use) | "Fit for: envelope, packaging and fit studies of the scanned assembly in the machine front panel" / "Not fit for: tooling, manufacture or fit-critical use of the connector shroud interior, the shroud-to-rim slot, the screw bores or the cap-collar gaps" | #12 | §13 |

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-25 … X-30 | OD-E01 holes H1…H6 are given (positions, radii) but nothing says which of the six are used to fasten the board into the tray, or whether clips/standoffs are used instead. How is OD-E01 fastened to OD-C08? |
| 2 | X-20 … X-24 | No row gives the board's orientation inside the tray (component side up or down, which edge faces the bulkhead, rotation about the vertical). What orientation does OD-E01 take in the x 70…120, z −240…−30 zone? |
| 3 | X-43 … X-45, X-40 … X-42 | No input gives the wire routes from OD-E01's connectors (J1, J2, J3) and faston tabs to the bulkhead's four wire windows (X-16…X-19), or which window each wire bundle uses. What are the wire routes and which window does each connector/faston group use? |
| 4 | X-58, X-60 | No input gives the mains cord entry point, its grommet, or its path to OD-E01 (BOM rows OD-E06 power cord, OD-F06 spade terminals exist but no routing). Where does the mains cord enter the machine and reach the tray? |
| 5 | X-64, X-67 | No input states creepage/clearance distances for mains safety on or around the tray (PROJECT_RULES.md names the safety rules in general but gives no numeric creepage/clearance values). What creepage and clearance distances must OD-C08 hold around mains-carrying parts of OD-E01? |
| 6 | X-60, X-68 … X-70 | REQUEST.md says the tray is "screwed to bulkhead and plate later" but no input gives a hole pattern, count, or position for this fastening. How does OD-C08 fasten to OD-C01 and OD-C02 (hole pattern, count)? |
| 7 | X-62, X-63, X-76 | Chassis order-of-work row 9 designs OD-C08 "against OD-E01, OD-E02"; row 10 designs OD-C09 (front panel) "against OD-G01 mouth, OD-E02 buttons"; the job's own "what it is for" section says OD-E02's "place (behind the front panel OD-C09) is not designed" and is a gap. Does OD-C08 carry OD-E02 at all, or does OD-E02 belong entirely to OD-C09 (front panel)? |
| 8 | X-58 | Neither REQUEST.md, PROJECT_RULES.md, nor bom_rows.csv names a target printer or build volume for OD-C08 (OD-C01 used Kobra Max 3 at 420×420×500 mm per memory, A-09; OD-C02 used K1C at 220×220×250 mm per memory, A-08 — both for other parts). Which printer and build volume applies to OD-C08? |
| 9 | X-48, X-56 | Both OD-E01 and OD-E02 deliveries are verdict `BAND_NOT_MET`, accepted by the owner only for "component-side envelope and clearance studies" (OD-E01) and "envelope, packaging and fit studies" (OD-E02), not for fit-critical or tooling use. Does the Usta accept designing OD-C08's fastening features (which are fit-critical, e.g. around holes H1/H2 or the screw bores) against this band-missed geometry, or does the tray need a caliper check first? |
| 10 | X-74 … X-76 | Switches, buttons OD-E03 (microswitch), OD-E04 (on/off push button), OD-E05 (unipolar switch) are listed in bom_rows.csv as `todo` with no SCAN/ENVELOPE source; it is not given whether any of them mount on OD-C08. Do any of OD-E03/E04/E05 mount on the electronics bay tray? |
| 11 | X-16 … X-19 | OD-C02 spec A-13 says the wire windows "take rubber grommets or the wires are tied clear" and this is "OD-E00's" responsibility, not OD-C02's or (by extension) OD-C08's; no input assigns grommet parts or sealing to OD-C08. Does OD-C08 need grommet bosses, or is sealing entirely the wiring loom's concern? |
| 12 | — (general) | The brief states the side panel OD-C13, top panel OD-C10, back panel OD-C11, wiring looms, and OD-E02's place behind OD-C09 are all not designed. None of these appear as geometry in any input; they remain open for the design stage, not resolved here. |

## §5 Unreadable

None. Every listed input was read in full (markdown and CSV) or hashed and listed (the four STEP files, per the brief's rule 6 instruction that their geometry is measured later by `tools/measure`).
