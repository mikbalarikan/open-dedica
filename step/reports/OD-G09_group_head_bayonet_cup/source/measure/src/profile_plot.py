"""Run-local: overlay r-z points of the full-res scan (datum frame) over theta windows.
Usage: profile_plot.py out.png th0,th1[;th0,th1...] [rlo,rhi,zlo,zhi]"""
import sys, json, numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4'])
V = m.vertices @ T[:3, :3].T + T[:3, 3]
r = np.hypot(V[:, 0], V[:, 1]); th = np.degrees(np.arctan2(V[:, 1], V[:, 0])) % 360
wins = [tuple(map(float, w.split(','))) for w in sys.argv[2].split(';')]
lim = list(map(float, sys.argv[3].split(','))) if len(sys.argv) > 3 else [20, 42, -29, 4]
fig, axs = plt.subplots(1, len(wins), figsize=(7 * len(wins), 7), squeeze=False)
for ax, (a, b) in zip(axs[0], wins):
    s = ((th - a) % 360 < (b - a) % 360) & (r > lim[0]) & (r < lim[1]) & (V[:, 2] > lim[2]) & (V[:, 2] < lim[3])
    ax.scatter(r[s], V[s, 2], s=0.2, c=th[s], cmap='viridis'); ax.set_aspect('equal'); ax.grid(True, lw=.3)
    ax.set_title(f'theta {a}-{b} n={s.sum()}'); ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3])
    ax.minorticks_on(); ax.grid(True, which='minor', lw=.15)
fig.tight_layout(); fig.savefig(sys.argv[1], dpi=70)
