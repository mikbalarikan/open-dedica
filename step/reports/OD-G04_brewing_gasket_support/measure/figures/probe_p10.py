res={}
for a in [-154.5,-94.5,-39.5,25.5,81.0,140.5]:
  t=np.radians(a);u=np.array([np.cos(t),np.sin(t)]);v=np.array([-np.sin(t),np.cos(t)])
  d=c[:,:2]@v; al=c[:,:2]@u; nv=n[:,:2]@v
  base=B(10.5,20,al)&B(-10,-3.5,c[:,2])&(abs(d)<1.5)
  kp=base&(nv>0.85); km=base&(nv<-0.85)
  dp=np.median(d[kp]) if kp.sum() else np.nan; dm=np.median(d[km]) if km.sum() else np.nan
  # rib bottom step radius: along-radius where min z drops below -12
  res[a]=(dp,dm)
  print(f'rib {a}: +side d={dp:.3f} (n{kp.sum()}) -side d={dm:.3f} (n{km.sum()}) t={dp-dm:.3f} mid={np.degrees(np.arctan2((dp+dm)/2,15)):.2f}deg offset {(dp+dm)/2:.3f}mm')
  # step location: down faces on rib at z<-12
  kk=(abs(d)<0.6)&(n[:,2]<-0.8)&B(-13.5,-12.5,c[:,2])&B(10,20.5,al)
  k2=(abs(d)<0.6)&(n[:,2]<-0.8)&B(-11,-10.3,c[:,2])&B(10,20.5,al)
  print('    deep bottom along r: %s   shallow bottom along r: %s'%(np.round(np.percentile(al[kk],[1,99]),2) if kk.sum() else '-',np.round(np.percentile(al[k2],[1,99]),2) if k2.sum() else '-'))
