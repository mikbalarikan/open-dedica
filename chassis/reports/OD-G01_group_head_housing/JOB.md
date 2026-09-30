---
schema: oguz-job-v1
job_id: "20260930-od-g01-group-head-housing"
code: ODG01
milestone: M1
title: "Open Dedica OD-G01 printed group head housing"
lane: CAD
state: J2_PLAN
blocked_on: null
next_action: "J2: designer J2 package WP-02 returns DESIGN_PLAN.md; check it covers every C1 feature and section 5 row"
data_class: PUBLIC
size: M
process: [FDM]
gate_sections: [U, D, J, E]
spec: "00_Spec/DESIGN_SPEC.md"
spec_version: "1.0"
workspace: "${OGUZ_JOBS}/20260930-od-g01-group-head-housing"
delivery: "${OGUZ_DELIVERY}/20260930-od-g01-group-head-housing"
artifacts: "${OGUZ_ARTIFACTS}/20260930-od-g01-group-head-housing"
repo_commit: e0b3c9471554d989fb8dc8cdc006c93c02a40ac5
active_target: od_g01_housing_v01
revision: A
open_assumptions: [A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18, A-19, A-20, A-21, A-22, A-23, A-24, A-25]
attempts: {build: 0, export: 0, tool: 0}
caps: {build: 2, export: 2, tool: 2, fix_cycles: 3}
reviews: []
usta_gates:
  - {gate: spec_ratified, outcome: "1.0", date: "2026-09-30"}
  - {gate: concept_picked, outcome: C1, date: "2026-09-30"}
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

Cloud container job (2026-09-30): the record is mirrored to open-dedica/chassis/reports/OD-G01_group_head_housing/ after every stage; recreate the workspace from there (its README). Env: source /home/user/oguz-env.sh before every tools call. Intake attempt 1 died with a session interrupt (see the note event). Usta gates of 2026-09-30 rest on the standing instruction and want explicit confirmation.

## Close summary

