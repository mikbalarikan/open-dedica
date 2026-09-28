# DECISIONS — OD-E01_Power-PCB

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.

- 2026-09-28 | Ikbal (owner brief) | REGIME | baseline-skill, material class plastic: p95 <= 0.30 / max <= 0.80 mm ("p95 plastik parça toleransı kullan") | decisions/owner_brief.md
- 2026-09-28 | Ikbal (owner brief) -> agent | MEASUREMENTS | scan-only: no caliper sheet supplied, owner asked for a finished zip delivery; limitations "Tier-1 not run" and "absolute scale not caliper-verified" carried to the verdict | decisions/owner_brief.md
- 2026-09-28 | agent (delegated by owner brief) | PART-CLASS | populated PCB assembly (board + components) modelled as ONE fused envelope solid of analytic primitives (board plate, component boxes/cylinders, extruded heatsink profile); no multi-body assembly, no electrical detail (pads, traces, silkscreen, solder) | decisions/owner_brief.md
- 2026-09-28 | agent | OTHER | scan_resolution declared "full": the supplied STL (398,079 faces, 19.9 MB) is the only and original file, not a *_decimated copy | input/INPUT_HASHES.json
- 2026-09-28 | agent | OTHER | datum try 1 STOP (board-top rms 0.0342 > film-cap noise 0.0275) caused by board bow/twist (~-0.2..+0.1 mm) and copper-trace relief; re-ran align with the noise floor measured on the board top itself (self-referential, OD-H22 precedent); try 1 kept in intake/_datum_try1_STOP/ | intake/INTAKE_CARD.md
- 2026-09-28 | agent (orchestrator) | OTHER | it1 verdict REVISE (independent verify, qa gate in _it1_SUPERSEDED/qa/gate.json): fixable misses routed to measure (C5 underside, J3 cavity floor, TO-220 tab hole position, K2 bump, clip lower hook); supersede --route measure; the run-local scripts measure_pcb.py, make_params.py, model.py and MODELING_PLAN.md copied forward as the diffable base | _it1_SUPERSEDED/qa/review.json
- 2026-09-28 | Ikbal (owner) | ACCEPT-BAND | accept scan_to_cad:masked and cad_to_scan_observable misses of the it2 BAND_NOT_MET gate 948b8a16472b for delivery | decisions/accept_band_it2.md
