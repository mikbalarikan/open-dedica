import trimesh, numpy as np
m=trimesh.load_mesh("aligned.ply")
v,fi=trimesh.sample.sample_surface(m,4000000,seed=7); n=m.face_normals[fi]
x,y,z=v.T; r=np.hypot(x,y); th=np.degrees(np.arctan2(y,x))%360
def kasa(P):
    A=np.c_[2*P,np.ones(len(P))]; b=(P**2).sum(1); s=np.linalg.lstsq(A,b,rcond=None)[0]; return s[:2],np.sqrt(s[2]+s[0]**2+s[1]**2)
# pins
for nm,c0 in (("center",(0.2,0.4)),("second",(-11.7,0.3))):
    k=(np.hypot(x-c0[0],y-c0[1])<2.6)&(z<-0.6)&(np.abs(n[:,2])<0.3)
    c,rr=kasa(np.c_[x[k],y[k]]); kb=(np.hypot(x-c0[0],y-c0[1])<2.6)
    print(nm,"pin c (%.3f,%.3f) r %.3f zmin %.3f"%(c[0],c[1],rr,z[kb].min()), "r by z:",[ (zz,round(kasa(np.c_[x[k&(np.abs(z-zz)<0.3)],y[k&(np.abs(z-zz)<0.3)]])[1],3)) for zz in (-1.0,-2.5,-4.0,-5.5,-6.5) if (k&(np.abs(z-zz)<0.3)).sum()>30])
# downward faces histogram by region
d=n[:,2]<-0.9
for nm,sel in (("rim r14-15.9",(r>14.2)&(r<15.6)),("panel r4-13",(r>4.5)&(r<13)&(np.minimum(np.abs(x),np.abs(y))>1.2)),("spokes",(r>4.5)&(r<13)&(np.minimum(np.abs(x),np.abs(y))<0.3)),("hub r<3",(r<3.0)&(r>2.3))):
    k=d&sel&(z<3)
    print(nm,"z med %.3f p5 %.3f p95 %.3f n %d"%(np.median(z[k]),np.percentile(z[k],5),np.percentile(z[k],95),k.sum()))
# spoke widths: at z 1.0, side walls of spokes
for ax in ("x+","x-","y+","y-"):
    if ax[0]=="x": sel=(np.abs(y)<2)&((x>5) if ax[1]=="+" else (x<-5))&(np.abs(x)<12.5); w=y
    else: sel=(np.abs(x)<2)&((y>5) if ax[1]=="+" else (y<-5))&(np.abs(y)<12.5); w=x
    k=sel&(np.abs(z-1.0)<0.5)&(np.abs(n[:,2])<0.4)
    ww=w[k]; print("spoke",ax,"side walls at",np.percentile(ww,[3,50,97]).round(2),"n",k.sum())
# hub outer wall r
k=(r>2.3)&(r<4.5)&(z>0.2)&(z<1.8)&(np.abs(n[:,2])<0.4)
c,rr=kasa(np.c_[x[k],y[k]]); print("hub wall c (%.3f,%.3f) r %.3f n %d"%(c[0],c[1],rr,k.sum()))
# rim inner wall
k=(r>13)&(r<14.8)&(z>0.3)&(z<1.7)&(np.abs(n[:,2])<0.4)
c,rr=kasa(np.c_[x[k],y[k]]); print("rim inner wall c (%.3f,%.3f) r %.3f n %d"%(c[0],c[1],rr,k.sum()))
