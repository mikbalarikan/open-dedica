# DESIGN_SPEC — OD-C08 printed electronics bay tray (20261001-od-c08-electronics-bay-tray)

Version 1.0 · RATIFIED by the Usta on 2026-10-01 (standing instruction of 2026-09-30, the "what can start now please initiate it" and the path choice "c08 i will use original pcb for this stage" of 2026-10-01: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C08 is the 3D-printed electronics bay tray of the Open Dedica espresso
machine: it holds the original OEM power PCB OD-E01 (electronics path 1, the
Usta's choice of 2026-10-01) in the electric zone of the base frame OD-C01
(x 70 … 120, z −240 … −30, OD-C01 A-08), behind the bulkhead OD-C02, standing on
edge parallel to the bulkhead with its solder side toward the bulkhead and its
components toward the right side panel. Done means: one valid printable solid
standing on the OD-C01 plate in the zone, held by four M3 screws driven from
above into four new inserts in the plate, the board seated on four standoffs
(two M3 screws in its Ø4 holes, two locating pins in its Ø2.5 holes) with every
part of the board clear of the tray, the bulkhead and the zone's limits, and
every unconfirmed value in §6. The control board OD-E02 (front buttons) belongs
to the front panel OD-C09; the wiring, the side panel OD-C13 and the mains entry
(back panel OD-C11) are not designed here: their rows are assumptions.

**Deliverables** (tier M): STEP AP242 of the tray; the check assembly STEP (tray
+ OD-E01 at its joint + OD-C01 + OD-C02); STL and 3MF; build and check scripts;
REPORT; sections. No drawings or renders.

**Out of scope:** path 2 (OD-E51 … E58), the control board OD-E02 and its bezel
(OD-C09), the wiring looms and their routes, the mains entry and grommet
(OD-C11, OD-C14), the side panel OD-C13, calipers, drawings, renders. OD-C01
itself is not changed by this job: the four new insert holes it needs are an
OD-C01 spec change handed over (A-01).

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| OD-C01 base frame (delivered) | `00_Spec/inputs/OD-C01_base_frame.step` (identity): plate y −6 … 0, x ±120, z −305 … +100, corners R 10; the electronics zone x 70 … 120, z −240 … −30; no hole yet under this tray (A-01) | — | OD-C01 spec 1.2 §4, A-08, REQ-07 (INTAKE X-01 … X-10) | CONFIRMED as the input; its numbers are §6 rows |
| OD-C02 bulkhead (delivered) | `00_Spec/inputs/OD-C02_bulkhead.step` (identity): electric face x 67.0; base rail to x 71.0 (y 0 … 12), top rail to x 70.5 (y 207 … 215); wire windows Ø14 at (y 150, z −200 / −130 / −60) and (y 60, z −55) | — | OD-C02 spec 1.2 §4, REQ-02, REQ-04, A-07 (INTAKE X-11 … X-19) | CONFIRMED as the input |
| OD-E01 power PCB (path 1, the Usta 2026-10-01) | `00_Spec/inputs/OD-E01_power_pcb.step`, datum frame: origin on hole H1's axis at the board's top face, +Z out of the component side, +X along the long edge; one fused envelope solid of the component side (its solder side invented flat) | — | step/reports/OD-E01_power_pcb (INTAKE X-20 … X-50) | CONFIRMED as the input; every scan value an A-## row (A-02) |
| Fasteners | M3 heat-set inserts (OD-F01, Ø4.0 bore, 5.7 long), M3 × 8 screws (OD-F02, ISO 7380, head Ø5.7) | — | open-dedica `docs/bom.csv` (INTAKE X-68 … X-70) | CONFIRMED (project standard) |

**Coordinate frame:** the OD-C01 machine frame, every overlay the identity: X to
the user's right, +Y up, +Z toward the user (the front), the plate's top face
y = 0. Every artifact of this job uses this frame; OD-E01 enters by the joint of §4.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c08_tray | FDM | machines/creality-k1c.toml (enclosed; build volume UNKNOWN → A-09) | PETG (BOM) | 1270 | as printed | A-10 |

Environment: the electric zone behind the bulkhead; the board's heatsink (TO-220
triac) warms the air beside it; mains on the board's solder side and faston tabs;
dry (the bulkhead's base rail dams the wet side, OD-C02 A-12). Loads: the board
(≈ 0.1 kg), the push of a faston plug onto a tab (toward −X, into the standoffs),
a pulled wire.

## §4 Architecture and concepts

- **C1 — an upright wall on a floor flange, four standoffs, the board on edge
  (CHOSEN).** One solid.
  - **Board joint** (A-03): the OD-E01 datum frame (origin on hole H1's axis at
    the board's top face, +Z out of the component side, +X along the long edge)
    maps into the machine frame by the proper rotation board x → −Z,
    board y → +Y, board z → +X, its origin at (84.0, 80.0, −100.0): the board's
    component face lies on the plane x 84.0, its solder face on x 82.44
    (thickness 1.562, INTAKE X-24), its outline over y 24.0 … 83.87,
    z −195.0 … −94.84 (X-20 … X-23), its tallest part (the heatsink, 25.262
    above the board, X-33) reaching x 109.26; the six faston tabs (X-40 … X-42)
    stand along the lower edge at y ≈ 29.5, z −136 … −188, tips at x 94.6, and
    the connectors J1 … J3 (X-43 … X-45) at the front end, z −88 … −112.
  - **Wall** 3.0 thick, x 73.0 … 76.0 (2.0 of air to the bulkhead's base rail at
    x 71), z −230.0 … −70.0, y 0 … 92.0 (its front end 8 behind the bulkhead's
    window 4 at z −55 ± 7, X-19).
  - **Floor flange** 4.0 thick, y 0 … 4.0, x 73.0 … 112.0, z −230.0 … −70.0, the
    wall rising from its −X edge; four Ø3.4 through-holes along Y at
    (x 88.0, z −222.0), (x 106.0, z −222.0), (x 88.0, z −78.0), (x 106.0, z −78.0)
    — outside the board's z span, so each is reached from above with a driver
    after the top panel is off — for M3 × 8 screws into four new M3 inserts in
    OD-C01 at the same (x, z) (A-01).
  - **Gussets**, four, 3.0 thick in XY planes, at z −230.0 … −227.0,
    −212.0 … −209.0, −88.0 … −85.0 and −73.0 … −70.0 (clear of the screw
    heads at z −222 and −78, ≥ 6 outside the board's z span): right triangles
    with a 20.0 leg up the wall's +X face and a 20.0 leg along the flange's top
    (E-06).
  - **Standoffs**, four, along +X from the wall's face x 76.0 to the solder face
    x 82.44 (6.44 tall), at the board's holes as mapped by the joint: H1
    (z −100.00, y 80.00) and H2 (z −100.01, y 27.99) (X-25, X-26), Ø10.0 with a
    Ø4.0 × 6.0 blind insert bore along −X from x 82.44 for M3 × 8 screws
    through the board's Ø4.0 holes (A-04); H5 (z −157.52, y 81.98) and H6
    (z −157.51, y 30.99) (X-29, X-30), Ø6.0 with a locating pin Ø1.8 × 2.5 on
    top through the board's Ø2.48 holes (0.34 per side, D-04d). The solder face
    keeps 6.44 of air to the wall (A-05). Every standoff grows from the wall
    (E-06).
  - **Tie points** for the board's wires (E-11): two pairs of slots 2.0 (z) ×
    4.0 (y) through the wall along X, at y 86.0 … 90.0, each pair 8.0 apart
    (centres z −176 / −168 and z −122 / −114), so a 2.5 mm cable tie loops
    through the wall above the board's top edge (y 83.87).
  - Print orientation (A-08): **lying on the wall's outer face** x 73 on the
    bed, build direction +X: the flange, gussets, standoffs and pins rise as
    vertical prisms; the insert bores are vertical; the four flange holes run
    along Y, horizontal in the print (their crowns are the named exception).
    Envelope 39.0 × 92.0 × 160.0 (x 73 … 112, y 0 … 92, z −230 … −70); on
    the bed 92 × 160, 39 tall.
- **C2 — the board lying flat on a tray.** Rejected: the board is 59.9 wide and
  the zone 50 (x 70 … 120).
- **C3 — the board on the bulkhead's electric face.** Deferred: OD-C02 has no
  inserts on that face and is delivered.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 39.0 × 92.0 × 160.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x 73.0 … 112.0, y 0 … 92.0, z −230.0 … −70.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) at the identity: the flange's underside on OD-C01's top face is the designed contact, `clearance = 0`, `interference ≤ 0` mm³; OD-E01 at the joint of §4: the solder face on the four standoff tops is the designed contact (`clearance = 0`, `interference ≤ 0`), the two pins inside H5 and H6 with ≥ 0.30 per side (D-04d), everything else of the board ≥ 0.5 from the tray (E-01); tray to OD-C02 ≥ 1.5; OD-E01 to OD-C02 ≥ 10.0; OD-E01 inside x 70 … 117, z −240 … −30, y ≥ 10 (A-06). (b) the board slid onto the pins along −X from +5.0 above its seat in steps ≤ 0.5: `interference ≤ 0` with the tray | Hard | CAD | house | `clearance`, `interference`, `envelope` | A-02, A-03, A-06 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 wall, 1 flange, 4 gussets, 4 standoffs (2 with a Ø4.0 blind bore, 2 with a Ø1.8 pin), 4 Ø3.4 flange holes, 4 tie slots | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh (written by the orchestrator, checked by the reviewer) | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0`, except the two locating pins (Ø1.8, gated by D-06a) and the 0.44 floor under each insert bore, which stands on the 3.0 wall | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the K1C build volume, lying on the wall: 92.0 × 160.0 on the bed, 39.0 tall | Hard | part | machine | `envelope` | A-09 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (wall on the bed, build direction +X): the flange, gussets, standoffs and pins are vertical prisms, the gusset hypotenuses face up; the crowns of the four horizontal Ø3.4 flange holes are the named exception below, excluded by position, their least angle reported | Hard | part | floor | `overhang_census(build_dir=(1,0,0))` | A-08 |
| D-03b | Unsupported bridge | span ≤ 5: the Ø3.4 flange holes bridge 3.4; nothing else bridges | Hard | part | floor | reviewer, from sections | A-08 |
| D-04a | Clearance hole for a fastener | the four flange holes Ø ≥ 3.25 (designed Ø3.4) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-04c | Clearance around a seated component | ≥ 0.5 per side between the tray and OD-E01 away from the designed contacts (= U-03 (a)) | Hard | part | house | `clearance` | A-02 |
| D-04d | Printed sliding fit | each pin in its board hole ≥ 0.30 per side (pin Ø1.8 in Ø2.486 / Ø2.460) | Hard | part | house | `clearance` (pin to the hole's wall in OD-E01) | A-02 |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around each of the two Ø4.0 insert bores (the Ø10 standoffs) | Hard | part | struct | `bore_census`, `radial_extent` | A-07 |
| D-05b | Heat-set insert hole | the two insert bores Ø 4.0 ± 0.05, depth 6.0 ± 0.1 (≥ 5.7) | Hard | part | floor | `bore_census`, `locate_bore` | A-07 |
| D-06a | Minimum feature | ≥ 1.0 (the pins Ø1.8) | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the insert bores are formed by the insert, the flange holes are clearance holes | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 around each insert bore (Ø10 standoff: 3.0) | Hard | part | struct | `min_wall` | — |
| E-01 | Component keep-out | = D-04c | Hard | part | house | `clearance` | A-02 |
| E-05 | Mounting-hole alignment | the two insert bores coaxial with OD-E01's H1 and H2, the two pins with H5 and H6, at the joint: offset ≤ 0.10 | Hard | CAD | house | `locate_bore` on both solids | A-02, A-03 |
| E-06 | Boss support | every standoff grows from the wall; the flange tied to the wall by four gussets | Hard | part | struct | reviewer, from sections | — |
| E-11 | Strain relief and venting | two cable-tie slot pairs above the board; the bay is vented by the back panel (OD-C11) and the tray does not enclose the board (open on +X, ±Z and above) | Hard | part | house | reviewer, from sections | A-11 |
| REQ-01 | Floor inserts | four Ø3.4 ± 0.1 through-holes along Y at (x 88.0, z −222.0), (106.0, −222.0), (88.0, −78.0), (106.0, −78.0), offset ≤ 0.10, 4.0 ± 0.1 long; the flange's underside one plane at y 0.00 ± 0.10 | Hard | CAD | A-01 | `locate_bore`, `envelope` | A-01 |
| REQ-02 | Board joint and seat | standoff tops at x 82.44 ± 0.05 (four coplanar faces); insert bores Ø4.0 at (z −100.00, y 80.00) and (z −100.01, y 27.99); pins Ø1.8 ± 0.05 at (z −157.52, y 81.98) and (z −157.51, y 30.99), 2.5 ± 0.1 long; every position offset ≤ 0.10 | Hard | CAD | A-03 | `locate_bore`, `bore_census`; reviewer from sections | A-02, A-03 |
| REQ-03 | Bulkhead clearance | nothing of the tray at x < 73.0 (`envelope` min_x); its front end at z −70.0 ± 0.1 keeps the bulkhead's window 4 (z −62 … −48) clear | Hard | CAD | A-06 | `envelope` | A-06 |
| REQ-04 | Driver access | each flange hole's axis clear of the tray and of OD-E01 from y 4.0 up to y 120 within r 4.0 (a driver reaches every screw from above with the board mounted) | Hard | CAD | client (X-66) | `interference` of four Ø8 × 116 cylinders with the tray and the board = 0 | A-03 |
| REQ-05 | Faston access | nothing of the tray at x > 84.0 within z −195 … −95 (the board's span) other than the standoffs and pins, so a faston plug reaches each tab from +X | Hard | CAD | A-03 | `interference` of the box x 85 … 117, y 4 … 92, z −195 … −95 with the tray = 0 (the pins end at x 84.94) | A-03 |
| REQ-06 | Hold under a plug push | **Soft.** The board does not flex visibly when a faston plug is pushed on at the tab farthest from the standoffs (z −188, 31 behind H5/H6); not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered at the first assembly | Soft | part | client | — (bench) | A-04, A-12 |

**Named exceptions** (Usta U-18): D-03a for the crowns of the four horizontal Ø3.4 flange holes in the print (bridges 3.4, within D-03b), the usual FDM practice for small horizontal holes (as on OD-C02); recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | Fastening to OD-C01 (INTAKE §4 gap 6) | four M3 × 8 screws from above through the flange into four **new** M3 inserts in the OD-C01 plate at (88, −222), (106, −222), (88, −78), (106, −78): an OD-C01 spec change (a REQ row like its REQ-10 for OD-C07), or Ø4.0 holes drilled into a printed plate before the inserts go in; nothing fastens to OD-C02 (it has no inserts on its electric face) | the plate has no holes there; the Usta prefers another fastening | this spec (design choice); INTAKE X-60 | OD-C01's next revision or the Usta's drill | OPEN |
| A-02 | OD-E01 geometry (INTAKE §4 gap 9) | the scanned envelope as delivered (BAND_NOT_MET, accepted for envelope and clearance studies, X-79): outline −5.162 … 95.002 × −56 … 3.869, thickness 1.562, holes H1 Ø4.044 at (0, 0), H2 Ø4.012 at (0.013, −52.009), H5 Ø2.486 at (57.519, 1.976), H6 Ø2.460 at (57.511, −49.008); heatsink top 25.262; no calipers | the holes or the outline are off by more than the clearances; the pins miss | INTAKE X-20 … X-50 | calipers on H1–H2 pitch, H5–H6, outline (the E01 report's L1 rerun list) | OPEN |
| A-03 | Board orientation and fastening (INTAKE §4 gaps 1, 2) | on edge, parallel to the bulkhead, solder side toward it, the H1/H2 edge to the front (joint of §4); M3 × 8 through H1 and H2 into inserts, pins in H5 and H6; the heatsink's own screws and the other holes untouched | the OEM fixing differs; a tab or a connector is unreachable | this spec (design choice) | the first assembly | OPEN |
| A-04 | Screws into the board | M3 × 8 ISO 7380 through the 1.562 board into the 5.7 insert (6.4 of thread in the insert), a plastic or fibre washer under the head on the component side | a head touches a track; the screw bottoms out | this spec; INTAKE X-70 | the Usta looks at the board around H1, H2 | OPEN |
| A-05 | Solder side and mains (INTAKE §4 gap 5) | the solder side (invented flat in the scan, X-49) keeps 6.44 of air to the tray's wall, and the standoffs touch it only within r 5 of H1 and H2 and r 3 of H5 and H6; the tray is an insulator (PETG); no creepage figure is gated (the board's own design sets it); the heatsink's two screw heads on the solder side (X-35, X-36) protrude < 6 | a lead, a screw head or a track at mains potential lies on a standoff | this spec; INTAKE X-49, §4 gap 5 | the Usta looks at the solder side | OPEN |
| A-06 | Zone limits | the board within x 70 … 117 (a side panel's inner face assumed at x ≥ 117), z −240 … −30, ≥ 10 above the plate; the tray 2.0 from the bulkhead's base rail (OD-C02 A-07: keep 3 from the wall's face, here 6) | the side panel OD-C13 comes closer than x 117 | OD-C01 A-08; OD-C02 A-07 (INTAKE X-01, X-02, X-13, X-61) | OD-C13 design | OPEN |
| A-07 | Insert | M3 × 5.7 × Ø4.6 heat-set inserts in Ø4.0 × 6.0 blind bores (the project's figure) | the insert pulls out | INTAKE X-69 (as OD-C01 A-11) | the Usta's stocked insert datasheet | OPEN |
| A-08 | Print orientation | lying on the wall's outer face (x 73 on the bed), build direction +X, no supports | the 160 long wall warps; the pins break | this spec | first print | OPEN |
| A-09 | K1C build volume (INTAKE §4 gap 8) | 220 × 220 × 250 (Creality specification, not in the machine file); the tray is 92 × 160 on the bed | does not fit (no risk at this size) | as OD-C02 A-08 | the Usta reads the printer | OPEN |
| A-10 | Material | PETG, 1270 kg/m³ (BOM), on the K1C; the heatsink is ≥ 25 from the tray's wall | the standoffs creep under the screws' clamp | INTAKE X-58, X-65 | the Usta names the filament | OPEN |
| A-11 | Wires, mains entry, venting (INTAKE §4 gaps 3, 4, 11) | the looms run from the faston tabs and connectors to the bulkhead's windows and the back panel's cord pass-through (OD-C11) over the tray's top and front; two tie points on the tray; the bay is open to the back panel's vent slots; grommets in the bulkhead windows are OD-E00's | a wire is too short or chafes; the heatsink runs hot | this spec | OD-E00 wiring; the first power-on | OPEN |
| A-12 | Board support | two screws and two pins on four standoffs hold the board on edge; the faston tabs (pushed toward −X) are 31 … 45 behind the nearest support | the board flexes when a plug is pushed on | this spec | first assembly (REQ-06) | OPEN |
| A-13 | Scope (INTAKE §4 gaps 7, 10) | OD-E02 (front buttons) and OD-E03 … E05 (switches) mount on the front panel OD-C09, not on this tray | the OEM loom is too short from the bay to the front | this spec; chassis/README row 10 (INTAKE X-63, X-76) | OD-C09 design | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-01 | electronics path 1 (the OEM power PCB OD-E01): "c08 i will use original pcb for this stage" | the Usta | usta_gate question_answered |
| 2026-10-01 | job opened at PUBLIC on the Usta's "what can start now please initiate it"; C1 proposed | Oğuz | job_start |
| 2026-10-01 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and the request of 2026-10-01; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-10-01 | INTAKE §4 gaps 1 … 12 are answered by §4 as design choices, all A-## rows | Oğuz | INTAKE_v01 §4 |
| 2026-10-01 | REQ-06 (the board under a plug push) is a Soft bench gate answered at the first assembly | Oğuz | §5 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-01 | first draft from the OD-C01 and OD-C02 specs and the OD-E01 report |
| 1.0 | 2026-10-01 | INTAKE_v01 cross-references in §6; ratified |
