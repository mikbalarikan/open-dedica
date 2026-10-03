"""Reviewer RV01 helpers: paths, the GATES band, gating, JSON out."""
import json, math, sys
from pathlib import Path
from tools.result import gate
J = Path("/root/oguz-jobs/20261001-od-c08-electronics-bay-tray")
W = J / "reviews/RV01_work"
PART = J / "02_STEP_STL/od_c08_tray_C1_v01.step"
ASM = J / "02_STEP_STL/od_c08_assembly_C1_v01.step"
STL = J / "02_STEP_STL/od_c08_tray_C1_v01.stl"
TMF = J / "02_STEP_STL/od_c08_tray_C1_v01.3mf"
E01 = J / "00_Spec/inputs/OD-E01_power_pcb.step"
C01 = J / "00_Spec/inputs/OD-C01_base_frame.step"
C02 = J / "00_Spec/inputs/OD-C02_bulkhead.step"
BAND = {"mm": 0.005, "mm3": 0.001, "deg": 0.001, "count": 0, "bool": 0, "rad": 0.001}
ROWS = []
def g(gid, res, op, limit, assumes=(), required=None, note=""):
    gt = gate(gid, res, op, limit, band=BAND.get(res.unit, 0.005), assumes=assumes, required=required)
    row = gt.row(); row["note"] = note
    if res.status != "MEASURED": row["reason"] = res.reason
    ROWS.append(row)
    print(f"{row['gate']:40s} {row['status']:13s} {row['measured']} {row['unit']} req {row['required']} margin {row['margin']} at {row['at']} {note} {row.get('reason','') or ''}", flush=True)
    return gt
def dump(name, extra=None):
    out = {"rows": ROWS, "extra": extra or {}}
    (W / name).write_text(json.dumps(out, indent=1, default=str))
