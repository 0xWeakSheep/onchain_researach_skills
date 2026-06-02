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
| `logs/` | Execution notes, command logs, validation traces, finalizer checks |

Do not place generated artifacts in the repository root or in `generated/`.

## Artifact Location Gate

Before final delivery, `onchain-finalizer` must verify the active run directory:

- The run directory is under `out/runs/<run_id>/`.
- Top-level run files are limited to `manifest.json` and `run.md`.
- Final artifacts live only in `data/`, `charts/`, `summaries/`, `reports/`, `specs/`, or `logs/`.
- Manifest artifact paths are run-relative, existing, and match their artifact section.
- Non-placeholder artifact files are listed in `manifest.json`.
- No delivered output remains in the repository root or `generated/`.

Preferred command:

```bash
python3 onchain-finalizer/scripts/check_output_location.py out/runs/<run_id> --scan-repo --write-log logs/output-location-check.txt
```

For multi-step runs, add `--require-skill-plan`.

Before using `--write-log`, list `logs/output-location-check.txt` in `manifest.json` under `artifacts.logs`.

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
7. `onchain-finalizer`: verify artifact location convergence and record the check in `logs/`.
