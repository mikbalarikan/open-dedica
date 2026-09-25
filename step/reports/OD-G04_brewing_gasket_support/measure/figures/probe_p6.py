def kasa(P):
  A_=np.c_[2*P,np.ones(len(P))];s=np.linalg.lstsq(A_,(P**2).sum(1),rcond=None)[0];R=np.sqrt(s[2]+s[0]**2+s[1]**2);res=np.hypot(P[:,0]-s[0],P[:,1]-s[1])-R;return s[0],s[1],R,res.std()
for z in [-11.5,-13.5,-14.0,-14.5,-15.0]:
  sec=m.section(plane_origin=[0,0,z],plane_normal=[0,0,1])
  if sec is None: continue
  out=[]
  for e in sec.discrete:
    P=e[:,:2]
    if len(P)<15: continue
    cx,cy,R,rs=kasa(P)
    if R<5 and np.hypot(cx,cy)>11: out.append((round(cx,3),round(cy,3),round(R,3),round(rs,3),round(float(np.degrees(np.arctan2(cy,cx))),2),round(float(np.hypot(cx,cy)),3)))
  print('z',z);[print('  ',o) for o in sorted(out,key=lambda o:o[4])]
# boss bottoms
for nm,(bx,by) in {'b175':(-15.6,1.7),'b-3':(15.5,-1.8),'b113':(-7.3,17.4),'b-62':(8.6,-16.6)}.items():
  d=np.hypot(c[:,0]-bx,c[:,1]-by)
  for lo,hi in [(0,1.4),(1.6,2.8),(2.9,4.2)]:
    k=B(lo,hi,d)&(n[:,2]<-0.9)&(c[:,2]<-10)
    if k.sum(): print(nm,'ring',lo,hi,'down z50',round(float(np.median(c[k,2])),3),'n',k.sum())
    k=B(lo,hi,d)&(n[:,2]>0.9)&(c[:,2]<-3)
    if k.sum(): print(nm,'ring',lo,hi,'UP z50',round(float(np.median(c[k,2])),3),'n',k.sum())
