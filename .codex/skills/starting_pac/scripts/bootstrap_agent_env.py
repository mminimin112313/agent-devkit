#!/usr/bin/env python3
"""Bootstrap a repo-local Codex agent environment from a project plan.

This helper creates the same kind of AGENTS.md, MEMORY.md, .codex skill
structure, and work-log files that a careful manual setup would create.
It is intentionally conservative: existing files are not overwritten unless
--force is passed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


PLAN_CANDIDATES = ("기획.md", "PRD.md", "prd.md", "plan.md", "PLAN.md", "README.md")
GENERATED_DIRS = ("node_modules", ".git", ".build", "build", "dist", "target", "coverage")


def slugify(value: str, fallback: str = "project") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value)
    value = value.strip("-")
    return value or fallback


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_file(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return f"kept existing {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    return f"wrote {path}"


def find_plan(root: Path, explicit: str | None) -> Path | None:
    if explicit:
        path = (root / explicit).resolve() if not Path(explicit).is_absolute() else Path(explicit)
        return path if path.exists() else None
    for name in PLAN_CANDIDATES:
        path = root / name
        if path.exists():
            return path
    docs = root / "docs"
    if docs.exists():
        for path in sorted(docs.glob("*.md")):
            if any(token in path.name.lower() for token in ("plan", "prd", "brief", "기획")):
                return path
    return None


def extract_headings(text: str, limit: int = 12) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        if line.startswith("#"):
            cleaned = line.lstrip("#").strip()
            if cleaned:
                headings.append(cleaned)
        if len(headings) >= limit:
            break
    return headings


def infer_product_name(root: Path, plan_text: str) -> str:
    bold_names = re.findall(r"\*\*([^*\n]{2,60})\*\*", plan_text)
    for candidate in bold_names:
        if any(token in candidate.lower() for token in ("studio", "app", "서비스", "프로젝트")):
            return candidate.strip()
    first_heading = next(iter(extract_headings(plan_text, limit=1)), "")
    return first_heading or root.name


def summarize_plan(plan: Path | None, root: Path) -> tuple[str, list[str], str]:
    if not plan:
        return root.name, ["No plan file found during bootstrap."], "No canonical plan file found."
    text = read_text(plan)
    product_name = infer_product_name(root, text)
    headings = extract_headings(text)
    summary = headings[:8] if headings else ["Plan exists but no markdown headings were found."]
    return product_name, summary, str(plan.name)


def agents_md(root: Path, project_name: str, continuation_slug: str) -> str:
    return f"""# {project_name} Agent Rules

## Scope

These rules govern `{root}` and all child paths.

## Default Operating Mode

- When the user says `이어서 작업해`, `계속`, or `ㄱㄱㄱ`, continue from `MEMORY.md` and `.codex/work-log/` without asking for a recap.
- Treat `MEMORY.md` as the project state ledger: update it when goals, decisions, blockers, verification results, or next steps change.
- Use `.codex/skills/{continuation_slug}/SKILL.md` for continuation, planning, logging, and completion discipline.
- Prefer concrete execution over discussion once the next step is clear.

## Project Context Contract

Before making non-trivial changes, read:

1. `MEMORY.md`
2. `.codex/README.md`
3. `.codex/skills/{continuation_slug}/SKILL.md`
4. The most recent relevant file in `.codex/work-log/`

If the implementation surface is absent or unclear, create the smallest durable project skeleton needed to make the next task executable, then record the decision.

## Work Logging

- Add or update a dated entry under `.codex/work-log/` for meaningful work sessions.
- Every log entry should include: goal, files touched, decisions, validation, remaining next steps.
- Keep `MEMORY.md` concise and current; detailed notes belong in `.codex/work-log/`.

## Documentation

- Keep agent-maintained operating docs under 200 lines: `AGENTS.md`, `MEMORY.md`, `.codex/**/*.md`, and `docs/*.md`.
- Long source plans may exceed 200 lines; split them only when asked or when they become hard to operate from.
- When adding project behavior or architecture, update `MEMORY.md` and relevant docs in the same change.

## Validation

- Run the narrowest useful validation after changes.
- If no runnable app or test suite exists yet, verify the instruction system itself with file inventory and line-count checks.
- Do not claim runtime verification until a runnable implementation exists and has been exercised.
- Problem solving must target the root cause and apply a fundamental fix. Fallbacks, bypasses, temporary patches, or workaround-first approaches require explicit user approval with reason, scope, risk, and rollback plan before they are applied.
- For non-trivial development, consider file-based runtime logs and standardized error codes early so failures remain searchable and reproducible across agent sessions.
"""


def memory_md(root: Path, project_name: str, plan_name: str, headings: list[str], continuation_slug: str) -> str:
    heading_lines = "\n".join(f"- {item}" for item in headings)
    return f"""# {project_name} Project Memory

## Current State

- Project root: `{root}`
- Status: agent work environment initialized from `{plan_name}`; implementation status needs current inspection.
- Primary operating phrase: `이어서 작업해`
- Continuation skill: `.codex/skills/{continuation_slug}/SKILL.md`

## Product Intent

Derived from `{plan_name}`. Re-read the plan before making architecture or scope decisions.

## Plan Outline

{heading_lines}

## Operating Decisions

- `AGENTS.md` owns path-scoped rules for this repository.
- `MEMORY.md` owns current state, decisions, blockers, and next actions.
- `.codex/work-log/` owns session-level evidence and detailed progress history.
- `.codex/skills/{continuation_slug}/` owns the reusable continuation workflow.
- `{plan_name}` is the canonical product plan until a newer PRD or architecture doc supersedes it.

## Development Diagnostics

- File-based logging: decide during the first implementation pass whether runtime/debug logs should be written under a project-owned path such as `logs/`, `.codex/runtime-log/`, or an app-specific data directory.
- Error code standardization: introduce stable error codes when failures cross UI, CLI, API, background jobs, or agent handoff boundaries.
- Root-cause fixes: prefer fundamental fixes over fallbacks, bypasses, temporary patches, or workaround-first solutions.
- Non-root solution approval: require explicit user approval with reason, scope, risk, and rollback plan before applying a fallback, bypass, temporary patch, or workaround.
- If logging or error codes are deferred, record the reason here and revisit after the first runnable workflow exists.

## Next Actions

1. Inspect the current source tree and package/runtime files.
2. Derive the next implementation step from `{plan_name}`.
3. Decide whether the first implementation needs file-based logging and standardized error codes.
4. Add or update the first runnable validation command.
5. Update this memory after the first implementation pass.

## Blockers

- Unknown until the source tree and runtime setup are inspected.

## Last Verification

- {dt.date.today().isoformat()}: agent environment bootstrap files generated. Runtime verification is pending until implementation is inspected or created.
"""


def codex_readme(continuation_slug: str) -> str:
    return f"""# Codex Workspace

This folder contains the project-local operating layer for Codex.

## Files

- `skills/{continuation_slug}/SKILL.md`: continuation workflow for `이어서 작업해`.
- `work-log/`: dated session logs with evidence, touched files, validation, and next steps.

## Continuation Flow

```text
IF user_says("이어서 작업해" OR "계속" OR "ㄱㄱㄱ")
  THEN read(MEMORY.md, AGENTS.md, latest .codex/work-log entry)
  THEN choose(next_action)
  THEN execute
  THEN validate
  THEN update(MEMORY.md, .codex/work-log)
```
"""


def skills_readme(continuation_slug: str) -> str:
    return f"""# Repo-Local Skills

## Available Skills

- `{continuation_slug}`: continue project work from `MEMORY.md`, the canonical plan, and `.codex/work-log/`.

## Routing

```text
IF user_says("이어서 작업해" OR "계속" OR "ㄱㄱㄱ")
  THEN USE({continuation_slug})
```
"""


def continuation_skill(project_name: str, plan_name: str) -> str:
    skill_name = f"{slugify(project_name)}-continuation"
    return f"""---
name: {skill_name}
description: Use in this project when the user says "이어서 작업해", "계속", "ㄱㄱㄱ", asks to continue work, or asks Codex to plan, execute, record, validate, and finish from repo-local memory.
---

# Project Continuation

<ROOT-CAUSE-SOLUTION-HOOK>
IF problem_solving_requires(fallback OR workaround OR bypass OR temporary_patch) THEN
  ASK_USER_APPROVAL(reason, scope, risk, rollback_plan) BEFORE applying_non_root_solution
  RECORD(root_cause_status := confirmed OR hypothesis_only OR blocked)
  PREFER(root_cause_fix) OVER(symptom_workaround)
  STOP("fallback or workaround requires explicit user approval and a root-cause plan") IF approval_is_missing
</ROOT-CAUSE-SOLUTION-HOOK>

## Trigger

```text
USE_THIS_SKILL IF
  user_says("이어서 작업해" OR "계속" OR "ㄱㄱㄱ")
  OR user_asks(project_continuation OR repo_local_memory)
```

## Required Reads

```text
READ := {{
  "AGENTS.md",
  "MEMORY.md",
  "{plan_name}",
  ".codex/README.md",
  "latest relevant .codex/work-log/*.md"
}}

IF package_manifest_exists THEN READ(package_manifest)
IF source_tree_exists THEN INVENTORY(source_tree)
```

## Process

```text
STEP_1 := ORIENT
  read required files
  inspect git status when repository exists
  inspect package/build/test files when present

STEP_2 := SELECT_NEXT_ACTION
  IF MEMORY.next_actions has actionable item THEN choose first unblocked item
  ELSE derive next implementation step from {plan_name}

STEP_3 := EXECUTE
  make scoped edits
  add file-based logging and standardized error codes when the first real workflow needs replayable diagnostics
  prefer root-cause fixes; ask approval before fallback, bypass, temporary patch, or workaround-first solution
  update docs and memory alongside behavior changes

STEP_4 := VERIFY
  run narrowest useful test/build/lint
  IF no runnable implementation exists THEN run instruction-system checks
  record exact command and result

STEP_5 := RECORD
  update MEMORY.md
  write dated .codex/work-log entry
```

## Completion Contract

```text
PASS IF user_goal_is_handled
  AND MEMORY_md_is_current
  AND work_log_entry_exists
  AND validation_result_is_recorded
```
"""


def work_log(project_name: str, plan_name: str, files: list[str]) -> str:
    file_lines = "\n".join(f"- `{path}`" for path in files)
    return f"""# {dt.date.today().isoformat()} Agent Environment Bootstrap

## Goal

Create a repo-local agent operating layer so future work can continue from local files.

## Starting Context

- Project: {project_name}
- Plan source: `{plan_name}`

## Files Changed

{file_lines}

## Decisions

- `AGENTS.md` governs this path.
- `MEMORY.md` stores current state and next actions.
- `.codex/work-log/` stores session evidence.
- The project continuation skill owns `이어서 작업해` behavior.

## Validation

- Bootstrap files were generated by `starting_pac`.
- Run file inventory and line-count checks before claiming completion.

## Next Steps

1. Inspect implementation files and runtime manifests.
2. Execute the next plan-derived implementation step.
3. Record validation in `MEMORY.md` and this work-log folder.
"""


def visible_files(root: Path) -> list[str]:
    files: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in GENERATED_DIRS for part in rel.parts):
            continue
        files.append(str(rel))
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--plan")
    parser.add_argument("--project-name")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists():
        print(f"project root does not exist: {root}", file=sys.stderr)
        return 2

    plan = find_plan(root, args.plan)
    project_name, headings, plan_name = summarize_plan(plan, root)
    if args.project_name:
        project_name = args.project_name
    project_slug = slugify(project_name, fallback=slugify(root.name))
    continuation_slug = f"{project_slug}-continuation"

    targets = [
        ("AGENTS.md", agents_md(root, project_name, continuation_slug)),
        ("MEMORY.md", memory_md(root, project_name, plan_name, headings, continuation_slug)),
        (".codex/README.md", codex_readme(continuation_slug)),
        (".codex/skills/README.md", skills_readme(continuation_slug)),
        (f".codex/skills/{continuation_slug}/SKILL.md", continuation_skill(project_name, plan_name)),
    ]
    log_path = f".codex/work-log/{dt.date.today().isoformat()}-agent-environment-bootstrap.md"
    targets.append((log_path, work_log(project_name, plan_name, [path for path, _ in targets] + [log_path])))

    for rel, content in targets:
        print(write_file(root / rel, content, args.force))

    print("inventory:")
    for rel in visible_files(root)[:200]:
        print(f"  {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
