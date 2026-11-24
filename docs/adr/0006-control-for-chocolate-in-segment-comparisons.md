# 6. Compare segments within chocolate and non-chocolate candies

Date: 2026-11-24
Status: Accepted

## Context

Every cookie-based candy contains chocolate, and no gummy does. A direct "gummy vs. cookie-based" comparison (49.0 vs. 66.2 mean `winpercent`) therefore mostly measures the chocolate effect (chocolate 60.9 vs. non-chocolate 42.3 across all 83 candies).

## Decision

Each segment is compared with its natural peers, on the 83 candies left after removing the coins:

| Group | n | Mean winpercent |
|---|---|---|
| cookie-based | 7 | 66.2 |
| other chocolate | 30 | 59.7 |
| gummy | 11 | 49.0 |
| other non-chocolate | 35 | 40.2 |

## Consequences

- The comparison shows whether each segment adds something on top of chocolate (here about +6.5 and +8.8 points).
- The direct gummy vs. cookie-based difference is not presented as a segment effect.
- Any later model has to deal with the same overlap, together with the strong negative correlation between `chocolate` and `fruity`.
