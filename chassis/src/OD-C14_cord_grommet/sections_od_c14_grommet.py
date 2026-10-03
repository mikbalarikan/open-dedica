"""D6 screening sections of od_c14_grommet_half v01 and of its check assembly, from the
re-imported STEP files (tools.drawing.write_sections; nothing_clipped on each picture).
OD-C11 and OD-C01 are clipped to a 40 × 63 × 30 mm box around the cord hole so the
pictures stay readable; the clip holds every part of the grommet, the cord and tie
envelopes in the box, and the nearest OD-C11 features (outer gusset, floor flange)."""
from __future__ import annotations

import json
from pathlib import Path

from build123d import Box, Compound, Pos

from tools.core import read_step
from tools.drawing import write

HERE = Path(__file__).resolve().parent
WS = HERE.parent
THROUGH = (95.0, 32.0, -296.6)     # x on the cord axis; y across the upper half; z across the groove and tie


def labelled(shape, label):
    for child in shape.children:
        if child.label == label:
            return child.solids()[0]
    raise ValueError(label)


def main():
    half = read_step(WS / "02_STEP_STL/od_c14_grommet_half_C1_v01.step").solids()[0]
    asm = read_step(WS / "02_STEP_STL/od_c14_assembly_C1_v01.step")
    box = Pos(95.0, 23.5, -295.0) * Box(40.0, 63.0, 30.0)        # x 75 … 115, y -8 … 55, z -310 … -280
    parts = [labelled(asm, n) for n in ("half_upper", "half_lower", "tie_envelope", "tie_head_box")]
    for n in ("od_c11_back_panel", "od_c01_base_frame", "cord_envelope"):
        parts += (labelled(asm, n) & box).solids()
    out = {}
    for name, shape in (("od_c14_grommet_half", half), ("od_c14_assembly", Compound(parts))):
        for w in write.write_sections(shape, WS / "03_Sections", part=name, version=1, through=THROUGH):
            c = w.checks["nothing_clipped"]
            out[str(w.path.relative_to(WS))] = {"sha256": w.sha256, "plane": w.detail["plane"],
                                               "cut_area_mm2": w.detail["cut_area_mm2"],
                                               "nothing_clipped": c.measured, "status": c.status}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
