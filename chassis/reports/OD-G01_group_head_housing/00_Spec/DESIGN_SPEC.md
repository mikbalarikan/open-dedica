# DESIGN_SPEC — OD-G01 printed group head housing (20260930-od-g01-group-head-housing)

Version 1.1 · RATIFIED by the Usta on 2026-09-30 (standing instruction "ilk öncelikli olan parçayı çizerek başlayalım"; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-G01 is the 3D-printed group-head housing of the Open Dedica espresso machine: the
open replacement for the housing molded into the De'Longhi Dedica EC685 case. It
must (a) lock the OEM 51 mm portafilter OD-G10 by its three bayonet ears exactly as
the OEM cup OD-G09 does, (b) hold the OEM brewing-gasket support OD-G04 by its three
tabs and two screws, (c) pass the support's hub tube through its rear plate, and
(d) mount to the printed chassis carrier OD-C05. Done means: one valid printable
solid whose functional zones reproduce OD-G09 within the tolerances of §5, checked
against the OD-G10 and OD-G04 solids as placed, with every unconfirmed value in §6.

**Deliverables** (tier M): STEP AP242 of the housing; the check assembly STEP
(housing + OD-G04 + OD-G10 as placed); STL; build and check scripts; REPORT;
sections. Drawings and renders are not required for v01 (the part goes to the
Usta's own printer, not a shop).

**Out of scope:** OD-C05 carrier, OD-G08 metal face plate, OD-T01 pressure rig,
the water connection parts (OD-H14, OD-H15, OD-G07), gaskets OD-G02/G03/G05, any
caliper work, drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-G09 (OEM cup) | `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` | — | the Usta, 2026-09-30 (open-dedica `step/`) | CONFIRMED as the input; its numbers are §6 rows |
| Mating solid OD-G04 (gasket support) | `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | — | same | CONFIRMED as the input |
| Mating solid OD-G10 (portafilter) | `00_Spec/inputs/OD-G10_portafilter.step` | — | same | CONFIRMED as the input |
| Fasteners | M3 heat-set inserts (OD-F01), M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard) |

**Coordinate frame:** identical to the OD-G09 STEP so the overlay is the identity:
Z is the cup axis, +Z points toward the mouth (the portafilter enters along −Z),
z = 0 is the plane of the lug top pads, the origin is on the axis, θ is measured
counter-clockwise about +Z from +X, and lug 1 spans θ = 336° … 30° (centre 3°).
In the machine, +Z is horizontal and faces the user. Every artifact of this job
uses this frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_g01_housing | FDM | machines/creality-k1c.toml (enclosed; build volume UNKNOWN → A-16) | ASA (BOM: ABS/ASA) | 1070 | as printed | A-15 |

Environment: kitchen counter; brew water at up to 125 °C and 15 bar reaches the
gasket support inside the housing; the portafilter is locked and unlocked by hand
many times a day; the housing carries the full brew load (A-21) through its lugs.

## §4 Architecture and concepts

- **C1 — OEM-faithful cup with a rear mounting flange (CHOSEN).** One solid. The
  functional interior is OD-G09's, parametrised: bore Ø74.20 straight (no draft)
  from the front face z = +3.30 down to the shelf z = −14.10; three lugs of 54°
  span at 120° pitch (starts 336°, 96°, 216°), inner R 31.68, top at z = 0, flat
  from R 31.68 to the bore (no top channel, A-23), underside a shallow plane from
  z = −6.57 at start + 7° to −5.59 at start + 41.8°, then a ramp to −1.15 at
  start + 54°; a stop block over the first 5.76° of each lug reaching down to
  z = −10.52; under each lug a pocket for an OD-G04 tab, floor z = −17.30 between
  R 35.00 and the bore over start − 5° … start + 58.5° (A-08), the shelf at
  z = −14.10 elsewhere; the lip ring for the OD-G04 flange and bead: R 31.70 over
  z −17.70 … −15.60 and R 31.30 over z −19.94 … −17.70 (A-09), down to the floor
  z = −19.94 on which OD-G04's flange rests (A-13). The rear slab is 5.00 thick
  (z −24.94 … −19.94, A-10), square 100 × 100 (corners R 8) so it is the mounting
  flange too, and carries: the central Ø26.0 opening for the OD-G04 hub; a rear
  counterbore Ø34.0 × 2.50 deep around it for the water connection (A-24); two
  Ø9.0 pass-through holes at r 15.5, θ 359.5° and 179.0° for OD-G04's boss pair A
  (they merge with the Ø26 opening into the OEM's two keyhole lobes, A-11); two
  Ø9.0 × 2.30 recesses from the floor with Ø3.8 through-holes at r 19.03,
  θ 119.3° and 304.0° for OD-G04's boss pair B and the OEM's own screws driven
  from the rear (A-12, A-26); four M3 heat-set inserts at (±44, ±44) from the rear
  face (hole Ø4.0 × 5.7, A-17) with a boss OD 8.0 on the floor side wherever the
  slab is thinner than the hole (a derivation, not a spec feature), for OD-C05
  (A-18). Outside: a wall 6.00 thick (outer Ø86.2) from the slab to the flat front
  face at z = +3.30 (no rim notches, A-23). Print orientation: mouth up, rear face
  on the bed; supports under the three lugs and three stop blocks only (A-22).
  Envelope 100 × 100 × 28.24.
- **C2 — C1 with OD-G08 metal face plate carrying the lugs.** Same housing, lugs
  replaced by a laser-cut plate clamped at the front. Deferred: it needs a shop
  part and the bench test of C1 first (open-dedica BOM: OD-G08 "optional upgrade").

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 100.0 × 100.0 × 28.24 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) housing|OD-G10 at the locked pose and housing|OD-G04 seated: `interference ≤ 0` mm³; designed contacts (the three ear tops on the lug undersides at the locked pose; OD-G04's flange bottom on the floor) are `clearance = 0` pairs and are not gated by the boolean; OD-G04's tabs, pair A and pair B bosses, bead and hub keep `clearance ≥ 0.5` to the housing (D-04c); (b) housing|OD-G10 along the lock path (insertion along −Z, then rotation to the stop, swept together, L-09/L-10): `interference ≤ 0` mm³. No fasteners move. | Hard | CAD | house | `interference`, `clearance`; sweep: reviewer's own script | A-13, A-14, A-19 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 1 Ø34 rear counterbore, 2 Ø9 pass-through holes (pair A), 2 Ø9 recesses and 2 Ø3.8 through-holes (pair B), 4 Ø4.0 insert bores | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 1.0 (same limit as D-01b here) | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/43.1) rad; `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none (inserts take the thread) | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 1.0`: set below the 2.0 default because the OEM lug ramp ends 1.15 thick (A-05); the cup wall itself is REQ-09 | Hard | part | struct | `min_wall` | A-05 |
| D-02 | Bed fit | each envelope size ≤ the K1C build volume, mouth up: 100 × 100 × 28.24 | Hard | part | machine | `envelope` | A-16 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal, or supported by decision: the lug undersides and stop-block bottoms are supported (A-22); everything else must pass | Hard | part | floor | reviewer, from sections | A-22 |
| D-03b | Unsupported bridge | span ≤ 5 | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | the two pair-B screw holes Ø ≥ 3.5 + 0.25 = 3.75 (designed Ø3.8) | Hard | part | house | `locate_bore` | A-26 |
| D-05a | Heat-set insert boss | the four carrier inserts: material ≥ 8.0 across around each Ø4.0 hole (slab or boss) | Hard | part | struct | `bore_census`, `radial_extent`; OD: reviewer | A-17 |
| D-05b | Heat-set insert hole | the four carrier inserts: Ø 4.0 ± 0.05, depth ≥ 5.7 from the rear face (A-17) | Hard | part | floor | `bore_census`, `locate_bore` | A-17 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | applies to reamed fit bores; this part has none (insert holes are formed by the insert, the Ø26 opening has ≥ 2.9 radial clearance to the hub) | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 (M3) around each of the four insert holes | Hard | part | struct | `min_wall` | — |
| E-06 | Boss support | every insert boss tied into the slab with a root fillet | Hard | part | struct | reviewer | — |
| REQ-01 | Lug inner radius | `radial_profile` inner over the lug sectors (start + 8° … start + 40°), z −5.0 … −1.0: min and max in [31.58, 31.78] | Hard | CAD | A-02 | `radial_profile` | A-02 |
| REQ-02 | Bore radius in the gaps | `radial_profile` inner over the gap sectors (start + 60° … start + 114°), z −13.0 … +2.0: min and max in [37.05, 37.15] | Hard | CAD | A-03 | `radial_profile` | A-03 |
| REQ-03 | Lug angular layout | at z = −3.0 the inner radius reads ≤ 31.78 at start + 1°, + 27°, + 53° and ≥ 37.05 at start − 1° and start + 55°, for all three lugs (starts 336°, 96°, 216°) | Hard | CAD | A-04 | `radial_extent` | A-04 |
| REQ-04 | Lug underside profile | at start + 20°: inner radius ≤ 31.78 at z = −5.9 and ≥ 34.0 at z = −7.0; at start + 50°: ≤ 31.78 at z = −2.3 and ≥ 34.0 at z = −3.2 (the shallow plane and the ramp of A-05, brackets ± 0.3) | Hard | CAD | A-05 | `radial_extent` | A-05 |
| REQ-05 | Stop block | at start + 2.9°: inner radius ≤ 31.78 at z = −9.0 and ≥ 34.0 at z = −11.0 | Hard | CAD | A-06 | `radial_extent` | A-06 |
| REQ-06 | Hub opening | one through-bore Ø 26.0 ± 0.1 on the axis through the rear plate | Hard | CAD | A-10, A-11 | `locate_bore` | A-10, A-11 |
| REQ-07 | OD-G04 pair B seats | two Ø3.8 through-holes at r 19.03, θ 119.3° and 304.0° (offset ≤ 0.10), each under a Ø9.0 ± 0.1 recess 2.30 ± 0.10 deep from the floor | Hard | CAD | A-12 | `locate_bore` | A-12, A-26 |
| REQ-08 | Carrier inserts | four Ø4.0 insert bores at (±44, ±44) from the rear; offset ≤ 0.10 | Hard | CAD | A-18 | `locate_bore` | A-18 |
| REQ-09 | Cup wall | outer radius ≥ 43.05 at every 5° over z −19.0 … +3.0 and inner ≤ 37.15 in the gaps: wall ≥ 5.9 | Hard | part | A-21 | `radial_profile` outer and inner | A-21 |
| REQ-10 | Ear passage | over the insertion path (ears centred in the gaps, rim from z −5.0 down to the first-contact height ≈ −11.7, at least 5 poses) `clearance(housing, OD-G10) ≥ 0.30` (D-04d's floor; the OEM pair reads 0.50 at first contact), the nearest points reported | Hard | CAD | A-19 | `clearance` | A-19 |
| REQ-11 | Web under the floor | the Ø26 through-bore of REQ-06 has length 2.50 ± 0.10 (the web between the floor z −19.94 and the rear counterbore) | Hard | CAD | A-10 | `locate_bore` length | A-10 |
| REQ-13 | Rear counterbore and pair A holes | one Ø34.0 ± 0.1 bore 2.50 ± 0.10 deep from the rear face on the axis; two Ø9.0 ± 0.1 through-holes at r 15.5, θ 359.5° and 179.0° (offset ≤ 0.10) | Hard | CAD | A-11, A-24 | `locate_bore` | A-11, A-24 |
| REQ-12 | Brew load | withstands 15 bar on a Ø51 basket (3.06 kN, A-21) on the bench rig OD-T01; not a geometric gate: INCONCLUSIVE until tested | Hard | part | client | — (bench test) | A-21 |

**Named exceptions** (Usta U-18): none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | Scan scale and units | mm, scanner calibration, no caliper check (all three reference scans) | every fit off by the scale error | G09/G04/G10 reports L2; INTAKE X-001…X-144 (all scan rows); OD-G09 has no official grade (verify run HALT, owner override: INTAKE §4 Q5) | calipers on the donor cup (ENV rows) | OPEN |
| A-02 | Lug inner radius | 31.68 (S; per lug 31.70/31.84/31.49, ring 0.19 off axis) | ears bind or rattle | G09 PARAM_TABLE LUG_INNER_R; INTAKE X-022…X-030 (lugs) | caliper across lugs | OPEN |
| A-03 | Bore radius | 37.10 (S 37.074 at z 0 with 0.645° draft; designed straight) | ears bind in the gaps | G09 PARAM_TABLE BORE_R_Z0; INTAKE X-007…X-010 | caliper bore Ø | OPEN |
| A-04 | Lug angles | starts 336/96/216, span 54, pitch 120 (S) | ears miss the gaps (37° ears in 66° gaps: 14° margin) | G09 PARAM_TABLE lugs; INTAKE X-022…X-024; the ears are at 120.5/120.5/119° (A-25) | protractor on the donor | OPEN |
| A-05 | Lug underside profile | −6.57 at +7°, −5.59 at +41.8°, −1.15 at +54° (S, lower edge only); the rest of the underside hidden | gasket compression wrong: leak or a lock that will not close | G09 PARAM_TABLE underside; INTAKE X-031…X-036 | caliper depth rim → underside at three angles | OPEN |
| A-06 | Stop block | 0 … 5.76° from the lug start, bottom z −10.52, full radial depth (S/A) | portafilter over-rotates | G09 PARAM_TABLE stop; INTAKE X-027…X-030 | donor | OPEN |
| A-07 | Shelf level | −14.10 for all gaps (S per gap −14.10/−13.44/−14.23) | G04 tab clearance | G09 PARAM_TABLE shelf; INTAKE X-045…X-047 | donor | OPEN |
| A-08 | Pocket floor and riser | OEM −16.80 and R 34.39 (S); designed −17.30 and R 35.00 so the tabs (tip R 34.52, bottom 0.30 above the OEM pocket floor when the flange is on the floor) keep 0.5 clearance | G04 tabs do not seat | G09 PARAM_TABLE pockets; INTAKE X-037…X-044; the tabs are assumed to seat in the pockets, not the rim notches (INTAKE §4 Q8) | donor | OPEN |
| A-09 | Lip ring | OEM R 30.82 upper, R 31.33 lower (S); designed R 31.70 upper (the bead R 31.175 + 0.5) and R 31.30 lower (the flange R 30.8 + 0.5), step at −17.70, floor −19.94 | G04 flange does not locate | G09 PARAM_TABLE lip; INTAKE X-051…X-056 | donor | OPEN |
| A-10 | Plate thickness and level | floor z −19.94 (S); OEM plate 2.5 (A); designed slab 5.0 with a rear counterbore Ø34 × 2.5 so the web at the opening is 2.5 like the OEM | hub tube ends 2.4 inside the slab: the water connection may not reach (A-24) | G09 PARAM_TABLE PLATE_T (photo, ±); INTAKE X-017, X-018, X-068, X-069 (§4 Q6) | calipers; the connection parts | OPEN |
| A-11 | Keyhole lobes | the lobes are the pass-throughs of OD-G04's boss pair A (r 15.5, OD 6.98, 3.0 below its flange): designed as Ø9.0 holes at θ 359.5° and 179.0° (pair A at the A-12 clock, + 1.0 clearance); the photo's lobes (133°/310°) and bosses (66°/246°) both read as ≈ 50° mis-clocked, which the designer's measurement supports (pair A passes the photo lobes at clock −40°) | G04 does not seat: a reprint after calipers | G09 PARAM_TABLE keyhole; INTAKE X-057…X-059, X-062…X-065 | calipers | OPEN |
| A-12 | G04 clock and screws | clock +6.05°: tab 1 (−3.3° in G04's frame) centred on pocket 1 (sector centre 2.75°); pair B (r 19.03, at 113.27° and −62.02° in G04's frame) lands at θ 119.3° and 304.0° and takes the OEM's screws from the rear through Ø3.8 holes; pair A lands at 359.5° and 179.0° (A-11) | screws miss | G04 PARAM_TABLE bosses; INTAKE X-091…X-101 against X-060, X-061, X-066 (§4 Q1, Q2, Q3, Q7: pair A at PCD 31.0 is taken as the diffuser's screws, pair B as the housing's) | calipers on the donor cup | OPEN |
| A-13 | G04 axial seat | the flange bottom (G04 z −13.12) rests on the floor z −19.94: back face at housing z −6.82; the tabs then float 0.5 above the designed pocket floors, pair A bottoms at −22.94 and pair B bottoms at −21.70 inside the slab, the hub tube bottom at −22.55 (derived; the tabs-on-pocket-floor seat −7.28 overlapped the OEM cup by 0.46 mm) | G04 floats or is proud | derived from A-08 and G04 tabs | assembly of the donor parts | OPEN |
| A-14 | Locked pose of OD-G10 | ears under the lugs at the stop: ear top face on the shallow underside at start + 7° … + 42°, the ear leading edge 0.5° short of the stop; rim face 5.10 below the ear top (G10 lug thickness, S) | wrong compression; the check pose is not the real pose | G10 PARAM_TABLE lugs; A-05 | donor lock test | OPEN |
| A-15 | Material | ASA, density 1070 kg/m³, printed on the K1C (recorded material PLA; ASA needs the enclosure) | wrong mass; PLA deforms at brew temperature (thesis) | BOM OD-G01 (INTAKE X-167); chassis rule 3 (X-155, §4 Q9: the housing carries 95–125 °C water, so it is near heat); typical ASA datasheet | the Usta names the filament | OPEN |
| A-16 | K1C build volume | 220 × 220 × 250 (Creality specification, not in the machine file) | part does not fit | memory of the spec sheet | the Usta reads the printer | OPEN |
| A-17 | M3 heat-set insert | hole Ø 4.0, depth 5.7, insert length 5.7 (reseller figure) | insert loose or proud | typical M3 × 5.7 × 4.6 insert listing | the Usta's stocked insert datasheet | OPEN |
| A-18 | Carrier interface | 4 × M3 inserts at (±44, ±44) from the rear, flange 100 × 100 × 4 | OD-C05 must be designed to it | this spec (design choice, no OD-C05 yet) | OD-C05 design | OPEN |
| A-19 | Ear geometry | 3 ears Ø 71.93 swept, 35–37° span, 5.10 thick, at 59.5/180/300.5° from the handle (S) | passage or lock wrong | G10 PARAM_TABLE lugs; INTAKE X-120…X-140 | calipers | OPEN |
| A-20 | Thesis Appendix 2 | not available; not used | none for geometry | BOM note | the Usta supplies it | OPEN |
| A-21 | Brew load | 15 bar × π (25.5)² = 3.06 kN on the lugs; cup wall 6.0 and lug root as OEM; strength not calculated | housing fails under pressure | this spec | OD-T01 bench test (REQ-12) | OPEN |
| A-22 | Print orientation and supports | mouth up; supports under the lugs and stop blocks | surface under the lugs rough: ears scrape | this spec | first print | OPEN |
| A-23 | Omitted OEM details | lug top channel, six rim notches, Ø6 side hole at θ 269° R 20.8 (P) are non-functional | a hidden function is lost | G09 PARAM_TABLE; INTAKE X-048…X-050 (notches), X-067 (side hole) | the Usta looks at the donor | OPEN |
| A-24 | Water connection below the plate | the hub tube (OD 20.06, bottom at housing z −22.55) receives OD-H14/H15 with OD-G07 from the rear through the Ø34 × 2.5 counterbore; their envelope is unknown | connection does not fit under the flange | G04 PARAM_TABLE hub (INTAKE X-102…X-110); BOM OD-G07/H14/H15 | scan or calipers of OD-H14/H15 | OPEN |
| A-25 | Ear pitch | the housing's lugs are symmetric at 120° while the scanned ears sit at 120.5/120.5/119° (S, not within noise); the 66° gaps leave 14° for a 37° ear, so the 1° asymmetry is absorbed by the gap | ears bind at the gap edges | G10 PARAM_TABLE (INTAKE X-124, X-131, X-138; §4 Q4) | donor lock test | OPEN |
| A-26 | OD-G04 screws | the OEM's two self-tapping screws, Ø 3.5 assumed (G04 pilot Ø 3.06); housing holes Ø 3.8 (D-04a) | screw does not pass or the head pulls through | G04 PARAM_TABLE boss holes; this spec | the Usta measures the donor screws | OPEN |
| A-27 | Brewing gasket and lock compression | the rim lands at z −11.67 at the shallow underside while the gasket groove floor (G04 flange top) is at −17.58: an 8.0 mm gasket compresses 1.6 mm, first contact after 3.8 mm of the 5.4 mm lock travel; gasket thickness unknown | no seal or a lock that will not close | G04 PARAM_TABLE (flange, lip); A-05, A-13; this spec | caliper on OD-G02 | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction of 2026-09-30 (the message that opened the job); the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | INTAKE §4 Q10 (group head ≥ 95 mm above the tray) is a chassis requirement: carried to OD-C05 and OD-C01, out of this job's scope | Oğuz | INTAKE_v01 §4 |
| 2026-09-30 | spec 1.1: the OD-G04 pose of 1.0 was measurably wrong (OEM cup and support overlap 1059 mm³ at it); 1.1 seats OD-G04 by its flange and reads the photo-derived plate layout as mis-clocked by ≈ 50°, to be confirmed by calipers on the donor cup | Oğuz on the standing instruction; the Usta confirms | DESIGN_PLAN §7 R1 |
| 2026-09-30 | REQ-12 (brew load) is a part gate answered only by the OD-T01 bench test; the review reports it INCONCLUSIVE and the delivery states it | Oğuz | §5 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the three reference reports and the STEP probes |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6, A-25 added, REQ-11 reworded; ratified |
| 1.1 | 2026-09-30 | after the designer's J2 stop (DESIGN_PLAN §7 R1, R2): OD-G04 seated by its flange on the floor, pair A through Ø9 lobes, pair B in recesses with the OEM screws from the rear (no inserts there), pockets and lip ring given 0.5 clearance, slab 5.0 with a rear counterbore, REQ-10 at 0.30 over the path, REQ-13, D-04a, A-26, A-27; ratified on the same standing instruction |
