# Measure run order (from the run folder)

1. `python3 measure/figures/src/measure_all.py`   -> measure/figures/m_all.json
2. `python3 measure/figures/src/make_params.py`   -> measure/params.json (first pass, no edge rounds)
3. `python3 measure/figures/src/measure_edges.py` -> measure/figures/m_edges.json (corner points come from params.json)
4. `python3 measure/figures/src/make_params.py`   -> measure/params.json (with round_* params)
5. `python3 <skills>/stl-re-measure-intent/scripts/param_table.py measure/params.json --alignment intake/alignment.json`

The other scripts here (sect.py, rzmap.py, rzhole.py, core.py, corners.py, render.py) made the exploration
figures in measure/figures/*.png.
