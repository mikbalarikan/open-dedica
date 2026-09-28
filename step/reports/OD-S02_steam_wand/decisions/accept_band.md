# ACCEPT-BAND — OD-S02_steam-rod (it3)

Owner: Ikbal. Decision (question card, 2026-09-28): "Kabul et, teslim et" — accept the band misses and deliver.

Gate accepted: `qa/gate.json` sha256 prefix **34a11505e84d**, created 2026-09-28T09:57:42+00:00
(re-assembled as BAND_NOT_MET from the loop-3 REVISE gate 69b36b1ef4d5 on the owner's HALT resolution; numbers unchanged).

Band misses accepted (names as in `gate.json#band_fails`):
- `cad_to_scan_observable` — CAD surface with no scan behind it (unscanned window floors, bore interior, scan holes).
- `zone:Z4 bushing + tip:scan_to_cad` — marginal (p95 at the band edge) from the unmodelled bushing-top collar and underside rim (limitation L6).
- `zone:Z4 bushing + tip:cad_to_scan` — same cause as the first.

Why: a 4th loop was not wanted; the first and third misses cannot be fixed by geometry without new data; the
remaining geometric cause is declared as L6 with its re-run trigger.
