import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from mesh_lib import *
from build123d import Solid
from tools.core.mesh import write_stl, mesh_sagitta
from tools.core.step import file_sha256
from tools.measure import mesh_census, mesh_deviation
import math
s = Solid(solids(read_step(STEP))[0])
res = {}
res["ang_limit"] = 4 * math.acos(1 - 0.01 / 6.0)
w = write_stl(s, OUT / "remesh_0p01_0p20.stl", tolerance=0.01, angular_tolerance=0.20)
res["remesh"] = {"sha": w.sha256 if hasattr(w, "sha256") else str(w), "detail": w.detail, "sagitta": w.checks["max_sagitta"]}
res["remesh_sha"] = file_sha256(OUT / "remesh_0p01_0p20.stl")
res["delivered_sha"] = file_sha256(STL)
res["byte_identical"] = res["remesh_sha"] == res["delivered_sha"]
res["census_delivered"] = mesh_census(STL)
res["deviation_delivered"] = mesh_deviation(STL, s)
st = read_stl(STL)
m = read_3mf(MF3)
res["3mf"] = {"names": m["names"], "unit": m["unit"], "objects": m["objects"], "items": m["items"], "triangles": int(len(m["tris"]))}
res["stl_triangles"] = int(len(st))
a, b = tri_key_set(st), tri_key_set(m["tris"])
res["tri_sets_equal"] = a == b
res["tri_only_stl"] = len(a - b); res["tri_only_3mf"] = len(b - a)
res["vol_stl"] = signed_volume(st); res["vol_3mf"] = signed_volume(m["tris"]); res["vol_brep"] = s.volume
res["bbox_stl"] = [st.reshape(-1,3).min(0).tolist(), st.reshape(-1,3).max(0).tolist()]
res["bbox_3mf"] = [m["tris"].reshape(-1,3).min(0).tolist(), m["tris"].reshape(-1,3).max(0).tolist()]
dump("m5_mesh", res); print("done")
