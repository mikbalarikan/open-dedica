# outer part of the boss-A webs (boss edge r 19.0 -> cup wall r 20.6), found by the second self-check
for a in [-6.55,172.95]:
  t=np.radians(a);u=np.array([np.cos(t),np.sin(t)]);v=np.array([-np.sin(t),np.cos(t)])
  d=c[:,:2]@v; al=c[:,:2]@u; nv=n[:,:2]@v
  base=B(19.1,20.5,al)&(abs(d)<2)&B(-14,-3,c[:,2])
  kp=base&(nv>0.8); km=base&(nv<-0.8); kd=base&(n[:,2]<-0.8)&(abs(d)<0.6)
  g=lambda k,a_: f'{np.median(a_[k]):.3f} n{k.sum()}' if k.sum()>5 else 'none'
  print(f'boss {a}: +side d {g(kp,d)} | -side d {g(km,d)} | bottom z {g(kd,c[:,2])}')
