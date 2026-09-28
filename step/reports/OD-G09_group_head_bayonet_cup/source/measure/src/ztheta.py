"""Run-local: z(theta) of up-facing faces in several r bands (full-res, datum frame) -> PNG."""
import json, sys, numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); m.apply_transform(T)
c = m.triangles_center; n = m.face_normals
r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360
bands = [(25, 28, -21, -19), (28.5, 30.5, -21, -19), (31.8, 33.6, -18, -12.5), (34.6, 36.6, -16, -12.5), (31.8, 34.0, -1, 1), (34.8, 36.8, -3.6, 1), (37.4, 38.2, 2.8, 3.6), (38.8, 39.6, 2, 2.8)]
fig, axs = plt.subplots(len(bands), 1, figsize=(22, 3 * len(bands)))
for ax, (r0, r1, z0, z1) in zip(axs, bands):
    s = (n[:, 2] > 0.8) & (r > r0) & (r < r1) & (c[:, 2] > z0) & (c[:, 2] < z1)
    ax.scatter(th[s], c[s, 2], s=0.2, c='k'); ax.set_title(f'r {r0}-{r1}'); ax.set_xticks(range(0, 361, 10)); ax.grid(True, lw=.3); ax.set_xlim(0, 360)
fig.tight_layout(); fig.savefig('measure/figures/ztheta.png', dpi=50)
