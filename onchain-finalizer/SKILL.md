---
name: onchain-finalizer
description: "Ending convergence skill for onchain workflows. Use when finalizing an analysis, chart, notebook, dashboard, or report run, especially to verify artifact location convergence so generated files live inside the active out run directory, use approved subfolders, are listed in manifest.json, and no generated outputs remain in the repository root or generated directory."
---

# Onchain Finalizer

## Overview

Use this as the final skill before delivering an onchain workflow. It verifies that produced artifacts are consolidated into the active `out/runs/<run_id>/` directory and that the final response points only to normalized output paths.

This skill does not redo analysis, redraw charts, or change metric conclusions. It checks the output boundary and sends any missing work back to the responsible skill.

## Finalization Workflow

1. Confirm the active run directory: `out/runs/<run_id>/`.
2. Read `manifest.json`, `run.md`, and `specs/skill-plan.md` when present.
3. Apply the artifact location gate in `references/artifact-location-gate.md`.
4. Add `logs/output-location-check.txt` to `manifest.json` when the check log will be delivered.
5. Prefer running `scripts/check_output_location.py` against the active run directory with `--write-log logs/output-location-check.txt`.
6. Fix or route any misplaced files before final delivery.
7. Update `manifest.json` and `run.md` if paths or finalization notes changed.
8. Final response should reference only files under the active run directory.

## Artifact Location Gate

The first ending convergence point is complete only when:

- The active run directory exists under `out/runs/`.
- Required run files exist: `manifest.json` and `run.md`.
- Multi-step runs include `specs/skill-plan.md`.
- Final artifacts use only approved subdirectories: `data/`, `charts/`, `summaries/`, `reports/`, `specs/`, `logs/`.
- No generated artifacts remain in the repository root or `generated/`.
- Every artifact file is listed in the correct `manifest.json` artifact section.
- Manifest paths are run-relative, existing, and do not escape the active run directory.

## Handoff Rules

- If chart files are misplaced, return to `onchain-charting`.
- If data files or source logs are misplaced, return to `onchain-analysis` or the platform/data skill.
- If report files are misplaced, return to the reporting step that produced them.
- Do not mark delivery complete while the location gate fails.

## References

- Read `references/artifact-location-gate.md` for detailed placement rules.
- Use `scripts/check_output_location.py` for deterministic location validation.
- Read `../out/README.md` for the repository-wide output contract.
