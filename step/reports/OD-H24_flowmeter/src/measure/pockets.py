import numpy as np
from scipy import ndimage
import shapely.geometry as sg
zmax=np.load("zmax.npy"); res=0.2; x0,y0=-22,-38
H,W=zmax.shape
yy,xx=np.mgrid[0:H,0:W]; X=x0+(xx+0.5)*res; Y=y0+(yy+0.5)*res
R=np.hypot(X,Y); TH=np.degrees(np.arctan2(Y,X))%360
low=(R<19.9)&(R>8.2)&((np.isnan(zmax))|(zmax<19.3))
# exclude tube corridor & connector
lab,n=ndimage.label(low)
for i in range(1,n+1):
    k=lab==i
    if k.sum()<15: continue
    r=R[k]; t=TH[k]; z=zmax[k]
    # angular extent robust (handle wrap)
    tt=np.sort(t); gaps=np.diff(np.r_[tt,tt[0]+360]); j=np.argmax(gaps); t0=tt[(j+1)%len(tt)]; t1=tt[j]
    print("comp %d npx %d r[%.2f %.2f] (p2/p98 %.2f %.2f) th[%.1f -> %.1f] zfloor med %.2f nanfrac %.2f cxy (%.2f,%.2f)"%(i,k.sum(),r.min(),r.max(),np.percentile(r,2),np.percentile(r,98),t0,t1,np.nanmedian(z) if (~np.isnan(z)).any() else -1,np.isnan(z).mean(),X[k].mean(),Y[k].mean()))
    if np.percentile(r,2)>14:
        pts=np.c_[X[k],Y[k]]; rect=sg.MultiPoint(pts).minimum_rotated_rectangle
        c=np.array(rect.exterior.coords)[:4]; e=[np.linalg.norm(c[(q+1)%4]-c[q]) for q in range(4)]
        ang=np.degrees(np.arctan2(*(c[1]-c[0])[::-1]))
        print("    minrect %.2f x %.2f ang %.1f center (%.2f,%.2f) centre r %.2f th %.1f"%(e[0]+res,e[1]+res,ang,c[:,0].mean(),c[:,1].mean(),np.hypot(c[:,0].mean(),c[:,1].mean()),np.degrees(np.arctan2(c[:,1].mean(),c[:,0].mean()))%360))
