import json,sys,numpy as np, trimesh
from scipy.optimize import least_squares
m=trimesh.load_mesh(sys.argv[1]); P=json.load(open(sys.argv[2])); out=sys.argv[3]
C,N,A=m.triangles_center,m.face_normals,m.area_faces
R={}
# concave outline corner: outer wall faces z 2.6-5.0 in corner windows
kw=(C[:,2]>2.6)&(C[:,2]<5.0)&(np.abs(N[:,2])<0.3)
for sx in (1,-1):
    for sy in (1,-1):
        k=kw&(C[:,0]*sx>8.3)&(C[:,0]*sx<10.6)&(C[:,1]*sy>6.0)&(C[:,1]*sy<8.8)
        Q=C[k,:2]
        def res(x): return np.hypot(Q[:,0]-x[0],Q[:,1]-x[1])-x[2]
        s=least_squares(res,[sx*11.0,sy*8.5,1.5],loss='soft_l1',f_scale=0.05); rr=res(s.x)
        R['outline_corner_%+d%+d'%(sx,sy)]=dict(cx=float(s.x[0]),cy=float(s.x[1]),r=float(abs(s.x[2])),n=int(k.sum()),rms=float(np.sqrt((rr**2).mean())))
# back-edge round from outline inset vs z (central |x|<5)
zs=[];ins=[]
Rw=11.697
for z in np.arange(0.05,1.9,0.1):
    s=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z]).reshape(-1,3); rr=np.hypot(s[:,0],s[:,1]); kk=(np.abs(s[:,0])<5)&(rr>9.5)
    zs.append(z); ins.append(Rw-np.median(rr[kk]))
zs=np.array(zs); ins=np.array(ins)
def res(x):
    Rf=x[0]; zz=np.clip(zs,0,Rf); return (Rf-np.sqrt(np.maximum(Rf**2-(Rf-zz)**2,0)))-ins
s=least_squares(res,[1.5]); rr=res(s.x)
R['back_edge_round']=dict(R=float(s.x[0]),rms=float(np.sqrt((rr**2).mean())),z=zs.round(2).tolist(),inset=np.round(ins,3).tolist())
# port bore step
for nm in ('port_pY','port_nY'):
    p=np.array(P[nm]['axis_point_at_y0']); d=np.array(P[nm]['axis_dir'])
    q=C-p; t=q@d; w=q-np.outer(t,d); r=np.linalg.norm(w,axis=1); nr=(N*w).sum(1)/np.maximum(r,1e-9)
    k=(nr<-0.7)&(np.abs(N@d)<0.4)&(r<4.8)&(r>3.0)
    prof=[]
    for tt in np.arange(11,20.2,0.5):
        kk=k&(np.abs(t-tt)<0.25)
        prof.append([float(tt),float(np.median(r[kk])) if kk.sum()>5 else None,int(kk.sum())])
    R[nm+'_bore_profile']=prof
    kf=(N@d>0.8)&(r<4.3)&(r>3.2)&(t>13)&(t<19)   # step face (facing the port mouth)
    R[nm+'_bore_step_t']=dict(p50=float(np.median(t[kf])),n=int(kf.sum())) if kf.sum()>5 else None
json.dump(R,open(out,'w'),indent=1)
for k,v in R.items(): print(k,json.dumps(v)[:400])
