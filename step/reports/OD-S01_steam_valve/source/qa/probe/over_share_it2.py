"""QA-only probe (it2, NOT a gate): how far is the gated scan->CAD p95 from 0.30 and could another
loop plausibly close it? (1) fraction of scan points over 0.30 / 0.80 (p95<=0.30 needs <=5 % over 0.30);
(2) share per z bucket and per it1 named region (same boxes as _it1_SUPERSEDED/qa/probe/over_share.py);
(3) hypothetical p95/max if every over-band (>0.8) cluster neighbourhood (cluster bbox grown by 1.5 mm)
were perfect -> sizes the 'diffuse' 0.3..0.8 population that no cluster fix touches.
Inputs: qa/dev_arrays.npz (post-ICP gate frame)."""
import json, sys
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial import cKDTree
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import select
z = np.load("qa/dev_arrays.npz"); P, d = z["s2c_pts"], z["s2c_d"]
n = len(d); over = d > 0.30
res = {"n": n, "frac_over_0.3": round(float(over.mean()), 4), "frac_over_0.8": round(float((d > 0.8).mean()), 4),
       "p95": round(float(np.percentile(d, 95)), 4),
       "points_over_0.3_to_remove_for_p95_0.30": int(over.sum() - np.floor(0.05 * n))}
buckets = {"z<0": {"z": [None, -0.25]}, "0-8.2": {"z": [-0.25, 8.2]}, "8.2-15.4": {"z": [8.2, 15.4]},
           "15.4-27.7": {"z": [15.4, 27.7]}, "27.7-43.4": {"z": [27.7, 43.4]}, ">43.4": {"z": [43.4, None]}}
res["buckets"] = {}
for k, pr in buckets.items():
    m = select(pr, P)
    res["buckets"][k] = {"n": int(m.sum()), "frac_over_0.3": round(float(over[m].mean()), 4),
                         "share_of_all_over_0.3": round(float((m & over).sum() / over.sum()), 4),
                         "n_over_0.8": int((m & (d > 0.8)).sum())}
it1_regions = {
 "R1 upper port +X end wall / U-window": {"x": [-1.8, 0.3], "y": [4.5, 14], "z": [22, 37]},
 "R2 lower port +X end wall / U-window": {"x": [-1.8, 0.3], "y": [-14, -4.5], "z": [8, 25]},
 "R3 shoulder block 120 slope": {"x": [-11, -3.5], "y": [4.5, 12], "z": [3, 15]},
 "R4 barb top rib": {"x": [-0.6, 0.6], "y": [-9, -4.5], "z": [33.5, 38]},
 "R5 switch side tab / bar 330": {"x": [5, 13], "y": [-7, -5.3], "z": [10.5, 12.5]},
 "R6 switch underside bump": {"x": [10, 14.5], "y": [1, 5], "z": [14, 15.9]},
 "R7 cam pockets th 96/270": {"r": [9, 11.5], "z": [2.2, 8.2], "any_of": [{"theta_deg": [88, 102]}, {"theta_deg": [262, 276]}]},
 "R8 holder/bracket junction th 45..95": {"r": [8, 11], "z": [16, 23], "theta_deg": [45, 95]},
 "R9 top bore floor": {"r": [0, 5], "z": [42, 44]},
 "R10 spindle teeth": {"z": [None, -0.25]},
 "N1 (it2) upper port junction box by the neck": {"x": [-3.6, -0.6], "y": [4.3, 8.1], "z": [26.8, 32.8]},
}
res["it1_regions_same_boxes"] = {}
for k, pr in it1_regions.items():
    m = select(pr, P)
    res["it1_regions_same_boxes"][k] = {"n": int(m.sum()), "n_over_0.3": int((m & over).sum()),
                                        "n_over_0.8": int((m & (d > 0.8)).sum()),
                                        "max": round(float(d[m].max()), 3) if m.any() else None}
# cluster neighbourhoods, same clustering as deviation_gate (eps 1.0, >=20 pts)
sel = np.where(d > 0.8)[0]; Q = P[sel]
pairs = cKDTree(Q).query_pairs(1.0, output_type="ndarray")
g = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(len(Q), len(Q)))
_, lab = connected_components(g, directed=False)
ids, cnt = np.unique(lab, return_counts=True)
fix = np.zeros(n, bool)
for o in np.where(cnt >= 20)[0]:
    C = Q[lab == ids[o]]; lo, hi = C.min(0) - 1.5, C.max(0) + 1.5
    fix |= np.all((P >= lo) & (P <= hi), axis=1)
dd = d.copy(); dd[fix] = 0.0
res["all_clusters_ge20_perfect_(bbox+1.5mm)"] = {
    "n_points_zeroed": int(fix.sum()), "p95_if_perfect": round(float(np.percentile(dd, 95)), 4),
    "max_if_perfect": round(float(dd.max()), 4), "frac_over_0.3_left": round(float((dd > 0.3).mean()), 4),
    "note": "hypothetical upper bound on what fixing every >0.8 mm cluster region could achieve; not a gate"}
json.dump(res, open("qa/probe/over_share_it2.json", "w"), indent=1)
print(json.dumps(res, indent=1))
