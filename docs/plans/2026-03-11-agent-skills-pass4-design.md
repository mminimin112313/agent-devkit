# Agent-Skills Pass 4 Design

**Date:** 2026-03-11

**Scope:** Absorb reusable implementation, testing, and performance guidance from `sources/agent-skills/builder/`, `sources/agent-skills/artisan/`, `sources/agent-skills/radar/`, and `sources/agent-skills/bolt/`.

## Intent

Pass 4 targets the execution layer:

- backend implementation discipline
- frontend implementation discipline
- test and performance verification discipline

The target remains the broad SoloPilot skillpack. Implementation-specific source branding, AUTORUN markers, and journaling rules remain excluded.

## Inputs

- `sources/agent-skills/builder/SKILL.md`
- `sources/agent-skills/artisan/SKILL.md`
- `sources/agent-skills/radar/SKILL.md`
- `sources/agent-skills/bolt/SKILL.md`

## What to absorb

- backend: type-first interfaces, boundary validation, edge-case handling, error messages, side-effect isolation, performance considerations
- frontend: production-grade state and error handling, accessibility, loading/error/empty states, component isolation, feasible performance defaults
- review/testing: smallest high-value test first, regression-first thinking, flaky-test handling, coverage blind-spot review, behavior-over-implementation testing, performance regression evidence when optimization work lands

## What to reject

- `Builder`, `Artisan`, `Radar`, `Bolt` branding
- `_STEP_COMPLETE`, `NEXUS_HANDOFF`, AUTORUN, and journaling rules
- narrow framework- or tool-version specifics that do not generalize

## Target skills

- `implementation-backend`
- `implementation-frontend`
- `quality-and-review`

## Delivery shape

- `implementation-backend` gains type-and-contract-first implementation rules, validation at boundaries, edge-case and performance checks
- `implementation-frontend` gains production UI state handling, accessibility, and bounded frontend performance expectations
- `quality-and-review` gains stronger testing selection rules, regression safety-net logic, flaky-test handling, and performance-regression review fields

## Execution model

- Work in isolated git worktrees under `.worktrees/`
- Use one implementer and one reviewer per worktree
- Converge only the approved subset into the main working tree

## Acceptance

- Backend skill stays implementation-oriented rather than becoming a DDD manifesto
- Frontend skill stays framework-agnostic enough for the broad repo-local package
- Review skill stays evidence- and acceptance-focused rather than becoming a full testing framework catalog
- No imported agent markers or journaling paths appear in `.codex/skills/**`
