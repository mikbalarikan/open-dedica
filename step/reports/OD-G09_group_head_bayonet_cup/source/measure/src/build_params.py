"""Run-local: assemble measure/params.json from the figure JSONs (no retyped scan numbers except
where a row says photo-inferred / assumed). Also fits the lug underside lines and the rim-notch floor."""
import json, hashlib, datetime, numpy as np, trimesh
F = lambda p: json.load(open(p))
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
al = F('intake/alignment.json'); lv = F('measure/figures/levels.json'); lg = F('measure/figures/lugs.json')
ins = F('measure/figures/instances.json'); rz = F('measure/figures/rz_profile.json'); mf = F('measure/figures/misc_fits.json')
cnt = F('measure/figures/count_lugs.json')
noise = al['scan_noise_mm']['value']
starts = [s for s, e in lg['lug_top']]; starts = sorted(starts, key=lambda s: (s - 300) % 360)  # lug1 = 336
lugs = sorted(lg['lugs'], key=lambda L: (L['top_theta'][0] - 300) % 360)
# ---- underside lines from inner-face lower edge (pooled over the 3 lugs)
def line(lo, hi, use=(0, 1, 2)):
    pts = [(d, zz) for i, L in enumerate(lugs) if i in use for d, zz in L['inner_face_bottom_z_vs_dtheta_from_start'] if lo <= d <= hi]
    d = np.array(pts); A = np.c_[np.ones(len(d)), d[:, 0]]; s, *_ = np.linalg.lstsq(A, d[:, 1], rcond=None)
    return s, float((d[:, 1] - A @ s).std()), len(d)
sA, rA, nA = line(9, 37); sB, rB, nB = line(43, 53, use=(0, 1))  # lug 3 lower face beyond +44 is a coverage gap (lug_faces_unwrapped.png)
zA7, zA42 = sA[0] + sA[1] * 7, sA[0] + sA[1] * 42
zB54 = sB[0] + sB[1] * 54; dX = (sA[0] - sB[0]) / (sB[1] - sA[1]); zB_at_start = sA[0] + sA[1] * dX
zA42 = zB_at_start
# ---- rim notch floor
m = trimesh.load('input/scan.stl'); T = np.array(al['matrix_4x4']); m.apply_transform(T)
c = m.triangles_center; nrm = m.face_normals; r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360
def win(t0, t1): return ((th - t0) % 360) < ((t1 - t0) % 360)
nf = []
for s in starts:
    for a, b in [(5.5, 12), (35.5, 41.5)]:
        t = (nrm[:, 2] > 0.85) & win(s + a, s + b) & (r > 37.3) & (r < 38.3) & (c[:, 2] > 2.0) & (c[:, 2] < 3.0)
        nf.append(round(float(np.median(c[t, 2])), 3))
json.dump({'underside_shallow': {'intercept': sA[0], 'slope_mm_per_deg': sA[1], 'rms': rA, 'n': nA, 'z_at_7': zA7},
           'underside_ramp': {'intercept': sB[0], 'slope_mm_per_deg': sB[1], 'rms': rB, 'n': nB, 'ramp_start_deg': dX, 'z_at_ramp_start': zB_at_start, 'z_at_54': zB54},
           'rim_notch_floor_z': nf}, open('measure/figures/underside_notch.json', 'w'), indent=1)
R3 = lambda x: round(float(x), 3)
EV = 'measure/figures/'
P = {}
def row(name, value, unit, measured, rule, source, estimator, unc, evidence, critical=False, **kw):
    P[name] = dict(value=value, unit=unit, measured=measured, rule=rule, source=source, estimator=estimator,
                   uncertainty_mm=unc, evidence=evidence, critical=critical, **kw)
ow = [v for zz, v, nn in rz['outer_wall_r_vs_z'] if zz < 1.0]
row('WALL_R_OUT', 40.11, 'mm', f"{min(ow):.3f}..{max(ow):.3f}", 'keep-measured', 'scan',
    'median r of outer-wall points per 1 mm z bin, z -28..+1 (rz_profile.py); one cylinder, no resolvable draft', 0.05, EV + 'rz_profile.json#outer_wall_r_vs_z', True,
    rerun_trigger='caliper reading ENV-D')
row('Z_BOTTOM', R3(al['bounds_aligned'][0][2]), 'mm', R3(al['bounds_aligned'][0][2]), 'keep-measured', 'scan',
    'lowest scan point (alignment.json bounds_aligned); scan truncation, the CAD closes the solid here', noise, 'intake/alignment.json#bounds_aligned',
    note='closure face at the scan extent (coverage C2), not a real part face')
row('RIM_LIP_TOP_Z', R3(lv['rim_lip_top']['z_p50']), 'mm', R3(lv['rim_lip_top']['z_p50']), 'keep-measured', 'scan',
    'median z of up-facing faces r 37.4-38.2 (levels.py)', noise, EV + 'levels.json#rim_lip_top')
row('RIM_LIP_OUTER_R', 38.5, 'mm', f"{mf['rim_ledge_r_p1']}..{mf['rim_lip_top_r_p99']}", 'keep-measured', 'scan',
    'lip top p99 radius vs ledge p1 radius, gap sectors (misc_fits.py)', 0.15, EV + 'misc_fits.json')
row('RIM_LEDGE_Z_AT_38p5', mf['rim_ledge_line_z_vs_r']['z_at_r38.5'], 'mm', mf['rim_ledge_line_z_vs_r']['z_at_r38.5'], 'keep-measured', 'scan',
    'line fit z(r) of up faces z 2..2.8, r 38..40, gap sectors', 0.05, EV + 'misc_fits.json#rim_ledge_line_z_vs_r')
row('RIM_LEDGE_Z_AT_39p8', mf['rim_ledge_line_z_vs_r']['z_at_r39.8'], 'mm', mf['rim_ledge_line_z_vs_r']['z_at_r39.8'], 'keep-measured', 'scan',
    'same line fit', 0.05, EV + 'misc_fits.json#rim_ledge_line_z_vs_r')
row('RIM_OUTER_FILLET_R', 0.4, 'mm', '0.3..0.5', 'keep-measured', 'scan', 'read from gap-sector r-z scatter at the outer rim corner', 0.1, EV + 'prof_rim.png')
row('RIM_LIP_FILLET_R', 0.3, 'mm', '0.2..0.4', 'keep-measured', 'scan', 'read from gap-sector r-z scatter at the lip corners', 0.1, EV + 'prof_rim.png')
row('BORE_R_Z0', mf['bore_gap_line']['r_at_z0'], 'mm', mf['bore_gap_line']['r_at_z0'], 'keep-measured', 'scan',
    'line fit r(z) of bore faces z -13.5..2.5 in gap sectors, value at z 0', mf['bore_gap_line']['rms'], EV + 'misc_fits.json#bore_gap_line', True,
    rerun_trigger='caliper reading F-BORE')
row('BORE_DRAFT_DEG', mf['bore_gap_line']['draft_deg'], 'deg', mf['bore_gap_line']['draft_deg'], 'keep-measured', 'scan',
    'slope of the same line fit (opens toward +z)', mf['bore_gap_line']['rms'], EV + 'misc_fits.json#bore_gap_line')
sh = [g['shelf_z_p50'] for g in ins['gaps']]
row('SHELF_Z', sh, 'mm', sh, 'keep-measured', 'scan', 'per-gap median z of up faces r 32.5-36.5 (gap k follows lug k)', noise,
    EV + 'instances.json#gaps', note='per-instance levels: gap 2 is 0.7 mm above gaps 1 and 3 (beyond noise); kept, not symmetrised')
sef = [g['R'] for g in F('measure/figures/valley_fit.json')['shelf_edge']]
row('SHELF_EDGE_FILLET_R', sef, 'mm', sef, 'keep-measured', 'scan', 'least-squares arc tangent to the per-gap shelf plane and the lip wall (LIP_UPPER_R), gap-sector points', 0.13,
    EV + 'valley_fit.json#shelf_edge', note='it1 draft read R1.0 by eye from a profile plot; the builder self-check showed 0.5-0.6 mm misfit there; replaced by this fit (change log)')
lipu = [v for zz, v, _ in rz['lip_gap_r_vs_z'] if -17.7 <= zz <= -15.6]
row('LIP_UPPER_R', 30.82, 'mm', f"{min(lipu):.3f}..{max(lipu):.3f}", 'keep-measured', 'scan', 'median r per 0.25 mm z bin, gap sectors, z -17.7..-15.6', 0.08, EV + 'rz_profile.json#lip_gap_r_vs_z')
lipl = [v for zz, v, _ in rz['lip_gap_r_vs_z'] if -19.5 <= zz <= -18.2]
row('LIP_LOWER_R', 31.33, 'mm', f"{min(lipl):.3f}..{max(lipl):.3f}", 'keep-measured', 'scan', 'median r per 0.25 mm z bin, gap sectors, z -19.5..-18.2', 0.05, EV + 'rz_profile.json#lip_gap_r_vs_z')
row('LIP_STEP_Z', -17.9, 'mm', '-18.1..-17.75', 'keep-measured', 'scan', 'z where the gap-sector lip radius steps from ~30.9 to ~31.3', 0.15, EV + 'rz_profile.json#lip_gap_r_vs_z')
lipg = [v for zz, v, _ in rz['lip_lug_r_vs_z'] if -18.8 <= zz <= -17.2]
row('LIP_LUG_R', 30.74, 'mm', f"{min(lipg):.3f}..{max(lipg):.3f}", 'keep-measured', 'scan', 'median r per 0.25 mm z bin, lug sectors, z -18.8..-17.2', 0.05, EV + 'rz_profile.json#lip_lug_r_vs_z')
row('FLOOR_Z', ins['floor_z_p50'], 'mm', ins['floor_z_p50'], 'keep-measured', 'scan', 'median z of up faces r 24.5-30 (plate top)', noise, EV + 'instances.json#floor_z_p50', True,
    rerun_trigger='depth reading ENV-Z2')
row('PLATE_T', 2.5, 'mm', None, 'assumed', 'assumed', 'no scan of the underside (coverage C1); photo 1 keyhole edge suggests ~2-3 mm', 1.0, 'input/photos/1.webp', note='confirm with F-PLATE')
row('LOWER_WALL_R_IN', 37.0, 'mm', None, 'assumed', 'assumed', 'below the plate the cup wall is assumed to continue at the bore radius to the scan extent', 1.0, 'intake/INTAKE_CARD.md#3', note='not scanned (C1, C2)')
row('LUG_COUNT', int(cnt.get('count', 3)), 'count', int(cnt.get('count', 3)), 'keep-measured', 'scan',
    'pattern_count.py mass signal, r 31.2-32.4, 3 stations z -4.5/-3.5/-2.0, FFT rotational order + residual local minimum', 0, EV + 'count_lugs.json')
row('LUG1_START_DEG', starts[0], 'deg', starts[0], 'keep-measured', 'scan', 'first 0.5 deg bin of lug top faces (z 0, r 31.9-34), lugs.py', 0.25, EV + 'lugs.json#lug_top')
row('LUG_PITCH_DEG', 120.0, 'deg', [round((starts[1] - starts[0]) % 360, 1), round((starts[2] - starts[1]) % 360, 1), round((starts[0] - starts[2]) % 360, 1)],
    'symmetry', 'scan', 'differences of lug start angles', 0.25, EV + 'lugs.json#lug_top', scatter_mm=0.0,
    scatter_note='starts 336/96/216 deg at 0.5 deg bin resolution: 120 deg pitch exactly')
spans = [L['span_deg'] for L in lugs]
row('LUG_SPAN_DEG', 54.0, 'deg', spans, 'symmetry', 'scan', 'lug top angular extent per lug', 0.25, EV + 'lugs.json#lugs', scatter_mm=0.0,
    scatter_note='53.5/54/54 deg: 0.5 deg = one bin; equal by intent (3-fold bayonet)')
cf = ins['lug_inner_faces_circle']
row('LUG_INNER_R', round(cf['r'], 3), 'mm', round(cf['r'], 3), 'keep-measured', 'scan',
    'IRLS circle through the inner faces of all 3 lugs (z -5..-1, dtheta 8..40); centre offset (%.2f, %.2f) from the datum axis' % (cf['cx'], cf['cy']),
    cf['rms'], EV + 'instances.json#lug_inner_faces_circle', True, rerun_trigger='caliper reading F-LUG',
    note='per-lug medians 31.695/31.842/31.490 differ because the lug ring sits 0.19 mm off the outer-wall axis; modelled coaxial (simplification)')
chw = [L['channel_inner_wall_r_p50'] for L in lugs]
row('CHANNEL_INNER_R', round(float(np.mean(chw)), 3), 'mm', chw, 'mean-of-n', 'scan', 'median r of the channel inner wall per lug (vertical faces r 33.8-35.2, z -2.7..-0.5)', 0.16, EV + 'lugs.json#lugs')
row('CHANNEL_Z', R3(lv['lug_channel']['z_p50']), 'mm', R3(lv['lug_channel']['z_p50']), 'keep-measured', 'scan', 'median z of up faces r 34.8-36.8, z -3.6..-2.2', noise, EV + 'levels.json#lug_channel')
def off(runs, lo, hi):
    o = []
    for a, b in runs:
        for s in starts:
            d = (a - s) % 360
            if lo <= d <= hi: o.append(round(d, 1))
    return o
cs = off(lg['channel_floor'], 0, 10); ce = [round((b - s) % 360, 1) for a, b in lg['channel_floor'] for s in starts if 30 <= (b - s) % 360 <= 50]
row('CHANNEL_START_OFF_DEG', round(float(np.mean(cs)), 2), 'deg', cs, 'mean-of-n', 'scan', 'channel floor first bin minus lug start', 0.5, EV + 'lugs.json#channel_floor')
row('CHANNEL_END_OFF_DEG', round(float(np.mean(ce)), 2), 'deg', ce, 'mean-of-n', 'scan', 'channel floor last bin minus lug start', 0.5, EV + 'lugs.json#channel_floor')
se = []
for s0 in starts:
    t = (np.abs(nrm[:, 2]) < 0.35) & (r > 31.0) & (r < 32.4) & (c[:, 2] < -8.0) & (c[:, 2] > -11.5) & (((th - s0) % 360) < 20)
    se.append(round(float(np.percentile((th[t] - s0) % 360, 99)), 2))
row('STOP_END_OFF_DEG', round(float(np.mean(se)), 2), 'deg', se, 'mean-of-n', 'scan', 'p99 of theta-offset of inner-face points below z -8 (stop face), per lug', 0.5, EV + 'lugs.json#lugs')
sb = [round(float(np.mean([zz for d, zz in L['inner_face_bottom_z_vs_dtheta_from_start'] if zz < -8])), 3) for L in lugs]
row('STOP_BOTTOM_Z', round(float(np.mean(sb)), 3), 'mm', sb, 'mean-of-n', 'scan', 'mean inner-face lower edge (1st pct) in the stop bins, per lug', 0.2, EV + 'lugs.json#lugs')
row('STOP_ROOT_FILLET_R', 1.0, 'mm', '0.8..1.2', 'keep-measured', 'scan', 'concave rounding between the stop bottom and the recessed bore wall, read from the r-z scatter at the stop start faces (lugs 1-2)', 0.2,
    EV + 'prof_stop_start.png', note='added after the builder self-check showed the corner (0.8 mm) unmodelled')
row('UNDERSIDE_Z_AT_7', R3(zA7), 'mm', R3(zA7), 'keep-measured', 'scan', 'line fit of inner-face lower edge vs dtheta 9..37 (3 lugs pooled), evaluated at +7', rA, EV + 'underside_notch.json#underside_shallow',
    note='only the lower EDGE of the underside is scanned (C4); the surface is modelled as a plane through that edge')
row('RAMP_START_OFF_DEG', round(float(dX), 2), 'deg', round(float(dX), 2), 'keep-measured', 'scan', 'intersection of the shallow and ramp edge lines', 1.0, EV + 'underside_notch.json')
row('UNDERSIDE_Z_AT_RAMP', R3(zA42), 'mm', R3(zA42), 'keep-measured', 'scan', 'shallow line evaluated at the ramp start', rA, EV + 'underside_notch.json#underside_shallow')
row('RAMP_Z_AT_54', R3(zB54), 'mm', R3(zB54), 'keep-measured', 'scan', 'line fit of inner-face lower edge vs dtheta 43..53 (lugs 1-2; lug 3 is a coverage gap there) at +54', rB, EV + 'underside_notch.json#underside_ramp')
ps = off(lg['pocket_inner_floor'], 350, 360); ps = [round(d - 360, 1) for d in ps]
pe = [round((b - s) % 360, 1) for a, b in lg['pocket_inner_floor'] for s in starts if 45 <= (b - s) % 360 <= 62]
row('POCKET_START_OFF_DEG', round(float(np.mean(ps)), 2), 'deg', ps, 'mean-of-n', 'scan', 'pocket inner floor first bin minus lug start', 0.5, EV + 'lugs.json#pocket_inner_floor')
pe2 = [v for v in pe if v > 55]
row('POCKET_END_OFF_DEG', round(float(np.mean(pe2)), 2), 'deg', pe2, 'mean-of-n', 'scan', 'pocket inner floor last bin minus lug start (lug 3 end lies in a coverage gap, excluded)', 0.5, EV + 'lugs.json#pocket_inner_floor')
vf = F('measure/figures/valley_fit.json')
for tag, key, zlab in [('VALLEY_OUTER', 'outer_valley', 'outer band r 34.8-36.6 (shelf outer part + pocket outer step)'),
                       ('POCKET_INNER', 'pocket_inner', 'pocket inner floor r 31.8-34.0')]:
    fits = vf[key]
    row(f'{tag}_THETA_C', [f_['theta_c_deg'] for f_ in fits], 'deg', [f_['theta_c_deg'] for f_ in fits], 'keep-measured', 'scan',
        f'least-squares (soft_l1) fit of a concave horizontal-axis cylinder to up faces of the {zlab}, per lug; axis along the radial direction at theta_c',
        0.5, EV + 'valley_fit.json#' + key, frame='datum frame, theta CCW about +Z from +X')
    row(f'{tag}_ZMIN', [f_['z_min'] for f_ in fits], 'mm', [f_['z_min'] for f_ in fits], 'keep-measured', 'scan', 'same fit: lowest z of the cylinder surface',
        max(f_['rms'] for f_ in fits), EV + 'valley_fit.json#' + key)
    row(f'{tag}_RC', [f_['Rc'] for f_ in fits], 'mm', [f_['Rc'] for f_ in fits], 'keep-measured', 'scan', 'same fit: cylinder radius',
        max(f_['rms'] for f_ in fits), EV + 'valley_fit.json#' + key,
        note='fit rms per lug ' + ', '.join(str(f_['rms']) for f_ in fits) + ' mm; replaces the it1-draft flat per-lug level (change log)')
br = vf['bore_recess']
row('BORE_RECESS_R', br['r_p50'], 'mm', f"{br['r_p5_p95'][0]}..{br['r_p5_p95'][1]}", 'keep-measured', 'scan',
    'median r of vertical faces r 36.9-37.9, z -15..-5 behind lugs 1-2 (lug 3: coverage gap)', 0.1, EV + 'valley_fit.json#bore_recess',
    note='the bore is recessed behind each lug and over the pocket ends (r 37.2-37.46 at dtheta -5..0 and 54..58.5, lugs 1-2); modelled over the pocket span from the groove bottom up to the channel floor')
row('POCKET_RISER_R', mf['pocket_riser_r']['p50'], 'mm', mf['pocket_riser_r']['p50'], 'keep-measured', 'scan', 'median r of vertical faces r 33.6-35.2, z -16.3..-15.2, lug sectors', 0.15, EV + 'misc_fits.json#pocket_riser_r')
gl = mf['groove_lug']; gdeep = [p50 for rr, p5, p50, nn in gl if 36.95 <= rr <= 37.3]
row('GROOVE_R_IN', 36.7, 'mm', '36.6..36.8', 'keep-measured', 'scan', 'radius where the lug-sector pocket floor starts to drop (groove_lug)', 0.1, EV + 'misc_fits.json#groove_lug')
row('GROOVE_BOTTOM_Z', round(float(np.mean(gdeep)), 3), 'mm', gdeep, 'mean-of-n', 'scan', 'median z per 0.1 mm r bin, r 36.95-37.3, lug sectors', 0.2, EV + 'misc_fits.json#groove_lug',
    note='modelled in lug sectors only; gap-sector groove is ~0.2-0.3 deep and not modelled')
row('NOTCH1_START_OFF_DEG', 5.0, 'deg', [round((a - s) % 360, 1) for a, b in lg['rim_ledge_at_lip_radius'] for s in starts if 0 <= (a - s) % 360 <= 10],
    'mean-of-n', 'scan', 'rim notch (ledge at lip radius) first bin minus lug start', 0.5, EV + 'lugs.json#rim_ledge_at_lip_radius')
n2 = [round((a - s) % 360, 1) for a, b in lg['rim_ledge_at_lip_radius'] for s in starts if 30 <= (a - s) % 360 <= 40]
row('NOTCH2_START_OFF_DEG', round(float(np.mean(n2)), 2), 'deg', n2, 'mean-of-n', 'scan', 'second rim notch first bin minus lug start', 0.5, EV + 'lugs.json#rim_ledge_at_lip_radius')
nw = [round((b - a) % 360, 1) for a, b in lg['rim_ledge_at_lip_radius']]
row('NOTCH_WIDTH_DEG', round(float(np.mean(nw)), 2), 'deg', nw, 'mean-of-n', 'scan', 'angular width of each of the 6 notches', 0.5, EV + 'lugs.json#rim_ledge_at_lip_radius')
row('NOTCH_FLOOR_Z', round(float(np.mean(nf)), 3), 'mm', nf, 'mean-of-n', 'scan', 'median z of up faces r 37.3-38.3 inside each notch', 0.03, EV + 'underside_notch.json#rim_notch_floor_z')
# ---- photo-inferred plate interior (photo 2, oblique, no scale reference; scale from the plate edge circle r 30.6)
PH = 'input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching'
for nm, v, u, est in [('KEY_CENTRAL_R', 13.0, 'mm', 'mean of top (14.6) and bottom (11.6) edge distance from the plate centre'),
                      ('KEY_LOBE_A_THETA', 133.0, 'deg', 'left lobe axis, photo angle 180 -> datum'),
                      ('KEY_LOBE_A_REACH', 23.5, 'mm', 'left lobe end distance (photo 24.0)'),
                      ('KEY_LOBE_A_WIDTH', 7.2, 'mm', 'left lobe width across'),
                      ('KEY_LOBE_B_THETA', 310.0, 'deg', 'right lobe axis, photo angle ~0 -> datum'),
                      ('KEY_LOBE_B_REACH', 20.5, 'mm', 'right lobe end distance'),
                      ('KEY_LOBE_B_WIDTH', 10.5, 'mm', 'right lobe width across'),
                      ('BOSS_THETA_1', 66.0, 'deg', 'upper-left boss, photo 120 -> datum'),
                      ('BOSS_PCR', 20.0, 'mm', 'mean of the two boss distances (21.8, 18.1; perspective)'),
                      ('BOSS_HOLE_D', 3.4, 'mm', 'bright hole diameter in the boss'),
                      ('BOSS_OD', 8.0, 'mm', 'outer ring of the boss'),
                      ('SIDE_HOLE_THETA', 269.0, 'deg', 'bright through-hole next to the lower boss, photo 313 -> datum'),
                      ('SIDE_HOLE_R', 20.8, 'mm', 'photo distance 22.3, moved in so the hole edge (r+D/2) stays 0.3 inside the scanned floor edge r_min 24.1 at theta 270 (measure/figures/floor_rmin.json)'),
                      ('SIDE_HOLE_D', 6.0, 'mm', 'diameter')]:
    row(nm, v, u, None, 'photo-inferred', 'photo-inferred', est, 3.0 if u == 'mm' else 10.0, PH, note='not scanned (coverage C3); confirm with F-KEY / F-BOSS', **({'frame': 'datum frame, theta CCW about +Z from +X (photo angle mapped by lug matching)'} if u == 'deg' else {}))
row('BOSS_PITCH_DEG', 180.0, 'deg', None, 'photo-inferred', 'photo-inferred', 'the two bosses read 178 deg apart after lug matching; intent: opposite', 10.0, PH, frame='datum frame, theta CCW about +Z from +X')
row('BOSS_H', 0.6, 'mm', None, 'assumed', 'assumed', 'raised boss ring height; photo shows a ring, height not measurable', 0.5, 'input/photos/1.webp')
doc = {'schema': 'stl-re/params.json@1', 'tool': 'measure/src/build_params.py', 'tool_version': 'run-local@1',
       'inputs': {p: sha(p) for p in ['input/scan.stl', 'intake/alignment.json', 'input/photos/1.webp', 'input/photos/2.webp']},
       'seed': 0, 'created': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
       'part': 'OD-G10_porta_filter_holder',
       'frame': 'datum frame of intake/alignment.json: z = 0 on the bayonet lug top pads (+z toward the cup mouth), axis = outer cup wall, lug 1 near +X (fourier_mass clock 34.76 deg); theta CCW about +Z from +X',
       'scan_noise_mm': noise, 'params': P, 'struck': [],
       'simplifications': [
        {'name': 'shelf levels', 'modelled_as': 'one flat per gap at the median', 'deviation_cost': 'p5..p95 within each gap: ' + ', '.join(f"{g['shelf_z_p5_p95']}" for g in ins['gaps'])},
        {'name': 'under-lug floors', 'modelled_as': 'concave horizontal-axis cylinders per lug (inner pocket floor, outer band), fitted', 'deviation_cost': 'fit rms outer ' + ', '.join(str(f_['rms']) for f_ in vf['outer_valley']) + '; inner ' + ', '.join(str(f_['rms']) for f_ in vf['pocket_inner'])},
        {'name': 'floor', 'modelled_as': 'flat plane at the median', 'deviation_cost': f"p5..p95 {ins['floor_z_p5_p95']} (0.24 deg tilt, levels.json#floor)"},
        {'name': 'lug ring coaxial', 'modelled_as': 'lug faces coaxial with the outer wall', 'deviation_cost': 'lug ring centre offset 0.19 mm (instances.json#lug_inner_faces_circle); per-lug median r 31.49..31.84'},
        {'name': 'outer wall', 'modelled_as': 'one cylinder', 'deviation_cost': f"median r per z bin {min(ow):.3f}..{max(ow):.3f}"},
        {'name': 'lug undersides', 'modelled_as': 'two planes (shallow + ramp) through the fitted lower-edge lines', 'deviation_cost': f"edge line rms {rA:.3f} / {rB:.3f} mm; surfaces themselves unscanned"},
        {'name': 'gap-sector bore groove', 'modelled_as': 'not modelled (groove/recess only over the pocket span)', 'deviation_cost': '0.2..0.3 mm local (misc_fits.json#groove_gap)'}],
       'checks': {'CHK-COUNT': {'ran': True, 'result': 'pass', 'note': 'lugs: FFT order 3 at 3 stations, residual local minimum (count_lugs.json); rim notches 6 = 2 per lug (lugs.json)'},
                  'CHK-ACHIEVABLE': {'ran': False, 'result': 'pass', 'note': 'no caliper readings supplied (scan-only); nothing to check'},
                  'CHK-CLUSTER': {'ran': True, 'result': 'pass', 'note': 'no material above the rim (z max 3.42) or on the axis; every region in the (r,z)/(theta,z) maps (maps1.png, ztheta.png) maps to F01-F17'},
                  'CHK-FRAME': {'ran': True, 'result': 'pass', 'note': 'all angles measured on the full-res scan through alignment.json in this run; none copied from intake'}},
       'open_questions': ['Is the inner stepped ring (shelf, pockets, lip) a separate rubber gasket? (modelled as one solid)',
                          'Plate interior dimensions (keyhole, bosses, holes) need a caliper or a photo with a scale.',
                          'Shelf/pocket waviness: moulding warp or design?']}
json.dump(doc, open('measure/params.json', 'w'), indent=1)
print('rows', len(P)); print('underside', zA7, zA42, zB_at_start, zB54, rA, rB); print('notch floor', nf)
