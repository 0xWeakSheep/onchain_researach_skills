# Chart Output Contract

Use this file when a chart, diagram, dashboard mock, or report figure will be written to disk.

## Required Output Paths

| Artifact | Path |
|---|---|
| Chart-ready data | `out/runs/<run_id>/data/` |
| Chart spec or rendering config | `out/runs/<run_id>/specs/` |
| Rendered chart image or HTML | `out/runs/<run_id>/charts/` |
| Metric summary | `out/runs/<run_id>/summaries/` |
| Figure note or report section | `out/runs/<run_id>/reports/` |
| Rendering or QA log | `out/runs/<run_id>/logs/` |

## Required Chart Metadata

Each chart spec or report figure note should include:

- Metric name.
- Chain/source.
- Asset, address, protocol, or entity scope.
- Time window and timezone.
- Unit and normalization.
- Data file path.
- Rendered chart path.
- Caveats.
- Skills used.

## File Naming

Use lowercase descriptive file names:

```text
charts/eth-usdc-daily-volume.png
data/eth-usdc-daily-volume.json
specs/eth-usdc-daily-volume-chart-spec.json
summaries/eth-usdc-daily-volume-summary.json
reports/eth-usdc-daily-volume.md
```

## Manifest Update

Before final delivery, update `out/runs/<run_id>/manifest.json` so every file appears under the correct `artifacts` section.

Then use `onchain-finalizer` to verify the active run directory, manifest paths, and repository-root misplacement check.
