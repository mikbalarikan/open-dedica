"""Radial wall profile r(z) in theta windows from radial-facing faces (datum frame).
usage: rprofile.py mesh th_lo th_hi z0 z1 dz [rmin rmax]"""
import sys, numpy as np, trimesh
m=trimesh.load(sys.argv[1]); C=m.triangles_center; N=m.face_normals; A=m.area_faces
tl,th_,z0,z1,dz=map(float,sys.argv[2:7]); rmin,rmax=(float(sys.argv[7]),float(sys.argv[8])) if len(sys.argv)>8 else (0,99)
th=np.degrees(np.arctan2(C[:,1],C[:,0]))%360; r=np.hypot(C[:,0],C[:,1])
rh=np.c_[C[:,0]/np.maximum(r,1e-9),C[:,1]/np.maximum(r,1e-9)]; nr=(N[:,:2]*rh).sum(1)
s=(th>=tl%360)&(th<=th_%360) if tl%360<=th_%360 else ((th>=tl%360)|(th<=th_%360))
s&=(nr>0.8)&(r>rmin)&(r<rmax)
for z in np.arange(z0,z1,dz):
    k=s&(C[:,2]>=z)&(C[:,2]<z+dz)
    if k.sum()<3: print(f'z {z:6.2f}  -'); continue
    rr=r[k]; w=A[k]
    print(f'z {z:6.2f} n {k.sum():4d} r p5 {np.percentile(rr,5):6.3f} p50 {np.percentile(rr,50):6.3f} p95 {np.percentile(rr,95):6.3f}')
