# Build guide: from the BOM to a running machine

This guide takes you from the bill of materials ([`bom.csv`](bom.csv), [BOM.md](BOM.md))
to an assembled Open Dedica. It collects what the part job records already say
(each printed part's spec in `chassis/reports/<part>/00_Spec/DESIGN_SPEC.md`, the
order of work and interfaces in [`chassis/README.md`](../chassis/README.md)) into one
sequence. Where the repository does not give a value, this guide says so instead of
filling it in.

Part numbers follow [PART_NUMBERING.md](PART_NUMBERING.md). Coordinates are mm in the
machine frame (X right, +Y up, +Z toward the front, plate top at y = 0) unless a
part's own frame is named.

## Contents

1. [Scope and status](#1-scope-and-status)
2. [Safety](#2-safety)
3. [What you need](#3-what-you-need)
4. [Printing](#4-printing)
5. [Heat-set inserts](#5-heat-set-inserts)
6. [Assembly sequence](#6-assembly-sequence)
7. [First power-up and tests](#7-first-power-up-and-tests)
8. [Open items](#8-open-items)

---

## 1. Scope and status

Read this before you print anything.

- **Every printed part is designed and reviewed in CAD only.** `OD-G01`, `OD-C01`…`OD-C05`,
  `OD-C07`…`OD-C16` and `OD-T01` are `modeled` in the BOM. Most were "approved on
  assumptions": every gate passes, but on values taken from 3D scans that nobody has
  confirmed with calipers yet. `OD-G01` was reviewed REVISE on its brew-load row
  alone (REQ-12), which only the `OD-T01` bench test can answer. The Usta accepted that
  as a documented deviation on 2026-10-02. `OD-C07` was reviewed REVISE as well, and
  the Usta accepted two seat gaps as deviations.
- **Nothing has been printed or fit-checked yet.** No part is `validated`. The first
  build is also the first fit check of every part.
- **Calipers beat scans on every interface.** Before you print a part, measure the
  OEM parts it touches and compare them with the open assumptions in its spec §6 (see
  [§8](#8-open-items)). If a measurement disagrees, stop and report it on the part's
  issue. Do not file the print to fit.
- **The base plate `OD-C01` is being revised to revision B** (spec 1.3, ratified
  2026-10-05). Revision B has **38 Ø4.0 insert holes**: the 20 of build v02 plus 18 new
  ones for `OD-C08`, `OD-C11`, `OD-C16` and `OD-C09`. The `chassis/OD-C01_base_frame.step`
  delivered from build v02 has only the 20 holes. **Until the revised plate STEP lands
  on main, only print the plate after you have checked that the file has 38 Ø4.0 insert
  holes** (plus 4 Ø3.4 feet holes and 2 Ø8 drain holes). Whether the 18 new holes go
  through the 6 mm plate or are blind is still a decision for revision B.
- The steam system (`OD-S00`) is phase 2 and is not in this build. The water tank dock
  `OD-C06` is deferred, so the tank stands on the table behind the machine.
- The top assembly `OD-000` (STEP) is being built. When it lands in `chassis/`, use it
  to check the steps below.

## 2. Safety

This is a mains-powered pressure appliance. Read this section in full.

- **Mains electrics.** The machine runs on mains voltage (230 V for the parts in this
  BOM; the EC685 also exists in 120 V, and every electrical part must match your mains,
  [SOURCING_GUIDE §2](SOURCING_GUIDE.md)). **All mains wiring, and the thermoblock's
  connections, must be done or checked by someone competent in mains electrics.**
- **Earth.** Bond earth to every metal part. The printed chassis does not conduct, so
  check earth continuity from the plug's earth pin to each metal part.
- **Unplug the machine whenever it is open.** Do not rely on the switch.
- **Keep the thermal cutoff.** The 192 °C TCO `OD-H18` stays in the heater circuit at all
  times ([SOURCING_GUIDE §6](SOURCING_GUIDE.md) rule 7; [CONTRIBUTING](../CONTRIBUTING.md)).
- **Test behind an RCD/GFCI**, and keep the build PAT-testable (README; SOURCING_GUIDE §6).
- **Pressure and heat.** Brew pressure is about 15 bar (the ULKA pump's rated
  maximum and the OEM over-pressure valve setting). The README and the `OD-G01` spec
  give water temperatures of up to about 125 °C on the hot side. The housing carries
  about 3.06 kN at 15 bar on a Ø51 basket (`OD-G01` A-21).
- **Keep wet and electric apart.** The bulkhead `OD-C02` separates the wet zone (x < 59)
  from the electric zone (x ≥ 70). Keep the drain holes in `OD-C01` clear.

**All printed parts are PLA for now.** This was the Usta's decision on 2026-10-02.
`bom.csv` lists each part's service material next to it. PLA softens at about
55–60 °C (the repository says "near 60 °C"), so:

- **PLA prints of `OD-G01`, `OD-C04` and `OD-C05` are dry fit checks only.** Never run
  hot water or pressure through them, and never power the thermoblock with them fitted.
- **The group head housing `OD-G01` must be printed in ASA and must pass the `OD-T01`
  bench pressure test behind a shield before any hot use** (section 7.1). Its strength
  has not been calculated or tested.
- `OD-C04` (service ASA/PC) and `OD-C05` (service ASA) must be reprinted in their
  service material before the thermoblock is ever powered.
- `OD-C02` sits 13 mm from the thermoblock casting (≈ 130 °C, its spec §3). Its service
  material is ASA, and SOURCING_GUIDE §3.2 asks for ABS/ASA/PC for anything within
  radiant range of the thermoblock. Print it in ASA before the first hot run as well.
- The front panel `OD-C09` (≈ 9 mm from the warm group head), the lid `OD-C10` and the
  side panels `OD-C12`/`OD-C13` each have an open assumption that asks for a
  temperature reading in the running machine (C09 A-11, C10 A-10, C12/C13 A-08). If a
  reading comes near PLA's softening point, reprint the part in its service material.
  The geometry stays the same.
- The `OD-T01` rig is PLA by design. It is used with cold water only, so PLA's heat
  limit does not apply to it.

## 3. What you need

### 3.1 OEM parts: sourcing

Follow [SOURCING_GUIDE.md](SOURCING_GUIDE.md). The recommended route is **Strategy A:
a donor machine** (a used or broken Dedica EC680 / EC685 / EC885), stripped for every
functional part, plus new wear parts. Buy the wear parts twice, because you will tear
one during assembly: gaskets `OD-G02`, `OD-G03`, `OD-G05`, generator gaskets `OD-H13`,
O-rings `OD-W22` and the brew gasket (SOURCING_GUIDE §4 tip 3).

Before and during teardown, **photograph every stage, especially the wiring, the tube
runs and the group head stack**. The repository has no wiring diagram yet (see 6.10),
and the donor is the reference.

For v1 (electronics path 1, no steam) you need the BOM's OEM rows for the hydraulic
core `OD-H01`…`OD-H25`, the group head and portafilter `OD-G02`…`OD-G07`,
`OD-G10`…`OD-G12`, the water path `OD-W01`…`OD-W23`, the electronics `OD-E01`…`OD-E09`
and the drip tray and cup rest `OD-C21`…`OD-C24`. The quantities and OEM codes are in
[BOM.md](BOM.md).

### 3.2 Hardware (`OD-F` rows)

Quantities from `bom.csv`. The "used for" column comes from the BOM text and
`chassis/README.md`.

| Part | Item | BOM qty | Used for |
|---|---|---|---|
| `OD-F01` | M3 heat-set insert, Ø4.0 bore × 6 | ~70 | every printed screw joint (count in §5) |
| `OD-F02` | M3×8 screw, ISO 7380 / DIN 912 A2 | ~65 | mounts, tray, panels, brackets, lid, housing to carrier |
| `OD-F03` | Acrylic sheet 3 mm | per design | **not used**: the side panels are printed (status `deferred`) |
| `OD-F04` | Food-safe silicone tube 4×2 mm | 1 m | routing reserve |
| `OD-F05` | High-temp epoxy (125 °C / 15 bar) | 1 | blanking port B of `OD-H23` (the steam port) in v1 |
| `OD-F06` | 6.3 mm insulated spade terminals + 105 °C wire | 1 set | your own looms, where an OEM loom does not reach |
| `OD-F07` | Metal spacer Ø7 × 10.10 (Ø4 bore), cut +0.10/−0 | 1 | `OD-C04` standoff S1 to the thermoblock |
| `OD-F08` | Metal spacer Ø7 × 37.70 (Ø4 bore), cut +0.10/−0 | 1 | `OD-C04` standoff S2 to the thermoblock's mid lug |
| `OD-F09` | Cable tie 4.8 mm | 3 | 2 × `OD-C03` pump strap, 1 × `OD-C14` grommet |
| `OD-F15` | Cable tie 2.5 mm | 2 | `OD-C08` loom slots (2.0 × 4.0) |
| `OD-F16` | Self-tapping screw Ø3.5 | 2 | `OD-C04` into the thermoblock through the spacers: S1 ≈ 22, S2 ≈ 50 long (A-04; measure the donor's screws) |
| `OD-F10` | M3×12 screw | 8 | 4 × `OD-C02` from below the plate, 4 × `OD-C15` feet from the plate top |
| `OD-F11` | M3×6 screw | 2 | `OD-E01` board holes H1/H2 into the `OD-C08` standoffs |
| `OD-F12` | M3 hex nut, ISO 4032 A2 | 4 | captive in the `OD-C15` feet |
| `OD-F13` | M3×18 screw, ISO 4762 / DIN 912 | 2 | `OD-E02` button board into the `OD-C09` bosses |
| `OD-F14` | M3×10 screw, ISO 7380 | 4 | `OD-T01` rig into the `OD-G01` inserts (bench only) |

Notes:

- **The OD-C04 thermoblock screws (`OD-F16`)** are an assumption (`OD-C04` A-04):
  Ø3.5 self-tapping screws into the thermoblock's own pilot holes, about 22 long for S1
  and about 50 long for S2. Measure the OEM screws before you choose.
- **The OEM `OD-G04` screws** (two self-tapping screws, Ø3.5 assumed, `OD-G01` A-26)
  come from the donor.
- **`OD-C08` tie slots:** the slots are 2.0 × 4.0 and the spec calls for a 2.5 mm tie.
  Use the 2.5 mm ties `OD-F15` there; a 4.8 mm `OD-F09` will not pass them.
- **`OD-C15` feet:** if you use a nylon-insert nut (ISO 10511), you need an M3×16
  instead of the M3×12. A drop of medium threadlocker on the M3×12 is the spec's
  suggestion against creep (`OD-C15` A-07).

Tally of the screws this guide uses: 50 × `OD-F02`, 8 × `OD-F10`, 2 × `OD-F11`,
2 × `OD-F13` and 4 × `OD-F14`. The BOM quantities include spares.

### 3.3 Tools

- **Printers.** The specs name two: a **Creality K1C** (enclosed; needed for ASA and PC)
  and an **Anycubic Kobra Max 3** (large panels). Neither printer's build volume is in
  the workshop's machine files. The specs assume 220 × 220 × 250 for the K1C and
  420 × 420 × 500 for the Kobra Max 3. Check that your printer matches before you print
  the large parts.
- **Heat-set insert tool** (soldering iron with an M3 insert tip). The insert
  temperature is not given in the repository: use the insert maker's figure.
- **Calipers** (0.05 mm resolution, as in CONTRIBUTING's scan rules).
- **Hex keys and drivers** for the M3 heads you stock. The `OD-T01` procedure uses a
  2 mm key for its ISO 7380 M3 × 10.
- **A long M3 driver with ≥ 210 mm reach** for the four `OD-C05` foot screws. Their
  heads sit 203–204.4 mm below the carrier's top face (`OD-C05` RV02 F5).
- Side cutters for the cable ties; a multimeter for the earth continuity checks.
- For the bench test: the `OD-T01` parts list in
  [`chassis/OD-T01_TEST_PROCEDURE.md`](../chassis/OD-T01_TEST_PROCEDURE.md) (hand
  hydrostatic test pump, 0–25 bar gauge, bleed valve and tee, tube rated ≥ 25 bar,
  stainless 51 mm blind basket, polycarbonate shield, safety glasses).

## 4. Printing

The STL/3MF files are in `chassis/`. For each part, the table gives the printer,
orientation and supports from its spec §3/§4 and `chassis/src/<part>/README.md`.
Layer height, wall count, nozzle and bed temperatures are **not given** in the
repository, except the 100 % infill for `OD-T01`. Use your slicer's defaults for the
material, and use generous walls around the insert holes.

| Part | Name | Qty | Printer | Orientation | Supports | Notes | Service material (BOM) |
|---|---|---|---|---|---|---|---|
| `OD-G01` | Group head housing | 1 (+1 ASA) | K1C | mouth up, rear face on the bed | under the three lugs and three stop blocks only | PLA = dry fit only. Print the ASA housing for `OD-T01` and the machine. Lug roots are sharp, no fillet (RV01 F4) | ASA |
| `OD-C01` | Base plate | 1 | Kobra Max 3 | flat, bottom face on the bed | none | brim against warp (A-14); 240 × 405 × 6. **Check for 38 insert holes first** (§1) | PETG or ASA |
| `OD-C02` | Wet/electric bulkhead | 1 | K1C | standing on its rear end (z −240), 215 × 14 footprint, 210 tall | none | the four Ø14 windows have 45° gable roofs | ASA |
| `OD-C03` | Pump cradle | 1 | Kobra Max 3 (spec) | foot on the bed, saddles up | none | tie slots have 45° roofs | PETG |
| `OD-C04` | Thermoblock mount | 1 | K1C | plate back face on the bed, foot standing up | none | PLA = dry fit only | ASA / PC |
| `OD-C05` | Group head carrier | 1 | K1C | plate on the bed, foot up; 110 × 152 on the bed, 210 tall | none | the eight counterbore floors bridge (named exception). PLA = dry fit only | ASA |
| `OD-C07` | Valve and flowmeter mount | 1 | Kobra Max 3 (also fits the K1C) | bottom face on the bed | under the deck and the three hook catches only | | PETG |
| `OD-C08` | Electronics bay tray | 1 | K1C | lying on the wall's outer face (x 73); 92 × 160 on the bed, 39 tall | none | | PETG |
| `OD-C09` | Front panel | 1 | Kobra Max 3 | lying on the front face; 232 × 215 on the bed, 25 tall | none | brim if the plate lifts; about 119 g | ASA |
| `OD-C10` | Top panel (lid) | 1 | Kobra Max 3 | upside down, top face on the bed; 240 × 405, 39.5 tall | none | brim against warp (A-08) | PETG |
| `OD-C11` | Back panel | 1 | Kobra Max 3 | lying on the outer face; 232 × 215 on the bed, 25 tall | none | | PETG |
| `OD-C12` | Left side panel | 1 | Kobra Max 3 | lying on the outer face; 385 × 219 on the bed, 10 tall | none | brim against warp (A-11) | ASA / PETG |
| `OD-C13` | Right side panel | 1 | Kobra Max 3 | as `OD-C12` | none | brim against warp | ASA / PETG |
| `OD-C14` | Cord grommet half | 2 | K1C | standing on the flange's outer face | none | two identical halves | TPU |
| `OD-C15` | Foot | 4 | K1C (direct drive for TPU) | top face (the face against the plate) on the bed | none | the nut enters from the counter side | TPU 95A |
| `OD-C16` | Side panel corner bracket | 6 | K1C | on its underside | none | three per side; the left ones are the same part turned 180° | ASA / PETG |
| `OD-T01` | Pressure-test rig | 1 | Kobra Max 3 | lying on its rear face (z −60); 240 × 160 on the bed, 120 tall | none | **100 % infill** (or at least solid round the four counterbores); brim if it lifts; about 1.4 kg of PLA | PLA (cold water only) |

The `OD-C15` spec designs the foot in TPU 95A, and its nut pocket (5.60 across flats
for a 5.50 nut) grips by the TPU's give. A PLA foot printed "for now" is a hard puck,
and the nut fit is untested in PLA.

## 5. Heat-set inserts

All inserts are `OD-F01`: M3, 5.7 long, Ø4.6 outside, pressed into Ø4.0 holes (`OD-C01`
A-11; the stocked insert's datasheet is not confirmed yet). Set each one square and
flush with the face it is driven from.

**Rule: before you set any inserts, check each insert pattern with calipers against
the part that bolts onto it** (hole spacing and position from an edge), and fit the
mating part dry. A misplaced insert is hard to recover from.

| Where | Count | Driven from | Takes |
|---|---|---|---|
| `OD-C01` plate: `OD-C05` carrier | 4 | plate top | (±35, z −40), (±35, z −60) |
| `OD-C01`: `OD-C04` thermoblock mount | 4 | plate top | (±40, z −148), (±40, z −114) |
| `OD-C01`: `OD-C03` pump cradle | 4 | plate top | (−4 / 37, z −239 / −171) |
| `OD-C01`: `OD-C07` valve and flowmeter mount | 4 | plate top | (−113 / −71, z −42 / −148.5) |
| `OD-C01`: `OD-C08` tray (rev B) | 4 | plate top | (88 / 106, z −222 / −78) |
| `OD-C01`: `OD-C11` back panel (rev B) | 4 | plate top | (±81 / ±95, z −282) |
| `OD-C01`: `OD-C16` brackets (rev B) | 6 | plate top | (±104.5, z −262 / −15 / +62) |
| `OD-C01`: `OD-C09` front panel (rev B) | 4 | plate top | (±85 / ±95, z +77) |
| `OD-C02` base rail | 4 | rail underside (y 0) | M3×12 from below the plate |
| `OD-C02` top rail | 2 | rail top (y 215) | lid screws at (65, z −60 / −210) |
| `OD-C07` deck | 2 | deck underside | `OD-H22` ear screws |
| `OD-C08` standoffs H1, H2 | 2 | standoff tips | `OD-E01` board |
| `OD-C09` bosses | 2 | boss end faces | `OD-E02` button board |
| `OD-C11` ledge bosses | 2 | ledge top (y 215) | lid rear screws at (±90, z −293) |
| `OD-C16` brackets | 6 (1 each) | bracket outer face | side panel screws |
| `OD-G01` rear face | 4 | rear face | `OD-C05` (machine) or `OD-T01` (bench), at (±44, ±44) |
| **Total** | **58** | | 34 in the plate, 24 in other parts |

Notes:

- **Leave the four plate holes on the bulkhead line (x 65, z −45 / −105 / −165 / −225)
  empty.** They are clearance holes for the `OD-C02` M3×12 screws from below, and the
  inserts for that joint sit in the bulkhead's rail. So the plate's 38 holes take 34
  inserts.
- `OD-C07`'s two deck inserts go in from below. Set them before the mount is screwed to
  the plate.
- `OD-G01`'s insert holes have no depth margin and open on the flange front (RV01 F6).
  Press the inserts flush and no deeper. Each housing you print (the PLA fit check, the
  ASA test and service housing) needs its own four.
- `OD-C02`: an M3×12 ends exactly on the base-rail bore floor (RV01 F2). Before the
  final assembly, check that each screw clamps rather than bottoms out. A shorter screw
  or a deeper bore is the Usta's call.
- `OD-C08`: an M3×8 through the board bottoms 0.44 past the bore floor, so use M3×6
  (`OD-F11`), or an M3×8 with a washer ≥ 0.5 (RV01 F3).

## 6. Assembly sequence

The machine is built up from the plate. The order below follows the constraints the
part jobs recorded (chassis/README "Keep-outs" and the specs' assembly notes). Where
the order is this guide's inference rather than a recorded constraint, the step says
so. Dry-fit every part with its OEM neighbour before you drive screws.

Placement summary (plate frame, top view):

| Zone | x | z | What |
|---|---|---|---|
| Front, centre | ±75 | −15 … +85 | drip tray zone (keep the plate top clear) |
| Front-centre, behind the tray | ±55 | −70 … −26 | `OD-C05` foot (group head carrier) |
| Centre | ±50 | −157 … −107 | `OD-C04` foot (thermoblock mount) |
| Rear | −10 … 42 | −245 … −165 | `OD-C03` foot (pump across the back) |
| Left | −117 … −67 | −154 … −35 | `OD-C07` (valve and flowmeter) |
| Bulkhead line | 59 … 71 | −240 … −30 | `OD-C02` |
| Right (electric zone) | 73 … 112 | −230 … −70 | `OD-C08` with the board |
| Rear strip | ±70 | −305 … −250 | reserved tank zone (the tank now stands on the table) |

### 6.1 Plate: inserts and checks

Parts: `OD-C01`, 34 × `OD-F01`.

1. Check the plate: 240 × 405 × 6, 38 Ø4.0 holes, 4 Ø3.4 feet holes at (±110, +90) and
   (±110, −295), 2 Ø8 drain holes at (−80, −120) and (−80, −230).
2. Lay it on a flat surface and check for warp (record it: `OD-C01` REQ-09, §7.4).
3. Set the 34 inserts from the top face (§5). Leave the four x 65 holes empty.

### 6.2 Bulkhead `OD-C02`

Parts: `OD-C02` with its 6 inserts set, 4 × `OD-F10` M3×12.

The bulkhead is screwed from **below**: turn the plate over (`OD-C02` A-03), so this is
easiest while the plate is still bare (a recorded constraint).

1. Stand the bulkhead on the plate with its base rail over the four x 65 holes, wet face
   (x 59) toward the left. The rail's bores line up with the plate holes.
2. Turn the plate and bulkhead over together. Drive the four M3×12 up through the plate
   into the rail inserts. The heads sit under the plate, where the feet lift it clear of
   the counter.

### 6.3 Feet `OD-C15`

Parts: 4 × `OD-C15`, 4 × `OD-F10` M3×12, 4 × `OD-F12` nut.

1. Push a nut into each foot's hex pocket from the counter side.
2. Hold each foot under its Ø3.4 hole and drive the M3×12 from the plate top. The screw
   pulls the nut up onto its seat. Snug, not crushed. Add threadlocker if you like
   (A-07).
3. **Keep-out:** a Ø8 × 2.0 cylinder above each foot hole on the plate top stays free
   for the screw head (`OD-C15` A-09). Nothing else may sit there.

### 6.4 Pump cradle `OD-C03` and pump `OD-H01`

Parts: `OD-C03`, `OD-H01` in its rubber sleeve `OD-H02`, 4 × `OD-F02`, 2 × `OD-F09`.

1. Screw the cradle to the plate: 4 × M3×8 from above through the foot into the inserts
   at (−4 / 37, z −239 / −171).
2. Lay the pump in its sleeve on the two saddles. The pump axis runs along X at y 40,
   terminal block up and outlet toward −X (the valve side) (`OD-C03` A-08). The OEM
   spring `OD-H03` is not used by this cradle (A-05).
3. Pass two 4.8 mm cable ties through the post slots and over the sleeve, then pull them
   tight enough to hold the pump without crushing the sleeve.

The sleeve's outside diameter (53.3) is an assumption that no input gave. If the
saddles do not fit your sleeve, measure it and report it rather than forcing it
(`OD-C03` A-03).

### 6.5 Thermoblock mount `OD-C04` and thermoblock `OD-H11`

Parts: `OD-C04` (ASA/PC for any powered use), `OD-H11` with its NTC `OD-H16` on bracket
`OD-H17` and TCO `OD-H18` on bracket `OD-H19`, spacers `OD-F07` (10.10) and `OD-F08`
(37.70), 2 × `OD-F16` thermoblock screws (see §3), 4 × `OD-F02`.

The repository does not record an order for this joint. This order is inferred from the
geometry: the rear foot screws sit under the thermoblock, and the thermoblock screws are
driven from behind the mount's rear plate, toward where the pump now sits.

1. Cut the spacers to length (+0.10/−0) and deburr them.
2. Screw the mount to the plate first: 4 × M3×8 from above into the inserts at (±40,
   z −148 / −114). The rear plate faces the pump and the standoffs face the group head.
3. Offer the thermoblock: axis horizontal along Z, pipes and terminals up (`OD-C04`
   A-07). Put S1's 10.10 spacer between standoff S1 and the base face, and S2's 37.70
   spacer between standoff S2 and the mid-lug underside. Drive the two screws from the
   rear face of the mount through the standoffs and spacers into the thermoblock's blind
   holes.
4. Check the air gap: no printed surface may come within 10 mm of the casting (`OD-C04`
   REQ-01; the standoff tips sit 10.10 from it). The lowest point of the casting sits
   16.5 above the plate.

If the pump blocks a driver behind the mount, fit the thermoblock before 6.4.

### 6.6 Group head: housing `OD-G01` on carrier `OD-C05`

Parts: `OD-G01` (ASA for any wet use; PLA only for a dry fit), its 4 inserts, OEM stack
`OD-G04` with its two OEM screws, gaskets `OD-G02`, `OD-G03`, `OD-G05`, diffuser `OD-G06`;
`OD-C05`; 8 × `OD-F02`.

**Fit only a housing that has passed the `OD-T01` test (§7.1) into a machine that will
see water.**

1. Assemble the OEM group head stack into the housing as it came out of the donor
   cup: the gasket support `OD-G04` on the floor with its two screws through the pair-B
   holes from the rear, plus the gaskets and the diffuser. The repository does not
   document the stack order, so follow your teardown photos.
2. Test the bayonet dry: insert the portafilter `OD-G10` turned about −50°, lift it and
   lock it. Note the handle angle at lock. It should lock turned about 28° toward the
   right (`OD-C09` A-05).
3. On the bench, put the housing's rear face against the underside of the carrier's plate
   (the designed contact). Drive 4 × M3×8 from above through the Ø6.5 counterbores into
   the housing's inserts at (±44, ±44).
4. Stand the carrier on the plate with its foot over the inserts at (±35, z −40 / −60).
   The group head axis is vertical with the mouth down, over the tray zone. Drive the four
   foot screws (M3×8) through the **hatch** with the ≥ 210 mm driver.
5. Check: the housing's rear face is about 205 above the plate, and the mouth face about
   176.8 (`OD-C05` A-03; this layout still awaits the Usta's confirmation).

The column's foot is an undrained trough with the screw heads at its lowest point
(`OD-C05` RV02 F2). Keep water from falling through the hatch, and check it after the
leak tests.

### 6.7 Valve and flowmeter mount `OD-C07`

Parts: `OD-C07` with its 2 deck inserts set (from below, before this step), flowmeter
`OD-H24`, 3-way valve `OD-H22`, 6 × `OD-F02`.

1. Screw the mount to the plate: 4 × M3×8 from above through its footprint holes into
   the inserts at (−113 / −71, z −42 / −148.5). The flowmeter end faces the front and the
   valve end faces the pump.
2. Press the flowmeter down onto its pedestal until the three hooks catch the flange.
   The axis is vertical, the pipes face the tank side (in the mount's frame, −Y) and the
   connector faces the valve (`OD-C07` A-21).
3. Slide the valve into the deck slot at its seated height (along the mount's −Y, i.e.
   from the left side of the machine), ports under the deck and drive tube up. Drive
   2 × M3×8 down through the ears into the deck inserts.
4. **Do this before the left side panel `OD-C12` goes on.** With its screws loose, the
   valve slides out along the mount's +Y, toward the left panel (A-22).

The OPV sits inside the valve's drive tube and is reached from above with the lid off
(`OD-C07` A-10).

### 6.8 Electronics tray `OD-C08` and board `OD-E01` (path 1)

Parts: `OD-C08` with its 2 standoff inserts, OEM power PCB `OD-E01`, 4 × `OD-F02`,
2 × `OD-F11` M3×6, 2 × `OD-F15` ties for the loom slots.

1. Screw the tray to the plate: 4 × M3×8 from above through the flange into the inserts
   at (88 / 106, z −222 / −78). The wall stands at x 73…76, 2 mm from the bulkhead's
   rail.
2. Put the board on edge, solder side toward the tray's wall, with the H1/H2 edge
   (connectors J1…J3) toward the front. Pins on standoffs H5/H6 go through the board's
   holes. Fasten H1 and H2 with M3×6 (`OD-F11`). The spec suggests a plastic or fibre
   washer under each head on the component side (`OD-C08` A-04).
3. The solder side keeps 6.44 of air to the wall. Nothing may touch it except the
   standoffs.
4. **Keep-out:** the tray with the board occupies x 73…112, z −230…−70, y 0…92 (board to
   x ≈ 109.3). Keep wires and other parts out of this box.

### 6.9 Tubing

Follow [WATER_FLOW.md](WATER_FLOW.md) and the donor. Use the OEM tubes with their bushes,
springs `OD-W21`, O-rings `OD-W22` and clips `OD-W23`. Route at room temperature and
with no water in the system.

| # | From → to | Tube |
|---|---|---|
| 1 | tank `OD-W01` → flowmeter `OD-H24` | `OD-W11` (L270), through `OD-C11`'s tube hole |
| 2 | flowmeter → pump `OD-H01` | `OD-H25` |
| 3 | pump → 3-way valve `OD-H22` | TUBE 1 (up to 15 bar) |
| 4 | 3-way valve → thermoblock `OD-H11` | TUBE 2 |
| 5 | 3-way valve → tank (bypass return) | TUBE 3, through `OD-C11`'s other tube hole |
| 6 | thermoblock → connector `OD-H23` port A | TUBE 4 (hot) |
| 7 | connector port C → group head | TUBE 7 (hot) |
| 8 | connector port B | **blanked in v1** with `OD-F05` epoxy (steam is phase 2) |

- Only `OD-W11` and `OD-H25` have been matched to BOM lines. TUBE 1…7 are to be matched
  to `OD-W12`…`OD-W15` during teardown (WATER_FLOW.md). Record the matches you find.
- **TUBE 7** enters the carrier's column through its rear window (x ±10, machine y 40…70),
  rises inside the column, leaves through the hatch and drops into the hub window from
  above to the OEM water connection (`OD-G07` gasket, `OD-H14`, `OD-H15`) on `OD-G04`'s
  hub tube (`OD-C05` A-06, A-07). The lid leaves 37 mm of headroom above the carrier's
  plate for this loop (`OD-C10` A-06).
- The valve's hose ports sit about 16 mm above the plate, with the mount's window open
  below them for the bend (`OD-C07` A-19).
- The anti-drip valve `OD-H21` "sits in the water path, not on the mount" (chassis/README).
  WATER_FLOW.md does not show where. Follow the donor.
- The tank tubes leave through the two Ø12 holes in `OD-C11` at (−100, 30) and (−84, 30)
  (fit them when the back panel goes on, 6.11). The tank dock `OD-C06` is deferred and the
  tank stands on the table; how its seat `OD-W03` is held is not designed yet.
- Leave both drain holes in the plate (−80, −120 and −80, −230) open, and keep tubes off
  them.

### 6.10 Wiring

**No wiring diagram is in the repository yet.** [`electronics/README.md`](../electronics/README.md)
is a placeholder for phase 4. Do not improvise: wire path 1 exactly as the donor was
wired, with the OEM PCB `OD-E01`, the button board `OD-E02` and the OEM looms
`OD-E07`…`OD-E09`. Use your teardown photos and have a competent person check the result
(§2). Use `OD-F06` spades and 105 °C wire only where an OEM loom is too short, and match
the OEM conductor and terminal.

What the chassis provides:

- Four Ø14 wire windows through the bulkhead `OD-C02` (no printed grommets; fit rubber
  grommets or tie the wires clear of the edges, `OD-C02` A-13): (y 150, z −200) pump;
  (y 150, z −130) thermoblock heater and thermostat; (y 150, z −60) group head side;
  (y 60, z −55) valve and flowmeter wires along the front (`OD-C02` A-04).
- Tie slots on `OD-C08` above the board's top edge (two pairs at y 86…90).
- The mains cord `OD-E06` enters through `OD-C11`'s Ø12 hole at (95, 30) in the grommet
  `OD-C14` (6.11).

Rules: the TCO `OD-H18` stays in series in the heater circuit. Earth goes to every metal
part, and you check it with a meter. No mains conductor may touch the board's solder
side or lie on the wet side of the bulkhead.

Not designed yet: the microswitch `OD-E03`, the on/off push button `OD-E04` and the
unipolar switch `OD-E05`. The `OD-C08` spec assigns them to the front panel, but `OD-C09`
has holes only for `OD-E02`'s three buttons. Until a panel revision gives them a place,
decide where they sit with the person doing the electrics.

### 6.11 Back panel `OD-C11` and cord grommet `OD-C14`

Parts: `OD-C11` with its 2 ledge inserts, 2 × `OD-C14`, 4 × `OD-F02`, 1 × `OD-F09`.

1. Thread the tank tubes through the two Ø12 tube holes, and the mains cord's inner end
   through the Ø12 cord hole at (95, 30) from outside.
2. Screw the panel to the plate: 4 × M3×8 from above through the floor flanges into the
   inserts at (±81 / ±95, z −282). Each screw is 5 in front of the top ledge, so a
   straight driver reaches it.
3. Grommet: put the two halves round the cord outside the machine and push them in along
   the cord until the flanges meet the wall. Tie one 4.8 mm tie round the groove just
   inside the wall, **head upward** (away from the gusset below), pull it tight and cut
   the tail. Nothing may sit within 0.5 of the tie head.
4. Check grip: a firm pull on the cord must not move it (`OD-C14` REQ-05, §7.4).

The printed Ø12 holes may come out 0.1…0.2 undersize (`OD-C14` A-01). Ream them rather
than force the grommet.

### 6.12 Front panel `OD-C09` and button board `OD-E02`

Parts: `OD-C09` with its 2 boss inserts, `OD-E02`, 4 × `OD-F02`, 2 × `OD-F13` M3×18.

**Order (`OD-C09` A-14): screw the panel to the plate before the board goes on.** The
board lies over the left flange screws.

1. Stand the panel on the plate's front edge (wall at z +94…+97) and drive 4 × M3×8 from
   above through the floor flanges into the inserts at (±85 / ±95, z +77).
2. With the lid off, offer the button board from behind, its three caps through the three
   Ø15 holes in the left pillar (1 cup at the top, 2 cups in the middle, steam at the
   bottom). Drive the two M3×18 from the board's back into the boss inserts.
3. Connect the board to `OD-E01` with its OEM loom (6.10).
4. Lock the portafilter and check the handle clears the window. At a lock 10° past the
   new-gasket position, the clearance is 2.5. It touches at +12° (`OD-C09` RV01 F2), so
   recheck as the brew gasket wears.

Keep free: the drip tray slot (x ±74.8, y 0…49.8) and the phase-2 steam knob place
(Ø32 about x +95.5, y 140) on the right pillar.

### 6.13 Side panels `OD-C12`, `OD-C13` and brackets `OD-C16`

Parts: 6 × `OD-C16` with their inserts, `OD-C12`, `OD-C13`, 12 × `OD-F02`.

Order (side panels spec, §4): brackets first (lid and panels off), then the panels, then
the lid.

1. Screw the six brackets to the plate: one M3×8 each from above through the bracket's
   counterbore into the inserts at (±104.5, z −262 / −15 / +62). The insert bore in each
   bracket faces outward, toward its panel.
2. Fit the valve (6.7) before the left panel. `OD-C12` has a 0.9 relief over `OD-C07`.
3. Offer each panel from outside against its three brackets and drive 3 × M3×8 from
   outside through the panel's Ø3.4 holes (y 10) into the bracket inserts.
4. Small openings stay at the corners: about 4 at each front corner and about 4 × 4 at
   each rear corner, closed from above by the lid. A small printed cap can close them
   later (chassis/README).

### 6.14 Drip tray and cup rest

Slide the drip tray `OD-C21` (with float `OD-C22` and cup holders `OD-C23`/`OD-C24`)
into the tray slot under the group head. Its zone is x ±75, z −15…+85 on the plate, with
the cup rest top ≤ 36.9 above the plate (`OD-C01` A-06). The tray is not scanned yet
(issue #9).

### 6.15 Lid `OD-C10`

Parts: `OD-C10`, 4 × `OD-F02`.

1. Lower the lid: its side skirts close over the side panels' 60° lips (0.40 per side).
   The front skirt rests on `OD-C09`'s top edge (y 215), with no screws at the front.
   The lid rests on the panel tops.
2. Drive 4 × M3×8 from above through the counterbored columns: two into `OD-C02`'s
   top-rail inserts at (65, z −60 / −210), two into `OD-C11`'s ledge inserts at
   (±90, z −293).
3. The lid's two rest pads stand 0.5 above the carrier's plate, so a hand pressing the
   lid bears on the carrier.

Service: the lid comes off with 4 screws. That gives access to the OPV, the housing
screws and the carrier hatch.

## 7. First power-up and tests

Test in this order. Behind an RCD, with the shield and glasses for anything under
pressure. Stop at the first fault.

### 7.1 `OD-T01` bench pressure test of the ASA housing

Before the housing goes into a machine that will see water, follow
[`chassis/OD-T01_TEST_PROCEDURE.md`](../chassis/OD-T01_TEST_PROCEDURE.md) in full. In short:

- Print the rig in PLA at 100 % infill and screw it to the bench.
- Hang the ASA housing (with its inserts and `OD-G04`) under the plate with
  4 × `OD-F14` M3×10. Snug them, do not crush.
- Feed the hub through the OEM water connection, close the mouth with a blind basket in
  the portafilter, bleed the air out, and use cold tap water only.
- Behind the shield, raise the pressure in steps of 3, 6, 9, 12 and 15 bar, holding each
  for 60 s, then hold 15 bar for 5 min.
- **Stop at once** on a gauge drop, a crack or whitening, a weep at the lugs or inserts, a
  screw head sinking into the plate, or the plate bowing.
- **Pass:** 15 bar for 5 min with no crack, no step on the gauge and no weep at the lugs.

Record what the procedure lists (date, rig version v02, filament, infill and settings,
washers or not, handle angle at lock, gauge readings per step, highest pressure held,
photos before and after). File the result in `chassis/reports/OD-G01_group_head_housing/`
(REQ-12) and `chassis/reports/OD-T01_pressure_test_rig/` (REQ-08).

### 7.2 Cold leak check in the machine

With the ASA housing fitted, the lid off and the machine on its feet, check every joint
of the water path for drips: tube ends, the valve, the flowmeter, the thermoblock
connections, the hub connection and the blanked steam port. Also check that a drip on the
wet side runs to the drain holes and not under the bulkhead (`OD-C02` A-12), and that
nothing collects in the carrier's foot.

**The repository has no cold leak-check procedure yet.** In particular, it does not say
how to run the pump with the OEM board (path 1) without the board also heating the
thermoblock. Agree the method with the person doing the electrics before mains is
applied. Until then, a check without mains is the safe minimum: fill the tank and look
for drips.

### 7.3 First hot run

Only when §7.1 has passed, §7.2 is dry, and `OD-G01`, `OD-C04` and `OD-C05` (and, per
§2, `OD-C02`) are in their service material. The machine must also be checked by a
competent person (earth continuity to every metal part, TCO in circuit, insulation)
and run behind an RCD.

- Heat up with the lid off and watch the thermoblock zone, the mounts and the carrier.
- Pull the first shots with a basket, then look again for leaks hot.
- Take the temperature readings the specs ask for: the front panel's top bar after a
  run of shots (`OD-C09` A-11), under the lid (`OD-C10` A-10), inside the machine at the
  side panels (`OD-C12`/`OD-C13` A-08), and the carrier's column if TUBE 7 warms it
  (`OD-C05` RV02 F1).

### 7.4 What to record so parts can move to `validated`

`validated` needs a print and a fit check by the Usta, and for the group head the
`OD-T01` test (chassis/README). File the record under `chassis/reports/<part>/`, with a
photo of the fit, and update the part's `status` in `docs/bom.csv` in the same PR
(CONTRIBUTING).

| Part | Bench row | What to check and record |
|---|---|---|
| `OD-G01` | REQ-12 brew load (Hard) | the `OD-T01` result (§7.1) |
| `OD-T01` | REQ-08 strength | no visible yield or crack at 15 bar |
| `OD-C01` | REQ-09 flatness | warp of the printed plate, and whether the mounts seat without rocking |
| `OD-C02` | REQ-09 stiffness | no rattle or visible flex with the panels on |
| `OD-C03` | REQ-09 vibration | vibration passed to the chassis with the sleeve fitted, at the first run |
| `OD-C04` | REQ-08 heat | the mount holds the thermoblock through a heating cycle without softening (service material only) |
| `OD-C05` | REQ-09 stiffness | lock the portafilter and push the handle: no visible flex |
| `OD-C08` | REQ-06 plug push | the board does not flex when a faston is pushed onto the farthest tab |
| `OD-C09` | REQ-08 stiffness | no visible flex under a button press or with the pump running |
| `OD-C10` | REQ-08 stiffness | the lid does not sag or rattle |
| `OD-C11` | REQ-09 stiffness | the panel does not drum or flex |
| `OD-C12`, `OD-C13` | REQ-08 stiffness | no flex or drumming with the lid on; a hand on a side does not shift the lid |
| `OD-C14` | REQ-05 grip | the tied grommet holds against a firm pull and does not turn |
| `OD-C15` | A-06, A-07 | the nut grips in its pocket; the screw has not loosened after a month |
| `OD-C07` | A-15, A-19 | the hooks snap without cracking; the hoses bend without kinking |

With each record, list the caliper readings that close the part's assumptions (§8).

## 8. Open items

These are assumptions the Usta still has to confirm with calipers, a print or a
decision. Each is OPEN in the part's spec §6 unless noted. The specs have the full
lists.

**All parts**

- Scan scale and units are unconfirmed on every scanned OEM part. Calipers are needed on
  every interface.
- The M3 insert datasheet (5.7 long, Ø4.6 in a Ø4.0 hole) is unconfirmed.
- The K1C and Kobra Max 3 build volumes are not in the machine files.
- The Usta still has to name the service filament for each part.

**`OD-G01` group head housing**

- Calipers or a protractor on the donor cup: lug inner radius 31.68 (A-02), bore 37.10
  (A-03), lug angles (A-04), lug underside profile (A-05), stop block (A-06), shelf
  −14.10 (A-07), pocket and lip ring (A-08, A-09).
- `OD-G04` screws Ø3.5 assumed (A-26), ear geometry and pitch (A-19, A-25), brewing
  gasket compression (A-27, needs `OD-G02` measured).
- Brew load (A-21): needs the `OD-T01` test.
- Spec 1.4 (the corrected sentence that the axis is vertical) awaits ratification.

**`OD-C01` base plate**

- Revision B (38 holes) must land on main. The 18 new holes still need a through-or-blind
  decision.
- The machine layout (group head vertical, housing rear face 205 above the plate, pump
  and thermoblock poses) awaits the Usta's confirmation (A-01…A-03, A-16).
- Drip tray zone (A-06; tray scan, issue #9), drainage (A-13), flatness (REQ-09).

**`OD-C02` bulkhead**

- The M3×12 ends exactly on the bore floor (A-03, RV01 F2). Window use and grommets
  (A-04, A-13) are open, and so is drainage (A-12).

**`OD-C03` pump cradle**

- Coil Ø47.3 (A-02), sleeve OD 53.3 (A-03, no input gives it), frame side plates
  (A-04), tie path (A-07), and whether the pump is an EP5 or an EX5 (A-15).

**`OD-C04` thermoblock mount**

- Thermoblock screw holes (A-03) and screw type and length (A-04: Ø3.5 self-tapping
  vs. chassis/README's M3).
- Spacer lengths 10.10 / 37.70 and the 10.10 air gap (A-05).
- NTC and TCO brackets `OD-H17`/`OD-H19` are not scanned (A-06).
- The `OD-H11` STEP is not a valid solid (A-14).

**`OD-C05` group head carrier**

- Group head height (A-03).
- The water connection parts must fit within r 30 of the axis (A-06, not scanned).
- TUBE 7 route (A-07).
- A drain for the foot trough (RV02 F2).
- The counterbore floors' named exception must be signed (F4).
- The ≥ 210 mm driver (F5).

**`OD-C07` valve and flowmeter mount**

- Ear holes (A-02), flowmeter cup and flange (A-06: cup ≈ Ø31.5, flange ≈ Ø40.6, rim to
  flange top 19.9) and base pins (A-07).
- OPV position (A-10).
- The snap-hook strain limit was set for PETG (A-15); the part is now PLA.
- Hose bend space (A-19).

**`OD-C08` electronics bay tray**

- Board hole pitch H1–H2 and H5–H6 by calipers: the pins tolerate about 0.03 (A-02,
  RV01 F4).
- The board's solder side (A-05).
- Wiring, mains entry and venting (A-11).

**`OD-C09` front panel**

- `OD-E02` geometry (A-03) and the button layout (A-04).
- Portafilter lock angle (A-05, RV01 F2).
- Top-bar temperature (A-11).
- No place yet for `OD-E03`…`OD-E05`.

**`OD-C10` top panel**

- Headroom for the tube loop (A-06) and the temperature under the lid (A-10).

**`OD-C11` back panel**

- Cord (A-03), tank tubes in hand (A-04), venting at the first power-on (A-06), and
  clearance to the pump's rear end (A-07).

**`OD-C12`, `OD-C13`, `OD-C16` side panels and brackets**

- Rear corner gap (A-03), the temperature inside the running machine (A-08), the lip fit
  of 0.40 (A-14), and the bracket count of 6 instead of the BOM's old 16 (A-15).

**`OD-C14` cord grommet**

- The Ø12 hole may print undersize (A-01).
- Is the Usta's Ø7.0 cord reading the jacket diameter? (A-02)
- Squeeze when tied (A-05).

**`OD-C15` foot**

- TPU 95A in the spec vs. PLA for now (A-03).
- Machine mass taken as ≤ 8 kg (A-05).
- Nut pocket fit (A-06) and clamp creep (A-07).

**`OD-T01` rig**

- Strength (A-02), bench fittings (A-04), blind basket (A-06), bench fixing (A-11), and
  the pair-B screw heads ≤ Ø17.7 (A-12).

**Not yet designed or documented**

- Wiring diagram (`electronics/`).
- Tank dock `OD-C06` (deferred).
- Places for `OD-E03`…`OD-E05`.
- Matching TUBE 1…7 to `OD-W12`…`OD-W15`, and the position of `OD-H21`.
- A cold leak-check procedure for path 1.
- Corner caps.
