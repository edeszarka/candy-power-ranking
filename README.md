# candy-power-ranking

A small data science case study on candy popularity. Using FiveThirtyEight's "candy-power-ranking" dataset, it looks at which candy characteristics (chocolate, fruity, caramel, price, sugar content, etc.) are associated with a candy winning head-to-head popularity matchups.

## Data

`candy-data.csv` from FiveThirtyEight: https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking

The data is by FiveThirtyEight and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It is downloaded into `data/` on first run.

## Setup

```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

## Run

```
python src/load_data.py
```

This downloads the data if it is missing, runs basic sanity checks and prints the shape and first rows.

## Results
