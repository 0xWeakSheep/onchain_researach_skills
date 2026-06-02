# Data Shaping

Prepare chart data before choosing visual polish. Stable columns make charts easier to render across AntV, Plotly, Observable Plot, D3, ECharts, spreadsheets, and notebooks.

## Common Fields

| Field | Meaning |
|---|---|
| `chain` | Chain or network name |
| `block_time` | Timestamp in UTC unless the user asks otherwise |
| `date` | Calendar bucket derived from `block_time` |
| `tx_hash` | Transaction hash for audit tables |
| `address` | Wallet, contract, or entity address |
| `entity` | Resolved label or cluster |
| `token_symbol` | Token symbol |
| `token_address` | Token contract address |
| `amount` | Human-readable token amount |
| `amount_usd` | USD value at the relevant time |
| `source` | Data source or platform |
| `caveat` | Short note about missing labels, price source, sampling, or assumptions |

## Chart Schemas

### Time Series

```json
[
  {"date": "2026-01-01", "metric": "volume_usd", "value": 12345.67, "group": "ETH"}
]
```

Required: `date`, `value`.
Optional: `metric`, `group`, `unit`, `source`.

### Ranked Bar

```json
[
  {"category": "wallet_a", "value": 1200000, "unit": "USD", "rank": 1}
]
```

Sort descending unless the user asks for chronological or alphabetical order. Keep Top-N plus an "other" row when long-tail values matter.

### Sankey Flow

```json
[
  {"source": "CEX", "target": "Bridge", "value": 500000, "unit": "USD"}
]
```

Aggregate by meaningful source and target labels. Keep a separate audit table for raw tx hashes.

### Network Graph

```json
{
  "nodes": [{"id": "0x...", "label": "Wallet A", "group": "cluster_1"}],
  "edges": [{"source": "0x...", "target": "0x...", "value": 10, "label": "transfers"}]
}
```

Cap nodes for readability. Use edge weights only when they represent a defined metric.

### Candlestick

```json
[
  {"time": "2026-01-01", "open": 100, "high": 120, "low": 95, "close": 110, "volume": 5000}
]
```

Required: `time`, `open`, `high`, `low`, `close`. Add volume as a lower panel or bar series.

### Distribution

```json
[
  {"bucket": "1k-10k", "count": 42, "metric": "transfer_usd"}
]
```

Use log bins for highly skewed transfer or holder values. Document the binning method.

## Privacy And Auditability

- Redact private watchlists before sending data to external chart APIs.
- Keep raw addresses in tables when needed, but use labels in charts when possible.
- Keep `source` and `caveat` fields near exported chart specs.
- Preserve units and decimal normalization; raw token units are not chart-ready.
