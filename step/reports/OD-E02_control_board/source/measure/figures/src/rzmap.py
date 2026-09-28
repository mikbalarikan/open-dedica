import numpy as np, trimesh, sys, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
m=trimesh.load(sys.argv[1]); out=sys.argv[2]
cents={'B1':(-26.6,-4.8),'B2':(0.0,0.0),'B3':(26.5,-5.2)}
v,_=trimesh.sample.sample_surface(m,400000,seed=0)
fig,axs=plt.subplots(3,4,figsize=(22,15))
for i,(k,c) in enumerate(cents.items()):
    q=v[:,:2]-c; r=np.hypot(*q.T); th=np.degrees(np.arctan2(q[:,1],q[:,0]))
    for j,(lo,hi) in enumerate([(-45,45),(45,135),(135,225),(-135,-45)]):
        if lo<180<hi: s=(th>lo)|(th<hi-360)
        else: s=(th>lo)&(th<hi)
        s&=(r<11)&(v[:,2]<-8)
        ax=axs[i,j]; ax.scatter(r[s],v[s,2],s=0.3,c='k'); ax.set_title(f'{k} theta {lo}..{hi}'); ax.set_xlim(0,11); ax.set_ylim(-30,-8); ax.grid(alpha=.4); ax.minorticks_on(); ax.grid(which='minor',alpha=.15)
fig.tight_layout(); fig.savefig(out,dpi=70)
