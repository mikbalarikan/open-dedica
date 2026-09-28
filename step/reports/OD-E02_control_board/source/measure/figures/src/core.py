import numpy as np, trimesh, sys, json
from shapely.geometry import Polygon, Point
from shapely import distance, points
m=trimesh.load(sys.argv[1])
BL=(-32.78,-12.70);BR=(32.32,-13.13);TR=(32.30,1.07);TL=(-32.73,1.48)
bTL=(-20.05,8.98);bTR=(10.80,8.79)
main=Polygon([BL,BR,TR,TL])
# bump core: x between bTL.x,bTR.x; y from main top line (approx 1.3) to bump y
bump=Polygon([(bTL[0],0.5),(bTR[0],0.5),bTR,bTL])
def sect(z):
    s=m.section(plane_origin=[0,0,z],plane_normal=[0,0,1])
    return np.vstack([s.vertices[e.points][:,:2] for e in s.entities])
for z in [float(a) for a in sys.argv[2].split(',')]:
    P=sect(z); pp=points(P)
    dm=distance(main,pp); db=distance(bump,pp)
    # exclude clips/tab: points far (>R+1.2) from both
    d=np.minimum(dm,db)
    med=np.median(d)
    keep=np.abs(d-med)<1.2
    isb=(db<dm)&keep&(P[:,1]>6)   # bump top & sides
    ism=(dm<=db)&keep
    # split main by side
    out={'z':z}
    for lab,sel in [('main_all',ism),('main_-Y',ism&(P[:,1]<-13.2)),('main_+Y',ism&(P[:,1]>1.3)),('main_-X',ism&(P[:,0]<-33)),('main_+X',ism&(P[:,0]>32.4)),('bump',isb)]:
        v=np.minimum(dm,db)[sel]
        if len(v)>5: out[lab]=[round(float(np.median(v)),3),round(float(np.percentile(v,10)),3),round(float(np.percentile(v,90)),3),int(len(v))]
    print(json.dumps(out))
