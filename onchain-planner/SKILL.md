---
name: onchain-planner
description: Entry planner for onchain analysis workflows. Use when Codex needs to decide which skills to use, in what order, for wallet, token, protocol, market, dashboard, chart, notebook, or report tasks; creates a skill execution plan, chooses the run directory, and routes follow-up work to onchain-analysis, onchain-charting, platform skills, Binance Web3 data skills, or chart-visualization.
---

# Onchain Planner

## Overview

Use this as the first skill for multi-step onchain work. It decides the skill sequence, output directory, artifact contract, and validation gates before data collection, analysis, chart rendering, or report writing starts.

Do not use this skill to fetch data, write SQL, call APIs, or design charts in detail. Delegate execution to the selected downstream skills.

## Planning Workflow

1. Classify the request: analysis, data lookup, chart, dashboard, notebook, report, security check, market scan, or mixed workflow.
2. Create or reuse `out/runs/<run_id>/` when files may be produced.
3. Write or update `out/runs/<run_id>/specs/skill-plan.md` when the task has more than one step or uses more than one skill.
4. Select the next skill sequence using `references/skill-routing.md`.
5. Define expected artifacts before execution: data, specs, charts, summaries, reports, logs.
6. Route source and metric decisions to `onchain-analysis`.
7. Route chart and rendering decisions to `onchain-charting`.
8. Route platform-specific details to only the platform skill needed for that step.
9. Record privacy and API-key constraints before using external APIs or hosted chart renderers.
10. Keep `manifest.json` and `run.md` aligned with the selected skill plan.

## Planner Output

Use this shape in `specs/skill-plan.md` and in the user-facing planning answer:

- Objective
- Run directory
- Skill sequence
- Why each skill is selected
- Expected files
- Validation gates
- Privacy and API-key notes
- Open questions only if execution cannot proceed safely

## Routing Rules

- Use `onchain-analysis` after planning for metric definition, source selection, validation method, and platform handoff.
- Use `onchain-charting` after planning whenever the output includes a chart, dashboard, figure, or diagram.
- Use `chart-visualization` only after `onchain-charting` confirms the data is chart-ready and safe for the AntV online API.
- Use Binance Web3 market data skills only as data inputs for token search, market data, K-lines, address holdings, audits, rankings, meme data, tokenized securities, and smart-money signal datasets.
- Use Arkham, Etherscan, Dune, Hex, Observable, or Deepnote only when the task specifically needs that platform's data model, API, SQL, notebook, dashboard, or delivery surface.
- If a user asks only for a quick explanation and no artifact, produce the skill sequence without creating files.

## References

- Read `references/skill-routing.md` for the decision matrix.
- Read `references/planner-output.md` when writing `specs/skill-plan.md`.
- Read `../out/README.md` for the normalized output directory contract.
