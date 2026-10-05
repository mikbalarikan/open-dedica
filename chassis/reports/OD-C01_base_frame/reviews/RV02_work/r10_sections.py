import json
from pathlib import Path
from tools.drawing import nothing_clipped
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
res={}
for p in sorted((W/"03_Sections").glob("od_c01_frame_v03_*.png")):
    r = nothing_clipped(str(p))
    res[p.name]=dict(m=r.measured, st=str(r.status), why=getattr(r,"reason",None))
bad={k:v for k,v in res.items() if v["m"]!=0 or v["st"]!="MEASURED"}
print("sections:",len(res),"not clean:",bad)
json.dump(res, open(W/"reviews/RV02_work/r10_sections.json","w"), indent=1)
