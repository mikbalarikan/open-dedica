import trimesh, numpy as np
T0=np.load("T0.npy")
Tt=np.eye(4); Tt[:2,3]=[1.68,-0.34]
phi=np.radians(-90+49.90); Rz=np.eye(4); Rz[:2,:2]=[[np.cos(phi),-np.sin(phi)],[np.sin(phi),np.cos(phi)]]
T=Rz@Tt@T0
m=trimesh.load_mesh("OD-H24_flowmeter_raw.stl"); m.apply_transform(T)
n=m.face_normals; a=m.area_faces; c=m.triangles_center
for sg in (1,-1):
    f=(sg*n[:,2])>0.985
    h,e=np.histogram(c[f,2],bins=np.arange(-12,36,0.1),weights=a[f])
    top=np.argsort(-h)[:14]
    print("normal",sg, [(round(e[i],1),round(h[i],1)) for i in sorted(top)])
np.save("T1pre.npy",T)
