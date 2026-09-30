# DESIGN_SPEC — OD-C05 printed group head carrier (20260930-od-c05-group-head-carrier)

Version 1.0 · RATIFIED by the Usta on 2026-09-30 (standing instruction of 2026-09-30 and the "confirmed go" / "go" of the same day: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-C05 is the 3D-printed group head carrier of the Open Dedica espresso machine: the
bracket that holds the printed group head housing OD-G01 by the four M3 heat-set
inserts in its rear flange, keeps the space behind the housing open for the OD-G04
hub tube, the OEM water connection and the hot water tube (TUBE 7), holds the group
head high enough for a mug under the portafilter (≥ 95 mm above the drip tray,
INTAKE X-66), and bolts to the printed base frame OD-C01. Done means: one valid
printable solid with a flat front face that seats on the housing's rear face, four
screw holes on the housing's insert pattern, a foot with a screw pattern for
OD-C01, two windows behind the housing, nothing closer than 10 mm to the thermoblock
zone, and every unconfirmed value in §6. The drip tray OD-C21, the tube TUBE 7 with
its connector OD-H23, and OD-C01 are not designed or scanned: their rows are
assumptions and the job is reopened when they land.

**Deliverables** (tier S): STEP AP242 of the carrier; the check assembly STEP
(carrier + OD-G01 build v02 + OD-G04 as the housing's REPORT places it); STL and
3MF; build and check scripts; REPORT; sections. No drawings or renders.

**Out of scope:** OD-C01 base frame, OD-C02 bulkhead, the drip tray, TUBE 7 and
OD-H23, the OEM water connection parts OD-G07 / OD-H14 / OD-H15, the thermoblock
mount OD-C04 (placed by OD-C01), calipers, drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-G01 (housing, build v02) | `00_Spec/inputs/OD-G01_housing_C1_v02.step` (INTAKE §1 #1); its rear flange has not changed since OD-G01 spec 1.2 (spec 1.3 changed only a probe definition) | — | OD-G01 job record, 2026-09-30 | CONFIRMED as the input; its numbers are §6 rows |
| Mating solid OD-G04 (gasket support) | `00_Spec/inputs/OD-G04_brewing_gasket_support.step` (INTAKE §1 #2), placed as the OD-G01 REPORT v02 §5 places it | — | open-dedica `step/` | CONFIRMED as the input |
| Reference solid OD-H11 (thermoblock) | `00_Spec/inputs/OD-H11_thermoblock.step` (INTAKE §1 #3); not placed: its zone is A-05 | — | open-dedica `step/` | CONFIRMED as the input; not gated against |
| Fasteners | M3 heat-set inserts (OD-F01) in OD-G01 and OD-C01, M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` (INTAKE X-75, X-76) | CONFIRMED (project standard) |

**Coordinate frame:** identical to the OD-G01 STEP so the overlay is the identity
(OD-G01 spec §2): Z is the group head axis, +Z points toward the mouth and the user,
z = 0 is the plane of the housing's lug top pads, the housing's rear face is the
plane z = −24.94 (INTAKE X-07), the origin is on the axis, θ counter-clockwise about
+Z from +X. In the machine +Z is horizontal and faces the user, and **+Y points up**
(A-02): the carrier hangs the housing from a vertical wall behind it and stands on
the base frame's floor plane y = −150.0 (A-03). Every artifact of this job uses this
frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c05_carrier | FDM | machines/creality-k1c.toml (enclosed; build volume UNKNOWN → A-08) | ASA (BOM: ASA) | 1070 | as printed | A-12 |

Environment: inside the machine, behind the group head; hot water tube and the OEM
water connection behind the housing (≈ 100 °C), drips and steam possible; the
thermoblock is at least 10 mm away (A-05). Loads: the housing (≈ 97 g, INTAKE X-25)
with the portafilter and the brewing gasket stack, the user's locking torque on the
portafilter, and the pull of the water connection; the brew load itself (INTAKE
X-24) is reacted inside the housing between lugs and gasket, not by the carrier.

## §4 Architecture and concepts

- **C1 — vertical wall on a foot, two gussets, two windows (CHOSEN).** One solid.
  A wall 5.0 thick along Z, z −29.94 … −24.94, whose front face is the plane of the
  housing's rear face (a designed contact, A-01), spanning x −50 … +50 and
  y −150.0 … +50.0, its two top corners R 8 like the housing flange (INTAKE X-04),
  its bottom edge on the foot. Through the wall along Z: four Ø3.4 holes at
  (x ±44.0, y ±44.0), coaxial with the housing's four insert bores (INTAKE X-10,
  X-11), each with a counterbore Ø6.5 × 2.0 from the rear face (z −29.94) so an M3 × 8
  screw leaves 3.0 of wall under its head and reaches 5.0 into the 5.7 insert (A-09);
  a hub window centred on the axis, R 30.0 (a Ø60 opening around the housing's Ø26
  hub opening, the OD-G04 hub tube and the two OEM pair-B screw heads at r 19.03,
  INTAKE X-19, X-36; the unknown water connection behind the hub gets r ≤ 30, A-06)
  whose top is a 45° gable (apex at y = 30√2 = 42.43) for the print; a lower window
  R 25.0 centred at (0, −95.0) with the same 45° gable (apex y −59.64) for TUBE 7 and
  for a hand (A-07). A foot plate 4.0 thick, y −150.0 … −146.0, x ±50, from the
  wall's front face z −24.94 back to z −69.94, with four Ø3.4 through-holes along Y
  at (x ±35.0, z −40.0) and (x ±35.0, z −60.0) for M3 screws into OD-C01 inserts
  (A-04). Two gussets 4.0 thick at x ±46 … ±50 tie the wall's rear face to the foot:
  right triangles with legs of 40 (from z −29.94 to −69.94 on the foot, from
  y −146.0 to −106.0 on the wall), hypotenuse at 45°. Nothing of the carrier lies at
  z < −69.94 (REQ-07): the thermoblock zone begins at z −85 (A-05). Print
  orientation: foot on the bed (−Y down), wall vertical, the windows' 45° gables and
  the gussets' 45° faces need no support, the eight holes are horizontal or vertical
  (A-13). Envelope 100.0 × 200.0 × 45.0 (x ±50, y −150 … +50, z −69.94 … −24.94).
- **C2 — cantilever arms from OD-C01 with the housing hanging on studs.** Deferred:
  needs the OD-C01 layout first; more material, less stiff.
- **C3 — the wall doubles as the wet/electric bulkhead OD-C02.** Deferred until
  OD-C01 and the tube runs exist (chassis order of work rows 7 and 8).

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 100.0 × 200.0 × 45.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±50.0, y −150.0 … +50.0, z −69.94 … −24.94) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) carrier|OD-G01 (build v02) at the identity pose: the wall's front face on the housing's rear face is the designed contact, `clearance = 0`, `interference ≤ 0` mm³; the four carrier holes coaxial with the housing's insert bores (REQ-01); carrier|OD-G04 as the OD-G01 REPORT places it (its plate back face at housing z −6.82, clocked +6.05°, INTAKE X-35): `clearance ≥ 2.0`, the nearest points reported. (b) N/A: no motion variable | Hard | CAD | house | `clearance`, `interference`, `locate_bore` on both solids | A-01, A-06 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 wall, 1 foot, 2 gussets, 2 windows, 4 Ø3.4 through-holes along Z with 4 Ø6.5 counterbores, 4 Ø3.4 through-holes along Y | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/6.0) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default; the carrier holds the group head) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the K1C build volume, foot down: 100.0 × 45.0 on the bed, 200.0 tall | Hard | part | machine | `envelope` | A-08 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (foot on the bed, build direction +Y): the window gables and the gusset hypotenuses at 45°; nothing supported | Hard | part | floor | `overhang_census(build_dir=(0,1,0))`; reviewer from sections | A-13 |
| D-03b | Unsupported bridge | span ≤ 5 (the counterbores and holes along Z are Ø6.5 and Ø3.4 horizontal bores: their crowns are the only bridges, ≤ 6.5 by construction and accepted as a named exception below) | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | all eight Ø3.4 holes Ø ≥ 3.25 | Hard | part | house | `locate_bore` | — |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | the holes are clearance holes, not fit bores: none on this part | Hard | part | floor | — (N/A by this row) | — |
| E-06 | Boss support | the wall is tied to the foot by the two gussets; no free-standing boss | Hard | part | struct | reviewer | — |
| REQ-01 | Housing holes | four Ø3.4 ± 0.1 through-holes along Z at (x ±44.0, y ±44.0), offset ≤ 0.10 from the housing's insert bores measured on the OD-G01 STEP in the check assembly | Hard | CAD | A-01 | `locate_bore` on both solids | A-01 |
| REQ-02 | Counterbores | four Ø6.5 ± 0.1 counterbores 2.0 ± 0.1 deep from the rear face z −29.94, coaxial with REQ-01 | Hard | CAD | A-09 | `bore_census`, `locate_bore`; reviewer from sections | A-09 |
| REQ-03 | Wall faces | the wall's front face at z = −24.94 ± 0.10 (`envelope` max_z), its rear face at z = −29.94 ± 0.10 | Hard | CAD | A-01 | `envelope`; reviewer from sections | A-01 |
| REQ-04 | Hub window | no carrier material within r ≤ 30.0 of the axis over z −29.94 … −24.94 at every 10° (`radial_extent` INCONCLUSIVE "no material" is the expected reading, recorded as such; positive control on the whole ray: first material at θ 90° is the gable apex at r 42.43); roof at 45° (D-03a) | Hard | CAD | A-06 | `radial_extent`; reviewer from sections | A-06 |
| REQ-05 | Foot plane | the foot's underside at y = −150.00 ± 0.10 (`envelope` min_y), 4.0 ± 0.1 thick | Hard | CAD | A-03, A-04 | `envelope`; reviewer from sections | A-03, A-04 |
| REQ-06 | Frame holes | four Ø3.4 ± 0.1 through-holes along Y at (x ±35.0, z −40.0) and (x ±35.0, z −60.0), offset ≤ 0.10 | Hard | CAD | A-04 | `locate_bore` | A-04 |
| REQ-07 | Thermoblock keep-out | no carrier material at z < −70.0 (`envelope` min_z ≥ −70.0); the thermoblock zone begins at z −85 (A-05), so every printed surface keeps ≥ 10 mm of air to it by construction | Hard | CAD | client (INTAKE X-64, X-65) | `envelope` | A-05 |
| REQ-08 | Lower window | an opening through the wall containing the circle R 25.0 about (0, −95.0) and nothing else of the wall missing below y −50 (`radial_extent` about (0, −95.0, z) over r ≤ 25 reads "no material" at every 10°); roof at 45° | Hard | CAD | A-07 | `radial_extent`; reviewer from sections | A-07 |
| REQ-09 | Stiffness | **Soft.** The carrier holds the group head without visible flex under the user's locking torque and the brewing pull; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, and it is answered by the first print | Soft | part | client | — (bench) | A-11 |

**Named exceptions** (Usta U-18): D-03b for the crowns of the horizontal Ø3.4 holes and Ø6.5 counterbores through the wall (bridges ≤ 6.5 over ≤ 5.0 of depth), the usual FDM practice for small horizontal holes; recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-G01 rear flange | the build v02 STEP: slab 5.00 thick, z −24.94 … −19.94, 100 × 100 square with R 8 corners, rear face z −24.94, four insert bores Ø4.0 × 5.7 at (±44, ±44), Ø26 hub opening on the axis, pair-B screw heads on the rear face at r 19.03; the OD-G01 job is at its third round with this geometry unchanged, and its A-18 note "flange 100 × 100 × 4" is stale (built and measured 5.00, INTAKE §4 gap 1) | the carrier does not fit the delivered housing | INTAKE X-01 … X-26 | OD-G01's final approved build; calipers on the print | OPEN |
| A-02 | Machine up direction | +Y of the housing frame points up in the machine; the housing's clocking about its axis is otherwise free (its features are three-fold or on the axis) | the wall or the windows sit at the wrong clock; OD-C01 must agree | this spec (P4); OD-G01 spec §2 (+Z faces the user) | the Usta's layout decision for OD-C01 | OPEN |
| A-03 | Group head height | the axis 150.0 above the base frame's floor plane (y = −150.0 in this frame), so the housing's lowest point (y −43.1) is 106.9 above the floor and INTAKE X-66's ≥ 95 holds while the tray's top stands ≤ 11.9 above the floor; the tray is not scanned (INTAKE X-67, §4 gap 3) | mug does not fit; OD-C01 must lower or raise the whole carrier | this spec; SOURCING_GUIDE §6 rule 5 (INTAKE X-66) | the drip tray's scan or calipers; OD-C01's layout | OPEN |
| A-04 | OD-C01 interface | four M3 inserts on a 70.0 × 20.0 pattern (x ±35.0, z −40.0 and −60.0 in this frame); the foot underside is the frame's floor plane, the same plane OD-C03 and OD-C04 stand on | OD-C01 must be designed to it | this spec (design choice, OD-C03 and OD-C04 precedent, INTAKE X-63) | OD-C01 design | OPEN |
| A-05 | Thermoblock zone | OD-H11 with its mount OD-C04 stays at z ≤ −85.0 in this frame (behind the foot's rear edge by ≥ 15), so no printed surface of the carrier is within 10 mm of the casting; the thermoblock's own axis height and offset are OD-C01's to fix (INTAKE §4 gap 2) | the ≥ 10 mm air gap breaks; the carrier must be shortened or moved | this spec; INTAKE X-64, X-65; OD-C04 spec A-07 | OD-C01's layout | OPEN |
| A-06 | Water connection behind the hub | the OEM connection parts OD-G07 / OD-H14 / OD-H15 and the OD-G04 hub tube (bottom at housing z −22.55, OD 20.06, INTAKE X-36) fit within r ≤ 30 of the axis behind the housing; they are not scanned | the connection fouls the window's edge | this spec; OD-G01 spec A-24; INTAKE §4 gap 10 | calipers on the connection parts | OPEN |
| A-07 | TUBE 7 and access | the hot water tube (TUBE 7, ≈ Ø8 silicone, INTAKE X-77, X-78) and OD-H23 pass through or beside the lower window R 25 at (0, −95); the window also gives a hand access to the screws and the connection | tube route blocked; OD-C02 must route around | this spec; INTAKE §4 gap 4 | the tube run in OD-C01 / OD-C02 | OPEN |
| A-08 | K1C build volume | 220 × 220 × 250 (Creality specification, not in the machine file); the part stands 200 tall | part does not fit | memory of the spec sheet (as OD-C04 A-09) | the Usta reads the printer | OPEN |
| A-09 | Screw and engagement | M3 × 8 (OD-F02, ISO 7380 button head Ø5.7 or DIN 912 head Ø5.5) through 3.0 of wall under a Ø6.5 × 2.0 counterbore, reaching 5.0 into the housing's 5.7 insert (OD-G01 A-17); the screw is driven from behind the wall | too short or too long a screw; the head fouls the counterbore | this spec; INTAKE X-12, X-13, X-76 | the Usta's stocked screws | OPEN |
| A-10 | Scan fidelity of the neighbours | OD-G04's deviation gate BAND_NOT_MET (p95 0.376, INTAKE X-39) and OD-H11's PARTIAL (p95 0.474, X-51); no calipers | the r ≤ 30 window and the thermoblock zone are off by the scan error | INTAKE X-39, X-40, X-51, X-52, §4 gaps 8, 9 | calipers | OPEN |
| A-11 | Loads | the housing ≈ 97 g plus the portafilter and gasket stack, the user's locking torque (tens of N·m at the lugs, reacted through the four screws as a couple across 88 mm), the water connection's pull; strength not calculated; the wall 5.0 with two gussets | the wall flexes or cracks at the screws | this spec; INTAKE X-24, X-25 | the first print (REQ-09) | OPEN |
| A-12 | Material | ASA, density 1070 kg/m³, printed on the K1C | carrier softens near the hot tube | BOM OD-C05 (INTAKE X-60); SOURCING_GUIDE §6 rule 3 (X-70) | the Usta names the filament | OPEN |
| A-13 | Print orientation | foot on the bed, wall vertical, no supports; the windows' gables at 45° | gable sag; the tall thin wall warps | this spec | first print | OPEN |
| A-14 | Serviceability | the housing is removed forward after the four screws are driven out from behind the wall, reached through the removable back panel and the lower window; the gaskets are changed with the housing off the carrier | the screws cannot be reached in the assembled machine | this spec; SOURCING_GUIDE §6 rule 4 (INTAKE X-71) | the OD-C00 assembly | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC on the Usta's "go" after OD-C03 and OD-C04; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and "go" of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | the OD-G01 blocker (chassis order-of-work row 2) is lifted on the Usta's "go": the housing's rear flange is unchanged since OD-G01 spec 1.2 and the build v02 STEP is the reference; the job is reopened if OD-G01's final build changes the flange | Oğuz on the Usta's "go" | REQUEST.md |
| 2026-09-30 | INTAKE §4 gap 1 (OD-G01 A-18 says flange × 4, built 5.00): the built and measured value governs (A-01) | Oğuz | INTAKE_v01 §4 |
| 2026-09-30 | REQ-09 (stiffness) is a Soft bench gate answered by the first print (the OD-C03 RV01 lesson) | Oğuz | §5 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the OD-G01 spec 1.3 and REPORT v02, the OD-G04 and OD-H11 reports |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6; ratified |
