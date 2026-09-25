rd=(n[:,0]*c[:,0]+n[:,1]*c[:,1])/np.maximum(r,1e-9)
print('flange inner corner profile: per r bin, median z of faces with n.z<-0.1 or inward (z -13.4..-10)')
k0=B(20.4,23.2,r)&B(-13.4,-10,c[:,2])&((n[:,2]<-0.1)|(rd<-0.5))
for r0 in np.arange(20.4,23.2,0.2):
  k=k0&B(r0,r0+0.2,r)
  if k.sum()>10: print(f'  r {r0:.1f} zmin {np.percentile(c[k,2],5):.3f} z50 {np.median(c[k,2]):.3f} n {k.sum()}')
def kasa(P):
  A_=np.c_[2*P,np.ones(len(P))];s=np.linalg.lstsq(A_,(P**2).sum(1),rcond=None)[0];R=np.sqrt(s[2]+s[0]**2+s[1]**2);res=np.hypot(P[:,0]-s[0],P[:,1]-s[1])-R;return s[0],s[1],R,res.std()
k=B(28.0,29.3,r)&B(-10.8,-9.3,c[:,2])&(n[:,2]>0.05)&(rd<0.05)&(n[:,2]<0.97)
if k.sum()>30: print('flange-lip inner fillet', [round(x,3) for x in kasa(np.c_[r[k],c[k,2]])], k.sum())
# constrained fit: arc tangent to wall r=cup_R_in (20.60) and bottom z=flange_bot_z (-13.12); scan R
rw,zb_=20.60,-13.12
best=None
for R in np.arange(1.5,3.21,0.05):
  cx,cz=rw+R,zb_+R
  kk=B(20.7,cx,r)&B(-13.4,cz,c[:,2])&((n[:,2]<-0.1)|(rd<-0.5))
  res=np.hypot(r[kk]-cx,c[kk,2]-cz)-R
  s=np.sqrt(np.mean(res**2))
  if best is None or s<best[1]: best=(R,s,kk.sum())
print('constrained tangent-arc R=%.2f rms=%.3f n=%d'%best)
