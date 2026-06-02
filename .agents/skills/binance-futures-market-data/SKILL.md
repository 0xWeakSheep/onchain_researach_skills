---
name: binance-futures-market-data
description: |
  Binance futures market-data workflow guide for chart-ready USDS-M and COIN-M perpetual and delivery contracts.
  Use when users ask for Binance Futures data for analysis or charts: futures klines, continuous contract klines,
  mark/index/premium price, funding rates, funding info, open interest, open interest statistics, basis,
  long/short ratios, top trader ratios, taker buy/sell volume, order book/trades, 24h ticker stats,
  quarterly settlement price, ADL risk, real-time market-wide liquidation subscriptions, or user force-order/liquidation history when authenticated user data is explicitly requested.
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
- Liquidation wording: distinguish real-time market-wide liquidation streams from authenticated user force-order history. The currently reliable Binance route for market-wide liquidations is WebSocket subscription from the time of connection forward; do not claim Binance can backfill prior market-wide liquidation history through HTTPS.

## Liquidation Data Limits

- Market-wide liquidations: use Binance Futures WebSocket force-order streams, such as `wss://fstream.binance.com/ws/btcusdt@forceOrder` for USDS-M `BTCUSDT`. These streams only deliver events after the subscription is active and cannot query past hours or days.
- Historical market-wide liquidations: do not use Binance HTTPS as a dependable source for past market-wide liquidation data. The previously known `GET /fapi/v1/allForceOrders` route may appear in old references, but it has returned `{"code":400,"msg":"The endpoint has been out of maintenance"}` in current checks. Treat it as unavailable unless Binance official docs and a live request prove otherwise.
- User force orders: authenticated HTTPS force-order endpoints are for the requesting account's own liquidation or ADL records. They are not market-wide liquidation volume and must not be used to answer requests like "BTCUSDT market liquidation volume over the last 24 hours."
- Backfill requirement: if a user asks for past market-wide liquidation volume, use a third-party historical aggregation provider with credentials, or explain that Binance WebSocket collection must start now and accumulate future data.
- Direction mapping for force-order events: `SELL` usually means a long position was force-sold, so label it as long liquidation; `BUY` usually means a short position was force-bought, so label it as short liquidation. Keep this mapping explicit in charts and summaries.

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
| Real-time market-wide liquidations | WebSocket force-order stream only; subscription starts now and has no historical backfill |
| Historical market-wide liquidation volume | Not available from dependable Binance HTTPS in this skill; use a third-party historical provider if credentials are supplied |
| User liquidation history | user's force orders only; auth required |

## Safety And Scope

- Never place, modify, cancel, or test orders from this skill.
- Never request or store API secrets in repository files, generated outputs, or prompts.
- State whether a dataset is public market data or authenticated account/user data.
- For production code or endpoint parameters, re-check Binance official docs or the source Binance Skills Hub reference because futures API fields can change.

## References

- Read `references/futures-market-data.md` for endpoint families and chart metric mapping.
