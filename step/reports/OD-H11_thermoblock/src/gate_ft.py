"""Two-way CAD-vs-scan deviation gate (stl2step §7). Scan = ORIGINAL (unrepaired) aligned mesh."""
import trimesh, numpy as np, json
scan=trimesh.load_mesh("aligned.ply"); cad=trimesh.load_mesh("ft/out/thermoblock_ft_datum.stl")
rng=np.random.default_rng(0)
sv=scan.vertices[rng.choice(len(scan.vertices),120000,replace=False)]
d1=np.abs(trimesh.proximity.signed_distance(cad,sv)) if False else trimesh.proximity.closest_point(cad,sv)[1]
cs,_=trimesh.sample.sample_surface(cad,60000,seed=0)
cp,d2,_=trimesh.proximity.closest_point(scan,cs)
from scipy.spatial import cKDTree
from trimesh.grouping import group_rows
be=scan.edges_sorted[group_rows(scan.edges_sorted,require_count=1)]; bv=scan.vertices[np.unique(be)]
near_hole=cKDTree(bv).query(cp)[0]<1.0
rep=trimesh.load_mesh("repaired.ply"); d2r=trimesh.proximity.closest_point(rep,cs)[1]
restored=(d2>0.3)&(np.hypot(cs[:,0]+8.0,cs[:,1]+14.05)<18.5)&(cs[:,2]>1.0)&(cs[:,2]<34.5)
nodata=(d2>0.3)&((d2r<0.5*d2)|near_hole)&~restored   # CAD follows a MeshFix patch where the scanner saw nothing
def st(d): return dict(RMS=round(float(np.sqrt((d**2).mean())),3),p95=round(float(np.percentile(d,95)),3),p99=round(float(np.percentile(d,99)),3),max=round(float(d.max()),3),frac_le_0_3=round(float((d<=0.3).mean()),4))
R={"scan->CAD":st(d1),"CAD->scan (all)":st(d2),"CAD->scan (scanned surface only)":st(d2[~(nodata|restored)]),"CAD area on no-scan-data patches (fraction)":round(float(nodata.mean()),4),"CAD area in bore sector restored by 3-fold symmetry (fraction)":round(float(restored.mean()),4)}
# where are the big deviations? report by region
def region(p):
    z=p[:,2]; return np.where(z<1.0,"bottom face features (z<1)",np.where(z>46.8,"top face features (z>46.8)",np.where(np.hypot(p[:,0]+9.3,p[:,1]+13.8)>40,"lug / pipes / terminals","main body")))
for name,P,d in [("scan->CAD",sv,d1),("CAD->scan (scanned only)",cs[~(nodata|restored)],d2[~(nodata|restored)])]:
    rg=region(P); R[name+" by region"]={g:dict(n=int((rg==g).sum()),**st(d[rg==g])) for g in np.unique(rg)}
    bad=P[d>0.8]; R[name+" worst clusters (d>0.8mm) centroid samples"]=np.round(bad[rng.choice(len(bad),min(12,len(bad)),replace=False)],1).tolist() if len(bad) else []
np.save("ft/out/gate_d1.npy",np.c_[sv,d1]); np.save("ft/out/gate_d2.npy",np.c_[cs,d2,nodata|restored])
json.dump(R,open("ft/out/deviation_report.json","w"),indent=1); print(json.dumps(R,indent=1))
