# DESIGN_SPEC — OD-C12, OD-C13 printed side panels and OD-C16 corner brackets (20261002-od-c12-c13-c16-side-panels)

Version 1.1 · RATIFIED by the Usta on 2026-10-02 (the answer "3/ printed … all printed in pla for now" of 2026-10-02 22:58 UTC and the standing instruction of 2026-09-30: design every printable part with the pipeline, ask only where a decision is needed, ledger the open questions and proceed; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C12 (left) and OD-C13 (right) are the 3D-printed side panels of the Open
Dedica espresso machine (the Usta chose printed over 3 mm acrylic, 2026-10-02).
Each stands on the base frame OD-C01 along one side edge, flush with the plate's
edge, from the back panel OD-C11 to the front, up to y 215 under the top panel
OD-C10's skirt, which then rests on the panel's top face: this carries the lid's
side edges (OD-C10 A-04, RV01 F1: today the lid leans on its −X rest pad). A lip
along each panel's top rises inside the lid's skirt and holds the panel's top
edge in place. OD-C16 is the printed corner bracket that fastens a panel's foot
to the plate: three per side, each screwed down into a new insert in OD-C01 and
taking the panel's screw from outside into its own insert. With printed panels
the bracket takes the place of the BOM's "corner bracket for acrylic skins"
(qty 16 → 6, A-15). Done means: three valid printable solids (left panel, right
panel, bracket) seated at the poses of §2, clear of every delivered part, and
every unconfirmed value in §6. The front panel OD-C09 is not designed: the
panels end at z +90 and the job reopens when OD-C09 lands (A-06).

**Deliverables** (tier M): STEP AP242 of each of the three parts; the check
assembly STEP (OD-C01, OD-C02, OD-C05, OD-C07, OD-C08, OD-C10, OD-C11, four
OD-C15 feet, the two panels and six brackets as placed); STL of each part (the
3MF is written by the orchestrator from the reviewed STL); build and check
scripts; REPORT; sections. No drawings or renders.

**Out of scope:** the front panel OD-C09, the tank dock OD-C06, the grommet
OD-C14 (its own job), any change to a delivered part (the six new OD-C01 inserts
are an OD-C01 change handed over, A-01), calipers, drawings, renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| OD-C01 base frame (delivered) | `00_Spec/inputs/OD-C01_base_frame.step` (identity): plate x ±120, z −305 … +100, y −6 … 0 (top y 0), vertical corner edges R 10 about (±110, −295) and (±110, +90); feet holes Ø3.4 at (±110, −295) and (±110, +90); no insert yet under the brackets (A-01) | — | OD-C01 spec 1.2 §4 | CONFIRMED as the input; A-01 |
| OD-C10 top panel (delivered) | `00_Spec/inputs/OD-C10_top_panel.step` (identity): outline x ±120, z −305 … +100, R 10 corners; skirt 3.0 thick (side skirts x ±117 … ±120), bottom face y 215.0; skin underside y 247; columns at (65, −60), (65, −210), (±90, −293), their ribs within x 45 … 97.5; rest pads at (±48, 30) | — | OD-C10 spec 1.2 §4; its DESIGN_PLAN F04, F05 | CONFIRMED as the input; A-02 |
| OD-C11 back panel (delivered) | `00_Spec/inputs/OD-C11_back_panel.step` (identity): wall z −302 … −299, x ±116, y 0 … 215; ledge x ±114, y 211 … 215, z −299 … −287; floor flanges x ±(72 … 104), z −299 … −277, gussets to z −283 | — | OD-C11 spec 1.2 §4 | CONFIRMED as the input; A-03 |
| OD-C07 valve mount (delivered) | `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` placed by x → −Z, y → −X, z → +Y, origin (−92, 0, −60): its zone x −117 … −67, z −154 … −35, top y 48 | — | OD-C07 spec 1.2; OD-C01 spec 1.2 A-05, A-17 | CONFIRMED as the input; A-04 |
| OD-C08 electronics tray (delivered) | `00_Spec/inputs/OD-C08_electronics_bay_tray.step` (identity): x 73 … 112, y 0 … 92, z −230 … −70 | — | OD-C08 spec 1.0 U-02 | CONFIRMED as the input; A-05 |
| OD-C02, OD-C05 (delivered) | `OD-C02_bulkhead.step` (identity, x 59 … 71); `OD-C05_group_head_carrier.step` by x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0) (x ±55) | — | their specs | CONFIRMED as inputs |
| OD-C15 feet (delivered) | `00_Spec/inputs/OD-C15_foot.step` at foot x → X, y → +Z, z → −Y, origins (±110, −6, +90) and (±110, −6, −295); keep-out: a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) for the screw head | — | OD-C15 spec 1.2 A-09 | CONFIRMED as the input |
| Fasteners | M3 heat-set inserts (OD-F01, Ø4.0 × 6.0 bore, 5.7 long) and M3 × 8 screws (OD-F02, ISO 7380, head Ø5.7 × 1.65) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard); A-12 |

**Coordinate frame:** the OD-C01 machine frame (X to the user's right, +Y up,
+Z toward the user, plate top y = 0). The panels are modelled in it at their
installed pose (identity). The bracket is modelled in its own frame (§4) and
placed at six poses: right side, bracket x → X, y → Y, z → Z, origin
(117.0, 0, z_c); left side, rotated 180° about Y (x → −X, y → Y, z → −Z), origin
(−117.0, 0, z_c); z_c ∈ {−262.0, −15.0, +62.0} on each side.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c12_left, od_c13_right | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-09) | PLA (the Usta, 2026-10-02: "all printed in pla for now"; the BOM says ASA / PETG) | 1240 | as printed | A-08 |
| od_c16_bracket | FDM | machines/creality-k1c.toml (build volume UNKNOWN → A-10) | PLA (as above) | 1240 | as printed | A-08 |

Environment: the two sides of the machine, room temperature on the outside;
inside, the electronics bay on the right (OD-C08), the valve mount on the left
(OD-C07), the thermoblock and group head ≥ 60 from either panel (x ≤ 55). Loads:
the panels' own weight, the lid's edges, a hand on the side, the screws.

## §4 Architecture and concepts

- **C1 — flat panels on three brackets each, the top held by the lid (CHOSEN).**
  Three solids.
  - **OD-C13 right panel**, in the machine frame:
    - **Wall** 3.0 thick, x 117.0 … 120.0, from the plate's top y 0 to y 215.0,
      from z −295.0 to z +90.0, its outer face on the plate's edge plane x 120;
      square end faces at z −295.0 and z +90.0, where the plate's corner arcs
      (R 10 about (110, −295) and (110, +90)) begin, so the whole footprint lies
      over the plate (1.1: an end following the arcs lifts off the bed in the
      print, J2 Q2). The wall's underside stands on the plate's top face; its top
      face y 215.0 carries the lid's side skirt (x 117 … 120), a designed contact.
    - **Top rail** x 110.0 … 117.0, y 205.0 … 215.0, z −280.0 … +80.0, on the
      wall's inner face.
    - **Lip** on the rail, z −280.0 … +80.0: a wedge whose section (in the XY
      plane) is the triangle (110.0, 215.0), (116.6, 215.0), (110.0, 218.81):
      its sloped face rises at 60° from the panel's plane, so it prints without
      support (1.1: a rectangular lip x 114 … 116.6, y 215 … 225 was a 10 deep
      ceiling in the flat print, J2 Q1); its outer edge at y 215 lies 0.40 from
      the lid skirt's inner face (x 117.0) (D-04d) and guides the skirt down onto
      the wall's top face.
    - **Bracket holes**, three Ø3.4 through the wall along X at (y 10.0,
      z −262.0), (y 10.0, z −15.0), (y 10.0, z +62.0), coaxial with the inserts
      of the brackets behind them; the M3 × 8 screws go in from outside, their
      button heads on the outer face.
  - **OD-C12 left panel**: the mirror image of OD-C13 about x = 0, and one
    feature more: a **relief** 0.9 deep in the inner face, x −117.9 … −117.0,
    y 0 … 55.0, z −160.0 … −29.0, over the valve mount's zone (OD-C07's two
    floor pads reach x −117 at y 0 … 4; the wall is 2.1 there).
  - **OD-C16 bracket**, in its own frame (x toward the panel, the outer face at
    x 0): a block x −19.0 … 0, y 0 … 16.0, z −8.0 … +8.0; a Ø3.4 through-hole
    along Y at (x −12.5, z 0) with a Ø6.5 counterbore from the top face y 16.0
    down to its floor at y 3.0, for an M3 × 8 driven from above into a new M3
    insert in OD-C01 (3.0 of bracket under the head, 5.0 into the 5.7 insert);
    a Ø4.0 × 6.0 blind insert bore along −X from the outer face x 0 at
    (y 10.0, z 0), for the M3 insert that takes the panel's screw (3.0 of panel,
    5.0 into the insert). The block is symmetric about z = 0, so the left
    brackets are the same part turned 180° about Y. Placed (§2), the six
    brackets put their plate holes at (±104.5, z_c) and their insert bores on
    the panels' hole axes.
  - Assembly order: brackets screwed to the plate (lid and panels off), then
    each panel offered from the outside against its three brackets and screwed,
    then the lid lowered; the lid's skirt closes over the lips.
  - Print orientation (A-11): each panel **lying on its outer face**, build
    direction −X for OD-C13 and +X for OD-C12: the wall is a flat plate, rail
    and end faces rise as vertical prisms, the lip's sloped face at 60° from the
    bed and its back face vertical, the three holes are vertical,
    the relief opens upward; no supports. The bracket **on its underside**,
    build direction +Y: the vertical hole and counterbore are vertical, the
    counterbore floor faces up; the insert bore runs horizontal, its crown the
    named exception. Envelopes: OD-C13 10.0 × 218.81 × 385.0 (x 110 … 120,
    y 0 … 218.81, z −295 … +90), on the bed 385 × 219, 10.0 tall; OD-C12 the
    same at x −120 … −110; OD-C16 19.0 × 16.0 × 16.0.
- **C2 — panels with floor flanges screwed into the plate (as OD-C11), no
  brackets.** Not chosen: the flange holes run horizontal in the panel's flat
  print, the flanges stand 12 proud of a 385 × 215 plate, and a flange the
  length of the panel crosses the valve mount's and the bay's zones.
- **C3 — 3 mm acrylic skins in OD-C16 corner brackets.** Not chosen: the Usta
  chose printed panels (2026-10-02).

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0`, for each of the three part files | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | OD-C13 10.0 × 218.81 × 385.0, OD-C12 10.0 × 218.81 × 385.0, OD-C16 19.0 × 16.0 × 16.0, each size in [spec − 0.1, spec + 0.1]; position against the datum reported apart (OD-C13 x 110.0 … 120.0, OD-C12 x −120.0 … −110.0, both y 0 … 218.81, z −295.0 … +90.0; OD-C16 x −19.0 … 0, y 0 … 16.0, z −8.0 … +8.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) in the check assembly at the poses of §2: designed contacts `clearance = 0`, `interference ≤ 0` mm³: each panel's underside on OD-C01's top face; each bracket's underside on OD-C01's top face; each bracket's outer face on its panel's inner face (x ±117); OD-C10's side-skirt bottom faces on the panels' top faces (y 215, over x ±117 … ±120); the lip to OD-C10's skirt inner face 0.40 ± 0.05 (REQ-02, D-04d); every other pair of a new part with any solid (OD-C01, OD-C02, OD-C05, OD-C07, OD-C08, OD-C10, OD-C11, the four OD-C15 feet, the other new parts) `clearance ≥ 0.5`; each bracket's insert bore coaxial with its panel hole, offset ≤ 0.10 (`locate_bore` on both solids). (b) assembly path, in the order of §4: each bracket lowered along −Y from +20.0 to its seat in steps ≤ 2.0 with every delivered part present; each panel moved inward along X from 20.0 outside its seat in steps ≤ 2.0 with the brackets in place; OD-C10 lowered along −Y from +40.0 to its seat in steps ≤ 2.0 with the panels in place: `interference ≤ 0` mm³ at every step against every solid | Hard | CAD | house | `clearance`, `interference`, `locate_bore` | A-01 … A-05 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import, for each part file | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: OD-C13 1 wall with 2 square end faces, 1 rail, 1 lip (one 60° sloped face), 3 Ø3.4 through-holes along X; OD-C12 the same plus 1 relief; OD-C16 1 block, 1 Ø3.4 through-hole and 1 Ø6.5 counterbore along Y, 1 Ø4.0 blind bore along X | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad, R_max the largest curved-face radius of each part; `stl_max_sagitta ≤ 0.01` | Hard | CAD | house | `write_stl`, `stl_max_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; these targets have none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (wall 3.0; 2.1 at OD-C12's relief; rail 7.0 × 10.0; the lip's thin edge is its 0.40 gap side, D-06a; the bracket's least web, counterbore to insert bore, 3.25) | Hard | part | struct | `min_wall` | — |
| D-02 | Bed fit | each panel ≤ the Kobra Max 3 build volume lying on its outer face (385.0 × 218.81 on the bed, 10.0 tall); the bracket ≤ the K1C build volume (19 × 16 × 16) | Hard | part | machine | `envelope` | A-09, A-10 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation of §4 (panels: `overhang_census(build_dir=(−1,0,0))` for OD-C13 and `(1,0,0)` for OD-C12; bracket: `(0,1,0)`); the panels' only downward faces are the lips' sloped faces at 60°; the bracket's insert-bore crown is the named exception below, excluded by position, its least angle reported | Hard | part | floor | `overhang_census` | A-11 |
| D-03b | Unsupported bridge | span ≤ 5: only the bracket's Ø4.0 insert-bore crown bridges (4.0) | Hard | part | floor | reviewer, from sections | A-11 |
| D-04a | Clearance hole for a fastener | the panels' six holes and the brackets' vertical holes Ø ≥ 3.25 (designed Ø3.4) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-04d | Printed sliding fit | the lip to OD-C10's skirt inner face ≥ 0.30 per side (designed 0.40) | Hard | part | house | `clearance` | A-02, A-14 |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around the bracket's insert bore (the block 16 × 16 about it) | Hard | part | struct | `bore_census`, `radial_extent` | A-12 |
| D-05b | Heat-set insert hole | the bracket's insert bore Ø4.0 ± 0.05, depth 6.0 ± 0.1 (≥ 5.7) | Hard | part | floor | `bore_census`, `locate_bore` | A-12 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the insert bore is formed by the insert, the rest are clearance holes | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 around the bracket's insert bore (4.0 to the top face, 6.0 to each side, 3.25 to the counterbore) | Hard | part | struct | `min_wall` | — |
| E-06 | Boss support | the bracket is one solid block; each panel's lip is tied into its rail and the rail into the wall | Hard | part | struct | reviewer, from sections | — |
| REQ-01 | Panel wall and footprint | each panel's outer face at x ±120.00 ± 0.10 and inner face at x ±117.00 ± 0.10 over z −295 … +90 (sections at y 50 and y 200); underside one plane at y 0.00 ± 0.05; top face y 215.00 ± 0.05 over x ±(116.6 … 120); square end faces at z −295.00 and +90.00 ± 0.10; the footprint wholly over plate material (never outside the plate's outline seen along Y) | Hard | CAD | A-01 | `envelope`, `radial_extent`; reviewer from sections | A-01 |
| REQ-02 | Lid seat and lip | each lip the wedge of §4: its section through (±110.0, 215.0), (±116.6, 215.0), (±110.0, 218.81) ± 0.1, sloped face 60° ± 1° from the panel's plane, z −280.0 … +80.0 ± 0.1; `clearance`(lip, OD-C10) = 0.40 ± 0.05 at the identity; OD-C10's side-skirt bottoms rest on the panels' top faces (U-03 (a)) | Hard | CAD | A-02 | `envelope`, `clearance` | A-02, A-14 |
| REQ-03 | Panel holes | three Ø3.4 ± 0.1 through-holes per panel along X at (y 10.0, z −262.0 / −15.0 / +62.0), offset ≤ 0.10 | Hard | CAD | A-07 | `locate_bore`, `bore_census` | A-07 |
| REQ-04 | Valve-mount relief (OD-C12 only) | the inner face at x −117.90 ± 0.05 over y 0 … 55.0, z −160.0 … −29.0 (± 0.1); `clearance`(OD-C12, OD-C07) ≥ 0.5 | Hard | CAD | A-04 | `envelope` of the relief; `clearance` | A-04 |
| REQ-05 | Bracket | block 19.0 × 16.0 × 16.0; Ø3.4 ± 0.1 through-hole along Y at (x −12.5, z 0), offset ≤ 0.10, Ø6.5 ± 0.1 counterbore from y 16.0 with its floor at y 3.00 ± 0.10; Ø4.0 insert bore along −X from x 0 at (y 10.0, z 0), offset ≤ 0.10 (D-05b); at the six poses the plate holes fall at (±104.5, z_c) ± 0.10 | Hard | CAD | A-01, A-07 | `locate_bore`, `bore_census`, `envelope` | A-01, A-07 |
| REQ-06 | New OD-C01 inserts | each of the six positions (±104.5, z_c) lies ≥ 8.0 from the plate's edge (centre to edge), ≥ 6.0 centre to centre from every existing OD-C01 hole and from every insert already handed over (OD-C08 (88/106, −222/−78), OD-C11 (±81/±95, −282)), and the plate is solid in a Ø8 circle about it | Hard | CAD | A-01 | `bore_census` of OD-C01; reviewer computes the distances | A-01 |
| REQ-07 | Keep-outs and access | no new part inside the Ø8 × 2.0 cylinder above each OD-C15 foot hole (`interference` = 0 with four such cylinders); each bracket screw's axis clear of every solid within r 4.0 from y 16.0 to y 215.0 with the panels and OD-C10 removed (a straight driver reaches it from above); each panel hole's axis clear of every solid within r 4.0 from the outer face out to 20.0 outside it | Hard | CAD | client (SOURCING_GUIDE §6 rule 4) | `interference` of the keep-out and access cylinders with the assembly = 0 | A-05 |
| REQ-08 | Stiffness | **Soft.** The panels do not flex or drum visibly with the lid on; a hand on a side does not shift the lid; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print | Soft | part | client | — (bench) | A-13 |

**Named exceptions** (Usta U-18): D-03a for the crown of the bracket's
horizontal Ø4.0 insert bore in its print (a bridge of 4.0, within D-03b), the
usual FDM practice for small horizontal holes (as on OD-C02 and OD-C11);
recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | What the brackets fasten to | six **new** M3 inserts in OD-C01 at (±104.5, −262.0), (±104.5, −15.0), (±104.5, +62.0), as blind or through Ø4.0 bores from the top (OD-C01's spec decides, as for the eight handed over by OD-C08/C11); the panels' outer faces flush with the plate's side edges and corner arcs | the plate has no holes there; the plate's edge is not straight enough for a flush panel | this spec (design choice); OD-C01 spec 1.2 §4 | OD-C01's next revision; calipers | OPEN |
| A-02 | OD-C10 interface | the delivered lid: side skirts x ±117 … ±120 with their bottom face at y 215.0; nothing of the lid in x ±(113 … 117) below y 247 within z −285 … +85 but the skirt; the lid's weight now bears on the panels' top faces as well as on its four columns | the lid rocks on four columns plus two edges | OD-C10 spec 1.2 §4, DESIGN_PLAN F04, F05 (INTAKE) | the first assembly | OPEN |
| A-03 | Rear corner | OD-C11's wall ends at x ±116 and z −302 … −299; the panel ends square at z −295 (the corner arcs' start) with its inner face at x ±117: each rear corner keeps an opening ≈ 4 × 4 seen from outside, between the panel's end and the wall's end over the plate's R 10 corner, closed above by the lid's corner skirt; a printed corner cap can close it later | the slit looks unfinished; an insect or a finger gets in | OD-C11 spec 1.2 §4 | the first assembly; a later corner cap | OPEN |
| A-04 | OD-C07 under the left panel | the valve mount reaches x −117 (OD-C01 A-05; its envelope ±25 about x −92); OD-C12's 1.0 relief over y 0 … 55, z −160 … −29 keeps ≥ 0.5 from it | the mount or its valve reaches further out or higher | OD-C01 spec 1.2 A-05, A-17; OD-C07 spec U-02 | the check assembly (U-03) | OPEN |
| A-05 | OD-C08 beside the right panel | the tray x 73 … 112, z −230 … −70, y 0 … 92 (board to x ≈ 109.3): 5.0 from the panel's inner face; the brackets keep out of its z range | the board or its looms reach the panel | OD-C08 spec 1.0 U-02; C08_C11 notes | the check assembly | OPEN |
| A-06 | Front panel OD-C09 (not designed) | the panels end square at z +90.0 (the front corner arcs' start), leaving the front R 10 corners to OD-C09; OD-C09 meets them between their inner faces or across their ends, and may add brackets of this design at the front corners; this job reopens when OD-C09 lands | OD-C09 needs a different end, posts or more brackets | this spec | OD-C09 design | OPEN |
| A-07 | Fixing | three brackets per side at z −262, −15, +62 (clear of the feet holes, the bay, the valve mount and OD-C11's flanges); per bracket two M3 × 8 ISO 7380 (one down into OD-C01, one through the panel from outside, its head proud on the panel's outer face) and two inserts (one in the bracket, one in OD-C01); 12 screws and 12 inserts in all | the panel needs more fixing points; the proud heads are not wanted | this spec | the Usta; the first assembly | OPEN |
| A-08 | Material | PLA, 1240 kg/m³ (the Usta, 2026-10-02, "for now"); the BOM said ASA / PETG and SOURCING_GUIDE §6 rule 3 says "PLA nowhere structural": PLA softens near 55–60 °C; the panels are ≥ 60 from the thermoblock and the group head, and the bay's heat leaves through OD-C11's vents | the panels creep or warp warm; a later print in PETG or ASA needs no change of geometry | the Usta's message; SOURCING_GUIDE §6 | a temperature reading inside the running machine | OPEN |
| A-09 | Kobra Max 3 build volume | 420 × 420 × 500 (Anycubic specification, not in the machine file); a panel is 385 × 219 on the bed | does not fit: two halves per panel | as OD-C01 A-09 | the Usta reads the printer | OPEN |
| A-10 | K1C build volume | 220 × 220 × 250 (Creality listing, not in the machine file) | none for a 19 mm part | as OD-C15 A-08 | the machine file | OPEN |
| A-11 | Print orientation | panels on the outer face, no supports, brim against warp; brackets on their underside | a 393 mm PLA plate warps at its corners | this spec | first print | OPEN |
| A-12 | Inserts and screws | M3 heat-set inserts 5.7 long in Ø4.0 × 6.0 bores; M3 × 8 ISO 7380 | the stocked insert wants another bore | as OD-C11 A-05; OD-C01 A-11 | the Usta's stocked insert datasheet | OPEN |
| A-13 | Stiffness | a 3.0 PLA plate 385 × 215, fixed at three points along its foot and held along its top by the lid's skirt over the lip: no calculation | it drums or bows between the brackets | this spec | first print (REQ-08) | OPEN |
| A-14 | Lip fit | 0.40 between the lip's outer edge and the skirt at y 215, opening upward along the 60° slope; the lip locates the skirt over its lowest 3.8 only; the lid's skirt is straight within that | the lid binds on the lips or rattles | this spec; D-04d | first assembly | OPEN |
| A-15 | Bracket count | 6 brackets (OD-C16, three per side) replace the BOM's 16 for acrylic skins; the acrylic sheet OD-F03 is not used | the Usta goes back to acrylic | this spec; BOM OD-C16, OD-F03 | the Usta | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-02 | printed side panels, not acrylic; every printed part in PLA for now | the Usta (2026-10-02 22:58 UTC) | REQUEST.md |
| 2026-10-02 | job opened at PUBLIC; OD-C12, OD-C13 and OD-C16 in one job (a mirrored pair and the bracket between them and the plate; one build, one review of the three part files); C1 proposed | Oğuz | job_start |
| 2026-10-02 | spec 1.0 ratified and C1 chosen on the Usta's answer and standing instruction; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |
| 2026-10-02 | spec 1.1 on the J2 plan's Q1 … Q4 (§8): of the plan's options for Q1, a printable lip shape in place of supports, a standing print or a separate strip; ratified on the standing instruction | Oğuz (standing instruction) | usta_gate spec_ratified 1.1 |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-02 | first issue from the INTAKE and the delivered neighbours' specs; ratified |
| 1.1 | 2026-10-02 | on the J2 plan's questions, before the first build: Q1 the lip becomes a 60° wedge on a rail x 110 … 117 (a rectangular lip was a ceiling in the flat print); Q2 square panel ends at z −295 and +90 (ends on the corner arcs lifted off the bed); Q3 the lip's z range −280 … +80 governs; Q4 OD-C12's relief 0.9 deep (wall 2.1); envelopes 10.0 × 218.81 × 385.0 (§4, U-02, U-05, D-01b, D-02, D-03a, REQ-01, REQ-02, REQ-04, A-03, A-06, A-14). Spec 1.0 kept as `DESIGN_SPEC_v1.0.md` |
