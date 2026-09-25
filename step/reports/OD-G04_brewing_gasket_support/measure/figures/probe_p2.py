zlev(B(10.5,20.5,r)&B(0,95,th)&B(-5,-1,c[:,2]),False,'underside sector 0-95')
for a0 in range(-180,180,20):
  k=B(10.5,20,r)&B(a0,a0+20,th)&B(-5,-1,c[:,2])&(n[:,2]<-0.9)
  if k.sum(): print(' sector',a0,k.sum(),np.round(np.percentile(c[k,2],[5,50,95]),2), 'r',np.round(np.percentile(r[k],[5,95]),1))
k=(r<3.5)&(c[:,2]<-0.5); print('centre r<3.5 z<-0.5: n',k.sum(), np.round(np.percentile(c[k,2],[0,5,50,95,100]),2) if k.sum() else '')
k=(r<3.5)&(c[:,2]>-3)
print('centre cone faces r<5 nz dist'); 
kk=(r<4.6)&(r>1.5)&(c[:,2]>-3)
# cone slope from z vs r
if kk.sum(): p=np.polyfit(r[kk],c[kk,2],1); print(' cone fit z=%.3f*r+%.3f n=%d'%(p[0],p[1],kk.sum()), 'angle from axis %.1f deg'%np.degrees(np.arctan(1/abs(p[0]))))
