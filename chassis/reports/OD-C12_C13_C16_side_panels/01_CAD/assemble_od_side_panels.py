"""Check assembly of od_side_panels_v01 (F31-F34): the delivered references by their section 2 joints,
the two panels at identity and six brackets at the section 2 poses, each read back from its
exported part STEP, written as one AP242 assembly with one labelled occurrence per solid.

Run: assemble_od_side_panels.py
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Compound  # noqa: E402

from params_od_side_panels import P  # noqa: E402
from placements_od_side_panels import OUT, new_parts, references  # noqa: E402
from tools.core import read_step, write_step  # noqa: E402

ASM = OUT / "od_side_assembly_C1_v01.step"


def assemble(p=P):
    children = []
    for label, solids in references().items():
        for i, s in enumerate(solids):
            s = copy.deepcopy(s)       # its own TShape, so the writer keeps one label per occurrence
            s.label = label if len(solids) == 1 else f"{label}-{i + 1}"
            children.append(s)
    for label, s in new_parts(p).items():
        s = copy.deepcopy(s)
        s.label = label
        children.append(s)
    return Compound(children=children, label="od_side_assembly")


if __name__ == "__main__":
    asm = assemble()
    w = write_step(asm, ASM, timestamp=P.step_timestamp)
    back = read_step(ASM)
    facts = {"file": ASM.name, "sha256": w.sha256, "children": [c.label for c in asm.children],
             "solids_written": len(asm.solids()), "solids_read_back": len(back.solids())}
    (Path(__file__).resolve().parent / "results_v01" / "export_od_side_assembly_C1_v01.json").write_text(
        json.dumps(facts, indent=1))
    print(json.dumps(facts))
