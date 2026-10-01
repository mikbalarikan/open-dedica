import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from tools.drawing import write_sections
from build123d import Compound
m = load_mount(); h22, h24, h22p, h24p = load_oem()
out = []
for part, shape, views, through in (
        ("rv01_mount_deck", m, ("top", "front"), (62.0, 0.0, 47.99)),
        ("rv01_mount_notch", m, ("top",), (0.0, 0.0, 10.25)),
        ("rv01_mount_insert", m, ("left",), (46.662, 0.0, 44.0)),
        ("rv01_asm_rib", Compound(children=[m] + h24p), ("left",), (0.75, -13.96, 10.1)),
        ("rv01_asm_ringroot", Compound(children=[m] + h24p), ("front",), (-10.58, -12.0, 10.0)),
        ("rv01_asm_valve", Compound(children=[m] + h22p), ("left", "front"), (62.0, 0.0, 45.0))):
    for w in write_sections(shape, W / "sections", part=part, version=1, views=views, through=through):
        out.append((str(w.path.name) if hasattr(w, "path") else str(w), {k: (v.measured, v.status) for k, v in w.checks.items()}))
        print(out[-1])
dump("s11.json", out)
