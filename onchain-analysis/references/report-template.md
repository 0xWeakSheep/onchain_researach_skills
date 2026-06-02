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

1. Run directory setup under `out/runs/<run_id>/`.
2. Skill plan in `specs/skill-plan.md`.
3. Data discovery and source selection.
4. Query/API extraction parameters.
5. Normalization and deduplication.
6. Cross-checks.
7. Chart or report assembly through `onchain-charting`.
8. Artifact location check through `onchain-finalizer`.

## Findings

Use short bullets with numbers, dates, units, and denominators. Separate facts from interpretation.

## Chart Plan

Summarize the `onchain-charting` decision:

- Chart objective.
- Chart type.
- Data file path.
- Chart spec path.
- Rendered chart path.
- Visual QA caveats.

## Artifact Paths

List final files:

- `manifest.json`:
- `run.md`:
- `specs/skill-plan.md`:
- `logs/output-location-check.txt`:
- `data/`:
- `charts/`:
- `summaries/`:
- `reports/`:
- `specs/`:
- `logs/`:

## Caveats

Call out missing chains, unknown labels, attribution confidence, API limits, stale results, pagination risk, pricing source, decoded-table gaps, and assumptions that could change the conclusion.

## Next Checks

List the smallest next checks that would materially improve confidence.
