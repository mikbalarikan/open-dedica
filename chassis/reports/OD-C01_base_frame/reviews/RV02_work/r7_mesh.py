import json, math, struct, zipfile, re
from pathlib import Path
import numpy as np
from build123d import import_step
from tools.core import write_stl, mesh_sagitta
from tools.measure import mesh_census, mesh_deviation, envelope
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
WK = W/"reviews/RV02_work"
sh = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
STL = W/"02_STEP_STL/od_c01_frame_C1_v03.stl"
out={}
def R(r): return dict(m=getattr(r,"measured",None), st=str(getattr(r,"status",None)),
                      at=getattr(r,"at",None), why=getattr(r,"reason",None))
mc = mesh_census(str(STL))
out["mesh_census"]={k:R(v) for k,v in mc.items()}
# raw STL read
raw = STL.read_bytes()
n = struct.unpack("<I", raw[80:84])[0]
out["stl_header_triangles"]=n; out["stl_bytes"]=len(raw)
tris = np.frombuffer(raw[84:], dtype=np.dtype([("n","<3f4"),("v","<3,3f4"),("a","<u2")]), count=n)
V = tris["v"].reshape(-1,3).astype(float)
out["stl_bbox"]=[list(map(float,V.min(0))), list(map(float,V.max(0)))]
# angular limit
out["angular_limit_rad"]=4*math.acos(1-0.01/6.0)
# deviation
dev = mesh_deviation(str(STL), sh)
out["mesh_deviation"]=R(dev)
# re-mesh independently at the REPORT's tolerances
res = write_stl(sh, str(WK/"remesh_tol01.stl"), tolerance=0.01, angular_tolerance=0.20)
out["remesh"]={"checks":{k:R(v) for k,v in (getattr(res,"checks",None) or {}).items()}} if hasattr(res,"checks") else {"raw":repr(res)}
try:
    out["remesh_sagitta"]=R(res.checks["max_sagitta"]); out["remesh_triangles"]=res.measured
except Exception as e: out["remesh_err"]=repr(e)
rraw=(WK/"remesh_tol01.stl").read_bytes()
out["remesh_header_triangles"]=struct.unpack("<I", rraw[80:84])[0]
out["remesh_bytes_equal_delivered"]= (rraw==raw)
out["remesh_census"]={k:R(v) for k,v in mesh_census(str(WK/"remesh_tol01.stl")).items()}
# 3MF
TMF = W/"02_STEP_STL/od_c01_frame_C1_v03.3mf"
with zipfile.ZipFile(TMF) as z:
    out["3mf_entries"]=z.namelist()
    model=[nm for nm in z.namelist() if nm.endswith(".model")][0]
    xml=z.read(model).decode("utf8","replace")
verts=re.findall(r'<vertex\s+x="([^"]+)"\s+y="([^"]+)"\s+z="([^"]+)"', xml)
trs=re.findall(r'<triangle\s+v1="(\d+)"\s+v2="(\d+)"\s+v3="(\d+)"', xml)
out["3mf_vertices"]=len(verts); out["3mf_triangles"]=len(trs)
P=np.array(verts,float); T=np.array(trs,int)
out["3mf_bbox"]=[list(map(float,P.min(0))), list(map(float,P.max(0)))]
a,b,c = P[T[:,0]],P[T[:,1]],P[T[:,2]]
out["3mf_volume"]=float(np.einsum('ij,ij->i', a, np.cross(b,c)).sum()/6.0)
out["3mf_unit"]=re.search(r'unit="([^"]+)"', xml).group(1) if re.search(r'unit="([^"]+)"', xml) else None
# compare 3MF mesh to STL mesh as point sets
sv = np.unique(np.round(V,4),axis=0); pv = np.unique(np.round(P,4),axis=0)
out["stl_unique_vertices"]=len(sv); out["3mf_unique_vertices"]=len(pv)
out["vertex_sets_equal"]= len(sv)==len(pv) and bool(np.array_equal(np.sort(sv,axis=0),np.sort(pv,axis=0)))
json.dump(out, open(WK/"r7_mesh.json","w"), indent=1, default=str)
for k,v in out.items(): print(k,"=",v if len(str(v))<300 else str(v)[:300]+"...")
