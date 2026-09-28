import numpy as np, trimesh, sys, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
m=trimesh.load(sys.argv[1]); axis=sys.argv[2]; vals=[float(v) for v in sys.argv[3].split(',')]; out=sys.argv[4]
lim=[float(v) for v in sys.argv[5].split(',')] if len(sys.argv)>5 else None
idx={'x':0,'y':1,'z':2}[axis]; nrm=np.zeros(3); nrm[idx]=1
other=[i for i in range(3) if i!=idx]
n=len(vals); cols=min(n,4); rows=(n+cols-1)//cols
fig,axs=plt.subplots(rows,cols,figsize=(5.5*cols,5*rows)); axs=np.atleast_1d(axs).ravel()
for ax,v in zip(axs,vals):
    o=np.zeros(3); o[idx]=v
    s=m.section(plane_origin=o,plane_normal=nrm)
    if s is not None:
        for e in s.entities:
            p=s.vertices[e.points]; ax.plot(p[:,other[0]],p[:,other[1]],'k-',lw=0.6)
    ax.set_aspect('equal'); ax.grid(alpha=.4); ax.set_title(f'{axis}={v}'); ax.set_xlabel('xyz'[other[0]]); ax.set_ylabel('xyz'[other[1]])
    if lim: ax.set_xlim(lim[0],lim[1]); ax.set_ylim(lim[2],lim[3])
    ax.minorticks_on(); ax.grid(which='minor',alpha=.15)
fig.tight_layout(); fig.savefig(out,dpi=80)
