# Onchain Analysis Report Template

Use this structure for final user-facing analysis.

## Objective

State the exact question, subject, chain(s), timeframe, and intended decision.

## Scope and Assumptions

List addresses/entities/contracts/tokens, included chains, excluded data, timestamp convention, token unit conversion, and USD pricing source if used.

## Sources Used

List each platform and why it was used. Include query IDs, endpoint names, notebook/app links, explorer URLs, and docs links when relevant.

## Method

Explain the steps in execution order:

1. Data discovery and source selection.
2. Query/API extraction parameters.
3. Normalization and deduplication.
4. Cross-checks.
5. Chart or report assembly.

## Findings

Use short bullets with numbers, dates, units, and denominators. Separate facts from interpretation.

## Chart Suggestions

- Time series: line or area chart for balances, flows, volume, active users, fees, or TVL.
- Category comparison: bar chart for counterparties, tokens, chains, protocols, or holders.
- Composition over time: stacked area when categories sum to a meaningful total.
- Outlier review: scatter plot or ranked table for unusual transfers, wallets, or days.
- Audit trail: table with tx hash, block/time, from, to, token, amount, source, and notes.

## Caveats

Call out missing chains, unknown labels, attribution confidence, API limits, stale results, pagination risk, pricing source, decoded-table gaps, and assumptions that could change the conclusion.

## Next Checks

List the smallest next checks that would materially improve confidence.
