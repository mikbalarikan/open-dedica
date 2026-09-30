import json
from pathlib import Path
from build123d import Solid, Compound, Location
from tools.core import read_step, step_roundtrip, volume_mm3, validity
from tools.core.step import labels
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); W = J / "reviews/RV01_work"; TS = "2026-09-30T00:00:00"
out = {}
plate = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step")
out["plate_type"] = [type(plate).__name__, getattr(plate, "label", None), len(list(plate.children or [])), plate.parent is not None]
out["plate_validity_detail"] = validity(plate)["brep_valid"].detail
s = Solid(plate.solids()[0].wrapped); s.label = "od_c01_frame"
rt = step_roundtrip(s, W / "rt_plate.step", timestamp=TS)
out["rt_plate"] = {k: [v.measured, v.status, v.reason[:150], v.detail.get("built_mm3"), v.detail.get("reimported_mm3")] for k, v in rt.items()}
out["rt_plate_vs_delivered_vol"] = volume_mm3(read_step(W / "rt_plate.step")) - volume_mm3(plate)
asm = read_step(J / "02_STEP_STL/od_c01_assembly_C1_v02.step")
out["asm_type"] = [type(asm).__name__, asm.label, asm.parent is not None, [(type(c).__name__, c.label, c.parent is asm) for c in asm.children]]
kids = []
for c in asm.children:
    k = Solid(c.solids()[0].wrapped); k.label = c.label; kids.append(k)
A = Compound(children=kids, label=asm.label or "asm")
rta = step_roundtrip(A, W / "rt_asm.step", timestamp=TS)
out["rt_asm"] = {k: [v.measured, v.status, v.reason[:150]] for k, v in rta.items()}
if (W / "rt_asm.step").exists():
    back = read_step(W / "rt_asm.step"); bk = {c.label: c for c in back.children}
    out["rt_asm_per_part"] = {c.label: [volume_mm3(bk[c.label]) - volume_mm3(c), len(bk[c.label].faces()) - len(c.faces()),
                              validity(bk[c.label])["brep_valid"].measured] for c in asm.children}
(W / "rv_b2.json").write_text(json.dumps(out, indent=1, default=str)); print(json.dumps(out, indent=1, default=str))
