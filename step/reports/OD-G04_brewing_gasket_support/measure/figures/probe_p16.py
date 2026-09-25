# second-pass probes after the first self-check: hub tube inner draft, flange faces vs r, lip/tab
rd=(n[:,0]*c[:,0]+n[:,1]*c[:,1])/np.maximum(r,1e-9)
print('hub tube inner r vs z (inward faces r 7-9)')
for z0 in np.arange(-15,-2.5,1.0):
  k=B(7,9,r)&B(z0,z0+1,c[:,2])&(abs(n[:,2])<0.3)&(rd<-0.9)
  if k.sum()>20: print(f'  z {z0:.0f}..{z0+1:.0f} r50 {np.median(r[k]):.3f} n {k.sum()}')
print('hub tube outer r vs z')
for z0 in np.arange(-15,-2.5,2.0):
  k=B(9.3,11,r)&B(z0,z0+2,c[:,2])&(abs(n[:,2])<0.3)&(rd>0.9)
  if k.sum()>20: print(f'  z {z0:.0f}..{z0+2:.0f} r50 {np.median(r[k]):.3f} n {k.sum()}')
print('flange bottom z vs r (down faces)')
for r0 in np.arange(21,31,1.0):
  k=B(r0,r0+1,r)&(n[:,2]<-0.9)&B(-14,-12.3,c[:,2])
  if k.sum()>20: print(f'  r {r0:.0f}..{r0+1:.0f} z50 {np.median(c[k,2]):.3f} n {k.sum()}')
print('flange top z vs r (up faces)')
for r0 in np.arange(22.5,30,0.5):
  k=B(r0,r0+0.5,r)&(n[:,2]>0.9)&B(-11.5,-9.8,c[:,2])
  if k.sum()>20: print(f'  r {r0:.1f}..{r0+0.5:.1f} z50 {np.median(c[k,2]):.3f} n {k.sum()}')
print('lip outer r vs z (outward, away from tabs)')
notab=~(B(-160,-86,th)|B(-40,34,th)|B(80,154,th))
for z0 in np.arange(-13,-7,0.5):
  k=B(30,31.6,r)&B(z0,z0+0.5,c[:,2])&(abs(n[:,2])<0.3)&(rd>0.9)&notab
  if k.sum()>20: print(f'  z {z0:.1f} r50 {np.median(r[k]):.3f} n {k.sum()}')
print('cup inner wall r vs z')
for z0 in np.arange(-12,-3,1.0):
  k=B(19.8,21.2,r)&B(z0,z0+1,c[:,2])&(abs(n[:,2])<0.3)&(rd<-0.9)
  if k.sum()>20: print(f'  z {z0:.0f} r50 {np.median(r[k]):.3f} n {k.sum()}')
