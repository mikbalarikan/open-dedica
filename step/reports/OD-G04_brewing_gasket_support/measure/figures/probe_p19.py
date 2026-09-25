# short web between hub tube and boss pair A (found by the first self-check, max ~1.0 mm at r 11)
for a in [-6.55,172.95]:
  t=np.radians(a);u=np.array([np.cos(t),np.sin(t)]);v=np.array([-np.sin(t),np.cos(t)])
  d=c[:,:2]@v; al=c[:,:2]@u; nv=n[:,:2]@v
  base=B(10.3,11.9,al)&(abs(d)<2)&B(-16,-3,c[:,2])
  kp=base&(nv>0.8); km=base&(nv<-0.8); kd=base&(n[:,2]<-0.8)&(abs(d)<0.6)
  print(f'boss {a}: +side d50 {np.median(d[kp]):.3f} n{kp.sum()} z {np.percentile(c[kp,2],[2,98]).round(2)} | -side d50 {np.median(d[km]):.3f} n{km.sum()} z {np.percentile(c[km,2],[2,98]).round(2)} | bottom z50 {np.median(c[kd,2]) if kd.sum() else float("nan"):.3f} n{kd.sum()}')
