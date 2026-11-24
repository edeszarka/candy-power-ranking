# 2. Import style and how to run modules

Date: 2026-11-24
Status: Accepted

## Context

`src/features.py` imports from `src/load_data.py` and is also imported from the notebooks. `from load_data import ...` only works when the file is run as a script, and `from src.load_data import ...` only works when the repo root is on the import path. Supporting both would need a `sys.path` workaround inside the module.

## Decision

- Modules inside `src/` import each other as `src.<module>`.
- Modules that import from `src` are run from the repo root as modules: `python -m src.features`.
- Notebooks in `notebooks/` add the repo root with `sys.path.append("..")` before importing.

## Consequences

- One import style works for both the command line and the notebooks.
- `python src/features.py` and the VS Code "Run Python File" button fail with `ModuleNotFoundError: No module named 'src'`; use `python -m src.features` instead.
