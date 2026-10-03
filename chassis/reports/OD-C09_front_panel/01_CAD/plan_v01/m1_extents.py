"""D1: placed extents of every reference solid (machine frame)."""
import sys, json; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, BOARD, load
from tools.core import solids, solid_count, brep_valid, naked_edges
from tools.measure import envelope
from build123d import Solid
items = [("OD-C01_base_frame.step", None), ("OD-C05_group_head_carrier.step", HOUSING),
         ("od_g01_assembly_C1_v03.step", HOUSING), ("od_g01_housing_C1_v03.step", HOUSING),
         ("OD-C10_top_panel.step", None), ("OD-C11_back_panel.step", None),
         ("OD-E02_control_board.step", BOARD), ("OD-S03_steam_knob.step", None)]
for name, t in items:
    s = load(name, t)
    print("==", name, "solids", len(solids(s)))
    for i, so in enumerate(solids(s)):
        so = Solid(so)
        bb = so.bounding_box()
        print(f"  [{i}] vol {so.volume:.1f} x {bb.min.X:.2f}..{bb.max.X:.2f} y {bb.min.Y:.2f}..{bb.max.Y:.2f} z {bb.min.Z:.2f}..{bb.max.Z:.2f} valid {so.is_valid}")
