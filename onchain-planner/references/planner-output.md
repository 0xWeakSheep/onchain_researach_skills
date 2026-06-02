# Planner Output

Use this template for `out/runs/<run_id>/specs/skill-plan.md`.

```markdown
# Skill Plan: <title>

## Objective

## Run Directory

`out/runs/<run_id>/`

## Skill Sequence

| Step | Skill | Why | Expected artifacts |
|---|---|---|---|
| 1 | `onchain-planner` | Classify request and choose workflow | `specs/skill-plan.md`, `run.md` |
| 2 | `onchain-analysis` | Define source, metric, and validation plan | `specs/`, `summaries/` |
| 3 | Platform or data skill | Collect or specify source data | `data/`, `logs/` |
| 4 | `onchain-charting` | Prepare chart plan and QA | `specs/`, `summaries/` |
| 5 | Renderer or delivery surface | Create chart/report/dashboard output | `charts/`, `reports/` |

## Expected Files

- `manifest.json`
- `run.md`
- `specs/skill-plan.md`

## Validation Gates

- Source and metric definitions are explicit.
- Important conclusions have a validation source or stated caveat.
- Every produced file is listed in `manifest.json`.
- Chart data is either local-safe or explicitly approved for hosted rendering.

## Privacy And API-Key Notes

State whether the selected tools require API keys, external uploads, private labels, wallet notes, or redaction.

## Open Questions

Only list blockers that prevent safe execution.
```
