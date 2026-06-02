---
name: binance-futures-market-data
description: |
  Binance futures market-data workflow guide for chart-ready USDS-M and COIN-M perpetual and delivery contracts.
  Use when users ask for Binance Futures data for analysis or charts: futures klines, continuous contract klines,
  mark/index/premium price, funding rates, funding info, open interest, open interest statistics, basis,
  long/short ratios, top trader ratios, taker buy/sell volume, order book/trades, 24h ticker stats,
  quarterly settlement price, ADL risk, or user force-order/liquidation history when authenticated user data is explicitly requested.
  NOT for placing, modifying, or canceling futures orders; payments; P2P; wallet operations; or spot/token Web3 data.
metadata:
  author: project-derived-from-binance-skills-hub
  source: binance/binance-skills-hub
  sourceCommit: ea2ae15308497b42e0b346c3945d4ca8914790d8
  sourcePaths:
    - skills/binance/binance/references/futures-usds.md
    - skills/binance/binance/references/futures-coin.md
---

# Binance Futures Market Data

## Overview

Use this skill for read-only Binance Futures datasets that feed charting or derivatives market analysis. Keep it scoped to data retrieval and planning; do not use it to trade or manage accounts.

## Product Routing

- USDS-M futures: use for USDT-M/USDC-M perpetual and delivery-style futures datasets.
- COIN-M futures: use for coin-margined perpetual and quarterly delivery contracts.
- Delivery/quarterly contracts: prefer continuous contract klines, basis, quarterly settlement price, open interest statistics, and contract-type filters.
- Liquidation wording: distinguish market-wide liquidation data from authenticated user force-order history. This Binance Skills Hub snapshot lists user's force-order endpoints, not a public market-wide liquidation feed.

## Workflow

1. Identify the product family: USDS-M or COIN-M.
2. Define chart metric, symbol or pair, contract type, interval or period, and UTC timestamp bounds.
3. Read `references/futures-market-data.md` for endpoint selection and parameter conventions.
4. Collect data with read-only market-data endpoints whenever possible. The endpoint names come from Binance Skills Hub `futures-usds` and `futures-coin` references; verify current CLI or official API syntax before execution.
5. If the user asks for their own force orders, account positions, income, or balance history, mark it as authenticated user data and do not proceed without explicit authorization and credential handling.
6. Shape output for `onchain-charting`: keep timestamps in UTC milliseconds, preserve symbol/pair/contractType, and retain raw response rows for audit.
7. Store data, summaries, charts, and logs under `out/runs/<run_id>/` and run `onchain-finalizer` before delivery.

## Common Chart Routes

| User asks for | Use data family |
|---|---|
| Futures price or volume trend | kline/candlestick or continuous contract kline |
| Mark/index/premium divergence | mark price kline, index price kline, premium index kline |
| Funding rate chart | funding rate history and funding rate info |
| Open interest trend | open interest and open interest statistics |
| Basis or delivery premium | basis and quarterly settlement price |
| Long/short sentiment | long/short ratio and top trader long/short ratios |
| Aggressive buy/sell pressure | taker buy/sell volume |
| Order-book depth or microstructure | order book, recent trades, aggregate trades |
| User liquidation history | user's force orders only; auth required |

## Safety And Scope

- Never place, modify, cancel, or test orders from this skill.
- Never request or store API secrets in repository files, generated outputs, or prompts.
- State whether a dataset is public market data or authenticated account/user data.
- For production code or endpoint parameters, re-check Binance official docs or the source Binance Skills Hub reference because futures API fields can change.

## References

- Read `references/futures-market-data.md` for endpoint families and chart metric mapping.
