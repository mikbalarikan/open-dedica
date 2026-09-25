"""QA-own probe of scan->CAD over-band clusters: scan-vertex normals, distance to the nearest scan
open-boundary vertex, and local scan-surface shape (registered datum frame)."""
import json, numpy as np, trimesh
from scipy.spatial import cKDTree
m = trimesh.load('input/scan.stl')
T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4'])
Tr = np.array(json.load(open('qa/registration.json'))['T_refine'])
m.apply_transform(T); m.apply_transform(np.linalg.inv(Tr))
a = np.load('qa/dev_arrays.npz'); sp, d = a['s2c_pts'], a['s2c_d']
# open boundary vertices
e = m.edges_sorted; u, c = np.unique(e, axis=0, return_counts=True); bv = np.unique(u[c == 1])
bt = cKDTree(m.vertices[bv]); vt = cKDTree(m.vertices)
_, vi = vt.query(sp); nrm = m.vertex_normals[vi]
out = {}
dev = json.load(open('qa/deviation.json'))
for i, cl in enumerate(dev['over_band_clusters']['scan_to_cad']['clusters']):
    lo, hi = np.array(cl['bbox_min']), np.array(cl['bbox_max'])
    s = (d > 0.8) & np.all(sp >= lo - 1e-6, 1) & np.all(sp <= hi + 1e-6, 1)
    P = sp[s]; r = np.hypot(P[:, 0], P[:, 1])
    rn = (nrm[s][:, 0] * P[:, 0] + nrm[s][:, 1] * P[:, 1]) / r
    db, _ = bt.query(P)
    # neighbourhood: scan points within 3 mm of the cluster centroid, band of r
    C = np.array(cl['centroid']); nb = np.linalg.norm(sp - C, axis=1) < 3.0
    out[i] = {'n': int(s.sum()), 'radial_normal_component_median': float(np.median(rn)),
              'nz_median': float(np.median(nrm[s][:, 2])),
              'dist_to_open_boundary_mm': {'p50': float(np.median(db)), 'max': float(db.max())},
              'frac_within_1mm_of_boundary': float((db < 1.0).mean()),
              'neighbourhood_3mm_r_range': [float(np.hypot(*sp[nb][:, :2].T).min()), float(np.hypot(*sp[nb][:, :2].T).max())],
              'neighbourhood_3mm_frac_over_band': float((d[nb] > 0.8).mean())}
json.dump(out, open('qa/cluster_probe.json', 'w'), indent=1); print(json.dumps(out, indent=1))
