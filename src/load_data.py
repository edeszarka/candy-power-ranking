import urllib.request
from pathlib import Path

import pandas as pd

URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv"
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "candy-data.csv"

BINARY_COLS = [
    "chocolate", "fruity", "caramel", "peanutyalmondy", "nougat",
    "crispedricewafer", "hard", "bar", "pluribus",
]
NUMERIC_COLS = ["sugarpercent", "pricepercent", "winpercent"]


def download_data():
    """Download the csv into data/ unless it is already there."""
    if DATA_PATH.exists():
        return
    DATA_PATH.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(URL, DATA_PATH)


def load_data():
    """Read the csv and run basic sanity checks."""
    df = pd.read_csv(DATA_PATH)
    assert len(df) == 85, f"expected 85 rows, got {len(df)}"
    assert df.notna().all().all(), "found missing values"
    for col in BINARY_COLS:
        assert df[col].isin([0, 1]).all(), f"{col} is not 0/1"
    for col in NUMERIC_COLS:
        assert pd.api.types.is_numeric_dtype(df[col]), f"{col} is not numeric"
    return df


if __name__ == "__main__":
    download_data()
    df = load_data()
    print(df.shape)
    print(df.head())
