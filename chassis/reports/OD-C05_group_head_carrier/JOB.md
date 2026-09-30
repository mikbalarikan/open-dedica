---
schema: oguz-job-v1
job_id: "20260930-od-c05-group-head-carrier"
code: ODC05
milestone: M1
title: "Open Dedica OD-C05 printed group head carrier"
lane: CAD
state: J3_BUILD
blocked_on: null
next_action: "spec 2.0 (A-02 vertical axis, concept C4), then designer package WP-05: plan v02 and build od_c05_carrier_v02"
data_class: PUBLIC
size: S
process: [FDM]
gate_sections: [U, D, E]
spec: "00_Spec/DESIGN_SPEC.md"
spec_version: "1.2"
workspace: "${OGUZ_JOBS}/20260930-od-c05-group-head-carrier"
delivery: "${OGUZ_DELIVERY}/20260930-od-c05-group-head-carrier"
artifacts: "${OGUZ_ARTIFACTS}/20260930-od-c05-group-head-carrier"
repo_commit: d7ea010502a30dd025c5123992847da1b15f3ee3
active_target: od_c05_carrier_v01
revision: A
open_assumptions: [A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09, A-10, A-11, A-12, A-13, A-14]
attempts: {build: 0, export: 0, tool: 0}
caps: {build: 2, export: 2, tool: 2, fix_cycles: 3}
reviews:
  - {id: RV01, target: od_c05_carrier_v01, verdict: REVISE, blockers: 1, date: "2026-09-30"}
usta_gates:
  - {gate: spec_ratified, outcome: "1.0", date: "2026-09-30"}
  - {gate: concept_picked, outcome: C1, date: "2026-09-30"}
  - {gate: spec_ratified, outcome: "1.1", date: "2026-09-30"}
  - {gate: exception_signed, outcome: D-03a, date: "2026-09-30"}
  - {gate: spec_ratified, outcome: "1.2", date: "2026-09-30"}
  - {gate: revise_decision, outcome: another_round, date: "2026-09-30"}
deliverables: [STEP, STL, "3MF"]
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

## Close summary

