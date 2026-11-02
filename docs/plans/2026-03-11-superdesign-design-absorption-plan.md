# Superdesign Design Absorption Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb reusable design-domain knowledge from `sources/superdesign` into `product-and-ux` and `implementation-frontend` without importing extension-specific runtime behavior.

**Architecture:** Extend existing references instead of creating a parallel “design agent” skill. Put direction-shaping rules in `product-and-ux` and implementation-facing presentation rules in `implementation-frontend`. Add regression tests that check for design-domain coverage without pinning extension details.

**Tech Stack:** Markdown skill packages, pytest regression tests, repo-local design docs

---

### Task 1: Record the mapping and non-goals

**Files:**
- Create: `docs/plans/2026-03-11-superdesign-design-absorption-design.md`
- Create: `docs/plans/2026-03-11-superdesign-design-absorption-plan.md`

**Step 1: Write the absorption design**

- record which design rules map to `product-and-ux`
- record which implementation-facing rules map to `implementation-frontend`
- record the extension-specific items that stay out

**Step 2: Verify both planning docs exist**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-superdesign-design-absorption-*.md' | sort`
Expected: both files are listed

### Task 2: Add failing regression tests for the design-domain absorption

**Files:**
- Create: `tests/test_superdesign_design_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that:
- `product-and-ux` carries variation-first ideation, wireframe discipline, and design-system extraction rules
- `implementation-frontend` carries theme token handoff, component-only presentation, and preview-safe responsive proof rules

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_superdesign_design_absorption_contract.py`
Expected: FAIL before the references are updated

### Task 3: Absorb the design-domain knowledge into the two skills

**Files:**
- Modify: `.codex/skills/product-and-ux/SKILL.md`
- Modify: `.codex/skills/product-and-ux/references/ui-ideation-prompt-patterns.md`
- Modify: `.codex/skills/product-and-ux/references/design-system-methodology.md`
- Modify: `.codex/skills/product-and-ux/references/ux-research-methods.md`
- Create: `.codex/skills/product-and-ux/references/wireframe-discipline.md`
- Create: `.codex/skills/product-and-ux/references/design-system-extraction.md`
- Modify: `.codex/skills/implementation-frontend/SKILL.md`
- Modify: `.codex/skills/implementation-frontend/references/design-system-foundations.md`
- Modify: `.codex/skills/implementation-frontend/references/component-implementation-playbook.md`
- Modify: `.codex/skills/implementation-frontend/references/responsive-layout-patterns.md`

**Step 1: Apply the minimal knowledge transfer**

- absorb design-domain rules only
- keep extension-specific workflow mechanics out
- preserve current pseudocode style

**Step 2: Run test to verify it passes**

Run: `pytest -q tests/test_superdesign_design_absorption_contract.py`
Expected: PASS

### Task 4: Verify the full pass

**Files:**
- Verify: `.codex/skills/product-and-ux/**`
- Verify: `.codex/skills/implementation-frontend/**`
- Verify: `tests/test_superdesign_design_absorption_contract.py`

**Step 1: Run targeted and full verification**

Run:
- `pytest -q tests/test_superdesign_design_absorption_contract.py`
- `pytest -q`

Expected: both commands pass
