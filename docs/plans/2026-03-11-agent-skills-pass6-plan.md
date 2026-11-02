# Agent-Skills Pass 6 Plan

## Working Model

- create three worktrees with disjoint write scopes
- assign one implementer and one reviewer to each lane
- converge approved changes into the main tree
- run catalog and verification gates from the main tree

## Lane A: Meta And Catalog

### Files

- `.codex/AGENTS.md`
- `.codex/skills/AGENTS.md`
- `.codex/skills/README.md`
- `.codex/skills/skillsmith/**`
- `.codex/skills/multi-agent-orchestration/**`
- `.codex/skills/intake-and-routing/**`
- `.codex/skills/failure-memory/**`

### Primary Goals

- remove stale catalog-cap wording
- align lagging skills with explicit choose/output structure
- keep dispatch and actual-usage traceability durable

## Lane B: Execution And Review

### Files

- `.codex/skills/architecture-and-design/**`
- `.codex/skills/implementation-backend/**`
- `.codex/skills/implementation-frontend/**`
- `.codex/skills/quality-and-review/**`
- `.codex/skills/release-and-operations/**`

### Primary Goals

- review asset and reference freshness
- tighten stale wording or implicit selection rules
- preserve explicit support-path selection

## Lane C: Product And Security

### Files

- `.codex/skills/planning-and-scoping/**`
- `.codex/skills/product-and-ux/**`
- `.codex/skills/security-review/**`
- `.codex/skills/security-lab/**`

### Primary Goals

- review asset and reference freshness
- tighten stale wording or implicit selection rules
- keep local-lab and review rules explicit and current

## Verification

- `python3` inventory checks for missing package structure and stale local paths
- `rg -n "ten or fewer|ten top-level|top-level catalog to ten" .codex`
- `git diff --check`
- `pytest`

## Stop Condition

Stop after the three lanes converge into the main tree, shared docs match the live catalog, and verification gates pass.
