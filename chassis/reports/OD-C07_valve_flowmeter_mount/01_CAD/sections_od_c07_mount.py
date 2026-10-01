"""D6 screening sections of od_c07_mount v01 (and the check assembly), from the exported STEPs.
Each set is written by tools.drawing.write_sections, then named after its plane and position."""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
from tools.core import read_step
from tools.drawing import write_sections

part = read_step(WS / "02_STEP_STL/od_c07_mount_C1_v01.step")
asm = read_step(WS / "02_STEP_STL/od_c07_assembly_C1_v01.step")
out = WS / "03_Sections"
tmp = HERE / "check_out_v01" / "_sections_tmp"
sets = [  # (shape, name, views, through point, what it shows)
    (part, "od_c07_mount", ("front",), (0.0, 0.0, 10.25), "y0"),        # XZ through both axes: pedestal, recess, pin holes, ring, deck, slits, screw and insert bores
    (part, "od_c07_mount", ("top",), (0.0, 0.0, 10.25), "z10p25"),      # ring notches, pin holes, recess wall
    (part, "od_c07_mount", ("top",), (62.0, 0.0, 47.0), "z47"),         # U-slot, slits, screw holes, deck arms
    (part, "od_c07_mount", ("left",), (62.0, 0.0, 44.0), "x62"),        # YZ through the valve axis: slot open to +Y, deck, legs
    (part, "od_c07_mount", ("left",), (7.48, 0.0, 20.0), "x7p48"),      # through the 70° hook: beam, catch, lead-in, root fillets
    (part, "od_c07_mount", ("left",), (-11.78, 0.0, 10.0), "xm11p78"),  # through pin hole 2, the ring and the 160° hook region
    (asm, "od_c07_assembly", ("front",), (0.0, 0.0, 10.25), "y0"),      # seats as placed: rim on the pedestal, flange on the deck, stem in the slot
    (asm, "od_c07_assembly", ("left",), (62.0, 0.0, 44.0), "x62"),
]
log = []
for shape, name, views, through, tag in sets:
    if tmp.exists():
        shutil.rmtree(tmp)
    ws = write_sections(shape, tmp, part=name, version=1, views=views, through=through)
    for w in ws:
        dst = out / f"{name}_v01_{w.detail['view']}_{tag}.png"
        out.mkdir(parents=True, exist_ok=True)
        shutil.move(str(w.path), dst)
        nc = w.checks["nothing_clipped"]
        log.append({"file": str(dst.relative_to(WS)), "sha256": w.sha256, "view": w.detail["view"], "through": through,
                    "plane": w.detail["plane"], "cut_area_mm2": w.detail["cut_area_mm2"],
                    "nothing_clipped": nc.measured, "status": nc.status, "reason": nc.reason})
shutil.rmtree(tmp, ignore_errors=True)
(HERE / "check_out_v01" / "sections_v01.json").write_text(json.dumps(log, indent=1, default=str))
for r in log:
    print(r["file"], r["plane"], round(r["cut_area_mm2"], 1), "clipped px", r["nothing_clipped"], r["status"])
