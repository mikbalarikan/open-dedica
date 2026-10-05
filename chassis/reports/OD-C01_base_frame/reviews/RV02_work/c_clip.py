import json
from pathlib import Path
from build123d import import_step, Solid
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); WK=W/"reviews/RV02_work"
part = Solid(import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step")).wrapped)
res={}
for mm in (-8.0,-30.0,-60.0,-100.0):
    w = write_sections(part, str(WK/"mutants"), part=f"cclip{abs(int(mm))}", version=3,
                       views=("front",), through=(0,-3,0), margin_mm=mm)[0]
    nc=w.checks["nothing_clipped"]
    res[mm]=dict(px=nc.measured, st=str(nc.status))
    print("margin",mm,"clipped px",nc.measured,nc.status, flush=True)
json.dump(res, open(WK/"c_clip.json","w"), indent=1, default=str)
