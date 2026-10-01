"""RV01: compare triangle sets of delivered STL, my re-mesh, and the 3MF via vertex matching (KD tree)."""
import json, zipfile, re
import numpy as np, trimesh
from scipy.spatial import cKDTree
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
def load3mf(path):
    z = zipfile.ZipFile(path); xml = z.read([n for n in z.namelist() if n.endswith(".model")][0]).decode()
    vs = np.array(re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml), float)
    ts = np.array(re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml), int)
    return vs[ts]
def tris_stl(path): return trimesh.load(path, process=False).triangles
def compare(A, B, tol=1e-3):
    va = np.unique(np.round(A.reshape(-1, 3), 5), axis=0); vb = np.unique(np.round(B.reshape(-1, 3), 5), axis=0)
    ta = cKDTree(va); tb = cKDTree(vb)
    da, _ = tb.query(va); db, _ = ta.query(vb)
    # triangle keys by vertex ids in a common set
    allv = np.vstack([va, vb]); t = cKDTree(allv)
    def key(T):
        ids = []
        for tri in T:
            k = []
            for v in tri:
                _, i = t.query(v); k.append(tuple(np.round(allv[i], 3)))
            ids.append(tuple(sorted(k)))
        return set(ids)
    ka, kb = key(A), key(B)
    return {"tris": [len(A), len(B)], "verts": [len(va), len(vb)], "max_vertex_gap": float(max(da.max(), db.max())),
            "tri_sets_equal": ka == kb, "only_a": len(ka - kb), "only_b": len(kb - ka)}
S = tris_stl(f"{J}/02_STEP_STL/od_c11_back_C1_v03.stl")
R = tris_stl(f"{W}/remesh_0p01_0p20.stl")
M = load3mf(f"{J}/02_STEP_STL/od_c11_back_C1_v03.3mf")
out = {"stl_vs_3mf": compare(S, M), "stl_vs_remesh": compare(S, R)}
print(out); json.dump(out, open(f"{W}/m6b_meshcmp.json", "w"), indent=1)
