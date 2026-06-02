---
name: onchain-charting
description: Onchain chart planning and visualization routing guide. Use when Codex needs to choose chart types, shape wallet/token/protocol/market data for charts, prepare chart specs, decide between AntV chart images, Mermaid/FigJam diagrams, notebook charts, spreadsheets, or frontend chart libraries, or review chart clarity, auditability, accessibility, and privacy for onchain analysis outputs.
---

# Onchain Charting

## Overview

Use this skill as the entry point for chart-related work in this repository. It turns onchain data questions into chart plans, data schemas, tool choices, and visual QA checks.

## Workflow

1. Identify the decision the chart must support: trend, comparison, flow, distribution, relationship, audit table, or report summary.
2. Select a chart type from `references/chart-selection.md`.
3. Shape the data with the schemas in `references/data-shaping.md`.
4. Choose the output tool using `references/tool-routing.md`.
5. Apply `references/visual-qa.md` before final delivery.

## Tool Rules

- Use `chart-visualization` when the user wants a generated chart image and the data is safe to send to the AntV online API.
- Use Mermaid or FigJam for flowcharts, sequence diagrams, decision trees, ER diagrams, and architecture diagrams.
- Use notebook/front-end chart libraries when the user needs reusable code, interactivity, local data privacy, or a dashboard.
- Use tables beside charts when exact addresses, transaction hashes, token symbols, or source rows must remain auditable.
- Do not send private, unredacted investigation data to external chart APIs.

## Chart Defaults

- Time-series metrics: line chart; area only for cumulative or stacked contribution.
- Ranked entities, tokens, protocols, or chains: horizontal bar with Top-N plus "other".
- Fund flow between entities: Sankey when amounts are aggregated; transaction path diagram when sequence matters.
- Holder or trade-size distribution: histogram, boxplot, or log-scale bar bins.
- Address relationships: network graph only when edges and clusters are meaningful; otherwise use a table plus grouped bars.
- Token candles: candlestick/K-line only when OHLC data exists; do not fake candles from close-only data.

## References

- Read `references/chart-selection.md` when choosing the chart type.
- Read `references/data-shaping.md` when preparing input rows for a chart.
- Read `references/tool-routing.md` when deciding how to render or export the visual.
- Read `references/visual-qa.md` before delivering a final chart, report figure, or dashboard mock.
