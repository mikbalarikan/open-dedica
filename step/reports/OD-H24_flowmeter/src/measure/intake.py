import trimesh, numpy as np
m = trimesh.load_mesh("OD-H24_flowmeter_raw.stl")
print("faces", len(m.faces), "verts", len(m.vertices), "wt", m.is_watertight)
print("bounds", m.bounds, "extent", m.extents)
print("area", m.area, "bodies", m.body_count)
m.export("orig.ply")
# normal clustering
from sklearn.cluster import KMeans
n=m.face_normals; a=m.area_faces
rng=np.random.default_rng(0); idx=rng.choice(len(n),200000,p=a/a.sum())
km=KMeans(24,n_init=4,random_state=0).fit(n[idx])
c,cnt=np.unique(km.labels_,return_counts=True)
for i in np.argsort(-cnt): 
    cen=km.cluster_centers_[i]; spread=np.linalg.norm(n[idx][km.labels_==i]-cen,axis=1).mean()
    print(np.round(cen/np.linalg.norm(cen),3), cnt[i], round(spread,3))
# obb
print("obb extents", m.bounding_box_oriented.extents)
