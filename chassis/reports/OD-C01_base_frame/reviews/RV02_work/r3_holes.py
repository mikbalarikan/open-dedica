import json, itertools, math
from pathlib import Path
import numpy as np
from build123d import import_step
from tools.measure import bore_census, locate_bore
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
sh = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
bc = bore_census(sh)
NOM = {
 "REQ-01":(4.0,[(-35,-40),(35,-40),(-35,-60),(35,-60)]),
 "REQ-02":(4.0,[(-40,-148),(40,-148),(-40,-114),(40,-114)]),
 "REQ-03":(4.0,[(-4,-239),(-4,-171),(37,-239),(37,-171)]),
 "REQ-04":(4.0,[(65,-45),(65,-105),(65,-165),(65,-225)]),
 "REQ-05":(3.4,[(-110,90),(110,90),(-110,-295),(110,-295)]),
 "REQ-06":(8.0,[(-80,-120),(-80,-230)]),
 "REQ-10":(4.0,[(-113,-42),(-71,-42),(-113,-148.5),(-71,-148.5)]),
 "REQ-11":(4.0,[(88,-222),(106,-222),(88,-78),(106,-78)]),
 "REQ-12":(4.0,[(-81,-282),(81,-282),(-95,-282),(95,-282)]),
 "REQ-13":(4.0,[(-104.5,-262),(104.5,-262),(-104.5,-15),(104.5,-15),(-104.5,62),(104.5,62)]),
 "REQ-14":(4.0,[(-85,77),(85,77),(-95,77),(95,77)]),
}
res={}
for gid,(d,pts) in NOM.items():
    rows=[]
    for (x,z) in pts:
        r = locate_bore(bc, (x,0.0,z), (0,1,0))
        rows.append(dict(at=[x,z], dia=r["diameter"].measured, off=r["offset"].measured,
                         length=r["length"].measured, through=r["through"].measured,
                         status=str(r["diameter"].status)))
    res[gid]=dict(nominal_d=d, rows=rows,
      worst_dia_dev=max(abs(q["dia"]-d) for q in rows),
      worst_off=max(q["off"] for q in rows),
      min_len=min(q["length"] for q in rows),
      all_through=all(q["through"]==1 for q in rows))
# all measured axes
axes=[(b["start"][0], b["start"][2], b["diameter"]) for b in bc.detail["bores"]]
# centre-to-centre nearest for each of the 18 new holes
new = NOM["REQ-11"][1]+NOM["REQ-12"][1]+NOM["REQ-13"][1]+NOM["REQ-14"][1]
c2c={}
for (x,z) in new:
    # find own measured axis
    own=min(axes,key=lambda a:(a[0]-x)**2+(a[1]-z)**2)
    best=min(((math.hypot(a[0]-own[0],a[1]-own[1]),a) for a in axes if a is not own),key=lambda t:t[0])
    c2c[f"{x},{z}"]=dict(dist=round(best[0],6), to=[best[1][0],best[1][1],best[1][2]],
                         wall=round(best[0]-own[2]/2-best[1][2]/2,6))
res["new_hole_c2c"]=c2c
res["least_c2c"]=min(v["dist"] for v in c2c.values())
res["least_wall_between_holes"]=min(v["wall"] for v in c2c.values())
# distance to outline analytically: straight sides x=+-120, z=-305,+100; corner arcs R10 at (+-110,+90),(+-110,-295)
def outline_dist(x,z):
    ds=[120-abs(x), 100-z, z+305]
    for (cx,cz) in [(110,90),(-110,90),(110,-295),(-110,-295)]:
        # arc region only; distance to arc = |R - dist to centre| if outside quadrant else ignore; use conservative
        ds.append(abs(10-math.hypot(x-cx,z-cz)))
    return min(ds)
res["new_hole_outline"]={f"{x},{z}":round(outline_dist(x,z),6) for (x,z) in new}
res["least_outline"]=min(res["new_hole_outline"].values())
json.dump(res, open(W/"reviews/RV02_work/r3_holes.json","w"), indent=1, default=str)
for k,v in res.items():
    if k.startswith("REQ"): print(k, "dev",round(v["worst_dia_dev"],6),"off",round(v["worst_off"],6),"len",round(v["min_len"],4),"through",v["all_through"])
print("least c2c", res["least_c2c"], "least wall between holes", res["least_wall_between_holes"])
print("least outline", res["least_outline"])
print("outline per hole", res["new_hole_outline"])
