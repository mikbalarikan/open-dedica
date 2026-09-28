"""Unwrapped outer-radius map r_max(theta, z) from centre-out rays on z-sections. usage: unwrap.py out.png z0 z1 dz rmax"""
import sys, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
m=trimesh.load('intake/aligned_work.stl'); out=sys.argv[1]; z0,z1,dz,rmax=map(float,sys.argv[2:6])
zs=np.arange(z0,z1,dz); th=np.arange(0,360,1.0); M=np.full((len(zs),len(th)),np.nan)
for i,z in enumerate(zs):
    seg=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z])
    if len(seg)==0: continue
    P=seg.reshape(-1,3)[:,:2]; mid=seg.mean(1)[:,:2]
    # densify segments
    t=np.linspace(0,1,6)[:,None,None]; Q=(seg[None,:,0,:2]*(1-t)+seg[None,:,1,:2]*t).reshape(-1,2)
    rr=np.hypot(*Q.T); tt=np.degrees(np.arctan2(Q[:,1],Q[:,0]))%360
    k=rr<rmax; rr,tt=rr[k],tt[k]; b=np.floor(tt).astype(int)
    for j in range(360):
        s=b==j
        if s.any(): M[i,j]=rr[s].max()
np.save(out.replace('.png','.npy'),M)
fig,ax=plt.subplots(figsize=(18,7)); im=ax.imshow(M,origin='lower',aspect='auto',extent=[0,360,z0,z1],cmap='turbo')
fig.colorbar(im); ax.set_xlabel('theta deg'); ax.set_ylabel('z'); ax.set_xticks(range(0,361,15)); ax.grid(alpha=.4)
plt.tight_layout(); plt.savefig(out,dpi=70)
