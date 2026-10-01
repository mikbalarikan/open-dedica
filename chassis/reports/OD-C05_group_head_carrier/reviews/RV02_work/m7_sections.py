import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Solid, Pos, Rot, Compound
from tools.drawing import write_sections
SD = W / "sections"; SD.mkdir(exist_ok=True)
s = Solid(solids(read_step(STEP))[0])
out = {}
for name, view, through in [("x0", "left", (0, 0, 0)), ("x35", "left", (35, 0, 0)), ("ym100", "front", (0, -100, 0)),
                            ("ym72", "front", (0, -72, 0)), ("y0", "front", (0, 0, 0)), ("z165", "top", (0, 0, 165)),
                            ("zm27p44", "top", (0, 0, -27.44)), ("x53", "left", (53, 0, 0))]:
    d = SD / name; d.mkdir(exist_ok=True)
    w = write_sections(s, d, part="rv02_carrier", version=4, views=(view,), through=through)
    out[name] = [(str(x.path), x.checks["nothing_clipped"].measured) for x in w]
a = read_step(ASM)
for name, view, through in [("asm_x0", "left", (0, 0, 0)), ("asm_y0", "front", (0, 0, 0))]:
    d = SD / name; d.mkdir(exist_ok=True)
    w = write_sections(a, d, part="rv02_assembly", version=4, views=(view,), through=through)
    out[name] = [(str(x.path), x.checks["nothing_clipped"].measured) for x in w]
dump("m7_sections", out); print(out)
