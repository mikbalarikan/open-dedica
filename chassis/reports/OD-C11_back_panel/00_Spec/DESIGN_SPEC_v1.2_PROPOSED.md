# DESIGN_SPEC — OD-C11 printed back panel (20261001-od-c11-back-panel)

Version 1.2 · PROPOSED (awaits the Usta's halt decision after the v02 stop; 1.1 was RATIFIED by the Usta on 2026-10-01 (standing instruction of 2026-09-30 and the "what can start now please initiate it" of 2026-10-01: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7)) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C11 is the 3D-printed removable back panel of the Open Dedica espresso machine
(BOM: removable with 4 screws; SOURCING_GUIDE §6 rule 4): the rear wall of the
machine, standing on the base frame OD-C01 along its rear edge, behind the pump
cradle OD-C03 with the pump and behind the rear ends of the bulkhead OD-C02 and
the electronics bay. It passes the mains cord (through a grommet, OD-C14) on the
electric side and, while the water tank stands on the table (the Usta,
2026-10-01), the tank's two tubes on the wet side; it vents the electronics bay;
and it gives the top panel OD-C10 the two insert bosses for its rear screws.
Done means: one valid printable solid standing on the OD-C01 plate inside its
rear edge, held by four M3 screws driven from above into four new inserts in the
plate, nothing of it in the pump's or the bulkhead's space, its pass-throughs and
vents at the places of §4, and every unconfirmed value in §6. The side panels,
the top panel, the tank dock, the grommet, the feet and the tube runs are not
designed: their rows are assumptions and the job is reopened when they land.

**Deliverables** (tier M): STEP AP242 of the panel; the check assembly STEP
(panel + OD-C01 + OD-C02 + OD-C03 with OD-H01 as OD-C01 places them); STL and
3MF; build and check scripts; REPORT; sections. No drawings or renders.

**Out of scope:** the side panels OD-C12/C13 and their corners (OD-C16), the
top panel OD-C10 (next job; it uses REQ-07), the tank dock OD-C06 (deferred by
the Usta), the grommet OD-C14, the feet OD-C15, the tube and cord runs, calipers,
drawings, renders. OD-C01 itself is not changed by this job: the four new insert
holes it needs are an OD-C01 spec change handed over (A-01).

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-C01 (base frame, delivered) | `00_Spec/inputs/OD-C01_base_frame.step` (INTAKE §1): plate y −6 … 0, x ±120, z −305 … +100, corners R 10 about (±110, −295) and (±110, +90); feet holes Ø3.4 at (±110, −295); no hole yet under this panel's flange (A-01) | — | OD-C01 spec 1.2 §4, REQ-05, REQ-07 | CONFIRMED as the input; its numbers are §6 rows |
| Reference solids, the rear neighbours | OD-C02 bulkhead (identity; rear end z −240, x 59 … 71, y 0 … 215); OD-C03 + OD-H01 placed by OD-C01 A-03 (rotation local x → +Z, y → −Y, z → +X at (0, 40, −205)): the cradle's foot reaches z −245 | — | OD-C01 spec 1.2 §4; OD-C02 spec 1.2 §4 | CONFIRMED as inputs; poses are the OD-C01 rows |
| Fasteners | M3 heat-set inserts (OD-F01, Ø4.0 bore, 5.7 long) and M3 × 8 screws (OD-F02, ISO 7380 head Ø5.7) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard) |

**Coordinate frame:** the OD-C01 machine frame, so every overlay is the identity:
X to the user's right, +Y up, +Z toward the user (the front), the plate's top face
y = 0. The panel's outer face is the plane z = −302.0, its inner face z = −299.0.
Every artifact of this job uses this frame.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c11_back | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-09) | PETG (BOM: ASA; a 232 × 215 panel warps in ASA on the open Kobra; the panel is far from the heat, A-10) | 1270 | as printed | A-10 |

Environment: the rear of the machine, 56 mm behind the pump cradle's foot and
57 behind the bulkhead's and the bay's rear ends; mains cord on the right,
cold-water tubes on the left; room temperature plus the bay's warm air. Loads:
the top panel's two rear screws, a hand pulling the panel off, the cord's pull
(taken by the grommet).

## §4 Architecture and concepts

- **C1 — one wall with a floor flange at each end, a top ledge with two insert
  bosses, three pass-throughs and five vent slots (CHOSEN).** One solid.
  - **Wall** 3.0 thick, z −302.0 … −299.0, x −116.0 … +116.0, from the plate
    y 0 up to y 215.0 (the bulkhead's height, OD-C02 A-06; the top panel sits on
    y 215). At |x| = 116 the plate's corner arc (R 10 about (±110, −295)) lies at
    z −303.0, so the wall's foot stands on the plate everywhere with ≥ 1.0 of
    plate behind it (A-02; INTAKE X-01 … X-05).
  - **Floor flanges**, two, 4.0 thick, y 0 … 4.0, z −299.0 … −277.0 (22 deep),
    at x −104.0 … −72.0 and +72.0 … +104.0, outside the tank zone x ±70 (OD-C01
    A-07) and clear of the feet holes at (±110, −295) (INTAKE X-06; 1.1: the
    flanges of 1.0 reached x ±114 and covered them, v01 REPORT). Each has two
    Ø3.4 through-holes along Y at (x ±81.0, z −282.0) and (x ±95.0, z −282.0),
    for M3 × 8 screws driven from above into four new M3 inserts in OD-C01 at the
    same (x, z) (A-01); each screw axis lies 5.0 in front of the top ledge
    (z −287), so a straight driver Ø ≤ 6 reaches it from above (1.1: at z −290
    the ledge covered every screw, v01 REPORT); the screw heads Ø5.7 keep ≥ 2.1
    from the gussets. Two **gussets** per flange, 4.0 thick, at its ends
    (x ±72.0 … ±76.0 and x ±100.0 … ±104.0): right triangles in the YZ plane
    with a 16.0 leg along the flange's top and a leg up the wall of 30.0 for the
    inner gussets (top y 34) and 18.0 for the outer gussets (top y 22, 2.0 below
    the pass-throughs at y 24; 1.2: the 30.0 outer leg blocked the tube hole at
    (−100, 30) and the cord hole at (95, 30), v02 REPORT) (E-06).
  - **Top ledge** 4.0 thick, y 211.0 … 215.0, z −299.0 … −287.0 (12 deep), along
    x −114.0 … +114.0, its top face flush with the wall's top at y 215.0; two
    **insert bosses** below it, blocks x ±(84.0 … 96.0), y 203.0 … 211.0,
    z −299.0 … −287.0, each with a Ø4.0 × 6.0 blind bore along −Y from y 215.0
    at (x ±90.0, z −293.0) for the M3 inserts that take the top panel's rear
    screws (A-05).
  - **Pass-throughs** through the wall along Z, round: **cord** Ø12.0 at
    (x 95.0, y 30.0) for the mains cord OD-E06 in the grommet OD-C14 (A-03);
    **tubes** Ø12.0 at (x −100.0, y 30.0) and (x −84.0, y 30.0) for the tank
    tube OD-W11 and the bypass return TUBE 3 (A-04; the tank seat's hose
    nipples are Ø6.9 over the lip, INTAKE X-25).
  - **Vents**: five slots through the wall along Z, 4.0 wide (X) × 80.0 tall
    (Y), centres x 78.0, 86.0, 94.0, 102.0, 110.0, from y 100.0 to 180.0, ends
    round (R 2.0), behind the electronics bay (A-06).
  - Nothing of the panel lies at z > −277.0 (REQ-05): the pump cradle's foot
    ends at z −245, the bulkhead at −240.
  - Print orientation (A-08): **lying on the outer face** z = −302 on the bed,
    build direction +Z: the wall is a flat plate, the flanges, ledge, gussets and
    bosses rise as vertical prisms; the pass-throughs and vents are vertical
    holes; the four Ø3.4 flange holes and the two Ø4.0 boss bores run along Y,
    horizontal in the print (their crowns are the named exception); the ledge's
    underside (y 211, facing −Y) is a vertical face in the print. Envelope
    232.0 × 215.0 × 25.0 (x ±116, y 0 … 215, z −302 … −277); on the bed
    232 × 215, 25 tall.
- **C2 — the back panel screwed to the side panels' rear edges from outside.**
  Removable without the top panel, but it needs side panels with rear posts and
  inserts; deferred until OD-C12/C13 (and the acrylic option, chassis/README row
  12) are decided.
- **C3 — two half panels for the K1C (≤ 220).** Deferred until A-09 is answered.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 232.0 × 215.0 × 25.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±116.0, y 0 … 215.0, z −302.0 … −277.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) at the identity: the wall's and the flanges' undersides on OD-C01's top face are the designed contact, `clearance = 0`, `interference ≤ 0` mm³; the panel's underside lies wholly over plate material (its footprint inside the plate's outline, ≥ 0.5 from the edge and the corner arcs; the flanges ≥ 3.0 and the wall's foot ≥ 2.0 from the edge of every existing OD-C01 hole (1.2: the wall foot stands 2.300 from the feet holes' rims by §4's geometry, v02 REPORT)); the four flange holes ≥ 6.0 centre to centre from every existing OD-C01 hole (the feet holes at (±110, −295)); panel to OD-C03 and OD-H01 (as OD-C01 A-03 places them) ≥ 20.0; panel to OD-C02 ≥ 20.0. (b) the panel lowered along −Y from +40.0 above its seat in steps ≤ 2.0: `interference ≤ 0` with every reference solid at every step | Hard | CAD | house | `clearance`, `interference`, `envelope` | A-01, A-02, A-07 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 wall, 2 floor flanges, 4 gussets, 1 top ledge, 2 insert bosses, 4 Ø3.4 flange holes, 2 Ø4.0 blind bores, 3 Ø12.0 pass-throughs, 5 vent slots | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh (written by the orchestrator, checked by the reviewer) | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default for enclosures; wall 3.0, flanges and ledge 4.0, the webs between vent slots 4.0, between the tube holes 4.0) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the Kobra Max 3 build volume, lying on the outer face: 232.0 × 215.0 on the bed, 25.0 tall | Hard | part | machine | `envelope` | A-09 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (outer face on the bed, build direction +Z): the flanges, ledge, gussets and bosses are vertical prisms, the gusset hypotenuses face up; the crowns of the four horizontal Ø3.4 flange holes and the two horizontal Ø4.0 boss bores are the named exception below, excluded by position, their least angle reported | Hard | part | floor | `overhang_census(build_dir=(0,0,1))` | A-08 |
| D-03b | Unsupported bridge | span ≤ 5: the Ø3.4 and Ø4.0 horizontal holes bridge ≤ 4.0; nothing else bridges | Hard | part | floor | reviewer, from sections | A-08 |
| D-04a | Clearance hole for a fastener | the four flange holes Ø ≥ 3.25 (designed Ø3.4) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around each of the two Ø4.0 insert bores (the 12 × 12 bosses) | Hard | part | struct | `bore_census`, `radial_extent` | A-05 |
| D-05b | Heat-set insert hole | the two insert bores Ø 4.0 ± 0.05, depth 6.0 ± 0.1 (≥ 5.7) | Hard | part | floor | `bore_census`, `locate_bore` | A-05 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the insert bores are formed by the insert, the rest are clearance holes and pass-throughs | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 around each insert bore (the boss 12 wide about the bore: 4.0 each side; 4.0 to the wall's inner face) | Hard | part | struct | `min_wall` | — |
| E-06 | Boss support | each insert boss is a block tied into the wall and the ledge; each flange tied to the wall by two gussets | Hard | part | struct | reviewer, from sections | — |
| E-11 | Strain relief and venting | the cord's strain relief is the grommet OD-C14 in the Ø12 cord hole (not designed: A-03); the five vent slots open the electronics bay's rear | Hard | part | house | reviewer, from sections | A-03, A-06 |
| REQ-01 | Floor inserts | four Ø3.4 ± 0.1 through-holes along Y at (x ±81.0, z −282.0) and (x ±95.0, z −282.0), offset ≤ 0.10, 4.0 ± 0.1 long; the underside one plane at y 0.00 ± 0.10 | Hard | CAD | A-01 | `locate_bore`, `envelope` | A-01 |
| REQ-02 | Wall plane and footprint | the outer face at z −302.00 ± 0.10 and the inner face at z −299.00 ± 0.10 over the wall's height (sections at y 50 and y 200); x ±116.0 ± 0.1 | Hard | CAD | A-02 | `envelope`; reviewer from sections | A-02 |
| REQ-03 | Cord pass-through | one Ø12.0 ± 0.1 hole through the wall along Z at (x 95.0, y 30.0), offset ≤ 0.10 | Hard | CAD | A-03 | `locate_bore` | A-03 |
| REQ-04 | Tube pass-throughs | two Ø12.0 ± 0.1 holes through the wall along Z at (x −100.0, y 30.0) and (x −84.0, y 30.0), offset ≤ 0.10 | Hard | CAD | A-04 | `locate_bore` | A-04 |
| REQ-05 | Keep-out | no panel material at z > −277.0 (`envelope` max_z) and none inside the tank zone x ±70 below y 100 except the wall itself (z ≤ −299 ± 0.1) | Hard | CAD | A-07 | `envelope`; `interference` of the box x ±70, y 0 … 100, z −298.8 … −250 with the panel = 0 (1.1: the box starts 0.2 in front of the wall's nominal face so the wall's ±0.1 band does not read as an intrusion, v01 sweep) | A-07 |
| REQ-06 | Vents | five slots 4.0 ± 0.1 × 80.0 ± 0.1 through the wall along Z, centres x 78/86/94/102/110 (± 0.1), y 100.0 … 180.0 (± 0.1) | Hard | CAD | A-06 | `feature_census`; reviewer from sections | A-06 |
| REQ-07 | Top panel inserts | two Ø4.0 ± 0.05 blind bores along −Y from y 215.0, depth 6.0 ± 0.1, at (x ±90.0, z −293.0), offset ≤ 0.10; the ledge's top face one plane at y 215.00 ± 0.10 over z −299 … −287 | Hard | CAD | A-05 | `locate_bore`, `bore_census`, `envelope` | A-05 |
| REQ-08 | Driver access | each flange hole's axis clear of the panel from y 4.0 up to y 260.0 within r 3.0 (a straight driver reaches every screw from above with the top panel off) | Hard | CAD | client (X-36, X-37) | `interference` of four Ø6 cylinders y 4 … 260 with the panel = 0 | — |
| REQ-09 | Stiffness | **Soft.** The panel does not drum or flex visibly with the top panel on and the side panels absent; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print | Soft | part | client | — (bench) | A-11 |

**Named exceptions** (Usta U-18): D-03a for the crowns of the four horizontal Ø3.4 flange holes and the two horizontal Ø4.0 insert bores in the print (bridges ≤ 4.0, within D-03b), the usual FDM practice for small horizontal holes (as on OD-C02); recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | What the panel fastens to (INTAKE §4 gaps 2, 8) | four M3 × 8 screws from above through the floor flanges into four **new** M3 inserts in the OD-C01 plate at (±81, −282) and (±95, −282): an OD-C01 spec change (a REQ row like its REQ-10 for OD-C07), or Ø4.0 holes drilled into a printed plate; the feet holes at (±110, −295) are 19.8 away and the flanges end 4.3 from their edge; the panel comes off after the top panel (whose rear screws go into REQ-07) | the plate has no holes there; the Usta wants the panel off without the top panel (C2) | this spec (design choice) | OD-C01's next revision or the Usta's drill | OPEN |
| A-02 | Plate edge and corners | the delivered plate: rear edge z −305, corners R 10 about (±110, −295) (at x ±116 the edge lies at z −303.0); the wall at z −302 … −299 stands 3 inside the rear edge, its ends 4 inside the side edges, leaving the strip for the side panels and their corners | the side panels need the strip differently | INTAKE X-01 … X-05 | OD-C12/C13, OD-C16 designs | OPEN |
| A-03 | Mains cord (INTAKE §4 gaps 3, 5) | the cord OD-E06 (≈ Ø7, not measured) passes a Ø12 hole at (95, 30) in a TPU grommet OD-C14 (not designed) that clamps it; an IEC inlet OD-E60 would need its own cut-out (a later revision) | the grommet does not fit Ø12; the cord pulls on the board | this spec; INTAKE X-45 … X-48 | OD-C14 design; the cord in hand | OPEN |
| A-04 | Tank tubes (INTAKE §4 gaps 4, 12) | the tank on the table (the Usta, 2026-10-01); its tubes (OD-W11, TUBE 3; silicone, over the seat's Ø6.9 hose nipples, INTAKE X-23 … X-27) pass two Ø12 holes at (−100, 30) and (−84, 30) on the wet side, toward the flowmeter on the left (OD-C07) | a tube's outer Ø exceeds 12 with a grommet; the route is long | this spec | the tubes in hand; OD-C06 | OPEN |
| A-05 | Top panel inserts | OD-C10 screws down into two M3 inserts in this panel's ledge at (±90, −293) (OD-C10 spec 1.0 REQ-04); the ledge top at y 215, the bulkhead's height | OD-C10 changes its pattern | this spec; OD-C10 spec 1.0 | OD-C10 review | OPEN |
| A-06 | Venting (INTAKE §4 gap 6) | five slots 4 × 80 behind the electronics bay (x 76 … 112, y 100 … 180) let the board's heat out; no vent on the wet side | the bay runs hot; a tool or a finger reaches through a slot (4.0 wide) | this spec | the first power-on | OPEN |
| A-07 | Rear neighbours (INTAKE §4 gap 11) | the pump cradle's foot ends at z −245 and the bulkhead at z −240 (OD-C01 §4, INTAKE X-11, X-14); the pump body's rear-most z is not stated and is measured from OD-H01 as placed; the tank zone x ±70, z −305 … −250 stays free above the floor flanges (the flanges stop at |x| 72) | the pump or a hose touches the panel | INTAKE X-11 … X-14, X-18 | the OD-000 assembly | OPEN |
| A-08 | Print orientation | lying on the outer face, build direction +Z, no supports | the 232 × 215 plate warps; brim needed | this spec | first print | OPEN |
| A-09 | Kobra Max 3 build volume (INTAKE §4 gap 10) | 420 × 420 × 500 (Anycubic specification, not in the machine file); the panel is 232 × 215 on the bed | does not fit: C3 (halves) | INTAKE X-59 (as OD-C01 A-09) | the Usta reads the printer | OPEN |
| A-10 | Material (INTAKE §4 gaps 1, 9) | PETG, 1270 kg/m³, on the Kobra Max 3 (the BOM says ASA; the panel is ≥ 50 from any hot part, so PETG fits the thermal map; ASA on the open Kobra warps at this size, as OD-C01 A-10) | the Usta wants ASA throughout the shell | INTAKE X-33, X-40, X-57, X-60 | the Usta names the filament | OPEN |
| A-11 | Stiffness | a 3 mm PETG wall 232 × 215 with a 4 mm ledge on top and two floor flanges, screwed at four points to the plate and held by the top panel's two screws at the top; the side edges free until the side panels exist | the panel drums with the pump's vibration | this spec | first print (REQ-09) | OPEN |
| A-12 | Joints with the side and top panels (INTAKE §4 gap 7) | the top panel's skirt (outer z −305) closes over the wall's top; the side panels OD-C12/C13 meet the wall's ends at x ±116 (not designed) | the side panels need posts or a lip on this panel | this spec | OD-C12/C13 designs | OPEN |
| A-13 | Gaskets (INTAKE §4 gap 13) | none on this panel | — | PROJECT_RULES rule 4 reads on the group head | — | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-01 | the water tank stands on the table; no tank dock now ("i will hold water tank on the table myself no need to design for it now"); the tubes enter through this panel | the Usta | usta_gate question_answered |
| 2026-10-01 | job opened at PUBLIC on the Usta's "what can start now please initiate it"; C1 proposed | Oğuz | job_start |
| 2026-10-01 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and the request of 2026-10-01; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-10-01 | INTAKE §4 gaps 1 … 13 are answered by §4 as design choices, all A-## rows | Oğuz | INTAKE_v01 §4 |
| 2026-10-01 | REQ-09 (stiffness) is a Soft bench gate answered by the first print | Oğuz | §5 |
| 2026-10-01 | v01 REPORT stop: spec 1.0's flanges (to x ±114) covered OD-C01's feet holes at (±110, −295), and the top ledge covered every flange screw at z −290; 1.1 ends the flanges at x ±104, deepens them to z −277 and moves the screws to (±81, −282) and (±95, −282), 5 in front of the ledge; REQ-05's box starts 0.2 in front of the wall | Oğuz (on the standing instruction) | 01_CAD/REPORT_od_c11_back_v01.md; A-01 |
| 2026-10-01 | v02 REPORT stop at the build cap: the outer gussets (wall leg 30) blocked two pass-throughs and the wall's foot stands 2.300 from the feet holes' rims against U-03's 3.0; 1.2 shortens the outer gussets' wall leg to 18 and sets the wall foot's distance at ≥ 2.0; a third build waits on the Usta's halt decision | Oğuz (proposed) | 01_CAD/REPORT_od_c11_back_v02.md |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-01 | first draft from the OD-C01, OD-C02 and OD-C03 specs and the OD-W03 report |
| 1.0 | 2026-10-01 | INTAKE_v01 cross-references in §6; ratified |
| 1.2 | 2026-10-01 | v02 stop: outer gussets' wall leg 18.0 (top y 22) so they clear the pass-throughs; U-03 (a) hole-edge distance ≥ 3.0 for the flanges and ≥ 2.0 for the wall's foot (§4, U-03); spec 1.1 kept as `DESIGN_SPEC_v1.1.md` |
| 1.1 | 2026-10-01 | v01 stop: flanges x ±(72 … 104), z −299 … −277; flange screws at (±81, −282), (±95, −282); outer gussets at x ±(100 … 104); envelope 232 × 215 × 25 (§4, U-02, U-03, D-02, REQ-01, REQ-05, REQ-08, A-01); spec 1.0 kept as `DESIGN_SPEC_v1.0.md` |
