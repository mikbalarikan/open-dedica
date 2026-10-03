"""RV01: per-part measurements on the exported STEP and STL (U-01, U-02, U-04, U-05,
U-06, U-07, D-01a/b, D-02, D-03a, D-03b corroboration, D-04a, D-05a/b, D-06a, J-05,
REQ-01..05 part rows)."""
import sys, time, math
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
from tools.core import validity, step_roundtrip, write_stl, mesh_sagitta
from tools.core.step import labels
from tools.measure import (envelope, feature_census, bore_census, min_wall, overhang_census,
                           flat_ceiling_spans, mesh_census, mesh_deviation)
from tools.measure.features import cylinder, kind
from tools.core.shapes import faces

which = sys.argv[1:] or ["c13", "c12", "c16"]
FILES = {"c13": ("od_c13_right_C1_v01", (-1, 0, 0)), "c12": ("od_c12_left_C1_v01", (1, 0, 0)),
         "c16": ("od_c16_bracket_C1_v01", (0, 1, 0))}
for key in which:
    stem, bdir = FILES[key]
    t0 = time.time()
    out = {"step_sha": sha(EXP / f"{stem}.step"), "stl_sha": sha(EXP / f"{stem}.stl")}
    shape = load(f"{stem}.step")
    out["labels"] = labels(shape)
    out["validity"] = validity(shape)
    out["envelope"] = envelope(shape)
    out["roundtrip"] = step_roundtrip(shape, WORK / f"rt_{stem}.step", timestamp="2026-10-03T00:00:00")
    fc = feature_census(shape)
    out["feature_census"] = fc
    bc = bore_census(shape)
    out["bore_census"] = bc
    # faces list with kind and, for planes, normal/point; for cylinders radius
    fl = []
    from OCP.BRepAdaptor import BRepAdaptor_Surface
    from OCP.GeomAbs import GeomAbs_Plane, GeomAbs_Cylinder
    from build123d import Face
    rmax = 0.0
    for f in faces(shape):
        ad = BRepAdaptor_Surface(f)
        F = Face(f)
        bb = F.bounding_box()
        rec = {"kind": kind(f), "area": round(F.area, 4),
               "bb": [round(v, 4) for v in (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)]}
        if ad.GetType() == GeomAbs_Plane:
            n = F.normal_at(F.center())
            rec["normal"] = [round(n.X, 5), round(n.Y, 5), round(n.Z, 5)]
        if ad.GetType() == GeomAbs_Cylinder:
            r = ad.Cylinder().Radius(); rec["radius"] = r; rmax = max(rmax, r)
        fl.append(rec)
    out["faces"] = fl
    out["r_max"] = rmax
    out["ang_limit"] = 4 * math.acos(1 - 0.01 / rmax) if rmax else None
    out["overhang"] = overhang_census(shape, build_dir=bdir, spacing=0.5)
    out["flat_ceiling"] = flat_ceiling_spans(shape, build_dir=bdir, max_span=5.0, spacing=0.5)
    mw = min_wall(shape, spacing=0.4)
    if mw.status != "MEASURED":
        out["min_wall_0.4"] = mw
        mw = min_wall(shape, spacing=1.0)
    out["min_wall"] = mw
    # STL: delivered mesh census and deviation; fresh mesh at the REPORT settings
    stl = EXP / f"{stem}.stl"
    out["mesh_census"] = mesh_census(stl)
    out["mesh_deviation"] = mesh_deviation(stl, shape)
    ang = out["ang_limit"]
    w = write_stl(load(f"{stem}.step"), WORK / f"fresh_{stem}.stl", tolerance=0.01, angular_tolerance=ang)
    out["fresh_stl"] = {"sha": w.sha256, "detail": w.detail, "sagitta": w.checks["max_sagitta"],
                        "same_bytes_as_delivered": w.sha256 == out["stl_sha"]}
    out["seconds"] = time.time() - t0
    dump(out, f"parts_{key}.json")
    print(key, "done", round(out["seconds"], 1))
