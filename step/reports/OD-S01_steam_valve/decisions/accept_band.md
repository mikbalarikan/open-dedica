# ACCEPT-BAND: OD-S01_steam-valve, iteration 2

- Who / when: Ikbal (owner), question card in the session, 2026-09-28, answer "Accept and deliver (ACCEPT-BAND)".
- Gate: `qa/gate.json` sha256 prefix **19f6d742b0ae**, created 2026-09-28T08:12:03+00:00, verdict BAND_NOT_MET,
  regime baseline-skill plastic (p95 <= 0.30 / max <= 0.80 mm).
- Accepted band fails (as named in `gate.json#band_fails`): `scan_to_cad:masked`, `cad_to_scan_observable`,
  `zone:Z1_spindle:scan_to_cad`, `zone:Z2_cap_cam_ring:scan_to_cad`, `zone:Z3_top_clip_port:scan_to_cad`,
  `zone:Z4_side_ports:scan_to_cad`, `zone:Z6_microswitch:scan_to_cad`.
- What the owner was shown before deciding: scan->CAD p95 0.449 / max 1.94 (it1 0.520 / 2.27), observable CAD->scan
  p95 0.761 / max 2.89; only the barb zone passes; misses in the cam ring, top clip port, microswitch, spindle max;
  the 1.94 max is an it2 regression at the port junction box by the neck; QA probe: even with every >0.8 mm cluster
  fixed, p95 ~0.34 / max ~1.09, so a third loop would not reach the band. Options offered: accept, loop 3, calipers, HALT.
