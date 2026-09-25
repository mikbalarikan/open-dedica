def kasa(P):
  A_=np.c_[2*P,np.ones(len(P))];s=np.linalg.lstsq(A_,(P**2).sum(1),rcond=None)[0];R=np.sqrt(s[2]+s[0]**2+s[1]**2);res=np.hypot(P[:,0]-s[0],P[:,1]-s[1])-R;return s[0],s[1],R,res.std()
rd=(n[:,0]*c[:,0]+n[:,1]*c[:,1])/np.maximum(r,1e-9)
def arc(sel,lab):
  P=np.c_[r[sel],c[sel,2]]
  if len(P)<30: print(lab,'few');return
  a,b,R,s=kasa(P);print(f'{lab}: centre r={a:.3f} z={b:.3f} R={R:.3f} rms={s:.3f} n={len(P)}')
arc(B(20.7,22.8,r)&B(-13.0,-10.9,c[:,2])&(n[:,2]<-0.2)&(rd<-0.2),'flange inner-bottom round')
arc(B(20.3,20.9,r)&B(-13.0,-10.9,c[:,2])&(n[:,2]<-0.2)&(rd<-0.2),'x')
arc(B(7.8,10.6,r)&(c[:,2]<-15.0)&(n[:,2]<0.3),'hub tube bottom U')
arc(B(28.9,31.2,r)&(c[:,2]>-7.6)&(n[:,2]>-0.2),'lip top')
arc(B(20.0,21.8,r)&(c[:,2]>0.3),'bead top')
arc(B(22.2,23.2,r)&B(-1,0.3,c[:,2])&(rd>0.2)&(n[:,2]>0.2),'plate outer edge round')
arc(B(4.4,5.1,r)&B(0.4,1.0,c[:,2]),'hub top inner (cone->flat) round')
arc(B(5.6,6.3,r)&B(0.3,1.0,c[:,2])&(rd>0.2),'hub ring outer top round')
arc(B(33.4,34.8,r)&B(-9.7,-7.6,c[:,2])&(rd>0.2),'tab outer edge')
arc(B(30.4,31.2,r)&B(-13.3,-12.4,c[:,2])&(rd>0.2)&(n[:,2]<-0.2),'flange outer-bottom round')
arc(B(22.9,23.8,r)&B(-10.9,-9.8,c[:,2])&(rd>0.1)&(n[:,2]>0.1),'wall-flange top fillet')
arc(B(29.2,29.8,r)&B(-10.9,-10.0,c[:,2])&(rd<0.)&(n[:,2]>0.1),'flange-lip inner fillet')
