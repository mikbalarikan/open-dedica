"""QA-own diagnostic (NOT the gate): where does CAD->scan exceed 0.8 mm once CAD points whose
nearest scan point lies within 0.8 mm of a scan open boundary are set aside (the M1 rule, recomputed)?
Also a coverage-based observability proxy for the known ray-test defect (OD-H22 defect #3)."""
import json, numpy as np, trimesh
from scipy.spatial import cKDTree
m = trimesh.load('input/scan.stl')
T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); Tr = np.array(json.load(open('qa/registration.json'))['T_refine'])
m.apply_transform(T); m.apply_transform(np.linalg.inv(Tr))
a = np.load('qa/dev_arrays.npz'); cp, d = a['c2s_pts'], a['c2s_d']
e = m.edges_sorted; u, c = np.unique(e, axis=0, return_counts=True); bv = np.unique(u[c == 1])
_, ni = cKDTree(m.vertices).query(cp); db, _ = cKDTree(m.vertices[bv]).query(m.vertices[ni])
gap = db < 0.8
r = np.hypot(cp[:, 0], cp[:, 1]); z = cp[:, 2]
def st(x): return {'n': int(len(x)), 'p95': float(np.percentile(x, 95)), 'max': float(x.max())} if len(x) else {'n': 0}
out = {'rule': 'coverage proxy: CAD point is a coverage gap when its nearest scan vertex is within 0.8 mm of a scan open-boundary vertex',
       'all': st(d), 'not_gap': st(d[~gap]), 'gap_fraction': float(gap.mean())}
o = (~gap) & (d > 0.8)
out['residual_over_0p8_not_gap'] = {'n': int(o.sum())}
if o.any():
    zones = {'crevice z14.9-17.2 r5.4-10.7': (z > 14.9) & (z < 17.2) & (r > 5.4) & (r < 10.7),
             'pocket floor': (z > 8) & (z < 12.6) & (r > 13.4) & (r < 22.1) & (abs(cp[:, 1]) < 2.6),
             'bore deep z<35.5 r<4.3': (z < 35.5) & (r < 4.3)}
    for k, s in zones.items(): out['residual_over_0p8_not_gap'][k] = int((o & s).sum())
    out['residual_over_0p8_not_gap']['z_range'] = [float(z[o].min()), float(z[o].max())]
    out['residual_over_0p8_not_gap']['r_range'] = [float(r[o].min()), float(r[o].max())]
json.dump(out, open('qa/c2s_residual_probe.json', 'w'), indent=1); print(json.dumps(out, indent=1))
