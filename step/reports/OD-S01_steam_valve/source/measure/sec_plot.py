"""Plot planar sections of a mesh as raw segments. usage: sections.py mesh out.png axis v1 v2 ... [--lim a b c d]"""
import sys, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
args=sys.argv[1:]; lim=None
if '--lim' in args:
    i=args.index('--lim'); lim=[float(v) for v in args[i+1:i+5]]; args=args[:i]+args[i+5:]
m=trimesh.load(args[0]); out=args[1]; ax_=args[2]; vals=[float(v) for v in args[3:]]
k='xyz'.index(ax_); nrm=np.eye(3)[k]; other=[i for i in range(3) if i!=k]
nc=min(4,len(vals)); nr=int(np.ceil(len(vals)/nc))
fig,axs=plt.subplots(nr,nc,figsize=(5*nc,5*nr),squeeze=False)
for a,v in zip(axs.flat,vals):
    seg=trimesh.intersections.mesh_plane(m,nrm,nrm*v)
    if len(seg): a.add_collection(LineCollection(seg[:,:,other],lw=0.6,color='k'))
    a.autoscale(); a.set_title(f'{ax_}={v}'); a.set_aspect('equal'); a.set_xlabel('xyz'[other[0]]); a.set_ylabel('xyz'[other[1]])
    if lim: a.set_xlim(lim[0],lim[1]); a.set_ylim(lim[2],lim[3])
    a.minorticks_on(); a.grid(alpha=.4); a.grid(which='minor',alpha=.15)
plt.tight_layout(); plt.savefig(out,dpi=70)
