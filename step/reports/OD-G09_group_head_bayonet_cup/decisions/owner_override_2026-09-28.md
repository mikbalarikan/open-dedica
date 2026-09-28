# Owner override: deliver the HALT run as-is (Ikbal, chat, 2026-09-28)

Verbatim: "bu haliyle deliver et" ("deliver it as it is"), in reply to the HALT report and its options
(a) fix tier2_icp.py and re-verify, (b) deliver on datum-frame numbers as inspection only, (c) more scan / calipers.

Applies to gate `qa/gate.json` sha256 prefix **a415ac1263b6** (created 2026-09-28T09:25:40+00:00), verdict **HALT**, label INVALID
(own ICP not converged at 60 and 500 iterations).

What this decision does and does not do:
- The verdict stays **HALT**; nothing in qa/ or build/ is edited. There is no official grade.
- The package is named with the HALT verdict and every document says "no official grade,
  inspection-only numbers (datum frame, no converged ICP)".
- stl-re-deliver refuses HALT by design (_common.DELIVERABLE_VERDICTS). The delivery scripts were run
  through `deliver/src/override_run.py`, which adds HALT to that list for this run only; every other
  preflight check (inputs unchanged, hash freeze, headline verdict, regime) still runs.
- Re-run trigger: tier2_icp.py fixed (CAD-side coverage masks + facing-normal rejection) -> re-verify.
