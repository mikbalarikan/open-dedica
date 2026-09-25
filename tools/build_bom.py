"""Render docs/BOM.md from docs/bom.csv (the single source of truth).

Usage:  python tools/build_bom.py          # rewrite docs/BOM.md
        python tools/build_bom.py --check  # exit 1 if BOM.md is stale or the CSV is invalid
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "docs" / "bom.csv"
MD = ROOT / "docs" / "BOM.md"

PART_NO = re.compile(r"^OD-\d{3}$")
TYPES = {"ASM", "OEM", "PRINT", "MFG", "ELEC", "STD", "REF", "FIX"}
CADS = {"SCAN", "CALIPER", "ENVELOPE", "DESIGN", "VENDOR", "—"}
STATUS = {"todo", "proposed", "scanned", "modeled", "validated", "deferred", "ref"}
STATUS_ICON = {"todo": "☐", "proposed": "✎", "scanned": "📷", "modeled": "🧊",
               "validated": "✅", "deferred": "⏸", "ref": "—"}

GROUPS = [
    ("OD-0", "OD-000 — Top assembly"),
    ("OD-1", "OD-100 — Hydraulic core"),
    ("OD-2", "OD-200 — Group head & portafilter"),
    ("OD-3", "OD-300 — Water path"),
    ("OD-4", "OD-400 — Electronics"),
    ("OD-5", "OD-500 — Chassis & body"),
    ("OD-6", "OD-600 — Standard hardware & consumables"),
    ("OD-7", "OD-700 — Steam system (phase 2)"),
    ("OD-8", "OD-800 — OEM parts not used (reference only)"),
    ("OD-9", "OD-900 — Fixtures & test rigs"),
]

HEADER = """# Master BOM — Open Dedica (EC685 platform, 230 V build)

> **Generated from [`bom.csv`](bom.csv) by `tools/build_bom.py` — edit the CSV, not this file.**

Every part that appears in CAD, in a scan folder, or on the shopping list has a project **part number** `OD-NNN`.
See [PART_NUMBERING.md](PART_NUMBERING.md) for the rules. Ref# / OEM code = De'Longhi EC885.M exploded view
(EC680/EC685 interchange on the wet side — verify by PNC before ordering). Prices are 2026 estimates in €.

**Type:** ASM assembly · OEM De'Longhi spare · PRINT our printed part · MFG our non-printed part ·
ELEC off-the-shelf electronics · STD standard hardware · REF reference only · FIX fixture/test rig
**CAD:** SCAN scan + parametric rebuild · CALIPER model from calipers · ENVELOPE simple placeholder solid ·
DESIGN native design · VENDOR vendor STEP
**Status:** ☐ todo · ✎ proposed · 📷 scanned · 🧊 modeled · ✅ validated (check-fixture) · ⏸ deferred
"""


def load():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    seen, errors = set(), []
    for r in rows:
        p = r["part_no"]
        if not PART_NO.match(p):
            errors.append(f"{p}: bad part number")
        if p in seen:
            errors.append(f"{p}: duplicate")
        seen.add(p)
        if r["type"] not in TYPES:
            errors.append(f"{p}: unknown type {r['type']}")
        if r["cad"] not in CADS:
            errors.append(f"{p}: unknown cad {r['cad']}")
        if r["status"] not in STATUS:
            errors.append(f"{p}: unknown status {r['status']}")
    for r in rows:
        if r["parent"] and r["parent"] not in seen:
            errors.append(f"{r['part_no']}: parent {r['parent']} missing")
    return rows, errors


def tree(rows):
    kids = {}
    for r in rows:
        if r["type"] == "ASM" or any(c["parent"] == r["part_no"] for c in rows):
            kids.setdefault(r["parent"], []).append(r)
    out = []

    def walk(parent, depth):
        for r in kids.get(parent, []):
            out.append(f"{'  ' * depth}- `{r['part_no']}` {r['name']}")
            walk(r["part_no"], depth + 1)

    walk("", 0)
    return "\n".join(out)


def render(rows):
    md = [HEADER, "## Assembly tree\n", tree(rows), ""]
    for prefix, title in GROUPS:
        group = [r for r in rows if r["part_no"].startswith(prefix)]
        if not group:
            continue
        md += [f"## {title}\n",
               "| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |",
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in group:
            name = f"**{r['name']}**" if r["type"] == "ASM" else r["name"]
            md.append("| " + " | ".join([
                f"`{r['part_no']}`", r["parent"], r["type"], name, r["ref"], r["oem_code"],
                r["qty"], r["cad"], r["material_spec"], r["source"], r["price_eur"],
                r["issue"], STATUS_ICON[r["status"]],
            ]) + " |")
        md.append("")
    md.append(BUDGET)
    return "\n".join(md)


BUDGET = """## Budget summary (230 V, no donor)

| Block | Estimate |
|---|---|
| OD-100 Hydraulic core | €85–120 |
| OD-200 Group head + portafilter | €45–60 |
| OD-300 Water path | €50 |
| OD-400 Electronics (either path) | €60–100 |
| OD-500/600 Chassis hardware | €50 |
| **Total (all new parts)** | **€290–380** |
| **Donor-machine route** (broken EC685 €50 + wear kit €40 + chassis €50) | **~€140** |

Thesis reference total (2019, all-new UK spares): £295.
"""


def main():
    rows, errors = load()
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    text = render(rows)
    if "--check" in sys.argv:
        if MD.read_text(encoding="utf-8") != text:
            print("docs/BOM.md is stale — run: python tools/build_bom.py")
            sys.exit(1)
        print(f"OK — {len(rows)} parts")
        return
    MD.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {MD.relative_to(ROOT)} — {len(rows)} parts")


if __name__ == "__main__":
    main()
