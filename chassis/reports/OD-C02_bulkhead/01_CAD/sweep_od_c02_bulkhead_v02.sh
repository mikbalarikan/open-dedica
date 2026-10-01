#!/usr/bin/env bash
# D7 sweep of od_c02_bulkhead v02: every fit-critical parameter at low and high (plan
# amendment v02 section 4), each variant built into 01_CAD/sweep_v02/<name>/ and checked
# with the full check script. Run from anywhere; needs OGUZ_JOBS (oguz-env.sh).
set -u
source /home/claude/oguz-env.sh
REPO=/home/claude/oguz-atolye
WS="$OGUZ_JOBS/20260930-od-c02-bulkhead"
run() {
  name="$1"; var="$2"; d="01_CAD/sweep_v02/$name"
  mkdir -p "$WS/$d"
  (cd "$REPO" && uv run tools/run.py python "$WS/01_CAD/build_od_c02_bulkhead_v02.py" --variant "$var" \
      --out-dir "$d" --tag "v02_$name" --record "$d/build_record.json" > "$WS/$d/build.log" 2>&1 && \
   uv run tools/run.py python "$WS/01_CAD/check_od_c02_bulkhead_v02.py" --variant "$var" \
      --step "$d/od_c02_bulkhead_C1_v02_$name.step" --asm "$d/od_c02_assembly_C1_v02_$name.step" \
      --stl "$d/od_c02_bulkhead_C1_v02_$name.stl" --record "$d/build_record.json" \
      --scratch "$d/_mesh_check" --out "$d/check.json" > "$WS/$d/check.log" 2>&1)
  echo "$name done $?"
}
run bore_d_low '{"bore_d": 3.95}' &
run bore_d_high '{"bore_d": 4.05}' &
run bore_depth_low '{"bore_depth": 5.9}' &
run bore_depth_high '{"bore_depth": 6.1}' &
wait
run bore_shift_low '{"shift_x": -0.07, "shift_z": -0.07}' &
run bore_shift_high '{"shift_x": 0.07, "shift_z": 0.07}' &
run wall_low '{"wall_x0": 62.9, "wall_x1": 66.9}' &
run wall_high '{"wall_x0": 63.1, "wall_x1": 67.1}' &
wait
run brail_x0_low '{"brail_x0": 58.9}' &
run brail_x0_high '{"brail_x0": 59.1}' &
run brail_x1_low '{"brail_x1": 70.9}' &
run brail_x1_high '{"brail_x1": 71.1}' &
wait
echo sweep finished
