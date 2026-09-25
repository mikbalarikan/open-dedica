# MODELING PLAN: OD-H22_3-way-valve

Iteration: it1 of 3. Written before `build/model.py`. Every number comes from
`measure/params.json` (scan-only run: every measured value is `source: scan`, rule and
estimator in `measure/PARAM_TABLE.md`). Port lists are ordered [+Y port, −Y port].

## 0. Build deviations (filled after the build)

Filled after it1 (build_log.txt, fillets.json, face_stats.json). No fillet was reduced or
dropped (5/5 OK at target radius). Face count 162 (in 140–260). 1 valid closed solid.

| Item | Planned | Built | Why | Declared to verify/deliver |
|---|---|---|---|---|
| `slot_count` | drives the slot pattern | used as an assert on the per-instance lists (slot angles/widths are held per instance, C9) | first build logged it UNUSED | yes (BUILDER_REPORT) |
| F05 cone bottom | from cone angle | z −7.172, r 4.074 (derived, logged) | as planned | — |
| F06 gusset bottom at axis | from angle | z −10.490 (derived, logged) | as planned | — |

## 1. Strategy summary

A moulded 3-way valve: flange plate + axisymmetric drive tube/stem + two angled ports.
(1) The flange is ONE XY sketch (disc `plate_R` ∪ two tapered ears whose ends are circles
`ear_end_R` about each ear hole) extruded to the rim top; the tray is the same sketch offset
inward by `rim_wall_t` and pocketed down to the floor (OD-H12 hull+offset idiom). (2) The core
(stem cylinder, 40° cone, neck, collar, drive tube) is ONE revolved (r,z) profile about Z.
(3) Each port is ONE revolved (r,t) profile about its own measured axis, plus a square clip
block; bores, tube slots, clip slots and ear holes are cut tools subtracted last. Mirror
symmetry is NOT forced: ear holes, slot angles/widths and port angles are held per instance
(critical interfaces, C9). Strategy rows: revolve (D2), sub-bodies unioned (D3), one
instance + placements (D4), cut tools (D5), sketch+extrude / hull+offset.

## 2. Expectations (reported, not gated)

- Expected ops before fillets: **12** (F01–F12).
- Expected face count **140–260**: flange side walls 12 + top/bottom 2 + tray walls ~12 + floor
  1 + back-edge round ~12 + blends 8; core revolve ~10; tube bore 2 + slots 4×3; ear holes 2;
  gussets 2×3; per port: neck/step/sleeve/lip/end ~7 + block 6 + corner rounds 4 + bores 4 +
  clip slots 2×4 ≈ 29 → 58; rib 5; boolean splits ~+20.
- Surface types: planes, cylinders, cones; tori only from fillets; no B-spline expected.

## 3. Ordered feature list

| F## | Operation | Datum / plane | Driving params (source) | Acceptance (checkable on the STEP) |
|---|---|---|---|---|
| F01 | flange outline sketch (disc ∪ 2 ears), extrude z 0 → `rim_top_z` | XY @ z=0 | `plate_R`, `ear_hole_x`[2], `ear_end_R`, `ear_side_angle_deg`, `rim_top_z` (scan) | bbox x ≈ ear_hole_x ± ear_end_R; top z = rim_top_z |
| F02 | fillet the 4 concave vertical disc/ear edges | vertical edges at the corners | `outline_blend_R` (scan) | fillet_log OK |
| F03 | fillet the bottom outer edge loop (local: before any body is fused to the back face) | edges at z=0 on the outline | `back_edge_R` (scan) | fillet_log OK |
| F04 | tray pocket: same sketch offset inward by `rim_wall_t`, blends `outline_blend_R + rim_wall_t`, cut z `flange_floor_z` → top | XY | `rim_wall_t`, `flange_floor_z` (scan) | floor z = flange_floor_z; rim wall = rim_wall_t |
| F05 | core revolve (r,z): stem cyl `stem_R` to `stem_cone_top_z`, cone to `stem_neck_R` (cone angle `stem_cone_half_angle_deg` gives the cone bottom), neck down to `stem_neck_bottom_z`; collar `collar_R` to `collar_top_z`; tube `tube_R` to `tube_top_z` | axis Z | all listed (scan) | 1 solid after union; radii on STEP = params |
| F06 | gussets: XZ triangle (0,0)-(`gusset_x_at_z0`,0)-(0,−x·tan `gusset_angle_deg`), extruded ±`gusset_t`/2, at +X and mirrored to −X | XZ plane | `gusset_*` (scan) | two webs, thickness gusset_t |
| F07 | port body ×2: revolve (r,t) about each port axis: neck `port_neck_R` t 0→`port_sleeve_t`, sleeve `port_sleeve_R` → `port_block_t1`, lip `port_lip_R` → `port_end_t` | per-port plane: origin (0,0,`port_axis_z0`), t = (0, ±cos e, −sin e), e = `port_elev_deg` | port_* (scan) | per-port axis angle = param |
| F08 | clip block ×2: box 2·`port_block_half_u` × 2·`port_block_half_v` over t `port_block_t0`→`port_block_t1`, 4 axial edges rounded `port_block_corner_R` (local fillet on the tool, then fused) | port frame | `port_block_*` (scan), corner R (assumed) | block flats = params |
| F09 | bottom rib: box `rib_t` × 2·`rib_half_len`, z `rib_bottom_z` → `stem_neck_bottom_z`+1 (top buried in the stem) | XY | `rib_t`, `rib_bottom_z` (scan), `rib_half_len` (assumed, buried) | flat bottom at rib_bottom_z |
| F10 | cut tools, fused, subtracted once: tube bore `tube_bore_r` from `tube_bore_bottom_z`; 4 tube slots at `slot_theta_deg`[i], width `slot_w`[i], floor `slot_bottom_z_x` (θ≈0/180) / `slot_bottom_z_y` (θ≈90/270); ear holes r `ear_hole_r` at `ear_hole_x`[i] | Z / XY | slot_* (scan, per instance), tube_bore_bottom_z (assumed) | 4 slots, bore open to the top |
| F11 | port cut tools ×2: bore `port_bore_R` from `port_bore_step_t` to the mouth; bore `port_bore2_R` from `port_bore2_end_t` to the step; 2 clip slots: stadium in the (t,v) plane, t `port_block_t0+port_slot_dt0` … +`port_slot_w`, v ±[`port_slot_v_in`, `port_slot_v_out`], ends radius `port_slot_w`/2, through along X | port frame | port_bore*, port_slot_* (scan), bore2 end (assumed) | 2 slots per port through the block, bores open at the mouth |
| F12 | `.clean()`, export both frames | — | alignment.json | 1 valid closed solid in both frames |

Allowed operations only (sketch/extrude/revolve/boolean/fillet). No loft, no polyline stacks.
Straight profile polygons are param-vertex profiles, not scan slices.

## 4. Intake feature map (CHK-ENUM)

| Intake feature (INTAKE_CARD.md §5) | Built by F## | or: out of scope because |
|---|---|---|
| E01 flange plate + ears | F01, F02 | |
| E02 back-edge round | F03 | |
| E03 tray rim wall | F04 | |
| E04 ear holes | F10 | |
| E05 boss collar | F05 | |
| E06 drive tube + 4 slots | F05, F10 | |
| E07 tube-bore floor / web | F10 (blind bore to `tube_bore_bottom_z`, assumed) | web not scanned: not modelled |
| E08 stem, cone, neck | F05 | |
| E09 gussets | F06 | |
| E10 Y-junction + ports | F07 | junction = boolean union of stem neck and port necks |
| E11 neck→sleeve step | F07 | |
| E12 clip block + slots | F08, F11 | |
| E13 lip + bore | F07, F11 | |
| E14 bottom rib | F09 | |
| E15 ejector-pin circles | — | cosmetic, ~0.3 mm; declared simplification in params.json |
| E16 internal flow passages | — | not in the scan; not invented |

## 5. Fillet / chamfer plan (CHK-FILLET)

| F## | Edges (selector rule) | Target param | Fallback radii (reason) | Order |
|---|---|---|---|---|
| F02 | vertical LINE edges of the flange prism whose midpoint lies in the concave corner window (|x| between the disc/ear line intersection ±2, |y| > 4) — 4 expected | `outline_blend_R` | none | local, before F03/F04 (F04 needs the blended outline) |
| F03 | edges with both vertices at z=0 on the outer outline (after F02) | `back_edge_R` | none | local, before the stem/gussets are fused to the back face (they would split this edge loop) |
| F04 tool | same as F02 on the pocket prism | `outline_blend_R + rim_wall_t` (derived: inward offset of a concave blend) | none | on the tool, before the cut |
| F08 tool | 4 box edges parallel to the port axis | `port_block_corner_R` (assumed) | none | on the tool, before the fuse |

## 6. Unscanned or invented geometry (provenance)

| Item | Value | Source tag | Why it is needed |
|---|---|---|---|
| tube-bore floor | z = `tube_bore_bottom_z` 1.5 | assumed | bore bottom not scanned; blind bore ends at the lowest scanned wall |
| port inner bore end | t = `port_bore2_end_t` 12.5 | assumed | passage to the junction not scanned |
| rib length | `rib_half_len` 4.5 | assumed | ends buried in the sleeves; no outer-surface effect |
| block corner rounds | `port_block_corner_R` 0.5 | assumed | visibly rounded, not fitted |
| clip-slot rounded ends | radius `port_slot_w`/2 | photo-inferred (photo_4 oblong slots) | end shape not fitted |
| internal flow passages | none | — | not invented (E16) |

## 7. Known risks

- Port revolve and block booleans at oblique axes: coincident faces avoided by overshooting
  every cut tool by a documented 1.0 mm clearance and by starting the port neck at t=0 inside
  the stem cylinder.
- F02 selector may catch the wrong vertical edges if the ear lines meet the disc elsewhere;
  the log asserts 4 edges. F03 may fail at the tight blend/round junction: reported, not hidden.
- Lower body is ~0.1–0.17 mm off-axis in the scan (CHK-TILT ≈0.5°); the model is coaxial by
  intent (declared simplification) — verify will see it as a systematic offset on the stem/ports.

## 8. Change log

- it1: initial plan.
- it1 build 1: valid solid, 162 faces; `slot_count` logged UNUSED.
- it1 build 2: `slot_count` asserted against the per-slot lists; geometry unchanged (volume
  6395.59 mm³). Builder self-check (not QA) scan→CAD p95 0.234 / max 1.419; the max lies in the
  damaged +X ear (scan material inside the +X ear hole at z 0.06–0.65, absent in the −X hole);
  outside that zone p95 0.222 / max 0.765. No loop 2: remaining hotspots are the declared
  simplifications (ejector circles, +X ear damage, coaxial lower body) and unscanned interior;
  modelling them would add specimen damage or cosmetic marks, not design intent.
