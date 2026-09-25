import trimesh, numpy as np, json
m=trimesh.load_mesh("aligned.ply")
def fit_line(p0,d,s_list,rad_win,excl=None):
    e1=np.cross(d,[0,0,1]); e1/=np.linalg.norm(e1); e2=np.cross(d,e1)
    C=[];R=[]
    for s in s_list:
        o=p0+s*d
        q=trimesh.intersections.mesh_plane(m,d,o).reshape(-1,3)
        uv=np.c_[(q-o)@e1,(q-o)@e2]; k=np.hypot(*uv.T)<rad_win; uv=uv[k]
        if len(uv)<30: continue
        A=np.c_[2*uv,np.ones(len(uv))]; b=(uv**2).sum(1); so=np.linalg.lstsq(A,b,rcond=None)[0]
        rr=np.sqrt(so[2]+so[0]**2+so[1]**2); res=np.hypot(uv[:,0]-so[0],uv[:,1]-so[1])-rr
        C.append(o+so[0]*e1+so[1]*e2); R.append((s,rr,np.percentile(res,90)-np.percentile(res,10),len(uv)))
    return np.array(C),R
out={}
for name,p0,d in (("low",np.array([-10.3,0,7.1]),np.array([0,-1.0,0])),("up",np.array([-4.52,-0.47,19.78]),np.array([0.1027,-0.9947,0]))):
    for it in range(3):
        C,R=fit_line(p0,d,np.arange(22,31,1.0) if name=="up" else np.arange(24,32,1.0),4.2)
        mu=C.mean(0); dd=np.linalg.svd(C-mu)[2][0]; dd*=np.sign(dd@d)
        tc=-(mu[:2]@dd[:2])/(dd[:2]@dd[:2]) if name=="up" else -mu[1]/dd[1]
        p0=mu+tc*dd; d=dd
    print(name,"p0",p0.round(3),"d",d.round(4),"az %.2f tilt %.2f"%(np.degrees(np.arctan2(d[1],d[0])),np.degrees(np.arcsin(d[2]))))
    C,R=fit_line(p0,d,np.arange(14,37,0.25),4.5)
    for s,rr,sp,nn in R: print("  s %.2f r %.3f spread %.3f n %d"%(s,rr,sp,nn))
    out[name]=dict(p0=p0.tolist(),d=d.tolist(),prof=[r[:2] for r in R])
json.dump(out,open("tubes.json","w"),indent=1)
