import json, math
from pathlib import Path
from build123d import import_step
from tools.measure import radial_extent, bore_census
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
sh = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
bc = bore_census(sh)
ins = [b for b in bc.detail["bores"] if abs(b["diameter"]-4.0) < 1e-6]
assert len(ins)==38, len(ins)
rows=[]; inc=0
for b in ins:
    x,_,z = b["start"]
    least=None; least_ang=None
    for a in range(0,360,5):
        r = radial_extent(sh, (x,-6.0,z), (0,1,0), (1,0,0), float(a), 5.5,
                          side="outer")
        if str(r.status)!="MEASURED":
            inc+=1; continue
        if least is None or r.measured < least:
            least, least_ang = r.measured, a
    rows.append(dict(x=x,z=z,least_r=least,ang=least_ang,
                     across=2*least if least else None, ring=least-2.0 if least else None))
rows.sort(key=lambda q:q["least_r"])
res=dict(n=len(rows), unread=inc,
         least_across=min(q["across"] for q in rows),
         least_ring=min(q["ring"] for q in rows),
         worst=rows[:6], rows=rows)
json.dump(res, open(W/"reviews/RV02_work/r6_rings.json","w"), indent=1, default=str)
print("holes",res["n"],"unread rays",inc)
print("least across (D-05a)",round(res["least_across"],6))
print("least ring (J-05)",round(res["least_ring"],6))
for q in rows[:6]: print("  ",q["x"],q["z"],"r",round(q["least_r"],5),"@",q["ang"],"deg")
