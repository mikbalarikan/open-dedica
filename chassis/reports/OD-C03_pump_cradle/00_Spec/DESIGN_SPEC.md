# DESIGN_SPEC — OD-C03 printed pump cradle (20260930-od-c03-pump-cradle)

Version 1.0 · RATIFIED by the Usta on 2026-09-30 (standing instruction of 2026-09-30: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size S · lane CAD

## §1 Intent

OD-C03 is the 3D-printed pump cradle of the Open Dedica espresso machine. It holds
the OEM ULKA EP5 vibratory pump OD-H01 horizontally inside the printed chassis,
through the OEM rubber pump protector sleeve OD-H02 that damps its vibration (the
thesis's rigid mount vibrated unacceptably; INTAKE X-163, X-164), and bolts to the
printed base frame OD-C01 with M3 screws into heat-set inserts. Done means: one valid
printable solid that cradles the sleeve-clad coil on two saddles, keeps every printed
surface at least 2.0 mm from the pump itself, exposes strap passages for retention and
a screw pattern for OD-C01, with every unconfirmed value in §6. OD-H02 and OD-H03 are
not scanned: their rows are assumptions and the job is reopened when they are measured.

**Deliverables** (tier S): STEP AP242 of the cradle; the check assembly STEP
(cradle + OD-H01 + the assumed sleeve solid as placed); STL; build and check
scripts; REPORT; sections. No drawings or renders (the part goes to the Usta's own
printer).

**Out of scope:** OD-C01 base frame, OD-H03 spring (see A-05), the water tubes on the
pump spigots, calipers, drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-H01 (pump) | `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` (SHA-256 b05302af…3fb62, INTAKE §1 #1) | — | the Usta, 2026-09-30 (open-dedica `step/`) | CONFIRMED as the input; its numbers are §6 rows |
| Fasteners | M3 heat-set inserts (OD-F01) in OD-C01, M3 × 8 screws (OD-F02) | — | open-dedica `docs/bom.csv` (INTAKE X-178, X-179) | CONFIRMED (project standard) |

**Coordinate frame:** identical to the OD-H01 STEP so the overlay is the identity:
Z is the pump axis, +Z points toward the inlet hose fitting (the outlet spigot is at
−Z), X is the normal of the sheet-metal frame's side plate, the origin is on the
pump axis, θ is measured counter-clockwise about +Z from +X. In the machine the pump
axis is horizontal and **+Y points down**: the cradle sits on the +Y side of the
pump and the terminal block (at −Y, INTAKE X-98…X-104) faces up (A-08). Every
artifact of this job uses this frame; the foot's underside is the plane y = +40.0.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c03_cradle | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-10) | PETG (BOM) | 1270 | as printed | A-09 |

Environment: inside the machine base, wet side; the pump vibrates at mains
frequency under 15 bar load and warms in use; the cradle carries the pump's mass
(≈ 0.5 kg, A-12) and the strap tension; no water contact by design.

## §4 Architecture and concepts

- **C1 — two-saddle cradle on a foot plate, strap-retained (CHOSEN).** One solid.
  A foot plate 3.0 thick (y 37.0 … 40.0) spanning x −40 … +40, z −10 … 40, with four
  Ø3.4 through-holes along Y at (x ±34.0, z −4.0) and (x ±34.0, z 34.0) for M3
  screws into OD-C01 inserts (A-11). Two saddle ribs 6.0 thick along Z, rib 1 over
  z 0.0 … 6.0 and rib 2 over z 24.0 … 30.0 (inside the sleeve span A-03 and clear of
  the terminal block, which ends at z −3.3), each an arc of inner radius 26.65 (the
  sleeve OD 53.3 / 2, A-03: a designed contact) and outer radius 32.0, spanning θ
  45° … 135° (centred on +Y, so it stays clear of the frame's side plate corners at
  |x| 24.1 … 27.2, |y| ≤ 16.2, A-06) and joined to the foot by a web below it. On each
  side of each rib a post 4.0 thick along X, inner face at |x| = 29.5 (2.3 clear of
  the frame plate at |x| 27.2), rising from the foot to y = 0.0 (the axis height),
  6.0 wide along Z (the rib's width), with a through-slot along X of clear section
  6.0 (Z) × 2.5 (Y) centred at y = 7.0 whose top is roofed at 45° for a cable tie
  (4.8 wide, A-07) that passes over the sleeve. Print orientation: foot on the bed,
  ribs and posts vertical, the saddle faces up (A-13). Envelope 80.0 × 40.0 × 50.0
  (x, y from 0.0 to 40.0, z).
- **C2 — full-ring clamp with a bolted cap.** Two printed halves around the sleeve.
  Deferred: two parts, and the OEM sleeve's real shape is unknown (A-03).
- **C3 — OEM-faithful sleeve pocket with the spring.** Needs the scanned OD-H02 and a
  measured OD-H03 (A-03, A-05); revisit when they land.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 80.0 × 40.0 × 50.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (y from 0.0 to 40.0, z from −10.0 to 40.0, x ±40.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) cradle|OD-H01 at the identity pose: `clearance ≥ 2.0` (REQ-03 governs; the boolean only where OD-H01 is a sound solid, else INCONCLUSIVE and reported); cradle|sleeve solid (A-03, modelled by the designer): designed contact on the two saddles, `clearance = 0` and `interference ≤ 0` mm³. (b) no motion variable: the cable ties are not modelled | Hard | CAD | house | `clearance`, `interference` | A-01, A-03 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 2 saddle ribs, 4 posts, 4 strap slots, 4 Ø3.4 through-holes, 1 foot plate | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/32.0) rad; `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `mesh_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (the default; the cradle carries the pump) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each envelope size ≤ the Kobra Max 3 build volume, foot down: 80.0 × 50.0 × 40.0 | Hard | part | machine | `envelope` | A-10 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (foot down, +Y is down): the slot roofs at 45°, the saddle faces up; nothing supported | Hard | part | floor | `overhang_census(build_dir=(0,−1,0))`; reviewer from sections | A-13 |
| D-03b | Unsupported bridge | span ≤ 5 | Hard | part | floor | reviewer, from sections | — |
| D-04a | Clearance hole for a fastener | the four frame holes Ø ≥ 3.0 + 0.25 = 3.25 (designed Ø3.4) | Hard | part | house | `locate_bore` | — |
| D-04c | Clearance around a seated component | ≥ 0.5 per side to OD-H01; REQ-03 raises it to 2.0 | Hard | part | house | `clearance` | A-01 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | the four Ø3.4 holes are clearance holes, not fit bores: none on this part | Hard | part | floor | — (N/A by this row) | — |
| REQ-01 | Saddle radius | `radial_profile` inner about the pump axis (origin, +Z, ref +X) over θ 50° … 130° at every 5°, z 0.5 … 5.5 and 24.5 … 29.5: min and max in [26.60, 26.70] | Hard | CAD | A-03 | `radial_profile` | A-03 |
| REQ-02 | Saddle sector and rib faces | at z = 3.0 and z = 27.0 the inner radius reads ≤ 26.70 at θ 50° and 130° and no material reads within r ≤ 32.0 at θ 40° and 140° (`radial_extent` INCONCLUSIVE "no material" is the expected reading, recorded as such); rib faces at z 0.0, 6.0, 24.0, 30.0 ± 0.10 from sections | Hard | CAD | A-06 | `radial_extent`; reviewer from sections | A-06 |
| REQ-03 | Pump clearance | `clearance(cradle, OD-H01)` ≥ 2.0 at the identity pose, the nearest points reported | Hard | CAD | A-01, A-03 | `clearance` | A-01, A-03 |
| REQ-04 | Sleeve contact | `clearance(cradle, sleeve solid) = 0` with the nearest points on the saddle arcs; `interference ≤ 0` mm³ | Hard | CAD | A-03 | `clearance`, `interference` | A-03 |
| REQ-05 | Strap slots | four through-slots along X, one per post, clear section ≥ 6.0 (Z) × 2.5 (Y), centre y 7.0 ± 0.5, roof at 45° (D-03a) | Hard | CAD | A-07 | reviewer, from sections and `envelope` of the slot faces | A-07 |
| REQ-06 | Post clearance | post inner faces at |x| = 29.5 ± 0.1; `clearance` post|OD-H01 ≥ 2.0 (part of REQ-03) | Hard | CAD | A-06 | `envelope`, `clearance` | A-06 |
| REQ-07 | Frame holes | four Ø3.4 ± 0.1 through-holes along Y at (x ±34.0, z −4.0) and (x ±34.0, z 34.0), offset ≤ 0.10 | Hard | CAD | A-11 | `locate_bore` | A-11 |
| REQ-08 | Foot plane | the foot's underside at y = 40.00 ± 0.10 (`envelope` max_y), 3.0 ± 0.1 thick | Hard | CAD | A-11 | `envelope`; reviewer from sections | A-11 |
| REQ-09 | Vibration | the printed cradle transmits no unacceptable vibration to the chassis with the OEM sleeve fitted; not a geometric gate: INCONCLUSIVE until the first run | Hard | part | client | — (bench) | A-03, A-05 |

**Named exceptions** (Usta U-18): none.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | Scan scale and OD-H01 fidelity | mm, scanner calibration; the deviation gate's own band is not met (p95 0.448, max 2.49) and the hidden geometry (sheet 3.1, core tube, bore depths) is estimated | every clearance off by the scan error; the frame plates could sit elsewhere | INTAKE X-143…X-159, X-182…X-185 (§4 Q5) | calipers on the pump (INTAKE X-188) | OPEN |
| A-02 | Coil | Ø47.3 (r 23.65), z −8.8 … 34.5, centre 0.2 off the axis, edge fillet 1.0 | sleeve OD and saddle radius wrong | INTAKE X-49…X-56 (§4 Q2) | caliper coil Ø | OPEN |
| A-03 | Rubber sleeve OD-H02 | a tube on the coil: ID 47.3, wall 3.0, OD 53.3, over z −6.0 … 32.0 between the frame end plates; modelled as a solid for the check assembly; the saddle radius 26.65 is its OD / 2 with no gap (rubber grips) | the saddle does not fit the real sleeve: reprint after calipers | this spec (no input gives it; INTAKE §4 Q6, X-180, X-186) | scan or calipers of OD-H02 | OPEN |
| A-04 | Sheet-metal frame | end plates at z −12.4 and 37.65, x −27.2 … 26.85, y ±16.2, sheet 3.1, one side plate along a long x edge (which side the designer measures at D2 and the plan records) | posts or saddles collide with the frame | INTAKE X-58…X-72 | calipers; the plan's measurement | OPEN |
| A-05 | Suspension spring OD-H03 | not modelled and not needed by C1: retention is the cable ties on the rubber sleeve; the OEM spring's function (axial location, damping) is reproduced when OD-H03 is measured (C3) | axial creep or rattle in service | INTAKE §4 Q7, X-181 | calipers on OD-H03; the first run (REQ-09) | OPEN |
| A-06 | Free sector and post positions | saddles over θ 45° … 135° and posts at |x| ≥ 29.5 keep ≥ 2.0 to the frame plates (corner at |x| 24.1 … 27.2, |y| 16.2 → r 29.05 at 146°) | a collision the check finds: adjust the sector in the plan | derived from A-04 | the plan's measurement | OPEN |
| A-07 | Retention strap | cable tie 4.8 wide × 1.4 thick, two per cradle (one per rib) over the sleeve through the post slots | strap does not pass or does not hold | this spec | the Usta names the strap | OPEN |
| A-08 | Pump orientation in the machine | axis horizontal; +Y (the side opposite the terminal block) down; terminals up for wiring; the outlet (−Z) toward the 3-way valve | wiring or tube runs awkward; OD-C01 layout | this spec (P4) | the Usta's layout decision for OD-C01 | OPEN |
| A-09 | Material | PETG, density 1270 kg/m³, printed on the Kobra Max 3 (recorded material PLA) | wrong mass; PETG softens if the pump runs hot | BOM OD-C03 (INTAKE X-160); typical PETG datasheet | the Usta names the filament | OPEN |
| A-10 | Kobra Max 3 build volume | 420 × 420 × 500 (Anycubic specification, not in the machine file) | part does not fit (it is 80 × 50 × 40) | memory of the spec sheet | the Usta reads the printer | OPEN |
| A-11 | OD-C01 interface | four M3 inserts on a 68.0 × 38.0 pattern (x ±34.0, z −4.0 and 34.0 in this frame); the foot underside at y = 40.0 is the frame's floor plane | OD-C01 must be designed to it | this spec (design choice; INTAKE §4 Q8, Q10) | OD-C01 design | OPEN |
| A-12 | Pump mass and load | ≈ 0.5 kg; the cradle sees its weight, the strap tension and vibration; strength not calculated | cradle cracks in service | ULKA EP5 datasheet memory | the first run | OPEN |
| A-13 | Print orientation | foot on the bed (y = 40 face down), no supports; the slot roofs at 45° | slot roofs sag | this spec | first print | OPEN |
| A-14 | ≥ 10 mm air gap rule | applies to the thermoblock only (SOURCING_GUIDE §3.2), not to the pump | none for geometry | INTAKE X-167 (§4 Q9) | the Usta confirms | OPEN |
| A-15 | Pump variant | the scanned pump is the EP5 (plastic outlet); the EX5 differs only at the outlet spigot, outside the cradle | none for the cradle | INTAKE §4 Q11 | the Usta looks at the pump | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-09-30 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-09-30 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction of 2026-09-30; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-09-30 | INTAKE §4 Q1…Q4 (numeric spreads inside the scan's own band) need no answer for the cradle: the cradle keeps 2.0 to the pump, more than the scan's deviation; carried in A-01 | Oğuz | INTAKE_v01 §4 |
| 2026-09-30 | REQ-09 (vibration) is a part gate answered only by the first run; the review reports it INCONCLUSIVE | Oğuz | §5 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-30 | first draft from the OD-H01 report |
| 1.0 | 2026-09-30 | INTAKE_v01 cross-references in §6, A-14 and A-15 added; ratified |
