# DESIGN_SPEC — OD-T01 group head bench pressure-test rig (20261002-od-t01-pressure-test-rig)

Version 1.2 · RATIFIED by the Usta on 2026-10-02 (standing instruction "Usta'ya yalnız karar gereken yerde sor; açık soruları A-## satırı olarak ledger'a yaz ve ilerle" and the message of 2026-10-02 22:58 UTC; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-T01 is the bench pressure-test rig of the Open Dedica project (BOM: "Group
head bench pressure-test rig (M1 close-out)", printed + fittings). It holds the
printed group head housing OD-G01, with the OEM gasket support OD-G04 inside and
the OEM portafilter OD-G10 locked in its bayonet, mouth down, exactly the way the
machine's carrier OD-C05 holds it: the housing's rear face against the underside
of a plate, four M3 × 8 screws driven from above through that plate into the
housing's four inserts, the hub reachable through a window above. With a blind
basket in the portafilter and water pumped into the hub, the housing carries the
brew load through its lugs, its body and its inserts as it will in the machine.
OD-G01's review left that load (REQ-12: 15 bar on a Ø51 basket, 3.06 kN) to this
test, and the Usta accepted OD-G01 with the deviation stated. Done means: one
valid printable solid that seats the housing at the carrier's interface, lets the
portafilter go in, lock and come out, leaves room under the portafilter to catch
water and see a leak, stands on the bench and screws down to it, and is far
stronger than the load it carries, with every unconfirmed value in §6.

**Deliverables** (tier S): STEP AP242 of the rig; the check assembly STEP (rig +
OD-G01 with OD-G04 and OD-G10 as placed); STL, and at J5 a 3MF written from the
reviewed STL; build and check scripts; REPORT; sections; at J5 a one-page
`TEST_PROCEDURE.md` (fittings list, steps, what to record) written by Oğuz from
§6. No drawings or renders.

**Out of scope:** OD-G01 itself (accepted); the water connection to the hub
(OD-G07, OD-H14, OD-H15, not scanned: bought or OEM, A-05); the pump, gauge,
valve and tubes (bought, A-04); the blind basket (bought, A-06); the test itself
(the Usta's bench; its result closes OD-G01 REQ-12); calipers; drawings; renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Mating solid OD-G01 (housing v03, accepted) | `00_Spec/inputs/od_g01_housing_C1_v03.step`, housing frame (Z the cup axis, +Z toward the mouth, z 0 the lug top plane): rear face z −24.94, square 100 × 100, four M3 insert bores Ø4.0 at (±44, ±44) from the rear face, Ø26 hub opening on the axis | — | OD-G01 spec 1.3 §4 | CONFIRMED as the input; its numbers are §6 rows |
| Placed set | `od_g01_assembly_C1_v03.step`: housing + OD-G04 + OD-G10 locked, in the housing frame | — | OD-G01 v03 | CONFIRMED as the input |
| Interface precedent OD-C05 | the same screw: Ø3.4 holes at (±44, ±44), Ø6.5 counterbores leaving 3.0 of plate under the head, M3 × 8 reaching 5.0 into the 5.7 insert; hub window R 30 | — | OD-C05 spec 2.2 §4 | CONFIRMED (delivered part) |
| Fasteners | M3 heat-set inserts (OD-F01, in OD-G01) and M3 × 8 screws ISO 7380 (OD-F02, head Ø5.7) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard) |

**Coordinate frame (rig):** X to the right of a user standing at the rig, +Y up,
+Z toward the user (the side the handle comes out), the bench top y = 0, the
housing's axis the line x 0, z 0. **Housing pose**: housing x → X, y → +Z,
z → −Y, origin (0, 110.06, 0), so the housing's rear face lies at y 135.0 (the
plate's underside) and its mouth's front face at y 106.76; this is OD-C05's pose
in the machine with the axis moved to (x 0, z 0) and the plate underside to
y 135. OD-G04 and OD-G10 go with the housing. **OD-G10 poses**: "rotated by φ"
turns the locked portafilter about the housing's axis, φ > 0 turning the handle
toward +X; locked, its handle points ≈ 34° from +Z toward +X (measured, plan D1). Every artifact of
this job uses these frames.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_t01_rig | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-09) | PLA (the Usta, 2026-10-02: "all printed in pla for now") | 1240 | as printed | A-08 |

Environment: the workshop bench; cold tap water (a hydrostatic test, A-03)
inside the housing up to the test pressure; water on the rig's base when a seal
weeps; the portafilter locked and unlocked by hand (handle force ≈ 50 N at
≈ 150 mm); the brew load 3.06 kN at 15 bar pulling the housing down from the
plate through four screws.

## §4 Architecture and concepts

- **C1 — a closed frame printed on its side (CHOSEN).** One solid, a profile in
  the XY plane extruded along Z from z −60.0 to +60.0 (120 deep), with holes:
  - **Top plate** 15.0 thick, y 135.0 … 150.0, x −90.0 … +90.0. Its underside
    y 135.0 is the plane of the housing's rear face (a designed contact). Through
    it along Y: four Ø3.4 holes at (x ±44.0, z ±44.0), coaxial with the
    housing's insert bores, each with a Ø6.5 counterbore from the top face
    y 150.0 down to y 138.0 (12.0 deep) with a 45.1° teardrop roof toward +Z
    (apex 4.61 from its axis), so an M3 × 8 driven from above bears
    on 3.0 of plate and reaches 5.0 into the 5.7 insert, as on OD-C05; a **hub
    window** R 30.0 about the axis (OD-C05's), with a 45.1° teardrop roof toward
    +Z (apex on the axis at z +42.51) so it prints without a bridge.
  - **Two walls** 15.0 thick, x ±(75.0 … 90.0), from the base's top y 10.0 up to
    the plate y 135.0, over z −60 … +40 only: the walls stop 20 short of the
    plate's and the base's front edge (z +60), so the handle, which swings past
    x ±75 near the front, keeps its distance (1.1, plan Q1). The portafilter's
    body (r ≤ 36) and ears pass between them; its handle leaves the frame at the
    open front.
  - **Base** 10.0 thick, y 0 … 10.0, x −120.0 … +120.0, the full depth: the
    bench foot and the floor under the portafilter (a catch tray or a cup stands
    on it). Four **bench holes** Ø4.5 through it along Y at (x ±105.0,
    z ±40.0), each with a 45.1° teardrop roof toward +Z (apex 3.19 from its axis), outside the walls, for M4 or 4 mm wood screws into the bench (or
    a clamp on each wing).
  - **Corner fillets**: the four inside corners of the frame (plate to wall,
    wall to base) carry a 45° chamfer 10.0 × 10.0 along Z, as part of the
    profile.
  - Headroom: the portafilter's lowest point (housing z +47.76) lies at y 62.3,
    52.3 above the base's top (A-07).
  - Above the plate nothing of the rig: the hub, the water connection and the
    four screw heads are open to the hand and the eye.
  - Print orientation (A-10): **lying on its rear face** z = −60 on the bed,
    build direction +Z: the profile is a vertical prism; the four Ø3.4 holes, the
    Ø6.5 counterbores, the four Ø4.5 bench holes and the hub window run along
    Y, horizontal in the print: the hub window, the counterbores and the bench
    holes print their roofs as 45.1° teardrops; the crowns of the four Ø3.4 holes
    are the named exception. The counterbore floors
    are vertical faces in the print. Envelope 240.0 × 150.0 × 120.0 (x ±120,
    y 0 … 150, z ±60); on the bed 240 × 150, 120 tall.
  - Strength (A-02, a hand calculation, not a gate): the frame is a closed ring,
    so each wall's root carries less than a cantilever's moment; taken as a
    simply supported plate of 120 × 15 between the walls (inner faces x ±75)
    with 1.53 kN at x ±44 on each side, M = 1.53 kN × 31 mm = 47.4 N·m,
    Z = 120 × 15² / 6 = 4500 mm³, σ ≈ 10.5 MPa against ≈ 40 MPa for printed
    PLA in the layer plane: a factor ≈ 3.8 at 15 bar. The layers lie in XY
    planes, so the bending stress runs along the layers.
- **C2 — a printed copy of OD-C05's plate on four threaded rods.** Not chosen:
  more bought parts and a plate 5 thick at 3 kN.
- **C3 — the same frame printed upright, plate on the bed.** Not chosen: the
  base spanning 150 between the walls would be a bridge, and the bench wings an
  overhang.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 240.0 × 150.0 × 120.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±120, y 0 … 150, z ±60) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) at the housing pose of §2: designed contact `clearance = 0` between the plate's underside and the housing's rear face; every pair `interference ≤ 0` mm³; rig to the housing elsewhere, to OD-G04 and to OD-G10 (locked) ≥ 2.0. (b) the housing set (housing + OD-G04 + OD-G10) moved along −Y from its seat by 0 … 30 in steps ≤ 2.0 (offered up from below): `interference ≤ 0` with the rig at every step | Hard | CAD | house | `clearance`, `interference` | A-01 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 plate, 2 walls (z −60 … +40), 1 base, 4 corner chamfers, 4 Ø3.4 holes with 4 Ø6.5 counterbores (teardrop), 1 hub window (R 30 + teardrop), 4 Ø4.5 bench holes (teardrop) | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh (written at J5) | Hard | CAD | house | `write_stl`, `stl_max_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the webs between the counterbores and the hub window, and around the bench holes, included) | Hard | part | struct | `min_wall` | A-08 |
| D-02 | Bed fit | each envelope size ≤ the Kobra Max 3 build volume, lying on the rear face: 240.0 × 150.0 on the bed, 120.0 tall | Hard | part | machine | `envelope` | A-09 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (rear face on the bed, build direction +Z): the teardrop roofs of the hub window, the counterbores and the bench holes at 45.1°; the crowns of the four Ø3.4 holes are the named exception below, excluded by position, their least angle reported | Hard | part | floor | `overhang_census(build_dir=(0,0,1))` | A-10 |
| D-03b | Unsupported bridge | span ≤ 5: the four Ø3.4 crowns bridge ≤ 3.4; nothing else bridges | Hard | part | floor | reviewer, from sections | A-10 |
| D-04a | Clearance hole for a fastener | the four housing screw holes Ø ≥ 3.25 (designed 3.4); the four bench holes Ø ≥ 4.25 (designed 4.5) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: clearance holes only | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | applies to threaded holes in this part; it has none (the inserts are in OD-G01) | Hard | part | struct | — (N/A by this row) | — |
| REQ-01 | Housing screws | four Ø3.4 ± 0.1 holes along Y at (x ±44.0, z ±44.0), offset ≤ 0.10 from the housing's insert bores as posed, through the plate; Ø6.5 ± 0.1 counterbores from y 150.0 to y 138.00 ± 0.10, leaving 3.0 ± 0.1 of plate under each head | Hard | CAD | client (OD-C05's interface) | `locate_bore`, `bore_census` | A-01 |
| REQ-02 | Seat | the plate's underside one plane at y 135.00 ± 0.10 over the housing's square (x ±50, z ±50), the housing's rear face on it | Hard | CAD | client | `envelope`; `clearance` = 0 (U-03) | A-01 |
| REQ-03 | Hub window | R 30.0 ± 0.1 about the axis through the plate, its teardrop roof at 45.1° ± 1° toward +Z with the apex at z +42.51 ± 0.15 (the apex is R / cos 45.1°, so R's ± 0.1 moves it ± 0.14); OD-G04's hub tube ≥ 2.0 from the rig; the two pair-B screw axes (r 19.03) ≥ 10.87 from the window's face (R 29.9 − 19.03), so a head up to Ø17.7 clears by ≥ 2.0 at R's low limit (A-12) | Hard | CAD | client (OD-C05 A-06) | `bore_census`; reviewer from sections; `clearance` | A-05 |
| REQ-04 | Portafilter travel | OD-G10 (a) at its locked pose rotated by φ from −60° to +15° in steps ≤ 5°: `clearance` to the rig ≥ 5.0; (b) rotated by φ = −50°, lowered 15.0 along −Y and moved along +Z from z 0 to z +200 in steps ≤ 5.0: `interference ≤ 0` with the rig at every step. OD-G10 is not a sound solid (`brep_valid` 0, as OD-G01 A-28): every `interference` with it here and in U-03 is read as `clearance > 0` with `detail["inside"] == False` | Hard | CAD | client (the portafilter goes in and out) | `clearance`, `interference` (OD-G10: `clearance` fallback) | A-07 |
| REQ-05 | Headroom | the locked OD-G10's lowest point ≥ 50.0 above the base's top face (y 10) | Hard | CAD | client (catch the water, see a leak) | `envelope` of the placed OD-G10 | A-07 |
| REQ-06 | Bench fixing | four Ø4.5 ± 0.1 holes along Y through the base at (x ±105.0, z ±40.0), offset ≤ 0.10, each axis clear of the rig from y 10 to y 300 within r 4.0 (a driver from above) | Hard | CAD | client | `locate_bore`; `interference` of four Ø8 cylinders with the rig = 0 | A-11 |
| REQ-07 | Screw access | each housing screw's axis clear of the rig above the plate (y 150 … 300) within r 3.0 | Hard | CAD | client | `interference` of four Ø6 cylinders with the rig = 0 | — |
| REQ-08 | Strength | **Soft.** The rig holds 3.06 kN on the four screws with no visible yield or crack at the test pressure; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating against §4's hand calculation; answered by the first test | Soft | part | client | — (bench) | A-02 |

**Named exceptions** (Usta U-18): D-03a for the crowns of the four
horizontal Ø3.4 holes in the print (bridges ≤ 3.4, within D-03b), the usual FDM
practice for small horizontal holes (as on OD-C02 and OD-C11); recorded here for
the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | Housing interface | the accepted OD-G01 v03: rear face plane, four insert bores at (±44, ±44), 100 × 100 square, as the STEP gives them; the inserts set to their bores' depth (5.7) | the screws miss the inserts or bottom out | OD-G01 spec 1.3; OD-C05 spec 2.2 | the printed housing with its inserts | OPEN |
| A-02 | The rig's strength | §4's hand calculation: σ ≈ 10.5 MPa at 15 bar against ≈ 40 MPa for printed PLA along its layers; the screws' heads on 3.0 of plate as on OD-C05 | the rig fails before the housing and the test proves nothing | this spec (hand calculation; PLA strength a common printed value, not sourced) | the first test (REQ-08) | OPEN |
| A-03 | Test medium and pressure | cold water (hydrostatic: little stored energy), raised in steps to 15 bar (the Ulka pump's rated maximum, the OEM's over-pressure valve setting) and held 60 s per step; the housing passes when it holds 15 bar for 5 min with no crack, no step in the gauge and no weep at the lugs | the test should go higher (a proof factor) or hot | SOURCING_GUIDE (15 bar pump; piping 125 °C / 15 bar); OD-G01 A-21 | the Usta's test plan | OPEN |
| A-04 | Pressure source and fittings | a hand hydrostatic test pump (or the Ulka pump OD-H01 with its OPV), a 0–25 bar gauge, a bleed valve and a tee, PTFE or reinforced tube rated ≥ 25 bar; bought, listed in TEST_PROCEDURE.md | the Usta has other parts | this spec | the Usta's bench | OPEN |
| A-05 | Water to the hub | the OEM water connection (OD-G07 gasket, OD-H14, OD-H15) seats on OD-G04's hub tube as in the machine, inside r 30 above the plate (OD-C05 A-06); the rig keeps everything above the plate free | the connection needs more room or its own clamp | OD-C05 spec 2.2 A-06 | the connection parts in hand | OPEN |
| A-06 | Blind basket | a stainless 51 mm blind (no-hole) basket in OD-G10 closes the mouth; bought | the OEM baskets have holes and the test needs a blind | this spec | the Usta's portafilter kit | OPEN |
| A-07 | Portafilter travel and headroom | OD-G10 locks as the v03 assembly places it; it goes in turned −50°, lowered 15; the gasket's wear turns the lock up to +15°; a catch tray up to 50 tall stands on the base | the handle meets a wall | `od_g01_assembly_C1_v03.step` | the first locked portafilter | OPEN |
| A-08 | Material | PLA, 1240 kg/m³ (the Usta, 2026-10-02); cold water only, so PLA's heat limit does not apply | the rig creeps under a long hold | the Usta's message | the first test | OPEN |
| A-09 | Kobra Max 3 build volume | 420 × 420 × 500 (Anycubic specification, not in the machine file), as OD-C11 A-09; the rig is 240 × 150 on the bed, 120 tall (too big for the K1C's 220) | does not fit | OD-C11 A-09 | the Usta reads the printer | OPEN |
| A-10 | Print orientation | lying on its rear face (z −60), build direction +Z, no supports; the layers lie in XY planes, along the plate's bending stress | the long thin profile warps; a brim is needed | this spec | first print | OPEN |
| A-12 | Pair-B screw heads | the OEM screws through OD-G01's pair-B holes have heads ≤ Ø17.7 (no size in any input; an M3 or M3.5 head is ≈ Ø6 … 7) | a bigger head or a tool needs the window larger | this spec (plan Q2) | the screws in hand | OPEN |
| A-11 | Bench fixing | four M4 or 4 mm wood screws through the base's wings into the bench, or two clamps on the wings; the locking torque (≈ 7.5 N·m) and the test load stay inside the rig | the bench cannot take screws: clamps only | this spec | the Usta's bench | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-02 | OD-G01 accepted with its documented deviation (REQ-12 left to this bench test); everything printed in PLA for now | the Usta (message 22:58 UTC) | REQUEST.md |
| 2026-10-02 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-10-03 | spec 1.2: REQ-03's apex band and pair-B threshold did not stack with R 30.0 ± 0.1 (REPORT v01 §4 note 2, §9.1); apex band ± 0.15, pair-B axes ≥ 10.87 with the A-12 head bound Ø17.7; no geometry change. Ratified on the standing instruction | Oğuz (standing instruction) | usta_gate spec_ratified 1.2 |
| 2026-10-02 | spec 1.1 on the designer's J2 questions: Q1 → the walls stop at z +40 (a relief of the front 20, option (b) in its simplest form; the plate and base keep z ±60 for the seat and the screws); Q2 → the axis-distance check, head size ledgered as A-12; Q3 → every teardrop at 45.1°, apexes as §4; Q4 → the locked handle at ≈ 34° in §2; Q5 → the `clearance` fallback for OD-G10 accepted (OD-G01 A-28). Ratified on the standing instruction | Oğuz (standing instruction) | usta_gate spec_ratified 1.1 |
| 2026-10-02 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and the message of 2026-10-02 22:58 UTC; INTAKE_v01 §4 questions answered by §4 and §6 as design choices, all A-## rows; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-10-03 | after the J3 build (REPORT v01 §4, §9.1): REQ-03 tolerances made to stack (apex ± 0.15, pair-B ≥ 10.87, A-12 ≤ Ø17.7); no geometry change; spec 1.1 kept as `DESIGN_SPEC_v1.1.md` |
| 1.1 | 2026-10-02 | after the J2 plan (DESIGN_PLAN §7): walls z −60 … +40 (REQ-04a was 0.0 at φ +15° on 1.0); teardrops 45.1°; A-12; OD-G10 `clearance` fallback in REQ-04; handle ≈ 34°; spec 1.0 kept as `DESIGN_SPEC_v1.0.md` |
| 1.0 | 2026-10-02 | INTAKE_v01 read; ratified |
| 0.1 | 2026-10-02 | first draft from the OD-G01 v03 records, the OD-C05 spec and INTAKE_v01 |
