#!/usr/bin/env python3
"""Validate artifact location convergence for one out/runs/<run_id> directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ALLOWED_DIRS = ("data", "charts", "summaries", "reports", "specs", "logs")
ALLOWED_ROOT_FILES = {"manifest.json", "run.md"}
IGNORED_FILENAMES = {".gitkeep", ".DS_Store"}
ROOT_ARTIFACT_SUFFIXES = {
    ".png",
    ".svg",
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
    ".parquet",
    ".pdf",
    ".html",
}
ROOT_ALLOWED_JSON = {
    "package.json",
    "package-lock.json",
    "skills-lock.json",
    "tsconfig.json",
}


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def display(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate that generated artifacts are consolidated into one out/runs directory."
    )
    parser.add_argument("run_dir", help="Active run directory, for example out/runs/20260602-eth-volume")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--require-skill-plan",
        action="store_true",
        help="Require specs/skill-plan.md for multi-step workflows.",
    )
    parser.add_argument(
        "--scan-repo",
        action="store_true",
        help="Check the repository root for misplaced generated outputs and generated/.",
    )
    parser.add_argument(
        "--write-log",
        help="Write successful check output to a run-relative logs/ path that is already listed in manifest.json.",
    )
    return parser.parse_args()


def load_manifest(run_dir: Path, errors: list[str]) -> dict:
    manifest_path = run_dir / "manifest.json"
    try:
        return json.loads(manifest_path.read_text())
    except FileNotFoundError:
        errors.append("missing manifest.json")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid manifest.json: {exc}")
    return {}


def validate_run_boundary(repo_root: Path, run_dir: Path, errors: list[str]) -> None:
    runs_root = repo_root / "out" / "runs"
    if not run_dir.exists():
        errors.append(f"run directory does not exist: {display(run_dir, repo_root)}")
        return
    if not run_dir.is_dir():
        errors.append(f"run path is not a directory: {display(run_dir, repo_root)}")
        return
    if not is_relative_to(run_dir, runs_root):
        errors.append(f"run directory must be under out/runs/: {display(run_dir, repo_root)}")


def validate_required_shape(run_dir: Path, repo_root: Path, require_skill_plan: bool, errors: list[str]) -> None:
    for name in ALLOWED_DIRS:
        path = run_dir / name
        if not path.is_dir():
            errors.append(f"missing required directory: {display(path, repo_root)}")
    for name in ALLOWED_ROOT_FILES:
        path = run_dir / name
        if not path.is_file():
            errors.append(f"missing required file: {display(path, repo_root)}")
    if require_skill_plan:
        path = run_dir / "specs" / "skill-plan.md"
        if not path.is_file():
            errors.append(f"missing required multi-step plan: {display(path, repo_root)}")


def resolve_manifest_path(value: str, run_dir: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path.resolve()
    return (run_dir / path).resolve()


def validate_manifest(
    manifest: dict,
    repo_root: Path,
    run_dir: Path,
    pending_log_path: Path | None,
    errors: list[str],
) -> set[Path]:
    listed: set[Path] = set()

    run_id = manifest.get("run_id")
    if run_id and run_id != run_dir.name:
        errors.append(f"manifest run_id '{run_id}' does not match directory '{run_dir.name}'")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict):
        errors.append("manifest artifacts must be an object")
        return listed

    for key in ALLOWED_DIRS:
        values = artifacts.get(key)
        if values is None:
            errors.append(f"manifest artifacts missing section: {key}")
            continue
        if not isinstance(values, list):
            errors.append(f"manifest artifacts.{key} must be a list")
            continue

        for value in values:
            if not isinstance(value, str) or not value:
                errors.append(f"manifest artifacts.{key} contains a non-string or empty path")
                continue
            path = Path(value)
            if path.is_absolute():
                errors.append(f"manifest path must be run-relative, not absolute: {value}")
                continue
            if ".." in path.parts:
                errors.append(f"manifest path must not contain '..': {value}")
                continue
            if not path.parts or path.parts[0] != key:
                errors.append(f"manifest path must start with {key}/: {value}")
                continue

            resolved = resolve_manifest_path(value, run_dir)
            if not is_relative_to(resolved, run_dir):
                errors.append(f"manifest path escapes active run: {value}")
                continue
            if not resolved.is_file() and resolved != pending_log_path:
                errors.append(f"manifest path does not exist: {value}")
                continue
            listed.add(resolved)

    return listed


def validate_files_in_run(repo_root: Path, run_dir: Path, listed: set[Path], errors: list[str]) -> None:
    for path in sorted(run_dir.rglob("*")):
        if not path.is_file() or path.name in IGNORED_FILENAMES:
            continue

        rel = path.relative_to(run_dir)
        if len(rel.parts) == 1:
            if rel.name not in ALLOWED_ROOT_FILES:
                errors.append(f"unexpected top-level run file: {display(path, repo_root)}")
            continue

        top = rel.parts[0]
        if top not in ALLOWED_DIRS:
            errors.append(f"file is outside approved artifact directories: {display(path, repo_root)}")
            continue
        if path.resolve() not in listed:
            errors.append(f"artifact file is missing from manifest: {rel.as_posix()}")


def scan_repo_root(repo_root: Path, errors: list[str]) -> None:
    generated = repo_root / "generated"
    if generated.exists():
        errors.append("generated/ exists; delivered outputs must be moved under out/runs/<run_id>/")

    for path in sorted(repo_root.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() in ROOT_ARTIFACT_SUFFIXES:
            errors.append(f"generated-looking file at repository root: {path.name}")
        if path.suffix.lower() == ".json" and path.name not in ROOT_ALLOWED_JSON:
            errors.append(f"generated-looking JSON file at repository root: {path.name}")


def parse_pending_log(run_dir: Path, value: str | None, errors: list[str]) -> Path | None:
    if not value:
        return None
    path = Path(value)
    if path.is_absolute():
        errors.append(f"--write-log must be run-relative, not absolute: {value}")
        return None
    if ".." in path.parts:
        errors.append(f"--write-log must not contain '..': {value}")
        return None
    if not path.parts or path.parts[0] != "logs":
        errors.append(f"--write-log must start with logs/: {value}")
        return None
    return (run_dir / path).resolve()


def success_lines(repo_root: Path, run_dir: Path, scan_repo: bool, write_log: Path | None) -> list[str]:
    lines = [
        "output-location-check: OK",
        f"run_dir: {display(run_dir, repo_root)}",
        "checked: required shape, manifest paths, artifact placement",
    ]
    if scan_repo:
        lines.append("checked: repository root misplacements")
    if write_log:
        lines.append(f"log: {display(write_log, run_dir)}")
    return lines


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    run_dir = Path(args.run_dir)
    if not run_dir.is_absolute():
        run_dir = repo_root / run_dir
    run_dir = run_dir.resolve()

    errors: list[str] = []
    pending_log_path = parse_pending_log(run_dir, args.write_log, errors)
    validate_run_boundary(repo_root, run_dir, errors)
    if run_dir.exists() and run_dir.is_dir():
        validate_required_shape(run_dir, repo_root, args.require_skill_plan, errors)
        manifest = load_manifest(run_dir, errors)
        listed = validate_manifest(manifest, repo_root, run_dir, pending_log_path, errors) if manifest else set()
        if pending_log_path and pending_log_path not in listed:
            errors.append(f"--write-log path must be listed in manifest artifacts.logs: {display(pending_log_path, run_dir)}")
        validate_files_in_run(repo_root, run_dir, listed, errors)
    if args.scan_repo:
        scan_repo_root(repo_root, errors)

    if errors:
        print("output-location-check: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    lines = success_lines(repo_root, run_dir, args.scan_repo, pending_log_path)
    if pending_log_path:
        pending_log_path.parent.mkdir(parents=True, exist_ok=True)
        pending_log_path.write_text("\n".join(lines) + "\n")
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
