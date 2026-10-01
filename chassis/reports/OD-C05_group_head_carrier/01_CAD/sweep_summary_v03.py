"""Summarise the v03 sweep: per run, the gates not passing and the worst margin per gate
family; writes 01_CAD/sweep_v03/summary_v03.json and SHA256SUMS_v03.txt."""
import hashlib
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
OUT = WS / "01_CAD/sweep_v03"


def family(gid):
    return re.split(r" ", gid)[0]


runs = {}
for f in sorted(OUT.glob("check_*.json")):
    tag = f.stem[len("check_"):]
    d = json.loads(f.read_text())
    worst, bad = {}, []
    for r in d["gates"]:
        if r["status"] not in ("PASS", "PASS_ASSUMED", "N/A") and r["gate"] != "REQ-09":
            bad.append((r["gate"], r["status"], r.get("measured")))
        m = r.get("margin")
        if isinstance(m, (int, float)):
            fam = family(r["gate"])
            if fam not in worst or m < worst[fam][0]:
                worst[fam] = (m, r["gate"], r.get("measured"), r["status"])
    build = json.loads((OUT / f"build_{tag}.json").read_text()) if (OUT / f"build_{tag}.json").exists() else {}
    solids = next((r.get("measured") for r in d["gates"] if r["gate"] == "exactly_one_solid"), None)
    runs[tag] = {"one_solid": solids == 1, "not_passing": bad, "worst": worst,
                 "params": build.get("params")}
(OUT / "summary_v03.json").write_text(json.dumps(runs, indent=1, default=str))
lines = []
for p in sorted(OUT.iterdir()):
    if p.name.startswith("SHA256SUMS"):
        continue
    lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}")
(OUT / "SHA256SUMS_v03.txt").write_text("\n".join(lines) + "\n")
for tag, r in runs.items():
    print(tag, r["one_solid"], [b[0] for b in r["not_passing"]])
