# DESIGN_PLAN v03 amendment — od_c11_back (20261001-od-c11-back-panel, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.2 (SHA-256 6da33456…a61245) · brief WP-04, build attempt 3 of 3, fix_cycles 3 · amends `01_CAD/DESIGN_PLAN.md` (v01) as amended by `01_CAD/DESIGN_PLAN_v02.md`. Every section not named below stands as written there.

## 1. Datum

Unchanged.

## 2. Library and tools

Unchanged: same card, same `tools/` functions. The U-03 (a) hole-rim job code from v02 is split in two by spec 1.2:
- The single footprint face (REQ-01 keeps it one plane) is clipped by position at the wall's inner face.
- That plane is the z measured by the REQ-02 ray at y 50, x 0, so the split follows the wall in the sweep.
- The part at z ≤ that plane is the wall's foot, gated at ≥ 2.0.
- The part at z ≥ that plane is the flanges, gated at ≥ 3.0.
- Each value is the distance from the hole's centre to the region, minus the hole's radius.

One new fact beside E-11 (not a gate): for each pass-through, a Ø12 cylinder on its axis from z −299 to −277. The check reports its common volume with the panel and its clearance to the panel's material in front of the wall. No `tools/measure` function is missing.

## 3. Feature order (changes only)

| F## | v02 | v03 (spec 1.2 §4) |
|---|---|---|
| F03 | four gussets, wall leg 30.0 | inner gussets x ±(72 … 76): wall leg 30.0 (top y 34). Outer gussets x ±(100 … 104): wall leg 18.0 (top y 22, 2.0 below the pass-throughs' bottoms at y 24). Flange leg 16.0 for all four |

The v01 cutter premise holds again: the F08 cutters (z −303 … −298) meet no fused feature. The outer gussets end at y 22 and the holes start at y 24. The inner gussets lie at |x| 72 … 76, and the nearest hole edge is at |x| 78 (the −84 tube hole).

Expected census (v01 derivation, valid again): planar 46, cylindrical 19 (concave 19), bores 9, refilled solid 57 faces.

## 4. Parameters (changes only)

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| gusset_leg_wall | (30.0, 18.0), paired with gusset_x0 (72.0, 100.0) | mm | — | §4 (1.2), E-06 | no (the gap to the holes is swept through pass_d and wall_z) |

## 5. Placements

Unchanged joints. The check assembly is `02_STEP_STL/od_c11_assembly_C1_v03.step`.

## 6. Checks planned (changes only)

| Gate | v03 predicate |
|---|---|
| U-03 (a) hole rim | `U-03.wall_foot_to_plate_hole_rim` ≥ 2.0; `U-03.flanges_to_plate_hole_rim` ≥ 3.0 (replaces v02's single ≥ 3.0 row) |
| U-05 / feature_census | v01 counts: planar 46, cylindrical 19, bores 9, Ø12 along Z through 3 |
| D-03a | refilled solid 57 faces, then `overhang_census(build_dir=(0,0,1))` outside the named exception |

Sections (D6): the v02 cuts plus one through each pass-through and its nearest gusset:
- x 100.5 (left view): the cord hole and the +X outer gusset.
- x −101 (left view): the −100 tube hole and the −X outer gusset.
- y 30 (front view): the −84 tube hole and the −X inner gusset, 2.0 apart in X.

Sweep (D7): the same 15 runs into `01_CAD/sweep_v03/`.

## 7. Risks (v03)

- At pass_d 12.1, the holes' bottoms move to y 23.95: 1.95 above the outer gussets' tops. At wall_z +0.1 the gussets move with the wall. Neither changes the gap in Y.
- The wall's foot reads 2.300 to the feet-hole rims at nominal and 2.200 at wall_z +0.1 (v02 sweep). That is above the new 2.0, with a margin of +0.2 at the tolerance limit.
