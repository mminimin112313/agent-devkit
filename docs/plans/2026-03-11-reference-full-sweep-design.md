# Reference Full Sweep Design

**Date:** 2026-03-11

**Scope:** Tighten every repo-local `.codex/skills/**/references/*.md` file so references read as compact decision logic without flattening asset forms or dropping substantive guidance.

## Approved Requirement

- tighten references only
- do it without omissions
- run six parallel workers
- keep central review and convergence with the orchestrator

## Intent

The previous pass proved the style direction on a representative subset. This pass finishes the remaining reference surface and closes the gap between rulebook and repository reality.

## Non-Goals

- do not flatten `assets/` into reference-style pseudocode
- do not widen skill boundaries or move content across packages unless a file is clearly misplaced
- do not change role prompts, scripts, or runtime behavior

## Slice Model

- slice 1: `architecture-and-design`, `failure-memory`
- slice 2: `implementation-backend`, `intake-and-routing`
- slice 3: `implementation-frontend`
- slice 4: `planning-and-scoping`, `multi-agent-orchestration`, `release-and-operations`
- slice 5: `product-and-ux`
- slice 6: `quality-and-review`, `security-lab`, `security-review`, `skillsmith`

## Merge Strategy

- workers edit only their owned `references/*.md`
- orchestrator reviews every return, checks for missing files, then adds repo-wide regression coverage
- convergence happens in the main worktree only after all six slices return or a blocked slice is collapsed back to the orchestrator

## Acceptance

- every `references/*.md` file is either tightened or explicitly confirmed already compliant in its slice return
- no `assets/*.md` file is rewritten as part of the sweep
- repository tests pass after convergence
- drift checks cover the full reference surface, not only a sampled subset
