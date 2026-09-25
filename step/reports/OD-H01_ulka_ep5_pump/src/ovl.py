import trimesh, numpy as np, sys
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
scan = trimesh.load_mesh("pump.stl"); scan.apply_transform(np.load("T1.npy"))
cad = trimesh.load_mesh(sys.argv[1]); out = sys.argv[2]
specs = [s.split(":") for s in sys.argv[3].split(";")]  # axis:value:xmin,xmax,ymin,ymax
nc = 3; nr = int(np.ceil(len(specs)/nc))
fig, axs = plt.subplots(nr, nc, figsize=(10*nc, 9*nr))
for ax, (a, v, lim) in zip(np.atleast_1d(axs).flat, specs):
    a = "xyz".index(a); v = float(v); lim = [float(t) for t in lim.split(",")]
    n = np.zeros(3); n[a] = 1; o = np.zeros(3); o[a] = v; oth = [i for i in range(3) if i != a]
    for mesh, col, lw in ((scan, "#1f4fd1", 1.0), (cad, "#e8141c", 1.3)):
        seg = trimesh.intersections.mesh_plane(mesh, n, o)
        ax.add_collection(LineCollection(seg[:, :, oth], colors=col, linewidths=lw))
    ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3]); ax.set_aspect("equal")
    ax.minorticks_on(); ax.grid(alpha=.4); ax.grid(which="minor", alpha=.15)
    ax.set_title(f"{'xyz'[a]}={v}  blue=scan red=CAD  (h={'xyz'[oth[0]]}, v={'xyz'[oth[1]]})")
plt.tight_layout(); plt.savefig(out, dpi=65)
