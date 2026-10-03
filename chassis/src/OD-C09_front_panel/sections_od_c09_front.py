"""D6 screening sections of od_c09_front v01, cut from the re-imported STEP (tools.drawing.write_sections).
Each picture is renamed 03_Sections/od_c09_front_v01_<plane>.png; nothing_clipped is gated == 0.
The x -91 and y 153.2 / 127.3 planes are also cut with the posed OD-E02 beside the panel (suffix _with_E02)."""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from build123d import Compound, Solid

from tools.core import read_step, solids
from tools.drawing import write_sections

HERE = Path(__file__).resolve().parent
WS = HERE.parent
sys.path.insert(0, str(HERE))
from check_od_c09_front import load_refs  # noqa: E402

STEP = WS / "02_STEP_STL" / "od_c09_front_C1_v01.step"
OUT = WS / "03_Sections"
# (plane name, view, a point the plane passes through)
PLANES = [
    ("z95p5", "top", (0.0, 100.0, 95.5)),        # opening outline, button holes (REQ-03, REQ-04)
    ("z89p0", "top", (0.0, 100.0, 89.0)),        # ribs, bosses, flanges, gussets behind the wall (E-06)
    ("y100", "front", (0.0, 100.0, 90.0)),       # wall planes (REQ-02)
    ("y200", "front", (0.0, 200.0, 90.0)),       # wall planes on the top bar (REQ-02)
    ("y2p0", "front", (0.0, 2.0, 90.0)),         # flanges and flange holes (REQ-01)
    ("y153p2", "front", (0.0, 153.2349, 90.0)),  # upper boss, insert bore, relief
    ("y127p3", "front", (0.0, 127.2515, 90.0)),  # lower boss, insert bore, relief
    ("x-95", "left", (-95.0, 100.0, 90.0)),      # flange hole, button holes
    ("x-85", "left", (-85.0, 100.0, 90.0)),      # flange hole
    ("x85", "left", (85.0, 100.0, 90.0)),
    ("x95", "left", (95.0, 100.0, 90.0)),
    ("x-78", "left", (-78.0, 100.0, 90.0)),      # inner left gusset and R4 / R5 (E-06, D-03a)
    ("x102", "left", (102.0, 100.0, 90.0)),      # outer right gusset (E-06, D-03a)
    ("x-91", "left", (-91.03, 140.0, 90.0)),     # both bosses, insert bores (E-06, D-05)
    ("x36", "left", (36.0, 100.0, 90.0)),        # top bar and R1 where the handle passes
]
WITH_BOARD = {"x-91", "y153p2", "y127p3"}


def main():
    panel = Solid(solids(read_step(STEP))[0])
    board = load_refs()["E02"]
    OUT.mkdir(parents=True, exist_ok=True)
    log = []
    with tempfile.TemporaryDirectory() as tmp:
        for name, view, through in PLANES:
            for suffix, shape in (("", panel), ("_with_E02", None)):
                if suffix and name not in WITH_BOARD:
                    continue
                if suffix:
                    shape = Compound([Solid(panel.wrapped), Solid(board.wrapped)])
                try:
                    w = write_sections(shape, Path(tmp), part=f"s{name}{suffix}", version=1, views=(view,), through=through)[0]
                except Exception as exc:  # noqa: BLE001
                    log.append({"plane": name + suffix, "error": f"{type(exc).__name__}: {exc}"})
                    continue
                dest = OUT / f"od_c09_front_v01_{name}{suffix}.png"
                Path(w.path).replace(dest)
                nc = w.checks["nothing_clipped"]
                log.append({"plane": name + suffix, "file": dest.name, "sha256": w.sha256, "view": view,
                            "through": through, "nothing_clipped": nc.measured, "status": nc.status,
                            "cut_area_mm2": w.detail.get("cut_area_mm2")})
    (HERE / "sections_v01.json").write_text(json.dumps(log, indent=1))
    for row in log:
        print(row)


if __name__ == "__main__":
    main()
