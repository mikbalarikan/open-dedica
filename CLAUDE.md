# Open Dedica — notes for Claude Code sessions

- This is an open-source hardware repository (CC BY 4.0, data class PUBLIC).
  Read `README.md`, `CONTRIBUTING.md`, and `docs/PART_NUMBERING.md` first.
- Custom-designed parts (`cad = DESIGN` in `docs/bom.csv`: the group head housing
  OD-G01 and the chassis OD-C01…C16) are designed with the OGUZ Atölye pipeline in
  the sibling repository `mikbalarikan/oguz-atolye` (`AGENTS.md`, `atolye/PLAYBOOK.md`).
  Reference geometry for them is the scan-rebuilt STEP library in `step/` with its
  reports in `step/reports/`; calipers beat scans on every interface, and every
  scan-derived value is an assumption until the Usta confirms it.
- Design job records live under `chassis/reports/<part>/` (first: OD-G01), each
  with a README that says how to resume it. Job state is written only through
  `oguz-atolye/tools/jobstate.py`, never by hand.
- Deliverables: STEP (mm, one named solid per part), STL, and the parametric
  build script; update `docs/bom.csv` and regenerate `docs/BOM.md` and the progress
  board (`python tools/build_bom.py && python tools/build_progress.py`) in the same PR.
- Talk to the Usta (the repository owner) in the language of the latest message;
  repo documents in English.
