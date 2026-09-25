import json, sys, numpy as np, trimesh
m=trimesh.load_mesh(sys.argv[1]); out=sys.argv[2]
C,N,A=m.triangles_center,m.face_normals,m.area_faces
r=np.hypot(C[:,0],C[:,1]); th=np.degrees(np.arctan2(C[:,1],C[:,0]))
R={}
def zlev(mask,up=True):
    k=mask&((N[:,2]>0.95) if up else (N[:,2]<-0.95))
    if k.sum()<5: return None
    return dict(p50=float(np.median(C[k,2])),p10=float(np.percentile(C[k,2],10)),p90=float(np.percentile(C[k,2],90)),area=float(A[k].sum()),n=int(k.sum()))
R['floor_z']=zlev((r>8.8)&(r<9.2)|((np.abs(C[:,0])>9)&(np.abs(C[:,0])<13)&(np.abs(C[:,1])<3)))
R['rim_top_z']=zlev((r>10)&(np.abs(C[:,0])<6)&(C[:,2]>4.5))
R['collar_top_z']=zlev((r>6.5)&(r<7.8)&(C[:,2]>3))
R['tube_top_z']=zlev((r>4.6)&(r<6.1)&(C[:,2]>12))
R['back_face_z']=zlev((r>7)&(r<10.5),up=False)
R['rib_bottom_z']=zlev((np.abs(C[:,0])<1.5)&(np.abs(C[:,1])<3)&(C[:,2]<-20),up=False)
R['tube_bore_floor_z']=zlev((r<4.3)&(C[:,2]>0.5)&(C[:,2]<6))
# ear top face region (inside rim, around the holes) and ear back face
for sgn,nm in ((1,'px'),(-1,'nx')):
    k=(np.abs(C[:,0]-sgn*15.4)<3.3)&(np.abs(C[:,1])<3.3)
    R['ear_floor_z_'+nm]=zlev(k&(C[:,2]>1))
# ear holes: inward-facing (towards hole axis) wall faces z 0.3..1.9
from scipy.optimize import least_squares
for sgn,nm in ((1,'px'),(-1,'nx')):
    k=(np.abs(C[:,0]-sgn*15.4)<2.6)&(np.abs(C[:,1])<2.6)&(C[:,2]>0.3)&(C[:,2]<1.9)&(np.abs(N[:,2])<0.3)
    P=C[k,:2]; 
    def res(x): return np.hypot(P[:,0]-x[0],P[:,1]-x[1])-x[2]
    s=least_squares(res,[sgn*15.4,0,1.9],loss='soft_l1',f_scale=0.1); rr=res(s.x)
    R['ear_hole_'+nm]=dict(cx=float(s.x[0]),cy=float(s.x[1]),r=float(s.x[2]),n=int(k.sum()),rms=float(np.sqrt((rr**2).mean())))
# plate outline from outer wall faces z 2.6..5.0 (outward normals, horizontal)
kw=(C[:,2]>2.6)&(C[:,2]<5.0)&(np.abs(N[:,2])<0.3)&((N[:,0]*C[:,0]+N[:,1]*C[:,1])>0)
P=C[kw]; rP=np.hypot(P[:,0],P[:,1])
kc=(np.abs(P[:,0])<5)&(rP>10.9); R['plate_central_R']=dict(p50=float(np.median(rP[kc])),p10=float(np.percentile(rP[kc],10)),p90=float(np.percentile(rP[kc],90)),n=int(kc.sum()),
   note='outer rim wall, |x|<5, z 2.6-5.0; +Y half p50 %.3f, -Y half p50 %.3f'%(np.median(rP[kc&(P[:,1]>0)]),np.median(rP[kc&(P[:,1]<0)])))
for x0 in (10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5):
    kk=(np.abs(np.abs(P[:,0])-x0)<0.3)&(np.abs(P[:,1])>3)&(np.abs(P[:,1])<8)
    R['ear_halfwidth_x%.1f'%x0]=float(np.median(np.abs(P[kk,1]))) if kk.sum()>5 else None
for sgn,nm in ((1,'px'),(-1,'nx')):
    kk=(P[:,0]*sgn>19)&(np.abs(P[:,1])<1.5); R['ear_tip_x_'+nm]=float(np.median(np.abs(P[kk,0]))) if kk.sum() else None
# rim inner wall (inward normals)
ki=(C[:,2]>2.8)&(C[:,2]<4.8)&(np.abs(N[:,2])<0.3)&((N[:,0]*C[:,0]+N[:,1]*C[:,1])<0)&(r>9)
Pi=C[ki]; rI=np.hypot(Pi[:,0],Pi[:,1]); kc=(np.abs(Pi[:,0])<5)
R['rim_inner_central_R']=dict(p50=float(np.median(rI[kc])),n=int(kc.sum()))
for sgn,nm in ((1,'px'),(-1,'nx')):
    kk=(Pi[:,0]*sgn>17.5)&(np.abs(Pi[:,1])<1.5); R['rim_inner_ear_x_'+nm]=float(np.median(np.abs(Pi[kk,0]))) if kk.sum() else None
for x0 in (12.5,14.5,16.5):
    kk=(np.abs(np.abs(Pi[:,0])-x0)<0.3)&(np.abs(Pi[:,1])>2.5)
    R['rim_inner_halfwidth_x%.1f'%x0]=float(np.median(np.abs(Pi[kk,1]))) if kk.sum()>5 else None
# back-edge round: outline R at z=0.15/0.5/1.0/1.5/2.0 central
for z in (0.1,0.3,0.6,1.0,1.5,2.0):
    s=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z]).reshape(-1,3); rr=np.hypot(s[:,0],s[:,1]); kk=(np.abs(s[:,0])<5)&(rr>10)
    R['outline_R_at_z%.1f'%z]=float(np.median(rr[kk])) if kk.sum() else None
# slots in tube: angular mass at z 10-13, r 4.6-6.3
k=(C[:,2]>9.5)&(C[:,2]<13)&(r>4.7)&(r<6.3)
h,e=np.histogram(th[k],bins=np.arange(-180,181,1),weights=A[k])
R['slot_theta_mass_hist_1deg']=h.round(3).tolist()
# slot side walls: faces with normal tangential, r 4.8-6.1, z 10-13
tang=np.stack([-np.sin(np.radians(th)),np.cos(np.radians(th))],1)
nt=(N[:,:2]*tang).sum(1)
k=(C[:,2]>10)&(C[:,2]<13)&(r>4.8)&(r<6.1)&(np.abs(nt)>0.85)
sw=[]
for c0 in (0,90,180,-90):
    dth=((th-c0+180)%360)-180
    kk=k&(np.abs(dth)<25)
    # half-width = distance of wall faces from the slot mid-plane
    ang=np.radians(c0); nrm=np.array([-np.sin(ang),np.cos(ang)])
    dist=C[kk,:2]@nrm
    sw.append(dict(theta=c0,n=int(kk.sum()),pos=float(np.median(dist[dist>0])) if (dist>0).sum() else None,neg=float(np.median(dist[dist<0])) if (dist<0).sum() else None))
R['slot_walls']=sw
# slot bottom: up-facing faces r 4.6-6.3 z 7-11 near slot centres
for c0 in (0,90,180,-90):
    dth=((th-c0+180)%360)-180
    R['slot_bottom_z_th%d'%c0]=zlev((np.abs(dth)<8)&(r>4.7)&(r<6.2)&(C[:,2]>7)&(C[:,2]<11.5))
# stem: z-levels for cone
for z in np.arange(-8,0.01,0.5):
    kk=(np.abs(C[:,2]-z)<0.15)&(np.abs(N[:,2])<0.9)&(np.abs(np.abs(th)-90)<50)&(r<7.5)&((N[:,0]*C[:,0]+N[:,1]*C[:,1])>0)
    R['stem_r_at_z%.1f'%z]=float(np.median(r[kk])) if kk.sum()>10 else None
# gussets: faces with |N.y|>0.9 , |x| 5..13, z -8..0
for sgn,nm in ((1,'px'),(-1,'nx')):
    kk=(C[:,0]*sgn>6.8)&(C[:,0]*sgn<11)&(C[:,2]<-0.5)&(C[:,2]>-6)&(np.abs(N[:,1])>0.9)
    y=C[kk,1]; R['gusset_y_'+nm]=dict(pos=float(np.median(y[N[kk,1]>0])) if (N[kk,1]>0).sum() else None,neg=float(np.median(y[N[kk,1]<0])) if (N[kk,1]<0).sum() else None,n=int(kk.sum()))
    # hypotenuse: faces with normal in xz plane pointing down-outwards
    kk=(C[:,0]*sgn>5)&(C[:,0]*sgn<13)&(C[:,2]<-0.3)&(np.abs(C[:,1])<1.5)&(np.abs(N[:,1])<0.4)&(N[:,2]<-0.3)&(N[:,0]*sgn>0.3)
    if kk.sum()>10:
        xs=np.abs(C[kk,0]); zs=C[kk,2]; a,b=np.polyfit(xs,zs,1)
        R['gusset_edge_'+nm]=dict(slope=float(a),z_at_x0=float(b),x_at_z0=float(-b/a),n=int(kk.sum()),deg=float(np.degrees(np.arctan(-a))))
# rib under junction
kk=(C[:,2]<-19.5)&(C[:,2]>-23.4)&(np.abs(C[:,1])<2.5)&(np.abs(N[:,0])>0.9)
R['rib_x']=dict(pos=float(np.median(C[kk&(N[:,0]>0),0])) if (kk&(N[:,0]>0)).sum() else None,neg=float(np.median(C[kk&(N[:,0]<0),0])) if (kk&(N[:,0]<0)).sum() else None,n=int(kk.sum()))
json.dump(R,open(out,'w'),indent=1)
for k,v in R.items():
    if k!='slot_theta_mass_hist_1deg': print(k, json.dumps(v)[:200])
h=np.array(R['slot_theta_mass_hist_1deg']); print('slot low-mass bins (deg):',[int(e[i]) for i in np.where(h<0.15*np.median(h))[0]])
