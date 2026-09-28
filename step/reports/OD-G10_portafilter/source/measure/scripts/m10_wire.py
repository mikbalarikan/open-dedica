"""(v2: wire radius fixed from the cleanest segment, core points z > -5.0 only, ends that dive into the
windows are excluded.) Retaining wire spring: the three exposed wire segments inside the rim bore. Points with
r in [21, 27.35] and z in [-7.5, -1.6] (inside the bore, above the ledge), clustered by angle.
Per segment: circle fit (Kasa) of the xy trace of the wire's inner-most (bore-facing away) points,
median z of the wire top/bottom -> centre z and wire diameter, angular span."""
import json, numpy as np, trimesh
from scipy import optimize
m = trimesh.load('intake/aligned_work.stl'); P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0)
r = np.hypot(P[:, 0], P[:, 1]); th = np.degrees(np.arctan2(P[:, 1], P[:, 0])) % 360
s = (r > 21) & (r < 27.3) & (P[:, 2] > -7.5) & (P[:, 2] < -1.6)
segs = []
WIRE_R = None
order = np.argsort(th[s]); ths = th[s][order]
gaps = np.where(np.diff(ths) > 8)[0]
bounds = [ths[0]] + sum([[ths[g], ths[g + 1]] for g in gaps], []) + [ths[-1]]
groups = [(bounds[i], bounds[i + 1]) for i in range(0, len(bounds), 2)]
# merge wrap-around
if len(groups) > 1 and groups[0][0] < 5 and groups[-1][1] > 355: groups = [(groups[-1][0], groups[0][1] + 360)] + groups[1:-1]
groups.sort(key=lambda g: 0 if g[0] < 5 or g[1] > 360 else 1)
for a0, a1 in groups:
    tt = th.copy(); tt[tt < a0 - 1e-6] += 360
    g = s & (tt >= a0) & (tt <= a1)
    if g.sum() < 300: continue
    Q = P[g]
    # wire axis path ~ circle in xy; the wire is a tube of radius a: fit a torus section: centre (cx,cy), R, zc, a
    Q = Q[Q[:, 2] > -5.0] if WIRE_R is not None else Q
    def f(p):
        cx, cy, R, zc = p[:4]; a = p[4] if WIRE_R is None else WIRE_R
        rho = np.hypot(Q[:, 0] - cx, Q[:, 1] - cy)
        return np.hypot(rho - R, Q[:, 2] - zc) - a
    thm = np.radians((a0 + a1) / 2)
    sol = optimize.least_squares(f, [0.0, 0.0, 26.0, -3.3, 0.6] if WIRE_R is None else [0.0, 0.0, 26.0, -3.3], loss='soft_l1', f_scale=0.1)
    if WIRE_R is None: WIRE_R = abs(sol.x[4])
    e = f(sol.x)
    segs.append({"theta_span_deg": [float(a0 % 360), float(a1 % 360)], "n": int(g.sum()), "cx": float(sol.x[0]), "cy": float(sol.x[1]),
                 "R": float(sol.x[2]), "zc": float(sol.x[3]), "wire_r": float(WIRE_R),
                 "rms": float(np.sqrt(np.mean(e**2))), "p90_abs": float(np.percentile(np.abs(e), 90))})
json.dump({"segments": segs}, open('measure/figures/wire.json', 'w'), indent=1)
for x in segs: print(x)
