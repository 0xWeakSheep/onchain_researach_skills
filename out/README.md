# Output Directory

All generated analysis artifacts must live under `out/`.

## Run Layout

Use one run directory per analysis task:

```text
out/runs/YYYYMMDD-topic-slug/
  manifest.json
  run.md
  data/
  charts/
  summaries/
  reports/
  specs/
  logs/
```

## Directory Roles

| Path | Content |
|---|---|
| `data/` | Raw or transformed data files: `.csv`, `.json`, `.parquet`, `.xlsx` |
| `charts/` | Rendered chart outputs: `.png`, `.svg`, `.html`, `.pdf` |
| `summaries/` | Machine-readable metric summaries: `.json`, `.md` |
| `reports/` | Human-readable analysis reports, memos, decks, or exports |
| `specs/` | Chart specs, API/query plans, prompts, rendering configs |
| `logs/` | Execution notes, command logs, validation traces |

Do not place generated artifacts in the repository root or in `generated/`.

## Required Files

Every run should include:

- `manifest.json`: source, scope, skills used, files produced, caveats.
- `run.md`: short human-readable description of the task, method, outputs, and next checks.
- `specs/skill-plan.md`: required when a task uses more than one skill or has multiple execution steps.

## Naming

Use lowercase, hyphen-separated run IDs:

```text
YYYYMMDD-asset-pair-metric
YYYYMMDD-protocol-wallet-flow
YYYYMMDD-token-holder-distribution
```

Use descriptive file names:

```text
data/eth-usdc-daily-volume.json
charts/eth-usdc-daily-volume.png
summaries/eth-usdc-daily-volume-summary.json
specs/eth-usdc-daily-volume-chart-spec.json
reports/eth-usdc-volume-report.md
```

## Skill Flow

1. `onchain-planner`: choose skill sequence, run directory, expected artifacts, validation gates.
2. `onchain-analysis`: choose data source, platform skill, metric definition, validation plan.
3. Platform skill: collect or plan platform-specific data work.
4. `onchain-charting`: choose chart type, shape chart data, decide renderer, run visual QA.
5. `chart-visualization`: generate hosted AntV image only when data is safe for external upload.
6. Final output: write all artifacts to the active `out/runs/<run_id>/` directory and update `manifest.json`.
