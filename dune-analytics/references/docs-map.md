# Dune Official Docs Map

Sources:

- Main docs: https://docs.dune.com/
- Documentation index: https://docs.dune.com/llms.txt
- Data API overview: https://docs.dune.com/api-reference/api-overview.md
- Authentication: https://docs.dune.com/api-reference/overview/authentication.md
- Execute SQL: https://docs.dune.com/api-reference/executions/endpoint/execute-sql.md
- Dune + Hex connector: https://docs.dune.com/api-reference/connectors/trino/hex.md

## Product Surface

- Data Hub: SQL editor, dashboards, visualizations, sharing, embeds, imports/exports, search/discovery, contract decoding, team management.
- Data API: query execution, raw SQL execution, results retrieval, query management, uploads, materialized views, pipelines, usage, webhooks.
- Datashare: stream Dune data into Snowflake, BigQuery, or Databricks.
- Sim realtime APIs: realtime balances, transactions, DeFi positions, and application APIs.
- Catalyst: blockchain integration toolkit for chains and protocols.
- Agent tools: Dune CLI, Dune skills, MCP, and Machine Payment Protocol.

## Authentication and API Context

- API keys are created under a user or team context.
- A key can have `Read` or `Read/Write` scope.
- Prefer header auth: `X-DUNE-API-KEY: <api_key>`.
- Query parameter auth exists as `api_key`, but avoid it in shared URLs and logs.
- Never commit keys. Use environment variables or the platform secret store.
- Query ownership and private query management depend on the account/team context behind the key.

## Data API Endpoint Groups

### Executions and Results

- Execute saved query.
- Execute raw SQL.
- Execute query pipeline.
- Cancel execution.
- Get execution status.
- Get execution result as JSON.
- Get execution result as CSV.
- Get latest query result as JSON or CSV.
- Result filtering, pagination, sampling, and sorting.

Raw SQL endpoint:

- Path: `POST https://api.dune.com/api/v1/sql/execute`
- Body fields: `sql`, optional `performance` (`small`, `medium`, `large`).
- Response includes `execution_id` and initial state.
- Follow-up calls poll status and retrieve results.

### Query Management

- Create, read, update, list, archive, unarchive, private, and unprivate queries.
- Get query pipeline definition.
- Private and owner-scoped operations require the correct API-key context.

### Materialized Views and Pipelines

- Upsert, get, list, refresh, and delete materialized views.
- Execute pipelines and get pipeline execution status.
- Use pipelines when a query depends on multiple queries or materialized views.

### Uploaded Tables

- Create table.
- Upload CSV.
- Insert CSV or NDJSON.
- Clear data.
- List uploaded tables.
- Delete table.
- Migration guide for deprecated `/v1/table/*` endpoints to `/v1/uploads/*`.

### Datasets, Usage, Webhooks, and SDKs

- List/get/search datasets.
- Search datasets by contract address.
- Get usage for billing periods.
- Create webhooks from query results.
- Official SDKs: Python, TypeScript/JavaScript, Go.

## Connectors and Transformations

- dbt connector: project setup, incremental models, dbt to Datashare, CI/CD workflows, pricing/best practices, supported SQL operations.
- Trino connector: Trino/Presto access from Hex, Metabase, DBeaver, PowerBI-like BI flows, SDKs.
- Datashare: Snowflake, BigQuery, Databricks targets.

## Data Catalog Coverage

Use the Data Catalog before inventing tables. Important families:

- Chain raw tables: blocks, transactions, logs, traces, creation traces.
- Decoded tables: contracts, decoded logs, decoded traces, call tables, event tables.
- Curated balances: latest balances, daily balance updates, balance updates.
- Bridges: deposits, withdrawals, flows.
- CEX flows: exchange address directories, deposit addresses, flows.
- DEX trades: `dex.trades`, `dex_aggregator.trades`, sandwich tables, Solana DEX/Jupiter tables.
- Gas and fees: EVM gas fees and Solana fee data.
- Labels: address labels, owner details, owner addresses, ENS, Safe addresses.
- Lending: supply, borrow, flash loans, market info.
- NFT: trades, mints, transfers, metadata.
- Payments: stablecoin commerce flows, card transactions, agentic payments.
- Prediction markets: Polymarket, Kalshi, and cross-venue normalized markets/trades/OHLCV.
- Prices: latest, minute, hourly, daily, and legacy USD prices.
- Rollup economics: L1 fees and L2 revenue.
- Stablecoins: transfers, balances, enriched activity, token reference tables across EVM/Solana/Tron.
- Staking: Ethereum deposits, entities, flows, validator info.
- Token metadata and transfers: EVM, Solana, Aptos, Sui, Stellar, XRPL, multichain.
- Utilities: calendar/scaffold tables such as `utils.days`.

## SQL and Metric Rules

- Prefer curated tables for standard protocol/market metrics.
- Use decoded/raw tables when exact contract behavior, event semantics, or auditability matters.
- Always define time grain, chain filters, token decimals, price source, and dedupe keys.
- Parameterize user-facing queries for addresses, tokens, protocols, chains, and dates.
- Add `LIMIT` while exploring; remove or justify it in final production queries.
