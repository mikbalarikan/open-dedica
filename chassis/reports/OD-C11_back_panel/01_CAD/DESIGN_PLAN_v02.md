# DESIGN_PLAN v02 amendment — od_c11_back (20261001-od-c11-back-panel, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.1 (SHA-256 c4369d16…a117d2) · brief WP-03, build attempt 2 of 2, fix_cycles 3 · amends `01_CAD/DESIGN_PLAN.md` (v01). Every section not named below stands as written in v01.

## 1. Datum

Unchanged.

## 2. Library and tools

Unchanged: same card, same `tools/` functions. One new piece of job code in the check script: the U-03 (a) clause added by spec 1.1, "≥ 3.0 from the edge of every existing OD-C01 hole". For every plate bore along Y (`bore_census` on the placed plate), it computes the distance in the plane y = 0 from the hole's centre to the panel's footprint faces, minus the hole's radius. A negative value means the rim reaches into the footprint. No `tools/measure` function is missing.

## 3. Feature order (changes only)

| F## | v01 | v02 (spec 1.1 §4) |
|---|---|---|
| F02 | flanges x ±(72.0 … 114.0), z −299.0 … −283.0 | flanges x ±(72.0 … 104.0), z −299.0 … −277.0 (22 deep) |
| F03 | gussets at x ±(72 … 76) and ±(110 … 114); flange leg = the flange's depth | gussets at x ±(72 … 76) and ±(100 … 104); the flange leg is its own parameter, 16.0 from the wall's inner face (vertices (y 4, z −299), (y 4, z −283), (y 34, z −299)), so it no longer equals the 22-deep flange |
| F06 | holes at (±81, −290), (±100, −290) | holes at (±81.0, −282.0), (±95.0, −282.0) |

The v01 order note said: "the cutters of F08 and F09 stop at z −298.0, which is clear of every fused feature at those (x, y)". **That premise fails under spec 1.1.** The outer gussets at x ±(100 … 104), y 4 … 34 now lie behind two pass-throughs. The tube hole Ø12 at (−100, 30) spans x −106 … −94, y 24 … 36, and its axis lies on the −X gusset's inner face. The cord hole at (95, 30) reaches x 101, 1.0 into the +X gusset. The build keeps the plan's cutter (overshoot 1.0) and the spec's gussets, and reports what it measures (REPORT §10).

Expected census (unchanged derivation): planar 46, cylindrical 19, bores 9, refilled solid 57 faces. These hold only while the pass-throughs clear the gussets; under spec 1.1 they do not.

## 4. Parameters (changes only)

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| flange_x | 72.0 / 104.0 (both sides) | mm | — | §4 (1.1), REQ-05, A-07 | no |
| flange_z1 | −277.0 | mm | ±0.1 | §4 (1.1), REQ-05, U-02 | no |
| gusset_x0 | ±72.0, ±100.0 (each 4.0 along +X from x0, mirrored) | mm | — | §4 (1.1) | no |
| gusset_leg_flange | 16.0, from the wall's inner face | mm | — | §4, E-06 (derivation: a separate parameter now that the flange is 22 deep; it is measured from the wall face so the gusset moves with the wall in the sweep) | no |
| flange_hole_xz | (±81.0, −282.0), (±95.0, −282.0) | mm | offset ≤ 0.10 | REQ-01 (1.1), A-01 | yes |

## 5. Placements

Unchanged joints. The check assembly is `02_STEP_STL/od_c11_assembly_C1_v02.step`.

## 6. Checks planned (changes only)

| Gate | v02 predicate |
|---|---|
| U-02 / envelope_within_spec | sizes 232.0 × 215.0 × 25.0 (±0.1); position z −302.0 … −277.0 |
| U-03 (a) | as v01, plus: the least distance from the rim of every OD-C01 hole along Y to the footprint ≥ 3.0 (job code, §2 above) |
| REQ-01, D-04a, REQ-08, U-03 under each hole | at (±81.0, −282.0), (±95.0, −282.0) |
| REQ-05 | max_z ≤ −277.0; the box x ±70, y 0 … 100, z −298.8 … −250 |
| REQ-08 | Ø6 cylinders y 4 … 260 on the four axes, common volume = 0 (the v01 tilted-driver fact is dropped) |
| D-03a region | the flange-hole crowns are named at z −282, x ±81 / ±95 |
| D-02 | 25.0 tall |

Sweep (D7): the same 15 runs into `01_CAD/sweep_v02/`. The wall-plane run at ±0.1 is read against REQ-05's new box.

## 7. Risks (v02)

- U-03 (a)'s new clause also reads on the wall's foot. The foot's inner edge (z −299) is 4.0 from the feet-hole centres (±110, −295), so 2.3 from their Ø3.4 rim, below 3.0. The wall's plane is a spec §4 value (A-02), so this is measured and reported, not changed.
- The outer gussets overlap the tube and cord pass-throughs (§3 above).
