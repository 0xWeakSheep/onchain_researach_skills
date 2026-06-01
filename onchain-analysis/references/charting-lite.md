# Lightweight Charting Guidance

This is intentionally shallow. Do not turn this skill into a visual design system until a dedicated chart-design package is added.

## Chart Choice

- Use a line chart for a single metric over time.
- Use a grouped or stacked bar chart for category comparison.
- Use a stacked area chart only when categories are parts of a total.
- Use a scatter plot for outliers or relationship checks.
- Use a table when the user needs auditability, tx hashes, or exact rows.

## Minimum Quality Bar

- Title must state metric, chain/scope, and timeframe.
- Axis labels must include units.
- Legends must use human-readable token/protocol/entity names when available.
- Do not hide zero baselines on bar charts.
- Annotate major known events if they explain a visible discontinuity.
- Keep chart and table filters aligned with the written analysis.

## Onchain-Specific Notes

- Separate inflow and outflow unless net flow is explicitly requested.
- Show native units and USD value only when the conversion source is documented.
- Avoid mixing chains in one series unless the chain dimension is explicit.
- For labels and entities, include an "unknown" bucket instead of dropping unlabeled rows.
- For holder charts, state whether contracts, bridges, exchanges, team wallets, or burn addresses are included.
