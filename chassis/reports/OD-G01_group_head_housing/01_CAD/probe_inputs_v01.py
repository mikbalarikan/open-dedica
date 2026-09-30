"""Diagnostic probe of the three reference solids, in the housing frame (D4 input work).

Not a gate: it measures the imported parts so the build's parameters and the
U-03 / REQ-10 feature clearances rest on measured features, not on the reports.
Run: uv run tools/run.py python <this file>
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from build123d import Pos, Rot

from tools.core import read_step, validity
from tools.measure import envelope, radial_extent

WORKSPACE = Path(__file__).resolve().parents[1]
INPUTS = WORKSPACE / "00_Spec" / "inputs"

G04_CLOCK_DEG = 6.05          # spec 1.1 §5 joint (A-12)
G04_SEAT_DZ = -6.82           # flange bottom (its z -13.12) onto the floor z -19.94 (A-13)
G10_LOCK_CLOCK_DEG = 60.26    # DESIGN_PLAN §5
G10_LOCK_RIM_Z = -11.20
G10_INSERT_CLOCK_DEG = 122.5

ORIGIN, ZDIR, XDIR = (0, 0, 0), (0, 0, 1), (1, 0, 0)


def place_g04(shape):
    return Pos(0, 0, G04_SEAT_DZ) * Rot(Z=G04_CLOCK_DEG) * shape


def place_g10(shape, clock_deg: float, rim_z: float):
    return Pos(0, 0, rim_z) * Rot(Z=clock_deg) * Rot(X=180) * shape


def extent(shape, angle, z, side, r_min=0.0, r_max=None):
    r = radial_extent(shape, ORIGIN, ZDIR, XDIR, angle, z, side=side, r_min=r_min, r_max=r_max)
    return None if not r.ok else round(r.measured, 4)


def report(name, shape):
    v = {k: r.measured for k, r in validity(shape).items()}
    e = {k: round(r.measured, 4) for k, r in envelope(shape).items() if r.ok}
    return {"validity": v, "envelope": e}


def main():
    out = {}
    g09 = read_step(INPUTS / "OD-G09_group_head_bayonet_cup.step")
    g04 = read_step(INPUTS / "OD-G04_brewing_gasket_support.step")
    g10 = read_step(INPUTS / "OD-G10_portafilter.step")

    out["OD-G09 raw"] = report("g09", g09)
    out["OD-G04 raw"] = report("g04", g04)
    out["OD-G10 raw"] = report("g10", g10)

    g04p = place_g04(g04)
    out["OD-G04 placed"] = report("g04p", g04p)

    # tab 1 is at housing theta 2.75 (tab phase -3.3 + clock 6.05); tabs at +/-120
    tab_centres = [(-3.3 + G04_CLOCK_DEG + 120 * k) % 360 for k in range(3)]
    out["g04 tab centres deg"] = [round(t, 3) for t in tab_centres]
    tabs = {}
    for k, centre in enumerate(tab_centres, start=1):
        rows = []
        for d in (-28, -20, -10, 0, 10, 20, 28):
            for z in (-16.2, -15.5, -14.8):
                rows.append({"dtheta": d, "z": z,
                             "r_out": extent(g04p, centre + d, z, "outer", r_min=25.0, r_max=40.0)})
        tabs[f"tab{k}"] = rows
    out["g04 tab outer radius"] = tabs

    # tab z extent: walk z at the tab centre looking for material beyond r 32
    walk = []
    for z in [round(-17.4 + 0.1 * i, 2) for i in range(40)]:
        walk.append({"z": z, "r_out@tab1": extent(g04p, tab_centres[0], z, "outer", r_min=32.0, r_max=40.0),
                     "r_out@gap": extent(g04p, tab_centres[0] + 60, z, "outer", r_min=25.0, r_max=40.0)})
    out["g04 z walk"] = walk

    # boss pair A / B and hub, below the floor
    for name, r_c, thetas in (("pairA", 15.5, (-6.55 + G04_CLOCK_DEG, 172.95 + G04_CLOCK_DEG)),
                              ("pairB", 19.03, (113.27 + G04_CLOCK_DEG, -62.02 + G04_CLOCK_DEG))):
        rows = []
        for theta in thetas:
            for z in (-20.2, -21.0, -21.6, -22.3, -22.9):
                rows.append({"theta": round(theta, 3), "z": z,
                             "r_in": extent(g04p, theta, z, "inner", r_min=r_c - 6, r_max=r_c + 6),
                             "r_out": extent(g04p, theta, z, "outer", r_min=r_c - 6, r_max=r_c + 6)})
        out[f"g04 {name}"] = rows
    out["g04 hub"] = [{"z": z, "r_out": extent(g04p, 45.0, z, "outer", r_min=0.0, r_max=12.0)}
                      for z in (-19.0, -20.0, -21.0, -22.0, -22.5, -22.6)]

    for tag, clock, rim in (("locked", G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z),
                            ("insertion", G10_INSERT_CLOCK_DEG, -11.69)):
        p = place_g10(g10, clock, rim)
        out[f"OD-G10 {tag}"] = report("g10p", p)
        ears = []
        for k, theta_g10 in enumerate((59.5, 180.0, 300.5), start=1):
            theta = (clock - theta_g10) % 360
            for d in (-16, -8, 0, 8, 16):
                col = []
                for z in [round(rim + 0.1 * i, 2) for i in range(0, 80)]:
                    col.append(extent(p, theta + d, z, "outer", r_min=28.0, r_max=40.0))
                ears.append({"ear": k, "theta": round(theta + d, 3), "z0": rim,
                             "r_out_by_z": col})
        out[f"g10 {tag} ear radius"] = ears
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
