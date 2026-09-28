# INTAKE CARD — OD-S02 steam rod (DeLonghi-type steam wand assembly)

Scan: `input/scan.stl` sha256 75cedf513bc86fcf51dfc22194a93a93f12857925e45854a095752be6f57c5e9. Working copy: `intake/work.stl`
(499164 faces, no decimation: the full scan is the working copy). Official gates run on
`input/scan.stl`. scan_resolution = **full** (owner confirmed "orijinal", DECISIONS.md).

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill**, material_class **plastic**: p95 ≤ 0.3 / max ≤ 0.8 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`). Tier-1 and interface bands: not in this regime (null).
Why: owner: 'p95 plastik parça toleransı kullan' (DECISIONS REGIME 2026-09-28); moulded plastic/rubber assembly with a steel tube, scan-only. No calipers (scan-only, DECISIONS.md MEASUREMENTS).

## 1. What it is (photos + mesh)
A coffee-machine steam wand assembly scanned as ONE mesh (owner decision PART-CLASS: one fused solid).
From photo_1/photo_2: a black tapered connector rod with O-ring seats (the machine interface), a black
ball-joint knob with a flat lever paddle (finger dish on the top face), a black sleeve with a sealing band
where the steel tube leaves the elbow, a Ø6 steel tube with one ~85° bend, a white bushing on the tube near
the tip, and a short steel tip with an open bore. Materials inferred from the photos (plastic/rubber black,
white plastic, stainless steel). The black part is torn at the knob/sleeve junction (photos: ragged flap).

## 2. Scan health (numbers from intake.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 499164 / 251631 |
| Bodies; kept; removed fragments % | 1; all; 0.0 |
| Scanner table removed % | 0.0 (none present) |
| Watertight; open boundary edges / loops | False; 4192 / 33 |
| Normal orientation | ray vote on the working copy (open mesh: volume sign is origin-dependent): outward, flipped False |
| bbox raw extents; datum extents | 106.59, 65.54, 71.37; 68.98, 25.73, 125.07 |
| Units verdict (CHK-SCALE) | finding: no calipers (scan-only, DECISIONS MEASUREMENTS): units assumed mm, scale unverified; re-run trigger: any caliper reading (>=3 ENV dims for a scale test) |
| Noise floors | plane: 0.0187 (rms of RANSAC+SVD plane on knob top face (annulus around rod) (6283 faces)); lever back face 0.0349; circle (IRLS, one loop): 0.0144 (rms of IRLS circle on rod taper circle z=30 (black plastic) at z=30.0 (n=376)); steel circle: 0.0514 (median Kasa rms of 13 slabs normal to the steel tube axis, segment between the bend and the white bushing (disjoint from the clock crop)) |
| Artefact zones | **D1 torn flash at the knob/sleeve junction** (datum x ≈ 6.5..13, both sides of the sleeve and above it, z ≈ -15..-1; photos show a torn rubber flap): specimen damage, not design geometry, not modelled — a named mask candidate for verify. Mould flash strands on the knob rim near the tube (photo_1). |

## 3. Coverage / occlusion map (datum frame; intake/coverage.json)
33 open-boundary loops. Largest: r 2.3..4.6, z 35.5..66.8, θ 180+79°; r 5.1..6.9, z 6.9..13.3, θ 143+158°; r 39.1..42.1, z -52.9..-43.7, θ -21+13°; r 8.6..14.0, z -12.9..-5.1, θ -32+17°; r 35.5..37.9, z -33.0..-30.4, θ -12+11°; r 35.8..40.8, z -57.6..-54.6, θ -22+7°.
Not observable: the bore of the tip beyond ~2.5 mm, the bushing underside windows beyond ~1.3 mm, the lever
plate faces under the knob, everything inside the assembly (hidden interfaces between the parts).

## 4. Functional surfaces & interfaces
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 | rod spigot taper + O-ring seats (z 21..67) | plugs into the machine steam outlet | yes (spigot Ø at a marked height) | regime p95/max |
| Z2 | steel tube Ø6 (B, bend, C) | tube OD for the bushing and the elbow | yes | regime |
| Z3 | lever paddle | operator handle | yes (thickness) | regime |
| Z4 | bushing + tip | steam outlet | yes | regime |

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh | Seen in photo | Status |
|---|---|---|---|---|
| 1 | rod tapered spigot with round nose | z 26..67 | photo_1/2 | both |
| 2 | O-ring on the spigot (z ≈ 27.3) | bump r 5.77 | photo_2 (ring) | both |
| 3 | step + cone z 21..26 | yes | photo_2 | both |
| 4 | rod body with bead/shallow groove z 9..21 | yes | photo_2 (O-rings) | both |
| 5 | groove z 6.8..9.2 | yes | photo_2 | both |
| 6 | lower collar + small rounded-rect lug at θ ≈ -90° | yes | photo_2 (small nub on the collar) | both |
| 7 | knob: cylinder + ellipsoidal bottom, fairing toward the sleeve | yes | photo_1/2 | both |
| 8 | lever paddle, round end, dished top face, dished underside | yes | photo_1/2 (dish visible on top) | both (underside mesh-only: dish found in the scan) |
| 9 | black sleeve (drafted) + sealing band | yes | photo_1/2 | both |
| 10 | steel tube B, bend, C | yes | photo_1/2 | both |
| 11 | white bushing (barrel), 6-spoke underside windows | yes | photo_1 (bushing), underside not photographed | mesh-only for the windows |
| 12 | steel tip with bore | yes | photo_1 (open tip) | both |
| 13 | torn flash at the junction (D1) | yes | photo_1/2 | both — damage, not modelled |
CHK-ENUM result: pass — both photos checked; material above the rod top: none (rod nose is the top); no unexplained cluster.

## 6. Datum plan and result (from alignment.json)
- Primary: axis — rod taper spigot (black connector, z 44..75 above the knob). WHY: the rod is the machine interface: tapered spigot + O-ring seats that plug into the steam outlet; every turned feature of the rod and the knob dome is coaxial with it. Fit (cone residual): rms 0.0255 / max 0.238 mm;
  section-circle refinement moved the normals-eigen axis by 0.582°.
- Secondary / clock: rule `axis_direction: steel tube leaving the elbow (Ø6 segment between the sleeve O-ring and the bend) -> +X`, angle -3.063°. WHY: the tube exit is the only functional non-coaxial axis; the lever paddle flat is noisier than the scan noise floor (noise_paddle_back 0.035 vs knob top 0.019). Clock axis rms 0.0495
  vs steel noise 0.0514; tube B elevation -8.464°.
- Origin: rod axis ∩ knob top face (annulus around the rod, facing the rod tip).
- Tilt (CHK-TILT): common slope, per-feature intercept, 40 stations over 2 feature(s), z 16.500..63.000 vs frame Z; NOT RESOLVABLE (heuristic): 'rod collar cylinder' (0.71 deg @ -54.3 deg) vs 'rod taper' (0.05 deg @ 32.0 deg) differ by 0.71 deg > combined stderr 0.06 deg — result finding (report-only).
- Landmarks: rod tip end above knob top (z max near axis): expected 67.3 / observed 67.257 / ok; tube tip end is below the knob (z min): expected -57.8 / observed -57.816 / ok.
- Status: OK. Findings: axis-primary radial residual not compared: no noise_secondary (circle noise) measured on a clean circle (plane noise is not comparable to a radial residual); secondary circle residual not compared: no noise_secondary measured on a clean circle (plane noise is not comparable to section-circle residuals). STOP-rule estimator mismatch recorded in DECISIONS.md (OTHER).

## 7. Rebuild strategy summary
Rod + knob: revolves about datum Z; knob fairing: non-ruled loft through fitted ellipse sections; lever: outline
sketch extruded and trimmed by two fitted planes, two sphere dishes; sleeve/band: revolves on their own fitted
axes; tube: one sweep (line–arc–line); bushing + tip: revolves on the tip axis, 6 window pockets. Plan:
`build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations
- One mesh of an assembly: hidden interfaces are not modelled; the STEP is one fused solid (PART-CLASS).
- D1 torn flash: excluded from the model; verify should report it with and without a named mask.
- The white bushing and the tip sit 4.8° off the steel tube C axis; kept as measured (bent tip or seating).
- No calipers: absolute scale not verified; Tier-1 not run.

## 9. Measurement request → `intake/MEASUREMENTS.md`
