"""D7 robustness sweep of od_t01_rig v02 (spec 1.3): rebuild at low and high of every fit-critical
parameter (DESIGN_PLAN §4), export into 01_CAD/sweep_<tag>/, and run every predicate
of check_od_t01_rig_v02.py on each export (the motion checks U-03b and REQ-04 included).
Nominal is the delivered 02_STEP_STL export, checked by the same script.

Usage (repo root): uv run tools/run.py python <ws>/01_CAD/sweep_od_t01_rig.py [--tag v02] [--jobs 4]
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = 0.1 / math.sqrt(2.0)          # a 0.10 radial offset of the screw holes, split over x and z

SWEEP = {  # parameter: (low overrides, high overrides)
    "screw_d": ({"screw_d": 3.3}, {"screw_d": 3.5}),
    "cbore_d": ({"cbore_d": 6.4}, {"cbore_d": 6.6}),
    "cbore_floor_y": ({"cbore_floor_y": 139.9}, {"cbore_floor_y": 140.1}),
    "screw_xz_radial": ({"screw_x": 44.0 - D, "screw_z": 44.0 - D}, {"screw_x": 44.0 + D, "screw_z": 44.0 + D}),
    "window_r": ({"window_r": 29.9}, {"window_r": 30.1}),
    "theta_roof": ({"theta_roof": 45.05}, {"theta_roof": 45.14}),
    "bench_d": ({"bench_d": 4.4}, {"bench_d": 4.6}),
    "plate_y0": ({"plate_y0": 134.9}, {"plate_y0": 135.1}),
    "wall_x_in": ({"wall_x_in": 74.9}, {"wall_x_in": 75.1}),
    "depth_z1": ({"depth_z1": 59.9}, {"depth_z1": 60.1}),
}


def one(tag, param, side, over):
    out = HERE / f"sweep_{tag}"
    name = f"od_t01_rig_C1_{param}_{side}"
    sets = [f"{k}={v!r}" for k, v in over.items()]
    b = subprocess.run([sys.executable, str(HERE / "build_od_t01_rig_v02.py"), "--out-dir", str(out), "--tag", tag,
                        "--name", name, "--no-assembly", "--meta-dir", str(out), "--set", *sets], capture_output=True, text=True)
    if b.returncode != 0:
        return {"parameter": param, "side": side, "over": over, "built": False, "error": b.stderr[-2000:]}
    step = out / f"{name}_{tag}.step"
    gates = out / f"{name}_{tag}.gates.json"
    # every predicate of check_od_t01_rig_v02.py, split into groups run side by side, rows merged
    sys.path.insert(0, str(HERE))
    import check_od_t01_rig_v02 as chk
    names = [f.__name__ for f in chk.PREDICATES]
    groups = [["u03b_offer_up"], ["req04_travel"], [n for n in names if n not in ("u03b_offer_up", "req04_travel")]]
    base = [sys.executable, str(HERE / "check_od_t01_rig_v02.py"), "--step", str(step), "--stl",
            str(out / f"{name}_{tag}.stl"), "--params", str(out / f"{name}_{tag}.params.json"),
            "--mesh-meta", str(out / f"{name}_{tag}.mesh.json")]
    parts = [out / f"{name}_{tag}.gates.g{i}.json" for i in range(len(groups))]
    with ThreadPoolExecutor(len(groups)) as pool:
        runs = list(pool.map(lambda gi: subprocess.run(base + ["--out", str(parts[gi]), "--only", *groups[gi]],
                                                       capture_output=True, text=True), range(len(groups))))
    bad = [r for r in runs if r.returncode != 0]
    if bad:
        return {"parameter": param, "side": side, "over": over, "built": True, "error": bad[0].stderr[-2000:]}
    rows, timing, seat = [], {}, None
    for i, part in enumerate(parts):
        g = json.loads(part.read_text())
        seat = g["seat_y"]
        timing.update(g["timing_s"])
        rows += [r for r in g["rows"] if i == len(groups) - 1 or r["status"] != "N/A" and r["gate"] != "REQ-08"]
        part.unlink()
    merged = {"step": str(step), "seat_y": seat, "rows": rows, "summary": chk.summarise(rows), "timing_s": timing,
              "predicates": names}
    gates.write_text(json.dumps(merged, indent=1, default=str))
    return {"parameter": param, "side": side, "over": over, "built": True, "gates": gates.name}


def summarise(tag):
    """Per run: the status per gate and the worst signed margin of each gate (from the
    rows check_od_t01_rig_v02.py wrote); written to sweep_<tag>/sweep_summary.json."""
    folder = HERE / f"sweep_{tag}"
    index = json.loads((folder / "sweep_index.json").read_text())
    out = []
    for r in index:
        entry = {k: r[k] for k in ("parameter", "side", "over", "built")}
        if "gates" not in r:
            entry["error"] = r.get("error", "")[-500:]
            out.append(entry)
            continue
        g = json.loads((folder / r["gates"]).read_text())
        entry["summary"] = g["summary"]
        worst = {}
        for row in g["rows"]:
            m = row.get("margin")
            if m is None:
                continue
            if row["gate"] not in worst or m < worst[row["gate"]]["margin"]:
                worst[row["gate"]] = {"margin": m, "measured": row["measured"], "status": row["status"],
                                      "note": row.get("note", "")}
        entry["worst"] = worst
        entry["not_pass"] = {k: v for k, v in g["summary"].items()
                             if v not in ("PASS", "PASS_ASSUMED", "N/A") and k != "REQ-08"}
        out.append(entry)
    (folder / "sweep_summary.json").write_text(json.dumps(out, indent=1))
    for e in out:
        print(e["parameter"], e["side"], e.get("over"), "built", e["built"], "not pass:", e.get("not_pass"),
              e.get("error", ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="v02")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--summarise", action="store_true")
    a = ap.parse_args()
    if a.summarise:
        summarise(a.tag)
        return
    jobs = [(a.tag, p, side, over) for p, (lo, hi) in SWEEP.items() if not a.only or p in a.only
            for side, over in (("low", lo), ("high", hi))]
    with ThreadPoolExecutor(a.jobs) as pool:
        results = list(pool.map(lambda j: one(*j), jobs))
    idx = HERE / f"sweep_{a.tag}" / "sweep_index.json"      # merged across chunked calls (--only)
    prev = json.loads(idx.read_text()) if idx.exists() else []
    done = {(r["parameter"], r["side"]) for r in results}
    merged = [r for r in prev if (r["parameter"], r["side"]) not in done] + results
    order = {p: i for i, p in enumerate(SWEEP)}
    merged.sort(key=lambda r: (order.get(r["parameter"], 99), r["side"] != "low"))
    idx.write_text(json.dumps(merged, indent=1))
    for r in results:
        print(r["parameter"], r["side"], r.get("gates") or r.get("error", "")[-300:])


if __name__ == "__main__":
    main()
