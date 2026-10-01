# REPORT — od_c11_back v03 (20261001-od-c11-back-panel)

Designer: Claude Code, claude-opus-5-5 · spec version 1.2 (SHA-256 6da33456…a61245, checked) · plan `01_CAD/DESIGN_PLAN.md` as amended by `01_CAD/DESIGN_PLAN_v02.md` and `01_CAD/DESIGN_PLAN_v03.md` · 2026-10-01 UTC · brief WP-04, build attempt 3 of 3, fix cycles used 0 of 3 · outcome SUBMITTED

All input hashes in brief WP-02 (and the spec 1.2 hash in WP-04) were checked and match.

## 1. Files

SHA-256 of every file is in the JSON block (section 11), computed after the last file was written.

| File | Note |
|---|---|
| `01_CAD/DESIGN_PLAN_v03.md` | plan amendment for spec 1.2 (the v01 plan and v02 amendment stand otherwise) |
| `01_CAD/build_od_c11_back_v03.py` | parametric script. The v02 script with `gusset_leg_wall` = (30.0, 18.0), paired with `gusset_x0` (72.0, 100.0) |
| `01_CAD/check_od_c11_back_v03.py` | checks. The v02 predicates, with the U-03 (a) hole-rim row split into wall foot (≥ 2.0) and flanges (≥ 3.0) |
| `01_CAD/build_record_v03.json` | parameters, export hashes, STL settings, placements |
| `01_CAD/check_od_c11_back_v03.json`, `.log` | every gate row and fact, measured on the re-imported STEP files |
| `01_CAD/sections_od_c11_back_v03.py`, `01_CAD/sections_v03.json` | D6 sections and their `nothing_clipped` results |
| `01_CAD/sweep_od_c11_back_v03.sh`, `01_CAD/sweep_summary_v03.py`, `01_CAD/sweep_v03/sweep_summary.json`, `01_CAD/sweep_v03_driver.log` | D7 sweep: 15 runs into `01_CAD/sweep_v03/<run>/` |
| `01_CAD/probe/probe_passthrough_gap_v03.py`, `.json` | fact: the gap from each measured pass-through to the panel's material in front of the wall, for every run |
| `01_CAD/report_block_v03.py` | writes this REPORT's JSON block from the check JSON, the sweep summary and the files on disk |
| `02_STEP_STL/od_c11_back_C1_v03.step` | AP242 (`tools.core.write_step`), part `od_c11_back`; re-imported for every measurement |
| `02_STEP_STL/od_c11_assembly_C1_v03.step` | AP242 check assembly: od_c11_back, od_c01_frame, od_c02_bulkhead, od_c03_cradle, od_h01_pump as placed |
| `02_STEP_STL/od_c11_back_C1_v03.stl` | binary, meshed afresh (cached triangulation cleared); tolerance 0.01 mm, angular 0.20 rad, 3928 triangles |
| `03_Sections/*_v03_*.png` (20 files) | sections; each measured `nothing_clipped` = 0 |

No v01 or v02 file was overwritten.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3) · ocpsvg 0.6.0 · repo commit 10929db1408d89144bd4af9cad971440427933d0 (unchanged since v01)

## 3. Gate self-check

`01_CAD/check_od_c11_back_v03.py` measured these rows on the re-imported STEP files. The JSON holds 226 rows:

| Status | Rows |
|---|---|
| PASS | 95 |
| PASS_ASSUMED | 126 |
| FAIL | 0 |
| INCONCLUSIVE | 3 (E-06, E-11: reviewer rows; REQ-09: Soft bench) |
| N/A | 2 |

The table below gives the worst row of each §5 ID and shows U-03 row by row. Bands are from GATES.md §0: mm 0.005, deg 0.001, mm³ 0.001, rad 0.00002; counts and mm² 0.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | 1 solid; brep_valid 1; naked edges 0 | 1, 1, 0 | 0 | — | PASS | — |
| U-02 | 232.000 × 215.000 × 25.000. Position: x −116.000 … 116.000, y 0.000 … 215.000, z −302.000 … −277.000 | each size in [spec − 0.1, spec + 0.1]; position ± 0.1 | +0.100 | — | PASS | — |
| U-03 (a) plate contact | clearance 0.000; common volume 0.000 mm³ | = 0; ≤ 0 | 0 | — | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) footprint inside the outline | 0.000 mm² outside the outline; least distance to the outline 0.780 | = 0; ≥ 0.5 | +0.280 | wall corner to the R 10 arc | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) underside over plate material | 0.000 mm² of the 2067.683 mm² footprint lies over plate holes | = 0 | 0 | — | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| **U-03 (a) wall's foot to the edge of every existing hole (1.2)** | **2.300** to the rims of the feet holes Ø3.400 at (±110, −295), centre 4.000 from the foot. 26 plate holes along Y were checked. The foot region is 696.0 mm², split at the measured inner face z −299.000 | ≥ 2.0 | **+0.300** | (±110, 0, −295) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| **U-03 (a) flanges to the edge of every existing hole (1.2)** | **4.300** to the same rims, centre 6.000 from the flange ends at x ±104. The flange region is 1371.683 mm² | ≥ 3.0 | **+1.300** | (±110, 0, −295) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) under each flange hole | plate material missing under a Ø3.4 plug: 0.000 mm³ (all four). Nearest existing plate hole: 31.780 (x ±81) and 19.849 (x ±95) | ≤ 0; ≥ 6.0 | +13.849 | (±95, 0, −282) to (±110, −295) | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (a) neighbours | OD-C03 43.863, OD-H01 61.540, OD-C02 37.014; common volume 0.000 mm³ each | ≥ 20.0; ≤ 0 | +17.014 | — | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-03 (b) | lowered from +40.0 to 0 in 2.0 steps (21 poses). Worst common volume 0.000 mm³ with OD-C01, OD-C02, OD-C03 and OD-H01 | ≤ 0 at every step | 0 | every pose | PASS (assumed: A-01, A-02, A-07) | A-01, A-02, A-07 |
| U-04 | part: AP242, 1 solid, volume delta 6.4e-10 mm³, faces delta 0, label kept, valid after. Assembly: 5 solids, labels kept, faces delta 0, valid after, per-child volume delta ≤ 4.3e-9 mm³ | in [0, 0] mm³ (band 0.001); 0; 1 | inside the band | — | PASS | — |
| U-05 / feature_census | planar 46, cylindrical 19 (concave 19), cone/sphere/torus/B-spline/other 0, bores 9. Along Y: 4 Ø3.4 through, 2 Ø4.0 blind. Along Z: 3 Ø12 through. 10 R 2.0 slot ends, 4 gusset hypotenuses, 2 boss undersides, 2 flange fronts, 3 ledge-underside pieces, 2 ledge ends, 1 wall outer face | plan §3 counts | 0 | — | PASS | — |
| U-06 (Soft) | `min_wall_wide` 3.000 (spacing 0.7) | ≥ 2.0 | +1.000 | — | PASS | — |
| U-07 | tolerance 0.01; angular 0.20 rad; max sagitta 0.00499 on a fresh re-mesh of the re-imported STEP; mesh 1 body, 0 naked edges, winding 1 | ≤ 0.01; ≤ 0.23097 rad; ≤ 0.01 | +0.00501 (sagitta) | — | PASS | — |
| U-08 | no threads | N/A by its row | — | — | N/A | — |
| D-01a | `min_wall` 3.000 (spacing 0.7) | ≥ 0.8 | +2.200 | — | PASS | — |
| D-01b | 3.000 | ≥ 2.0 | +1.000 | — | PASS | — |
| D-02 | 232.0 × 215.0 on the bed, 25.0 tall | ≤ 420 × 420, ≤ 500 | +188.0 | — | PASS (assumed: A-09) | A-09 |
| D-03a | `overhang_census(build_dir=(0,0,1))` on the solid with the six named-exception holes refilled by position (57 faces as planned, 1 solid): least downward angle 90.0°. Named exception, reported apart: the 4 Ø3.4 flange-hole crowns and the 2 Ø4.0 insert-bore crowns read 0.0° (whole-part census 0.0° at (−95, 0, −280.3), a flange-hole crown). No downward face lies outside the exception | ≥ 45° outside the exception | +45.0 | — | PASS (assumed: A-08) | A-08 |
| D-03b | reviewer row. Designer reading: horizontal holes bridge 3.400 and 4.000; `flat_ceiling_spans` 0.000 (spacing 0.7) | ≤ 5.0 | +1.000 | — | PASS (assumed: A-08), designer reading | A-08 |
| D-04a | 3.400 (all four) | ≥ 3.25 | +0.150 | (±81 / ±95, 0, −282) | PASS | — |
| D-05a | across X 12.000, across Z 15.000 (both bosses) | ≥ 8.0 | +4.000 | (84 … 96, 210, −293) | PASS (assumed: A-05) | A-05 |
| D-05b | Ø4.000, depth 6.000 (both) | Ø in [3.95, 4.05]; depth in [5.9, 6.1] and ≥ 5.7 | +0.050 | (±90, 209, −293) | PASS (assumed: A-05) | A-05 |
| D-06a | 3.000 | ≥ 1.0 | +2.000 | — | PASS | — |
| D-07 | no fit-critical bores | N/A by its row | — | — | N/A | — |
| J-05 | +X 4.000, −X 4.000, +Z 4.000, −Z 7.000 (both bores) | ≥ 3.0 | +1.000 | (±96, 210, −293) | PASS | — |
| E-06 | reviewer row. Designer reading (sections x 74, x ±102, x 90, y 207, z −290): one solid. Each boss is a 12 × 8 × 12 block fused to the wall and to the ledge's underside. Each flange (32 × 22) is fused to the wall and tied by two 4.0 gussets at its ends: inner 16 × 30, outer 16 × 18. No notch remains in any gusset | reviewer, from sections | — | — | INCONCLUSIVE (reviewer row) | — |
| E-11 | reviewer row. Designer reading: the five slots open the wall behind the bay (centre lines clear through the wall). The cord hole and both tube holes are through, and nothing is behind them: common volume of a Ø12 cylinder from the wall's inner face to z −277 is 0.000 mm³ on each. Gap to the nearest material in front of the wall: cord 3.434 (+X outer gusset top corner (100, 22)), tube −100 2.000 (−X outer gusset top, y 22), tube −84 2.000 (−X inner gusset face, x −76) | reviewer, from sections | — | — | INCONCLUSIVE (reviewer row) | A-03, A-06 |
| REQ-01 | four holes Ø3.400, offset 0.000, length 4.000, through; underside one planar face at y 0.000 | Ø 3.4 ± 0.1; ≤ 0.10; 4.0 ± 0.1; 1 face at 0.00 ± 0.10 | +0.100 | (±81 / ±95, 0, −282) | PASS (assumed: A-01) | A-01 |
| REQ-02 | outer face −302.000 and inner face −299.000 at y 50 and y 200 (x −40, 0, 40); x −116.000 / 116.000 | ± 0.10; ± 0.1 | +0.100 | — | PASS (assumed: A-02) | A-02 |
| REQ-03 | Ø12.000, offset 0.000, through | 12.0 ± 0.1; ≤ 0.10; through | +0.100 | (95, 30) | PASS (assumed: A-03) | A-03 |
| REQ-04 | (−100, 30) and (−84, 30): Ø12.000, offset 0.000, through | 12.0 ± 0.1; ≤ 0.10; through | +0.100 | — | PASS (assumed: A-04) | A-04 |
| REQ-05 | max z −277.000; common volume with the box x ±70, y 0 … 100, z −298.8 … −250: 0.000 mm³ | ≤ −277.0; = 0 | 0.000 | — | PASS (assumed: A-07) | A-07 |
| REQ-06 | five slots: width 4.000, height 80.000, centres x 78/86/94/102/110 at 0.000 off, y 100.000 … 180.000 | ± 0.1 each | +0.100 | rays at (x_c, 140, −300.5) | PASS (assumed: A-06) | A-06 |
| REQ-07 | two bores Ø4.000, depth 6.000, offset 0.000, blind. The top is one planar face at y 215.000 spanning z −302.000 … −287.000 | Ø 4.0 ± 0.05; 6.0 ± 0.1; ≤ 0.10; 1 face over z −299 … −287 | +0.050 | (±90, 209, −293) | PASS (assumed: A-05) | A-05 |
| REQ-08 | common volume of each of the four Ø6 cylinders y 4 … 260 with the panel: 0.000 mm³. They touch the flange top at y 4 by construction (clearance 0.000) | = 0 | 0 | — | PASS | — |
| REQ-09 (Soft) | bench gate, not geometric | answered by the first print | — | — | INCONCLUSIVE (by its row) | A-11 |
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| feature_census | as U-05 | plan §3 | 0 | — | PASS | — |
| envelope_within_spec | sizes as U-02. Position (reported apart): min/max x, y, z each within ± 0.1 of ±116.0, 0 … 215.0, −302.0 … −277.0 | ± 0.1 | +0.100 | — | PASS | — |

These are self-checks: no HARD gate is cleared until the reviewer measures it.

## 4. Robustness sweep (D7)

Each fit-critical parameter in the plan was rebuilt at its spec tolerance limits. Each run was exported into `01_CAD/sweep_v03/<run>/` and run through the same checks. All 15 runs built one solid of 65 faces, and every run passed every row (none FAIL; INCONCLUSIVE only on E-06, E-11 and REQ-09, by their rows). The table gives the worst margin of the parameter's own rows.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| flange_hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01 diameter at both ends | 0.000 (at the limit, PASS). D-04a +0.050 at low |
| flange_hole_dx (holes moved along X) | −0.1 · 0 · +0.1 | yes | REQ-01 offset 0.100 at both ends | 0.000 (at the limit, PASS). Nearest plate hole 19.774 at high (+13.774). REQ-08 0.000 mm³ |
| insert_d | 3.95 · 4.0 · 4.05 | yes | REQ-07 / D-05b diameter at both ends | 0.000 (at the limit, PASS). J-05 3.975 at high (+0.975) |
| insert_depth | 5.9 · 6.0 · 6.1 | yes | REQ-07 / D-05b depth at both ends | 0.000 (at the limit, PASS). Depth ≥ 5.7: +0.200 at low |
| pass_d | 11.9 · 12.0 · 12.1 | yes | REQ-03 / REQ-04 diameter at both ends | 0.000 (at the limit, PASS). All three holes through. Gap to the gussets 1.950 at high (probe) |
| wall_z (both faces moved, the gussets with them) | −0.1 · 0 · +0.1 | yes | U-02 size_z 25.1 / 24.9 and REQ-02 at the limit | 0.000 (at the limit, PASS). **U-03 wall foot to hole rim 2.400 at low, 2.200 at high (+0.200)**; flanges 4.300; outline 0.704 at low (+0.204); REQ-05 box 0.000 mm³ at both ends |
| y_top | 214.9 · 215.0 · 215.1 | yes | REQ-07 top and U-02 size_y at both ends | 0.000 (at the limit, PASS) |

Reading: the part passes at nominal and at every tolerance limit. The least margins that are not "at the limit" are U-03's wall foot (+0.200 at wall_z high) and the outline distance (+0.204 at wall_z low).

## 5. Build facts

- Envelope 232.000 × 215.000 × 25.000 mm (x −116 … 116, y 0 … 215, z −302 … −277).
- Volume 165 529.565 mm³; mass 210.223 g at 1270 kg/m³ (A-10); centre of mass (−2.514, 110.049, −299.371).
- STL (for the orchestrator's 3MF): 3928 triangles. Bounding box (−116.0, 0.0, −302.0) … (116.0, 215.0, −277.0), size 232.0 × 215.0 × 25.0. Tolerance 0.01 mm, angular 0.20 rad, sagitta 0.00499 mm; one closed body, 0 naked edges. Meshed afresh with the cached triangulation cleared (`tools.core.write_stl`); a re-mesh of the re-imported STEP gives the same 3928 triangles.
- Fillets: none (the spec names none); the ladder was not used.
- Placements in the assembly, unchanged from v01:
  - OD-C01 and OD-C02: RigidJoint at the identity.
  - OD-C03 and OD-H01: RigidJoint at `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`, read back as position (0, 40, −205), orientation (0, 90, 180).

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The panel stands upright on the plate's top face along the rear edge, on its 3 mm foot and two 22-deep flanges. It prints flat on its outer face. It rests and mounts the way it is used. |
| P2 | Function chains | All three chains are open. Cord through (95, 30) and tubes through (−100, 30) and (−84, 30): each hole is through with nothing behind it, the nearest gusset 2.0 to 3.4 away (sections x 100.5, x −101, y 30). The vents sit behind the bay. Driver to each flange screw from y 260: clear. |
| P3 | Motion clearance | No moving parts. The panel lowers along −Y onto the plate clear of every neighbour at all 21 poses (U-03 (b)). |
| P4 | Human factors | A straight Ø6 driver reaches all four flange screws from above with the top panel off (REQ-08). The tube holes leave 2.0 to the gussets behind the wall: enough for a silicone tube that passes straight through, tight for a grommet with a rear flange (A-04). |
| P5 | Next to a real product | An ordinary appliance back panel: a flat wall, a top ledge with two inserts, floor tabs with gussets, three grommet holes low on the sides, a vent grille behind the board. The v02 notches are gone. |
| P6 | Floating, embedded, mirrored, upside-down | Nothing floats (one solid) and nothing is embedded in a placed neighbour (common volume 0). The flanges stay off the feet holes (0.000 mm² over holes). The wall's foot passes 2.3 from their rims (section x 110, assembly), which spec 1.2 accepts at ≥ 2.0. |

## 7. Library and tools used

- Card: UNO10 U5 tank heat-set (size and position gated apart), as in v01. No precedent files were read in v03.
- `tools.core`: `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`.
- `tools.measure`: `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, `min_wall_wide` (spacing 0.7), `overhang_census` (build +Z, spacing 0.7), `flat_ceiling_spans` (spacing 0.7), `radial_extent`, `clearance`, `mass_properties`, `mesh_census`.
- `tools.result.gate`; `tools.drawing.write_sections`.
- Job code in `01_CAD/`, never in the repo:
  - the U-03 hole-rim distance, now per region (the footprint face clipped at the measured inner face);
  - the pass-through gap fact (check facts and probe).
- No `tools/measure` function was missing.

## 8. Deviations from the plan

1. The only geometry change is spec 1.2's: the outer gussets' wall leg is 18.0. `gusset_leg_wall` became a pair matched to `gusset_x0`.
2. The behind-wall fact inside the check uses the nominal hole diameter and the nominal inner face z −299. Two sweep runs show its limits:
   - At wall_z +0.1 it reads 0.000 clearance, because its cylinder starts 0.1 inside the moved wall. This is an artefact of the fact, not a defect.
   - At pass_d 12.1 it reads the nominal 2.000.
   - `01_CAD/probe/probe_passthrough_gap_v03.json` measures each hole as built (measured diameter and end) for every run. It reads 1.950 at pass_d high, 2.000 at both wall_z ends, and 0.000 mm³ common volume everywhere. Neither number is a §5 threshold.
3. Three sections were added (brief WP-04): x 100.5 (cord hole and +X outer gusset), x −101 (tube hole −100 and −X outer gusset), and y 30 through (−80, 30) (tube hole −84 and the −X inner gusset; the same plane as the y 30 pass-through cut).

## 9. What I am least sure of

1. **The tube holes' 2.0 gap behind the wall.** The −100 tube hole clears the −X outer gusset's top by 2.000, and the −84 hole clears the −X inner gusset's face by 2.000 (1.950 at pass_d 12.1). That meets spec 1.2's words, but a grommet or bulkhead fitting with a rear flange wider than about Ø16 would sit on a gusset. A-04 (tube and grommet sizes) is still open.
2. **The wall foot's U-03 margin is thin: +0.300 at nominal and +0.200 at wall_z +0.1.** It depends on the feet holes staying Ø3.4 at (±110, −295). If the OD-C01 revision that adds the A-01 inserts also enlarges or moves the feet holes, this row has to be re-measured.
3. **How the region split reads the footprint.** U-03's distance is split at the wall's inner face as measured (z −299.000). A reviewer who splits at the flange/gusset outline instead would get the same numbers here, because the flanges start at x ±72 / ±104 and the feet holes lie outside them. But the split is job code, not a `tools/measure` function.

## 10. Stop

Not stopped. Spec 1.2 answered both v02 stops: no gate fails at nominal or at any sweep limit, and no fix cycle was used (0 of 3).

## 11. JSON block

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20261001-od-c11-back-panel",
 "part": "od_c11_back",
 "tag": "v03",
 "spec_version": "1.2",
 "outcome": "SUBMITTED",
 "fix_cycles": "0 of 3",
 "files": [
  {
   "path": "01_CAD/DESIGN_PLAN_v03.md",
   "sha256": "0793968205d092999f56d7b88d9b6e1cec99968e986cfd0af8c312dab1f41d3a"
  },
  {
   "path": "01_CAD/build_od_c11_back_v03.py",
   "sha256": "8b86b5bf0fad6f13c5966115b0e907b14076c1d06e3632eda9581778fd1f8d9c"
  },
  {
   "path": "01_CAD/build_record_v03.json",
   "sha256": "35f9273ecffa33c0e0362e85eb7de0a5c358c84f33ac7bf82ec5aaee9c9bcc71"
  },
  {
   "path": "01_CAD/check_od_c11_back_v03.json",
   "sha256": "ec5a36c5dae443d29c2c41e2a9e2f393e7dbb36b03e4e4eb9707d6cabd06262e"
  },
  {
   "path": "01_CAD/check_od_c11_back_v03.log",
   "sha256": "14a4876a8bf41b7791d7cbd419bcdb25e86e0dcf65cf564ca3494c54822cbf95"
  },
  {
   "path": "01_CAD/check_od_c11_back_v03.py",
   "sha256": "1d8d5de5a15529d2b522e65594d07b34f6972a66b629578860236401f3b1ae7e"
  },
  {
   "path": "01_CAD/probe/probe_passthrough_gap_v03.json",
   "sha256": "e39719e8eb403fcd6541edccf946f896057c167640f9bc198aa8204d3089509a"
  },
  {
   "path": "01_CAD/probe/probe_passthrough_gap_v03.py",
   "sha256": "d3dd813df2ac0108d8175f7493397b7f52d3ca0c2e39840a5660a423ff7226a8"
  },
  {
   "path": "01_CAD/report_block_v03.py",
   "sha256": "cd5c794294542376e4b812c33bfa7d0c8dcac21ac25a45d15d32ac895f9f10cd"
  },
  {
   "path": "01_CAD/sections_od_c11_back_v03.py",
   "sha256": "9aab0771f6519db9f29bee28550c196f7df90899923fa56c25f66cc37fe99e32"
  },
  {
   "path": "01_CAD/sections_v03.json",
   "sha256": "f21464764209634591af3a45211679c440254ff27e12aaef6b676749e6c7f96f"
  },
  {
   "path": "01_CAD/sweep_od_c11_back_v03.sh",
   "sha256": "c55ad76b094d5364980d2c498224b6787202fa3b1a16ed0243833eacca7f1f7a"
  },
  {
   "path": "01_CAD/sweep_summary_v03.py",
   "sha256": "afbcf4cac25930630470174a1e01c99d997aaaf63d670fd1f9f06a9374e291bb"
  },
  {
   "path": "01_CAD/sweep_v03/sweep_summary.json",
   "sha256": "e27c239d60f330e4bead1a86025bc90699b9ac1fcc9618504d08b195eb7feb50"
  },
  {
   "path": "01_CAD/sweep_v03_driver.log",
   "sha256": "e41b854b4893e37599840a9e7ea3bbc03a07fbd45c46767c16f9b02bafec1b14"
  },
  {
   "path": "02_STEP_STL/od_c11_assembly_C1_v03.step",
   "sha256": "900c822e2b05cf5d3d67d8ca7874900a845713c9be2d70628e9ad26be95bed73"
  },
  {
   "path": "02_STEP_STL/od_c11_back_C1_v03.step",
   "sha256": "8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db"
  },
  {
   "path": "02_STEP_STL/od_c11_back_C1_v03.stl",
   "sha256": "8fa761335a2bb2aaf5bb75e388c8151f75131bc5b652e19c3f7144625965f96a"
  },
  {
   "path": "03_Sections/od_c11_assembly_feethole_x110_v03_left.png",
   "sha256": "c0fb9a23a60defc7b7395c3fd4e0e98795e5f3ab33028bcdb83e9c789971e384"
  },
  {
   "path": "03_Sections/od_c11_back_bosses_y207_v03_front.png",
   "sha256": "b0b2dd144b8302a5675f1eb334e5148fd62370c567b8ef323871ea0995ca06c8"
  },
  {
   "path": "03_Sections/od_c11_back_cord_gusset_x100p5_v03_left.png",
   "sha256": "7c9f8855208eef808b1e0b350ee2cc29bff32ec780b1e0a67bd76fbd95ca97ad"
  },
  {
   "path": "03_Sections/od_c11_back_flanges_y2_v03_front.png",
   "sha256": "564d5c93d753ec1394d3350de058f5f39cdc56a1ff1b3c8c60c5193a28c2062a"
  },
  {
   "path": "03_Sections/od_c11_back_gusset_x102_v03_left.png",
   "sha256": "ae9999df6729761a0fe603f39d3218cbc155dd679e90a64fc1492fc71e6b422c"
  },
  {
   "path": "03_Sections/od_c11_back_gusset_x74_v03_left.png",
   "sha256": "f3a435b0cabe0bc1f1fb8d7de24688d765231057e3a1eaf8546340ce797b3118"
  },
  {
   "path": "03_Sections/od_c11_back_gusset_xm102_v03_left.png",
   "sha256": "116c513c9b80b073135fbd32fac97f87d7cf43c60558cd1ec55fff4d9a035c24"
  },
  {
   "path": "03_Sections/od_c11_back_gussets_z290_v03_top.png",
   "sha256": "9d1d4a68c51ba6e152e3b4072afe59959d70d3132ff43fe9b180e18b13b083a2"
  },
  {
   "path": "03_Sections/od_c11_back_hole_x81_v03_left.png",
   "sha256": "d7d07411d0ad9e5324d42a3d7a150c8d568f5efff9fe7c5f782af23054a9c1e4"
  },
  {
   "path": "03_Sections/od_c11_back_hole_x95_v03_left.png",
   "sha256": "e3894fc29ca85c98dbea598fadf2bfdf1932cd9283c728e6e77381748f1b0e5e"
  },
  {
   "path": "03_Sections/od_c11_back_insert_x90_v03_left.png",
   "sha256": "da9956c89bfe9514d29e7a79bbf3c7955624ffa8b43702859bc04d0532d40df2"
  },
  {
   "path": "03_Sections/od_c11_back_ledge_y213_v03_front.png",
   "sha256": "39fe83b4a238a84e94526b8ab6a9c12e542e73d4e0a4daeb17b0e7eefa6bd49a"
  },
  {
   "path": "03_Sections/od_c11_back_passthroughs_y30_v03_front.png",
   "sha256": "a0972fabb7c90b7b0f17374aa54f00fb145a806f0f3c1e3bf57f4b0bb5d695e2"
  },
  {
   "path": "03_Sections/od_c11_back_tube84_gusset_y30_v03_front.png",
   "sha256": "c775b1db031a86431e0feebb556027e2500f16ca73faf62245c1cf724e1986b7"
  },
  {
   "path": "03_Sections/od_c11_back_tube_gusset_xm101_v03_left.png",
   "sha256": "1e6a293cae03a0247df044b1f5e68bc4b7a80b80269c7aaf666969448d562b35"
  },
  {
   "path": "03_Sections/od_c11_back_tube_xm100_v03_left.png",
   "sha256": "21e540cab636f72762df812b49fc0ddb56f3022b3c537a8801f32af3ea3c4a7b"
  },
  {
   "path": "03_Sections/od_c11_back_vents_y140_v03_front.png",
   "sha256": "2d5418bed790b2e4ff886a2ca8af368f784ce31ede60cab830c3a678c75617b6"
  },
  {
   "path": "03_Sections/od_c11_back_wall_y200_v03_front.png",
   "sha256": "1323787de713cb383a1d434037f39d0c9210976b7e8131ad688ac41ce9eac640"
  },
  {
   "path": "03_Sections/od_c11_back_wall_y50_v03_front.png",
   "sha256": "6fa671a10f129afbb2a8ce865e488b811210d97f22d1b9d7cbf8c05aa934693d"
  },
  {
   "path": "03_Sections/od_c11_back_wall_z300p5_v03_top.png",
   "sha256": "23577b424f81c5abeedb54777301b2e409aa71cc4a2bfc86df2eaaff150a6a8e"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "cadquery-ocp-novtk 7.9.3.1.1",
  "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"
 },
 "gates": [
  {
   "gate": "U-01",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "U-01.solid_count",
   "rows": 3
  },
  {
   "gate": "U-02",
   "measured": 232.0,
   "unit": "mm",
   "required": "in [231.9, 232.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "U-02.size_x",
   "rows": 3
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(116.0000, 0.0000, -302.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02",
    "A-07"
   ],
   "worst_row": "U-03.plate.clearance",
   "rows": 25
  },
  {
   "gate": "U-04",
   "measured": 4.307366907596588e-09,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -4e-09,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "U-04.assembly.od_h01_pump.volume_delta",
   "rows": 16
  },
  {
   "gate": "U-05",
   "measured": 46,
   "unit": "count",
   "required": "== 46",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "U-05.plane_faces",
   "rows": 20
  },
  {
   "gate": "U-06",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 1.0,
   "at": "(76.0000, 34.0000, -302.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "U-06(Soft)",
   "rows": 1
  },
  {
   "gate": "U-07",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "U-07.mesh.bodies",
   "rows": 6
  },
  {
   "gate": "U-08",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": [],
   "worst_row": "U-08",
   "rows": 1
  },
  {
   "gate": "D-01a",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 2.2,
   "at": "(116.0000, 0.0000, -299.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "D-01a",
   "rows": 1
  },
  {
   "gate": "D-01b",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": 1.0,
   "at": "(116.0000, 0.0000, -299.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "D-01b",
   "rows": 1
  },
  {
   "gate": "D-02",
   "measured": 232.0,
   "unit": "mm",
   "required": "<= 420.0",
   "margin": 188.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ],
   "worst_row": "D-02.size_x",
   "rows": 3
  },
  {
   "gate": "D-03a",
   "measured": 90.0,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": 45.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ],
   "worst_row": "D-03a",
   "rows": 1
  },
  {
   "gate": "D-03b",
   "measured": 4.0,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ],
   "worst_row": "D-03b.widest_insert_bore",
   "rows": 3
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(81.0000, 0.0000, -282.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "D-04a.x81_z-282.diameter",
   "rows": 4
  },
  {
   "gate": "D-05a",
   "measured": 12.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.0,
   "at": "[(96.0, 210.0, -293.0), (84.0, 210.0, -293.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ],
   "worst_row": "D-05a.x90_z-293.across_x",
   "rows": 4
  },
  {
   "gate": "D-05b",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(90.0000, 209.0000, -293.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ],
   "worst_row": "D-05b.x90_z-293.diameter",
   "rows": 6
  },
  {
   "gate": "D-06a",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 2.0,
   "at": "(116.0000, 0.0000, -299.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "D-06a",
   "rows": 1
  },
  {
   "gate": "D-07",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": [],
   "worst_row": "D-07",
   "rows": 1
  },
  {
   "gate": "J-05",
   "measured": 4.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 1.0,
   "at": "(96.0000, 210.0000, -293.0000) mm",
   "status": "PASS",
   "assumes": [],
   "worst_row": "J-05.x90_z-293.+x",
   "rows": 8
  },
  {
   "gate": "E-06",
   "measured": null,
   "unit": "",
   "required": "reviewer",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [],
   "worst_row": "E-06",
   "rows": 1
  },
  {
   "gate": "E-11",
   "measured": null,
   "unit": "",
   "required": "reviewer",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-03",
    "A-06"
   ],
   "worst_row": "E-11",
   "rows": 1
  },
  {
   "gate": "REQ-01",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ],
   "worst_row": "REQ-01.underside_faces",
   "rows": 22
  },
  {
   "gate": "REQ-02",
   "measured": -116.0,
   "unit": "mm",
   "required": "in [-116.1, -115.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ],
   "worst_row": "REQ-02.min_x",
   "rows": 14
  },
  {
   "gate": "REQ-03",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(95.0000, 30.0000, -302.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ],
   "worst_row": "REQ-03.x95_y30.through",
   "rows": 3
  },
  {
   "gate": "REQ-04",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(-100.0000, 30.0000, -302.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04"
   ],
   "worst_row": "REQ-04.x-100_y30.through",
   "rows": 6
  },
  {
   "gate": "REQ-05",
   "measured": -277.0,
   "unit": "mm",
   "required": "<= -277.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ],
   "worst_row": "REQ-05.max_z",
   "rows": 2
  },
  {
   "gate": "REQ-06",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "[(80.0, 140.0, -300.5), (76.0, 140.0, -300.5)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ],
   "worst_row": "REQ-06.x78.width",
   "rows": 25
  },
  {
   "gate": "REQ-07",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-05"
   ],
   "worst_row": "REQ-07.top_faces",
   "rows": 12
  },
  {
   "gate": "REQ-08",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "REQ-08.x81_z-282",
   "rows": 4
  },
  {
   "gate": "REQ-09",
   "measured": null,
   "unit": "",
   "required": "bench",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-11"
   ],
   "worst_row": "REQ-09(Soft)",
   "rows": 1
  },
  {
   "gate": "exactly_one_solid",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "exactly_one_solid",
   "rows": 1
  },
  {
   "gate": "feature_census",
   "measured": 46,
   "unit": "count",
   "required": "== 46",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "feature_census.plane_faces",
   "rows": 17
  },
  {
   "gate": "envelope_within_spec",
   "measured": 232.0,
   "unit": "mm",
   "required": "in [231.9, 232.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": [],
   "worst_row": "envelope_within_spec.size_x",
   "rows": 9
  }
 ],
 "sweep": [
  {
   "parameter": "flange_hole_d",
   "runs": [
    "flange_hole_d_lo",
    "nominal",
    "flange_hole_d_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "REQ-05.max_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "flange_hole_dx",
   "runs": [
    "flange_hole_dx_lo",
    "nominal",
    "flange_hole_dx_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "REQ-05.max_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_d",
   "runs": [
    "insert_d_lo",
    "nominal",
    "insert_d_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "REQ-05.max_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_depth",
   "runs": [
    "insert_depth_lo",
    "nominal",
    "insert_depth_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "REQ-05.max_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "pass_d",
   "runs": [
    "pass_d_lo",
    "nominal",
    "pass_d_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "REQ-05.max_z",
   "worst_margin": 0.0
  },
  {
   "parameter": "wall_z",
   "runs": [
    "wall_z_lo",
    "nominal",
    "wall_z_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "U-02.size_z",
   "worst_margin": -2.1316282072803006e-14
  },
  {
   "parameter": "y_top",
   "runs": [
    "y_top_lo",
    "nominal",
    "y_top_hi"
   ],
   "all_built_one_solid": true,
   "not_pass": [],
   "worst_gate": "U-02.size_y",
   "worst_margin": 0.0
  }
 ],
 "least_sure": [
  "tube holes clear the -X gussets by 2.000 behind the wall (1.950 at pass_d 12.1): a grommet with a rear flange wider than about 16 would sit on a gusset (A-04 open)",
  "U-03 wall foot to the feet-hole rims 2.300 (+0.300; +0.200 at wall_z +0.1): depends on OD-C01's feet holes staying 3.4 at (+-110, -295)",
  "U-03 region split at the measured inner face is job code, not a tools/measure function"
 ],
 "stopped": false
}
```
