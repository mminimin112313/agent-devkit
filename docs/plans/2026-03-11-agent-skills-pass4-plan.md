# Agent-Skills Pass 4 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb reusable implementation, testing, and performance guidance from `agent-skills` into the broad SoloPilot skillpack without importing persona branding or execution markers.

**Architecture:** Limit this pass to `implementation-backend`, `implementation-frontend`, and `quality-and-review`. Execute each slice in a separate git worktree with paired implementation and review, then converge the approved subset in the main working tree.

**Tech Stack:** Markdown skill packages, git worktrees, repository docs, pytest verification

---

### Task 1: Record the approved pass-4 scope in repo docs

**Files:**
- Create: `docs/plans/2026-03-11-agent-skills-pass4-design.md`
- Create: `docs/plans/2026-03-11-agent-skills-pass4-plan.md`

**Step 1: Verify planning docs do not already exist**

Run: `test -f docs/plans/2026-03-11-agent-skills-pass4-design.md || test -f docs/plans/2026-03-11-agent-skills-pass4-plan.md`
Expected: non-zero exit status before creation

**Step 2: Write minimal implementation**

- add the approved design summary
- add this implementation plan with slice ownership and verification

**Step 3: Run test to verify it passes**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-agent-skills-pass4-*.md' | sort`
Expected: both new files are listed

### Task 2: Update `implementation-backend` with type-first boundary and edge-case discipline

**Files:**
- Modify: `.codex/skills/implementation-backend/SKILL.md`
- Modify: `.codex/skills/implementation-backend/assets/backend-handoff.md`
- Modify: `.codex/skills/implementation-backend/assets/contract-checklist.md`
- Modify: `.codex/skills/implementation-backend/assets/pipeline-review-checklist.md`
- Modify: `.codex/skills/implementation-backend/references/data-pipeline-reliability.md`
- Modify: `.codex/skills/implementation-backend/references/schema-and-lineage-rules.md`

**Step 1: Write the failing test**

Check that the backend package does not yet require type-first public contracts, boundary validation, edge-case handling, actionable error messages, or backend performance notes.

**Step 2: Run test to verify it fails**

Run: `rg -n "type-first|boundary validation|edge case|actionable error|side effect|performance note|public contract" .codex/skills/implementation-backend`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add public-contract and validation-first rules
- require edge-case and error-message handling
- add performance notes for data-heavy or latency-sensitive seams

**Step 4: Run test to verify it passes**

Run: `rg -n "type-first|boundary validation|edge case|actionable error|side effect|performance note|public contract" .codex/skills/implementation-backend`
Expected: the backend package now carries the pass-4 protocol

### Task 3: Update `implementation-frontend` with production UI state and accessibility discipline

**Files:**
- Modify: `.codex/skills/implementation-frontend/SKILL.md`
- Modify: `.codex/skills/implementation-frontend/assets/component-state-checklist.md`
- Modify: `.codex/skills/implementation-frontend/assets/frontend-implementation-brief.md`
- Modify: `.codex/skills/implementation-frontend/references/design-system-foundations.md`
- Modify: `.codex/skills/implementation-frontend/references/ui-state-coverage.md`

**Step 1: Write the failing test**

Check that the frontend package does not yet require error/loading/empty states, accessibility and keyboard handling, component isolation, or bounded performance checks.

**Step 2: Run test to verify it fails**

Run: `rg -n "loading state|error state|empty state|keyboard|focus|accessible|component isolation|performance budget|re-render" .codex/skills/implementation-frontend`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add production UI state coverage rules
- add accessibility and keyboard/focus expectations
- add bounded frontend performance checks without over-specializing frameworks

**Step 4: Run test to verify it passes**

Run: `rg -n "loading state|error state|empty state|keyboard|focus|accessible|component isolation|performance budget|re-render" .codex/skills/implementation-frontend`
Expected: the frontend package now carries the pass-4 protocol

### Task 4: Update `quality-and-review` with testing and performance-regression review rules

**Files:**
- Modify: `.codex/skills/quality-and-review/SKILL.md`
- Modify: `.codex/skills/quality-and-review/assets/code-review.md`
- Modify: `.codex/skills/quality-and-review/assets/integration-checklist.md`
- Modify: `.codex/skills/quality-and-review/assets/qa-verdict.md`
- Modify: `.codex/skills/quality-and-review/references/review-sequencing.md`
- Modify: `.codex/skills/quality-and-review/references/root-cause-and-prevention.md`

**Step 1: Write the failing test**

Check that the review package does not yet require smallest-high-value test selection, behavior-over-implementation testing, flaky-test handling, coverage blind-spot notes, or performance regression evidence.

**Step 2: Run test to verify it fails**

Run: `rg -n "smallest high-value|behavior not implementation|flaky|coverage blind|performance regression|regression safety net" .codex/skills/quality-and-review`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add testing selection and regression-safety-net rules
- add flaky-test and coverage blind-spot review rules
- require performance regression evidence when optimization work is part of acceptance

**Step 4: Run test to verify it passes**

Run: `rg -n "smallest high-value|behavior not implementation|flaky|coverage blind|performance regression|regression safety net" .codex/skills/quality-and-review`
Expected: the review package now carries the pass-4 protocol

### Task 5: Integrate and verify the combined pass

**Files:**
- Verify: `.codex/skills/implementation-backend/**`
- Verify: `.codex/skills/implementation-frontend/**`
- Verify: `.codex/skills/quality-and-review/**`

**Step 1: Run syntax and drift checks**

Run:
- `git diff --check`
- `pytest`

Expected: no whitespace errors and repository tests pass

**Step 2: Review for forbidden imports**

Run: `rg -n "BUILDER|ARTISAN|RADAR|BOLT|AUTORUN|NEXUS_|\\.agents/" .codex/skills`
Expected: no matches introduced by this pass
