# INTAKE v01 — 20260930-od-c05-group-head-carrier

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
| 1 | 00_Spec/inputs/OD-G01_housing_C1_v02.step | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | 437578 | STEP | n/a | listed and hashed only (geometry measured later, rule 6) |
| 2 | 00_Spec/inputs/OD-G04_brewing_gasket_support.step | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | 768162 | STEP | n/a | listed and hashed only (geometry measured later, rule 6) |
| 3 | 00_Spec/inputs/OD-H11_thermoblock.step | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff | 2400893 | STEP | n/a | listed and hashed only (geometry measured later, rule 6) |
| 4 | 00_Spec/inputs/REQUEST.md | b3aa5d8826defcffe0ff4f5a7b5850f3ecc6e3ccf3a2c9ae78a4e1de6a98fb02 | 2216 | Markdown | 1 page | full text read |
| 5 | 00_Spec/inputs/PROJECT_RULES.md | c9f89b58d9c3e0d0f7261dfcde6a71fd24c599161a87d3d5ad4a0ff651a926de | 8022 | Markdown | 1 page | full text read |
| 6 | 00_Spec/inputs/bom_rows.csv | 2a908505dabd079c662771c0dfba846b8427471b8a3e20990afd37f8aea3f74c | 3811 | CSV | 39 rows | full table read |
| 7 | 00_Spec/inputs/reports/OD-G01_group_head_housing/DESIGN_SPEC_v1.3.md | 55841f6ba178ac7250a22e156b55941002437a794ce008f231c1ea090138e44b | 25091 | Markdown | §1-§8 | full text read |
| 8 | 00_Spec/inputs/reports/OD-G01_group_head_housing/REPORT_v02.md | 02ee81dea9dc7fd9d2dd249cc32481fa96c61e6c89c627df5d8c59466742d5b6 | 62645 | Markdown | §1-§10 + closing JSON block | full text read; the closing JSON block (after §10) restates the §3 gate table and §4 sweep table already read in prose/markdown form and was scanned for new content only |
| 9 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/README.md | 0fcc6197a2aa5ea4acff96600133ab6cde7e8a01b75b39aa4e9356dd01b0db82 | 3759 | Markdown | 1 page | full text read |
| 10 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/deliver_README.md | f1fb8ce7b203b676d4606327e1604c5373d2616bb05382dab08f54e614cb9830 | 31612 | Markdown | §1-§16 | full text read |
| 11 | 00_Spec/inputs/reports/OD-H11_thermoblock/README.md | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0 | 5385 | Markdown | 1 page | full text read |
| 12 | 00_Spec/inputs/reports/OD-H11_thermoblock/params.json | 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c5203 | 7091 | JSON | n/a | full file read |
| 13 | 00_Spec/inputs/reports/OD-H11_thermoblock/ports.json | 77fbb8b2a53e929216ddea4752a7b18e67f6f57ba1ba3864ec24e179cf224fd5 | 3865 | JSON | n/a | full file read |
| 14 | 00_Spec/inputs/reports/OD-H11_thermoblock/export_check.json | ecba71c6aebb34c59dd7bcb61d67f09662d07954a724ae3729171bc1fc547a73 | 1326 | JSON | n/a | full file read |
| 15 | 00_Spec/inputs/scan/OD-H11_thermoblock/README.md | 71737a61742eef1ef2ac7f36ece62e62ae96a305fe80206efe94c6c3c1eaa75c | 1156 | Markdown | 1 page | full text read |
| 16 | 00_Spec/inputs/scan/OD-H11_thermoblock/calipers.md | 761d29432f8db6afe181247b16b8f23a7c5a1033a394dd5a81e3c12ae623c444 | 536 | Markdown | 1 page | full text read (blank template, see §5) |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-G01 rear slab thickness, design value | 5.00 | mm | 5.00 | — | #7 | §4 C1 | text (design description) | not confirmed |
| X-02 | OD-G01 rear slab z range, design value | z −24.94 … −19.94 | mm | −24.94 … −19.94 | — | #7 | §4 C1 | text | not confirmed |
| X-03 | OD-G01 rear slab thickness, measured (REQ-11) | 5.000 | mm | 5.000 | 5.00 ± 0.10 (spec band) | #8 | §3 gate table REQ-11 | CAD measurement on re-imported STEP | not confirmed |
| X-04 | OD-G01 rear flange square, design value | 100 × 100, corners R8 | mm | 100.00 × 100.00, R 8.00 | — | #7 | §4 C1 | text | not confirmed |
| X-05 | OD-G01 envelope size, measured (U-02) | 100.0000002 × 100.0000002 × 28.2400002 | mm | 100.0000002 × 100.0000002 × 28.2400002 | each in [spec − 0.1, spec + 0.1] | #8 | §3 gate table U-02 / envelope_within_spec | CAD measurement | not confirmed |
| X-06 | OD-G01 envelope bounding box, measured | min (−50.0000001, −50.0000001, −24.9400001), max (50.0000001, 50.0000001, 3.3000001) | mm | same | — | #8 | §5 Build facts | CAD measurement | not confirmed |
| X-07 | OD-G01 rear face z, design value | −24.94 | mm | −24.94 | — | #7 | §4 C1; REQUEST.md quote | text | not confirmed |
| X-08 | OD-G01 front face z, design value | +3.30 | mm | +3.30 | — | #7 | §4 C1 | text | not confirmed |
| X-09 | OD-G01 outer wall diameter, design value | Ø86.2 | mm | Ø86.2 | — | #7 | §4 C1 | text | not confirmed |
| X-10 | OD-G01 four M3 heat-set insert positions | (±44, ±44) from the rear face | mm | (±44.00, ±44.00) | — | #7 | §2 (frame), §4 C1, REQ-08 | text | not confirmed |
| X-11 | OD-G01 insert positions, measured (REQ-08) | four Ø4.000 bores at (±44.0000, ±44.0000), offset 0.000 | mm | (±44.0000, ±44.0000) | offset ≤ 0.10 | #8 | §3 gate table REQ-08 | CAD measurement | not confirmed |
| X-12 | OD-G01 insert hole size, design value | Ø4.0 × depth 5.7 from the rear face, no mouth chamfer | mm | Ø4.00 × 5.70 | Ø 4.0 ± 0.05 (spec D-05b) | #7 | §4 C1; §5 D-05a, D-05b | text | not confirmed |
| X-13 | OD-G01 insert hole, measured (D-05b) | Ø4.0000, depth 5.7000 from the rear face, all four | mm | Ø4.0000 × 5.7000 | Ø in [3.95, 4.05]; depth ≥ 5.7 | #8 | §3 gate table D-05b | CAD measurement | not confirmed; margin by construction is 2.7e-15 mm (§10 item 4) |
| X-14 | OD-G01 insert boss, material across each hole, design floor | ≥ 8.0 (D-05a) / ≥ 3.0 around each hole (J-05) | mm | ≥ 8.0 / ≥ 3.0 | Hard gate floors | #7 | §5 D-05a, J-05 | text (gate threshold, not a built value) | not confirmed |
| X-15 | OD-G01 insert boss, built/measured | boss OD 10.30 (D-05a, worst of 288 rays); wall around axis 3.1500 (J-05) | mm | 10.30 / 3.1500 | D-05a ≥ 8.0; J-05 ≥ 3.0 | #8 | §3 gate table D-05a, J-05; §8 deviation item 2 | CAD measurement | not confirmed; report notes plan named 8.00, built 10.30 (§8 item 2, adopted by spec 1.2) |
| X-16 | OD-G01 insert boss root fillet, achieved | R 1.0 requested → R 0.6 achieved | mm | R 0.6 | requested R 1.0 | #8 | §5 Build facts; §8 item — | CAD measurement | not confirmed; no §5 row reads this dimension |
| X-17 | OD-G01 hub opening (Ø26 through-bore), design value | Ø26.0, straight through the slab, no rear counterbore | mm | Ø26.00 | Ø 26.0 ± 0.1 (REQ-06) | #7 | §4 C1; REQ-06; A-10, A-24 | text | not confirmed |
| X-18 | OD-G01 hub opening, measured (REQ-06) | Ø26.000, axis offset 0.000, through = 1 | mm | Ø26.000 | Ø 26.0 ± 0.1, on axis | #8 | §3 gate table REQ-06 | CAD measurement | not confirmed |
| X-19 | OD-G01 pair-B (OEM screws) holes, design value | two Ø3.8 through-holes at r 19.03, θ 119.3° and 304.0°, each under a Ø9.0 recess 2.30 deep from the floor | mm/deg | Ø3.80 at r 19.03, θ 119.3°/304.0°; recess Ø9.00 × 2.30 | offset ≤ 0.10; Ø9.0 ± 0.1; 2.30 ± 0.10 (REQ-07) | #7 | §4 C1; REQ-07 | text | not confirmed; A-12, A-26 |
| X-20 | OD-G01 pair-B holes, measured (REQ-07) | two Ø3.800 through-holes at r 19.03, θ 119.3°/304.0°, offset 2.6e-07; recesses Ø9.000 × 2.300 deep from the floor | mm/deg | same | offset ≤ 0.10; Ø9.0 ± 0.1; 2.30 ± 0.10 | #8 | §3 gate table REQ-07 | CAD measurement | not confirmed |
| X-21 | OD-G01 pair-A (OD-G04 boss pair A) holes, design value | two Ø9.0 through-holes at r 15.5, θ 359.5° and 179.0°, merging with the Ø26 opening into the OEM's two keyhole lobes | mm/deg | Ø9.00 at r 15.5, θ 359.5°/179.0° | offset ≤ 0.10; Ø9.0 ± 0.1 (REQ-13) | #7 | §4 C1; REQ-13; A-11 | text | not confirmed |
| X-22 | OD-G01 pair-A holes, measured (REQ-13) | two Ø9.000 through-holes at r 15.500, θ 359.5°/179.0°, offset 4.1e-07, through = 1 | mm/deg | same | Ø9.0 ± 0.1; offset ≤ 0.10 | #8 | §3 gate table REQ-13 | CAD measurement | not confirmed |
| X-23 | OD-G01 clearance hole floor for a fastener (D-04a) | pair-B holes Ø ≥ 3.5 + 0.25 = 3.75 (designed Ø3.8) | mm | ≥ 3.75, designed 3.80 | — | #7 | §5 D-04a | text | not confirmed; A-26 |
| X-24 | OD-G01 brew load reaction on lugs (REQ-12) | 15 bar × π(25.5)² = 3.06 kN on a Ø51 basket | kN | 3.06 kN | not gated geometrically; bench test only | #7 | §5 REQ-12; §6 A-21 | text (derivation) | not confirmed; INCONCLUSIVE until OD-T01 bench test |
| X-25 | OD-G01 mass and material density (reported, not gated) | 96.532 g at 1070 kg/m³, ASA | g / kg/m³ | 96.532 g | — | #8 | §5 Build facts | CAD measurement | not confirmed; A-15 |
| X-26 | OD-G01 carrier-interface ledger note (A-18) | "4 × M3 inserts at (±44, ±44) from the rear, flange 100 × 100 × 4" | mm | flange stated as 100 × 100 × 4 | — | #7 | §6 A-18 | text | conflicts with X-01/X-02/X-03/X-05 (built and measured slab is 5.00 mm thick, not 4); see §4 |
| X-27 | OD-G04 hub tube outer radius (own frame) | `hub_tube_R_out` 10.03 | mm | Ø20.06 (2×10.03) | ± 0.0489 | #10 | §5 parameter table | scan measurement (round-within-noise) | not confirmed; fit-critical value from a scan, not confirmable from an image |
| X-28 | OD-G04 hub tube bottom z (own frame) | `hub_tube_bot_z` −15.73 | mm | −15.73 | ± 0.0489 | #10 | §5 parameter table | scan measurement | not confirmed |
| X-29 | OD-G04 stepped bore, lower radius (own frame) | `hub_bore_R_lower` 8.38 | mm | 8.38 | ± 0.0489 | #10 | §5 parameter table | scan measurement | not confirmed |
| X-30 | OD-G04 stepped bore, upper radius (own frame) | `hub_bore_R_upper` 7.81 | mm | 7.81 | ± 0.0489 | #10 | §5 parameter table | scan measurement | not confirmed |
| X-31 | OD-G04 stepped bore, step z (own frame) | `hub_bore_step_z` −10.45 | mm | −10.45 | ± 0.0489 | #10 | §5 parameter table | scan measurement | not confirmed |
| X-32 | OD-G04 flange bottom z (own frame) | `flange_bot_z` −13.12 | mm | −13.12 | ± 0.0489; "critical" flagged | #10 | §5 parameter table | scan measurement | not confirmed; fit-critical |
| X-33 | OD-G04 plate back z (own frame, datum) | `plate_back_z` 0 (measured −0.02) | mm | 0.00 (measured −0.02) | ± 0.0489; "critical" flagged | #10 | §5 parameter table | scan measurement | not confirmed; fit-critical |
| X-34 | OD-G04 datum-frame bounding box | max [34.52, 34.52, 1.09]; min [−31.1763, −34.48, −16.12]; size [65.6963, 69.00, 17.21] | mm | same | — | #10 | §2 deliverables table | CAD measurement of the delivered STEP | not confirmed |
| X-35 | OD-G01's report placement of OD-G04: back face location | OD-G04 plate back face lands at housing z −6.82 | mm | −6.82 | — | #8 | §5 Build facts | CAD measurement, placed solid | not confirmed; derived from A-13 |
| X-36 | OD-G01's report placement of OD-G04: hub bottom | hub bottom −22.550, OD 20.06 | mm | −22.550 (housing frame); OD 20.06 | — | #8 | §5 Build facts | CAD measurement, placed solid | not confirmed; A-24 notes the hub tube then ends 2.4 mm inside the 5.00 mm slab |
| X-37 | OD-G01's report placement of OD-G04: envelope as placed | z −22.940 … −5.730 | mm | −22.940 … −5.730 | — | #8 | §5 Build facts | CAD measurement, placed solid | not confirmed |
| X-38 | OD-G01's report placement of OD-G04: pair A / pair B extents as placed | pair A reaching z −22.940, spanning r 12.01 … 18.99; pair B reaching z −21.700 | mm | same | — | #8 | §5 Build facts | CAD measurement, placed solid | not confirmed |
| X-39 | OD-G04 deviation gate (scan ↔ CAD, default ICP, reported/gated) | scan→CAD p95 0.3756 / max 0.8316; CAD→scan observable p95 2.3247 / max 4.5923 | mm | same | band p95 ≤ 0.30 / max ≤ 0.80 | #10 | §8 deviation table | scan-to-CAD deviation gate | FAIL against the band; not confirmed; BAND_NOT_MET, accepted by the owner for delivery (2026-09-25) |
| X-40 | OD-G04 deviation, datum-frame / diagnostic ICP (informational, not gated) | datum-frame p95 0.218; diagnostic ICP (1 mm correspondence) p95 0.194 | mm | same | band p95 ≤ 0.30 | #9, #10 | README "scan → CAD p95 miss" note; deliver_README §9 | scan-to-CAD deviation gate, alternate registration | PASS on these readings; not confirmed; not the gated number |
| X-41 | OD-H11 datum frame | base at Z = 0, body axis = +Z, top face Z = 47.64 | mm | Z = 0 base; top face 47.64 | — | #11 | Deliverables table | text (frame definition) | not confirmed |
| X-42 | OD-H11 re-import envelope / bounding box | datum bbox 86.11 × 106.89 × 50.79; export_check bbox_min [−43.27, −53.508, −0.0], bbox_max [42.839, 53.381, 50.79] | mm | same | — | #11, #14 | README "Re-import check"; export_check.json | CAD measurement | not confirmed; conflict check: 86.11 = 42.839−(−43.27) ✓, 106.89 = 53.381−(−53.508) ✓, 50.79 matches both — no conflict found |
| X-43 | OD-H11 volume | 159 767 mm³ (repaired scan: 160 289 mm³) | mm³ | 159767 (159766.5 in export_check.json) | — | #11, #14 | README; export_check.json | CAD measurement | not confirmed |
| X-44 | OD-H11 suggested caliper dimensions (not yet measured) | body Ø top ~69.9 / bottom ~67.6; height 47.64; counterbore Ø28.3 (at base); pipe Ø / positions; terminal positions; lug hole Ø | mm | same | — | #11 | "Assumptions / open questions" | text (suggested checks, not measured) | not confirmed; calipers.md (#16) is blank — see §5 |
| X-45 | OD-H11 body cone radii (params.json, cross-check against README's suggested body Ø) | `coneA` [33.78, 34.95]; `coneB` [34.97, 33.85] over `sectorB` θ 69.0–172.0° | mm/deg | R 33.78–34.95 / R 34.97–33.85 | — | #12 | params.json | scan-derived parameter | not confirmed; ×2 ≈ Ø67.56–69.90, consistent with README's "body Ø top ~69.9 / bottom ~67.6" — no conflict found |
| X-46 | OD-H11 counterbore radii (params.json, cross-check against README's suggested Ø28.3) | `r_cb_floor` 14.13, `r_cb_top` 14.99 | mm | R 14.13 / R 14.99 | — | #12 | params.json | scan-derived parameter | not confirmed; ×2 = Ø28.26, consistent with README's "counterbore Ø28.3" — no conflict found |
| X-47 | OD-H11 water pipe 1: position, direction, bore | origin (39.321, 27.174, 42.7); direction (−0.35899, −0.93334, 0.0); bore_r 1.95; bore_depth 2.3 | mm | same | — | #13 | ports.json "pipes"[0] | scan-derived parameter | not confirmed; fit-critical, not confirmable from a scan |
| X-48 | OD-H11 water pipe 2: position, direction, bore | origin (−16.058, 49.403, 5.3); direction (−0.35899, −0.93334, 0.0); bore_r 1.95; bore_depth 2.3 | mm | same | — | #13 | ports.json "pipes"[1] | scan-derived parameter | not confirmed |
| X-49 | OD-H11 heater terminal 1: position, direction, blade | origin (−0.558, 32.64, 5.2); direction (−0.58599, −0.81031, 0.0); blade thickness 0.8; hole_d 1.7 | mm | same | — | #13 | ports.json "terminals"[0] | scan-derived parameter | not confirmed |
| X-50 | OD-H11 heater terminal 2: position, direction, blade | origin (17.032, 25.811, 42.5); direction (0.10407, 0.99457, 0.0); blade thickness 0.8; hole_d 2.1 | mm | same | — | #13 | ports.json "terminals"[1] | scan-derived parameter | not confirmed |
| X-51 | OD-H11 deviation gate (scan ↔ CAD, datum frame) | scan→CAD RMS 0.252, p95 0.474, p99 1.05, max 2.71; CAD→scan RMS 0.268, p95 0.430, p99 0.97, max 4.77 | mm | same | band p95 ≤ 0.30 / max ≤ 0.80 | #11 | Deviation gate table | scan-to-CAD deviation gate | FAIL against the band; not confirmed; verdict PARTIAL |
| X-52 | OD-H11 regional scan→CAD p95 | base 0.37 · top face 0.34 · main body 0.53 · lugs/pipes/terminals 0.54 | mm | same | — | #11 | Deviation gate section | scan-to-CAD deviation gate | not confirmed; the lugs/pipes/terminals region (0.54) is the one closest to what a carrier or mount would touch |
| X-53 | OD-H11 scan → datum transform | 4×4 matrix in export_check.json `T_scan_to_datum` | — | — | — | #14 | export_check.json | file content | not confirmed; recorded for traceability only, not a dimension the carrier uses directly |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-60 | OD-C05 part identity and material/process | "Group head carrier (ties OD-G00 to frame)" ... ASA ... printed ... status "proposed" | #6 | bom_rows.csv row `OD-C05,OD-C00,PRINT,...` |
| X-61 | OD-C05 chassis order-of-work and blocker | "`OD-C05` group head carrier | OD-G01's rear flange, OD-H11 outlet side | OD-G01" | #5 | PROJECT_RULES.md, chassis/README.md order-of-work table, row 2 |
| X-62 | OD-C05 job scope (from the standing instruction) | "The carrier takes the housing by those four inserts, passes the OD-G04 hub tube and the hot water tube (TUBE 7 from the 3-way valve connector OD-H23 port C) behind it, holds the group head ≥ 95 mm above the drip tray ... and ties down to the printed base frame OD-C01, which is not designed yet" | #4 | REQUEST.md, para 2 |
| X-63 | OD-C05 foot interface is a design choice, with precedent | "the foot interface is a design choice of this job, recorded as an assumption for OD-C01 to follow (OD-C03 and OD-C04 chose four Ø3.4 through-holes for M3 screws into OD-C01 inserts)" | #4 | REQUEST.md, para 2 |
| X-64 | Air gap to the thermoblock | "wherever it ends up, every printed wall keeps ≥ 10 mm of air to it" | #4 | REQUEST.md, para 2 |
| X-65 | Air gap to the thermoblock (project rule, chassis order-of-work) | "`OD-C04` thermoblock mount (≥10 mm air gap to printed walls)" | #6 | bom_rows.csv row `OD-C04` |
| X-66 | Group head height above the drip tray | "Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 5 |
| X-67 | Drip tray not scanned | "The drip tray `OD-C21` is not scanned; its height under the group head is a gap too." | #4 | REQUEST.md, para 2 |
| X-68 | Two-zone layout / wet-electric separation | "Two-zone layout. Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) ... In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 1 |
| X-69 | Anti-vibration mounting | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 2 |
| X-70 | Thermal map / material by zone | "Respect the thermal map. Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 3 |
| X-71 | Serviceability | "Serviceability is the point. The Dedica's worst trait (thesis: \"very difficult to disassemble\") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 4 |
| X-72 | Sensor bosses left in the chassis design from day one | "Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 6 |
| X-73 | Safety spec (piping rating, TCO, PAT, RCD) | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #5 | PROJECT_RULES.md, SOURCING_GUIDE §6 rule 7 |
| X-74 | Safety note (mains voltage, heat, pressure) | "this machine runs on mains voltage (230 V / 120 V), heats water to ~125 °C and pressurizes it to 15 bar. Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA." | #5 | PROJECT_RULES.md, README.md safety note |
| X-75 | Fastener standard: M3 heat-set insert | "OD-F01,OD-000,STD,M3 heat-set insert,,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo" | #6 | bom_rows.csv row `OD-F01` |
| X-76 | Fastener standard: M3×8 screw | "OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo" | #6 | bom_rows.csv row `OD-F02` |
| X-77 | Water path, Connector port C → group head | "Connector port C → Group head `OD-G00` / portafilter `OD-G10` | TUBE 7 | hot | Coffee path" | #5 | PROJECT_RULES.md, WATER_FLOW.md flow table row 7 |
| X-78 | Tube numbering, unresolved | "TUBE 1–7 follow the numbering of the community EC685M flow diagram ... Only the first two tubes (`OD-W11`, `OD-H25`) have been matched to BOM lines so far. The rest will be matched to `OD-W12…W15` during teardown." | #5 | PROJECT_RULES.md, WATER_FLOW.md "Tube numbering" |
| X-79 | Standing instruction: deliverables and assumption discipline | "design every 3D-printable part of Open Dedica ... with the oguz-atolye pipeline; each part needs a parametric build script, STEP, STL/3MF and an independent review verdict; every value from a scan or report is an A-## assumption until the Usta confirms it; calipers beat scans; a fit-critical value cannot be confirmed from an image; data class PUBLIC (CC BY 4.0)." | #4 | REQUEST.md, para 1 |
| X-80 | OD-G01 rear flange as fixed since spec 1.2 (quoted in the standing instruction) | "the OD-G01 housing is at its third build round with its rear flange fixed since spec 1.2 (a 100 × 100 × 5 slab, rear face at its z −24.94, four M3 heat-set inserts at (±44, ±44) from the rear, hole Ø4.0 × 5.7, the Ø26 hub opening on the axis, the two OEM screws of OD-G04 driven from the rear; OD-G01 spec 1.3 A-17, A-18)" | #4 | REQUEST.md, para 2 |
| X-81 | Machine build volumes not yet read in | "Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into `oguz-atolye/atolye/machines/`." | #5 | PROJECT_RULES.md, chassis/README.md "Machine profiles" |
| X-82 | Sourcing/pricing rows touching this job's neighbours | "Brewing gasket support | 48: AS00005377 | €3"; "Thermoblock (generator 230 V 1300 W + plastic connector) ... 25–40" | #5, #6 | PROJECT_RULES.md §3.2/§3.3; bom_rows.csv rows OD-G04, OD-H11 |
| X-83 | REQ-12 brew load is a bench-test gate, not geometric | "REQ-12 (brew load) is a part gate answered only by the OD-T01 bench test; the review reports it INCONCLUSIVE and the delivery states it" | #7 | DESIGN_SPEC_v1.3.md §7 decisions table |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-01, X-02, X-03, X-05, X-26 | The OD-G01 spec's built and measured rear slab is 5.00 mm thick (z −24.94 … −19.94), but the spec's own §6 ledger row A-18 describes the carrier interface as "flange 100 × 100 × 4". Which is the carrier-facing flange thickness OD-C05 should design to: 5.00 mm (the built/measured value) or 4 mm (A-18's stated value)? |
| 2 | X-25 (this job's REQUEST.md), REQ context | The thermoblock OD-H11's position and orientation relative to the OD-G01 housing is not fixed by any input in this job. What is the intended placement (position, rotation, and which face/frame it references) of OD-H11 relative to OD-G01's rear flange, so the ≥ 10 mm air-gap requirement (X-64/X-65) can be checked? |
| 3 | X-67 | The drip tray OD-C21 is not scanned. What is its height under the group head (needed to verify the ≥ 95 mm group head height, X-66) and its footprint/position under the carrier? |
| 4 | X-77, X-78 | TUBE 7 (Connector port C → group head, the hot water tube the carrier must pass behind the housing) has no route, bend radius, or OD-H23 connector size/position given in any input. What is TUBE 7's routing and the OD-H23 port C geometry the carrier must clear? |
| 5 | X-62, X-63 | OD-C01 (the base frame the carrier ties down to) is not designed yet: its mounting interface and floor level are unknown beyond the precedent of OD-C03/OD-C04 (four Ø3.4 through-holes for M3 screws into OD-C01 inserts, X-63). Should OD-C05 assume that same interface, and at what floor level? |
| 6 | X-01…X-24 (OD-G01 frame) | DESIGN_SPEC_v1.3 §2 fixes the OD-G01 STEP's own coordinate frame (Z = cup axis, +Z toward the mouth, "in the machine +Z is horizontal and faces the user") but gives no rotation about that axis (θ = 0 reference) relative to the machine, and no input states the machine's front/up directions in OD-G01's frame. How is the housing clocked about its own Z axis in the finished machine, and what are the machine's front and up directions in the OD-G01 frame? |
| 7 | (no input) | No input states OD-C05's own print orientation or target machine (Creality K1C vs Anycubic Kobra Max 3, X-81). Which machine profile and print orientation should OD-C05 be designed against? |
| 8 | X-39, X-40 | OD-G04's scan-to-CAD deviation gate is BAND_NOT_MET on the default registration (p95 0.376 / max 0.832 vs band 0.30/0.80) and was delivered only on the owner's acceptance of that miss; a datum-frame/diagnostic reading passes (p95 0.218/0.194). Does OD-C05's design (clearance to the hub tube, X-27…X-31, X-36) rely on the gated (failing) number or the alternate (passing) reading, and is a caliper check on OD-G04 needed before OD-C05 is frozen? |
| 9 | X-51, X-52 | OD-H11's scan-to-CAD deviation gate is also PARTIAL (p95 0.474/0.430, both over the 0.30 band), and its pipe (X-47, X-48) and terminal (X-49, X-50) positions are flagged in its own README as needing calipers; `00_Spec/inputs/scan/OD-H11_thermoblock/calipers.md` (#16) is a blank template with no measured values. Should OD-C05's ≥ 10 mm air-gap check (X-64) be run against the as-scanned OD-H11 envelope, or held until calipers land? |
| 10 | X-36 (housing REPORT's placement of OD-G04), A-24 | The OD-G01 REPORT places OD-G04's hub tube bottom at housing z −22.550, 2.4 mm inside the 5.00 mm rear slab (housing floor −19.94 to slab bottom −24.94), and A-24 notes the envelope of the water-connection parts (OD-G07, OD-H14, OD-H15) that would reach the hub from behind is unknown. Since OD-C05 passes the hub tube and TUBE 7 behind the housing, what clearance must OD-C05 leave below the rear face for those un-scanned connection parts? |
| 11 | (no input, cf. DESIGN_SPEC_v1.3 §7/§10 REPORT_v02) | REPORT_v02 §10 records an unresolved 0.051 mm disagreement between A-05 (the OD-G09 lug underside, measured) and A-14 (the locked rim z, derived) in the OD-G01 assembly, still open at spec 1.3. This does not directly touch the carrier's rear-flange interface, but it affects the housing's mouth position (relevant to the ≥ 95 mm group head height, X-66, measured from the mouth). Does OD-C05's height check use the ledger's A-14 value (rim z −11.20) or the built housing's own measured contact (rim z −11.25103)? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None of the sixteen listed input files was unreadable. Two notes on content, not readability:

- `00_Spec/inputs/scan/OD-H11_thermoblock/calipers.md` (#16) is a blank template: its table header row is present but every data cell is empty ("To be filled in"). No caliper values exist for OD-H11 yet (see §4 question 9).
- `00_Spec/inputs/reports/OD-G04_brewing_gasket_support/deliver_README.md` (#10) references four catalogue photos under `input/photos/` and an overlay image under `qa/overlays/overlay.png`; the brief's input list does not include these image files under `00_Spec/inputs/`, so they were not read. `00_Spec/inputs/reports/OD-G04_brewing_gasket_support/README.md` (#9) states explicitly that these photo links are "intentionally broken" in this delivered copy.
