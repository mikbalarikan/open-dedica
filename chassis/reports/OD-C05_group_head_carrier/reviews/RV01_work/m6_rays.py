"""RV01: REQ-04 / REQ-08 read as the innermost material radius on the whole ray, every 10 deg at five depths;
nominal and the bar mutant (positive control)."""
import json
from pathlib import Path
from tools.core import read_step
from tools.measure import radial_extent
from tools.result import gate, Result
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier"); W = J / "reviews/RV01_work"
nom = read_step(J / "02_STEP_STL/od_c05_carrier_C1_v01.step")
mut = read_step(W / "mutants/M9_bars_in_windows.step")
r = radial_extent(mut, (0, 0, -27.44), (0, 0, 1), (1, 0, 0), 0, 0.0, side="inner", r_min=0, r_max=30.0)
print("bounded mutant reason:", r.reason)
out = {}
for tag, s in (("nominal", nom), ("M9", mut)):
    for key, org, lim in (("REQ-04", (0, 0), 30.0), ("REQ-08", (0, -110), 25.0)):
        least, n, bad = None, 0, []
        for z in (-29.9, -29.5, -27.44, -25.4, -24.98):
            for th in range(0, 360, 10):
                q = radial_extent(s, (org[0], org[1], z), (0, 0, 1), (1, 0, 0), th, 0.0, side="inner")
                n += 1
                if q.status != "MEASURED": bad.append((z, th, q.reason)); continue
                if least is None or q.measured < least[0]: least = (q.measured, th, z, q.at)
        g = gate(key, Result("innermost", least[0], "mm", at=least[3]), ">=", lim, band=0.005) if least and not bad else None
        out[f"{tag} {key}"] = dict(rays=n, unread=bad, least=least, status=None if g is None else g.status, margin=None if g is None else g.margin)
        print(tag, key, n, "rays, unread", len(bad), "least", least, "->", None if g is None else (g.status, g.margin))
(W / "m6_rays.json").write_text(json.dumps(out, indent=1, default=str))
