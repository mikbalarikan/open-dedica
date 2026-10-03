"""RV01 reviewer: plane-level geometry (flanks, apexes, underside, walls, chamfers), D-03a with crowns filled, U-04, U-07."""
import json, sys, time, math
from pathlib import Path
import numpy as np
from build123d import Solid, Compound, Location, Cylinder, Box, Vector, Face
from tools.core import read_step, solids, validity, write_stl, mesh_sagitta, step_roundtrip
from tools.core.step import file_sha256
from tools.core import compare_step
from tools.measure import overhang_census, mesh_census, mesh_deviation, min_wall_mesh, envelope
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN, TopAbs_OUT, TopAbs_ON

J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
W = J / "reviews/RV01_work"
rig_path = Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else J / "02_STEP_STL/od_t01_rig_C1_v01.step"
tag = sys.argv[2] if len(sys.argv) > 2 else "nominal"
which = sys.argv[3].split(",") if len(sys.argv) > 3 else ["all"]
def want(k): return "all" in which or k in which
out = {}
rig = Solid(solids(read_step(rig_path))[0])
planes = []
for f in rig.faces():
    ad = BRepAdaptor_Surface(f.wrapped)
    if ad.GetType() != GeomAbs_Plane: continue
    n = f.normal_at(f.center()); c = f.center(); bb = f.bounding_box()
    planes.append({"n": (round(n.X, 6), round(n.Y, 6), round(n.Z, 6)), "c": (c.X, c.Y, c.Z), "area": f.area,
                   "bb": ((bb.min.X, bb.min.Y, bb.min.Z), (bb.max.X, bb.max.Y, bb.max.Z)), "f": f})
def flank_info(sel):
    res = []
    for p in sel:
        n = np.array(p["n"]); ang = math.degrees(math.acos(min(1, abs(n[2]))))
        res.append({"n": p["n"], "c": p["c"], "angle_from_horizontal_deg": ang, "bb": p["bb"]})
    return res
def apex(sel, x0, z0):
    # two flank planes, both containing Y; intersect lines in XZ: n.(p - c) = 0
    (a, b) = sel[:2]
    A = np.array([[a["n"][0], a["n"][2]], [b["n"][0], b["n"][2]]])
    rhs = np.array([a["n"][0] * a["c"][0] + a["n"][2] * a["c"][2], b["n"][0] * b["c"][0] + b["n"][2] * b["c"][2]])
    x, z = np.linalg.solve(A, rhs)
    return float(x), float(z), math.hypot(x - x0, z - z0)
oblique = [p for p in planes if abs(p["n"][1]) < 1e-6 and abs(p["n"][0]) > 1e-3 and abs(p["n"][2]) > 1e-3]
groups = {}
for p in oblique:
    cx, cy, cz = p["c"]
    if cy > 134.9 and abs(cx) < 40: key = "window"
    elif cy > 134.9: key = f"cbore_{int(math.copysign(1, cx))}{int(math.copysign(1, cz - 0))}"
    elif cy < 10.1 and abs(cx) > 95: key = f"bench_{int(math.copysign(1, cx))}{int(math.copysign(1, cz))}"
    else: key = "chamfer"
    groups.setdefault(key, []).append(p)
res = {}
for k, sel in groups.items():
    if k == "chamfer":
        res[k] = [{"n": p["n"], "c": p["c"], "bb": p["bb"]} for p in sel]; continue
    if k == "window": x0, z0 = 0.0, 0.0
    elif k.startswith("cbore"): x0, z0 = math.copysign(44, sel[0]["c"][0]), None
    else: x0, z0 = math.copysign(105, sel[0]["c"][0]), None
    fi = flank_info(sel)
    if len(sel) == 2:
        x, z, _ = apex(sel, x0, 0)
        # the bore axis z: nearest of ±44 / ±40 below the apex
        if k == "window": zc = 0.0
        elif k.startswith("cbore"): zc = min((44.0, -44.0), key=lambda v: abs(z - v))
        else: zc = min((40.0, -40.0), key=lambda v: abs(z - v))
        res[k] = {"flanks": fi, "apex_x": x, "apex_z": z, "apex_from_axis": z - zc, "axis_z": zc}
    else:
        res[k] = {"flanks": fi, "count": len(sel)}
out["oblique"] = res
# chamfer planes: normals in XY at 45 deg
ch = [p for p in planes if abs(p["n"][2]) < 1e-6 and abs(abs(p["n"][0]) - abs(p["n"][1])) < 1e-4 and abs(p["n"][0]) > 0.5]
out["chamfers"] = [{"n": p["n"], "c": p["c"], "bb": p["bb"], "width": math.hypot(p["bb"][1][0] - p["bb"][0][0], p["bb"][1][1] - p["bb"][0][1])} for p in ch]
# underside faces at y 135 facing -Y
und = [p for p in planes if abs(p["n"][1] + 1) < 1e-6 and abs(p["c"][1] - 135) < 0.2]
out["underside_faces"] = [{"c": p["c"], "bb": p["bb"], "area": p["area"]} for p in und]
# wall inner faces: normals ±X at |x|≈75
wi = [p for p in planes if abs(abs(p["n"][0]) - 1) < 1e-6 and 70 < abs(p["c"][0]) < 80]
out["wall_inner"] = [{"n": p["n"], "c": p["c"], "bb": p["bb"]} for p in wi]
wo = [p for p in planes if abs(abs(p["n"][0]) - 1) < 1e-6 and 85 < abs(p["c"][0]) < 95]
out["wall_outer"] = [{"n": p["n"], "c": p["c"], "bb": p["bb"]} for p in wo]
zf = [p for p in planes if abs(abs(p["n"][2]) - 1) < 1e-6]
out["z_faces"] = [{"n": p["n"], "c": p["c"], "bb": p["bb"]} for p in zf]
# REQ-02: grid over x,z in [-50,50] at y 135 +/- 0.002: above inside (or in a hole), below outside
clsr = BRepClass3d_SolidClassifier(rig.wrapped)
def state(x, y, z):
    clsr.Perform(gp_Pnt(x, y, z), 1e-6); return clsr.State()
bad_above = bad_below = n_hole = n = 0
for x in np.linspace(-50, 50, 101):
    for z in np.linspace(-50, 50, 101):
        r = math.hypot(x, z)
        in_hole = r < 30.0 + 1e-3 or (z > 0 and abs(x) <= (42.5 - z) * 1 + 1e-3) or any(math.hypot(x - sx * 44, z - sz * 44) < 1.7 + 1e-3 for sx in (1, -1) for sz in (1, -1))
        n += 1
        if in_hole: n_hole += 1; continue
        if state(x, 135.002, z) != TopAbs_IN: bad_above += 1
        if state(x, 134.998, z) != TopAbs_OUT: bad_below += 1
out["REQ02_grid"] = {"points": n, "skipped_holes": n_hole, "not_material_above": bad_above, "material_below": bad_below}
if want("d03a"):
    plugs = [Cylinder(1.8, 3.0, align=None).moved(Location((sx * 44.0, 135.0, sz * 44.0)) * Location((0, 0, 0), (1, 0, 0), -90)) for sx in (1, -1) for sz in (1, -1)]
    filled = rig
    for p in plugs: filled = filled.fuse(p)
    fs = solids(filled)
    out["filled_solids"] = len(fs)
    fsol = Solid(fs[0])
    out["filled_valid"] = {k: x.measured for k, x in validity(fsol).items()}
    oc = overhang_census(fsol, build_dir=(0, 0, 1), min_deg=45)
    out["D03a_filled"] = oc.to_dict()
if want("mesh"):
    stl = J / "02_STEP_STL/od_t01_rig_C1_v01.stl"
    out["mesh_census"] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for k, v in (mesh_census(stl).items() if isinstance(mesh_census(stl), dict) else [("r", mesh_census(stl))])}
    w = write_stl(rig, W / f"remesh_{tag}.stl", tolerance=0.01, angular_tolerance=0.10)
    out["remesh"] = {"sha": w.sha256 if hasattr(w, "sha256") else None, "detail": w.detail, "sagitta": w.checks["max_sagitta"].to_dict()}
    out["delivered_stl_sha"] = file_sha256(stl)
    out["mesh_deviation"] = mesh_deviation(stl, rig).to_dict()
    out["min_wall_mesh"] = min_wall_mesh(stl).to_dict()
    out["ang_limit"] = 4 * math.acos(1 - 0.01 / 30.0)
if want("rt"):
    s2 = Solid(rig.wrapped.Located(rig.wrapped.Location()))
    s2 = Solid(solids(read_step(rig_path))[0].Moved(__import__("OCP").TopLoc.TopLoc_Location()))
    s2.label = "od_t01_rig"
    rt = step_roundtrip(s2, W / f"rt_{tag}.step", timestamp="2026-10-03T00:00:00")
    out["roundtrip"] = {k: x.to_dict() for k, x in rt.items()}
(W / f"geom_{tag}_{'_'.join(which)}.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, default=str)[:15000])
