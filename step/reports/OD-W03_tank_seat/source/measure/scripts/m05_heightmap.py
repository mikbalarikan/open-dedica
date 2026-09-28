"""m05_heightmap.py - top-down max-z height map and normal-shaded image of the aligned scan (CHK-CLUSTER/ENUM look).
Writes measure/figures/m05_heightmap.png."""
import numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
m = trimesh.load('intake/aligned_work.stl')
pts, fi = trimesh.sample.sample_surface(m, 1500000, seed=0)
res = 0.1
ix = ((pts[:, 0] + 44) / res).astype(int); iy = ((pts[:, 1] + 17) / res).astype(int)
H = np.full((int(34/res)+1, int(88/res)+1), np.nan); S = np.full_like(H, np.nan)
order = np.argsort(pts[:, 2])
H[iy[order], ix[order]] = pts[order, 2]
nz = m.face_normals[fi]; shade = nz @ np.array([-0.4, 0.5, 0.77])
S[iy[order], ix[order]] = shade[order]
fig, ax = plt.subplots(2, 1, figsize=(20, 16))
im = ax[0].imshow(H, origin='lower', extent=(-44, 44, -17, 17), cmap='viridis'); plt.colorbar(im, ax=ax[0]); ax[0].set_title('max z')
ax[1].imshow(S, origin='lower', extent=(-44, 44, -17, 17), cmap='gray'); ax[1].set_title('shaded (top view)')
for a in ax: a.grid(True, lw=0.3)
plt.tight_layout(); plt.savefig('measure/figures/m05_heightmap.png', dpi=60)
