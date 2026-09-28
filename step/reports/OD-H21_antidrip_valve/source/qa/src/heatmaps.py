"""QA run-local deviation heatmaps (post-ICP, from qa/dev_arrays.npz written by deviation_gate.py).
Sequential single-hue ramp 0..0.8 mm (regime max band); points over the band drawn on top in red with
a label. Three orthographic views per direction, each view split into the near/far half so both
sides of the part are visible. Writes qa/overlays/heatmap_scan_to_cad.png and heatmap_cad_to_scan.png."""
import sys
from pathlib import Path
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
RUN = Path(sys.argv[1]); z = np.load(RUN / 'qa/dev_arrays.npz')
cmap = LinearSegmentedColormap.from_list('seq', ['#dbe7f5', '#08306b'])
views = [('front (x-z), y<0 half', 0, 2, 1, -1), ('back (x-z), y>0 half', 0, 2, 1, 1),
         ('side (y-z), x<0 half', 1, 2, 0, -1), ('side (y-z), x>0 half', 1, 2, 0, 1),
         ('bottom (x-y), z<0 half', 0, 1, 2, -1), ('top (x-y), z>0 half', 0, 1, 2, 1)]
for key, name in (('s2c', 'scan_to_cad'), ('c2s', 'cad_to_scan')):
    P, d = z[f'{key}_pts'], z[f'{key}_d']
    fig, axes = plt.subplots(2, 3, figsize=(21, 15), dpi=90); axes = axes.T.ravel()
    for ax, (t, i, j, k, s) in zip(axes, views):
        m = (P[:, k] * s) >= 0
        Q, dd = P[m], d[m]; o = np.argsort(dd); Q, dd = Q[o], dd[o]
        inb = dd <= 0.8
        sc = ax.scatter(Q[inb, i], Q[inb, j], c=dd[inb], s=0.6, cmap=cmap, vmin=0, vmax=0.8, linewidths=0)
        ax.scatter(Q[~inb, i], Q[~inb, j], c='#d62728', s=9, linewidths=0, label=f'> 0.8 mm (over max band): {int((~inb).sum())} pts')
        ax.set_aspect('equal'); ax.set_title(t, fontsize=11); ax.set_xlabel('xyz'[i]); ax.set_ylabel('xyz'[j]); ax.grid(True, lw=0.3, color='#dddddd')
        ax.legend(loc='lower right', fontsize=9, frameon=False)
    cb = fig.colorbar(sc, ax=axes.tolist(), shrink=0.6, pad=0.02); cb.set_label(f'{name} distance, mm (0 .. 0.8 = regime max band)')
    fig.suptitle(f'{ {"scan_to_cad": "scan→CAD", "cad_to_scan": "CAD→scan"}[name] } deviation, post-ICP datum frame, n={len(d)}  (p95 {np.percentile(d, 95):.3f}, max {d.max():.3f} mm; unmasked)', fontsize=14)
    fig.savefig(RUN / f'qa/overlays/heatmap_{name}.png'); plt.close(fig)
    print(name, 'over band', int((d > 0.8).sum()))
