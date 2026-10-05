import json, math
from pathlib import Path
from build123d import import_step
from tools.core import validity, common_volume
from tools.measure import clearance, envelope, bore_census, locate_bore
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
asm = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
parts = {c.label: c for c in asm.children}
def R(r):
    return dict(m=getattr(r,"measured",None), at=getattr(r,"at",None),
                st=str(getattr(r,"status",None)), why=getattr(r,"reason",None))
out={"labels":list(parts)}
out["validity"]={n:{k:R(v) for k,v in validity(p).items()} for n,p in parts.items()}
out["envelopes"]={n:{k:getattr(v,"measured",None) for k,v in envelope(p).items()} for n,p in parts.items()}
plate = parts["od_c01_frame"]
pairs = [("od_c01_frame",n) for n in parts if n!="od_c01_frame"] + [
   ("od_c03_cradle","od_c04_mount"),
]
# OD-G01 to everything
pairs += [("od_g01_housing",n) for n in parts if n not in ("od_g01_housing",)]
cl={}; iv={}
for a,b in pairs:
    key=f"{a}|{b}"
    if key in cl: continue
    cl[key]=R(clearance(parts[a],parts[b]))
    iv[key]=R(common_volume(parts[a],parts[b]))
out["clearance"]=cl; out["interference"]=iv
json.dump(out, open(W/"reviews/RV02_work/r5_asm.json","w"), indent=1, default=str)
print("== validity")
for n,v in out["validity"].items(): print(" ",n,{k:x["m"] for k,x in v.items()})
print("== clearance / interference")
for k in cl: print(f"  {k}: clr {cl[k]['m']} ({cl[k]['st']})  common {iv[k]['m']} ({iv[k]['st']}) {iv[k]['why'] or ''}")
