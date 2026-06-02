# onchain_researach_skills

Codex skill pack for onchain analysis charts: route data sources, shape analysis outputs, and turn results into auditable visualizations.

## Main Flow

1. Use `onchain-analysis` to choose the right data source or analysis surface.
2. Use the platform skill only when the task needs platform-specific details.
3. Use `onchain-charting` before producing any chart, dashboard, diagram, or report figure.
4. Use `chart-visualization` only when a hosted AntV chart image is appropriate and the data is safe to send to its online API.

## Skills

| Skill | Role |
|---|---|
| `onchain-analysis` | Main onchain analysis router for wallet, token, protocol, flow, and dashboard tasks. |
| `onchain-charting` | Chart selection, data shaping, tool routing, and visual QA. |
| `arkham-intelligence-api` | Arkham entity, address, flow, portfolio, transfer, token, and alert workflows. |
| `etherscan-api` | Etherscan API V2 for EVM addresses, contracts, logs, token transfers, stats, gas, and verification. |
| `dune-analytics` | Dune SQL, Data API, catalog, materialized views, uploads, pipelines, and dashboards. |
| `hex-analytics` | Hex SQL/Python notebooks, chart cells, data apps, integrations, and shared reports. |
| `observable-notebooks` | Observable notebooks, Plot, Inputs, SQL/data cells, sharing, and embeds. |
| `deepnote-notebooks` | Deepnote SQL/Python notebooks, chart blocks, integrations, schedules, APIs, and apps. |

## Project Installed Skills

- `chart-visualization`: Installed from `antvis/chart-visualization-skills@chart-visualization`.
  It generates chart images through the AntV online visualization API, so redact sensitive data before using it on private investigations.
- Binance Web3 market data skills from `binance/binance-skills-hub`: `binance-tokenized-securities-info`, `crypto-market-rank`, `meme-rush`, `query-address-info`, `query-token-audit`, `query-token-info`, `trading-signal`.
  These are kept only as market, token, address, audit, and signal data sources for chart workflows.

## Scope

Keep skills that help with onchain analysis data, chart planning, chart rendering, and report/dashboard figures.
Do not add broad trading, wallet operation, payment, posting, fiat/P2P, or CEX account-management skills unless they are explicitly needed for a chart workflow.

## Git Practice

Changes are committed and pushed in small batches. Avoid single oversized commits.
