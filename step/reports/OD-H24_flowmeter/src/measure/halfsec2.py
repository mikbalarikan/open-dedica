import trimesh, numpy as np, matplotlib, sys
matplotlib.use("Agg"); import matplotlib.pyplot as plt
m = trimesh.load_mesh("aligned.ply")
angs=[float(a) for a in sys.argv[2].split(",")]
nc=4; nr=(len(angs)+nc-1)//nc
fig,axs=plt.subplots(nr,nc,figsize=(10*nc,10*nr))
for ax,th in zip(np.array(axs).flat,angs):
    t=np.radians(th); U=np.array([np.cos(t),np.sin(t),0]); N=np.array([-np.sin(t),np.cos(t),0])
    for seg in trimesh.intersections.mesh_plane(m,N,[0,0,0]):
        u=seg@U
        if u.min()<-0.3: continue
        ax.plot(u,seg[:,2],"k-",lw=0.7)
    ax.set_aspect("equal"); ax.set_xlim(-0.5,24); ax.set_ylim(-1,26); ax.grid(alpha=.4); ax.set_xticks(range(0,24,1)); ax.set_yticks(range(-1,26,1)); ax.tick_params(labelsize=6); ax.set_title("theta=%g"%th)
plt.tight_layout(); plt.savefig(sys.argv[1],dpi=45)
