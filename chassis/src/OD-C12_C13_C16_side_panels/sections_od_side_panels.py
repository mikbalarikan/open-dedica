"""D6 screening sections of the exported STEPs (tools.drawing.write_sections), into 03_Sections/.

Planes: "top" cuts across Z (an XY section), "front" across Y (an XZ section), "left" across X
(a YZ section). Each picture records nothing_clipped (L-04).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from placements_od_side_panels import OUT, solid_of  # noqa: E402
from tools.core import read_step  # noqa: E402
from tools.drawing import write_sections  # noqa: E402

WS = Path(__file__).resolve().parents[1]
SEC = WS / "03_Sections"

PLAN = [
    # (file, picture name, view, point the plane passes through, what it shows)
    ("od_c13_right_C1_v01.step", "od_c13_right", "top", (115.0, 100.0, -100.0), "wall, rail and lip wedge (E-06, REQ-02)"),
    ("od_c13_right_C1_v01.step", "od_c13_right", "front", (118.0, 50.0, -100.0), "wall at y 50 (REQ-01)"),
    ("od_c13_right_C1_v01.step", "od_c13_right", "left", (118.5, 100.0, -100.0), "wall mid-plane with the three holes"),
    ("od_c13_right_C1_v01.step", "od_c13_right_y200", "front", (118.0, 200.0, -100.0), "wall at y 200 (REQ-01)"),
    ("od_c13_right_C1_v01.step", "od_c13_right_z-262", "top", (118.0, 10.0, -262.0), "through the rear hole (REQ-03)"),
    ("od_c12_left_C1_v01.step", "od_c12_left", "top", (-115.0, 100.0, -100.0), "relief, wall, rail and lip (REQ-04, E-06)"),
    ("od_c12_left_C1_v01.step", "od_c12_left", "front", (-118.0, 30.0, -100.0), "wall at y 30 through the relief (REQ-04)"),
    ("od_c12_left_C1_v01.step", "od_c12_left", "left", (-118.5, 100.0, -100.0), "wall mid-plane: relief edge and holes"),
    ("od_c12_left_C1_v01.step", "od_c12_left_y200", "front", (-118.0, 200.0, -100.0), "wall at y 200 (REQ-01)"),
    ("od_c12_left_C1_v01.step", "od_c12_left_z-15", "top", (-118.0, 10.0, -15.0), "through the middle hole (REQ-03)"),
    ("od_c16_bracket_C1_v01.step", "od_c16_bracket", "top", (-9.5, 8.0, 0.0), "counterbore, hole and insert bore (REQ-05, J-05, D-03b)"),
    ("od_c16_bracket_C1_v01.step", "od_c16_bracket", "front", (-9.5, 10.0, 0.0), "across the insert bore axis (D-05a)"),
    ("od_c16_bracket_C1_v01.step", "od_c16_bracket", "left", (-3.0, 8.0, 0.0), "across the insert bore: its crown (D-03b)"),
    ("od_side_assembly_C1_v01.step", "od_side_assembly_z-15", "top", (0.0, 100.0, -15.0), "machine at z -15: brackets, panels, lips, lid (U-03)"),
    ("od_side_assembly_C1_v01.step", "od_side_assembly_z-262", "top", (0.0, 100.0, -262.0), "machine at z -262: rear brackets (U-03)"),
]


def main():
    cache, log = {}, []
    for fname, name, view, through, what in PLAN:
        if fname not in cache:
            sh = read_step(OUT / fname)
            cache[fname] = solid_of(sh) if "assembly" not in fname else sh
        w = write_sections(cache[fname], SEC, part=name, version=1, views=(view,), through=through)[0]
        nc = w.checks["nothing_clipped"]
        log.append({"png": w.path.name, "sha256": w.sha256, "view": view, "through": through, "shows": what,
                    "nothing_clipped": nc.measured, "status": nc.status})
        print(log[-1], flush=True)
    (WS / "01_CAD" / "results_v01" / "sections_v01.json").write_text(json.dumps(log, indent=1))


if __name__ == "__main__":
    main()
