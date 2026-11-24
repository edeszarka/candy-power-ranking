# 3. Remove the coin entries

Date: 2026-11-24
Status: Accepted

## Context

The dataset has 85 entries. "One dime" and "One quarter" are real coins that were used as a control in the original survey; they are not candies. Left in, they distort averages: for example, they are the only entries with zero binary features.

## Decision

`remove_coins(df)` in `src/features.py` drops both rows before any analysis, leaving 83 candies. The original index is kept (no `reset_index`), so every row can still be traced back to its line in the source csv.

## Consequences

- All results describe 83 candies, not 85.
- The index has gaps; code that needs positional alignment (for example assigning a plain numpy array back) must use `.iloc` or reset the index locally.
