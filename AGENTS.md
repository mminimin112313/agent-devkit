# Codex Orchestration Repository Guide

This repository is the reusable baseline for a repo-local Codex operating system.

## Project Identity

- This repository is not an application product.
- This repository is the source package for reusable orchestration rules, role prompts, skills, assets, and verification contracts.
- The primary authority for runtime behavior lives under `.codex/`.
- The main purpose of changes here is to keep the operating layer coherent, copyable, and actually runnable after reuse in other repositories.

## Load Order

1. Read this root `AGENTS.md`.
2. Read [`.codex/AGENTS.md`](.codex/AGENTS.md).
3. Read the selected skill under [`.codex/skills/`](.codex/skills).
4. Read only the exact skill-local assets and references declared by that skill.

## Repository Layout

- [`.codex/AGENTS.md`](.codex/AGENTS.md): top-level operating laws for this package.
- [`.codex/config.toml`](.codex/config.toml): runtime flags and registered repo roles.
- [`.codex/agents/`](.codex/agents): shared repo role configs.
- [`.codex/skills/`](.codex/skills): active reusable skill catalog.
- [`docs/plans/`](docs/plans): design and implementation history for the skillpack itself.
- [`tests/`](tests): regression suite for skill contracts and documentation structure.

## Active Skill Catalog

The active top-level skills in this repository are:

- `intake-and-routing`
- `product-and-ux`
- `planning-and-scoping`
- `architecture-and-design`
- `implementation-frontend`
- `implementation-backend`
- `quality-and-review`
- `release-and-operations`
- `multi-agent-orchestration`
- `security-review`
- `security-lab`
- `skillsmith`
- `starting_pac`

If a skill is not in that catalog, it should be treated as removed, legacy, or historical only.

## Project-Specific Rules

- Keep this repository focused on the orchestration system itself, not unrelated product features.
- Prefer removing legacy skill surface area instead of carrying aliases, compatibility shells, or duplicate authority.
- Keep the skill catalog small and sharp. New top-level skills need explicit justification.
- When a behavior has been absorbed into an existing skill, remove the old public surface instead of documenting both.
- Prefer portable repo-local workflows over host-specific daemons, launch agents, mailbox stores, or machine-local side channels.
- Shared operating assets must remain runnable with plain repo-local files plus common `git`, `python`, `node`, or shell usage across environments.
- Keep file paths, required reads, output contracts, and routing gates internally consistent across `AGENTS.md`, skill docs, assets, references, and tests.
- Update tests in the same change whenever a skill contract changes.
- Historical planning docs may remain, but they must not advertise removed skills as active current surface area.
- Do not infer progress from intention, green-looking output, or stale notes. Judge progress from inspected source files, commands, generated artifacts, and documented acceptance evidence.
- Modify shared skills and operating rules only within an explicit user-requested improvement. Do not run background self-improvement or create automatic failure logs.
- For meaningful changes, update `docs/` in the same change with the file inventory, current logic, verification commands, artifact inspection notes, and unresolved risk. If docs cannot be updated, the change is incomplete.
- For every non-trivial change, define evaluation criteria before implementation, then route implementation output to an evaluator role that is distinct from both planner and implementer. The planner, implementer, and evaluator must be different agents or roles. Completion is invalid when plan author, implementation owner, and final evaluator collapse into one role without an explicit environment limitation.
- Programming work must search existing code, tests, docs, config, and patterns before editing; if the preferred search tool fails or is permission-denied, record the command failure signal and use a shell-native fallback without narrowing the intended search scope or bypassing existing ignore intent; avoid hardcoded addresses or environment-specific values; scaffold new projects with separated extension seams instead of god classes; audit changed file line counts at the end and split oversized files before completion unless a documented exception is recorded.
- Problem solving must target the root cause and apply a fundamental fix. Fallbacks, bypasses, temporary patches, or workaround-first approaches require explicit user approval with reason, scope, risk, and rollback plan before they are applied.
- If any state or technical fact is uncertain, verify it directly before proceeding. If the work grows broad, reduce it into sequential verified steps and ask an independent evaluator or sub-agent to challenge the judgment before final acceptance.

## Verification

- Primary verification command: `pytest -q`
- A change is not complete until the skill-contract suite passes.
- If catalog, routing, or required-read wording changes, update the affected regression tests in `tests/`.

## Response Rules For This Repository

- Give the user the result first, not process narration.
- Keep status updates short and factual.
- Do not describe internal skill-loading chatter unless the user specifically asks.
- If a skill or rule was removed, say it was removed. Do not imply it is still available through a hidden alias.
