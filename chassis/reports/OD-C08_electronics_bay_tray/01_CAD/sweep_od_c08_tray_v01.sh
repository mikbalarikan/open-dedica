#!/usr/bin/env bash
# D7 sweep of od_c08_tray v01: every fit-critical parameter of DESIGN_PLAN section 4 at its
# low and high value, one at a time (no motion variables), into 01_CAD/sweep_v01/<run>/.
# Run from the repository root after `. $HOME/oguz-env/env.sh`; the workspace is this file's ../
set -u
WS="$(cd "$(dirname "$0")/.." && pwd)"
CAD="$WS/01_CAD"
run() {
  name="$1"; variant="$2"
  out="01_CAD/sweep_v01/$name"
  mkdir -p "$WS/$out"
  uv run tools/run.py python "$CAD/build_od_c08_tray.py" --variant "$variant" --out-dir "$out" --tag "sw_$name" \
     --record "$out/build_record.json" > "$WS/$out/build.log" 2>&1
  uv run tools/run.py python "$CAD/check_od_c08_tray.py" --step "$out/od_c08_tray_C1_sw_$name.step" \
     --asm "$out/od_c08_assembly_C1_sw_$name.step" --stl "$out/od_c08_tray_C1_sw_$name.stl" \
     --record "$out/build_record.json" --out "$out/check.json" --scratch "$out/_mesh" --variant "$variant" \
     > "$WS/$out/check.log" 2>&1
  echo "done $name"
}
RUNS=(
"pin_d_low|{\"pin_d\":1.75}"
"pin_d_high|{\"pin_d\":1.85}"
"bore_d_low|{\"bore_d\":3.95}"
"bore_d_high|{\"bore_d\":4.05}"
"hole_d_low|{\"hole_d\":3.3}"
"hole_d_high|{\"hole_d\":3.5}"
"seat_x_low|{\"seat_x\":82.388}"
"seat_x_high|{\"seat_x\":82.488}"
"shift_y_low|{\"shift_y\":-0.1}"
"shift_y_high|{\"shift_y\":0.1}"
"shift_z_low|{\"shift_z\":-0.1}"
"shift_z_high|{\"shift_z\":0.1}"
)
n=0
for item in "${RUNS[@]}"; do
  run "${item%%|*}" "${item#*|}" &
  n=$((n + 1))
  if [ $((n % 3)) -eq 0 ]; then wait; fi
done
wait
