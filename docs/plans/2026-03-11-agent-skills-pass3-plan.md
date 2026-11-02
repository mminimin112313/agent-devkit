# Agent-Skills Pass 3 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb reusable architecture, operational maintenance, and design-direction guidance from `agent-skills` into the broad SoloPilot skillpack without importing persona branding or execution markers.

**Architecture:** Limit this pass to `architecture-and-design`, `release-and-operations`, and `product-and-ux`. Execute each slice in a separate git worktree with paired implementation and review, then converge the approved subset in the main working tree.

**Tech Stack:** Markdown skill packages, git worktrees, repository docs, pytest verification

---

### Task 1: Record the approved pass-3 scope in repo docs

**Files:**
- Create: `docs/plans/2026-03-11-agent-skills-pass3-design.md`
- Create: `docs/plans/2026-03-11-agent-skills-pass3-plan.md`

**Step 1: Verify planning docs do not already exist**

Run: `test -f docs/plans/2026-03-11-agent-skills-pass3-design.md || test -f docs/plans/2026-03-11-agent-skills-pass3-plan.md`
Expected: non-zero exit status before creation

**Step 2: Write minimal implementation**

- add the approved design summary
- add this implementation plan with slice ownership and verification

**Step 3: Run test to verify it passes**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-agent-skills-pass3-*.md' | sort`
Expected: both new files are listed

### Task 2: Update `architecture-and-design` with evidence-backed analysis and migration framing

**Files:**
- Modify: `.codex/skills/architecture-and-design/SKILL.md`
- Modify: `.codex/skills/architecture-and-design/assets/design-note.md`
- Modify: `.codex/skills/architecture-and-design/assets/service-boundary-record.md`
- Modify: `.codex/skills/architecture-and-design/references/service-decomposition.md`
- Modify: `.codex/skills/architecture-and-design/references/platform-contracts.md`

**Step 1: Write the failing test**

Check that the architecture package does not yet require current-state evidence, target-state framing, migration path, or rollback planning.

**Step 2: Run test to verify it fails**

Run: `rg -n "current state|target state|migration path|rollback|trade-off|architecture evidence" .codex/skills/architecture-and-design`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add architecture-evidence and trade-off framing
- add current-vs-target state, migration path, and rollback expectations
- keep the result broad and repo-local

**Step 4: Run test to verify it passes**

Run: `rg -n "current state|target state|migration path|rollback|trade-off|architecture evidence" .codex/skills/architecture-and-design`
Expected: the architecture package now carries the pass-3 protocol

### Task 3: Update `release-and-operations` with safer maintenance and verification framing

**Files:**
- Modify: `.codex/skills/release-and-operations/SKILL.md`
- Modify: `.codex/skills/release-and-operations/assets/operational-readiness.md`
- Modify: `.codex/skills/release-and-operations/assets/release-gate.md`
- Modify: `.codex/skills/release-and-operations/assets/rollback-record.md`
- Modify: `.codex/skills/release-and-operations/references/release-evidence.md`

**Step 1: Write the failing test**

Check that the release package does not yet require change type, risk level, explicit verification status, or rollback instructions for operational changes.

**Step 2: Run test to verify it fails**

Run: `rg -n "change type|risk level|verification status|rollback instructions|safe maintenance|runtime readiness" .codex/skills/release-and-operations`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add safer maintenance/change-type framing
- add verification and rollback expectations
- keep the result general and not CI-tool-specific

**Step 4: Run test to verify it passes**

Run: `rg -n "change type|risk level|verification status|rollback instructions|safe maintenance|runtime readiness" .codex/skills/release-and-operations`
Expected: the release package now carries the pass-3 protocol

### Task 4: Update `product-and-ux` with strategic design-direction rules

**Files:**
- Modify: `.codex/skills/product-and-ux/SKILL.md`
- Modify: `.codex/skills/product-and-ux/assets/product-brief.md`
- Modify: `.codex/skills/product-and-ux/assets/ux-review.md`
- Modify: `.codex/skills/product-and-ux/references/design-system-methodology.md`
- Modify: `.codex/skills/product-and-ux/references/interaction-accessibility-principles.md`

**Step 1: Write the failing test**

Check that the product/ux package does not yet require multiple direction options, token/component priorities, mobile-first/WCAG baseline, or measurable design success criteria.

**Step 2: Run test to verify it fails**

Run: `rg -n "direction option|token direction|component priority|mobile-first|WCAG|success criteria" .codex/skills/product-and-ux`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add direction-option and rationale rules
- add design-system priorities and accessibility baseline expectations
- add measurable UX review criteria

**Step 4: Run test to verify it passes**

Run: `rg -n "direction option|token direction|component priority|mobile-first|WCAG|success criteria" .codex/skills/product-and-ux`
Expected: the product/ux package now carries the pass-3 protocol

### Task 5: Integrate and verify the combined pass

**Files:**
- Verify: `.codex/skills/architecture-and-design/**`
- Verify: `.codex/skills/release-and-operations/**`
- Verify: `.codex/skills/product-and-ux/**`

**Step 1: Run syntax and drift checks**

Run:
- `git diff --check`
- `pytest`

Expected: no whitespace errors and repository tests pass

**Step 2: Review for forbidden imports**

Run: `rg -n "ATLAS|GEAR|VISION|AUTORUN|NEXUS_|\\.agents/" .codex/skills`
Expected: no matches introduced by this pass
