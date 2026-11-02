# Agent-Skills Pass 1 Design

**Date:** 2026-03-11

**Scope:** Absorb only the reusable common protocol guidance from `sources/agent-skills/_common/` into the broad SoloPilot skills under `.codex/skills/`.

## Intent

`simota/agent-skills` is too large to absorb as a flat prompt import. Pass 1 isolates the operating layer that can improve the existing broad skillpack without importing product-specific markers, persona names, or auto-run behavior.

## Inputs

- `sources/agent-skills/_common/BOUNDARIES.md`
- `sources/agent-skills/_common/HANDOFF.md`
- `sources/agent-skills/_common/PARALLEL.md`
- `sources/agent-skills/_common/SUBAGENT.md`

## What to absorb

- Explicit boundary checks before dispatching or editing
- Handoff records that carry assumptions, stop conditions, proof, and open risks
- Parallel-work rules that separate independent slices from converged review
- Subagent selection guidance that distinguishes reconnaissance, implementation, and review ownership

## What to reject

- Named agent brands such as `Nexus`
- Marker protocols such as `NEXUS_HANDOFF` or `_STEP_COMPLETE`
- Auto-run defaults and loop contracts
- Repo-specific journaling conventions under `.agents/`
- Language constraints that do not belong in this repository

## Target skills

- `planning-and-scoping`
- `multi-agent-orchestration`
- `quality-and-review`

## Delivery shape

- `planning-and-scoping` absorbs sharper boundary, dependency, and owned-slice rules
- `multi-agent-orchestration` absorbs dispatch, split, and convergence protocol guidance
- `quality-and-review` absorbs stronger handoff, review sequencing, and proof expectations

## Execution model

- Work in isolated git worktrees under `.worktrees/`
- Keep each slice on a dedicated branch with disjoint file ownership as much as possible
- Central orchestrator reviews and merges slice outputs back into the main working tree

## Acceptance

- New guidance is procedural and local to the affected broad skills
- No imported protocol names or persona names remain
- Existing uncommitted work outside the owned files is preserved
- `pytest` baseline remains green after integration
