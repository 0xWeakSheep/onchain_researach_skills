# Binance Futures Market Data Reference

Source snapshot: `binance/binance-skills-hub` commit `ea2ae15308497b42e0b346c3945d4ca8914790d8`.
Relevant source files:

- `skills/binance/binance/references/futures-usds.md`
- `skills/binance/binance/references/futures-coin.md`

This reference keeps only read-oriented datasets useful for charts and analysis.

## Product Families

| Product | Source reference | Typical identifier | Contract types |
|---|---|---|---|
| USDS-M futures | `futures-usds.md` | `symbol`, e.g. `BTCUSDT` | `PERPETUAL`, `CURRENT_MONTH`, `NEXT_MONTH`, `CURRENT_QUARTER`, `NEXT_QUARTER`, `PERPETUAL_DELIVERING` |
| COIN-M futures | `futures-coin.md` | `symbol` or `pair`, e.g. `BTCUSD_PERP`, `BTCUSD` | `PERPETUAL`, `CURRENT_QUARTER`, `NEXT_QUARTER`, `CURRENT_QUARTER_DELIVERING`, `NEXT_QUARTER_DELIVERING`, `PERPETUAL_DELIVERING` |

## Market Data Endpoints

| Metric family | USDS-M endpoint names | COIN-M endpoint names | Chart use |
|---|---|---|---|
| Contract metadata | `exchange-information`, `trading-schedule`, `futures-tradfi-perps-contract` | `exchange-information` | Validate symbols, contract status, delivery availability |
| Price and volume | `kline-candlestick-data`, `continuous-contract-kline-candlestick-data`, `ticker24hr-price-change-statistics`, `symbol-price-ticker`, `symbol-price-ticker-v2` | `kline-candlestick-data`, `continuous-contract-kline-candlestick-data`, `ticker24hr-price-change-statistics`, `symbol-price-ticker` | Price trend, volume, continuous quarterly/perp series |
| Mark/index/premium | `mark-price`, `mark-price-kline-candlestick-data`, `index-price-kline-candlestick-data`, `premium-index-kline-data`, `composite-index-symbol-information`, `query-index-price-constituents` | `index-price-and-mark-price`, `mark-price-kline-candlestick-data`, `index-price-kline-candlestick-data`, `premium-index-kline-data`, `query-index-price-constituents` | Mark vs index spread, premium trend, fair-price diagnostics |
| Funding | `get-funding-rate-history`, `get-funding-rate-info` | `get-funding-rate-history-of-perpetual-futures`, `get-funding-rate-info` | Funding rate time series and regime comparison |
| Open interest | `open-interest`, `open-interest-statistics` | `open-interest`, `open-interest-statistics` | OI trend, leverage buildup, contract comparison |
| Basis and delivery | `basis`, `quarterly-contract-settlement-price` | `basis` | Delivery basis, annualized basis, settlement review |
| Long/short sentiment | `long-short-ratio`, `top-trader-long-short-ratio-accounts`, `top-trader-long-short-ratio-positions` | `long-short-ratio`, `top-trader-long-short-ratio-accounts`, `top-trader-long-short-ratio-positions` | Sentiment and positioning charts |
| Flow and microstructure | `taker-buy-sell-volume`, `order-book`, `rpi-order-book`, `recent-trades-list`, `compressed-aggregate-trades-list`, `old-trades-lookup`, `symbol-order-book-ticker` | `taker-buy-sell-volume`, `order-book`, `recent-trades-list`, `compressed-aggregate-trades-list`, `old-trades-lookup`, `symbol-order-book-ticker` | Taker imbalance, depth snapshots, trade intensity |
| Risk snapshots | `adl-risk`, `query-insurance-fund-balance-snapshot` | none listed in source snapshot | ADL/insurance fund context |

## Authenticated User Data

| User data | USDS-M endpoint names | COIN-M endpoint names | Scope |
|---|---|---|---|
| Account and balance | `account-information-v2`, `account-information-v3`, `futures-account-balance-v2`, `futures-account-balance-v3` | `account-information`, `futures-account-balance` | Auth required |
| User positions | `position-information-v2`, `position-information-v3`, `position-adl-quantile-estimation`, `get-position-margin-change-history` | `position-information`, `position-adl-quantile-estimation`, `get-position-margin-change-history` | Auth required |
| User income/history | `get-income-history`, futures order/trade/transaction download endpoints | `get-income-history`, futures order/trade/transaction download endpoints | Auth required |
| User force orders | `users-force-orders` with `auto-close-type` = `LIQUIDATION` or `ADL` | `users-force-orders` with `auto-close-type` = `LIQUIDATION` or `ADL` | Auth required; user's own force orders, not necessarily market-wide liquidations |

## Parameter Conventions

- Timestamps: Unix milliseconds.
- Intervals: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`.
- Periods: `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `12h`, `1d`.
- Auto close type: `LIQUIDATION`, `ADL`.
- Position side: `BOTH`, `LONG`, `SHORT`.

## Data-Shaping Notes

- Preserve both raw symbol fields and normalized fields: `venue`, `productFamily`, `symbol`, `pair`, `contractType`, `metric`, `timestamp`.
- Keep units explicit: contract quantity, base asset, quote asset, USD/USDT/USDC, coin margin, percent, or ratio.
- For continuous contract data, include `contractType` in every output row.
- For long/short ratios, store whether the ratio is global, top-trader accounts, or top-trader positions.
- For funding and basis, record the period/frequency used before annualizing.
- For user force orders, label the output as authenticated user data and avoid mixing it with market-wide liquidation claims.
