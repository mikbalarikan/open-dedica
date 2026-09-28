import sys,trimesh,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
m=trimesh.load(sys.argv[1]); out=sys.argv[2]
specs=eval(sys.argv[3])  # list of (normal, origin, axes idx, title)
n=len(specs); cols=min(n,3); rows=(n+cols-1)//cols
fig,axs=plt.subplots(rows,cols,figsize=(7*cols,5*rows)); axs=np.atleast_1d(axs).ravel()
for ax,(nrm,org,(i,j)) in zip(axs,specs):
    s=m.section(plane_normal=nrm,plane_origin=org)
    if s is not None:
        for e in s.entities:
            p=s.vertices[e.points]; ax.plot(p[:,i],p[:,j],'k-',lw=0.6)
    ax.set_aspect('equal');ax.grid(True,lw=0.3);ax.set_title(f'n={nrm} o={org}')
    ax.minorticks_on();ax.grid(True,which='minor',lw=0.1)
plt.tight_layout();plt.savefig(out,dpi=80)
