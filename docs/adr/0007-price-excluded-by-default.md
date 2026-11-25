# 7. pricepercent is left out of the features by default

Date: 2026-11-24
Status: Accepted

## Context

`build_features(df, include_price=False)` returns the model features: the 9 binary columns, `gummy` and `sugarpercent`.

Because price moves together with chocolate, it would absorb part of the chocolate effect. Price is set by Lidl, so it is a decision, not a product attribute.

## Decision

- `pricepercent` is not part of the default feature set.
- It is added only with `include_price=True`, as a sensitivity check.
- `src/features.py` contains no interactions, scaling or feature selection; those belong to the modelling step.

## Consequences

- The default feature set describes popularity from candy characteristics only.
- Running with `include_price=True` shows whether the conclusions change when price is included.
