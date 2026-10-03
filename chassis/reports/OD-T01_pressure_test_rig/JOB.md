---
schema: oguz-job-v1
job_id: "20261002-od-t01-pressure-test-rig"
code: ODT01
milestone: M1
title: "Open Dedica OD-T01 group head bench pressure-test rig"
lane: CAD
state: J4_REVIEW
blocked_on: null
next_action: "J4: await RV02 (WP-06) on v02; APPROVED -> replace v01 in the open-dedica branch (STEP, STL, 3MF, scripts, test procedure)"
data_class: PUBLIC
size: S
process: [FDM]
gate_sections: [U, D, J]
spec: "00_Spec/DESIGN_SPEC.md"
spec_version: "1.3"
workspace: "${OGUZ_JOBS}/20261002-od-t01-pressure-test-rig"
delivery: "${OGUZ_DELIVERY}/20261002-od-t01-pressure-test-rig"
artifacts: "${OGUZ_ARTIFACTS}/20261002-od-t01-pressure-test-rig"
repo_commit: "10929db1408d89144bd4af9cad971440427933d0"
active_target: od_t01_rig_v02
revision: A
open_assumptions: [A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09, A-10, A-11, A-12]
attempts: {build: 2, export: 0, tool: 0}
caps: {build: 2, export: 2, tool: 2, fix_cycles: 3}
reviews:
  - {id: RV01, target: od_t01_rig_v01, verdict: APPROVED_ASSUMPTION_CONDITIONAL, blockers: 0, date: "2026-10-03"}
usta_gates:
  - {gate: spec_ratified, outcome: "1.0", date: "2026-10-02"}
  - {gate: concept_picked, outcome: C1, date: "2026-10-02"}
  - {gate: spec_ratified, outcome: "1.1", date: "2026-10-02"}
  - {gate: spec_ratified, outcome: "1.2", date: "2026-10-03"}
  - {gate: question_answered, outcome: v02_25mm_plate, date: "2026-10-03"}
  - {gate: spec_ratified, outcome: "1.3", date: "2026-10-03"}
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

## Close summary

