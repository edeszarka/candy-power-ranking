# 1. Minimal project structure

Date: 2026-11-23
Status: Accepted

## Context

This is a small case study. Every extra tool (config files, CLI framework, tests, CI, Docker) has to be understood and maintained, and adds little at this size.

## Decision

- Plain Python functions in `src/`, no classes and no extra abstractions.
- `src/load_data.py` downloads `candy-data.csv` with the standard library (`urllib`) only if the file is missing, then checks it with plain `assert`s (85 rows, no missing values, binary columns are 0/1, the percent columns are numeric).
- The csv is committed in `data/`, so the analysis does not depend on the source URL staying available.
- `requirements.txt` lists only pandas, numpy, scipy and matplotlib, plus notebook to run the notebooks, pinned to the versions installed in a fresh virtualenv.

## Consequences

- Anyone can follow the code without learning a framework.
- Pinned versions make the results reproducible, but they have to be updated by hand.
- The sanity checks stop the pipeline early if the source data ever changes.
