# Deepnote Workflows

## Onchain Notebook Workflow

1. Define the analysis question, target chains, date range, addresses/contracts, and required outputs.
2. Connect the primary source through a warehouse/database integration, uploaded file, cloud file, or API call from Python.
3. Use SQL blocks to create staged tables for transfers, swaps, events, balances, labels, and time buckets.
4. Use query preview mode while shaping large SQL; switch to DataFrame mode only for data that Python must process fully.
5. Normalize fields early: `chain`, `block_time`, `tx_hash`, `log_index`, `address`, `token_address`, `amount_raw`, `amount`, `amount_usd`, `label`, `source`.
6. Use Python blocks for API enrichment, entity matching, address clustering imports, token metadata, anomaly scoring, and final chart/table formatting.
7. Add chart blocks or Python charts for first-pass visuals, then add notes with source, assumptions, and unresolved caveats.

## SQL And Python Pattern

1. Start with a SQL block that scopes the base population.
2. Keep intermediate SQL blocks small and named; use query chaining for CTE-like development.
3. Use DataFrame SQL for local CSV/Excel/Parquet-style snapshots and DataFrame joins.
4. Inject Python variables into SQL with JinjaSQL only for controlled parameters such as date ranges, selected chains, or address lists.
5. Use `inclause` for address/token lists and avoid raw string concatenation.
6. Push expensive filtering and aggregation into the warehouse before loading DataFrames.
7. Use Python for operations that are awkward in SQL: graph traversals, scoring, API batching, custom visualization, and report exports.

## Scheduled Monitoring

1. Put the reusable monitoring logic in a dedicated notebook or project.
2. Ensure every block can run from a clean state with secrets and integrations configured.
3. Add explicit checks that fail the run when thresholds are breached, such as abnormal inflow, missing rows, stale source data, or unexpected holder concentration.
4. Configure schedule frequency according to the signal: hourly/daily for monitoring, weekly/monthly for reporting.
5. Enable success/failure notifications when the result should go to an operator or research channel.
6. Review run snapshots and logs when a scheduled execution fails.
7. Split work across projects when more than one scheduled notebook is required.

## API-Triggered Run

1. Confirm the workspace plan supports the needed API surface.
2. Create a workspace API key and store it in the caller's secret manager.
3. Send `Authorization: Bearer <token>`; never put the token in notebooks, URLs, or logs.
4. Use the classic API for programmatic execution of an existing notebook.
5. Use Public API v2 only after checking whether preview status is acceptable for the workflow.
6. For production-critical automation, design retries, failure alerts, idempotent inputs, and run-result checks outside Deepnote.
7. Record the notebook URL, run snapshot, input parameters, and output artifact location for auditability.

## Data App Or Streamlit Delivery

1. Decide whether the audience needs an internal notebook, a Deepnote app, an embedded block, or a Streamlit app.
2. Keep the notebook logic separate from presentation blocks where possible.
3. Use input blocks only for meaningful controls: chain, protocol, token, address, date range, top-N, threshold.
4. Make every displayed chart or table traceable to a source query or DataFrame.
5. Hide or remove private tables, secrets, API keys, and intermediate debug output before sharing.
6. Use workspace permissions, notebook locking, comments, and code reviews when multiple people maintain the analysis.

## Lightweight Chart Rules

- Use chart blocks for fast exploration and stakeholder previews.
- Use line charts for time series, bar charts for ranked categories, scatterplots for relationships, and big number blocks for headline metrics.
- Keep units visible: token amount, USD, percentage, transaction count, address count, or basis points.
- Add grouping only when it explains a second dimension such as chain, protocol, token, or entity type.
- Use filters for drill-down, not for hiding inconvenient missing or unlabeled data.
- Put transaction hashes, addresses, and labels in tables when auditability matters.
- Use custom tooltips for extra context such as entity label, address, tx count, or last activity time.

## Safety Checklist

- Secrets live in environment variables, SSH keys, or managed integrations.
- Public notebooks/apps contain no private credentials, raw secrets, or non-public data.
- SQL injected from Python variables is parameter-like and uses JinjaSQL helpers where needed.
- Large warehouse queries are previewed/cached before full DataFrame loads.
- Scheduled notebooks fail loudly on stale data, empty result sets, or threshold breaches.
- API usage treats Public API v2 preview status as a deployment risk.
