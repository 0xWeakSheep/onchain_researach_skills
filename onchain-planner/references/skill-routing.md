# Skill Routing

Use this file to choose the next skills after `onchain-planner`.

## Default Sequence

```text
onchain-planner
  -> onchain-analysis
  -> platform or data skill
  -> onchain-charting
  -> renderer or delivery surface
  -> onchain-finalizer
```

Skip steps that are not needed by the user request.

## Decision Matrix

| User intent | Skill sequence | Main artifacts |
|---|---|---|
| Decide how to approach an onchain task | `onchain-planner` | `specs/skill-plan.md`, `run.md` |
| Analyze a wallet, token, protocol, bridge, or entity | `onchain-planner` -> `onchain-analysis` -> platform skill -> `onchain-finalizer` | `specs/`, `data/`, `summaries/`, `logs/` |
| Raw EVM transaction, log, ABI, contract, or token-transfer evidence | `onchain-planner` -> `onchain-analysis` -> `etherscan-api` -> `onchain-finalizer` | `data/`, `logs/` |
| Entity attribution, counterparty, portfolio, transfer path, or labeled flow | `onchain-planner` -> `onchain-analysis` -> `arkham-intelligence-api` -> `onchain-finalizer` | `data/`, `summaries/`, `logs/` |
| Hyperliquid or HyperCore perp positions, spot balances, account summary, margin exposure, funding, liquidation risk, or trades | `onchain-planner` -> `onchain-analysis` -> `arkham-intelligence-api` -> optional `onchain-charting` -> `onchain-finalizer` | `data/`, `summaries/`, optional `charts/`, `logs/` |
| Binance USDS-M or COIN-M perpetual/delivery futures chart data: funding, OI, basis, long/short ratio, taker volume, futures klines, mark/index/premium, user force orders | `onchain-planner` -> `onchain-analysis` -> `binance-futures-market-data` -> `onchain-charting` -> `onchain-finalizer` | `data/`, `summaries/`, `charts/`, `logs/` |
| SQL aggregate, cross-chain metric, query API, or dashboard dataset | `onchain-planner` -> `onchain-analysis` -> `dune-analytics` -> `onchain-finalizer` | `specs/`, `data/`, `logs/` |
| Collaborative notebook or stakeholder app/report | `onchain-planner` -> `onchain-analysis` -> `hex-analytics` or `deepnote-notebooks` -> `onchain-finalizer` | `specs/`, `reports/`, `logs/` |
| Web-native interactive notebook or public/private embed | `onchain-planner` -> `onchain-analysis` -> `observable-notebooks` -> `onchain-finalizer` | `specs/`, `charts/`, `reports/`, `logs/` |
| Token market data, K-line, ranking, meme, audit, address holdings, or signal data | `onchain-planner` -> `onchain-analysis` -> Binance Web3 data skill -> `onchain-finalizer` | `data/`, `summaries/`, `logs/` |
| Chart, dashboard figure, Sankey, network graph, report visual, or diagram | `onchain-planner` -> `onchain-charting` -> `onchain-finalizer` | `specs/`, `charts/`, `summaries/`, `logs/` |
| Hosted AntV chart image from safe chart-ready data | `onchain-planner` -> `onchain-charting` -> `chart-visualization` -> `onchain-finalizer` | `specs/`, `charts/`, `logs/` |
| Final written report | `onchain-planner` -> `onchain-analysis` -> `onchain-charting` -> `onchain-finalizer` | `reports/`, `charts/`, `summaries/`, `logs/` |

## Selection Heuristics

- Prefer `onchain-analysis` when the metric, source, entity scope, or validation method is unclear.
- Prefer `onchain-charting` when data is already chart-ready or the user asks mainly for visualization.
- Prefer platform skills only for platform-specific API, SQL, notebook, dashboard, or data semantics.
- Prefer local rendering over hosted chart APIs for private investigation data.
- Prefer SQL warehouses for aggregates and raw explorers for transaction-level proof.
- Prefer notebooks for exploratory or reusable work; prefer static charts for report-ready deliverables.
- Route Binance Futures / USDS-M / COIN-M / delivery contract chart-data questions to `binance-futures-market-data`; do not route these to Binance Web3 token skills.
- Treat Hyperliquid, HyperCore, HL perp, perp positions, margin, leverage, funding, liquidation price, and account summary as Arkham-routable unless the user asks for direct official Hyperliquid API code.
- If a named platform does not have a dedicated skill, do not stop at "unsupported"; first check whether an installed platform skill covers the same data through an alias or integrated endpoint family.
- Use `onchain-finalizer` as the final step when any file is created or delivered.
