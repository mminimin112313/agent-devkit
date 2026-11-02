# Agent-Skills Pass 2 Design

**Date:** 2026-03-11

**Scope:** Absorb reusable routing, decomposition, and investigation guidance from `sources/agent-skills/nexus/`, `sources/agent-skills/sherpa/`, `sources/agent-skills/scout/`, and `sources/agent-skills/nexus/references/agent-disambiguation.md`.

## Intent

Pass 1 absorbed the common protocol layer. Pass 2 pulls in the next reusable operating tier:

- minimum-viable routing and disambiguation
- atomic-step decomposition and anti-drift planning
- reproduction-first investigation and RCA handoff

The target remains the existing broad SoloPilot skillpack. No imported persona brands, mode markers, journaling files, or autorun semantics are allowed.

## Inputs

- `sources/agent-skills/nexus/SKILL.md`
- `sources/agent-skills/sherpa/SKILL.md`
- `sources/agent-skills/scout/SKILL.md`
- `sources/agent-skills/nexus/references/agent-disambiguation.md`

## What to absorb

- route directly when ownership is clear; avoid unnecessary chains
- ask one focused clarification question when ambiguity remains material
- use disambiguation rules when two skills plausibly fit the same request
- decompose large work into atomic, testable, committable steps
- detect drift, blockers, and replanning thresholds early
- prefer reproduction-first investigation, explicit confidence levels, impact scope, and fix/test handoff artifacts

## What to reject

- `Nexus`, `Sherpa`, `Scout` branding
- mode and marker contracts such as `NEXUS_HANDOFF`, `_STEP_COMPLETE`, `_AGENT_CONTEXT`
- `.agents/*` logging rules
- Japanese output requirements
- fixed multi-engine or autorun behavior

## Target skills

- `intake-and-routing`
- `planning-and-scoping`
- `quality-and-review`

## Delivery shape

- `intake-and-routing` absorbs minimum-skill routing, ambiguity handling, and disambiguation rules
- `planning-and-scoping` absorbs atomic-step decomposition, drift control, and replanning thresholds
- `quality-and-review` absorbs bug-investigation, reproduction, confidence, and RCA-to-fix handoff rules

## Execution model

- Work in isolated git worktrees under `.worktrees/`
- Use one implementer and one reviewer per worktree
- Converge only the approved subset back into the main tree

## Acceptance

- Routing guidance gets sharper without becoming a full orchestration engine
- Planning gains atomic-step and anti-drift discipline without becoming a run log
- Review gains investigation-grade evidence and RCA handoff fields without turning into a debugger-specific narrow skill
- No forbidden imported markers or journaling paths appear in `.codex/skills/**`
