"""Port measurements on the full-res scan in the frozen datum frame (scratch copy of the estimator
also saved to measure/figures). Axis: robust (soft-L1) cylinder fit to outward sleeve faces."""
import json, sys, numpy as np, trimesh
from scipy.optimize import least_squares
m=trimesh.load_mesh(sys.argv[1]); out=sys.argv[2]
C,N,A=m.triangles_center,m.face_normals,m.area_faces
def frame(p,d):
    e1=np.array([1.,0,0]); e1=e1-d*(e1@d); e1/=np.linalg.norm(e1); e2=np.cross(d,e1); return e1,e2
def coords(p,d):
    e1,e2=frame(p,d); q=C-p; t=q@d; u=q@e1; v=q@e2; r=np.hypot(u,v)
    nr=(N@e1*u+N@e2*v)/np.maximum(r,1e-9); return t,u,v,r,nr
def cylfit(p,d,tlo,thi,rlo,rhi):
    for _ in range(3):
        t,u,v,r,nr=coords(p,d)
        sel=(t>tlo)&(t<thi)&(r>rlo)&(r<rhi)&(np.abs(N@d)<0.25)&(nr>0.8)
        P=C[sel]
        def res(x):
            dd=x[3:6]/np.linalg.norm(x[3:6]); q=P-x[:3]; w=q-np.outer(q@dd,dd); return np.linalg.norm(w,axis=1)-x[6]
        s=least_squares(res,np.r_[p,d,np.median(r[sel])],loss='soft_l1',f_scale=0.1)
        d2=s.x[3:6]/np.linalg.norm(s.x[3:6]); p2=s.x[:3]
        p=p2+((p-p2)@d2)*d2; d=d2
    rr=res(s.x)
    return p,d,float(s.x[6]),dict(n=int(sel.sum()),rms=float(np.sqrt((rr**2).mean())),p95=float(np.percentile(np.abs(rr),95)))
R={}
for side,name in ((1,'port_pY'),(-1,'port_nY')):
    d=np.array([0,side*np.cos(np.radians(34.5)),-np.sin(np.radians(34.5))]); p=np.array([0,0,-14.4])
    p,d,Rs,st=cylfit(p,d,8.5,14.0,5.0,6.6)
    # re-reference p to the plane x... take point on axis with y=0
    s=-p[1]/d[1]; p=p+s*d
    t,u,v,r,nr=coords(p,d)
    rec={'axis_point_at_y0':p.tolist(),'axis_dir':d.tolist(),'elev_deg':float(np.degrees(np.arcsin(-d[2]))),
         'azimuth_x_offset_deg':float(np.degrees(np.arcsin(d[0]))),'sleeve_fit':{'R':Rs,**st}}
    out_=(nr>0.8)&(np.abs(N@d)<0.3)
    def band(tl,th,extra=None):
        k=out_&(t>tl)&(t<th)
        if extra is not None: k&=extra
        return r[k]
    rn=band(3.5,6.2,(v<2.5)); rec['neck_R_p50']=float(np.median(rn)); rec['neck_R_p10_p90']=np.percentile(rn,[10,90]).tolist()
    rs=band(8.5,14.5,(np.abs(u)<4.5)|(v>-4)); rec['sleeve_R_p50']=float(np.median(rs))
    # sleeve start: first t where median outer r of v<2 faces exceeds (neck+sleeve)/2
    mid=(rec['neck_R_p50']+rec['sleeve_R_p50'])/2
    ts=np.arange(5,10,0.05); prof=[np.median(r[out_&(np.abs(t-x)<0.1)&(v<0)]) if (out_&(np.abs(t-x)<0.1)&(v<0)).sum()>5 else np.nan for x in ts]
    rec['t_sleeve_start']=float(ts[np.nanargmax(np.array(prof)>mid)])
    # block: faces with |N.d|<0.3 and |u|>5.5 (side faces, normal ~ +/-e1)
    e1,e2=frame(p,d)
    ksu=(np.abs(N@e1)>0.9)&(t>15.6)&(t<19.0)&(np.abs(u)>5); rec['block_half_u_p50']=float(np.median(np.abs(u[ksu])))
    ksv=(np.abs(N@e2)>0.9)&(t>15.6)&(t<19.0)&(np.abs(v)>5)&(np.abs(u)>2.5); rec['block_half_v_p50']=float(np.median(np.abs(v[ksv])))
    # block axial faces: faces with N.d ~ -1 at t 14.5-15.6 (start) and N.d ~ +1 at 18.8-19.8 (end, outside lip)
    kst=(N@d<-0.9)&(t>14.3)&(t<15.8)&(r>6.3); rec['t_block_start_p50']=float(np.median(t[kst])) if kst.sum() else None
    ket=(N@d>0.9)&(t>18.5)&(t<19.9)&(r>6.5); rec['t_block_end_p50']=float(np.median(t[ket])) if ket.sum() else None
    kend=(N@d>0.9)&(t>19.5)&(r<6.0)&(r>4.4); rec['t_end_p50']=float(np.median(t[kend])); rec['t_end_n']=int(kend.sum())
    kl=out_&(t>rec['t_block_end_p50']+0.15)&(t<rec['t_end_p50']-0.2)&(r<6.6); rec['lip_R_p50']=float(np.median(r[kl])) if kl.sum() else None
    kb=(nr<-0.8)&(np.abs(N@d)<0.3)&(t>17.8)&(t<rec['t_end_p50']-0.3)&(r<5); rec['bore_r_p50']=float(np.median(r[kb])); rec['bore_r_n']=int(kb.sum())
    kb2=(nr<-0.8)&(np.abs(N@d)<0.3)&(t>12.5)&(t<15.5)&(r<5); rec['bore_inner_r_p50']=float(np.median(r[kb2])) if kb2.sum()>20 else None; rec['bore_inner_n']=int(kb2.sum())
    kbt=(nr<-0.8)&(np.abs(N@d)<0.3)&(r<5); rec['bore_visible_t_min']=float(np.percentile(t[kbt],1))
    # clip slot: faces on block side region with normal ~ +/-d (slot walls) inside |u|>4.6, 1<|v|<5
    kw=(np.abs(N@d)>0.85)&(np.abs(u)>4.8)&(np.abs(v)>1.0)&(np.abs(v)<5.0)&(t>15.8)&(t<18.2)
    tw=t[kw]; lo=tw[N[kw]@d>0]; hi=tw[N[kw]@d<0]
    rec['slot_wall_t_lo_p50']=float(np.median(lo)) if len(lo) else None; rec['slot_wall_t_hi_p50']=float(np.median(hi)) if len(hi) else None
    ke=(np.abs(N@e2)>0.85)&(np.abs(u)>4.8)&(t>16.2)&(t<17.8)&(np.abs(v)<5.2)
    vv=np.abs(v[ke]); rec['slot_v_ends_hist']=np.histogram(vv,bins=np.arange(0,5.4,0.2))[0].tolist()
    rec['slot_v_inner_p50']=float(np.median(vv[vv<2.5])) if (vv<2.5).sum() else None
    rec['slot_v_outer_p50']=float(np.median(vv[(vv>3)&(vv<5.0)])) if ((vv>3)&(vv<5.0)).sum() else None
    R[name]=rec
    print(name,json.dumps({k:(round(x,3) if isinstance(x,float) else x) for k,x in rec.items()}))
json.dump(R,open(out,'w'),indent=1)
