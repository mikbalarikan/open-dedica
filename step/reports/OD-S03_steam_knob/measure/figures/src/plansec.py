import sys, numpy as np, trimesh
RUN=sys.argv[1]; z=float(sys.argv[2]); box=eval(sys.argv[3]); eps=float(sys.argv[4])
m=trimesh.load(f"{RUN}/intake/aligned_work.stl"); s=m.section([0,0,1],[0,0,z])
def rdp(P,e):
    if len(P)<3: return P
    a,b=P[0],P[-1]; d=b-a; L=np.linalg.norm(d)
    dist=np.abs(d[0]*(P[:,1]-a[1])-d[1]*(P[:,0]-a[0]))/L if L>1e-12 else np.linalg.norm(P-a,axis=1)
    i=int(np.argmax(dist)); return np.vstack([rdp(P[:i+1],e)[:-1],rdp(P[i:],e)]) if dist[i]>e else np.vstack([a,b])
for e in s.entities:
    P=s.vertices[e.points][:,:2]
    k=(P[:,0]>box[0])&(P[:,0]<box[1])&(P[:,1]>box[2])&(P[:,1]<box[3])
    if k.sum()<5: continue
    idx=np.where(k)[0]; runs=np.split(idx,np.where(np.diff(idx)>1)[0]+1)
    for ru in runs:
        if len(ru)<5: continue
        S=rdp(P[ru],eps); print(len(ru),' '.join(f'({a:.2f},{b:.2f})' for a,b in S))
