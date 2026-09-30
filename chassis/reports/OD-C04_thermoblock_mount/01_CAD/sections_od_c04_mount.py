"""Screening sections (PLAYBOOK D6) of the re-imported od_c04_mount v01 and of the
check assembly, through the functional features; nothing clipped (L-04).

Writes 03_Sections/od_c04_mount_v01_<plane>_<where>.png (and _asm_ for the
assembly) and 01_CAD/check_v01/sections_v01.json with each picture's hash, plane,
cut area and nothing_clipped reading.
"""
from __future__ import annotations

import json
from pathlib import Path

from build123d import Compound

from tools.core import read_step
from tools.drawing import write_sections

HERE = Path(__file__).resolve().parent
WS = HERE.parent
SECTIONS = WS / "03_Sections"
PART = "od_c04_mount"

# (view, point the plane passes through, where-tag): the plane is normal to the view
MOUNT_CUTS = [
    ("left", (-19.62, 0.0, 0.0), "xS1"),      # through the S1 standoff and bore axis
    ("left", (25.01, 0.0, 0.0), "xS2"),       # through the S2 standoff and bore axis
    ("left", (46.0, 0.0, 0.0), "xGusset"),    # through the +X gusset
    ("left", (40.0, 0.0, 0.0), "xFrameHoles"),  # along the +X frame holes
    ("front", (0.0, -68.0, 0.0), "yFoot"),    # across the foot: the four teardrop holes
    ("top", (0.0, 0.0, -11.0), "zStandoffs"),  # across the standoffs, gussets and foot
]
ASM_CUTS = [
    ("left", (-19.62, 0.0, 0.0), "asm_xS1"),
    ("left", (25.01, 0.0, 0.0), "asm_xS2"),
]


def cut(shape, view, point, tag, log):
    try:
        written = write_sections(shape, SECTIONS, part=PART, version=1, views=(view,), through=point)
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
                    "nothing_clipped": nc.measured, "nothing_clipped_status": nc.status,
                    "reason": nc.reason})


def main():
    log: list = []
    mount = read_step(WS / "02_STEP_STL/od_c04_mount_C1_v01.step")
    for view, point, tag in MOUNT_CUTS:
        cut(mount, view, point, tag, log)
    asm = read_step(WS / "02_STEP_STL/od_c04_assembly_C1_v01.step")
    for view, point, tag in ASM_CUTS:
        cut(asm, view, point, tag, log)
    (HERE / "check_v01").mkdir(exist_ok=True)
    (HERE / "check_v01/sections_v01.json").write_text(json.dumps(log, indent=1, default=str))
    for row in log:
        print(row)


if __name__ == "__main__":
    main()
