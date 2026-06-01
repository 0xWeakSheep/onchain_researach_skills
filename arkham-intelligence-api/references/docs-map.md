# Arkham Official Docs Map

Sources:

- Main API docs: https://intel.arkm.com/api/docs
- LLM index: https://intel.arkm.com/llms.txt
- Full docs: https://intel.arkm.com/llms-full.txt
- OpenAPI spec: https://intel.arkm.com/openapi.json
- Endpoint docs pattern: `https://intel.arkm.com/llms/<method-path>.md`
- Base URL: `https://api.arkm.com`

## Guide Coverage

- Introduction: overview, design principles, intended users.
- Getting started: API access, key creation, authentication.
- Data model: addresses, entities, labels, tags, wallet labeling.
- Usage: rate limits, credit pricing, pagination, timestamps, sorting.
- Troubleshooting: errors, HTTP codes, security practices.
- Resources: cookbook, starter kits, coding-agent guidance, support.

## Authentication

- Send every request with `API-Key: <YOUR_API_KEY>`.
- Store keys in a password manager or secret manager; never paste keys into skill files, notebooks, commits, or examples.
- Use separate keys per environment and service.
- Rotate keys by creating a new key, deploying it, confirming success, then revoking the old key.
- Use REST for historical/batch/enrichment work; use WebSocket for low-latency streaming.

## Pagination and Query Safety

- Arkham uses offset-based pagination with `limit` and `offset`.
- `/transfers` default is 20; 50-500 is recommended for bulk iteration.
- `/swaps` default is 50; 50-500 is recommended.
- `/counterparties/*` defaults to 1000 and has a hard max of 1000.
- `/tokens` defaults to 100 and maxes at 250.
- `/tag/{id}/params` defaults to 100 and maxes at 1000.
- Prefer time-window paging for changing datasets to avoid duplicate or missed records.
- Track credit cost, response size, sorting, and timestamp bounds for all bulk jobs.

## Endpoint Groups

### Account and Usage Analytics

- `GET /analytics/credit-periods`
- `GET /analytics/endpoint-calls`
- `GET /subscription/intel-usage`

### Chains, Networks, and Supply

- `GET /chains`
- `GET /networks/status`
- `GET /networks/history/{chain}`
- `GET /arkm/circulating`

### Address and Entity Intelligence

- `GET /intelligence/address/{address}`
- `GET /intelligence/address/{address}/all`
- `POST /intelligence/address/batch`
- `POST /intelligence/address/batch/all`
- `GET /intelligence/address_enriched/{address}`
- `GET /intelligence/address_enriched/{address}/all`
- `POST /intelligence/address_enriched/batch`
- `POST /intelligence/address_enriched/batch/all`
- `GET /intelligence/entity/{entity}`
- `GET /intelligence/entity/{entity}/summary`
- `GET /intelligence/entity_predictions/{entity}`
- `GET /intelligence/entity_types`
- `GET /intelligence/search`
- `GET /intelligence/contract/{chain}/{address}`
- `GET /intelligence/token/{chain}/{address}`
- `GET /intelligence/token/{id}`

### Intelligence Updates

- `GET /intelligence/addresses/updates`
- `GET /intelligence/address_tags/updates`
- `GET /intelligence/entities/updates`
- `GET /intelligence/tags/updates`
- `GET /intelligence/entity_balance_changes`

### Holdings, Balances, Portfolios, and Loans

- `GET /balances/address/{address}`
- `GET /balances/entity/{entity}`
- `GET /balances/solana/subaccounts/address/{addresses}`
- `GET /balances/solana/subaccounts/entity/{entities}`
- `GET /portfolio/address/{address}`
- `GET /portfolio/entity/{entity}`
- `GET /portfolio/timeSeries/address/{address}`
- `GET /portfolio/timeSeries/entity/{entity}`
- `GET /history/address/{address}`
- `GET /history/entity/{entity}`
- `GET /loans/address/{address}`
- `GET /loans/entity/{entity}`

### Transfers, Flows, Counterparties, Swaps, and Transactions

- `GET /transfers`
- `GET /transfers/unenriched`
- `GET /transfers/histogram`
- `GET /transfers/histogram/simple`
- `GET /transfers/tx/{hash}`
- `GET /tx/{hash}`
- `GET /flow/address/{address}`
- `GET /flow/entity/{entity}`
- `GET /volume/address/{address}`
- `GET /volume/entity/{entity}`
- `GET /counterparties/address/{address}`
- `GET /counterparties/entity/{entity}`
- `GET /swaps`

### Token and Market Data

- `GET /token/addresses/{id}`
- `GET /token/balance/{id}`
- `GET /token/balance/{chain}/{address}`
- `GET /token/holders/{id}`
- `GET /token/holders/{chain}/{address}`
- `GET /token/market/{id}`
- `GET /token/price/history/{id}`
- `GET /token/price/history/{chain}/{address}`
- `GET /token/price_change/{id}`
- `GET /token/top`
- `GET /token/top_flow/{id}`
- `GET /token/top_flow/{chain}/{address}`
- `GET /token/trending`
- `GET /token/trending/{id}`
- `GET /token/volume/{id}`
- `GET /token/volume/{chain}/{address}`
- `GET /marketdata/altcoin_index`

### Tags, Clusters, Alerts, and User Data

- `GET /tag/{id}/params`
- `GET /tag/{id}/summary`
- `GET /cluster/{id}/summary`
- `GET /user/alerts`, `POST /user/alerts`, `GET /user/alerts/{id}`, `PUT /user/alerts/{id}`, `DELETE /user/alerts/{id}`
- `GET /user/entities`, `GET /user/entities/{id}`, `PUT /user/entities/only_add/{id}`
- `GET /user/labels`, `POST /user/labels`

### HyperCore, Polymarket, and WebSockets

- HyperCore: perp positions, spot balances, account summary, trades.
- Polymarket: activity, events, event positions, order book, wallet positions, PnL, prices, stats, top events, top holders, leaderboard.
- WebSocket admin/streaming: active connections, session info, sessions, transfer streaming. Prefer current WebSocket docs when building new streaming work because some v1 WebSocket session endpoints are deprecated.

## Search Patterns

- Use the LLM index to find endpoint docs: `curl https://intel.arkm.com/llms.txt`.
- For endpoint detail, open the specific Markdown page before writing request parameters.
- For response fields, open the linked schema under `https://intel.arkm.com/llms/schemas/`.
