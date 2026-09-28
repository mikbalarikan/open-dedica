"""Top-view height map of the cup interior: max z per 0.2 mm cell over x,y in [-25,25], z in [-60,-20],
from 2.5M seeded (seed 0) surface samples of intake/aligned_work.stl. Writes floor_heightmap_max_z.npy."""
import numpy as np, trimesh
m = trimesh.load('intake/aligned_work.stl'); P, _ = trimesh.sample.sample_surface(m, 2500000, seed=0)
x0, x1 = -25, 25; s = (P[:, 0] > x0) & (P[:, 0] < x1) & (P[:, 1] > x0) & (P[:, 1] < x1) & (P[:, 2] < -20) & (P[:, 2] > -60); P = P[s]
res = 0.2; nx = int((x1 - x0) / res); ix = ((P[:, 0] - x0) / res).astype(int); iy = ((P[:, 1] - x0) / res).astype(int)
H = np.full(nx * nx, -np.inf); np.maximum.at(H, iy * nx + ix, P[:, 2]); H = H.reshape(nx, nx); H[~np.isfinite(H)] = np.nan
np.save('measure/figures/floor_heightmap_max_z.npy', H); print(H.shape, np.nanmin(H), np.nanmax(H))
