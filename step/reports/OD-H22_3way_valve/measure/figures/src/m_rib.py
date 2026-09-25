import json,sys,numpy as np, trimesh
m=trimesh.load_mesh(sys.argv[1]); out=sys.argv[2]
R={}
for x in (-0.3,0.14,0.6):
    s=trimesh.intersections.mesh_plane(m,[1,0,0],[x,0,0]).reshape(-1,3)
    k=(s[:,2]<-23.3)&(np.abs(s[:,1])<6); R['x=%.2f'%x]=dict(flat_y_extent=[float(s[k,1].min()),float(s[k,1].max())],flat_z_p50=float(np.median(s[k,2])),n=int(k.sum()))
json.dump(R,open(out,'w'),indent=1); print(json.dumps(R))
