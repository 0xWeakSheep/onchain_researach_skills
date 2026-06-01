# Observable Workflows

## Interactive Onchain Notebook

1. Create named cells for data loading, parsing, metric computation, chart, inputs, and notes.
2. Load data from API, file attachment, cloud file, database, or pasted result.
3. Normalize columns early: timestamp, chain, address, token, amount, USD value, label.
4. Use Plot or chart cells for first-pass charts.
5. Add Inputs only for meaningful controls such as chain, token, date range, top-N, or address.
6. Add caveats in Markdown cells near the chart.

## Plot vs D3

- Use Plot for bars, lines, areas, dots, histograms, heatmaps, faceting, and most exploratory charts.
- Use D3 when the user asks for custom network diagrams, force layouts, bespoke interactions, custom scales, or complex annotation.
- Use data tables for audit trails and exact row inspection.

## Data Access Choice

- Use file attachments for local CSV/JSON snapshots.
- Use cloud files when the team already keeps data in managed storage.
- Use SQL/database docs when connecting to warehouses.
- Use API calls for live onchain/explorer/API data, with secrets for credentials.
- Use imports for reusable chart helpers or existing notebook logic.

## Sharing and Embedding

1. Decide whether the notebook is public, private, workspace-only, or embedded.
2. Remove secrets and private data before public sharing.
3. Use comments for review and history for rollback.
4. Use templates or forks when adapting reusable analysis patterns.
5. For React embedding, use the dedicated embed docs and preserve notebook access rules.

## Lightweight Chart Rules

- Put the core takeaway in a Markdown sentence above or below the chart.
- Use time on the x-axis for trends and sorted categories for bars.
- Keep labels short but include units.
- Use Inputs for filtering, not for decoration.
- Use tables beside charts when a transaction hash, address, or label must be auditable.
- Include an "unknown" or "unlabeled" category rather than dropping missing labels.
