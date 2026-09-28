import numpy as np, trimesh, sys, json
m=trimesh.load(sys.argv[1])
def pts(z):
    s=m.section(plane_origin=[0,0,z],plane_normal=[0,0,1])
    return np.vstack([s.vertices[e.points][:,:2] for e in s.entities])
def kasa(p):
    A=np.c_[2*p,np.ones(len(p))]; b=(p**2).sum(1); c=np.linalg.lstsq(A,b,rcond=None)[0]
    r=np.sqrt(c[2]+c[0]**2+c[1]**2); res=np.hypot(*(p-c[:2]).T)-r
    return dict(cx=round(c[0],3),cy=round(c[1],3),r=round(r,3),rms=round(float(np.sqrt((res**2).mean())),4),n=len(p))
def edge(P,axis,lo,hi,which):
    o=1-axis; s=(P[:,o]>lo)&(P[:,o]<hi); v=P[s,axis]
    return float(np.median(v[v<np.percentile(v,3)+0.15]) if which=='min' else np.median(v[v>np.percentile(v,97)-0.15]))
z=float(sys.argv[2]); spec=json.loads(sys.argv[3])
P=pts(z); out={'z':z}
# straight edges: name -> [axis, lo, hi, which]
E={k:edge(P,*v) for k,v in spec['edges'].items()}; out['edges']={k:round(v,3) for k,v in E.items()}
for name,(ex,ey,sx,sy,R0) in spec['corners'].items():
    x0=E[ex]; y0=E[ey]
    # corner box: from edge line inward by 1.3*R0 (sx,sy = direction into material)
    xs=sorted([x0,x0+sx*1.3*R0]); ys=sorted([y0,y0+sy*1.3*R0])
    s=(P[:,0]>xs[0]-0.3)&(P[:,0]<xs[1])&(P[:,1]>ys[0]-0.3)&(P[:,1]<ys[1])
    q=P[s]; q=q[(np.abs(q[:,0]-x0)>0.06)&(np.abs(q[:,1]-y0)>0.06)]
    out[name]=kasa(q) if len(q)>6 else None
print(json.dumps(out))
