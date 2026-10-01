# INTAKE v01 — 20261001-od-c15-feet

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
| 1 | 00_Spec/inputs/REQUEST.md | a734976b74a9b18930400d3e27319034a9e829724db7b1a48be0ae95808308d0 | 2865 | Markdown | 1 | full text |
| 2 | 00_Spec/inputs/bom_rows.csv | d857768df5e204e7290d943592d309f014ec5b950b04964a1ee0d7d1f0e9f19c | 862 | CSV | 8 rows | full text |
| 3 | 00_Spec/inputs/CHASSIS_README.md | b7d09997bb99ef4d9fe185e19661688b94b3a4de87f06d6fcc50dd32afeb58f1 | 5976 | Markdown | 1 | full text |
| 4 | 00_Spec/inputs/SOURCING_GUIDE_s3_10.md | 64d7bf2180037ff6b2edee15bc2823e2176e030abd48421d05aef31f1ed7e926 | 505 | Markdown (extract §3.10) | 1 | full text |
| 5 | 00_Spec/inputs/SOURCING_GUIDE_s6.md | 9e5f68bc4ad318b99445f393304fbcf6e7378b40c57a74d66fb7a81fc31bf4cc | 933 | Markdown (extract §6) | 1 | full text |
| 6 | 00_Spec/inputs/OD-C01_DESIGN_SPEC.md | 75e1af2c360ce388c4db51aedd9f27f9691603f7addb5a98e965aacf4f238681 | 25226 | Markdown | 1 | full text |
| 7 | 00_Spec/inputs/OD-C01_RV01.md | 3d8995d95670709f5d9bbd344d687c5a0f4ce3668ce6d566af3e66f7159d381d | 22144 | Markdown | 1 | full text |
| 8 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP | — | listed and hashed only (intake rule 6); not opened; geometry measured later with `tools/measure` |

## §2 Dimensions — OD-C01 values a foot could touch or depend on

<!-- All values below are text/table values taken from OD-C01's own spec and its RV01 review, not measured by this intake from the STEP (rule 6). None are confirmed (rule 3); none are from a photo or scaled drawing. -->

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C01 plate footprint size (length × width) and thickness | 240 × 405, 6.0 | mm | 240.00 × 405.00 × 6.00 | within [spec − 0.1, spec + 0.1] (U-02) | #6, #7 | DESIGN_SPEC §4 C1; RV01 §2 U-02 (measured 240.000 × 6.000 × 405.000) | table / reviewer measurement | — |
| X-02 | OD-C01 plate envelope position (machine frame) | x ±120, y −6.0…0.0, z −305…+100 | mm | x ±120.0, y −6.0…0.0, z −305.0…+100.0 | ±0.1 per U-02 | #6, #7 | DESIGN_SPEC §4 C1; RV01 §2 U-02 | table / reviewer measurement | — |
| X-03 | Top face level (the floor plane every mount's foot stands on) | y = 0.00 | mm | 0.00 | ±0.10 | #6, #7 | DESIGN_SPEC §5 REQ-07; RV01 §2 REQ-07 (measured max_y 0.000) | gate row / reviewer measurement | — |
| X-04 | Bottom face level (plate occupies y −6.0 … 0) | y = −6.0 | mm | −6.00 | — | #6 | DESIGN_SPEC §4 C1 | text | — |
| X-05 | Corner radius, four corners of the plate | R 10 | mm | 10.00 | — | #6, #7 | DESIGN_SPEC §4 C1; RV01 §3 F01 census ("4 convex R10 corner cylinders") | text / reviewer census | — |
| X-06 | Feet holes — diameter and positions | four Ø3.4 through-holes at (x ±110.0, z +90.0) and (x ±110.0, z −295.0) | mm | Ø3.40 at (±110.0, +90.0) and (±110.0, −295.0) | — | #6 | DESIGN_SPEC §4 C1, §5 REQ-05; A-12 | text / gate row | fit-critical; not a confirmed value |
| X-07 | Feet holes — tolerance | Ø3.4 ± 0.1, position offset ≤ 0.10 | mm | Ø3.40 ± 0.10; offset ≤ 0.10 | ±0.1 / ≤0.10 | #6 | DESIGN_SPEC §5 REQ-05 | gate row | fit-critical |
| X-08 | Feet holes — as measured by the reviewer | four Ø3.400 through, offset 0.000; each concentric with its R10 corner | mm | Ø3.400, offset 0.000 | — | #7 | RV01 §2 REQ-05 / D-04a | reviewer measurement | fit-critical |
| X-09 | Feet hole — minimum clearance diameter for the fastener | Ø ≥ 3.25 (designed Ø3.4) | mm | ≥ 3.25 | — | #6 | DESIGN_SPEC §5 D-04a (assumes A-12) | gate row | — |
| X-10 | Feet hole to corner — web | 8.3 | mm | 8.30 | — | #7 | RV01 §2 REQ-05 note | reviewer measurement | — |
| X-11 | Insert holes under OD-C05 carrier (nearest reserved zone, not the feet) | four Ø4.0 at (x ±35.0, z −40.0) and (x ±35.0, z −60.0) | mm | Ø4.00 at (±35.0, −40.0/−60.0) | ±0.05, offset ≤0.10 | #6 | DESIGN_SPEC §5 REQ-01 | gate row | — |
| X-12 | Insert holes under OD-C04 thermoblock mount | four Ø4.0 at (x ±40.0, z −148.0) and (x ±40.0, z −114.0) | mm | Ø4.00 at (±40.0, −148.0/−114.0) | ±0.05, offset ≤0.10 | #6 | DESIGN_SPEC §5 REQ-02 | gate row | — |
| X-13 | Insert holes under OD-C03 pump cradle | four Ø4.0 at (x −4.0, z −239.0), (−4.0, −171.0), (37.0, −239.0), (37.0, −171.0) | mm | Ø4.00 at the four points above | ±0.05, offset ≤0.10 | #6 | DESIGN_SPEC §5 REQ-03 | gate row | — |
| X-14 | Insert holes on the OD-C02 bulkhead line | four Ø4.0 at (x 65.0, z −45.0/−105.0/−165.0/−225.0) | mm | Ø4.00 at the four points above | ±0.05, offset ≤0.10 | #6 | DESIGN_SPEC §5 REQ-04 | gate row | — |
| X-15 | Insert holes under the OD-C07 valve/flowmeter mount | four Ø4.0 at (x −113.0/−71.0, z −42.0/−148.5) | mm | Ø4.00 at the four points above | ±0.05, offset ≤0.10 | #6 | DESIGN_SPEC §5 REQ-10 | gate row | — |
| X-16 | Insert hole spec, all twenty insert holes (underside feature) | Ø4.0 ± 0.05, depth ≥ 5.7 through the 6.0 plate, for M3×5.7×Ø4.6 heat-set inserts (OD-F01) driven from the top | mm | Ø4.00 ± 0.05, depth ≥ 5.70 | — | #6 | DESIGN_SPEC §5 D-05b; §6 A-11 | gate row / assumption row | — |
| X-17 | Drain holes — diameter, positions, tolerance | two Ø8.0 through-holes at (x −80.0, z −120.0) and (x −80.0, z −230.0) | mm | Ø8.00 at (−80.0, −120.0/−230.0) | ±0.1, offset ≤0.10 | #6 | DESIGN_SPEC §5 REQ-06; §6 A-13 | gate row / assumption row | — |
| X-18 | OD-C01 plate mass | 737 | g | 737 | — | #7 | RV01 §4 P5 ("240 x 405 x 6 PETG base 737 g") | reviewer plausibility note | — |
| X-19 | OD-C01 plate centre of mass | (0.09, −102.4) | mm (x, z, machine frame) | (0.09, −102.4) | — | #7 | RV01 §4 P1 | reviewer plausibility note | — |
| X-20 | OD-C01 material | PETG, density 1270 | kg/m³ | — | — | #6 | DESIGN_SPEC §3; §6 A-10 (OPEN) | table / assumption row | unconfirmed (A-10 OPEN; BOM lists ASA as an alternative, see X-48) |
| X-21 | OD-C01 printer | Anycubic Kobra Max 3 | — | — | — | #6 | DESIGN_SPEC §3 | table | — |
| X-22 | OD-C01 print orientation | flat, bottom face on the bed, no supports, brim against warp | — | — | — | #6 | DESIGN_SPEC §4 C1; §6 A-14 (OPEN) | text / assumption row | unconfirmed; retired by first print |
| X-23 | Assumption A-12 (feet), verbatim | "four printed TPU feet OD-C15 (or the OEM pads OD-C25/C26 under a printed cup) screwed from below through Ø3.4 holes at (±110, +90) and (±110, −295) into inserts of the feet themselves" | — | — | — | #6 | DESIGN_SPEC §6 A-12 | quote | OPEN; retire by: "the Usta picks the feet" |
| X-24 | Assumption A-16 (footprint and height, names "feet"), verbatim | "240 × 405 plate; machine height ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet; the thesis' 0.4 m³ figure (INTAKE X-53) is read as an upper bound the machine is far below" | — | — | — | #6 | DESIGN_SPEC §6 A-16 | quote | OPEN; foot height not in the figure "plus feet" |
| X-25 | Gate REQ-09, flatness in service (Soft) | "The printed plate stays flat enough for the three mounts to seat without rocking after printing and in use (PETG warp on a 405 mm plate); not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, and it is answered by the first print" | — | — | — | #6, #7 | DESIGN_SPEC §5 REQ-09; RV01 §2 REQ-09 (INCONCLUSIVE, bench gate, F1) | gate row / reviewer verdict | not measurable in CAD; bears on feet seating |
| X-26 | Finding F1 (flatness/warp risk at the corners, where the feet sit) | "an unribbed 240 x 405 x 6 PETG plate printed flat can lift at the corners and creep under a 1 kg tank; the three mounts seat on its top face, so warp shows as rocking; only a print can tell" | — | — | — | #7 | RV01 §6 F1, at "whole plate, corners (±120, −6, 100 / −305)" | reviewer finding | risk MEDIUM; non-blocking; bears on feet because the feet sit at the corners (X-06) |
| X-27 | Finding F1 fix direction | "first print with brim, measure flatness under the mounts and at the feet; if it rocks, C2 ribs or a two-piece C3" | — | — | — | #7 | RV01 §6 F1 | reviewer finding | — |
| X-28 | Plausibility P1 (gravity), feet vs. centre of mass | "Plate lies flat, bottom on the counter via four feet at (+-110, 90 / -295) enclosing the plate COM (0.09, -102.4) and every placed part; each mount stands on y 0 with 0 mm3 overlap." | — | — | — | #7 | RV01 §4 P1 | reviewer plausibility note | YES per reviewer, but rests on OPEN assumptions A-01…A-03 placing the mounts |
| X-29 | Assumption A-11 (heat-set insert hardware, bears on screw length for the feet) | "M3 × 5.7 × Ø4.6 heat-set inserts in Ø4.0 through-holes of the 6.0 plate, driven from the top (OD-G01 A-17's figure); the screw tips may reach 0.3 below the plate" | — | — | — | #6 | DESIGN_SPEC §6 A-11 | quote | OPEN; retire by: "the Usta's stocked insert datasheet" |

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-30 | OD-C15 part definition: PRINT, parent OD-C00, qty 4, material TPU, source "printed", status "proposed" | `OD-C15,OD-C00,PRINT,Foot (alternative to OD-C25/526),,,4,DESIGN,TPU,printed,print,,proposed` | #2 | bom_rows.csv, row 3 |
| X-31 | OEM alternative OD-C25: rubber foot pad, ref 34, OEM code 5313229381, qty 2, not scanned/measured | `OD-C25,OD-C00,OEM,Rubber foot pad,34,5313229381,2,CALIPER,rubber,FixPart,4 (set),,todo` | #2 | bom_rows.csv, row 4 |
| X-32 | OEM alternative OD-C26: rubber foot pad, ref 76, OEM code 5313274719, qty 2, not scanned/measured | `OD-C26,OD-C00,OEM,Rubber foot pad,76,5313274719,2,CALIPER,rubber,FixPart,(set),,todo` | #2 | bom_rows.csv, row 5 |
| X-33 | The BOM's own name field for OD-C15 reads "OD-C25/526", not "OD-C25/C26" | "Foot (alternative to OD-C25/526)" | #2 | bom_rows.csv, row 3 (name field, verbatim) |
| X-34 | Order-of-work: OD-C15 feet (TPU), designed against OD-C01 and the OD-E06 cord; blocked by nothing | row 13: "`OD-C14` cable grommets, `OD-C15` feet (TPU) \| OD-C01, OD-E06 cord \| —" | #3 | CHASSIS_README.md, order-of-work table, row 13 |
| X-35 | Deliverable form for every printed part | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #3 | CHASSIS_README.md, Goal |
| X-36 | Assembly placement | "the top assembly `OD-000` as a STEP that places every printed part and every OEM part of the `step/` library by joints" | #3 | CHASSIS_README.md, Goal |
| X-37 | Definition of "validated" | "`validated` needs a print and a fit check by the Usta" | #3 | CHASSIS_README.md, Goal |
| X-38 | Anti-vibration requirement (TPU feet named directly) | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #5 | SOURCING_GUIDE_s6.md, §6 rule 2 |
| X-39 | Foot alternatives named | "Rubber feet 34/76 or printed TPU feet" | #4 | SOURCING_GUIDE_s3_10.md, §3.10 |
| X-40 | Fastener guidance (general) | "M3 heat-set inserts + M3 screws (the thesis tapped printed holes; inserts are better)" | #4 | SOURCING_GUIDE_s3_10.md, §3.10 |
| X-41 | Project fastener standard | "Fasteners are the project standard: M3 heat-set inserts (OD-F01), M3 screws ISO 7380 / DIN 912 A2 (OD-F02 M3×8, OD-F10 M3×12)." | #1 | REQUEST.md, "Project rules that bind this part" |
| X-42 | BOM row OD-F01: M3 heat-set insert | `OD-F01,OD-000,STD,M3 heat-set insert (Ø4.0 bore × 6; 26 in the chassis),,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo` | #2 | bom_rows.csv, row 6 |
| X-43 | BOM row OD-F02: M3×8 screw | `OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo` | #2 | bom_rows.csv, row 7 |
| X-44 | BOM row OD-F10: M3×12 screw (not named for the feet; recorded for fastener family completeness) | `OD-F10,OD-000,STD,M3×12 screw (OD-C01 into the OD-C02 base rail; tip ends on the bore floor),,,4,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo` | #2 | bom_rows.csv, row 8 |
| X-45 | Printers named for the project; no build volume or TPU capability stated | "Machines: Creality K1C and Anycubic Kobra Max 3, 0.4 mm nozzles; the machine files record PLA only and no build volume." | #1 | REQUEST.md, "Project rules that bind this part" |
| X-46 | Machine profile, Creality K1C | "Creality K1C (enclosed: ASA, PC)" | #3 | CHASSIS_README.md, "Order of work" footer |
| X-47 | Machine profile, Anycubic Kobra Max 3 | "Anycubic Kobra Max 3 (large panels: PETG)" | #3 | CHASSIS_README.md, "Order of work" footer |
| X-48 | BOM row OD-C01 (the part the feet screw into; material still open) | `OD-C01,OD-C00,PRINT,Base frame / floor plate,,,1,DESIGN,PETG (spec) or ASA — Usta to confirm (A-10),printed (Anycubic Kobra Max 3),print,,modeled` | #2 | bom_rows.csv, row 2 |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-06, X-23 | The foot height is not given by any input: what overall height (and base-to-screw-boss thickness) should the TPU foot be? |
| 2 | X-06, X-23 | The foot's outer diameter or footprint is not given: what diameter/footprint should it have, and must it clear the plate's R10 corners (web 8.3 mm, X-10) and the feet-hole position at (±110, +90 / −295)? |
| 3 | X-23, X-29 | A-12 (OPEN) says the feet are "screwed from below through Ø3.4 holes … into inserts of the feet themselves," but this is an unconfirmed assumption, not the Usta's pick: does the Usta confirm this fixing method and direction (screw from below, insert in the foot), or pick a different one? |
| 4 | X-07, X-29, X-41, X-43, X-44 | No input gives a screw length for the feet: given the plate is 6.0 mm thick (X-01/X-04) and the insert sits in the foot itself (X-23), should OD-F02 (M3×8) or another length be used, and how much thread should engage the foot's own insert? |
| 5 | X-20, X-30, X-38, X-39 | No input states a TPU grade (Shore hardness, brand, or filament name): which TPU should the foot use? |
| 6 | X-21, X-30, X-45, X-46, X-47 | Neither machine profile given (Creality K1C, Anycubic Kobra Max 3) states TPU capability (e.g. a direct-drive extruder), and the machine files record PLA only with no build volume: which printer prints the TPU feet? |
| 7 | X-06, X-11 … X-17 | What sits on the plate's top face directly above each feet hole — i.e. is the zone above (±110, +90) and (±110, −295) clear, or does it fall inside a reserved zone (tray x ±75 z −15…+85, tank x ±70 z −305…−250, valve mount x −117…−67 z −154…−35, electronics bay x 70…120 z −240…−30) or under an insert boss? No input states this. |
| 8 | X-18, X-19 | No input gives the assembled machine's total mass (only component figures: OD-C01 plate 737 g (X-18), pump ≈0.5 kg, thermoblock ≈0.45 kg, tank ≈1 kg full, per OD-C01 DESIGN_SPEC §3): what total mass should the four feet be sized to carry? |
| 9 | X-33 | bom_rows.csv itself names the OD-C15 alternative as "OD-C25/526", not "OD-C25/C26"; REQUEST.md glosses this as "the '526' is read as OD-C26" without the Usta's confirmation: does "526" mean OD-C26 (ref 76, 5313274719), or something else? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None. `OD-C01_base_frame.step` (#8) was listed and hashed only, per the brief and intake rule 6 (STEP geometry is measured later by `tools/measure`), not because it could not be read.
