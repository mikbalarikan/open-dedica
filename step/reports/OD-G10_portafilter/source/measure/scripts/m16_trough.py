"""it2 (verify it1 clusters 0/2/3): the +X floor is a trough running along the insert wall between the two
outlet pockets. From the top-view height map: cells with r in [13, 23.6], theta between the two spout
angles (m07), away from the pockets (< 4.5 mm from a spout axis excluded), off the ribs (H < -39.3), not a see-through shadow cell (H > -44.5), and
with data. Fit a circular (r,z) section revolved about the cup axis: z = zc - sqrt(rho^2 - (r - rc)^2),
first with constant (rc, zc, rho), then with zc linear in |theta| (depth growing toward the pockets).
Also the per-10-degree median bottom depth."""
import json, numpy as np
from scipy import optimize
H = np.load('measure/figures/floor_heightmap_max_z.npy'); res = 0.2; n = H.shape[0]; xs = -25 + res * (np.arange(n) + .5); X, Y = np.meshgrid(xs, xs)
R = np.hypot(X, Y); TH = np.degrees(np.arctan2(Y, X))
S = json.load(open('measure/figures/spouts_screw.json'))
t0, t1 = S['spout_1']['theta_deg'], S['spout_0']['theta_deg']
pk = np.zeros_like(R, bool)
for k in ('spout_0', 'spout_1'): pk |= np.hypot(X - S[k]['cx'], Y - S[k]['cy']) < 4.5
sel = (~np.isnan(H)) & (R > 13) & (R < 23.6) & (TH > t0) & (TH < t1) & ~pk & (H < -39.3) & (H > -44.5)
r, z, th = R[sel], H[sel], TH[sel]
def m1(p, r, th): rc, zc, rho = p; return zc - np.sqrt(np.clip(rho**2 - (r - rc)**2, 0, None))
s1 = optimize.least_squares(lambda p: m1(p, r, th) - z, [18.5, -38.0, 5.0]); e1 = s1.fun
def m2(p, r, th): rc, zc, rho, k = p; return (zc + k * np.abs(th)) - np.sqrt(np.clip(rho**2 - (r - rc)**2, 0, None))
s2 = optimize.least_squares(lambda p: m2(p, r, th) - z, [18.5, -38.0, 5.0, 0.0]); e2 = s2.fun
st = lambda e: {"rms": float(np.sqrt((e**2).mean())), "p95": float(np.percentile(np.abs(e), 95)), "max": float(np.abs(e).max())}
out = {"theta_range_deg": [float(t0), float(t1)], "n_cells": int(sel.sum()),
       "const": {"rc": float(s1.x[0]), "zc": float(s1.x[1]), "rho": float(s1.x[2]), **st(e1)},
       "zc_linear_in_abs_theta": {"rc": float(s2.x[0]), "zc0": float(s2.x[1]), "rho": float(s2.x[2]), "dzc_per_deg": float(s2.x[3]), **st(e2)},
       "bottom_by_theta": [[float(a), float(np.percentile(z[(th >= a) & (th < a + 10)], 5))] for a in range(int(t0) - 1, int(t1) + 1, 10) if ((th >= a) & (th < a + 10)).sum() > 30]}
json.dump(out, open('measure/figures/trough.json', 'w'), indent=1); print(json.dumps(out, indent=1))
