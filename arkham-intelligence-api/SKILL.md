---
name: arkham-intelligence-api
description: Arkham Intel API workflow guide. Use when Codex needs Arkham API guidance for address or entity intelligence, labels, tags, attribution confidence, token balances, portfolios, transfers, flows, counterparties, market data, Polymarket, alerts, private entities, WebSocket sessions, credit usage, rate limits, pagination, authentication, errors, or coding-agent use of Arkham docs.
---

# Arkham Intelligence API

## Overview

Use Arkham when analysis depends on entity-first intelligence, labels, attribution, enriched transfers, counterparty context, and portfolio/flow views that raw explorer data does not provide.

## Workflow

1. Identify whether the subject is an address, entity, contract, token, tag, cluster, or transaction.
2. Check `references/docs-map.md` for the relevant guide or endpoint group.
3. Prefer enriched intelligence endpoints when labels or entity context matter; prefer raw transfer/history endpoints when auditability matters.
4. Track pagination, sorting, timestamps, chain scope, credit cost, and rate limits before recommending bulk work.
5. Treat Arkham labels as probabilistic intelligence; include confidence/caveats when attribution affects the conclusion.
6. Cross-check critical balances, transfers, or contract facts against Etherscan or Dune when possible.

## Common Tasks

- Address/entity intelligence: lookup, enriched lookup, batch lookup, all-chain lookup, updates.
- Money movement: transfers, transfer histograms, transaction transfers, flow, volume, counterparties.
- Holdings: balances, portfolio history, portfolio time series, token balances, loans/borrows.
- Token and market views: token intelligence, holders, prices, market data, trending/top tokens, volume, top flow.
- Operations: auth, pagination, errors, usage analytics, subscription usage, alerts, private entities, user labels.

## References

- Read `references/docs-map.md` for official docs coverage and endpoint groups.
- Read `references/workflows.md` for common onchain analysis recipes.
