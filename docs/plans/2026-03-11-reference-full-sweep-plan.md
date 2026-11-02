# Reference Full Sweep Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Finish the repo-local reference-style migration across every `.codex/skills/**/references/*.md` file without flattening assets and with explicit parallel convergence.

**Architecture:** Use six disjoint worker slices keyed by owned skill packages. Workers tighten only their owned `references/*.md` files and report exact files touched. The orchestrator then runs a repository-wide reference-style test, verifies no asset drift, reviews returns, and pushes a single converged branch update.

**Tech Stack:** Markdown skill packages, repo-local planning docs, pytest regression tests, parallel subagents

---

### Task 1: Record fan-out and ownership

**Files:**
- Create: `docs/plans/2026-03-11-reference-full-sweep-design.md`
- Create: `docs/plans/2026-03-11-reference-full-sweep-plan.md`

**Step 1: Write the ownership and non-goal record**

- list the six slices
- state merge strategy and shutdown condition
- state that `assets/` are out of scope

**Step 2: Verify the plan record exists**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-reference-full-sweep-*.md' | sort`
Expected: both files are listed

### Task 2: Dispatch six disjoint reference-tightening workers

**Files:**
- Modify: owned `references/*.md` files only within each slice

**Step 1: Dispatch each slice with exact owned paths**

- slice 1: `architecture-and-design`, `failure-memory`
- slice 2: `implementation-backend`, `intake-and-routing`
- slice 3: `implementation-frontend`
- slice 4: `planning-and-scoping`, `multi-agent-orchestration`, `release-and-operations`
- slice 5: `product-and-ux`
- slice 6: `quality-and-review`, `security-lab`, `security-review`, `skillsmith`

**Step 2: Require explicit return contracts**

- list actual files edited
- list support paths actually used
- confirm whether any owned file was left unchanged and why

### Task 3: Add repository-wide reference drift coverage

**Files:**
- Create: `tests/test_all_reference_files_style_contract.py`

**Step 1: Write the failing test**

Add a repository-wide scan that:
- enumerates every `references/*.md` file
- checks each file has logic-shaped markers rather than plain narrative only
- confirms representative assets stay form-shaped

**Step 2: Run test to verify it fails if a straggler remains**

Run: `pytest -q tests/test_all_reference_files_style_contract.py`
Expected: PASS only when the full sweep is complete

### Task 4: Converge, review, and verify

**Files:**
- Verify: `.codex/skills/**/references/*.md`
- Verify: `tests/test_reference_tightening_contract.py`
- Verify: `tests/test_all_reference_files_style_contract.py`

**Step 1: Run verification**

Run:
- `pytest -q tests/test_reference_tightening_contract.py tests/test_all_reference_files_style_contract.py`
- `pytest -q`

Expected: both commands pass

**Step 2: Check omission risk**

Run: `find .codex/skills -path '*/references/*.md' | sort`
Expected: every file is accounted for by a slice return and passes style coverage
