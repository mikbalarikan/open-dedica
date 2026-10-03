"""Screening sections (PLAYBOOK D6) of the re-imported od_c08_tray v01 and of the
check assembly, through the functional features; nothing clipped (L-04).

Writes 03_Sections/od_c08_tray_v01_<view>_<where>.png and 01_CAD/sections_v01.json
with each picture's hash, plane, cut area and nothing_clipped reading. View names:
"top" cuts across Z, "left" across X, "front" across Y (tools.drawing.views).
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.core import read_step
from tools.drawing import write_sections

HERE = Path(__file__).resolve().parent
WS = HERE.parent
SECTIONS = WS / "03_Sections"
PART = "od_c08_tray"

PART_CUTS = [
    ("top", (90.0, 50.0, -100.0), "z-100_H1_H2_inserts"),     # both insert standoffs and bores, wall, flange
    ("top", (90.0, 50.0, -157.515), "z-157.5_H5_H6_pins"),    # both pin standoffs and pins
    ("top", (90.0, 50.0, -222.0), "z-222_rear_holes"),        # the rear flange holes across their axes
    ("top", (90.0, 50.0, -78.0), "z-78_front_holes"),         # the front flange holes
    ("top", (90.0, 50.0, -86.5), "z-86.5_gusset"),            # a gusset in profile
    ("top", (90.0, 50.0, -168.0), "z-168_tie_slot"),          # a tie slot through the wall
    ("left", (74.5, 50.0, -150.0), "x74.5_wall"),             # mid-wall: the four tie slots
    ("left", (79.4, 50.0, -150.0), "x79.4_standoffs"),        # the four standoffs and the insert bores mid-depth
    ("left", (83.5, 50.0, -150.0), "x83.5_pins"),             # the two pins above the seat
    ("front", (90.0, 2.0, -150.0), "y2_flange"),              # the flange and its four holes
    ("front", (90.0, 88.0, -150.0), "y88_slots"),             # the slots' height
    ("front", (90.0, 80.0, -150.0), "y80_H1_H5"),             # H1 insert and H5 pin standoffs along their axes
]
ASM_CUTS = [
    ("top", (90.0, 50.0, -100.0), "asm_z-100_board_H1_H2"),   # board on the insert standoffs, bulkhead, plate
    ("top", (90.0, 50.0, -157.515), "asm_z-157.5_board_pins"),  # board on the pin standoffs, pins in H5 and H6
    ("front", (90.0, 80.0, -150.0), "asm_y80_board_H1_H5"),   # board seated, along the axes of H1 and H5
    ("top", (90.0, 50.0, -222.0), "asm_z-222_screw_path"),    # flange hole over the plate: the screw and driver path
]


def cut(shape, view, point, tag, log, part=PART):
    try:
        written = write_sections(shape, SECTIONS, part=part, version=1, views=(view,), through=point)
    except Exception as exc:  # noqa: BLE001
        log.append({"tag": tag, "view": view, "through": point, "error": f"{type(exc).__name__}: {exc}"})
        return
    for w in written:
        target = SECTIONS / f"{PART}_v01_{view}_{tag}.png"
        Path(w.path).replace(target)
        nc = w.checks["nothing_clipped"]
        log.append({"tag": tag, "view": view, "through": point, "file": str(target.relative_to(WS)),
                    "sha256_at_write": w.sha256, "plane": w.detail.get("plane"),
                    "cut_area_mm2": w.detail.get("cut_area_mm2"), "cut_faces": w.detail.get("cut_faces"),
                    "nothing_clipped": nc.measured, "nothing_clipped_status": nc.status, "reason": nc.reason})


def main():
    log: list = []
    part = read_step(WS / "02_STEP_STL/od_c08_tray_C1_v01.step")
    for view, point, tag in PART_CUTS:
        cut(part, view, point, tag, log)
    asm = read_step(WS / "02_STEP_STL/od_c08_assembly_C1_v01.step")
    for view, point, tag in ASM_CUTS:
        cut(asm, view, point, tag, log)
    (HERE / "sections_v01.json").write_text(json.dumps(log, indent=1, default=str))
    for row in log:
        print({k: row.get(k) for k in ("tag", "file", "cut_area_mm2", "nothing_clipped", "error")})


if __name__ == "__main__":
    main()
