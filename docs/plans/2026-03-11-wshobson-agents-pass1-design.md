# Wshobson Agents Pass 1 Design

**Date:** 2026-03-11

**Scope:** Absorb only the reusable operating guidance from selected `sources/wshobson-agents` skills into broad SoloPilot skills under `.codex/skills/` without importing marketplace, plugin, or runtime-specific product surface.

## Intent

`wshobson/agents` is structurally rich, but most of its value is packaged as pluginized workflow product surface. Pass 1 stays narrow:

- keep `conductor` as a source of context-first planning and work-unit discipline
- keep `agent-teams` as a source of decomposition and handoff hygiene
- keep `llm-application-dev` only as a source of abstract prompt and guardrail heuristics
- reject marketplace, install, and Claude-runtime specifics

## Inputs

- `sources/wshobson-agents/plugins/conductor/README.md`
- `sources/wshobson-agents/plugins/conductor/skills/context-driven-development/SKILL.md`
- `sources/wshobson-agents/plugins/conductor/skills/track-management/SKILL.md`
- `sources/wshobson-agents/plugins/agent-teams/skills/task-coordination-strategies/SKILL.md`
- `sources/wshobson-agents/plugins/agent-teams/skills/team-communication-protocols/SKILL.md`
- `sources/wshobson-agents/plugins/llm-application-dev/skills/prompt-engineering-patterns/SKILL.md`
- `sources/wshobson-agents/docs/architecture.md`
- `sources/wshobson-agents/docs/agent-skills.md`
- `sources/wshobson-agents/docs/plugins.md`

## What To Absorb

- Context-before-implementation as an operating rule:
  - verify current product, workflow, and technical context before planning or editing
  - route missing context into explicit planning instead of silent assumptions
- Work-unit discipline:
  - every slice names scope, non-goals, dependencies, acceptance, and proof
  - plans stay attached to an owned seam rather than loose prose
- Parallel-work contract hygiene:
  - decompose by ownership or interface seam
  - keep dependency graphs shallow
  - require interface contracts and acceptance wording at dispatch time
  - message only at real integration points instead of routine chatter
- Prompt and AI guardrail heuristics at the abstract level only:
  - progressive disclosure
  - structured outputs where they reduce ambiguity
  - iterative refinement and failure-mode thinking

## What To Reject

- Marketplace or plugin product surface:
  - install commands
  - plugin counts and category catalogs
  - model-tier policy
  - marketplace metadata
- Conductor-specific operating shell:
  - fixed `conductor/` directory layout
  - `product.md`, `tracks.md`, `spec.md`, `plan.md` filenames as required repo contracts
  - slash-command workflows
  - git-notes and revert-by-track features
- Agent-team runtime specifics:
  - teammate config paths under `~/.claude`
  - JSON message protocol types as hard rules
  - shutdown handshake mechanics
- Vendor and stack examples:
  - LangChain, Pydantic, Anthropic SDK, or similar implementation snippets
  - dynamic example-selection stacks as required runtime architecture

## Target Skills

- `planning-and-scoping`
- `multi-agent-orchestration`
- `architecture-and-design`
- `intake-and-routing`

## Delivery Shape

- `planning-and-scoping` absorbs context freshness checks, work-unit discipline, and tighter requirement-to-proof packaging
- `multi-agent-orchestration` absorbs ownership-first decomposition, interface-contract dispatch, shallow dependency expectations, and low-noise integration signaling
- `architecture-and-design` absorbs only repo-neutral AI guardrails such as progressive disclosure, structured output selection, and failure-mode review
- `intake-and-routing` absorbs the rule that missing context or artifact freshness should route work back to planning instead of pretending implementation is ready

## Explicit Exclusions

- no new top-level skills
- no import of plugin brands, slash commands, or runtime configuration paths
- no marketplace catalog or installer behavior inside `.codex`
- no framework-specific prompt-engineering examples copied into the broad skillpack

## Acceptance

- imported guidance reads as repo-local operating rules rather than plugin documentation
- no copied marketplace, install, or runtime path assumptions remain
- changed skills stay broad and reusable
- pass-1 edits remain limited to the named target skills and supporting assets or references
- `git diff --check` passes
- `pytest -q` passes
