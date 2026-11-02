# Agent-Skills Pass 2 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb reusable routing, decomposition, and investigation guidance from `agent-skills` into the broad SoloPilot skillpack without importing persona branding or execution markers.

**Architecture:** Limit this pass to `intake-and-routing`, `planning-and-scoping`, and `quality-and-review`. Execute each slice in a separate git worktree with paired implementation and review, then converge the approved subset in the main working tree.

**Tech Stack:** Markdown skill packages, git worktrees, repository docs, pytest verification

---

### Task 1: Record the approved pass-2 scope in repo docs

**Files:**
- Create: `docs/plans/2026-03-11-agent-skills-pass2-design.md`
- Create: `docs/plans/2026-03-11-agent-skills-pass2-plan.md`

**Step 1: Verify planning docs do not already exist**

Run: `test -f docs/plans/2026-03-11-agent-skills-pass2-design.md || test -f docs/plans/2026-03-11-agent-skills-pass2-plan.md`
Expected: non-zero exit status before creation

**Step 2: Write minimal implementation**

- add the approved design summary
- add this implementation plan with slice ownership and verification

**Step 3: Run test to verify it passes**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-agent-skills-pass2-*.md' | sort`
Expected: both new files are listed

### Task 2: Update `intake-and-routing` with minimum-skill routing and disambiguation rules

**Files:**
- Modify: `.codex/skills/intake-and-routing/SKILL.md`
- Modify: `.codex/skills/intake-and-routing/assets/intake-record.md`
- Modify: `.codex/skills/intake-and-routing/assets/routing-decision.md`
- Modify: `.codex/skills/intake-and-routing/references/intake-clarification-patterns.md`
- Modify: `.codex/skills/intake-and-routing/references/severity-and-escalation.md`

**Step 1: Write the failing test**

Check that the intake package does not yet require minimum-skill routing, one-question ambiguity handling, or direct-vs-orchestrated route rules.

**Step 2: Run test to verify it fails**

Run: `rg -n "minimum viable route|one focused question|direct route|disambiguation|defer" .codex/skills/intake-and-routing`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add direct-route-first rules
- add one-question ambiguity handling and deferred-route reasoning
- add simple disambiguation guidance for overlapping broad skills

**Step 4: Run test to verify it passes**

Run: `rg -n "minimum viable route|one focused question|direct route|disambiguation|defer" .codex/skills/intake-and-routing`
Expected: the intake package now carries the pass-2 routing protocol

### Task 3: Update `planning-and-scoping` with atomic-step and anti-drift rules

**Files:**
- Modify: `.codex/skills/planning-and-scoping/SKILL.md`
- Modify: `.codex/skills/planning-and-scoping/assets/plan-record.md`
- Modify: `.codex/skills/planning-and-scoping/assets/task-breakdown-stub.md`
- Modify: `.codex/skills/planning-and-scoping/assets/active-slices.md`
- Modify: `.codex/skills/planning-and-scoping/references/scope-control-rules.md`

**Step 1: Write the failing test**

Check that the planning package does not yet require atomic-step sizing, drift control, or replanning thresholds.

**Step 2: Run test to verify it fails**

Run: `rg -n "atomic step|parking lot|drift|re-plan|commit point|5-15 min" .codex/skills/planning-and-scoping`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add atomic-step guidance and handoff-ready current-step framing
- add anti-drift and parking-lot rules
- add replan thresholds and commit-point expectations

**Step 4: Run test to verify it passes**

Run: `rg -n "atomic step|parking lot|drift|re-plan|commit point|5-15 min" .codex/skills/planning-and-scoping`
Expected: the planning package now carries the pass-2 decomposition protocol

### Task 4: Update `quality-and-review` with repro-first investigation and RCA handoff rules

**Files:**
- Modify: `.codex/skills/quality-and-review/SKILL.md`
- Modify: `.codex/skills/quality-and-review/assets/repro-intake.md`
- Modify: `.codex/skills/quality-and-review/assets/review-handoff.md`
- Modify: `.codex/skills/quality-and-review/assets/qa-verdict.md`
- Modify: `.codex/skills/quality-and-review/references/root-cause-and-prevention.md`
- Modify: `.codex/skills/quality-and-review/references/support-triage-and-evidence.md`

**Step 1: Write the failing test**

Check that the review package does not yet require exactly bounded investigation hypotheses, reproduction conditions, confidence labeling, or fix/test handoff outputs.

**Step 2: Run test to verify it fails**

Run: `rg -n "reproduction conditions|confidence|hypothesis|fix brief|regression brief|workaround" .codex/skills/quality-and-review`
Expected: missing or incomplete coverage before edits

**Step 3: Write minimal implementation**

- add repro-first investigation rules and confidence labels
- add impact, workaround, and handoff-to-fix/test fields
- keep the result generic and review-owned rather than debugger-branded

**Step 4: Run test to verify it passes**

Run: `rg -n "reproduction conditions|confidence|hypothesis|fix brief|regression brief|workaround" .codex/skills/quality-and-review`
Expected: the review package now carries the pass-2 investigation protocol

### Task 5: Integrate and verify the combined pass

**Files:**
- Verify: `.codex/skills/intake-and-routing/**`
- Verify: `.codex/skills/planning-and-scoping/**`
- Verify: `.codex/skills/quality-and-review/**`

**Step 1: Run syntax and drift checks**

Run:
- `git diff --check`
- `pytest`

Expected: no whitespace errors and repository tests pass

**Step 2: Review for forbidden imports**

Run: `rg -n "NEXUS_|SHERPA_|SCOUT|AUTORUN|\\.agents/" .codex/skills`
Expected: no matches introduced by this pass
