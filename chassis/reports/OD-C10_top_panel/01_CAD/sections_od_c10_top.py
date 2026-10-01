"""D6 screening sections of od_c10_top v01 from the re-imported STEP, and of the check
assembly at the seats, the pads and the rear corners. Names carry _v01; nothing clipped
is measured on each picture. Paths relative to the workspace (pathlib).

Usage: uv run tools/run.py python <ws>/01_CAD/sections_od_c10_top.py"""
import json
from pathlib import Path

from tools.core import read_step
from tools.drawing import write_sections

WS = Path(__file__).resolve().parent.parent
OUT = WS / "03_Sections"
STEP = WS / "02_STEP_STL" / "od_c10_top_C1_v01.step"
ASM = WS / "02_STEP_STL" / "od_c10_assembly_C1_v01.step"

# (name, view, point): front cuts at y, top at z, left at x
CUTS = [
    ("od_c10_top_cols_x65", "left", (65.0, 232.0, -135.0)),           # both bulkhead column axes
    ("od_c10_top_col_z-60", "top", (0.0, 232.0, -60.0)),              # bulkhead column 1 axis, its two ribs
    ("od_c10_top_col_z-210", "top", (0.0, 232.0, -210.0)),            # bulkhead column 2 axis, its two ribs
    ("od_c10_top_cols_z-293", "top", (0.0, 232.0, -293.0)),           # both rear column axes
    ("od_c10_top_col_x90", "left", (90.0, 232.0, -150.0)),            # rear column (+X) axis, pocket, skirt
    ("od_c10_top_col_x-90", "left", (-90.0, 232.0, -150.0)),          # rear column (-X) axis
    ("od_c10_top_rearrib_x94", "left", (94.0, 232.0, -150.0)),        # a rear rib into the rear skirt
    ("od_c10_top_pads_z30", "top", (0.0, 232.0, 30.0)),               # both rest pads, the headroom over the hub
    ("od_c10_top_plan_y230", "front", (0.0, 230.0, -102.5)),          # skirt, columns, ribs, pads in plan
    ("od_c10_top_holes_y216p5", "front", (0.0, 216.5, -102.5)),       # the four through-holes, skirt bottom band
    ("od_c10_top_skin_y248p5", "front", (0.0, 248.5, -102.5)),        # the skin and the four counterbores
]
ASM_CUTS = [
    ("od_c10_assembly_cols_x65", "left", (65.0, 200.0, -135.0)),      # bulkhead columns on OD-C02's rail
    ("od_c10_assembly_cols_z-293", "top", (0.0, 200.0, -293.0)),      # rear columns on OD-C11's ledge
    ("od_c10_assembly_pads_z30", "top", (0.0, 200.0, 30.0)),          # pads 0.5 over OD-C05's plate
    ("od_c10_assembly_corner_z-300p5", "top", (0.0, 200.0, -300.5)),  # rear corners: skirt arc over OD-C11's wall top
    ("od_c10_assembly_corner_x113", "left", (113.0, 200.0, -150.0)),  # through the +X corner contact patch
]
rows = []
part = read_step(STEP)
for name, view, pt in CUTS:
    for w in write_sections(part, OUT, part=name, version=1, views=(view,), through=pt):
        c = w.checks["nothing_clipped"]
        rows.append({"file": str(w.path.relative_to(WS)), "sha256": w.sha256, **w.detail,
                     "nothing_clipped": c.measured, "status": c.status})
asm = read_step(ASM)
for name, view, pt in ASM_CUTS:
    for w in write_sections(asm, OUT, part=name, version=1, views=(view,), through=pt):
        c = w.checks["nothing_clipped"]
        rows.append({"file": str(w.path.relative_to(WS)), "sha256": w.sha256, **w.detail,
                     "nothing_clipped": c.measured, "status": c.status})
(WS / "01_CAD" / "sections_v01.json").write_text(json.dumps(rows, indent=1, default=str))
print(json.dumps([{k: r[k] for k in ("file", "nothing_clipped", "status")} for r in rows], indent=1))
