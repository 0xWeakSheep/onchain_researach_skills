# Platform Selection

Use this file when a request could be solved by multiple onchain platforms.

## Source Roles

- Arkham: entity-first intelligence, labels, attribution, entity/address portfolios, counterparties, transfers, alerts, and confidence-aware investigation.
- Etherscan: raw EVM explorer evidence, address transactions, token transfers, logs/topics, ABI/source, contract creation, gas, block stats, chain IDs, and verification.
- Dune: SQL over indexed onchain datasets, cross-chain aggregates, dashboards, Data API, materialized views, pipelines, uploads, dbt, Trino, and BI/notebook connections.
- Hex: collaborative SQL/Python notebook and stakeholder app/report surface, especially for internal analysis and Dune Trino workflows.
- Observable: reactive JavaScript notebooks, interactive charts, public/private embeds, Plot/D3, and lightweight web-native data storytelling.
- Deepnote: AI-assisted SQL/Python notebooks, scheduled notebooks, API-triggered runs, Streamlit/data apps, and team data science workflows.

## Default Routing

- Wallet identity or counterparty question: Arkham first, Etherscan for raw transaction evidence, Dune if aggregation is needed.
- Contract or event question: Etherscan first for ABI/source/logs, Dune for large-scale aggregation, Arkham for labeled counterparties.
- Protocol metric question: Dune first, Etherscan for spot checks, Arkham for entity labels.
- Dashboard/report question: Dune for data and query execution; Hex, Observable, or Deepnote for the delivery surface.
- Automation question: Dune Data API for query execution/results; Deepnote API or schedules for notebook runs; Hex schedules for internal apps; Arkham/Etherscan APIs for direct lookups.

## Validation Rules

- Always record chain, address/entity/token, timeframe, block or timestamp bounds, and unit conventions.
- Cross-check important balances or transfer totals with another platform before treating them as final.
- Treat labels, name tags, and entity attributions as evidence with confidence and source caveats.
- Prefer raw explorer/API evidence for transaction-level claims and SQL datasets for aggregate claims.
- If a platform feature or endpoint can change, consult the official docs before writing implementation details.
