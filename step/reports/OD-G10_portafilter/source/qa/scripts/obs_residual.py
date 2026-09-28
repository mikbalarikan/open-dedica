#!/usr/bin/env python3
"""QA diagnostic (NOT a gate, NOT a mask): observable CAD->scan stats with the points of the full-set
CAD->scan over-band clusters 0-3 (unscanned regions named in it1 L2: both outlet-pocket bores, U-rib
centre open-boundary region, grip strip) removed, to size what a geometry fix could still move.
usage: obs_residual.py <arrays.npz> <step> <deviation.json>"""
import sys, tempfile, json
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
sys.path.insert(0, str(Path(__file__).parent))
from _common import stats, step_to_mesh
from observability import observable_split
import importlib.util
spec = importlib.util.spec_from_file_location("ca", str(Path(__file__).parent / "cluster_attrib.py"))
A = np.load(sys.argv[1]); cp, cfi, cd = A["c2s_pts"], A["c2s_fid"], A["c2s_d"]
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
sel = np.where(cd > 0.8)[0]; Q = cp[sel]
pr = cKDTree(Q).query_pairs(1.0, output_type="ndarray")
_, lab = connected_components(coo_matrix((np.ones(len(pr)), (pr[:, 0], pr[:, 1])), shape=(len(Q), len(Q))), directed=False)
ids, cnt = np.unique(lab, return_counts=True); order = np.lexsort((ids, -cnt))
rank = np.full(len(cd), -1); rk = {int(ids[o]): k for k, o in enumerate(order)}; rank[sel] = [rk[int(x)] for x in lab]
cad = step_to_mesh(sys.argv[2], Path(tempfile.mkdtemp()) / "t.stl")
ob = observable_split(cad, cp, cfi, cd, 20000, 5, 0.5, 60.0, chunk=200)
sub, om = ob["_sub"], ob["_obs_mask"]
d, rr, P = cd[sub][om], rank[sub][om], cp[sub][om]
keep = ~np.isin(rr, [0, 1, 2, 3])
out = {"observable_all": stats(d), "observable_without_full_clusters_0_3": stats(d[keep]),
       "removed_n": int((~keep).sum())}
rest = np.where(keep & (d > 0.8))[0]
out["remaining_over_band"] = [{"d": round(float(d[i]), 3), "xyz": P[i].round(2).tolist(), "full_cluster": int(rr[i])} for i in rest[np.argsort(-d[rest])]]
print(json.dumps(out, indent=1))
