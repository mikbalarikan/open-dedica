# DESIGN_SPEC — OD-C10 printed top panel (20261001-od-c10-top-panel)

Version 1.2 · RATIFIED by the Usta on 2026-10-01 (standing instruction of 2026-09-30 and the "what can start now please initiate it" of 2026-10-01: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C10 is the 3D-printed removable top panel of the Open Dedica espresso machine
(BOM: removable with 4 screws; SOURCING_GUIDE §6 rule 4): a lid over the whole
machine that comes off to reach the group head housing's four screws and the
carrier's foot screws (OD-C05 A-14), the OPV on the valve mount (OD-C07 A-10)
and the hot water connection above the carrier (OD-C05 A-06, A-07). It covers
the OD-C01 footprint, leaves headroom over the carrier's plate for the hot water
tube's loop, and is held by four M3 screws driven from above: two into the
inserts the bulkhead OD-C02 provides in its top rail (OD-C02 REQ-07, A-05), two
into the inserts of the back panel OD-C11's top ledge (OD-C11 REQ-07). Done
means: one valid printable solid seated on those four bosses, clear of every
delivered part below it, and every unconfirmed value in §6. The side and front
panels, the water tank (on the table, the Usta 2026-10-01) and the tube runs are
not designed: their rows are assumptions and the job is reopened when they land.

**Deliverables** (tier M): STEP AP242 of the panel; the check assembly STEP
(panel + OD-C01 + OD-C02 + OD-C05 + OD-C07 + OD-C11 as placed); STL and 3MF;
build and check scripts; REPORT; sections. No drawings or renders.

**Out of scope:** the side panels OD-C12/C13 and corner brackets OD-C16, the
front panel OD-C09, the back panel OD-C11 (its own job, a reference solid here),
the tank dock OD-C06 (deferred by the Usta), the tube runs, calipers, drawings,
renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| OD-C01 base frame (delivered) | `00_Spec/inputs/OD-C01_base_frame.step`: plate x ±120, z −305 … +100, corners R 10 about (±110, −295) and (±110, +90), top face y 0 | — | OD-C01 spec 1.2 §4 | CONFIRMED as the input |
| OD-C02 bulkhead (delivered) | `00_Spec/inputs/OD-C02_bulkhead.step` (identity): top rail x 59.5 … 70.5, top face y 215.0, z −240 … −30; two Ø4.0 × 6.0 insert bores along −Y from y 215 at (65, −60) and (65, −210) for this panel | — | OD-C02 spec 1.2 §4, REQ-06, REQ-07, A-05 | CONFIRMED as the input; A-01 |
| OD-C05 carrier (delivered) | `00_Spec/inputs/OD-C05_group_head_carrier.step` placed by OD-C01 A-01 (local x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0)): plate top y 210.0 over x ±55, z −70 … +82; hub window R 30 about (0, 32); hatch x ±40, z −64 … −32; four counterbored housing-screw holes at (±44, −12) and (±44, 76) | — | OD-C05 spec 2.2 §4; OD-C01 spec 1.2 §4 A-01 | CONFIRMED as the input; A-03 |
| OD-C07 valve mount (delivered) | `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` placed by OD-C01 A-17 (local x → −Z, y → −X, z → +Y, origin (−92, 0, −60)): top of the mount y 48, the valve's drive tube top at mount z 61.7 | — | OD-C07 spec 1.2 §4, A-10; OD-C01 spec 1.2 §4 A-17 | CONFIRMED as the input |
| OD-C11 back panel (this round's sibling job) | its build v02 STEP (`OD-C11_back_panel_v02.step`, unreviewed: that build stopped on its gussets and feet-hole margin, its wall and ledge are as specified), else the spec's ledge; its wall z −302 … −299, x ±116, top y 215.0: top face y 215.0, z −299 … −287; two Ø4.0 × 6.0 insert bores along −Y from y 215 at (±90, −293) | — | OD-C11 spec 1.0 §4, REQ-07 | A-02 |
| Fasteners | M3 heat-set inserts (OD-F01) in the neighbours; M3 × 8 screws (OD-F02, ISO 7380, head Ø5.7) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard) |

**Coordinate frame:** the OD-C01 machine frame, every overlay the identity: X to
the user's right, +Y up, +Z toward the user (the front), the plate's top face
y = 0. The panel's top face is the plane y = 250.0. Every artifact uses this frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c10_top | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-09) | PETG (BOM: ASA; a 240 × 405 lid warps in ASA on the open Kobra; heat below, A-10) | 1270 | as printed | A-10 |

Environment: the top of the machine; under it the carrier's plate (y 210) over
the group head, the hot water tube's loop and the thermoblock further down; cups
and hands on top. Loads: its own weight, a hand pressing on it, a cup.

## §4 Architecture and concepts

- **C1 — a lid: top skin, perimeter skirt, four screw columns, two rest pads
  (CHOSEN).** One solid.
  - **Top skin** 3.0 thick, y 247.0 … 250.0, over the plate outline: x ±120.0,
    z −305.0 … +100.0, vertical corner edges R 10.0 (the plate's corners).
  - **Skirt** 3.0 thick along the whole perimeter, its outer face on the outline
    above, from the skin down to y 215.0 (32.0 tall below the skin): the lid's
    bottom edge meets the side, front and back panels at y 215 (A-04).
  - **Screw columns**, four, Ø12.0, from the skin's underside down to y 215.0:
    two at (x 65.0, z −60.0) and (x 65.0, z −210.0) over the bulkhead's top-rail
    inserts (their bottoms seat on the rail's top face, a designed contact), two
    at (x ±90.0, z −293.0) over the back panel's ledge inserts (seated on the
    ledge). Each has a Ø3.4 through-hole on its axis and a Ø6.5 counterbore from
    the top face y 250.0 down to y 218.0, so an M3 × 8 screw driven from above
    bears on 3.0 of column and reaches 5.0 into the 5.7 insert (A-05); the wall
    around the counterbore is 2.75. Each
    column is tied into the skin and, for the rear two, into the rear skirt by
    two ribs 3.0 thick (E-06).
  - **Rest pads**, two, Ø10.0, at (x ±48.0, z 30.0) over the carrier's plate,
    from the skin down to y 210.5: 0.5 above the carrier's top face, so a hand
    on the lid bears on the carrier after 0.5 of deflection (A-03); 33 from the
    housing screws' counterbores, 13 outside the hub window.
  - **Headroom**: the skin's underside at y 247.0 leaves 37.0 above the
    carrier's plate for the hot water tube's loop from the hatch to the hub
    window and the water connection above the hub (OD-C05 A-06, A-07; A-06 here).
  - Print orientation (A-08): **upside down**, the top face y 250 on the bed,
    build direction −Y (the machine's down): the skirt, columns, ribs and pads
    rise as vertical prisms; the counterbores open at the bed; each counterbore
    floor (the screw-head seat, facing +Y, down in the print) is a ring bridging
    Ø6.5 over Ø3.4, the named exception. Envelope 240.0 × 39.5 × 405.0 (x ±120,
    y 210.5 … 250.0, z −305 … +100); on the bed 240 × 405, 39.5 tall.
- **C2 — the lid in two halves joined over the bulkhead (for the K1C).**
  Deferred until A-09 is answered.
- **C3 — a flat 3 mm plate on the side panels' top rails.** Deferred: it needs
  the side panels and leaves no headroom for the tube loop under y 215.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 240.0 × 39.5 × 405.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±120.0, y 210.5 … 250.0, z −305.0 … +100.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) at the identity: the two bulkhead columns' bottoms on OD-C02's top-rail face and the two rear columns' bottoms on OD-C11's ledge are the designed contacts, `clearance = 0`, `interference ≤ 0` mm³; each column's Ø3.4 hole coaxial with the insert bore under it, offset ≤ 0.10 (`locate_bore` on both solids); panel to OD-C05 = 0.50 ± 0.05 (the pads) and nowhere less; panel to OD-C07 ≥ 3.0; panel to OD-C01 ≥ 3.0; panel to OD-C02 and OD-C11 away from the column bottoms ≥ 0.5, except the rear skirt's bottom inner edge (y 215, z −302), which meets the top outer edge of OD-C11's wall along x ±116 as a designed line contact, and the rear skirt's bottom face over its R 10 corner arcs at x ±110 … ±116, which rests on OD-C11's wall top (two patches, ≈ 5.9 mm² each): `clearance = 0`, `interference ≤ 0` (1.1: the skirt z −305 … −302 and the wall z −302 … −299 share that edge by §4's geometry; 1.2: the corner patches, v01 REPORT §10, accepted by the Usta). (b) the panel lowered along −Y from +40.0 above its seat to the seat in steps ≤ 2.0: `interference ≤ 0` with every reference solid at every step | Hard | CAD | house | `clearance`, `interference`, `locate_bore` | A-01, A-02, A-03 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 skin, 1 perimeter skirt, 4 columns each with a Ø3.4 through-hole and a Ø6.5 counterbore, 2 rest pads, the column ribs (E-06) | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh (written by the orchestrator, checked by the reviewer) | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default for enclosures; skin and skirt 3.0, the column wall around the counterbore 2.75) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the Kobra Max 3 build volume, upside down: 240.0 × 405.0 on the bed, 39.5 tall | Hard | part | machine | `envelope` | A-09 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (top face on the bed, build direction −Y): the skirt, columns, ribs and pads are vertical prisms, their ends face up; the four counterbore floors (the screw-head seats, normal +Y) are the named exception below, excluded by position, their area reported | Hard | part | floor | `overhang_census(build_dir=(0,-1,0))` | A-08 |
| D-03b | Unsupported bridge | span ≤ 5: nothing bridges but the four counterbore floors (Ø6.5 rings over Ø3.4, the named exception) | Hard | part | floor | reviewer, from sections | A-08 |
| D-04a | Clearance hole for a fastener | the four column holes Ø ≥ 3.25 (designed Ø3.4) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-05a | Heat-set insert boss | none on this part (the inserts sit in OD-C02 and OD-C11) | Hard | part | struct | — (N/A by this row) | — |
| D-05b | Heat-set insert hole | none on this part | Hard | part | floor | — (N/A by this row) | — |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the column holes are clearance holes | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | none on this part | Hard | part | struct | — (N/A by this row) | — |
| E-06 | Boss support | every column tied into the skin and by two ribs (the rear two also into the rear skirt); the pads tied into the skin | Hard | part | struct | reviewer, from sections | — |
| REQ-01 | Top skin | the top face one plane at y 250.00 ± 0.10 (`envelope` max_y) less the four counterbore mouths; skin 3.0 ± 0.1 thick (underside y 247.0) | Hard | CAD | A-06 | `envelope`; reviewer from sections | A-06 |
| REQ-02 | Outline and skirt | outline x ±120.0 ± 0.1, z −305.0 … +100.0 ± 0.1, vertical corner edges R 10.0 ± 0.1 about (±110, −295) and (±110, +90); skirt 3.0 ± 0.1 thick all round, its bottom face at y 215.00 ± 0.10 | Hard | CAD | A-04 | `envelope`, `radial_extent`; reviewer from sections | A-04 |
| REQ-03 | Bulkhead columns | two Ø12.0 ± 0.1 columns at (x 65.0, z −60.0) and (65.0, −210.0), offset ≤ 0.10; bottoms y 215.00 ± 0.05; Ø3.4 ± 0.1 through-holes, coaxial with OD-C02's insert bores (offset ≤ 0.10); Ø6.5 ± 0.1 counterbores from y 250.0 with floors at y 218.0 ± 0.1 | Hard | CAD | A-01, A-05 | `locate_bore` on both solids, `bore_census` | A-01, A-05 |
| REQ-04 | Back panel columns | two Ø12.0 ± 0.1 columns at (x ±90.0, z −293.0), offset ≤ 0.10; bottoms y 215.00 ± 0.05; Ø3.4 ± 0.1 through-holes coaxial with OD-C11's insert bores (offset ≤ 0.10); counterbores as REQ-03 | Hard | CAD | A-02, A-05 | `locate_bore` on both solids, `bore_census` | A-02, A-05 |
| REQ-05 | Rest pads | two Ø10.0 ± 0.1 pads at (x ±48.0, z 30.0), offset ≤ 0.10, bottoms y 210.50 ± 0.05; `clearance`(pad, OD-C05) 0.50 ± 0.05; each pad ≥ 10.0 from the hub window's edge (r ≥ 40 from (0, 32)) and ≥ 20.0 from the housing screws' counterbores | Hard | CAD | A-03 | `locate_bore`, `clearance` | A-03 |
| REQ-06 | Headroom | no panel material below y 247.0 inside the box x ±42, z −70 … +70 over the carrier's hatch and hub window (the pads lie at |x| 43 … 53) | Hard | CAD | A-06 | `interference` with that box = 0 | A-06 |
| REQ-07 | Screws from above | each of the four screw axes clear from y 250 down to its counterbore floor: Ø6.5 open over the whole depth (a driver Ø ≤ 6 reaches the head) | Hard | CAD | client (X-41, X-43) | `locate_bore`; reviewer from sections | — |
| REQ-08 | Stiffness | **Soft.** The lid does not sag visibly or rattle on its four columns with the side panels absent (the edges away from the bulkhead and back panel free, A-04); a hand on the lid bears on the pads; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print | Soft | part | client | — (bench) | A-04, A-11 |

**Named exceptions** (Usta U-18): D-03a and D-03b for the four counterbore floors (Ø6.5 rings over Ø3.4, bridging ≤ 6.5 in the upside-down print), as on OD-C05 (its §5 named exception); recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-C02 interface | the delivered bulkhead (identity): top rail x 59.5 … 70.5, top face y 215.0, z −240 … −30; two Ø4.0 × 6.0 insert bores along −Y from y 215 at (65, −60) and (65, −210) | the columns miss the inserts or rock | INTAKE X-06 … X-12, X-42, X-62, X-63 (OD-C02 spec 1.2 REQ-06, REQ-07, A-05) | OD-C02's print, calipers | OPEN |
| A-02 | OD-C11 interface (the other two screws, INTAKE §4 gap 9) | the back panel (sibling job, spec 1.0): a ledge with its top face at y 215.0 over z −299 … −287 and two Ø4.0 × 6.0 insert bores along −Y from y 215 at (±90, −293); checked against its build v02 STEP (OD-C11 spec 1.1; spec 1.2 changes only its outer gussets and a footprint margin, neither near the lid) | OD-C11 changes and the columns move | OD-C11 spec 1.0 §4, REQ-07 (this round's design choice) | OD-C11 review; its print | OPEN |
| A-03 | OD-C05 carrier as placed | the delivered carrier at the OD-C01 joint (x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0)): plate top y 210.0 over x ±55, z −70 … +82; housing screws' counterbores at (±44, −12) and (±44, 76); hub window R 30 about (0, 32); hatch x ±40, z −64 … −32; the pads 0.5 above the plate | the pads touch and the lid rocks, or land on a screw | INTAKE X-14 … X-20, X-33 | OD-C05's print, calipers on its height | OPEN |
| A-04 | Edges and the other panels (INTAKE §4 gaps 2, 3) | the lid is held at four columns along x 65 and z −293; its skirt's bottom edge at y 215 meets the side panels OD-C12/C13 (outer faces x ±120) and the front panel OD-C09 (outer face z +100), which are not designed and must reach y 215 under the skirt; until they exist the left and front edges are free | the lid sags or rattles at the free edges; the other panels need another joint | this spec (design choice) | OD-C09, OD-C12, OD-C13 designs | OPEN |
| A-05 | Screws | M3 × 8 ISO 7380 (head Ø5.7) from above, 3.0 of column under the head, 5.0 into the 5.7 insert | the screw bottoms out or bites too little | INTAKE X-58; this spec | the Usta's stocked screws | OPEN |
| A-06 | Headroom over the carrier (INTAKE §4 gaps 1, 8) | the hot water tube's loop from the hatch to the hub window and the water connection above the hub (OD-C05 A-06, A-07; Ø8 silicone, not scanned) stay below y 247: 37 above the carrier's plate; the machine top is y 250 | the tube kinks or the lid presses on it | this spec; INTAKE X-21, X-44 | the tube run (OD-W00), the first assembly | OPEN |
| A-07 | Water tank (INTAKE §4 gap 4) | the tank stands on the table (the Usta, 2026-10-01); the lid covers the whole footprint including the reserved tank zone x ±70, z −305 … −250; the tank dock job OD-C06 reopens this panel if the tank moves inside | a later tank inside needs an opening in the lid | INTAKE X-28, X-46 | OD-C06 | OPEN |
| A-08 | Print orientation | upside down, the top face on the bed, build direction −Y, no supports; brim against warp | the large skin warps; the counterbore rings sag | this spec | first print | OPEN |
| A-09 | Kobra Max 3 build volume (INTAKE §4 gaps 6, 7) | 420 × 420 × 500 (Anycubic specification, not in the machine file); the lid is 240 × 405 on the bed, in one piece | does not fit: C2 (two halves) | INTAKE X-30 (as OD-C01 A-09) | the Usta reads the printer | OPEN |
| A-10 | Material (INTAKE §4 gap 5) | PETG, 1270 kg/m³, on the Kobra Max 3 (the BOM says ASA; an open-frame printer warps ASA at 240 × 405); the lid's lowest point is 37 above the carrier's plate and far from the thermoblock (x ≤ 50, y ≤ ≈ 130) | the lid softens over the group head (PETG HDT ≈ 70 °C) | INTAKE X-40, X-51, X-55 | the Usta names the filament; a temperature reading under the lid | OPEN |
| A-11 | Stiffness | a 3 mm PETG skin 240 × 405 with a 32 tall skirt on four columns and two pads: no calculation | the lid sags or drums | this spec | first print (REQ-08) | OPEN |
| A-12 | Machine height (INTAKE §4 gap 8) | the top face at y 250 above the plate's top: the machine 256 tall from the plate's underside plus the feet, within OD-C01 A-16's ≈ 260 | the machine is taller than the Usta wants | INTAKE X-05, X-64, X-65 | the Usta's layout confirmation | OPEN |
| A-13 | OD-C07 under the lid | the valve mount at the OD-C01 joint (x → −Z, y → −X, z → +Y, origin (−92, 0, −60)), its top at y 48 and the valve's drive tube at y ≈ 62: far below the lid; the OPV is adjusted with the lid off | none for the lid | INTAKE X-23 … X-26 | — | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-01 | job opened at PUBLIC on the Usta's "what can start now please initiate it"; C1 proposed | Oğuz | job_start |
| 2026-10-01 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and the request of 2026-10-01; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-10-01 | INTAKE §4 gaps 1 … 9 are answered by §4 as design choices, all A-## rows: the lid's height (A-06, A-12), its edges (A-04), the tank (A-07), material and printer (A-09, A-10), the other two screws into OD-C11's ledge (A-02) | Oğuz | INTAKE_v01 §4 |
| 2026-10-01 | INTAKE §4 gap 10 (OD-C01 §2's "axis the line (x 0, y 175) along Z") is that spec's text from before the group head stood vertical (OD-C01 spec 1.2 §4 A-01 governs: axis vertical at (x 0, z 32), mouth at y 176.76); no effect on this panel | Oğuz | OD-C01 spec 1.2 §7 |
| 2026-10-01 | REQ-08 (stiffness) is a Soft bench gate answered by the first print | Oğuz | §5 |
| 2026-10-01 | 1.1 before the first build: OD-C11's wall top meets the rear skirt along a line, which U-03's 0.5 rule would have failed by construction; recorded as a designed contact; OD-C11's build v02 STEP is the reference | Oğuz (on the standing instruction) | OD-C11 REPORT v02 |
| 2026-10-01 | v01 REPORT stop on U-03 (a): the lid's rear skirt also rests on OD-C11's wall top at its two R 10 corners (two 5.907 mm² patches, interference 0); the Usta accepts them as designed contact, v01 goes to review as built | the Usta (decision card, 13:06Z) | 01_CAD/REPORT_od_c10_top_v01.md §10; usta_gate question_answered |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-01 | first draft from the OD-C01, OD-C02, OD-C05 and OD-C07 specs |
| 1.0 | 2026-10-01 | INTAKE_v01 cross-references in §6; ratified |
| 1.2 | 2026-10-01 | after build v01: U-03 (a)'s designed contact includes the rear skirt's corner patches on OD-C11's wall top, accepted by the Usta (U-03); no geometry change; spec 1.1 kept as `DESIGN_SPEC_v1.1.md` |
| 1.1 | 2026-10-01 | before build v01: the reference for OD-C11 is its build v02 STEP; U-03 (a) names the rear skirt's line contact with OD-C11's wall top (§1 table, U-03, A-02); spec 1.0 kept as `DESIGN_SPEC_v1.0.md` |
