import sys,trimesh,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
m=trimesh.load(sys.argv[1]); out=sys.argv[2]
specs=eval(sys.argv[3]); lim=eval(sys.argv[4]) if len(sys.argv)>4 else None
n=len(specs); cols=min(n,3); rows=(n+cols-1)//cols
fig,axs=plt.subplots(rows,cols,figsize=(6*cols,5*rows)); axs=np.atleast_1d(axs).ravel()
for ax,(nrm,org,(i,j)) in zip(axs,specs):
    s=m.section(plane_normal=nrm,plane_origin=org)
    if s is not None:
        for e in s.entities:
            p=s.vertices[e.points]; ax.plot(p[:,i],p[:,j],'k-',lw=0.7)
    ax.set_aspect('equal');ax.set_title(f'n={nrm} o={org}')
    if lim: ax.set_xlim(*lim[0]);ax.set_ylim(*lim[1])
    ax.minorticks_on();ax.grid(True,which='major',lw=0.4);ax.grid(True,which='minor',lw=0.15)
plt.tight_layout();plt.savefig(out,dpi=75)
