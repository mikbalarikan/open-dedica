# it2 QA: copied from _it1_SUPERSEDED/qa/probe/cluster_probe.py unchanged (same method, CHK-LIKE4LIKE).
"""QA-only probe (not a gate): characterise each scan->CAD over-band cluster of qa/deviation.json.
Re-clusters exactly as deviation_gate.over_band_clusters (eps 1.0, >=20 pts, same order), then for
each cluster reports: fraction of scan points INSIDE the CAD solid (CAD has excess material there /
scan surface sunk) vs OUTSIDE (scan material the CAD lacks), the mean scan vertex normal, and the
per-axis extent. Inputs: qa/dev_arrays.npz (post-ICP design frame), build/<part>_datum.step
tessellated by QA's own _common.step_to_mesh. Writes qa/probe/cluster_probe.json."""
import json, sys, tempfile
from pathlib import Path
import numpy as np
S = "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts"
sys.path.insert(0, S)
from _common import step_to_mesh, load_mesh, load_matrix
from deviation_gate import over_band_clusters
import trimesh
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial import cKDTree

z = np.load("qa/dev_arrays.npz")
cad = step_to_mesh("build/OD-S01_steam-valve_datum.step", Path(tempfile.mkdtemp()) / "c.stl")
# scan vertex normals in the same frame
scan = load_mesh("input/scan.stl"); scan.apply_transform(load_matrix("intake/alignment.json"))
Tr = np.asarray(json.load(open("qa/registration.json"))["T_refine"]); scan.apply_transform(np.linalg.inv(Tr))
assert np.allclose(scan.vertices, z["s2c_pts"])
N = scan.vertex_normals
out = {}
for dn, P, d in (("scan_to_cad", z["s2c_pts"], z["s2c_d"]),):
    sel = np.where(d > 0.8)[0]; Q = P[sel]
    pairs = cKDTree(Q).query_pairs(1.0, output_type="ndarray")
    g = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(len(Q), len(Q)))
    _, lab = connected_components(g, directed=False)
    ids, cnt = np.unique(lab, return_counts=True)
    order = [o for o in np.lexsort((ids, -cnt)) if cnt[o] >= 20]
    rows = []
    for rank, o in enumerate(order):
        m = lab == ids[o]; C = Q[m]; idx = sel[m]
        inside = cad.contains(C)
        nm = N[idx].mean(0); nm /= np.linalg.norm(nm)
        rows.append({"rank": rank, "n": int(m.sum()), "centroid": C.mean(0).round(2).tolist(),
                     "min": C.min(0).round(2).tolist(), "max": C.max(0).round(2).tolist(),
                     "frac_inside_cad": round(float(inside.mean()), 3),
                     "mean_scan_normal": nm.round(2).tolist(),
                     "d_p50": round(float(np.median(d[idx])), 3), "d_max": round(float(d[idx].max()), 3)})
    out[dn] = rows
json.dump(out, open("qa/probe/cluster_probe.json", "w"), indent=1)
for r in out["scan_to_cad"]:
    print(r)
