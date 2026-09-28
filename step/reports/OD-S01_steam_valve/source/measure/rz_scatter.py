"""(r,z) scatter of face centres in theta windows (datum frame). usage: rz_scatter.py mesh out.png th1 th2 ... [--hw 4]"""
import sys, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
a=sys.argv[1:]; hw=4.0
if '--hw' in a: i=a.index('--hw'); hw=float(a[i+1]); a=a[:i]+a[i+2:]
m=trimesh.load(a[0]); C=m.triangles_center; th=np.degrees(np.arctan2(C[:,1],C[:,0])); r=np.hypot(C[:,0],C[:,1])
ths=[float(t) for t in a[2:]]; nc=min(4,len(ths)); nr=int(np.ceil(len(ths)/nc))
fig,axs=plt.subplots(nr,nc,figsize=(5*nc,8*nr),squeeze=False)
for ax,t in zip(axs.flat,ths):
    s=np.abs(((th-t+180)%360)-180)<hw
    ax.scatter(r[s],C[s,2],s=0.3,c='k'); ax.set_title(f'theta {t}±{hw}'); ax.set_xlim(0,24); ax.set_ylim(-16,50)
    ax.set_aspect('equal'); ax.minorticks_on(); ax.grid(alpha=.5); ax.grid(which='minor',alpha=.2)
plt.tight_layout(); plt.savefig(a[1],dpi=70)
