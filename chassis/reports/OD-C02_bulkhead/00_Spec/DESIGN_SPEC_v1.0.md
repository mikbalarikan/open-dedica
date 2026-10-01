# DESIGN_SPEC — OD-C02 printed wet/electric bulkhead (20260930-od-c02-bulkhead)

Version 1.0 · RATIFIED by the Usta on 2026-09-30 (standing instruction of 2026-09-30 and the "confirmed go" / "go" of the same day: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C02 is the 3D-printed bulkhead of the Open Dedica espresso machine: a wall that
stands on the base frame OD-C01 along the plane x = 65 (OD-C01 A-04, REQ-04) and
separates the wet zone (pump, thermoblock, group head, valves, tank; x < 65) from
the electric zone (the electronics bay OD-C08; x ≥ 70), keeps a leak on the wet
side on the wet side (its base rail is a dam on the plate; the drain holes are at
x −80, INTAKE X-13, X-14), passes the wires that cross (pump, thermoblock heater and
thermostat, flowmeter Hall sensor, valve solenoid; INTAKE X-19) through raised
windows well above splash height, and gives the top panel OD-C10 two insert bosses.
Done means: one valid printable solid standing on the four OD-C01 inserts with its
wet face on x = 63, nothing of it in the wet neighbours' space, its windows at the
heights of §4, and every unconfirmed value in §6. The tube runs, the wiring, the
electronics bay and the panels are not designed: their rows are assumptions and the
job is reopened when they land (INTAKE §4).

**Deliverables** (tier M): STEP AP242 of the bulkhead; the check assembly STEP
(bulkhead + OD-C01 + the wet-side neighbours as OD-C01 places them); STL and 3MF;
build and check scripts; REPORT; sections. No drawings or renders.

**Out of scope:** OD-C08 electronics bay, the panels OD-C09 … C13, the wiring
and its grommets, the tube runs, sealing compounds, calipers, drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-C01 (base frame, delivered v02) | `00_Spec/inputs/OD-C01_base_frame.step` (INTAKE §1); its top face y = 0, its four bulkhead inserts Ø4.0 at (x 65, z −45 / −105 / −165 / −225) | — | OD-C01 spec 1.2 REQ-04, REQ-07; REPORT v02 | CONFIRMED as the input; its numbers are §6 rows |
| Wet-side neighbours as OD-C01 places them | OD-C03 + OD-H01 (rotation x → +Z, y → −Y, z → +X at (0, 40, −205)), OD-C04 + OD-H11 (identity at (0, 70, −140)), OD-G01 v02 (x → X, y → +Z, z → −Y at (0, 180.06, 32)); the OD-C05 carrier as its foot box x ±55, z −70 … −26 up to y 210 (its spec 2.1 §4: column x ±55) | — | OD-C01 spec 1.2 §4, A-01 … A-03 | CONFIRMED as inputs; poses are the OD-C01 rows |
| Fasteners | M3 heat-set inserts (OD-F01, Ø4.6 × 5.7) in OD-C01 and in the bulkhead's top rail, M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` (INTAKE X-09) | CONFIRMED (project standard) |

**Coordinate frame:** the OD-C01 machine frame, so every overlay is the identity
(OD-C01 spec §2): X to the user's right, +Y up, +Z toward the user (the front),
the plate's top face y = 0, the origin on the plate's top face under the group
head's front axis line. The bulkhead's wet face is the plane x = 63.0, its electric
face x = 67.0 (the wall centred on x = 65, OD-C01 A-04). Every artifact of this
job uses this frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c02_bulkhead | FDM | machines/creality-k1c.toml (enclosed; build volume UNKNOWN → A-08) | ASA (BOM: ASA) | 1070 | as printed | A-09 |

Environment: inside the machine, between the wet and electric zones; steam and
drips on the wet face, the thermoblock casting (≈ 130 °C, INTAKE X-32) at
x ≤ 50 (≥ 13 mm of air), the pump's +X end at x 55.5 (7.5 mm), mains wiring on the
electric face. Loads: none but its own stiffness and the top panel's four screws.

## §4 Architecture and concepts

- **C1 — one wall on a base rail, a top rail, wire windows, two ribs (CHOSEN).**
  One solid, printed lying on its wet face. A **wall** 4.0 thick, x 63.0 … 67.0,
  z −240.0 … −30.0 (210 long), from the plate y 0 up to y 215.0 (A-06: the machine
  is ≈ 260 tall with the top panel above; the carrier's plate top is y 210). A
  **base rail** along the whole length, x 59.0 … 70.0 (11 wide), y 0 … 12.0, the
  wall rising from it: four Ø3.4 through-holes along Y at (x 65.0, z −45.0 /
  −105.0 / −165.0 / −225.0) on the OD-C01 inserts (INTAKE X-04 … X-07), each with a
  Ø6.5 × 8.0 counterbore from the rail's top (y 12) so an M3 × 8 screw driven from
  above leaves 4.0 of rail under its head and reaches 4.0 into the 5.7 insert
  (A-03); the rail's wet face at x 59 is the dam (nothing of the plate's top at
  x 59 … 70 is open under the wall). A **top rail** x 62.0 … 73.0 (11 wide),
  y 207.0 … 215.0, along the whole length, with two Ø4.0 × 6.0 blind bores along
  −Y from the top at (x 67.5, z −60.0) and (x 67.5, z −210.0) for M3 inserts that
  take the top panel OD-C10 (A-05). Four **wire windows** through the wall along
  X, round, with a raised collar 2.0 tall × 2.0 wide on the wet face (x 61 … 63,
  a drip ring): Ø14.0 at (y 150.0, z −200.0) for the pump, (y 150.0, z −130.0)
  for the thermoblock heater and thermostat, (y 150.0, z −60.0) for the group head
  side, and (y 60.0, z −40.0) for the valve and flowmeter wires that run along the
  front (A-04). Two **ribs** on the electric face, 4.0 thick (z) × 5.0 deep
  (x 67 … 72), from the base rail's top (y 12) to the top rail (y 207), at
  z −70.0 and z −200.0 (the ribs and the top rail reach x 73 at most: 3 mm into
  the bay zone x ≥ 70, A-07). Nothing of the bulkhead lies at x < 59.0 (REQ-05);
  the nearest wet neighbour is the pump's +X end at x 55.5 (OD-C01 REPORT). Print
  orientation (A-10): neither face is flat (rails and collars stand proud on
  both sides), so the part prints **standing on its rear end** z = −240 (a 215 × 14 footprint,
  210 tall), build direction +Z: every window is a horizontal hole (crowns are
  the named exception), the counterbores along Y and the insert bores along −Y are
  horizontal holes too (crowns, same exception), the rails and ribs are prisms
  along Z; no supports. Envelope 14.0 × 215.0 × 210.0 (x 59 … 73, y 0 … 215,
  z −240 … −30).
- **C2 — the wall as part of the electronics bay tray OD-C08.** Deferred: OD-C08
  is not designed (chassis order of work row 9).
- **C3 — a wall lying flat for printing with the rails on one side only.**
  Rejected: the counterbores must be centred on x = 65 with heads clear of the
  wall, so the rail must straddle the wall.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 14.0 × 215.0 × 210.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x 59.0 … 73.0, y 0 … 215.0, z −240.0 … −30.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) bulkhead|OD-C01 at the identity: the rail's underside on the plate's top face is the designed contact, `clearance = 0`, `interference ≤ 0` mm³; the four bulkhead holes coaxial with the plate's Ø4.0 inserts, offset ≤ 0.10 (`locate_bore` on both solids); bulkhead to OD-H01, OD-H11, OD-C03, OD-C04, OD-G01 (as OD-C01 places them) ≥ 3.0 each, nearest points reported (the OD-H11 boolean INCONCLUSIVE by OD-C04 A-14); bulkhead to the carrier's box x ±55 ≥ 4.0. (b) N/A | Hard | CAD | house | `clearance`, `interference`, `locate_bore` | A-01, A-02 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 wall, 1 base rail, 1 top rail, 2 ribs, 4 windows with 4 collars, 4 Ø3.4 through-holes along Y with 4 Ø6.5 counterbores, 2 Ø4.0 blind bores | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/6.0) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh (written by the orchestrator, checked by the reviewer) | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 1.75` (spec value ≥ D-01a: the counterbore Ø6.5 in the 11 rail leaves 1.75 on the electric side at x 68.25 … 70; the wall itself is 4.0) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the K1C build volume, standing on z −240: 14.0 × 215.0 on the bed, 210.0 tall | Hard | part | machine | `envelope` | A-08 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (standing on the rear end, build direction +Z): every rail, rib and collar face is vertical; the crowns of the fourteen horizontal bores (4 windows, 4 holes, 4 counterbores, 2 insert bores) are the named exception below, excluded from the census by position and their least angle reported | Hard | part | floor | `overhang_census(build_dir=(0,0,1))`; reviewer from sections | A-10 |
| D-03b | Unsupported bridge | span ≤ 5: the crowns of the horizontal bores are the named exception (the windows Ø14 are printed as horizontal holes with a 45° gable roof: their crown is the gable, see REQ-04) | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | the four Ø3.4 holes Ø ≥ 3.25 | Hard | part | house | `locate_bore` | — |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around each Ø4.0 insert bore (the top rail is 11 wide) | Hard | part | struct | `bore_census`, `radial_extent` | A-05 |
| D-05b | Heat-set insert hole | the two insert bores Ø 4.0 ± 0.05, depth 6.0 ± 0.1 (≥ 5.7) | Hard | part | floor | `bore_census`, `locate_bore` | A-05 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the insert bores are formed by the insert, the rest are clearance holes and windows | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 around each insert bore (the top rail 11 wide about x 67.5: 3.5 each side) | Hard | part | struct | `min_wall` | — |
| E-06 | Boss support | the collars and ribs sit on the wall, the rails span its whole length; no free-standing boss | Hard | part | struct | reviewer | — |
| REQ-01 | Frame holes | four Ø3.4 ± 0.1 through-holes along Y at (x 65.0, z −45.0 / −105.0 / −165.0 / −225.0), offset ≤ 0.10 from the OD-C01 inserts in the check assembly; Ø6.5 ± 0.1 counterbores 8.0 ± 0.1 deep from y 12.0 | Hard | CAD | A-01, A-03 | `locate_bore` on both solids, `bore_census` | A-01, A-03 |
| REQ-02 | Wall plane | the wall's wet face at x = 63.00 ± 0.10 and its electric face at x = 67.00 ± 0.10 over its whole height above the rail (sections at y 100 and y 200: the face x reported); the rail's wet face x 59.00 ± 0.10 (`envelope` min_x) | Hard | CAD | A-01 | `envelope`; reviewer from sections | A-01 |
| REQ-03 | Rail and dam | the base rail's underside at y = 0.00 ± 0.10 over x 59 … 70 and z −240 … −30 (one planar face, the designed contact of U-03); rail top at y 12.0 ± 0.1 | Hard | CAD | A-01 | `envelope`, `feature_census`; reviewer from sections | A-01 |
| REQ-04 | Wire windows | four Ø14.0 ± 0.1 openings through the wall along X at (y 150.0, z −200.0), (150.0, −130.0), (150.0, −60.0), (60.0, −40.0), offset ≤ 0.10; each with a 45° gable roof toward +Z (the print's up; apex 7.0 above the circle's top) so the window prints without a bridge; a collar ring OD 18.0 × 2.0 tall on the wet face around each | Hard | CAD | A-04 | `locate_bore` (the round part), `radial_extent`; reviewer from sections | A-04 |
| REQ-05 | Wet-side keep-out | no bulkhead material at x < 59.0 (`envelope` min_x ≥ 59.0); clearances of U-03 to every wet neighbour ≥ 3.0 | Hard | CAD | A-02 | `envelope`, `clearance` | A-02 |
| REQ-06 | Height | top rail's top face at y 215.0 ± 0.1 (`envelope` max_y); the wall reaches the top rail everywhere (sections) | Hard | CAD | A-06 | `envelope`; reviewer from sections | A-06 |
| REQ-07 | Top panel inserts | two Ø4.0 ± 0.05 blind bores along −Y from y 215.0, depth 6.0 ± 0.1, at (x 67.5, z −60.0) and (67.5, −210.0), offset ≤ 0.10 | Hard | CAD | A-05 | `locate_bore`, `bore_census` | A-05 |
| REQ-08 | Electric-zone intrusion | nothing of the bulkhead at x > 73.0 (`envelope` max_x ≤ 73.0); the wall face itself at x 67 ≤ 70 | Hard | CAD | A-07 | `envelope` | A-07 |
| REQ-09 | Stiffness | **Soft.** The wall does not rattle or flex visibly with the panels on; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print | Soft | part | client | — (bench) | A-11 |

**Named exceptions** (Usta U-18): D-03a and D-03b for the crowns of the ten small horizontal bores in the print (4 Ø3.4 holes, 4 Ø6.5 counterbores, 2 Ø4.0 insert bores: bridges ≤ 6.6), the usual FDM practice for small horizontal holes; the four Ø14 windows are not excepted: they carry a 45° gable roof (REQ-04). Recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-C01 interface | the delivered OD-C01 v02 plate: top face y 0, four Ø4.0 inserts at (65, −45 / −105 / −165 / −225), wall on x = 65 (OD-C01 A-04, REQ-04, spec 1.2 ratified on the standing instruction) | the bulkhead does not seat or its holes miss | INTAKE X-02 … X-11; OD-C01 spec 1.2, REPORT v02 | OD-C01's print and the Usta's layout confirmation | OPEN |
| A-02 | Wet-side neighbours | OD-C03 + OD-H01, OD-C04 + OD-H11, OD-G01 v02 and the carrier box as OD-C01 §4 places them; the pump's +X end at x 55.5 (OD-C01 REPORT), the carrier's column at x 55, the thermoblock casting at x ≤ 50; OD-H11 is unsound (brep_valid 0) so its booleans are INCONCLUSIVE | the wall fouls a neighbour or a tube | INTAKE X-20 … X-40; OD-C01 spec §4, REPORT v02 | the OD-000 assembly; calipers | OPEN |
| A-03 | Screw and engagement | M3 × 8 (OD-F02, head Ø5.7 or Ø5.5) through 4.0 of rail under a Ø6.5 × 8.0 counterbore, reaching 4.0 into the 5.7 insert (a 10 mm screw would reach 5.7 + 0.3: A-03 keeps the 8 of the BOM) | too short a screw; the head fouls the counterbore | this spec; INTAKE X-08, X-09 | the Usta's stocked screws | OPEN |
| A-04 | Wire windows | four Ø14 windows: three at y 150 (above every wet part: the pump top ≈ y 67, the thermoblock's pipes and terminals ≈ y 130, OD-C04 A-07) at z −200, −130, −60 for the pump, the thermoblock and the group head side; one low at (y 60, z −40) for the valve and flowmeter wires along the front; grommets or sealing are OD-E00's | a window is in the wrong place or too small; water reaches a window | this spec; INTAKE X-19, §4 gap 8 | the wiring plan (OD-E00) | OPEN |
| A-05 | Top panel inserts | OD-C10 screws down into two M3 inserts in the bulkhead's top rail at (67.5, z −60 / −210); the panel is not designed | the panel's pattern differs | this spec (design choice); INTAKE §4 gap 3 | OD-C10 design | OPEN |
| A-06 | Height | the wall 215 tall: the machine ≈ 260 with feet (OD-C01 A-16), the carrier's plate top at y 210, the top panel above 215 | the top panel does not meet the wall or the wall is too tall | this spec; INTAKE X-41 | OD-C10 / OD-000 | OPEN |
| A-07 | Electric-zone intrusion | the top rail (to x 73) and the ribs (to x 72) reach 3 mm into the bay zone x ≥ 70; OD-C08 is not designed and can keep 5 mm from the wall | the bay tray does not fit | this spec; INTAKE X-16, X-17 | OD-C08 design | OPEN |
| A-08 | K1C build volume | 220 × 220 × 250 (Creality specification, not in the machine file); the part stands 14 × 215 on the bed, 210 tall | part does not fit | memory of the spec sheet | the Usta reads the printer | OPEN |
| A-09 | Material | ASA, density 1070 kg/m³, printed on the K1C (BOM row) | warps on the bed (a 210 tall thin wall) | BOM OD-C02 (INTAKE); SOURCING_GUIDE §6 rule 3 | the Usta names the filament | OPEN |
| A-10 | Print orientation | standing on its rear end z −240, build direction +Z, no supports; the windows with 45° gables, the small bores as horizontal holes | the tall wall warps or topples on the bed; a brim is needed | this spec | first print | OPEN |
| A-11 | Stiffness | a 4 mm ASA wall 210 × 215 with two rails and two ribs, screwed down at four points and to the top panel at two: no calculation | the wall rattles or bows | this spec | first print (REQ-09) | OPEN |
| A-12 | Drainage | the rail is a continuous dam over z −240 … −30; a leak on the wet side runs to the drain holes at x −80 with the plate flat; no lip or slope on the plate (OD-C01 A-13) | water crosses under the plate's edge at the wall's ends (z > −30 or z < −240) | this spec; INTAKE X-13 … X-15, §4 gap 6 | the first wet test | OPEN |
| A-13 | Sealing and grommets | none printed: the windows take rubber grommets or the wires are tied clear; "sealed" in REQUEST.md is read as "raised and grommeted" | steam reaches the electric side | this spec; INTAKE §4 gap 8 | OD-E00 wiring | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC on the Usta's "go" after OD-C01 delivered; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and "go" of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | the tube-run blocker (chassis order-of-work row 8) is lifted on the Usta's "go": the tube runs are assumption rows; the job is reopened when they exist | Oğuz on the Usta's "go" | REQUEST.md |
| 2026-09-30 | INTAKE §4 gaps 1 … 8 (height, thickness, windows, panel attachment, build volumes, one piece, drainage lip, sealing) are answered by §4 as design choices, all A-## rows; INTAKE X-31 (16.5 vs 16.4925) is OD-C01's, the measured value governs | Oğuz | INTAKE_v01 §4 |
| 2026-09-30 | REQ-09 (stiffness) is a Soft bench gate answered by the first print | Oğuz | §5 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the OD-C01 spec 1.2 and REPORT v02 |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6; ratified |
