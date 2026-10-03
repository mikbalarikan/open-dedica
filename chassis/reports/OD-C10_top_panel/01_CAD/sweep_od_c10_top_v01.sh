#!/usr/bin/env bash
# D7 sweep of od_c10_top v01 (spec 1.1): rebuild at nominal, low and high of every fit-critical
# parameter (plan section 4) into 01_CAD/sweep_v01/<run>/ and run the same checks, the descent
# (U-03 (b), dy +40 .. 0 in 2.0 steps) included in every run. The wall scan (min_wall, the
# whole-part overhang census, flat ceilings) runs where the parameter can move a wall: the
# counterbore diameter; every other run passes --quick.
# Usage: sweep_od_c10_top_v01.sh <run> ...   (no argument: every run); from any folder.
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
  local r="$1"; local d="01_CAD/sweep_v01/$r"; mkdir -p "$WS/$d"
  local q="--quick"; [ -n "${FULL[$r]:-}" ] && q=""
  uv run tools/run.py python "$WS/01_CAD/build_od_c10_top.py" --variant "${V[$r]}" --out-dir "$d" \
     --tag "v01_$r" --record "$d/build_record.json" > "$WS/$d/build.log" 2>&1
  uv run tools/run.py python "$WS/01_CAD/check_od_c10_top.py" --step "$d/od_c10_top_C1_v01_$r.step" \
     --asm "$d/od_c10_assembly_C1_v01_$r.step" --stl "$d/od_c10_top_C1_v01_$r.stl" \
     --record "$d/build_record.json" --scratch "$d/_mesh_check" --variant "${V[$r]}" $q \
     --out "$d/check.json" > "$WS/$d/check.log" 2>&1
  echo "$r done"
}
for r in "${RUNS[@]}"; do run_one "$r" &
  while [ "$(jobs -rp | wc -l)" -ge "${OGUZ_SWEEP_JOBS:-3}" ]; do wait -n; done
done
wait
