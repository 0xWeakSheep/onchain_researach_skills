# Etherscan Official Docs Map

Sources:

- Introduction: https://docs.etherscan.io/introduction
- Documentation index: https://docs.etherscan.io/llms.txt
- Getting started: https://docs.etherscan.io/getting-started.md
- Supported chains: https://docs.etherscan.io/supported-chains.md
- Rate limits: https://docs.etherscan.io/resources/rate-limits.md
- V2 migration: https://docs.etherscan.io/v2-migration.md

## V2 Basics

- Base path: `https://api.etherscan.io/v2/api`
- Required auth parameter: `apikey`
- Required multichain selector: `chainid`
- Ethereum mainnet: `chainid=1`
- Polygon mainnet example: `chainid=137`
- API V2 uses one Etherscan account/API key across supported chains.
- Legacy V1 endpoints were deprecated on August 15, 2025; migrate V1 and explorer-specific URLs to the V2 base path plus `chainid`.

## Supported Chains

The docs list 60+ supported networks. Common chain IDs:

- Ethereum Mainnet: `1`
- Sepolia: `11155111`
- BNB Smart Chain: `56`
- Polygon: `137`
- Base: `8453`
- Arbitrum One: `42161`
- OP Mainnet: `10`
- Avalanche C-Chain: `43114`
- Gnosis: `100`
- Mantle: `5000`
- Sonic: `146`
- Unichain: `130`
- Berachain: `80094`
- Monad: `143`
- HyperEVM: `999`
- Plasma: `9745`

Use the Supported Chains page or the `chainlist` endpoint before hardcoding less-common chain IDs.

## Rate Limits

- Free: 3 calls/second, up to 100,000 calls/day, selected chains only.
- Lite: 5 calls/second, up to 100,000 calls/day.
- Standard: 10 calls/second, up to 200,000 calls/day.
- Advanced: 20 calls/second, up to 500,000 calls/day.
- Professional: 30 calls/second, up to 1,000,000 calls/day.
- Pro Plus: 30 calls/second, up to 1,500,000 calls/day.

Some high-volume list endpoints have tier-specific record limits. The docs warn that on July 1, 2026, affected Free tier endpoints will reduce maximum records per request from 10,000 to 1,000.

## Endpoint Groups

### Account

- Native balance: `balance`, `balancemulti`, `balancehistory`.
- Transactions: `txlist`, `txlistinternal`, internal by tx hash or block range.
- Token holdings: address ERC20, ERC721 holdings, NFT inventory.
- Token transfers: `tokentx`, `tokennfttx`, `token1155tx`.
- Address origin and labels: `fundedby`, address metadata/name tag.

### Blocks and Stats

- Block countdown, block by timestamp, block/uncle rewards.
- Daily stats: block count/rewards, average block size/time/gas limit/gas price, gas used, utilization, tx count, tx fees, new addresses, hash rate, difficulty, node count, chain size.

### Contracts

- `getabi`
- `getsourcecode`
- `getcontractcreation`
- contract execution status and receipt status.

### Contract Verification

- Verify Solidity, Vyper, Stylus, zkSync source code.
- Verify proxy contracts.
- Check source code/proxy verification status.
- Foundry, Hardhat, and Remix verification guides use the same Etherscan key under V2.

### Gas Tracker

- Gas oracle.
- Gas estimate / confirmation time.
- `eth_gasPrice` through proxy methods.

### Geth/Parity Proxy

- `eth_blockNumber`
- `eth_call`
- `eth_estimateGas`
- `eth_getBlockByNumber`
- `eth_getBlockTransactionCountByNumber`
- `eth_getCode`
- `eth_getStorageAt`
- `eth_getTransactionByHash`
- `eth_getTransactionCount`
- `eth_getTransactionReceipt`
- `eth_sendRawTransaction`

### Logs

- Logs by address.
- Logs by topics.
- Logs by address and topics.
- Always record address, topics, `fromBlock`, `toBlock`, page, offset, and sort direction.

### Tokens

- Token balance and historical token balance.
- Token supply and historical token supply.
- Token holder count/list/top holders.
- Token info.
- ERC20, ERC721, ERC1155 transfer history.

### L2 Deposits/Withdrawals, Nametags, Usage

- Deposit transactions by address.
- Withdrawal transactions by address.
- Plasma deposits.
- Beacon withdrawals.
- Label master list and address tag export.
- API usage endpoint.

### AI and Resources

- Etherscan MCP page for AI-agent workflows.
- Common error messages, best practices, PRO endpoints, changelog, contact/support.

## Response Handling

- Treat `status`, `message`, and `result` together; do not assume HTTP 200 means successful data.
- Preserve endpoint URL and parameters for reproducibility.
- Convert token amounts with `tokenDecimal` when present.
- Use `timeStamp` fields as Unix timestamps unless endpoint docs state otherwise.
