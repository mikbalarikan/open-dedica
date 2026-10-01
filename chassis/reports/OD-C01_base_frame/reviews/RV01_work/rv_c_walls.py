"""RV01 C: walls, overhang, radial rings on the delivered plate (spacing 0.7 per brief)."""
import json, sys, time
from pathlib import Path
from tools.core import read_step
from tools.measure import min_wall, min_wall_wide, overhang_census, radial_extent
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
W = J / "reviews/RV01_work"
src = Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else J / "02_STEP_STL/od_c01_frame_C1_v02.step"
tag = sys.argv[2] if len(sys.argv) > 2 else "plate"
what = sys.argv[3] if len(sys.argv) > 3 else "all"
s = read_step(src)
out = {}
t = time.time()
if what in ("all", "wall"):
    r = min_wall(s, spacing=0.7); out["min_wall"] = r.to_dict()
    r = min_wall_wide(s, spacing=0.7); out["min_wall_wide"] = r.to_dict()
if what in ("all", "over"):
    r = overhang_census(s, build_dir=(0, 1, 0), spacing=0.7); out["overhang"] = r.to_dict()
if what in ("all", "rings"):
    inserts = [(35,-40),(-35,-40),(35,-60),(-35,-60),(40,-148),(-40,-148),(40,-114),(-40,-114),
               (-4,-239),(-4,-171),(37,-239),(37,-171),(65,-45),(65,-105),(65,-165),(65,-225),
               (-113,-42),(-71,-42),(-113,-148.5),(-71,-148.5)]
    rings = []
    unread = 0
    for x, z in inserts:
        for ang in [a + 0.5 for a in range(0, 360, 5)]:
            for lev in (0.5, 3.0, 5.5):   # distance below the top face along -Y
                try:
                    r = radial_extent(s, (x, 0.0, z), (0, -1, 0), (1, 0, 0), ang, lev, side="outer", r_min=0.0)
                except Exception as e:
                    unread += 1; continue
                if not r.ok:
                    unread += 1; continue
                mat = r.detail["material"]
                first = [m for m in mat if m[1] > 1.99]
                if not first: unread += 1; continue
                a0, a1 = first[0]
                rings.append({"hole": [x, z], "ang": ang, "lev": lev, "start": a0, "end": a1})
    out["rings_unread"] = unread
    out["rings_n"] = len(rings)
    worst = min(rings, key=lambda q: q["end"])
    out["ring_worst"] = worst
    out["ring_start_max_dev"] = max(abs(q["start"] - 2.0) for q in rings)
    per = {}
    for q in rings:
        k = f"{q['hole'][0]},{q['hole'][1]}"
        per[k] = min(per.get(k, 1e9), q["end"])
    out["ring_per_hole_min_end"] = per
out["seconds"] = time.time() - t
(W / f"rv_c_{tag}_{what}.json").write_text(json.dumps(out, indent=1, default=str))
print("done", tag, what, out.get("min_wall", {}).get("measured"), out.get("overhang", {}).get("measured"), out.get("ring_worst"))
