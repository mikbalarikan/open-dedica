"""it2 (verify it1 CHK-FILLET finding, overlay x=40): the neck legs end in rounded feet. In the handle-axis
frame (handle_axis.json), per x-section at x = 33..41 (1 mm), the scan points of each leg with w < -5 and
|v| in [5.5, 10.5]; Kasa circle fit to the lowest 1.8 mm of each leg (the foot round) -> radius, centre."""
import json, numpy as np, trimesh
A = json.load(open('measure/figures/handle_axis.json')); p0 = np.array(A['axis_point_x0']); d = np.array(A['axis_dir'])
m = trimesh.load('intake/aligned_work.stl'); out = []
for x in np.arange(33.0, 41.5, 1.0):
    L = trimesh.intersections.mesh_plane(m, [1, 0, 0], [x, 0, 0]).reshape(-1, 3)
    v = L[:, 1] - (p0[1] + d[1] / d[0] * x); w = L[:, 2] - (p0[2] + d[2] / d[0] * x)
    for sgn in (1, -1):
        s = (sgn * v > 5.5) & (sgn * v < 10.5) & (w < -5)
        if s.sum() < 20: continue
        wm = w[s].min(); f = s & (w < wm + 1.8); vv, ww = v[f], w[f]
        Am = np.c_[2 * vv, 2 * ww, np.ones(len(vv))]; c, *_ = np.linalg.lstsq(Am, vv**2 + ww**2, rcond=None)
        R = float(np.sqrt(c[2] + c[0]**2 + c[1]**2)); res = np.hypot(vv - c[0], ww - c[1]) - R
        out.append({"x": float(x), "side": sgn, "foot_w_min": float(wm), "R": R, "cv": float(c[0]), "cw": float(c[1]), "rms": float(np.sqrt((res**2).mean())), "n": int(f.sum())})
Rs = np.array([o["R"] for o in out])
res = {"sections": out, "R_median": float(np.median(Rs)), "R_p25_p75": [float(np.percentile(Rs, 25)), float(np.percentile(Rs, 75))]}
json.dump(res, open('measure/figures/arch_feet.json', 'w'), indent=1)
for o in out: print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in o.items()})
print('R median', res['R_median'], res['R_p25_p75'])
