import trimesh,numpy as np,json
R='/tmp/claude-0/-home-user-agentic-STL-to-CAD/d8e5b691-152f-55fe-9a52-555e01807691/scratchpad/job/OD-W03_water-tank-valve'
m=trimesh.load(R+'/intake/work.stl')
n=np.array([-0.658069,0.44949,0.604073]);n/=np.linalg.norm(n)
c=np.array([9.716,-25.1343,-206.0183])
# material side: which side of plane has most area
d=(m.triangles_center-c)@n
print('area above',m.area_faces[d>0.3].sum(),'below',m.area_faces[d<-0.3].sum(), 'range',d.min(),d.max())
z=n if m.area_faces[d>0.3].sum()>m.area_faces[d<-0.3].sum() else -n
# pca in plane
P=m.vertices-c; Pp=P-np.outer(P@z,z)
w,v=np.linalg.eigh(np.cov(Pp.T)); x=v[:,-1]; x-= (x@z)*z; x/=np.linalg.norm(x); y=np.cross(z,x)
Rm=np.array([x,y,z]); V=P@Rm.T
T=np.eye(4);T[:3,:3]=Rm;T[:3,3]=-Rm@c
m.apply_transform(T)
print('extents',m.bounds)
m.export('pre.stl'); np.save('preT.npy',T)
