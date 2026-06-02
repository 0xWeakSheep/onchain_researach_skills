# Arkham Workflows

## Address or Entity Profile

1. Determine whether the input is an address, entity slug, contract, token, or ambiguous search term.
2. Use `GET /intelligence/search` for ambiguity; use address/entity endpoints once identified.
3. Fetch address intelligence or enriched address intelligence. Use all-chain variants when chain is uncertain.
4. Add balances, portfolio history, and counterparties if the user asks for behavior or exposure.
5. State label/entity attribution caveats and cross-check critical facts with Etherscan or Dune.

## Transfer and Flow Analysis

Use `GET /transfers` when the question is row-level movement. Record:

- `base`
- `chains`
- `flow`
- `from`
- `to`
- `counterparties`
- `tokens`
- `timeGte`, `timeLte`, or `timeLast`
- `valueGte`, `valueLte`, `usdGte`, `usdLte`
- `sortKey`, `sortDir`
- `limit`, `offset`

Use `GET /flow/address/{address}` or `GET /flow/entity/{entity}` for historical USD flow summaries. Use histograms for chart-ready transfer distribution.

## Counterparty Map

1. Fetch address/entity intelligence.
2. Fetch top counterparties for the same subject.
3. Pull transfers for the largest counterparties and time window.
4. Bucket counterparties by Arkham entity type or tag when available.
5. Chart ranked counterparties as bars; keep an audit table for largest transfers.

## Holdings and Exposure

1. Fetch balances for address/entity.
2. Use portfolio history or time series if the user asks for trend, not just current exposure.
3. Use loans endpoints for borrow/lending exposure.
4. For token-specific exposure, fetch token balance and market data.
5. State whether values are token units, USD, current price, or historical price.

## Hyperliquid / HyperCore Position Analysis

1. Treat Hyperliquid user wording as HyperCore in Arkham references. Do not report "no related skill" just because there is no Hyperliquid-named skill directory.
2. Resolve the subject as address, entity, or account scope before querying. Record whether the user wants current positions, account summary, spot balances, trades, funding, liquidation risk, or a chart/report.
3. Use the HyperCore endpoint group from `references/docs-map.md` for perp positions, spot balances, account summary, and trades. Re-read the endpoint-specific official Markdown before writing production request parameters or code.
4. Preserve market, side, size, notional, margin currency, leverage, liquidation price, unrealized PnL, realized PnL, funding, timestamp, and trade identifiers when available.
5. For chart work, hand the shaped data to `onchain-charting`; common outputs are position notional by market, PnL over time, funding paid/received, exposure by side, and liquidation-risk tables.
6. If the user explicitly asks for direct official Hyperliquid API integration, state that this repository currently has no dedicated direct Hyperliquid skill and propose adding one instead of pretending Arkham is the official API.

## Token or Market Review

1. Resolve token by ID or chain/address.
2. Fetch token intelligence, market data, holders, volume, top flow, price history, and trending context as needed.
3. Use Dune if the requested token analysis needs custom cohort logic or long historical aggregation.
4. Use Etherscan for contract source/ABI, supply, and transfer spot checks.

## Alerts and Monitoring

Use user alert endpoints for user-owned alert workflows only. Do not create, update, or delete alerts without explicit user instruction. For planning, specify alert subject, chain, flow direction, token, value threshold, and delivery surface.

## Coding-Agent Safety

- Never hardcode API keys.
- Prefer request examples with placeholder keys.
- Mention credit, rate limit, pagination, and timestamp assumptions in every reusable workflow.
- For large extraction, use time-window paging and persist checkpoint timestamps.
- Re-read the endpoint-specific official Markdown before producing production code.
