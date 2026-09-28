# DECISIONS — OD-G10_porta_filter_holder

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.


- 2026-09-28 | Ikbal (owner, chat) | REGIME | baseline-skill, class plastic (p95 <= 0.30 / max <= 0.80 mm), "p95 plastik parça toleransı kullan" | decisions/owner_request_2026-09-28.md
- 2026-09-28 | Ikbal (owner, chat) | MEASUREMENTS | no calipers supplied; proceed scan-only on the owner's end-to-end request. Limitations: Tier-1 not run; absolute scale not caliper-verified (re-run trigger: filled MEASUREMENTS.md) | decisions/owner_request_2026-09-28.md
- 2026-09-28 | agent (delegated) | OTHER | scan_resolution declared full: owner upload as exported, 400,123 faces (non-round), 20.0 MB; re-run trigger: owner says it was decimated | decisions/owner_request_2026-09-28.md
- 2026-09-28 | orchestrator (agent) | HALT | verify (fresh agent) returned HALT, gate a415ac1263b6: own ICP did not converge (60 and 500 iterations), gate label INVALID, so no official grade. Cause per verify: tier2_icp.py pairs unscanned CAD faces (~13 % of kept pairs) with the opposite wall; it has no CAD-side mask and no normal-direction test. Not a geometry REVISE. Options for the owner: (a) fix tier2_icp.py in the skill (CAD-side coverage masks + facing-normal rejection), then re-verify in a fresh agent; (b) owner-recorded override to deliver on datum-frame numbers (inspection only); (c) supply more scan coverage / calipers. No deliver/ until decided. | qa/gate.json, qa/review.json, qa/icp_diagnose.json
- 2026-09-28 | Ikbal (owner, chat) | OTHER | owner override: deliver the HALT result as-is ("bu haliyle deliver et"), gate a415ac1263b6; verdict stays HALT, no official grade, inspection-only numbers; delivery scripts run via deliver/src/override_run.py (HALT added to the deliverable list for this run only) | decisions/owner_override_2026-09-28.md
