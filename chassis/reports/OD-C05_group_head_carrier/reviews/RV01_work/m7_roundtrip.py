from pathlib import Path
from tools.core import read_step, step_roundtrip
from tools.core.shapes import solids, faces
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_FACE, TopAbs_SOLID
from tools.core.shapes import occ
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier"); W = J / "reviews/RV01_work"
p = read_step(J / "02_STEP_STL/od_c05_carrier_C1_v01.step")
def count(kind, avoid=None):
    e = TopExp_Explorer(occ(p), kind, avoid) if avoid is not None else TopExp_Explorer(occ(p), kind)
    n = 0
    while e.More(): n += 1; e.Next()
    return n
print("solids", count(TopAbs_SOLID), "shells not in a solid", count(TopAbs_SHELL, TopAbs_SOLID), "faces not in a shell", count(TopAbs_FACE, TopAbs_SHELL))
r = step_roundtrip(p, W / "roundtrip_rv01.step", timestamp="2026-09-30T12:00:00")
print({k: (v.measured, v.status, v.reason) for k, v in r.items()})
from build123d import Solid
from tools.core.shapes import solids as sol
s = Solid(sol(p)[0]); s.label = "od_c05_carrier"
r = step_roundtrip(s, W / "roundtrip_rv01.step", timestamp="2026-09-30T12:00:00")
print("fresh solid:", {k: (v.measured, v.status) for k, v in r.items()})
