# Agent-Skills Pass 3 Design

**Date:** 2026-03-11

**Scope:** Absorb reusable architecture, operational maintenance, and design-direction guidance from `sources/agent-skills/atlas/`, `sources/agent-skills/gear/`, and `sources/agent-skills/vision/`.

## Intent

Pass 3 targets broad high-value domain knowledge that maps cleanly into the existing SoloPilot skillpack:

- architecture analysis and proposal discipline
- operational maintenance and verification discipline
- strategic product and UX direction discipline

The goal is still broad, reusable repo-local skills. Imported agent brands, autorun markers, and journaling rules remain out of scope.

## Inputs

- `sources/agent-skills/atlas/SKILL.md`
- `sources/agent-skills/gear/SKILL.md`
- `sources/agent-skills/vision/SKILL.md`

## What to absorb

- evidence-backed architecture analysis, current-vs-target state, ADR/RFC style tradeoff framing, migration and rollback planning
- operational change typing, risk levels, verification/rollback expectations, safe incremental maintenance, and reproducible runtime readiness
- design-direction options, rationale, design-system direction, accessibility and mobile-first baselines, measurable UX success criteria

## What to reject

- `Atlas`, `Gear`, `Vision` branding
- `_STEP_COMPLETE`, `NEXUS_HANDOFF`, AUTORUN, or hub-mode contracts
- `.agents/*` logging
- narrow product-specific tool references that do not generalize

## Target skills

- `architecture-and-design`
- `release-and-operations`
- `product-and-ux`

## Delivery shape

- `architecture-and-design` gains stronger current-state evidence, target-state proposal, migration path, risks, and rollback framing
- `release-and-operations` gains safer maintenance/change-type framing, operational verification depth, and rollback readiness
- `product-and-ux` gains strategic direction options, token/component priorities, accessibility baselines, and measurable review criteria

## Execution model

- Work in isolated git worktrees under `.worktrees/`
- Use one implementer and one reviewer per worktree
- Converge only the approved subset in the main working tree

## Acceptance

- Architecture stays proposal- and contract-focused, not a narrow enterprise-architecture persona
- Release/ops stays about readiness, rollback, and safe maintenance rather than CI-tool-specific procedure
- Product/UX stays strategic and execution-guiding without collapsing into implementation detail
- No imported agent markers or journaling paths appear in `.codex/skills/**`
