from pathlib import Path
from build123d import import_step
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
WK = W/"reviews/RV02_work/sections"
asm = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
for w in write_sections(asm, str(WK), part="rv02asm_x104", version=3, views=("left",), through=(104.5,0,0)):
    print(w.detail["cut_area_mm2"], w.checks["nothing_clipped"].measured)
