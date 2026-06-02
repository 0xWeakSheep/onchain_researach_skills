# onchain_researach_skills

Codex skill pack for onchain analysis charts: route data sources, shape analysis outputs, and turn results into auditable visualizations.

## Demo Video

[Usage process demo](public/onchain-skills-usage-demo.mp4)

## Main Flow

1. Use `onchain-planner` as the entry skill for multi-step analysis, charting, dashboard, notebook, or report work.
2. Create or reuse a run directory under `out/runs/<run_id>/` and write `specs/skill-plan.md` when the workflow has multiple steps.
3. Use `onchain-analysis` to choose the right data source, metric definition, validation plan, and platform skill.
4. Use the platform skill only when platform-specific details are needed.
5. Use `onchain-charting` before producing any chart, dashboard, diagram, or report figure.
6. Use `chart-visualization` only when a hosted AntV chart image is appropriate and the data is safe to send to its online API.
7. Store every artifact in the active `out/runs/<run_id>/` directory and update `manifest.json`.
8. Use `onchain-finalizer` before delivery to verify artifact location convergence.

## Skill Flow

| Step | Use Skill | Output Location |
|---|---|---|
| Plan workflow and skill sequence | `onchain-planner` | `out/runs/<run_id>/specs/skill-plan.md`, `out/runs/<run_id>/run.md` |
| Define scope and source | `onchain-analysis` | `out/runs/<run_id>/run.md`, `out/runs/<run_id>/specs/` |
| Platform-specific plan or collection | Arkham, Etherscan, Dune, Hex, Observable, Deepnote, or Binance Web3 data skill | `out/runs/<run_id>/data/`, `out/runs/<run_id>/logs/` |
| Chart planning and data shaping | `onchain-charting` | `out/runs/<run_id>/specs/`, `out/runs/<run_id>/summaries/` |
| Render chart image or diagram | `chart-visualization`, Mermaid/FigJam, notebook, spreadsheet, or frontend chart library | `out/runs/<run_id>/charts/` |
| Final narrative or report | `onchain-analysis` plus `onchain-charting` QA | `out/runs/<run_id>/reports/` |
| Finalize artifact location | `onchain-finalizer` | `out/runs/<run_id>/logs/output-location-check.txt`, `out/runs/<run_id>/manifest.json` |

## Skills

| Skill | Role |
|---|---|
| `onchain-planner` | Entry planner that chooses skill sequence, run directory, expected artifacts, and validation gates. |
| `onchain-analysis` | Main onchain analysis router for wallet, token, protocol, flow, and dashboard tasks. |
| `onchain-charting` | Chart selection, data shaping, tool routing, and visual QA. |
| `onchain-finalizer` | Ending convergence check for artifact placement, manifest paths, and delivery output paths. |
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

## Output Contract

All generated files must go under `out/`. See `out/README.md` for directory layout, naming rules, required `manifest.json`, and run documentation standards.

## Git Practice

Changes are committed and pushed in small batches. Avoid single oversized commits.
