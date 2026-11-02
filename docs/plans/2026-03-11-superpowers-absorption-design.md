# Superpowers Absorption Design

## Goal

Absorb the current `superpowers` skill set into the repo-local SoloPilot skillpack without turning the exported catalog into a second, duplicated hierarchy.

The target state is:

- repo-local skills remain the primary operating layer
- superpower principles are compiled into existing repo-local triggers, hard gates, assets, references, and tests
- new top-level skills are added only when compilation would materially weaken trigger clarity or output-contract discipline

## Decision

Compile first, promote rarely.

This program will not copy `superpowers` as a parallel top-level namespace. Instead, each source skill is translated into one of three destinations:

1. existing repo-local skill packages
2. shared repo-local operating docs such as `.codex/README.md`, `.codex/AGENTS.md`, and scoped `AGENTS.md`
3. a new top-level repo-local skill only if the admission gate passes

## Admission Gate For New Top-Level Skills

Create a new top-level repo-local skill only if all of the following are true:

- no current repo-local skill can own the trigger without becoming fuzzy
- merging would hide or weaken the source output contract
- the source needs its own reusable local support files to stay deterministic
- keeping the behavior only in root docs would make routing implicit instead of explicit

Fail the admission gate if the source can be preserved by tightening:

- the trigger wording of an existing skill
- the required reads, choose-assets, or choose-references rules of an existing skill
- the repo-local operating docs or runtime role contracts
- pytest contract coverage

## Compilation Rules

1. Preserve force, not branding.
   - Keep the hard gate, anti-pattern, or review order if it changes behavior.
   - Drop persona-heavy narration that does not add operational force.
2. Prefer the narrowest existing owner.
   - process entry -> `intake-and-routing`, `planning-and-scoping`
   - orchestration and delegated execution -> `multi-agent-orchestration`
   - verification, review, debugging discipline -> `quality-and-review`
   - implementation discipline -> `implementation-backend`, `implementation-frontend`
   - release completion and branch-exit behavior -> `release-and-operations`
   - skill-authoring behavior -> `skillsmith`
   - repeated failure lessons -> `failure-memory`
3. Preserve strong source claims with repo-local tests.
   - if a compiled rule matters, add or widen a pytest contract instead of relying on narration
4. Do not import structure blindly.
   - adapt useful prompt-template shape from `superpowers` when it improves spawn quality
   - do not keep duplicate execution systems in parallel once repo-local wording is stronger

## Initial Source-To-Destination Map

- `intake-and-routing`
  - destination: root `AGENTS.md`, `.codex/README.md`, `intake-and-routing`
- `brainstorming`
  - destination: `intake-and-routing`, `product-and-ux`, `planning-and-scoping`
- `writing-plans`
  - destination: `planning-and-scoping`
- `executing-plans`
  - destination: `planning-and-scoping`, `multi-agent-orchestration`
- `subagent-driven-development`
  - destination: `multi-agent-orchestration`, `quality-and-review`
- `dispatching-parallel-agents`
  - destination: `multi-agent-orchestration`
- `systematic-debugging`
  - destination: `quality-and-review`, `failure-memory`
- `test-driven-development`
  - destination: `implementation-backend`, `implementation-frontend`, `quality-and-review`
- `verification-before-completion`
  - destination: `quality-and-review`, `release-and-operations`, repo-local operating docs
- `requesting-code-review`
  - destination: `quality-and-review`
- `receiving-code-review`
  - destination: `quality-and-review`
- `using-git-worktrees`
  - destination: `release-and-operations`, repo-local operating docs
- `finishing-a-development-branch`
  - destination: `release-and-operations`
- `writing-skills`
  - destination: `skillsmith`

## Program Shape

Use staged passes instead of one sweep.

### Pass 1

Catalog and admission-gate hardening:

- codify compile-first policy
- codify new top-level admission gate
- add tests that fail if the catalog regresses into parallel duplication

### Pass 2

Spawn and delegated-execution absorption:

- improve `.codex/config.toml`
- improve `.codex/agents/*.toml`
- improve `multi-agent-orchestration` dispatch templates and prompt shape
- absorb the useful prompt structure learned from `subagent-driven-development`

### Pass 3

Ideation and planning absorption:

- absorb `brainstorming` into intake, product, and planning seams
- absorb `writing-plans` and selected `executing-plans` rules into planning handoff structure

### Pass 4

Execution and review-loop absorption:

- absorb `dispatching-parallel-agents`
- absorb `subagent-driven-development`
- preserve ordered review gates rather than generic parallel fan-out

### Pass 5

Quality-discipline absorption:

- absorb `systematic-debugging`
- absorb `test-driven-development`
- absorb `verification-before-completion`
- absorb `requesting-code-review`
- absorb `receiving-code-review`

### Pass 6

Release and closure absorption:

- absorb `using-git-worktrees`
- absorb `finishing-a-development-branch`
- ensure release and branch-exit rules stay repo-local

### Pass 7

Skillsmith convergence:

- absorb `writing-skills`
- update catalog docs and support-file rules
- revisit whether any source still needs new top-level promotion

## Non-Goals

- no blind 1:1 import of all `superpowers` into `.codex/skills/`
- no second public catalog that competes with repo-local routing
- no live subagent feel checks as the primary proof mechanism
- no weakening of existing repo-local skill boundaries just to fit source wording quickly

## Acceptance

- every absorbed source skill is mapped to a named repo-local owner
- every behavior-changing source rule is preserved as a repo-local hard gate, asset, reference, runtime prompt, or test
- new top-level skills appear only with explicit admission-gate justification
- `.codex/skills/README.md` and related docs describe the compiled system clearly
- `pytest -q` passes after each pass
