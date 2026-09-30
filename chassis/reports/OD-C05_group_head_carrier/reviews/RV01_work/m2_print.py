"""RV01: D-03a / D-03b by analytic face angles and plane sections; E-06; REQ-04 / REQ-08 rays."""
import json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from build123d import Box, Pos
from tools.core import read_step, common_volume
from tools.measure import radial_extent
from lib_rv import downward_faces, section_edges, section_area
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
W = J / "reviews/RV01_work"
path = Path(sys.argv[1]) if len(sys.argv) > 1 else J / "02_STEP_STL/od_c05_carrier_C1_v01.step"
tag = sys.argv[2] if len(sys.argv) > 2 else "nominal"
part = read_step(path) if path.suffix == ".step" else None
out = {}
rows = downward_faces(part)
def is_exception(r):
    if r["kind"] != "cylinder": return False
    ax, loc = np.array(r["axis_dir"]), np.array(r["axis_loc"])
    return (abs(abs(ax[2]) - 1) < 1e-9 and abs(abs(loc[0]) - 44) < 1e-6 and abs(abs(loc[1]) - 44) < 1e-6
            and (abs(r["radius"] - 1.7) < 0.06 or abs(r["radius"] - 3.25) < 0.06))
for r in rows: r["exception"] = is_exception(r)
out["downward_faces"] = rows
rest = [r for r in rows if not r["exception"]]
exc = [r for r in rows if r["exception"]]
under = [r for r in rows if r["least_deg"] is not None and r["least_deg"] < 45 - 1e-3]
out["least_outside_exception"] = min(rest, key=lambda r: r["least_deg"]) if rest else None
out["exception_faces"] = len(exc)
out["faces_under_45"] = [(r["face"], r["kind"], r.get("radius"), r["axis_loc"] if "axis_loc" in r else None, r["least_deg"]) for r in under]
out["under_45_all_in_exception"] = all(r["exception"] for r in under)
print("downward faces:")
for r in rows:
    print(f"  f{r['face']:>3} {r['kind']:8} R={r.get('radius','-')!s:>6} least={r['least_deg']:.9f} at={np.round(r['at'],4).tolist()} {r.get('where','')} exc={r['exception']}")
print("least outside exception:", out["least_outside_exception"]["least_deg"], out["least_outside_exception"]["at"])
print("exception faces:", len(exc), "under-45 faces all in exception:", out["under_45_all_in_exception"], len(under))
if tag == "nominal":
    # sections
    for name, o, n in (("z-27.44", (0, 0, -27.44), (0, 0, 1)), ("z-28.94", (0, 0, -28.94), (0, 0, 1)), ("x0", (0, 0, 0), (1, 0, 0))):
        es = section_edges(part, o, n)
        out[f"section_{name}"] = es
        print("section", name, len(es), "edges")
        for e in es:
            if e["kind"] == "line":
                d = np.array(e["p1"]) - np.array(e["p0"])
                ang = math.degrees(math.atan2(abs(d[1]), math.hypot(d[0], d[2])))
                e["slope_deg"] = ang
                if 0.5 < ang < 89.5: print("   line", np.round(e["p0"], 4).tolist(), np.round(e["p1"], 4).tolist(), f"slope {ang:.6f}")
            elif e["kind"] == "circle":
                print("   circle R", round(e["radius"], 4), "c", np.round(e["centre"], 3).tolist(), "p0", np.round(e["p0"], 4).tolist(), "p1", np.round(e["p1"], 4).tolist(), "t0", np.round(e["t0"], 6).tolist(), "t1", np.round(e["t1"], 6).tolist())
    # E-06 gussets: material in the gusset triangles' boxes and the gusset cut area at x = +-48
    for sx in (1, -1):
        box = Pos(sx * 48, -151, -49.94) * Box(4, 40, 40)
        cv = common_volume(part, box)
        a, _ = section_area(part, (sx * 48, 0, 0), (1, 0, 0))
        out[f"gusset_{sx}"] = dict(volume=cv.measured, status=cv.status, x_section_area=a)
        print("gusset", sx, cv.measured, cv.status, "section area x=", sx * 48, a)
    # REQ-04 / REQ-08 rays
    for key, org, rmax, ctrl in (("REQ-04", (0, 0, 0), 30.0, ((90, 42.42640687), (0, 30.0))),
                                 ("REQ-08", (0, -110, 0), 25.0, ((90, 35.35533906), (270, 25.0)))):
        hits, n = [], 0
        for z in (-29.9, -29.5, -27.44, -25.4, -24.98):
            for th in range(0, 360, 10):
                r = radial_extent(part, (org[0], org[1], z), (0, 0, 1), (1, 0, 0), th, 0.0, side="inner", r_min=0, r_max=rmax)
                n += 1
                if r.status == "MEASURED": hits.append((z, th, r.measured))
                elif "no material" not in r.reason: hits.append((z, th, r.reason))
        cs = []
        for th, exp in ctrl:
            r = radial_extent(part, (org[0], org[1], -27.44), (0, 0, 1), (1, 0, 0), th, 0.0, side="inner")
            cs.append((th, r.measured, exp, r.status))
        out[key] = dict(rays=n, with_material=hits, controls=cs)
        print(key, n, "rays; with material:", hits, "controls:", cs)
(W / f"m2_{tag}.json").write_text(json.dumps(out, indent=1, default=str))
