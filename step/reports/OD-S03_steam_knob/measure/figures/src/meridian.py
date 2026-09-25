"""Meridian (r,z) half-sections in a local frame (centre cx,cy, optional tilt), several azimuths.
Usage: meridian.py RUN name cx cy dxdz dydz z0ref thetas(comma) -> ../meridian_<name>.npz + RDP print"""
import json, sys, numpy as np, trimesh
RUN, name = sys.argv[1], sys.argv[2]; cx, cy, dxdz, dydz, zref = map(float, sys.argv[3:8]); thetas = [float(t) for t in sys.argv[8].split(",")]
eps = float(sys.argv[9]) if len(sys.argv) > 9 else 0.02
m = trimesh.load(f"{RUN}/intake/aligned_work.stl")
V = m.vertices.copy(); V[:, 0] -= cx + dxdz * (V[:, 2] - zref); V[:, 1] -= cy + dydz * (V[:, 2] - zref)
m2 = trimesh.Trimesh(V, m.faces, process=False)
def rdp(P, e):
    if len(P) < 3: return P
    a, b = P[0], P[-1]; d = b - a; Ln = np.linalg.norm(d)
    dist = np.abs(d[0]*(P[:, 1]-a[1]) - d[1]*(P[:, 0]-a[0]))/Ln if Ln > 1e-12 else np.linalg.norm(P-a, axis=1)
    i = int(np.argmax(dist))
    return np.vstack([rdp(P[:i+1], e)[:-1], rdp(P[i:], e)]) if dist[i] > e else np.vstack([a, b])
arrs = {}
for t in thetas:
    c, s = np.cos(np.radians(t)), np.sin(np.radians(t))
    sec = m2.section(plane_normal=[-s, c, 0], plane_origin=[0, 0, 0])
    if sec is None: continue
    for k, pl in enumerate([sec.vertices[e.points] for e in sec.entities]):
        rr = pl[:, 0]*c + pl[:, 1]*s
        keep = rr > 0.05
        # split into runs where rr>0
        idx = np.where(keep)[0]
        if len(idx) < 5: continue
        runs = np.split(idx, np.where(np.diff(idx) > 1)[0] + 1)
        for j, ru in enumerate(runs):
            if len(ru) < 5: continue
            P = np.c_[rr[ru], pl[ru, 2]]
            arrs[f"t{t:g}_{k}_{j}"] = P
            S = rdp(P, eps)
            print(f"t{t:g}_{k}_{j} n={len(P)}:", " ".join(f"({a:.2f},{b:.2f})" for a, b in S))
np.savez(f"{RUN}/measure/figures/meridian_{name}.npz", **arrs)
