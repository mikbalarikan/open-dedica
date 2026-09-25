# BUILDER REPORT: OD-S03_steam-knob (stl-re skills, builder stages only)

Stages run: intake → measure → rebuild (orchestrate §2). `intake*` was skipped because the run is
scan-only (DECISIONS.md MEASUREMENTS). Verify and deliver were **not** run (CHK-INDEP). There is no
`qa/` output and no `deliver/`. Nothing below is a gate verdict.
Regime: baseline-skill, plastic, p95 ≤ 0.30 / max ≤ 0.80 mm (`intake/regime.json`, written by
`intake.py regime`). `init_run.py status`: intake, measure and rebuild are complete. The input
sha256 is unchanged (`ce4a9dfc…`).

## 1. Intake (`intake/`)
- `intake.py stats`: 363,988 faces, 1 body, open (1,202 boundary edges in 17 loops, which are
  chrome scan holes). Ray-vote orientation: outward. **No decimation**, so `work.stl` is the
  full-resolution mesh.
- Datum (`alignment.json`, status **OK**):
  - Primary: the cap crown face → z = 0, with +Z toward the sleeve. rms 0.0146 against a plane
    noise of 0.0187, measured on the lever −Y flank (independent, not self-referential).
    The first run used the default 10° cone and read 0.0216 → **STOP**. The excess comes from the
    onset of the crown edge round; the seed sweep 0–5 was stable, so it was not a tie. I re-ran
    with `cone_deg: 3` (evidence `intake/alignment_attempt1_STOP.json`; DECISIONS OTHER).
  - Secondary: sleeve-envelope Kåsa sections + cap-wall IRLS. Median rms 0.0431 against a circle
    noise of 0.0436.
  - Clock: the lever goes to +X via `fourier_mass` n = 1, **area-weighted** through a scratch
    wrapper (defect D1). After the fix, the two flank planes read −0.64° / +1.03° about +X.
  - CHK-TILT: a finding, not resolvable (see D3). CHK-SCALE: FLAG.
- `INTAKE_CARD.md` has feature list E01–E20 (CHK-ENUM). `MEASUREMENTS.md` is the request, with
  scan-predicted values and every row ABSENT. `coverage.json` and `noise_*.json` are written.

## 2. Measure (`measure/params.json`, 71 params; `PARAM_TABLE.md` validator: 0 errors, 0 warnings)
- Scripts are in `measure/figures/src/`: `axes.py`, `stations.py`, `measure_all.py`, `jog.py`,
  `thread.py`, `lever.py`, `pocket.py`, `ribs.py`, `rib_tip.py`, `stem_base.py`, and
  `build_params.py`. `build_params.py` builds params.json from the JSONs, so no number is retyped.
- Sub-body axes are kept as measured positions in the frozen frame:
  - Cap: (0.032, −0.095). Tilt 0.07°, so it is Z-parallel.
  - Collar: (−0.117, −0.047).
  - Stem group (core, neck, sleeve, bore): one line through 20 station centres, tilted **0.754°**
    (residual rms 0.042). It sits 0.1–0.3 mm off the cap axis, which fits a cap + stem + sleeve
    assembly.
- Key values (mm/deg):

  | Param | Value | Rule |
  |---|---|---|
  | cap_R_z0 | 12.530 | keep-measured |
  | draft | 3.006 | mean-of-n of cap/flanks |
  | crown_round_R | 2.459 | mean-of-n |
  | step_z | 13.689 | mean-of-n |
  | collar_R | 11.116 | keep-measured |
  | stem core R | 5.317 → 5.159 | keep-measured |
  | neck_R | 4.736 | keep-measured |
  | rib_count | 4 | FFT order 4 at 3 stations, **CHK-COUNT pass** |
  | rib_theta_deg | −0.9 / 90.7 / 179.4 / −90.4 | keep-measured |
  | rib_width | 1.07 / 0.92 / 1.24 / 1.02 | keep-measured, tip full round |
  | pocket floor | 8.535 | keep-measured (floor seen by 64 faces) |
  | bore_R | 4.088 | keep-measured, critical |

- **Sleeve (thread) findings.** The ripple is **planar rings**, not a uniform helix:
  - Pitch 1.231, crest R 5.952, arc ρ 1.137, depth 0.181 (scanner-smoothed).
  - The crossover is at both ends: the bottom edge rises 1.059 over 132.6°→255.4° and the top
    edge rises 0.908 over 124.6°→245.4°. Both are right-hand, each ends in a step, and the fit rms
    is 0.073 / 0.056. This fits a formed coil.
  - The pitch, crest and bore values are critical, with a re-run trigger.
- Checks:
  - CHK-COUNT: pass.
  - CHK-CLUSTER: pass. The bore cluster is the planned shoulder E19. The E20 bore notch (≈0.5 deep)
    is declared.
  - CHK-FRAME: pass.
  - CHK-ACHIEVABLE: did not run; there are no readings.
- 16 simplifications are declared, each with its measured cost. There are 4 open questions.

## 3. Rebuild (`build/`)
- `MODELING_PLAN.md` was written first; the F01–F15 feature list maps E01–E20. `model.py` is
  params-driven, all params are used, and it has no geometry literals beyond the documented
  clearances OV 0.5, CUT_OVER 1.0 and EPS 0.02.
- Construction steps:
  - Cap cylinder ∪ lever outline (tip arc tangent to the flanks).
  - 2 blend fillets, then ONE `draft()` → planes and cones.
  - Crown round and step-edge round as loop fillets.
  - Drafted slot pocket.
  - Collar, stem and spigot revolves; the crest arcs are tori.
  - 4 ribs: slot section extruded along the measured tip line.
  - **Real helical geometry**: two helical sweeps, a bottom-ramp cut and a top tail. These gave a
    valid single solid.
- Result:
  - **1 valid closed solid in both frames.**
  - 88 faces, against a plan range of 85–160.
  - Volume **11,657.12 mm³**.
  - Surface types: plane 34, cone 15, torus 17, cylinder 11, revolution 1, B-spline 10. The
    B-splines are only on the helical ramps (1.4 % of area); the analytic area share is 0.986.
  - Fillets: 4 OK.
  - Exports: `_datum.step`, `.step` (scan frame), `_cad.stl`, `export_check.json` (pass,
    frames agree), `face_stats.json`, `fillets.json`, `build_log.txt`.
- There were 2 builds in one iteration. Build 2 only moved the tail tool EPS inside crest_R, to
  remove a 1e-6 mm² sliver face.

## 4. Builder self-check (NOT QA)
Full-res scan, scan frame, 200k seeded samples, unsigned distances; script
`build/selfcheck_NOT_QA.py`.

**scan→CAD:**

| rms | p50 | p95 | p99 | max |
|---|---|---|---|---|
| 0.110 | 0.030 | **0.178** | 0.353 | **2.302** |

1.5 % of samples are above 0.3 and 0.22 % are above 0.8.

- **Max cluster:** 392 samples at r 10.7–12.1, z 6.9–11, θ 100–108°. This is inside the cap wall,
  in intake hole B, and looks like bridged or collapsed chrome skin; the photos show an intact cap.
- **Second cluster:** the stem/collar crevice, r 5.25–6.2, z 15.0–16.0, θ −135..−45°, max 1.07
  (43 samples). The crevice floor depth varies about ±0.6 mm around θ.
- **Zone p95:** collar/grooves 0.347 (above the band locally), neck 0.232, sleeve 0.186, all other
  zones ≤ 0.16.

**CAD→scan raw:** p95 0.481. This includes the unscanned interior and the scan holes.

Expected verdict risk: the p95 band is likely met; **max 0.80 is likely missed** because of the
hole-B artefact and the crevice.

## 5. Skill/script defects found (repo not modified)
- **D1** `stl-re-intake-datum/scripts/align.py:247-259` (the phase at :255): `fourier_mass` sums
  vertex counts. It was biased 3.8° here by scan vertex density and holes. Workaround:
  `intake/workaround/align_areaw.py` monkeypatches only this branch to area-weighted face centres
  (DECISIONS OTHER).
- **D2** `align.py:366`: the axis-primary crop is an infinite radial cylinder, with no z window. On
  a stepped part it cannot "crop to one clean cylinder" as the skill requires. I used a plane
  primary instead.
- **D3** `align.py:102` (`wall_face_stations`): there is no θ exclusion. One-sided lever-root faces
  bias the IRLS centres, so the cap per-feature tilt read 1.46° against 0.13° from a lever-excluded
  cone fit. On the 3.25 mm span of the helical sleeve, per-feature tilt is unreliable.
- **D4** `stl-re-orchestrate/scripts/init_run.py:359-362`: `status` reports "scan-only needs a
  MEASUREMENTS decision" even though DECISIONS.md has one; it never reads DECISIONS.md.
- **D5** `stl-re-intake-datum/scripts/datum_fit.py:487`: `noise --circle-z` needs a closed loop.
  On the holed chrome neck no z worked, so I used the cap-mouth ring at z 14.0.
- **D6** Rebuild skill: there is no thread or helix guidance. `references/strategy-catalogue.md:123`
  lists "sweeps along 3D paths" among the HALT classes. Separately,
  `scripts/face_stats.py:180` labels helicoid sweep faces `ruled_like` with a "find the loft"
  note: a false positive for helical sweeps. I declared it in the plan.
- **D7** Known from OD-H22: the negative-vector CLI needs `--arg=-x,...`; I used that form.

## it2 (REVISE, route geometry; it1 in `_it1_SUPERSEDED/`)
- Finding: the 0.005 mm tessellation was not watertight at z≈15.99, r≈6.42, θ≈180°, where the rib
  foot touched the inner-groove torus along a line.
- Changes, both construction only; **params.json is unchanged**:
  - (1) F11 rib foot: `groove_in_bottom_z` → `groove_in_bottom_z − OV`. This covers all 4 ribs,
    which shared the tangent foot plane.
  - (2) F13 bottom-ramp tool floor: `zb − OV` → `zb − OV − sleeve_bottom_ramp_h`. My own 0.005 mm /
    0.1 rad check found a second non-manifold run in it1 at z = sleeve_bottom_z, θ≈193°. It was
    there in it1 but hidden at 0.05 rad. The shallow tool floor left an unintended wedge of sleeve
    material, up to ≈0.53 mm, under the ramp for θ 193°→255°.
- Result: 1 valid closed solid in both frames, **83 faces** (it1 88), volume **11,655.64 mm³** (it1
  11,657.12). Fillets 4 OK. B-spline faces 9, all on the ramps.
- **Watertight:** each STEP was tessellated at 0.003/0.005/0.01 mm × 0.1/0.05 rad. trimesh
  `is_watertight` is True with 0 non-manifold and 0 open edges, in both frames. `_cad.stl` is
  watertight too.
- Self-check (NOT QA): scan→CAD p95 0.178 / max 2.302, unchanged (the max is the hole-B artefact).
  CAD→scan raw p95 0.455.
- Script/verify note: at 0.005 mm the verifier's probe evidently used the finer angular deflection
  (0.05 rad), and at that setting the F13 defect does not show. A probe should sweep the angular
  deflection too.
