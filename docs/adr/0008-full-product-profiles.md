# 8. Compare full product profiles, not single coefficients

Date: 2026-11-25
Status: Accepted

## Context

The case question is cookie-based vs. gummy. The model gives one coefficient for each
(crispedricewafer and gummy), but these are not products. Every cookie candy also
contains chocolate, and almost every gummy is fruity (see ADR 0006). A new product has
a whole set of attributes, so the decision needs a prediction for a full profile.

## Decision

- Each segment gets one typical profile: the attributes that more than half of the
  candies in the segment have.
  - Cookie: chocolate + crispedricewafer + bar.
  - Gummy: fruity + gummy + pluribus.
  - Peanut/almond: chocolate + peanutyalmondy (bar is exactly 50%, so it is left out).
- sugarpercent is set to the median of all candies for all profiles, so only the
  product type differs.
- `predict()` gives the expected winpercent with a 95% CI for the average product with
  that profile, not a prediction interval for one product.
- The two profiles are compared with `contrast()`, so the difference has its own CI and p-value.
- The profile difference is also checked in the robustness table (strict gummy definition,
  model without Starburst).
- No chocolate gummy profile: there is no such candy in the data.

## Consequences

- Sugar cancels out in the difference, so the median choice only moves the levels,
  not the comparison.
- The profile difference is mostly chocolate vs. fruity, not cookie vs. gummy texture.
- The >50% rule is a judgement call. A different threshold could give a different profile.
- A single new product will vary more than the CI shows.
- The profile weights are written twice in the notebook (robustness cell and profiles
  cell). If a profile changes, both need to change.
