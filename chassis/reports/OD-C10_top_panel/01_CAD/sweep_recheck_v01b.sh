#!/usr/bin/env bash
# v01b re-check of the v01 sweep (spec 1.2 U-03 (a)): no rebuild, no export. Runs
# check_od_c10_top_v01b.py on the STEP/STL files already in 01_CAD/sweep_v01/<run>/ and writes
# 01_CAD/sweep_v01b/<run>/check.json. Same variants and --quick choice as sweep_od_c10_top_v01.sh.
set -u
. "$HOME/oguz-env/env.sh"
WS="$(cd "$(dirname "$0")/.." && pwd)"
REPO="${OGUZ_REPO:-/home/claude/oguz-atolye}"
declare -A V=(
  [nominal]='{}'
  [hole_d_lo]='{"hole_d": 3.3}'                  [hole_d_hi]='{"hole_d": 3.5}'
  [cbore_d_lo]='{"cbore_d": 6.4}'                [cbore_d_hi]='{"cbore_d": 6.6}'
  [cbore_floor_y_lo]='{"cbore_floor_y": 217.9}'  [cbore_floor_y_hi]='{"cbore_floor_y": 218.1}'
  [col_dx_lo]='{"col_dx": -0.1}'                 [col_dx_hi]='{"col_dx": 0.1}'
  [col_dz_lo]='{"col_dz": -0.1}'                 [col_dz_hi]='{"col_dz": 0.1}'
  [col_bottom_y_lo]='{"col_bottom_y": 214.95}'   [col_bottom_y_hi]='{"col_bottom_y": 215.05}'
  [pad_bottom_y_lo]='{"pad_bottom_y": 210.45}'   [pad_bottom_y_hi]='{"pad_bottom_y": 210.55}'
  [skirt_bottom_y_lo]='{"skirt_bottom_y": 214.9}' [skirt_bottom_y_hi]='{"skirt_bottom_y": 215.1}'
)
declare -A FULL=([cbore_d_lo]=1 [cbore_d_hi]=1)
RUNS=("$@"); [ ${#RUNS[@]} -eq 0 ] && RUNS=("${!V[@]}")
cd "$REPO"
run_one() {
  local r="$1"; local s="01_CAD/sweep_v01/$r"; local d="01_CAD/sweep_v01b/$r"; mkdir -p "$WS/$d"
  local q="--quick"; [ -n "${FULL[$r]:-}" ] && q=""
  uv run tools/run.py python "$WS/01_CAD/check_od_c10_top_v01b.py" --step "$s/od_c10_top_C1_v01_$r.step" \
     --asm "$s/od_c10_assembly_C1_v01_$r.step" --stl "$s/od_c10_top_C1_v01_$r.stl" \
     --record "$s/build_record.json" --scratch "$d/_mesh_check" --variant "${V[$r]}" $q \
     --out "$d/check.json" > "$WS/$d/check.log" 2>&1
  echo "$r done"
}
for r in "${RUNS[@]}"; do run_one "$r" &
  while [ "$(jobs -rp | wc -l)" -ge "${OGUZ_SWEEP_JOBS:-4}" ]; do wait -n; done
done
wait
