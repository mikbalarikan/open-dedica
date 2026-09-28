"""Pad on the +X cup wall: per-z circle fits (Kasa) on the pad face points (normal ~ outward, r > cup
cone + 0.25, |y| < 12.5, outside the arch). Reports centre (x,y) and radius vs z; then a cone with a
vertical axis (x0, y0, R(z) = R0 + k z) fitted to all pad points."""
import json, numpy as np, trimesh
from scipy import optimize
m = trimesh.load('intake/aligned_work.stl'); P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0); Nf = m.face_normals[fi]
r = np.hypot(P[:, 0], P[:, 1]); cone = 30.5864 + 0.044919 * P[:, 2]
arch = (np.abs(P[:, 1]) < 10.3) & (P[:, 2] < -20.2)
pad = (P[:, 0] > 20) & (P[:, 0] < 34) & (np.abs(P[:, 1]) < 12.3) & (P[:, 2] > -32) & (P[:, 2] < -3) & (r - cone > 0.15) & ~arch & (Nf[:, 0] > 0.6) & (np.abs(Nf[:, 2]) < 0.4)
st = []
for zc in np.arange(-31, -3, 1.0):
    s = pad & (np.abs(P[:, 2] - zc) < 0.5)
    if s.sum() < 40: continue
    x, y = P[s, 0], P[s, 1]; A = np.c_[2*x, 2*y, np.ones(len(x))]; c, *_ = np.linalg.lstsq(A, x*x + y*y, rcond=None)
    R = np.sqrt(c[2] + c[0]**2 + c[1]**2); res = np.hypot(x-c[0], y-c[1]) - R
    st.append({"z": float(zc), "xc": float(c[0]), "yc": float(c[1]), "R": float(R), "rms": float(np.sqrt((res**2).mean())), "n": int(s.sum()), "y_span": [float(y.min()), float(y.max())]})
x, y, z = P[pad, 0], P[pad, 1], P[pad, 2]
f = lambda p: np.hypot(x - p[0], y - p[1]) - (p[2] + p[3] * z)
sol = optimize.least_squares(f, [-8, 0, 39, -0.1]); e = sol.fun
out = {"stations": st, "cone_vertical_axis": {"x0": sol.x[0], "y0": sol.x[1], "R0_at_z0": sol.x[2], "dRdz": sol.x[3],
       "rms": float(np.sqrt((e**2).mean())), "p95": float(np.percentile(np.abs(e), 95)), "max": float(np.abs(e).max()), "n": int(pad.sum())}}
out["cone_vertical_axis"] = {k: float(v) for k, v in out["cone_vertical_axis"].items()}
# plane alternative
A = np.c_[y, z, np.ones(len(x))]; c, *_ = np.linalg.lstsq(A, x, rcond=None); e2 = x - A @ c
out["plane_alternative"] = {"coef_x_eq_ay_bz_c": c.tolist(), "rms": float(np.sqrt((e2**2).mean()))}
json.dump(out, open('measure/figures/pad_fit.json', 'w'), indent=1)
for s_ in st[::3]: print(s_)
print(out["cone_vertical_axis"], out["plane_alternative"])
