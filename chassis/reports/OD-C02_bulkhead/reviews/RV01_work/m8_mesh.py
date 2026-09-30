import json, math, zipfile, re
import numpy as np
from pathlib import Path
from tools.core.step import read_step
from tools.core.mesh import write_stl, mesh_sagitta
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh
from tools.measure.wall import load_mesh
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); W = J/"reviews/RV01_work"
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
stl = J/"02_STEP_STL/od_c02_bulkhead_C1_v02.stl"
out = {}
out["census"] = {k: v.to_dict() for k, v in mesh_census(stl).items()}
out["deviation"] = mesh_deviation(stl, s).to_dict()
out["ang_limit"] = 4*math.acos(1 - 0.01/6.0)
w = write_stl(s, W/"rv01_remesh.stl", tolerance=0.01, angular_tolerance=0.2)
out["remesh"] = {"sha": w.sha256, **w.detail}
m0 = load_mesh(stl); m1 = load_mesh(W/"rv01_remesh.stl")
out["same_vertices"] = bool(len(m0.vertices) == len(m1.vertices) and np.allclose(np.unique(np.round(m0.vertices, 5), axis=0), np.unique(np.round(m1.vertices, 5), axis=0)))
out["stl_bounds"] = m0.bounds.tolist(); out["stl_volume"] = float(m0.volume)
import hashlib
out["remesh_same_bytes"] = hashlib.sha256(open(W/"rv01_remesh.stl","rb").read()[80:]).hexdigest() == hashlib.sha256(open(stl,"rb").read()[80:]).hexdigest()
# 3MF
z = zipfile.ZipFile(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.3mf")
out["3mf_names"] = z.namelist()
model = [n for n in z.namelist() if n.endswith(".model")][0]
txt = z.read(model).decode()
unit = re.search(r'unit="([^"]+)"', txt)
V = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', txt)])
T = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', txt)])
tr = re.findall(r'transform="([^"]+)"', txt)
out["3mf"] = {"unit": unit.group(1) if unit else None, "vertices": len(V), "triangles": len(T), "bounds": [V.min(0).tolist(), V.max(0).tolist()], "transforms": tr, "objects": len(re.findall(r"<object ", txt))}
import trimesh
m3 = trimesh.Trimesh(V, T, process=True)
out["3mf"]["volume"] = float(m3.volume); out["3mf"]["watertight"] = bool(m3.is_watertight)
tri0 = np.sort(np.round(m0.vertices[m0.faces], 4).reshape(len(m0.faces), -1), axis=1)
# compare triangle sets as sorted vertex triples
def key(m):
    t = np.round(m.vertices[m.faces], 4)
    t = np.sort(t.view([('', t.dtype)]*3).reshape(len(t), 3), axis=1).view(t.dtype).reshape(len(t), 9)
    return set(map(tuple, t))
k0, k3 = key(m0), key(m3)
out["3mf_vs_stl"] = {"stl_tris": len(k0), "3mf_tris": len(k3), "common": len(k0 & k3)}
out["min_wall_mesh"] = min_wall_mesh(stl).to_dict()
(W/"m8_mesh.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps({k: v for k, v in out.items()}, default=str)[:4000])
