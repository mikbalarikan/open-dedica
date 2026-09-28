"""m03_profile_fits.py - fits on the meridian profiles written by m02 (cups A/B, boss).
Estimators: median per z- or r-window, least-squares lines, Kasa circles for corner rounds.
Writes measure/figures/m03_profile_fits.json."""
import json, numpy as np
def win(d, zr=None, rr=None):
    k = np.ones(len(d['r']), bool)
    if zr: k &= (d['z'] >= zr[0]) & (d['z'] <= zr[1])
    if rr: k &= (d['r'] >= rr[0]) & (d['r'] <= rr[1])
    return d['r'][k], d['z'][k]
def line(a, b):
    A = np.c_[np.ones(len(a)), a]; c, *_ = np.linalg.lstsq(A, b, rcond=None)
    res = b - A @ c
    return {"c0": float(c[0]), "c1": float(c[1]), "rms": float(np.sqrt((res**2).mean())), "n": int(len(a))}
def kasa(x, y):
    A = np.c_[2*x, 2*y, np.ones(len(x))]; b = x**2 + y**2
    s, *_ = np.linalg.lstsq(A, b, rcond=None); r = np.sqrt(s[2] + s[0]**2 + s[1]**2)
    res = np.hypot(x - s[0], y - s[1]) - r
    return {"cr": float(s[0]), "cz": float(s[1]), "R": float(r), "rms": float(np.sqrt((res**2).mean())), "n": int(len(x))}
out = {"tool": "measure/scripts/m03_profile_fits.py"}
for nm in ('cupA', 'cupB'):
    d = dict(np.load(f'measure/figures/m02_profile_{nm}.npz'))
    o = {}
    r, z = win(d, (0.9, 6.4), (11.3, 12.4)); o['lower_wall_r_vs_z'] = line(z, r)
    o['lower_wall_r_at_z0'] = o['lower_wall_r_vs_z']['c0']
    o['lower_wall_draft_deg'] = float(np.degrees(np.arctan(-o['lower_wall_r_vs_z']['c1'])))
    r, z = win(d, (7.9, 10.6), (10.4, 11.7)); o['upper_wall_r_vs_z'] = line(z, r)
    o['upper_wall_r_p50'] = float(np.median(r))
    o['upper_wall_draft_deg'] = float(np.degrees(np.arctan(-o['upper_wall_r_vs_z']['c1'])))
    # step: per 0.05 z-bin median r between 6.4 and 8.2
    bins = np.arange(6.4, 8.2, 0.1); prof = []
    for b0 in bins:
        rr, zz = win(d, (b0, b0 + 0.1), (10.4, 12.2))
        if len(rr) > 10: prof.append((b0 + 0.05, float(np.median(rr))))
    o['step_profile'] = prof
    r, z = win(d, (11.6, 13.0), (8.7, 9.8)); o['top_face_z_p50'] = float(np.median(z)); o['top_face_n'] = int(len(z))
    r, z = win(d, (11.5, 12.6), (9.4, 10.4)); o['top_face_z_outer_p50'] = float(np.median(z))
    r, z = win(d, (12.6, 15.0), (4.4, 7.4)); o['shoulder_z_vs_r'] = line(r, z)
    o['shoulder_angle_deg_from_horizontal'] = float(np.degrees(np.arctan(-o['shoulder_z_vs_r']['c1'])))
    r, z = win(d, (16.8, 22.8), (2.0, 3.3)); o['shank_r_p50'] = float(np.median(r)); o['shank_r_p10_p90'] = [float(np.percentile(r, 10)), float(np.percentile(r, 90))]
    o['shank_r_vs_z'] = line(z, r)
    r, z = win(d, (23.6, 25.0), (2.8, 3.8)); i = np.argsort(r)[-50:]; o['lip_r_top50_median'] = float(np.median(r[i])); o['lip_z_at_rmax'] = float(np.median(z[i]))
    r, z = win(d, (25.0, 27.9), (2.4, 3.6)); o['barb_taper_r_vs_z'] = line(z, r)
    r, z = win(d, (23.0, 24.2), (2.4, 3.6)); o['barb_flare_r_vs_z'] = line(z, r)
    r, z = win(d, (28.0, 29.0), (1.9, 2.8)); o['barb_top_z_p50'] = float(np.median(z)); o['barb_top_n'] = int(len(z))
    # corner rounds (Kasa on profile points)
    r, z = win(d, (10.9, 12.45), (10.2, 11.3)); k = (z - 11.0) + (r - 10.2) > 0.3; o['top_corner_round'] = kasa(r[k], z[k])
    r, z = win(d, (14.6, 16.4), (2.6, 3.9)); o['shank_fillet'] = kasa(r, z)
    out[nm] = o
d = dict(np.load('measure/figures/m02_profile_boss.npz')); o = {}
r, z = win(d, (1.0, 10.5), (5.5, 7.0)); o['wall_r_vs_z'] = line(z, r); o['wall_r_p50'] = float(np.median(r))
r, z = win(d, (11.8, 13.0), (2.6, 5.0)); o['top_z_p50'] = float(np.median(z)); o['top_z_vs_r'] = line(r, z)
r, z = win(d, (10.8, 12.7), (5.0, 6.6)); k = (z > 11.3) & (r > 5.2); o['top_corner_round'] = kasa(r[k], z[k])
r, z = win(d, (10.5, 12.7), (1.5, 2.6)); o['hole_edge_r_p50'] = float(np.median(r)); o['hole_edge_n'] = int(len(r))
out['boss'] = o
json.dump(out, open('measure/figures/m03_profile_fits.json', 'w'), indent=1)
for nm in ('cupA', 'cupB', 'boss'):
    print(nm, json.dumps({k: v for k, v in out[nm].items() if k != 'step_profile'}))
print('stepA', out['cupA']['step_profile']); print('stepB', out['cupB']['step_profile'])
