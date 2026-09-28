# OD-E01_Power-PCB — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 2 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — fresh agent; see independence  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner), 2026-09-28, record `decisions/accept_band_it2.md`).

## 1. The part

![reference photo](../input/photos/1.png)

Populated appliance power PCB (board id PCB00572-01): board, heatsink with a TO-220 and spring clip, electrolytic and film capacitors, faston tabs, connectors and SMD parts, delivered as ONE fused envelope solid of the component side for enclosure / fit design.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-E01_Power-PCB_datum.step` | datum | 1 | yes | yes | 1233 | 20609.8947 | max: [95.002, 3.869, 25.262]; min: [-5.162, -56, -1.562]; size: [100.164, 59.869, 26.824] |
| `build/OD-E01_Power-PCB.step` | scan | 1 | yes | yes | 1233 | 20609.8947 | max: [63.2131, 28.0764, -160.7284]; min: [-8.5579, -82.5441, -248.1771]; size: [71.771, 110.6205, 87.4488] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: full-resolution scan hashed, noise floors measured, datum = PCB top face (z 0, +Z out of the component side), mounting hole H1 axis as origin, +X along the long board edge (clock on the +X short edge).
2. Measure: seeded height map plus per-part fits on the frozen datum-frame scan (run-local measure/measure_pcb.py): edge-line fits for the board, bore-wall circle fits for holes, side-wall faces for tall boxes, per-z-bin circle fits for the leaning cans, profile fits for the heatsink, SDF fit for the Y-capacitor; every value in measure/params.json with its estimator.
3. Rebuild: params-driven build123d model (build/model.py): board plate with slot and holes, one extruded heatsink profile, cans revolved on their measured axes, boxes and wires for the rest, one union; exported in the datum frame and the scan frame.
4. Verify: independent fresh-context QA with its own ICP and two-way deviation on the full-resolution scan; iteration 1 REVISE (five geometry findings), iteration 2 BAND_NOT_MET, accepted by the owner for delivery (decisions/accept_band_it2.md).

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | mounting hole H1 axis ∩ PCB top face | — | — |
| primary (plane) | PCB top face (component side, solder mask) | 0.0342 / 0.1101 | the board top is the seating plane of every component and the reference an enclosure / mating part locates the PCB on |
| secondary (axis) | mounting hole H1 wall faces (corner hole, wall fully scanned) | 0.0165 / 0.1069 | mounting holes locate the PCB in the enclosure |
| clock | plane_normal: PCB short edge on the far side from H1 (edge face outward normal) -> +X (angle 121.954°) | — | — |

Measured tilt: 1.0338° (common slope, per-feature intercept, 4 stations over 1 feature(s), z -1.320..-0.540 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0344 mm (rms of RANSAC+SVD plane on PCB top face (solder-mask side) (76252 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.517796  -0.758912  -0.394892  -41.147142
 0.234411  -0.569784   0.787654   112.511507
-0.822763   0.315277   0.472929   128.868106
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: assumed 1, scan 173, standard 3 (total 177). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `ax_D1` | [67.837, 1.639, 1.294, -11.6, -5.8, 67.75, -3.4, 1.757, 67.85, -13.7, 2.076] | mm | [67.837, 1.639, 1.294, -11.6, -5.8, 67.75, -3.4, 1.757, 67.85, -13.7, 2.076] | keep-measured | scan | 0.197 | no | measure/figures/pcb_measure.json#axial_D1 |
| `ax_D2` | [70.632, 1.419, 1.348, -11.6, -5.8, 70.65, -3.1, 1.716, 70.85, -14.5, 1.782] | mm | [70.632, 1.419, 1.348, -11.6, -5.8, 70.65, -3.1, 1.716, 70.85, -14.5, 1.782] | keep-measured | scan | 0.189 | no | measure/figures/pcb_measure.json#axial_D2 |
| `ax_L2` | [79.112, 1.769, 1.507, -24.6, -16.8, 79.15, -12.2, 2.412] | mm | [79.112, 1.769, 1.507, -24.6, -16.8, 79.15, -12.2, 2.412] | keep-measured | scan | 0.175 | no | measure/figures/pcb_measure.json#axial_L2 |
| `ax_R1` | [68.504, 6.367, 2.112, -39.6, -27.2, 68.95, -22.2, 7.017, 68.65, -44.9, 6.87] | mm | [68.504, 6.367, 2.112, -39.6, -27.2, 68.95, -22.2, 7.017, 68.65, -44.9, 6.87] | keep-measured | scan | 0.135 | no | measure/figures/pcb_measure.json#resistor_R1 |
| `axlead_D1_1` | [67.859, -3.866, 0.2, 67.838, -4.191, 0.6] | mm | [67.859, -3.866, 0.2, 67.838, -4.191, 0.6] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#axial_D1.leads |
| `axlead_D1_2` | [67.744, -13.409, 0.2, 67.581, -13.379, 1] | mm | [67.744, -13.409, 0.2, 67.581, -13.379, 1] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#axial_D1.leads |
| `axlead_D2_1` | [70.731, -3.598, 0.2, 70.799, -3.601, 0.6] | mm | [70.731, -3.598, 0.2, 70.799, -3.601, 0.6] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#axial_D2.leads |
| `axlead_D2_2` | [70.49, -12.923, 0.2, 70.666, -13.321, 0.6] | mm | [70.49, -12.923, 0.2, 70.666, -13.321, 0.6] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#axial_D2.leads |
| `axlead_L2_1` | [79.485, -13.257, 0.2, 79.332, -12.786, 0.6, 79.469, -12.877, 1.4] | mm | [79.485, -13.257, 0.2, 79.332, -12.786, 0.6, 79.469, -12.877, 1.4] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#axial_L2.leads |
| `axlead_R1_1` | [69.459, -23.969, 0.2, 69.609, -23.797, 0.6, 69.501, -24.079, 1.4, 69.467, -23.939, 1.8, 69.356, -23.556, 2.2, 69.432, -23.023, 3, 69.262, -22.934, 3.4, 69.468, -22.399, 4.6, 69.084, -22.981, 5.8] | mm | [69.459, -23.969, 0.2, 69.609, -23.797, 0.6, 69.501, -24.079, 1.4, 69.467, -23.939, 1.8, 69.356, -23.556, 2.2, 69.432, -23.023, 3, 69.262, -22.934, 3.4, 69.468, -22.399, 4.6, 69.084, -22.981, 5.8] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#resistor_R1.leads |
| `axlead_R1_2` | [69.879, -43.242, 0.2, 69.695, -42.974, 1.4, 69.706, -43.407, 2.2, 69.13, -43.918, 3, 69.062, -44.584, 3.8, 68.548, -44.255, 5.8] | mm | [69.879, -43.242, 0.2, 69.695, -42.974, 1.4, 69.706, -43.407, 2.2, 69.13, -43.918, 3, 69.062, -44.584, 3.8, 68.548, -44.255, 5.8] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#resistor_R1.leads |
| `blk_K1` | [5.703, 12.51, -54.752, -47.285, 2.875, 5.6, 6.917, 7.831, -53.6, -48.6, 9.537] | mm | [5.703, 12.51, -54.752, -47.285, 2.875, 5.6, 6.917, 7.831, -53.6, -48.6, 9.537] | keep-measured | scan | 0.165 | no | measure/figures/pcb_measure.json#base_riser.K1 |
| `blk_K2` | [-3.822, 1.892, -34.047, -29.065, 3.21, -4, -2.387, -2.759, -32.7, -30, 11.735] | mm | [-3.822, 1.892, -34.047, -29.065, 3.21, -4, -2.387, -2.759, -32.7, -30, 11.735] | keep-measured | scan | 0.321 | no | measure/figures/pcb_measure.json#base_riser.K2 |
| `board_thickness` | 1.562 | mm | 1.562 | keep-measured | scan | 0.1 | yes | measure/figures/pcb_measure.json#board.wall_bottom_z_p50 |
| `board_x_max` | 95.002 | mm | 95.002 | keep-measured | scan | 0.06 | yes | measure/figures/pcb_measure.json#board.edges.x_max |
| `board_x_min` | -5.162 | mm | -5.162 | keep-measured | scan | 0.068 | yes | measure/figures/pcb_measure.json#board.edges.x_min |
| `board_y_max` | 3.869 | mm | 3.869 | keep-measured | scan | 0.094 | yes | measure/figures/pcb_measure.json#board.edges.y_max |
| `board_y_min` | -56 | mm | -56 | keep-measured | scan | 0.093 | yes | measure/figures/pcb_measure.json#board.edges.y_min |
| `box_001` | [3.7, 6.3, -23.5, -22, 0.457] | mm | [3.7, 6.3, -23.5, -22, 0.457] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_002` | [3.7, 6.3, -21.5, -20, 0.429] | mm | [3.7, 6.3, -21.5, -20, 0.429] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_003` | [3.9, 5.9, -46.1, -44.9, 0.49] | mm | [3.9, 5.9, -46.1, -44.9, 0.49] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_004` | [3.9, 6, -44.1, -42.9, 0.486] | mm | [3.9, 6, -44.1, -42.9, 0.486] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_005` | [3.9, 6.1, -41.7, -40.5, 0.471] | mm | [3.9, 6.1, -41.7, -40.5, 0.471] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_006` | [3.9, 6.1, -39.6, -38.6, 0.436] | mm | [3.9, 6.1, -39.6, -38.6, 0.436] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_007` | [3.9, 6, -34.5, -33.1, 0.747] | mm | [3.9, 6, -34.5, -33.1, 0.747] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_008` | [3.9, 6, -32.1, -31, 0.441] | mm | [3.9, 6, -32.1, -31, 0.441] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_009` | [3.9, 6, -30.3, -29.1, 0.404] | mm | [3.9, 6, -30.3, -29.1, 0.404] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_010` | [4, 5.9, -37.8, -36.8, 0.754] | mm | [4, 5.9, -37.8, -36.8, 0.754] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_011` | [4, 6, -19.2, -18.2, 0.356] | mm | [4, 6, -19.2, -18.2, 0.356] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_012` | [9, 9.5, -45.7, -45.1, 0.214] | mm | [9, 9.5, -45.7, -45.1, 0.214] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_013` | [10.9, 12.7, -46.1, -45, 0.751] | mm | [10.9, 12.7, -46.1, -45, 0.751] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_014` | [12.9, 15, -2.9, -2.1, 0.304] | mm | [12.9, 15, -2.9, -2.1, 0.304] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_015` | [12.9, 14.9, -1.1, 0.2, 0.305] | mm | [12.9, 14.9, -1.1, 0.2, 0.305] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_016` | [13.1, 14.9, 1, 2, 0.619] | mm | [13.1, 14.9, 1, 2, 0.619] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_017` | [13.9, 16, -54.4, -53.4, 0.462] | mm | [13.9, 16, -54.4, -53.4, 0.462] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_018` | [13.9, 16, -52.5, -51.5, 0.456] | mm | [13.9, 16, -52.5, -51.5, 0.456] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_019` | [14, 16, -50.7, -49.5, 0.465] | mm | [14, 16, -50.7, -49.5, 0.465] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_020` | [14, 16.1, -43.4, -42.4, 0.438] | mm | [14, 16.1, -43.4, -42.4, 0.438] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_021` | [14, 16.2, -41.5, -40.4, 0.449] | mm | [14, 16.2, -41.5, -40.4, 0.449] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_022` | [14, 16.2, -37.8, -36.8, 0.43] | mm | [14, 16.2, -37.8, -36.8, 0.43] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_023` | [14, 17.7, -31.3, -29.6, 0.522] | mm | [14, 17.7, -31.3, -29.6, 0.522] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_024` | [14, 17.7, -28.6, -27, 0.506] | mm | [14, 17.7, -28.6, -27, 0.506] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_025` | [14.1, 15.7, -49, -45.9, 1.012] | mm | [14.1, 15.7, -49, -45.9, 1.012] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_026` | [14.1, 16.1, -45.2, -44.1, 0.455] | mm | [14.1, 16.1, -45.2, -44.1, 0.455] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_027` | [14.1, 16.2, -39.6, -38.6, 0.446] | mm | [14.1, 16.2, -39.6, -38.6, 0.446] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_028` | [14.1, 16.1, -35.9, -35, 0.434] | mm | [14.1, 16.1, -35.9, -35, 0.434] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_029` | [16.895, 27.088, -9.469, -4.34, 1.777] | mm | [16.895, 27.088, -9.469, -4.34, 1.777] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_030` | [17.1, 19, -37.9, -36.8, 0.756] | mm | [17.1, 19, -37.9, -36.8, 0.756] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_031` | [17.2, 19, -54.4, -53.5, 0.768] | mm | [17.2, 19, -54.4, -53.5, 0.768] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_032` | [17.2, 19, -39.5, -38.6, 0.785] | mm | [17.2, 19, -39.5, -38.6, 0.785] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_033` | [17.2, 17.7, -33.6, -32.9, 0.19] | mm | [17.2, 17.7, -33.6, -32.9, 0.19] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_034` | [17.2, 20.7, -0.9, 0.9, 0.716] | mm | [17.2, 20.7, -0.9, 0.9, 0.716] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_035` | [17.4, 26.7, -10.5, -9.7, 1.038] | mm | [17.4, 26.7, -10.5, -9.7, 1.038] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_036` | [17.4, 26.6, -4.1, -3.4, 1.021] | mm | [17.4, 26.6, -4.1, -3.4, 1.021] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_037` | [18.5, 19.4, -14.7, -12.9, 0.741] | mm | [18.5, 19.4, -14.7, -12.9, 0.741] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_038` | [20.1, 21.1, -14.8, -12.7, 0.401] | mm | [20.1, 21.1, -14.8, -12.7, 0.401] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_039` | [20.2, 21.1, -18, -16, 0.409] | mm | [20.2, 21.1, -18, -16, 0.409] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_040` | [21.8, 23.2, -1.6, 0.9, 0.459] | mm | [21.8, 23.2, -1.6, 0.9, 0.459] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_041` | [21.9, 22.9, -14.7, -12.9, 0.706] | mm | [21.9, 22.9, -14.7, -12.9, 0.706] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_042` | [23.4, 26.5, -14.7, -13.1, 0.92] | mm | [23.4, 26.5, -14.7, -13.1, 0.92] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_043` | [23.7, 25.2, -1.6, 1, 0.449] | mm | [23.7, 25.2, -1.6, 1, 0.449] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_044` | [24.427, 30.681, -53.599, -47.684, 2.355] | mm | [24.427, 30.681, -53.599, -47.684, 2.355] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_045` | [24.7, 26.5, -47.5, -44.6, 1.567] | mm | [24.7, 26.5, -47.5, -44.6, 1.567] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_046` | [24.7, 26, -43.2, -40.7, 0.51] | mm | [24.7, 26, -43.2, -40.7, 0.51] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_047` | [24.8, 30.3, -54.8, -53.8, 0.601] | mm | [24.8, 30.3, -54.8, -53.8, 0.601] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_048` | [26.1, 27.2, -1.4, 0.7, 0.375] | mm | [26.1, 27.2, -1.4, 0.7, 0.375] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_049` | [26.9, 28.4, -47.5, -46.7, 1.606] | mm | [26.9, 28.4, -47.5, -46.7, 1.606] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_050` | [27.1, 29, -16, -12.3, 0.542] | mm | [27.1, 29, -16, -12.3, 0.542] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_051` | [27.3, 28.3, -42.9, -40.9, 0.457] | mm | [27.3, 28.3, -42.9, -40.9, 0.457] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_052` | [28, 29, -1.3, 0.6, 0.724] | mm | [28, 29, -1.3, 0.6, 0.724] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_053` | [28.8, 29.9, -22.1, -20, 0.436] | mm | [28.8, 29.9, -22.1, -20, 0.436] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_054` | [29.2, 30.7, -47.5, -44.7, 1.55] | mm | [29.2, 30.7, -47.5, -44.7, 1.55] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_055` | [29.2, 30.2, -42.9, -41, 0.745] | mm | [29.2, 30.2, -42.9, -41, 0.745] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_056` | [29.8, 30.8, -1.4, 0.7, 0.405] | mm | [29.8, 30.8, -1.4, 0.7, 0.405] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_057` | [32.5, 35.7, -20.6, -19, 0.954] | mm | [32.5, 35.7, -20.6, -19, 0.954] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_058` | [34.7, 38.4, -24, -22.3, 0.538] | mm | [34.7, 38.4, -24, -22.3, 0.538] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_059` | [36, 37.2, -20.6, -18.7, 0.748] | mm | [36, 37.2, -20.6, -18.7, 0.748] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_060` | [38, 39.1, -20.7, -18.6, 0.444] | mm | [38, 39.1, -20.7, -18.6, 0.444] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_061` | [64.6, 66.4, -41.8, -38.1, 0.532] | mm | [64.6, 66.4, -41.8, -38.1, 0.532] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_062` | [68.3, 70.2, -15.9, -15, 0.758] | mm | [68.3, 70.2, -15.9, -15, 0.758] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_063` | [72.5, 73.7, -3.5, -1.8, 0.738] | mm | [72.5, 73.7, -3.5, -1.8, 0.738] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_064` | [72.7, 74.8, -8.8, -7.7, 0.441] | mm | [72.7, 74.8, -8.8, -7.7, 0.441] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_065` | [74.9, 76.2, -7.4, 1.9, 1.934] | mm | [74.9, 76.2, -7.4, 1.9, 1.934] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_066` | [76.449, 82.612, -7.4, 2.153, 3.444] | mm | [76.449, 82.612, -7.4, 2.153, 3.444] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_067` | [82.8, 84, -2.4, 2.1, 1.897] | mm | [82.8, 84, -2.4, 2.1, 1.897] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_068` | [83.1, 84, -6.6, -5.7, 0.646] | mm | [83.1, 84, -6.6, -5.7, 0.646] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#auto_boxes |
| `box_bump_K2_1` | [-1.6, -0.9, -32.9, -32.2, 4.211] | mm | [-1.6, -0.9, -32.9, -32.2, 4.211] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#base_riser.K2.bumps |
| `box_bump_K2_2` | [-2.5, -2.1, -31, -30.1, 7.359] | mm | [-2.5, -2.1, -31, -30.1, 7.359] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#base_riser.K2.bumps |
| `box_side_D2_1` | [72.7, 74.3, -10.6, -9.5, 0.457] | mm | [72.7, 74.3, -10.6, -9.5, 0.457] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#axial_D2.side_parts |
| `box_side_D2_2` | [72.8, 74.3, -8.8, -7.8, 0.452] | mm | [72.8, 74.3, -8.8, -7.8, 0.452] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#axial_D2.side_parts |
| `box_side_R1_1` | [64.6, 66.1, -39.6, -38.1, 0.539] | mm | [64.6, 66.1, -39.6, -38.1, 0.539] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#resistor_R1.side_parts |
| `box_side_R1_2` | [64.6, 66.1, -36.7, -33, 0.558] | mm | [64.6, 66.1, -36.7, -33, 0.558] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#resistor_R1.side_parts |
| `box_side_R1_3` | [64.6, 66.1, -31.6, -27.8, 0.552] | mm | [64.6, 66.1, -31.6, -27.8, 0.552] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#resistor_R1.side_parts |
| `cap_C1` | [69.039, 0.297, 0.003, -0.049, 2.316, 1.5, 2.316, 2.5, 2.446, 5.423] | mm | [69.039, 0.297, 0.003, -0.049, 2.316, 1.5, 2.316, 2.5, 2.446, 5.423] | keep-measured | scan | 0.104 | no | measure/figures/pcb_measure.json#caps.C1.profile |
| `cap_C1_base` | [66.423, 71.515, -2.277, 2.896, 1.593] | mm | [66.423, 71.515, -2.277, 2.896, 1.593] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#caps.C1.base_plate |
| `cap_C2` | [74.179, -16.149, -0.048, -0.015, 3.147, 2.5, 2.975, 3.5, 3.235, 11.957] | mm | [74.179, -16.149, -0.048, -0.015, 3.147, 2.5, 2.975, 3.5, 3.235, 11.957] | keep-measured | scan | 0.071 | no | measure/figures/pcb_measure.json#caps.C2.profile |
| `cap_C3` | [86.065, -12.313, 0.009, -0.041, 5.042, 2.5, 4.755, 4.5, 5.089, 13.371] | mm | [86.065, -12.313, 0.009, -0.041, 5.042, 2.5, 4.755, 4.5, 5.089, 13.371] | keep-measured | scan | 0.084 | yes | measure/figures/pcb_measure.json#caps.C3.profile |
| `cap_C4` | [88.251, -22.392, -0.002, -0.053, 5.031, 2.5, 4.767, 4.5, 5.095, 13.392] | mm | [88.251, -22.392, -0.002, -0.053, 5.031, 2.5, 4.767, 4.5, 5.095, 13.392] | keep-measured | scan | 0.084 | yes | measure/figures/pcb_measure.json#caps.C4.profile |
| `cap_C5` | [89.407, -3.071, 0.034, -0.015, 3.85, 2.5, 3.405, 5.5, 3.906, 7.113] | mm | [89.407, -3.071, 0.034, -0.015, 3.85, 2.5, 3.405, 5.5, 3.906, 7.113] | keep-measured | scan | 0.254 | no | measure/figures/pcb_measure.json#caps.C5.profile |
| `capstem_C5` | [2.077, 1.2] | mm | [2.077, 1.2] | keep-measured | scan | 0.2 | no | measure/figures/pcb_measure.json#caps.C5.profile.standoff |
| `clip_hook` | [48.785, -37.886, 50.392, -38.162, 50.464, -37.103] | mm | [48.785, -37.886, 50.392, -38.162, 50.464, -37.103] | keep-measured | scan | 0.4 | no | measure/figures/pcb_measure.json#clip_S1_hook |
| `clip_path` | [49.55, -3.65, 48.75, -4.85, 47.95, -5.05, 47.15, -4.95, 46.55, -2.95, 45.45, -2.15, 40.45, -2.25, 39.65, -3.35, 41.15, -15.35, 41.55, -16.85, 42.15, -17.55, 42.55, -22.05, 42.15, -25.15, 41.45, -25.55, 40.75, -28.75, 39.55, -39.25, 40.65, -40.45, 45.75, -40.05, 46.35, -39.55, 46.55, -37.55, 47.25, -36.75, 47.15, -36.05] | mm | [49.55, -3.65, 48.75, -4.85, 47.95, -5.05, 47.15, -4.95, 46.55, -2.95, 45.45, -2.15, 40.45, -2.25, 39.65, -3.35, 41.15, -15.35, 41.55, -16.85, 42.15, -17.55, 42.55, -22.05, 42.15, -25.15, 41.45, -25.55, 40.75, -28.75, 39.55, -39.25, 40.65, -40.45, 45.75, -40.05, 46.35, -39.55, 46.55, -37.55, 47.25, -36.75, 47.15, -36.05] | keep-measured | scan | 0.25 | no | measure/figures/pcb_measure.json#clip_S1.path_vertices |
| `clip_width` | 0.8 | mm | 0.8 | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#clip_S1 |
| `clip_z` | [6.904, 13.342] | mm | [6.904, 13.342] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#clip_S1 |
| `conn_J1` | [7.217, 12.734, -39.147, -21.869, 6.819, 7.853, 12.08, -38.378, -22.558, 2.89] | mm | [7.217, 12.734, -39.147, -21.869, 6.819, 7.853, 12.08, -38.378, -22.558, 2.89] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1 |
| `conn_J2` | [-3.384, 2.195, -46.385, -36.618, 6.877, -2.774, 1.428, -45.35, -37.322, 3.324] | mm | [-3.384, 2.195, -46.385, -36.618, 6.877, -2.774, 1.428, -45.35, -37.322, 3.324] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J2 |
| `conn_J3` | [6.602, 11.489, -4.53, 2.711, 5.791, 7.348, 10.736, -3.969, 2.119, 1.86] | mm | [6.602, 11.489, -4.53, 2.711, 5.791, 7.348, 10.736, -3.969, 2.119, 1.86] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J3 |
| `connpin_J1_01` | [8, 8.5, -38.2, -35.6, 6.54] | mm | [8, 8.5, -38.2, -35.6, 6.54] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J1_02` | [9.7, 11.9, -38.2, -37.6, 5.529] | mm | [9.7, 11.9, -38.2, -37.6, 5.529] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J1_03` | [8, 8.3, -35.5, -31.5, 4.638] | mm | [8, 8.3, -35.5, -31.5, 4.638] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J1_04` | [11.3, 11.9, -33.8, -32.5, 4.155] | mm | [11.3, 11.9, -33.8, -32.5, 4.155] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J1_05` | [8, 9.6, -24.8, -22.7, 4.736] | mm | [8, 9.6, -24.8, -22.7, 4.736] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J1_06` | [11.3, 11.9, -24.3, -22.7, 6.467] | mm | [11.3, 11.9, -24.3, -22.7, 6.467] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J1_07` | [9.9, 11.1, -23.1, -22.7, 5.644] | mm | [9.9, 11.1, -23.1, -22.7, 5.644] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J1.inner_parts |
| `connpin_J2_01` | [-2.6, -1.6, -45.2, -39.3, 6.051] | mm | [-2.6, -1.6, -45.2, -39.3, 6.051] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J2.inner_parts |
| `connpin_J2_02` | [-2.6, -1.8, -39.1, -37.5, 4.732] | mm | [-2.6, -1.8, -39.1, -37.5, 4.732] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J2.inner_parts |
| `connpin_J2_03` | [-0.8, 0.4, -38.4, -37.5, 6.032] | mm | [-0.8, 0.4, -38.4, -37.5, 6.032] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J2.inner_parts |
| `connpin_J3_01` | [7.5, 8.5, -3.8, -2.8, 5.833] | mm | [7.5, 8.5, -3.8, -2.8, 5.833] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J3.inner_parts |
| `connpin_J3_02` | [7.5, 8.9, -2.7, -0.7, 5.185] | mm | [7.5, 8.9, -2.7, -0.7, 5.185] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J3.inner_parts |
| `connpin_J3_03` | [7.5, 8.9, -0.1, 2, 5.451] | mm | [7.5, 8.9, -0.1, 2, 5.451] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#connectors.J3.inner_parts |
| `faston_chamfer` | 1.02 | mm | [0.999, 1.08, 0.945, 1.065, 1.009] | mean-of-n | scan | 0.049 | no | measure/figures/pcb_measure.json#fastons |
| `faston_foot_dx` | -0.152 | mm | [-0.164, -0.175, -0.21, -0.139, -0.154, -0.07] | mean-of-n | scan | 0.043 | no | measure/figures/pcb_measure.json#fastons |
| `faston_foot_len` | 8.013 | mm | [8.087, 8.098, 7.984, 7.967, 7.929] | mean-of-n | scan | 0.067 | no | measure/figures/pcb_measure.json#fastons |
| `faston_foot_top_z` | 1.8 | mm | [1.8, 1.8, 1.8, 1.7, 1.9] | mean-of-n | scan | 0.063 | no | measure/figures/pcb_measure.json#fastons |
| `faston_hole_d` | 1.649 | mm | [1.657, 1.602, 1.625, 1.695, 1.689, 1.624] | mean-of-n | scan | 0.035 | no | measure/figures/pcb_measure.json#faston_detent_holes |
| `faston_hole_dy` | 0.009 | mm | [-0.018, 0.009, 0.04, -0.03, -0.039, 0.093] | mean-of-n | scan | 0.046 | no | measure/figures/pcb_measure.json#faston_detent_holes |
| `faston_hole_z` | 6.311 | mm | [6.264, 6.291, 6.341, 6.305, 6.366, 6.3] | mean-of-n | scan | 0.033 | no | measure/figures/pcb_measure.json#faston_detent_holes |
| `faston_thickness` | 0.779 | mm | [0.763, 0.742, 0.766, 0.805, 0.794, 0.802] | mean-of-n | scan | 0.023 | no | measure/figures/pcb_measure.json#fastons |
| `faston_top_z` | 10.617 | mm | [10.624, 10.627, 10.6, 10.611, 10.602, 10.639] | mean-of-n | scan | 0.014 | yes | measure/figures/pcb_measure.json#fastons |
| `faston_width` | 6.318 | mm | [6.298, 6.36, 6.291, 6.33, 6.313, 6.318] | mean-of-n | scan | 0.023 | no | measure/figures/pcb_measure.json#fastons |
| `faston_x` | [36.245, 51.223, 64.782, 71.218, 77.744, 88.097] | mm | [36.245, 51.223, 64.782, 71.218, 77.744, 88.097] | keep-measured | scan | 0.05 | yes | measure/figures/pcb_measure.json#fastons |
| `faston_y` | [-50.515, -50.523, -50.572, -50.57, -50.573, -50.558] | mm | [-50.515, -50.523, -50.572, -50.57, -50.573, -50.558] | keep-measured | scan | 0.05 | no | measure/figures/pcb_measure.json#fastons |
| `hole_H1` | [0.003, 0.001, 2.022] | mm | [0.003, 0.001, 2.022] | keep-measured | scan | 0.019 | yes | measure/figures/pcb_measure.json#holes.H1 |
| `hole_H2` | [0.013, -52.009, 2.006] | mm | [0.013, -52.009, 2.006] | keep-measured | scan | 0.035 | yes | measure/figures/pcb_measure.json#holes.H2 |
| `hole_H3` | [11.396, -6.614, 0.909] | mm | [11.396, -6.614, 0.909] | keep-measured | scan | 0.054 | no | measure/figures/pcb_measure.json#holes.H3 |
| `hole_H4` | [11.378, -19.416, 0.91] | mm | [11.378, -19.416, 0.91] | keep-measured | scan | 0.043 | no | measure/figures/pcb_measure.json#holes.H4 |
| `hole_H5` | [57.519, 1.976, 1.243] | mm | [57.519, 1.976, 1.243] | keep-measured | scan | 0.038 | no | measure/figures/pcb_measure.json#holes.H5 |
| `hole_H6` | [57.511, -49.008, 1.23] | mm | [57.511, -49.008, 1.23] | keep-measured | scan | 0.022 | no | measure/figures/pcb_measure.json#holes.H6 |
| `hs_bottom_z` | 0 | mm | — | assumed | assumed | 0.5 | no | intake/INTAKE_CARD.md §8 |
| `hs_fin_01` | [48.077, -29.399, 42.31, -29.792, 1.311] | mm | [48.077, -29.399, 42.31, -29.792, 1.311] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_02` | [44.935, -31.76, 42.155, -33.64, 1.183] | mm | [44.935, -31.76, 42.155, -33.64, 1.183] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_03` | [45.042, -34.325, 41.976, -37.644, 1.027] | mm | [45.042, -34.325, 41.976, -37.644, 1.027] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_04` | [50.971, -34.476, 53.852, -37.879, 1.104] | mm | [50.971, -34.476, 53.852, -37.879, 1.104] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_05` | [51.214, -31.629, 53.791, -33.858, 1.228] | mm | [51.214, -31.629, 53.791, -33.858, 1.228] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_06` | [48.629, -29.485, 53.938, -30.056, 1.236] | mm | [48.629, -29.485, 53.938, -30.056, 1.236] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_07` | [48.414, -12.173, 53.92, -11.404, 1.323] | mm | [48.414, -12.173, 53.92, -11.404, 1.323] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_08` | [51.444, -9.59, 54.081, -7.468, 1.255] | mm | [51.444, -9.59, 54.081, -7.468, 1.255] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_09` | [51.194, -6.851, 53.993, -3.468, 1.099] | mm | [51.194, -6.851, 53.993, -3.468, 1.099] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_10` | [45.024, -6.902, 42.21, -3.72, 1.03] | mm | [45.024, -6.902, 42.21, -3.72, 1.03] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_11` | [45.026, -9.679, 42.349, -7.692, 1.25] | mm | [45.026, -9.679, 42.349, -7.692, 1.25] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_12` | [48.082, -12.073, 42.523, -11.547, 1.264] | mm | [48.082, -12.073, 42.523, -11.547, 1.264] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_fin_width_short` | 1.192 | mm | [1.311, 1.183, 1.027, 1.104, 1.228, 1.236, 1.323, 1.255, 1.099, 1.03, 1.25, 1.264] | mean-of-n | scan | 0.099 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_hub_lower` | [48.07, -33.385, 3.5, 1.165, 47.1, 48.9] | mm | [48.07, -33.385, 3.5, 1.165, 47.1, 48.9] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.hubs.lower |
| `hs_hub_upper` | [48.155, -7.889, 3.6, 1.122, 47.1, 49] | mm | [48.155, -7.889, 3.6, 1.122, 47.1, 49] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.hubs.upper |
| `hs_shortfin_01` | [47.306, -33.927, 45.722, -37.553] | mm | [47.306, -33.927, 45.722, -37.553] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_shortfin_02` | [48.751, -33.994, 50.15, -37.667] | mm | [48.751, -33.994, 50.15, -37.667] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_shortfin_03` | [48.837, -7.338, 50.246, -3.71] | mm | [48.837, -7.338, 50.246, -3.71] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_shortfin_04` | [47.408, -7.37, 45.801, -3.768] | mm | [47.408, -7.37, 45.801, -3.768] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.arms |
| `hs_spine_hole` | [-20.679, 18.331, 3.07] | mm | [-20.679, 18.331, 3.07] | keep-measured | scan | 0.031 | no | measure/figures/pcb_measure.json#to220_Q1.tab_hole |
| `hs_spine_notch` | [-25.71, -15.699, 8.072] | mm | [-25.71, -15.699, 8.072] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#to220_Q1.spine_notch |
| `hs_spine_x` | [47.3, 49.2] | mm | [47.3, 49.2] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#heatsink.spine_x |
| `hs_top_z` | 25.262 | mm | 25.262 | keep-measured | scan | 0.034 | yes | measure/figures/pcb_measure.json#heatsink.top_z_p50 |
| `lead_d` | 0.8 | mm | — | assumed | standard | 0.2 | no | measure/figures/pcb_measure.json#resistor_R1.leads |
| `q1_body` | [42.86, 46.077, -26.3, -16.1, 6.114, 14.979] | mm | [42.86, 46.077, -26.3, -16.1, 6.114, 14.979] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#to220_Q1 |
| `q1_lead_1` | [-23.353, 41.132, 0.25, 41.447, 1.25, 42.075, 1.75, 44.457, 2.75, 44.544, 4.25] | mm | [-23.353, 41.132, 0.25, 41.447, 1.25, 42.075, 1.75, 44.457, 2.75, 44.544, 4.25] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#to220_Q1.leads |
| `q1_lead_2` | [-20.872, 44.576, 0.25, 44.901, 2.25, 44.513, 2.75, 44.533, 4.25] | mm | [-20.872, 44.576, 0.25, 44.901, 2.25, 44.513, 2.75, 44.533, 4.25] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#to220_Q1.leads |
| `q1_lead_3` | [-18.259, 41.171, 0.25, 41.117, 0.75, 41.768, 1.75, 42.417, 2.25, 43.9, 2.75, 44.431, 3.25, 44.454, 4.25] | mm | [-18.259, 41.171, 0.25, 41.117, 0.75, 41.768, 1.75, 42.417, 2.25, 43.9, 2.75, 44.431, 3.25, 44.454, 4.25] | keep-measured | scan | 0.15 | no | measure/figures/pcb_measure.json#to220_Q1.leads |
| `q1_lead_t` | 0.5 | mm | — | assumed | standard | 0.1 | no | JEDEC TO-220AB outline |
| `q1_lead_w` | 0.8 | mm | — | assumed | standard | 0.1 | no | JEDEC TO-220AB outline |
| `q1_tab` | [46.077, 47.485, -26.479, -16.381, 21.618] | mm | [46.077, 47.485, -26.479, -16.381, 21.618] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#to220_Q1 |
| `q1_tab_hole` | [-21.699, 18.604, 3.247] | mm | [-21.699, 18.604, 3.247] | keep-measured | scan | 0.075 | no | measure/figures/pcb_measure.json#to220_Q1.tab_hole_in_tab |
| `slot_x_end` | 2.2 | mm | 2.2 | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#board.slot |
| `slot_y` | [-27, -25.7] | mm | [-27, -25.7] | keep-measured | scan | 0.1 | no | measure/figures/pcb_measure.json#board.slot |
| `x2_CX1` | [73.677, 90.981, -35.273, -30.503, 10.831] | mm | [73.677, 90.981, -35.273, -30.503, 10.831] | keep-measured | scan | 0.1 | yes | measure/figures/pcb_measure.json#x2_CX1 |
| `ycap_CY1` | [81.403, -44.064, 8.173, 0.222, 0.816, 0.535, 3.544, 1.653] | mm | [81.403, -44.064, 8.173, 0.222, 0.816, 0.535, 3.544, 1.653] | keep-measured | scan | 0.112 | no | measure/figures/pcb_measure.json#ycap_CY1 |
| `ycap_lead_1` | [81.692, -37.985, 0.436, 81.002, -39.377, 5.096] | mm | [81.692, -37.985, 0.436, 81.002, -39.377, 5.096] | keep-measured | scan | 0.596 | no | measure/figures/pcb_measure.json#ycap_leads |
| `ycap_lead_2` | [88.042, -40.693, 0.03, 84.665, -43.164, 4.289] | mm | [88.042, -40.693, 0.03, 84.665, -43.164, 4.289] | keep-measured | scan | 0.837 | no | measure/figures/pcb_measure.json#ycap_leads |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01 | board plate - slot - holes H1..H6 | [board_x_min, board_x_max, board_y_min, board_y_max, board_thickness, slot_y, slot_x_end, hole_H1] |
| F02 | heatsink extruded profile (hubs with C-channels, spine, fins) - spine notch - screw hole | [hs_hub_upper, hs_hub_lower, hs_spine_x, hs_fin_01, hs_shortfin_01, hs_top_z, hs_spine_notch, hs_spine_hole] |
| F03 | TO-220 body, tab with hole, bent leads | [q1_body, q1_tab, q1_tab_hole, q1_lead_1] |
| F04 | spring clip strap and lower hook | [clip_path, clip_hook, clip_width, clip_z] |
| F05 | electrolytic cans (base, groove, body on a leaning axis), C1 V-chip base, C5 stem | [cap_C1, cap_C3, cap_C1_base, capstem_C5] |
| F06 | X2 film capacitor box | [x2_CX1] |
| F07 | 6 faston tabs (chamfered blade, detent hole, foot) | [faston_x, faston_y, faston_width, faston_thickness, faston_top_z, faston_chamfer] |
| F08 | connector housings - cavities + inner contacts | [conn_J1, conn_J2, conn_J3] |
| F09 | base + sloped riser blocks | [blk_K1, blk_K2] |
| F10 | axial parts along Y with leads | [ax_R1, ax_D1, ax_D2, ax_L2, lead_d] |
| F11 | Y-capacitor rounded disc with leads | [ycap_CY1, ycap_lead_1, ycap_lead_2] |
| F12 | SMD / low-part boxes | [box_001] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 65/200, converged yes, correction 0.1471° / 0.7248 mm.  
Unobservable CAD fraction: 0.0804.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 203996 | 0.4554 | 0.2892 | 0.7629 | 0.7838 | 1.3653 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 203996 | 0.4554 | 0.2892 | 0.7629 | 0.7838 | 1.3653 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.9419 | 0.6929 | 1.9859 | 3.1368 | 5.068 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 135843 | 0.5829 | 0.5848 | 0.8917 | 1.2273 | 4.503 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 18392 | 0.8304 | 0.6718 | 1.599 | 2.7384 | 4.4081 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.7629 max 1.3653 (n 203996) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 1.599 max 4.4081 (n 18392) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| I1 board outline edges | functional_interface | scan_to_cad | reported | reported | n 3973 · p95 0.2775 · max 0.4476 | n 3973 · p95 0.2775 · max 0.4476 | INTAKE_CARD §4 I1: the four board edge walls (card guides), z -1.7..0.1, near-horizontal normals |
| I1 board outline edges | functional_interface | cad_to_scan | reported | reported | n 5997 · p95 0.8415 · max 1.231 | n 4097 · p95 0.847 · max 1.231 | INTAKE_CARD §4 I1: the four board edge walls (card guides), z -1.7..0.1, near-horizontal normals |
| I1 board top face | functional_interface | scan_to_cad | reported | reported | n 1912 · p95 0.6942 · max 0.8911 | n 1912 · p95 0.6942 · max 0.8911 | INTAKE_CARD §4 I1: PCB top face (seating plane); upward-facing faces within the board outline, z -0.5..0.3 |
| I1 board top face | functional_interface | cad_to_scan | reported | reported | n 58941 · p95 0.9614 · max 3.4365 | n 49044 · p95 0.9142 · max 1.7048 | INTAKE_CARD §4 I1: PCB top face (seating plane); upward-facing faces within the board outline, z -0.5..0.3 |
| I2 mounting holes H1 H2 | functional_interface | scan_to_cad | reported | reported | n 316 · p95 0.1618 · max 0.4226 | n 316 · p95 0.1618 · max 0.4226 | INTAKE_CARD §4 I2 / E02: bore walls of H1 (0,0) and H2 (0,-51.8), r <= 2.6 about each axis (box approximation) |
| I2 mounting holes H1 H2 | functional_interface | cad_to_scan | reported | reported | n 506 · p95 0.8931 · max 1.0651 | n 288 · p95 0.6458 · max 0.9656 | INTAKE_CARD §4 I2 / E02: bore walls of H1 (0,0) and H2 (0,-51.8), r <= 2.6 about each axis (box approximation) |
| I3 faston tab row | functional_interface | scan_to_cad | reported | reported | n 12734 · p95 0.3187 · max 0.7964 | n 12734 · p95 0.3187 · max 0.7964 | INTAKE_CARD §4 I3 / E11: six faston blades at x 36-88, y -53.7..-47.4 (located on scan faces z 9-11), z 0.3..11.5 |
| I3 faston tab row | functional_interface | cad_to_scan | reported | reported | n 11473 · p95 0.5783 · max 0.9194 | n 10532 · p95 0.551 · max 0.9194 | INTAKE_CARD §4 I3 / E11: six faston blades at x 36-88, y -53.7..-47.4 (located on scan faces z 9-11), z 0.3..11.5 |
| I4 heatsink top and tallest parts | functional_interface | scan_to_cad | reported | reported | n 28912 · p95 0.6445 · max 1.1417 | n 28912 · p95 0.6445 · max 1.1417 | INTAKE_CARD §4 I4: lid clearance; everything above z 12 (heatsink, clip, big caps) |
| I4 heatsink top and tallest parts | functional_interface | cad_to_scan | reported | reported | n 43065 · p95 2.2477 · max 3.6553 | n 15354 · p95 0.9808 · max 2.5003 | INTAKE_CARD §4 I4: lid clearance; everything above z 12 (heatsink, clip, big caps) |
| X between caps | interior | scan_to_cad | reported | reported | n 5239 · p95 0.5867 · max 0.9872 | n 5239 · p95 0.5867 · max 0.9872 | INTAKE_CARD §3: x 74-86, y -30..-8, shadowed (reported only) |
| X between caps | interior | cad_to_scan | reported | reported | n 6430 · p95 1.0804 · max 2.0995 | n 3904 · p95 0.6042 · max 1.3431 | INTAKE_CARD §3: x 74-86, y -30..-8, shadowed (reported only) |
| X solder side | interior | scan_to_cad | reported | reported | n 8732 · p95 0.7836 · max 1.2928 | n 8732 · p95 0.7836 · max 1.2928 | INTAKE_CARD §3: board bottom, not scanned (reported only) |
| X solder side | interior | cad_to_scan | reported | reported | n 73503 · p95 1.8001 · max 4.4254 | n 257 · p95 0.1242 · max 0.3149 | INTAKE_CARD §3: board bottom, not scanned (reported only) |
| X under heatsink clip TO-220 | interior | scan_to_cad | reported | reported | n 15565 · p95 0.5356 · max 1.3653 | n 15565 · p95 0.5356 · max 1.3653 | INTAKE_CARD §3: x 38-55, y -41..-1, below z 12, partly occluded (reported only) |
| X under heatsink clip TO-220 | interior | cad_to_scan | reported | reported | n 38095 · p95 3.3359 · max 5.068 | n 11514 · p95 1.6164 · max 4.503 | INTAKE_CARD §3: x 38-55, y -41..-1, below z 12, partly occluded (reported only) |
| Z1 board band z<0.3 | region | scan_to_cad | reported | reported | n 95621 · p95 0.7719 · max 1.2928 | n 95621 · p95 0.7719 · max 1.2928 | z bucket |
| Z1 board band z<0.3 | region | cad_to_scan | reported | reported | n 144026 · p95 1.4125 · max 4.4254 | n 56579 · p95 0.9066 · max 2.3091 | z bucket |
| Z2 low parts z 0.3-3 | region | scan_to_cad | reported | reported | n 27036 · p95 0.6951 · max 1.1643 | n 27036 · p95 0.6951 · max 1.1643 | z bucket (SMD parts, leads) |
| Z2 low parts z 0.3-3 | region | cad_to_scan | reported | reported | n 35152 · p95 1.5452 · max 3.5738 | n 19840 · p95 0.858 · max 2.3088 | z bucket (SMD parts, leads) |
| Z3 mid parts z 3-12 | region | scan_to_cad | reported | reported | n 52427 · p95 0.5276 · max 1.3653 | n 52427 · p95 0.5276 · max 1.3653 | z bucket |
| Z3 mid parts z 3-12 | region | cad_to_scan | reported | reported | n 77757 · p95 2.7773 · max 5.068 | n 44070 · p95 0.8319 · max 4.503 | z bucket |
| Z4 high parts z>12 | region | scan_to_cad | reported | reported | n 28912 · p95 0.6445 · max 1.1417 | n 28912 · p95 0.6445 · max 1.1417 | z bucket |
| Z4 high parts z>12 | region | cad_to_scan | reported | reported | n 43065 · p95 2.2477 · max 3.6553 | n 15354 · p95 0.9808 · max 2.5003 | z bucket |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 solder side unscanned | cad_to_scan | the board bottom (solder side) was never scanned, so CAD->scan distance there measures the invented flat bottom face against the board top/edges, not a surface deviation | 0.241 | n: 72286; rms: 1.0206; mean: 0.9364; p50: 0.8544; p95: 1.8111; p99: 2.6528; max: 4.4254 |
| M2 scan open boundary | cad_to_scan | distance measured to a scan hole EDGE (55 open-boundary loops: connector cavities, under heatsink, hole bores) is not a surface deviation | 0.3155 | n: 94663; rms: 1.2976; mean: 0.9638; p50: 0.7325; p95: 2.7897; p99: 3.6934; max: 5.068 |
| M3 skin normal disagreement | cad_to_scan | a CAD point whose nearest scan triangle faces > 70 deg away is an occluded/interior correspondence, not an outer-skin deviation | 0.0922 | n: 27647; rms: 1.333; mean: 0.9789; p50: 0.6455; p95: 2.927; p99: 3.8545; max: 4.9972 |

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.6754; max_over_by: 3.703 | cad_to_scan | n: 193965; rms: 0.701; mean: 0.5893; p50: 0.6935; p95: 0.9754; p99: 1.7149; max: 4.503 | all masks except M1 solder side unscanned |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.5012; max_over_by: 4.268 | cad_to_scan | n: 202872; rms: 0.8498; mean: 0.5992; p50: 0.5959; p95: 1.8012; p99: 3.0526; max: 5.068 | all masks except M2 scan open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.6121; max_over_by: 4.1269 | cad_to_scan | n: 146153; rms: 0.6111; mean: 0.4752; p50: 0.5752; p95: 0.9121; p99: 1.6017; max: 4.9269 | all masks except M3 skin normal disagreement |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.7538; max_over_by: 4.1418 | cad_to_scan | n: 181682; rms: 0.6534; mean: 0.4878; p50: 0.5225; p95: 1.0538; p99: 2.1363; max: 4.9418 | M2 scan open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.6333; max_over_by: 3.703 | cad_to_scan | n: 160546; rms: 0.5962; mean: 0.4574; p50: 0.5192; p95: 0.9333; p99: 1.6183; max: 4.503 | M2 scan open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.604; max_over_by: 3.703 | cad_to_scan | n: 151166; rms: 0.5809; mean: 0.4533; p50: 0.539; p95: 0.904; p99: 1.4158; max: 4.503 | M2 scan open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5917; max_over_by: 3.703 | cad_to_scan | n: 135843; rms: 0.5829; mean: 0.4631; p50: 0.5848; p95: 0.8917; p99: 1.2273; max: 4.503 | M2 scan open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5654; max_over_by: 3.703 | cad_to_scan | n: 103890; rms: 0.5946; mean: 0.4814; p50: 0.6222; p95: 0.8654; p99: 1.1354; max: 4.503 | M2 scan open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5375; max_over_by: 3.703 | cad_to_scan | n: 75970; rms: 0.5922; mean: 0.49; p50: 0.6381; p95: 0.8375; p99: 0.9921; max: 4.503 | M2 scan open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

1576 points (0.0077 fraction) in 21 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 131 | [47.962, -22.396, 20.934] | [50.888, 55.041] | [331.1, 341.3] | 1.1417 | Spine z~21.6 surface (x 47.0-48.4, y -26.6..-16.3): scanned surface INSIDE the modelled heatsink spine in the plane of the TO-220 tab top. Same scan points in the datum frame p50 0.73 / max 0.96 (38% > 0.8), and it is the only >=20-point over-band cluster in the datum frame. Not modelled by design (MODELING_PLAN §9: likely reconstruction artefact continuing the tab-top surface; cannot be reached by a straight line from outside). UNRESOLVED: real slot vs artefact is not decidable from scan or photos (limitation L7). |
| 1 | 122 | [0.236, 0.434, -2.547] | [1.746, 2.16] | [5.3, 354.7] | 1.2928 | ICP-bias artefact: H1 bore lower rim / board-bottom edge fringe (gate-frame z -2.8..-2.4). Same points in the datum frame p50 0.26 / max 0.59 (within band). Caused by the +0.72 mm z lift of the QA ICP (L3). |
| 2 | 113 | [10.216, -51.491, 2.053] | [50.274, 55.077] | [279, 283.4] | 0.8547 | ICP-bias artefact: flat top of a low box (x 8.0-11.7, y -53.9..-49.0). Datum frame p50 0.008 / max 0.041. |
| 3 | 69 | [47.562, -21.583, 5.066] | [50.471, 53.615] | [332.4, 340.6] | 1.3653 | Spine notch / TO-220 body at z~5 (x 47.4-47.7, y -24.9..-16.8), partly occluded zone under the heatsink. Datum frame p50 0.33 / max 0.79 (within band); over band only through the ICP bias. |
| 4 | 61 | [-0.375, -31.29, 2.37] | [30.053, 32.993] | [265.6, 271.9] | 0.9492 | ICP-bias artefact: block top (x -2.3..1.0, y -33..-30). Datum frame p50 0.035 / max 0.16. |
| 5 | 48 | [49.645, -55.901, -2.429] | [71.305, 78.552] | [308.3, 314.6] | 0.9841 | ICP-bias artefact: board bottom edge fringe along the y -56 edge (x 44-55). Datum frame p50 0.10 / max 0.20. |
| 6 | 48 | [7.726, 3.756, -2.473] | [5.549, 12.551] | [17.7, 43.6] | 1.1012 | ICP-bias artefact: board bottom edge fringe along the y +3.8 edge (x 4-12). Datum frame p50 0.19 / max 0.40. |
| 7 | 47 | [44.8, -24.309, 14.11] | [49.187, 52.515] | [329.9, 333.2] | 0.9634 | ICP-bias artefact: horizontal top at z~14 beside the TO-220 / clip (x 43.7-46.0, y -25.4..-22.2). Datum frame p50 0.15 / max 0.25. |
| 8 | 46 | [11.466, -36.225, 1.88] | [37.789, 38.101] | [286.8, 287.8] | 1.1643 | ICP-bias artefact: low part top at (11.5,-36.2,z~1.9). Datum frame p50 0.24 / max 0.38. |
| 9 | 43 | [73.454, -15.963, 11.121] | [74.042, 76.517] | [346.5, 348.8] | 0.8928 | ICP-bias artefact: can top at z~11.1 (x 72.2-74.8, y -17.8..-14.4). Datum frame p50 0.17 / max 0.24. |
| 10 | 42 | [27.493, -51.48, 1.51] | [55.768, 59.512] | [296.5, 300] | 0.9225 | ICP-bias artefact: SMD box top (x 25.5-29.3, y -52.6..-49.2). Datum frame p50 0.023 / max 0.13. |
| 11 | 37 | [85.692, -43.344, 2.213] | [95.243, 96.266] | [332.6, 333.8] | 1.0849 | Y-cap lead wire (x 85.3-86.4, y -44.3..-42.1, z 0.8-4.0): lead modelled as a standard 0.8 mm straight wire; datum frame p50 0.58 / max 0.83 (3 of 37 points > 0.8, by 0.03 mm); rest of the excess is the ICP bias. Minor lead-path residual. |

### Over-band point clusters, CAD → scan (> 0.8 mm)

101675 points (0.3389 fraction) in 80 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 50807 | [53.55, -24.241, -1.562] | [16.864, 108.708] | [0, 360] | 4.4254 | **UNEXPLAINED** |
| 1 | 24778 | [46.221, -18.824, 10.791] | [41.859, 60.508] | [317.6, 356.5] | 5.068 | **UNEXPLAINED** |
| 2 | 5839 | [2.495, -11.808, 0.024] | [2.019, 49.698] | [0.2, 359.9] | 1.2345 | **UNEXPLAINED** |
| 3 | 2697 | [36.632, -51.563, 0.154] | [37.992, 92.33] | [273.4, 322.8] | 1.9842 | **UNEXPLAINED** |
| 4 | 2055 | [48.117, -33.662, 10.508] | [57.361, 61.828] | [322.5, 326.4] | 4.4562 | **UNEXPLAINED** |
| 5 | 1859 | [51.174, -30.612, 12.425] | [58.012, 62.362] | [328.5, 331] | 2.9394 | **UNEXPLAINED** |
| 6 | 1364 | [87.488, -18.315, 2.67] | [83.647, 93.938] | [345.9, 349.8] | 3.5922 | **UNEXPLAINED** |
| 7 | 1246 | [78.312, -22.322, 0.384] | [76.185, 86.074] | [339.1, 349.2] | 2.9737 | **UNEXPLAINED** |
| 8 | 1211 | [52.177, -7.614, 12.503] | [52.165, 54.301] | [350.6, 353.2] | 1.7849 | **UNEXPLAINED** |
| 9 | 993 | [52.05, -33.422, 11.754] | [60.999, 63.431] | [326.1, 327.6] | 1.7365 | **UNEXPLAINED** |
| 10 | 659 | [84.455, -8.481, 0.405] | [77.228, 89.631] | [351.9, 359.2] | 3.5359 | **UNEXPLAINED** |
| 11 | 527 | [9.828, -30.99, 3.018] | [24.783, 40.077] | [281.9, 296] | 1.9756 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.0735°, origin offset 0.0799 mm, point disagreement p95 0.0639 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (within).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part scan->CAD (gated, post-ICP): p95 0.763 / max 1.365 vs 0.30 / 0.80 | p95: almost entirely the QA ICP +0.72 mm z lift (L3), which shifts every board-level point and box top by ~0.7 mm (zone Z1 board band p95 0.772 post-ICP vs 0.243 datum frame). In the builder datum frame the same statistic is p95 0.292 / max 1.027 (0.05% of points > 0.8), and with the diagnostic ICP p95 0.287 / max 1.068. Residual max in the datum frame: 3-point fringe below the +X board edge at (96.0,-8.5,-1.5) 1.027 (scan fringe of the unscanned bottom edge, artefact); spine z~21.6 surface 0.963 (L7, unresolved); unmodelled content in both heatsink hub screw channels 0.944 / 0.895 (17 + 9 points); Y-cap lead 0.826 (3 points). All five it1 geometry findings are fixed. | (a) owner ACCEPT-BAND (BAND_NOT_MET) quoting the gated numbers; (b) record an owner/skill decision on the ICP correspondence radius for thin plates with one invented face and re-run QA with both protocols (would bring p95 inside band; the max would still be ~1.03-1.07); (c) optional minor geometry: hub-channel content, spine z~21.6 once decided by a photo - neither clears the CAD->scan miss below. |
| whole part CAD->scan observable (gated): p95 1.599 / max 4.408 vs 0.30 / 0.80 (datum frame 1.832 / 4.419) | CAD surface with no scan behind it that the CAD-only ray test still counts as observable: the invented board bottom (26.8% of the observable subset, p95 1.788 / max 4.103), the heatsink block with its deep fin/spine side faces and roots (21.4%, p95 2.506 / max 4.408), and in the rest of the part (51.8%, p95 0.901 / max 2.949 post-ICP; 0.539 / 3.216 datum frame) lower can walls between the caps, connector cavities, box sides and raised-part undersides (qa/diag_observable_breakdown.json, diagnostic). With all three named CAD masks the number is still p95 0.892 / max 4.503 (M1 24.1%, M2 31.6%, M3 9.2%); leave-one-out and the open-boundary radius sweep all stay over band. Not fixable by geometry without scan data of those faces. | (a) solder-side scan plus oblique scans of the heatsink fins, the inter-cap area and the connector cavities, then rebuild those faces from data and re-run verify; (b) owner ACCEPT-BAND (BAND_NOT_MET) for a component-side envelope use, quoting the unmasked numbers. |
| named zones (reported; the regime has no interface band) | I1 board top face post-ICP captures only 1,912 scan points because the +0.72 mm bias moves the scanned top out of the zone window (datum frame n 57,138, p95 0.170 / max 0.847); I1 outline edges scan->CAD p95 0.278 / max 0.448; I2 H1/H2 bores p95 0.162 / max 0.423; I3 faston row p95 0.319 / max 0.796; I4 heatsink/tall parts p95 0.644 / max 1.142 (ICP bias + spine surface). CAD->scan in I1/I4 is dominated by invented faces. | as above (L3 decision; L7 photo). |

Missed band(s): `scan_to_cad:masked: p95 0.763 max 1.365 vs 0.3/0.8`; `cad_to_scan_observable: p95 1.599 max 4.408 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 dims (scan-only run), nothing to attribute |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | finding | QA gate independent: QA's own datum audit on the raw scan (0.074 deg / 0.080 mm), QA's own ICP (T_refine never written back to intake/alignment.json), no expected value from params.json or the builder. Finding (carried from it1): the builder record contains self-referential checks - MODELING_PLAN §8 builder self-check against the same scan (it2: scan->CAD p95 0.259 / max 0.968) and the intake datum try 2 noise floor measured on the board top itself (DECISIONS.md) - consistency checks, not independent evidence. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 12 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | Every intake feature family E01-E15 exists in the CAD (overlays Z -0.8/0.1/1.9/4.2/10/12/18.4/21.6/24.5, x 9.0/46.6/48.2/90.7, y -0.6/-8.5/-23/-32.8/-37.6/-50.5); E16/E17 declared not modelled. No hallucinated body: all CAD->scan clusters sit on declared unscanned/invented surfaces (board bottom, heatsink fin/spine sides and roots, lower can walls between caps, connector cavities, X2/C box sides, raised-part undersides). All five routed it1 scan->CAD findings are fixed (see CHK-LIKE4LIKE). Open finding: the scanned surface inside the heatsink spine at z~21.6 (x 48.1-48.4, y -26.4..-16.3) is still not modelled (builder declares it a reconstruction artefact, MODELING_PLAN §9); not decidable from the scan or photos. Minor residuals below the 20-point cluster floor in the datum frame: 17 pts at the north hub channel (48.0,-6.7,z 0.9-5.6) max 0.944 and 9 pts at the south hub channel (47.9,-34.6,z 1.1-3.1) max 0.895 (unmodelled channel content, e.g. a screw), 3 pts of Y-cap lead (85.4,-44.0) max 0.826, 3 pts of fringe below the +X board edge (96.0,-8.5,-1.5) max 1.027. |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | MODELING_PLAN §5 plans no fillet/chamfer operation; build/fillets.json and export_check.json fillets empty (0 OK/REDUCED/FAILED/NO_EDGES/SELECTOR_ERROR); nothing skipped or shrunk. |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh agent; see independence |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | it1 (_it1_SUPERSEDED/qa) vs it2 use the same protocol: same regime file, identical zones.json predicates and masks.json masks/parameters (M1 region, M2 open boundary 0.8, M3 normal 70), same ICP parameters incl. the same once-raised cap 200, same deviation sampling (all scan vertices, 300k CAD samples seed 2, k 8, n_samp 3M, obs 20k seed 5), same datum spec regions. Deltas therefore come from geometry: gate scan->CAD p95 0.764 -> 0.763, max 1.501 -> 1.365; gate CAD->scan observable p95 1.623 -> 1.599, max 4.408 -> 4.408; datum-frame scan->CAD p95 0.294 -> 0.292, max 1.499 -> 1.027; diagnostic max-corr-1.0 run scan->CAD max 1.509 -> 1.068; ICP 0.162 deg/0.726 mm (62 its) -> 0.147 deg/0.725 mm (65 its). Per it1 finding region, same scan points, datum frame (it1 -> it2): C5 ring part max 1.499 -> 0.543; J3 cavity floor max 1.487 (43.5% > 0.8) -> 0.314 (0%); TO-220 tab/spine hole max 1.201 -> 0.719; K2 bump max 1.141 -> 0.332; hub-channel / clip lower hook (48.5,-37.6) max 0.977 -> 0.623; spine z~21.6 surface max 0.963 -> 0.963 (unchanged, not modelled by design). |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | QA census (qa/step_check.json): 1233 faces, 100% analytic area (plane 1054, cylinder 178, torus 1), no B-spline/ruled faces; plane faces are ~60 SMD boxes and component bodies, not facets. model.py grep: no loft/ruled; Wire.make_polygon only for small parametric profiles (can r-z revolve profile, faston blade, K riser trapezoid); clip strap/hook are slot chains of a measured polyline extruded once, not a stack of scan slices. Plan expected cone faces; census has none (cans built as revolved polygons with vertical walls) - reported, not gated. |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | finding | Photos 1-4 walked. Photo 1 matches the scanned configuration (star heatsink with TO-220 held by the gold spring strap, 3 large cans + small cans, drum/can part top-left, grey X2 box, blue Y-cap, 6 faston tabs, 5 white connectors, SOIC, edge pads): every photographed feature family exists in the CAD. Photos 2-4 are installed/catalogue photos of a variant (no spring clip, different heatsink), so they cannot confirm heatsink/clip/spine detail. No photo shows the solder side, the spine z~21.6 region or the hub channel interiors. |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 5 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | No Tier-1 (no calipers run): scan-only job, every requested dimension is ABSENT, not passed; absolute scale is not caliper-verified (units assumed mm). | caliper readings for ENV-X, ENV-Y, F01 (H1 diameter), F02 (H1-H2 pitch) and F03 (board thickness) entered in input/MEASUREMENTS.md | qa/gate.json#limitations.0; intake/MEASUREMENTS.md |
| L2 | Unscanned surfaces are invented: the whole solder side (board bottom), deep heatsink fin and spine sides and roots, connector cavity floors, lower can walls between the caps, undersides of raised parts and the Y-cap back. They drive the observable CAD-to-scan miss (p95 1.599 / max 4.4081 mm); the solder-side mask alone removes a fraction 0.241 of the CAD samples. | a solder-side scan and oblique scans between the heatsink fins and caps | qa/gate.json#limitations.1; build/MODELING_PLAN.md §6, §9 |
| L3 | QA ICP bias: with the golden ICP parameters the invented board bottom corresponds to the scanned board top, so the ICP lifts the CAD (correction 0.7248 mm) and the official scan-to-CAD reads p95 0.7629 / max 1.3653 mm; in the builder datum frame the same statistic reads p95 0.2923 / max 1.0269 mm. | a solder-side scan, or an owner / skill decision on the ICP correspondence radius or a signed normal test for thin plates with one invented face (QUESTIONS.md §F) | qa/gate.json#limitations.2; qa/gate.json#auto_limitations: datum-frame vs post-ICP scan_to_cad p95 differ by 0.471 mm (> band 0.3 mm) |
| L4 | Board warp is not modelled: the board is a flat design-intent plate while the scanned board top is bowed / twisted by a few tenths of a millimetre (worst at the H1 corner). | the owner asks for the as-scanned warped board, or an enclosure fit check needs the warp | qa/gate.json#limitations.3; intake/INTAKE_CARD.md §6, §8 |
| L5 | QA ICP did not converge at its default iteration cap; the cap was raised once (same reason as iteration 1) and it converged; both runs are kept. | any rebuild: re-run ICP with the same cap and report both runs again | qa/gate.json#limitations.4; qa/registration_run1_cap60.json |
| L6 | The photos are catalogue / installed photos; photos 2-4 show a variant heatsink without the spring clip, so heatsink, clip and spine details are confirmed by photo 1 only. | photos of the scanned unit (top, both heatsink sides, spine top) | qa/gate.json#limitations.5; qa/review.json#photos |
| L7 | A scanned surface inside the heatsink spine above the TO-220 tab is not modelled (real slot or reconstruction artefact is undecided); it holds the largest datum-frame scan-to-CAD residual after the edge fringe. | a side photo / oblique scan of the spine above the TO-220 tab, or an owner statement | qa/gate.json#limitations.6; build/MODELING_PLAN.md §9 |
| L8 | Simplifications with a deviation cost: SMD terminations, solder fillets and lead toes below half part height are not modelled; lead bends are straight segments with square knuckles; can tops are flat (vent crosses and rim crimp omitted); the Y-cap is a rounded disc without its epoxy necks. | a use that needs pad-level or lead-level geometry | measure/params.json#simplifications |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `hs_bottom_z` | 0 | assumed | intake/INTAKE_CARD.md §8 |
| `lead_d` | 0.8 | standard | measure/figures/pcb_measure.json#resistor_R1.leads |
| `q1_lead_t` | 0.5 | standard | JEDEC TO-220AB outline |
| `q1_lead_w` | 0.8 | standard | JEDEC TO-220AB outline |

- Heatsink root stands on the board top (fin roots hidden). _(source: assumed; measure/params.json#hs_bottom_z)_
- TO-220 lead cross-section and through-hole lead wire diameter are standard values. _(source: standard; measure/params.json#q1_lead_w, q1_lead_t, lead_d)_
- Every sub-body is embedded slightly into the board top (and the TO-220 tab into the spine) so the union has no coplanar faces (documented clearance in build/model.py). _(source: assumed; build/model.py#EMBED)_
- The board bottom is an invented flat face at the measured board thickness below the datum top face. _(source: assumed; measure/params.json#board_thickness)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** manufacture, tooling, PCB footprint or electrical work
- **Not fit for:** solder-side or board-thickness-critical fits (the solder side is invented, scale not caliper-verified)
- **Not fit for:** fits that depend on hidden geometry: heatsink fin roots and sides, connector cavities, part undersides
- Fit for: component-side envelope and clearance studies for an enclosure (lid heights, part positions, mounting holes, faston access), with the band miss and limitations above in mind
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Component-side envelope / fit reference only, iteration 2, band NOT met. Not fit for manufacture, tooling, PCB footprint or electrical work, or any solder-side / board-thickness-critical fit: the solder side, heatsink fin roots and sides, connector cavity floors and part undersides are invented; absolute scale is not caliper-verified; the board is modelled flat; the spine z~21.6 surface is undecided. Delivery needs a recorded owner ACCEPT-BAND citing this gate.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner)** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): accept scan_to_cad:masked and cad_to_scan_observable misses of the it2 BAND_NOT_MET gate 948b8a16472b for delivery. Record: `decisions/accept_band_it2.md` (sha256 `4aa4889152d2da2dd9297f4c542723cde4ec77f01a167be9716dc1e6ed5a6259`).

## 15. Reproduction

```
python3 build/model.py   (from the run root; writes build/*.step, *_cad.stl, export_check.json)
python3 measure/measure_pcb.py && python3 measure/make_params.py   (re-derives measure/params.json from intake/aligned_work.stl)
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-E01_Power-PCB.step | 20609.8947 | 0 | 0 | yes | yes | no |
| OD-E01_Power-PCB_datum.step | 20609.8947 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 948b8a16472b0e88a7055478c5860b3c84c5d5f80579f7ae3e3326f1bc16a17d |
| `measure/params.json` | 00068f900e9fc900550f4f58bf4d8cef8be191068462d0fb440e3052f29e2571 |
| `build/export_check.json` | 4cbfa6967d7cf4642aa5c31305a06435ce00dd2fc7d5b548db692bbc0c397d41 |
| `intake/alignment.json` | c547794d77c9878a3d4102a69b4794ca11f3dd03ab0865b34c97029fc7de2dfe |
| `deliver/repro.json` | a8b0cbaaddac070f8015053403f1f1afeb068afabdc3d6834b7c6768d8d01875 |
| `deliver/limitations.json` | f3c02f6d9d46a165cbd9f93c72985eaf81092a25aab887362853cc0c01bd5f69 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
