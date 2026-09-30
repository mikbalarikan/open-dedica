"""probe_placed_v02.py - the placed mating parts, measured where the joints put them.

A record for REPORT §5: with OD-G04 at its seated pose and OD-G10 at the locked and
insertion poses, this reads back the envelope of each placed solid and the radius
and height of the features the joints were built from, so the REPORT states measured
positions rather than the numbers the joint was given.

Run: uv run tools/run.py python 01_CAD/probe_placed_v02.py
"""
from __future__ import annotations

import json
from pathlib import Path

from tools.measure import envelope, radial_extent

from assemble_od_g01_check_v02 import (G10_INSERT_CLOCK_DEG, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z,
                                       G10_ROTATE_RIM_Z, feature_pieces, g04_tab_centres,
                                       g10_ear_centres, load_mates, place_g04, place_g10)

WORKSPACE = Path(__file__).resolve().parents[1]
ORIGIN, ZDIR, XDIR = (0, 0, 0), (0, 0, 1), (1, 0, 0)


def env(shape) -> dict:
    e = envelope(shape)
    return {k: (round(r.measured, 4) if r.ok else None) for k, r in e.items()}


def main():
    g04, g10 = load_mates()
    g04p = place_g04(g04)
    out = {"od_g04_seated": {"envelope": env(g04p), "tab_centres_deg": g04_tab_centres()},
           "od_g10_locked": {"envelope": env(place_g10(g10, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z)),
                             "ear_centres_deg": g10_ear_centres(G10_LOCK_CLOCK_DEG)},
           "od_g10_insertion": {"envelope": env(place_g10(g10, G10_INSERT_CLOCK_DEG,
                                                          G10_ROTATE_RIM_Z)),
                                "ear_centres_deg": g10_ear_centres(G10_INSERT_CLOCK_DEG)}}
    pieces = feature_pieces(g04p)
    out["od_g04_pieces"] = {name: env(piece) for name, piece in pieces.items()}
    # the tab tip radius and the bead peak, on the placed solid
    tips = {}
    for k, centre in enumerate(g04_tab_centres(), start=1):
        r = radial_extent(g04p, ORIGIN, ZDIR, XDIR, centre, -15.50, side="outer",
                          r_min=25.0, r_max=40.0)
        tips[f"tab{k}"] = {"angle_deg": round(centre, 3), "z": -15.50,
                           "outer_r": round(r.measured, 4) if r.ok else None}
    bead = radial_extent(g04p, ORIGIN, ZDIR, XDIR, 60.0, -15.17, side="outer",
                         r_min=25.0, r_max=40.0)
    out["od_g04_tab_tips"] = tips
    out["od_g04_bead_at_60deg_z_-15.17"] = round(bead.measured, 4) if bead.ok else None
    print(json.dumps(out, indent=1, default=str))
    (WORKSPACE / "01_CAD" / "probe_placed_v02.json").write_text(
        json.dumps(out, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
