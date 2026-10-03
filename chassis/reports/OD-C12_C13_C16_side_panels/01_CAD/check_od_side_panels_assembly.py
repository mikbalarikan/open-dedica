"""Assembly checks for od_side_panels_v01 (D3): U-03 (a) and (b), REQ-05 at the six poses, REQ-06, REQ-07.

Written before assemble_od_side_panels.py. The parts are read from the re-imported assembly STEP
by label; the same labels are placed again from the three part STEPs and the inputs by the joints
of section 2, and the two must agree (the assembly holds the reviewed part files, as placed).

Run: check_od_side_panels_assembly.py [--asm S] [--json OUT] [--quick]
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np  # noqa: E402
from build123d import Cylinder, Location, Vector  # noqa: E402

from checklib_od_side_panels import (BAND_MM, BAND_MM3, BAND_N, CAD, OUT, Rows, axis_offset, bores_along,  # noqa: E402
                                     nearest_bore, run_guarded, val)
from params_od_side_panels import P  # noqa: E402
from placements_od_side_panels import bracket_poses, new_parts, references  # noqa: E402
from tools.core import common_volume, read_step  # noqa: E402
from tools.measure import bore_census, clearance  # noqa: E402

SPEC = {
    "contact": 0.0,                 # U-03 (a) designed contacts: clearance = 0
    "others_min": 0.5,              # U-03 (a) every other pair
    "lip_gap": (0.35, 0.45),        # U-03 (a) / REQ-02: 0.40 +- 0.05
    "coax": 0.10,                   # U-03 (a) insert bore to panel hole
    "plate_hole_x": 104.5, "plate_hole_tol": 0.10,          # REQ-05
    "edge_min": 8.0, "hole_min": 6.0, "disc_d": 8.0,        # REQ-06
    "handed_over": [(88, -222), (88, -78), (106, -222), (106, -78),          # OD-C08
                    (81, -282), (95, -282), (-81, -282), (-95, -282)],       # OD-C11
    "plate": {"x": 120.0, "z": (-305.0, 100.0), "y": (-6.0, 0.0)},          # section 2
    "keepout": {"d": 8.0, "h": 2.0, "at": [(110, 90), (-110, 90), (110, -295), (-110, -295)]},  # REQ-07
    "access_r": 4.0, "access_y": (16.0, 215.0), "access_out": 20.0,          # REQ-07
    "path": {"bracket": 20.0, "panel": 20.0, "lid": 40.0, "step": 2.0},     # U-03 (b)
}
NEW_PANELS = ("od_c13_right", "od_c12_left")


def leaves(shape, out=None):
    out = {} if out is None else out
    kids = list(getattr(shape, "children", ()) or ())
    if kids:
        for k in kids:
            leaves(k, out)
    elif shape.label:
        sol = shape.solids()
        out.setdefault(shape.label, []).extend(sol)
    return out


def from_assembly(path):
    asm = read_step(path)
    got = leaves(asm)
    return {k: (v[0] if len(v) == 1 else v) for k, v in got.items()}


def side_of(label):
    return 1 if (label.endswith("right") or "_R" in label) else -1


def contacts(labels):
    pairs = set()
    for b in [l for l in labels if l.startswith("od_c16_bracket")]:
        pairs.add(frozenset((b, "OD-C01")))
        pairs.add(frozenset((b, "od_c13_right" if "_R" in b else "od_c12_left")))
    for p in NEW_PANELS:
        pairs.add(frozenset((p, "OD-C01")))
        pairs.add(frozenset((p, "OD-C10")))
    return pairs


def cv(a, b):
    return common_volume(a, b)


def static(rows, named):
    labels = list(named)
    new = [l for l in labels if l in NEW_PANELS or l.startswith("od_c16_bracket")]
    con = contacts(labels)
    done = set()
    for a in new:
        for b in labels:
            if a == b or frozenset((a, b)) in done:
                continue
            done.add(frozenset((a, b)))
            pair = f"{a}|{b}"
            cl = clearance(named[a], named[b])
            if frozenset((a, b)) in con:
                rows.add(f"U-03a contact {pair} clearance", cl, "==", SPEC["contact"], BAND_MM,
                         assumes=("A-01",) if "OD-C01" in pair else ("A-02",) if "OD-C10" in pair else ())
                rows.add(f"U-03a contact {pair} interference", cv(named[a], named[b]), "<=", 0.0, BAND_MM3)
            else:
                rows.add(f"U-03a {pair} clearance", cl, ">=", SPEC["others_min"], BAND_MM,
                         assumes=("A-04",) if "OD-C07" in pair else ("A-05",) if "OD-C08" in pair else ("A-03",)
                         if "OD-C11" in pair else ())


def lip(rows, named):
    from checklib_od_side_panels import box, common_part
    for p in NEW_PANELS:
        s = 1 if p.endswith("right") else -1
        region = common_part(named[p], box(s * 100.0, s * 125.0, P.wall_top_y, 230.0, -300.0, 100.0))
        cl = clearance(region, named["OD-C10"])
        rows.add(f"U-03a lip {p}|OD-C10 gap", cl, "in", SPEC["lip_gap"], BAND_MM, assumes=("A-02", "A-14"))


def coaxial_and_plate_holes(rows, named, p=P):
    bc = {p_: bore_census(named[p_]) for p_ in NEW_PANELS}
    for label, (origin, _, _) in bracket_poses(p).items():
        s = 1 if "_R" in label else -1
        zc = origin[2]
        panel = "od_c13_right" if s > 0 else "od_c12_left"
        b_c = bore_census(named[label])
        ins = nearest_bore(b_c, (s * (p.bracket_origin_x - 1.0), 10.0, zc), (1, 0, 0))
        hole = nearest_bore(bc[panel], (s * 118.5, 10.0, zc), (1, 0, 0))
        off = axis_offset(ins, hole)
        rows.add(f"U-03a coaxial {label} insert bore | {panel} hole", val("coax_offset", off, "mm",
                 insert=ins["start"], hole=hole["start"]), "<=", SPEC["coax"], BAND_MM)
        ph = nearest_bore(b_c, (s * SPEC["plate_hole_x"], 1.5, zc), (0, 1, 0))
        d = math.hypot(ph["start"][0] - s * SPEC["plate_hole_x"], ph["start"][2] - zc)
        rows.add(f"REQ-05 plate hole {label} at ({s * SPEC['plate_hole_x']:+.1f}, {zc:+.0f})",
                 val("plate_hole_offset", d, "mm", at=ph["start"]), "<=", SPEC["plate_hole_tol"], BAND_MM,
                 assumes=("A-01", "A-07"))


def req06(rows, named, p=P):
    c01 = named["OD-C01"]
    bc = bore_census(c01)
    vertical = bores_along(bc, (0, 1, 0))
    existing = [(b["start"][0], b["start"][2], b["diameter"]) for b in vertical]
    pl = SPEC["plate"]
    for sx in (1, -1):
        for zc in p.hole_z:
            x = sx * SPEC["plate_hole_x"]
            edge = min(pl["x"] - abs(x), zc - pl["z"][0], pl["z"][1] - zc)
            rows.add(f"REQ-06 ({x:+.1f},{zc:+.0f}) to plate edge", val("edge_distance", edge, "mm"), ">=",
                     SPEC["edge_min"], BAND_MM, assumes=("A-01",))
            dists = [(math.hypot(x - ex, zc - ez), (ex, ez, d)) for ex, ez, d in existing]
            dmin = min(dists)
            rows.add(f"REQ-06 ({x:+.1f},{zc:+.0f}) to nearest OD-C01 hole", val("hole_distance", dmin[0], "mm",
                     nearest=dmin[1], holes=len(existing)), ">=", SPEC["hole_min"], BAND_MM, assumes=("A-01",))
            hmin = min((math.hypot(x - hx, zc - hz), (hx, hz)) for hx, hz in SPEC["handed_over"])
            rows.add(f"REQ-06 ({x:+.1f},{zc:+.0f}) to nearest handed-over insert", val("insert_distance", hmin[0],
                     "mm", nearest=hmin[1]), ">=", SPEC["hole_min"], BAND_MM, assumes=("A-01",))
            h = pl["y"][1] - pl["y"][0]
            disc = Cylinder(SPEC["disc_d"] / 2, h).moved(Location((x, (pl["y"][0] + pl["y"][1]) / 2, zc), (90, 0, 0)))
            c = common_volume(disc, c01)
            short = val("disc_missing", disc.volume - c.measured, "mm3", disc=disc.volume) if c.ok else c
            rows.add(f"REQ-06 ({x:+.1f},{zc:+.0f}) plate solid in a D8 disc (missing volume)", short, "<=", 0.0,
                     BAND_MM3, assumes=("A-01",))


def _cyl_y(x, z, r, y0, y1):
    return Cylinder(r, y1 - y0).moved(Location((x, (y0 + y1) / 2, z), (90, 0, 0)))


def _cyl_x(x0, x1, y, z, r):
    return Cylinder(r, abs(x1 - x0)).moved(Location(((x0 + x1) / 2, y, z), (0, 90, 0)))


def req07(rows, named, p=P):
    new = [l for l in named if l in NEW_PANELS or l.startswith("od_c16_bracket")]
    ko = SPEC["keepout"]
    for x, z in ko["at"]:
        cyl = _cyl_y(x, z, ko["d"] / 2, 0.0, ko["h"])
        worst = None
        for l in new:
            r = common_volume(cyl, named[l])
            if not r.ok:
                worst = r
                break
            if worst is None or r.measured > worst.measured:
                worst = val("keepout_common", r.measured, "mm3", part=l)
        rows.add(f"REQ-07 keep-out D8x2 at foot ({x:+.0f},{z:+.0f})", worst, "<=", 0.0, BAND_MM3)
    r_ = SPEC["access_r"]
    for label, (origin, _, _) in bracket_poses(p).items():
        s = 1 if "_R" in label else -1
        zc = origin[2]
        x = s * SPEC["plate_hole_x"]
        cyl = _cyl_y(x, zc, r_, *SPEC["access_y"])
        worst = None
        for l, sh in named.items():
            if l in NEW_PANELS or l == "OD-C10":
                continue
            r = common_volume(cyl, sh)
            if not r.ok:
                worst = r
                break
            if worst is None or r.measured > worst.measured:
                worst = val("access_common", r.measured, "mm3", part=l)
        rows.add(f"REQ-07 driver access {label} (r4, y16..215)", worst, "<=", 0.0, BAND_MM3, assumes=("A-05",))
        xo = s * p.wall_outer_x
        cyl = _cyl_x(xo, xo + s * SPEC["access_out"], p.panel_hole_y, zc, r_)
        worst = None
        for l, sh in named.items():
            r = common_volume(cyl, sh)
            if not r.ok:
                worst = r
                break
            if worst is None or r.measured > worst.measured:
                worst = val("access_common", r.measured, "mm3", part=l)
        rows.add(f"REQ-07 panel screw access {label} (r4, 20 outside)", worst, "<=", 0.0, BAND_MM3)


def _steps(total, step):
    n = int(round(total / step))
    return [total - i * step for i in range(n + 1)]


def path(rows, named):
    st = SPEC["path"]["step"]
    delivered = [l for l in named if l.startswith("OD-")]
    brackets = [l for l in named if l.startswith("od_c16_bracket")]

    def sweep(mover, against, vec, total, gate_name, assumes=()):
        worst, worst_at, bad, computed = None, None, None, 0
        for d in _steps(total, st):
            moved = named[mover].moved(Location(tuple(c * d for c in vec)))
            for other in against:
                r = common_volume(moved, named[other])
                if not r.ok:
                    bad = (r, d, other)
                    break
                computed += r.detail.get("pairs_computed", 0)
                if worst is None or r.measured > worst:
                    worst, worst_at = r.measured, (d, other)
            if bad:
                break
        if bad:
            rows.add(gate_name, bad[0], "<=", 0.0, BAND_MM3, note=f"INCONCLUSIVE at offset {bad[1]} vs {bad[2]}")
        else:
            rows.add(gate_name, val("path_interference", worst, "mm3", worst_at=worst_at,
                                    poses=len(_steps(total, st))), "<=", 0.0, BAND_MM3, assumes=assumes,
                     note=f"worst {worst:.6f} mm3 first at offset {worst_at[0]} vs {worst_at[1]}; "
                          f"{len(_steps(total, st))} poses x {len(against)} solids; {computed} solid pairs "
                          f"computed by boolean, the rest apart by bounding box")
    # (1) brackets lowered along -Y from +20 with every delivered part present (and the other brackets)
    for b in brackets:
        sweep(b, delivered + [o for o in brackets if o != b], (0, 1, 0), SPEC["path"]["bracket"],
              f"U-03b path bracket {b} down from +20")
    # (2) panels moved inward along X from 20 outside, brackets in place, lid off
    for p_ in NEW_PANELS:
        s = 1 if p_.endswith("right") else -1
        against = [l for l in named if l not in (p_, "OD-C10")]
        sweep(p_, against, (s, 0, 0), SPEC["path"]["panel"], f"U-03b path panel {p_} inward from 20 outside")
    # (3) OD-C10 lowered from +40 with the panels in place
    sweep("OD-C10", [l for l in named if l != "OD-C10"], (0, 1, 0), SPEC["path"]["lid"],
          "U-03b path OD-C10 down from +40")


def agree(rows, from_asm, from_parts):
    """The assembly STEP holds the part files as placed: same labels; per label volume and centre."""
    rows.add("assembly labels match the placements", val("labels_match",
             int(sorted(from_asm) == sorted(from_parts)), "bool", asm=sorted(from_asm)), "==", 1, BAND_N)
    worst = 0.0
    for k, s in from_parts.items():
        a = from_asm.get(k)
        if a is None or isinstance(a, list):
            worst = float("inf")
            continue
        dc = (Vector(*a.center()) - Vector(*s.center())).length
        dv = abs(a.volume - s.volume)
        worst = max(worst, dc, dv)
    rows.add("assembly solids = placed part files (max centre / volume delta)", val("asm_delta", worst, "mm"),
             "<=", 0.0, BAND_MM)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asm", default=str(OUT / "od_side_assembly_C1_v01.step"))
    ap.add_argument("--json", default=str(CAD / "results_v01" / "check_od_side_panels_assembly.json"))
    ap.add_argument("--skip-path", action="store_true")
    a = ap.parse_args()
    rows = Rows("od_side_assembly")
    t0 = time.time()
    named = from_assembly(Path(a.asm))
    refs = {k: (v[0] if len(v) == 1 else v) for k, v in references().items()}
    placed = {**refs, **new_parts()}
    run_guarded(rows, "assembly agreement", "mm", agree, rows, named, placed)
    multi = [k for k, v in named.items() if isinstance(v, list)]
    rows.add("assembly: one solid per label", val("multi_solid_labels", len(multi), "count", labels=multi), "==", 0, BAND_N)
    rows.add("assembly solid count", val("asm_solids", sum(1 for _ in named), "count"), "==", 19, BAND_N)
    for name, fn in (("U-03a static", static), ("U-03a lip", lip), ("U-03a coax/REQ-05", coaxial_and_plate_holes),
                     ("REQ-06", req06), ("REQ-07", req07)):
        run_guarded(rows, name, "-", fn, rows, named)
        print(f"[{time.time() - t0:7.1f}s] {name}", flush=True)
    if not a.skip_path:
        run_guarded(rows, "U-03b", "mm3", path, rows, named)
        print(f"[{time.time() - t0:7.1f}s] U-03b", flush=True)
    rows.table()
    rows.dump(Path(a.json), {"asm": a.asm})
    print("WORST", rows.worst())


if __name__ == "__main__":
    main()
