"""Run-local: per-10deg-sector median z of up-facing faces in named r/z windows (full-res scan, datum frame)."""
import json, numpy as np, trimesh
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4'])
m.apply_transform(T)
c = m.triangles_center; n = m.face_normals; a = m.area_faces
r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360
W = {'rim_lip_top': (37.4, 38.2, 2.8, 3.6), 'rim_ledge': (38.8, 39.6, 2.0, 2.8), 'lug_top': (31.8, 34.0, -0.6, 0.6),
     'lug_channel': (34.8, 36.8, -3.6, -2.2), 'shelf': (32.5, 36.0, -15.0, -12.8), 'pocket_outer': (34.6, 36.6, -16.0, -14.6),
     'pocket_inner': (31.8, 33.6, -17.6, -16.2), 'floor': (25.0, 30.0, -20.6, -19.4)}
out = {}
for k, (r0, r1, z0, z1) in W.items():
    s = (n[:, 2] > 0.9) & (r > r0) & (r < r1) & (c[:, 2] > z0) & (c[:, 2] < z1)
    sec = {}
    for b in range(36):
        t = s & ((th // 10) == b)
        if a[t].sum() > 3: sec[b * 10] = round(float(np.median(c[t, 2])), 3)
    P = c[s]; A = np.c_[P[:, 0], P[:, 1], np.ones(len(P))]; sol = np.linalg.lstsq(A, P[:, 2], rcond=None)[0]
    res = P[:, 2] - A @ sol
    out[k] = {'n': int(s.sum()), 'area': round(float(a[s].sum()), 1), 'z_p50': round(float(np.median(P[:, 2])), 3),
              'z_p5_p95': [round(float(x), 3) for x in np.percentile(P[:, 2], [5, 95])],
              'plane_fit_slope_deg': round(float(np.degrees(np.arctan(np.hypot(*sol[:2])))), 3),
              'plane_fit_dir_deg': round(float(np.degrees(np.arctan2(sol[1], sol[0]))), 1), 'plane_fit_rms': round(float(res.std()), 3),
              'sector_median_z': sec}
    print(k, {kk: vv for kk, vv in out[k].items() if kk != 'sector_median_z'}); print('   ', sec)
json.dump(out, open('measure/figures/levels.json', 'w'), indent=1)
