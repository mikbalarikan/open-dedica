"""probe_oem_contact_v02.py - a diagnostic, not a gate.

Where does the OEM pair itself meet? The housing reproduces OD-G09's lug undersides
from A-05, and spec 1.2 §5 U-03(a) tests the housing against OD-G10 at the ledger's
locked rim z -11.20 (A-14). This probe measures, by the same bisection on the
distance, the rim height at which the OEM cup OD-G09 first meets OD-G10 at the same
locked clock, so REPORT §10 can say whether -11.20 describes the OEM pair.

Booleans are not used: both reference STEPs read brep_valid = 0 (A-28 and
DESIGN_PLAN §7 R7), and a boolean on an unsound solid is INCONCLUSIVE. Distance is
unaffected.

Run: uv run tools/run.py python 01_CAD/probe_oem_contact_v02.py
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.core import read_step
from tools.measure import clearance

from assemble_od_g01_check_v02 import G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z, load_mates, place_g10

WORKSPACE = Path(__file__).resolve().parents[1]
G09_STEP = WORKSPACE / "00_Spec" / "inputs" / "OD-G09_group_head_bayonet_cup.step"


def contact_rim_z(cup, g10, shallow: float = -10.5, deep: float = -12.5,
                  steps: int = 18) -> float | None:
    deep_c = clearance(cup, place_g10(g10, G10_LOCK_CLOCK_DEG, deep))
    shallow_c = clearance(cup, place_g10(g10, G10_LOCK_CLOCK_DEG, shallow))
    if not (deep_c.ok and shallow_c.ok) or deep_c.measured <= 0 or shallow_c.measured > 0:
        return {"error": "the bracket does not straddle the contact",
                "deep": deep_c.measured if deep_c.ok else None,
                "shallow": shallow_c.measured if shallow_c.ok else None}
    clear, touching = deep, shallow
    for _ in range(steps):
        mid = (clear + touching) / 2
        c = clearance(cup, place_g10(g10, G10_LOCK_CLOCK_DEG, mid))
        if not c.ok:
            return None
        if c.measured > 0:
            clear = mid
        else:
            touching = mid
    return round(clear, 6)


def main():
    cup = read_step(G09_STEP)
    _, g10 = load_mates()
    rim = contact_rim_z(cup, g10)
    rows = {"reference": "OD-G09 group head bayonet cup", "locked_clock_deg": G10_LOCK_CLOCK_DEG,
            "ledger_locked_rim_z": G10_LOCK_RIM_Z, "first_contact_rim_z": rim}
    for label, dz in (("locked", 0.0), ("locked -0.20", -0.20), ("locked +0.20", 0.20)):
        c = clearance(cup, place_g10(g10, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z + dz))
        rows[label] = {"rim_z": round(G10_LOCK_RIM_Z + dz, 4),
                       "clearance": c.measured if c.ok else None, "at": str(c.at),
                       "on_b": str(c.detail.get("on_b")) if c.ok else None}
    print(json.dumps(rows, indent=1, default=str))
    (WORKSPACE / "01_CAD" / "probe_oem_contact_v02.json").write_text(
        json.dumps(rows, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
