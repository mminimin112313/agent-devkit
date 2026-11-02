# Agent-Skills Pass 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb the reusable common protocol layer from `sources/agent-skills/_common/` into the broad SoloPilot skillpack without importing vendor-specific markers or persona branding.

**Architecture:** Limit this pass to three broad skills that already own planning, orchestration, and review. Execute each slice in an isolated worktree, then converge the changes in the main working tree through central review and verification.

**Tech Stack:** Markdown skill packages, git worktrees, repository docs, pytest verification

---

### Task 1: Record the approved pass-1 scope in repo docs

**Files:**
- Create: `docs/plans/2026-03-11-agent-skills-pass1-design.md`
- Create: `docs/plans/2026-03-11-agent-skills-pass1-plan.md`

**Step 1: Verify planning docs do not already exist**

Run: `test -f docs/plans/2026-03-11-agent-skills-pass1-design.md || test -f docs/plans/2026-03-11-agent-skills-pass1-plan.md`
Expected: non-zero exit status before creation

**Step 2: Write minimal implementation**

- add the approved design summary
- add this implementation plan with slice ownership and verification

**Step 3: Run test to verify it passes**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-agent-skills-pass1-*.md' | sort`
Expected: both new files are listed

### Task 2: Prepare the repository for isolated worktrees

**Files:**
- Modify: `.gitignore`

**Step 1: Write the failing test**

Check that `.worktrees/` is not yet ignored.

**Step 2: Run test to verify it fails**

Run: `git check-ignore -q .worktrees`
Expected: non-zero exit status

**Step 3: Write minimal implementation**

- add `.worktrees/` to `.gitignore`

**Step 4: Run test to verify it passes**

Run: `git check-ignore -v .worktrees`
Expected: `.gitignore` reports the `.worktrees/` rule

### Task 3: Update `planning-and-scoping` with pass-1 boundary discipline

**Files:**
- Modify: `.codex/skills/planning-and-scoping/SKILL.md`
- Modify: `.codex/skills/planning-and-scoping/assets/owned-slice.md`
- Modify: `.codex/skills/planning-and-scoping/assets/plan-record.md`
- Modify: `.codex/skills/planning-and-scoping/assets/scope-boundary-checklist.md`
- Modify: `.codex/skills/planning-and-scoping/references/dependency-risk-review.md`

**Step 1: Write the failing test**

Check that these files do not yet mention pass-1 concepts such as boundary proof, handoff proof, or explicit stop conditions.

**Step 2: Run test to verify it fails**

Run: `rg -n "boundary proof|stop condition|handoff proof" .codex/skills/planning-and-scoping`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add boundary-first planning rules
- require owned slices to state assumptions, dependencies, stop conditions, and proof
- keep the guidance generic and repo-local

**Step 4: Run test to verify it passes**

Run: `rg -n "boundary proof|stop condition|handoff proof|independent slice" .codex/skills/planning-and-scoping`
Expected: the planning package now carries the new protocol language

### Task 4: Update `multi-agent-orchestration` with pass-1 dispatch and convergence rules

**Files:**
- Modify: `.codex/skills/multi-agent-orchestration/SKILL.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/slice-record.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/dispatch-handoff.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/convergence-record.md`
- Modify: `.codex/skills/multi-agent-orchestration/references/convergence-rules.md`

**Step 1: Write the failing test**

Check that the orchestration package does not yet fully separate dispatch readiness, independent execution, and convergence evidence.

**Step 2: Run test to verify it fails**

Run: `rg -n "dispatch readiness|convergence evidence|independent execution|shared state" .codex/skills/multi-agent-orchestration`
Expected: missing or partial coverage before edits

**Step 3: Write minimal implementation**

- add readiness checks before dispatch
- require explicit shared-state detection before parallelism
- strengthen convergence records with proof and unresolved risk fields

**Step 4: Run test to verify it passes**

Run: `rg -n "dispatch readiness|convergence evidence|independent execution|shared state" .codex/skills/multi-agent-orchestration`
Expected: the orchestration package now documents the pass-1 protocol

### Task 5: Update `quality-and-review` with pass-1 handoff and proof rules

**Files:**
- Modify: `.codex/skills/quality-and-review/SKILL.md`
- Modify: `.codex/skills/quality-and-review/assets/spec-review.md`
- Modify: `.codex/skills/quality-and-review/assets/review-handoff.md`
- Modify: `.codex/skills/quality-and-review/assets/qa-verdict.md`
- Modify: `.codex/skills/quality-and-review/references/review-sequencing.md`

**Step 1: Write the failing test**

Check that the review package does not yet require proof-bearing handoffs and explicit unresolved risk tracking.

**Step 2: Run test to verify it fails**

Run: `rg -n "proof|unresolved risk|handoff|acceptance evidence" .codex/skills/quality-and-review`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- require handoffs to carry scope, evidence, risks, and recommended next action
- keep spec-first then quality review sequencing
- make QA verdicts reject unsupported completion claims

**Step 4: Run test to verify it passes**

Run: `rg -n "acceptance evidence|unresolved risk|proof|next action" .codex/skills/quality-and-review`
Expected: the review package now carries the stronger protocol

### Task 6: Integrate and verify the combined pass

**Files:**
- Verify: `.codex/skills/planning-and-scoping/**`
- Verify: `.codex/skills/multi-agent-orchestration/**`
- Verify: `.codex/skills/quality-and-review/**`
- Verify: `.gitignore`

**Step 1: Run syntax and drift checks**

Run:
- `git diff --check`
- `pytest`

Expected: no whitespace errors and repository tests pass

**Step 2: Review for forbidden imports**

Run: `rg -n "NEXUS_|_STEP_COMPLETE|AUTORUN|\\.agents/" .codex/skills`
Expected: no matches introduced by this pass
