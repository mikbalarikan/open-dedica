"""V-rib cross-section (it1 self-check follow-up): in each rib's frame (s along the m08 PCA line, u
perpendicular, +u toward the wedge containing the U rib), the visible flank offset u vs z (median of
flank samples |n.u| > 0.8 per 1 mm z bin), and the top crest offset (z within 0.25 of the crest).
Only the inner (wedge-side) flank is visible on most of the length; the outer flank is used where seen."""
import json, numpy as np, trimesh
rf = json.load(open('measure/figures/ribs_floor.json'))
m = trimesh.load('intake/aligned_work.stl'); P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0); N = m.face_normals[fi]
out = {}
for key in ("V_pos", "V_neg"):
    V = rf[key]; c = np.array(V["centre"]); d = np.array(V["dir"]); nrm = np.array([-d[1], d[0]])
    if nrm @ (np.array([0.0, 0.0]) - c) < 0: nrm = -nrm      # +u points toward the cup centre / the U
    q = P[:, :2] - c; s = q @ d; u = q @ nrm; nu = N[:, :2] @ nrm
    band = (s > V["t_min"] + 2) & (s < V["t_max"] - 2) & (np.abs(u) < 3.0)
    top = band & (P[:, 2] > V["top_z"] - 0.25)
    res = {"crest_u_median": float(np.median(u[top])), "bins": []}
    for z0 in np.arange(-38.0, -29.0, 1.0):
        zb = band & (P[:, 2] >= z0) & (P[:, 2] < z0 + 1)
        fin = zb & (nu > 0.8) & (u > -1.5); fout = zb & (nu < -0.8) & (u < 1.5)
        res["bins"].append({"z": float(z0 + 0.5), "inner_flank_u": float(np.median(u[fin])) if fin.sum() > 20 else None, "n_in": int(fin.sum()),
                            "outer_flank_u": float(np.median(u[fout])) if fout.sum() > 20 else None, "n_out": int(fout.sum())})
    out[key] = res
json.dump(out, open('measure/figures/vrib_flanks.json', 'w'), indent=1)
for k, v in out.items():
    print(k, 'crest', round(v['crest_u_median'], 3))
    for b in v['bins']: print('  ', b)
