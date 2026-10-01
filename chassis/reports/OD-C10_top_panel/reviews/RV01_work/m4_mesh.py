import sys, time, json, zipfile, re, hashlib, math
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
import numpy as np, trimesh
from tools.core import write_stl
from tools.core.step import file_sha256
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh
STL = JOB / "02_STEP_STL/od_c10_top_C1_v01.stl"; MF = JOB / "02_STEP_STL/od_c10_top_C1_v01.3mf"
out = {}
L = lid()
out["census"] = {k: (r.measured, r.status, r.reason) for k, r in mesh_census(STL).items()}
m = trimesh.load(STL, process=False)
out["stl_bounds"] = m.bounds.tolist(); out["stl_volume"] = float(m.volume)
md = mesh_deviation(STL, L); out["deviation"] = (md.measured, md.at, md.detail)
# fresh mesh at the recorded settings
w = write_stl(L, WORK / "remesh_0.01_0.17.stl", tolerance=0.01, angular_tolerance=0.17)
out["remesh"] = {"sha": w.sha256, "same_bytes_as_delivered": w.sha256 == file_sha256(STL), "detail": w.detail,
                 "sagitta": (w.checks["max_sagitta"].measured, w.checks["max_sagitta"].status)}
out["ang_limit"] = 4 * math.acos(1 - 0.01 / 10.0)
# 3MF
with zipfile.ZipFile(MF) as z:
    xml = z.read("3D/3dmodel.model").decode()
out["3mf_unit"] = re.search(r'unit="([a-z]+)"', xml).group(1) if 'unit="' in xml else "default(mm)"
vs = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml)])
ts = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml)])
out["3mf_counts"] = (len(vs), len(ts))
t3 = trimesh.Trimesh(vs, ts, process=False)
out["3mf_volume"] = float(t3.volume); out["3mf_bounds"] = t3.bounds.tolist(); out["3mf_watertight"] = bool(t3.is_watertight)
# triangle-set equality: sorted triangle vertex coordinates
def key(mesh):
    tri = np.round(mesh.vertices[mesh.faces], 4)
    tri = np.sort(tri.reshape(-1, 3, 3).tolist(), axis=None) if False else tri
    rows = [tuple(sorted(map(tuple, t))) for t in tri]
    return sorted(rows)
ks, k3 = key(m), key(t3)
out["3mf_same_triangles_as_stl"] = (ks == k3)
diff = max(np.abs(np.array(ks) - np.array(k3)).max(), 0) if len(ks) == len(k3) else None
out["3mf_max_coord_diff"] = float(diff) if diff is not None else None
dump("m4_mesh.json", out)
print(json.dumps(out, default=str)[:5000])
