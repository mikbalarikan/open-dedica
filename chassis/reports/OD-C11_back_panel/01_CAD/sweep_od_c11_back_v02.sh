#!/usr/bin/env bash
# D7 sweep of od_c11_back v02 (spec 1.1): rebuild at nominal, low and high of every fit-critical
# parameter (plan section 4) into 01_CAD/sweep_v02/<run>/ and run the same checks.
# Usage: sweep_od_c11_back_v02.sh <run> ...   (no argument: every run); from any folder.
set -u
. "$HOME/oguz-env/env.sh"
WS="$(cd "$(dirname "$0")/.." && pwd)"
REPO="${OGUZ_REPO:-/home/claude/oguz-atolye}"
declare -A V=(
  [nominal]='{}'
  [flange_hole_d_lo]='{"flange_hole_d": 3.3}'        [flange_hole_d_hi]='{"flange_hole_d": 3.5}'
  [flange_hole_dx_lo]='{"flange_hole_dx": -0.1}'     [flange_hole_dx_hi]='{"flange_hole_dx": 0.1}'
  [insert_d_lo]='{"insert_d": 3.95}'                 [insert_d_hi]='{"insert_d": 4.05}'
  [insert_depth_lo]='{"insert_depth": 5.9}'          [insert_depth_hi]='{"insert_depth": 6.1}'
  [pass_d_lo]='{"pass_d": 11.9}'                     [pass_d_hi]='{"pass_d": 12.1}'
  [wall_z_lo]='{"wall_z_out": -302.1, "wall_z_in": -299.1}'  [wall_z_hi]='{"wall_z_out": -301.9, "wall_z_in": -298.9}'
  [y_top_lo]='{"y_top": 214.9}'                      [y_top_hi]='{"y_top": 215.1}'
)
RUNS=("$@"); [ ${#RUNS[@]} -eq 0 ] && RUNS=("${!V[@]}")
cd "$REPO"
run_one() {
  local r="$1"; local d="01_CAD/sweep_v02/$r"; mkdir -p "$WS/$d"
  uv run tools/run.py python "$WS/01_CAD/build_od_c11_back_v02.py" --variant "${V[$r]}" --out-dir "$d" \
     --tag "v02_$r" --record "$d/build_record.json" > "$WS/$d/build.log" 2>&1
  uv run tools/run.py python "$WS/01_CAD/check_od_c11_back_v02.py" --step "$d/od_c11_back_C1_v02_$r.step" \
     --asm "$d/od_c11_assembly_C1_v02_$r.step" --stl "$d/od_c11_back_C1_v02_$r.stl" \
     --record "$d/build_record.json" --scratch "$d/_mesh_check" --variant "${V[$r]}" \
     --out "$d/check.json" > "$WS/$d/check.log" 2>&1
  echo "$r done"
}
for r in "${RUNS[@]}"; do run_one "$r" & 
  while [ "$(jobs -rp | wc -l)" -ge "${OGUZ_SWEEP_JOBS:-5}" ]; do wait -n; done
done
wait
