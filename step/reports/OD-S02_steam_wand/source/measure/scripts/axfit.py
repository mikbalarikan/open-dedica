import numpy as np
from scipy.optimize import least_squares
def frame(d):
    d=d/np.linalg.norm(d); a=np.array([1,0,0]) if abs(d[0])<0.9 else np.array([0,1,0])
    u=np.cross(d,a); u/=np.linalg.norm(u); v=np.cross(d,u); return u,v,d
def kasa(xy):
    A=np.c_[2*xy,np.ones(len(xy))]; b=(xy**2).sum(1); s=np.linalg.lstsq(A,b,rcond=None)[0]
    r=np.sqrt(s[2]+s[0]**2+s[1]**2); return s[:2],r
def fit_axis(P, p0, d0, zranges, iters=5, halfw=0.25):
    """P: points; zranges: list of (lo,hi) station ranges along axis (relative to p0); per-station Kasa circle, line fit thru centers"""
    p,d=np.array(p0,float),np.array(d0,float)/np.linalg.norm(d0)
    for _ in range(iters):
        u,v,d=frame(d); q=P-p; t=q@d; x=q@u; y=q@v
        cs=[]
        for lo,hi in zranges:
            for z in np.arange(lo,hi+1e-9,0.5):
                s=np.abs(t-z)<halfw
                if s.sum()<30: continue
                c,r=kasa(np.c_[x[s],y[s]]); res=np.hypot(x[s]-c[0],y[s]-c[1])-r
                cs.append((z,c[0],c[1],r,np.sqrt((res**2).mean())))
        cs=np.array(cs); A=np.c_[np.ones(len(cs)),cs[:,0]]
        ax_=np.linalg.lstsq(A,cs[:,1],rcond=None)[0]; ay_=np.linalg.lstsq(A,cs[:,2],rcond=None)[0]
        p=p+ax_[0]*u+ay_[0]*v; d=d+ax_[1]*u+ay_[1]*v; d/=np.linalg.norm(d)
    return p,d,cs
