import sys, json
from pathlib import Path
from tools.core.step import read_step, labels, node_labels, read_schema, read_length_unit, read_header
from tools.core.shapes import solids, faces
from tools.core import validity
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v02.step")
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v02.step")
pump = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
print("part labels", labels(part), node_labels(part), type(part))
print("part schema", read_schema(W/"02_STEP_STL/od_c03_cradle_C1_v02.step"), read_length_unit(W/"02_STEP_STL/od_c03_cradle_C1_v02.step"))
print("header", read_header(W/"02_STEP_STL/od_c03_cradle_C1_v02.step"))
print("asm labels", labels(asm), node_labels(asm))
print("asm schema", read_schema(W/"02_STEP_STL/od_c03_assembly_C1_v02.step"))
for c in asm.children:
    print(c.label, len(solids(c)), c.volume, c.bounding_box())
print("pump", labels(pump), len(solids(pump)), pump.volume, pump.bounding_box())
for name, s in [("part", part), ("pump", pump)]:
    v = validity(s)
    print(name, {k: (r.measured, r.status, r.reason) for k, r in v.items()})
for c in asm.children:
    v = validity(c)
    print(c.label, {k: (r.measured, r.status, r.reason) for k, r in v.items()})
print("part vol", part.volume, len(faces(part)))
