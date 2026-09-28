"""Spline tooth pitch on a partial arc (the D-flat and key interrupt the circle).
For each z station: outer radius per ray (0.25 deg) over theta in [lo,hi], then least-squares
fit r(theta)=a+b cos(k theta)+c sin(k theta) for k=12..60; report the residual per k."""
import sys, json, numpy as np, trimesh
m=trimesh.load('intake/aligned_work.stl')
out={}
for z in [-12,-10,-8,-6,-4,-2]:
    seg=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z]); P=seg.reshape(-1,3)[:,:2]
    P=P[np.hypot(*P.T)<4.5]
    th=np.degrees(np.arctan2(P[:,1],P[:,0]))%360; r=np.hypot(*P.T)
    bins=np.arange(45,315,0.5); rb=[]
    for b in bins:
        k=np.abs(th-b)<0.5
        rb.append(r[k].max() if k.any() else np.nan)
    rb=np.array(rb); ok=~np.isnan(rb); t=np.radians(bins[ok]); y=rb[ok]
    res={}
    for k in range(12,61):
        A=np.c_[np.ones_like(t),np.cos(k*t),np.sin(k*t),t]
        c,*_=np.linalg.lstsq(A,y,rcond=None); res[k]=float(np.sqrt(np.mean((A@c-y)**2)))
    best=sorted(res,key=res.get)[:4]
    out[z]={'best':best,'rms':[round(res[b],4) for b in best],'r_p95':float(np.percentile(y,95)),'r_p5':float(np.percentile(y,5)),'r_med':float(np.median(y))}
    print(z,out[z])
json.dump(out,open('measure/figures/spline_pitch.json','w'),indent=1)
