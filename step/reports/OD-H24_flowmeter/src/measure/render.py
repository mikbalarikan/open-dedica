"""render.py mesh out.png [T.npy] - 6 shaded orthographic views (painter's algorithm)."""
import sys, numpy as np, trimesh, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
m = trimesh.load_mesh(sys.argv[1])
if len(sys.argv) > 3: m.apply_transform(np.load(sys.argv[3]))
if len(m.faces) > 150000:
    import fast_simplification
    v, f = fast_simplification.simplify(m.vertices.astype(np.float32), m.faces.astype(np.int32), 1 - 150000 / len(m.faces))
    m = trimesh.Trimesh(v, f)
c = m.bounds.mean(0)
views = {"+X": [1,0,0], "-X": [-1,0,0], "+Y": [0,1,0], "-Y": [0,-1,0], "+Z": [0,0,1], "-Z": [0,0,-1], "iso1": [1,1,1], "iso2": [-1,-1,1]}
fig, axs = plt.subplots(2, 4, figsize=(28, 14))
for ax, (name, d) in zip(axs.flat, views.items()):
    d = np.array(d, float); d /= np.linalg.norm(d)
    up = np.array([0, 0, 1.0]) if abs(d[2]) < 0.9 else np.array([0, 1.0, 0])
    x = np.cross(up, d); x /= np.linalg.norm(x); y = np.cross(d, x)
    V = m.vertices - c
    P = np.c_[V @ x, V @ y]; depth = V @ d
    fn = m.face_normals; vis = fn @ d > 0
    F = m.faces[vis]; sh = np.clip(fn[vis] @ (d * 0.8 + y * 0.4 + x * 0.2) / 1.0, 0.05, 1)
    order = np.argsort(depth[F].mean(1))
    pc = PolyCollection(P[F[order]], facecolors=plt.cm.gray(0.15 + 0.8 * sh[order]), edgecolors="none")
    ax.add_collection(pc); ax.autoscale(); ax.set_aspect("equal"); ax.set_title(name); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig(sys.argv[2], dpi=55)
