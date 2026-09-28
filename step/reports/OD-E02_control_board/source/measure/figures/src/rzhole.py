import numpy as np, trimesh, sys, matplotlib, sys
sys.path.insert(0,'/home/user/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts')
from datum_fit import closed_loops_at_z, fit_circle_irls
matplotlib.use('Agg'); import matplotlib.pyplot as plt
m=trimesh.load(sys.argv[1])
v,_=trimesh.sample.sample_surface(m,500000,seed=0)
fig,axs=plt.subplots(1,2,figsize=(12,7))
for ax,c in zip(axs,[(-13.34,-7.95),(12.65,-8.01)]):
    q=v[:,:2]-c; r=np.hypot(*q.T); s=(r<6)&(v[:,2]<2)&(v[:,2]>-18)
    ax.scatter(r[s],v[s,2],s=0.3,c='k'); ax.set_xlim(0,6); ax.set_ylim(-18,2); ax.grid(alpha=.4); ax.minorticks_on(); ax.grid(which='minor',alpha=.15); ax.set_title(str(c))
fig.tight_layout(); fig.savefig(sys.argv[2],dpi=70)
for z in [-0.5,-1.5,-2.5,-3.5,-5,-7,-9,-11,-12.5,-13.5,-14.5,-15.5]:
    out=[]
    for xy in closed_loops_at_z(m,z):
        c=fit_circle_irls(xy)
        if c['r']<5 and min(abs(c['cx']+13.3),abs(c['cx']-12.65))<1.5: out.append('(%.2f,%.2f) r%.3f rms%.3f'%(c['cx'],c['cy'],c['r'],c['rms']))
    print(z,out)
