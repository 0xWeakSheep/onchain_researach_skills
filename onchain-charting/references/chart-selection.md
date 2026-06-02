# Chart Selection

Use the user's analytical intent to choose the simplest chart that answers the question.

## Intent Map

| Intent | Default chart | Use when | Avoid when |
|---|---|---|---|
| Trend over time | Line | Daily volume, fees, TVL, holders, active addresses | The x-axis is not time |
| Cumulative trend | Area | Cumulative inflow, cumulative users, cumulative supply | Comparing precise values across many groups |
| Ranked comparison | Horizontal bar | Top wallets, protocols, tokens, chains, counterparties | There are more than 20 categories without grouping |
| Part-to-whole | Stacked bar or treemap | Composition by chain, token, entity type | Precise comparison matters |
| Flow volume | Sankey | Aggregated source-target flows | Showing individual transaction sequence |
| Transaction path | Flow diagram | A small number of ordered hops | Many nodes or repeated loops |
| Relationship map | Network graph | Address clusters, counterparty graph, bridge routes | Edges do not have meaning or there are too many nodes |
| Distribution | Histogram | Trade sizes, transfer values, holding values | Exact entity-level audit is required |
| Outliers and spread | Boxplot or violin | Fee distribution, slippage, trade-size spread | The audience is unfamiliar with distribution charts |
| OHLC price | Candlestick | Token or stock-token K-line with open/high/low/close | Only close price is available |
| Two metrics | Dual-axis with care | Volume bars plus price line | Axes imply a false relationship |
| Calendar behavior | Heatmap | Hour/day activity, gas spikes, recurring flows | Sparse data with too many empty buckets |
| Cohort retention | Cohort heatmap | Wallet retention, repeated trader behavior | Cohorts are not comparable |
| Audit rows | Table | Addresses, tx hashes, raw labels, exact values | Trying to explain a trend visually |

## Onchain-Specific Defaults

- Wallet flow: use a Sankey for aggregated flow and a table for tx hashes.
- Token market: line for close price, candlestick for OHLC, bar for volume.
- Holder concentration: ranked bar for top holders, Lorenz-style cumulative line for concentration, histogram for distribution.
- Protocol revenue: line by time, stacked bar by source, table for source definitions.
- Bridge analysis: Sankey by bridge direction, map only if geography is truly relevant.
- Smart-money activity: line for signal count over time, bar for top tokens, scatter for gain vs holding time.
- Security/audit findings: risk matrix or table, not a decorative chart.

## Chart Restraints

- Do not use pie charts for more than five categories.
- Do not use network graphs as decoration; every edge needs a definition.
- Do not use Sankey on raw transaction rows before aggregation.
- Do not stack unrelated units.
- Do not mix token amount and USD value without clear labels.
- Do not hide "unknown", "unlabeled", or "other" categories if they affect interpretation.
