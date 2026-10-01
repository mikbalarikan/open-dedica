"""RV01: U-07 export mesh: delivered STL census and deviation from the B-rep, my own re-mesh at the
REPORT's settings (0.01 mm, 0.20 rad) compared triangle-for-triangle, sagitta, and the 3MF against the STL."""
import json, math, zipfile, re, hashlib
import numpy as np
import trimesh
from tools.core import read_step, write_stl, mesh_sagitta
from tools.measure import mesh_census, mesh_deviation, mass_properties
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
W = f"{J}/reviews/RV01_work"
STL = f"{J}/02_STEP_STL/od_c11_back_C1_v03.stl"
p = read_step(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
out = {}
out["census"] = {k: v.to_dict() for k, v in mesh_census(STL).items()}
print({k: v["measured"] for k, v in out["census"].items()})
dev = mesh_deviation(STL, p); out["deviation"] = dev.to_dict(); print("deviation", dev.measured, dev.status, dev.reason)
vol_b = p.volume; out["brep_volume"] = vol_b
m = trimesh.load(STL); out["stl_bbox"] = m.bounds.tolist(); out["stl_volume"] = float(m.volume); out["stl_tris"] = len(m.faces)
print("stl", out["stl_tris"], out["stl_volume"], vol_b, m.bounds.tolist())
# my own re-mesh at the recorded settings
w = write_stl(p, f"{W}/remesh_0p01_0p20.stl", tolerance=0.01, angular_tolerance=0.20)
out["remesh"] = {"triangles": w.detail["triangles"], "sagitta": w.detail["max_sagitta_mm"], "sha256": w.sha256}
r = trimesh.load(f"{W}/remesh_0p01_0p20.stl")
same = (len(r.faces) == len(m.faces)) and np.allclose(np.sort(r.triangles.reshape(-1, 9), axis=0), np.sort(m.triangles.reshape(-1, 9), axis=0), atol=1e-4)
out["remesh_same_triangles_as_delivered"] = bool(same)
out["remesh_sha_equals_delivered"] = w.sha256 == hashlib.sha256(open(STL, "rb").read()).hexdigest()
print("remesh", out["remesh"], same, out["remesh_sha_equals_delivered"])
# angular limit
Rmax = 6.0
out["angular_limit"] = 4 * math.acos(1 - 0.01 / Rmax)
# 3MF
z = zipfile.ZipFile(f"{J}/02_STEP_STL/od_c11_back_C1_v03.3mf")
names = z.namelist(); out["3mf_names"] = names
model = [n for n in names if n.endswith(".model")][0]
xml = z.read(model).decode()
unit = re.search(r'unit="(\w+)"', xml); out["3mf_unit"] = unit.group(1) if unit else None
vs = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml)])
ts = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml)])
tm = trimesh.Trimesh(vertices=vs, faces=ts, process=False)
tr = re.findall(r'transform="([^"]+)"', xml); out["3mf_transforms"] = tr
out["3mf"] = {"triangles": len(ts), "vertices": len(vs), "volume": float(tm.volume), "watertight": bool(tm.is_watertight),
              "bbox": tm.bounds.tolist()}
a = np.sort(np.round(tm.triangles.reshape(-1, 3), 4), axis=0); b = np.sort(np.round(m.triangles.reshape(-1, 3), 4), axis=0)
out["3mf_same_vertices_as_stl"] = bool(a.shape == b.shape and np.allclose(a, b, atol=1e-3))
# triangle sets compared (as sorted vertex triples)
def tri_keys(t): return sorted(tuple(sorted(tuple(np.round(v, 3)) for v in tri)) for tri in t)
out["3mf_same_triangles_as_stl"] = tri_keys(tm.triangles) == tri_keys(m.triangles)
print("3mf", out["3mf"], out["3mf_unit"], out["3mf_transforms"], out["3mf_same_vertices_as_stl"], out["3mf_same_triangles_as_stl"])
json.dump(out, open(f"{W}/m6_mesh.json", "w"), indent=1, default=str)
