---
schema: oguz-job-v1
job_id: "20261002-od-c12-c13-c16-side-panels"
code: ODC12
milestone: M1
title: "Open Dedica OD-C12/OD-C13 printed side panels and OD-C16 corner brackets"
lane: CAD
state: J5_DELIVER
blocked_on: null
next_action: "The Usta merges open-dedica PR #51; then J6 close with PHYSICAL_OUTCOME pending the first prints"
data_class: PUBLIC
size: M
process: [FDM]
gate_sections: [U, D, J, E]
spec: "00_Spec/DESIGN_SPEC.md"
spec_version: "1.2"
workspace: "${OGUZ_JOBS}/20261002-od-c12-c13-c16-side-panels"
delivery: "${OGUZ_DELIVERY}/20261002-od-c12-c13-c16-side-panels"
artifacts: "${OGUZ_ARTIFACTS}/20261002-od-c12-c13-c16-side-panels"
repo_commit: "10929db1408d89144bd4af9cad971440427933d0"
active_target: od_side_panels_v01
revision: A
open_assumptions: [A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09, A-10, A-11, A-12, A-13, A-14, A-15]
attempts: {build: 1, export: 0, tool: 0}
caps: {build: 2, export: 2, tool: 2, fix_cycles: 3}
reviews:
  - {id: RV01, target: od_side_panels_v01, verdict: APPROVED_ASSUMPTION_CONDITIONAL, blockers: 0, date: "2026-10-03"}
usta_gates:
  - {gate: spec_ratified, outcome: "1.0", date: "2026-10-02"}
  - {gate: concept_picked, outcome: C1, date: "2026-10-02"}
  - {gate: spec_ratified, outcome: "1.1", date: "2026-10-02"}
  - {gate: spec_ratified, outcome: "1.2", date: "2026-10-03"}
deliverables: [STEP, STL, "3MF", scripts, REPORT]
physical_outcome: n/a
client_source_delete_after: null
---

<!--
JOB.md is the job's state and its resume point (PLAYBOOK §5). Only
tools/jobstate.py writes it (D-032), at the end of every orchestrator turn. Keep the
whole file under 5,000 tokens so it survives compaction whole: no narrative, no
logs, no measurements (those live in REPORT, VERDICT, and EVENTS.jsonl).

The SessionStart hook prints job_id, code, lane, data_class, state, blocked_on,
active_target, attempts against caps, next_action, open_assumptions, and the notes
section below.

Counters: build counts the designer packages sent for the active target (in the RE
lane, the re-drafter packages for the active feature), a RETURNED submission
included; export and tool count retries in the current step. Counters reset only
when a new target or RE feature starts, or when the Usta orders another round.
Reaching a cap is a halt (PLAYBOOK rule 9). fix_cycles goes into the designer's brief
and bounds its own fix-and-re-measure loop.
-->

## Notes for a resuming session

Cloud container job (2026-10-02): the record is mirrored to open-dedica/chassis/reports/ (OD-C14_cord_grommet, OD-C12_C13_C16_side_panels) after every stage; recreate the workspace from there (its README). Env: source an env file setting the four OGUZ_* variables before every tools call. Specs rest on the Usta's answer of 2026-10-02 22:58 UTC (printed panels, PLA for now, cord 7 mm) and the standing instruction; explicit confirmation of §5/§6 pending. Shared files (bom.csv, BOM.md, progress board, chassis/README.md, OD-000, OD-C01 inserts, HANDOVER) belong to the OD-G01 thread; notes in the project folder chassis-C12-C16/integration_notes.md. The container restarted twice; a lost package is re-run as the same attempt with a note event.

## Close summary

