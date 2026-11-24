# 5. Cookie-based segment uses the crispedricewafer column

Date: 2026-11-24
Status: Accepted

## Context

Only Twix is a cookie-based candy in the strict sense (Kit Kat is a wafer), which is too few to analyse. The dataset's own `crispedricewafer` column is defined by FiveThirtyEight as "Does it contain crisped rice, wafers, or a cookie component?". It covers 7 candies: Twix, Kit Kat, 100 Grand, Hershey's Krackel, Nestle Crunch, Snickers Crisper and Whoppers.

## Decision

- The cookie-based segment is `crispedricewafer == 1`. No manual label is created for it.
- No extra `chocolate == 1` filter is applied: all 7 candies already contain chocolate, so the filter would change nothing.

## Consequences

- The segment comes from the source data, not from a manual judgement.
- It is broader than "cookie" and should be presented as "cookie / wafer / crisped rice" (crunchy).
- n = 7, so results are indicative only.
