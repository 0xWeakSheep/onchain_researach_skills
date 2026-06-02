# Artifact Location Gate

Use this gate before final delivery of any run that produced files.

## Active Run Boundary

All final artifacts must be inside exactly one active run directory:

```text
out/runs/<run_id>/
```

Do not deliver files from the repository root, `generated/`, temporary folders, or a different run directory unless the final answer clearly identifies them as historical references.

## Required Shape

```text
out/runs/<run_id>/
  manifest.json
  run.md
  data/
  charts/
  summaries/
  reports/
  specs/
  logs/
```

`specs/skill-plan.md` is required when the task used more than one skill or execution step.

## Allowed Artifact Directories

| Directory | Allowed content |
|---|---|
| `data/` | Raw, cleaned, transformed, or chart-ready data |
| `charts/` | Rendered chart, diagram, dashboard, or figure files |
| `summaries/` | Machine-readable metric summaries or compact notes |
| `reports/` | Final memos, report sections, decks, exports, or figure notes |
| `specs/` | Skill plan, query/API plan, chart spec, render config, prompts |
| `logs/` | Command output, API/query trace, validation output, finalizer check |

Top-level files in the run directory should be limited to `manifest.json` and `run.md`.

## Manifest Path Rules

- Use run-relative paths such as `charts/eth-usdc-volume.png`.
- Do not use absolute paths.
- Do not use `..` path segments.
- Each listed file must exist.
- Each listed file must be inside the matching artifact directory.
- Each non-placeholder artifact file must appear in `manifest.json`.

Ignore `.gitkeep` placeholders when checking manifest coverage.

## Repository-Level Misplacement Rules

Before delivery, check the repository root for generated outputs:

- No root-level `.png`, `.svg`, `.csv`, `.tsv`, `.xlsx`, `.parquet`, `.pdf`, `.html`, or generated data `.json` files. Project metadata such as `skills-lock.json` is allowed.
- No `generated/` directory for delivered outputs.
- No final file paths in the user-facing answer outside the active run directory.

## Deterministic Check

Run:

```bash
python3 onchain-finalizer/scripts/check_output_location.py out/runs/<run_id> --scan-repo --write-log logs/output-location-check.txt
```

For multi-step runs, add:

```bash
--require-skill-plan
```

Before using `--write-log`, add `logs/output-location-check.txt` to `manifest.json` under `artifacts.logs`. The script accepts that pending log path, writes it after the location gate passes, and then the final state remains manifest-complete.
