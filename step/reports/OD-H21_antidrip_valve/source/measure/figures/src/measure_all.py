"""measure_all.py - every scan measurement behind measure/params.json (OD-H21).
Run: python measure/figures/src/measure_all.py  -> measure/figures/fits.json
All numbers in the frozen datum frame (intake/alignment.json). Deterministic."""
from __future__ import annotations
import json
import numpy as np
from mlib import *

m = mesh(); C = m.triangles_center; N = m.face_normals; A = m.area_faces; V = m.vertices
out = {"inputs": {"intake/aligned_work.stl": sha(RUN / 'intake/aligned_work.stl'),
                  "intake/alignment.json": sha(RUN / 'intake/alignment.json')}}
WIN_EX = [(-80, -55), (-12, 14), (98, 126), (165, 181), (-181, -165)]
RIB_TH0 = 23.75  # refined below

# ---------------------------------------------------------------- 1. coaxial segments
seg = {}
seg['nozzle'] = fit_axis_cyl(C[select_faces(-22.3, -14.7, 5.3, 6.3)], -18.5, (0, 0, 5.78))
# nut base: exclude +-11 deg around the 8 ribs (ribs measured separately)
q = C[:, :2] - [-0.065, -0.153]; th = np.degrees(np.arctan2(q[:, 1], q[:, 0]))
ribs0 = np.arange(8) * 45 + RIB_TH0 - 180
dr = np.abs(((th[:, None] - ribs0[None] + 180) % 360) - 180).min(1)
s = select_faces(-13.3, -7.2, 10.3, 11.5, c=(-0.065, -0.153)) & (dr > 11)
seg['nut'] = fit_axis_cyl(C[s], -10.0, (-0.065, -0.153, 10.84), taper=True, fix_tilt=True)
seg['nut_tiltfree'] = fit_axis_cyl(C[s], -10.0, (-0.065, -0.153, 10.84), taper=True)
seg['band_lo'] = fit_axis_cyl(C[select_faces(-5.8, -2.9, 11.7, 12.9, (-0.07, -0.24), [(-25, 25)])], -4.35, (-0.07, -0.24, 12.2), taper=True, fix_tilt=True)
seg['band_up'] = fit_axis_cyl(C[select_faces(-2.3, -0.75, 11.6, 12.5, (-0.07, -0.24), [(-25, 25)])], -1.5, (0.1, -0.2, 12.0), fix_tilt=True)
seg['body'] = fit_axis_cyl(C[select_faces(0.5, 8.4, 9.4, 10.7, (0.15, -0.16), [(-35, 35)])], 4.5, (0.15, -0.16, 10.02), fix_tilt=True)
seg['body_tiltfree'] = fit_axis_cyl(C[select_faces(0.5, 8.4, 9.4, 10.7, (0.15, -0.16), [(-35, 35)])], 4.5, (0.15, -0.16, 10.02))
# cap part: ring + cap share one axis (one moulded part); joint fit, two radii
Pa = C[select_faces(10.8, 16.1, 12.7, 14.0, (0, 0), WIN_EX)]
Pb = C[select_faces(17.4, 22.5, 11.5, 12.8, (0.25, -0.25), [(35, 75)])]
def rj(x):
    ra, _ = rho_u(Pa, x[0], x[1], 17.0, x[2], x[3]); rb, _ = rho_u(Pb, x[0], x[1], 17.0, x[2], x[3])
    return np.r_[ra - x[4], rb - x[5]]
sl = least_squares(rj, [0.1, -0.2, 0.05, -0.03, 13.27, 12.14], loss='soft_l1', f_scale=0.05)
e = rj(sl.x); d_cap = axis_dir(sl.x[2], sl.x[3])
seg['cap_part'] = dict(cx=float(sl.x[0]), cy=float(sl.x[1]), z0=17.0, tx_deg=float(np.degrees(sl.x[2])), ty_deg=float(np.degrees(sl.x[3])),
                       tilt_deg=float(np.degrees(np.arccos(d_cap[2]))), tilt_dir_deg=float(np.degrees(np.arctan2(d_cap[1], d_cap[0]))),
                       R_ring=float(sl.x[4]), R_cap=float(sl.x[5]), ring=stats(e[:len(Pa)]), cap=stats(e[len(Pa):]))
out['segments'] = seg

def seg_axis(k):
    f = seg[k]; d = axis_dir(np.radians(f['tx_deg']), np.radians(f['ty_deg']))
    return np.array([f['cx'], f['cy'], f['z0']]) - f['z0'] * d, d   # point at u=0, u ~ datum z
AX = {k: seg_axis(k) for k in ('nozzle', 'nut', 'band_lo', 'band_up', 'body', 'cap_part')}
out['axes'] = {k: {"p": v[0].tolist(), "d": v[1].tolist()} for k, v in AX.items()}

# ---------------------------------------------------------------- 2. axial faces (levels along each axis)
def level(k, sign, ulo, uhi, rlo, rhi, cos_min=0.97):
    p, d = AX[k]; q = C - p; u = q @ d; rr = np.linalg.norm(q - np.outer(u, d), axis=1)
    s = (sign * (N @ d) > cos_min) & (u > ulo) & (u < uhi) & (rr > rlo) & (rr < rhi)
    w = A[s]; uu = u[s]; med = float(np.median(uu))
    return dict(u_median=med, u_wmean=float((uu * w).sum() / w.sum()), p5=float(np.percentile(uu, 5)), p95=float(np.percentile(uu, 95)),
                area_mm2=float(w.sum()), n=int(s.sum()), scatter=float(np.std(uu)))
lv = {}
lv['nozzle_tip'] = level('nozzle', -1, -27.6, -27.0, 4.2, 5.4)
lv['shoulder'] = level('nut', -1, -14.6, -13.5, 7.0, 10.0)
lv['band_step'] = level('band_up', 1, -2.8, -2.3, 12.0, 12.3, 0.9)
lv['primary'] = level('band_up', 1, -0.3, 0.3, 10.3, 11.4)
lv['ring_bottom'] = level('cap_part', -1, 9.2, 10.0, 10.3, 12.6)
lv['ring_top'] = level('cap_part', 1, 16.5, 17.0, 12.3, 12.9, 0.9)
lv['cap_top'] = level('cap_part', 1, 22.9, 23.6, 3.5, 11.5)
out['levels'] = lv

# ---------------------------------------------------------------- 3. profile tables (evidence) and rounds
keep_noz_outlet = lambda th: ~((th > -40) & (th < 40))
tabs = {}
tabs['body_frame'] = profile_table(*AX['body'], -16, 12, 0.1, 16, keep_noz_outlet)
tabs['nozzle_frame'] = profile_table(*AX['nozzle'], -27.8, -13.5, 0.1, 9)
kcap = lambda th: ~(((th > 20) & (th < 90)) | ((th > -80) & (th < -55)) | ((th > -12) & (th < 14)) | ((th > 98) & (th < 126)) | (np.abs(th) > 165))
tabs['cap_frame'] = profile_table(*AX['cap_part'], 8.5, 24.0, 0.1, 14, kcap)
out['tables_cols'] = "u_mid, rho p1, p10, p50, p90, p99, n"
rounds = {}
rounds['ring_bottom_outer'] = fit_arc_rz(*AX['cap_part'], 9.5, 10.3, 12.6, 13.35, kcap, [10.1, 12.7, 0.6])
rounds['ring_top_outer'] = fit_arc_rz(*AX['cap_part'], 16.1, 16.8, 12.7, 13.3, kcap, [16.2, 12.7, 0.6])
rounds['cap_root'] = fit_arc_rz(*AX['cap_part'], 16.85, 17.3, 12.15, 12.6, kcap, [17.3, 12.6, 0.4])
rounds['cap_top_edge'] = fit_arc_rz(*AX['cap_part'], 22.75, 23.3, 11.5, 12.2, lambda th: ~((th > 20) & (th < 90)), [22.9, 11.7, 0.4])
rounds['band_up_top'] = fit_arc_rz(*AX['band_up'], -0.7, -0.05, 11.4, 12.02, keep_noz_outlet, [-0.6, 11.4, 0.6])
rounds['nozzle_tip_outer'] = fit_arc_rz(*AX['nozzle'], -27.3, -26.8, 5.2, 5.85, None, [-27.0, 5.5, 0.3])
rounds['shoulder_root'] = fit_arc_rz(*AX['nozzle'], -14.75, -14.1, 5.8, 6.4, None, [-14.8, 6.3, 0.4])
out['rounds'] = rounds
# nut top chamfer: straight line through the transition (rho p50 in nut frame, ribs excluded)
p, d = AX['nut']; Vl = V - p; u = Vl @ d; rr = np.linalg.norm(Vl - np.outer(u, d), axis=1)
q = V[:, :2] - p[:2]; thv = np.degrees(np.arctan2(q[:, 1], q[:, 0]))
drv = np.abs(((thv[:, None] - ribs0[None] + 180) % 360) - 180).min(1)
s = (u > -6.7) & (u < -6.15) & (drv > 12) & ~((thv > -40) & (thv < 40)) & (rr > 10.9) & (rr < 12.2)
cf = np.polyfit(u[s], rr[s], 1)
out['nut_chamfer'] = dict(slope_drho_du=float(cf[0]), rho_at_m6p7=float(np.polyval(cf, -6.7)), rho_at_m6p15=float(np.polyval(cf, -6.15)),
                          angle_to_axis_deg=float(np.degrees(np.arctan(cf[0]))), **stats(rr[s] - np.polyval(cf, u[s])))

# ---------------------------------------------------------------- 4. nut ribs (vertical rods)
cn = np.array(AX['nut'][0][:2]); q = C[:, :2] - cn; r = np.hypot(*q.T); th = np.degrees(np.arctan2(q[:, 1], q[:, 0]))
base = seg['nut']['R'] + seg['nut']['k'] * (C[:, 2] - (-10.0))
ribs = []
for a in ribs0:
    dth = ((th - a + 180) % 360) - 180
    s = (np.abs(dth) < 9) & (r > base + 0.2) & (r < 12.8) & (C[:, 2] > -13.2) & (C[:, 2] < -7.3) & (np.abs(N[:, 2]) < 0.3)
    f = fit_circle_irls(C[s, :2], A[s], scale=0.1); cc = np.array([f['cx'], f['cy']]) - cn
    ribs.append(dict(theta_deg=float(np.degrees(np.arctan2(cc[1], cc[0]))), rho_c=float(np.hypot(*cc)), rod_r=float(f['r']),
                     peak=float(np.hypot(*cc) + f['r']), rms=float(f['rms']), n=int(s.sum())))
out['ribs'] = ribs

# ---------------------------------------------------------------- 5. nozzle lip (rounded square), bore, window
pn, dn = AX['nozzle']; Vn = local_verts(pn, dn); rn = np.hypot(Vn[:, 0], Vn[:, 1]); tn = np.degrees(np.arctan2(Vn[:, 1], Vn[:, 0]))
def env_pts(zl, zh, step=1.0):
    s = (Vn[:, 2] > zl) & (Vn[:, 2] < zh); b = np.floor(tn[s] / step); P = []
    for x in np.unique(b):
        t = np.where(s)[0][b == x]; k = t[np.argmax(rn[t])]; P.append(Vn[k, :2])
    return np.array(P)
def rect_sdf(P, x):
    cx, cy, a, b, rc, phi = x
    c, s_ = np.cos(np.radians(-phi)), np.sin(np.radians(-phi)); Q = np.abs((P - [cx, cy]) @ np.array([[c, -s_], [s_, c]]).T)
    qq = Q - np.array([a - rc, b - rc]); return np.hypot(np.maximum(qq[:, 0], 0), np.maximum(qq[:, 1], 0)) + np.minimum(np.maximum(qq[:, 0], qq[:, 1]), 0) - rc
lugfits = {}
for nm, (zl, zh) in {'mid': (-24.8, -23.6), 'low': (-25.9, -25.5), 'top': (-23.5, -23.25)}.items():
    Pe = env_pts(zl, zh); tp = np.degrees(np.arctan2(Pe[:, 1], Pe[:, 0])); rp = np.hypot(*Pe.T)
    use = (rp > 5.95) & ~((tp > 85) & (tp < 142))   # outline outside the nozzle cylinder; latch-window side excluded
    sl = least_squares(lambda x: rect_sdf(Pe[use], x), [0, 0, 5.8, 6.3, 0.3, 23.6], loss='soft_l1', f_scale=0.05)
    lugfits[nm] = dict(cx=float(sl.x[0]), cy=float(sl.x[1]), half_a=float(sl.x[2]), half_b=float(sl.x[3]), corner_r=float(sl.x[4]),
                       phi_deg=float(sl.x[5]), **stats(rect_sdf(Pe[use], sl.x)))
lug = dict(lugfits['mid']); lug['bands'] = lugfits
lug['side_normal_deg'] = lug['phi_deg']
cz = []
for a0 in np.arange(4) * 90 + lug['side_normal_deg'] + 45:
    dd = ((tn - a0 + 180) % 360) - 180; s = (np.abs(dd) < 6) & (rn > 7.2) & (Vn[:, 2] < -22)
    cz.append([float(np.percentile(Vn[s, 2], 1)), float(np.percentile(Vn[s, 2], 99))])
lug['corner_theta_deg'] = [float(((a + 180) % 360) - 180) for a in np.arange(4) * 90 + lug['side_normal_deg'] + 45]
lug['corner_z_p1_p99'] = cz
out['lip'] = lug
s = (rn > 3.3) & (rn < 4.3) & (Vn[:, 2] > -26.9) & (Vn[:, 2] < -25.0)
fb = fit_circle_irls(Vn[s, :2])
sw = (rn > 3.3) & (rn < 4.3) & (Vn[:, 2] > -27.1) & (Vn[:, 2] < -22)
out['nozzle_bore'] = dict(r=float(fb['r']), rms=float(fb['rms']), cx=float(fb['cx']), cy=float(fb['cy']),
                          wall_z_pct_1_50_95_99=np.percentile(Vn[sw, 2], [1, 50, 95, 99]).round(3).tolist(),
                          note="scan wall ends in an open boundary loop (coverage.json loop 1); deeper bore bridged/unseen")
# latch window (through-lip opening at the side normal ~ +115 deg): angular / axial extent where the outer wall is missing
side = [((lug['side_normal_deg'] + 90 * k + 180) % 360) - 180 for k in range(4)]
win = []
for a0 in side:
    dd = ((tn - a0 + 180) % 360) - 180
    s = (np.abs(dd) < 30) & (Vn[:, 2] > -25.6) & (Vn[:, 2] < -24.0) & (rn > 3.9) & (rn < 5.55)
    win.append(dict(side_theta_deg=float(a0), n_pts_inside_r5p55=int(s.sum()),
                    u_p5_p95=np.percentile(Vn[s, 2], [5, 95]).round(3).tolist() if s.sum() > 30 else None,
                    theta_p5_p95=np.percentile(dd[s] + a0, [5, 95]).round(2).tolist() if s.sum() > 30 else None,
                    rho_p10_p50=np.percentile(rn[s], [10, 50]).round(3).tolist() if s.sum() > 30 else None))
out['nozzle_windows'] = win

# ---------------------------------------------------------------- 6. side outlet
f, p, d = refine_axis([0, 0, 4.1], [1, 0, 0], 11.0, 19.2, 4.0, 5.2, 4.6)
O = dict(axis_p=p.tolist(), axis_d=d.tolist(), elev_deg=float(np.degrees(np.arcsin(d[2]))), az_deg=float(np.degrees(np.arctan2(d[1], d[0]))), tube=f)
Cl, Nl, Al = local_faces(p, d); rl = np.hypot(Cl[:, 0], Cl[:, 1])
s = (Cl[:, 2] > 20.9) & (Cl[:, 2] < 22.3) & (rl > 6.5) & (rl < 7.2) & (np.abs(Nl[:, 2]) < 0.3)
O['collar_R'] = float(np.median(rl[s])); O['collar_R_stats'] = stats(rl[s] - np.median(rl[s]))
for nm, sg, lo, hi, r0, r1 in [('collar_inner_face', -1, 19.7, 20.2, 5.4, 6.2), ('collar_outer_face', 1, 22.4, 22.8, 5.7, 6.6), ('end_face', 1, 29.6, 30.2, 2.0, 3.7)]:
    t = (sg * Nl[:, 2] > 0.95) & (Cl[:, 2] > lo) & (Cl[:, 2] < hi) & (rl > r0) & (rl < r1)
    O[nm] = dict(u=float(np.median(Cl[t, 2])), scatter=float(np.std(Cl[t, 2])), n=int(t.sum()))
Vo = local_verts(p, d); ro = np.hypot(Vo[:, 0], Vo[:, 1]); to = np.degrees(np.arctan2(Vo[:, 1], Vo[:, 0]))
O['oring'] = fit_arc_rz(p, d, 22.85, 24.35, 4.9, 5.7, None, [23.6, 4.5, 0.9])
s = (Vo[:, 2] > 25.0) & (Vo[:, 2] < 29.0) & (ro > 3.8) & (ro < 4.9)
O['thread_rho'] = dict(mean=float(ro[s].mean()), p1=float(np.percentile(ro[s], 1)), p99=float(np.percentile(ro[s], 99)),
                       p50=float(np.median(ro[s])), n=int(s.sum()))
# pitch by helical phase coherence of (rho - mean) over (u, theta), right- or left-hand
res_ = ro[s] - ro[s].mean(); us, ts = Vo[s, 2], np.radians(to[s]); best = []
for hand in (1, -1):
    for P_ in np.arange(0.80, 1.10, 0.002):
        ph = 2 * np.pi * (us - hand * P_ * ts / (2 * np.pi)) / P_
        best.append((float(np.abs((res_ * np.exp(1j * ph)).mean())), float(P_), hand))
best.sort(reverse=True)
O['thread_pitch'] = dict(pitch=best[0][1], hand=('right' if best[0][2] == 1 else 'left') + ' (sign convention: u along +outlet axis, theta CCW about it)',
                         coherence_amp=best[0][0], runner_up=[b for b in best if abs(b[1] - best[0][1]) > 0.05][:1])
s = (Vo[:, 2] > 29.3) & (Vo[:, 2] < 29.85) & (ro > 3.8) & (ro < 4.6)
cf = np.polyfit(Vo[s, 2], ro[s], 1); O['end_chamfer'] = dict(slope=float(cf[0]), rho_at_29p3=float(np.polyval(cf, 29.3)), rho_at_29p85=float(np.polyval(cf, 29.85)))
s = (ro > 1.4) & (ro < 1.95) & (Vo[:, 2] > 28.4) & (Vo[:, 2] < 29.8)
fb = fit_circle_irls(Vo[s, :2]); O['end_bore'] = dict(r=float(fb['r']), rms=float(fb['rms']))
s = (ro < 1.4) & (Vo[:, 2] > 27.8) & (Vo[:, 2] < 29.0)
O['end_bore_floor_u'] = dict(p50=float(np.median(Vo[s, 2])), p5=float(np.percentile(Vo[s, 2], 5)), n=int(s.sum()))
O['root_round'] = fit_arc_rz(p, d, 19.2, 19.95, 4.65, 5.3, None, [19.4, 5.2, 0.5])
O['collar_round'] = fit_arc_rz(p, d, 19.98, 20.9, 6.0, 6.87, None, [20.7, 6.2, 0.6])
out['outlet'] = O

# ---------------------------------------------------------------- 7. top barb
th0 = np.radians(55)
f, p, d = refine_axis([0, 0, 24.3], [np.cos(th0), np.sin(th0), 0.0], 13.5, 22.5, 2.3, 3.4, 2.75)
B = dict(axis_p=p.tolist(), axis_d=d.tolist(), elev_deg=float(np.degrees(np.arcsin(d[2]))), az_deg=float(np.degrees(np.arctan2(d[1], d[0]))), tube=f)
Cl, Nl, Al = local_faces(p, d); rl = np.hypot(Cl[:, 0], Cl[:, 1])
s = (Cl[:, 2] > 12.6) & (Cl[:, 2] < 22.5) & (rl > 2.4) & (rl < 3.1) & (np.abs(Nl[:, 2]) < 0.3)
B['tube_taper'] = fit_axis_cyl(Cl[s], 17.5, (0, 0, 2.75), taper=True, fix_tilt=True)
Vb = local_verts(p, d); rb = np.hypot(Vb[:, 0], Vb[:, 1])
for nm, sg, lo, hi, r0, r1 in [('rear_face', -1, -3.4, -2.7, 0.0, 1.9), ('end_face', 1, 28.0, 28.6, 1.3, 2.6)]:
    t = (sg * Nl[:, 2] > 0.9) & (Cl[:, 2] > lo) & (Cl[:, 2] < hi) & (rl > r0) & (rl < r1)
    B[nm] = dict(u=float(np.median(Cl[t, 2])), scatter=float(np.std(Cl[t, 2])), n=int(t.sum()))
s = (Vb[:, 2] > 25.1) & (Vb[:, 2] < 27.8) & (rb > 2.7) & (rb < 4.1)
cf = np.polyfit(Vb[s, 2], rb[s], 1); B['bulb_cone'] = dict(slope=float(cf[0]), half_angle_deg=float(np.degrees(np.arctan(-cf[0]))),
                                                             rho_at_25=float(np.polyval(cf, 25.0)), rho_at_28=float(np.polyval(cf, 28.0)), **stats(rb[s] - np.polyval(cf, Vb[s, 2])))
s = (Vb[:, 2] > 23.6) & (Vb[:, 2] < 24.7) & (rb > 2.8) & (rb < 3.9)
cf = np.polyfit(Vb[s, 2], rb[s], 1); B['flare'] = dict(slope=float(cf[0]), rho_at_23p6=float(np.polyval(cf, 23.6)), rho_at_24p7=float(np.polyval(cf, 24.7)), **stats(rb[s] - np.polyval(cf, Vb[s, 2])))
s = (Cl[:, 2] > 25.1) & (Cl[:, 2] < 27.9) & (rl > 2.6) & (rl < 4.2) & (np.abs(Nl[:, 2]) < 0.6)
B['bulb_cone_offset'] = fit_axis_cyl(Cl[s], 26.5, (0, 0, 3.4), taper=True, fix_tilt=True)   # bulb centre offset from the tube axis (local e1 ~ datum up)
s = (Vb[:, 2] > 24.75) & (Vb[:, 2] < 25.1) & (rb > 3.3)
B['bulb_max'] = dict(p50=float(np.median(rb[s])), p90=float(np.percentile(rb[s], 90)))
s = (rb > 0.9) & (rb < 1.5) & (Vb[:, 2] > 26.9) & (Vb[:, 2] < 28.2)
fb = fit_circle_irls(Vb[s, :2]); B['end_bore'] = dict(r=float(fb['r']), rms=float(fb['rms']))
s = (rb < 0.9) & (Vb[:, 2] > 26.0) & (Vb[:, 2] < 27.5)
B['end_bore_floor_u'] = dict(p50=float(np.median(Vb[s, 2])), p5=float(np.percentile(Vb[s, 2], 5)), n=int(s.sum()))
B['rear_round'] = fit_arc_rz(p, d, -3.1, -2.4, 1.6, 2.72, None, [-2.5, 2.1, 0.6])
out['barb'] = B

# ---------------------------------------------------------------- 8. ring windows (cap frame)
p, d = AX['cap_part']; Vc = local_verts(p, d); rc = np.hypot(Vc[:, 0], Vc[:, 1]); tc = np.degrees(np.arctan2(Vc[:, 1], Vc[:, 0]))
tcw = np.where(tc < -150, tc + 360, tc)   # theta domain [-150, 210): no window straddles it
s = (Vc[:, 2] > 13.0) & (Vc[:, 2] < 13.8) & (rc > 9) & (rc < 14)
b = np.floor(tcw[s] * 2) / 2; ub = np.unique(b); env = np.array([rc[s][b == x].max() for x in ub])
low = sorted(ub[env < 13.0].tolist())
groups = []
for x in low:
    if groups and x - groups[-1][-1] <= 1.5: groups[-1].append(x)   # merge gaps <= 1 deg (scan speckle)
    else: groups.append([x])
W = []
for g in groups:
    lo, hi = g[0], g[-1] + 0.5; c0 = 0.5 * (lo + hi); half = 0.5 * (hi - lo)
    dd = ((tc - c0 + 180) % 360) - 180
    t = (np.abs(dd) < half - 1.5) & (rc < 13.0) & (rc > 9.5) & (Vc[:, 2] > 11.5) & (Vc[:, 2] < 15.5)
    W.append(dict(theta_c=float(((c0 + 180) % 360) - 180), width_deg=float(hi - lo), chord_mm=float(2 * seg['cap_part']['R_ring'] * np.sin(np.radians(half))),
                  u_lo=float(np.percentile(Vc[t, 2], 1)), u_hi=float(np.percentile(Vc[t, 2], 99)),
                  floor_rho_p50=float(np.median(rc[t])), floor_rho_p10=float(np.percentile(rc[t], 10)), n=int(t.sum())))
out['ring_windows'] = W
(RUN / 'measure/figures/fits.json').write_text(json.dumps(out, indent=1, default=float))
print(json.dumps({k: v for k, v in out.items() if k not in ('tables_cols',) and not k.startswith('tab')}, indent=1, default=float)[:20000])

# ================================================================= it1 build 2 additions (self-check driven, see MODELING_PLAN §8)
F2 = json.loads((RUN / 'measure/figures/fits.json').read_text())
def bridged_floor(p, d, rmax, ulo, uhi):
    Cl, Nl, Al = local_faces(p, d); r = np.hypot(Cl[:, 0], Cl[:, 1]); s = (r < rmax) & (Cl[:, 2] > ulo) & (Cl[:, 2] < uhi)
    u = Cl[s, 2]; w = Al[s]; o = np.argsort(u); cw = np.cumsum(w[o]) / w.sum()
    q = lambda f: float(u[o][np.searchsorted(cw, f)])
    return dict(u_p10=q(0.1), u_p50=q(0.5), u_p90=q(0.9), area_mm2=float(w.sum()), n=int(s.sum()),
                method='area-weighted quantiles of the axial position of scan faces inside the bore radius (the scanner bridge)')
ax_n = F2['axes']['nozzle']
F2['bore_floors'] = {'nozzle': bridged_floor(ax_n['p'], ax_n['d'], 3.4, -27.0, -20.0),
                     'outlet': bridged_floor(F2['outlet']['axis_p'], F2['outlet']['axis_d'], 1.4, 26.0, 30.5),
                     'barb': bridged_floor(F2['barb']['axis_p'], F2['barb']['axis_d'], 1.0, 25.0, 28.8)}
# latch windows on both lug b-sides (nozzle frame): angular extent where the wall is cut, floor radius
Vn = local_verts(ax_n['p'], ax_n['d']); rn = np.hypot(Vn[:, 0], Vn[:, 1]); tn = np.degrees(np.arctan2(Vn[:, 1], Vn[:, 0]))
lg_ = F2['lip']; Rn_ = F2['segments']['nozzle']['R']
def outline_r(t):
    ds = np.linspace(0, 9, 1801); P_ = np.c_[np.cos(np.radians(t)) * ds, np.sin(np.radians(t)) * ds]
    return ds[np.where((rect_sdf(P_, [lg_['cx'], lg_['cy'], lg_['half_a'], lg_['half_b'], lg_['corner_r'], lg_['phi_deg']]) <= 0) | (ds <= Rn_))[0].max()]
lat = []
for c0 in (lg_['phi_deg'] + 90.0, lg_['phi_deg'] - 90.0):
    dd = ((tn - c0 + 180) % 360) - 180
    band = (Vn[:, 2] > -25.2) & (Vn[:, 2] < -24.65) & (np.abs(dd) < 60)
    b = np.floor(dd[band] / 4) * 4; bins = []
    for x in np.unique(b):
        env = float(rn[band][b == x].max()); bins.append((float(x + 2), env, float(outline_r(x + 2 + c0)) - env))
    bins = np.array(bins)
    rec = bins[bins[:, 2] > 0.25]; lo_, hi_ = rec[:, 0].min() - 2, rec[:, 0].max() + 2   # contiguous around the side normal
    core = bins[(bins[:, 0] > lo_ + 8) & (bins[:, 0] < hi_ - 8)]
    deep = bins[bins[:, 1] < 5.3]
    s = (np.abs(dd - 0.5 * (lo_ + hi_)) < 0.5 * (hi_ - lo_)) & (Vn[:, 2] > -25.8) & (Vn[:, 2] < -23.9) & (rn < Rn_ - 0.12) & (rn > 3.99)
    rowd = dict(side_theta_deg=float(c0), recess_theta=[float(lo_ + c0), float(hi_ + c0)], recess_floor_rho=float(np.median(core[core[:, 1] >= 5.3, 1])),
                u_p3_p97=np.percentile(Vn[s, 2], [3, 97]).tolist(), bins_dtheta_env_deficit=bins.round(3).tolist(),
                method='4-deg bins of the outer envelope in u -25.2..-24.65 vs the fitted lug outline; recess = bins > 0.25 mm inside the outline')
    if len(deep) >= 3:
        dl = deep[:, 0]; runs = np.split(dl, np.where(np.diff(dl) > 4.5)[0] + 1); r0 = max(runs, key=len)
        if len(r0) >= 3:
            rowd['deep_theta'] = [float(r0.min() - 2 + c0), float(r0.max() + 2 + c0)]
            rowd['deep_floor_rho'] = float(np.median(deep[np.isin(deep[:, 0], r0), 1]))
    lat.append(rowd)
F2['latch_windows'] = lat
# ring windows: floor = median radius of interior points deeper than 0.7 mm below the ring surface
pc_, dc_ = F2['axes']['cap_part']['p'], F2['axes']['cap_part']['d']
Vc = local_verts(pc_, dc_); rc = np.hypot(Vc[:, 0], Vc[:, 1]); tc = np.degrees(np.arctan2(Vc[:, 1], Vc[:, 0]))
for wd in F2['ring_windows']:
    dd = ((tc - wd['theta_c'] + 180) % 360) - 180
    t = (np.abs(dd) < wd['width_deg'] / 4) & (Vc[:, 2] > wd['u_lo']) & (Vc[:, 2] < wd['u_hi']) & (rc < F2['segments']['cap_part']['R_ring'] - 0.7) & (rc > 9.5)
    wd['floor_rho_deep_median'] = float(np.median(rc[t])); wd['floor_n'] = int(t.sum())
# slits under the ring skirt (open loops L5, L7): sector extents in the cap frame
sl_ = []
ub_ = F2['levels']['ring_bottom']['u_median']
for c0 in (-146.0, 163.0):
    dd = ((tc - c0 + 180) % 360) - 180
    s = (np.abs(dd) < 20) & (rc > 10.1) & (rc < 11.8) & (Vc[:, 2] > ub_ + 0.35) & (Vc[:, 2] < 12.5)   # above the ring bottom, inside the skirt
    sl_.append(dict(theta_p2_p98=(np.percentile(dd[s], [2, 98]) + c0).tolist(), u_p98=float(np.percentile(Vc[s, 2], 98)),
                    rho_p2_p98=np.percentile(rc[s], [2, 98]).tolist(), n=int(s.sum()),
                    method='scan vertices 0.35 mm or more above the ring bottom face, rho 10.1..11.8 (inside the skirt), +-20 deg'))
F2['skirt_slits'] = sl_
# web between the outlet tube top and the ring bottom (datum frame, z 8.3..8.5 sections)
secs = []
for zz in (8.3, 8.4, 8.5):
    sec = mesh().section(plane_origin=[0, 0, zz], plane_normal=[0, 0, 1]); P = np.asarray(sec.vertices)
    for x in np.arange(10.25, 12.76, 0.25):
        s = (np.abs(P[:, 0] - x) < 0.06) & (np.abs(P[:, 1]) < 5.5)
        if s.sum() >= 2:
            secs.append((zz, float(x), float(P[s, 1].min()), float(P[s, 1].max())))
secs = np.array(secs)
ok_ = (secs[:, 2] < -0.1) & (secs[:, 3] > -0.2) & ((secs[:, 3] - secs[:, 2]) > 0.2)
hw_ = (secs[ok_, 3] - secs[ok_, 2]) / 2; yc_ = (secs[ok_, 3] + secs[ok_, 2]) / 2; xs_ = secs[ok_, 1]
cf_ = np.polyfit(xs_, hw_, 1)
F2['outlet_ring_web'] = dict(sections=secs.tolist(), hw_slope=float(cf_[0]), hw_at_10p5=float(np.polyval(cf_, 10.5)),
                             x_end=float(-cf_[1] / cf_[0]), y_centre=float(np.median(yc_)), fit=stats(hw_ - np.polyval(cf_, xs_)),
                             n_sections=int(ok_.sum()),
                             note='z 8.3..8.5 lies above the outlet tube top (8.03) and below the ring bottom (~8.9): the scan material there is a web; top view = trapezoid, half-width linear in x')
(RUN / 'measure/figures/fits.json').write_text(json.dumps(F2, indent=1, default=float))
print(json.dumps({k: F2[k] for k in ('bore_floors', 'latch_windows', 'skirt_slits')}, indent=1, default=float)[:6000])
print([ (w['theta_c'], w['floor_rho_deep_median'], w['floor_n']) for w in F2['ring_windows']])
print({k: v for k, v in F2['outlet_ring_web'].items() if k != 'sections'})
