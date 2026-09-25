"""render2.py mesh out.png view(+Z/-Z/...) [xlim ylim] - one big shaded view"""
import sys, numpy as np, trimesh, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
m = trimesh.load_mesh(sys.argv[1])
dirs={"+X":[1,0,0],"-X":[-1,0,0],"+Y":[0,1,0],"-Y":[0,-1,0],"+Z":[0,0,1],"-Z":[0,0,-1],"iso1":[1,-1,1],"iso2":[-1,1,1],"iso3":[1,1,-1],"iso4":[-1,-1,-1],"iso5":[1,1,1],"iso6":[-1,-1,1]}
names=sys.argv[3].split(",")
fig,axs=plt.subplots(1,len(names),figsize=(16*len(names),16))
axs=np.atleast_1d(axs)
for ax,nm in zip(axs,names):
    d=np.array(dirs[nm],float); d/=np.linalg.norm(d)
    up=np.array([0,0,1.0]) if abs(d[2])<0.9 else np.array([0,1.0,0])
    x=np.cross(up,d); x/=np.linalg.norm(x); y=np.cross(d,x)
    V=m.vertices; P=np.c_[V@x,V@y]; depth=V@d
    fn=m.face_normals; vis=fn@d>0; F=m.faces[vis]
    sh=np.clip(fn[vis]@(d*0.7+y*0.5+x*0.3),0.05,1)
    o=np.argsort(depth[F].mean(1))
    ax.add_collection(PolyCollection(P[F[o]],facecolors=plt.cm.gray(0.1+0.85*sh[o]),edgecolors="none"))
    ax.autoscale(); ax.set_aspect("equal"); ax.set_title(nm); ax.grid(alpha=.35)
    xl=ax.get_xlim(); yl=ax.get_ylim(); ax.set_xticks(np.arange(np.floor(xl[0]),xl[1],2)); ax.set_yticks(np.arange(np.floor(yl[0]),yl[1],2)); ax.tick_params(labelsize=7)
plt.tight_layout(); plt.savefig(sys.argv[2],dpi=int(sys.argv[4]) if len(sys.argv)>4 else 50)
