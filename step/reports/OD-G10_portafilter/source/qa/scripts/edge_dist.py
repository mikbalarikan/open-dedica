#!/usr/bin/env python3
"""QA diagnostic (NOT a gate, NOT a mask): for each scan->CAD over-band cluster (same KD graph as
deviation_gate.over_band_clusters), distance from its points to the nearest scan open-boundary vertex
(edges used once in the welded full-res scan), in the datum frame (alignment.json, then inverse T_refine as
deviation_gate does). Tests whether a cluster sits on a scan hole edge.
usage: edge_dist.py <arrays.npz> <registration.json>"""
import sys, json
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import load_mesh, load_matrix
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
A = np.load(sys.argv[1]); sp, sd = A["s2c_pts"], A["s2c_d"]
scan = load_mesh("input/scan.stl")
M = load_matrix("intake/alignment.json")
T = np.array(json.load(open(sys.argv[2]))["T_refine"])
Mi = np.linalg.inv(T) @ M
eu, ct = np.unique(np.sort(scan.edges, axis=1), axis=0, return_counts=True)
bv = np.unique(eu[ct == 1].ravel())
B = (np.c_[scan.vertices[bv], np.ones(len(bv))] @ Mi.T)[:, :3]
tb = cKDTree(B)
sel = np.where(sd > 0.8)[0]; Q = sp[sel]
pr = cKDTree(Q).query_pairs(1.0, output_type="ndarray")
_, lab = connected_components(coo_matrix((np.ones(len(pr)), (pr[:, 0], pr[:, 1])), shape=(len(Q), len(Q))), directed=False)
ids, cnt = np.unique(lab, return_counts=True); order = np.lexsort((ids, -cnt))
# sanity: nearest boundary distance of ALL scan vertices, to show the check is discriminating
dall, _ = tb.query(sp)
out = {"n_boundary_vertices": int(len(bv)), "all_scan_points_dist_to_boundary_p50": float(np.median(dall)),
       "frac_all_scan_points_within_3mm_of_boundary": float((dall < 3).mean()), "clusters": []}
for k, o in enumerate(order):
    if cnt[o] < 20: break
    m = lab == ids[o]; dd, _ = tb.query(Q[m])
    out["clusters"].append({"cluster": k, "n": int(m.sum()), "dist_to_scan_boundary_p50": round(float(np.median(dd)), 2),
                            "dist_to_scan_boundary_max": round(float(dd.max()), 2),
                            "frac_within_3mm": round(float((dd < 3).mean()), 2)})
print(json.dumps(out, indent=1))
