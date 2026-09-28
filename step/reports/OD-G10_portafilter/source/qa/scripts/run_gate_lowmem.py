#!/usr/bin/env python3
"""QA wrapper: run stl-re-verify deviation_gate.py unchanged, except that the observability ray
test is chunked in 200 rays instead of the hard-coded 2000 (observability.py:237 `chunk`, not
exposed on deviation_gate's CLI). `chunk` only bounds memory; the per-point result is identical.
Reason: the default run was OOM-killed on this 15 GB box with the 0.005 mm STEP tessellation
(~459k triangles) -- see qa/VERDICT.md / review.json script-defect note."""
import functools
import sys

S = "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts"
sys.path.insert(0, S)
import observability  # noqa: E402
observability.observable_split = functools.partial(observability.observable_split, chunk=200)
import deviation_gate  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(deviation_gate.main(sys.argv[1:]))
