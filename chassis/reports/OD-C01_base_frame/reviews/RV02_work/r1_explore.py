import json, sys
from pathlib import Path
from tools.core import read_step, validity, read_schema, read_length_unit
from OCP.TopoDS import TopoDS_Shape
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
# labelled read: use build123d importer to get names
from build123d import import_step
for name in ["od_c01_frame_C1_v03.step", "od_c01_assembly_C1_v03.step"]:
    p = W/"02_STEP_STL"/name
    print("==", name, "schema", read_schema(p), "unit", read_length_unit(p))
    sh = import_step(str(p))
    print("  type", type(sh).__name__, "label", getattr(sh,"label",None))
    try:
        ch = list(sh.children)
    except Exception as e:
        ch = []
    print("  children", len(ch))
    for c in ch:
        print("   -", c.label, type(c).__name__, len(c.solids()))
    print("  solids total", len(sh.solids()))
