from common import *
from tools.drawing import write_sections
s, ss = part(); P = Solid(ss[0])
outd = WORK / "sections"
res = {}
for name, view, pt in [("rv_xm78", "left", (-78, 0, 90)), ("rv_xm91", "left", (-91.03, 0, 90)), ("rv_xm85", "left", (-85, 0, 90)),
                       ("rv_x102", "left", (102, 0, 90)), ("rv_x80", "left", (78, 0, 90)),
                       ("rv_z89", "top", (0, 0, 89.0)), ("rv_z95p5", "top", (0, 0, 95.5)), ("rv_z86", "top", (0, 0, 86.0)),
                       ("rv_y2", "front", (0, 2.0, 0)), ("rv_y100", "front", (0, 100, 0)), ("rv_y153", "front", (0, 153.2349, 0)), ("rv_y127", "front", (0, 127.2515, 0))]:
    w = write_sections(P, outd, part=name, views=(view,), through=pt)
    res[name] = [(str(x.path), x.checks["nothing_clipped"].measured) for x in w]
print(res)
dump("s07_sections.json", res)
