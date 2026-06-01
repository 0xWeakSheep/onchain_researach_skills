---
name: etherscan-api
description: Etherscan API V2 workflow guide. Use when Codex needs Etherscan guidance for EVM account balances, normal/internal transactions, ERC20/ERC721/ERC1155 transfers, token holdings, top holders, blocks, gas, Geth/Parity proxy methods, logs and event topics, contract ABI/source/creator/verification, stats, chain IDs, nametags, API usage, rate limits, V2 migration, MCP, or explorer-backed validation.
---

# Etherscan API

## Overview

Use Etherscan for raw, explorer-backed EVM data and contract metadata. Prefer it when the task needs auditable transactions, logs, token transfers, source code, ABI, chain IDs, or verification state.

## Workflow

1. Confirm chain and `chainid`; API V2 uses one account/API key across supported chains.
2. Identify the module: account, token, logs, contract, transaction, block, gas, stats, proxy, L2 deposits/withdrawals, nametags, or usage.
3. Use block ranges and pagination for any list endpoint; avoid assuming explorer UI totals equal API totals.
4. Decode logs with ABI/topic context when event semantics matter.
5. Cross-check attribution and labels with Arkham when identity matters; use Dune when aggregate SQL is more efficient.
6. Preserve endpoint, parameters, chain ID, block range, page/offset, sort direction, and response status in the method.

## Common Tasks

- Wallet audit: native balance, token balances, normal/internal transactions, ERC transfers, funded-by, nametag.
- Token analysis: token info, total supply, holder count/list, top holders, transfer history, holder inventory.
- Contract analysis: ABI, source code, creator, creation tx, verification status, proxy verification.
- Event analysis: logs by address, topics, or address+topics; pair with ABI and known event signatures.
- Network analysis: daily stats, gas oracle, block by timestamp, block rewards, node count, chainlist.

## References

- Read `references/docs-map.md` for official docs coverage and endpoint groups.
- Read `references/workflows.md` for common EVM explorer recipes.
