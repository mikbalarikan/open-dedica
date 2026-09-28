# BUILDER REPORT: OD-H21_antidrip-valve (stl-re skills @ 2e8e159)

Builder stages run: intake-datum, measure-intent, rebuild-build123d. Verify and deliver were **not** run
(CHK-INDEP), and `deliver/` was not created. Nothing below is a gate verdict. Regime: baseline-skill,
plastic, p95 ≤ 0.30 / max ≤ 0.80 mm (`intake/regime.json`, DECISIONS.md REGIME). Run type: scan-only,
no calipers (DECISIONS.md MEASUREMENTS). `scan_resolution` = full, by agent inference (DECISIONS.md OTHER).
Loops: 1 of 3 used, with 3 builds inside it (MODELING_PLAN.md §8).

## 1. Datum (`intake/alignment.json`, status OK)
- **Primary:** the band top face. This is the up-facing annulus (r 10–11.5) where the body cylinder
  leaves the band. It is z = 0, and +Z points to the cap. The trimmed fit is rms 0.0266 / max 0.1016;
  untrimmed it is 0.0256 / 0.1016 (7,175 faces, 52.6 mm²).
  - Why this face: the more functional nozzle shoulder reads rms 0.041–0.042 (seeds 0–7). That would
    STOP against any clean-flat noise floor (nozzle end face 0.0347, band top 0.0266).
  - The band-top normal agrees with the body axis within 0.11°.
- **Secondary / origin:** the nozzle OD axis (Kåsa, 15 stations, z −22…−15). Median rms is 0.0313, the
  worst station 0.1130. The circle noise is 0.0325, measured on a cap OD section.
- **Origin:** nozzle OD axis ∩ band top face plane.
- **Clock:** plane_normal of the side-outlet collar outer face → +X, 13.878°. That face fits to rms 0.0255
  and is 0.54° out of perpendicular to Z.
- **Noise floors:** plane 0.0347 (nozzle end face), circle 0.0325 (cap OD). The other flats read
  0.0266 / 0.0407 / 0.0457 (`intake/noise_*.json`).
- **CHK-TILT: finding.** The nozzle is 1.267° ± 0.032° off Z over 7.0 mm. This is real, not frame
  error: the body is square to Z (0.11°), and the cap part (ring + cap, one axis) is tilted 3.36°
  towards −31.9°.
  - The part is an **assembly scanned as one shell**, and each sub-part sits on its own axis. Nut, band
    and body centres are 0.07–0.25 mm apart.
  - The model keeps every sub-part pose as measured (keep-measured, intent-rules §5 "beyond noise,
    intent not clear").
- **CHK-SCALE: FLAG.** Units are assumed mm; no scale was applied.
- **Landmarks (all ok):** tip zmin −27.455, shoulder −14.033, cap top 23.480, barb top 28.483.
  Datum extents are 43.83 × 38.01 × 55.94.
- **matrix_4x4 (raw → datum), rows:**
  - [−0.788645, −0.218663, −0.574652, −110.011810]
  - [−0.150680, 0.974858, −0.164156, −17.568500]
  - [0.596099, −0.042872, −0.801765, −104.575327]

## 2. Feature tree (`build/MODELING_PLAN.md`, `build/model.py`)
Each sub-body is a revolve of one (r,u) profile about its **own measured axis**. The bodies are unioned,
then the cut tools are fused and subtracted once. Rounds are measured arcs inside the profiles, so there
are no 3D fillet operations.

| F | Operation | Result |
|---|---|---|
| F01 | Nozzle revolve (tilted 1.36°): tip face, tip round R0.52, OD R5.780, root fillet R0.51 | 6 faces |
| F02 | Corner lugs: RectangleRounded 11.27 × 11.93, corner R0.49, phi 23.97°, u −25.76…−23.12 | prism |
| F03 | Nut revolve: drafted cone (1.78°) + chamfer | ok |
| F04 | 8 rib rods, one instance at the 8 measured angles (CHK-COUNT pass, FFT order 8) | 8 placed |
| F05, F06, F07 | Lower band (drafted cone), upper band with top round, body cylinder R10.022 | ok |
| F08 / F08b | Cap part (ring R13.271 + cap R12.141, 4 profile rounds, tilted 3.36°); 2 skirt slits cut before the union | ok |
| F09 / F09b | Outlet revolve: tube R4.608, root fillet, collar R6.848 with R1.08 round, thread as a cylinder, end chamfer, end bore. Outlet→ring web as a pentagon prism | ok |
| F10 | O-ring torus (u 23.60, ρ 4.427, a 0.915), fused | ok |
| F11, F12 | Barb tube (drafted, rear round R0.93). Head: flare + bulb cone (half-angle 15.5°) on its measured offset axis, end bore | ok |
| F13, F14 | Union, then one fused cut: nozzle bore, 2 lug cut-backs + 1 deep latch window, 4 ring-window sectors | 1 solid |

- **Result:** 142 faces (expected 130–220), volume 19,368.65 mm³, area 6,005.8 mm².
- **Census:** analytic area share 1.0. Plane 73 / cylinder 36 / cone 22 / torus 11 faces.
  0 ruled-like faces, 0 free-form faces, no lofts.
- **`export_check.json`: pass.** Datum and scan frame are each 1 solid, valid and closed, with 0 naked
  edges. The frames agree (round-trip 2.9e-7 mm). `validate_step.py` passes on both STEPs.
- **`fillets.json`:** 0 entries. CHK-FILLET has nothing to report because all rounds are profile arcs
  (see §6 D4).

## 3. Key params (`measure/params.json`, 101 params; `PARAM_TABLE.md`, validator 0 errors / 0 warnings)
All values are scan authority and keep-measured. Estimators are recorded per param; the fits are in
`measure/figures/fits.json`, produced by `measure/figures/src/measure_all.py` and `make_params.py`.

| Param | Value | Note |
|---|---|---|
| noz_R / noz_bore_R | 5.7799 / 3.9415 | critical; nozzle Ø11.56 / bore Ø7.88 |
| lug_half_a / half_b / corner_R | 5.634 / 5.964 / 0.493 | critical (b) |
| nut_R0, nut_k / rib_rod_R | 10.8335, 0.0311 / 1.34–1.53 | ribs at 23.8° + 45k (±0.3°) |
| band_lo R0, k / band_up R / body_R | 12.2048, 0.051 / 12.0089 / 10.0218 | per-part centres kept |
| ring_R / cap_R / cap_top_u | 13.2709 / 12.1411 / 23.2744 | cap part tilt (2.855°, −1.775°) |
| out_tube_R / out_collar_R / O-ring (ρ, a) | 4.6084 / 6.8482 / (4.4273, 0.9153) | critical |
| out_thread_R / pitch | 4.4169 / 0.908 | 0.908 = 28 TPI (G1/8): identification only |
| barb_R0 / bulb_R0, k | 2.7516 / 3.3506, −0.2775 | bulb offset (0.174, −0.062) from the tube axis |
| win_theta / win_floor_rho | [−66.75, −0.25, 112.0, 180.0] / [12.07, 12.12, 11.35, 12.01] | per window |
| bore floors (nozzle / outlet / barb) | −23.406 / 29.211 / 27.283 | mid of the scanner-bridge p10..p90 |

**Checks:**
- CHK-COUNT pass (ribs).
- CHK-FRAME pass.
- CHK-ACHIEVABLE: nothing to test (no readings).
- **CHK-CLUSTER finding.** Three features were missed at intake and surfaced as self-check residual
  clusters: the outlet→ring web (E25), two skirt slits (E21) and the phi−90 lug cut-back (E23). They are
  now measured and modelled, and recorded in the INTAKE_CARD §10 addendum.

## 4. Limitations (declared)
- **Scan-only.** Absolute scale is unverified (CHK-SCALE FLAG); Tier-1 was not run.
- **Assembly modelled as scanned.** The sub-part poses are keep-measured: nozzle tilt 1.36°, cap part
  tilt 3.36°, centre offsets 0.07–0.25 mm. A nominal coaxial valve would be a different deliverable and
  would miss the band at the cap (≈0.7 mm).
- **No internals.** Internal flow passages and valve internals are not in the scan. The CAD is the outer
  envelope plus the observed openings; **it is not a functional flow part.**
- **Bores.** The three bores are blind recesses to the scanner bridge. Their floors are unobserved, which
  drives the CAD→scan max (§5).
- **O-ring.** Fused to the outlet as a torus: an invented connection of two real parts.
- **Thread.** Modelled as a plain cylinder at the mean radius. Its cost is ≤ 0.16 / 0.21 mm about the
  mean; the scanned profile is only 0.37 mm peak-to-peak.
- **Other simplifications, with their cost:**
  - skirt/body gap left closed except at the two slits: ≤ 0.5–0.66
  - web vertical walls: fit rms 0.18
  - nut→band transition as straight chamfers: max 0.38
  - barb flare as a cone: max 0.63
  - body out-of-round: max 0.30
  - small unmodelled edge rounds and the ring-top speckle: < 0.3
  - lug corner (−21°) extends 0.6 mm lower locally: flash or damage, not modelled

## 5. Builder self-check (NOT QA; `build/selfcheck.json`)
Method: frozen datum, no ICP. Full-res `input/scan.stl` against `build/<part>_cad.stl`, both in the scan
frame, unsigned distances in mm. 300k area-weighted scan samples; 150k CAD samples. "Facing" means the
outward-normal ray (voxel march) does not re-enter the CAD; that is 85.6 % of the CAD samples.

| Direction | rms | p50 | p95 | p99 | max | > 0.8 |
|---|---|---|---|---|---|---|
| scan→CAD | 0.091 | 0.041 | **0.183** | 0.317 | **1.060** | 0.03 % |
| CAD→scan raw | 0.192 | 0.044 | 0.265 | 0.721 | 3.205 | 0.84 % |
| CAD→scan facing | 0.168 | 0.040 | **0.189** | 0.401 | **3.205** | 0.56 % |
| CAD→scan facing, three bore floors left out (1.0 % of samples) | – | – | 0.175 | – | 0.808 | 0.001 % |

**p95 is inside the band in both directions. Max is not.**
- scan→CAD max 1.06: scanner bridging spread 1.7 mm deep inside the outlet end bore.
- CAD→scan max 3.21: the nozzle bore floor, which the scan never saw (open loop L1).

Everything else is ≤ 0.89: the latch-window and ring-window interiors (bridged), and the ring-bottom
gap. Zone p95 values run 0.07–0.30. The worst zone, the nozzle tip/lugs, is 0.30 scan→CAD and 1.71
CAD→scan: that is the bore floor.

Build history (3 builds, 1 loop):
- build 1: s2c p95 0.193 / max 1.55
- build 2: s2c max 1.34
- build 3: s2c p95 0.183 / max 1.06

What is left is scanner bridging or unscanned floor. Chasing it would model artefacts, not intent.

## 6. Skill defects found (file:line, what happened)
- **D1** `stl-re-intake-datum/scripts/align.py:358-367`: the axis-primary crop is radial only (an
  infinite cylinder `dist < crop_radius`, no axial window). On a stacked turned part it always includes
  the bore and the barb crossing the axis, so it can never isolate one cylinder. The result was a forced
  plane primary. A `crop_z` / u-range would fix this.
- **D2** `align.py:404, 465` (OD-H22 D1 still open): the STOP comparisons have no tie margin.
  - Plane: the functional shoulder (0.041) was rejected against 0.035 and 0.027 floors.
  - Circle: the origin circle passes 0.0313 vs 0.0325 by 0.001.
  - The noise floor itself spreads 0.027–0.046 across clean flats of the same scan.
- **D3** `stl-re-measure-intent/scripts/{sections,fits,pattern_count}.py`: every tool assumes features
  coaxial with datum Z. There is no local-frame or tilted-axis fit for assemblies or off-axis ports.
  Worked around with the run-local `measure/figures/src/mlib.py` (tilted cylinder/cone fits,
  local-frame profiles, (u,ρ) arc fits).
- **D4** `stl-re-rebuild-build123d/SKILL.md:185` (Step 4): the skill says to route every fillet through
  `FilletLog`, but gives no rule for rounds drawn as measured arcs in a revolve profile. CHK-FILLET is
  blind to them (`fillets.json` is empty here). Their radii are in `params.json` and MODELING_PLAN §5.
- **D5** `stl-re-measure-intent/scripts/param_table.py:26`: `UNITS = {mm, deg, count}` has no
  dimensionless unit. Draft slopes (mm/mm) and axis direction cosines had to be filed as `mm` with a note.
- **D6** CLI, OD-H22 D5 still open: `datum_fit.py noise --offset-range=-91.6 -91.0` fails silently
  (nothing parseable is printed). The `--offset-range -78.4 -77.8` form works.
- **D7** `stl-re-intake-datum/SKILL.md` Step 5 (CHK-ENUM) has no residual-driven pass. Three real
  features (web, slits, the second latch cut-back) were first found by the builder's self-check, not by
  enumeration.
- **D8 (risk for verify)** `stl-re-verify/scripts/observability.py:63-84` uses trimesh's pure-python
  `RayMeshIntersector`. In this environment the same engine was OOM-killed (13.9 GB) on the 518k-triangle
  CAD STL with 50k-ray chunks. Verify's 2k chunks on the far points should be fine, but the CAD STL
  tolerance 0.003 (`export_frames.py` default) makes it 26 MB.

## 7. Files
- **`intake/`:** intake.json, work.stl, datum_spec.json, alignment.json, aligned_work.stl, coverage.json,
  noise_primary.json, noise_circle.json, noise_plane_*.json, regime.json, INTAKE_CARD.md (with the §10
  addendum), MEASUREMENTS.md (request; all rows ABSENT).
- **`measure/`:** params.json, PARAM_TABLE.md, figures/ (fits.json, planar/radial/maps JSON+NPZ+PNG,
  count_nut_ribs.json, src/mlib.py, src/measure_all.py, src/make_params.py).
- **`build/`:**
  - model: MODELING_PLAN.md, model.py, build_log.txt
  - STEP and mesh: OD-H21_antidrip-valve_datum.step, OD-H21_antidrip-valve.step (scan frame),
    OD-H21_antidrip-valve_cad.stl
  - checks: export_check.json, fillets.json, face_stats.json
  - self-check (not QA): selfcheck.py, selfcheck.json, selfcheck_map.png, selfcheck_render_{cad,scan}.png
- **Reproduce:**
  `python build/model.py --params measure/params.json --alignment intake/alignment.json --out build --part OD-H21_antidrip-valve --scripts <repo>/skills/stl-re-rebuild-build123d/scripts`

---

# it2 (REVISE, route geometry, gate dd052135f7c2): loop 2 of 3

Scope: only the three geometric findings in `_it1_SUPERSEDED/qa/gate.json#miss_explanations`. Datum,
intake and every other parameter and op are unchanged. The bore floors and the outlet bore bridge are
not touched (coverage facts, per the orchestrator).

New run-local code:
- `measure/figures/src/measure_it2.py` → `measure/figures/fits_it2.json`
- `measure/figures/src/make_params_it2.py` overlays `params.json`: each changed row carries an
  `it1 -> it2` note, and `params.json#revisions` lists what changed and what was removed.
- `PARAM_TABLE.md` regenerated: 103 params, 0 errors, 0 warnings.

## Param diffs vs _it1 (values; it1 rows remain in `_it1_SUPERSEDED/measure/params.json`)
| Param | it1 | it2 |
|---|---|---|
| `latch_theta0_deg` / `latch_theta1_deg` | [77.97, −102.03] / [149.97, −30.03] | removed |
| `latch_floor_rho` | [5.7188, 5.7779] (cylindrical floor) | removed |
| `latch_deep_theta` / `latch_deep_floor_rho` | [89.97, 113.97] / 4.7929 | removed |
| `latch_cut_d` | — | [5.4247, 5.5724] (plane floor ∥ lug b-flat) |
| `latch_cut_y0` / `latch_cut_y1` | — | [−4.3929, −4.1991] / [4.0878, 4.0486] |
| `latch_through_theta` | — | [82.97, 137.97] (through into the bore) |
| `win_theta_deg` / `win_width_deg` | [−66.75, −0.25, 112.0, 180.0] / [16.5, 17.5, 18.0, 13.0] | removed |
| `win_theta0_deg` / `win_theta1_deg` | — | [−74.75, −8.25, 103.0, 174.0] / [−58.75, 8.75, 121.0, −173.0] |
| `win_u_lo` | [12.2869, 12.2855, 12.1798, 12.4642] | [12.4, 12.4, 12.4, 12.6] |
| `win_u_hi` | [14.8568, 14.1629, 14.5205, 14.4293] | [14.6, 14.0, 14.4, 14.2] |
| `win_floor_rho` | [12.0722, 12.1231, 11.3465, 12.0094] | [11.9258, 12.1263, 11.4953, 11.9058] |
| `win_deep_theta` / `win_deep_u` / `win_deep_floor_rho` | — | [104, 116] / [12.8, 14.0] / 10.5134 |
| `slit_theta0_deg` | [−159.9594, 146.4008] | [−158.135, 151.6072] |
| `slit_theta1_deg` | [−126.933, 172.8675] | [−140.135, 172.6072] |
| `slit_u_top` | [10.9686, 11.0493] | [10.8622, 10.9502] |
| `slit_rho_in` | [10.1105, 10.1075] | [10.0568, 10.0127] |
| `slit_rho_out` | [11.0966, 10.9822] | [10.7359, 10.6312] |

Estimators (full text in `params.json`):
- **Latch.** 1° envelope bins vs the fitted lug outline.
  - The cut-back floor is a plane: d = median(env·cos Δθ).
  - The through span is the bins with no nozzle-wall vertex.
- **Windows.** An occupancy map of the outer skirt surface in the cap frame.
  - Span = open in ≥ 50 % of rows / columns.
  - Floor = median per-cell minimum radius over cells at r ≥ 11.
  - Cells at r < 11 form the deep sector.
- **Slits.** The scanned slit ceiling: 1° bins above ring_bottom + 0.9.
  - The open loops L5/L7 alone under-cut: trimming to them gave s2c 1.20 / 1.34, so it was not kept.

## Build
- **Solid:** 146 faces, volume 19,376.50 mm³.
- **Export:** 1 solid in each frame, valid and closed, 0 naked edges; `export_check.json` passes;
  `validate_step.py` passes on both STEPs.
- **Census:** analytic area share 1.0, 0 ruled-like faces; `fillets.json` has 0 entries.
- **Artefacts:** `build_log.txt`, `face_stats.json`, both STEPs and `_cad.stl` were regenerated.
- **Plan:** `MODELING_PLAN.md §9` records the it2 changes.

## Self-check it2 (NOT QA; same method as §5)
| Direction | rms | p95 | p99 | max | > 0.8 |
|---|---|---|---|---|---|
| scan→CAD | 0.089 | **0.182** | 0.309 | **1.060** | 0.02 % |
| CAD→scan raw | 0.187 | 0.257 | 0.624 | 3.205 | 0.74 % |
| CAD→scan facing | 0.168 | **0.187** | 0.401 | **3.205** | 0.59 % |

Zones named in the findings, it1 → it2:
- **Nozzle tip/lugs:** s2c max 0.885 → 0.775.
- **Ring (windows, slits):**
  - s2c p95 0.249 → 0.236 and max 0.891 → 0.661.
  - c2s facing p95 0.166 → 0.160 and max 0.808 → 0.780.
- The old slit-ceiling and latch clusters are gone.

Regions still over 0.8, all bore interiors (not rebuild targets):
1. The nozzle bore floor, which the scan never saw (c2s up to 3.21).
2. The nozzle bore wall above the scan's observed wall end at θ −45…−66, u ≈ −24.5 (c2s up to 1.74).
   The new through-window makes it visible to the normal-ray test.
3. The outlet bore scanner bridge (s2c 1.06; c2s 0.92).
4. The barb bore floor (c2s 0.81).

Leaving out bore interiors 1, 3 and 4, CAD→scan facing is p95 0.174 but its max is 1.735, because item 2
is not covered by that exclusion.
