# DESIGN_SPEC — OD-C15 printed TPU foot (20261001-od-c15-feet)

Version 1.2 · RATIFIED by the Usta on 2026-10-01 (standing instruction "Usta'ya yalnız karar gereken yerde sor; açık soruları A-## satırı olarak ledger'a yaz ve ilerle" and the message of 2026-10-01 10:58 UTC "what can start now please initiate it"; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-C15 is the printed TPU foot of the Open Dedica espresso machine, four per
machine, one under each of the four Ø3.4 feet holes of the delivered base frame
OD-C01. It carries the machine on the counter, keeps a gap under the plate for its
drain holes, damps the pump's vibration and keeps the machine from walking
(SOURCING_GUIDE §6 rule 2). Each foot is a round TPU puck held by one M3 screw
from the plate top into a hex nut captive in the foot. Done means: one valid
printable solid that seats flat on the plate underside, coaxial with its hole,
inside the plate's outline, holds the nut, and stands the machine level, with
every unconfirmed value in §6.

**Deliverables** (tier S): STEP AP242 of one foot; the check assembly STEP
(OD-C01 + four feet + screw and nut envelopes as placed); STL of one foot
(print four), and at J5 a 3MF written from the reviewed STL by OD-C01's
`stl_to_3mf.py` (geometry unchanged); build and check scripts; REPORT; sections. No drawings, no renders.

**Out of scope:** OD-C01 itself (delivered; its holes are fixed); the OEM pads
OD-C25/C26 and any cup for them (C2); the side panels, corner brackets and other
parts on the plate top (they receive the keep-out of A-09); the OD-000 assembly
(the OD-G01 thread owns it); calipers.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Mating solid OD-C01 base frame | `00_Spec/inputs/OD-C01_base_frame.step` (INTAKE §1) | — | open-dedica `chassis/`, delivered and merged (PR #46) | CONFIRMED as the input; its numbers are A-01 |
| Quantity and material | 4 feet, TPU | — | BOM OD-C15 (INTAKE §3) | CONFIRMED (BOM) |
| Fastener family | M3 screws ISO 7380 / DIN 912 A2 (OD-F02, OD-F10) | — | BOM (INTAKE §3) | CONFIRMED (project standard); the exact screw and nut are A-02 |

**Coordinate frame (foot):** origin at the centre of the foot's top face (the
face that bears on the plate underside), on the screw axis; +Z runs down in the
machine, away from the plate, and is the print build direction (the top face lies
on the bed); the foot occupies z 0 … 10. +X is parallel to the OD-C01 X axis; one
pair of the hex pocket's flats is parallel to X. **Joint to OD-C01** (machine
frame, X right, +Y up, +Z front, plate top y = 0): foot x → X, y → +Z, z → −Y,
origin at (±110.0, −6.0, +90.0) and (±110.0, −6.0, −295.0), so the top face lies on
the plate underside y −6.0 and the counter face at y −16.0. Every artifact of this
job uses these frames.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c15_foot | FDM | machines/creality-k1c.toml (direct-drive extruder for TPU; build volume UNKNOWN → A-08) | TPU 95A | 1210 | as printed | A-03 |

Environment: under the machine on a kitchen counter, wet (the plate's two Ø8 drain
holes and the tray zone shed water onto the counter between the feet); room
temperature, far from the thermoblock; static load a quarter of the machine's
weight per foot (A-05) plus the portafilter locking torque and the pump's
vibration.

## §4 Architecture and concepts

- **C1 — round TPU puck with a captive hex nut (CHOSEN).** One solid per foot,
  printed top face down (z 0 on the bed). **Body**: cylinder Ø18.0 × 10.0 on the
  hole axis (radius 9.0 inside the plate's R10 corner arc, which is centred on the
  hole, so the foot stays 1.0 inside the plate outline), a chamfer 0.50 along
  the axis × 0.29 radial (60° from horizontal) on the top-face edge (z 0, the
  bed side: elephant-foot relief) and a 1.0 × 45°
  chamfer on the counter-face edge (z 10). **Lid**: the solid layer z 0 … 2.5 under
  the plate, with a Ø3.4 clearance hole on the axis (D-04a). **Nut pocket**: a
  hexagonal pocket across flats 5.60, from the nut seat at z 2.5 to the counter
  face z 10.0 (open, 7.5 deep), with a 0.5 × 45° entry chamfer at the mouth; an
  ISO 4032 M3 nut (s 5.5, m 2.4) is pulled up the pocket by the screw onto the seat
  at z 2.5 … 4.9, and the hex flats hold it against turning (A-06). **Fixing**: an
  M3×12 ISO 7380 A2 button-head screw from the plate top (head on y 0 … 1.65),
  through the plate's Ø3.4 hole and the lid, into the nut; it clamps the lid
  between the nut and the plate (A-02, A-07); its tip ends at foot z 6.0, 1.1 past
  the nut and 4.0 above the counter. No supports, no bridges: every face is
  vertical, horizontal facing up in the build direction, or the 60° bed chamfer.
  Envelope 18.0 × 18.0 × 10.0. Mass ≈ 2.8 g at 1210 kg/m³.
- **C2 — printed cup for the OEM rubber pads OD-C25 / OD-C26.** A PETG or TPU cup
  screwed the same way, holding the OEM pad. Not chosen: the pads are neither
  scanned nor measured (BOM `CALIPER`), and the BOM row names the printed foot as
  the part to design; reopened if the Usta prefers the OEM pads (A-10).
- **C3 — foot with a heat-set insert, screwed from below** (OD-C01 A-12 as
  written). Not chosen: a heat-set insert holds poorly in TPU, and a screw from
  below puts its head in the counter face or needs a nut on the plate top anyway.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 18.0 × 18.0 × 10.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (min x −9, min y −9, min z 0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) in the check assembly at the four poses of §2: designed contacts `clearance = 0`: each foot's top face on the plate underside, each nut envelope's top face on its foot's nut seat (z 2.5), each screw head envelope's underside on the plate top; every other pair `interference ≤ 0` mm³: foot \| plate, foot \| nut, foot \| screw, nut \| plate, screw \| plate (the screw shank in the Ø3.4 holes is D-04a, the nut in its pocket REQ-03). (b) assembly path: each nut envelope slid along the pocket axis from the mouth (nut bottom at foot z 10.0) to its seat, at least 5 poses, `interference ≤ 0` mm³ against its foot. The fasteners are envelopes: the screw a Ø5.7 × 1.65 head and a Ø3.0 shank to its tip at y −12.0 (C01 frame); the nut a hexagon s 5.5 × e 6.35 × m 2.4 with a Ø3.0 bore (threads not modelled) | Hard | CAD | house | `interference`, `clearance`; the sweep: reviewer's own script | A-01, A-02 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 outer cylinder Ø18.0; 1 lid through-hole Ø3.4 (axis Z, z 0 … 2.5); 1 hex pocket of 6 planar flats, open at z 10; 3 chamfers (top edge 0.5, counter edge 1.0, pocket mouth 0.5); 2 planar end faces (top annulus, counter annulus) and the nut seat | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 (same limit as D-01b) | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad, R_max the largest curved-face radius (9.0); `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `stl_max_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none (the nut takes the thread; the check assembly's fasteners are envelopes) | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall` ≥ 0.8 | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural default | `min_wall` ≥ 2.0 | Hard | part | struct | `min_wall` | A-03 |
| D-02 | Bed fit | each envelope size ≤ the build volume, top face down: 18 × 18 × 10 against 220 × 220 × 250 | Hard | part | machine | `envelope` | A-08 |
| D-03a | Unsupported overhang | every downward face (against the build direction +Z) ≥ 45° from horizontal; the only downward face is the top-edge chamfer at 60° | Hard | part | floor | `overhang_census`; reviewer from sections | — |
| D-03b | Unsupported bridge | span ≤ 5; this part has none in its print orientation (the lid lies on the bed) | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | lid hole Ø ≥ 3.25 (M3, designed Ø3.4) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-04c | Clearance around a seated component | ≥ 0.5 per side between the foot and the screw shank below the nut seat (the shank in the pocket); the nut is REQ-03, the shank in the lid hole D-04a | Hard | part | house | `clearance` | A-02 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | applies to reamed fit bores; this part has none (the nut pocket is REQ-03) | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | the wall around the nut pocket, measured on the ring z 2.5 … 10 only (from the hex flats and corners to the outer cylinder and the chamfers) ≥ 3.0 (M3); the lid z 0 … 2.5 is not this row's region (D-01b governs it) | Hard | part | struct | `min_wall` | — |
| J-06 | Printed threads | none below M5: no threaded bore in the part | Hard | part | floor | `bore_census` | — |
| REQ-01 | Top face | the face at z 0.0 ± 0.1 is one plane, an annulus from the lid hole to Ø17.42 (the 0.29 radial chamfer), normal −Z | Hard | CAD | house | `envelope`; `feature_census` | — |
| REQ-02 | Lid hole | Ø3.4 ± 0.1 through z 0 … 2.5, coaxial with the outer cylinder, offset ≤ 0.10 | Hard | CAD | house | `locate_bore` | A-01 |
| REQ-03 | Nut pocket | hexagon across flats 5.60 +0.05 / −0 (ISO 4032 M3 s 5.32 … 5.50: 0.05 … 0.165 per side), flats parallel to X ± 1°, centred on the axis ≤ 0.10, from the seat z 2.50 ± 0.1 to z 10.0 (open), entry chamfer 0.5 | Hard | CAD | house | `feature_census`; `clearance` nut envelope to each flat; sections | A-06 |
| REQ-04 | Body | outer Ø18.0 ± 0.1, height 10.0 ± 0.1; chamfers 0.50 axial × 0.29 radial (60°, z 0 edge) and 1.0 × 45° (z 10 edge), each ± 0.1 | Hard | CAD | house | `envelope`; sections | A-05 |
| REQ-05 | Inside the plate | at each pose, the foot's footprint lies within the OD-C01 plate's outline seen along Y: least distance from the foot's outer cylinder to the plate edge ≥ 0.9 (designed 1.0 at the R10 corner arc, 1.0 to the straight edges) | Hard | CAD | house | `envelope` of each placed foot against the plate's; reviewer computes the corner arc | A-01 |
| REQ-06 | Level stance | the four counter faces coplanar at y −16.00 ± 0.10 (C01 frame); the four feet enclose the plate's centre of mass | Hard | CAD | house | `envelope` of each placed foot; `mass_properties` of the plate | A-01, A-04 |
| REQ-07 | Screw engagement | the M3×12 screw tip at foot z 6.0 ± 0.1: ≥ 0.5 past the nut's lower face (z 4.9) and ≥ 2.0 above the counter face | Hard | CAD | house | `envelope` of the screw envelope in the foot frame | A-02 |

**Named exceptions:** none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-C01 interface | plate 240 × 405 × 6.0, top y 0, underside y −6.0, four Ø3.4 through-holes at (±110.0, +90.0) and (±110.0, −295.0), corner R10 centred on each hole, as built in the delivered STEP; the plate underside is flat around each hole | the foot misses its hole or rocks | OD-C01 spec 1.2 REQ-05, REQ-07, A-12; RV01 F06; the STEP (INTAKE X-01 … X-10) | the Usta's print of OD-C01 and a flatness check (OD-C01 RV01 F1) | OPEN |
| A-02 | Fixing | one M3×12 ISO 7380 A2 button-head screw per foot from the plate top (head Ø5.7 × 1.65 on y 0) into an ISO 4032 M3 A2 hex nut captive in the foot; replaces OD-C01 A-12's "screwed from below into inserts of the feet" (C3) | the screw is too short or too long; the head clashes on the plate top (A-09) | this spec; BOM OD-F10 (same screw); ISO 7380, ISO 4032 (INTAKE X-23, X-41, X-44; §4 Q3, Q4) | the Usta's choice of screw and nut | OPEN |
| A-03 | Material and printer | TPU 95A (Shore A), density 1210 kg/m³, printed on the K1C (its machine file lists PLA only) | a softer TPU lets the nut turn in its pocket and the machine sway | BOM OD-C15; this spec (INTAKE X-30, X-45 … X-47; §4 Q5, Q6) | the Usta names the filament and the printer | OPEN |
| A-04 | Foot height | 10.0: a 10 mm gap between the plate underside and the counter for the drain holes (OD-C01 A-13) and air; the machine grows by 10 (OD-C01 A-16) | drains do not clear; the machine is too tall for a shelf | this spec (INTAKE X-17, X-24; §4 Q1) | the Usta's layout confirmation | OPEN |
| A-05 | Foot diameter and load | Ø18.0, contact ≈ 220 mm² per foot; the machine's mass unknown, taken ≤ 8 kg with a full tank (≈ 20 N per foot, ≈ 0.1 MPa) | none at this load; grip on the counter is a bench check | this spec (INTAKE X-18, X-19; §4 Q2, Q8) | the Usta weighs the machine | OPEN |
| A-06 | Nut pocket fit | across flats 5.60 (+0.10 over the nut's 5.50) grips the nut in TPU without heat; the nut is drawn up by the screw | the nut spins while tightening (too loose) or will not enter (too tight) | this spec (common practice for TPU nut traps, no source) | the first printed foot | OPEN |
| A-07 | Clamp creep | the 2.5 lid clamped between nut and plate creeps a little; a drop of medium threadlocker holds the screw. A nylon-insert nut (ISO 10511, m 4.0) also fits the pocket but needs an M3×16 | the feet loosen over time | this spec | the first month of use | OPEN |
| A-08 | Build volume | the K1C's volume taken as 220 × 220 × 250 (not in its machine file) | none for an 18 mm part | Creality product listing, not copied into the machine file | the machine file | OPEN |
| A-09 | Plate-top keep-out | a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) stays free for the screw head; handed to OD-C12, OD-C13, OD-C16 and OD-C06 | a corner bracket or panel lands on the screw head | this spec (INTAKE §4 Q7: the reserved zones of OD-C01 §4 all lie clear of the four holes) | those parts' jobs | OPEN |
| A-10 | Printed vs OEM feet | the printed foot is the machine's foot; the OEM pads OD-C25 / OD-C26 are not used (C2 deferred) | the Usta prefers the OEM pads | BOM OD-C15, OD-C25, OD-C26 (INTAKE X-31 … X-33, X-39; §4 Q9: "526" read as OD-C26) | the Usta | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-01 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-10-01 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and the message of 2026-10-01 10:58 UTC; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-10-01 | spec 1.1 on the designer's J2 questions: Q1 → chamfer at 60° (option a; keeping 45° would leave D-03a to the reviewer's judgement); Q2 → J-05 on the ring z 2.5 … 10, D-04c on the shank below the seat, as named; Q3 → 3MF at J5 from the reviewed STL. Ratified on the standing instruction | Oğuz (standing instruction) | usta_gate spec_ratified 1.1 |
| 2026-10-01 | spec 1.2: REQ-03's parenthetical per-side range read 0.16 where its own limits give 0.165 (the D7 sweep corner af 5.65 × s 5.32); corrected, no geometry change. Ratified on the standing instruction | Oğuz (standing instruction) | usta_gate spec_ratified 1.2 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-01 | first version from INTAKE_v01; ratified |
| 1.2 | 2026-10-01 | after the J3 build (REPORT v01 §4, §9.1): REQ-03's per-side range corrected to 0.05 … 0.165, the arithmetic of its own limits ((5.65 − 5.32) / 2); no geometry change |
| 1.1 | 2026-10-01 | after the J2 plan (DESIGN_PLAN §7): the bed-edge chamfer becomes 0.50 axial × 0.29 radial at 60° so D-03a is measurable (`overhang_census` is INCONCLUSIVE at exactly 45°; Q1); J-05 and D-04c measured on their named regions only (Q2); the 3MF is written at J5 from the reviewed STL (Q3) |
