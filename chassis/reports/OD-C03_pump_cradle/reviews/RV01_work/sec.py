from pathlib import Path
from build123d import Compound
from tools.core import read_step
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle"); WK = W/"reviews/RV01_work/sections"
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v01.step")
part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
for w in write_sections(asm, WK, part="rv01_assembly", version=1, views=("front",), through=(0,0,18.0)): print(w.path, w.checks)
for w in write_sections(asm, WK, part="rv01_assembly_z10", version=1, views=("front",), through=(0,0,10.0)): print(w.path, w.checks)
for w in write_sections(part, WK, part="rv01_cradle", version=1, views=("left",), through=(-31.5,0,0)): print(w.path, w.checks)
