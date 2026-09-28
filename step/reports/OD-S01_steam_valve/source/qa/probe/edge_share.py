# it2 QA: copied unchanged from _it1_SUPERSEDED/qa/probe/edge_share.py.
"""QA-only probe: how much of the diffuse scan->CAD 0.30..0.80 mm population sits next to sharp CAD
edges (dihedral > 30 deg), i.e. where a moulded/scanned rounded edge meets a sharp CAD corner?
Distance from each scan point to the nearest sharp-edge polyline sample (0.05 mm spacing)."""
import json, sys, tempfile
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import step_to_mesh
from scipy.spatial import cKDTree
z = np.load("qa/dev_arrays.npz"); P, d = z["s2c_pts"], z["s2c_d"]
cad = step_to_mesh("build/OD-S01_steam-valve_datum.step", Path(tempfile.mkdtemp()) / "c.stl")
ang = np.degrees(cad.face_adjacency_angles)
E = cad.face_adjacency_edges[ang > 30]
A, B = cad.vertices[E[:, 0]], cad.vertices[E[:, 1]]
L = np.linalg.norm(B - A, axis=1)
pts = [A[i] + np.outer(np.linspace(0, 1, max(2, int(L[i] / 0.05) + 1)), B[i] - A[i]) for i in range(len(E))]
S = np.vstack(pts)
de = cKDTree(S).query(P, workers=-1)[0]
res = {"n_sharp_edges": int(len(E)), "sharp_edge_length_mm": float(L.sum())}
for band in ((0.3, 0.8), (0.8, 99)):
    m = (d > band[0]) & (d <= band[1])
    res[f"d_{band[0]}_{band[1]}"] = {"n": int(m.sum()), "frac_of_all": round(float(m.mean()), 4)}
    for r in (0.5, 1.0, 1.5):
        res[f"d_{band[0]}_{band[1]}"][f"within_{r}mm_of_sharp_edge"] = round(float((de[m] <= r).mean()), 3)
for r in (0.5, 1.0):
    res[f"all_points_within_{r}mm_of_sharp_edge"] = round(float((de <= r).mean()), 3)
    dd = d.copy(); dd[de <= r] = 0
    res[f"p95_excluding_within_{r}mm_of_edges (hypothetical, not a gate)"] = round(float(np.percentile(d[de > r], 95)), 4)
print(json.dumps(res, indent=1))
json.dump(res, open("qa/probe/edge_share.json", "w"), indent=1)
