"""Overlay several z-sections in one plot. usage: sec_overlay.py out.png lim z1 z2 ..."""
import sys, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
m=trimesh.load('intake/aligned_work.stl'); out=sys.argv[1]; L=float(sys.argv[2]); zs=[float(z) for z in sys.argv[3:]]
fig,ax=plt.subplots(figsize=(13,13)); cols=plt.cm.tab10(np.linspace(0,1,10))
for i,z in enumerate(zs):
    seg=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z])
    ax.add_collection(LineCollection(seg[:,:,:2],lw=0.9,color=cols[i%10],label=f'z={z}'))
ax.set_xlim(-L,L); ax.set_ylim(-L,L); ax.set_aspect('equal'); ax.minorticks_on(); ax.grid(alpha=.5); ax.grid(which='minor',alpha=.2); ax.legend()
th=np.linspace(0,2*np.pi,400)
for r in [8.6,12.6,14.36]: ax.plot(r*np.cos(th),r*np.sin(th),'k:',lw=0.5)
plt.tight_layout(); plt.savefig(out,dpi=70)
