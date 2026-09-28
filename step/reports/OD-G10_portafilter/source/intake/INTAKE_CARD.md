# INTAKE CARD — OD-G11 portafilter (DeLonghi-style pressurised portafilter)

Scan: `input/scan.stl` sha256 9eb34045f9be50df2320a989f96fc1135a7a75e1d4cc9ac673b2e1bfce0c30aa. Working copy: `intake/work.stl`
(500182 → 299999 faces, work-vs-full p95 0.0047 / max 0.321 mm, seed 0).
Official gates run on the full-resolution original (owner confirmed "orijinal export", DECISIONS.md 2026-09-28), never on the working copy.

## 0. Band regime
Regime: **baseline-skill**, material class **plastic**: p95 ≤ 0.3 / max ≤ 0.8 mm (`baseline/skills/stl2step-build123d/SKILL.md:87`).
Why: Owner instruction 'p95 plastik parça toleransı kullan' (2026-09-28); scan-only job. Declared before any gate numbers exist (DECISIONS.md REGIME).

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
| Faces / verts (welded) | 500182 / 250812 |
| Bodies; kept; removed fragments % | 1; all; 0.0 |
| Scanner table removed % | 0.0 (no table in the scan) |
| Watertight; open boundary edges / loops | False; 1488 / 15 |
| Normal orientation | ray vote on the working copy (open mesh: volume sign is origin-dependent): outward, flipped False |
| bbox raw extents; datum extents | [183.4, 109.73, 113.17]; [201.6, 69.21, 59.14] |
| Units verdict (CHK-SCALE) | FLAG: no calipers (scan-only, DECISIONS MEASUREMENTS 2026-09-28); units assumed mm, scale unverified, none applied |
| Noise floor | 0.0224 mm, rms of RANSAC+SVD plane on cup rim end face (sealing face, incl. lug tops in the same plane) (3756 faces); independent flat (handle end cap): see `intake/noise_primary.json` |
| Artefact zones | spout pockets and neck channel are open holes (unscanned); wire spring ends dive out of sight |

## 3. Coverage (coverage.json, datum frame)
| r band | z | θ covered | Note |
|---|---|---|---|
| 0.0–16.6 | -58.7..-26.7 | 360.0° | cup: full |
| 16.6–33.2 | -59.1..0.1 | 360.0° | cup: full |
| 33.2–49.9 | -46.3..0.1 | 146.0° | lugs / neck / handle (non-round by design) |
| 49.9–66.5 | -44.2..-17.5 | 37.0° | lugs / neck / handle (non-round by design) |
| 66.5–83.1 | -44.6..-17.2 | 24.0° | lugs / neck / handle (non-round by design) |
| 83.1–99.7 | -44.9..-17.0 | 20.0° | lugs / neck / handle (non-round by design) |
| 99.7–116.3 | -45.4..-16.8 | 17.0° | lugs / neck / handle (non-round by design) |
| 116.3–132.9 | -45.9..-16.6 | 15.0° | lugs / neck / handle (non-round by design) |
| 132.9–149.6 | -46.4..-16.5 | 14.0° | lugs / neck / handle (non-round by design) |
| 149.6–166.2 | -46.6..-16.2 | 12.0° | lugs / neck / handle (non-round by design) |

Open-boundary loops: {'count': 15, 'largest': [{'n_vertices': 276, 'r': [10.381240608796844, 23.41808539719607], 'z': [-44.058109283447266, -28.96917152404785], 'theta_start_deg': -104.17889021416507, 'theta_span_deg': 95.33786660598003}, {'n_vertices': 203, 'r': [6.279473346176221, 19.518218734987702], 'z': [-40.615318298339844, -27.03582191467285], 'theta_start_deg': -38.52716427664006, 'theta_span_deg': 197.92171065245174}, {'n_vertices': 155, 'r': [13.839351647854942, 23.254550819661116], 'z': [-44.962467193603516, -29.122913360595703], 'theta_start_deg': 15.442697055941752, 'theta_span_deg': 85.25435193915803}, {'n_vertices': 153, 'r': [24.703959184291218, 27.472385187382237], 'z': [-6.3956685066223145, -3.272951126098633], 'theta_start_deg': -120.4887442403306, 'theta_span_deg': 54.454971838848735}, {'n_vertices': 151, 'r': [102.59108174743773, 160.66116473534828], 'z': [-41.09000778198242, -28.18575096130371], 'theta_start_deg': 4.131491656356432, 'theta_span_deg': 3.2608336943139875}, {'n_vertices': 122, 'r': [23.772617304618137, 27.209506754484213], 'z': [-6.341574192047119, -3.6592705249786377], 'theta_start_deg': 108.27530543199877, 'theta_span_deg': 60.077687918392655}, {'n_vertices': 85, 'r': [12.42572689016436, 22.950700515006297], 'z': [-36.657718658447266, -28.169233322143555], 'theta_start_deg': -172.31526513128674, 'theta_span_deg': 14.889595279662899}, {'n_vertices': 64, 'r': [4.433218080233104, 5.943450421568733], 'z': [-32.97264862060547, -28.695390701293945], 'theta_start_deg': -63.38371914655367, 'theta_span_deg': 88.77074581655313}, {'n_vertices': 29, 'r': [4.720472339665783, 5.885421187171972], 'z': [-33.75020980834961, -29.11302947998047], 'theta_start_deg': -123.5838798855928, 'theta_span_deg': 54.95168657016063}, {'n_vertices': 22, 'r': [25.70073654344429, 27.38121444553496], 'z': [-4.5697150230407715, -3.2970330715179443], 'theta_start_deg': 6.236900784039626, 'theta_span_deg': 9.072967323140688}, {'n_vertices': 17, 'r': [27.85940300385059, 28.518497347931756], 'z': [-3.3391385078430176, -2.2806217670440674], 'theta_start_deg': -77.84226537625159, 'theta_span_deg': 6.94421510284792}, {'n_vertices': 10, 'r': [27.341330264723755, 27.84694095065802], 'z': [-3.363863706588745, -2.389814853668213], 'theta_start_deg': -114.5424568092001, 'theta_span_deg': 4.803892775745908}, {'n_vertices': 9, 'r': [26.865939199884863, 27.25681856110834], 'z': [-6.450789451599121, -4.785458564758301], 'theta_start_deg': -98.44227680087285, 'theta_span_deg': 3.7057576817729796}, {'n_vertices': 9, 'r': [40.11610827389905, 41.167676456351586], 'z': [-29.74555206298828, -26.946361541748047], 'theta_start_deg': -7.911516768358192, 'theta_span_deg': 2.137339328920291}, {'n_vertices': 8, 'r': [162.80868807828637, 165.25592266356688], 'z': [-34.5743408203125, -32.64558410644531], 'theta_start_deg': 3.985891215336559, 'theta_span_deg': 0.6320426422034302}]} (the spout pockets inside the cup, the neck channel roof end and small gaps).
Occluded (from sections): the spout pocket interiors below z≈-43.5, one flank of each rib, the wire behind the bore.

## 4. Functional surfaces
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| RIM | rim end face z = 0 | seats on the group gasket (datum primary) | height gauge | regime band |
| LUGS | 3 lug outer radii and under-face ramps | bayonet engagement | yes (lug-to-wall, feeler) | regime band |
| BORE | rim bore r≈27.90 and ledge z≈-11.53 | basket seat | yes (ID, depth) | regime band |
| SPOUTS | spout tips, spacing | cup clearance | yes | regime band |

## 5. Feature enumeration (CHK-ENUM)
| # | Feature | Mesh | Photo | Status |
|---|---|---|---|---|
| 1 | cup body: drafted outer wall, rim, spherical bottom, bottom round | yes | 1, 2 | both |
| 2 | rim bore, ledge, taper to the insert wall | yes | 1 | both |
| 3 | three bayonet lugs (59.5, 180.0, 300.5 deg) with ramped under-faces | yes | 1, 2 | both |
| 4 | two rim notches (90.0, 270.0 deg) | yes | not visible | mesh-only: small notches in the rim face, accepted as real (clean, symmetric, flat floor) |
| 5 | flat pad on the +X wall above the neck | yes | 2 | both |
| 6 | open-bottom arch neck, handle collar, tapered grip, end cap | yes | 1, 2 | both |
| 7 | two spout bosses with pan-head screws (θ 56.3, -56.8) | yes | 2 | both |
| 8 | centre screw with cross recess on the bottom | yes | 2 | both |
| 9 | insert funnel floor, U rib, 2 diagonal ribs, 2 outlet pockets | yes | 1 | both (pocket interiors occluded → assumed) |
| 10 | retaining wire spring (3 exposed arcs) | yes | 1 | both |
| 11 | cast lettering on the bottom (faint) | barely | 2 | not modelled (cosmetic, < noise-level relief) |
CHK-ENUM: both photos checked; nothing above the rim plane (z max 59.14 extent) or on the axis unexplained.

## 6. Datum (alignment.json)
- Primary: cup rim end face (sealing face, incl. lug tops in the same plane) → z = 0, material −z. WHY: the rim end face seats against the group-head gasket; it is the functional axial datum of a portafilter. Fit rms / max 0.0224 / 0.0976.
- Secondary: cup outer wall (drafted) + cup rim bore above the basket flange. Fit rms / max 0.0269 / 0.1266.
- Clock: plane_normal: handle end-cap flat normal -> +X, angle -25.423°.
- Origin: cup axis (outer wall) ∩ rim end-face plane.
- Tilt (CHK-TILT): 0.262 ± 0.113° over 28.9 mm → pass (report-only).
- Landmarks: primary plane at z=0 exp 0.0 obs 0.003 ok=True; spout boss tips (part bottom) exp -59.0 obs -59.074 ok=True; lug outer radius exp 36.0 obs 36.003 ok=True
- Status: OK. Findings: ['primary STOP check is self-referential (noise measured on the primary itself)'].
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
