---
name: onchain-analysis
description: Cross-platform onchain analysis coordinator. Use when Codex needs to plan, execute, or review wallet, entity, token, protocol, bridge, exchange, flow, dashboard, or reporting work across Arkham, Etherscan, Dune, Hex, Observable, Deepnote, Binance Web3 market data, or similar tools; choose data sources, define metrics, write query/API plans, cross-check results, and hand chart work to onchain-charting.
---

# Onchain Analysis

## Overview

Coordinate onchain analysis across explorer APIs, intelligence APIs, SQL warehouses, and notebook/reporting tools. Keep this skill focused on routing, method design, validation, and output structure; use platform skills for platform-specific syntax and endpoints.

## Routing

- Use `arkham-intelligence-api` for entity attribution, label confidence, wallet/entity portfolios, counterparty maps, flows, transfers, alerts, and intelligence updates.
- Use `etherscan-api` for raw EVM explorer data: address transactions, ERC transfers, logs/topics, contract ABI/source, gas, block stats, chain IDs, and verification status.
- Use `dune-analytics` for SQL over indexed onchain data, dashboards, query APIs, materialized views, uploads, pipelines, dbt, Trino, and cross-chain aggregate metrics.
- Use `hex-analytics` when the requested output is a collaborative SQL/Python notebook, app, report, scheduled run, or stakeholder-facing internal analysis.
- Use `observable-notebooks` when the requested output is a reactive JavaScript notebook, interactive visualization, Plot/D3 chart, public embed, or lightweight web-native exploratory notebook.
- Use `deepnote-notebooks` when the requested output is an AI-assisted SQL/Python notebook, scheduled notebook, API-triggered run, Streamlit app, or team workflow.
- Use Binance Web3 market data project skills only for token search, token market data/K-lines, address holdings, audit signals, tokenized securities, market rankings, meme launch data, and smart-money signal datasets. Do not route wallet operations, payments, posting, fiat/P2P, or order execution through this repository.
- Use `onchain-charting` for chart type selection, data shaping, rendering route, and visual QA whenever the output includes a chart, dashboard, diagram, or report figure.

## Analysis Workflow

1. Create or reuse `out/runs/<run_id>/` and initialize `manifest.json` plus `run.md`.
2. Define the subject: chain(s), address/entity/token/protocol, timeframe, asset scope, and required granularity.
3. Choose source roles: primary data source, secondary validation source, visualization/reporting surface, and any manual explorer check.
4. Define metrics before querying: units, USD conversion source, timestamp convention, block range, inclusion/exclusion rules, and dedupe keys.
5. Collect data with reproducible parameters and preserve query/API URLs, query IDs, endpoint names, or notebook links.
6. Store data, specs, summaries, logs, reports, and chart outputs under the active `out/runs/<run_id>/` directory.
7. Cross-check totals across at least two independent surfaces when the conclusion depends on balances, volumes, labels, or transfers.
8. Output concise findings with method, caveats, and next checks.

## Output Contract

Use this shape unless the user asks for another format:

- Objective
- Scope and assumptions
- Sources used
- Method
- Query/API/notebook plan
- Findings
- Chart plan: delegate details to `onchain-charting`
- Caveats and validation gaps

Keep chart decisions centralized in `onchain-charting`; do not duplicate chart-selection rules in platform skills.

## References

- Read `references/platform-selection.md` when choosing between platforms.
- Read `references/workflow-output.md` when setting up the full run flow and output directory.
- Read `references/report-template.md` when the user asks for a final analysis report.
- Read `references/charting-lite.md` only as a compatibility pointer to `onchain-charting`.
