"""U-04 (STEP re-read), U-07 (STL), U-05 probes, cap axes, healed OD-G10 corroboration."""
from common import *
import hashlib, os
from tools.core import compare_step, write_stl, mesh_sagitta, validity, common_volume
from tools.core.step import read_schema, read_header, labels
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh, clearance
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.TopAbs import TopAbs_IN, TopAbs_OUT, TopAbs_ON
out = {}
s, ss = part(); P = Solid(ss[0])
out["schema"] = read_schema(PART_STEP); out["header"] = read_header(PART_STEP); out["labels"] = labels(s)
cs = compare_step(s, PART_STEP)
out["compare_step"] = {k: (v.measured, v.status) for k, v in cs.items()}
# a fresh write into the work folder and back (the delivered file is not touched)
from tools.core import step_roundtrip
rt = step_roundtrip(s, WORK / "rt_od_c09_front.step", timestamp="2026-10-03T00:00:00")
out["roundtrip_work"] = {k: (v.measured, v.status, v.reason) for k, v in rt.items()}
# STL
mc = mesh_census(PART_STL); out["mesh_census"] = {k: v.measured for k, v in mc.items()}
md = mesh_deviation(PART_STL, P); out["mesh_deviation"] = (md.measured, md.status, md.at)
fresh = WORK / "fresh_0p01_0p15.stl"
w = write_stl(P, fresh, tolerance=0.01, angular_tolerance=0.15)
out["fresh_write"] = {"triangles": w.detail.get("triangles") if hasattr(w, "detail") else None}
try:
    out["fresh_sagitta"] = (w.checks["max_sagitta"].measured, w.checks["max_sagitta"].status)
except Exception as ex:
    out["fresh_sagitta"] = str(ex)
out["sha_fresh"] = hashlib.sha256(fresh.read_bytes()).hexdigest()
out["sha_delivered"] = hashlib.sha256(PART_STL.read_bytes()).hexdigest()
out["stl_bytes_equal"] = fresh.read_bytes() == PART_STL.read_bytes()
out["stl_bytes_equal_after80"] = fresh.read_bytes()[80:] == PART_STL.read_bytes()[80:]
mwm = min_wall_mesh(PART_STL); out["min_wall_mesh"] = (mwm.measured, mwm.status, mwm.reason, mwm.detail.get("vertex_precision_mm"))
import trimesh
m = trimesh.load(PART_STL); out["mesh_volume"] = float(m.volume); out["brep_volume"] = P.volume
# curved face radii (R_max)
radii = sorted({round(f.radius, 4) for f in P.faces() if f.geom_type.name == "CYLINDER"})
out["cyl_radii"] = radii
print(json.dumps(out, indent=1, default=str), flush=True)
# U-05 probes: point classification
def cls(pt):
    c = BRepClass3d_SolidClassifier(P.wrapped, gp_Pnt(*pt), 1e-6)
    st = c.State(); return {TopAbs_IN: "IN", TopAbs_OUT: "OUT", TopAbs_ON: "ON"}.get(st, str(st))
probes = {
 "wall_left": (-100, 100, 95.5), "wall_right": (100, 100, 95.5), "top_bar": (0, 200, 95.5),
 "opening_slot": (0, 25, 95.5), "opening_window": (0, 120, 95.5), "opening_slot_left": (-66, 25, 95.5), "opening_win_right": (70, 180, 95.5),
 "R1": (0, 189.5, 89), "R2": (76.5, 100, 89), "R3": (-59, 120, 89), "R4": (-76.5, 25, 89), "R5": (-70, 51.5, 89),
 "R1_end_out": (79, 189.5, 89), "R1_back_out": (0, 189.5, 83.9),
 "flange_L": (-90, 2, 85), "flange_R": (90, 2, 85), "flange_L_out": (-90, 4.1, 85),
 "gus_Lin": (-78, 6, 92), "gus_Lout": (-102, 6, 92), "gus_Rin": (78, 6, 92), "gus_Rout": (102, 6, 92),
 "gus_Lin_above_hyp": (-78, 30, 82), "gus_Rout_above_hyp": (102, 30, 82),
 "slot_free_under_R": (74, 25, 90), "knob_place": (95.5, 140, 90),
 "bossL": (-94.5, 153.2349, 90), "bossR": (-94.5, 127.2515, 90), "boreL": (-91.0555, 153.2349, 88), "boreR": (-90.9987, 127.2515, 88),
 "boreL_floor_above": (-91.0555, 153.2349, 92.0), "behind_boss": (-91.0555, 153.2349, 85.3),
}
out["probes"] = {k: cls(v) for k, v in probes.items()}
print(out["probes"], flush=True)
# concave arcs (collar reliefs)
from tools.measure.features import _bores
bores, arcs, _ = _bores(P)
out["arcs"] = [(round(a["radius"], 4), a["axis_dir"], a["start"], a["end"], a["span_deg"]) for a in arcs]
print(out["arcs"], flush=True)
# cap axes, B1 and B3 at more levels
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln
from build123d import Wire, Face
r = refs(); E = r["E02"]
caps = {}
for k, (x, y) in {"B1": (-94.2478, 166.5135), "B3": (-93.7652, 113.4263), "B2": (-98.9908, 139.9014)}.items():
    cents = {}
    for z in (88.6, 88.8, 89.0, 89.5, 90.0, 90.5):
        sec = BRepAlgoAPI_Section(E.wrapped, gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))); sec.Build()
        es = [e for e in Compound(sec.Shape()).edges() if abs(e.center().X - x) < 7.4 and abs(e.center().Y - y) < 7.4]
        try:
            fs = [Face(w) for w in Wire.combine(es) if w.is_closed]
            f = max(fs, key=lambda f: f.area); c = f.center()
            cents[z] = (round(c.X, 4), round(c.Y, 4), round(f.area, 3), round(math.hypot(c.X - x, c.Y - y), 4))
        except Exception as ex:
            cents[z] = str(ex)[:60]
    caps[k] = cents
print(caps, flush=True)
out["caps_more"] = caps
# collar relief geometry vs collars: collar sections at z 87
# healed OD-G10 corroboration of the HOUS|G10 reference pair
from OCP.ShapeFix import ShapeFix_Shape
from tools.core import brep_valid
for k in ("G10", "E02"):
    fx = ShapeFix_Shape(r[k].wrapped); fx.Perform()
    hs = Solid(fx.Shape()) if fx.Shape().ShapeType().name.endswith("SOLID") else Compound(fx.Shape())
    bv = brep_valid(hs)
    out["healed_" + k] = {"brep_valid": bv.measured, "vol_before": r[k].volume, "vol_after": hs.volume}
    if bv.measured == 1:
        other = r["HOUS"] if k == "G10" else P
        cv = common_volume(hs, other); out["healed_" + k]["common_with_" + ("HOUS" if k == "G10" else "PANEL")] = (cv.measured, cv.status, cv.reason)
    print(k, out["healed_" + k], flush=True)
dump("s06_export.json", out)
