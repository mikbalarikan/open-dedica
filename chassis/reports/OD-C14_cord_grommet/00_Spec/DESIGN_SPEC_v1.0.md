# DESIGN_SPEC — OD-C14 printed cord grommet (20261002-od-c14-cord-grommet)

Version 1.0 · RATIFIED by the Usta on 2026-10-02 (the answer "4/ 7mm … all printed in pla for now" of 2026-10-02 22:58 UTC and the standing instruction of 2026-09-30: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-C14 is the 3D-printed grommet and strain relief of the Open Dedica mains cord
OD-E06 where it passes the delivered back panel OD-C11 through its Ø12.0 cord
hole at (x 95, y 30) (OD-C11 REQ-03, E-11, A-03). The cord already carries its
moulded plug, and the hole is closed, so the grommet is **split along its axis
into two identical halves** (the BOM's qty 2 is the pair, INTAKE §4 Q4, Q5). The
halves are laid around the cord, pushed into the hole from outside until their
flange meets the wall, and a cable tie (OD-F09) pulled tight in a groove just
inside the wall closes them onto the cord. The tie, wider than the hole, keeps
the grommet from being pulled out; the flange keeps it from being pushed in; the
halves, cut 0.4 short of the axis, close by 0.8 and squeeze the cord, so a pull
on the cord bears on the wall and not on the board's terminals. Done means: one
valid printable solid (one half) that, with its 180° copy, seats in the OD-C11
hole around a Ø7.0 cord at the poses of §2, and every unconfirmed value in §6.

**Deliverables** (tier S): STEP AP242 of the half; the check assembly STEP
(OD-C11, OD-C01, both halves at the open pose, the cord and tie envelopes); STL
(the 3MF is written by the orchestrator from the reviewed STL); build and check
scripts; REPORT; sections. No drawings or renders.

**Out of scope:** any change to OD-C11, the cord's route inside the machine,
the tube pass-throughs, an IEC inlet (OD-E60), calipers, drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| OD-C11 back panel (delivered) | `00_Spec/inputs/OD-C11_back_panel.step` (identity): wall 3.0, outer face z −302.0, inner face z −299.0; cord hole Ø12.0 through along Z at (x 95.0, y 30.0); nearest features: the right floor flange x 72 … 104, y 0 … 4, z −299 … −277, its outer gusset x 100 … 104 rising to y 22 at the wall, the vent slots from y 100 | — | OD-C11 spec 1.2 §4, REQ-03 (INTAKE) | CONFIRMED as the input; A-01 |
| OD-C01 base frame (delivered) | `00_Spec/inputs/OD-C01_base_frame.step` (identity), top face y 0, rear edge z −305 | — | OD-C01 spec 1.2 | CONFIRMED as the input |
| Mains cord OD-E06 | Ø7.0, round, measured with the Usta's calipers (2026-10-02) | — | the Usta's answer (INTAKE X-36) | A-02 |
| Cable tie OD-F09 | 4.8 wide, band ≈ 1.3 thick, PA66 (the BOM's stocked tie) | — | BOM OD-F09 (INTAKE X-39) | A-04 |

**Coordinate frame:** the OD-C01 machine frame (X right, +Y up, +Z front, plate
top y 0). The cord's axis is the line (x 95.0, y 30.0) along Z. The half is
modelled at its installed **open pose** (the upper half, y ≥ 30.4); the other
half is the same solid turned 180° about the cord's axis. The **closed pose**
(tie tight) moves each half 0.4 toward the axis along Y.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c14_grommet_half | FDM | machines/creality-k1c.toml (build volume UNKNOWN → A-07) | PLA (the Usta, 2026-10-02, "all printed in pla for now"; the BOM says TPU) | 1240 | as printed | A-03 |

Environment: the rear wall on the electric side, room temperature plus the bay's
warm air. Loads: a pull or twist on the cord from outside, the tie's tension.

## §4 Architecture and concepts

- **C1 — a split grommet: two identical halves, outer flange, neck, tie groove,
  collar; one cable tie (CHOSEN).** One solid, used twice.
  - The **whole grommet** (both halves before the cut) is a body of revolution
    about the cord's axis, from z −304.0 (outside) to z −291.0 (inside):
    - **Flange** Ø20.0, z −304.0 … −302.0; its inner face on the wall's outer
      face z −302.0 (designed contact).
    - **Neck** Ø11.4, z −302.0 … −299.2: in the Ø12.0 hole with 0.30 per side
      (D-04d), 0.2 beyond the wall's inner face.
    - **Tie groove** Ø10.2, z −299.2 … −294.0 (5.2 wide for the 4.8 tie); the
      tie's band (≈ 1.3) makes a ring ≈ Ø12.8 over the hole's Ø12.0 and its head
      stands higher still.
    - **Collar** Ø11.4, from a 60° flank (from Ø10.2 at z −294.0 to Ø11.4 at
      z −293.654) to z −291.0; it keeps the tie in the groove.
    - **Bore** Ø7.0 through, on the axis; its inside end (z −291.0) chamfered
      0.5 × 45°, its outside end (z −304.0) chamfered 0.50 axial × 0.29 radial
      (60° from horizontal in the print).
  - **The half**: the whole grommet less everything below the plane y 30.4,
    i.e. cut 0.4 short of the axis: its split face is the plane y 30.4. Two
    halves at the open pose leave a 0.8 gap and hold the Ø7.0 cord without
    squeeze; the tie closes the gap, and the bore becomes 7.0 × 6.2: 0.4 of
    squeeze from each side (A-05).
  - Fitting: halves around the cord outside the machine, pushed in along +Z
    until the flanges meet the wall, the tie around the groove with its head
    upward (away from OD-C11's gusset below), pulled tight, the tail cut.
  - Print orientation (A-06): **standing on the flange's outer face** (z −304 on
    the bed), build direction +Z: the flange, neck, groove and collar rise as
    half-cylinders, the split face and the bore are vertical; the downward
    faces are the collar's 60° flank and the bore's 60° chamfer at the bed; no
    supports. Envelope 20.0 × 9.6 × 13.0 (x 85 … 105, y 30.4 … 40.0,
    z −304.0 … −291.0).
- **C2 — a clamp screwed to the plate inside, behind a plain bushing.** Not
  chosen: two different parts and two new OD-C01 inserts for what the tie does.
- **C3 — a one-piece C-ring grommet sprung over the cord.** Not chosen: opening
  a PLA ring by the cord's 7 mm strains it far past PLA's elongation.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 20.0 × 9.6 × 13.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x 85.0 … 105.0, y 30.4 … 40.0, z −304.0 … −291.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | The check assembly carries OD-C11 and OD-C01 at the identity, the half and its 180° copy, a cord envelope (a Ø7.0 cylinder on the axis, z −330 … −260) and a tie envelope (a ring Ø10.2 inside, Ø12.8 outside, z −299.0 … −294.2, i.e. against the wall's inner face). (a) open pose: designed contacts `clearance = 0`: each half's flange face on OD-C11's outer face; each half's bore on the cord envelope (tangent); the tie envelope on each half's groove floor and on OD-C11's inner face; every other pair: half to OD-C11 ≥ 0.30 (the neck in the hole, D-04d), the halves to each other 0.80 ± 0.05, half and tie to OD-C11's gusset and flange ≥ 0.5, to OD-C01 ≥ 10; the tie envelope overlaps the hole's rim seen along Z (its outside Ø > 12.0). (b) closed pose (each half 0.4 toward the axis): the halves touch each other (`clearance = 0`, `interference ≤ 0`), each half to OD-C11 ≥ 0.30, and the cord envelope overlaps each half by 0.40 ± 0.05 radially (the designed squeeze; not an interference finding). (c) assembly path: both halves at the open pose moved along +Z from 20.0 outside their seat to the seat in steps ≤ 2.0, `interference ≤ 0` mm³ against OD-C11 and OD-C01 at every step | Hard | CAD | house | `clearance`, `interference`; the squeeze from `radial_extent` | A-01, A-02, A-04 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: flange, neck, groove, flank, collar (half-cylinders and their end faces), 1 split face (plane y 30.4), 1 half-bore Ø7.0, 2 bore chamfers | Hard | CAD | house | `feature_census`, `radial_extent` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 1.6 (the limit D-01b sets for this part) | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/10.0) rad; `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `stl_max_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 1.6`, set below the 2.0 default for this part (GATES D-01b: "the spec may set a lower value ≥ D-01a with its reason"): a Ø7.0 cord in a Ø12.0 hole leaves 2.5 radial, of which the neck's sliding fit takes 0.3 and the tie groove 0.6; the groove floor is the least wall (1.6) | Hard | part | struct | `min_wall` | A-03 |
| D-02 | Bed fit | 20.0 × 9.6 × 13.0 within the K1C build volume, standing on the flange | Hard | part | machine | `envelope` | A-07 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal with build direction +Z (`overhang_census(build_dir=(0,0,1))`): the collar flank and the bed-side bore chamfer at 60° | Hard | part | floor | `overhang_census` | A-06 |
| D-03b | Unsupported bridge | span ≤ 5: none in the print | Hard | part | floor | reviewer, from sections | A-06 |
| D-04d | Printed sliding fit | the neck and collar to the Ø12.0 hole ≥ 0.30 per side at the open pose | Hard | part | house | `clearance` | A-01 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the bore is a clamp on a compliant cord, sized by REQ-02 | Hard | part | floor | — (N/A by this row) | — |
| J-06 | Printed threads | none | Hard | part | floor | `bore_census` | — |
| E-11 | Strain relief | the cord gripped by the closed halves (REQ-02 squeeze), the grommet held against an outward pull by the tie on the wall's inner face and against an inward push by the flange on its outer face; no sharp edge on the cord at either bore end (the chamfers) | Hard | part | house | reviewer, from sections | A-02, A-04, A-05 |
| REQ-01 | Profile | flange Ø20.0 ± 0.1 over z −304.0 … −302.0; neck Ø11.4 ± 0.05 over z −302.0 … −299.2; groove Ø10.2 ± 0.05 over z −299.2 … −294.0; flank 60° ± 1° to Ø11.4; collar Ø11.4 ± 0.05 to z −291.0; each z ± 0.1; every surface coaxial with the cord's axis, offset ≤ 0.05 | Hard | CAD | house | `radial_extent`, `envelope`; sections | A-01 |
| REQ-02 | Bore and split | bore radius 3.50 ± 0.05 about the axis; split face one plane at y 30.40 ± 0.02; bore chamfers 0.5 × 45° (inside end) and 0.50 × 0.29 (outside end) ± 0.1 | Hard | CAD | house | `radial_extent`, `envelope`, `feature_census` | A-02, A-05 |
| REQ-03 | Identical halves | the half and its copy turned 180° about the cord's axis make the whole grommet less the 0.8 slab: their union at the closed pose has the outline of REQ-01 across X and 0.8 less across Y | Hard | CAD | house | `envelope` of the pair at the closed pose | — |
| REQ-04 | Tie seat | the groove takes the 4.8 tie (5.2 ± 0.1 wide at its floor); the tie envelope's outside Ø12.8 exceeds the hole's Ø12.0; the tie head's zone (5 × 5 × 6 above the groove at +Y) clear of OD-C11 ≥ 0.5 | Hard | CAD | A-04 | `envelope`; `clearance` of a head box | A-04 |
| REQ-05 | Grip | **Soft.** The tied grommet holds the cord against a firm hand pull and does not turn in the hole; not a geometric gate: INCONCLUSIVE with a risk rating, answered by the first fitting | Soft | part | client | — (bench) | A-05 |

**Named exceptions:** none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | OD-C11 hole | the delivered panel: Ø12.0 hole through a 3.0 wall (z −302 … −299) at (95, 30); printed holes come out undersize by 0.1 … 0.2 | the neck does not enter (0.30 per side covers it) | OD-C11 spec 1.2 REQ-03 (INTAKE) | OD-C11's print; calipers on the hole | OPEN |
| A-02 | Cord | Ø7.0 round (the Usta's calipers, 2026-10-02), a PVC jacket that takes 0.4 of squeeze per side | the cord is oval or harder; grip too weak or too tight | the Usta's reading (INTAKE X-36) | the Usta confirms the reading is the jacket's diameter | OPEN |
| A-03 | Material | PLA, 1240 kg/m³ (the Usta, 2026-10-02, "for now"; the BOM says TPU); the halves are stiff, so the squeeze is the tie's work, not the grommet's elasticity; SOURCING_GUIDE §6 rule 3 ("PLA nowhere structural") read as not applying to a cord grommet at room temperature | the halves crack at the tie or creep loose | the Usta's message; BOM OD-C14 | the first fitting | OPEN |
| A-04 | Tie | one OD-F09 cable tie 4.8 wide, band ≈ 1.3, head ≈ 5 × 5 × 6, head upward; one more tie than the BOM's 4 | a wider tie does not fit the 5.2 groove | BOM OD-F09 | the stocked tie | OPEN |
| A-05 | Squeeze | each half cut 0.4 short of the axis: 0.8 of closing, bore 7.0 × 6.2 when tied | not enough grip (cut more) or the jacket is crushed (cut less) | this spec | the first fitting (REQ-05) | OPEN |
| A-06 | Print orientation | standing on the flange, no supports | the 2.0 flange lifts at its corners | this spec | first print | OPEN |
| A-07 | K1C build volume | 220 × 220 × 250 (Creality listing, not in the machine file) | none for a 20 mm part | as OD-C15 A-08 | the machine file | OPEN |
| A-08 | Quantity | the BOM's qty 2 is the pair of halves of one grommet; the tank tubes' Ø12 holes take no OD-C14 | the BOM meant two grommets | this spec (INTAKE §4 Q4) | the Usta | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-02 | the cord measures 7 mm; every printed part in PLA for now | the Usta (2026-10-02 22:58 UTC) | REQUEST.md |
| 2026-10-02 | job opened at PUBLIC; INTAKE §4 Q1 … Q5 answered by §4 as design choices, all A-## rows (material A-03, retention and grip §4 and A-04, A-05, qty A-08, fitting over the plug: the split); C1 proposed | Oğuz | INTAKE_v01 §4 |
| 2026-10-02 | spec 1.0 ratified and C1 chosen on the Usta's answer and standing instruction; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-02 | first issue from INTAKE_v01 and OD-C11 spec 1.2; ratified |
