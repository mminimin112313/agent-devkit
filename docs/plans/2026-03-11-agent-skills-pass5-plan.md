# Agent-Skills Pass 5 Plan

## Scope

- source: `sources/agent-skills`
- target repo: `sources/codex-orchestrator-fresh`
- slices:
  - `product-and-ux`
  - `planning-and-scoping`
  - `quality-and-review`

## Slice 1

- owner: product lane
- target files:
  - `.codex/skills/product-and-ux/SKILL.md`
  - `.codex/skills/product-and-ux/assets/*`
  - `.codex/skills/product-and-ux/references/*`
- source concepts:
  - research questions first
  - study method and limitation visibility
  - feedback synthesis by segment and impact
  - voice/tone and accessibility-text implications

## Slice 2

- owner: planning lane
- target files:
  - `.codex/skills/planning-and-scoping/SKILL.md`
  - `.codex/skills/planning-and-scoping/assets/*`
  - `.codex/skills/planning-and-scoping/references/*`
- source concepts:
  - document audience and decision target
  - requirement IDs and testable acceptance wording
  - handoff-ready plan packaging
  - research and spec inputs turned into executable scope

## Slice 3

- owner: review lane
- target files:
  - `.codex/skills/quality-and-review/SKILL.md`
  - `.codex/skills/quality-and-review/assets/*`
  - `.codex/skills/quality-and-review/references/*`
- source concepts:
  - standards-based review with citations
  - docs-as-code review triggers
  - stale example and broken-reference checks
  - evidence-backed compliance and documentation gaps

## Verification

- `git diff --check`
- `rg -n "SCRIBE_TO_|RESEARCHER_TO_|VOICE_TO_|AUTORUN|_STEP_COMPLETE|\\.agents/" .codex/skills`
- `pytest`

## Stop Condition

Stop after pass-5 convergence, verification, and a concise status handoff. Do not start the next `agent-skills` pass until pass 5 is stable in the main tree.
