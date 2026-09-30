import json, numpy as np, tempfile, shutil
from pathlib import Path
from tools.core import read_step, compare_step, mesh_sagitta, write_stl
from tools.core.step import read_schema, read_length_unit, read_header, labels
from tools.core.shapes import faces, solids
from tools.measure import radial_extent, radial_profile, mesh_census, mesh_deviation, envelope
from tools.measure.features import cylinder, kind
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle"); WK = W/"reviews/RV01_work"
step = W/"02_STEP_STL/od_c03_cradle_C1_v01.step"; stl = W/"02_STEP_STL/od_c03_cradle_C1_v01.stl"
p = read_step(step)
O,A,R=(0,0,0),(0,0,1),(1,0,0)
out={}
angs=list(range(50,131,5))
for band in ((15.5,20.5),(25.5,30.5)):
    rp = radial_profile(p,O,A,R,angs,band,margin=0,z_step=0.1,side="inner")
    out[f"REQ01_{band}"]={k:{"m":v.measured,"st":v.status,"at":v.at,"reason":v.reason,"n_points":len(v.detail.get("points",[])),"unread":len(v.detail.get("unread",[]) or []),"on_face":v.detail.get("on_face")} for k,v in rp.items()}
for z in (18.0,28.0):
    for a in (50.0,130.0):
        r=radial_extent(p,O,A,R,a,z,side="inner"); out[f"REQ02_in_{a}_{z}"]=(r.measured,r.status,r.at)
    edge=[]
    for a in np.arange(43.0,47.01,0.25):
        for aa in (float(a),float(180-a)):
            r=radial_extent(p,O,A,R,aa,z,side="inner"); edge.append((aa, round(r.measured,4) if r.ok else None))
    out[f"edge_{z}"]=edge
for f in faces(p):
    if kind(f)=="cylinder":
        o,d,rr = cylinder(f); out.setdefault("cyl",[]).append(([round(float(x),4) for x in o],[round(float(x),4) for x in d],round(float(rr),5)))
# U-04: header, schema, unit, labels, compare the file against a second independent read
out["schema"]=read_schema(step); out["unit"]=read_length_unit(step); out["header"]=read_header(step); out["labels"]=labels(p)
txt=step.read_text(errors="replace")
out["step_counts"]={k: txt.count(k) for k in ("MANIFOLD_SOLID_BREP","CLOSED_SHELL","OPEN_SHELL","SHELL_BASED_SURFACE_MODEL","ADVANCED_FACE","PRODUCT(","B_SPLINE_SURFACE")}
cmp_ = compare_step(p, step); out["compare_step"]={k:(v.measured,v.status,v.reason) for k,v in cmp_.items()}
# U-07: delivered STL
mc = mesh_census(str(stl)); out["mesh_census"]={k:(v.measured,v.status) for k,v in mc.items()} if isinstance(mc,dict) else mc.to_dict()
md = mesh_deviation(str(stl), p); out["mesh_deviation"]=md.to_dict() if hasattr(md,"to_dict") else {k:v.to_dict() for k,v in md.items()}
# fresh mesh at the delivery settings into work dir
ang = 4*np.arccos(1-0.01/32.0); out["ang_limit"]=float(ang)
p2 = read_step(step)
wr = write_stl(p2, WK/"remesh_tol0p01.stl", tolerance=0.01, angular_tolerance=0.1)
out["remesh"]={"sha":wr.sha256,"detail":wr.detail}
mc2=mesh_census(str(WK/"remesh_tol0p01.stl")); out["remesh_census"]={k:(v.measured,v.status) for k,v in mc2.items()} if isinstance(mc2,dict) else mc2.to_dict()
out["stl_bytes_equal_remesh"] = (WK/"remesh_tol0p01.stl").read_bytes()==stl.read_bytes()
json.dump(out, open(WK/"m5.json","w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:9000])
