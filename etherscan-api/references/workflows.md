# Etherscan Workflows

## Wallet Audit

1. Confirm chain and `chainid`.
2. Fetch native balance and token balances.
3. Fetch normal transactions, internal transactions, ERC20 transfers, ERC721 transfers, and ERC1155 transfers as needed.
4. Use `fundedby` for initial funding origin if the subject is an EOA.
5. Add nametag/metadata when the identity matters.
6. Normalize token values with decimals and keep hashes for auditability.

## ERC20 Transfer Extraction

Use the token transfer endpoint when the user asks for stablecoin movement, inflow/outflow, token activity, or wallet transfer history.

Required or common parameters:

- `apikey`
- `chainid`
- `module=account`
- `action=tokentx`
- `contractaddress`
- `address`
- `startblock`
- `endblock`
- `page`
- `offset`
- `sort`

For large windows, page deterministically and store the last seen block/hash. For Free tier work after July 1, 2026, assume lower max records per request unless the docs and plan prove otherwise.

## Contract and Event Investigation

1. Fetch contract creator and creation tx.
2. Fetch ABI and source code.
3. If source/ABI is unavailable, use method IDs/topics and bytecode cautiously.
4. Query event logs by address and topics over bounded block ranges.
5. Decode events with ABI and verify sample transactions in the explorer UI when precision matters.

## Token Holder Review

1. Fetch token info and total supply.
2. Fetch holder count, holder list, or top holders depending on plan availability.
3. Flag contracts, bridges, exchanges, burns, and team wallets if known.
4. Cross-check label-heavy interpretation with Arkham and aggregate trends with Dune.

## Chain or Network Stats

Use stats/block endpoints for daily macro series such as tx count, gas used, gas price, new addresses, fees, utilization, hash rate, difficulty, block count, or node count. Prefer Dune when the user needs custom grouping, protocol filters, or multi-series charts beyond the official endpoint output.

## Common Failure Checks

- Wrong `chainid`.
- Missing or invalid `apikey`.
- Deprecated V1 base path.
- Empty result caused by block bounds or contract filter.
- `status=0` with a useful error in `message` or `result`.
- Pagination truncation from `offset`, tier limit, or unsupported plan.
- Token amounts not divided by `tokenDecimal`.
