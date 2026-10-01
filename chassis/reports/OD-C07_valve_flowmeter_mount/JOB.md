---
schema: oguz-job-v1
job_id: "20260930-od-c07-valve-flowmeter-mount"
code: ODC07
milestone: M1
title: "Open Dedica OD-C07 printed valve and flowmeter mount"
lane: CAD
state: J6_CLOSE
blocked_on: null
next_action: "J6: PHYSICAL_OUTCOME.md after the first print; lessons; the OD-G01 thread carries the BOM, README row 5, progress board and OD-000 placement"
data_class: PUBLIC
size: M
process: [FDM]
gate_sections: [U, D, J, E]
spec: "00_Spec/DESIGN_SPEC.md"
spec_version: "1.2"
workspace: "${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount"
delivery: "${OGUZ_DELIVERY}/20260930-od-c07-valve-flowmeter-mount"
artifacts: "${OGUZ_ARTIFACTS}/20260930-od-c07-valve-flowmeter-mount"
repo_commit: "70826895ab7666f9e5aee3f77ce88f099995f3c1"
active_target: od_c07_mount_v01
revision: A
open_assumptions: [A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-18, A-19, A-20, A-21, A-22]
attempts: {build: 2, export: 0, tool: 0}
caps: {build: 2, export: 2, tool: 2, fix_cycles: 3}
reviews:
  - {id: RV01, target: od_c07_mount_v01, verdict: REVISE, blockers: 4, date: "2026-09-30"}
usta_gates:
  - {gate: question_answered, outcome: water_path, date: "2026-09-30"}
  - {gate: concept_picked, outcome: C1, date: "2026-09-30"}
  - {gate: spec_ratified, outcome: "1.0", date: "2026-09-30"}
  - {gate: concept_picked, outcome: C1, date: "2026-09-30"}
  - {gate: spec_ratified, outcome: "1.1", date: "2026-09-30"}
  - {gate: spec_ratified, outcome: "1.2", date: "2026-09-30"}
  - {gate: revise_decision, outcome: accept_deviations, date: "2026-09-30"}
  - {gate: exception_signed, outcome: signed, date: "2026-09-30"}
deliverables: [STEP, STL, scripts, REPORT]
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

Cloud container job (2026-09-30): the record is mirrored to open-dedica/chassis/reports/OD-C07_valve_flowmeter_mount/ after every stage; recreate the workspace from there (its README). Env: source $HOME/oguz.env before every tools call. The Usta answered the OD-H21 question on a decision card (water path); spec 1.0 rests on the standing instruction and wants explicit confirmation.

## Close summary

