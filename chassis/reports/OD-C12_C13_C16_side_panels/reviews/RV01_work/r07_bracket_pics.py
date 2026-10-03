import sys
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
from tools.drawing import write_sections
BR = one(load("od_c16_bracket_C1_v01.step"))
res = {}
for part, thr, views in (("rv01_c16_z0.3", (-9.5, 8, 0.3), ("top",)), ("rv01_c16_y10.3", (-9.5, 10.3, 0.0), ("front",))):
    try:
        ws = write_sections(BR, WORK / "sections", part=part, version=1, views=views, through=thr)
        res[part] = [(w.path.name, w.sha256, w.checks["nothing_clipped"].measured) for w in ws]
    except Exception as exc:
        res[part] = f"{type(exc).__name__}: {exc}"
    print(part, res[part])
dump(res, "bracket_pics.json")
