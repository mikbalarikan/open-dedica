import trimesh, numpy as np, matplotlib, sys
matplotlib.use("Agg"); import matplotlib.pyplot as plt
m=trimesh.load_mesh("aligned.ply")
v,_=trimesh.sample.sample_surface(m,4000000,seed=1)
res=0.2; x0,y0=-22,-38
ix=((v[:,0]-x0)/res).astype(int); iy=((v[:,1]-y0)/res).astype(int)
W,H=int(44/res),int(60/res)
ok=(ix>=0)&(ix<W)&(iy>=0)&(iy<H)
zmax=np.full((H,W),np.nan); zmin=np.full((H,W),np.nan)
lin=iy[ok]*W+ix[ok]
a=np.full(H*W,-1e9); np.maximum.at(a,lin,v[ok,2]); a[a<-1e8]=np.nan; zmax=a.reshape(H,W)
b=np.full(H*W,1e9); np.minimum.at(b,lin,v[ok,2]); b[b>1e8]=np.nan; zmin=b.reshape(H,W)
np.save("zmax.npy",zmax); np.save("zmin.npy",zmin)
fig,axs=plt.subplots(1,2,figsize=(36,26))
ext=[x0,x0+44,y0,y0+60]
im=axs[0].imshow(zmax,origin="lower",extent=ext,cmap="nipy_spectral",vmin=12,vmax=25); plt.colorbar(im,ax=axs[0],shrink=0.5); axs[0].set_title("top z-max")
im=axs[1].imshow(zmin,origin="lower",extent=ext,cmap="nipy_spectral",vmin=-1,vmax=16); plt.colorbar(im,ax=axs[1],shrink=0.5); axs[1].set_title("bottom z-min (viewed from TOP, not mirrored)")
for ax in axs: ax.set_xticks(range(-22,23,1)); ax.set_yticks(range(-38,23,1)); ax.grid(alpha=.35,color="w"); ax.tick_params(labelsize=7)
plt.tight_layout(); plt.savefig("hmap.png",dpi=40)
