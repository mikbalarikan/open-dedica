import json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build123d import Solid
from tools.core.step import read_step, step_roundtrip
from tools.core import write_stl
from tools.result import gate, Result
from tools.measure import envelope, mesh_census, mesh_deviation
import checks as C
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle"); R = W/"reviews/RV02_work"
P = W/"02_STEP_STL/od_c03_cradle_C1_v02.step"
part = read_step(P); asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v02.step")
pump = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
sleeve = {c.label: c for c in asm.children}["od_h02_sleeve_assumed_A03"]
rows = []
rows += C.g_validity(part)
r, e = C.g_envelope(part); rows += r
rows += [gate("D-02", e["size_x"], "<=", 420, band=C.MM, assumes=["A-10"]), gate("D-02", e["size_z"], "<=", 420, band=C.MM, assumes=["A-10"]),
         gate("D-02", e["size_y"], "<=", 500, band=C.MM, assumes=["A-10"])]
rows += C.g_census(part); rows += C.g_bores(part)
r, mw = C.g_walls(part); rows += r
r, oh = C.g_overhang(part); rows += r
rows += C.g_bridge(part); rows += C.g_radial(part); rows += C.g_req02(part)
r, zs = C.g_ribfaces(part); rows += r
r, sl = C.g_slots(part); rows += r
rows += C.g_posts(part); rows += C.g_foot(part)
r, extra = C.g_pump(part, pump, sleeve); rows += r
rows += C.g_roundtrip(part, P)
# own round trip in the work folder, from a parentless copy
copy = Solid(part.wrapped); copy.label = part.label
rt = step_roundtrip(copy, R/"rt_od_c03_cradle.step", timestamp="2026-09-30T00:00:00")
rows += [gate("U-04", rt["volume_delta"], "<=", 0.001, band=C.MM3), gate("U-04", rt["faces_delta"], "==", 0, band=C.CNT),
         gate("U-04", rt["labels"], "==", 1, band=C.CNT), gate("U-04", rt["valid_after"], "==", 1, band=C.CNT)]
# U-07
ang = 4 * math.acos(1 - 0.01 / 32.0)
w = write_stl(read_step(P), R/"remesh_check.stl", tolerance=0.01, angular_tolerance=0.1)
rows += [gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=C.MM),
         gate("U-07", Result("stl_angular_tolerance", 0.1, "rad"), "<=", ang, band=0.00002)]
STL = W/"02_STEP_STL/od_c03_cradle_C1_v02.stl"
mc = mesh_census(STL)
rows += [gate("U-07", mc["bodies"], "==", 1, band=0), gate("U-07", mc["naked_edges"], "==", 0, band=0), gate("U-07", mc["winding"], "==", 1, band=0)]
rows += [gate("U-07", mesh_deviation(STL, read_step(P)), "<=", 0.01 + 0.001, band=C.MM, required="<= 0.01 chordal + 0.001 reference tol (V-05)")]
out = [dict(g.row(), reason=getattr(g, "reason", "")) for g in rows]
(R/"gates_delivered.json").write_text(json.dumps({"rows": out, "rib_faces": zs, "slots": sl, "stl_sha": w.sha256}, indent=1, default=str))
for g in out: print(g["gate"], g["status"], g["measured"], g["unit"], g["margin"], g["required"], g["at"], g["method"])
print("rib faces", zs); print("slots", sl); print("remesh sha", w.sha256)
