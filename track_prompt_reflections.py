#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_PROMPTS_ROOT = REPO_ROOT.parent / "docs" / "prompts"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_text(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def git_output(*args: str) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(REPO_ROOT), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return completed.stdout.strip() or "clean"


@dataclass
class PromptSnapshot:
    source: str
    observed_mtime_utc: str
    observed_sha256: str


def load_status(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def collect_prompts(prompts_root: Path) -> list[PromptSnapshot]:
    snapshots: list[PromptSnapshot] = []
    for path in sorted(prompts_root.rglob("*.md")):
        snapshots.append(
            PromptSnapshot(
                source=path.relative_to(prompts_root).as_posix(),
                observed_mtime_utc=iso_mtime(path),
                observed_sha256=sha256_text(path),
            )
        )
    return snapshots


def compute_review_state(status: str, reflected_source_sha256: str | None, observed_sha256: str) -> str:
    if status == "pending":
        return "needs_review"
    if reflected_source_sha256 != observed_sha256:
        return "source_changed_since_reflection"
    return "current"


def sync_status(prompts_root: Path, status_path: Path) -> dict[str, Any]:
    existing = load_status(status_path)
    if not prompts_root.exists():
        if existing.get("entries") is not None:
            return existing
        raise SystemExit(f"prompts root does not exist and no status artifact is available: {prompts_root}")

    existing_entries = {
        entry["source"]: entry for entry in existing.get("entries", [])
    }

    entries: list[dict[str, Any]] = []
    for snapshot in collect_prompts(prompts_root):
        previous = existing_entries.get(snapshot.source, {})
        status = previous.get("status", "pending")
        reflected_source_sha256 = previous.get("reflected_source_sha256")
        entries.append(
            {
                "source": snapshot.source,
                "observed_mtime_utc": snapshot.observed_mtime_utc,
                "observed_sha256": snapshot.observed_sha256,
                "status": status,
                "review_state": compute_review_state(
                    status=status,
                    reflected_source_sha256=reflected_source_sha256,
                    observed_sha256=snapshot.observed_sha256,
                ),
                "reflected_at_utc": previous.get("reflected_at_utc"),
                "reflected_source_sha256": reflected_source_sha256,
                "reflected_to": previous.get("reflected_to", []),
                "reflection_note": previous.get("reflection_note", ""),
            }
        )

    document = {
        "tracked_prompts_root": str(prompts_root),
        "generated_at_utc": utc_now(),
        "orchestration_git_head": git_output("rev-parse", "HEAD"),
        "orchestration_git_status": git_output("status", "--short"),
        "status_summary": build_status_summary(entries),
        "entries": entries,
    }
    status_path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    return document


def mark_entry(
    prompts_root: Path,
    status_path: Path,
    source: str,
    status: str,
    reflected_to: list[str],
    note: str,
) -> dict[str, Any]:
    document = sync_status(prompts_root, status_path)
    entries = {entry["source"]: entry for entry in document["entries"]}
    if source not in entries:
        raise SystemExit(f"Unknown prompt source: {source}")

    entry = entries[source]
    entry["status"] = status
    entry["reflected_at_utc"] = utc_now()
    entry["reflected_source_sha256"] = entry["observed_sha256"]
    entry["reflected_to"] = reflected_to
    entry["reflection_note"] = note
    entry["review_state"] = compute_review_state(
        status=status,
        reflected_source_sha256=entry["reflected_source_sha256"],
        observed_sha256=entry["observed_sha256"],
    )

    document["generated_at_utc"] = utc_now()
    document["status_summary"] = build_status_summary(document["entries"])
    status_path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    return document


def build_status_summary(entries: list[dict[str, Any]]) -> dict[str, int]:
    summary = {
        "total": len(entries),
        "reflected": 0,
        "not_applicable": 0,
        "pending": 0,
        "needs_review": 0,
        "source_changed_since_reflection": 0,
        "current": 0,
    }
    for entry in entries:
        status = entry["status"]
        review_state = entry["review_state"]
        summary[status] += 1
        summary[review_state] += 1
    return summary


def print_summary(document: dict[str, Any]) -> None:
    summary = document["status_summary"]
    print(f"Tracked prompts root: {document['tracked_prompts_root']}")
    print(f"Generated at UTC: {document['generated_at_utc']}")
    print(f"Git head: {document['orchestration_git_head']}")
    print("Status counts:")
    print(f"  total: {summary['total']}")
    print(f"  reflected: {summary['reflected']}")
    print(f"  not_applicable: {summary['not_applicable']}")
    print(f"  pending: {summary['pending']}")
    print(f"  needs_review: {summary['needs_review']}")
    print(f"  source_changed_since_reflection: {summary['source_changed_since_reflection']}")
    print("")

    flagged = [
        entry for entry in document["entries"]
        if entry["review_state"] in {"needs_review", "source_changed_since_reflection"}
    ]
    if not flagged:
        print("No prompt files currently need reflection review.")
        return

    print("Prompt files needing review:")
    for entry in flagged:
        print(f"  - {entry['source']} [{entry['review_state']}]")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Track which extracted prompt lessons were reflected into codex-orchestrator."
    )
    parser.add_argument(
        "--prompts-root",
        type=Path,
        default=DEFAULT_PROMPTS_ROOT,
        help="Path to the extracted prompt directory. Defaults to ../docs/prompts.",
    )
    parser.add_argument(
        "--status-path",
        type=Path,
        required=True,
        help="Explicit output record outside this publication repository.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("sync", help="Refresh source metadata and preserve manual reflection status.")
    subparsers.add_parser("summary", help="Refresh metadata and print a human-readable review summary.")

    mark = subparsers.add_parser("mark", help="Mark one prompt file as reflected or not applicable.")
    mark.add_argument("source", help="Prompt path relative to the prompts root.")
    mark.add_argument("--status", choices=["reflected", "not_applicable", "pending"], required=True)
    mark.add_argument("--reflected-to", action="append", default=[], help="Target file or surface that absorbed the lesson.")
    mark.add_argument("--note", required=True, help="Short rationale for the current status.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    prompts_root = args.prompts_root.resolve()
    status_path = args.status_path.resolve()
    if status_path.is_relative_to(REPO_ROOT):
        parser.error("--status-path must be outside this publication repository")
    status_path.parent.mkdir(parents=True, exist_ok=True)

    if args.command == "sync":
        sync_status(prompts_root, status_path)
        return

    if args.command == "summary":
        document = sync_status(prompts_root, status_path)
        print_summary(document)
        return

    if args.command == "mark":
        mark_entry(
            prompts_root=prompts_root,
            status_path=status_path,
            source=args.source,
            status=args.status,
            reflected_to=args.reflected_to,
            note=args.note,
        )
        return

    raise SystemExit(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
