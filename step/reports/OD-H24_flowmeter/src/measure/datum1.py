import trimesh, numpy as np
m = trimesh.load_mesh("OD-H24_flowmeter_raw.stl")
n=m.face_normals; a=m.area_faces; c=m.triangles_center
n0=np.array([-0.565,-0.813,-0.139]); n0/=np.linalg.norm(n0)
dp=n@n0
# refine axis from side-wall normals: min eigenvector of sum a n n^T over |dp|<0.2
sel=np.abs(dp)<0.25
M=(n[sel]*a[sel,None]).T@n[sel]
w,V=np.linalg.eigh(M); ax=V[:,0]; ax*=np.sign(ax@n0)
print("eig",w, "axis",ax, "angle to n0",np.degrees(np.arccos(ax@n0)))
# planar faces
for s in (1,-1):
    f=(s*dp)>0.98
    h=c[f]@n0
    hist,edges=np.histogram(h,bins=120,weights=a[f])
    top=np.argsort(-hist)[:8]
    print("side",s,"area",a[f].sum(), [(round(edges[i],2),round(hist[i],1)) for i in sorted(top)])
np.save("ax0.npy",ax)
