import trimesh, numpy as np, pymeshfix
T=np.load("T1pre.npy"); S=np.eye(4); S[2,3]=2.013; T=S@T
np.save("T.npy",T)
m=trimesh.load_mesh("OD-H24_flowmeter_raw.stl"); m.apply_transform(T); m.export("aligned.ply")
print(m.bounds)
v=np.ascontiguousarray(m.vertices,dtype=np.float64); f=np.ascontiguousarray(m.faces,dtype=np.int32)
vc,fc=pymeshfix.clean_from_arrays(v,f)
r=trimesh.Trimesh(vc,fc); print("repaired wt",r.is_watertight,"vol",r.volume,"faces",len(fc)); r.export("repaired.ply")
