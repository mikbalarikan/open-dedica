"""secpoly.py z [tol] [minlen] [mesh] : simplified polylines of a z-section (chained segments)"""
import trimesh, numpy as np, sys
import shapely.geometry as sg, shapely.ops as so
z=float(sys.argv[1]); tol=float(sys.argv[2]) if len(sys.argv)>2 else 0.15; minlen=float(sys.argv[3]) if len(sys.argv)>3 else 3
m = trimesh.load_mesh(sys.argv[4] if len(sys.argv)>4 else "aligned.ply")
segs=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z])[:,:,:2]
segs=np.round(segs,5)
ml=so.linemerge(sg.MultiLineString([s for s in segs if np.linalg.norm(s[0]-s[1])>1e-9]))
geoms=list(ml.geoms) if hasattr(ml,"geoms") else [ml]
geoms=sorted(geoms,key=lambda g:-g.length)
for i,L in enumerate(geoms):
    if L.length<minlen: continue
    d=np.array(L.coords); s=np.array(L.simplify(tol).coords)
    print("poly %d len %.1f closed %s n %d x[%.2f,%.2f] y[%.2f,%.2f]"%(i,L.length,L.is_ring,len(s),d[:,0].min(),d[:,0].max(),d[:,1].min(),d[:,1].max()))
    print("   "+" ".join("(%.2f,%.2f)"%tuple(q) for q in s))
