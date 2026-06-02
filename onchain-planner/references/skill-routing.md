# Skill Routing

Use this file to choose the next skills after `onchain-planner`.

## Default Sequence

```text
onchain-planner
  -> onchain-analysis
  -> platform or data skill
  -> onchain-charting
  -> renderer or delivery surface
```

Skip steps that are not needed by the user request.

## Decision Matrix

| User intent | Skill sequence | Main artifacts |
|---|---|---|
| Decide how to approach an onchain task | `onchain-planner` | `specs/skill-plan.md`, `run.md` |
| Analyze a wallet, token, protocol, bridge, or entity | `onchain-planner` -> `onchain-analysis` -> platform skill | `specs/`, `data/`, `summaries/` |
| Raw EVM transaction, log, ABI, contract, or token-transfer evidence | `onchain-planner` -> `onchain-analysis` -> `etherscan-api` | `data/`, `logs/` |
| Entity attribution, counterparty, portfolio, transfer path, or labeled flow | `onchain-planner` -> `onchain-analysis` -> `arkham-intelligence-api` | `data/`, `summaries/`, `logs/` |
| SQL aggregate, cross-chain metric, query API, or dashboard dataset | `onchain-planner` -> `onchain-analysis` -> `dune-analytics` | `specs/`, `data/`, `logs/` |
| Collaborative notebook or stakeholder app/report | `onchain-planner` -> `onchain-analysis` -> `hex-analytics` or `deepnote-notebooks` | `specs/`, `reports/`, `logs/` |
| Web-native interactive notebook or public/private embed | `onchain-planner` -> `onchain-analysis` -> `observable-notebooks` | `specs/`, `charts/`, `reports/` |
| Token market data, K-line, ranking, meme, audit, address holdings, or signal data | `onchain-planner` -> `onchain-analysis` -> Binance Web3 data skill | `data/`, `summaries/`, `logs/` |
| Chart, dashboard figure, Sankey, network graph, report visual, or diagram | `onchain-planner` -> `onchain-charting` | `specs/`, `charts/`, `summaries/` |
| Hosted AntV chart image from safe chart-ready data | `onchain-planner` -> `onchain-charting` -> `chart-visualization` | `specs/`, `charts/`, `logs/` |
| Final written report | `onchain-planner` -> `onchain-analysis` -> `onchain-charting` | `reports/`, `charts/`, `summaries/` |

## Selection Heuristics

- Prefer `onchain-analysis` when the metric, source, entity scope, or validation method is unclear.
- Prefer `onchain-charting` when data is already chart-ready or the user asks mainly for visualization.
- Prefer platform skills only for platform-specific API, SQL, notebook, dashboard, or data semantics.
- Prefer local rendering over hosted chart APIs for private investigation data.
- Prefer SQL warehouses for aggregates and raw explorers for transaction-level proof.
- Prefer notebooks for exploratory or reusable work; prefer static charts for report-ready deliverables.
