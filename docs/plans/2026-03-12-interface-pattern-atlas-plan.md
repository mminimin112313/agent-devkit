# Interface Pattern Atlas Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb a broad interface-pattern atlas into the existing `product-and-ux` and `implementation-frontend` skills as durable pattern language, implementation guidance, and traceable coverage.

**Architecture:** Keep the top-level skill catalog unchanged. Expand `product-and-ux` with broad pattern-atlas references, then wire `implementation-frontend` to translate those patterns into seam-level build and review behavior. Add a domain-to-file coverage map so traceability stays auditable.

**Tech Stack:** Markdown skill packages under `.codex/skills/**`, repo-local planning docs under `docs/plans/**`, shell verification with `rg`, `git diff --check`, and `pytest`.

---

### Task 1: Add the approved design record

**Files:**
- Create: `docs/plans/2026-03-12-interface-pattern-atlas-design.md`
- Create: `docs/plans/2026-03-12-interface-pattern-atlas-plan.md`

**Step 1: Confirm the design files do not already exist**

Run: `rg -n "Interface Pattern Atlas" docs/plans`
Expected: no existing 2026-03-12 atlas design or plan pair

**Step 2: Write the design and plan docs**

Record:

- scope and non-goals
- five broad pattern groups
- exact target files
- acceptance rules

**Step 3: Verify the docs are readable**

Run: `sed -n '1,220p' docs/plans/2026-03-12-interface-pattern-atlas-design.md`
Expected: design intent, scope, pattern groups, and acceptance all appear

### Task 2: Expand product-and-ux with the pattern atlas

**Files:**
- Modify: `.codex/skills/product-and-ux/SKILL.md`
- Modify: `.codex/skills/product-and-ux/assets/product-brief.md`
- Modify: `.codex/skills/product-and-ux/assets/ux-review.md`
- Create: `.codex/skills/product-and-ux/references/human-centered-interface-patterns.md`
- Create: `.codex/skills/product-and-ux/references/structure-navigation-and-wayfinding-patterns.md`
- Create: `.codex/skills/product-and-ux/references/screen-layout-visual-and-mobile-patterns.md`
- Create: `.codex/skills/product-and-ux/references/action-data-and-input-patterns.md`
- Create: `.codex/skills/product-and-ux/references/interface-systems-and-smart-surfaces.md`
- Create: `.codex/skills/product-and-ux/references/interface-pattern-coverage-map.md`

**Step 1: Tighten the skill routing**

Update the skill so product work names:

- human behavior and memory assumptions
- IA and navigation model
- pattern families chosen and rejected
- layout and visual hierarchy implications

**Step 2: Write the broad references**

Create five references that repackage the incoming pattern language into reusable decision rules instead of source summaries.

**Step 3: Update the assets**

Make `product-brief` and `ux-review` ask for:

- pattern families
- wayfinding model
- reversibility and interruption handling
- list/detail, form, or data model where relevant

### Task 3: Translate the atlas into frontend execution

**Files:**
- Modify: `.codex/skills/implementation-frontend/SKILL.md`
- Modify: `.codex/skills/implementation-frontend/assets/frontend-implementation-brief.md`
- Modify: `.codex/skills/implementation-frontend/assets/component-state-checklist.md`
- Modify: `.codex/skills/implementation-frontend/assets/ui-review-checklist.md`
- Create: `.codex/skills/implementation-frontend/references/interface-pattern-translation.md`

**Step 1: Add a frontend translation reference**

Write one broad reference that turns approved pattern language into seam-level implementation prompts:

- orientation and wayfinding
- layout and disclosure
- collections and drilldown
- actions and reversibility
- forms and validation
- data exploration

**Step 2: Update the skill and assets**

Make the frontend skill require pattern-fit checks before implementation and during review.

**Step 3: Re-check cross-skill fit**

Ensure the frontend skill consumes product-direction inputs without duplicating product strategy wording.

### Task 4: Verify coverage and hygiene

**Files:**
- Verify: `.codex/skills/product-and-ux/**`
- Verify: `.codex/skills/implementation-frontend/**`
- Verify: `docs/plans/2026-03-12-interface-pattern-atlas-*.md`

**Step 1: Run formatting and hygiene checks**

Run: `git diff --check`
Expected: no whitespace or merge-marker issues

**Step 2: Check the new references are wired**

Run: `rg -n "human-centered-interface-patterns|structure-navigation-and-wayfinding-patterns|screen-layout-visual-and-mobile-patterns|action-data-and-input-patterns|interface-systems-and-smart-surfaces|interface-pattern-translation|interface-pattern-coverage-map" .codex/skills`
Expected: each new reference is both present and referenced from a live skill or asset

**Step 3: Run repository tests**

Run: `pytest`
Expected: existing tests continue to pass

**Step 4: Stop condition**

Stop after the two skills, their supporting assets and references, and the trace file all land cleanly and verification is recorded.
