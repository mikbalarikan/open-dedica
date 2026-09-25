# BUILDER REPORT: OD-H22_3-way-valve (stl-re skills @ b8d9c97)

Builder stages run: orchestrate, intake-datum, measure-intent, rebuild-build123d. Verify and
deliver were **not** run (CHK-INDEP: they are for an independent agent). Nothing below is a gate
verdict. Regime: baseline-skill, plastic, p95 <= 0.30 / max <= 0.80 mm, confirmed by Ikbal
via decision card at 10:54 (`DECISIONS.md` REGIME x2, `intake/regime.json`). Run type: scan-only,
no calipers (`DECISIONS.md` MEASUREMENTS). `scan_resolution` = unknown (`DECISIONS.md` OTHER).

## 1. Datum (`intake/alignment.json`, status OK)
- Primary: the flange back face (stem side), used as XY with z=0. +Z points to the tray and drive tube. The trimmed fit is rms 0.0357 / max 0.1086 over 8,304 faces (261 mm2); untrimmed it is rms 0.0508 / max 0.202.
- Secondary: the valve axis. It is the median of 17 Kasa section circles on three coaxial features (boss collar r 8.05, tube OD r 6.22, stem neck r 4.08). Median circle rms is 0.0694 and the worst is 0.230; the circle noise is 0.0767.
- Clock: fourier_mass n=2 on the ears, -84.99 deg. This puts the ears on +/-X and the ports on +/-Y. The origin is where the axis meets the back-face plane.
- Tilt (CHK-TILT, finding): 0.470 +/- 0.014 deg over 18.2 mm, and each feature reads about 0.5 deg. Marked not resolvable. The model makes the axis perpendicular to the flange (design intent), so the lower body's 0.1–0.17 mm lateral offset is a declared simplification.
- Landmarks: tray floor 2.245, top 13.979, bottom -30.835.
- Datum extents: 42.56 x 39.90 x 44.81.
- CHK-SCALE: FLAG. Units are assumed mm and the scale is unverified.
- matrix_4x4 (raw to datum) rows: [0.222223, 0.973708, -0.050097, 35.944170]; [-0.872040, 0.175514, -0.456882, -87.776537]; [-0.436077, 0.145216, 0.888116, 187.930701].
- STOP-rule note: the first pass used the tray floor as the noise reference (0.0355) and stopped, because 0.0357 > 0.0355. Across seeds 0–7 the two values overlap (primary 0.0344–0.0361, tray 0.0354–0.0373). Re-run with the self-referential noise path; align.py records this as a finding. See §6 D1.

## 2. Feature tree (`build/MODELING_PLAN.md`, `build/model.py`)
| F | Operation | Result |
|---|---|---|
| F01 | flange outline sketch: disc plate_R plus 2 tapered ears ending in circles ear_end_R about the holes; extruded 0 to rim_top_z | prism |
| F02 | concave disc/ear blends outline_blend_R 4.617 | 4 edges OK |
| F03 | back-edge round back_edge_R 1.868, local, before the stem is fused | 12 edges OK |
| F04 | tray pocket: inward offset by rim_wall_t, blends R6.064, down to flange_floor_z | OK |
| F05 | core revolve: stem cylinder, 40 deg cone, neck, collar, drive tube | 1 solid |
| F06 | 2 XZ triangular gussets (mirrored) | OK |
| F07 | port body x2: revolve about each measured axis (neck, sleeve, lip) | per-port angles |
| F08 | clip block x2 with R0.5 axial rounds (assumed) | 4+4 edges OK |
| F09 | bottom rib box, top buried in the stem | OK |
| F10 | cuts: tube bore, 4 slots (per-instance angle and width), 2 ear holes | OK |
| F11 | port cuts: mouth bore, inner bore, 2 stadium clip slots per port | OK |
| F12 | clean and export in both frames | 1 valid closed solid |

Results: 162 faces (expected 140–260, `build/face_stats.json`); volume 6395.59 mm3; fillet_log: 5 OK, 0 reduced, 0 failed.
- `export_check.json`: analytic area share 1.0; datum STEP, scan-frame STEP and CAD STL written.
- No loft and no polyline stacks. Each profile vertex comes from a param.

## 3. Key params (`measure/params.json`, 52 params; `PARAM_TABLE.md`, validator 0 warnings)
Every value has source scan unless marked. The estimator is recorded per param.
| Param | Value (mm/deg) | Rule | Note |
|---|---|---|---|
| ear_hole_x | [15.447, -15.338] | keep-measured, critical | pitch 30.79; not forced symmetric (C9) |
| ear_hole_r | 1.936 | symmetry, critical | hole diameter 3.87 |
| plate_R / rim_top_z / flange_floor_z | 11.70 / 5.63 / 2.26 | keep-measured | full-circle and plane fits |
| collar_R / tube_R / tube_bore_r | 8.06 / 6.203 / 4.561 | keep-measured, critical (tube) | Kasa, multi-station |
| slot_count | 4 | pattern_count (radius signal) | CHK-COUNT pass |
| slot_theta_deg | [-0.11, 90.2, 179.79, 269.38] | keep-measured, critical | per instance |
| slot_w | [3.086, 2.722, 3.041, 2.572] | keep-measured, critical | ear-axis vs cross-axis slots differ |
| stem_R / stem_neck_R / cone half-angle | 6.547 / 4.074 / 40.09 | keep-measured | |
| port_elev_deg | [34.059, 35.03] | keep-measured | per-port axis fit |
| port_axis_z0 | [-14.301, -14.42] | keep-measured | per-port axis fit |
| port_lip_R / port_bore_R / port_sleeve_R | 6.162 / 4.339 / 5.585 | symmetry, critical (lip, bore) | hose interface |
| port_block_half_u / half_v | 5.891 / 5.913 | symmetry, critical | clip block flats |
| port_slot_w | 1.353 | symmetry, critical | U-clip slot |

Assumed, unscanned values: tube_bore_bottom_z 1.5, port_bore2_end_t 12.5, rib_half_len 4.5 (buried), port_block_corner_R 0.5.

Checks: CHK-CLUSTER pass, CHK-FRAME pass, CHK-ENUM pass (E01–E16).

## 4. Limitations (declared)
- **Scan-only.** No calipers and no scale reference, so absolute scale is unverified (CHK-SCALE FLAG) and Tier-1 was not run. `scan_resolution` is unknown; the evidence suggests full-res (495,881 faces, mean edge 0.154 mm).
- **Tilt.** The axis is about 0.5 deg off the flange normal, and the lower body sits 0.05–0.17 mm off-axis. The model is coaxial by intent.
- **Unscanned interior.** Not invented: the tube-bore floor/web, the port bores beyond t of about 13–16, and the internal flow passages.
- **Specimen damage.** The +X ear tip is torn. The +X ear hole also contains scan material at z 0.06–0.65 (about 3 mm2 of vertical-normal faces at r 0.5–1.5 from the hole axis); the -X hole is clean. Not modelled.
- **Ear holes.** The radius narrows to about 1.7 at z 0.1–0.3 (1.93 at mid-thickness). This is not modelled; it is possibly an edge or lip.
- **Other simplifications, with their cost:** ejector-pin circles on the port sleeves (up to about 0.3–0.6); port bore draft (<= 0.2); small edge rounds and finger tops (<= 0.3); rim/tray detail (<= 0.12).

## 5. Builder self-check (NOT QA; datum frame, no ICP, full-res scan, 200k samples)
Unsigned scan-to-CAD distances (mm):
| Scope | rms | p50 | p95 | p99 | max |
|---|---|---|---|---|---|
| all | 0.124 | 0.068 | 0.234 | 0.408 | 1.419 |
| excluding the damaged +X ear zone (x > 13.4, abs(y) < 7, z < 6; 6.8 % of samples) | – | – | 0.222 | 0.372 | 0.765 |

- 0.12 % of all samples are above 0.8. The overall max, at (15.96, -0.08, 0.37), is the material inside the +X ear hole.
- The largest value outside that zone (0.765) is at (-4.65, -8.69, -22.07), on the -Y port junction/sleeve.
- CAD-to-scan distances are dominated by the unscanned interior: raw p95 is 1.53, and 0.651 for CAD points that face the scan.
- Loops: 1 of 3 used, with 2 builds. Build 2 only added a slot_count assert, so the geometry is unchanged. No loop 2: what remains is specimen damage, cosmetic marks or unscanned interior, and modelling it would not be design intent.

## 6. Skill defects found (file:line, what happened)
- **D1** `stl-re-intake-datum/SKILL.md:45-49`, `scripts/align.py:404`: the STOP comparison `fit_rms > noise` has no tie margin and no estimator precision. The primary (0.0357) and the tray-floor noise (0.0355) come from the same trimmed estimator (`datum_fit.py:179`, |d| < 2 tol), and their seed ranges overlap. The result was a STOP on a clean face, and the only way out was the self-referential noise path.
- **D2** `stl-re-measure-intent/scripts/param_table.py:37-44,199-200`: `_num()` averages a list, so the C9 critical-move check compares means. A symmetry param with a list `measured` can move each instance beyond noise and still pass. Worked around by holding critical per-instance values as keep-measured lists.
- **D3** `stl-re-measure-intent/scripts/fits.py:124-135` (theta box): arc-only circle fits (theta 60–120 deg) are ill-conditioned (centre drift) and give no warning or conditioning number.
- **D4** `stl-re-measure-intent/scripts/pattern_count.py:82,198`: the `mass` signal returned order 8, an edge harmonic of the 4 slots; the `radius` signal gave the correct 4. There is no harmonic or sub-multiple check.
- **D5** CLI (align.py, datum_fit.py, fits.py): vector arguments with a leading minus (`--plane-normal -0.43,...`, `--z -3.6,...`) are parsed as flags. They need `--arg=-0.43,...`, which is undocumented.
- **D6 (environment)** `stl-re-intake-datum/scripts/intake.py:192-194`: on the shared rclone/FUSE mount, the reload of the freshly exported `work.stl` hit FileNotFoundError 3 times. Worked around by running in a scratch mirror and copying the results with sha checks (`DECISIONS.md` OTHER). A side effect is that the JSON `inputs` keys hold scratch absolute paths.
- **D7 (environment)** `init_run.py`: chmod read-only on the inputs had no effect on the FUSE mount. The inputs were never written; their sha256 matches `input/INPUT_HASHES.json`.

## 7. Files
- `intake/`: alignment.json, regime.json, datum_spec.json, INTAKE_CARD.md, MEASUREMENTS.md (request, all absent), coverage.json, noise_*.json.
- `measure/`: params.json, PARAM_TABLE.md, figures/ (with the scripts in figures/src).
- `build/`: model.py, MODELING_PLAN.md, OD-H22_3-way-valve_datum.step, OD-H22_3-way-valve.step (scan frame), _cad.stl, export_check.json, fillets.json, face_stats.json, build_log.txt.
