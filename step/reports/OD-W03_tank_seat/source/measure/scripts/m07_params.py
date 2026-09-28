"""m07_params.py - assemble measure/params.json from the measurement JSONs (no retyped numbers).
Lists are per instance: cups [A (-X), B (+X)], ears [neg (-X), pos (+X)]."""
import json, math, hashlib, datetime
from pathlib import Path
J = lambda p: json.load(open(p))
al = J('intake/alignment.json'); f1 = J('measure/figures/m01_flange.json'); f3 = J('measure/figures/m03_profile_fits.json')
f4 = J('measure/figures/m04_ears_webs.json'); f6 = J('measure/figures/m06_refine.json')
noise = al['scan_noise_mm']['value']
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
P = {}
def add(name, value, unit, measured, rule, source, estimator, unc, evidence, critical=False, **kw):
    P[name] = dict(value=value, unit=unit, measured=measured, rule=rule, source=source, estimator=estimator,
                   uncertainty_mm=unc, evidence=evidence, critical=critical, **kw)
r3 = lambda x: round(float(x), 3)
L = lambda a, b: [r3(a), r3(b)]
RT = "one caliper reading on this feature -> re-run measure/rebuild/verify"
# --- frame / pitch
sep = al['clock']['detail']['separation_mm']
add('cup_pitch', r3(sep), 'mm', r3(sep), 'keep-measured', 'scan',
    'distance between cup A and cup B axis centres (wall-face IRLS, z 1.2-3.6, 3 stations each) = the clock feature_line; cups at x = -/+ pitch/2',
    0.01, 'intake/alignment.json#clock.detail.separation_mm', True, rerun_trigger=RT)
# --- flange
yt, yb = f1['skirt_y_top']['p50'], f1['skirt_y_bot']['p50']
add('flange_half_width', r3((yt - yb) / 2), 'mm', r3((yt - yb) / 2), 'keep-measured', 'scan',
    'half of (median y of the +y straight skirt side - median y of the -y side), sections z -0.5/-1.0/-1.5, |x|<15', 0.08,
    'measure/figures/m01_flange.json#skirt_y_top,skirt_y_bot')
add('flange_centre_y', r3((yt + yb) / 2), 'mm', r3((yt + yb) / 2), 'keep-measured', 'scan',
    'mid of the two straight skirt sides (same sections); the flange sits 0.14 mm -y of the cup-axis line', 0.08,
    'measure/figures/m01_flange.json', note='kept, not snapped to 0: 3.5x the plane noise floor; the end arcs (cy -0.137/-0.122) agree')
ea = [f1['ends']['neg']['arc_fit']['cx'], f1['ends']['pos']['arc_fit']['cx']]
add('flange_end_arc_cx', L(*ea), 'mm', L(*ea), 'keep-measured', 'scan',
    'IRLS circle (Cauchy 0.3) on skirt section points with |x|>22, |y|>5.8 per end; arc radius set = flange_half_width (tangent stadium)', 0.14,
    'measure/figures/m01_flange.json#ends.*.arc_fit', note='measured arc radii 14.679 / 14.642 vs half width 14.716 (0.04-0.07 apart)')
tx = [f4['neg']['tab_outer_face_x']['p50'], f4['pos']['tab_outer_face_x']['p50']]
add('end_face_x', L(*tx), 'mm', L(*tx), 'keep-measured', 'scan',
    'median x of +-X-facing faces |y|<3.5, z -2.5..11 (ear tab outer face; the flange end flat is flush with it: m01 end_flat_x -34.164 / 34.303)', 0.1,
    'measure/figures/m04_ears_webs.json#*.tab_outer_face_x')
zs = [-3.03, -3.17]
add('skirt_bottom_z', -3.1, 'mm', '-3.17..-3.03', 'keep-measured', 'scan',
    'deepest scanned skirt z per 10-deg perimeter bin; the 6 deepest bins span -3.03..-3.17 (scan edge is ragged; the true edge is at or below the deepest reach)', 0.07,
    'measure/figures/m01_flange.json#skirt_wall_z; intake/alignment.json#sanity_landmarks[3]')
add('flange_top_z', 0.0, 'mm', r3(f1['flange_top_z_p50']), 'round-within-noise', 'scan',
    'primary datum plane; median z of up-facing faces |z|<0.3', noise, 'intake/alignment.json#primary; measure/figures/m01_flange.json#flange_top_z_p50')
add('wall_t', 1.2, 'mm', None, 'assumed', 'assumed',
    'not scanned (underside and interiors); typical moulded wall; owner chose a hollow shell (DECISIONS.md 2026-09-28)', None,
    'DECISIONS.md OTHER interior design intent; intake/coverage.json', note='applies to flange plate, skirt, cup, shoulder and boss walls')
# --- cups (profile, lists [A, B])
cA, cB = f6['cupA'], f6['cupB']
add('cup_lower_r0', L(cA['lower_wall']['c0'], cB['lower_wall']['c0']), 'mm', L(cA['lower_wall']['c0'], cB['lower_wall']['c0']), 'keep-measured', 'scan',
    'lower outer wall r at z=0 from a line fit to 0.25-mm z-bin medians of meridian r, z 0.9..6.6, sectors >30 deg from +-X', 0.03,
    'measure/figures/m06_refine.json#cup*.lower_wall; m02_cup_profile.png', True, rerun_trigger=RT)
dl = [math.degrees(math.atan(-cA['lower_wall']['c1'])), math.degrees(math.atan(-cB['lower_wall']['c1']))]
add('cup_lower_draft_deg', L(*dl), 'deg', L(*dl), 'keep-measured', 'scan', 'atan(-slope) of the same binned-median line', 0.03,
    'measure/figures/m06_refine.json#cup*.lower_wall')
du = [math.degrees(math.atan(-cA['upper_wall']['c1'])), math.degrees(math.atan(-cB['upper_wall']['c1']))]
add('cup_upper_r0', L(cA['upper_wall']['c0'], cB['upper_wall']['c0']), 'mm', L(cA['upper_wall']['c0'], cB['upper_wall']['c0']), 'keep-measured', 'scan',
    'upper outer wall line r(z) intercept at z=0 (binned medians z 7.8..10.7)', 0.04, 'measure/figures/m06_refine.json#cup*.upper_wall')
add('cup_upper_draft_deg', L(*du), 'deg', L(*du), 'keep-measured', 'scan', 'atan(-slope) of the upper-wall binned-median line', 0.04,
    'measure/figures/m06_refine.json#cup*.upper_wall')
add('cup_step_z_lo', L(cA['step_z_lo'], cB['step_z_lo']), 'mm', L(cA['step_z_lo'], cB['step_z_lo']), 'keep-measured', 'scan',
    'last 0.05-mm bin whose median r is within 0.04 of the lower-wall line', 0.05, 'measure/figures/m06_refine.json#cup*.step_z_lo')
add('cup_step_z_hi', L(cA['step_z_hi'], cB['step_z_hi']), 'mm', L(cA['step_z_hi'], cB['step_z_hi']), 'keep-measured', 'scan',
    'first bin above step_z_lo whose median r is within 0.04 of the upper-wall line; step modelled as a cone between the two knees', 0.05,
    'measure/figures/m06_refine.json#cup*.step_z_hi')
f8 = J('measure/figures/m08_top_annulus.json')
t9 = [f8['cupA']['z0'] + 9 * f8['cupA']['dz_dr'], f8['cupB']['z0'] + 9 * f8['cupB']['dz_dr']]
add('cup_top_z_r9', L(*t9), 'mm', L(*t9), 'keep-measured', 'scan', 'top annulus cone: line fit z(r) to 0.2-mm r-bin medians, r 8.4..10.1 (rms of medians 0.009 / 0.016), evaluated at r = 9', 0.03,
    'measure/figures/m08_top_annulus.json#cup*', note='it1 attempt 2: replaces the flat cup_top_z (median 12.338 / 12.259, m03) after the builder self-check showed a ring on the flat top')
ta = [f8['cupA']['slope_deg'], f8['cupB']['slope_deg']]
add('cup_top_slope_deg', L(*ta), 'deg', L(*ta), 'keep-measured', 'scan', 'atan(-dz/dr) of the same line (top falls outward)', 0.03, 'measure/figures/m08_top_annulus.json#cup*')
tr = [f3['cupA']['top_corner_round']['R'], f3['cupB']['top_corner_round']['R']]
add('cup_top_round_r', L(*tr), 'mm', L(*tr), 'keep-measured', 'scan', 'Kasa circle on meridian points of the top outer corner (rms 0.107 / 0.168)', 0.17,
    'measure/figures/m03_profile_fits.json#cup*.top_corner_round')
sa = [f3['cupA']['shoulder_angle_deg_from_horizontal'], f3['cupB']['shoulder_angle_deg_from_horizontal']]
add('shoulder_angle_deg', L(*sa), 'deg', L(*sa), 'keep-measured', 'scan', 'line fit z(r) on meridian points r 4.4..7.4 (conical shoulder), angle from horizontal', 0.12,
    'measure/figures/m03_profile_fits.json#cup*.shoulder_z_vs_r')
s5 = [f3['cupA']['shoulder_z_vs_r']['c0'] + 5 * f3['cupA']['shoulder_z_vs_r']['c1'], f3['cupB']['shoulder_z_vs_r']['c0'] + 5 * f3['cupB']['shoulder_z_vs_r']['c1']]
add('shoulder_z_at_r5', L(*s5), 'mm', L(*s5), 'keep-measured', 'scan', 'the same line evaluated at r = 5', 0.12, 'measure/figures/m03_profile_fits.json#cup*.shoulder_z_vs_r')
sh = [f3['cupA']['shank_r_p50'], f3['cupB']['shank_r_p50']]
add('barb_shank_r', L(*sh), 'mm', L(*sh), 'keep-measured', 'scan', 'median meridian r, z 16.8..22.8 (p10-p90 A 2.44-2.85, B 2.38-2.74)', 0.14,
    'measure/figures/m03_profile_fits.json#cup*.shank_r_p50', True, rerun_trigger=RT, note='A and B differ by 0.13 (> noise); kept per barb, not averaged')
sf = [f3['cupA']['shank_fillet']['R'], f3['cupB']['shank_fillet']['R']]
add('shank_fillet_r', L(*sf), 'mm', L(*sf), 'keep-measured', 'scan', 'Kasa circle on meridian points r 2.6..3.9, z 14.6..16.4 (shoulder-to-shank round; rms 0.22)', 0.23,
    'measure/figures/m03_profile_fits.json#cup*.shank_fillet')
fz = [(f3['cupA']['shank_r_p50'] - f3['cupA']['barb_flare_r_vs_z']['c0']) / f3['cupA']['barb_flare_r_vs_z']['c1'],
      (f3['cupB']['shank_r_p50'] - f3['cupB']['barb_flare_r_vs_z']['c0']) / f3['cupB']['barb_flare_r_vs_z']['c1']]
add('barb_flare_z0', L(*fz), 'mm', L(*fz), 'keep-measured', 'scan', 'z where the flare line r(z) (fit z 23.0..24.2) meets the shank radius', 0.15,
    'measure/figures/m03_profile_fits.json#cup*.barb_flare_r_vs_z')
lr = [f3['cupA']['lip_r_top50_median'], f3['cupB']['lip_r_top50_median']]
add('barb_lip_r', L(*lr), 'mm', L(*lr), 'keep-measured', 'scan', 'median of the 50 largest meridian r in z 23.6..25.0', 0.07,
    'measure/figures/m03_profile_fits.json#cup*.lip_r_top50_median', True, rerun_trigger=RT)
lz = [f3['cupA']['lip_z_at_rmax'], f3['cupB']['lip_z_at_rmax']]
add('barb_lip_z', L(*lz), 'mm', L(*lz), 'keep-measured', 'scan', 'median z of those 50 points', 0.1, 'measure/figures/m03_profile_fits.json#cup*.lip_z_at_rmax')
bt = [f3['cupA']['barb_top_z_p50'], f3['cupB']['barb_top_z_p50']]
add('barb_top_z', L(*bt), 'mm', L(*bt), 'keep-measured', 'scan', 'median z of meridian points r 1.9..2.8, z > 28', 0.05, 'measure/figures/m03_profile_fits.json#cup*.barb_top_z_p50')
tipr = [f3['cupA']['barb_taper_r_vs_z']['c0'] + f3['cupA']['barb_taper_r_vs_z']['c1'] * bt[0], f3['cupB']['barb_taper_r_vs_z']['c0'] + f3['cupB']['barb_taper_r_vs_z']['c1'] * bt[1]]
add('barb_tip_r', L(*tipr), 'mm', L(*tipr), 'keep-measured', 'scan', 'taper line r(z) (fit z 25.0..27.9, rms 0.068/0.123) evaluated at barb_top_z; profile runs lip -> tip straight', 0.12,
    'measure/figures/m03_profile_fits.json#cup*.barb_taper_r_vs_z', True, rerun_trigger=RT)
br = f4['hole_loops']['barbB']['r']
add('barb_bore_r', r3(br), 'mm', r3(br), 'keep-measured', 'scan', 'Kasa circle on the open-boundary loop at the barb B tip (73 verts, z 27.7..28.6, rms 0.21); barb A loop not closed -> same value used',
    0.21, 'measure/figures/m04_ears_webs.json#hole_loops.barbB', note='bore depth beyond ~0.9 mm is not scanned: assumed through into the cup cavity')
# --- boss
b = f3['boss']
add('boss_r0', r3(b['wall_r_vs_z']['c0']), 'mm', r3(b['wall_r_vs_z']['c0']), 'keep-measured', 'scan', 'line fit r(z) on meridian points z 1..10.5 about x=0 (rms 0.10)', 0.1,
    'measure/figures/m03_profile_fits.json#boss.wall_r_vs_z')
bd = math.degrees(math.atan(-b['wall_r_vs_z']['c1']))
add('boss_draft_deg', r3(bd), 'deg', r3(bd), 'keep-measured', 'scan', 'atan(-slope) of that line', 0.1, 'measure/figures/m03_profile_fits.json#boss.wall_r_vs_z')
add('boss_top_z_r4', r3(f8['boss']['z0'] + 4 * f8['boss']['dz_dr']), 'mm', r3(f8['boss']['z0'] + 4 * f8['boss']['dz_dr']), 'keep-measured', 'scan',
    'boss top cone: line fit z(r) to 0.2-mm r-bin medians r 2.6..5.2 (rms 0.014), at r = 4', 0.03, 'measure/figures/m08_top_annulus.json#boss',
    note='it1 attempt 2: replaces the flat boss_top_z (median 12.354, m03)')
add('boss_top_slope_deg', r3(f8['boss']['slope_deg']), 'deg', r3(f8['boss']['slope_deg']), 'keep-measured', 'scan', 'atan(-dz/dr) of that line', 0.03, 'measure/figures/m08_top_annulus.json#boss')
add('boss_top_round_r', r3(b['top_corner_round']['R']), 'mm', r3(b['top_corner_round']['R']), 'keep-measured', 'scan', 'Kasa circle on the top outer corner (rms 0.17)', 0.17,
    'measure/figures/m03_profile_fits.json#boss.top_corner_round')
add('boss_hole_r', r3(f4['hole_loops']['boss']['r']), 'mm', r3(f4['hole_loops']['boss']['r']), 'keep-measured', 'scan', 'Kasa circle on the open-boundary loop in the boss top (82 verts, z 11.0..11.8)', 0.14,
    'measure/figures/m04_ears_webs.json#hole_loops.boss', note='hole assumed through into the boss cavity')
# --- webs
ws = [f4[s][k] ['p50'] for s in ('neg', 'pos') for k in ('web_boss_side_ypos', 'web_tab_side_ypos')] + [-f4[s][k]['p50'] for s in ('neg', 'pos') for k in ('web_boss_side_yneg', 'web_tab_side_yneg')]
ws = [r3(w) for w in ws]
add('web_half_width', r3(sum(ws) / len(ws)), 'mm', ws, 'symmetry', 'scan', 'median |y| of the +-y-facing web side faces (4 webs x 2 sides), z 1..12', 0.07,
    'measure/figures/m04_ears_webs.json#*.web_*_side_*', scatter_mm=r3(max(ws) - min(ws)),
    scatter_note='four identical 1.9-mm moulded ribs by intent; side-face medians scatter 0.135 on a rough, partly occluded face; residual <= 0.07 per side')
wt = [r3(f4[s][k]['p50']) for s in ('neg', 'pos') for k in ('web_boss_top_z', 'web_tab_top_z')]
add('web_top_z', r3(sum(wt) / len(wt)), 'mm', wt, 'symmetry', 'scan', 'median z of up-facing faces on the web tops |y|<0.8', 0.06,
    'measure/figures/m04_ears_webs.json#*.web_*_top_z', scatter_mm=r3(max(wt) - min(wt)),
    scatter_note='one rib height by intent (cup tops 12.26-12.34, boss 12.35); residual <= 0.09')
# --- ears [neg, pos]
ti = [(f4['neg']['tab_inner_face_x']['p50'] + f4['neg']['tab_inner_face_x_ypos']['p50']) / 2, (f4['pos']['tab_inner_face_x']['p50'] + f4['pos']['tab_inner_face_x_ypos']['p50']) / 2]
add('tab_inner_x', L(*ti), 'mm', L(*ti), 'keep-measured', 'scan', 'mean of the medians of the cup-facing tab faces either side of the web (x 31.8..33.2)', 0.15,
    'measure/figures/m04_ears_webs.json#*.tab_inner_face_x*')
def tabw(s):
    zc = [-0.5, 3.5, 7.5, 11.25]; keys = ['z-2_1', 'z2_5', 'z6_9', 'z10_12.5']
    w = [(f4[s][f'tab_side_ypos_{k}']['p50'] - f4[s][f'tab_side_yneg_{k}']['p50']) / 2 for k in keys]
    n = len(zc); mz = sum(zc) / n; mw = sum(w) / n
    k1 = sum((a - mz) * (c - mw) for a, c in zip(zc, w)) / sum((a - mz) ** 2 for a in zc)
    return mw - k1 * mz, k1
(w0n, k1n), (w0p, k1p) = tabw('neg'), tabw('pos')
add('tab_half_width_z0', L(w0n, w0p), 'mm', L(w0n, w0p), 'keep-measured', 'scan', 'line fit of the tab half-width (median side-face y, 4 z bands) vs z, value at z=0', 0.05,
    'measure/figures/m04_ears_webs.json#*.tab_side_*')
td = [math.degrees(math.atan(-k1n)), math.degrees(math.atan(-k1p))]
add('tab_side_draft_deg', L(*td), 'deg', L(*td), 'keep-measured', 'scan', 'atan(-slope) of that line (each side tapers inward going up)', 0.05, 'measure/figures/m04_ears_webs.json#*.tab_side_*')
lt = [f4['neg']['lug_top_z']['p50'], f4['pos']['lug_top_z']['p50']]
add('lug_top_z', L(*lt), 'mm', L(*lt), 'keep-measured', 'scan', 'median z of up-facing lug faces x 34.5..41.5, |y|<3.5 (also the tab top)', 0.06, 'measure/figures/m04_ears_webs.json#*.lug_top_z')
lb = [f6['lug_side_neg_z']['1'], f6['lug_side_pos_z']['1']]
add('lug_bottom_z', L(*lb), 'mm', L(*lb), 'keep-measured', 'scan', 'p1 z of the lug side faces (x 35..41): the lowest the scan saw the side walls; the underside itself is not scanned', 0.15,
    'measure/figures/m06_refine.json#lug_side_*_z', note='a bound, not a seen face: the underside may sit lower only if the side walls were occluded below 12.2')
lw = [(f4['neg']['lug_side_ypos']['p50'] - f4['neg']['lug_side_yneg']['p50']) / 2, (f4['pos']['lug_side_ypos']['p50'] - f4['pos']['lug_side_yneg']['p50']) / 2]
add('lug_half_width', L(*lw), 'mm', L(*lw), 'keep-measured', 'scan', 'half of the gap between median +-y lug side faces, x 34.5..38.5', 0.08, 'measure/figures/m04_ears_webs.json#*.lug_side_*')
le = [f4['neg']['lug_end_x_extreme_p99'], f4['pos']['lug_end_x_extreme_p99']]
add('lug_end_x', L(*le), 'mm', L(*le), 'keep-measured', 'scan', 'p99 of |x| of lug-end faces |y|<2 (end arc apex); end = semicircle of radius lug_half_width', 0.1, 'measure/figures/m04_ears_webs.json#*.lug_end_x_extreme_p99')
hx = [f4['neg']['lug_hole_fit']['cx'], f4['pos']['lug_hole_fit']['cx']]
hy = [f4['neg']['lug_hole_fit']['cy'], f4['pos']['lug_hole_fit']['cy']]
hr = [f4['neg']['lug_hole_fit']['r'], f4['pos']['lug_hole_fit']['r']]
add('lug_hole_cx', L(*hx), 'mm', L(*hx), 'keep-measured', 'scan', 'IRLS circle on hole-wall section points z 13.6/13.9/14.2/14.5', 0.1, 'measure/figures/m04_ears_webs.json#*.lug_hole_fit', True, rerun_trigger=RT)
add('lug_hole_cy', L(*hy), 'mm', L(*hy), 'keep-measured', 'scan', 'same fit', 0.1, 'measure/figures/m04_ears_webs.json#*.lug_hole_fit')
add('lug_hole_r', L(*hr), 'mm', L(*hr), 'keep-measured', 'scan', 'same fit (rms 0.093 / 0.106)', 0.1, 'measure/figures/m04_ears_webs.json#*.lug_hole_fit', True, rerun_trigger=RT)
doc = {"schema": "stl-re/params.json@1", "tool": "measure/scripts/m07_params.py", "tool_version": "run-local",
       "inputs": {p: sha(p) for p in ('intake/aligned_work.stl', 'intake/alignment.json', 'input/photos/OD-W03_photo1.png', 'measure/figures/m08_top_annulus.json')},
       "seed": 0, "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
       "part": "OD-W03",
       "frame": "datum frame of intake/alignment.json: z=0 flange top face (material below), origin = midpoint of cup A/B axes, +X from cup A axis to cup B axis; theta CCW about +Z from +X. Lists: cups [A (-X), B (+X)], ears [neg (-X), pos (+X)].",
       "scan_noise_mm": noise, "params": P, "struck": [],
       "simplifications": [
         {"name": "cup wall ripple", "modelled_as": "straight drafted lines (binned-median fits)", "deviation_cost": "raw-point rms about the line 0.08-0.17 mm (m03 lower/upper wall rms) vs 0.02-0.04 mm for the bin medians"},
         {"name": "barb shank", "modelled_as": "cylinder at the median radius", "deviation_cost": "p10-p90 spread A 0.40 / B 0.36 mm (rough scan on a small radius)"},
         {"name": "barb tip taper", "modelled_as": "straight cone lip -> tip", "deviation_cost": "fitted taper line rms 0.068 / 0.123 mm; lip edge sharp"},
         {"name": "webs, tabs", "modelled_as": "planar ribs of one width; tab as a trapezoid prism", "deviation_cost": "web side scatter 0.135 (<= 0.07 per side); tab half-width line residual < 0.05"},
         {"name": "cosmetic parting line on the cup shoulders along y=0", "modelled_as": "not modelled", "deviation_cost": "faint ridge, < 0.1 mm high (m05 shaded top view)"}],
       "checks": {
         "CHK-COUNT": {"ran": True, "result": "pass", "note": "no rotational patterns: 2 cups, 1 boss, 4 webs, 2 ears counted directly in sections and the top view (m05_heightmap.png)"},
         "CHK-ACHIEVABLE": {"ran": False, "result": "pass", "note": "no caliper readings (scan-only run): nothing to check"},
         "CHK-CLUSTER": {"ran": True, "result": "pass", "note": "top-view height map and meridian profiles show no unexplained material; above the cups only the barbs (coverage radial bands); faint y=0 ridge on the shoulders = parting line (cosmetic, declared); junk facets at the tab/lug junction x~+-33 z 12.5-14.5 are scan artefacts (many small loops, no flat top)"},
         "CHK-FRAME": {"ran": True, "result": "pass", "note": "no angles carried over from intake; all positions re-measured on intake/aligned_work.stl in the frozen datum frame"}},
       "open_questions": ["Interior (underside, cup/boss cavities, bore depth) is assumed: wall 1.2 mm, hollow shell (owner decision).",
                          "Lug underside not scanned: lug_bottom_z is the lowest visible side-wall point.",
                          "Absolute scale unverified (no calipers)."]}
json.dump(doc, open('measure/params.json', 'w'), indent=1)
print(len(P), 'params')
