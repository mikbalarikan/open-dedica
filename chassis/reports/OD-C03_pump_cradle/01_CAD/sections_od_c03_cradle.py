"""D6 screening sections of od_c03_cradle v01 from the exported STEP files.

Each plane is written by tools.drawing.write_sections into a scratch folder and
moved to 03_Sections/<part>_v01_<plane>.png; nothing_clipped is recorded per picture.
"""
import json
import shutil
import sys
import tempfile
from pathlib import Path

from build123d import Compound

from tools.core import read_step
from tools.drawing import write_sections

WS = Path(__file__).resolve().parents[1]
OUT = WS / "03_Sections"
PART = "od_c03_cradle"
cradle = read_step(WS / "02_STEP_STL/od_c03_cradle_C1_v01.step")
asm = read_step(WS / "02_STEP_STL/od_c03_assembly_C1_v01.step")

PLANES = [  # (file plane name, view, through point, shape)
    ("xy_z18p0", "top", (0.0, 20.0, 18.0), cradle),
    ("xy_z28p0", "top", (0.0, 20.0, 28.0), cradle),
    ("yz_x0p0", "left", (0.0, 20.0, 16.0), cradle),
    ("yz_x31p5", "left", (31.5, 20.0, 16.0), cradle),
    ("yz_x34p0", "left", (34.0, 38.5, 16.0), cradle),
    ("xz_y7p0", "front", (0.0, 7.0, 16.0), cradle),
    ("xz_y38p5", "front", (0.0, 38.5, 16.0), cradle),
    ("assembly_xy_z18p0", "top", (0.0, 0.0, 18.0), asm),
    ("assembly_yz_x0p0", "left", (0.0, 0.0, 16.0), asm),
]
log = {}
for name, view, through, shape in PLANES:
    with tempfile.TemporaryDirectory() as tmp:
        try:
            w = write_sections(shape, tmp, part=PART, version=1, views=(view,), through=through)[0]
        except Exception as exc:  # noqa: BLE001
            log[name] = {"error": f"{type(exc).__name__}: {exc}"}
            print(name, "ERROR", exc)
            continue
        dest = OUT / f"{PART}_v01_{name}.png"
        shutil.move(str(w.path), dest)
        nc = w.checks["nothing_clipped"]
        log[name] = {"file": str(dest.relative_to(WS)), "sha256": w.sha256, "plane": w.detail["plane"],
                     "cut_area_mm2": w.detail["cut_area_mm2"], "nothing_clipped": nc.measured,
                     "status": nc.status, "reason": nc.reason}
        print(name, w.sha256, w.detail["plane"], nc.measured, nc.status)
(WS / "01_CAD/sections_od_c03_cradle_v01.json").write_text(json.dumps(log, indent=1, default=str))
