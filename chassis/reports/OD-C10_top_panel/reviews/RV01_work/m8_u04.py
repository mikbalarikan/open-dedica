import sys, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.core.step import step_roundtrip, compare_step, read_schema, read_length_unit, labels, node_labels
from tools.core.shapes import solids, faces
from tools.core import validity
from tools.measure import bore_census
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_SOLID, TopAbs_FACE
out = {}
raw = read_step(LID)
def count(sh, kind, avoid=None):
    from OCP.TopExp import TopExp_Explorer
    e = TopExp_Explorer(sh.wrapped, kind) if avoid is None else TopExp_Explorer(sh.wrapped, kind, avoid)
    n = 0
    while e.More(): n += 1; e.Next()
    return n
out["part"] = {"schema": read_schema(LID), "unit": read_length_unit(LID), "labels": labels(raw), "solids": len(solids(raw)),
               "free_shells": count(raw, TopAbs_SHELL, TopAbs_SOLID), "free_faces": count(raw, TopAbs_FACE, TopAbs_SHELL)}
from build123d import Solid
from OCP.BRepBuilderAPI import BRepBuilderAPI_Copy
S = Solid(BRepBuilderAPI_Copy(lid().wrapped).Shape()); S.label = "od_c10_top"
out["part_vs_delivered"] = {k: (v.measured, v.status, v.reason) for k, v in compare_step(S, LID).items()}
rt = step_roundtrip(S, WORK / "rt_part.step", timestamp="2026-10-01T00:00:00")
out["part_roundtrip"] = {k: (v.measured, v.status, v.reason) for k, v in rt.items()}
A = JOB / "02_STEP_STL/od_c10_assembly_C1_v01.step"
araw = read_step(A)
out["asm"] = {"schema": read_schema(A), "unit": read_length_unit(A), "labels": labels(araw), "nodes": node_labels(araw), "solids": len(solids(araw)),
              "free_shells": count(araw, TopAbs_SHELL, TopAbs_SOLID), "valid": {k: v.measured for k, v in validity(araw).items()}}
rt2 = {}
out["asm_roundtrip"] = {k: (v.measured, v.status, v.reason) for k, v in rt2.items()}
c05 = placed("C05")
out["c05_cbores"] = [(b["diameter"], b["start"]) for b in bore_census(c05).detail["bores"] if b["start"][1] > 200]
dump("m8_u04.json", out); print(json.dumps(out, default=str))
