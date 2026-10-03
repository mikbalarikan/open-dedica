# INTAKE v01 — 20261002-od-c14-cord-grommet

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
| 1 | 00_Spec/inputs/REQUEST.md | 6ebbd56bc9929e5e3c92fdb409e0b2971fb2b1fa603d309ed58eff95a1c12e04 | 1174 | Markdown | 1 page | full text |
| 2 | 00_Spec/inputs/bom_rows.csv | e30b9e2d6cfa76fdddc81c823a7022ae18eefea50de7cc808a60936c756e8633 | 1225 | CSV | 11 rows (incl. header) | full text |
| 3 | 00_Spec/inputs/CHASSIS_README.md | ac5e9383209553c87b271dfc55c0776d75dfc25899dbf176afdd5668a2603443 | 8917 | Markdown | 1 page | full text |
| 4 | 00_Spec/inputs/SOURCING_GUIDE_s6.md | 7c5705ead4480fa954c9646e6f78f6241a55a78f85dfb0bee439f0bc5844bb21 | 1541 | Markdown | 1 page (§6 excerpt) | full text |
| 5 | 00_Spec/inputs/OD-C11_DESIGN_SPEC.md | 6da33456e123942bb92e7419ff190f6e01522b0580d36d510fa9c5eee6d61245 | 22734 | Markdown | 1 page (§1-§8) | full text |
| 6 | 00_Spec/inputs/OD-C11_back_panel.step | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | 236640 | STEP | n/a | listed and hashed only (intake rule 6); geometry measured later by `tools/measure` |
| 7 | 00_Spec/inputs/OD-C01_base_frame.step | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | 134325 | STEP | n/a | listed and hashed only (intake rule 6); geometry measured later by `tools/measure` |
| 8 | 00_Spec/inputs/OD-C08_electronics_bay_tray.step | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 | 171518 | STEP | n/a | listed and hashed only (intake rule 6); geometry measured later by `tools/measure` |

## §2 Dimensions

Frame: the OD-C01 machine frame throughout (OD-C11 spec §2, CHASSIS_README.md
"Frames for OD-000"): X to the user's right, +Y up, +Z toward the user (front),
the plate's top face y = 0. All values below are as given in the named source;
none is confirmed (rule 3); none in this batch is a photo or a scaled drawing
read.

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | OD-C01 plate extents | x ±120, y −6 … 0, z −305 … +100 | mm | x ±120, y −6 … 0, z −305 … +100 | — | #5 | §2 (citing OD-C01 spec 1.2 §4) | table | — |
| X-02 | OD-C01 plate corner radius | R 10 about (±110, −295) | mm | R 10 about (±110, −295) | — | #5 | §2 | table | — |
| X-03 | OD-C01 plate feet holes | Ø3.4 at (±110, −295) | mm | Ø3.4 at (±110, −295) | — | #5 | §2 | table | — |
| X-04 | OD-C11 panel outer face | z = −302.0 | mm | z = −302.0 | — | #5 | §2 | table | — |
| X-05 | OD-C11 panel inner face | z = −299.0 | mm | z = −299.0 | — | #5 | §2 | table | — |
| X-06 | OD-C11 wall thickness and z-span | 3.0 thick, z −302.0 … −299.0 | mm | 3.0; z −302.0 … −299.0 | — | #5 | §4 C1 | table | — |
| X-07 | OD-C11 wall x/y extents | x −116.0 … +116.0, y 0 up to 215.0 | mm | x −116.0 … +116.0, y 0 … 215.0 | — | #5 | §4 C1 | table | — |
| X-08 | Wall-foot-to-plate-edge clearance | at \|x\| = 116 the plate's corner arc lies at z −303.0; wall foot stands with ≥ 1.0 of plate behind it | mm | ≥ 1.0 | — | #5 | §4 C1 (A-02) | table | — |
| X-09 | Cord pass-through | one Ø12.0 hole through the wall along Z at (x 95.0, y 30.0), for mains cord OD-E06 in the grommet OD-C14 | mm | Ø12.0 at (x 95.0, y 30.0) | ±0.1 (REQ-03), offset ≤ 0.10 | #5 | §4 C1; §5 REQ-03 | table | — |
| X-10 | Tube pass-throughs (neighbouring, wet side) | two Ø12.0 holes through the wall along Z at (x −100.0, y 30.0) and (x −84.0, y 30.0) | mm | Ø12.0 at (x −100.0, y 30.0) and (x −84.0, y 30.0) | ±0.1 (REQ-04), offset ≤ 0.10 | #5 | §4 C1; §5 REQ-04 | table | — |
| X-11 | Tank seat hose nipples (cross-job reference) | the tank seat's hose nipples are Ø6.9 over the lip | mm | Ø6.9 | — | #5 | §4 C1 (cites "INTAKE X-25", a different job's intake, not in this workspace) | table | source not in this job's inputs |
| X-12 | Floor flange thickness and y/z span | 4.0 thick, y 0 … 4.0, z −299.0 … −277.0 (22 deep) | mm | 4.0; y 0 … 4.0; z −299.0 … −277.0 | — | #5 | §4 C1 | table | — |
| X-13 | Floor flange x extents | at x −104.0 … −72.0 and +72.0 … +104.0 | mm | x −104.0 … −72.0 and +72.0 … +104.0 | — | #5 | §4 C1 | table | — |
| X-14 | Floor flange screw holes | two Ø3.4 through-holes along Y per flange at (x ±81.0, z −282.0) and (x ±95.0, z −282.0) | mm | Ø3.4 at (x ±81.0, z −282.0) and (x ±95.0, z −282.0) | ±0.1 (REQ-01), offset ≤ 0.10 | #5 | §4 C1; §5 REQ-01 | table | — |
| X-15 | Flange screw axis offset from ledge | each screw axis lies 5.0 in front of the top ledge (z −287) | mm | 5.0; z −287 | — | #5 | §4 C1 | table | — |
| X-16 | Screw head clearance from gussets | screw heads Ø5.7 keep ≥ 2.1 from the gussets | mm | Ø5.7 head; ≥ 2.1 clearance | — | #5 | §4 C1 | table | — |
| X-17 | Gusset thickness and x positions | two gussets per flange, 4.0 thick, at its ends (x ±72.0 … ±76.0 and x ±100.0 … ±104.0) | mm | 4.0 thick; x ±72.0…±76.0 and x ±100.0…±104.0 | — | #5 | §4 C1 | table | — |
| X-18 | Gusset geometry (current, spec 1.2) | right triangles in the YZ plane: 16.0 leg along the flange's top; leg up the wall 30.0 for the inner gussets (top y 34), 18.0 for the outer gussets (top y 22, 2.0 below the pass-throughs at y 24) | mm | 16.0; inner leg 30.0 (top y 34); outer leg 18.0 (top y 22) | — | #5 | §4 C1 | table | — |
| X-19 | Gusset geometry (superseded, spec 1.1) | the 30.0 outer leg (spec 1.1) blocked the tube hole at (−100, 30) and the cord hole at (95, 30) (v02 REPORT); 1.2 shortens the outer leg to 18.0 | mm | 30.0 (superseded by X-18's 18.0) | — | #5 | §4 C1; §8 change log 1.2 | table | historical, superseded by X-18 |
| X-20 | Top ledge thickness and span | 4.0 thick, y 211.0 … 215.0, z −299.0 … −287.0 (12 deep), along x −114.0 … +114.0 | mm | 4.0; y 211.0…215.0; z −299.0…−287.0; x −114.0…+114.0 | — | #5 | §4 C1 | table | — |
| X-21 | Insert bosses (top ledge) | blocks at x ±(84.0 … 96.0), y 203.0 … 211.0, z −299.0 … −287.0 | mm | x ±(84.0…96.0); y 203.0…211.0; z −299.0…−287.0 | — | #5 | §4 C1 | table | — |
| X-22 | Insert bore (top ledge, for OD-C10) | Ø4.0 × 6.0 blind bore along −Y from y 215.0 at (x ±90.0, z −293.0) | mm | Ø4.0 × 6.0 at (x ±90.0, z −293.0) | ±0.05 dia, ±0.1 depth (REQ-07), offset ≤ 0.10 | #5 | §4 C1; §5 REQ-07 | table | — |
| X-23 | Vent slots | five slots through the wall along Z, 4.0 wide (X) × 80.0 tall (Y), centres x 78.0, 86.0, 94.0, 102.0, 110.0, from y 100.0 to 180.0, ends round R 2.0 | mm | 4.0 × 80.0; centres x 78/86/94/102/110; y 100…180; R 2.0 | ±0.1 (REQ-06) | #5 | §4 C1; §5 REQ-06 | table | — |
| X-24 | Keep-out behind the panel | nothing of the panel lies at z > −277.0; pump cradle's foot ends at z −245; bulkhead ends at z −240 | mm | z > −277.0 excluded; foot z −245; bulkhead z −240 | — | #5 | §4 C1 (REQ-05) | table | — |
| X-25 | Print orientation (OD-C11, context) | lying on the outer face z = −302 on the bed, build direction +Z | mm/deg | z = −302; build +Z | — | #5 | §4 C1 (A-08) | table | — |
| X-26 | OD-C11 envelope | 232.0 × 215.0 × 25.0 (x ±116, y 0 … 215, z −302 … −277) | mm | 232.0 × 215.0 × 25.0 | ±0.1 (U-02) | #5 | §4 C1; §5 U-02 | table | — |
| X-27 | Minimum wall thresholds around the cord hole's neighbourhood | wall 3.0, flanges and ledge 4.0, webs between vent slots 4.0, webs between the tube holes 4.0; structural floor `min_wall` ≥ 2.0 | mm | 3.0 / 4.0 / 4.0 / 4.0; floor ≥ 2.0 | — | #5 | §5 D-01b | table | — |
| X-28 | OD-C02 bulkhead position (neighbour) | identity; rear end z −240, x 59 … 71, y 0 … 215 | mm | z −240; x 59…71; y 0…215 | — | #5 | §2 | table | — |
| X-29 | OD-C03 + OD-H01 placement (neighbour) | rotation local x → +Z, y → −Y, z → +X at (0, 40, −205); cradle's foot reaches z −245 | mm/deg | origin (0, 40, −205); foot z −245 | — | #5 | §2 | table | — |
| X-30 | Fasteners (project standard) | M3 heat-set inserts (OD-F01, Ø4.0 bore × 5.7 long) and M3×8 screws (OD-F02, ISO 7380 head Ø5.7) | mm | Ø4.0 × 5.7; M3×8, head Ø5.7 | — | #5 | §2 | table | — |
| X-31 | Coordinate frame (restated) | the OD-C01 machine frame: X to the user's right, +Y up, +Z toward the user (front), the plate's top face y = 0 | — | — | — | #5, #3 | OD-C11 spec §2; CHASSIS_README.md "Frames for OD-000" | table | — |
| X-32 | A-03 assumption: cord and grommet | the cord OD-E06 (≈ Ø7, not measured [as of this spec's writing]) passes a Ø12 hole at (95, 30) in a TPU grommet OD-C14 (not designed) that clamps it; an IEC inlet OD-E60 would need its own cut-out (a later revision) | mm | ≈Ø7 (cord, as stated in OD-C11 spec); Ø12 hole at (95, 30) | — | #5 | §6 A-03 | table | fit-critical; not confirmed |
| X-33 | E-11 gate requirement | "the cord's strain relief is the grommet OD-C14 in the Ø12 cord hole (not designed: A-03); the five vent slots open the electronics bay's rear" | — | — | — | #5 | §5 E-11 | table | — |
| X-34 | A-06 assumption: venting | five slots 4 × 80 behind the electronics bay (x 76 … 112, y 100 … 180) let the board's heat out; no vent on the wet side | mm | 4 × 80; x 76…112; y 100…180 | — | #5 | §6 A-06 | table | — |
| X-35 | A-07 assumption: rear neighbours | the pump cradle's foot ends at z −245 and the bulkhead at z −240; the pump body's rear-most z is not stated; the tank zone x ±70, z −305 … −250 stays free above the floor flanges (the flanges stop at \|x\| 72) | mm | foot z −245; bulkhead z −240; tank zone x ±70, z −305…−250 | — | #5 | §6 A-07 | table | — |
| X-36 | Mains cord diameter, Usta's caliper reading | "4/ 7mm" (answer to "A caliper reading of the power cord's diameter for the C14 grommets") | mm | 7 | — | #1 | REQUEST.md, Usta's message quote, line 4 and line 14 | message | not confirmed per rule 3 despite being the Usta's own reading (confirmation is a separate ledger step) |
| X-37 | bom_rows.csv: OD-C14 row | parent OD-C00, type PRINT, name "Cable strain relief / grommet", qty 2, cad DESIGN, material_spec TPU, source printed, status proposed | — | qty 2; material TPU | — | #2 | row 5 | table | conflicts with §3 X-44 (Usta: "all printed in pla for now") |
| X-38 | bom_rows.csv: OD-E06 row | OEM, "Power supply cord with plug (region-specific; AU code shown)", ref 53, oem_code 5013276449, qty 1, source FixPart / generic, price 8 EUR, status todo | — | qty 1; price 8 EUR | — | #2 | row 2 | table | — |
| X-39 | bom_rows.csv: OD-F09 cable tie row | "Cable tie 4.8 mm (OD-C03 pump strap; OD-C08 loom slots 2 × 4)", qty 4, material PA66 UV-black, source hardware store, price 1 EUR, issue #1, status todo | mm | 4.8 | — | #2 | row 11 | table | not stated as used by OD-C14 |
| X-40 | bom_rows.csv: OD-F01 insert row | "M3 heat-set insert (Ø4.0 bore × 6; 38 in the chassis)", qty ~50, material brass M3, source AliExpress, price 10 EUR (set), status todo | mm | Ø4.0 × 6 | — | #2 | row 8 | table | — |
| X-41 | bom_rows.csv: OD-F02 screw row | "M3×8 screw", qty ~50, material_spec ISO 7380 / DIN 912 A2, source AliExpress, status todo | mm | M3×8 | — | #2 | row 9 | table | — |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-42 | Deliverables for this job | "Parametric build script, STEP (mm, one named solid), STL and 3MF, and one independent review." | #1 | REQUEST.md, "What the job delivers" |
| X-43 | BOM quantity | "OD-C14 ... BOM qty 2." | #1 | REQUEST.md, "What the job delivers" |
| X-44 | Material (overrides BOM) | "all printed in pla for now" | #1 | REQUEST.md, Usta's message, line 12 |
| X-45 | OD-C11 is delivered and unchanged | "OD-C11 is delivered (merged); it is not changed by this job." | #1 | REQUEST.md, "Constraints stated by the project" |
| X-46 | Shared files out of scope | "The shared files (docs/bom.csv, chassis/README.md, OD-000) belong to another thread: this job hands its changes over in integration notes." | #1 | REQUEST.md, "Constraints stated by the project" |
| X-47 | Usta's verbatim ruling (four questions) | "1/ merge\n2/ accept\n3/ printed\n4/ 7mm\n\nall printed in pla for now" | #1 | REQUEST.md, "The Usta's message", lines 7-12 |
| X-48 | Chassis-wide deliverable requirement | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #3 | CHASSIS_README.md, "Goal" |
| X-49 | OD-C14 order-of-work entry | "`OD-C14` cable grommets, `OD-C15` feet (TPU) | OD-C01, OD-E06 cord | ... `OD-C15` modeled, RV01 approved on assumptions (TPU 95A, K1C): Ø18 × 10 puck, M3×12 from the top into a captive M3 nut; `OD-C14` open" | #3 | CHASSIS_README.md, order-of-work table row 13 |
| X-50 | Two-zone layout (design rule 1) | "Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #4 | SOURCING_GUIDE_s6.md, rule 1 |
| X-51 | Anti-vibration (design rule 2) | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #4 | SOURCING_GUIDE_s6.md, rule 2 |
| X-52 | Thermal map / material rule (design rule 3) | "Respect the thermal map. Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #4 | SOURCING_GUIDE_s6.md, rule 3 |
| X-53 | Serviceability (design rule 4) | "Serviceability is the point. ... top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #4 | SOURCING_GUIDE_s6.md, rule 4 |
| X-54 | Safety spec (design rule 7) | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #4 | SOURCING_GUIDE_s6.md, rule 7 |
| X-55 | OD-C11 intent: cord passes through grommet | "It passes the mains cord (through a grommet, OD-C14) on the electric side" | #5 | OD-C11_DESIGN_SPEC.md §1 |
| X-56 | OD-C11 out of scope: grommet not designed there | "Out of scope: ... the grommet OD-C14, the feet OD-C15, the tube and cord runs, calipers, drawings, renders." | #5 | OD-C11_DESIGN_SPEC.md §1 |
| X-57 | OD-C11 environment/load on the grommet | "mains cord on the right ... Loads: the top panel's two rear screws, a hand pulling the panel off, the cord's pull (taken by the grommet)." | #5 | OD-C11_DESIGN_SPEC.md §3 |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-37, X-44, X-52 | bom_rows.csv gives OD-C14's material as TPU; the Usta's message says "all printed in pla for now"; SOURCING_GUIDE_s6.md rule 3 says "PLA nowhere structural." Which governs for OD-C14, and is a cord-clamping grommet "structural" under that rule? |
| 2 | X-09, X-32 | How is the grommet retained in the closed Ø12.0 round hole at (95, 30)? No input shows a flange, lip, slot, snap feature, or any other retention geometry on the wall or the grommet. |
| 3 | X-32, X-33 | How does the grommet grip the cord (its strain-relief function, per E-11)? No input states a clamping method, a split line, a compression fit, or a cable-tie channel. |
| 4 | X-37, X-43 | bom_rows.csv and REQUEST.md both give OD-C14's BOM quantity as 2. Does this mean two identical grommets for the one cord pass-through (e.g., a split/two-piece grommet), one grommet plus a spare, or something else? |
| 5 | X-38, X-32 | OD-E06 is "Power supply cord with plug (region-specific; AU code shown)" — the cord already carries its moulded plug. How does a grommet go onto a cord whose plug end cannot pass through a smaller bore? No input states an installation sequence, a split grommet, or any other method. |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None. The three STEP files (OD-C11_back_panel.step, OD-C01_base_frame.step,
OD-C08_electronics_bay_tray.step) were not read as geometry: per intake rule 6
they are listed and hashed only (§1, rows 6-8); their geometry is measured later
by `tools/measure`. Every markdown and CSV file named in the brief was read in full.
