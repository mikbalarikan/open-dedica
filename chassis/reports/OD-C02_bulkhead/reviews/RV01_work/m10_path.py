import json
import numpy as np
from pathlib import Path
from build123d import Box, Cylinder, Pos, Rot, Solid
from OCP.gp import gp_Trsf
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from tools.core.step import read_step
from tools.core.shapes import solids
from tools.core.boolean import common_volume
from tools.measure import clearance
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); I = J/"00_Spec/inputs"; W = J/"reviews/RV01_work"
def place(p, M, t):
    tr = gp_Trsf(); M = np.array(M, float).T; tr.SetValues(*M[0], t[0], *M[1], t[1], *M[2], t[2])
    return Solid(BRepBuilderAPI_Transform(solids(read_step(I/p))[0], tr, True).Shape())
I3 = [(1,0,0),(0,1,0),(0,0,1)]; RP = [(0,0,1),(0,-1,0),(1,0,0)]
nb = {"od_c01": place("OD-C01_base_frame.step", I3, (0,0,0)), "od_c03": place("OD-C03_pump_cradle.step", RP, (0,40,-205)),
      "od_h01": place("OD-H01_ulka_ep5_pump.step", RP, (0,40,-205)), "od_c04": place("OD-C04_thermoblock_mount.step", I3, (0,70,-140)),
      "od_h11": place("OD-H11_thermoblock.step", I3, (0,70,-140)), "od_g01": place("OD-G01_housing_C1_v02.step", [(1,0,0),(0,0,1),(0,-1,0)], (0,180.06,32)),
      "c05_box": Pos(0,105,-48) * Box(110,210,44)}
out = {}
# the path: the bulkhead lowered along -Y from above everything; sweep of its footprint box from y 0.001 to y 500
sweep = Pos(65, 250.0005, -135) * Box(12, 499.999, 210)
out["path_box"] = {k: (clearance(sweep, v).measured, clearance(sweep, v).at) for k, v in nb.items() if k != "od_c01"}
# the rail's first contact with the plate: sweep over the plate at 0.001 above
# screw path from below at each hole: M3 x 12 shank y -6..6, head D5.5 x 3 at y -9..-6, driver D6 y -80..-9
sc = {}
part = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
for z in (-45, -105, -165, -225):
    shank = Pos(65, 0, z) * Rot(90, 0, 0) * Cylinder(1.5, 12)
    head = Pos(65, -7.5, z) * Rot(90, 0, 0) * Cylinder(2.75, 3)
    drv = Pos(65, -44.5, z) * Rot(90, 0, 0) * Cylinder(3.0, 71)
    sc[z] = {"shank_plate_mm3": common_volume(shank, nb["od_c01"]).measured, "shank_part_mm3": common_volume(shank, part).measured,
             "shank_tip_to_floor_mm": 6.0 - 6.0,
             "head_plate_mm3": common_volume(head, nb["od_c01"]).measured, "head_plate_gap": clearance(head, nb["od_c01"]).measured,
             "driver": {k: round(clearance(drv, v).measured, 3) for k, v in nb.items()}}
out["screws"] = sc
(W/"m10_path.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, indent=0, default=str))
