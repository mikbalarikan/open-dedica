"""QA run-local analysis (report-only, not a gate input to verdict.py):
 (a) re-runs observability.observable_split with the SAME parameters/seed as qa/deviation.json on the
     same QA tessellation and CAD samples, and composes it with the declared masks (M1, M2) -> stats of
     'observable AND NOT masked' CAD->scan (deviation_gate.py computes observability on unmasked d only);
 (b) lists every over-band point that remains after the declared masks, per direction, grouped
     (KD radius graph eps 1.0 mm, min 1 pt) with location, for miss explanations.
Inputs: qa/dev_arrays.npz, qa/masks.json, qa/registration.json, scan + alignment, STEP (QA tessellation)."""
import sys, json, tempfile, functools
from pathlib import Path
import numpy as np, trimesh
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts')
from _common import load_mesh, load_matrix, read_json, select, stats, step_to_mesh, header, write_json, band_result
from deviation_gate import dist_to_mesh, boundary_vertices
from observability import observable_split
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
RUN = Path(sys.argv[1]); qa = RUN / 'qa'
z = np.load(qa / 'dev_arrays.npz')
sp, d1, cp, cfi, d2 = z['s2c_pts'], z['s2c_d'], z['c2s_pts'], z['c2s_fid'], z['c2s_d']
masks = read_json(qa / 'masks.json')['masks']; M1 = masks[0]['select']; M2r = masks[1]['radius_mm']
reg = read_json(qa / 'registration.json')
scan = load_mesh(RUN / 'input/scan.stl'); scan.apply_transform(load_matrix(RUN / 'intake/alignment.json'))
scan.apply_transform(np.linalg.inv(np.asarray(reg['T_refine'])))
cad = step_to_mesh(RUN / 'build/OD-H21_antidrip-valve_datum.step', Path(tempfile.mkdtemp()) / 'cad.stl')
# sanity: same tessellation => same CAD samples
cp2, cfi2 = trimesh.sample.sample_surface(cad, 300000, seed=2)
same = bool(np.allclose(cp2, cp) and (cfi2 == cfi).all())
btree = cKDTree(boundary_vertices(scan))
def m2(P):  # open-boundary mask on CAD points: nearest scan point within r of a scan hole edge
    _, f = dist_to_mesh(P, scan, 8, 3_000_000, 0, False)
    near = trimesh.triangles.closest_point(scan.triangles[f], P)
    return btree.query(near)[0] <= M2r
cn = cad.face_normals[cfi]
in1_s = select(M1, sp, None)
in1_c = select(M1, cp, cn)
ob = observable_split(cad, cp, cfi, d2, 20000, 5, 0.5, 60.0, 6, 0.05, None, chunk=64)
sub, obs = ob['_sub'], ob['_obs_mask']
in2_sub = m2(cp[sub])
keep = obs & ~in1_c[sub] & ~in2_sub
res = {'same_cad_samples_as_deviation_json': same,
       'observable_unmasked': ob['observable'], 'unobservable_fraction': ob['unobservable_fraction'],
       'observable_and_not_masked': stats(d2[sub][keep]),
       'observable_but_in_M1': stats(d2[sub][obs & in1_c[sub]]),
       'observable_but_in_M1_fraction_of_subsample': float((obs & in1_c[sub]).mean()),
       'observable_and_not_masked_band': band_result(stats(d2[sub][keep]), 0.30, 0.80),
       'params': ob['params'] | {'masks_composed': ['M1 unscanned bore interiors', 'M2 open boundary (0.8 mm)']}}
def groups(P, d, thr):
    sel = np.where(d > thr)[0]
    if len(sel) == 0: return []
    Q = P[sel]; pr = cKDTree(Q).query_pairs(1.0, output_type='ndarray')
    g = coo_matrix((np.ones(len(pr)), (pr[:, 0], pr[:, 1])), shape=(len(Q), len(Q)))
    _, lab = connected_components(g, directed=False); out = []
    for l in np.unique(lab):
        m = lab == l; C = Q[m]; dd = d[sel][m]
        out.append({'n': int(m.sum()), 'centroid': C.mean(0).round(2).tolist(), 'bbox_min': C.min(0).round(2).tolist(),
                    'bbox_max': C.max(0).round(2).tolist(), 'r': [round(float(np.hypot(*C[:, :2].T).min()), 2), round(float(np.hypot(*C[:, :2].T).max()), 2)],
                    'theta_deg': round(float((np.degrees(np.arctan2(C[:, 1].mean(), C[:, 0].mean())) + 360) % 360), 1),
                    'd_max': round(float(dd.max()), 3)})
    return sorted(out, key=lambda o: -o['d_max'])
over_c = np.where(d2 > 0.8)[0]
in2_c = np.zeros(len(cp), bool); in2_c[over_c] = m2(cp[over_c])
res['residual_over_band_after_masks'] = {
    'scan_to_cad': groups(sp[~in1_s], d1[~in1_s], 0.8),
    'cad_to_scan': groups(cp[~in1_c & ~in2_c], d2[~in1_c & ~in2_c], 0.8)}
res['residual_over_band_unmasked'] = {'scan_to_cad': groups(sp, d1, 0.8)}
write_json(qa / 'residual_analysis.json', {**header('residual_analysis', 'qa/src/residual_analysis.py',
           [str(qa / 'dev_arrays.npz'), str(qa / 'masks.json'), str(qa / 'registration.json')], 5), **res})
print(json.dumps({k: v for k, v in res.items() if k != 'params'}, indent=0, default=float)[:6000])
