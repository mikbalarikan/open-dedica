from pathlib import Path
from tools.core import read_step
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle"); WK = W/"reviews/RV01_work/sections"
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v01.step")
for v in ("top","left"):
    for w in write_sections(asm, WK, part=f"rv01_asm_z18_{v}", version=1, views=(v,), through=(0,0,18.0)): print(w.path, w.checks["nothing_clipped"].measured)
