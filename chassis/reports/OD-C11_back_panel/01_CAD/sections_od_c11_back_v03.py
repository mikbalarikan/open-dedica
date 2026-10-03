"""D6 screening sections of od_c11_back v03 from the re-imported STEP (and one of the
check assembly through an OD-C01 feet hole). Names carry _v03; nothing clipped is
measured on each picture. Paths relative to the workspace (pathlib).

Usage: uv run tools/run.py python <ws>/01_CAD/sections_od_c11_back_v03.py"""
import json
from pathlib import Path

from tools.core import read_step
from tools.drawing import write_sections

WS = Path(__file__).resolve().parent.parent
OUT = WS / "03_Sections"
STEP = WS / "02_STEP_STL" / "od_c11_back_C1_v03.step"
ASM = WS / "02_STEP_STL" / "od_c11_assembly_C1_v03.step"

# (name, view, point): front cuts at y, top at z, left at x
CUTS = [
    ("od_c11_back_wall_z300p5", "top", (0.0, 107.5, -300.5)),       # every hole and slot through the wall
    ("od_c11_back_gussets_z290", "top", (0.0, 107.5, -290.0)),      # gussets, bosses, ledge in front of the wall
    ("od_c11_back_flanges_y2", "front", (0.0, 2.0, -289.0)),        # flanges and the four flange holes
    ("od_c11_back_passthroughs_y30", "front", (0.0, 30.0, -295.0)), # cord and tube holes against the gussets
    ("od_c11_back_wall_y50", "front", (0.0, 50.0, -300.0)),         # REQ-02 at y 50
    ("od_c11_back_vents_y140", "front", (0.0, 140.0, -300.0)),      # the five slots
    ("od_c11_back_wall_y200", "front", (0.0, 200.0, -300.0)),       # REQ-02 at y 200
    ("od_c11_back_bosses_y207", "front", (0.0, 207.0, -293.0)),     # bosses under the ledge
    ("od_c11_back_ledge_y213", "front", (0.0, 213.0, -293.0)),      # ledge and the two insert bores
    ("od_c11_back_insert_x90", "left", (90.0, 107.5, -293.0)),      # boss, bore, ledge, wall
    ("od_c11_back_hole_x95", "left", (95.0, 107.5, -290.0)),        # flange hole along Y, cord hole, driver path
    ("od_c11_back_hole_x81", "left", (81.0, 107.5, -290.0)),        # inner flange hole, driver path past the ledge
    ("od_c11_back_gusset_x102", "left", (102.0, 107.5, -290.0)),    # outer gusset (+X), cord hole edge
    ("od_c11_back_gusset_x74", "left", (74.0, 107.5, -290.0)),      # inner gusset, flange
    ("od_c11_back_gusset_xm102", "left", (-102.0, 107.5, -290.0)),  # outer gusset (-X) across the tube hole
    ("od_c11_back_tube_xm100", "left", (-100.0, 107.5, -290.0)),    # tube hole axis at the gusset face
    # v03 (brief WP-04): one through each pass-through and its nearest gusset
    ("od_c11_back_cord_gusset_x100p5", "left", (100.5, 107.5, -290.0)),    # cord hole (x 89 .. 101) and the +X outer gusset
    ("od_c11_back_tube_gusset_xm101", "left", (-101.0, 107.5, -290.0)),    # tube hole (x -106 .. -94) and the -X outer gusset
    ("od_c11_back_tube84_gusset_y30", "front", (-80.0, 30.0, -297.0)),     # tube hole (x -90 .. -78) and the -X inner gusset (x -76 .. -72)
]
rows = []
part = read_step(STEP)
for name, view, pt in CUTS:
    for w in write_sections(part, OUT, part=name, version=3, views=(view,), through=pt):
        c = w.checks["nothing_clipped"]
        rows.append({"file": str(w.path.relative_to(WS)), "sha256": w.sha256, **w.detail,
                     "nothing_clipped": c.measured, "status": c.status})
asm = read_step(ASM)
for name, view, pt in [("od_c11_assembly_feethole_x110", "left", (110.0, 0.0, -295.0))]:
    for w in write_sections(asm, OUT, part=name, version=3, views=(view,), through=pt):
        c = w.checks["nothing_clipped"]
        rows.append({"file": str(w.path.relative_to(WS)), "sha256": w.sha256, **w.detail,
                     "nothing_clipped": c.measured, "status": c.status})
(WS / "01_CAD" / "sections_v03.json").write_text(json.dumps(rows, indent=1, default=str))
print(json.dumps(rows, indent=1, default=str))
