import trimesh, numpy as np
m = trimesh.load_mesh("aligned0.ply")
def kasa(P):
    A=np.c_[2*P[:,0],2*P[:,1],np.ones(len(P))]; b=(P**2).sum(1)
    s=np.linalg.lstsq(A,b,rcond=None)[0]; r=np.sqrt(s[2]+s[0]**2+s[1]**2); return s[:2],r
def ransac_circle(P,tol=0.15,it=400,seed=0):
    rng=np.random.default_rng(seed); best=None
    for _ in range(it):
        q=P[rng.choice(len(P),3,replace=False)]
        try: c,r=kasa(q)
        except: continue
        inl=np.abs(np.hypot(*(P-c).T)-r)<tol
        if best is None or inl.sum()>best.sum(): best=inl
    c,r=kasa(P[best]); res=np.hypot(*(P[best]-c).T)-r
    return c,r,best.mean(),res.std()
for z in [1,2,3,4,5,6,7,8,9,10, 11.5,12,13,14,15,16,17]:
    L=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z]).reshape(-1,3)[:,:2]
    # keep far points (outer wall): radius from rough center > 13
    rc=np.hypot(L[:,0]+2,L[:,1]-0.5)
    P=L[(rc>(13 if z<10.8 else 18.5))]
    c,r,f,s=ransac_circle(P)
    print("z %5.1f  c (%.3f, %.3f) r %.3f  inl %.2f  sd %.3f n %d"%(z,c[0],c[1],r,f,s,len(P)))
