"""m01_flange.py - flange outline, skirt and top-edge measurements on the aligned scan (datum frame).
Writes measure/figures/m01_flange.json + m01_flange.png. Deterministic (no sampling)."""
import json, sys, numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts')
from datum_fit import fit_circle, fit_circle_irls
m = trimesh.load('intake/aligned_work.stl')
out = {"tool": "measure/scripts/m01_flange.py", "mesh": "intake/aligned_work.stl"}
# skirt outline from sections at z = -0.5, -1.0, -1.5 (below the flange top, above the scan edge)
P = []
for z in (-0.5, -1.0, -1.5):
    s = m.section([0, 0, 1], [0, 0, z])
    for e in s.entities:
        p = s.vertices[e.points]; P.append(p)
P = np.vstack(P)
x, y = P[:, 0], P[:, 1]
side_top = (np.abs(x) < 15) & (y > 10); side_bot = (np.abs(x) < 15) & (y < -10)
out["skirt_y_top"] = {"p50": float(np.median(y[side_top])), "n": int(side_top.sum()), "std": float(y[side_top].std())}
out["skirt_y_bot"] = {"p50": float(np.median(y[side_bot])), "n": int(side_bot.sum()), "std": float(y[side_bot].std())}
ends = {}
for sgn, nm in ((-1, 'neg'), (1, 'pos')):
    arc = (sgn * x > 22) & (np.abs(y) > 5.8)
    c = fit_circle_irls(P[arc, :2], np.ones(arc.sum()), scale=0.3)
    flat = (sgn * x > 33) & (np.abs(y) < 3.5)
    ends[nm] = {"arc_fit": c, "end_flat_x_p50": float(np.median(x[flat])), "end_flat_n": int(flat.sum()),
                "end_flat_x_std": float(x[flat].std())}
out["ends"] = ends
# skirt lower edge: z of skirt wall vertices (outer wall faces, near-horizontal normals, r from centre line)
V = m.vertices; N = m.vertex_normals
sk = (V[:, 2] < -0.3) & (np.abs(N[:, 2]) < 0.4)
out["skirt_wall_z"] = {q: float(np.percentile(V[sk, 2], q)) for q in (1, 5, 10, 50)}
out["skirt_wall_z"]["n"] = int(sk.sum())
# flange top z (primary) re-read
top = (V[:, 2] > -0.3) & (V[:, 2] < 0.3) & (N[:, 2] > 0.9)
out["flange_top_z_p50"] = float(np.median(V[top, 2]))
# top edge round: profile of the long edge at |x|<15, y>0: points in y-z
fig, ax = plt.subplots(1, 3, figsize=(18, 6))
ax[0].plot(x, y, ',k'); ax[0].set_aspect('equal'); ax[0].set_title('skirt outline z=-0.5..-1.5')
for sgn, nm in ((-1, 'neg'), (1, 'pos')):
    c = ends[nm]["arc_fit"]; t = np.linspace(0, 2*np.pi, 200)
    ax[0].plot(c['cx'] + c['r']*np.cos(t), c['cy'] + c['r']*np.sin(t), 'r-', lw=0.5)
e = (np.abs(V[:, 0]) < 15) & (V[:, 1] > 12)
ax[1].plot(V[e, 1], V[e, 2], ',k'); ax[1].set_aspect('equal'); ax[1].set_title('+y edge profile |x|<15'); ax[1].grid(True, which='both', lw=0.3); ax[1].minorticks_on()
e2 = (np.abs(V[:, 0]) < 15) & (V[:, 1] < -12)
ax[2].plot(V[e2, 1], V[e2, 2], ',k'); ax[2].set_aspect('equal'); ax[2].set_title('-y edge profile |x|<15'); ax[2].grid(True, which='both', lw=0.3); ax[2].minorticks_on()
plt.tight_layout(); plt.savefig('measure/figures/m01_flange.png', dpi=80)
json.dump(out, open('measure/figures/m01_flange.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
