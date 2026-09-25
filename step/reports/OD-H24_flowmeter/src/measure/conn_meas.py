import trimesh, numpy as np
m=trimesh.load_mesh("aligned.ply")
v,fi=trimesh.sample.sample_surface(m,3000000,seed=4); n=m.face_normals[fi]
a=np.radians(5.2); c,s=np.cos(a),np.sin(a)
xr=v[:,0]*c+v[:,1]*s; yr=-v[:,0]*s+v[:,1]*c; z=v[:,2]
for pc in (-3.93,0.0,3.93):
    k=(np.abs(yr-pc)<1.9)&(xr>8.5)&(xr<13)&(z>24.2)
    print("pin y'=%.2f"%pc)
    for z0 in np.arange(24.25,30.5,0.5):
        q=k&(np.abs(z-z0)<0.25)
        if q.sum()<20: continue
        print("   z %.2f  x' [%.2f %.2f] y' [%.2f %.2f] n %d"%(z0,np.percentile(xr[q],1),np.percentile(xr[q],99),np.percentile(yr[q],1),np.percentile(yr[q],99),q.sum()))
    kp=(np.abs(yr-pc)<1.0)&(xr>9.5)&(xr<12)&(z>30)
    print("   pin top z %.2f  x' c %.2f y' c %.2f"%(z[kp].max(),np.median(xr[kp&(z>31)&(z<35)]),np.median(yr[kp&(z>31)&(z<35)])))
    kq=(np.abs(yr-pc)<2.0)&(xr>13.3)&(xr<16.5)&(z>24.3)
    print("   plate top z %.2f p99.5 %.2f ; x' p2/p98 at z27 %s"%(z[kq].max(),np.percentile(z[kq],99.5),np.percentile(xr[kq&(np.abs(z-27)<1)],[2,50,98]).round(2)))
    for z0 in (26,28,30):
        q=kq&(np.abs(z-z0)<0.4)
        if q.sum()>20: print("     plate z %g y' [%.2f %.2f]"%(z0,np.percentile(yr[q],1),np.percentile(yr[q],99)))
# frustum top: upward faces between 25 and 30 near pins
k=(n[:,2]>0.9)&(xr>8.5)&(xr<13)&(z>24.5)&(z<31)
print("up faces z hist",np.histogram(z[k],bins=np.arange(24.5,31,0.25)))
