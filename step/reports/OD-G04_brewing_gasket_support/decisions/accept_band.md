# ACCEPT-BAND — OD-G04 brewing gasket support

- Date: 2026-09-25
- Who: Ikbal (owner), session decision card, answer "Kabul et, teslim et"
- Gate: `qa/gate.json` sha256 prefix 6b2ca357f5c3 (created 2026-09-25T14:13:14+00:00), verdict BAND_NOT_MET,
  regime baseline-skill plastic (p95 ≤ 0.30 / max ≤ 0.80 mm).
- Accepted band misses (gate.json#band_fails):
  - `scan_to_cad` (p95 0.376 / max 0.832): verifier attributes the p95 miss to its ICP pairing faces across
    2.3–2.6 mm walls (builder-frame p95 0.218; diagnostic 1 mm-correspondence ICP p95 0.194, qa/diagnostic/),
    and the max miss to 3 isolated points of 245,660.
  - `cad_to_scan_observable` (p95 2.325 / max 4.592): driven by regions the scanner did not reach (front
    cavity/plate underside, hub interior, outer-wall gap); 65 % of over-band CAD points lie next to a scan-hole edge.
- Why accepted: a rebuild without new data cannot fix either miss (options shown: accept / REVISE / calipers / HALT).
