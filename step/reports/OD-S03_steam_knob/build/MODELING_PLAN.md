# MODELING PLAN: OD-S03_steam-knob

<!-- Written by stl-re-rebuild-build123d BEFORE build/model.py. Iteration: it2 of 3 (carried forward from it1 by
     `init_run.py supersede --route geometry`; it1 intact in _it1_SUPERSEDED/). -->

## 0. Build deviations (filled after the build)

See §8 "Build result" at the end (filled after build 1). Empty rows here = none at plan time.

| Item | Planned | Built | Why | Declared to verify/deliver |
|---|---|---|---|---|
| fillets | 4 fillet ops at target | 4 OK, 0 reduced/failed | — | export_check.json#fillets |
| unused params | none | none ("all params used", build_log.txt) | — | — |
| B-spline faces | only on the helical ramp sweeps | 10 B-spline faces, all on the sleeve ramps (z 32.6–37.7); 8 counted `ruled_like` by face_stats.py (build 2) | a helical sweep of a straight profile edge is a helicoid (ruled by nature); no loft, no scan slices | yes (this plan, build_log) |
| sliver face (build 1 only) | — | build 1: 1 B-spline face of 1.2e-6 mm² at the tail-sweep start (θ≈126°, z≈36.6); build 2: removed (smallest face 0.013 mm²) | F14 tool face was tangent to the top crest torus at r = crest_R; build 2 holds that tool face EPS (0.02) inside | yes (change log) |
| REVOLUTION face | — | 1 (crown round on the drafted lever-tip cone, 42.4 mm²) | OCC fillet of a cone edge | yes |
| lever tip | tangent arc (derived) | R 4.437 at z 0 (fitted tip circle 4.588): tip x max 27.08 vs scan ≈27.2 at z 2.5 | design-intent tangency | measure simplification "lever tip tangent to flanks" |

## 1. Strategy summary

A turned knob with one radial lever, modelled as four coaxial-group sub-bodies fused into one
solid (the physical part is a cap + stem + sleeve assembly; each group keeps its *measured* axis
position in the frozen datum frame, `measure/params.json` cap_*/collar_*/stem_axis_*):
(1) **cap + lever**: one plan sketch (cap circle ∪ lever outline with a tangent round tip), extruded
crown→step face, concave blends filleted, then ONE mould draft on every side face (planes → tilted
planes, cylinders → cones), crown round and step-edge round as loop fillets, and a drafted
slot-shaped pocket cut; (2) **collar** revolve (mouth chamfer, ring face, collar, bottom face with a
groove); (3) **stem** revolve (flange face, inner groove, core cone, shoulder) + 4 rib instances at
measured angles; (4) **spigot** revolve (neck, sleeve with 4 touching crest arcs, bore + shoulder)
+ two helical sweeps (bottom ramp cut, top tail) for the measured coil-like crossover.
Catalogue rows used: revolve (D2), sub-bodies unioned (D3), one instance + placements (D4), cut
tools (D5), sketch + extrude (DRM/OD), fillets logged (D7/D8). Sweeps along a helix: no golden
precedent (strategy-catalogue.md:123) — used only for the two measured end ramps (§7).

## 2. Expectations (reported, not gated)

- Expected ops before fillets: **13** (cap cyl, lever prism, union, draft, pocket tool+draft+cut,
  collar revolve, stem revolve, rib pattern (1 op), spigot revolve, ramp cut sweep, tail sweep,
  final union).
- Expected face count: **85–160**. Estimate: cap+lever after draft 8 side + crown 1 + step 1
  → crown-loop fillet ~8 + step-loop fillet ~8 (≈26); pocket 4 walls + 2 corners + floor (7);
  collar revolve ≈ 11; stem revolve ≈ 7; ribs 4 × ~6 = 24; spigot revolve ≈ 16 (4 crest tori +
  rounds + bore); ramps ≈ 8–12; boolean splits +10–30.
- Expected surface types: planes, cylinders, cones, tori; B-spline only on the two helical ramp
  sweeps (helicoidal faces) — not lofts.

## 3. Ordered feature list

Frames: cap centre (`cap_cx`,`cap_cy`); collar centre (`collar_cx`,`collar_cy`); stem centre =
stem-axis line (`stem_axis_x0/y0/tilt_deg/dir_deg`) evaluated at z = (`stem_base_z`+`stem_core_top_z`)/2;
spigot centre = same line at z = (`neck_bot_z`+`sleeve_top_z`)/2. All sources `scan` unless noted.

| F## | Operation | Datum / plane | Driving params (source) | Acceptance (checkable on the STEP) |
|---|---|---|---|---|
| F01 | cap cylinder, crown→step | XY @ `crown_z`, cap centre | `cap_R_z0`, `crown_z`, `step_z` (mean-of-n) | cap Ø at z 0 = 2·cap_R_z0 before draft |
| F02 | lever plan sketch + extrude | XY @ `crown_z` | `lever_flank_py_y0`, `lever_flank_py_plan_deg`, `lever_flank_my_y0`, `lever_flank_my_plan_deg`, `lever_tip_cx` (tip arc tangent to both flanks, centre on their bisector) | tip x max ≈ 27.3 at z 0 |
| F03 | union cap ∪ lever | — | — | 1 solid |
| F04 | concave blend fillets (2 vertical junction edges) — local, before draft | edges flank∩cap | `lever_blend_R_py_z0`, `lever_blend_R_my_z0` | fillet_log OK |
| F05 | draft all side faces, neutral plane z = crown_z, widening toward +Z | XY @ crown_z | `draft_deg` (mean-of-n) | side faces are PLANE/CONE; cap r(z=step) = R0 + step·tan(draft) |
| F06 | crown loop fillet (all edges at z = crown_z) | — | `crown_round_R` (mean-of-n) | OK |
| F07 | step-face outer loop fillet (edges at z = step_z) | — | `step_edge_R` (mean-of-n) | OK |
| F08 | pocket tool: slot sketch at step_z (square inner end with corner rounds, semicircular outer end), extruded to the floor, drafted, subtracted | XY @ step_z | `pocket_x_inner_at_step`, `pocket_end_cx`, `pocket_y_plus_at_step`, `pocket_y_minus_at_step`, `pocket_floor_z`, `pocket_corner_R`, `pocket_draft_deg` | pocket floor z = pocket_floor_z |
| F09 | collar revolve (r,z) | collar centre | `step_z`, `mouth_chamfer_r_out/_r_in`, `mouth_ring_z`, `collar_R`, `collar_top_round_R`, `collar_bot_round_R`, `collar_bot_z`, `groove_out_rc/_R/_bottom_z`, `flange_z`, `groove_in_*` (join radius) | collar r = collar_R |
| F10 | stem revolve (r,z) | stem centre | `mouth_ring_z`, `flange_z`, `groove_in_rc/_R/_bottom_z`, `stem_base_z`, `stem_core_R_base/_top`, `stem_core_top_z`, `neck_R`, `neck_bot_z` | core r at base/top = params |
| F11 | rib instance (slot section extruded along the measured tip line) × `rib_count` at `rib_theta_deg` | stem centre | `rib_width`, `rib_tip_r_flange`, `rib_tip_r_top`, `rib_top_z`, `groove_in_bottom_z` − OV (rib foot, buried; it2), `neck_R` (buried inner face) | 4 ribs, count == rib_count |
| F12 | spigot revolve (r,z): neck, sleeve bottom round (R = first crest − bottom), n touching crest arcs, top round (R = top − last crest), bore, shoulder cone, floor | spigot centre | `neck_R`, `stem_core_top_z`, `sleeve_bottom_z`, `sleeve_top_z`, `sleeve_crest_R`, `sleeve_ripple_rho`, `sleeve_ripple_pitch`, `sleeve_first_crest_z`, `bore_R`, `bore_shoulder_top_z`, `bore_floor_r`, `bore_floor_z` | crest count = floor((top−c1)/p)+1 |
| F13 | bottom ramp cut: swept tool (region below the rounded sleeve bottom, floor at zb − OV − h; it2) along a right-hand helix rising `h` over [start,end] | spigot centre | `sleeve_bottom_ramp_start_deg/_end_deg/_h` | step at end angle |
| F14 | top tail: swept profile (rounded top corner) along a helix rising `h` over [start,end], unioned | spigot centre | `sleeve_top_ramp_*`, `sleeve_tail_r_in` | z max ≈ top + h |
| F15 | union all sub-bodies, clean, export both frames | — | — | 1 valid closed solid (export_check.json) |

Documented construction constants in model.py (clearances, not geometry): `OV = 0.5` mm burial
overlap for sub-body joins; `CUT_OVER = 1.0` mm tool overshoot; `EPS = 0.02` mm tangent/coincident
clearance for the ramp tools (heuristic, n=1: B02 `build_OOM-B02.py:182-185`).

## 4. Intake feature map (CHK-ENUM)

| Intake feature (INTAKE_CARD.md §5) | Built by F## | or: out of scope because |
|---|---|---|
| E01 crown face | F01/F02 (z = crown_z) | |
| E02 crown edge round | F06 | |
| E03 cap wall drafted | F01 + F05 | |
| E04 lever wing | F02 + F05 | |
| E05 lever-cap blends | F04 (+F05) | |
| E06 lever pocket | F08 | floor shape assumed flat (seen by 64 faces) |
| E07 step face | F01/F02 top at step_z | |
| E08 step outer edge round | F07 | |
| E09 mouth bead/ring | F09 (chamfer + ring face + concave round) | |
| E10 collar | F09 | |
| E11 collar bottom face + groove | F09 | |
| E12 annular crevice at stem base | F10 (inner groove arc) | |
| E13 stem core | F10 | non-roundness declared |
| E14 4 ribs | F11 | |
| E15 stem-neck shoulder | F10 | |
| E16 neck | F12 (+F10 shoulder) | |
| E17 sleeve ripple + helical ends | F12 + F13 + F14 | ripple as rings (declared) |
| E18 sleeve top face | F12 | inner lip not modelled (declared ≤0.1) |
| E19 bore + shoulder | F12 | floor closure assumed |
| E20 bore notch θ≈180° | — | not modelled: declared simplification (≈0.5 mm deep, ≈25°) |

## 5. Fillet / chamfer plan (CHK-FILLET)

| F## | Edges (selector rule) | Target param | Fallback radii (reason) | Order |
|---|---|---|---|---|
| F04 | vertical LINE edges with centre radius from cap centre within [cap_R_z0 − 1, cap_R_z0 + 1] and y > 0 (+Y) / y < 0 (−Y) | `lever_blend_R_py_z0`, `lever_blend_R_my_z0` | none | local, before F05 (draft needs the blend faces) |
| F06 | all edges with centre z = crown_z (±1e-3) | `crown_round_R` | none | local, after draft, before pocket/union (edges destroyed by later unions otherwise) |
| F07 | all edges with centre z = step_z (±1e-3) on the cap+lever body (before the collar union) | `step_edge_R` | none | local, before F09 union (the step face gains an inner boundary after it) |
| F08 | 2D fillet of the two pocket inner-end corners in the sketch | `pocket_corner_R` | none | in the tool sketch |
| F09/F12 | rounds inside the revolve profiles (arcs: collar top/bottom, sleeve bottom/top, crest arcs, grooves) | profile params | — | exact in the profile, not fillet ops |

## 6. Unscanned or invented geometry (provenance)

| Item | Value | Source tag | Why it is needed |
|---|---|---|---|
| bore floor (flat disc) | at `bore_floor_z`, r ≤ `bore_floor_r` | assumed shape (z, r from scan: deepest observed) | the scan bore is open (no floor seen); a closed solid needs a closure |
| solid interior (cap/stem/sleeve internal interfaces) | solid | assumed | the scan is an outer skin; the deliverable is one fused solid |
| sub-body burial overlaps | OV = 0.5 mm | construction clearance | joins between the four coaxial groups must overlap (no zero-thickness union) |
| rib inner face | at r = `neck_R` (inside the core) | construction (buried) | rib must overlap the core |
| lever root | lever sketch starts at x = `cap_cx` (inside the cap) | construction (buried) | lever must overlap the cap |

## 7. Known risks

- Helical sweeps (F13/F14): no golden precedent; if the sweep or its boolean fails, fall back to
  flat sleeve ends at the measured levels and declare the cost (≈1 mm local at the step, would
  exceed the 0.8 max locally) — report it.
- Draft (F05) with a fillet-blended outline: if BRepOffsetAPI_DraftAngle fails, report and try
  drafting before the blend fillets (blends then as fillets on cones).
- Four sub-body axes 0.1–0.3 mm apart: small steps/slivers at the joins (collar↔cap step face,
  stem↔collar flange face at z = flange_z, stem shoulder↔spigot neck). Report face count.
- Pocket floor seen sparsely; ripple scanner-smoothed (true thread depth unknown) — declared.
- E20 notch and the top inner lip not modelled — declared.

## 8. Change log / build result

- Build 1 (it1): model.py ran first time; no plan changes. 1 valid closed solid in both frames,
  89 faces (plan 85–160, in range), volume 11,657.41 mm³; surface census (export_check.json):
  plane 35 (27.3 % area), cone 15 (38.6 %), torus 17 (21.7 %), cylinder 11 (9.7 %), revolution 1
  (1.1 %), B-spline 10 (1.5 %, helical ramps only). fillet_log: 4 OK.
- Builder self-check (NOT QA; scan frame, full-res scan, 200k seeded samples, unsigned closest
  point): scan→CAD rms 0.110, p50 0.030, p95 0.178, p99 0.353, max 2.302; 1.5 % > 0.3, 0.22 % > 0.8.
  Max cluster = 392 samples at r 10.7–12.1, z 6.9–11.0, θ 100–108° inside the cap wall, i.e. inside
  intake hole B (collapsed/bridged chrome skin; photos show an intact cap) — not modelled.
  Second cluster = stem/collar crevice (r 5.25–6.2, z 15.0–16.0, θ −135..−45°): the crevice floor
  depth varies ±0.6 mm around θ and is partly unscanned; the median groove arc leaves ≤1.07 mm
  (43 samples > 0.8). Not changed: deepening the groove would open new misses where the floor is
  seen shallow. Zone p95: crown 0.071, cap 0.160, lever 0.146, step/mouth 0.100, collar/grooves
  0.347, stem 0.156, neck 0.232, sleeve/bore 0.189.
- Build 2 (same iteration, one change): F14 tail-tool outer face moved EPS inside crest_R to remove the
  build-1 sliver. Result: 88 faces, volume 11,657.12 mm³, 1 valid closed solid in both frames; B-spline 10
  (1.4 % area, ramps only), analytic area share 0.986; fillets 4 OK. Self-check (NOT QA) unchanged:
  scan→CAD p95 0.178 / p99 0.353 / max 2.302; CAD→scan raw p95 0.481 (includes the unscanned
  interior and scan holes). The tail OD is 0.02 mm under crest_R (documented clearance).
- No loop 2: remaining misses are a scan artefact and an as-assembled crevice that one revolve
  cannot represent; both declared.

### it2 (REVISE, route geometry) — diff vs it1

Finding (`_it1_SUPERSEDED/qa/VERDICT.md`, `qa/tess_probe.json`): the 0.005 mm tessellation is not
watertight; non-manifold edges at z≈15.99, r≈6.42, θ≈180°: the rib foot touches the inner-groove
torus along a line.

Changes (construction only; **no parameter changed**, params.json identical to it1):
1. **F11 rib foot**: `zlo = groove_in_bottom_z` → `groove_in_bottom_z − OV` (OV = 0.5, the
   documented burial clearance). In it1 each rib's flat foot face lay exactly on the torus bottom
   circle (z = groove_in_bottom_z), which gave a line contact. All 4 ribs shared that foot z, so the fix
   covers every rib. The foot now sits inside solid material, so the visible geometry does not change.
2. **F13 bottom-ramp tool floor**: `zb − OV − EPS` → `zb − OV − sleeve_bottom_ramp_h − EPS`. My own
   check at 0.005 mm with a 0.1 rad angular deflection found a second non-manifold run in it1
   (z = sleeve_bottom_z, θ≈193° local, r ≈ crest_R − Rb). The verifier's probe missed it; it appears
   in it1 at 0.1 rad but not at 0.05 rad. Cause: the tool floor was only OV (0.5) below zb while the
   ramp rises 1.059. From θ≈193° to the step at 255.4° the tool floor rose above zb. That left an
   unintended wedge of sleeve material up to ≈0.53 mm thick under the ramp, and the tool face grazed
   the bottom plane at θ≈193°. The deeper floor removes both.

Result (it2): 1 valid closed solid in both frames; **83 faces** (it1 88: the 4 rib-foot faces and 1
wedge face are gone; 2 below the plan estimate 85–160, which is reported, not gated); volume
**11,655.64 mm³** (it1 11,657.12; −1.47 mm³ = the removed wedge); surface types plane 30, cone 15,
torus 17, cylinder 11, revolution 1, B-spline 9 (helical ramps only), analytic area share 0.987;
fillets 4 OK; all params used. Watertightness (builder, `build/tess_check_NOT_QA.py` + inline
check): each exported STEP tessellated at 0.003 / 0.005 / 0.01 mm and 0.1 / 0.05 rad →
trimesh `is_watertight` True, **0 non-manifold, 0 open edges**, in both frames; `_cad.stl`
watertight. Self-check (NOT QA): scan→CAD p95 0.178 / max 2.302, the same as it1 (the max cluster is
the hole-B scan artefact); CAD→scan raw p95 0.455 (it1 0.481).
