import trimesh, numpy as np
T=np.load("T1pre.npy")
m=trimesh.load_mesh("OD-H24_flowmeter_raw.stl"); m.apply_transform(T)
n=m.face_normals; a=m.area_faces; c=m.triangles_center
def fit(mask,sg):
    for it in range(4):
        P=c[mask]; w=a[mask]; mu=(P*w[:,None]).sum(0)/w.sum()
        _,_,vt=np.linalg.svd((P-mu)*np.sqrt(w)[:,None],full_matrices=False); nn=vt[2]*np.sign(vt[2][2])
        d=(c-mu)@nn; mask=(np.abs(d)<0.2)&((sg*n@nn)>0.97)
    tilt=np.degrees(np.arccos(nn[2])); az=np.degrees(np.arctan2(nn[1],nn[0]))
    z_at_axis=mu[2]-((mu[0]*nn[0]+mu[1]*nn[1])/nn[2])
    return nn,mu,tilt,az,z_at_axis,a[mask].sum(),np.sqrt((a[mask]*d[mask]**2).sum()/a[mask].sum())
for name,lo,hi,sg in (("rim",-2.5,-1.7,-1),("panel",-0.4,0.4,-1),("flange_top",17.3,18.3,1),("boss_top",19.5,20.1,1),("conn_top",21.6,22.3,1),("flange_under",10.2,11.1,-1)):
    mask=(c[:,2]>lo)&(c[:,2]<hi)&((sg*n[:,2])>0.97)
    nn,mu,tilt,az,z0,A,rms=fit(mask,sg)
    print("%-12s tilt %.3f deg az %7.1f  z@axis %.3f  area %.0f rms %.3f"%(name,tilt,az,z0,A,rms))
