# Visual QA

Use this checklist before delivering a chart, chart spec, dashboard mock, or report figure.

## Required Checks

- The title states the metric, asset/protocol/entity, and time window.
- Axes include units such as USD, token amount, tx count, address count, percent, or bps.
- Time zones are explicit when the chart depends on day boundaries.
- Labels fit without overlap.
- Top-N charts disclose the threshold and whether "other" is included.
- Missing, unlabeled, or unknown data is visible when material.
- The chart has a table alternative when addresses, tx hashes, or exact values matter.
- Colors do not carry the only meaning; use labels, ordering, or patterns as needed.
- Outliers are explained or intentionally retained.
- The data source and caveats are written near the visual.

## Onchain Caveats

- Labels and entity clusters may be incomplete.
- USD values depend on price source and timestamp.
- Token decimals must be normalized before plotting.
- Contract upgrades, wrapped assets, bridges, and chain migrations can split the same economic activity.
- Wash trading, MEV, internal transfers, and self-transfers can distort volume metrics.
- Exchange deposit addresses and shared hot wallets can distort holder counts.

## Common Fixes

- Replace a pie chart with a sorted bar chart when there are many categories.
- Replace a crowded network graph with a grouped bar, Sankey, or filtered ego network.
- Add a small table for top addresses next to a concentration chart.
- Split token amount and USD value into separate charts unless a dual-axis chart is justified.
- Use log scale only when documented and visually labeled.
- Redact sensitive addresses before hosted image generation.
