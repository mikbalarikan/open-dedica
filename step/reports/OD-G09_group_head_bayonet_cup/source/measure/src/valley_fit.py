"""Run-local: analytic fits for the under-lug floors and the shelf edge (full-res scan, datum frame).
 - outer band (r 34.8-36.6) and pocket inner floor (r 31.8-34.0): concave horizontal-axis cylinder per
   lug, axis along the radial direction at theta_c, surface z = z_axis - sqrt(Rc^2 - (r sin(theta-theta_c))^2)
 - shelf-edge rounding in gap sectors: arc tangent to the shelf plane (per-gap level) and the lip wall
 - bore recess behind the lugs: median r of vertical faces
Writes measure/figures/valley_fit.json"""
import json, numpy as np, trimesh
from scipy.optimize import least_squares
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); m.apply_transform(T)
c = m.triangles_center; n = m.face_normals; r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360; z = c[:, 2]
up = n[:, 2] > 0.85; vert = np.abs(n[:, 2]) < 0.3
P = json.load(open('measure/params.json'))['params']
starts = [P['LUG1_START_DEG']['value'] + k * 120.0 for k in range(3)]
shelf = P['SHELF_Z']['value']; L = P['LIP_UPPER_R']['value']
def cylfit(sel, s0):
    rr, tt, zz = r[sel], np.radians(th[sel]), z[sel]
    def res(p):
        tc, zmin, Rc = p
        s = rr * np.sin(tt - np.radians(tc))
        return (zmin + Rc - np.sqrt(np.maximum(Rc ** 2 - s ** 2, 1e-9))) - zz
    sol = least_squares(res, [s0, zz.min() + 0.2, 300.0], loss='soft_l1', f_scale=0.1, bounds=([s0 - 40, -20, 30], [s0 + 40, -10, 5000]))
    rs = res(sol.x)
    return {'theta_c_deg': round(float(sol.x[0] % 360), 2), 'z_min': round(float(sol.x[1]), 3), 'Rc': round(float(sol.x[2]), 1),
            'rms': round(float(np.sqrt(np.mean(rs ** 2))), 3), 'p95_abs': round(float(np.percentile(np.abs(rs), 95)), 3), 'n': int(sel.sum())}
def win(t0, t1): return ((th - t0) % 360) < ((t1 - t0) % 360)
out = {'outer_valley': [], 'pocket_inner': [], 'shelf_edge': [], 'bore_recess': {}}
for k, s in enumerate(starts):
    gprev, gnext = shelf[(k - 1) % 3], shelf[k]
    sel = up & (r > 34.8) & (r < 36.6) & win(s - 25, s + 80) & (z < -12.5) & (z > -16.0)
    sel &= z < np.where(((th - s) % 360) > 180, gprev, gnext) - 0.10          # exclude the flat gap-level parts
    out['outer_valley'].append(cylfit(sel, s + 25))
    sel2 = up & (r > 31.8) & (r < 34.0) & win(s - 3, s + 56) & (z < -15.4) & (z > -17.5)
    out['pocket_inner'].append(cylfit(sel2, s + 27))
for k, s in enumerate(starts):
    zs = shelf[k]; g0, g1 = s + 58.5 + 3, s + 115 - 3
    sel = win(g0 % 360, g1 % 360) & (r > L + 0.05) & (r < L + 3.0) & (z < zs - 0.05) & (z > zs - 3.0) & (n[:, 2] > 0.1)
    rr, zz = r[sel], z[sel]
    def res(p):
        Rf = p[0]; cr, cz = L + Rf, zs - Rf
        d = np.hypot(rr - cr, zz - cz); inq = (rr < cr) & (zz > cz)
        return np.where(inq, d - Rf, 0.0)
    sol = least_squares(res, [1.5], loss='soft_l1', f_scale=0.1, bounds=([0.3], [3.0]))
    rs = res(sol.x); cr, cz = L + sol.x[0], zs - sol.x[0]; inq = (rr < cr) & (zz > cz)
    out['shelf_edge'].append({'gap': k + 1, 'R': round(float(sol.x[0]), 3), 'rms': round(float(np.sqrt(np.mean(rs[inq] ** 2))), 3), 'n': int(inq.sum())})
rec = vert & (r > 36.9) & (r < 37.9) & (z > -15) & (z < -5) & np.any([win(s, s + 54) for s in starts[:2]], axis=0)
out['bore_recess'] = {'r_p50': round(float(np.median(r[rec])), 3), 'r_p5_p95': [round(float(v), 3) for v in np.percentile(r[rec], [5, 95])], 'n': int(rec.sum()),
                      'note': 'lugs 1-2 only; lug 3 sector behind the lug is a coverage gap'}
json.dump(out, open('measure/figures/valley_fit.json', 'w'), indent=1); print(json.dumps(out, indent=1))
