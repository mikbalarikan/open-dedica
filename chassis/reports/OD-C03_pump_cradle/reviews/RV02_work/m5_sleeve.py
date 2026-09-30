import json
from pathlib import Path
from build123d import Pos, Box
from tools.core.step import read_step
from tools.core import common_volume
from tools.measure import clearance, radial_extent
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v02.step")
ch = {c.label: c for c in asm.children}
pu, sl, cr = ch["OD_H01_ulka_ep5_pump"], ch["od_h02_sleeve_assumed_A03"], ch["od_c03_cradle"]
o = {}
for i, s in enumerate(sl.solids()):
    bb = s.bounding_box()
    o[f"sleeve{i}_y{bb.min.Y:.1f}..{bb.max.Y:.1f}"] = common_volume(s, pu).measured
    for zb in ((-6, 5.5), (5.5, 13.6), (13.6, 32)):
        clip = s & (Pos(0, 0, (zb[0]+zb[1])/2) * Box(60, 60, zb[1]-zb[0]))
        o[f"sleeve{i} z{zb}"] = common_volume(clip, pu).measured
# sleeve outer radius at mid saddle and sector edges
A = ((0,0,0),(0,0,1),(1,0,0))
for a in (46, 90, 134):
    for z in (0.0, 28.0):
        o[f"sleeve outer r th{a} z{z}"] = radial_extent(sl, *A, a, z, side="outer").measured
        o[f"cradle inner r th{a} z{z}"] = radial_extent(cr, *A, a, z, side="inner").measured
# per-rib contact
for name, zc in (("rib1", 0.0), ("rib2", 28.0)):
    rib = cr & (Pos(0, 25, zc) * Box(50, 20, 6.0))
    o[f"clr {name}|sleeve"] = clearance(rib, sl).measured
    o[f"int {name}|sleeve"] = common_volume(rib, sl).measured
print(json.dumps(o, indent=1)); (W/"reviews/RV02_work/m5_sleeve.json").write_text(json.dumps(o, indent=1))
