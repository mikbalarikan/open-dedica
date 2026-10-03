"""D1 diagnostic: OD-G10 handle direction, OD-G04 hub tube, OD-G10 heal attempt, versions."""
from pathlib import Path
import math, sys, platform
import build123d, OCP
from build123d import Location
from tools.core import read_step, validity
from tools.measure import feature_census, bore_census
from OCP.ShapeFix import ShapeFix_Shape
from build123d import Solid

WS = Path(__file__).resolve().parent.parent
asm = read_step(WS / "00_Spec" / "inputs" / "od_g01_assembly_C1_v03.step")
housing, g04, g10 = list(asm.solids())
POSE = Location((0, 110.06, 0)) * Location((0, 0, 0), (1, 0, 0), 90)
pg = POSE * g10
vs = [v for v in pg.vertices() if math.hypot(v.X, v.Z) > 120]
ang = [math.degrees(math.atan2(v.X, v.Z)) for v in vs]
print("handle verts r>120:", len(vs), "angle from +Z toward +X: min %.2f max %.2f mean %.2f" % (min(ang), max(ang), sum(ang)/len(ang)))
print("handle verts y range", min(v.Y for v in vs), max(v.Y for v in vs))
fc = feature_census(g04)
print("g04 census", {k: getattr(v, "measured", v) for k, v in fc.items()} if isinstance(fc, dict) else fc)
pc = POSE * g04
cyl = [f for f in pc.faces() if f.geom_type.name == "CYLINDER"]
for f in cyl:
    c = f.center(); r = f.radius if hasattr(f, "radius") else None
    bb = f.bounding_box()
    if bb.max.Y > 128:
        print("g04 cyl face r", round(r, 3) if r else r, "y", round(bb.min.Y, 2), round(bb.max.Y, 2), "x", round(bb.min.X, 2), round(bb.max.X, 2))
fx = ShapeFix_Shape(g10.wrapped); fx.Perform()
healed = Solid(fx.Shape()) if fx.Shape().ShapeType().name == "TopAbs_SOLID" else None
if healed is not None:
    v = validity(healed)
    print("healed g10", {k: x.measured for k, x in v.items()}, "vol", healed.volume, "orig", g10.volume)
else:
    print("healed type", fx.Shape().ShapeType())
print("python", platform.python_version(), "build123d", build123d.__version__, "OCP", getattr(OCP, "__version__", "?"))
