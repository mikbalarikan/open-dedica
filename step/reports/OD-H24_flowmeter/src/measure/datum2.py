import trimesh, numpy as np
m = trimesh.load_mesh("OD-H24_flowmeter_raw.stl")
n=m.face_normals; a=m.area_faces; c=m.triangles_center
ax=np.load("ax0.npy")
def planefit(mask):
    P=c[mask]; w=a[mask]; mu=(P*w[:,None]).sum(0)/w.sum()
    _,s,vt=np.linalg.svd((P-mu)*np.sqrt(w)[:,None],full_matrices=False)
    nn=vt[2]; r=(P-mu)@nn
    return nn,mu,np.sqrt((w*r**2).sum()/w.sum())
h=c@ax
for lvl,sg in ((63.17,-1),(81.11,1)):
    mask=(np.abs(h-lvl)<0.35)&((sg*n@ax)>0.95)
    for it in range(3):
        nn,mu,rms=planefit(mask); nn*=np.sign(nn@ax)
        d=(c-mu)@nn
        mask=(np.abs(d)<0.25)&((sg*n@nn)>0.95)
    print(lvl,"normal",nn,"ang to ax %.3f deg"%np.degrees(np.arccos(nn@ax)),"rms %.3f"%rms,"area %.1f"%a[mask].sum(),"h %.3f"%(mu@nn))
    np.save("plane_%d.npy"%int(lvl),np.r_[nn,mu])
