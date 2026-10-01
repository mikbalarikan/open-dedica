"""D7 robustness sweep for od_c15_foot (plan §4): every fit-critical parameter at its low and
high with the others nominal, then pocket_af x nut s jointly (L-09). Each run builds the foot
and the check assembly into sweep_v##/<run>/ (never 02_STEP_STL) and runs the same predicates
(check_od_c15_foot.py). Writes sweep_v##/summary.json.

Usage: python sweep_od_c15_foot.py --plate <OD-C01.step> --tag v01
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

RUNS = [  # (name, foot overrides, nut s)
    ("body_d_low", {"body_d": 17.9}, 5.5), ("body_d_high", {"body_d": 18.1}, 5.5),
    ("height_low", {"height": 9.9}, 5.5), ("height_high", {"height": 10.1}, 5.5),
    ("lid_t_low", {"lid_t": 2.4}, 5.5), ("lid_t_high", {"lid_t": 2.6}, 5.5),
    ("lid_hole_d_low", {"lid_hole_d": 3.3}, 5.5), ("lid_hole_d_high", {"lid_hole_d": 3.5}, 5.5),
    ("af560_s532", {"pocket_af": 5.60}, 5.32), ("af560_s550", {"pocket_af": 5.60}, 5.50),
    ("af565_s532", {"pocket_af": 5.65}, 5.32), ("af565_s550", {"pocket_af": 5.65}, 5.50),
]


def run(cmd):
    p = subprocess.run([sys.executable, *cmd], capture_output=True, text=True)
    return p.returncode, p.stdout[-4000:] + p.stderr[-4000:]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--plate", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args(argv)
    root = HERE / f"sweep_{a.tag}"
    summary_path = root / "summary.json"
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    for name, over, nut_s in RUNS:
        if a.only and name not in a.only:
            continue
        d = root / name
        d.mkdir(parents=True, exist_ok=True)
        sets = [x for k, v in over.items() for x in ("--set", f"{k}={v}")]
        rc_b, log_b = run([str(HERE / "build_od_c15_foot.py"), "--out-dir", str(d), "--cad-dir", str(d),
                           "--tag", a.tag, "--no-stl", *sets])
        foot = d / f"od_c15_foot_C1_{a.tag}.step"
        asm = d / f"od_c15_assembly_C1_{a.tag}.step"
        rc_a, log_a = run([str(HERE / "build_check_assembly.py"), "--plate", a.plate, "--foot", str(foot),
                           "--out", str(asm), "--nut-s", str(nut_s), "--log-dir", str(d)])
        res = d / "check_results.json"
        rc_c, log_c = run([str(HERE / "check_od_c15_foot.py"), "--foot", str(foot), "--assembly", str(asm),
                           "--params", str(d / f"od_c15_foot_C1_{a.tag}.params.json"), "--out", str(res),
                           "--nut-s", str(nut_s)])
        entry = {"overrides": over, "nut_s": nut_s, "rc": [rc_b, rc_a, rc_c]}
        if rc_c == 0 and res.exists():
            rows = json.loads(res.read_text())["rows"]
            gated = [r for r in rows if r["status"] in ("PASS", "PASS_ASSUMED", "FAIL", "INCONCLUSIVE")]
            entry["one_solid"] = all(r["status"] in ("PASS", "PASS_ASSUMED") for r in rows
                                     if r["gate"] == "exactly_one_solid")
            entry["fails"] = [(r["gate"], r["item"], r["measured"], r["status"], r["reason"]) for r in gated
                              if r["status"] in ("FAIL", "INCONCLUSIVE")]
            worst = {}
            for r in gated:
                if r["margin"] is not None and (r["gate"] not in worst or r["margin"] < worst[r["gate"]][0]):
                    worst[r["gate"]] = (r["margin"], r["item"], r["measured"])
            entry["worst"] = worst
        else:
            entry["log"] = (log_b + log_a + log_c)[-3000:]
        summary[name] = entry
        summary_path.write_text(json.dumps(summary, indent=1, default=str))
        print(name, entry["rc"], len(entry.get("fails", [])) if "fails" in entry else "no results", flush=True)


if __name__ == "__main__":
    sys.exit(main())
