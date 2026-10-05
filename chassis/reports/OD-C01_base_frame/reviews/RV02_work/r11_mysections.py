from pathlib import Path
from build123d import import_step
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
WK = W/"reviews/RV02_work/sections"; WK.mkdir(exist_ok=True)
part = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
asm  = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
for sh, nm, views, thr in [
    (part,"rv02plate_plan",("front",),(0,-3.0,0)),
    (part,"rv02plate_front77",("top",),(0,0,77.0)),
    (part,"rv02plate_x104",("left",),(104.5,0,0)),
    (asm,"rv02asm_mid",("left",),(0,0,0)),
    (asm,"rv02asm_front",("top",),(0,0,77.0)),
    (asm,"rv02asm_back",("top",),(0,0,-282.0)),
]:
    for w in write_sections(sh, str(WK), part=nm, version=3, views=views, through=thr):
        print(nm, w.detail["view"], "cut", round(w.detail["section_area_mm2"],2) if "section_area_mm2" in w.detail else w.detail,
              "clipped", w.checks["nothing_clipped"].measured)
