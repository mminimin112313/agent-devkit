# Agent-Skills Pass 6 Design

## Goal

Harden the current exported skill catalog so every existing skill is auditable, current, and explicit about:

- when the skill triggers
- which local assets and references to use
- how delegated work should be directed when applicable
- how catalog and subtree docs describe the current skillpack

This pass is a full-catalog maintenance pass, not a source-repo absorption pass.

## Scope

### Meta And Catalog Lane

- `.codex/AGENTS.md`
- `.codex/skills/AGENTS.md`
- `.codex/skills/README.md`
- `.codex/skills/skillsmith/**`
- `.codex/skills/multi-agent-orchestration/**`
- `.codex/skills/intake-and-routing/**`
- `.codex/skills/failure-memory/**`

### Execution And Review Lane

- `.codex/skills/architecture-and-design/**`
- `.codex/skills/implementation-backend/**`
- `.codex/skills/implementation-frontend/**`
- `.codex/skills/quality-and-review/**`
- `.codex/skills/release-and-operations/**`

### Product And Security Lane

- `.codex/skills/planning-and-scoping/**`
- `.codex/skills/product-and-ux/**`
- `.codex/skills/security-review/**`
- `.codex/skills/security-lab/**`

## Hardening Targets

1. Remove stale catalog assumptions such as the old `ten or fewer` cap where the live pack now exceeds it.
2. Bring lagging skills up to the newer structure:
   - trigger conditions
   - choose roles
   - choose assets
   - choose references
   - output contract
3. Ensure skills that can drive delegation or parallel work direct subagents to exact repo-local skills and support files.
4. Ensure skills and shared docs preserve traceability of dispatched versus actually used support material where delegation is involved.
5. Check that listed local `agents/`, `assets/`, `references/`, `scripts/`, and `presets/` paths still exist and match present wording.
6. Prefer targeted edits over package sprawl. Refresh stale wording before adding new files.

## Explicit Exclusions

- no new top-level skills
- no deletion of current skills in this pass
- no broad product-code changes outside `.codex/**` and pass docs
- no reintroduction of graph-first or root-template dependencies

## Acceptance

- every current skill either follows the newer explicit package pattern or is intentionally justified
- shared catalog docs no longer contradict the actual catalog shape
- delegated-work rules are explicit and traceable
- referenced local support paths remain valid
- `git diff --check` passes
- `pytest` passes
