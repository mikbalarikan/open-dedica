# exploratory probes on the aligned working copy (datum frame); prints compact summaries only
import trimesh,numpy as np,sys,json
m=trimesh.load('intake/aligned_work.stl')
c=m.triangles_center;n=m.face_normals;A=m.area_faces
r=np.hypot(c[:,0],c[:,1]);th=np.degrees(np.arctan2(c[:,1],c[:,0]))
def zlev(sel,up,label):
  k=sel&((n[:,2]>0.95) if up else (n[:,2]<-0.95))
  if k.sum()<20: print(label,'few',k.sum());return
  z=c[k,2];w=A[k];o=np.argsort(z);cw=np.cumsum(w[o])/w.sum()
  print(f'{label}: n={k.sum()} area={w.sum():.1f} z50={z[o][np.searchsorted(cw,.5)]:.3f} z05={z[o][np.searchsorted(cw,.05)]:.3f} z95={z[o][np.searchsorted(cw,.95)]:.3f}')
def rlev(sel,out,label):
  rd=(n[:,0]*c[:,0]+n[:,1]*c[:,1])/np.maximum(r,1e-9)
  k=sel&(abs(n[:,2])<0.3)&((rd>0.9) if out else (rd<-0.9))
  if k.sum()<20: print(label,'few',k.sum());return
  rr=r[k];w=A[k];o=np.argsort(rr);cw=np.cumsum(w[o])/w.sum()
  print(f'{label}: n={k.sum()} area={w.sum():.1f} r50={rr[o][np.searchsorted(cw,.5)]:.3f} r05={rr[o][np.searchsorted(cw,.05)]:.3f} r95={rr[o][np.searchsorted(cw,.95)]:.3f}')
B=lambda a,b,x: (x>a)&(x<b)
exec(open(sys.argv[1]).read())
