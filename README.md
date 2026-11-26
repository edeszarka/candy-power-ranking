# Lidl candy case: what drives candy preference?

**Recommendation:** a chocolate-based store-brand candy. Chocolate is the strongest driver of preference; texture (cookie vs. gummy) alone does not decide.

- Chocolate: +22 pp win rate (95% CI 14–30)
- Chocolate cookie bar vs. fruity gummy: +12.4 pp (p = 0.03); stable with a stricter gummy definition and without Starburst (+12.7 / +12.6)
- Cookie vs. gummy texture alone: −0.2 pp (p = 0.97)

Presentation: [presentation/candy_analysis.pdf](presentation/candy_analysis.pdf)

## Repository structure
- `src/` – data loading (`load_data.py`), features (`features.py`), OLS with numpy/scipy (`ols.py`)
- `notebooks/01_eda.ipynb` – exploratory analysis
- `notebooks/02_model.ipynb` – model, difference test, robustness, product profiles, diagnostics
- `data/candy-data.csv` – the dataset
- `data/manual_labels.csv` – manual gummy labels
- `docs/adr/` – analysis decisions
- `figures/` – all figures used in the notebooks and the presentation

## How to run
Tested with Python 3.14.3.
```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
jupyter notebook
```
Run `notebooks/01_eda.ipynb`, then `notebooks/02_model.ipynb`. The data is included in `data/` (downloaded if missing).

## Data and license
Data: "candy-power-ranking" by FiveThirtyEight
(https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking),
licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
Changes: the two coins are removed, and a manually labelled `gummy` feature is added.

## Limitations
- Associations, not causal effects.
- Win rate measures preference in head-to-head matchups, not sales.
- No brand or cost information in the data. Most products are well-known brands (my reading of the names), so a new store-brand product will likely do worse than predicted.
- Only 83 products; cookie (7) and gummy (11) groups are small.

## Use of AI
I used an AI assistant (Claude) for writing code, reviewing and wording. The analysis decisions (see `docs/adr/`) and the final recommendation are mine.
