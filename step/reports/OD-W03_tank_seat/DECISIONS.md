# DECISIONS — OD-W03

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.

- 2026-09-28 | Ikbal (owner, session message) | REGIME | baseline-skill, material_class plastic: p95 <= 0.30 / max <= 0.80 mm (baseline/skills/stl2step-build123d/SKILL.md:87). Owner wrote "p95 plastik parça toleransı kullan"; translucent moulded plastic part. Declared before any gate numbers exist. | session message; intake/regime.json
- 2026-09-28 | Ikbal (owner, decision card) | MEASUREMENTS | No calipers; proceed scan-only ("Sadece tarama ile ilerle"). Limitations carried to verdict: "Tier-1 not run" and "absolute scale not caliper-verified", re-run trigger: any caliper reading. The single catalogue photo has no scale reference: feature identification / plausibility only. | session decision card
- 2026-09-28 | Ikbal (owner, decision card) | OTHER | scan_resolution confirmed full ("Evet, orijinal tam çözünürlük"): 400,657 faces, mean edge 0.184 mm, one body. | input/INPUT_HASHES.json
- 2026-09-28 | Ikbal (owner, decision card) | OTHER | Interior design intent: hollow moulded shell ("İçi boş kabuk"). Cups and middle boss open from below, assumed wall thickness 1.2 mm, barb bore opens into its cup. Every interior dimension is `assumed` and declared (the underside and all interiors are unscanned). | session decision card; intake/coverage.json
- 2026-09-28 | orchestrator (agent) | OTHER | Datum: secondary (cup A/B outer wall, z 1.2-3.6) median circle rms 0.0815 vs the independent barb-shank circle noise 0.0708 (z=16) -> align.py STOP by 0.011 mm. Barb shanks as origin were worse (0.089); higher cup bands carry +/-0.15 mm scan ripple. Took the self-referential noise path (intake/noise_cups.json, OD-H22 D1 precedent: no tie margin); centre scatter per cup <= 0.007 mm over 3 stations of ~3,300 faces. Primary plane noise is also measured on the primary itself (flange top). Added align.py `feature_line` clock and `combine: midpoint` origin (fourier_mass n=2 was 0.7 deg off the cup line; pooled median picked one cup's centre). | intake/alignment.json; intake/noise_cups.json; intake/datum_spec.json
- 2026-09-28 | Ikbal (owner, decision card) | ACCEPT-BAND | Accept and deliver now: accepts scan_to_cad and cad_to_scan_observable band misses, gate 2fe9569f1fa0 (created 2026-09-28T08:17:23+00:00); REVISE for the cup B upper wall offered and declined. | decisions/accept_band.md
