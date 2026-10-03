# DESIGN_SPEC — OD-C09 printed front panel with button bezel (20261002-od-c09-front-panel)

Version 1.0 · RATIFIED by the Usta on 2026-10-02 (standing instruction "Usta'ya yalnız karar gereken yerde sor; açık soruları A-## satırı olarak ledger'a yaz ve ilerle" and the message of 2026-10-02 22:58 UTC; explicit confirmation of §5 and §6 pending, see §7) · data class PUBLIC · size M · lane CAD

## §1 Intent

OD-C09 is the 3D-printed front panel of the Open Dedica espresso machine, with the
bezel for the OEM front button board OD-E02 (BOM: "Front panel with button
bezel"). It stands on the base frame OD-C01 along its front edge, the mirror of
the delivered back panel OD-C11, under the front skirt of the delivered top panel
OD-C10. It frames the brew area: the group head housing OD-G01 stands vertical,
mouth down, on the carrier OD-C05 with its axis at (x 0, z 32); the portafilter
OD-G10 is carried in from the front, lifted into the bayonet and turned, and its
handle stays out through the panel while locked; the drip tray zone lies on the
plate under the mouth and the tray slides out to the front. The panel carries the
three OEM buttons (1 cup, 2 cups, steam) through three holes and holds the
button board behind them on two bosses. Done means: one valid printable solid
standing on the plate inside its front edge, held by four M3 screws driven from
above into four new inserts in the plate, the brew opening clear of the
portafilter's whole travel and of the tray's slide, the board held with its
three caps standing proud of the front face, nothing of it in the carrier's or
the housing's space, and every unconfirmed value in §6. The side panels, the
tray and the steam knob are not designed: their rows are assumptions and the job
is reopened when they land.

**Deliverables** (tier M): STEP AP242 of the panel; the check assembly STEP
(panel + OD-C01 + OD-C05 + OD-G01 with OD-G04 and OD-G10 as placed + OD-C10 +
OD-E02 as placed by §2); STL, and at J5 a 3MF written from the reviewed STL;
build and check scripts; REPORT; sections. No drawings or renders.

**Out of scope:** OD-C01 itself (the four new insert holes it needs are an OD-C01
spec change handed over, A-01); the side panels OD-C12/C13 and their corner
brackets OD-C16; the drip tray OD-C21/C22 (not scanned); the steam valve, wand
and knob OD-S01…S03 (phase 2: their place is reserved, A-13); the OD-000
assembly (the OD-G01 thread owns it); calipers; drawings; renders.

## §2 Interfaces and confirmed dimensions

| Item | Value | Tolerance | Source | Status |
|---|---|---|---|---|
| Reference solid OD-C01 (base frame, delivered) | `00_Spec/inputs/OD-C01_base_frame.step`: plate y −6 … 0, x ±120, z −305 … +100, corners R 10 about (±110, +90) and (±110, −295); feet holes Ø3.4 at (±110, +90); no hole yet under this panel's flanges (A-01) | — | OD-C01 spec 1.2 | CONFIRMED as the input; its numbers are §6 rows |
| Reference solids, the brew area | `OD-C05_group_head_carrier.step` and `od_g01_assembly_C1_v03.step` (housing + OD-G04 + OD-G10 locked), both in the housing frame, placed in the machine frame by housing x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0) (OD-C01 spec 1.2, OD-C05 spec 2.2); the mouth's front face at y 176.76 | — | OD-C05 spec 2.2; OD-G01 v03 (accepted by the Usta 2026-10-02) | CONFIRMED as inputs; the pose is A-05 |
| Reference solid OD-C10 (top panel, delivered) | `OD-C10_top_panel.step` at the identity: skin y 247 … 250, skirt 3.0 thick on the outline down to y 215.0, the front skirt z 97 … 100 | — | OD-C10 spec 1.2 | CONFIRMED as the input |
| OEM board OD-E02 | `OD-E02_control_board.step` (scan-rebuilt, datum frame: origin on the middle button collar axis on the back cover floor, +Z away from the caps, the caps at x −26.5, 0, +26.6 on −Z) | — | `OD-E02_REPORT.md` | CONFIRMED as the input; every number of it is A-03 |
| Fasteners | M3 heat-set inserts (OD-F01, Ø4.0 bore, 5.7 long) and M3 screws ISO 7380 (OD-F02, head Ø5.7) | — | open-dedica `docs/bom.csv` | CONFIRMED (project standard) |

**Coordinate frame:** the OD-C01 machine frame, so every overlay of the chassis
parts is the identity: X to the user's right, +Y up, +Z toward the user (the
front), the plate's top face y = 0. The panel's outer (front) face is the plane
z = +97.0, its inner face z = +94.0. **OD-E02 pose**: board x → −Y, board y → −X,
board z → −Z, its origin at (−99.0, 140.0, 69.35): the button row vertical on the
left pillar, 1 cup (B1) at the top, 2 cups (B2) at y 140, steam (B3) at the
bottom; the middle cap's top at z 98.5, 1.5 proud of the front face. **OD-G10
poses**: the locked pose of `od_g01_assembly_C1_v03.step` placed with the
housing; "rotated by φ" turns it about the housing's axis (machine x 0, z 32,
along Y), φ > 0 turning the handle toward +X. Every artifact of this job uses
these frames.

## §3 Process, material, environment

| Part | Process | Machine profile | Material (grade) | Density kg/m³ | Finish | Status |
|---|---|---|---|---|---|---|
| od_c09_front | FDM | machines/anycubic-kobra-max-3.toml (build volume UNKNOWN → A-10) | PLA (the Usta, 2026-10-02: "all printed in pla for now"; BOM: ASA) | 1240 | as printed | A-11 |

Environment: the front of the machine, 9 or more from the group head housing,
which carries brew water at up to 125 °C inside; drips and steam from the cup
area below; the user's hand on the buttons and on the portafilter's handle;
room temperature elsewhere. Loads: button presses (a few newtons per press,
through the board onto the two bosses), a hand steadying the machine on the
panel, the top panel's weight on its front edge.

## §4 Architecture and concepts

- **C1 — one wall with a brew opening, return ribs, two floor flanges, the
  button board on the left pillar (CHOSEN).** One solid.
  - **Wall** 3.0 thick, z +94.0 … +97.0, x −116.0 … +116.0, from the plate y 0
    up to y 215.0 (the top panel's skirt bottom). At |x| = 116 the plate's corner
    arc (R 10 about (±110, +90)) lies at z +98.0, so the wall's foot stands on the
    plate everywhere with ≥ 1.0 of plate in front of it (A-02); the mirror of
    OD-C11's wall (z −302 … −299).
  - **Brew opening** through the wall along Z, the union of the **tray slot**
    x −75.0 … +75.0, y 0 … 50.0 (the tray zone's width, open at the plate, A-06)
    and the **portafilter window** x −57.5 … +75.0, y 0 … 188.0; square corners.
    The panel is thus a right pillar x +75 … +116 over the full height, a left
    pillar x −116 … −75 below y 50 and −116 … −57.5 above, and a top bar
    y 188 … 215 over the full width. The portafilter's locked handle passes the
    wall at x ≈ 20 … 53, y ≈ 147 … 174 (it locks turned ≈ 28° toward +X, A-05);
    the window gives it φ from −55° to +10° (REQ-05).
  - **Return ribs**, 3.0 thick, z +84.0 … +94.0 (10 deep), on the wall's inner
    face along the opening's edges: R1 along the top edge, y 188.0 … 191.0,
    x −60.5 … +78.0; R2 along the right edge, x +75.0 … +78.0, y 0 … 191.0;
    R3 along the left edge above the step, x −60.5 … −57.5, y 50.0 … 191.0;
    R4 along the left edge below the step, x −78.0 … −75.0, y 0 … 53.0;
    R5 along the step's edge, y 50.0 … 53.0, x −78.0 … −57.5. Nothing of the
    panel lies at z < +84 inside |x| ≤ 60.5 (the carrier's and housing's front
    faces end at z +82.0 and +75.1).
  - **Floor flanges**, two, 4.0 thick, y 0 … 4.0, z +72.0 … +94.0 (22 deep), at
    x −104.0 … −76.0 and +76.0 … +104.0, outside the tray slot and clear of the
    feet holes at (±110, +90). Each has two Ø3.4 through-holes along Y at
    (x ±85.0, z +77.0) and (x ±95.0, z +77.0), for M3 × 8 screws driven from
    above into four new M3 inserts in OD-C01 at the same (x, z) (A-01); the
    screw heads Ø5.7 keep ≥ 1.5 from the gussets. Two **gussets** per flange,
    4.0 thick, at x ±(76.0 … 80.0) and ±(100.0 … 104.0): right triangles in the
    YZ plane with a 16.0 leg along the flange's top (z +78 … +94) and a 30.0 leg
    up the wall (y 4 … 34) (E-06).
  - **Button holes**, three, round, Ø15.0, through the wall along Z, each
    centred on its cap's axis where that axis crosses z +95.5 (OD-E02 as posed
    in §2; for B2 at (−99.0, 140.0)); each cap clears its hole by ≥ 0.5 all
    round (E-01). If a tilted side cap (B1, B3) needs a larger round hole for
    that, the plan says so and sizes it.
  - **Board bosses**, two, Ø11.0, axes along Z through the board's two screw
    holes as posed in §2 (expected near (−91.1, 153.2) and (−91.0, 127.3)),
    from the wall's inner face z +94.0 back to the board's front surface around
    each hole, where the boss's end face seats (a designed contact; the end
    levels near z +81.2 and +81.8 are measured in the plan from the posed
    OD-E02). Each has a Ø4.0 × 6.0 blind bore from its end face for an M3
    insert; the board is held by two M3 screws driven from its back through its
    own two holes into the inserts (screw length from the plan, A-03). If the
    board's surface around a hole is not flat to Ø11, the plan says so.
  - **Steam knob place** (phase 2, A-13): a cylinder Ø32 along Z about
    (x +95.5, y 140.0) on the right pillar is kept free of ribs and bosses
    behind the wall; no hole in this revision.
  - Nothing of the panel lies at z < +72.0 (REQ-07) or inside the tray slot's
    box (REQ-07).
  - The top panel's front skirt (z +97 … +100) stands on the wall's top edge
    at y 215.0 along the line z +97 (as at the back, A-07).
  - Print orientation (A-09): **lying on the front face** z = +97 on the bed,
    build direction −Z (toward the machine's rear): the wall is a flat plate,
    the ribs, flanges, gussets and bosses rise as vertical prisms, the button
    holes and insert bores are vertical holes, the gussets' hypotenuses face up;
    the four Ø3.4 flange holes run along Y, horizontal in the print (their
    crowns are the named exception). Envelope 232.0 × 215.0 × 25.0 (x ±116,
    y 0 … 215, z +72 … +97); on the bed 232 × 215, 25 tall.
- **C2 — the board horizontal above the opening.** Not chosen: the top bar above
  the portafilter's path is 27 tall (y 188 … 215) and the board 53.6 across its
  caps' row.
- **C3 — the board on the right pillar.** Not chosen: the locked handle turns
  ≈ 28° toward +X and needs the right side of the window (A-05); a right pillar
  wide enough for the board (≥ 58) would leave ≈ 5 between the window's edge and
  the locked handle.

## §5 Gate table

| ID | Requirement | Threshold | Hard/Soft | CAD/part | Basis | Check | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | Valid solid per part | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | Hard | CAD | house | `validity` | — |
| U-02 | Envelope within spec | 232.0 × 215.0 × 25.0 each in [spec − 0.1, spec + 0.1]; position against the datum reported apart (x ±116.0, y 0 … 215.0, z +72.0 … +97.0) | Hard | CAD | house | `envelope` | — |
| U-03 | Assembly closes | (a) at the identity with every reference solid placed by §2: designed contacts `clearance = 0`: the wall's and flanges' undersides on OD-C01's top face; the two boss end faces on OD-E02; OD-C10's front skirt on the wall's top edge. Every pair `interference ≤ 0` mm³. The panel's footprint inside the plate's outline, ≥ 0.5 from its edge and corner arcs; the flanges ≥ 3.0 and the wall's foot ≥ 2.0 from the edge of every existing OD-C01 hole; the four flange holes ≥ 6.0 centre to centre from every existing OD-C01 hole; panel to OD-C05, to the OD-G01 housing and to OD-G04 ≥ 2.0; the OD-C15 keep-outs (Ø8 × 2.0 cylinders on the plate top at (±110, +90), y 0 … 2.0) `interference ≤ 0`. (b) the panel lowered along −Y from +40.0 above its seat in steps ≤ 2.0, OD-C10 and OD-E02 absent: `interference ≤ 0` with OD-C01, OD-C05 and the OD-G01 assembly at every step | Hard | CAD | house | `clearance`, `interference`, `envelope` | A-01, A-02, A-05, A-07 |
| U-04 | Clean export | named body re-read unchanged, no stray shells, valid after re-import | Hard | CAD | house | `step_roundtrip` | — |
| U-05 | Every spec feature present | counts per the plan: 1 wall with 1 brew opening, 5 return ribs, 2 floor flanges, 4 gussets, 4 Ø3.4 flange holes, 3 button holes, 2 bosses Ø11.0 with 2 Ø4.0 blind bores | Hard | CAD | house | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | Soft: thin corners under a round | `min_wall` wide ≥ 2.0 | Soft | part | house | `min_wall` `detail["wide"]` | — |
| U-07 | Export mesh | STL at tol 0.01, angular a ≤ 4·acos(1 − 0.01/R_max) rad; `stl_max_sagitta ≤ 0.01`; the 3MF carries the same mesh (written at J5) | Hard | CAD | house | `write_stl`, `stl_max_sagitta` | — |
| U-08 | Threads cosmetic | applies to threaded parts; this target has none | Hard | CAD | house | — (N/A by this row) | — |
| D-01a | Wall, process floor | `min_wall ≥ 0.8` at a 0.4 nozzle | Hard | part | floor | `min_wall` | — |
| D-01b | Wall, structural | `min_wall ≥ 2.0` (wall and ribs 3.0, flanges and gussets 4.0, the webs beside the holes) | Hard | part | struct | `min_wall` | A-11 |
| D-02 | Bed fit | each envelope size ≤ the Kobra Max 3 build volume, lying on the front face: 232.0 × 215.0 on the bed, 25.0 tall | Hard | part | machine | `envelope` | A-10 |
| D-03a | Unsupported overhang | every downward face ≥ 45° from horizontal in the print orientation (front face on the bed, build direction −Z): the crowns of the four horizontal Ø3.4 flange holes are the named exception below, excluded by position, their least angle reported | Hard | part | floor | `overhang_census(build_dir=(0,0,-1))` | A-09 |
| D-03b | Unsupported bridge | span ≤ 5: the Ø3.4 horizontal holes bridge ≤ 3.4; nothing else bridges | Hard | part | floor | reviewer, from sections | A-09 |
| D-04a | Clearance hole for a fastener | the four flange holes Ø ≥ 3.25 (designed Ø3.4) | Hard | part | house | `bore_census`, `locate_bore` | — |
| D-05a | Heat-set insert boss | material ≥ 8.0 across around each Ø4.0 insert bore (the Ø11 bosses) | Hard | part | struct | `bore_census`, `radial_extent` | A-03 |
| D-05b | Heat-set insert hole | the two insert bores Ø 4.0 ± 0.05, depth 6.0 ± 0.1 (≥ 5.7) | Hard | part | floor | `bore_census`, `locate_bore` | A-03 |
| D-06a | Minimum feature | ≥ 1.0 | Hard | part | floor | `min_wall` | — |
| D-07 | Fit-critical bores | none: the insert bores are formed by the insert, the rest are clearance holes | Hard | part | floor | — (N/A by this row) | — |
| J-05 | Wall around a threaded hole | ≥ 3.0 around each insert bore (the Ø11 boss: 3.5) | Hard | part | struct | `min_wall` | — |
| E-01 | Component keep-out | panel to the posed OD-E02 ≥ 0.5 everywhere except the two boss end faces (the designed contacts of U-03): each cap in its hole, the board's housing behind the wall, the ribs | Hard | part | house | `clearance` (the plan names how the contact faces are excluded) | A-03 |
| E-05 | Mounting-hole alignment | each boss bore coaxial with its board screw hole as posed, offset ≤ 0.10 | Hard | CAD | house | `locate_bore` against the posed OD-E02's holes | A-03 |
| E-06 | Boss support | each board boss stands on the wall and is tied into it; each flange tied to the wall by two gussets | Hard | part | struct | reviewer, from sections | — |
| REQ-01 | Floor inserts | four Ø3.4 ± 0.1 through-holes along Y at (x ±85.0, z +77.0) and (x ±95.0, z +77.0), offset ≤ 0.10, 4.0 ± 0.1 long; the underside one plane at y 0.00 ± 0.10 | Hard | CAD | A-01 | `locate_bore`, `envelope` | A-01 |
| REQ-02 | Wall plane and footprint | the outer face at z +97.00 ± 0.10 and the inner face at z +94.00 ± 0.10 over the wall's height (sections at y 100 and y 200); x ±116.0 ± 0.1; the top face at y 215.00 ± 0.10 | Hard | CAD | A-02 | `envelope`; reviewer from sections | A-02 |
| REQ-03 | Brew opening | the opening's outline as §4 (tray slot x ±75.0, y 0 … 50.0; window x −57.5 … +75.0, y 0 … 188.0), each edge ± 0.1, from sections at z +95.5 | Hard | CAD | A-05, A-06 | reviewer from sections; `interference` of the two boxes (each shrunk 0.2 per side, z +93.8 … +97.2) with the panel = 0 | A-05, A-06 |
| REQ-04 | Buttons | with OD-E02 posed by §2: each cap's foremost point at z ≥ +97.5 (0.5 proud of the front face; B2 designed at +98.5); each button hole coaxial with its cap's axis at z +95.5, offset ≤ 0.25 | Hard | CAD | client (BOM: button bezel) | `envelope` of each cap region of the posed OD-E02; `locate_bore` | A-03, A-04 |
| REQ-05 | Portafilter travel | OD-G10 (a) at its locked pose rotated by φ from −55° to +10° in steps ≤ 5°: `clearance` to the panel ≥ 2.0 and to the posed OD-E02 ≥ 2.0; (b) rotated by φ = −50°, lowered 15.0 along −Y and moved along +Z from its axis at z +32 to z +182 in steps ≤ 5.0: `interference ≤ 0` with the panel and with OD-E02 at every step | Hard | CAD | client (the portafilter goes in and out) | `clearance`, `interference` | A-05 |
| REQ-06 | Driver access | each flange hole's axis clear of the panel from y 4.0 up to y 260.0 within r 3.0, and each OD-C15 screw axis at (±110, +90) clear of the panel from y 2.0 to y 260.0 within r 3.0 (a straight driver from above with the top panel off and the board out) | Hard | CAD | client (serviceability) | `interference` of six Ø6 cylinders with the panel = 0 | A-14 |
| REQ-07 | Keep-outs | no panel material at z < +72.0 (`envelope` min_z); none in the tray slot's box x ±74.8, y 0 … 49.8, z −15 … +120 (the tray slides out along +Z); none in the steam knob's place (Ø32 along Z about (+95.5, 140.0), z +60 … +93.8) | Hard | CAD | A-06, A-13 | `envelope`; `interference` of the boxes with the panel = 0 | A-06, A-13 |
| REQ-08 | Stiffness | **Soft.** The panel does not flex visibly under a button press or drum with the pump on, with the top panel on and the side panels absent; not a geometric gate: the review reports it INCONCLUSIVE with a risk rating, answered by the first print | Soft | part | client | — (bench) | A-12 |

**Named exceptions** (Usta U-18): D-03a for the crowns of the four horizontal
Ø3.4 flange holes in the print (bridges ≤ 3.4, within D-03b), the practice of
OD-C02 and OD-C11; recorded here for the Usta to confirm with §5.

## §6 Assumptions ledger

| ID | Question | Current assumption | Risk if wrong | Source of the value | Retire by | Status |
|---|---|---|---|---|---|---|
| A-01 | What the panel fastens to | four M3 × 8 screws from above through the floor flanges into four **new** M3 inserts in the OD-C01 plate at (±85, +77) and (±95, +77): an OD-C01 spec change handed over with OD-C08's and OD-C11's eight, or Ø4.0 holes drilled into a printed plate; the feet holes at (±110, +90) are 19.8 away | the plate has no holes there | this spec (the OD-C11 pattern, mirrored) | OD-C01's next revision | OPEN |
| A-02 | Plate edge and corners | the delivered plate: front edge z +100, corners R 10 about (±110, +90) (at x ±116 the edge lies at z +98.0); the wall at z +94 … +97 stands 3 inside the front edge and 4 inside the side edges, leaving the strip for the side panels | the side panels need the strip differently | OD-C01 spec 1.2; OD-C11 A-02 mirrored | OD-C12/C13 designs | OPEN |
| A-03 | OD-E02 geometry and fixing | the scan-rebuilt STEP is the board (scan only, no calipers: units and scale assumed; caps p95 ≈ 0.24); it is held by two M3 screws from its back through its own Ø3.5 holes into inserts in two bosses whose end faces seat on its front surface; the OEM held it with its own screws, which may be self-tapping | the board's holes or front surface are not where the scan puts them; the screws do not fit the holes | `OD-E02_REPORT.md` | calipers on the board; the first fit | OPEN |
| A-04 | Button layout | the three buttons in a vertical column on the left pillar, 1 cup at the top, steam at the bottom, the middle cap 1.5 proud of the front face; the caps of B1 and B3 are tilted ≈ 20° in the scan and stand proud by more | the user wants another order or the buttons on the right | this spec (design choice, §4 C2, C3) | the Usta | OPEN |
| A-05 | Portafilter pose and travel | OD-G10 locks as `od_g01_assembly_C1_v03.step` places it, the handle turned ≈ 28° toward +X from +Z; it is carried in turned φ = −50° (the bayonet's gaps are 66° wide and the ears lie under the lugs when locked), lowered 15 below its locked height; gasket wear turns the lock up to +10° further | the handle hits the window's edge on the way in or when the gasket is worn | `od_g01_assembly_C1_v03.step`; OD-G01 spec 1.3 §4 (lugs) | the first locked portafilter | OPEN |
| A-06 | Drip tray | the tray OD-C21 stands within x ±75, z −15 … +85 on the plate, its cup rest top ≤ 36.9 (OD-C01 A-06), and slides out to the front through the tray slot (x ±75, y 0 … 50) | the tray is wider or taller than the slot | OD-C01 spec 1.2 A-06 | the tray scan (issue #9) | OPEN |
| A-07 | Top panel joint | OD-C10's front skirt (z +97 … +100, bottom y 215) stands on the wall's top edge along the line z +97, as its rear skirt on OD-C11 (accepted by the Usta for OD-C10); no screws at the front (OD-C10 has none there) | the lid rattles at the front | OD-C10 spec 1.2 | the first assembly | OPEN |
| A-08 | Side panels | printed (the Usta, 2026-10-02); they lie outside x ±116 and meet the wall's ends (not designed); the board reaches x −115.17, 0.83 inside x −116 | a side panel's lip or post needs the space behind the left pillar | this spec | OD-C12/C13 designs | OPEN |
| A-09 | Print orientation | lying on the front face, build direction −Z, no supports | the 232 × 215 plate warps; a brim is needed | this spec | first print | OPEN |
| A-10 | Kobra Max 3 build volume | 420 × 420 × 500 (Anycubic specification, not in the machine file), as OD-C11 A-09 | does not fit (it does: 232 × 215) | OD-C11 A-09 | the Usta reads the printer | OPEN |
| A-11 | Material | PLA, 1240 kg/m³, on the Kobra Max 3 (the Usta, 2026-10-02); SOURCING_GUIDE §6 rule 3 reads "ASA near heat … PLA nowhere structural": the panel's nearest material is ≈ 9 from the group head housing, which carries brew water inside and runs warm | PLA softens near 55 °C: the top bar or the ribs creep near the group head | the Usta's message; SOURCING_GUIDE §6 | a thermometer on the top bar after a run of shots; reprint in PETG or ASA | OPEN |
| A-12 | Stiffness | a 3 mm wall with 10-deep return ribs along the opening, two floor flanges with gussets and the board on the left pillar; the top held only by the lid's skirt resting on it; the side edges free until the side panels exist | the panel flexes at a button press or drums | this spec | first print (REQ-08) | OPEN |
| A-13 | Steam knob (phase 2) | its place is a Ø32 area about (+95.5, 140) on the right pillar, kept free behind the wall; the hole and its valve mount come with the phase 2 steam job, which reopens this part | the steam valve needs another place | this spec | the phase 2 steam design | OPEN |
| A-14 | Assembly order | the panel is screwed to the plate before the board goes on (the board lies over the left flange screws); the board's two screws are driven from behind with the top panel off | — | this spec | the build guide | OPEN |

## §7 Decisions

| Date | Decision | By | Ref |
|---|---|---|---|
| 2026-10-02 | OD-G01 accepted with its documented deviation; side panels printed; everything printed in PLA for now | the Usta (message 22:58 UTC) | REQUEST.md |
| 2026-10-02 | job opened at PUBLIC; C1 proposed | Oğuz | job_start |
| 2026-10-02 | spec 1.0 ratified and C1 chosen on the Usta's standing instruction and the message of 2026-10-02 22:58 UTC; INTAKE_v01 §4 questions answered by §4 and §6 as design choices, all A-## rows; the Usta confirms or amends §5 and §6 at the next opportunity | the Usta (standing instruction), recorded by Oğuz | usta_gate spec_ratified, concept_picked |

## §8 Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-02 | INTAKE_v01 read; ratified |
| 0.1 | 2026-10-02 | first draft from the OD-C01, OD-C05, OD-C10, OD-C11 specs, the OD-G01 v03 assembly and the OD-E02 report |
