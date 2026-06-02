# Legacy ETH/USDC Outputs

## Objective

Preserve previously generated ETH/USDC volume and volatility artifacts in the normalized output layout.

## Scope

- Assets: ETH, USDC
- Time window: 2025-06-02 to 2026-06-02
- Source: Binance spot ETHUSDC 1d klines

## Skill Flow

1. `onchain-charting`: migrated existing chart and summary outputs into the normalized run layout.
2. `onchain-finalizer`: verified artifact location convergence.

## Outputs

- `data/eth_usdc_daily_volume.json`
- `charts/eth_usdc_daily_quote_volume.png`
- `charts/eth_usdc_30d_annualized_volatility.png`
- `summaries/eth_usdc_daily_volume_summary.json`

## Finalization

- Location check: `logs/output-location-check.txt`
- Manifest updated: yes
- Delivery paths: all files are under `out/runs/legacy-eth-usdc/`

## Caveats

- Migrated from legacy root-level files.
- No original chart specs were available.

## Next Checks

- Regenerate with a complete chart spec if this output is reused.
