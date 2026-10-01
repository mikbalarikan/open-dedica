# DESIGN_SPEC — OD-C05 printed group head carrier (20260930-od-c05-group-head-carrier)

Version 2.2 · RATIFIED by the Usta on 2026-09-30 (standing instruction of 2026-09-30 and the "confirmed go" / "go" of the same day: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-C05 is the 3D-printed group head carrier of the Open Dedica espresso machine: the
bracket that holds the printed group head housing OD-G01 by the four M3 heat-set
inserts in its rear flange, keeps the space behind the housing open for the OD-G04
hub tube, the OEM water connection and the hot water tube (TUBE 7), holds the group
head with its axis vertical and its mouth down, high enough for a mug under the
portafilter spouts (≥ 95 mm above the drip tray, INTAKE X-66), and bolts to the
printed base frame OD-C01. Done means: one valid printable solid with a flat
horizontal plate whose underside seats on the housing's rear face, four screw holes
on the housing's insert pattern, a wall behind the housing standing on a foot with
a screw pattern for OD-C01, a window over the hub, nothing closer than 10 mm to the
thermoblock zone, and every unconfirmed value in §6. (2.0: RV01 F1 found spec 1.x's
frame, taken from the OD-G01 spec §2, hung the group head on its side.) The drip tray OD-C21, the tube TUBE 7 with
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
(OD-G01 spec §2): Z is the group head axis, +Z points toward the mouth, z = 0 is
the plane of the housing's lug top pads, the housing's rear face is the plane
z = −24.94 (INTAKE X-07), the origin is on the axis, θ counter-clockwise about +Z
from +X. In the machine **the axis is vertical: +Z points down** (the mouth and the
portafilter face the drip tray), **−Z is up**, +Y points toward the user (the
front) and +X to the user's right (A-02; the OD-G01 spec §2 sentence "+Z is
horizontal and faces the user" is wrong, RV01 F1). The carrier's plate lies on the
housing's rear face (now its top), and its wall stands behind the housing on the
base frame's floor plane z = +180.06 (A-03). In the OD-C01 machine frame (X right,
+Y up, +Z front) the housing frame maps by x → X, y → +Z, z → −Y with the origin at
(0, 180.06, 32.0) (OD-C01 spec A-01). Every artifact of this job uses the housing
frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c05_carrier | FDM | machines/creality-k1c.toml (enclosed; build volume UNKNOWN → A-08) | ASA (BOM: ASA) | 1070 | as printed | A-12 |

Environment: inside the machine, above and behind the group head; hot water tube and the OEM
water connection above the housing (≈ 100 °C), drips and steam possible; the
thermoblock is at least 10 mm away (A-05). Loads: the housing (≈ 97 g, INTAKE X-25)
with the portafilter and the brewing gasket stack, the user's locking torque on the
portafilter, and the pull of the water connection; the brew load itself (INTAKE
X-24) is reacted inside the housing between lugs and gasket, not by the carrier.

## §4 Architecture and concepts

- **C4 — horizontal plate over the housing on a closed column behind it (CHOSEN in
  2.0, column in 2.1).** One solid, printed with the plate on the bed. A **plate**
  5.0 thick along Z, z −29.94 … −24.94, whose underside (z −24.94) is the plane of
  the housing's rear face (a designed contact, A-01), spanning x ±55.0 and
  y −102.0 … +50.0 (the housing's outline x ±50, y ±50 lies under its front part;
  its rear part is the column's lid), square corners. Through the plate along Z:
  four Ø3.4 holes at (x ±44.0, y ±44.0), coaxial with the housing's insert bores
  (INTAKE X-10, X-11), each with a counterbore Ø6.5 × 2.0 from the top face
  (z −29.94) so an M3 × 8 screw driven from above leaves 3.0 of plate under its
  head and reaches 5.0 into the 5.7 insert (A-09); a **hub window** R 30.0 about
  the axis (a Ø60 opening over the housing's Ø26 hub opening, the OD-G04 hub tube
  and the two OEM pair-B screw heads at r 19.03, INTAKE X-19, X-36; the water
  connection above the hub gets r ≤ 30, A-06); a **hatch** 80.0 × 32.0 (x ±40.0,
  y −96.0 … −64.0, corners R 4.0) over the column for the foot screws' driver and
  the hot water tube (A-07, A-14). A **column** below the plate's rear part, a
  rectangular tube open at the top (the hatch) from z −29.94 down to the floor
  z +180.06 (210.0 tall): the **front wall** 6.0 thick, y −58.0 … −52.0 (2.0 of air
  behind the housing's rear side y −50), x ±55.0; two **side walls** 4.0 thick at
  |x| 51.0 … 55.0, y −102.0 … −58.0; the **rear wall** 4.0 thick, y −102.0 … −98.0,
  x ±55.0; a **rear window** 20.0 wide (x ±10.0) through the rear wall, z +110.0 …
  +140.0 with a 45° gable toward +Z (the print's up; apex z +150.0) for the hot
  water tube (A-07; machine y 40 … 70, beside the thermoblock's outlet).
  The column's bottom is the **foot**: its underside the floor plane z +180.06,
  x ±55.0, y −102.0 … −58.0; its inside is a 45° gable roof (two faces from z +154.06 at
  the front and rear walls' inner faces, y −58 and y −98, rising in the print to a
  ridge along X at y −78.0, z +174.06), so the foot is 26.0 thick at the walls and
  6.0 at the ridge and prints without a ceiling or a bridge (A-13; 2.2: spec 2.1
  had the roof upside down for the print, v03 K-6); four Ø3.4 through-holes along Z at (x ±35.0, y −72.0) and
  (x ±35.0, y −92.0) for M3 screws into OD-C01 inserts (A-04; in the machine frame
  (±35, z −40) and (±35, z −60), the pattern of spec 1.x), each with a Ø6.5
  counterbore from the roof face down to 4.0 above the underside (their floors at
  z +176.06: the roof at y −72 is at z 168.06, so 8.0 deep; at y −92, z 160.06,
  16.0 deep) so the screw heads bear on 4.0 of foot. Two **gussets**
  4.0 thick at |x| 51.0 … 55.0 under the plate in front of the column, right
  triangles with 40.0 legs (from y −52.0 to −12.0 along the plate's underside and
  from z −24.94 to +15.06 down the front wall; their inner faces at |x| 51 clear
  the housing's sides at |x| 50 by 1.0). Nothing of the carrier lies at y < −102.0
  (REQ-07): the thermoblock zone begins at machine z −85, housing y −117 (A-05).
  The closed column answers RV01 F2 and the v02 REPORT §9: the locking torque about
  the vertical axis twists an open 6 × 110 wall by degrees, a closed 110 × 44 tube
  by a fraction of a degree (A-11). Print orientation (A-13): **plate on the bed**
  (the plate's top face z −29.94 down), build direction +Z (the machine's down):
  the walls, gussets, hatch and windows are vertical prisms; the roof faces and the
  rear window's gable are at 45°; the eight counterbore floors (four on the plate,
  four in the foot's roof) are the only downward faces, rings bridging ≤ 6.6 over a
  Ø3.4 hole, the named exception of §5. Envelope 110.0 × 152.0 × 210.0 (x ±55,
  y −102 … +50, z −29.94 … +180.06); on the bed 110 × 152, 210 tall.
- **C1 — vertical wall on a foot, two gussets, two windows (spec 1.0 … 1.2, built
  as v01, REVISE RV01 F1).** Built to a frame with the axis horizontal; sound as a
  part, wrong for the machine. Superseded by C4.
- **C2 — cantilever arms from OD-C01 with the housing hanging on studs.** Deferred:
  more material, less stiff.
- **C3 — the wall doubles as the wet/electric bulkhead OD-C02.** Deferred until
  OD-C01 and the tube runs exist (chassis order of work rows 7 and 8).

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 110.0 × 152.0 × 210.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±55.0, y −102.0 … +50.0, z −29.94 … +180.06) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) carrier|OD-G01 (build v02) at the identity pose: the plate's underside on the housing's rear face is the designed contact, the housing's sides ≥ 1.0 from the gussets and 2.0 from the front wall, `clearance = 0`, `interference ≤ 0` mm³; the four carrier holes coaxial with the housing's insert bores (REQ-01); carrier|OD-G04 as the OD-G01 REPORT places it (its plate back face at housing z −6.82, clocked +6.05°, INTAKE X-35): `clearance ≥ 2.0`, the nearest points reported. (b) N/A: no motion variable | Hard | CAD | house | `clearance`, `interference`, `locate_bore` on both solids | A-01, A-06 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 plate with 1 hub window and 1 hatch, 1 column (front, two side and rear walls, one rear window), 1 roofed foot, 2 gussets, 4 Ø3.4 through-holes along Z with 4 Ø6.5 counterbores in the plate, 4 Ø3.4 through-holes along Z with 4 Ø6.5 counterbores in the foot | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/6.0) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default; the carrier holds the group head) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the K1C build volume, plate down: 110.0 × 152.0 on the bed, 210.0 tall | Hard | part | machine | `envelope` | A-08 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (plate on the bed, build direction +Z): the foot's roof faces and the rear window's gable at 45°, both pointing +Z; nothing supported; the eight counterbore floors (rings between Ø6.5 and Ø3.4, four on the plate at z −27.94, four in the foot's roof at z +176.06) are the named exception below, excluded from the census by position and their least angle reported | Hard | part | floor | `overhang_census(build_dir=(0,0,1))`; reviewer from sections | A-13 |
| D-03b | Unsupported bridge | span ≤ 5 (the eight counterbore floors bridge the Ø6.5 ± 0.1 counterbore below them, ≤ 6.6 by construction, accepted as a named exception below; the hatch, the windows and the roof have no bridge (the roof's ridge is its highest line in the print, v03 K-7)) | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | all eight Ø3.4 holes Ø ≥ 3.25 | Hard | part | house | `locate_bore` | — |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | the holes are clearance holes, not fit bores: none on this part | Hard | part | floor | — (N/A by this row) | — |
| E-06 | Boss support | the plate is tied to the column's front wall by the two gussets and to the column by its lid part; no free-standing boss | Hard | part | struct | reviewer | — |
| REQ-01 | Housing holes | four Ø3.4 ± 0.1 through-holes along Z at (x ±44.0, y ±44.0), offset ≤ 0.10 from the housing's insert bores measured on the OD-G01 STEP in the check assembly | Hard | CAD | A-01 | `locate_bore` on both solids | A-01 |
| REQ-02 | Counterbores | four Ø6.5 ± 0.1 counterbores 2.0 ± 0.1 deep from the plate's top face z −29.94, coaxial with REQ-01 | Hard | CAD | A-09 | `bore_census`, `locate_bore`; reviewer from sections | A-09 |
| REQ-03 | Plate faces | the plate's underside at z = −24.94 ± 0.10 (the counterbore start z −29.94 plus the hole length 3.0; the contact plane of U-03), its top face at z = −29.94 ± 0.10 (`envelope` min_z) | Hard | CAD | A-01 | `envelope`; reviewer from sections | A-01 |
| REQ-04 | Hub window | the innermost carrier material over z −29.94 … −24.94 at every 10° is at r ≥ 30.0 (`radial_extent` over the whole ray, RV01 F4; round, r 30.0 at every angle; no gable, the window is vertical in the print) | Hard | CAD | A-06 | `radial_extent`; reviewer from sections | A-06 |
| REQ-05 | Foot plane | the foot's underside at z = +180.06 ± 0.10 (`envelope` max_z); 4.0 ± 0.1 of foot under each screw head (the foot counterbore floor at z +176.06 ± 0.10) | Hard | CAD | A-03, A-04 | `envelope`; reviewer from sections | A-03, A-04 |
| REQ-06 | Frame holes | four Ø3.4 ± 0.1 through-holes along Z through the foot at (x ±35.0, y −72.0) and (x ±35.0, y −92.0), offset ≤ 0.10, each with a Ø6.5 ± 0.1 counterbore from the roof face whose floor is at z +176.06 ± 0.10 | Hard | CAD | A-04 | `locate_bore` | A-04 |
| REQ-07 | Thermoblock keep-out | no carrier material at y < −102.0 (`envelope` min_y ≥ −102.0); the thermoblock zone begins at machine z −85, housing y −117 (A-05), so every printed surface keeps ≥ 10 mm of air to it by construction | Hard | CAD | client (INTAKE X-64, X-65) | `envelope` | A-05 |
| REQ-08 | Housing clearance | the housing's side faces (x ±50, y ±50) to the gussets ≥ 1.0 and to the front wall ≥ 2.0 (`clearance` of the housing against the carrier less the plate's underside contact: nearest points reported off the plane z −24.94) | Hard | CAD | A-01 | `clearance`; reviewer from sections | A-01 |
| REQ-09 | Stiffness | **Soft.** The carrier holds the group head without visible flex under the user's locking torque, the handle's sideways push and the brewing pull (the plate cantilevers 96 mm from the front wall to the front screws, RV01 F2; the column is closed against torsion, v02 REPORT §9); not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, and it is answered by the first print | Soft | part | client | — (bench) | A-11 |

**Named exceptions** (Usta U-18): D-03a and D-03b for the eight counterbore floors (four on the plate's top face, four in the foot's tent): rings 1.55 wide at 0° bridging the Ø6.5 ± 0.1 counterbore below them (≤ 6.6, REQ-02's upper tolerance), the usual FDM practice for a counterbore printed head-down; recorded here for the Usta to confirm with §5 (1.1 extended the exception to D-03a, plan K-2; 2.1 moved it from hole crowns to counterbore floors with the print orientation).

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-G01 rear flange | the build v02 STEP: slab 5.00 thick, z −24.94 … −19.94, 100 × 100 square with R 8 corners, rear face z −24.94, four insert bores Ø4.0 × 5.7 at (±44, ±44), Ø26 hub opening on the axis, pair-B screw heads on the rear face at r 19.03; the OD-G01 job is at its third round with this geometry unchanged, and its A-18 note "flange 100 × 100 × 4" is stale (built and measured 5.00, INTAKE §4 gap 1) | the carrier does not fit the delivered housing | INTAKE X-01 … X-26 | OD-G01's final approved build; calipers on the print | OPEN |
| A-02 | Machine up direction | the group head axis is vertical, −Z of the housing frame up and the mouth down, as in the Dedica; +Y toward the user; the housing's clocking about its axis is otherwise free (its features are three-fold or on the axis) | the carrier and the OD-C01 layout are wrong | RV01 F1 (P1, P5); this spec 2.0; put to the Usta as a decision card 2026-09-30 | the Usta's answer | OPEN |
| A-03 | Group head height | the housing's rear face (the plate's underside) 205.0 above the base frame's floor (floor at z +180.06 in this frame), the mouth face at 176.76; the portafilter OD-G10 reaches 59.0 below its rim (`step/OD-G10_portafilter.step`, measured), so with the rim on the housing's shelf (z −14.1) its spouts hang to housing z ≈ 44.9, 135.2 above the floor: INTAKE X-66's ≥ 95 holds (98.3) while the tray's top stands ≤ 36.9 above the floor; the tray is not scanned (INTAKE X-67, §4 gap 3) | mug does not fit; OD-C01 must lower or raise the whole carrier | this spec 2.0; RV01 F1 fix direction; SOURCING_GUIDE §6 rule 5 (INTAKE X-66) | the drip tray's scan or calipers; the Usta's layout confirmation | OPEN |
| A-04 | OD-C01 interface | four M3 inserts on a 70.0 × 20.0 pattern (x ±35.0, y −72.0 and −92.0 in this frame; machine (±35, z −40) and (±35, z −60), unchanged from spec 1.x); the foot underside is the frame's floor plane, the same plane OD-C03 and OD-C04 stand on | OD-C01 must be designed to it | this spec (design choice, OD-C03 and OD-C04 precedent, INTAKE X-63) | OD-C01 design | OPEN |
| A-05 | Thermoblock zone | OD-H11 with its mount OD-C04 stays at machine z ≤ −85.0 (housing y ≤ −117, behind the foot's rear edge y −102 by ≥ 15) and below the plate (OD-C01 spec A-02: the casting's top well under machine y 205), so no printed surface of the carrier is within 10 mm of the casting | the ≥ 10 mm air gap breaks; the carrier must be shortened or moved | this spec; INTAKE X-64, X-65; OD-C04 spec A-07 | OD-C01's layout | OPEN |
| A-06 | Water connection above the hub | the OEM connection parts OD-G07 / OD-H14 / OD-H15 and the OD-G04 hub tube (top at housing z −22.55, OD 20.06, INTAKE X-36) fit within r ≤ 30 of the axis above the housing, through the plate's window; they are not scanned | the connection fouls the window's edge | this spec; OD-G01 spec A-24; INTAKE §4 gap 10 | calipers on the connection parts | OPEN |
| A-07 | TUBE 7 route | the hot water tube (TUBE 7, ≈ Ø8 silicone, INTAKE X-77, X-78) enters the column through the rear window (x ±10, z +110 … +140, machine y 40 … 70, beside the thermoblock's outlet at machine y ≈ 56), rises inside the column, leaves through the hatch and enters the hub window from above; the four housing screws are reached from above | the tube's bend radius does not fit the window or the column; OD-C02 must route around | this spec; INTAKE §4 gap 4 | the tube run in OD-C01 / OD-C02 | OPEN |
| A-08 | K1C build volume | 220 × 220 × 250 (Creality specification, not in the machine file); the part stands 110 × 152 on the bed, 210 tall | part does not fit | memory of the spec sheet (as OD-C04 A-09) | the Usta reads the printer | OPEN |
| A-09 | Screw and engagement | M3 × 8 (OD-F02, ISO 7380 button head Ø5.7 or DIN 912 head Ø5.5) through 3.0 of plate under a Ø6.5 × 2.0 counterbore, reaching 5.0 into the housing's 5.7 insert (OD-G01 A-17); the screw is driven from above | too short or too long a screw; the head fouls the counterbore | this spec; INTAKE X-12, X-13, X-76 | the Usta's stocked screws | OPEN |
| A-10 | Scan fidelity of the neighbours | OD-G04's deviation gate BAND_NOT_MET (p95 0.376, INTAKE X-39) and OD-H11's PARTIAL (p95 0.474, X-51); no calipers | the r ≤ 30 window and the thermoblock zone are off by the scan error | INTAKE X-39, X-40, X-51, X-52, §4 gaps 8, 9 | calipers | OPEN |
| A-11 | Loads | the housing ≈ 97 g plus the portafilter and gasket stack, the user's locking torque about the vertical axis (tens of N·m at the lugs, reacted through the four screws as a couple across 88 mm, in the plate's plane), the handle's sideways push, the water connection's pull; hand estimates only: an open 6 × 110 wall 210 tall twists ≈ 0.3 rad under 10 N·m (J ≈ 7900 mm⁴, G ≈ 0.8 GPa; the v02 REPORT §9 read ≈ 5° under a 50 N push), the closed 110 × 44 column (J ≈ 1e6 mm⁴) ≈ 0.002 rad; the plate 5.0 cantilevers 96 to the front screws (RV01 F2) | the plate or the column flexes or cracks at the screws | this spec; INTAKE X-24, X-25 | the first print (REQ-09) | OPEN |
| A-12 | Material | ASA, density 1070 kg/m³, printed on the K1C | carrier softens near the hot tube | BOM OD-C05 (INTAKE X-60); SOURCING_GUIDE §6 rule 3 (X-70) | the Usta names the filament | OPEN |
| A-13 | Print orientation | plate's top face on the bed, build direction +Z (machine down), no supports; walls, gussets, hatch and windows vertical; the foot's roof and the rear window's gable at 45°, ridges up; the eight counterbore floors (named exception) | the tall column warps or the plate lifts off the bed | this spec | first print | OPEN |
| A-14 | Serviceability | the housing is removed downward after the four screws are driven out from above, reached through the removable top panel; the four foot screws are driven through the hatch with a long M3 driver (≈ 200 reach); the gaskets are changed with the housing off the carrier | the screws cannot be reached in the assembled machine | this spec; SOURCING_GUIDE §6 rule 4 (INTAKE X-71) | the OD-C00 assembly | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC on the Usta's "go" after OD-C03 and OD-C04; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and "go" of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | the OD-G01 blocker (chassis order-of-work row 2) is lifted on the Usta's "go": the housing's rear flange is unchanged since OD-G01 spec 1.2 and the build v02 STEP is the reference; the job is reopened if OD-G01's final build changes the flange | Oğuz on the Usta's "go" | REQUEST.md |
| 2026-09-30 | INTAKE §4 gap 1 (OD-G01 A-18 says flange × 4, built 5.00): the built and measured value governs (A-01) | Oğuz | INTAKE_v01 §4 |
| 2026-09-30 | REQ-09 (stiffness) is a Soft bench gate answered by the first print (the OD-C03 RV01 lesson) | Oğuz | §5 |
| 2026-09-30 | the group head axis goes to 175 above the floor (OD-C01 spec 1.0 §7, A-01) so a tray up to 36.9 tall fits under the ≥ 95 mm mug rule: wall and foot lengthen by 25, the lower window moves to (0, −110) to stay between the hub window and the gussets | Oğuz, on the OD-C01 layout | OD-C01 spec 1.0; A-03 |
| 2026-09-30 | plan K-1: the top corners become R 6.0 about (±44, 44) (web to the Ø6.5 counterbore 2.75 ≥ D-01b's 2.0); the counterbore and screw stay as A-09 | Oğuz (option 2 of the plan, on the standing instruction) | 01_CAD/DESIGN_PLAN.md §8 |
| 2026-09-30 | RV01 F1 (P1, P5): the machine frame of spec 1.x, taken from the OD-G01 spec §2, hung the group head on its side; another round with concept C4 (vertical axis, mouth down, a plate over the housing on a wall behind it), the up direction put to the Usta as a decision card; the OD-C01 joint pattern (±35, z −40 / −60) is kept so OD-C01's holes stand | Oğuz (REVISE packet option A, on the standing instruction) | reviews/REVISE_PACKET_RV01.md; A-02, A-03 |
| 2026-09-30 | v02 K-3 (gusset ceilings in the side print) and K-4 (R 6 corner overhang) and REPORT §9 (≈ 5° wall flex): concept option 3 taken, a closed column in place of the wall and rear gussets, plate on the bed; corners squared | Oğuz (v02 REPORT §8 option 3, on the standing instruction) | 01_CAD/REPORT_od_c05_carrier_v02.md; A-11, A-13 |
| 2026-09-30 | v03 K-6, K-7: spec 2.1 drew the foot's roof and the window's gable upside down for the plate-on-bed print (a flat 20 ceiling, a 102 bridge at the ridge); 2.2 turns both; the build cap (2) was reached by these spec errors, another round ordered on the standing instruction | Oğuz | 01_CAD/REPORT_od_c05_carrier_v03.md §10; usta_gate halt_decision |
| 2026-09-30 | plan K-2: the named exception of §5 extends to D-03a for the crowns of the eight horizontal holes and counterbores; the holes stay round | Oğuz (option 1 of the plan, on the standing instruction); the Usta confirms with §5 | 01_CAD/DESIGN_PLAN.md §8 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the OD-G01 spec 1.3 and REPORT v02, the OD-G04 and OD-H11 reports |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6; ratified |
| 2.2 | 2026-09-30 | v03 K-6, K-7: the foot's roof turned the right way up for the print (faces from z +154.06 at the walls to the ridge at y −78, z +174.06; counterbores 8.0 / 16.0 deep), the rear window moved to z +110 … +140 with its gable toward +Z (apex +150); no other change |
| 2.1 | 2026-09-30 | v02 REPORT K-3, K-4 and §9: the side-print gussets were ceilings and the open wall twists; the wall becomes a closed column (front 6, sides and rear 4) with a tented foot, a hatch in the plate's lid part, a rear window for the tube; the plate's corners square; print with the plate on the bed, build +Z; the named exception moves to the eight counterbore floors; foot counterbores in REQ-05, REQ-06; A-07, A-11, A-13, A-14 rewritten; D-03a's check column build_dir corrected |
| 2.0 | 2026-09-30 | RV01 F1: vertical axis (§2, A-02); concept C4 (§4): plate 110 × 108 × 5 over the housing with the hub window (gable toward +X), wall 6.0 behind it 210 tall, foot y −58 … −102 with the same OD-C01 pattern, four gussets; the lower window dropped; U-02, U-03, U-05, D-02, D-03a/b, REQ-02 … REQ-09 rewritten; A-02 … A-07, A-09, A-11, A-13, A-14 rewritten; height 205 from the portafilter spouts (A-03); the named exception covers twelve bores; spec 1.2 kept as `DESIGN_SPEC_v1.2.md` |
| 1.2 | 2026-09-30 | the named exception's bridge limit reads ≤ 6.6 (REQ-02's upper tolerance) instead of ≤ 6.5, found by the build v01 sweep (REPORT §9 item 2); no geometry change |
| 1.1 | 2026-09-30 | axis 175 (OD-C01 layout): wall y −175 … +50, foot y −175 … −171, gussets to y −131, lower window at (0, −110), envelope 100 × 225 × 45 (§2, §4, U-02, D-02, REQ-05, REQ-08, A-03, A-07, A-08); plan K-1: top corners R 6 about (±44, 44); plan K-2: named exception extended to D-03a (§4, §5) |
