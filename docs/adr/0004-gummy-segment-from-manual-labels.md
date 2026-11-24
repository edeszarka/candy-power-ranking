# 4. Gummy segment from hand-written labels

Date: 2026-11-24
Status: Accepted

## Context

The case question contrasts gummies with cookie-based sweets, but the dataset has no gummy column. A rule built from existing columns (`fruity & ~chocolate & ~hard & pluribus`, 19 candies) was tried first and rejected:

- It included candies that are not gummies: gum (Chiclets), licorice (Red vines), a wax bottle (Nik L Nip) and chewy candies (Skittles, Starburst, Mike & Ike).
- It missed real gummies: Haribo Happy Cola has `fruity = 0`, and Lifesavers big ring gummies has `pluribus = 0`.

## Decision

- Gummies are labelled by hand in `data/manual_labels.csv` (columns `competitorname`, `certainty`). Only gummies are listed.
- A broad definition is used: anything with a gummy texture, gelatin- or starch-based, because the case question is about the consumer experience rather than ingredients.
  - `certain` (7): Haribo Gold Bears, Haribo Happy Cola, Haribo Sour Bears, Haribo Twin Snakes, Lifesavers big ring gummies, Welch's Fruit Snacks, Sour Patch Tricksters.
  - `borderline` (4): Sour Patch Kids and Swedish Fish (starch-based, sold as "soft & chewy"), Trolli Sour Bites (gummy with a sugar shell), Dots (gumdrops).
  - Explicitly not gummies: Nik L Nip, Chiclets, Twizzlers, Red vines, and chewy candies such as Mike & Ike, Starburst and Skittles.
- `add_gummy(df, include_borderline=True)` adds a 0/1 `gummy` column. With `include_borderline=False`, only `certain` rows count; this serves as a sensitivity check.
- `add_gummy` asserts that every name in the labels file exists in the data, to catch typos.

## Consequences

- The segment matches the intended meaning, and the definition lives in one file that can be reviewed.
- The labels are a judgement call; results should be reported with both the broad (n = 11) and the strict (n = 7) definition.
- Both groups are small, so differences are indicative only.
