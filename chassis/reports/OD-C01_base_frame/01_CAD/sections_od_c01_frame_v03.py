"""Screening sections (PLAYBOOK D6) of the re-imported od_c01_frame v03 and of the
check assembly, through the functional features; nothing clipped (L-04).

v03 adds cuts through the eighteen new insert holes (REQ-11 .. REQ-14) and through
the OD-C08 tray, the OD-C11 back panel, the OD-C09 front panel and the OD-C16
brackets as placed.

Writes 03_Sections/od_c01_frame_v03_<view>_<where>.png and
01_CAD/sections_v03.json with each picture's hash, plane, cut area and
nothing_clipped reading. View names: "top" cuts across Z, "left" across X,
"front" across Y (tools.drawing.views).
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.core import read_step
from tools.drawing import write_sections

HERE = Path(__file__).resolve().parent
WS = HERE.parent
SECTIONS = WS / "03_Sections"
PART = "od_c01_frame"

PLATE_CUTS = [
    ("top", (0.0, -3.0, -40.0), "z-40_carrier"),        # carrier insert holes (+-35, -40)
    ("top", (0.0, -3.0, -148.0), "z-148_c04"),          # OD-C04 insert holes (+-40, -148)
    ("left", (37.0, -3.0, 0.0), "x37_c03"),             # OD-C03 insert holes at x 37
    ("left", (65.0, -3.0, 0.0), "x65_bulkhead"),        # bulkhead insert line
    ("top", (0.0, -3.0, -120.0), "z-120_drain"),        # drain hole (-80, -120)
    ("top", (0.0, -3.0, 90.0), "z90_feet"),             # front feet holes (+-110, 90)
    ("top", (0.0, -3.0, -42.0), "z-42_valve"),          # OD-C07 front insert pair (-113 / -71, -42)
    ("left", (-113.0, -3.0, 0.0), "x-113_valve"),       # OD-C07 outer insert line, 5.0 web to the edge
    ("front", (0.0, -3.0, 0.0), "y-3_plan"),            # mid-thickness plan: every hole
    ("top", (0.0, -3.0, -222.0), "z-222_tray"),         # OD-C08 rear insert pair (88 / 106, -222)
    ("top", (0.0, -3.0, -78.0), "z-78_tray"),           # OD-C08 front insert pair (88 / 106, -78)
    ("top", (0.0, -3.0, -282.0), "z-282_back"),         # OD-C11 inserts (+-81 / +-95, -282)
    ("top", (0.0, -3.0, 77.0), "z77_front"),            # OD-C09 inserts (+-85 / +-95, +77)
    ("top", (0.0, -3.0, 62.0), "z62_bracket"),          # OD-C16 front bracket inserts (+-104.5, +62)
    ("left", (104.5, -3.0, 0.0), "x104.5_bracket"),     # the right bracket insert line, three holes
]
ASM_CUTS = [
    ("left", (0.0, 50.0, 0.0), "asm_x0"),               # carrier box, OD-C04 + OD-H11, OD-C03 + OD-H01, OD-G01
    ("top", (0.0, 50.0, -148.0), "asm_z-148"),          # OD-C04 foot on the plate, OD-H11 above
    ("left", (37.0, 50.0, 0.0), "asm_x37"),             # OD-C03 foot and holes on the plate
    ("top", (0.0, 100.0, 32.0), "asm_z32_mouth"),       # through the vertical group head axis (0, 32)
    ("top", (0.0, 20.0, -222.0), "asm_z-222_tray"),     # OD-C08 flange on the plate, rear screws
    ("top", (0.0, 20.0, -282.0), "asm_z-282_back"),     # OD-C11 floor flanges on the plate
    ("top", (0.0, 20.0, 77.0), "asm_z77_front"),        # OD-C09 floor flanges on the plate
    ("left", (104.5, 20.0, 0.0), "asm_x104.5_bracket"), # the three right OD-C16 brackets and the tray
]


def cut(shape, view, point, tag, log):
    try:
        written = write_sections(shape, SECTIONS, part=PART, version=3, views=(view,), through=point)
    except Exception as exc:  # noqa: BLE001
        log.append({"tag": tag, "view": view, "through": point, "error": f"{type(exc).__name__}: {exc}"})
        return
    for w in written:
        target = SECTIONS / f"{PART}_v03_{view}_{tag}.png"
        Path(w.path).replace(target)
        nc = w.checks["nothing_clipped"]
        log.append({"tag": tag, "view": view, "through": point, "file": str(target.relative_to(WS)),
                    "sha256_at_write": w.sha256, "plane": w.detail.get("plane"),
                    "cut_area_mm2": w.detail.get("cut_area_mm2"), "cut_faces": w.detail.get("cut_faces"),
                    "nothing_clipped": nc.measured, "nothing_clipped_status": nc.status, "reason": nc.reason})


def main():
    log: list = []
    plate = read_step(WS / "02_STEP_STL/od_c01_frame_C1_v03.step")
    for view, point, tag in PLATE_CUTS:
        cut(plate, view, point, tag, log)
    asm = read_step(WS / "02_STEP_STL/od_c01_assembly_C1_v03.step")
    for view, point, tag in ASM_CUTS:
        cut(asm, view, point, tag, log)
    (HERE / "sections_v03.json").write_text(json.dumps(log, indent=1, default=str))
    for row in log:
        print({k: row.get(k) for k in ("tag", "file", "cut_area_mm2", "nothing_clipped", "error")})


if __name__ == "__main__":
    main()
