import numpy as np, trimesh, json
m=trimesh.load('intake/work.stl')
n=np.array([-0.392,-0.489,-0.779]); n/=np.linalg.norm(n)
z=-n  # +Z into the body
x=np.cross([0,0,1.],z); x/=np.linalg.norm(x); y=np.cross(z,x)
R=np.stack([x,y,z])
C=m.triangles_center@R.T; N=m.face_normals@R.T; A=m.area_faces
# disc face plane offset
sel=(N[:,2]<-0.98)
h,e=np.histogram(C[sel,2],bins=np.arange(C[:,2].min(),C[:,2].max(),0.2),weights=A[sel])
top=np.argsort(h)[::-1][:6]; print('down-facing planes z,area:',[(round(e[i],2),round(h[i],1)) for i in top])
sel2=(N[:,2]>0.98); h2,e2=np.histogram(C[sel2,2],bins=np.arange(C[:,2].min(),C[:,2].max(),0.2),weights=A[sel2])
top=np.argsort(h2)[::-1][:8]; print('up-facing planes z,area:',[(round(e2[i],2),round(h2[i],1)) for i in top])
print('z range', C[:,2].min(), C[:,2].max())
# circle fit on radial-ish faces near disc face
z0=e[np.argmax(h)]
for dz in [0.5,1,2,3,4,5,6,-2,-4,-6,-8,-10]:
    s=(np.abs(N[:,2])<0.2)&(np.abs(C[:,2]-(z0+dz))<0.25)
    P=C[s,:2]
    if len(P)<20: print(dz,'few'); continue
    # kasa
    Am=np.c_[2*P,np.ones(len(P))]; b=(P**2).sum(1); c=np.linalg.lstsq(Am,b,rcond=None)[0]; r=np.sqrt(c[2]+c[0]**2+c[1]**2)
    res=np.linalg.norm(P-c[:2],axis=1)-r
    print('dz',dz,'n',len(P),'c',c[:2].round(3),'r',round(r,3),'rms',round(res.std(),3))
