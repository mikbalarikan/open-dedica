"""sections_od_g01_v01.py - D6: the screening sections, from the exported STEP.

Cuts through the functional features with nothing clipped (L-04): the cup axis in
two planes, a plan cut through the lugs, a cut along a stop block, and a cut
through a carrier insert boss. A plane is put on a feature by turning a copy of
the part about its own axis, so every picture still shows the part in its own
frame with the plane named.

Run: uv run tools/run.py python 01_CAD/sections_od_g01_v01.py
"""
from __future__ import annotations

import json
from pathlib import Path

from build123d import Rot

from tools.core import read_step
from tools.drawing import write_sections

WORKSPACE = Path(__file__).resolve().parents[1]
STEP = WORKSPACE / "02_STEP_STL" / "od_g01_housing_C1_v01.step"
SECTIONS = WORKSPACE / "03_Sections"
VERSION = 1

LUG1_START = 336.0
STOP_CENTRE = LUG1_START + 2.9          # A-06: the stop block of lug 1
BOSS_DIAGONAL = 45.0                    # the carrier inserts sit at (+-44, +-44)


def main():
    part = read_step(STEP)
    written = []
    written += write_sections(part, SECTIONS, part="od_g01_housing", version=VERSION,
                              views=("front", "top", "left"))
    written += write_sections(Rot(Z=-STOP_CENTRE) * part, SECTIONS,
                              part="od_g01_housing_stopblock", version=VERSION, views=("front",))
    written += write_sections(Rot(Z=-BOSS_DIAGONAL) * part, SECTIONS,
                              part="od_g01_housing_insertboss", version=VERSION, views=("front",))
    out = [{"file": str(w.path.relative_to(WORKSPACE)), "sha256": w.sha256,
            "detail": w.detail,
            "nothing_clipped": w.checks["nothing_clipped"].measured,
            "reason": w.checks["nothing_clipped"].reason} for w in written]
    (WORKSPACE / "01_CAD" / f"sections_v{VERSION:02d}.json").write_text(
        json.dumps(out, indent=1, default=str), encoding="utf-8")
    for row in out:
        print(row["file"], row["nothing_clipped"], row["detail"].get("plane"))


if __name__ == "__main__":
    main()
