"""RV01 U-04 and U-07 provenance: detach the delivered solid, keep its label, write it
with write_step and compare; read the delivered file's schema and unit; compare the
delivered STL body (after the 80-byte header) with a fresh mesh at the REPORT's settings."""
import sys
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
from tools.core import step_roundtrip, compare_step, read_schema, read_length_unit
from tools.core.step import labels, read_header
from build123d import Solid
from OCP.BRepBuilderAPI import BRepBuilderAPI_Copy

out = {}
for stem in ("od_c13_right_C1_v01", "od_c12_left_C1_v01", "od_c16_bracket_C1_v01"):
    p = EXP / f"{stem}.step"
    shape = load(f"{stem}.step")
    lab = labels(shape)
    fresh = Solid(BRepBuilderAPI_Copy(one(shape).wrapped).Shape())
    fresh.label = lab[0]
    rec = {"labels_in_file": lab, "schema_in_file": read_schema(p), "unit_in_file": read_length_unit(p),
           "header": read_header(p)}
    rec["roundtrip"] = step_roundtrip(fresh, WORK / f"rt_{stem}.step", timestamp="2026-10-03T00:00:00")
    rec["compare_delivered"] = compare_step(fresh, p)
    d = (EXP / f"{stem}.stl").read_bytes()
    f = (WORK / f"fresh_{stem}.stl").read_bytes() if (WORK / f"fresh_{stem}.stl").exists() else b""
    rec["stl_header_delivered"] = d[:80].decode("latin1").strip("\x00 ")
    rec["stl_body_equal_fresh"] = d[80:] == f[80:] if f else None
    rec["stl_sizes"] = (len(d), len(f))
    out[stem] = rec
    print(stem, lab, rec["schema_in_file"], rec["unit_in_file"],
          {k: (v.measured, v.status) for k, v in rec["roundtrip"].items()},
          {k: (v.measured, v.status) for k, v in rec["compare_delivered"].items()},
          rec["stl_body_equal_fresh"], rec["stl_sizes"])
dump(out, "roundtrip.json")
