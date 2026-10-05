import json
from pathlib import Path
from build123d import import_step, Box, Pos, Align
from tools.measure import clearance, envelope
from tools.core import common_volume
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
asm = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
P = {c.label: c for c in asm.children}
def prism(x0,x1,z0,z1,h):
    return Pos((x0+x1)/2, 0, (z0+z1)/2)*Box(x1-x0, h, z1-z0, align=(Align.CENTER,Align.MIN,Align.CENTER))
Z = {"tray A-06":prism(-75,75,-15,85,36.9), "tank A-07":prism(-70,70,-305,-250,400),
     "valve A-05":prism(-117,-67,-154,-35,48), "electronics A-08":prism(70,120,-240,-30,400)}
out={}
for zn,pr in Z.items():
    for n,p in P.items():
        if n=="od_c01_frame": continue
        c=clearance(pr,p)
        if abs(c.measured)<1e-9:
            cv=common_volume(pr,p)
            out.setdefault(zn,{})[n]=dict(clearance=0.0, shared_mm3=cv.measured, st=str(cv.status),
                                          env={k:round(v.measured,3) for k,v in envelope(p).items()})
for zn,d in out.items():
    print("==",zn)
    for n,v in d.items(): print("   ",n,"shared",round(v["shared_mm3"],1) if isinstance(v["shared_mm3"],float) else v["shared_mm3"],
                                "z",v["env"]["min_z"],"..",v["env"]["max_z"],"x",v["env"]["min_x"],"..",v["env"]["max_x"])
json.dump(out, open(W/"reviews/RV02_work/r14_zones.json","w"), indent=1, default=str)
