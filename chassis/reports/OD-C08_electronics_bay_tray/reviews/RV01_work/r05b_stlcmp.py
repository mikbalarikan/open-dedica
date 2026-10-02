"""Delivered STL vs a fresh 0.01/0.2 re-mesh: where they differ and by how much (surface distance both ways)."""
import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
import numpy as np, trimesh
from scipy.spatial import cKDTree
a = trimesh.load(STL, process=False); b = trimesh.load(W / "remesh_0.01_0.2.stl", process=False)
d, idx = cKDTree(b.triangles_center).query(a.triangles_center)
bad = []
for i, j in enumerate(idx):
    dd = min(max(np.linalg.norm(a.triangles[i] - np.roll(b.triangles[j], k, axis=0), axis=1)) for k in range(3))
    if dd > 1e-4: bad.append(i)
n = a.face_normals[bad]
axis_aligned = np.sum(np.isclose(np.abs(n).max(axis=1), 1.0, atol=1e-6))
print("unmatched delivered tris", len(bad), "of which on axis-aligned planes", axis_aligned)
print("their normals (unique)", np.unique(np.round(n, 3), axis=0)[:10])
pts_a = np.vstack([a.vertices, a.triangles_center]); pts_b = np.vstack([b.vertices, b.triangles_center])
da = trimesh.proximity.closest_point(b, pts_a)[1].max(); db = trimesh.proximity.closest_point(a, pts_b)[1].max()
print("surface distance delivered->fresh", da, "fresh->delivered", db)
print("areas", a.area, b.area, "volumes", a.volume, b.volume)
