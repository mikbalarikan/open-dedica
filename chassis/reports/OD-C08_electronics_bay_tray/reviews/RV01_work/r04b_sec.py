import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from tools.core import read_step
from tools.drawing import write_sections
a = read_step(ASM)
for name, thr in (("rv_asm_z157_pins", (90, 50, -157.52)), ("rv_asm_z100_inserts", (90, 50, -100.0)), ("rv_asm_z222_holes", (90, 50, -222.0))):
    for wr in write_sections(a, W / "sections", part=name, views=("top", "left"), through=thr):
        print(wr.path, wr.checks)
