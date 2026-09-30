"""probe_oem_contact_v03.py - a diagnostic, not a gate.

Spec 1.3 §5 U-03(a) defines the locked pose as the measured first contact of the
ear tops with the lug undersides and probes 0.20 mm along -Z from it. This script
applies exactly that definition to the OEM pair OD-G09 | OD-G10, so REPORT §3 can
say whether the housing reads the same as the cup it reproduces. It measures:

  - the rim height at which OD-G09 first meets OD-G10 at the locked clock, by the
    same bisection on the distance the checks use;
  - the clearance 0.20 mm along -Z from that height, which is U-03(a)'s probe;
  - the clearance at A-14's -11.20 and at -11.20 -+ 0.20, the readings spec 1.2
    asked for, kept so the two specs can be compared on one part.

Booleans are not used: both reference STEPs read brep_valid = 0 (A-28 and
DESIGN_PLAN §7 R7), and a boolean on an unsound solid is INCONCLUSIVE. Distance is
unaffected.

Run: uv run tools/run.py python 01_CAD/probe_oem_contact_v03.py
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.core import read_step
from tools.measure import clearance

from assemble_od_g01_check_v03 import (A14_RIM_Z, G10_LOCK_CLOCK_DEG, first_contact_rim_z,
                                       load_mates, place_g10)

WORKSPACE = Path(__file__).resolve().parents[1]
G09_STEP = WORKSPACE / "00_Spec" / "inputs" / "OD-G09_group_head_bayonet_cup.step"
PROBE_MM = 0.20


def reading(cup, g10, rim_z: float) -> dict:
    c = clearance(cup, place_g10(g10, G10_LOCK_CLOCK_DEG, rim_z))
    return {"rim_z": round(rim_z, 6), "clearance": c.measured if c.ok else None,
            "at": str(c.at), "on_b": str(c.detail.get("on_b")) if c.ok else None,
            "reason": c.reason}


def main():
    cup = read_step(G09_STEP)
    _, g10 = load_mates()
    rim = first_contact_rim_z(cup, g10, G10_LOCK_CLOCK_DEG, bracket=(-10.5, -12.5), steps=24)
    rows = {"reference": "OD-G09 group head bayonet cup",
            "locked_clock_deg": G10_LOCK_CLOCK_DEG,
            "a14_expected_rim_z": A14_RIM_Z,
            "spec_1_3_locked_rim_z_measured": rim,
            "offset_from_a14_mm": None if rim is None else round(rim - A14_RIM_Z, 6)}
    if rim is not None:
        rows["spec_1_3: at the measured locked pose"] = reading(cup, g10, rim)
        rows["spec_1_3: probe, locked - 0.20 along -Z"] = reading(cup, g10, rim - PROBE_MM)
        rows["for comparison: at A-14 -11.20"] = reading(cup, g10, A14_RIM_Z)
        rows["for comparison: A-14 -11.20 - 0.20"] = reading(cup, g10, A14_RIM_Z - PROBE_MM)
    print(json.dumps(rows, indent=1, default=str))
    (WORKSPACE / "01_CAD" / "probe_oem_contact_v03.json").write_text(
        json.dumps(rows, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
