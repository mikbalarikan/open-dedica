import trimesh, numpy as np
m = trimesh.load_mesh("OD-H24_flowmeter_raw.stl")
n=m.face_normals; a=m.area_faces; c=m.triangles_center
ax=np.load("ax0.npy")
x=np.cross([0,0,1.0],ax); x/=np.linalg.norm(x); y=np.cross(ax,x)
R=np.vstack([x,y,ax])
pl=np.load("plane_63.npy"); z0=pl[3:]@ax
C=(c@R.T); C[:,2]-=z0
N=n@R.T
side=np.abs(N[:,2])<0.15
# axis point: least squares normals-lines intersection in XY: minimize sum |(I - nn^T)(p - c)|^2 over 2D
P=C[side,:2]; nn=N[side,:2]; nn/=np.linalg.norm(nn,axis=1)[:,None]; w=a[side]
A=np.zeros((2,2)); b=np.zeros(2)
for i in range(0,len(P),50000):
    Pi=P[i:i+50000]; ni=nn[i:i+50000]; wi=w[i:i+50000]
    Mi=np.eye(2)[None]-ni[:,:,None]*ni[:,None,:]
    A+=(wi[:,None,None]*Mi).sum(0); b+=(wi[:,None,None]*Mi@Pi[:,:,None]).sum(0)[:,0]
ctr=np.linalg.solve(A,b); print("axis pt (xy)",ctr)
r=np.hypot(P[:,0]-ctr[0],P[:,1]-ctr[1]); zz=C[side,2]
H,xe,ye=np.histogram2d(zz,r,bins=[np.arange(-40,30,0.5),np.arange(0,40,0.25)],weights=w)
for i in range(len(xe)-1):
    row=H[i]
    if row.sum()>3: 
        top=np.argsort(-row)[:3]
        print("z %.1f"%xe[i], [(round(ye[j],2),round(row[j],1)) for j in top])
T=np.eye(4); T[:3,:3]=R; T[:3,3]=-R@np.zeros(3); T[2,3]=-z0
T2=np.eye(4); T2[:2,3]=-ctr; T=T2@T
np.save("T0.npy",T)
