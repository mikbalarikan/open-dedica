"""Section overlays: scan (black) vs CAD (red) on datum planes, framed per cad-section (no clipping).

IN : argv[1] aligned scan mesh (datum frame), argv[2] CAD datum STL, argv[3] out PNG
"""

import sys

import matplotlib
import numpy as np
import trimesh

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

scan = trimesh.load_mesh(sys.argv[1])
cad = trimesh.load_mesh(sys.argv[2])
PLANES = [  # (title, normal, origin, u-axis, v-axis)
    ("XZ @ y=0 (through axis, connector +X)", [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 1]),
    ("YZ @ x=0 (through axis)", [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 1]),
    ("YZ @ x=-10.45 (lower tube axis)", [1, 0, 0], [-10.45, 0, 0], [0, 1, 0], [0, 0, 1]),
    ("Z = 1.0 (rim, spokes, hub)", [0, 0, 1], [0, 0, 1.0], [1, 0, 0], [0, 1, 0]),
    ("Z = 18.5 (windows, slots)", [0, 0, 1], [0, 0, 18.5], [1, 0, 0], [0, 1, 0]),
    ("Z = 23.0 (connector boss)", [0, 0, 1], [0, 0, 23.0], [1, 0, 0], [0, 1, 0]),
]
fig, axs = plt.subplots(2, 3, figsize=(33, 22))
for ax, (title, n, o, u, v) in zip(axs.flat, PLANES):
    u, v = np.array(u, float), np.array(v, float)
    allp = []
    for mesh, col, lw, lab in ((scan, "k", 0.8, "scan"), (cad, "r", 1.1, "CAD")):
        segs = trimesh.intersections.mesh_plane(mesh, n, o)
        for i, s in enumerate(segs):
            ax.plot(s @ u, s @ v, "-", color=col, lw=lw, label=lab if i == 0 else None)
        if len(segs):
            allp.append(segs.reshape(-1, 3))
    P = np.vstack(allp)
    xs, ys = P @ u, P @ v
    mx = max((xs.max() - xs.min()) * 0.08, 5.0)
    my = max((ys.max() - ys.min()) * 0.08, 5.0)
    ax.set_xlim(xs.min() - mx, xs.max() + mx)
    ax.set_ylim(ys.min() - my, ys.max() + my)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.35)
    ax.set_title(title, fontsize=18)
    ax.legend(loc="upper right", framealpha=0.9, fontsize=14)
fig.savefig(sys.argv[3], dpi=55, bbox_inches="tight", pad_inches=0.3)
