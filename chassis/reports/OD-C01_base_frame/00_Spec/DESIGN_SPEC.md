# DESIGN_SPEC — OD-C01 printed base frame (20260930-od-c01-base-frame)

Version 1.3 · RATIFIED by the Usta on 2026-10-05 ("continue now", answering the base-plate card on its recommended option) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C01 is the 3D-printed base frame of the Open Dedica espresso machine: the floor
plate every printed mount stands on and screws into. It fixes the machine layout
(§4, A-01 … A-06): the group head carrier OD-C05 at the front, the thermoblock mount
OD-C04 behind it, the pump cradle OD-C03 across the back, the drip tray in front
under the group head, the water tank at the rear, the valve and flowmeter mount on
the left, the electronics bay on the right behind the bulkhead OD-C02. Done means:
one valid printable plate with a flat top face (the floor plane every mount's spec
names), M3 heat-set insert holes under the three existing mounts' foot holes and
along the bulkhead line, screw holes for four feet, two drain holes in the wet zone,
reserved zones for the parts not yet designed, and every unconfirmed value in §6.
The drip tray OD-C21/C22 and the tank OD-W01 are not scanned, the tank dock OD-C06
is deferred (the tank stands on the table, the Usta 2026-10-02): their zones are
assumptions. OD-C07, OD-C08, OD-C10, OD-C11 and OD-C15 are delivered; 1.3 adds the
eighteen inserts OD-C08, OD-C11, the side-panel brackets OD-C16 and the front
panel OD-C09 screw into (REQ-11 … REQ-14).

**Deliverables** (tier M): STEP AP242 of the plate; the check assembly STEP (plate +
OD-C03 with OD-H01 + OD-C04 with OD-H11 + OD-G01 v02 at the carrier's pose, each by
its joint of §4); STL and 3MF; build and check scripts; REPORT; sections. No
drawings or renders.

**Out of scope:** the other parts themselves, the tray, tank, dock, side and front
panels, the tube runs, calipers. Revision B (1.3) changes only the insert holes and
the material; every other feature of build v02 stands.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| OD-C03 pump cradle (delivered) | `00_Spec/inputs/OD-C03_pump_cradle.step` (INTAKE §1 #1): foot underside its y = +40.0 (+Y down), holes Ø3.4 at (x ±34.0, z −4.0 / 37.0) in its frame | — | OD-C03 spec 1.2 §4, REQ-07, REQ-08, A-11 (INTAKE X-01 … X-06) | CONFIRMED as the input; A-03 places it |
| OD-C04 thermoblock mount (delivered) | `00_Spec/inputs/OD-C04_thermoblock_mount.step` (#2): foot underside its y = −70.0 (−Y down), holes Ø3.4 at (x ±40.0, z −8.0 / 26.0) | — | OD-C04 spec 1.2 §4, REQ-05, REQ-06, A-10 (X-12 … X-17) | CONFIRMED as the input; A-02 places it |
| OD-C05 group head carrier (in design) | spec 1.0 → 1.1 (A-01): foot underside its y = −175.0 (+Y up), holes Ø3.4 at (x ±35.0, z −40.0 / −60.0), wall z −29.94 … −24.94 | — | OD-C05 spec §4, REQ-05, REQ-06, A-03, A-04 (X-23 … X-33) | CONFIRMED as the input; A-01 places it |
| OD-H01 pump, OD-H11 thermoblock, OD-G01 housing v02 | `00_Spec/inputs/OD-H01_ulka_ep5_pump.step`, `OD-H11_thermoblock.step`, `OD-G01_housing_C1_v02.step` (#3 … #5), placed by the joints their mounts' specs state, in the mounts' frames | — | OD-C03 spec §2 (identity), OD-C04 spec §2 (identity), OD-C05 spec §2 (identity) | CONFIRMED as the inputs |
| OD-C08 electronics bay tray (delivered) | `00_Spec/inputs/OD-C08_electronics_bay_tray.step`: modelled in the machine frame, placed at the identity; flange underside on y 0; four Ø3.4 flange holes along Y at (x 88, z −222), (106, −222), (88, −78), (106, −78) | — | OD-C08 spec 1.0 §4, U-05, D-04a; integration notes 2026-10-01 | CONFIRMED as the input; A-18 places it |
| OD-C11 back panel (delivered, build v03) | `00_Spec/inputs/OD-C11_back_panel.step`: machine frame, identity; floor flanges on y 0; four Ø3.4 holes along Y at (x ±81, z −282) and (x ±95, z −282); its wall inner face at z −299 | — | OD-C11 spec 1.2 §4, U-05; integration notes 2026-10-01 | CONFIRMED as the input; A-18 places it |
| Fasteners | M3 heat-set inserts (OD-F01) in this plate, M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` (INTAKE §3) | CONFIRMED (project standard) |

**Coordinate frame (the machine frame):** X to the user's right, **+Y up**, +Z toward
the user (the front); the origin lies on the group head axis' vertical, on the
floor plane: y = 0 is the plate's top face, the floor plane every mount's foot
stands on (INTAKE X-01, X-12, X-23; §4 gap 11 answered by A-01 … A-03); the group
head axis is the line (x 0, y 175) along Z, and its housing's rear face is the plane
z = −24.94, as in OD-C05's frame. The plate occupies y −6.0 … 0. Every artifact of
this job uses this frame; the three mounts' local frames map into it by the joints
of §4 (A-01 … A-03), which answer INTAKE §4 gap 1.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c01_frame | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-09) | PLA for now (the Usta, 2026-10-02: all prints in PLA); service material PETG or ASA stays A-10 | 1240 | as printed | A-10 |

Environment: the bottom of the machine, on the counter through four feet; the wet
zone (left and centre) sees drips and leaks that must reach the tray, not the
electronics (INTAKE X-41, X-49); the thermoblock stays ≥ 10 mm above the plate by
its mount's design (OD-C04: lowest casting point 16.5 above the floor, INTAKE X-17);
loads: the mounts and their OEM parts (≈ 0.5 kg pump, ≈ 0.45 kg thermoblock, the
group head with the portafilter and the user's locking torque), the tank (≈ 1 kg
full), a hand pressing the buttons.

## §4 Architecture and concepts

- **C1 — one flat plate with insert holes, feet holes, drain holes and reserved
  zones (CHOSEN).** One solid. A plate 6.0 thick, y −6.0 … 0, spanning x −120 …
  +120 and z −305 … +100 (corners R 10), printed flat, top face up. The layout in
  this frame (every joint is a translation and a rotation of a mount's own frame):
  - **OD-C05 carrier and the group head** (A-01, 1.2): the group head axis is
    vertical, the mouth down (OD-C05 spec 2.0 A-02, RV01 F1). The carrier's frame
    (the OD-G01 housing frame) maps by the proper rotation local x → X, local
    y → +Z, local z → −Y, its origin at (0, 180.06, 32.0), so its foot underside
    (its z +180.06) lands on y 0, the housing's rear face (its z −24.94) lies at
    y 205.0 and the housing's mouth face (its z +3.30) at y 176.76; the carrier's
    holes at (x ±35, z −40) and (x ±35, z −60) (unchanged); its foot occupies
    x ±55, z −70 … −26, its wall z −26 … −20 up to y 210, its plate z −26 … +82 at
    y 205 … 210; the housing occupies x ±50, z −18 … +82; the portafilter spouts
    hang to y ≈ 135.2 (OD-C05 spec 2.0 A-03).
  - **OD-C04 thermoblock mount** (A-02): its frame at the identity rotation (its
    −Y is down, its +Z toward the group head), its origin at (0, 70, −140), so its
    foot underside y −70 lands on y 0; its holes at (x ±40, z −148) and
    (x ±40, z −114); its foot occupies x ±50, z −157 … −107; the thermoblock's
    outlet pins reach z −89.21 (its z 50.79), so the casting stays behind z −85 as
    OD-C05 A-05 assumes, 19.3 behind the carrier's foot, and its lowest point sits
    16.5 above the plate.
  - **OD-C03 pump cradle** (A-03): the pump axis along X across the back; its
    frame rotated so that its local x → +Z, local y → −Y, local z → +X (a proper
    rotation), its origin at (0, 40, −205), so its foot underside (its y +40)
    lands on y 0, the pump axis lies at y 40, its holes at (x −4, z −239),
    (x −4, z −171), (x 37, z −239), (x 37, z −171); its foot occupies x −10 … 42,
    z −245 … −165; the pump spans x −66.45 … +55.5 with its outlet toward −X (the
    valve side, A-05).
  - **Bulkhead line OD-C02** (A-04): the plane x = 65 from z −240 to −30, with four
    insert holes at (x 65, z −45), (65, −105), (65, −165), (65, −225) for the
    bulkhead's foot; everything at x ≥ 70 behind it is the electric zone.
  - **Reserved zones** (A-05 … A-08, documented in the plan, not gated): the drip
    tray x ±75, z −15 … +85 on the plate under the mouth at (0, 32) (cup rest top
    ≤ 36.9 above the plate, A-06; 1.2 moved it back 25 with the housing); the water tank x ±70, z −305 … −250 (A-07); the valve and flowmeter
    mount OD-C07 x −117 … −67, z −154 … −35 (A-05); the electronics bay x 70 … 120,
    z −240 … −30 (A-08).
  - **OD-C07 valve and flowmeter mount** (A-17, added in 1.1): its frame rotated so
    that its local x → −Z, local y → −X, local z → +Y (a proper rotation), its
    origin at (−92, 0, −60), so its bottom face lands on y 0, its flowmeter end
    faces the front and its valve end the pump; its footprint holes (its
    (−18, ±21) and (88.5, ±21)) land at (x −113, z −42), (x −71, z −42),
    (x −113, z −148.5), (x −71, z −148.5); its envelope (119 × 50 × 48 in its frame)
    occupies x −117 … −67, z −154 … −35, up to y 48; its hose window (its
    x 40 … 84, y ±25) lies over z −144 … −100, so the drain hole at (−80, −120)
    sits under it. The pump's −X end (x −66.45, z ≤ −165) stays ≥ 11 behind the
    mount's rear end (z −154).
  - **OD-C08 tray and OD-C11 back panel** (A-18, added in 1.3): both modelled in
    this frame and placed at the identity. Four insert holes under the tray's flange
    at (x 88, z −222), (106, −222), (88, −78), (106, −78), inside the electronics bay
    (A-08); four under the back panel's floor flanges at (x ±81, z −282) and
    (x ±95, z −282), outside the tank zone's x ±70.
  - **OD-C16 side-panel brackets** (A-19, added in 1.3): three per side, each one
    M3 down into an insert at (x ±104.5, z −262), (±104.5, −15), (±104.5, +62).
  - **OD-C09 front panel** (A-20, added in 1.3): modelled in this frame, placed at
    the identity; its two floor flanges screw into inserts at (x ±85, z +77) and
    (x ±95, z +77).
  - **Insert holes**: thirty-eight Ø4.0 through-holes along Y (sixteen under the four
    mounts, four on the bulkhead line, four under OD-C08, four under OD-C11, six
    under the OD-C16 brackets, four under OD-C09) for M3 × 5.7 heat-set inserts driven from the
    top (the 6.0 plate holds the 5.7 insert, A-11). **Feet holes**: four Ø3.4
    through-holes at (x ±110, z +90) and (x ±110, z −295) for the feet OD-C15
    (an M3 × 12 from the top into a nut captive in the foot) or the OEM pads (A-12). **Drain holes**: two Ø8.0 through-holes in the wet zone
    at (x −80, z −120) and (x −80, z −230) so a leak leaves the machine instead of
    pooling (A-13); the tray zone itself is the plate's top face.
  - Print orientation: flat, bottom face on the bed, no supports (A-14). Envelope
    240.0 × 6.0 × 405.0 (x ±120, y −6 … 0, z −305 … +100).
- **C2 — ribbed tray with a raised rim and a recessed tray well.** Stiffer and
  lighter, with the drip tray sunk into the plate. Deferred: needs the tray scan
  (INTAKE §4 gap 4) and the feet decision.
- **C3 — two half plates joined at the bulkhead line.** For a printer smaller than
  the Kobra Max 3. Deferred until A-09 is answered.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 240.0 × 6.0 × 405.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±120.0, y −6.0 … 0.0, z −305.0 … +100.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) plate|OD-C03 and plate|OD-C04 at the joints of §4: designed contacts, `clearance = 0`, `interference ≤ 0` mm³; each mount's four Ø3.4 holes coaxial with the plate's Ø4.0 holes, offset ≤ 0.10 (`locate_bore` on both solids); plate|OD-H01 ≥ 2.0 and plate|OD-H11 ≥ 10.0 (`clearance`; the OD-H11 boolean is INCONCLUSIVE by OD-C04 A-14 and reported); OD-C03|OD-C04 ≥ 2.0; OD-H11 max z ≤ −85.0 (`envelope` of the placed solid); OD-G01 v02 at the carrier's pose (the joint of §4, origin (0, 180.06, 32.0), rotation x → X, y → +Z, z → −Y) ≥ 2.0 to everything else; the carrier itself is not built yet (A-01: the check assembly places its foot outline x ±55, y 0 … 4, z −70 … −26 as a reference box, not a solid); 1.3: plate|OD-C08 and plate|OD-C11 at the identity (A-18) and plate|OD-C16 × 6 at the poses of A-19 and plate|OD-C09 at the identity (A-20): designed contacts `clearance = 0`, `interference ≤ 0` mm³, each of their Ø3.4 holes coaxial with its plate Ø4.0 hole, offset ≤ 0.20 (the sum of the two parts' 0.10 position bands); every new part `interference ≤ 0` mm³ with the plate. (b) N/A | Hard | CAD | house | `clearance`, `interference`, `locate_bore`, `envelope` | A-01 … A-03 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 plate, 38 Ø4.0 through-holes, 4 Ø3.4 through-holes, 2 Ø8.0 through-holes | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/6.0) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default; the plate carries the machine) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the Kobra Max 3 build volume, flat: 240.0 × 405.0 on the bed, 6.0 tall | Hard | part | machine | `envelope` | A-09 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (flat, build direction +Y): none but the bed face; nothing supported | Hard | part | floor | `overhang_census(build_dir=(0,1,0))` | A-14 |
| D-03b | Unsupported bridge | span ≤ 5: none | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | the four feet holes Ø ≥ 3.25 (designed Ø3.4); the drain holes are not fastener holes | Hard | part | house | `locate_bore` | A-12 |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around each Ø4.0 hole (the plate itself) | Hard | part | struct | `bore_census`, `radial_extent` | A-11 |
| D-05b | Heat-set insert hole | the thirty-eight insert holes Ø 4.0 ± 0.05, depth ≥ 5.7 (through the 6.0 plate) | Hard | part | floor | `bore_census`, `locate_bore` | A-11 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: insert holes are formed by the insert, the rest are clearance and drain holes | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 around each of the thirty-eight insert holes | Hard | part | struct | `min_wall` | — |
| E-06 | Boss support | no bosses on this part | Hard | part | struct | — (N/A by this row) | — |
| REQ-01 | Carrier inserts | four Ø4.0 ± 0.05 through-holes along Y at (x ±35.0, z −40.0) and (x ±35.0, z −60.0), offset ≤ 0.10 (OD-C05 A-04) | Hard | CAD | A-01 | `locate_bore` | A-01 |
| REQ-02 | Thermoblock mount inserts | four Ø4.0 ± 0.05 through-holes at (x ±40.0, z −148.0) and (x ±40.0, z −114.0), offset ≤ 0.10, coaxial with OD-C04's holes as placed (U-03) | Hard | CAD | A-02 | `locate_bore` | A-02 |
| REQ-03 | Pump cradle inserts | four Ø4.0 ± 0.05 through-holes at (x −4.0, z −239.0), (x −4.0, z −171.0), (x 37.0, z −239.0), (x 37.0, z −171.0), offset ≤ 0.10, coaxial with OD-C03's holes as placed (U-03) | Hard | CAD | A-03 | `locate_bore` | A-03 |
| REQ-04 | Bulkhead inserts | four Ø4.0 ± 0.05 through-holes at (x 65.0, z −45.0), (65.0, −105.0), (65.0, −165.0), (65.0, −225.0), offset ≤ 0.10 | Hard | CAD | A-04 | `locate_bore` | A-04 |
| REQ-05 | Feet holes | four Ø3.4 ± 0.1 through-holes at (x ±110.0, z +90.0) and (x ±110.0, z −295.0), offset ≤ 0.10 | Hard | CAD | A-12 | `locate_bore` | A-12 |
| REQ-06 | Drain holes | two Ø8.0 ± 0.1 through-holes at (x −80.0, z −120.0) and (x −80.0, z −230.0), offset ≤ 0.10 | Hard | CAD | A-13 | `locate_bore` | A-13 |
| REQ-07 | Floor plane | the top face at y = 0.00 ± 0.10 (`envelope` max_y), 6.0 ± 0.1 thick; the whole top face one plane (the mounts' feet seat on it) | Hard | CAD | A-01 … A-03 | `envelope`; reviewer from sections | — |
| REQ-08 | Thermoblock zone | OD-H11 as placed: `envelope` max_z ≤ −85.0 and `clearance(plate, OD-H11)` ≥ 10.0 (OD-C05 A-05, OD-C04 REQ-01) | Hard | CAD | client (INTAKE X-20, X-30) | `envelope`, `clearance` | A-02 |
| REQ-10 | Valve mount inserts | four Ø4.0 ± 0.05 through-holes at (x −113.0, z −42.0), (x −71.0, z −42.0), (x −113.0, z −148.5), (x −71.0, z −148.5), offset ≤ 0.10, coaxial with OD-C07's footprint holes as placed by A-17 (checked against the OD-C07 STEP when it delivers; until then against the pattern) | Hard | CAD | A-17 | `locate_bore` | A-17 |
| REQ-11 | Tray inserts | four Ø4.0 ± 0.05 through-holes at (x 88.0, z −222.0), (106.0, −222.0), (88.0, −78.0), (106.0, −78.0), offset ≤ 0.10, coaxial with OD-C08's flange holes at the identity (U-03); each ≥ 6.0 centre to centre from every other hole, ≥ 8.0 from the plate edge | Hard | CAD | A-18 | `locate_bore` | A-18 |
| REQ-12 | Back panel inserts | four Ø4.0 ± 0.05 through-holes at (x ±81.0, z −282.0) and (x ±95.0, z −282.0), offset ≤ 0.10, coaxial with OD-C11's flange holes at the identity (U-03); ≥ 8.0 from the plate edge | Hard | CAD | A-18 | `locate_bore` | A-18 |
| REQ-13 | Side-panel bracket inserts | six Ø4.0 ± 0.05 through-holes at (x ±104.5, z −262.0), (±104.5, −15.0), (±104.5, +62.0), offset ≤ 0.10, coaxial with the OD-C16 brackets' screw holes as placed (U-03); ≥ 8.0 from the plate edge, ≥ 6.0 centre to centre from every other hole | Hard | CAD | A-19 | `locate_bore` | A-19 |
| REQ-14 | Front panel inserts | four Ø4.0 ± 0.05 through-holes at (x ±85.0, z +77.0) and (x ±95.0, z +77.0), offset ≤ 0.10, coaxial with OD-C09's flange holes at the identity (U-03); ≥ 8.0 from the plate edge, ≥ 6.0 centre to centre from every other hole | Hard | CAD | A-20 | `locate_bore` | A-20 |
| REQ-09 | Flatness in service | **Soft.** The printed plate stays flat enough for the three mounts to seat without rocking after printing and in use (warp on a 405 mm plate; PLA for now); not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, and it is answered by the first print | Soft | part | client | — (bench) | A-10, A-14 |

**Named exceptions** (Usta U-18): none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-C05 carrier joint and height | the carrier's (= housing's) frame mapped by x → X, y → +Z, z → −Y with its origin at (0, 180.06, 32.0): the group head axis vertical, the mouth down (1.2, OD-C05 spec 2.0 A-02, RV01 F1); its foot underside at its z +180.06 on y 0; its holes at (±35, z −40 / −60) as OD-C05 spec §4 (the pattern of spec 1.x kept); the housing's rear face at y 205, the spouts at y ≈ 135.2 (OD-C05 A-03); the carrier is not built yet: the check assembly uses its foot outline box (x ±55, z −70 … −26) and the OD-G01 v02 STEP at the housing's pose | the carrier does not seat or its holes miss; the group head height changes | OD-C05 spec 2.0 §2, A-02 … A-04; this spec | OD-C05's delivered build; the Usta's answer to the up-direction card | OPEN |
| A-02 | OD-C04 joint | identity rotation, origin (0, 70, −140): the thermoblock's axis horizontal at y ≈ 55.9 (its axis at its y −14.13), pipes and terminals up, outlet pins at z −89.21 toward the group head, casting ≥ 16.5 above the plate (OD-C04 A-07, A-10) | the thermoblock fouls the carrier or the tube runs do not reach | OD-C04 spec 1.2 §2, A-07, A-10 (INTAKE X-12 … X-22); this spec (P4) | the Usta's layout confirmation; the tube runs | OPEN |
| A-03 | OD-C03 joint | rotation local x → +Z, y → −Y, z → +X, origin (0, 40, −205): pump axis along X at y 40 across the back, the terminal block (its −Y) up, the outlet (its −Z) toward −X where the valves sit; its foot 8 mm behind the thermoblock mount's foot | pump hoses do not reach; vibration path | OD-C03 spec 1.2 §2, A-08 (INTAKE X-01 … X-11); this spec | the Usta's layout confirmation; the tube runs | OPEN |
| A-04 | OD-C02 bulkhead interface | a wall on the plane x = 65 from z −240 to −30 (3 to 5 thick), standing on four M3 inserts at (65, −45), (65, −105), (65, −165), (65, −225); the electric zone is x ≥ 70 | OD-C02 must be designed to it | this spec (design choice; the OD-C03/C04/C05 precedent) | OD-C02 design | OPEN |
| A-05 | Valve and flowmeter zone | OD-C07 with OD-H21, OD-H22, OD-H24 within x −117 … −67, z −154 … −35, on the pump's outlet side, placed by A-17 (1.1) | the zone is too small or on the wrong side of the tube runs | this spec; WATER_FLOW.md (INTAKE §3) | OD-C07 design | OPEN |
| A-06 | Drip tray | the tray OD-C21 with its grid stands on the plate within x ±75, z −15 … +85, under the mouth at (0, 32), its cup rest top ≤ 36.9 above the plate (so the portafilter spouts at y ≈ 135.2 keep the ≥ 95 mm mug rule, INTAKE X-29, X-43; OD-C05 A-03); no locating features until the scan | the mug does not fit or the tray hangs over the edge | this spec; issue #9 (INTAKE X-57) | the tray scan (issue #9) | OPEN |
| A-07 | Water tank zone | OD-W01 with its dock OD-C06 stands within x ±70, z −305 … −250, lifted out upward; the tank seat OD-W03 faces the pump | the tank does not fit; the plate must grow | this spec; BOM OD-W01, OD-C06 (INTAKE §3) | the tank scan; OD-C06 design | OPEN |
| A-08 | Electronics bay | OD-C08 (path 1, the OEM PCB OD-E01; delivered) occupies x 73 … 112, z −230 … −70, y 0 … 92 inside the bay x 70 … 120, z −240 … −30 | the bay is too small | this spec; OD-C08 integration notes 2026-10-01 | OD-C08 print and fit | OPEN |
| A-09 | Kobra Max 3 build volume | 420 × 420 × 500 (Anycubic specification, not in the machine file); the plate is 240 × 405 flat | plate does not fit: C3 (two halves) | memory of the spec sheet (as OD-C03 A-10) | the Usta reads the printer | OPEN |
| A-10 | Material | PLA for now (the Usta, 2026-10-02), density 1240 kg/m³, on the Kobra Max 3; the service material (PETG or ASA) is still open | creep under the tank, softening near 60 °C (the plate is ≥ 16.5 below the thermoblock) | BOM OD-C01 (INTAKE §3); SOURCING_GUIDE §6 rule 3 | the Usta names the filament | OPEN |
| A-11 | Insert | M3 × 5.7 × Ø4.6 heat-set inserts in Ø4.0 through-holes of the 6.0 plate, driven from the top (OD-G01 A-17's figure); the screw tips may reach 0.3 below the plate | insert pulls out; the plate needs bosses | this spec; INTAKE §3 (OD-F01) | the Usta's stocked insert datasheet | OPEN |
| A-12 | Feet | four printed feet OD-C15 (or the OEM pads OD-C25/C26), each held by an M3 × 12 from the plate top through the Ø3.4 holes at (±110, +90) and (±110, −295) into a nut captive in the foot (OD-C15 A-02, 1.3; supersedes "screwed from below into inserts of the feet"); a Ø8 × 2 keep-out above each hole for the screw head | feet option changes; holes move | this spec; BOM OD-C15, C25, C26 (INTAKE X-44, X-68 … X-71) | the Usta picks the feet | OPEN |
| A-13 | Drainage | two Ø8 drain holes in the wet zone let a leak leave the machine onto the counter under it; the tray zone drains by the tray; no channels on the flat plate (C2 later) | a leak reaches the electronics before a drain | this spec; SOURCING_GUIDE §6 rule 1 (INTAKE X-41) | OD-C02's drainage path | OPEN |
| A-14 | Print orientation | flat on the bed, bottom face down, no supports, brim against warp | warp lifts the corners (REQ-09) | this spec | first print | OPEN |
| A-15 | Scan fidelity of the OEM parts | OD-H01 p95 0.448 and OD-H11 p95 0.474 (INTAKE X-08, X-19, §4 gap 13); the mounts' hole patterns are design values, not scan values, so only the placed OEM envelopes carry the scan error | the thermoblock zone or the pump reach is off by the scan error | the mounts' specs | calipers | OPEN |
| A-17 | OD-C07 joint and footprint | OD-C07 (spec at RV01 REVISE, not yet approved) needs four M3 inserts at its (−18, ±21) and (88.5, ±21) (its A-14, REQ-06), its bottom face on the floor; placed by the joint of §4 (x → −Z, y → −X, z → +Y, origin (−92, 0, −60)): holes at (−113, −42), (−71, −42), (−113, −148.5), (−71, −148.5), web to the plate edge 5.0 | the pattern or the pose changes when OD-C07 is approved; the holes move | OD-C07 spec A-14 (relayed from the "Chassis parts C06 to C11" thread, 2026-09-30); this spec (pose: design choice) | OD-C07's approved build and its delivered STEP | OPEN |
| A-18 | OD-C08 and OD-C11 joints | both modelled in the machine frame, placed at the identity: OD-C08's flange and OD-C11's floor flanges stand on y 0; their holes as REQ-11 and REQ-12; their reviewers found the plate solid under each (≥ 6 from every existing hole, ≥ 8 from the edge) | the parts move and the holes miss | OD-C08 and OD-C11 integration notes (2026-10-01) | their first print and fit | OPEN |
| A-19 | OD-C16 bracket joints | the bracket (its frame: block x −19 … 0, y 0 … 16, z ±8) placed on the right side by translation (117, 0, z_c), on the left by a 180° rotation about Y then (−117, 0, z_c), z_c ∈ {−262, −15, +62}; its screw hole lands on (±104.5, z_c) | the panels move and the holes miss | OD-C12/C13/C16 integration notes (2026-10-02), side spec A-01, REQ-06 | the first print and fit | OPEN |
| A-20 | OD-C09 joint | modelled in the machine frame, placed at the identity; its floor flanges (z +72 … +94) on y 0, holes as REQ-14, 19.8 from the feet holes at (±110, +90) and 17.8 from the bracket inserts at (±104.5, +62) | the panel moves and the holes miss | OD-C09/T01 integration notes (2026-10-03), C09 spec A-01, REQ-01 | the first print and fit | OPEN |
| A-16 | Footprint and height | 240 × 405 plate; machine height ≈ 260 (plate 6 + axis 175 + housing 43.1 + top panel and clearance) plus feet; the thesis' 0.4 m³ figure (INTAKE X-53) is read as an upper bound the machine is far below | the machine is too big for the Usta's counter | this spec | the Usta's layout confirmation | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC on the Usta's "go" after OD-C03 and OD-C04; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and "go" of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity, the layout of §4 above all | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | the drip tray blocker (chassis order-of-work row 7) is lifted on the Usta's "go": the tray is a reserved zone (A-06); the job is reopened when the scan lands | Oğuz on the Usta's "go" | REQUEST.md |
| 2026-09-30 | the group head axis goes to 175 above the floor (OD-C05 spec 1.1) so that a tray up to 36.9 tall fits under the ≥ 95 mm mug rule; OD-C05 spec 1.0's 150 left 11.9 | Oğuz | INTAKE §4 gap 4; A-01 |
| 2026-09-30 | INTAKE §4 gaps 1, 2, 11, 12 (frames, positions, floor planes, the thermoblock offset) are answered by the joints of §4 as design choices, all A-## rows | Oğuz | §4, A-01 … A-03 |
| 2026-09-30 | REQ-09 (flatness) is a Soft bench gate answered by the first print (the OD-C03 RV01 lesson) | Oğuz | §5 |
| 2026-09-30 | the group head axis is vertical with the mouth down (OD-C05 RV01 F1; put to the Usta as a decision card): the housing pose of §4 and A-01 rewritten, the tray zone moved under the mouth; the plate's holes and every other feature stand; the housing's rear face at y 205 from the portafilter spouts (OD-C05 spec 2.0 A-03) | Oğuz, on OD-C05 spec 2.0 | A-01, A-06 |
| 2026-09-30 | OD-C07's footprint (four inserts, 106.5 × 42) goes on the plate now (REQ-10, A-17) rather than as a later round: placed in the valve zone with the flowmeter to the front, the hose window over the drain at (−80, −120), 11 behind-clearance to the pump; the zone grows to x −117 … −67, z −154 … −35 | Oğuz, on the OD-C07 spec A-14 | A-05, A-17 |
| 2026-10-02 | revision B: eighteen Ø4.0 insert through-holes for OD-C08, OD-C11, the OD-C16 brackets and OD-C09 (REQ-11 … REQ-14, A-18 … A-20) in the plate's existing convention (through the 6.0 plate, insert from the top, as the other twenty); PLA for now (A-10); feet held from the top (A-12); every other feature of build v02 unchanged | Oğuz, on the Usta's 2026-10-02 answers and the C08/C11 integration notes | A-10, A-12, A-18 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the three mounts' specs and the OEM reports |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6; ratified |
| 1.2 | 2026-09-30 | the group head vertical (OD-C05 spec 2.0): the housing pose in §4, U-03, A-01, A-06, the tray zone z −15 … +85; no change to the plate's features |
| 1.1 | 2026-09-30 | OD-C07 joint and four insert holes (§4, U-05, D-05b, J-05, REQ-10, A-05, A-17); twenty insert holes |
| 1.3 | 2026-10-02 | revision B: thirty-eight insert holes (§4, U-03, U-05, D-05b, J-05, REQ-11 … REQ-14, A-18 … A-20); PLA for now (§3, A-10); feet from the top (A-12); OD-C08 path 1 (A-08) |
