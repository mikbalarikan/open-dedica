#!/usr/bin/env python3
"""QA run-local probe (report-only, not a skill script; it3 version of _it2_SUPERSEDED/qa/it1_it2_diff.py):
what changed between the it2 and it3 datum STEPs? Face-signature diff (type, area, centre) and boolean
differences it2-it3 / it3-it2 split into connected solids with volume and bbox, each piece and each
changed face classified into the QA zone boxes of qa/zones.json (datum frame). Checks the builder's claim
(MODELING_PLAN §8 it3) that only the Z2 bend, the Z3 perimeter round and the Z4 tip neck changed."""
import json, sys
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, write_json
from build123d import import_step

A = import_step("_it2_SUPERSEDED/build/OD-S02_steam-rod_datum.step").solids()[0]
B = import_step("build/OD-S02_steam-rod_datum.step").solids()[0]
Z = json.load(open("qa/zones.json"))["zones"]
def inbox(sel, p):
    x, y, z = p; r = float(np.hypot(x, y))
    for k, (lo, hi) in sel.items():
        v = {"x": x, "y": y, "z": z, "r": r}[k]
        if (lo is not None and v < lo) or (hi is not None and v >= hi): return False
    return True
def zone_of(p):
    hits = [z["name"].split(" ")[0] + (" " + z["name"].split(" ")[1] if z["name"].startswith("R ") else "") for z in Z if inbox(z["select"], p)]
    return hits or ["outside all zones"]
def info(s):
    bb = s.bounding_box()
    return {"volume_mm3": round(s.volume, 4), "bbox_min": [round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z)],
            "bbox_max": [round(v, 3) for v in (bb.max.X, bb.max.Y, bb.max.Z)], "faces": len(s.faces())}
out = {"it2": info(A), "it3": info(B)}
def faces_sig(s):
    return [(str(f.geom_type).split(".")[-1], round(f.area, 4), round(f.center().X, 3), round(f.center().Y, 3), round(f.center().Z, 3)) for f in s.faces()]
sa, sb = set(faces_sig(A)), set(faces_sig(B))
out["faces_identical"] = len(sa & sb)
out["faces_only_it2"] = sorted([list(x) + [zone_of(x[2:5])] for x in sa - sb])
out["faces_only_it3"] = sorted([list(x) + [zone_of(x[2:5])] for x in sb - sa])
def parts(s):
    res = []
    for p in (s.solids() if hasattr(s, "solids") else [s]):
        if p.volume < 1e-6: continue
        e = info(p); c = p.center(); e["center"] = [round(c.X, 3), round(c.Y, 3), round(c.Z, 3)]; e["zones"] = zone_of((c.X, c.Y, c.Z))
        res.append(e)
    return sorted(res, key=lambda e: -e["volume_mm3"])
out["it2_minus_it3_removed"] = parts(A - B)
out["it3_minus_it2_added"] = parts(B - A)
out["volume_change_mm3"] = round(B.volume - A.volume, 4)
small = lambda L: [e for e in L if e["volume_mm3"] < 1000]
chg = out["faces_only_it2"] + out["faces_only_it3"]
zc = {}
for f in chg:
    for zz in f[5]: zc[zz] = zc.get(zz, 0) + 1
out["summary"] = {"faces_it2": out["it2"]["faces"], "faces_it3": out["it3"]["faces"],
    "faces_changed_it2": len(out["faces_only_it2"]), "faces_changed_it3": len(out["faces_only_it3"]),
    "changed_faces_by_zone": zc,
    "removed_pieces": len(small(out["it2_minus_it3_removed"])), "removed_volume_mm3": round(sum(e["volume_mm3"] for e in small(out["it2_minus_it3_removed"])), 4),
    "removed_by_zone": sorted({tuple(e["zones"]) for e in small(out["it2_minus_it3_removed"])}),
    "added_pieces": len(small(out["it3_minus_it2_added"])), "added_volume_mm3": round(sum(e["volume_mm3"] for e in small(out["it3_minus_it2_added"])), 4),
    "added_by_zone": sorted({tuple(e["zones"]) for e in small(out["it3_minus_it2_added"])}),
    "note": "OCC boolean may return a whole-body component (~13.7e3 mm3) in a difference; pieces >= 1000 mm3 are excluded as boolean artefacts of coincident faces. Zone labels are the qa/zones.json boxes evaluated at the face/piece centre (datum frame)."}
write_json("qa/it2_it3_diff.json", {**header("it2_it3_diff", "qa/it2_it3_diff.py (run-local)",
    ["_it2_SUPERSEDED/build/OD-S02_steam-rod_datum.step", "build/OD-S02_steam-rod_datum.step"], None), **out})
print(json.dumps(out["summary"], indent=1, default=list))
