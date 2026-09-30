# DESIGN_SPEC — OD-C04 printed thermoblock mount (20260930-od-c04-thermoblock-mount)

Version 1.0 · RATIFIED by the Usta on 2026-09-30 (standing instruction of 2026-09-30: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-C04 is the 3D-printed thermoblock mount of the Open Dedica espresso machine. It
holds the OEM cast-aluminium 1300 W thermoblock OD-H11 with its axis horizontal and
its outlet face (the three-pin face) toward the group head, using the thermoblock's
own two screw holes, and bolts to the printed base frame OD-C01. The thermoblock's
skin runs above 100 °C, so no printed surface comes within 10 mm of it (INTAKE
X-R05: "Keep ≥10 mm air gap to any printed part"): the last 10 mm to each screw seat
is a metal spacer. Done means: one valid printable solid with two screw standoffs, a
foot with a screw pattern for OD-C01, ≥ 10.0 mm clearance to OD-H11 everywhere, and
every unconfirmed value in §6. The NTC and TCO brackets OD-H17 and OD-H19 are not
scanned: their rows are assumptions and the job is reopened when they are measured.

**Deliverables** (tier S): STEP AP242 of the mount; the check assembly STEP (mount +
OD-H11 + the two spacer solids as placed); STL; build and check scripts; REPORT;
sections. No drawings or renders (the part goes to the Usta's own printer).

**Out of scope:** OD-C01 base frame, OD-C05 carrier, the water connections OD-H14 /
OD-H15, the brackets OD-H17 / OD-H19 (A-06), the NTC and TCO themselves, calipers,
drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-H11 (thermoblock) | `00_Spec/inputs/OD-H11_thermoblock.step` (SHA-256 e2d186f2…4038f, INTAKE §1 #1) | — | the Usta, 2026-09-30 (open-dedica `step/`) | CONFIRMED as the input; its numbers are §6 rows |
| Fasteners | M3 heat-set inserts (OD-F01) in OD-C01, M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard) |

**Coordinate frame:** identical to the OD-H11 STEP so the overlay is the identity:
Z is the thermoblock's body axis, z = 0 is its base face, +Z points toward the
outlet face at z = 47.64 (the three locating pins reach z = 50.79), the origin is on
the axis, θ is measured counter-clockwise about +Z from +X. In the machine the axis
is horizontal, +Z points toward the group head, and **−Y points down**: the water
pipes and heater terminals (all at +Y, INTAKE X-51 … X-84) face up (A-07). Every
artifact of this job uses this frame; the foot's underside is the plane y = −70.0.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c04_mount | FDM | machines/creality-k1c.toml (enclosed; build volume UNKNOWN → A-09) | ASA (BOM: ASA / PC) | 1070 | as printed | A-08 |

Environment: inside the machine, next to a thermoblock whose skin exceeds 100 °C
(radiant heat across ≥ 10 mm of air); the mount carries the thermoblock's mass
(≈ 0.45 kg at 159 767 mm³ of aluminium, INTAKE X-104, A-11) and the pull of the
water connections; steam and drips possible.

## §4 Architecture and concepts

- **C1 — rear plate on a foot, two screw standoffs with metal spacers (CHOSEN).**
  One solid. A rear plate 5.0 thick, z −17.0 … −12.0 (its front face 12.0 behind the
  thermoblock's base face, so REQ-01's 10.0 holds with margin), spanning x −50 … +50
  and y −70 … +40 (corners R 5). A foot plate 4.0 thick, y −70.0 … −66.0, from the
  plate's back face z −17.0 to z +33.0, x ±50, with four Ø3.4 through-holes along Y
  at (x ±40.0, z −8.0) and (x ±40.0, z 26.0) for M3 screws into OD-C01 inserts
  (A-10); two gussets 4.0 thick tie the plate to the foot at x ±46. Two standoffs
  rise from the plate's front face along +Z, Ø12.0 with a Ø4.0 through-hole each
  (D-04a for a Ø3.5 screw, A-04), on the axes of the thermoblock's two blind screw
  holes: standoff S1 at (x −19.62, y 20.18) and S2 at (x 25.01, y 9.08) (A-03). Each
  standoff ends 10.0 short of the face its hole opens on, measured along the hole
  axis, and a metal spacer Ø7.0 × 10.0 (A-05) bridges the rest: the plan records the
  open-end face of each hole from the OD-H11 STEP and sets the standoff lengths
  (S1 tip at z = 3.2 − 10.0 = −6.8 if the hole opens on the notch floor at z 3.2;
  S2 tip at z = 27.6 − 10.0 = 17.6 if it opens on the mid-lug underside at z 27.6).
  A standoff longer than 20 gets a gusset to the plate (E-06). Print orientation:
  the plate's back face on the bed, standoffs vertical, the foot standing up
  (A-12). Envelope 100.0 × 110.0 × 50.0 (x ±50, y −70 … +40, z −17 … +33).
- **C2 — groove ribs.** Printed PC ribs sliding into the three R 4.25 vertical
  grooves (INTAKE X-14 … X-16), as the OEM case seems to. Deferred: direct contact
  with the hot casting breaks the ≥ 10 mm rule; only with the Usta's waiver.
- **C3 — OEM steel brackets.** Needs OD-H17 / OD-H19 scanned (A-06).

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 100.0 × 110.0 × 50.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±50.0, y −70.0 … +40.0, z −17.0 … +33.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) mount|OD-H11 at the identity pose: `clearance ≥ 10.0` (REQ-01 governs; the boolean only where OD-H11 is a sound solid, else INCONCLUSIVE and reported); mount|spacer and spacer|OD-H11: designed contacts, `clearance = 0`, `interference ≤ 0` mm³ (the spacers are the designer's modelled solids, A-05). (b) no motion variable | Hard | CAD | house | `clearance`, `interference` | A-01, A-03, A-05 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 plate, 1 foot, 2 gussets, 2 standoffs, 2 Ø4.0 through-bores, 4 Ø3.4 through-bores | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/6.0) rad; `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default; the mount carries the thermoblock) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the K1C build volume, plate down: 100.0 × 110.0 × 50.0 | Hard | part | machine | `envelope` | A-09 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (plate back face down, build direction +Z); nothing supported | Hard | part | floor | `overhang_census(build_dir=(0,0,1))`; reviewer from sections | A-12 |
| D-03b | Unsupported bridge | span ≤ 5 | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | the four frame holes Ø ≥ 3.25 (designed Ø3.4); the two standoff holes Ø ≥ 3.5 + 0.25 = 3.75 (designed Ø4.0) | Hard | part | house | `locate_bore` | A-04 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | the holes are clearance holes, not fit bores: none on this part | Hard | part | floor | — (N/A by this row) | — |
| E-06 | Boss support | each standoff tied into the plate with a root fillet, and gusseted when longer than 20 | Hard | part | struct | reviewer | — |
| REQ-01 | Air gap | `clearance(mount, OD-H11)` ≥ 10.0 at the identity pose, the nearest points reported | Hard | CAD | client (INTAKE X-R05) | `clearance` | A-01 |
| REQ-02 | Standoff bores | two Ø4.0 ± 0.1 through-bores on axes parallel to Z at (x −19.62, y 20.18) and (x 25.01, y 9.08), offset ≤ 0.10, through the plate and the standoff | Hard | CAD | A-03 | `locate_bore` | A-03 |
| REQ-03 | Standoff tips | each standoff's tip face 10.0 ± 0.10 from the face its hole opens on, along the hole axis (spacer length); the spacer solids `clearance = 0` at both ends | Hard | CAD | A-03, A-05 | `envelope` of the tip face; `clearance` | A-03, A-05 |
| REQ-04 | Plate face | the plate's front face at z = −12.00 ± 0.10; its back face at z = −17.00 ± 0.10 | Hard | CAD | A-02 | `envelope`; reviewer from sections | — |
| REQ-05 | Foot plane | the foot's underside at y = −70.00 ± 0.10 (`envelope` min_y), 4.0 ± 0.1 thick | Hard | CAD | A-10 | `envelope`; reviewer from sections | A-10 |
| REQ-06 | Frame holes | four Ø3.4 ± 0.1 through-holes along Y at (x ±40.0, z −8.0) and (x ±40.0, z 26.0), offset ≤ 0.10 | Hard | CAD | A-10 | `locate_bore` | A-10 |
| REQ-07 | Bracket keep-out | no mount material at r ≤ 45.0 from the axis within z 0 … 47.64 except the two standoffs and their gussets (the pads at θ 262.5° and 339.0° take the OEM brackets, A-06) | Hard | CAD | A-06 | reviewer, from sections and `envelope` | A-06 |
| REQ-08 | Heat | the mount holds the thermoblock through a heating cycle without softening; not a geometric gate: INCONCLUSIVE until the first run | Hard | part | client | — (bench) | A-08 |

**Named exceptions** (Usta U-18): none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | Scan scale and OD-H11 fidelity | mm, scanner calibration; the deviation gate's own band is not met (p95 0.474, max 2.71); no calipers | every clearance off by the scan error; the screw holes could sit elsewhere | INTAKE X-120 … X-137 (deviation), §4 | calipers on the thermoblock (INTAKE calipers.md) | OPEN |
| A-02 | Base face and axis | base face z = 0, body axis +Z, top face z 47.64, pins to 50.79; body r 33.78 … 34.97 | the plate's 12.0 standoff is measured from the wrong face | INTAKE X-01, X-02, X-21, X-102, X-103 | calipers | OPEN |
| A-03 | Screw holes | two blind holes: Ø3.5 at (25.01, 9.08) over z 27.0 … 33.2 and Ø3.6 at (−19.62, 20.18) over z 3.0 … 8.0; which face each opens on (toward −Z, the assumption, or toward +Z) the designer measures at D2 and the plan records; they are the OEM chassis's fixing points | the mount screws into nothing: reprint after calipers; a hole opening toward +Z cannot be reached from the plate and the spec is amended | INTAKE X-49, X-34, X-37; README feature tree 5 | calipers and a look at the OEM case | OPEN |
| A-04 | Screw | a Ø3.5 self-tapping screw (the holes are Ø3.5 / 3.6 pilots), length = plate 5.0 + standoff + spacer 10.0 + engagement 5.0; mount holes Ø4.0 (D-04a) | wrong screw; the holes may be M4 tapped | this spec; INTAKE X-49 | the Usta measures the OEM screws | OPEN |
| A-05 | Spacer | a metal spacer Ø7.0 × 10.0, Ø4.0 bore (brass or aluminium), one per standoff; modelled as a solid in the check assembly | the gap is bridged by plastic: heat reaches the standoff | this spec (the ≥ 10 mm rule, INTAKE X-R05) | the Usta names the spacer | OPEN |
| A-06 | Brackets OD-H17 / OD-H19 | steel clips on the pads at θ 262.5° and 339.0° (ear notches and clip holes, INTAKE X-23 … X-26, X-85, X-86) occupying r ≤ 45 around them; the mount keeps r > 45 within z 0 … 47.64 except the standoffs | the mount collides with a bracket | INTAKE §4 gaps 1–3; this spec | scan of OD-H17 and OD-H19 | OPEN |
| A-07 | Orientation in the machine | axis horizontal, +Z toward the group head, −Y down, pipes and terminals up | tube runs or the group-head height are wrong; OD-C05 must agree | this spec (P4); OD-G01's frame (+Z toward the user) | the Usta's layout decision for OD-C01 / OD-C05 | OPEN |
| A-08 | Material | ASA, density 1070 kg/m³, printed on the K1C (recorded material PLA); PC if the Usta prefers | mount softens near the thermoblock | BOM OD-C04 (INTAKE X-R09); typical ASA datasheet | the Usta names the filament | OPEN |
| A-09 | K1C build volume | 220 × 220 × 250 (Creality specification, not in the machine file) | part does not fit (it is 100 × 110 × 50) | memory of the spec sheet | the Usta reads the printer | OPEN |
| A-10 | OD-C01 interface | four M3 inserts on an 80.0 × 34.0 pattern (x ±40.0, z −8.0 and 26.0 in this frame); the foot underside at y = −70.0 is the frame's floor plane, 16.5 below the thermoblock's lowest point (y −53.5) | OD-C01 must be designed to it; the group-head height follows | this spec (design choice; INTAKE §4 gap 5) | OD-C01 design | OPEN |
| A-11 | Mass and load | ≈ 0.45 kg (159 767 mm³ × 2700 kg/m³ aluminium) plus the pull of the tubes and the group-head connection; strength not calculated | mount cracks | INTAKE X-104 | the first run | OPEN |
| A-12 | Print orientation | plate back face on the bed, no supports; the foot stands up; standoffs vertical | none expected | this spec | first print | OPEN |
| A-13 | Grooves | the three R 4.25 grooves are the OEM case's rib seats and are not used (C2 deferred) | a hidden function is lost | INTAKE X-14 … X-16 | the Usta looks at the donor case | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | the ≥ 10 mm air gap is REQ-01 with the project as its source; metal spacers carry the screw seats, so no printed surface touches the casting | Oğuz | §4 C1 |
| 2026-09-30 | REQ-08 (heat) is a part gate answered only by the first run; the review reports it INCONCLUSIVE | Oğuz | §5 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the OD-H11 report |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6; ratified |
