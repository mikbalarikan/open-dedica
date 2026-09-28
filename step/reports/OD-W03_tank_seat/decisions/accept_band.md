# ACCEPT-BAND — OD-W03 water tank valve

Owner: Ikbal (decision card, 2026-09-28): "Şimdi kabul et, teslim et".

Gate: `qa/gate.json` sha256 prefix **2fe9569f1fa0** (created 2026-09-28T08:17:23+00:00), verdict BAND_NOT_MET,
regime baseline-skill plastic (p95 <= 0.30 / max <= 0.80 mm).

Accepted band misses (gate.json#band_fails):
- scan_to_cad: masked p95 0.307 / max 0.785 (unmasked p95 0.320 / max 1.113) vs 0.30 / 0.80 — distributed:
  skirt lower edge (draft vs scan curl undecidable), cup B upper wall ~0.11 short, tab/lug junction, wall ripple;
  max from the barb A bore-mouth bridging film.
- cad_to_scan_observable: p95 1.512 / max 3.063 vs 0.30 / 0.80 — the owner-chosen hollow shell interior and
  underside were never scanned; no rebuild can pass it without new data.

Presented options: REVISE (cup B upper wall, likely still BAND_NOT_MET), accept now, HALT. Owner chose accept now.
