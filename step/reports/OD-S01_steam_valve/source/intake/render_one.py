"""Render one shaded view at higher resolution. usage: render_one.py mesh out.png dx dy dz [--clip axis lo hi]"""
import sys, numpy as np, trimesh, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
a=sys.argv[1:]; clip=None
if '--clip' in a:
    i=a.index('--clip'); clip=(a[i+1],float(a[i+2]),float(a[i+3])); a=a[:i]+a[i+4:]
m=trimesh.load(a[0]); out=a[1]; d=np.array([float(v) for v in a[2:5]]); d/=np.linalg.norm(d)
V=m.vertices; F=m.faces; N=m.face_normals; C=m.triangles_center
keep=np.ones(len(F),bool)
if clip:
    k='xyz'.index(clip[0]); keep=(C[:,k]>=clip[1])&(C[:,k]<=clip[2])
F=F[keep]; N=N[keep]; C=C[keep]
up=np.array([0,0,1.]) if abs(d[2])<0.9 else np.array([0,1.,0])
u=np.cross(up,d); u/=np.linalg.norm(u); v=np.cross(d,u)
o=np.argsort(C@d); sh=np.clip(N@d,0,1)[o]; tri=V[F[o]]
fig,ax=plt.subplots(figsize=(12,12))
ax.add_collection(PolyCollection(np.stack([tri@u,tri@v],-1),facecolors=plt.cm.gray(0.1+0.85*sh),edgecolors='none'))
ax.autoscale(); ax.set_aspect('equal'); ax.minorticks_on(); ax.grid(alpha=.5); ax.grid(which='minor',alpha=.2)
ax.set_title(f"view from {d.round(2)}  u={u.round(2)} v={v.round(2)}" + (f" clip {clip}" if clip else ""))
plt.tight_layout(); plt.savefig(out,dpi=75)
