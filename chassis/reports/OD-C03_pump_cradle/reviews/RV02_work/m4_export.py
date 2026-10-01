import json, math, hashlib
from pathlib import Path
from tools.core.step import read_step, compare_step, step_roundtrip, labels, file_sha256
from tools.core import write_stl, mesh_sagitta
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_FACE, TopAbs_SOLID
from tools.core.shapes import occ
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle"); R = W/"reviews/RV02_work"
P = W/"02_STEP_STL/od_c03_cradle_C1_v02.step"; A = W/"02_STEP_STL/od_c03_assembly_C1_v02.step"
STL = W/"02_STEP_STL/od_c03_cradle_C1_v02.stl"
part = read_step(P); asm = read_step(A)
d = lambda r: r.to_dict()
o = {}
def count(s, kind, avoid=None):
    e = TopExp_Explorer(occ(s), kind) if avoid is None else TopExp_Explorer(occ(s), kind, avoid)
    n = 0
    while e.More(): n += 1; e.Next()
    return n
o["part_shells"] = count(part, TopAbs_SHELL); o["part_free_shells"] = count(part, TopAbs_SHELL, TopAbs_SOLID)
o["part_free_faces"] = count(part, TopAbs_FACE, TopAbs_SHELL)
o["asm_free_shells"] = count(asm, TopAbs_SHELL, TopAbs_SOLID); o["asm_free_faces"] = count(asm, TopAbs_FACE, TopAbs_SHELL)
o["compare_delivered"] = {k: d(v) for k, v in compare_step(part, P).items()}
o["roundtrip_work"] = {k: d(v) for k, v in step_roundtrip(part, R/"rt_od_c03_cradle.step", timestamp="2026-09-30T00:00:00").items()}
o["compare_asm"] = {k: d(v) for k, v in compare_step(asm, A).items()}
o["rt_sha_equals_delivered"] = (R/"rt_od_c03_cradle.step").exists() and file_sha256(R/"rt_od_c03_cradle.step") == file_sha256(P); print(o["roundtrip_work"]["solids"]["reason"])
# STL
ang = 4 * math.acos(1 - 0.01 / 32.0)
o["ang_limit"] = ang
w = write_stl(part, R/"remesh_tol0p01.stl", tolerance=0.01, angular_tolerance=0.1)
o["remesh"] = {"sha256": w.sha256, "detail": w.detail, "sagitta": d(w.checks["max_sagitta"])}
w2 = write_stl(read_step(P), R/"remesh_tol0p01_angmax.stl", tolerance=0.01, angular_tolerance=ang)
o["remesh_angmax"] = {"sha256": w2.sha256, "detail": w2.detail, "sagitta": d(w2.checks["max_sagitta"])}
o["delivered_stl_sha"] = file_sha256(STL)
o["delivered_equals_remesh"] = file_sha256(STL) == w.sha256
o["census"] = {k: d(v) for k, v in mesh_census(STL).items()}
o["deviation"] = d(mesh_deviation(STL, read_step(P)))
o["min_wall_mesh"] = d(min_wall_mesh(STL))
(R/"m4_export.json").write_text(json.dumps(o, indent=1, default=str)); print("done")
