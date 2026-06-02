# Legacy BTC/USDC Outputs

## Objective

Preserve previously generated BTC/USDC volume and volatility artifacts in the normalized output layout.

## Scope

- Assets: BTC, USDC
- Time window: 2025-06-02 to 2026-06-02
- Source: Binance spot BTCUSDC 1d klines

## Skill Flow

1. `onchain-charting`: migrated existing chart and summary outputs into the normalized run layout.
2. `onchain-finalizer`: verified artifact location convergence.

## Outputs

- `data/btc_usdc_daily_volume.json`
- `data/btc_usdc_30d_historical_volatility.json`
- `charts/btc_usdc_daily_volume.png`
- `charts/btc_usdc_30d_historical_volatility.png`
- `summaries/btc_usdc_daily_volume_summary.json`
- `summaries/btc_usdc_30d_historical_volatility_summary.json`

## Finalization

- Location check: `logs/output-location-check.txt`
- Manifest updated: yes
- Delivery paths: all files are under `out/runs/legacy-btc-usdc/`

## Caveats

- Migrated from legacy generated files.
- No original chart specs were available.

## Next Checks

- Regenerate with a complete chart spec if this output is reused.
