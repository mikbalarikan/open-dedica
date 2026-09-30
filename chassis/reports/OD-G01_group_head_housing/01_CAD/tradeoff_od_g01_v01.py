"""tradeoff_od_g01_v01.py - the measured trade-off study behind REPORT §10 (D9).

Spec 1.1 asks, in one 5.00 mm slab, for REQ-13's Ø34.0 x 2.50 rear counterbore,
REQ-07's Ø3.8 screw holes at r 19.03 under Ø9.0 x 2.30 recesses, and REQ-11's
2.50 web at the Ø26 opening. The built part measures two walls below D-01a's 0.8:
the web between the counterbore wall and a screw hole, and the flake between a
recess floor and the counterbore ceiling. This script rebuilds the same model with
each option the REPORT offers and measures min_wall on it, so the Usta sees what
each option buys. Nothing here is a deliverable: the files land in
01_CAD/sweep_v01/ and carry the option in their name.

Run: uv run tools/run.py python 01_CAD/tradeoff_od_g01_v01.py
"""
from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

from tools.core import read_step, validity, write_step
from tools.measure import min_wall
from tools.result import gate

from build_od_g01_housing import P, TIMESTAMP, build

WORKSPACE = Path(__file__).resolve().parents[1]
SWEEP = WORKSPACE / "01_CAD" / "sweep_v01"

OPTIONS = {
    "as_specified": {},
    "opt1_counterbore_32p2_deep_1p70": {"counterbore_d": 32.2, "counterbore_depth": 1.70},
    "opt2_no_counterbore": {"counterbore_d": 26.0, "counterbore_depth": 0.0},
    "opt3_slab_6p50_counterbore_32p2": {"plate_t": 6.50, "counterbore_d": 32.2},
}


def main():
    SWEEP.mkdir(parents=True, exist_ok=True)
    out = []
    for name, changes in OPTIONS.items():
        params = replace(P, **changes) if changes else P
        part = build(params)["part"]
        part.label = "od_g01_housing"
        path = SWEEP / f"od_g01_housing_C1_v01_tradeoff_{name}.step"
        write_step(part, path, timestamp=TIMESTAMP)
        shape = read_step(path)
        v = {k: (r.measured if r.ok else None) for k, r in validity(shape).items()}
        wall = min_wall(shape)
        row = {"option": name, "changes": changes, "file": str(path.relative_to(WORKSPACE)),
               "validity": v,
               "min_wall_mm": wall.measured if wall.ok else None,
               "at": str(wall.at), "reason": wall.reason,
               "D-01a": gate("D-01a", wall, ">=", 0.8, band=0.005).status,
               "D-01b": gate("D-01b", wall, ">=", 1.0, band=0.005).status}
        out.append(row)
        print(json.dumps(row))
    (WORKSPACE / "01_CAD" / "tradeoff_v01.json").write_text(json.dumps(out, indent=1, default=str),
                                                            encoding="utf-8")


if __name__ == "__main__":
    main()
