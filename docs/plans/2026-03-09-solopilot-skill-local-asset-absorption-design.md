# SoloPilot Skill-Local Asset Absorption Design

**Date:** 2026-03-09

## Goal

Restructure SoloPilot so each top-level skill is a standalone package that owns its local role prompts, assets, and supporting references without depending on root-level `.codex/prompts/**` or `.codex/templates/**`.

## Approved Constraints

- keep the current ten top-level skills
- fully absorb prompts and assets into skill-local directories
- remove root `.codex/prompts/` and `.codex/templates/` as operating dependencies
- keep discovery and entry routing centered on the existing skill catalog
- strengthen role boundaries without exploding the public skill count

## Chosen Structure

Each skill becomes the canonical owner of its execution assets:

```text
.codex/skills/<skill-name>/
├─ SKILL.md
├─ agents/
│  ├─ openai.yaml
│  ├─ <role-a>.md
│  └─ <role-b>.md
├─ assets/
│  ├─ <asset-a>.md
│  └─ <asset-b>.md
├─ references/
│  └─ <reference>.md
└─ scripts/
   └─ optional-helper
```

## Design Principles

### 1. Skill-Local Canonical Ownership

If a role prompt or coordination asset is required to use a skill correctly, that asset must live under the same skill directory. A skill should be understandable after opening one directory, not after chasing root-level siblings.

### 2. Small Catalog, Rich Packages

The top-level catalog stays at ten skills. Richness moves downward into local `agents/`, `assets/`, and `references/` instead of sideways into more top-level directories.

### 3. No Hidden Global Dependencies

The redesign forbids routine references to root `.codex/prompts/**` and `.codex/templates/**`. Shared global storage previously made skill behavior harder to audit, copy, and evolve.

### 4. Local Duplication Is Better Than Global Ambiguity

If two skills need a similarly named checklist, each skill should own its local version unless they are truly the same operating artifact. Cross-skill hidden reuse is more expensive than controlled duplication because it weakens standalone packaging.

### 5. Role Meaning Is Scoped By Skill

Role names may repeat across skills, but the prompt content must be narrowed to the skill context. For example, `qa` inside frontend implementation is not the same canonical prompt as `qa` inside release readiness.

## Role Model

Each skill should declare and package three role layers:

- `core roles`: roles that normally execute or decide inside the skill
- `adjacent roles`: roles that join only in bounded cases
- `disallowed substitutions`: roles or shortcuts that should not replace the canonical path

This keeps the role surface sharp without increasing the number of top-level skills.

## Skill-Level Role Shape

### `intake-and-routing`

- core roles: `cto`, `po-pm`
- required additions: `assets/intake-record.md`, `assets/routing-decision.md`
- role emphasis: `cto` owns next-skill routing and escalation thresholds

### `planning-and-scoping`

- core roles: `cto`, `tech-lead`, `worker`
- required additions: `assets/plan-record.md`, `assets/owned-slice.md`
- role emphasis: `worker` validates execution readiness rather than implementation taste

### `architecture-and-design`

- core roles: `cto`, `tech-lead`, `ui-ux-designer`
- required additions: `assets/design-note.md`, localized ownership asset
- role emphasis: `cto` owns structural choice; `tech-lead` owns execution-ready decomposition

### `implementation-frontend`

- core roles: `software-engineer-frontend`, `ui-ux-designer`, `qa`
- required additions: `assets/frontend-handoff.md`, `assets/ui-review-checklist.md`
- role emphasis: local `qa` focuses on interaction and presentation verification

### `implementation-backend`

- core roles: `software-engineer-backend`, `platform`, `qa`
- required additions: `assets/backend-handoff.md`, `assets/contract-checklist.md`
- role emphasis: local `platform` owns shared seam and contract judgment

### `product-and-ux`

- core roles: `po-pm`, `ui-ux-designer`
- adjacent roles: `software-engineer-frontend`
- required additions: `assets/product-brief.md`, `assets/ux-review.md`
- role emphasis: frontend presence here is feasibility review, not implementation ownership

### `quality-and-review`

- core roles: `spec-reviewer`, `reviewer`, `qa`
- required additions: `assets/spec-review.md`, `assets/code-review.md`, `assets/qa-verdict.md`
- role emphasis: review remains split into requirement fit, then code quality, then QA evidence

### `release-and-operations`

- core roles: `release-manager`, `devops`, `security-privacy`, `qa`
- required additions: `assets/release-gate.md`, `assets/rollback-record.md`, `assets/operational-readiness.md`
- role emphasis: `release-manager` owns final ship/no-ship authority

### `multi-agent-orchestration`

- core roles: `orchestrator`, `tech-lead`, `worker`
- required additions: `assets/slice-record.md`, `assets/convergence-record.md`, `assets/dispatch-handoff.md`
- role emphasis: `orchestrator` owns fan-out justification and convergence sequencing

### `skillsmith`

- core roles: `skill-author`, `skill-reviewer`
- required additions: `agents/skill-author.md`, `agents/skill-reviewer.md`
- required assets: `assets/skill-authoring-record.md`, `assets/skill-audit.md`, `assets/asset-promotion-record.md`
- role emphasis: authoring and review should no longer collapse into one prompt

## Asset Migration Rules

### Prompt Absorption Rule

Move a root prompt into the skill whose operating concern makes it canonical. If a role appears in multiple skills, create skill-local variants instead of retaining a shared global file.

### Asset Absorption Rule

Move a root asset into the skill that directly owns the decision, handoff, or gate. If multiple skills need a similar structure, keep local copies with skill-scoped wording.

### Reference Rule

If a skill needs more than a short checklist or a short role prompt, store the longer guidance under `references/` and keep `SKILL.md` procedural.

## Canonical Prompt Migration Map

- `intake-and-routing/agents/cto.md`
- `intake-and-routing/agents/po-pm.md`
- `planning-and-scoping/agents/cto.md`
- `planning-and-scoping/agents/tech-lead.md`
- `planning-and-scoping/agents/worker.md`
- `architecture-and-design/agents/cto.md`
- `architecture-and-design/agents/tech-lead.md`
- `architecture-and-design/agents/ui-ux-designer.md`
- `implementation-frontend/agents/software-engineer-frontend.md`
- `implementation-frontend/agents/ui-ux-designer.md`
- `implementation-frontend/agents/qa.md`
- `implementation-backend/agents/software-engineer-backend.md`
- `implementation-backend/agents/platform.md`
- `implementation-backend/agents/qa.md`
- `product-and-ux/agents/po-pm.md`
- `product-and-ux/agents/ui-ux-designer.md`
- `product-and-ux/agents/software-engineer-frontend.md`
- `quality-and-review/agents/spec-reviewer.md`
- `quality-and-review/agents/reviewer.md`
- `quality-and-review/agents/qa.md`
- `release-and-operations/agents/release-manager.md`
- `release-and-operations/agents/devops.md`
- `release-and-operations/agents/security-privacy.md`
- `release-and-operations/agents/qa.md`
- `multi-agent-orchestration/agents/orchestrator.md`
- `multi-agent-orchestration/agents/tech-lead.md`
- `multi-agent-orchestration/agents/worker.md`
- `skillsmith/agents/skill-author.md`
- `skillsmith/agents/skill-reviewer.md`

## Canonical Asset Migration Map

- `intake-and-routing/assets/intake-record.md`
- `intake-and-routing/assets/routing-decision.md`
- `planning-and-scoping/assets/plan-record.md`
- `planning-and-scoping/assets/owned-slice.md`
- `architecture-and-design/assets/design-note.md`
- `architecture-and-design/assets/module-ownership.md`
- `architecture-and-design/assets/package-scaffold.md`
- `implementation-frontend/assets/frontend-handoff.md`
- `implementation-frontend/assets/ui-review-checklist.md`
- `implementation-backend/assets/backend-handoff.md`
- `implementation-backend/assets/contract-checklist.md`
- `product-and-ux/assets/product-brief.md`
- `product-and-ux/assets/ux-review.md`
- `quality-and-review/assets/spec-review.md`
- `quality-and-review/assets/code-review.md`
- `quality-and-review/assets/qa-verdict.md`
- `quality-and-review/assets/review-checklist.md`
- `quality-and-review/assets/integration-checklist.md`
- `quality-and-review/assets/worker-handoff.md`
- `release-and-operations/assets/release-gate.md`
- `release-and-operations/assets/rollback-record.md`
- `release-and-operations/assets/operational-readiness.md`
- `release-and-operations/assets/release-review-checklist.md`
- `multi-agent-orchestration/assets/slice-record.md`
- `multi-agent-orchestration/assets/convergence-record.md`
- `multi-agent-orchestration/assets/dispatch-handoff.md`
- `multi-agent-orchestration/assets/active-slices.md`
- `multi-agent-orchestration/assets/module-ownership.md`
- `multi-agent-orchestration/assets/mail-handoff.md`
- `skillsmith/assets/skill-authoring-record.md`
- `skillsmith/assets/skill-audit.md`
- `skillsmith/assets/asset-promotion-record.md`

## Shared Documentation Changes

The redesign requires shared operating docs to describe skill-local ownership rather than root-level prompt and template catalogs:

- `.codex/README.md`
- `.codex/skills/README.md`
- `.codex/skills/*/SKILL.md`
- `.codex/skills/*/agents/openai.yaml`

The root `.codex/prompts/` and `.codex/templates/` directories should be deleted after every active reference is removed.

## Trade-Offs

### Benefits

- skills become truly copyable and standalone
- local ownership makes audits and revisions easier
- role meaning is clearer inside each operating concern
- the user sees one coherent package instead of one skill plus hidden siblings

### Costs

- some prompt and asset duplication will increase
- migration touches many files at once
- search paths change and must be updated carefully

## Acceptance Conditions

The redesign is complete when:

- no active `SKILL.md` references `.codex/prompts/**` or `.codex/templates/**`
- every top-level skill owns its required role prompts and assets locally
- the root prompt and template directories are removable without breaking skill use
- the ten-skill catalog remains intact
- `skillsmith` gains explicit author/reviewer separation

## Recommended Next Step

Write and execute a repository-wide implementation plan that moves assets skill-by-skill, updates all references, and then removes the root prompt and template directories.
