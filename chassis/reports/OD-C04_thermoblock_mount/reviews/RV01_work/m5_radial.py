"""RV01: REQ-07 radial_profile reading on the part and on the keep-out boss mutant (per-ray reasons)."""
import json, collections
from pathlib import Path
from build123d import Solid, Box, Pos, Align
from tools.core import read_step
from tools.core.shapes import solids
from tools.measure import radial_profile
W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount"); OUT = W / "reviews/RV01_work"
m = Solid(solids(read_step(W / "02_STEP_STL/od_c04_mount_C1_v01.step"))[0])
boss = m + Pos(0, -66, 20) * Box(4, 8, 10, align=(Align.CENTER, Align.MIN, Align.MIN))
res = {}
for name, s in (("part", m), ("boss_mutant", boss)):
    rp = radial_profile(s, (-8.33, -14.13, 0), (0, 0, 1), (1, 0, 0), [float(a) for a in range(0, 360)], (0.0, 47.64),
                        margin=(0, 0), z_step=1.0, side="inner", r_min=0, r_max=45.0)
    r = rp["min"]; un = r.detail.get("unread", []) or []
    kinds = collections.Counter()
    ex = {}
    for u in un:
        txt = json.dumps(u, default=str)
        k = "no material" if "no material" in txt else ("crosses" if "crosses" in txt else txt[:120])
        kinds[k] += 1; ex.setdefault(k, txt[:300])
    res[name] = {"status": r.status, "reason0": r.reason[:200], "measured": r.measured, "rays": len(un) + len(r.detail.get("points", []) or []),
                 "unread": len(un), "reasons": dict(kinds), "examples": ex, "points": len(r.detail.get("points", []) or [])}
(OUT / "m5.json").write_text(json.dumps(res, indent=1, default=str)); print(json.dumps(res, indent=1, default=str))
