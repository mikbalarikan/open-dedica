"""QA run-local zoomed radial sections at every over-band cluster (post-ICP frame), using overlay.py's
rsec(). Scan black, CAD red. Writes qa/overlays/zoom_it2_extra.png (no JSON: panel scan counts are printed)."""
import sys, tempfile
from pathlib import Path
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts')
from _common import load_mesh, load_matrix, read_json, step_to_mesh
from overlay import rsec, length
RUN = Path(sys.argv[1])
scan = load_mesh(RUN / 'input/scan.stl'); scan.apply_transform(load_matrix(RUN / 'intake/alignment.json'))
scan.apply_transform(np.linalg.inv(np.asarray(read_json(RUN / 'qa/registration.json')['T_refine'])))
cad = step_to_mesh(RUN / 'build/OD-H21_antidrip-valve_datum.step', Path(tempfile.mkdtemp()) / 'c.stl')
P = [('latch edge θ=83', 83, (2, 8), (-27.8, -22)), ('bore far wall θ=300', 300, (2, 8), (-27.8, -22)),
     ('bore far wall θ=315', 315, (2, 8), (-27.8, -22)), ('nozzle bore θ=0', 0, (0, 8), (-27.8, -21)),
     ('ring window θ=110', 110, (9, 14.5), (9, 17)), ('ring window θ=121', 121, (9, 14.5), (9, 17)),
     ('ring window θ=285', 285, (9, 14.5), (9, 17)), ('ring window θ=290', 290, (9, 14.5), (9, 17)),
     ('ring window θ=116', 116, (9, 13.5), (8.5, 12.5)), ('skirt slit θ=158', 158, (9, 13.5), (8.5, 12.5)),
     ('skirt slit θ=217', 217, (9, 13.5), (8.5, 12.5)), ('skirt slit θ=229.5', 229.5, (9, 13.5), (8.5, 12.5)),
     ('outlet end θ=0', 0, (25, 31), (-0.5, 7.5)), ('barb end θ=55.7', 55.7, (22, 29), (20, 29))]
fig, axes = plt.subplots(4, 4, figsize=(20, 20), dpi=90); axes = axes.ravel()
for ax, (t, th, xr, zr) in zip(axes, P):
    S, C = rsec(scan, th), rsec(cad, th)
    ax.add_collection(LineCollection(S, colors='k', linewidths=1.0)); ax.add_collection(LineCollection(C, colors='r', linewidths=1.0))
    ax.set_xlim(*xr); ax.set_ylim(*zr); ax.set_aspect('equal'); ax.grid(True, lw=0.3); ax.set_title(t + ' — scan black / CAD red'); ax.set_xlabel('r'); ax.set_ylabel('z')
    print(t, 'scan segs', len(S), 'cad segs', len(C))
for ax in axes[len(P):]: ax.axis('off')
fig.tight_layout(); fig.savefig(RUN / 'qa/overlays/zoom_it2_extra.png')
