"""RV01 reviewer measurements, part rows, on the delivered mount STEP (read only)."""
import json, sys, math
from pathlib import Path
from tools.core import read_step, validity, read_schema, read_length_unit, compare_step, step_roundtrip, solids
from tools.core.step import labels, file_sha256, read_header
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, mass_properties, min_internal_radius)
from build123d import Face
from tools.measure.sampling import kind

W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount")
OUT = W / "reviews/RV01_work"
step = W / "02_STEP_STL/od_c04_mount_C1_v01.step"
out = {"sha256": file_sha256(step)}
part = read_step(step)
out["labels"] = labels(part)
out["schema"] = read_schema(step); out["unit"] = read_length_unit(step)
out["validity"] = {k: r.to_dict() for k, r in validity(part).items()}
out["envelope"] = {k: r.measured for k, r in envelope(part).items()}
fc = feature_census(part)
out["feature_census"] = {k: r.measured for k, r in fc.items()}
bc = bore_census(part)
out["bores"] = bc.detail["bores"]
loc = {}
for name, p, d in [("S1", (-19.62, 20.18, -13.5), (0, 0, 1)), ("S2", (25.01, 9.08, -13.5), (0, 0, 1)),
                   ("F-40_-8", (-40, -68, -8), (0, 1, 0)), ("F+40_-8", (40, -68, -8), (0, 1, 0)),
                   ("F-40_26", (-40, -68, 26), (0, 1, 0)), ("F+40_26", (40, -68, 26), (0, 1, 0))]:
    loc[name] = {k: r.to_dict() for k, r in locate_bore(bc, p, d).items()}
out["locate"] = loc
# faces by kind with location
fl = []
for f in part.faces():
    bb = f.bounding_box()
    fl.append({"kind": kind(f.wrapped), "area": round(f.area, 4),
               "min": [round(v, 4) for v in (bb.min.X, bb.min.Y, bb.min.Z)],
               "max": [round(v, 4) for v in (bb.max.X, bb.max.Y, bb.max.Z)]})
out["faces"] = fl
mw = min_wall(part); out["min_wall"] = mw.to_dict()
mww = min_wall_wide(part); out["min_wall_wide"] = mww.to_dict()
oh = overhang_census(part, build_dir=(0, 0, 1), min_deg=45); out["overhang"] = oh.to_dict()
out["mass"] = {k: r.measured for k, r in mass_properties(part, 1070).items()}
out["min_internal_radius"] = min_internal_radius(part).to_dict()
# U-04: delivered file header, and a round trip of the re-imported shape
out["header"] = read_header(step)
out["roundtrip"] = {k: r.to_dict() for k, r in step_roundtrip(part, OUT / "rt_mount.step", timestamp="2026-09-30T00:00:00").items()}
(OUT / "m1_part.json").write_text(json.dumps(out, indent=1, default=str))
print("done")
