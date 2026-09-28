#!/usr/bin/env python3
"""OD-S02 run-local: render intake/INTAKE_CARD.md and intake/MEASUREMENTS.md from the intake JSON
files (numbers copied, never retyped: CHK-NUMBERS spirit)."""
import json
from pathlib import Path
run = Path(__file__).resolve().parent.parent
I = json.loads((run / "intake/intake.json").read_text())
A = json.loads((run / "intake/alignment.json").read_text())
G = json.loads((run / "intake/regime.json").read_text())
Cv = json.loads((run / "intake/coverage.json").read_text())
H = json.loads((run / "input/INPUT_HASHES.json").read_text())
NK = json.loads((run / "intake/noise_knobtop.json").read_text())["scan_noise_mm"]
NP = json.loads((run / "intake/noise_paddle_back.json").read_text())["scan_noise_mm"]
NC = json.loads((run / "intake/noise_circle.json").read_text())["scan_noise_mm"]
NS = json.loads((run / "intake/noise_steel.json").read_text())["scan_noise_mm"]
w = I["working_full"]; t = A["tilt_deg"]; cl = A["clock"]; pr = A["primary"]
f = lambda x, n=3: f"{x:.{n}f}"
lm = "; ".join(f"{l['name']}: expected {l['expected']} / observed {f(l['observed'])} / {'ok' if l['ok'] else 'FAIL'}" for l in A["sanity_landmarks"])
loops = Cv["open_boundary_loops"]["largest"]
card = f"""# INTAKE CARD — OD-S02 steam rod (DeLonghi-type steam wand assembly)

Scan: `input/scan.stl` sha256 {H['inputs']['input/scan.stl']}. Working copy: `intake/work.stl`
({I['raw_welded']['faces']} faces, no decimation: the full scan is the working copy). Official gates run on
`input/scan.stl`. scan_resolution = **{H['scan_resolution']}** (owner confirmed "orijinal", DECISIONS.md).

## 0. Band regime (declared here, named again in the verdict)
Regime: **{G['name']}**, material_class **{G['material_class']}**: p95 ≤ {G['bands']['p95_mm']} / max ≤ {G['bands']['max_mm']} mm
(`{G['source']}`). Tier-1 and interface bands: not in this regime (null).
Why: {G['why']}. No calipers (scan-only, DECISIONS.md MEASUREMENTS).

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
| Faces / verts (welded) | {w['faces']} / {w['verts']} |
| Bodies; kept; removed fragments % | {I['bodies']}; all; {I['removed']['fragments_pct']} |
| Scanner table removed % | {I['removed']['table_pct']} (none present) |
| Watertight; open boundary edges / loops | {w['watertight']}; {w['open_boundary_edges']} / {w['open_boundary_loops']} |
| Normal orientation | {I['orientation']['method']}: {I['orientation']['verdict']}, flipped {I['normals_flipped']} |
| bbox raw extents; datum extents | {', '.join(f(x,2) for x in w['extents'])}; {', '.join(f(x,2) for x in A['extents_aligned'])} |
| Units verdict (CHK-SCALE) | {A['checks']['CHK-SCALE']['result']}: {A['checks']['CHK-SCALE']['note']} |
| Noise floors | plane: {f(NK['value'],4)} ({NK['method']}); lever back face {f(NP['value'],4)}; circle (IRLS, one loop): {f(NC['value'],4)} ({NC['method']}); steel circle: {f(NS['value'],4)} ({NS['method']}) |
| Artefact zones | **D1 torn flash at the knob/sleeve junction** (datum x ≈ 6.5..13, both sides of the sleeve and above it, z ≈ -15..-1; photos show a torn rubber flap): specimen damage, not design geometry, not modelled — a named mask candidate for verify. Mould flash strands on the knob rim near the tube (photo_1). |

## 3. Coverage / occlusion map (datum frame; intake/coverage.json)
{Cv['open_boundary_loops']['count']} open-boundary loops. Largest: """ + "; ".join(
    f"r {f(l['r'][0],1)}..{f(l['r'][1],1)}, z {f(l['z'][0],1)}..{f(l['z'][1],1)}, θ {f(l['theta_start_deg'],0)}+{f(l['theta_span_deg'],0)}°" for l in loops[:6]) + f""".
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
- Primary: axis — {pr['mesh_region_desc']}. WHY: {pr['why']}. Fit (cone residual): rms {f(pr['fit_rms_mm'],4)} / max {f(pr['fit_max_mm'],3)} mm;
  section-circle refinement moved the normals-eigen axis by {f(pr['refine']['normals_eigen_vs_refined_deg'],3)}°.
- Secondary / clock: rule `{cl['rule']}`, angle {f(cl['angle_deg'],3)}°. WHY: {cl['why']}. Clock axis rms {f(cl['detail']['fit_rms_mm'],4)}
  vs steel noise {f(cl['detail']['noise_ref']['value'],4)}; tube B elevation {f(cl['detail']['axis_elevation_deg'],3)}°.
- Origin: {A['origin']['definition']}.
- Tilt (CHK-TILT): {t['method']} — result {A['checks']['CHK-TILT']['result']} (report-only).
- Landmarks: {lm}.
- Status: {A['status']}. Findings: {'; '.join(A['findings'])}. STOP-rule estimator mismatch recorded in DECISIONS.md (OTHER).

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
"""
(run / "intake/INTAKE_CARD.md").write_text(card)
P = json.loads((run / "measure/params.json").read_text())["params"] if (run / "measure/params.json").exists() else {}
v = lambda k: P.get(k, {}).get("value")
meas = f"""# MEASUREMENTS — OD-S02 steam rod (request; scan-only run)

Instrument: none supplied. Date measured: not measured (owner proceeded scan-only, DECISIONS.md MEASUREMENTS).
Status summary: 0 of 6 rows carry a value; all are ABSENT, not passed. Any reading triggers a re-run
(CHK-SCALE needs ≥3 ENV rows).

"Scan says" is the scan-predicted value in the datum frame.

## A. Envelope
| ID | Feature | Jaw placement | Scan says | Reading (mm) | Status |
|---|---|---|---|---|---|
| ENV-1 | rod nose to knob top face, along the rod | depth rod on the knob top face | {v('rod_tip_z')} | | absent |
| ENV-2 | knob cylinder Ø | across the knob just below the top face | {2*v('knob_r'):.3f} | | absent |
| ENV-3 | lever plate thickness at the round end rim | outside jaws across the plate rim | ≈5.2 (fitted planes) | | absent |

## B. Functional dimensions
| ID | Feature | Datum ref | Why | Scan says | Reading | Status |
|---|---|---|---|---|---|---|
| F01 | spigot Ø at 10 mm below the nose | rod axis | machine interface | {2*(v('rod_taper_r_z30') + v('rod_taper_drdz')*(v('rod_tip_z')-10-30)):.3f} | | absent |
| F02 | steel tube OD | tube | bushing/elbow fit | {2*v('tube_r'):.3f} | | absent |
| F03 | bushing max Ø | tip axis | outlet part | {2*max(v('bush_barrel_r')):.3f} | | absent |
"""
(run / "intake/MEASUREMENTS.md").write_text(meas)
print("written")
