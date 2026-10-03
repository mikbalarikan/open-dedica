"""D6 screening sections of od_t01_rig v01 (and the check assembly where named), from
the exported STEP files. Planes: z 0 and z +44 (with the housing set), x +44, y 5,
y 142.5. Pictures go to 03_Sections/od_t01_rig_v01_<plane>.png.

Usage (repo root, tools venv): uv run tools/run.py python <ws>/01_CAD/sections_od_t01_rig.py [--tag v01]
"""
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path

from tools.core import read_step
from tools.drawing import write_sections

WS = Path(__file__).resolve().parent.parent

PLANES = [  # (plane name, view whose plane is cut, a point on the plane, with the housing set)
    ("z0_assembly", "top", (0.0, 75.0, 0.0), True),
    ("z44_assembly", "top", (0.0, 75.0, 44.0), True),
    ("x44", "left", (44.0, 75.0, 0.0), False),
    ("y5", "front", (0.0, 5.0, 0.0), False),
    ("y142", "front", (0.0, 142.5, 0.0), False),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="v01")
    a = ap.parse_args()
    version = int(a.tag.lstrip("v"))
    rig = read_step(WS / "02_STEP_STL" / f"od_t01_rig_C1_{a.tag}.step")
    asm = read_step(WS / "02_STEP_STL" / f"od_t01_assembly_C1_{a.tag}.step")
    out = WS / "03_Sections"
    out.mkdir(exist_ok=True)
    record = []
    for plane, view, through, with_set in PLANES:
        shape = asm if with_set else rig
        with tempfile.TemporaryDirectory() as tmp:
            try:
                written = write_sections(shape, tmp, part="od_t01_rig", version=version, views=(view,),
                                         through=through)
            except Exception as exc:  # noqa: BLE001
                record.append({"plane": plane, "error": f"{type(exc).__name__}: {exc}"})
                print(plane, "ERROR", exc)
                continue
            w = written[0]
            dest = out / f"od_t01_rig_{a.tag}_{plane}.png"
            shutil.copyfile(w.path, dest)
            nc = w.checks["nothing_clipped"]
            record.append({"plane": plane, "file": dest.name, "view": view, "through": through,
                           "nothing_clipped": nc.measured, "status": nc.status, "reason": nc.reason})
            print(plane, dest.name, "nothing_clipped", nc.measured, nc.status)
    (WS / "01_CAD" / f"sections_{a.tag}.json").write_text(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
