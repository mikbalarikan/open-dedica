# DECISIONS — OD-S03_steam-knob

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.


- 2026-09-25 | Ikbal (owner, session message) | REGIME | baseline-skill, material_class plastic: p95 <= 0.30 / max <= 0.80 mm (baseline/skills/stl2step-build123d/SKILL.md:87). User message: "p95 plastik parça toleransı kullan". Declared before any gate numbers exist. | session message; intake/regime.json
- 2026-09-25 | Ikbal (owner, session message) | MEASUREMENTS | No calipers supplied; proceed scan-only. Limitations carried to verdict: "Tier-1 not run" and "absolute scale not caliper-verified", re-run trigger: any caliper reading. The 5 photos are catalogue/product photos without a scale reference: feature identification and plausibility only. | session message; input/INPUT_HASHES.json
- 2026-09-25 | orchestrator (agent) | OTHER | scan_resolution recorded as `full` by agent inference, not stated by the user: 363,988 faces, one body, mean edge 0.153 mm, the same export profile as OD-H22 (mean edge 0.154 mm) whose full-res status the same owner confirmed (evals/real-runs/OD-H22.md). Re-run trigger if wrong: owner says this is a decimated copy. | input/INPUT_HASHES.json#scan_resolution
- 2026-09-25 | builder (agent) | OTHER | Datum primary (crown face) first fit with the default 10 deg normal cone read rms 0.0216 > plane noise 0.0187 (lever -Y flank) and align.py returned STOP; the excess comes from the onset of the crown edge round (ring r 10-12 alone rms 0.032; crown r<10 alone 0.0132; seed sweep 0-5 stable, so not a tie). Re-ran with primary cone_deg 3 (flat field only): rms 0.0146 < 0.0187, status OK. Noise reference kept independent (not self-referential). | intake/alignment_attempt1_STOP.json; intake/alignment.json; intake/INTAKE_CARD.md §6
- 2026-09-25 | builder (agent) | OTHER | Clock: align.py fourier_mass sums vertex counts (align.py:247-259) and was biased 3.8 deg by scan vertex density/holes (lever flank-plane bisector disagreed). Ran align.py unchanged except the fourier_mass branch, through a scratch wrapper that area-weights face centres (intake/workaround/align_areaw.py; repo not modified). Result: flank planes -0.64/+1.03 deg about +X. | intake/workaround/align_areaw.py; intake/alignment.json#clock.detail
- 2026-09-25 | orchestrator (agent) | OTHER | it1 verdict REVISE (qa/gate.json errors [], allowed): non-watertight tessellation (3/12 non-manifold edges where the 180° stem rib foot touches the inner-groove torus along a line). Routed `geometry`; it2 changes only that contact (plus nothing else unless verify-named). Loop 1 of 3 used. | _it1_SUPERSEDED/qa/VERDICT.md
- 2026-09-25 | Ikbal (owner, decision card) | ACCEPT-BAND | Accept and deliver: accepts scan_to_cad:masked, cad_to_scan_observable and zone:Z4 crown cap wall lever:scan_to_cad misses, gate f70ad05cf7ed (created 2026-09-25T15:11:43+00:00); scan->CAD p95 passes, max from a cap-wall scan artefact, CAD->scan observable from unreached assumed floors. | decisions/accept_band.md
