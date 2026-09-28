"""Interior (pressurised insert): rib paths and floor surfaces from the top-view height map
(max z per 0.2 mm cell of 2.5M seeded surface samples, x,y in [-25,25], z in [-60,-20]; built by
the same sampling as m03). U rib: cells with z > -28.2; V ribs: -30.5 < z < -28.2 and outside the U.
Floor: vertical-axis cone (funnel) outside the U, plane inside the U (least squares on flat cells)."""
import json, numpy as np
from scipy import ndimage, optimize
H = np.load('measure/figures/floor_heightmap_max_z.npy'); res = 0.2; x0 = -25
n = H.shape[0]; xs = x0 + res * (np.arange(n) + 0.5); X, Y = np.meshgrid(xs, xs); R = np.hypot(X, Y)
out = {}
U = (H > -28.2) & (R < 21.5)
out["U_top_z"] = float(np.median(H[U]))
V = (H > -30.5) & (H < -28.2) & (R < 22.5) & (X > -12)
V = ndimage.binary_opening(V, iterations=1)
for sgn, key in ((1, "V_pos"), (-1, "V_neg")):
    s = V & (np.sign(Y) == sgn) & (np.abs(Y) > 2)
    px, py = X[s], Y[s]; c = np.c_[px, py].mean(0); u, sv, vt = np.linalg.svd(np.c_[px, py] - c); d = vt[0]
    if d[0] < 0: d = -d
    t = (np.c_[px, py] - c) @ d; nrm = (np.c_[px, py] - c) @ np.array([-d[1], d[0]])
    out[key] = {"centre": c.tolist(), "dir": d.tolist(), "t_min": float(np.percentile(t, 0.5)), "t_max": float(np.percentile(t, 99.5)),
                "top_width_p02_p98": [float(np.percentile(nrm, 2)), float(np.percentile(nrm, 98))], "top_z": float(np.median(H[s])),
                "end_inner": (c + d * np.percentile(t, 99.5)).tolist(), "end_outer": (c + d * np.percentile(t, 0.5)).tolist()}
# floor fits
nanm = np.isnan(H); idx = ndimage.distance_transform_edt(nanm, return_distances=False, return_indices=True)
Hs = ndimage.median_filter(H[tuple(idx)], 5); gy, gx = np.gradient(Hs, res); g = np.hypot(gx, gy)
ok = (~nanm) & (R < 21) & (H < -33.0) & (H > -41.8) & ndimage.binary_erosion(g < 0.5, iterations=2)
inU = ((X > -15) & (X < 3.2) & (np.abs(Y) < 4.6)) | ((np.hypot(X - 3.2, Y) < 4.6) & (X >= 3.2))
s = ok & ~inU; x, y, z = X[s], Y[s], H[s]
sol = optimize.least_squares(lambda p: p[0] + p[1] * np.hypot(x - p[2], y - p[3]) - z, [-40, 0.2, 20, 0]); e = sol.fun
out["floor_funnel_cone"] = {"apex_z": float(sol.x[0]), "slope_dz_dr": float(sol.x[1]), "axis_x": float(sol.x[2]), "axis_y": float(sol.x[3]),
                            "rms": float(np.sqrt((e**2).mean())), "p95": float(np.percentile(np.abs(e), 95)), "max": float(np.abs(e).max()), "n_cells": int(s.sum())}
s = ok & inU; A = np.c_[np.ones(s.sum()), X[s], Y[s]]; c, *_ = np.linalg.lstsq(A, H[s], rcond=None); e = H[s] - A @ c
out["floor_in_U_plane"] = {"z0": float(c[0]), "dz_dx": float(c[1]), "dz_dy": float(c[2]), "rms": float(np.sqrt((e**2).mean())), "p95": float(np.percentile(np.abs(e), 95)), "n_cells": int(s.sum())}
json.dump(out, open('measure/figures/ribs_floor.json', 'w'), indent=1); print(json.dumps(out, indent=1))
