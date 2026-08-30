# paper/figures/

SVG artwork for the manuscript. Built from `adjudication/applications__full_census.csv` and Freeze 1 `applications__adjudicated.csv`. Captions live in `paper/figures.md`.

```
python3 paper/figures/build_figures.py
python3 paper/build_manuscript.py
python3 paper/verify_numbers.py
```

`series.py` asserts 298 / 14 / 0 before any file is written. If the census moves, the builder fails instead of drawing a stale chart.

Fig 6 artwork uses generic scoreboard labels. Company names for money stay in the caption and still need a publication naming pass.
