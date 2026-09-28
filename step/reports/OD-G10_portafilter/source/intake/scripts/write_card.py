"""Render intake/INTAKE_CARD.md and intake/MEASUREMENTS.md (request) with numbers read from the
intake JSON files and measure/figures (never retyped)."""
import json
I = json.load(open('intake/intake.json')); A = json.load(open('intake/alignment.json')); C = json.load(open('intake/coverage.json'))
G = json.load(open('intake/regime.json')); H = json.load(open('input/INPUT_HASHES.json'))
bp = json.load(open('measure/figures/body_profile.json')); ln = json.load(open('measure/figures/lugs_notches.json'))
ha = json.load(open('measure/figures/handle_axis.json')); hp = json.load(open('measure/figures/handle_profile.json')); ss = json.load(open('measure/figures/spouts_screw.json'))
rw = I['raw_welded']; dec = I['decimation']; ob = C['open_boundary_loops']
f = lambda v, n=3: f"{v:.{n}f}"
card = f"""# INTAKE CARD — OD-G11 portafilter (DeLonghi-style pressurised portafilter)

Scan: `input/scan.stl` sha256 {H['inputs']['input/scan.stl']}. Working copy: `intake/work.stl`
({dec['from_faces']} → {dec['to_faces']} faces, work-vs-full p95 {f(dec['work_vs_full_dev_mm']['p95'],4)} / max {f(dec['work_vs_full_dev_mm']['max'])} mm, seed {dec['work_vs_full_dev_mm']['seed']}).
Official gates run on the full-resolution original (owner confirmed "orijinal export", DECISIONS.md 2026-09-28), never on the working copy.

## 0. Band regime
Regime: **{G['name']}**, material class **{G['material_class']}**: p95 ≤ {G['bands']['p95_mm']} / max ≤ {G['bands']['max_mm']} mm (`{G['source']}`).
Why: {G['why']} Declared before any gate numbers exist (DECISIONS.md REGIME).

## 1. What it is
Espresso portafilter as one assembly: cast aluminium cup with three bayonet lugs, two spout bosses with pan-head
screws at the tips and a countersunk-looking centre screw on the bottom; an open-bottom arch neck; a black tapered
plastic grip with a collar and a cream end cap; inside, a black pressurised insert (funnel floor, a U rib, two
diagonal ribs, two outlet pockets) and a round-wire retaining spring visible through the rim bore. Photos 1.webp
(inside, top) and 2.webp (bottom). Static part; the rim end face seats on the group gasket (functional datum).
Materials inferred from the photos. Owner decision: ONE fused solid of the whole scanned assembly (DECISIONS PART-CLASS).

## 2. Scan health (intake.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | {rw['faces']} / {rw['verts']} |
| Bodies; kept; removed fragments % | {I['bodies']}; all; {I['removed']['fragments_pct']} |
| Scanner table removed % | {I['removed']['table_pct']} (no table in the scan) |
| Watertight; open boundary edges / loops | {rw['watertight']}; {rw['open_boundary_edges']} / {rw['open_boundary_loops']} |
| Normal orientation | {I['orientation']['method']}: {I['orientation']['verdict']}, flipped {I['normals_flipped']} |
| bbox raw extents; datum extents | {[round(v,2) for v in rw['extents']]}; {[round(v,2) for v in A['extents_aligned']]} |
| Units verdict (CHK-SCALE) | {A['checks']['CHK-SCALE']['note']} |
| Noise floor | {f(A['scan_noise_mm']['value'],4)} mm, {A['scan_noise_mm']['method']}; independent flat (handle end cap): see `intake/noise_primary.json` |
| Artefact zones | spout pockets and neck channel are open holes (unscanned); wire spring ends dive out of sight |

## 3. Coverage (coverage.json, datum frame)
| r band | z | θ covered | Note |
|---|---|---|---|
""" + "".join(f"| {round(b['r'][0],1)}–{round(b['r'][1],1)} | {round(b['z'][0],1)}..{round(b['z'][1],1)} | {b['theta_covered_deg']}° | {'cup: full' if b['theta_covered_deg']>=359 else 'lugs / neck / handle (non-round by design)'} |\n" for b in C['radial_bands']) + f"""
Open-boundary loops: {len(ob) if isinstance(ob, list) else ob} (the spout pockets inside the cup, the neck channel roof end and small gaps).
Occluded (from sections): the spout pocket interiors below z≈-43.5, one flank of each rib, the wire behind the bore.

## 4. Functional surfaces
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| RIM | rim end face z = 0 | seats on the group gasket (datum primary) | height gauge | regime band |
| LUGS | 3 lug outer radii and under-face ramps | bayonet engagement | yes (lug-to-wall, feeler) | regime band |
| BORE | rim bore r≈{f(bp['bore_upper']['a'],2)} and ledge z≈{f(bp['ledge_z']['median'],2)} | basket seat | yes (ID, depth) | regime band |
| SPOUTS | spout tips, spacing | cup clearance | yes | regime band |

## 5. Feature enumeration (CHK-ENUM)
| # | Feature | Mesh | Photo | Status |
|---|---|---|---|---|
| 1 | cup body: drafted outer wall, rim, spherical bottom, bottom round | yes | 1, 2 | both |
| 2 | rim bore, ledge, taper to the insert wall | yes | 1 | both |
| 3 | three bayonet lugs ({', '.join(str(l['centre_deg']) for l in ln['lugs'])} deg) with ramped under-faces | yes | 1, 2 | both |
| 4 | two rim notches ({', '.join(str(n['start_deg']+n['span_deg']/2) for n in ln['rim_notches'])} deg) | yes | not visible | mesh-only: small notches in the rim face, accepted as real (clean, symmetric, flat floor) |
| 5 | flat pad on the +X wall above the neck | yes | 2 | both |
| 6 | open-bottom arch neck, handle collar, tapered grip, end cap | yes | 1, 2 | both |
| 7 | two spout bosses with pan-head screws (θ {f(ss['spout_0']['theta_deg'],1)}, {f(ss['spout_1']['theta_deg'],1)}) | yes | 2 | both |
| 8 | centre screw with cross recess on the bottom | yes | 2 | both |
| 9 | insert funnel floor, U rib, 2 diagonal ribs, 2 outlet pockets | yes | 1 | both (pocket interiors occluded → assumed) |
| 10 | retaining wire spring (3 exposed arcs) | yes | 1 | both |
| 11 | cast lettering on the bottom (faint) | barely | 2 | not modelled (cosmetic, < noise-level relief) |
CHK-ENUM: both photos checked; nothing above the rim plane (z max {f(A['extents_aligned'][2],2)} extent) or on the axis unexplained.

## 6. Datum (alignment.json)
- Primary: {A['primary']['mesh_region_desc']} → z = 0, material −z. WHY: {A['primary']['why']}. Fit rms / max {f(A['primary']['fit_rms_mm'],4)} / {f(A['primary']['fit_max_mm'],4)}.
- Secondary: {A['secondary']['mesh_region_desc']}. Fit rms / max {f(A['secondary']['fit_rms_mm'],4)} / {f(A['secondary']['fit_max_mm'],4)}.
- Clock: {A['clock']['rule']}, angle {f(A['clock']['angle_deg'],3)}°.
- Origin: {A['origin']['definition']}.
- Tilt (CHK-TILT): {f(A['tilt_deg']['value'],3)} ± {f(A['tilt_deg']['stderr_deg'],3)}° over {f(A['tilt_deg']['z_span_mm'],1)} mm → {A['checks']['CHK-TILT']['result']} (report-only).
- Landmarks: """ + "; ".join(f"{L['name']} exp {L['expected']} obs {round(L['observed'],3)} ok={L['ok']}" for L in A['sanity_landmarks']) + f"""
- Status: {A['status']}. Findings: {A.get('findings')}.
- STOP-rule note: the first datum run used the handle end-cap flat as the noise reference
  (0.02207 mm) and stopped because the rim fit rms was 0.02245 mm (a 0.4 µm tie; same known defect as OD-H22
  D1, no tie margin). Re-run with the noise measured on the rim itself; align.py records it as a finding.

## 7. Rebuild strategy summary
Cup: one revolved (r,z) profile about Z (outer + bore + insert cavity walls), funnel floor = vertical-axis cone cut,
U plateau + ribs as sub-bodies; lugs = annular sectors cut by ramp planes; pad = offset reverse-draft cone ∩ wedge;
handle = revolve about the fitted handle axis (neck cone, collar, grip cone, end chamfer); arch neck = cylinder minus
channel slot, cut at the foot plane; spouts = revolves about their own axes; screws = spherical caps with cross recesses.

## 8. Risks / operator declarations
Scan-only: no calipers, scale unverified (CHK-SCALE FLAG). Unscanned: spout pockets, neck channel interior end,
wire ends. The assembly is delivered as one fused solid (owner). Soft features: none.

## 9. Measurement request → `intake/MEASUREMENTS.md`
"""
open('intake/INTAKE_CARD.md', 'w').write(card)
req = f"""# MEASUREMENTS — OD-G11 portafilter (request)

Instrument: caliper (state model/resolution) · Date measured: — · Status summary: 0 of 8 rows carry a value; the
owner chose a scan-only run (DECISIONS.md MEASUREMENTS 2026-09-28), so every row is ABSENT, not passed.

## A. Envelope
| ID | Feature | Jaw placement | Scan says | Reading | Status |
|---|---|---|---|---|---|
| ENV-X | rim centre to handle end, along the handle | jaws on lug 180° outer face and handle end face | {f(A['extents_aligned'][0],2)} (datum extent) | | absent |
| ENV-Y | across lugs 59.5°/300.5° is not diametral; use cup OD below lugs | cup OD at z≈-10 | {f(2*(bp['outer_wall']['a']+bp['outer_wall']['b']*-10),2)} | | absent |
| ENV-Z | rim face to spout tip | depth rod | {f(-ss['spout_0']['tip_zmin'],2)} | | absent |

## B. Functional
| ID | Feature | Datum ref | Scan says | Reading | Status |
|---|---|---|---|---|---|
| F01 | rim bore ID just above the ledge | cup axis | {f(2*(bp['bore_upper']['a']+bp['bore_upper']['b']*-9),2)} | | absent |
| F02 | ledge depth from the rim | rim face | {f(-bp['ledge_z']['median'],2)} | | absent |
| F03 | lug under-face height at both ends of a lug | rim face | see measure/figures/details.json#lug_ramps | | absent |
| F04 | spout centre distance | — | {f(abs(ss['spout_0']['cy']-ss['spout_1']['cy']),2)} | | absent |
| F05 | grip OD at the collar end and at the cap | handle axis | {f(2*(ha['r_linear']['r_at_x0']+ha['r_linear']['slope']*50),2)} / {f(2*(ha['r_linear']['r_at_x0']+ha['r_linear']['slope']*155),2)} | | absent |
"""
open('intake/MEASUREMENTS.md', 'w').write(req)
print('ok')
