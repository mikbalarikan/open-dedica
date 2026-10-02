"""RV01: print checks: min_wall (25 deg) and wide (45 deg), overhang census whole part and with the six
named-exception holes refilled by position (my own plugs), flat ceiling spans. Args: step [out] [tag]."""
import json, sys, time
from build123d import Cylinder, Location, Plane, Pos
from tools.core import read_step, validity
from tools.measure import min_wall, min_wall_wide, overhang_census, flat_ceiling_spans
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{J}/reviews/RV01_work/m4_print.json"
WHICH = sys.argv[3].split(",") if len(sys.argv) > 3 else ["wall", "wide", "over", "over_refill", "bridge"]
p = read_step(STEP)
out = {}
def keep(name, res):
    out[name] = res.to_dict(); print(name, res.measured, res.status, res.at, res.reason[:120], flush=True)
    json.dump(out, open(OUT, "w"), indent=1, default=str)
def refill(shape):
    plugs = None
    for (x, z) in [(81, -282), (95, -282), (-81, -282), (-95, -282)]:
        c = Plane.XZ.offset(0).located if False else None
    # plugs along Y: Cylinder is along Z by default; rotate so axis is Y
    from build123d import Rot
    s = shape
    for (x, z, d, y0, y1) in [(81, -282, 3.4, 0, 4), (95, -282, 3.4, 0, 4), (-81, -282, 3.4, 0, 4), (-95, -282, 3.4, 0, 4),
                              (90, -293, 4.0, 209, 215), (-90, -293, 4.0, 209, 215)]:
        plug = Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2 + 0.0, y1 - y0)
        s = s.fuse(plug).clean()
    return s
t = time.time()
if "wall" in WHICH: keep("min_wall", min_wall(p, spacing=0.7))
if "wide" in WHICH: keep("min_wall_wide", min_wall_wide(p, spacing=0.7))
if "over" in WHICH: keep("overhang_whole", overhang_census(p, build_dir=(0, 0, 1), spacing=0.7))
if "over_refill" in WHICH:
    rf = refill(p)
    v = validity(rf)
    out["refilled_validity"] = {k: r.measured for k, r in v.items()}
    out["refilled_faces"] = len(rf.faces())
    print("refilled", out["refilled_validity"], out["refilled_faces"], flush=True)
    keep("overhang_refilled", overhang_census(rf, build_dir=(0, 0, 1), spacing=0.7))
if "bridge" in WHICH: keep("flat_ceiling_spans", flat_ceiling_spans(p, build_dir=(0, 0, 1), max_span=5.0, spacing=0.7))
print("seconds", round(time.time() - t, 1))
