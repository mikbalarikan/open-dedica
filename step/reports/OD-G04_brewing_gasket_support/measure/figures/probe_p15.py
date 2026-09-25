def kasa(P):
  A_=np.c_[2*P,np.ones(len(P))];s=np.linalg.lstsq(A_,(P**2).sum(1),rcond=None)[0];R=np.sqrt(s[2]+s[0]**2+s[1]**2);return s[0],s[1],R
bos={'A175':(-15.44,1.91),'A-7':(15.355,-1.76),'B113':(-7.54,17.54),'B-62':(8.89,-16.74)}
rows={k:[] for k in bos}
for z in np.arange(-16.0,-11.9,0.25):
  sec=m.section(plane_origin=[0,0,z],plane_normal=[0,0,1])
  if sec is None: continue
  for e in sec.discrete:
    P=e[:,:2]
    if len(P)<12: continue
    cx,cy,R=kasa(P)
    for kname,(bx,by) in bos.items():
      if np.hypot(cx-bx,cy-by)<0.4 and R<3: rows[kname].append((round(float(z),2),round(float(R),3)))
for k,v in rows.items(): print(k,v)
