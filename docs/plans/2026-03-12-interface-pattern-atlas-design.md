# Interface Pattern Atlas Design

**Date:** 2026-03-12

**Scope:** Absorb reusable interface-design knowledge into the existing `product-and-ux` and `implementation-frontend` skills inside `sources/codex-orchestrator-fresh`.

## Intent

Strengthen the existing broad skills without adding a duplicate top-level interface-design skill.

The incoming pattern language should land as:

- reusable pattern language and decision rules inside `product-and-ux`
- implementation translation rules and review checks inside `implementation-frontend`
- an explicit coverage map showing where each pattern domain landed

## Constraints

- keep the top-level skill catalog unchanged
- prefer a few broad reference files over many tiny chapter mirrors
- absorb knowledge as procedure, patterns, and decision rules rather than source-summary prose
- preserve the current separation between product direction and frontend implementation

## Absorption Model

Repackage the source into five reference groups plus one trace artifact:

1. `human-centered-interface-patterns`
   - user goals, research grounding, cognition, memory, interruptions, repetition, collaboration, keyboard-only use
2. `structure-navigation-and-wayfinding-patterns`
   - information architecture, screen families, navigation models, signposts, list/detail structures, collection browsing
3. `screen-layout-visual-and-mobile-patterns`
   - hierarchy, gestalt, responsive layout, progressive disclosure, visual style, typography, color, mobile adaptation
4. `action-data-and-input-patterns`
   - action surfaces, command design, reversible work, collections, data exploration, forms, controls, validation
5. `interface-systems-and-smart-surfaces`
   - design systems, atomic design, framework boundaries, connected or anticipatory interfaces
6. `interface-pattern-coverage-map`
   - domain-to-file traceability record

## Target Files

### Product and UX

- modify `.codex/skills/product-and-ux/SKILL.md`
- modify `.codex/skills/product-and-ux/assets/product-brief.md`
- modify `.codex/skills/product-and-ux/assets/ux-review.md`
- add the five new pattern references
- add the coverage-map reference

### Implementation Frontend

- modify `.codex/skills/implementation-frontend/SKILL.md`
- modify `.codex/skills/implementation-frontend/assets/frontend-implementation-brief.md`
- modify `.codex/skills/implementation-frontend/assets/component-state-checklist.md`
- modify `.codex/skills/implementation-frontend/assets/ui-review-checklist.md`
- add `.codex/skills/implementation-frontend/references/interface-pattern-translation.md`

## Delivery Rules

- `product-and-ux` owns the pattern language, selection logic, and experience-direction framing
- `implementation-frontend` owns seam translation, execution prompts, and proof expectations
- new references must read as durable operating material, not source notes
- traceability must show every pattern domain landing in at least one live skill file

## Non-Goals

- no new top-level skill
- no vendor- or framework-specific UI doctrine
- no long verbatim excerpts from the source material
- no chapter-by-chapter mirror directories

## Acceptance

- both skills can call the new pattern language by path
- existing assets ask for pattern-family choices, not just generic UX notes
- frontend checklists explicitly test orientation, reversibility, hierarchy, and interruption handling where relevant
- the coverage map covers all intended pattern domains and points only at live repo files
