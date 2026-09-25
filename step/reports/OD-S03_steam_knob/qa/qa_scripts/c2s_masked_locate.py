"""QA-own diagnostic: locate the largest CAD->scan distances that survive the M1 open-boundary rule (0.8 mm,
recomputed as in c2s_residual_probe.py) and the M2 normal rule (70 deg, recomputed), for it1 and it2."""
import json, numpy as np, trimesh, sys
from scipy.spatial import cKDTree
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts')
from _common import step_to_mesh
out = {}
for it, q, step in (('it1', '_it1_SUPERSEDED/qa/', '_it1_SUPERSEDED/build/OD-S03_steam-knob_datum.step'), ('it2', 'qa/', 'build/OD-S03_steam-knob_datum.step')):
    m = trimesh.load('input/scan.stl')
    T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); Tr = np.array(json.load(open(q + 'registration.json'))['T_refine'])
    m.apply_transform(T); m.apply_transform(np.linalg.inv(Tr))
    a = np.load(q + 'dev_arrays.npz'); cp, d, fid = a['c2s_pts'], a['c2s_d'], a['c2s_fid']
    cad = step_to_mesh(step, '/tmp/claude-0/-home-user-agentic-STL-to-CAD/9155e2f4-24ea-56fd-9dd7-9d1972aab7f3/scratchpad/_c.stl')
    cn = cad.face_normals[fid]
    e = m.edges_sorted; u, c = np.unique(e, axis=0, return_counts=True); bv = np.unique(u[c == 1])
    _, ni = cKDTree(m.vertices).query(cp); db, _ = cKDTree(m.vertices[bv]).query(m.vertices[ni])
    keep = (db >= 0.8) & ((m.vertex_normals[ni] * cn).sum(1) >= np.cos(np.radians(70)))
    z = cp[:, 2]; r = np.hypot(cp[:, 0], cp[:, 1]); th = np.degrees(np.arctan2(cp[:, 1], cp[:, 0])) % 360
    idx = np.argsort(-np.where(keep, d, -1))[:12]
    out[it] = {'kept_n': int(keep.sum()), 'kept_max': float(d[keep].max()),
               'top': [{'d': round(float(d[i]), 3), 'z': round(float(z[i]), 2), 'r': round(float(r[i]), 2), 'theta': round(float(th[i]), 1)} for i in idx]}
    print(it, out[it]['kept_n'], out[it]['kept_max']); [print('  ', t) for t in out[it]['top']]
json.dump(out, open('qa/c2s_masked_locate.json', 'w'), indent=1)
