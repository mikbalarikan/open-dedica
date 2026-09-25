import trimesh, numpy as np, sys
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
def splat(m, R, ax, title, res=0.25):
    # sample surface points with normals, rotate, z-buffer, shade by normal.z (lambert)
    pts, fi = trimesh.sample.sample_surface_even(m, 1_500_000, seed=1) if False else trimesh.sample.sample_surface(m, 1_500_000, seed=1)
    n = m.face_normals[fi]
    p = pts @ R.T; nn = n @ R.T
    x, y, z = p[:,0], p[:,1], p[:,2]
    ix = ((x - x.min())/res).astype(int); iy = ((y - y.min())/res).astype(int)
    W, H = ix.max()+1, iy.max()+1
    zb = np.full((H, W), -np.inf); sh = np.full((H, W), np.nan)
    order = np.argsort(z)
    zb[iy[order], ix[order]] = z[order]
    sh[iy[order], ix[order]] = np.clip(nn[order] @ np.array([0.3,0.3,0.9]), 0.05, 1)
    ax.imshow(sh, origin="lower", cmap="gray", vmin=0, vmax=1, extent=[x.min(), x.max(), y.min(), y.max()])
    ax.set_title(title); ax.grid(alpha=.3)
m = trimesh.load_mesh(sys.argv[1]); out = sys.argv[2]
T = np.load(sys.argv[3]) if len(sys.argv) > 3 else np.eye(4)
m.apply_transform(T)
views = {"top(+Z)": np.eye(3), "bottom(-Z)": np.diag([1,-1,-1]),
 "front(-Y)": np.array([[1,0,0],[0,0,1],[0,-1,0]]), "back(+Y)": np.array([[-1,0,0],[0,0,1],[0,1,0]]),
 "right(+X)": np.array([[0,1,0],[0,0,1],[1,0,0]]), "left(-X)": np.array([[0,-1,0],[0,0,1],[-1,0,0]])}
fig, axs = plt.subplots(2, 3, figsize=(21, 14))
for ax, (k, R) in zip(axs.flat, views.items()): splat(m, R, ax, k)
plt.tight_layout(); plt.savefig(out, dpi=80)
