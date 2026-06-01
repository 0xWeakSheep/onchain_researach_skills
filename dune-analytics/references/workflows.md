# Dune Workflows

## SQL Metric Build

1. Define metric, chain(s), protocol/contracts, token scope, timeframe, grain, and output columns.
2. Search Data Catalog and existing Dune queries for matching curated tables.
3. Draft SQL with explicit chain/date filters and a small exploratory `LIMIT`.
4. Validate row counts, unit conversion, duplicate keys, and boundary dates.
5. Remove exploratory limits only after verifying cost and runtime.
6. Add chart-ready columns: `time`, `metric`, `category`, `value`, `unit`, and optional `source`.

## Raw SQL API Execution

Use when the query is dynamic or should not be saved first.

1. `POST /api/v1/sql/execute` with `sql` and optional `performance`.
2. Poll `GET /api/v1/execution/{execution_id}/status`.
3. Fetch `GET /api/v1/execution/{execution_id}/results` or CSV when completed.
4. Record execution ID, performance tier, SQL, parameters, and result retrieval URL.

## Saved Query API Execution

Use when the analysis should be reusable, shareable, or managed in Dune.

1. Create or identify a saved query.
2. Execute the query with parameters.
3. Poll status.
4. Fetch latest result or execution-specific result.
5. Use server-side filtering, sorting, pagination, or sampling for downstream applications.

## Dashboard and Report Build

1. Build one query per metric or panel unless a shared base query materially reduces cost.
2. Use parameterized queries for chain, address, token, or date controls.
3. Use line charts for trends, bars for top-N categories, stacked areas for composition, and tables for audit rows.
4. Share/embed only after validating freshness, permissions, and private-query status.
5. If a stakeholder needs a notebook/app surface, route to Hex, Observable, or Deepnote.

## Materialized View or Pipeline

Use materialized views when repeated expensive computation feeds dashboards or downstream APIs. Use pipelines when queries and refreshes must run in dependency order.

1. Identify stable intermediate tables and their refresh cadence.
2. Upsert or refresh materialized views.
3. Execute pipeline and monitor node-level status.
4. Document failure handling and credit impact.

## Uploaded Table Workflow

Use uploads for offchain labels, curated address lists, CSV snapshots, or external classifications.

1. Create uploaded table with explicit schema when possible.
2. Upload CSV or insert CSV/NDJSON.
3. Join uploaded data to Dune tables using normalized addresses and chain columns.
4. Clear or delete stale uploaded data intentionally; do not mutate user-owned tables without explicit instruction.

## Dune to Hex

Use Dune Trino when Hex should query Dune datasets directly. Confirm credentials, catalog/schema, query pushdown, and cost. Keep heavy joins in Dune/Trino and use Hex for presentation, parameterization, collaboration, and scheduled stakeholder reports.

## Cross-Platform Checks

- Use Etherscan to validate sample transaction hashes, logs, ABI/source, and address-level token transfers.
- Use Arkham to validate labels, entities, counterparties, and entity-level attribution.
- Use notebook tools for presentation after the Dune SQL result is stable.
