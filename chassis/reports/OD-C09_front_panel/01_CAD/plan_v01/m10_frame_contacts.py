"""D1: soundness of every reference solid; the planned panel against OD-C01, OD-C10, OD-C05,
the housing, OD-G04 and the OD-C15 keep-outs at the seat; driver axes."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, BOARD, load
from standin import panel, box, cyl_z
from build123d import Solid, Compound, Pos, Cylinder, Rot
from tools.core import solids, brep_valid, common_volume
from tools.measure import clearance
refs = {"C01": solids(load("OD-C01_base_frame.step"))[0], "C10": solids(load("OD-C10_top_panel.step"))[0],
        "C05": solids(load("OD-C05_group_head_carrier.step", HOUSING))[0]}
asm = solids(load("od_g01_assembly_C1_v03.step", HOUSING))
refs["housing"], refs["G04"] = asm[0], asm[1]
refs["E02"] = solids(load("OD-E02_control_board.step", BOARD))[0]
for k, v in refs.items():
    r = brep_valid(v); print("brep_valid", k, r.measured, r.detail.get("bop_faults"))
parts = panel([(-94.248, 166.514, 15.0), (-98.991, 139.901, 15.0), (-93.765, 113.426, 15.0)],
              [(-91.055, 153.235), (-90.999, 127.251)], (85.485, 85.485))
pan = Compound(list(parts.values()))
for k in ("C01", "C10", "C05", "housing", "G04"):
    r = clearance(pan, refs[k]); print(f"panel-{k} clearance {r.measured:.3f} at {r.at}")
for x in (-110, 110):
    ko = cyl_z(0, 0, 4.0, 0, 2.0)  # placeholder replaced below
    ko = Pos(x, 1.0, 90) * Rot(90, 0, 0) * Cylinder(4.0, 2.0)
    r = clearance(pan, ko); print(f"panel-keepout({x}) clearance {r.measured:.3f} at {r.at}")
for (x, z, y0) in [(-95, 77, 4), (-85, 77, 4), (85, 77, 4), (95, 77, 4), (-110, 90, 2), (110, 90, 2)]:
    d = Pos(x, (y0+260)/2, z) * Rot(90, 0, 0) * Cylinder(3.0, 260-y0)
    r = clearance(pan, d); print(f"driver ({x},{z}) clearance {r.measured:.3f} at {r.at}")
print("lowering, panel vs C01/C05/housing/G04 (G10 in the sweep script):")
for dy in range(40, -1, -10):
    moved = Pos(0, dy, 0) * pan
    print("  dy", dy, [f"{k} {clearance(moved, refs[k]).measured:.2f}" for k in ("C01", "C05", "housing", "G04")])
