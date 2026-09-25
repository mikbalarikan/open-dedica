import numpy as np, trimesh, json, sys
m=trimesh.load_mesh(sys.argv[1]); C,N=m.triangles_center,m.face_normals
k=(np.abs(C[:,1])<1.0)&(np.abs(C[:,0])>1.3)&(np.abs(C[:,0])<3.8)&(N[:,2]<-0.9)&(C[:,2]<-15)
json.dump({'stem_bottom_z':dict(p10=float(np.percentile(C[k,2],10)),p50=float(np.median(C[k,2])),p90=float(np.percentile(C[k,2],90)),n=int(k.sum()),selection='down-facing faces |y|<1, 1.3<|x|<3.8, z<-15 (flat underside of the stem cylinder, either side of the rib)')},open(sys.argv[2],'w'),indent=1)
