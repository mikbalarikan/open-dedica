import trimesh,numpy as np,matplotlib,json
matplotlib.use('Agg');import matplotlib.pyplot as plt
A='/tmp/claude-0/-home-user-agentic-STL-to-CAD/d8e5b691-152f-55fe-9a52-555e01807691/scratchpad/job/OD-W03_water-tank-valve/intake/aligned_work.stl'
m=trimesh.load(A); V=m.vertices
fig,axs=plt.subplots(1,3,figsize=(20,9))
for ax,(cx,name) in zip(axs,((-19.485,'cupA'),(19.485,'cupB'),(0,'boss'))):
    q=V[:,:2]-[cx,0]; r=np.hypot(*q.T); th=np.degrees(np.arctan2(q[:,1],q[:,0]))
    k=(np.abs(np.abs(th)-90)<60)&(r<16)   # away from webs along X
    ax.plot(r[k],V[k,2],',',alpha=0.3)
    zb=np.arange(-3,29,0.25); med=[]
    for z0 in zb:
        s=k&(np.abs(V[:,2]-z0)<0.125)
        # outermost surface ring: take points with r > 0.5*max
        if s.sum()>20:
            rr=r[s]; med.append((z0,np.percentile(rr,50),np.percentile(rr,90),s.sum()))
    med=np.array(med); ax.plot(med[:,1],med[:,0],'r-',lw=0.8)
    ax.set_title(name);ax.grid(True,which='both',lw=0.3);ax.minorticks_on();ax.set_aspect('equal')
    np.savetxt(f'prof_{name}.txt',med,fmt='%.3f')
plt.tight_layout();plt.savefig('prof.png',dpi=70)
