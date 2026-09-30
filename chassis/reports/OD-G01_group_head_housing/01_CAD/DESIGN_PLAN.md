# DESIGN_PLAN — od_g01_housing (20260930-od-g01-group-head-housing, concept C1)

Designer: Claude Code, Opus 5 · spec version 1.0 · written before any geometry (D2)

Versions recorded at D0 for the REPORT: Python 3.13.7 · build123d 0.11.1 (pinned,
D-023) · OCP 7.9.3.1 (OCCT 7.9.3) · numpy 2.5.3 · repository commit `3fa319f`.

Input hashes checked against the brief before any other work: all three match.

| Input | SHA-256 | Match |
|---|---|---|
| `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` | 2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906 | yes |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | yes |
| `00_Spec/inputs/OD-G10_portafilter.step` | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 | yes |

**Read §7 before commissioning the J3 package.** Three measurements taken on the
reference solids at D1 say that two hard gate rows cannot be met at the poses the
spec's own ledger gives. The plan below is complete and buildable; §7 states what
the build would measure as a FAIL and why no choice inside the spec's bands changes
it.

## 1. Datum

The frame is the OD-G09 STEP frame verbatim, as spec §2 requires, so that the
overlay of the housing on the OEM cup is the identity and every REQ row can be read
on the same rays:

- **Z is the cup axis**; **+Z points toward the mouth**; the portafilter enters
  along −Z.
- **z = 0 is the plane of the lug top pads.** The lug top pads are at the origin
  because they are the functional datum of the bayonet: the ear engagement depth,
  the stop-block reach, the pocket floors, the shelf, the lip step and the rear
  plate are all dimensioned from that plane in spec §4 C1 and in every REQ row of
  §5, and it is the one plane the OEM cup and the housing must share for the
  portafilter to lock at the same height.
- **The origin is on the axis** (r = 0 at the cup axis), so the three lugs, the
  keyhole and the two G04 bosses are polar features of one centre.
- **θ is measured counter-clockwise about +Z from +X**, and lug 1 spans
  θ = 336° … 30° (centre 3°). +X is therefore fixed by the lug 1 start, not chosen.
- The rear flange is square about the same origin: its sides are parallel to X and
  Y, so the four carrier inserts sit at (±44, ±44).

Confirmed against the input: `envelope(OD-G09)` reads max_z = 3.298 mm, which is
the front face at +3.30 of spec §4, and min_z = −27.835 mm, the scan truncation
below the OEM plate. The housing's own envelope is −23.94 … +3.30.

## 2. Library and tools (D1)

**Cards read (two, by tag):**

- `library/uno10/CARD.md#u4-puck` — tags round, annular-snap, polar profiles,
  known-bad. Taken from it: the datum-derived-from-measured-extents pattern and the
  polar (r, θ, z) profile map, which is what REQ-01 … REQ-05 and REQ-09 ask for.
  Its recorded lesson is the one this target turns on: the U4 check passed 36 of 36
  because it swept angle at a single height, and a press-turn joint must be swept
  over rotation and axial position together. The U-03(b) lock path here is swept
  jointly for that reason (L-09, L-10), not angle-then-axis.
- `library/uno10/CARD.md#u5-tank-heat-set` — tags heat-set, boss, fdm. Taken from
  it: the boss + blind bore + mouth chamfer arrangement for an M3 heat-set insert
  (D-05a, D-05b, J-05, E-06), and its lesson to keep "how big" and "where" separate
  in envelope arithmetic, which is how U-02 is reported here (size and position in
  separate rows, L-12).

Nothing in the index covers a bayonet cup or a reverse-engineered mating interface;
that is a finding, not a gap to fill with a new library card.

**`tools/` functions reused** (nothing else; no job code goes into the repository):

| Function | What it does here |
|---|---|
| `tools.core.read_step` | re-import the exported STEP and read the three reference solids |
| `tools.core.validity` | `solid_count`, `brep_valid`, `naked_edges` for U-01 and as the gate before every measurement |
| `tools.core.write_step` | the AP242 delivery writer (D-024); `export_step()` is not used |
| `tools.core.step_roundtrip` | U-04: labels, solids, volume delta, valid after re-import |
| `tools.core.write_stl`, `tools.core.mesh_sagitta` | U-07: the STL at tolerance 0.01 mm and angular tolerance 0.0861677 rad, then the sagitta actually achieved |
| `tools.core.common_volume` (through `tools.measure.interference`) | U-03(a) and the U-03(b) sweep |
| `tools.core.fillet_ladder` | every fillet, largest radius first, recording the radius achieved and why each larger rung failed |
| `tools.measure.envelope` | U-02, D-02, `envelope_within_spec` |
| `tools.measure.feature_census`, `bore_census`, `locate_bore` | U-05, REQ-06, REQ-07, REQ-08, REQ-11, D-05b |
| `tools.measure.min_wall` | D-01a, D-01b, D-06a, J-05 (global floor), U-06 through `detail["wide"]` |
| `tools.measure.radial_extent` | REQ-03, REQ-04, REQ-05, and the material around each insert axis for J-05 and D-05a |
| `tools.measure.radial_profile` | REQ-01, REQ-02, REQ-09 |
| `tools.measure.interference`, `tools.measure.clearance` | U-03, REQ-10 |
| `tools.result.gate` | the only comparison; band from GATES §0 (0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts) |
| `tools.drawing.write_sections`, `nothing_clipped` | D6 screening sections |

**New code needed (job-local, in `01_CAD/`):** `build_od_g01_housing.py`,
`check_od_g01_housing.py`, `assemble_od_g01_check.py` (places OD-G04 and OD-G10 by
the joints of §5 and exports the check assembly STEP), and `sweep_od_g01_v01.py`
(D7, writing into `01_CAD/sweep_v01/`).

**Missing `tools/measure` functions**, to be named again in REPORT §7:

- **No boss-OD measurement** for D-05a. GATES §D records the row as "OD: no tool
  yet (reviewer)". This plan measures the material around each insert axis with
  `radial_extent(side="outer", r_min=2.0)` on 24 rays and reports it as a local
  diagnostic; the gate row stays the reviewer's to answer.
- **No local wall measurement** for J-05. `min_wall` is whole-part, and the
  thinnest wall of this part is the lug ramp end (1.15 nominal), not the material
  around an insert. The same `radial_extent` ring is reported for each insert, with
  `min_wall` beside it; the J-05 row is answered from the ring, which is a located
  measurement of the B-rep, and the REPORT says so.
- **No overhang measurement** for D-03a and no bridge measurement for D-03b. GATES
  records both as "no tool yet (reviewer, from sections)". Sections are provided at
  D6; the rows are the reviewer's.
- **No sweep driver** for U-03(b). GATES records the motion sweep as the reviewer's
  own script. `sweep_od_g01_v01.py` runs the designer's own sweep over the lock
  path; the row is still re-measured by the reviewer.

## 3. Feature order

Build in build123d **Algebra mode**, one parameter structure at the top, named
intermediates, no index-based selectors: every face and edge is chosen by type,
by measured position, or by a polar predicate on its centre.

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Cup outer wall, outer Ø86.2, z −19.94 … +3.30 | `extrude` of a circle R `WALL_R_OUT` | — | §4 C1, REQ-09 |
| F02 | Rear slab: square 100 × 100, corners R 8, z −23.94 … −19.94 (the rear plate and the mounting flange are one 4.00 slab in one plane) | `extrude` of a rounded-corner rectangle sketch | — | §4 C1, U-02, REQ-11, A-18 |
| F03 | Blank | `+` union of F01 and F02 | F01, F02 | — |
| F04 | Main bore Ø74.20 straight, no draft, z −14.10 … +3.30; this also makes the flat front face at +3.30 (no rim notches, A-23) | `-` of a cylinder R `BORE_R` | F03 | §4 C1, REQ-02, REQ-09 |
| F05 | Upper lip wall R 30.82, z −17.70 … −14.10; this leaves the shelf annulus at z = −14.10 between R 30.82 and the bore | `-` of a cylinder R `LIP_UPPER_R` | F04 | §4 C1, A-07, A-09 |
| F06 | Lower lip wall R 31.33, z −19.94 … −17.70; this leaves the 0.51 down-facing step at z = −17.70 | `-` of a cylinder R `LIP_LOWER_R` | F05 | §4 C1, A-09 |
| F07 | Three under-lug pockets, floor z −16.80, between R 34.39 and the bore, over start − 5° … start + 58.5°, for starts 336°, 96°, 216° | `-` of three angular sector solids (`extrude` of a sector face) | F06 | §4 C1, A-08, U-05 |
| F08 | Three lug blanks, R 31.68 … bore, θ start … start + 54°, top face z = 0, down to z −12.0 | `+` of three sector solids | F07 | §4 C1, REQ-01, REQ-03, U-05 |
| F09 | Lug underside and stop block, cut in one operation per lug: a `loft` through radial sections at start, start + 5.76°, start + 7°, start + 41.8° and start + 54°, each section the r–z rectangle R 31.68 … bore from that section's underside level down to z −12.0. Section levels: −10.52 (stop block, start … start + 5.76°), then a vertical stop face up to −6.57 at start + 7°, the shallow ruled surface to −5.59 at start + 41.8°, then the ramp to −1.15 at start + 54° | `-` of the loft | F08 | §4 C1, A-05, A-06, REQ-04, REQ-05, U-05 |
| F10 | Keyhole central bore Ø26.0 through the slab, on the axis, z −23.94 … −19.94 | `-` of a cylinder R `KEYHOLE_R` | F09 | REQ-06, REQ-11, U-05 |
| F11 | Two keyhole lobes through the slab: lobe A on θ 133°, width 7.2, out to reach 23.5; lobe B on θ 310°, width 10.5, out to reach 20.5; each a slot of the stated width with a semicircular outer end at the reach radius, running from inside the central bore | `-` of two slot solids | F10 | §4 C1, A-11 |
| F12 | Two OD-G04 insert bosses, OD 8.0, at r 19.03, θ 118.0° and 302.7°, rising from the slab top face z −19.94 to z −18.24 (height 1.70) | `+` of two cylinders | F11 | REQ-07, D-05a, E-06 |
| F13 | Two OD-G04 insert bores Ø4.0, from the boss top face z −18.24 down to the slab rear face z −23.94 (length 5.70), with a 0.5 × 45° mouth chamfer at the boss top (the insert enters from the cup side and the screw comes down through OD-G04) | `-` of two cylinders and two cones | F12 | REQ-07, D-05b, J-05, U-05 |
| F14 | Four carrier insert bosses, OD 8.0, at (±44, ±44), rising from the slab top face z −19.94 to z −18.24 (height 1.70) | `+` of four cylinders | F13 | D-05a, D-05b, E-06, A-18 |
| F15 | Four carrier insert bores Ø4.0, from the slab rear face z −23.94 up to z −18.24 (length 5.70, blind, opening on the rear face because OD-C05 mounts on the rear), with a 0.5 × 45° mouth chamfer at the rear face | `-` of four cylinders and four cones | F14 | REQ-08, D-05b, J-05, U-05 |
| F16 | Fillet pass 1: the six boss roots, through a descending ladder [1.0, 0.8, 0.6, 0.4] mm, edges selected as the concave circles of radius 4.0 lying in the plane z = −19.94 | `fillet_ladder` | F15 | E-06, D-03a, U-06 |
| F17 | Fillet pass 2: the shelf-to-bore and shelf-to-lip concave edges, ladder [0.8, 0.6, 0.4] mm, capped at 0.8 so the round stays below z = −13.0 and outside the REQ-02 window | `fillet_ladder` | F16 | D-03a, U-06, REQ-02 |
| F18 | Fillet pass 3: the three lug root edges where the lug meets the bore wall (the two tangential side faces of each lug), ladder [0.8, 0.6, 0.4] mm; no round on the lug inner face top edge at z = 0 and none on the lug inner face itself, so the REQ-01 window z −5.0 … −1.0 reads the plain cylinder | `fillet_ladder` | F17 | D-06a, U-06, REQ-01 |
| F19 | Name the body `od_g01_housing` for the AP242 export | `Part.label` | F18 | U-04 |

Not modelled, each with its reason: the lug top channel, the six rim notches and
the Ø6 side hole at θ 269° (A-23 names all three as non-functional and spec §4 C1
omits them); the OEM bore recess R 37.379 behind the lugs and the lug-sector groove
at z −15.571 (spec §4 C1 states the bore as straight Ø74.20 to the shelf and states
no recess; both are OEM moulding relief and both would cut into the REQ-02 band);
the per-gap shelf spread (−14.10 / −13.44 / −14.23) and the 0.19 mm lug-ring
eccentricity (A-02, A-07 give the symmetrised values and spec §4 C1 states one
level and one radius).

## 4. Parameters

Lengths mm, angles degrees. One `Params` dataclass at the top of the build script;
no number below it.

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| `WALL_R_OUT` | 43.10 | mm | ±0.05 | §4 C1 "outer Ø86.2"; REQ-09 needs ≥ 43.05 | no |
| `FRONT_Z` | +3.30 | mm | ±0.05 | §4 C1 "flat front face at z = +3.30" | no |
| `BORE_R` | 37.10 | mm | REQ-02 [37.05, 37.15] | §4 C1 "bore Ø74.20 straight"; A-03 | **yes** |
| `LUG_INNER_R` | 31.68 | mm | REQ-01 [31.58, 31.78] | A-02 | **yes** |
| `LUG_STARTS` | 336, 96, 216 | deg | ±0.25 | A-04; §2 fixes lug 1 at 336° | **yes** |
| `LUG_SPAN` | 54.0 | deg | ±0.25 | A-04 | **yes** |
| `LUG_TOP_Z` | 0.0 | mm | datum | §2 (the datum plane) | no |
| `UNDER_Z_AT_7` | −6.57 | mm | REQ-04 ±0.3 | A-05 | **yes** |
| `UNDER_OFF_1` | 7.0 | deg | ±0.5 | A-05 | **yes** |
| `RAMP_START_OFF` | 41.8 | deg | ±1.0 | A-05 | **yes** |
| `UNDER_Z_AT_RAMP` | −5.59 | mm | REQ-04 ±0.3 | A-05 | **yes** |
| `RAMP_Z_AT_54` | −1.15 | mm | REQ-04 ±0.3 | A-05; also the thinnest section of the part, D-01b's stated reason | **yes** |
| `STOP_END_OFF` | 5.76 | deg | ±0.5 | A-06 | **yes** |
| `STOP_BOTTOM_Z` | −10.52 | mm | REQ-05 ±0.3 | A-06 | **yes** |
| `SHELF_Z` | −14.10 | mm | ±0.1 | §4 C1, A-07 | **yes** |
| `POCKET_FLOOR_Z` | −16.80 | mm | ±0.1 | §4 C1, A-08 | **yes** |
| `POCKET_RISER_R` | 34.39 | mm | ±0.15 | §4 C1, A-08 | **yes** |
| `POCKET_START_OFF` | −5.0 | deg | ±0.5 | A-08 | **yes** |
| `POCKET_END_OFF` | 58.5 | deg | ±0.5 | A-08 | **yes** |
| `LIP_UPPER_R` | 30.82 | mm | ±0.08 | §4 C1, A-09 | no |
| `LIP_LOWER_R` | 31.33 | mm | ±0.05 | §4 C1, A-09 | no |
| `LIP_STEP_Z` | −17.70 | mm | ±0.15 | §4 C1, A-09 | no |
| `FLOOR_Z` | −19.94 | mm | ±0.05 | §4 C1, A-09, A-10 | no |
| `PLATE_T` | 4.00 | mm | REQ-11 ±0.1 | §4 C1 "the rear plate 4.00 thick"; A-10 | **yes** |
| `PLATE_BACK_Z` | −23.94 | mm | ±0.05 | derivation: `FLOOR_Z − PLATE_T`, and the envelope floor of U-02 | no |
| `KEYHOLE_R` | 13.00 | mm | REQ-06 ±0.05 on the diameter | §4 C1 "central Ø26.0"; A-10, A-11 | **yes** |
| `LOBE_A` | θ 133.0, reach 23.5, width 7.2 | deg, mm | A-11 ±10° / ±3 mm | A-11 | no |
| `LOBE_B` | θ 310.0, reach 20.5, width 10.5 | deg, mm | A-11 ±10° / ±3 mm | A-11 | no |
| `G04_BOSS_PCR` | 19.03 | mm | REQ-07 offset ≤ 0.10 | A-12 (PCD 38.06) | **yes** |
| `G04_BOSS_THETA` | 118.0, 302.7 | deg | REQ-07 offset ≤ 0.10 | A-12 | **yes** |
| `CARRIER_XY` | 44.0 | mm | REQ-08 offset ≤ 0.10 | §4 C1, A-18 | **yes** |
| `FLANGE_SIDE` | 100.0 | mm | U-02 ±0.1 | §4 C1, A-18 | no |
| `FLANGE_CORNER_R` | 8.0 | mm | ±0.1 | §4 C1 "corners R 8" | no |
| `INSERT_HOLE_D` | 4.00 | mm | D-05b ±0.05 | A-17 | **yes** |
| `INSERT_DEPTH` | 5.70 | mm | D-05b ≥ 5.7 | A-17 (insert length 5.7) | **yes** |
| `BOSS_OD` | 8.00 | mm | ≥ 8.0 | derivation: D-05a's `2 × insert Ø` at `INSERT_HOLE_D` = 4.0 | no |
| `BOSS_RISE` | 1.70 | mm | +0.3 / −0.0 | derivation: `INSERT_DEPTH − PLATE_T` = 5.70 − 4.00, the least rise above the slab that lets a 5.70 bore fit; the bosses rise on the +Z side so `size_z` stays 27.24 for U-02 | **yes** |
| `CHAMFER` | 0.5 × 45° | mm | — | derivation: U5 card's insert-mouth chamfer, sized under `BOSS_RISE` so it does not break through the boss root | no |
| `FILLET_LADDER` | [1.0, 0.8, 0.6, 0.4] roots; [0.8, 0.6, 0.4] shelf and lug roots | mm | — | derivation: capped at 0.8 where a round would enter the REQ-01 (z −5.0 … −1.0) or REQ-02 (z −13.0 … +2.0) windows; radius achieved recorded per pass | no |
| `STL_TOL` | 0.01 | mm | — | U-07 | no |
| `STL_ANG_TOL` | 0.0861677 | rad | ≤ 4·acos(1 − 0.01/43.1) | U-07, evaluated at R_max = `WALL_R_OUT` = 43.1 | no |
| `DENSITY` | 1070 | kg/m³ | — | A-15 (ASA); mass reported, not gated | no |

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-G09 group head bayonet cup (reference only, never in the delivered assembly) | `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` (2f11c1b7…a831906) | identity: spec §2 makes the housing frame the OD-G09 frame | `RigidJoint` at the origin, identity | nothing; used only for the overlay comparison of REPORT §5 |
| OD-G04 brewing gasket support | `00_Spec/inputs/OD-G04_brewing_gasket_support.step` (19b4a140…098d6ad2) | its own datum measured from its own faces: plate back face (its z = 0, outward normal +Z, material in −Z) and tab 1 centre at −3.3° taken from the tangential end faces of the three tabs | `RigidJoint`: no rotation about X or Y (its +Z is parallel to the housing +Z, proved by its hub tube reaching housing z −23.01, the value A-24 states), **+4.74° about Z** and **translate z −7.28** | housing pocket floors (tab bottoms, the designed contact of U-03(a)) and the two F12 bosses |
| OD-G10 portafilter, locked pose | `00_Spec/inputs/OD-G10_portafilter.step` (3a525af1…ea187b257) | its own datum measured from its own faces: cup rim end face (its z = 0) and ear 1 centre at 59.5° from the handle end-cap flat | `RigidJoint`: **180° about +X** (its +Z, which points out of its cup opening, onto the housing −Z, so the rim leads into the bore), then **+60.26° about Z**, then **translate z −11.20** | ear top faces on the three lug undersides (the designed contact of U-03(a)) |
| OD-G10 portafilter, insertion pose | same | same | `RigidJoint`: **180° about +X**, then **+122.5° about Z** (ears centred in the three gaps, gap 1 centre 63°), then **translate z −11.69** | nothing; the REQ-10 pose |

**Derivations of the two OD-G10 numbers**, both checked against the reference cup
before being written here:

- **Clock +60.26°.** Under the 180°-about-X flip an angle negates, so
  θ_housing = clock − θ_G10. A-14 puts the ear leading edge 0.5° short of the stop,
  and A-06 puts the stop at start … start + 5.76°, so ear 1's leading (low-θ) edge
  lands at 336 + 5.76 + 0.5 = 342.26° and its centre, for a 37° ear, at 0.76°.
  clock = 0.76 + 59.5 = 60.26. The other two ears then fall at 240.26° and 119.76°,
  which are the centres of lug 3's and lug 2's engagement spans; the locking
  rotation is therefore toward decreasing θ, from the gap into the lug.
- **Locked z −11.20.** A-14 puts the ear top face on the shallow underside.
  Measured on the reference cup at this clock: first contact at rim z = −11.69, no
  overlap; 1.46 mm³ of overlap at rim z = −11.20, in three regions spanning
  z −6.47 … −6.08, which are the three ear tops on the three lug undersides. The
  locked pose is taken at the contact, and the U-03(a) designed-contact pairs are
  gated by `clearance = 0`, not by the boolean.
- **Insertion pose.** "Ears in the gaps, rim above the shelf" (REQ-10). Ear centres
  on the gap centres give clock 122.5°; the rim is taken at z −11.69, the shallowest
  height at which the ear top (rim + 5.10, A-14) clears the lug underside at −6.57
  and the bayonet can be rotated. Both the pose and its clearance are in §7.

No bounding-box centre and no assumed rotation is used anywhere (L-02): each frame
comes from a face or an angular feature of the part itself.

## 6. Checks planned (D3)

`01_CAD/check_od_g01_housing.py` is written before the build script. Every
predicate re-imports `02_STEP_STL/od_g01_housing_c1_v01.step`, gates
`tools.core.validity` first, measures with `tools/measure`, and compares through
`tools.result.gate` with the band GATES §0 states for the result's unit (0.005 mm,
0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts). Every predicate returns gate,
measured, unit, required, signed margin, location and PASS / FAIL / INCONCLUSIVE;
an exception or a missing value is INCONCLUSIVE and never a PASS.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| U-01 | one valid closed solid: `solid_count == 1`, `brep_valid == 1`, `naked_edges == 0` | `tools.core.validity` | 0 (counts, 1/0 facts) |
| U-02 | `size_x`, `size_y` in [99.9, 100.1]; `size_z` in [27.14, 27.34]; `min_x/y/z` and `max_x/y/z` reported in separate rows against the datum, never folded into the size rows (L-12, U5 card) | `envelope` | 0.005 mm |
| U-03(a) | with OD-G04 at its §5 joint and OD-G10 at the locked pose: `interference ≤ 0` mm³ for `housing\|OD-G04` and `housing\|OD-G10`; the designed contacts (three ear tops on the three lug undersides; the three OD-G04 tab bottoms in the pockets) gated as `clearance == 0` and excluded from the boolean | `interference`, `clearance` | 0.001 mm³ / 0.005 mm |
| U-03(b) | lock path swept jointly, not one variable at a time (L-09, L-10, U4 card's recorded failure): 21 insertion steps from first contact (rim z −5.0) to the locked depth and 25 rotation steps from the gap centre to the stop, as one joint path of 45 poses plus the two end poses; `interference ≤ 0` mm³ at every pose; no fastener moves | `interference` over the path (designer's own sweep script; the row is still the reviewer's own script) | 0.001 mm³ |
| U-04 | named body re-read unchanged: `step_roundtrip_labels`, `step_roundtrip_solids`, `step_roundtrip_valid`, `volume_delta` | `tools.core.step_roundtrip` | 0 / 0.001 mm³ |
| U-05 | feature census against §3: 3 lugs, 3 stop blocks, 3 pockets, 1 Ø26 through-bore, 2 OD-G04 insert bores, 4 carrier insert bores; the lugs counted as 3 concave-cylinder groups at R 31.68 over θ start … start + 54°, the stop blocks as 3 material stretches reaching z −10.52 at start + 2.9°, the pockets as 3 floors at z −16.80; plus `feature_census` faces per surface kind and concave/convex cylinders, compared row by row with the expected list below | `feature_census`, `bore_census`, `locate_bore`, `radial_extent` | 0 (exact counts) |
| U-06 (Soft) | `min_wall` `detail["wide"]` (45°) ≥ 1.0, wrapped as a Result and published beside the 25° value, never instead of it; a missing key is INCONCLUSIVE | `min_wall` | 0.005 mm |
| U-07 | STL written at tolerance 0.01 mm and angular tolerance 0.0861677 rad with the cached triangulation cleared; `stl_max_sagitta ≤ 0.01`; triangle count, both tolerances and the sagitta recorded | `tools.core.write_stl`, `mesh_sagitta` | 0.005 mm |
| U-08 | N/A by its row: the target has no thread. Answered by showing the census holds no helical or thread-named face and that every insert bore is a plain cylinder | `feature_census`, `bore_census` | — |
| D-01a | `min_wall ≥ 0.8` at 0.4 nozzle, `opposition_deg=25` | `min_wall` | 0.005 mm |
| D-01b | `min_wall ≥ 1.0` (the spec's stated value, below the 2.0 default, because the OEM lug ramp ends 1.15 thick) | `min_wall` (same measurement, second gate) | 0.005 mm |
| D-02 | each `envelope` size ≤ the K1C build volume 220 × 220 × 250 in the mouth-up orientation; PASS_ASSUMED A-16 | `envelope` | 0.005 mm |
| D-03a | reviewer, from sections. Sections supplied through each lug at start + 20°, through a stop block at start + 2.9°, through the lip step at z −17.70, and through one OD-G04 boss and one carrier boss; the down-facing faces they show are listed in REPORT §6 with their angle from horizontal and whether A-22 supports them | — (no tool yet) | — |
| D-03b | reviewer, from sections. The longest unsupported horizontal span is listed from the same sections: the 0.51 lip step at z −17.70 and the 2.00 boss overhang ring at the boss roots | — (no tool yet) | — |
| D-05a | the six insert bores read Ø4.0 by `bore_census`; material around each insert axis measured on 24 rays with `radial_extent(side="outer", r_min=2.0)`, reported as the boss OD achieved; the OD row itself is the reviewer's by GATES | `bore_census`, `radial_extent`, `min_wall` | 0.005 mm |
| D-05b | each insert bore: `bore_diameter` in [3.95, 4.05], `bore_length ≥ 5.7` | `locate_bore` on the six expected axes | 0.005 mm |
| D-06a | `min_wall ≥ 1.0` (same measurement, third gate) | `min_wall` | 0.005 mm |
| D-07 | N/A by its row: no reamed fit bore. Answered by showing the six insert bores are insert-formed and by measuring the radial clearance from the Ø26 opening to the OD-G04 hub tube as placed | `locate_bore`, `clearance` | — |
| J-05 | around each of the six insert axes, material out to ≥ 5.0 mm from the axis (2.0 hole radius + 3.0 wall) on 24 rays at three heights, with `min_wall` reported beside it | `radial_extent`, `min_wall` | 0.005 mm |
| E-06 | reviewer. Sections through one OD-G04 boss and one carrier boss show the root fillet tying each boss into the slab, and the fillet radius achieved at F16 is reported | — (no tool yet) | — |
| REQ-01 | `radial_profile(side="inner")` over start + 8° … start + 40° at 1° for all three starts, band (−5.0, −1.0), `margin=(0.0, 0.0)`, `z_step=0.1`, `r_min=25.0`, `r_max=40.0`: `min` and `max` both in [31.58, 31.78] | `radial_profile` | 0.005 mm |
| REQ-02 | `radial_profile(side="inner")` over start + 60° … start + 114° at 1° for all three starts, band (−13.0, +2.0), `margin=(0.0, 0.0)`, `z_step=0.1`, `r_min=25.0`, `r_max=40.0`: `min` and `max` both in [37.05, 37.15] | `radial_profile` | 0.005 mm |
| REQ-03 | `radial_extent(side="inner", r_min=25.0, r_max=40.0)` at z = −3.0: ≤ 31.78 at start + 1°, + 27°, + 53°; ≥ 37.05 at start − 1° and start + 55°; 15 rays over the three starts, each its own gate row | `radial_extent` | 0.005 mm |
| REQ-04 | `radial_extent(side="inner", r_min=25.0, r_max=40.0)`: at start + 20°, ≤ 31.78 at z −5.9 and ≥ 34.0 at z −7.0; at start + 50°, ≤ 31.78 at z −2.3 and ≥ 34.0 at z −3.2; 12 rays over the three starts | `radial_extent` | 0.005 mm |
| REQ-05 | `radial_extent(side="inner", r_min=25.0, r_max=40.0)` at start + 2.9°: ≤ 31.78 at z −9.0 and ≥ 34.0 at z −11.0; 6 rays over the three starts | `radial_extent` | 0.005 mm |
| REQ-06 | `locate_bore(census, (0, 0, −21.94), (0, 0, 1))`: `bore_diameter` in [25.9, 26.1], `bore_axis_offset ≤ 0.05`, `bore_through == 1` | `bore_census`, `locate_bore` | 0.005 mm / 0 |
| REQ-07 | `locate_bore` at (19.03 cos 118.0°, 19.03 sin 118.0°, −21.09) and at (19.03 cos 302.7°, 19.03 sin 302.7°, −21.09), direction (0, 0, 1): `bore_axis_offset ≤ 0.10` and `bore_diameter` in [3.95, 4.05] each; and the angle between the two axes re-measured as 175.3° | `bore_census`, `locate_bore` | 0.005 mm / 0.001 deg |
| REQ-08 | `locate_bore` at (±44, ±44, −21.09), direction (0, 0, 1): `bore_axis_offset ≤ 0.10` on each of the four | `bore_census`, `locate_bore` | 0.005 mm |
| REQ-09 | `radial_profile(side="outer")` at every 5° (72 angles), band (−19.0, +3.0), `margin=(0.0, 0.0)`, `r_min=38.0`, `r_max=55.0`: `min ≥ 43.05`; and the REQ-02 inner profile's `max ≤ 37.15`; the wall reported as the difference, ≥ 5.9 | `radial_profile` | 0.005 mm |
| REQ-10 | `clearance(housing, OD-G10 at the insertion pose of §5) ≥ 0.8`, with the nearest points on both solids reported | `clearance` | 0.005 mm |
| REQ-11 | `locate_bore` on the Ø26 axis: `bore_length` in [3.9, 4.1] | `locate_bore` | 0.005 mm |
| REQ-12 | not a geometric gate: INCONCLUSIVE until the OD-T01 bench test, stated as such in the REPORT and carried into the delivery | — (bench test) | — |
| `exactly_one_solid` | `solid_count == 1` on the re-imported STEP and on every sweep run | `tools.core.validity` | 0 |
| `feature_census` | the U-05 row above: faces per surface kind, concave and convex cylinders and bores, each against the expected list | `feature_census` | 0 |
| `envelope_within_spec` | the U-02 row above, size and position in separate rows | `envelope` | 0.005 mm |

**Expected census** (the list U-05 is gated against; a build that lands elsewhere is
a deviation reported in REPORT §9, not a re-written plan):

| Item | Expected | Exact? |
|---|---|---|
| Lugs (concave cylinder groups at R 31.68, θ span 54°) | 3 | exact |
| Stop blocks (material at start + 2.9° reaching z −10.52) | 3 | exact |
| Under-lug pockets (floors at z −16.80 between R 34.39 and the bore) | 3 | exact |
| Ø26 through-bore on the axis | 1 | exact |
| Ø4.0 OD-G04 insert bores | 2 | exact |
| Ø4.0 carrier insert bores | 4 | exact |
| Bores in total (`bore_census`) | 7 (Ø26 + 6 × Ø4.0), plus the concave cylinders of the bore, lip and pocket risers as the census groups them | count gated, grouping reported |
| Convex cylinders | 6 boss ODs + the outer wall + the 4 flange corner arcs + the 2 lobe end arcs | reported and compared |
| Planar faces | recorded at D5 against this feature list; every plane traced to one F## row of §3 | traced, not a fixed number |

## 7. Risks

**R1 — U-03(a) cannot be met at the pose the ledger gives (measured, blocking).**
With OD-G04 placed by the §5 joint (clock +4.74° from A-12, seat z −7.28 from
A-13) the **OEM cup OD-G09 and the OEM support OD-G04 overlap by 1059.25 mm³** in
nine regions:

- two of **74.84 mm³** each where OD-G04's boss pair A (r 13.00 … 17.50) drives
  through the full OEM plate thickness, z −22.437 … −19.937, at θ ≈ 177.7° and
  357.7°. The keyhole of A-11 puts its two lobes at θ 133° and 310°, so there is no
  opening at those angles;
- six rib feet of 2.07 … 3.97 mm³ each, z −20.400 … −19.937, at θ 27.6°, 87.6°,
  147.8°, 207.6°, 267.6° and 328.0°: OD-G04's six radial ribs 0.463 mm into the
  floor;
- one region of 889.70 mm³ spanning r 15.57 … 34.39, z −22.16 … −15.04, which
  merges the flange bottom, boss pair B and the tab region.

The housing of this plan reproduces that interior by REQ-01 … REQ-09 and carries a
**4.00 mm slab where the OEM has 2.50 mm**, plus two bosses at r 19.03, θ 118.0°
and 302.7° rising to z −18.24, which is exactly where OD-G04's boss pair B bottoms
sit (z −22.16 at this seat). The overlap on the housing is therefore at least the
1059.25 mm³ measured on the OEM. No value inside REQ-01 … REQ-11's bands changes
this, because none of them moves the slab, the boss pair A angles or the keyhole.
Two further measurements bound the problem:

- the overlap falls to **0.80 mm³ only at seat z ≈ −3.70**, 3.58 mm above A-13; at
  that seat OD-G04's hub tube bottom is at housing z −19.43, above the slab top
  face at −19.94, so the hub does not pass through the rear plate and spec §1(c)
  and A-24 are contradicted;
- at **clock −39.95°** (44.7° from A-12) boss pair A passes cleanly through the two
  A-11 lobes and the overlap at the A-13 seat drops to **23.81 mm³**, the rib and
  flange 0.463 mm dig alone. That clock puts OD-G04's tabs outside the pockets that
  A-08 assumes, which is the question INTAKE §4 Q8 left open.

So A-12 (clocking), A-13 (axial seat) and A-11 (keyhole outline) cannot all three
be right. Picking one is a fact about the OEM assembly, not a design choice, so it
is not made here.

**R2 — REQ-10 cannot be met at any pose from which the bayonet can rotate
(measured, blocking).** The governing gap is not the ear in the gap (1.14 mm at the
bore) but the portafilter's drafted outer wall against the lug inner faces: the
nearest point on the cup is r 31.68, θ 96.0°, z 0.000, the lug 2 start corner, and
the portafilter wall grows 0.0449 mm per mm of descent. Measured on OD-G09 with
OD-G10 at the insertion clock:

| Rim height z | Ear top (rim + 5.10) | `clearance` |
|---|---|---|
| −5.00 | +0.10 | 0.826 |
| −6.55 | −1.45 | 0.750 |
| −8.00 | −2.90 | 0.678 |
| −10.00 | −4.90 | 0.580 |
| −11.20 (locked) | −6.10 | 0.521 |
| −11.69 (shallowest rotatable) | −6.59 | **0.497** |
| −13.00 | −7.90 | 0.433 |

The ear top must reach z −6.57 (A-05's shallow underside) before the portafilter
can be turned, so the shallowest rotatable rim height is −11.69 and the clearance
there is 0.497 mm against REQ-10's 0.8. The threshold is met only at rim
z ≈ −5.5 and above, where the ear top is about 6.7 mm clear of the lug underside
and no rotation is possible. REQ-01 caps the lug inner radius at 31.78, which buys
0.10 mm and still leaves 0.60. The lug inner radius, the ear geometry and the
portafilter draft are all fixed by A-02, A-19 and the OD-G10 input.

**R3 — D-05b needs a boss that spec §4 C1 does not name (resolved by design).**
The rear flange is 4.00 thick and D-05b wants an insert hole ≥ 5.70 deep, so F14
raises a 1.70 boss of OD 8.0 around each carrier insert, on the +Z side, where it
does not change `size_z` and so does not disturb U-02. The same applies to the two
OD-G04 bosses (F12). If the reviewer reads §4 C1's "inserts sit in the flange body"
as forbidding the boss, D-05b cannot be met at a 4.00 flange and the trade-off is a
thicker flange, which changes the U-02 envelope.

**R4 — J-05 at the flange corners has 0.17 mm of margin.** From (44, 44) to the R 8
corner arc, centred at (42, 42), the material runs 8 − √8 = 5.172 mm, so the wall
around a Ø4.0 hole is 3.172 against J-05's 3.0. Any growth of `INSERT_HOLE_D` or
any inward move of the corner radius fails the row; both are swept at D7.

**R5 — fillets sit next to two gated windows.** A round at the shelf-to-bore edge
(z −14.10) reaches up into REQ-02's window at any radius above 1.1, and a round on
the lug inner top edge reaches down into REQ-01's window at any radius above 1.0.
F17 and F18 therefore cap their ladders at 0.8 and F18 leaves the lug inner face
unrounded. If the ladder drops to 0.4 and the part still shows a sharp concave edge
at the lug root, the REPORT records the radius achieved rather than widening the
cap.

**R6 — D-01b has 0.15 mm of margin.** The thinnest section of the part is the lug
ramp end at 1.15 (A-05), against D-01b's 1.0 and D-06a's 1.0. `RAMP_Z_AT_54` is
swept at ±0.3 at D7, and its low end (−1.45, a 1.45 thick end) is safe while its
high end (−0.85) fails both rows; the sweep will report that.

**R7 — the reference cup is not a valid solid by the workshop's own check.**
`validity(OD-G09)` reads `solid_count = 1`, `naked_edges = 0`, `brep_valid = 0`.
Nothing is gated on OD-G09, and the housing is built from parameters rather than
from the scan solid, but the overlay comparison of REPORT §5 is a diagnostic and is
reported as one. `interference` against OD-G09 would be INCONCLUSIVE for the same
reason, which is why R1 and R2 above are stated as boolean volumes and clearances
measured directly rather than as gate rows.

**R8 — the bore recess and the lug-sector groove are left out.** The OEM relieves
the bore to R 37.379 behind each lug and grooves the lug-sector pocket at
z −15.571. Spec §4 C1 states a straight Ø74.20 bore and neither feature, and both
would cut through REQ-02's [37.05, 37.15] band. They are omitted, and REPORT §9
records the omission against the OEM rather than against the plan.
