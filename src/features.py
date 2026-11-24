from pathlib import Path

import pandas as pd

from src.load_data import download_data, load_data

LABELS_PATH = Path(__file__).resolve().parent.parent / "data" / "manual_labels.csv"

BINARY_COLS = [
    "chocolate",
    "fruity",
    "caramel",
    "peanutyalmondy",
    "nougat",
    "crispedricewafer",
    "hard",
    "bar",
    "pluribus",
    "gummy",
]


def remove_coins(df):
    # "One dime" and "One quarter" are coins used as a control in the survey, not candies
    return df[~df["competitorname"].isin(["One dime", "One quarter"])]


def add_gummy(df, include_borderline=True):
    labels = pd.read_csv(LABELS_PATH)
    missing = labels.loc[
        ~labels["competitorname"].isin(df["competitorname"]), "competitorname"
    ]
    assert missing.empty, f"not in data: {missing.tolist()}"

    if not include_borderline:
        labels = labels[labels["certainty"] == "certain"]

    df = df.copy()
    df["gummy"] = df["competitorname"].isin(labels["competitorname"]).astype(int)
    return df


def build_features(df, include_price=False):
    cols = BINARY_COLS + ["sugarpercent"]
    if include_price:
        cols = cols + ["pricepercent"]
    return df[cols], df["winpercent"]


if __name__ == "__main__":
    download_data()
    df = add_gummy(remove_coins(load_data()))
    X, y = build_features(df)
    print(X.shape)
    print(list(X.columns))
    print(X[BINARY_COLS].sum())
