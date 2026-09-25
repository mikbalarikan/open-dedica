import trimesh, numpy as np, matplotlib, sys
matplotlib.use("Agg"); import matplotlib.pyplot as plt
m=trimesh.load_mesh("aligned.ply")
v,_=trimesh.sample.sample_surface(m,3000000,seed=3)
r=np.hypot(v[:,0],v[:,1]); th=np.degrees(np.arctan2(v[:,1],v[:,0]))%360
secs=[(float(a),float(b)) for a,b in (s.split(":") for s in sys.argv[2].split(","))]
lim=[float(a) for a in sys.argv[3].split(",")]
fig,axs=plt.subplots(1,len(secs),figsize=(12*len(secs),12*(lim[3]-lim[2])/(lim[1]-lim[0])+1))
for ax,(a,b) in zip(np.atleast_1d(axs),secs):
    s=((th-a)%360)<((b-a)%360)
    ax.hist2d(r[s],v[s,2],bins=[np.arange(lim[0],lim[1],0.05),np.arange(lim[2],lim[3],0.05)],cmap="gray_r",vmax=8)
    ax.set_aspect("equal"); ax.set_xticks(np.arange(lim[0],lim[1],0.5)); ax.set_yticks(np.arange(lim[2],lim[3],0.5)); ax.grid(alpha=.5)
    for t in ax.get_xticklabels()[1::2]+ax.get_yticklabels()[1::2]: t.set_visible(False)
    ax.tick_params(labelsize=13); ax.set_title("theta %g..%g"%(a,b),fontsize=18)
plt.tight_layout(); plt.savefig(sys.argv[1],dpi=40)
