# Hex Workflows

## Onchain Notebook

1. Define audience: analyst-only notebook, stakeholder report, or published app.
2. Connect Dune Trino, warehouse, file upload, cloud storage, API import, or semantic model.
3. Use SQL cells for warehouse/Dune queries and keep heavy operations in query mode.
4. Use Python cells only when transformation, modeling, or custom API calls are easier outside SQL.
5. Use chart/table/single-value cells for presentation.
6. Publish as an app only after parameters, permissions, and comments are ready.

## SQL Mode Choice

- Use warehouse SQL when the source is a warehouse table, Dune Trino table, or upstream query result from the same connection.
- Use dataframe SQL for local files, small dataframes, Python outputs, or cross-source joins.
- Use query mode for large data; use dataframe mode for Python consumption or small exploratory datasets.
- Avoid forcing full dataframe materialization for large query-mode outputs unless the user accepts slower execution and memory risk.

## Dune-to-Hex Report

1. Build and validate Dune SQL first.
2. Connect Hex through Dune Trino or import result data.
3. Keep Dune query IDs, dataset names, and refresh assumptions in a text cell.
4. Add input cells for chain, address, token, protocol, or date range only when the stakeholder needs controls.
5. Use scheduled runs and notifications for recurring internal reporting.

## App and Sharing

1. Separate notebook iteration from published app content.
2. Use input parameters for controlled exploration.
3. Use App builder for layout and stakeholder-safe views.
4. Set permissions deliberately: editor, viewer, app user, or explore-capable user.
5. Keep comments/reviews on notebook work; keep app comments separate when useful.

## Public API Automation

Use the Public API when external systems need to trigger or inspect Hex projects.

1. Confirm project is published when required by the endpoint.
2. Use a personal or workspace token with the right permissions.
3. Run project with default or custom inputs.
4. Poll run status.
5. Cancel active runs only with explicit user intent.
6. For credential rotation or collection permission changes, require explicit confirmation because these are administrative mutations.

## Lightweight Chart Rules

- Use line charts for balances, volume, fees, active users, or TVL over time.
- Use bar charts for top tokens, counterparties, chains, protocols, or addresses.
- Use tables for tx hashes, addresses, raw rows, and audit trails.
- Use single-value cells for headline totals only when the denominator/timeframe is visible nearby.
- Use color-by for meaningful categories, not decoration.
- Use dual Y-axis only when the units differ and both series are essential.
