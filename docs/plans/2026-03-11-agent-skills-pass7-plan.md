# Agent-Skills Pass 7 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Strengthen the repo-local skill system in parallel by tightening multi-agent orchestration contracts and deepening Refactoring UI absorption in `product-and-ux` and `implementation-frontend`.

**Architecture:** Use three disjoint skill-package slices so each worker owns one package with no shared writes. Converge on the controller by reviewing the returned package diffs, then extend regression tests so the new contracts are enforced by pytest instead of narration.

**Tech Stack:** Markdown skill packages, repo-local assets and references, pytest contract tests, parallel subagents

---

### Task 1: Tighten `multi-agent-orchestration`

**Files:**
- Modify: `.codex/skills/multi-agent-orchestration/SKILL.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/dispatch-handoff.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/slice-record.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/convergence-record.md`
- Modify: `.codex/skills/multi-agent-orchestration/references/parallel-governance.md`
- Test: `tests/test_agent_skills_absorption_lane1.py`

**Step 1: Write the failing test**

Add assertions that the orchestration package requires:
- receiver identity before work starts
- declared identity plus actual support paths in every return
- convergence owner and shutdown condition in convergence tracking
- explicit stop conditions when worker authority drifts

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_agent_skills_absorption_lane1.py`
Expected: FAIL before the new orchestration wording lands

**Step 3: Write minimal implementation**

Update the skill, asset, and reference wording so the dispatch and convergence contract are explicit and pseudocode-styled.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_agent_skills_absorption_lane1.py`
Expected: PASS

### Task 2: Deepen `product-and-ux` Refactoring UI absorption

**Files:**
- Modify: `.codex/skills/product-and-ux/SKILL.md`
- Modify: `.codex/skills/product-and-ux/assets/product-brief.md`
- Modify: `.codex/skills/product-and-ux/references/design-system-methodology.md`
- Modify: `.codex/skills/product-and-ux/references/ui-ideation-prompt-patterns.md`
- Modify: `.codex/skills/product-and-ux/references/wireframe-discipline.md`
- Modify: `.codex/skills/product-and-ux/references/design-system-extraction.md`
- Test: `tests/test_refactoring_ui_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that direction-facing guidance now requires:
- hierarchy before decoration
- explicit empty and missing-state shaping
- feature-first visual exploration and mobile-first typography/spacing rules
- extracted image and visual personality rules that remain reusable

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_refactoring_ui_absorption_contract.py`
Expected: FAIL before the product-and-ux wording is tightened

**Step 3: Write minimal implementation**

Strengthen only direction-layer guidance. Keep implementation-specific token and component details out of this package.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_refactoring_ui_absorption_contract.py`
Expected: PASS

### Task 3: Deepen `implementation-frontend` Refactoring UI absorption

**Files:**
- Modify: `.codex/skills/implementation-frontend/SKILL.md`
- Modify: `.codex/skills/implementation-frontend/assets/frontend-implementation-brief.md`
- Modify: `.codex/skills/implementation-frontend/references/design-system-foundations.md`
- Modify: `.codex/skills/implementation-frontend/references/component-implementation-playbook.md`
- Modify: `.codex/skills/implementation-frontend/references/responsive-layout-patterns.md`
- Test: `tests/test_refactoring_ui_book_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that implementation guidance now requires:
- token handoff details for measure, asset sizing, and non-linear scales
- stronger media, overlay, and emphasis rules
- responsive content-width and asset-size discipline
- component-state behavior that avoids dead controls and decorative border crutches

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_refactoring_ui_book_absorption_contract.py`
Expected: FAIL before the implementation wording is tightened

**Step 3: Write minimal implementation**

Strengthen only implementation-layer guidance. Keep high-level product direction and ideation guidance out of this package.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_refactoring_ui_book_absorption_contract.py`
Expected: PASS

### Task 4: Converge and verify

**Files:**
- Modify: `tests/test_agent_identity_contract.py` if shared role-discipline coverage must be widened
- Modify: `tests/test_agent_skills_absorption_lane1.py`
- Modify: `tests/test_refactoring_ui_absorption_contract.py`
- Modify: `tests/test_refactoring_ui_book_absorption_contract.py`

**Step 1: Review returned diffs**

Check that each slice stayed inside its write scope, used repo-local files, and reported deviations if any.

**Step 2: Run targeted verification**

Run:
- `pytest -q tests/test_agent_skills_absorption_lane1.py`
- `pytest -q tests/test_refactoring_ui_absorption_contract.py`
- `pytest -q tests/test_refactoring_ui_book_absorption_contract.py`

Expected: all targeted suites pass

**Step 3: Run full verification**

Run: `pytest -q`
Expected: PASS with no regressions across the skillpack
