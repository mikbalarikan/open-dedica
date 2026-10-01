import sys, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.drawing import write_sections
L = lid(); out = {}
for nm, pt, views in [("col65m60", (65, 230, -60), ("front", "top", "left")), ("col90m293", (90, 230, -293), ("front", "top", "left")),
                      ("rearrib94", (94, 230, -293), ("left",)), ("pads", (48, 230, 30), ("top", "left")),
                      ("cbore_floor", (65, 217.5, -60), ("front",)), ("skirt_corner", (113, 230, -300.5), ("left", "top"))]:
    ws = write_sections(L, WORK / "sections", part=f"rv01_{nm}", version=1, views=views, through=pt)
    out[nm] = [(w.path.name, w.detail, {k: (c.measured, c.status) for k, c in w.checks.items()}) for w in ws]
dump("m7_sections.json", out); print(json.dumps(out, default=str)[:4000])
