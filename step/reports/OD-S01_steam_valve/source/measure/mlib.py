"""Measurement helpers for OD-S01 (datum frame, intake/aligned_work.stl). Builder-side measurement only."""
import numpy as np, trimesh, json
_M=None
def mesh():
    global _M
    if _M is None: _M=trimesh.load('intake/aligned_work.stl')
    return _M
def kasa(P):
    A=np.c_[2*P,np.ones(len(P))]; b=(P**2).sum(1); c=np.linalg.lstsq(A,b,rcond=None)[0]
    r=np.sqrt(c[2]+c[0]**2+c[1]**2); res=np.linalg.norm(P-c[:2],axis=1)-r
    return dict(c=c[:2].tolist(), r=float(r), rms=float(res.std()), max=float(np.abs(res).max()), n=int(len(P)))
def irls(P,scale=0.3,it=20):
    w=np.ones(len(P))
    for _ in range(it):
        A=np.c_[2*P,np.ones(len(P))]*np.sqrt(w)[:,None]; b=(P**2).sum(1)*np.sqrt(w)
        c=np.linalg.lstsq(A,b,rcond=None)[0]; r=np.sqrt(c[2]+c[0]**2+c[1]**2)
        res=np.linalg.norm(P-c[:2],axis=1)-r; w=1/(1+(res/scale)**2)
    return dict(c=c[:2].tolist(), r=float(r), rms=float(np.sqrt(np.average(res**2,weights=w))), n=int(len(P)), p_in=float((np.abs(res)<scale).mean()))
def cyl_fit(axis, center, rng, rwin, wall='outer', perp=0.3, method='irls'):
    """axis 'x'|'y'|'z'; center (2 coords in the other axes order); rng along axis; rwin (rlo,rhi) about center.
    wall outer: normals point away from axis; inner: toward axis."""
    m=mesh(); C=m.triangles_center; N=m.face_normals
    k='xyz'.index(axis); o=[i for i in range(3) if i!=k]
    d=C[:,o]-np.asarray(center); rr=np.linalg.norm(d,axis=1)
    nd=(N[:,o]*d).sum(1)/np.maximum(rr,1e-9)
    s=(np.abs(N[:,k])<perp)&(C[:,k]>rng[0])&(C[:,k]<rng[1])&(rr>rwin[0])&(rr<rwin[1])
    s&=(nd>0.5) if wall=='outer' else (nd<-0.5)
    P=C[s][:,o]
    f=irls(P) if method=='irls' else kasa(P)
    f['axis']=axis; f['range']=list(rng); f['wall']=wall
    return f
def plane_pos(normal_axis, sign, box, pct=50):
    """position along axis of faces whose normal is ~sign*axis inside box {x:(lo,hi),...}"""
    m=mesh(); C=m.triangles_center; N=m.face_normals; A=m.area_faces
    k='xyz'.index(normal_axis); s=(N[:,k]*sign>0.95)
    for a,(lo,hi) in box.items():
        j='xyz'.index(a); s&=(C[:,j]>lo)&(C[:,j]<hi)
    v=C[s,k]
    if len(v)<3: return None
    return dict(p50=float(np.percentile(v,50)),p5=float(np.percentile(v,5)),p95=float(np.percentile(v,95)),n=int(s.sum()),area=float(A[s].sum()))
