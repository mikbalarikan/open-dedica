"""m06_refine.py - robust (binned-median) wall lines, step knees, barb-top inner edge, lug underside extent.
Writes measure/figures/m06_refine.json."""
import json, numpy as np, trimesh
out = {"tool": "measure/scripts/m06_refine.py"}
def binned(r, z, z0, z1, dz=0.25):
    zs, rs = [], []
    for b in np.arange(z0, z1, dz):
        k = (z >= b) & (z < b + dz)
        if k.sum() > 30: zs.append(b + dz/2); rs.append(np.median(r[k]))
    zs, rs = np.array(zs), np.array(rs)
    A = np.c_[np.ones(len(zs)), zs]; c, *_ = np.linalg.lstsq(A, rs, rcond=None)
    return {"c0": float(c[0]), "c1": float(c[1]), "bins": len(zs), "rms_of_medians": float(np.sqrt(((rs - A@c)**2).mean()))}
for nm in ('cupA', 'cupB'):
    d = np.load(f'measure/figures/m02_profile_{nm}.npz'); r, z = d['r'], d['z']
    o = {}
    k = (r > 11.3) & (r < 12.4); o['lower_wall'] = binned(r[k], z[k], 0.9, 6.6)
    k = (r > 10.4) & (r < 11.7); o['upper_wall'] = binned(r[k], z[k], 7.8, 10.7)
    lo, up = o['lower_wall'], o['upper_wall']
    prof = []
    for b in np.arange(6.3, 8.2, 0.05):
        kk = (z >= b) & (z < b + 0.05) & (r > 10.4) & (r < 12.3)
        if kk.sum() > 10: prof.append((b + 0.025, float(np.median(r[kk]))))
    prof = np.array(prof)
    rl = lo['c0'] + lo['c1'] * prof[:, 0]; ru = up['c0'] + up['c1'] * prof[:, 0]
    on_lo = prof[:, 1] >= rl - 0.04; on_up = prof[:, 1] <= ru + 0.04
    o['step_z_lo'] = float(prof[on_lo, 0].max() if on_lo.any() else np.nan)
    o['step_z_hi'] = float(prof[on_up & (prof[:, 0] > o['step_z_lo']), 0].min())
    k = z > 28.05; o['barb_top_inner_edge_r_p5'] = float(np.percentile(r[k & (r > 1.0)], 5)); o['barb_top_ring_r_p95'] = float(np.percentile(r[k], 95))
    out[nm] = o
m = trimesh.load('intake/aligned_work.stl'); C, N = m.triangles_center, m.face_normals
for s, nm in ((1, 'pos'), (-1, 'neg')):
    k = (s * C[:, 0] > 35) & (s * C[:, 0] < 41) & (np.abs(C[:, 1]) > 3.2) & (np.abs(C[:, 1]) < 4.5) & (np.abs(N[:, 1]) > 0.8) & (C[:, 2] > 10)
    zz = C[k, 2]
    out[f'lug_side_{nm}_z'] = {q: float(np.percentile(zz, q)) for q in (1, 2, 5, 10, 50)}
    out[f'lug_side_{nm}_z']['n'] = int(k.sum())
    k2 = (s * C[:, 0] > 39.5) & (np.abs(C[:, 1]) < 2.5) & (s * N[:, 0] > 0.7) & (C[:, 2] > 10)
    out[f'lug_end_{nm}_z'] = {q: float(np.percentile(C[k2, 2], q)) for q in (1, 5, 50)}; out[f'lug_end_{nm}_z']['n'] = int(k2.sum())
json.dump(out, open('measure/figures/m06_refine.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
