"""Probe (v03): the five new input solids as placed, their validity, envelopes and
Y-axis bores. Guides the build; no gate reads it."""
from __future__ import annotations
import json, math
from pathlib import Path
from build123d import Location, Plane
from tools.core import read_step, validity
from tools.measure import bore_census, envelope

HERE = Path(__file__).resolve().parent
WS = HERE.parent.parent
INPUTS = WS / "00_Spec" / "inputs"

def loc_c16(side, zc):
    if side == "r":
        return Location((117.0, 0.0, zc))
    return Location((-117.0, 0.0, zc)) * Location((0, 0, 0), (0, 180, 0))

PLACE = {
    "c07": ("OD-C07_valve_flowmeter_mount.step", Location(Plane(origin=(-92.0, 0.0, -60.0), x_dir=(0, 0, -1), z_dir=(0, 1, 0)))),
    "c08": ("OD-C08_electronics_bay_tray.step", Location((0, 0, 0))),
    "c09": ("OD-C09_front_panel.step", Location((0, 0, 0))),
    "c11": ("OD-C11_back_panel.step", Location((0, 0, 0))),
    "c16_r-262": ("OD-C16_corner_bracket.step", loc_c16("r", -262.0)),
    "c16_l-262": ("OD-C16_corner_bracket.step", loc_c16("l", -262.0)),
    "c16_r-15": ("OD-C16_corner_bracket.step", loc_c16("r", -15.0)),
    "c16_l-15": ("OD-C16_corner_bracket.step", loc_c16("l", -15.0)),
    "c16_r+62": ("OD-C16_corner_bracket.step", loc_c16("r", 62.0)),
    "c16_l+62": ("OD-C16_corner_bracket.step", loc_c16("l", 62.0)),
}

out = {}
for key, (fname, loc) in PLACE.items():
    comp = read_step(INPUTS / fname)
    sol = comp.solids()
    comp = sol[0] if len(sol) == 1 else comp
    placed = comp.moved(loc)
    v = {k: r.measured for k, r in validity(placed).items()}
    e = {k: round(r.measured, 4) if r.measured is not None else None for k, r in envelope(placed).items()}
    cen = bore_census(placed)
    bores = []
    for b in (cen.detail or {}).get("bores", []):
        a = b["axis_dir"]
        if abs(abs(a[1]) - 1.0) < 1e-6:
            bores.append({"dia": round(b["diameter"], 4), "start": [round(c, 4) for c in b["start"]],
                          "end": [round(c, 4) for c in b["end"]], "len": round(b["length"], 4),
                          "through": b["through"]})
    out[key] = {"validity": v, "envelope": e, "y_bores": sorted(bores, key=lambda r: (r["dia"], r["start"][0]))}
    print(key, v, e)
    for b in out[key]["y_bores"]:
        print("   ", b)
(HERE / "probe_newparts_v03.json").write_text(json.dumps(out, indent=1, default=str))
