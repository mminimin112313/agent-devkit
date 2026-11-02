# Refactoring UI Book Absorption Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb design-domain knowledge from the `Refactoring UI` PDF into existing broad skills, using text extraction first and targeted page-image review only when needed.

**Architecture:** First create repo-local text artifacts for the PDF. Then extend `skillsmith` with long-form source absorption rules. After that, split the book by chapter/topic bands across multiple workers, collect distilled returns, and converge the material into `product-and-ux` and `implementation-frontend`.

**Tech Stack:** PDF text extraction with `pdftotext`, optional page rendering with `pdftoppm`, Markdown skill packages, pytest regression tests, parallel subagents

---

### Task 1: Create source artifacts and plan docs

**Files:**
- Create: `docs/research/refactoring-ui/refactoring-ui.txt`
- Create: `docs/plans/2026-03-11-refactoring-ui-book-absorption-design.md`
- Create: `docs/plans/2026-03-11-refactoring-ui-book-absorption-plan.md`

**Step 1: Extract the PDF**

Run: `pdftotext '<pdf-path>' docs/research/refactoring-ui/refactoring-ui.txt`
Expected: text artifact exists and is readable

**Step 2: Record the design and plan**

- document text-first absorption
- document page-image fallback
- document chapter/topic distribution

### Task 2: Extend `skillsmith` for long-form book absorption

**Files:**
- Modify: `.codex/skills/skillsmith/SKILL.md`
- Modify: `.codex/skills/skillsmith/references/external-material-distillation.md`
- Create: `.codex/skills/skillsmith/references/book-absorption-rules.md`
- Test: `tests/test_skillsmith_pseudocode_contract.py`

**Step 1: Write the failing test**

Assert that `skillsmith` names the book-absorption rulebook and that the new rulebook requires:
- extracted text artifacts
- targeted page-image fallback
- chapter/topic slicing
- anti-verbatim distillation

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_skillsmith_pseudocode_contract.py`
Expected: FAIL before the rulebook lands

### Task 3: Dispatch chapter/topic slices

**Files:**
- Create or modify: `docs/research/refactoring-ui/*` as needed for working artifacts
- Modify later: target skill references only after convergence

**Step 1: Define slices**

- starting from scratch
- hierarchy is everything
- layout and spacing
- designing text
- color and depth
- images and finishing touches

**Step 2: Dispatch with exact return contract**

- changed target areas proposed
- chapter/topic summary
- page-image review used or not used
- ambiguities or collisions

### Task 4: Converge and verify

**Files:**
- Modify: target references in `product-and-ux` and `implementation-frontend`
- Add tests for the absorbed guidance

**Step 1: Verify targeted tests**

Run:
- `pytest -q tests/test_skillsmith_pseudocode_contract.py`
- `pytest -q`

Expected: both commands pass after convergence
