# Workflow And Output Contract

Use this file when starting any chain-analysis task that may produce files.

## Required Flow

1. Create a run directory under `out/runs/<run_id>/`.
2. Copy or create `manifest.json` from `out/_templates/manifest.json`.
3. Copy or create `run.md` from `out/_templates/run.md`.
4. Use `onchain-planner` to write `specs/skill-plan.md` when the task needs more than one skill or execution step.
5. Use `onchain-analysis` to define the scope, source roles, metrics, and validation plan.
6. Use one platform skill only when platform-specific docs, API parameters, SQL, notebook structure, or data semantics are needed.
7. Store collected or transformed data in `data/`.
8. Store API/query/chart specs in `specs/`.
9. Store rendered charts in `charts/`.
10. Store metric summaries in `summaries/`.
11. Store final reports in `reports/`.
12. Store command logs and validation traces in `logs/`.
13. Update `manifest.json` before final delivery.

## Skill Routing

| User intent | First skill | Next skill |
|---|---|---|
| "Which skills should handle this?" | `onchain-planner` | `onchain-analysis` or `onchain-charting` |
| "Analyze this wallet/token/protocol" | `onchain-planner` | `onchain-analysis`, then Arkham, Etherscan, Dune, or Binance Web3 data skill |
| "Write SQL/API plan" | `onchain-planner` | `onchain-analysis`, then Dune, Etherscan, Arkham, Hex, Deepnote |
| "Make a chart/dashboard/report figure" | `onchain-planner` | `onchain-charting`, then `chart-visualization`, Mermaid/FigJam, notebook, spreadsheet, or frontend chart |
| "Need an interactive notebook" | `onchain-planner` | `onchain-analysis`, then Hex, Observable, or Deepnote, then `onchain-charting` |
| "Need final report" | `onchain-planner` | `onchain-analysis`, then `onchain-charting` for chart QA |

## Artifact Rules

- Do not write new generated files to the repository root.
- Do not write new generated files to `generated/`.
- Every delivered file must appear in `manifest.json`.
- Every chart must have a chart-ready data source or a chart spec.
- Every final report must state source, metric definition, time window, caveats, and output paths.
