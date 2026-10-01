"""RV01: U-07 / V-05 on the delivered STL and 3MF."""
import json, math, hashlib, zipfile, re
from pathlib import Path
import numpy as np
from tools.core import read_step, write_stl, mesh_sagitta
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
W = J / "reviews/RV01_work"
stl = J / "02_STEP_STL/od_c05_carrier_C1_v01.stl"
tmf = J / "02_STEP_STL/od_c05_carrier_C1_v01.3mf"
part = read_step(J / "02_STEP_STL/od_c05_carrier_C1_v01.step")
out = {}
mc = mesh_census(stl); out["census"] = {k: v.measured for k, v in mc.items()}
print("census", out["census"])
md = mesh_deviation(stl, part); out["deviation"] = md.to_dict(); print("deviation", md.measured, md.at, md.status, md.reason)
# the D5 export re-made from the STEP at the recorded settings
w = write_stl(part, W / "remesh_0.01_0.20.stl", tolerance=0.01, angular_tolerance=0.20)
out["remesh"] = dict(sha=w.sha256, triangles=w.detail["triangles"], sagitta=w.detail["max_sagitta_mm"],
                     same_bytes=w.sha256 == hashlib.sha256(stl.read_bytes()).hexdigest())
print("remesh", out["remesh"])
lim = 4 * math.acos(1 - 0.01 / 6.0); out["angular_limit"] = lim; print("angular limit", lim)
try:
    mw = min_wall_mesh(stl); out["min_wall_mesh"] = mw.to_dict(); print("min_wall_mesh", mw.measured, mw.status, mw.reason, mw.detail.get("vertex_precision_mm"))
except Exception as e:
    print("min_wall_mesh err", e)
# the 3MF: parse the model XML
def load_stl(p):
    b = p.read_bytes(); n = int.from_bytes(b[80:84], "little")
    a = np.frombuffer(b[84:84 + n * 50], dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]))
    return a["v"].astype(float)
tri_stl = load_stl(stl)
with zipfile.ZipFile(tmf) as z:
    names = z.namelist(); model = [n for n in names if n.endswith(".model")][0]
    xml = z.read(model).decode()
unit = re.search(r'unit="(\w+)"', xml); unit = unit.group(1) if unit else "millimeter(default)"
verts = np.array([[float(x) for x in m] for m in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml)])
tris = np.array([[int(x) for x in m] for m in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml)])
tri_3mf = verts[tris]
def vol(t): return float(np.sum(np.einsum("ij,ij->i", t[:, 0], np.cross(t[:, 1], t[:, 2]))) / 6)
key = lambda t: sorted(tuple(np.round(t.reshape(-1, 3), 3).tolist()[i]) for i in range(3))
s1 = sorted(tuple(map(tuple, sorted(np.round(t, 3).tolist()))) for t in tri_stl)
s2 = sorted(tuple(map(tuple, sorted(np.round(t, 3).tolist()))) for t in tri_3mf)
out["3mf"] = dict(files=names, unit=unit, vertices=len(verts), triangles=len(tris), volume=vol(tri_3mf),
                  stl_triangles=len(tri_stl), stl_volume=vol(tri_stl), same_triangle_set=s1 == s2,
                  max_vertex_diff=None)
print("3mf", out["3mf"])
(W / "m4_mesh.json").write_text(json.dumps(out, indent=1, default=str))
