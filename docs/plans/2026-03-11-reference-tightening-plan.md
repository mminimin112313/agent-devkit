# Reference Tightening Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Tighten prose-heavy `.codex` reference files while preserving asset forms and avoiding information loss from over-compression.

**Architecture:** First encode the asset-vs-reference rule and symbol-discipline rule in `skillsmith`, then add regression tests for the chosen reference set, then rewrite the target references into clearer logic-shaped forms without flattening enumerations that carry meaning.

**Tech Stack:** Markdown skill packages, pytest regression tests, repo-local planning docs

---

### Task 1: Encode the reference-tightening rule in `skillsmith`

**Files:**
- Modify: `.codex/skills/skillsmith/references/pseudocode-style-rules.md`
- Test: `tests/test_skillsmith_pseudocode_contract.py`

**Step 1: Write the failing test**

Add assertions that the pseudocode style rulebook preserves asset form docs and requires symbol usage to justify itself by clarity.

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_skillsmith_pseudocode_contract.py`
Expected: FAIL before the wording is added

**Step 3: Write minimal implementation**

- add asset-form preservation guidance
- add reference-focused compression guidance
- add symbol-discipline wording that prioritizes structure and information retention over visual terseness

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_skillsmith_pseudocode_contract.py`
Expected: PASS

### Task 2: Add regression coverage for the selected reference set

**Files:**
- Create: `tests/test_reference_tightening_contract.py`

**Step 1: Write the failing test**

Add assertions for the selected reference files so the pass requires explicit logic blocks, preserved evidence requirements, and compact structure.

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_reference_tightening_contract.py`
Expected: FAIL before reference rewrites land

**Step 3: Write minimal implementation**

- assert the `product-and-ux`, `security-lab`, `security-review`, and `quality-and-review` targets contain the intended logic-shaped markers

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_reference_tightening_contract.py`
Expected: PASS after rewrites

### Task 3: Rewrite the selected reference files

**Files:**
- Modify: `.codex/skills/product-and-ux/references/design-system-methodology.md`
- Modify: `.codex/skills/product-and-ux/references/mobile-first-experience-principles.md`
- Modify: `.codex/skills/product-and-ux/references/ux-research-methods.md`
- Modify: `.codex/skills/product-and-ux/references/interaction-accessibility-principles.md`
- Modify: `.codex/skills/security-lab/references/web-check-playbooks.md`
- Modify: `.codex/skills/security-review/references/web-app-review-playbook.md`
- Modify: `.codex/skills/quality-and-review/references/root-cause-and-prevention.md`

**Step 1: Write the failing test**

Covered by `tests/test_reference_tightening_contract.py`

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_reference_tightening_contract.py`
Expected: FAIL before edits

**Step 3: Write minimal implementation**

- preserve all substantive guidance
- convert narrative sections into bounded pseudocode, named inputs, or explicit pass/fail checks
- keep list-shaped evidence and method menus as lists when flattening would lose meaning

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_reference_tightening_contract.py`
Expected: PASS

### Task 4: Verify the full pass

**Files:**
- Verify: `.codex/skills/skillsmith/references/pseudocode-style-rules.md`
- Verify: `.codex/skills/**/references/*.md`
- Verify: `tests/test_skillsmith_pseudocode_contract.py`
- Verify: `tests/test_reference_tightening_contract.py`

**Step 1: Run targeted verification**

Run:
- `pytest -q tests/test_skillsmith_pseudocode_contract.py tests/test_reference_tightening_contract.py`
- `pytest -q`

Expected: both commands pass
