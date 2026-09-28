#!/bin/sh
# Regenerates every figure cited as evidence in measure/params.json (run from the run root).
set -e
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_x.png x -20 -18 -15 -12 -9 -6 -3 0 3 6 9 12 14 16 --lim -24 22 -16 50
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_zlow.png z 0.3 1.2 2.0 2.8 3.5 5 6.5 8 9.5 11 12.5 14 15 16 --lim -16 16 -16 16
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_spindle.png z -14.5 -13 -10 -7 -4 -1 --lim -5 7 -5 5
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_xport_up.png x -20 -18 -15.5 -13 -10 -8 -6 -4 -2 -1 -0.5 0 --lim 0 20 22 38
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_xport_lo.png x -20 -18 -15.5 -13 -10 -8 -6 -4 -2 -1 -0.5 0 --lim -22 -2 10 26
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_ztop.png z 42.8 43.8 44.8 45.8 46.8 48.0 --lim -9 9 -9 9
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_x_top.png x 6.0 -6.0 --lim -8 8 42 49
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_ybarb.png y -21.5 -20 -17 -13 -10 -8.6 -8 -7 -6.2 -5.5 --lim -6 6 25 38
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_y_pos.png y 9 10.5 11.2 12 12.8 13.5 --lim -8 20 0 36
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_x_sw.png x 10.5 12.5 15 16.5 17.5 8.5 --lim -12 14 10 36
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_z_brk.png z 14.6 16.5 19 21.5 22.7 23 --lim -2 19 -12 15
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_z_cap.png z 0.6 1.2 1.8 --lim -13 13 -13 13
python3 measure/sec_plot.py intake/aligned_work.stl measure/figures/sec_zplates.png z 35.7 24.65 23.6 16.1 27.0 29 31 33 --lim -22 20 -22 20
python3 measure/rz_scatter.py intake/aligned_work.stl measure/figures/rz_a.png 45 135 225 315 0 90 180 270
python3 measure/rz_scatter.py intake/aligned_work.stl measure/figures/rz_b.png 96 110 125 140 266 270 320 330 --hw 2
python3 measure/unwrap.py measure/figures/unwrap_low.png 2.2 15.2 0.2 15
python3 intake/render_one.py intake/aligned_work.stl measure/figures/zoom_up_py.png 0 1 0 --clip x -22 2
python3 intake/render_one.py intake/aligned_work.stl measure/figures/zoom_lo_my.png 0 -1 0 --clip x -22 2
python3 measure/spline_pitch.py
python3 measure/profiles.py
