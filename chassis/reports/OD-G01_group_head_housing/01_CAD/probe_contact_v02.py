"""probe_contact_v02.py - a diagnostic, not a gate.

Spec 1.2 §5 U-03(a) asks the housing to meet OD-G10's ear tops exactly at the
ledger's locked pose: clearance 0 there, and 0.20 after a 0.20 mm displacement.
This probe measures, for each candidate value of a parameter, the rim height at
which this housing first meets OD-G10 at the locked clock, by bisection on the
distance between the two solids. It answers one question only: does any value
inside a spec §5 band put that contact at the ledger's locked rim z -11.20?

No gate is answered here; the numbers feed REPORT §8 and §10.

Run: uv run tools/run.py python 01_CAD/probe_contact_v02.py
"""
from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

from tools.measure import clearance

from assemble_od_g01_check_v02 import G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z, load_mates, place_g10
from build_od_g01_housing_v02 import P, build

WORKSPACE = Path(__file__).resolve().parents[1]

# candidates, each inside a spec §5 band unless the note says otherwise
CANDIDATES = [
    ("lug_inner_r", 31.58, "REQ-01 low"),
    ("lug_inner_r", 31.68, "A-02 nominal"),
    ("lug_inner_r", 31.78, "REQ-01 high"),
    ("under_knots", tuple((a, z + 0.051) for a, z in P.under_knots),
     "outside A-05: the whole underside 0.051 higher"),
]


def contact_rim_z(housing, g10, shallow: float = -10.8, deep: float = -11.8,
                  steps: int = 16) -> float | None:
    """The shallowest rim height at which the housing still stands clear of OD-G10."""
    deep_c = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, deep))
    shallow_c = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, shallow))
    if not (deep_c.ok and shallow_c.ok) or deep_c.measured <= 0 or shallow_c.measured > 0:
        return None
    clear, touching = deep, shallow
    for _ in range(steps):
        mid = (clear + touching) / 2
        c = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, mid))
        if not c.ok:
            return None
        if c.measured > 0:
            clear = mid
        else:
            touching = mid
    return round(clear, 6)


def main():
    _, g10 = load_mates()
    out = []
    for name, value, note in CANDIDATES:
        part = build(replace(P, **{name: value}))["part"]
        rim = contact_rim_z(part, g10)
        probe = clearance(part, place_g10(g10, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z - 0.20))
        row = {"parameter": name, "value": value, "note": note,
               "first_contact_rim_z": rim,
               "offset_from_ledger_mm": None if rim is None else round(rim - G10_LOCK_RIM_Z, 6),
               "clearance_at_locked_minus_0.20": probe.measured if probe.ok else None,
               "at": str(probe.at)}
        out.append(row)
        print(json.dumps(row), flush=True)
    (WORKSPACE / "01_CAD" / "probe_contact_v02.json").write_text(
        json.dumps(out, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
