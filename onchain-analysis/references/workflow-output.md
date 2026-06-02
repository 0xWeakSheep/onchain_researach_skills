# Workflow And Output Contract

Use this file when starting any chain-analysis task that may produce files.

## Required Flow

1. Create a run directory under `out/runs/<run_id>/`.
2. Copy or create `manifest.json` from `out/_templates/manifest.json`.
3. Copy or create `run.md` from `out/_templates/run.md`.
4. Use `onchain-analysis` to define the scope, source roles, metrics, and validation plan.
5. Use one platform skill only when platform-specific docs, API parameters, SQL, notebook structure, or data semantics are needed.
6. Store collected or transformed data in `data/`.
7. Store API/query/chart specs in `specs/`.
8. Store rendered charts in `charts/`.
9. Store metric summaries in `summaries/`.
10. Store final reports in `reports/`.
11. Store command logs and validation traces in `logs/`.
12. Update `manifest.json` before final delivery.

## Skill Routing

| User intent | First skill | Next skill |
|---|---|---|
| "Analyze this wallet/token/protocol" | `onchain-analysis` | Arkham, Etherscan, Dune, or Binance Web3 data skill |
| "Write SQL/API plan" | `onchain-analysis` | Dune, Etherscan, Arkham, Hex, Deepnote |
| "Make a chart/dashboard/report figure" | `onchain-charting` | `chart-visualization`, Mermaid/FigJam, notebook, spreadsheet, or frontend chart |
| "Need an interactive notebook" | `onchain-analysis` | Hex, Observable, or Deepnote, then `onchain-charting` |
| "Need final report" | `onchain-analysis` | `onchain-charting` for chart QA |

## Artifact Rules

- Do not write new generated files to the repository root.
- Do not write new generated files to `generated/`.
- Every delivered file must appear in `manifest.json`.
- Every chart must have a chart-ready data source or a chart spec.
- Every final report must state source, metric definition, time window, caveats, and output paths.
