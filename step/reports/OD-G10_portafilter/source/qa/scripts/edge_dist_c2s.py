#!/usr/bin/env python3
"""QA diagnostic (NOT a gate/mask): CAD->scan over-band clusters' distance to the nearest scan open-boundary
vertex (datum frame after inverse T_refine), same cluster graph as deviation_gate. usage: edge_dist_c2s.py <npz> <registration.json>"""
import sys, json
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import load_mesh, load_matrix
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
A = np.load(sys.argv[1]); cp, cd = A["c2s_pts"], A["c2s_d"]
scan = load_mesh("input/scan.stl"); M = load_matrix("intake/alignment.json")
Mi = np.linalg.inv(np.array(json.load(open(sys.argv[2]))["T_refine"])) @ M
eu, ct = np.unique(np.sort(scan.edges, axis=1), axis=0, return_counts=True)
bv = np.unique(eu[ct == 1].ravel()); B = (np.c_[scan.vertices[bv], np.ones(len(bv))] @ Mi.T)[:, :3]
tb = cKDTree(B)
sel = np.where(cd > 0.8)[0]; Q = cp[sel]
pr = cKDTree(Q).query_pairs(1.0, output_type="ndarray")
_, lab = connected_components(coo_matrix((np.ones(len(pr)), (pr[:, 0], pr[:, 1])), shape=(len(Q), len(Q))), directed=False)
ids, cnt = np.unique(lab, return_counts=True); order = np.lexsort((ids, -cnt))
out = []
for k, o in enumerate(order[:16]):
    if cnt[o] < 20: break
    m = lab == ids[o]; dd, _ = tb.query(Q[m])
    out.append({"cluster": k, "n": int(m.sum()), "dist_to_scan_boundary_p50": round(float(np.median(dd)), 2),
                "frac_within_3mm": round(float((dd < 3).mean()), 2)})
print(json.dumps({"cad_to_scan_clusters": out}, indent=1))
