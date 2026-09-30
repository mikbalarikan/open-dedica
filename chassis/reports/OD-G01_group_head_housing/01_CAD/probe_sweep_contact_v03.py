"""probe_sweep_contact_v03.py - spec 1.3's U-03(a) rows re-measured on the v02 sweep
solids. A diagnostic that carries REPORT §4, not a gate.

The build script is unchanged from v02, so WP-06 says the v02 sweep stands and 40
builds are not to be re-run. Its geometric rows are measurements of those same
solids and stand as they are; its two U-03(a) probe rows do not, because spec 1.3
redefines the pose they were measured at. This script re-measures those two rows
under spec 1.3 - first contact by bisection, then the clearance 0.20 mm along -Z
from it - on the sweep STEPs that already exist in 01_CAD/sweep_v02/, without
rebuilding anything.

Which cases: the sweep's fit-critical parameters that can move the ear-top contact.
`lug_inner_r` and `lug_starts` move the lug the ear lands on; `lug_span`,
`stop_end_off` and `stop_bottom_z` move the lug's ends and its stop block, which is
what the ear leading edge meets. The remaining sweep parameters are below the shelf
(lip, pockets, slab, bores, inserts) or are the bore radius, and cannot reach the
contact; `under_knots` is the underside itself and is the one lever, so both its
ends are measured too.

Run: uv run tools/run.py python 01_CAD/probe_sweep_contact_v03.py
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.core import read_step
from tools.measure import clearance

from assemble_od_g01_check_v03 import (A14_BAND, A14_RIM_Z, G10_LOCK_CLOCK_DEG,
                                       first_contact_rim_z, load_mates, place_g10)

WORKSPACE = Path(__file__).resolve().parents[1]
SWEEP = WORKSPACE / "01_CAD" / "sweep_v02"
PROBE_MM = 0.20
PROBE_BAND = (0.19, 0.21)

CASES = ("lug_inner_r_lo", "lug_inner_r_hi", "lug_starts_lo", "lug_starts_hi",
         "lug_span_lo", "lug_span_hi", "stop_end_off_lo", "stop_end_off_hi",
         "stop_bottom_z_lo", "stop_bottom_z_hi", "under_knots_lo", "under_knots_hi")


def main():
    _, g10 = load_mates()
    out = []
    for case in CASES:
        step = SWEEP / f"od_g01_housing_C1_v02_{case}.step"
        row = {"case": case, "file": str(step.relative_to(WORKSPACE))}
        if not step.exists():
            row["error"] = "no sweep STEP for this case"
            out.append(row)
            continue
        housing = read_step(step)
        rim = first_contact_rim_z(housing, g10, G10_LOCK_CLOCK_DEG)
        row["locked_rim_z_measured"] = rim
        if rim is None:
            row["error"] = "the bisection could not measure a first contact"
        else:
            row["within_a14_band"] = abs(rim - A14_RIM_Z) <= A14_BAND
            at_contact = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, rim))
            probe = clearance(housing, place_g10(g10, G10_LOCK_CLOCK_DEG, rim - PROBE_MM))
            row["clearance_at_locked"] = at_contact.measured if at_contact.ok else None
            row["clearance_at_locked_minus_0.20_along_-Z"] = (probe.measured if probe.ok
                                                              else None)
            row["probe_in_band"] = (probe.ok and PROBE_BAND[0] <= probe.measured
                                    <= PROBE_BAND[1])
            row["at"] = str(probe.at)
        out.append(row)
        print(json.dumps(row, default=str))
    (WORKSPACE / "01_CAD" / "probe_sweep_contact_v03.json").write_text(
        json.dumps(out, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
