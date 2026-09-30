# DESIGN_SPEC — OD-C07 printed valve and flowmeter mount (20260930-od-c07-valve-flowmeter-mount)

Version 1.2 · RATIFIED by the Usta on 2026-09-30 (standing instruction "açık soruları A-## satırı olarak ledger'a yaz ve ilerle"; explicit confirmation of §5, §6 and the 1.1 / 1.2 amendments pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C07 is the 3D-printed PETG bracket that carries two OEM hydraulic parts of the
Open Dedica espresso machine inside the printed chassis: the 3-way valve OD-H22,
whose over-pressure valve (OPV) spring sits in the top of its drive tube and must
stay reachable without disassembly, and the flowmeter OD-H24. OD-H21 (anti-drip
valve) is not carried by this part: the Usta ruled on 2026-09-30 that it plugs into
the water path (§7). The mount seats OD-H22 by its flange back face and two ear
screws, seats OD-H24 on its rim inside a locating ring with three snap hooks over
its flange, and itself screws down to the base frame OD-C01 through four holes
whose pattern this job fixes. Done means: one valid printable solid whose seats
hold the two OEM solids as placed with the clearances of §5, every unconfirmed
value in §6.

**Deliverables** (tier M): STEP AP242 of the mount; the check assembly STEP (mount
+ OD-H22 + OD-H24 as placed); STL; build and check scripts; REPORT; sections.
Drawings and renders are not required for v01 (the part goes to the Usta's own
printer).

**Out of scope:** OD-H21 and any socket for it; the tubes and their routing (not
scanned); OD-C01, OD-C03, the pump; caliper work; drawings; renders; the OD-000
assembly (the OD-G01 thread owns it).

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Mating solid OD-H22 (3-way valve) | `00_Spec/inputs/OD-H22_3way_valve.step` | — | the Usta, 2026-09-30 (open-dedica `step/`) | CONFIRMED as the input; its numbers are §6 rows |
| Mating solid OD-H24 (flowmeter) | `00_Spec/inputs/OD-H24_flowmeter.step` | — | same | CONFIRMED as the input |
| OD-H21 not carried by OD-C07 | plugs into the water path by its clipped spigot | — | the Usta, decision card 2026-09-30 12:10 UTC | CONFIRMED |
| Fasteners | M3 heat-set inserts (OD-F01), M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` (INTAKE X-267…X-269) | CONFIRMED (project standard) |

**Coordinate frame:** the mount's bottom face (the face that rests on the OD-C01
floor) is z = 0; +Z is up in the machine and is the print direction; the origin is
on the flowmeter axis, so the OD-H24 datum frame is the mount frame translated by
(0, 0, 10.0) (its rim face lies on the pedestal top); +X runs from the flowmeter
toward the valve, whose axis is the line (62.0, 0); the OD-H22 datum frame is the
mount frame translated by (62.0, 0, 48.0) (its flange back face lies on the deck
top, drive tube up, ears along X, ports toward ±Y). θ is counter-clockwise about
+Z from +X. Every artifact of this job uses this frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c07_mount | FDM | machines/anycubic-kobra-max-3.toml (the PETG printer; build volume UNKNOWN → A-12; must also fit the K1C) | PETG (BOM) | 1270 | as printed | A-11 |

Environment: wet zone of the machine; cold water parts (≤ 15 bar in the valve, cold
in the flowmeter); a leak must drain through the part to the tray, never pool; the
valve's OPV is adjusted from above with the top panel off; the part is not near
the thermoblock (PETG allowed by chassis rule 3).

## §4 Architecture and concepts

- **C1 — flat plate with a flowmeter pedestal and a bridge for the valve (CHOSEN).**
  One solid, printed bottom face down. **Plate** 4.0 thick over x −25 … 94,
  y ±25, with a through window x 40 … 84 over the full Y width (the plate is
  then two pieces joined by the bridge). **Flowmeter station** at the origin: a
  pedestal disc R 18.0 from the plate top z 4 to z 10.0 (the OD-H24 rim annulus
  r 13.98 … 15.71 rests on it, A-06), with a relief recess R 14.10, 0.60 deep
  (floor z 9.40), in the pedestal top inside the rim for the OD-H24 underside
  ribs and hub (at 0.1 below the rim face out to r 14.056, A-06; spec 1.1);
  a locating ring wall on the pedestal, inner
  R 16.30 (cup r 15.77 at 3 mm above the rim + 0.5 gap, A-06), outer R 18.30,
  top at z 13.0, with three drain notches 2.0 wide × 0.5 high cut radially
  through the ring wall at its base (z 10.0 … 10.5) at θ 25°, 115°, 225°, so
  the annulus between the rim and the ring drains to the plate top (spec 1.1);
  two clearance through-holes for the OD-H24 base pins, Ø4.8 at
  (0.185, 0.093) and Ø3.8 at (−11.78, 0.14) (A-07), which also drain the seat
  (they open in the recess floor, length 9.4);
  three cantilever snap hooks standing on the plate top at θ 70°, 160°, 320°
  (clear of the pipes, the connector and the flange slots, A-08, A-09; the third
  hook moved from 290° in spec 1.1), each a beam 2.0 thick (radial),
  6.0 wide (tangential), inner face at R 20.87 (flange r 20.37 + 0.5), from the
  plate top z 4.0 to a catch whose underside lies at z 29.9 (the flange top
  z 19.9 + 10.0) and reaches inward 2.0 to R 18.87, with a 45° lead-in chamfer
  on the catch top; beam length L = 25.9 (root z 4.0 to the catch underside),
  L/t = 13 so Q = 1; the catch overlaps the flange by 20.37 − 18.87 = 1.5, so
  ε = 1.5 · 1.5 · 2.0 / 25.9² = 0.67 % (J-01, A-15; corrected in spec 1.1). **Valve
  station**: two legs, walls 4.0 thick, y ±15, from the plate top to z 48, at
  x 36 … 40 and 84 … 88 (inner faces 22.0 from the valve axis: ear tips at 20.93
  + 1.0, A-02); a deck between them, 7.7 thick (z 40.3 … 48.0), y ±15, whose top
  seats the OD-H22 flange back face (A-03); through the deck a U-slot 14.1 wide
  for the stem (stem R 6.547 + 0.5): semicircular about the valve axis on its −Y
  side and open through the deck's +Y edge (y +15), so the valve slides into its
  seat along −Y at its seated height with the ports passing under the deck
  between the legs (spec 1.1, P-1: a closed bore cannot be assembled, the ports
  reach y ±20 under the flange); the deck top stays flat wherever it lies under
  the flange outline; two gusset slits 2.40 wide (y ±1.20)
  along X from the slot to x = 62 ± 11.85 at the deck top, their ends tapering
  down at 43.4° so the slit follows the gusset (A-03) with ≥ 0.5 clearance
  (spec 1.1: 2.3 / 11.6 left 0.36 at the gusset's sloped edge); two
  screw holes on the ear holes' measured positions x = 62 + 15.447 and
  x = 62 − 15.338, y 0 (A-02): Ø3.4 clearance through the top 2.0 of the deck,
  then an M3 heat-set insert bore Ø4.0 × 5.7 opening on the deck underside,
  coaxial (A-13, A-18; the insert is pressed from below, the screw comes down
  through the ear). **Footprint**: four Ø3.4 through-holes in the plate at
  (−18, ±21) and (88.5, ±21) for M3 screws into inserts in OD-C01 (A-14). Fillets
  at every root (hooks, legs, pedestal, ring) through the ladder. Envelope
  119 × 50 × 48. Print orientation: bottom face on the bed; supports under the
  deck and under the three hook catches only (A-16). OPV access: nothing of the
  mount above z 48 (the drive tube top sits at z 61.7 in the open). The valve is
  held down by its two ear screws only; with them loose it slides out along +Y
  (A-22).
- **C2 — valve on a vertical wall, OPV from the back.** The same flowmeter
  station; the valve seated on a vertical wall at the +X end with its axis along
  −Y toward the back panel, ports up and down. Not chosen: hoses would leave one
  port upward and the OPV would be reached only with the back panel off, while C1
  reaches it from the top, where OD-C10 is the removable panel.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 119.0 × 50.0 × 48.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (min x −25, min y −25, min z 0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) at the delivered pose: designed contacts `clearance = 0`: OD-H24 rim face on the pedestal top, OD-H22 flange back face on the deck top, each hook catch underside on the OD-H24 flange top; every other pair `interference ≤ 0` mm³ and `clearance ≥ 0.5` (D-04c) between the mount and each OEM solid away from the contacts (the ring gap is REQ-01, the pin holes REQ-02, the stem slot and slits REQ-04); hook beams and the flange are a J-04 pair. (b) motion: OD-H24 lowered along −Z into the seat from 25 mm above (the hooks deflect: the hook pair is exempt as a snap pair) and OD-H22 slid along −Y at 5.0 above its seat (flange back face at z 53.0, so its gussets, 3.82 below the flange, clear the deck top) from y +45 to y 0, then lowered 5.0 along −Z onto the deck (the stem enters the U-slot and the gussets the slits from above); at least 5 poses on each slide and 3 on the drop, `interference ≤ 0` mm³ against everything but the hooks. No fasteners move. (Spec 1.1: the −Y path replaces the −Z path for OD-H22; spec 1.2: the slide height 0.5 → 5.0, since at 0.5 the gussets cut the deck arms, REPORT v01 §10.) | Hard | CAD | house | `interference`, `clearance`; the sweep: reviewer's own script | A-02, A-03, A-06, A-07 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 plate window, 4 Ø3.4 footprint through-holes, 1 pedestal, 1 pedestal recess, 1 ring wall, 3 ring drain notches, 2 pin clearance through-holes (Ø4.8, Ø3.8), 3 hooks, 2 legs, 1 deck, 1 stem U-slot 14.1 wide open to +Y (no closed stem bore), 2 gusset slits, 2 Ø3.4 screw clearance holes, 2 Ø4.0 insert bores | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 1.5 (same limit as D-01b) | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad, R_max the largest curved-face radius; `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none (inserts take the thread) | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 1.5` (spec 1.1: the part is a bracket, not an enclosure; the only region under 2.0 is the deck wedge between each screw clearance hole and its slit end, 1.79 / 1.90 wide, 2.0 deep, clamped under the ear and carrying no load; the hooks stay 2.0 by design) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the build volume, bottom face down: 119 × 50 × 48 against 220 × 220 × 250 | Hard | part | machine | `envelope` | A-12 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal, or chamfered, or supported by decision: the deck underside and the three hook catch undersides are supported (A-16); the two insert-bore ceilings and the three notch ceilings are bridges gated under D-03b, not here; everything else must pass | Hard | part | floor | `overhang_census`; reviewer for the supported faces | A-16 |
| D-03b | Unsupported bridge | span ≤ 5 (the insert bore ceilings are Ø4.0, the notch ceilings 2.0; the deck is supported, A-16) | Hard | part | floor | reviewer, from sections | A-16 |
| D-04a | Clearance hole for a fastener | the 4 footprint holes and the 2 valve screw clearance holes Ø ≥ 3.25 (designed Ø3.4) | Hard | part | house | `locate_bore` | — |
| D-04c | Clearance around a seated component | ≥ 0.5 per side between the mount and each OEM solid away from the designed contacts | Hard | part | house | `clearance` | A-02, A-03, A-06, A-07 |
| D-04d | Printed sliding fit | the ring gap (REQ-01) and the pin holes (REQ-02) ≥ 0.30 per side | Hard | part | house | `clearance` | A-06, A-07 |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around each Ø4.0 insert bore (the deck pads) | Hard | part | struct | `radial_extent`; OD: reviewer | A-13 |
| D-05b | Heat-set insert hole | Ø 4.0 ± 0.05, depth ≥ 5.7 from the deck underside (A-13) | Hard | part | floor | `bore_census`, `locate_bore` | A-13 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | applies to reamed fit bores; this part has none (the insert holes are formed by the insert) | Hard | part | floor | — (N/A by this row) | — |
| J-01 | Cantilever snap root strain | ε = 1.5·y·t / (L²·Q) ≤ 1.5 % (A-15) for each hook, y and L measured from the STEP (y = catch reach past the flange r 20.37, L = root to catch underside), Q from L/t; × 0.6 not applied (the flowmeter is not removed repeatedly) | Hard | part | struct | arithmetic on `min_wall` (t) and sections (y, L); reviewer re-derives | A-15 |
| J-02 | Snap beam thickness | ≥ 0.5 × 2.0 = 1.0 | Hard | part | struct | `min_wall` on the beam | — |
| J-03 | Snap beam taper | the catch is not thinner than 0.5 × the root only if ε is within 0.2 % of its limit; report the ratio | Hard | part | struct | reviewer | — |
| J-04 | Snap in service | at the engaged pose each hook is undeflected: `interference ≤ 0` mm³ between each hook and OD-H24; the catch underside touches the flange top (`clearance = 0`) | Hard | CAD | struct | `interference`, `clearance` | A-06, A-08 |
| J-05 | Wall around a threaded hole | ≥ 3.0 around each of the two insert bores, over their whole 5.7 depth | Hard | part | struct | `min_wall`; `radial_extent` ring at three depths | — |
| J-06 | Printed threads | none (inserts) | Hard | part | floor | `bore_census` diameters (N/A by this row) | — |
| E-06 | Boss support | the insert pads are the deck itself, tied to the legs; the hooks and ring root-filleted to the plate and pedestal | Hard | part | struct | reviewer | — |
| REQ-01 | Flowmeter seat | pedestal top at z 10.0 ± 0.1 (the OD-H24 rim face rests on it, `clearance = 0`); ring inner radius: `radial_profile` inner over 0 … 360° at z 10.5 … 12.5 in [16.30, 16.40] (one-sided since spec 1.2: R 16.25 leaves 0.48 to the cup); ring top at z 13.0 ± 0.1; `clearance(ring, OD-H24 cup)` in [0.50, 0.70] | Hard | CAD | A-06 | `radial_profile`, `envelope`, `clearance` | A-06 |
| REQ-02 | Pin clearance holes and recess | through-bores Ø4.8 +0.1/−0 at (0.185, 0.093) and Ø3.8 +0.1/−0 at (−11.78, 0.14) (one-sided since spec 1.2: the lower end left 0.45 to the pins), offset ≤ 0.10, from the recess floor through the pedestal and plate (length 9.4 ± 0.1); `clearance` to each pin ≥ 0.5; the recess R 14.10 ± 0.1 with its floor at z 9.40 ± 0.05 (`radial_profile` inner at z 9.5 … 9.9), `clearance` from the recess to the OD-H24 underside ribs and hub ≥ 0.5 | Hard | CAD | A-07 | `locate_bore`, `clearance` | A-07 |
| REQ-03 | Hooks | three hooks centred at θ 70°, 160°, 320° ± 1°; beam inner face at R 20.87 ± 0.1 over z 6 … 26 (`radial_profile` inner on those rays); catch underside at z 29.9 ± 0.1 reaching R 18.87 ± 0.1; each catch lands on the OD-H24 flange top outside its slots and windows (`clearance = 0` at the catch, A-08); catch top chamfer 45° ± 1° | Hard | CAD | A-08, A-09 | `radial_profile`, `radial_extent`, `clearance` | A-06, A-08, A-09 |
| REQ-04 | Valve seat | deck top at z 48.0 ± 0.1, flat wherever it lies under the OD-H22 flange outline (the flange bears on the two deck arms and the −Y web); stem U-slot 14.1 +0.1/−0 wide through the deck (length 7.7 ± 0.1), semicircular about (62.0, 0) on the −Y side: `radial_profile` inner about (62, 0) over 180° … 360° at z 41 … 47 in [7.05, 7.10], the slot's straight walls at y ±(7.05 +0.05/−0) open through the deck's +Y edge; gusset slits 2.40 ± 0.1 wide reaching x = 62 ± (11.85 +0.1/−0) at the top (one-sided since spec 1.2: the lower ends left 0.45 / 0.46 to the stem and the gusset); `clearance(mount, OD-H22)` ≥ 0.5 away from the flange contact, the nearest points reported | Hard | CAD | A-03 | `locate_bore`, `envelope`, `clearance` | A-03 |
| REQ-05 | Valve screws | two Ø3.4 ± 0.1 clearance bores at (77.447, 0) and (46.662, 0), 2.0 ± 0.1 deep from the deck top, offset ≤ 0.10; under each, coaxial (offset ≤ 0.10), a Ø4.0 ± 0.05 insert bore 5.7 ± 0.1 deep opening on the deck underside | Hard | CAD | A-02, A-13 | `locate_bore` | A-02, A-13, A-18 |
| REQ-06 | Footprint | four Ø3.4 ± 0.1 through-holes at (−18, ±21) and (88.5, ±21), offset ≤ 0.10, length 4.0 ± 0.1 | Hard | CAD | A-14 | `locate_bore` | A-14 |
| REQ-07 | Hose space under the valve | no mount material below the OD-H22 port mouths within the plate window: the window spans x 40 … 84 and y −25 … 25 through the plate (`envelope` of the plate pieces reported apart); the legs' inner faces at x 40.0 and 84.0 ± 0.1 | Hard | CAD | A-04 | `envelope`, `radial_extent`; reviewer from sections | A-04, A-19 |
| REQ-08 | OPV reachable | no mount material above z 48.1 (`envelope` max z) and none within r 12 of the valve axis above the deck top | Hard | CAD | A-10 | `envelope`, `radial_extent` | A-10 |
| REQ-09 | Drainage | every pocket that faces up is open to the bottom face or to the plate top: the pin holes and the window are through (REQ-02, REQ-07); the recess drains through the pin holes; the annulus between the OD-H24 rim and the ring drains through three notches 2.0 ± 0.1 wide × 0.5 ± 0.1 high at the ring base at θ 25°, 115°, 225° ± 1° | Hard | part | house | reviewer, from sections | — |

**Named exceptions** (Usta U-18): none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | Scan scale and units | mm, scanner calibration, no caliper check (both reference scans; CHK-SCALE flagged) | every fit off by the scale error | H22/H24 reports; INTAKE X-273, §4 Q10 | calipers on the donor parts (ear pitch, flange Ø, cup Ø) | OPEN |
| A-02 | OD-H22 ear holes | at x +15.447 and −15.338 from the valve axis (asymmetric by 0.109, above noise, kept per hole), Ø3.87; ear tips at r 20.93 (ear end R 5.484); the +X ear tip is damaged on the specimen and modelled by symmetry | screws miss or the ears foul the legs | H22 PARAM_TABLE; INTAKE X-004…X-008, §4 Q9 | calipers on the ear holes | OPEN |
| A-03 | OD-H22 underside | flange back face flat (261 mm²), plate 2.26 thick; stem R 6.547 from z 0 to the cone at −4.23; gussets in the XZ plane, 1.306 thick, reaching x 11.085 at z 0, 43.4° below horizontal | stem or gussets foul the deck | H22 PARAM_TABLE; INTAKE X-001, X-029…X-036 | donor | OPEN |
| A-04 | OD-H22 ports and hoses | ports in the YZ plane at 34.1° / 35.0° below horizontal from z −14.3, mouths at t 20 with lip R 6.16, lowest point z −30.87; a hose needs ≥ 15 mm straight run past the mouth before bending; the deck at z 48 puts the port mouths ≈ 16 above the floor | hoses kink against the OD-C01 floor | H22 PARAM_TABLE; INTAKE X-037…X-054, X-066; run length: this spec | tube scan (OD-W12…W15) or the first assembly | OPEN |
| A-05 | OD-H22 tilt | the valve axis is 0.47° off the flange normal on the specimen; the STEP is modelled square and the mount uses it as modelled | stem bore clearance 0.5 absorbs ≈ 0.25 mm over the deck depth | INTAKE X-067, §4 Q8 | donor | OPEN |
| A-06 | OD-H24 lower body | rim face z 0 with the rim annulus r 13.98 … 15.71; cup r 15.71 + 0.0195·z (drafted, 15.77 at z 3); flange underside z 12.67, outer r 20.25 → 20.37, top z 19.9, top fillet 0.6 | flowmeter does not seat or the hooks miss | H24 params.json; INTAKE X-172…X-189 | calipers (cup Ø ≈ 31.5, flange Ø ≈ 40.6, rim → flange top 19.9) | OPEN |
| A-07 | OD-H24 base pins | Ø3.8 at (0.185, 0.093) to z −7.03; Ø2.8 at (−11.78, 0.14) to z −5.46 | pins foul the pedestal | INTAKE X-194…X-201 | calipers | OPEN |
| A-08 | OD-H24 flange top landing | the flange top between r 18.87 and 20.37 is free where no slot (r 16.75 … 18.9, at θ 26.5° + 90k, each ± 13.8°) and no window (r ≤ 12.45) lies; the specimen's 1.5° wedge warp is ± 0.2 at the flange edge, so a catch may bear 0.2 early or late | catch does not land, or the flowmeter rocks | INTAKE X-202…X-214, X-249, §4 Q7 | donor: the slots' function and a flatness check | OPEN |
| A-09 | OD-H24 pipes and connector | both pipes run toward −Y from x −10.6 (z 7.5) and x −4.4 (z 20.25) to y ≈ −36; the connector sits at +X (x 10 … 17, y ± 6.5) up to z 36.5; the hooks at θ 70°, 160°, 320° stay ≥ 5 mm from the pipes and clear of the connector by the D-04c gate (the plan's probe found 290° at 3.33 from the upper pipe and over the 296.5° slot, hence 320° in spec 1.1; the built 320° catch is 4.94 from the connector's corner, REPORT v01, accepted in spec 1.2: the 5 mm was a planning margin, the gate is D-04c ≥ 0.5) | a hook fouls a pipe or the connector | INTAKE X-215…X-247 | the STEP as placed (designer measures) | OPEN |
| A-10 | Where the OPV is | the OPV spring sits inside the OD-H22 drive tube and is reached from the tube's top (z 61.7 in the mount frame) with the top panel off | the OPV is elsewhere and C1's orientation does not help | SOURCING_GUIDE §3.5; INTAKE X-257, X-258, X-283; the H22 intake card ("knob/rotor drive") | the Usta looks at the donor | OPEN |
| A-11 | Material | PETG, density 1270 kg/m³ | wrong mass | BOM (INTAKE X-252); typical PETG datasheet | the Usta names the filament | OPEN |
| A-12 | Build volume | designed to 220 × 220 × 250 (the K1C's specification, not in the machine file); the Kobra Max 3 is larger | part does not fit | memory of the spec sheets | the Usta reads the printers | OPEN |
| A-13 | M3 heat-set insert | hole Ø 4.0, depth 5.7, insert length 5.7 (reseller figure; same as OD-G01 A-17) | insert loose or proud | typical M3 × 5.7 × 4.6 insert listing | the Usta's stocked insert datasheet | OPEN |
| A-14 | OD-C01 interface | four M3 screws from above through the plate at (−18, ±21) and (88.5, ±21) into inserts in OD-C01; the mount's bottom face is the OD-C01 floor plane | OD-C01 must be designed to it | this spec (design choice) | OD-C01 design | OPEN |
| A-15 | PETG snap strain limit | ε_perm 1.5 % for a printed PETG cantilever loaded across layers (house, unsourced; GATES J-01 has no printed material) | hooks crack or creep | this spec | a bend test on a printed hook, or a source the Usta accepts | OPEN |
| A-16 | Print orientation and supports | bottom face on the bed; supports under the deck (span 44) and under the three hook catches (2 mm overhangs); nothing else supported | deck sags or the catches print badly | this spec | first print | OPEN |
| A-17 | Ledger row reserved | (not used: the OD-H21 question was answered before ratification, §7) | — | — | — | RETIRED 2026-09-30 |
| A-18 | Screw engagement | M3 × 8 through the ear (2.26) and the 2.0 clearance layer leaves 3.74 mm in the insert (≥ 1 × d) | screw strips or bottoms | this spec; A-13 | the Usta's screws | OPEN |
| A-19 | Hose bend space | the port mouths sit ≈ 16 mm above the OD-C01 floor with the window open below (REQ-07) | hoses kink; the deck height changes | this spec; A-04 | the first assembly with the OEM tubes | OPEN |
| A-20 | Valve orientation | drive tube up, ears along X, ports toward ±Y | a hose route fails | this spec (C1) | the first assembly | OPEN |
| A-21 | Flowmeter orientation | axis vertical, pipes toward −Y (the tank side), connector toward +X (toward the valve) | a hose route or the cable fails | this spec (C1) | the first assembly | OPEN |
| A-22 | Valve retention | OD-H22 is held down by its two ear screws only; the deck slot is open to +Y, so with the screws loose the valve slides out along +Y (the hoses on its ports also restrain it) | the valve shifts during assembly before the screws are in | this spec (1.1, P-1) | the first assembly | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-09-30 | OD-H21 plugs into the water path by its clipped spigot and is not carried by OD-C07 (chassis/README.md row 5 lists it; the OD-G01 thread owns that file and is told) | the Usta, decision card | usta_gate question_answered |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | INTAKE §4 Q1 (the OD-H24 "connector" is the flowmeter's own Hall-sensor connector, not OD-H23), Q5 and Q6 (tube routes, OD-C01 floor) are chassis-level: carried to OD-C01 as A-14 and A-19 | Oğuz | INTAKE_v01 §4 |
| 2026-09-30 | spec 1.1 on the designer's J2 stop (DESIGN_PLAN §7 Q1 … Q6): Q1 → P-1, the stem bore becomes a U-slot open to +Y and OD-H22 is assembled along −Y (A-22; C2 and a two-part clamp rejected: one solid, OPV from the top); Q2 → slits 2.40 wide to x 62 ± 11.85, D-01b lowered to 1.5 with the reason in its row; Q3 → P-3 recess R 14.10 × 0.60, pin holes 9.4 long; Q4 → P-4, hook 3 at 320°; Q5 → P-5, three drain notches; Q6 → the insert-bore ceilings are D-03b bridges; J-01 arithmetic corrected to 0.67 %. Ratified on the standing instruction; the Usta confirms or amends at the next opportunity | Oğuz (standing instruction) | usta_gate spec_ratified 1.1 |
| 2026-09-30 | spec 1.2 on the designer's J3 stop (REPORT v01 §10): the OD-H22 −Y slide moves from 0.5 to 5.0 above the seat, then a 5.0 drop (at 0.5 the gussets cut the deck arms by 15.2 mm³; measured at 5.0: 0 mm³, least gap 0.858; the alternative, gusset slits open to +Y, was rejected: it takes the flange bearing off the −Y web). Geometry unchanged. The sweep (REPORT §4) showed the ring, pin, slot and slit-reach tolerances reaching under the 0.5 clearance at their lower ends: made one-sided. The 4.94 gap catch-to-connector is accepted (A-09). Ratified on the standing instruction | Oğuz (standing instruction) | usta_gate spec_ratified 1.2 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the two reference reports |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6, OD-H21 removed on the Usta's answer; ratified |
| 1.1 | 2026-09-30 | after the J2 plan: stem U-slot open to +Y and a −Y assembly path (U-03b, U-05, REQ-04, A-22); slits 2.40 / 11.85 and D-01b 1.5 (U-06); pedestal recess R 14.10 × 0.60 and pin holes 9.4 (REQ-02, U-05); hook 3 at 320° (REQ-03, A-09); three ring drain notches (REQ-09, U-05, D-03b); insert-bore ceilings under D-03b (D-03a); J-01 overlap 1.5, ε 0.67 % (§4) |
| 1.2 | 2026-09-30 | after the J3 build: OD-H22 assembly slide at 5.0 above the seat then a 5.0 drop (U-03b); one-sided tolerances on the ring inner R, the pin holes, the slot width and the slit reach (REQ-01, REQ-02, REQ-04); A-09 note on the 4.94 connector gap. No geometry change |
