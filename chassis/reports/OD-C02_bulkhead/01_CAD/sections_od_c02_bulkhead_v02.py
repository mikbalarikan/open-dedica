"""Screening sections (PLAYBOOK D6) of the re-imported od_c02_bulkhead v02 and of the
check assembly, through the functional features; nothing clipped (L-04).

Writes 03_Sections/od_c02_bulkhead_v02_<view>_<where>.png and 01_CAD/sections_v02.json
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
PART = "od_c02_bulkhead"

PART_CUTS = [
    ("left", (65.0, 100.0, -135.0), "x65_wall"),          # mid-wall: windows and gables, the six bores, both rails
    ("left", (61.0, 100.0, -135.0), "x61_wet_flanges"),   # the wet-side rail flanges, nothing else
    ("left", (69.0, 100.0, -135.0), "x69_elec_flanges"),  # the electric-side rail flanges, nothing else
    ("top", (65.0, 100.0, -45.0), "z-45_base_bore"),      # base-rail insert bore 1 and the front of window 4
    ("top", (65.0, 100.0, -105.0), "z-105_base_bore"),    # base-rail insert bore 2
    ("top", (65.0, 100.0, -60.0), "z-60_top_bore_w3"),    # top-rail insert bore 1, window 3, window 4
    ("top", (65.0, 100.0, -210.0), "z-210_top_bore"),     # top-rail insert bore 2
    ("top", (65.0, 100.0, -200.0), "z-200_w1"),           # window 1 through the wall
    ("top", (65.0, 100.0, -55.0), "z-55_w4"),             # window 4's centre
    ("top", (65.0, 100.0, -100.0), "z-100_profile"),      # the plain I-profile: rails, wall, faces
    ("front", (65.0, 100.0, -135.0), "y100_wall"),        # REQ-02 at y 100
    ("front", (65.0, 200.0, -135.0), "y200_wall"),        # REQ-02 at y 200
    ("front", (65.0, 150.0, -135.0), "y150_windows"),     # windows 1-3 through the wall
    ("front", (65.0, 60.0, -135.0), "y60_w4"),            # window 4 and the front end
    ("front", (65.0, 3.0, -135.0), "y3_base_bores"),      # the four base-rail insert bores
    ("front", (65.0, 212.0, -135.0), "y212_top_bores"),   # the two top-rail insert bores
]
ASM_CUTS = [
    ("top", (40.0, 100.0, -200.0), "asm_z-200_pump"),     # OD-H01 +X end against the rail and window 1
    ("front", (40.0, 40.0, -135.0), "asm_y40_pump_axis"), # the pump axis height, plate and rail
    ("top", (40.0, 100.0, -50.0), "asm_z-50_carrier"),    # the carrier box against the rail
    ("top", (40.0, 100.0, -45.0), "asm_z-45_screw_path"), # plate hole under base-rail bore 1: the screw path
]


def cut(shape, view, point, tag, log):
    try:
        written = write_sections(shape, SECTIONS, part=PART, version=2, views=(view,), through=point)
    except Exception as exc:  # noqa: BLE001
        log.append({"tag": tag, "view": view, "through": point, "error": f"{type(exc).__name__}: {exc}"})
        return
    for w in written:
        target = SECTIONS / f"{PART}_v02_{view}_{tag}.png"
        Path(w.path).replace(target)
        nc = w.checks["nothing_clipped"]
        log.append({"tag": tag, "view": view, "through": point, "file": str(target.relative_to(WS)),
                    "sha256_at_write": w.sha256, "plane": w.detail.get("plane"),
                    "cut_area_mm2": w.detail.get("cut_area_mm2"), "cut_faces": w.detail.get("cut_faces"),
                    "nothing_clipped": nc.measured, "nothing_clipped_status": nc.status, "reason": nc.reason})


def main():
    log: list = []
    part = read_step(WS / "02_STEP_STL/od_c02_bulkhead_C1_v02.step")
    for view, point, tag in PART_CUTS:
        cut(part, view, point, tag, log)
    asm = read_step(WS / "02_STEP_STL/od_c02_assembly_C1_v02.step")
    for view, point, tag in ASM_CUTS:
        cut(asm, view, point, tag, log)
    (HERE / "sections_v02.json").write_text(json.dumps(log, indent=1, default=str))
    for row in log:
        print({k: row.get(k) for k in ("tag", "file", "cut_area_mm2", "nothing_clipped", "error")})


if __name__ == "__main__":
    main()
