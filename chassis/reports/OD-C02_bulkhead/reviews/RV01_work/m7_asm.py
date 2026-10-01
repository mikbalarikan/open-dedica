import json, math
import numpy as np
from pathlib import Path
from build123d import Box, Pos, Location, Solid, Compound
from OCP.gp import gp_Trsf, gp_Mat, gp_XYZ
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from tools.core.step import read_step, labels
from tools.core.shapes import solids, volume_mm3
from tools.core.validity import validity, brep_valid
from tools.core.boolean import common_volume
from tools.measure import clearance, bore_census, locate_bore
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); I = J/"00_Spec/inputs"; W = J/"reviews/RV01_work"
def d(r): return r.to_dict()
def place(shape, cols, t):
    tr = gp_Trsf()
    M = np.array(cols, float).T   # columns are images of local x, y, z
    tr.SetValues(*M[0], t[0], *M[1], t[1], *M[2], t[2])
    return Solid(BRepBuilderAPI_Transform(solids(shape)[0] if len(solids(shape)) == 1 else shape.wrapped, tr, True).Shape()) if len(solids(shape)) == 1 else Compound(BRepBuilderAPI_Transform(shape.wrapped, tr, True).Shape())
def bbox(sh):
    b = Bnd_Box(); BRepBndLib.Add_s(sh.wrapped if hasattr(sh, "wrapped") else sh, b); return [round(v, 3) for v in b.Get()]
I3 = [(1,0,0),(0,1,0),(0,0,1)]
mine = {
 "od_c01": place(read_step(I/"OD-C01_base_frame.step"), I3, (0,0,0)),
 "od_c03": place(read_step(I/"OD-C03_pump_cradle.step"), [(0,0,1),(0,-1,0),(1,0,0)], (0,40,-205)),
 "od_h01": place(read_step(I/"OD-H01_ulka_ep5_pump.step"), [(0,0,1),(0,-1,0),(1,0,0)], (0,40,-205)),
 "od_c04": place(read_step(I/"OD-C04_thermoblock_mount.step"), I3, (0,70,-140)),
 "od_h11": place(read_step(I/"OD-H11_thermoblock.step"), I3, (0,70,-140)),
 "od_g01": place(read_step(I/"OD-G01_housing_C1_v02.step"), [(1,0,0),(0,0,1),(0,-1,0)], (0,180.06,32)),
}
mine["c05_box"] = Pos(0, 105, -48) * Box(110, 210, 44)
part = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
asm = read_step(J/"02_STEP_STL/od_c02_assembly_C1_v02.step")
out = {"asm_labels": labels(asm), "asm_solids": len(solids(asm))}
# assembly solids: label, volume, bbox
asm_rows = []
def walk(n):
    ch = list(getattr(n, "children", ()) or ())
    if ch:
        for c in ch: walk(c)
    else:
        asm_rows.append((getattr(n, "label", ""), n))
walk(asm)
out["asm"] = [{"label": l, "vol": round(volume_mm3(n), 3), "bbox": bbox(n), "solids": len(solids(n))} for l, n in asm_rows]
out["mine"] = {k: {"vol": round(volume_mm3(v), 3), "bbox": bbox(v)} for k, v in mine.items()}
out["part"] = {"vol": round(volume_mm3(part), 3), "bbox": bbox(part)}
out["valid"] = {k: {kk: (vv.measured, vv.reason) for kk, vv in validity(v).items()} for k, v in mine.items()}
# clearances and interference on my own placements
cl, it = {}, {}
for k, v in mine.items():
    c = clearance(part, v); cl[k] = {"mm": c.measured, "at": c.at, "on_b": c.detail.get("on_b"), "inside": c.detail.get("inside"), "status": c.status, "reason": c.reason}
    cv = common_volume(part, v); it[k] = {"mm3": cv.measured, "status": cv.status, "reason": cv.reason}
out["clearance"] = cl; out["interference"] = it
# coaxiality: plate holes vs bulkhead bores
pc = bore_census(mine["od_c01"]); bc = bore_census(part)
co = {}
for z in (-45, -105, -165, -225):
    b = locate_bore(bc, (65, 3, z), (0, 1, 0))
    # plate hole located at the bulkhead bore's axis point 3 below the top face -> offset = axis distance
    p = locate_bore(pc, (65 + 0, -3, z), (0, 1, 0))
    pb = [x for x in pc.detail["bores"] if abs(x["start"][0]-65) < 1 and abs(x["start"][2]-z) < 1]
    co[z] = {"plate": {k: (v.measured, v.at) for k, v in p.items()}, "plate_bore": pb,
             "bulk_axis": [x for x in bc.detail["bores"] if abs(x["start"][2]-z) < 0.5]}
out["coax"] = co
(W/"m7_asm.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps({k: out[k] for k in ("asm_labels","asm_solids","part","clearance","interference")}, default=str, indent=0))
for r in out["asm"]: print(r)
for k, v in out["mine"].items(): print(k, v)
print(out["valid"])
for z, c in co.items(): print(z, c["plate"], c["plate_bore"])
