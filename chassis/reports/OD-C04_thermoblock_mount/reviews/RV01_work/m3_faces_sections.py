"""RV01: face-level envelopes (REQ-03, REQ-04, REQ-05), root fillet radii (E-06), own sections."""
import json
from pathlib import Path
from build123d import Solid, Compound, GeomType
from OCP.BRepAdaptor import BRepAdaptor_Surface
from tools.core import read_step
from tools.core.shapes import solids
from tools.measure import envelope
from tools.drawing.write import write_sections

W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount")
OUT = W / "reviews/RV01_work"
m = Solid(solids(read_step(W / "02_STEP_STL/od_c04_mount_C1_v01.step"))[0])
out = {"planes": [], "tori": []}
for f in m.faces():
    if f.geom_type == GeomType.PLANE:
        n = f.normal_at(f.center())
        e = {k: round(r.measured, 6) for k, r in envelope(f).items()}
        out["planes"].append({"normal": [round(n.X, 4), round(n.Y, 4), round(n.Z, 4)], "area": round(f.area, 3), "env": e})
    if f.geom_type == GeomType.TORUS:
        s = BRepAdaptor_Surface(f.wrapped).Torus()
        c = s.Location()
        out["tori"].append({"major": s.MajorRadius(), "minor": s.MinorRadius(), "centre": [c.X(), c.Y(), c.Z()]})
asm = read_step(W / "02_STEP_STL/od_c04_assembly_C1_v01.step")
sec = {}
for tag, shape, view, through in [
        ("xS1", m, "left", (-19.62, 20.18, -12)), ("xS2", m, "left", (25.01, 9.08, -12)),
        ("xGusset", m, "left", (-46, -56, -2)), ("xFrame", m, "left", (40, -68, -8)),
        ("zStandoffs", m, "top", (0, 0, -11)), ("yFoot", m, "front", (0, -68, 0)),
        ("zTipPlusEps", m, "top", (0, 0, -10.2)),
        ("asm_xS1", asm, "left", (-19.62, 20.18, 0)), ("asm_xS2", asm, "left", (25.01, 9.08, 0))]:
    try:
        ws = write_sections(shape, OUT / "sections" / tag, part="rv01_" + tag, views=(view,), through=through)
        sec[tag] = [{"file": str(w.path), "detail": {k: v for k, v in w.detail.items()}, "clipped": w.checks["nothing_clipped"].measured} for w in ws]
    except Exception as ex:
        sec[tag] = f"{type(ex).__name__}: {ex}"
out["sections"] = sec
(OUT / "m3.json").write_text(json.dumps(out, indent=1, default=str))
print("done")
