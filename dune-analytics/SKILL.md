---
name: dune-analytics
description: Dune analytics workflow guide. Use when Codex needs Dune SQL, Query Engine, Data Catalog, dashboards, Data API, executions, query management, materialized views, pipelines, uploaded tables, usage/billing, webhooks, dbt connector, Trino/BI connectors including Hex, Datashare, Sim realtime APIs, Catalyst, Dune MCP/CLI/skills, or cross-chain onchain metric analysis.
---

# Dune Analytics

## Overview

Use Dune for SQL-first aggregate onchain analysis, cross-chain datasets, dashboards, query APIs, and productionized analytics workflows.

## Workflow

1. Define the metric and grain before writing SQL: chain, protocol, event/table, token units, USD pricing, time bucket, and dedupe logic.
2. Search the Data Catalog and existing query patterns before inventing table names.
3. Prefer curated spellbook/data catalog tables when they match the metric; use raw decoded/event tables when auditability or exact contract logic matters.
4. Use parameters for addresses, chain names, token lists, and date windows.
5. For automation, choose between saved query execution, raw SQL execution, latest results, CSV export, materialized views, pipelines, uploads, webhooks, dbt, or Trino.
6. Cross-check important address-level details with Etherscan and attribution with Arkham.

## Common Tasks

- Analytics: write SQL, inspect datasets, build dashboards, share/embed results.
- Data API: execute saved queries or raw SQL, poll status, retrieve JSON/CSV, filter/sort/sample/paginate results.
- Data engineering: materialized views, query pipelines, uploaded tables, dbt connector, SQL operations, CI/CD.
- BI and notebooks: Trino connector, Hex, Metabase, DBeaver, SDKs.
- Product/API surfaces: Sim realtime APIs, Datashare, Catalyst, Dune MCP, CLI and agent skills.

## References

- Read `references/docs-map.md` for official docs coverage and product/API map.
- Read `references/workflows.md` for Dune analysis and automation recipes.
