# Chronos Lessons Promotion Design

## Target

- seam: promote recent deployment and security lessons into reusable `.codex` operating assets without adding app-specific rules
- decision owner: CTO
- affected roles: release manager, devops, QA, security reviewer, reviewer
- constraints:
  - keep the skill catalog small and broad
  - prefer updates to existing skills over creating a new niche skill
  - keep product-specific UI decisions out of shared operating authority
  - preserve this repository as a reusable operating system, not a Chronos knowledge base

## Alternatives

- option a: create a new skill just for small-host web app launch baselines
- option b: update existing release and review skills, plus record a repo-local lesson
- option c: capture everything only in `docs/plans/` and leave skills unchanged
- recommended choice: option b

## Trade-Offs

- replaceability:
  - option b keeps the lessons in reusable assets and references without binding future projects to Chronos-specific flows
- hidden coupling risk:
  - a new skill would encode one product's scars as a top-level operating concept
  - docs-only would leave durable behavior changes too easy to miss
- implementation cost:
  - option b is small and surgical
  - it adds one repo-local lesson record, one new release reference, one new security reference, and focused checklist updates
- verification impact:
  - existing tests should keep passing
  - no new runtime or deployment surface should be introduced in this repository

## Acceptance

- chosen structure:
  - record the event under `.codex/lessons/records/`
  - promote low-RAM deployment and verification lessons into `release-and-operations`
  - promote reusable auth and deploy security baselines into `quality-and-review`
  - do not promote the landing/auth/app split into shared rules because it is still product-seam specific
- acceptance conditions:
  - `release-and-operations` explicitly covers tiny-host build strategy, ingress and TLS readiness, method-aware verification evidence, and rollback ownership
  - `quality-and-review` explicitly covers auth abuse throttling, generic auth failures where enumeration matters, production-safe error exposure, required secret handling, and baseline edge headers
  - one repo-local lesson record exists and is marked promoted
  - repository tests still pass
- next skill: implementation-backend
