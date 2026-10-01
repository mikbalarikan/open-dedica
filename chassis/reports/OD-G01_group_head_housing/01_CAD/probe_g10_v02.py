"""probe_g10_v02.py - a diagnostic, not a gate: which way does OD-G10 separate from
the lug undersides at the locked pose, and where is the housing's own first contact?

Spec 1.2 §5 U-03 asks for clearance in [0.19, 0.21] "with OD-G10 lifted 0.20 along
+Z from the locked pose". This probe measures the clearance at both signs of the
0.20 mm displacement on the v01 housing, so the v02 check script states a direction
it has measured rather than assumed. Diagnostic output only; no gate is answered here.

Run: uv run tools/run.py python 01_CAD/probe_g10_v02.py
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.core import read_step
from tools.measure import clearance

from assemble_od_g01_check import G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z, load_mates, place_g10

WORKSPACE = Path(__file__).resolve().parents[1]
V01 = WORKSPACE / "02_STEP_STL" / "od_g01_housing_C1_v01.step"


def main():
    housing = read_step(V01)
    _, g10 = load_mates()
    rows = []
    for label, dz in (("locked", 0.0), ("+0.20 along +Z", 0.20), ("-0.20 along -Z", -0.20),
                      ("+0.10", 0.10), ("-0.10", -0.10), ("-0.05", -0.05)):
        c = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z + dz))
        rows.append({"pose": label, "rim_z": round(G10_LOCK_RIM_Z + dz, 4),
                     "clearance": c.measured if c.ok else None, "at": str(c.at),
                     "reason": c.reason})
        print(rows[-1])
    # the shallowest rim height that still reads a positive distance, by bisection
    clear, touching = -13.5, -10.5
    for _ in range(24):
        mid = (clear + touching) / 2
        c = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, mid))
        if c.ok and c.measured > 0:
            clear = mid
        else:
            touching = mid
    print("first contact rim_z", round(clear, 6))
    print(json.dumps({"rows": rows, "first_contact_rim_z": round(clear, 6)}, indent=1))


if __name__ == "__main__":
    main()
